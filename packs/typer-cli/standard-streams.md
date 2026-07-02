---
title: "Standard streams"
source: https://en.wikipedia.org/wiki/Standard_streams
domain: typer-cli
license: CC-BY-SA-4.0
tags: python typer, typer cli, type hint cli
fetched: 2026-07-02
---

# Standard streams

In computer programming, **standard streams** are preconnected input and output communication channels between a computer program and its environment when it begins execution. The three input/output (I/O) connections are called **standard input** (**stdin**), **standard output** (**stdout**) and **standard error** (**stderr**). Originally I/O happened via a physically connected system console (input via keyboard, output via monitor), but standard streams abstract this. When a command is executed via an interactive shell, the streams are typically connected to the text terminal on which the shell is running, but can be changed with redirection or a pipeline. More generally, a child process inherits the standard streams of its parent process.

## Application

Users generally know standard streams as input and output channels that handle data coming from an input device, or that write data from the application. The data may be text with any encoding, or binary data. When a program is run as a daemon, its standard error stream is redirected into a log file, typically for error analysis purposes.

Streams may be used to chain applications, meaning that the output stream of one program can be redirected to be the input stream to another application. In many operating systems this is expressed by listing the application names, separated by the vertical bar character, for this reason often called the pipeline character. A well-known example is the use of a pagination application, such as more, providing the user control over the display of the output stream on the display.

## Background

In most operating systems predating Unix, programs had to explicitly connect to the appropriate input and output devices. OS-specific intricacies caused this to be a tedious programming task. On many systems it was necessary to obtain control of environment settings, access a local file table, determine the intended data set, and handle hardware correctly in the case of a punch card reader, magnetic tape drive, disk drive, line printer, card punch, or interactive terminal.

One of Unix's several groundbreaking advances was *abstract devices*, which removed the need for a program to know or care what kind of devices it was communicating with. Older operating systems forced upon the programmer a record structure and frequently non-orthogonal data semantics and device control. Unix eliminated this complexity with the concept of a data stream: an ordered sequence of data bytes which can be read until the end of file. A program may also write bytes as desired and need not, and cannot easily declare their count or grouping.

Another Unix breakthrough was to automatically associate input and output to terminal keyboard and terminal display, respectively, by default — the program (and programmer) did absolutely nothing to establish input and output for a typical input-process-output program (unless it chose a different paradigm). In contrast, previous operating systems usually required some—often complex—job control language to establish connections, or the equivalent burden had to be orchestrated by the program.

Since Unix provided standard streams, the Unix C runtime environment was obliged to support it as well. As a result, most C runtime environments (and C's descendants), regardless of the operating system, provide equivalent functionality.

## Standard input (stdin)

Standard input is a stream from which a program reads its input data. The program requests data transfers by use of the *read* operation. Not all programs require stream input. For example, the *dir* and *ls* programs (which display file names contained in a directory) may take command-line arguments, but perform their operations without any stream data input.

Unless redirected, standard input is inherited from the parent process. In the case of an interactive shell, that is usually associated with the input device of a terminal (or pseudo terminal) which is ultimately linked to a user's keyboard.

On POSIX systems, the file descriptor for standard input is 0 (zero); the POSIX `<unistd.h>` definition is `STDIN_FILENO`; the corresponding C `<stdio.h>` abstraction is provided via the `stdin` (of type `FILE*`) global variable. Similarly in C++, the global object `std::cin` (of type `std::istream`). provided in `<iostream>`, provides an abstraction via C++ streams. Similar abstractions exist in the standard I/O libraries of practically every programming language.

## Standard output (stdout)

Standard output is a stream to which a program writes its output data. The program requests data transfer with the *write* operation. Not all programs generate output. For example, the *file rename* command (variously called *mv*, *move*, or *ren*) is silent on success.

Unless redirected, standard output is inherited from the parent process. In the case of an interactive shell, that is usually the text terminal which initiated the program.

The file descriptor for standard output is 1 (one); the POSIX `<unistd.h>` definition is `STDOUT_FILENO`; the corresponding C `<stdio.h>` variable is `stdout` (of type `FILE*`); similarly in C++, the global object `std::cout` (of type `std::ostream`), provided in `<iostream>`, abstracts the output stream.

## Standard error (stderr)

Standard error is another output stream typically used by programs to output error messages or diagnostics. It is a stream independent of standard output and can be redirected separately.

This solves the semi-predicate problem, allowing output and errors to be distinguished, and is analogous to a function returning a pair of values – see Semipredicate problem § Multivalued return. The usual destination is the text terminal which started the program to provide the best chance of being seen even if *standard output* is redirected (so not readily observed). For example, output of a program in a pipeline is redirected to input of the next program or a text file, but user prompts and errors from each program still go directly to the text terminal so they can be reviewed by the user in real time.

It is acceptable and normal to direct *standard output* and *standard error* to the same destination, such as the text terminal. Messages appear in the same order as the program writes them, unless buffering is involved. For example, in common situations the standard error stream is unbuffered but the standard output stream is line-buffered; in this case, text written to standard error later may appear on the terminal earlier, if the standard output stream buffer is not yet full.

The file descriptor for standard error is defined by POSIX as 2 (two); the *<unistd.h>* header file provides the symbol `STDERR_FILENO`; the corresponding C `<stdio.h>` variable is `stderr` (of type `FILE*`). Similarly, C++ provides two global objects associated with this stream: `std::cerr` and `std::clog` (each of type `std::ostream`), in `<iostream>`, with the former being unbuffered and the latter using the same buffering mechanism as all other C++ streams.

Bourne-style shells allow *standard error* to be redirected to the same destination that standard output is directed to using

```
 2>&1
```

csh-style shells allow *standard error* to be redirected to the same destination that standard output is directed to using

```
 >&
```

Standard error was added to Unix in the 1970s after several wasted phototypesetting runs ended with error messages being typeset instead of displayed on the user's terminal.

## Timeline

### 1950s: Fortran

Fortran has the equivalent of Unix file descriptors: By convention, many Fortran implementations use unit numbers `UNIT=5` for stdin, `UNIT=6` for stdout and `UNIT=0` for stderr. In Fortran 2003, the intrinsic `ISO_FORTRAN_ENV` module was standardized to include the named constants `INPUT_UNIT`, `OUTPUT_UNIT`, and `ERROR_UNIT` to portably specify the unit numbers.

```mw
! FORTRAN 77 example
      PROGRAM MAIN
        INTEGER NUMBER
        READ(UNIT=5,*) NUMBER
        WRITE(UNIT=6,'(A,I3)') ' NUMBER IS: ',NUMBER
      END
```

```mw
! Fortran 2003 example
program main
  use iso_fortran_env
  implicit none
  integer :: number
  read (unit=INPUT_UNIT,*) number
  write (unit=OUTPUT_UNIT,'(a,i3)') 'Number is: ', number
end program
```

### 1960: ALGOL 60

ALGOL 60 was criticized for having no standard file access.

### 1968: ALGOL 68

ALGOL 68's input and output facilities were collectively referred to as the transput. Koster coordinated the definition of the *transput* standard. The model included three standard channels: `stand in`, `stand out`, and `stand back`.

| # ALGOL 68 example # main:( REAL number; getf(stand in,($g$,number)); printf(($"Number is: "g(6,4)"OR "$,number)); # OR # putf(stand out,($" Number is: "g(6,4)"!"$,number)); newline(stand out) ) |   |
|---|---|
| Input: | Output: |
| 3.14159 | Number is: +3.142 OR Number is: +3.142! |

### 1968: Simula

An other example is the OOP language.

```mw
class BASICIO (LINELENGTH); integer LINELENGTH;
    begin ref (infile) SYSIN;
        ref (infile) procedure sysin;
            sysin :- SYSIN;
        ref (printfle) SYSOUT;
        ref (printfle) procedure sysout;
            sysout :- SYSOUT;

        class FILE ....................;
        FILE class infile ............;
        FILE class outfile ...........;
        FILE class directfile ........;
        outfile class printfle .......;

        SYSIN :- new infile ("SYSIN");
        SYSOUT :- new printfle ("SYSOUT");
        SYSIN.open (blanks(80));
        SYSOUT.open(blanks(LINELENGTH));
        inner;
        SYSIN.close;
        SYSOUT.close;
    end BASICIO;
```

### 1970s: C and Unix

In the C programming language, the standard input, output, and error streams are attached to the existing Unix file descriptors 0, 1 and 2 respectively. In a POSIX environment the *<unistd.h>* definitions STDIN_FILENO, STDOUT_FILENO or STDERR_FILENO should be used instead rather than magic numbers. File pointers stdin, stdout, and stderr are also provided.

Ken Thompson (designer and implementer of the original Unix operating system) modified sort in Version 5 Unix to accept "-" as representing standard input, which spread to other utilities and became a part of the operating system as a special file in Version 8. Diagnostics were part of standard output through Version 6, after which Dennis M. Ritchie created the concept of standard error.

### 1990s: C++, Java

In C++, writing to standard streams was originally done using the `<iostream>` header and its streams, until the release of `<print>` which simplified input/output using print functions. C++ inherits C I/O facilities, but it is considered more idiomatic to use the newer C++ facilities.

```mw
#include <iostream>
#include <string>

using std::cerr;
using std::cin;
using std::cout;
using std::endl;
using std::string;

int main() {
    string input;
    cout << "Write a sentence: " << endl;
    cin >> input;
    int inputLength = input.length();
    cout << "Sentence: " << input << ", of length " << inputLength << endl;
    cerr << "Sentence written to stderr: " << input << endl;
}
```

In Java, the standard streams are referred to by `System.in` (for stdin), `System.out` (for stdout), and `System.err` (for stderr). It is also possible to read from any input stream using a `Scanner`.

```mw
package org.wikipedia.examples;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example {
    public static void main(String args[]) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String s = br.readLine();
            double number = Double.parseDouble(s);
            System.out.printf("Number is: %d%n", number);

            // Read input for a name and age:
            Scanner input = new Scanner(System.in);
            System.out.printf("%nEnter name: ");
            String name = input.nextLine();
            System.out.printf("%nEnter age: ");
            int age = input.nextInt();
            System.out.printf("Hello, %s! You are %d years old.", name, age);
        } catch (IOException e) {
            System.err.printf("Error in input/output: %s%n", e.getMessage());
        } catch (Exception e) {
            System.err.printf("Error: %s%n", e.getMessage());
        }
    }
}
```

### 2000s: .NET

In C# and other .NET languages, the standard streams are referred to by `System.Console.In` (for stdin), `System.Console.Out` (for stdout) and `System.Console.Error` (for stderr). Basic read and write capabilities for the stdin and stdout streams are also accessible directly through the class `System.Console` (e.g. `System.Console.WriteLine()` can be used instead of `System.Console.Out.WriteLine()`).

`System.Console.In`, `System.Console.Out` and `System.Console.Error` are respectively `System.IO.TextReader` (stdin) and `System.IO.TextWriter` (stdout, stderr) objects, which only allow access to the underlying standard streams on a text basis. Full binary access to the standard streams must be performed through the `System.IO.Stream` objects returned by `System.Console.OpenStandardInput()`, `System.Console.OpenStandardOutput()` and `System.Console.OpenStandardError()` respectively.

```mw
namespace Wikipeda.Examples;

using System;

public class Example {
    static int Main(string[] args)
    {
        try 
        {
            string s = Console.In.ReadLine();
            double number = Double.Parse(s);
            Console.Out.WriteLine("Number is: {0:F3}", number);
        } // If Parse() threw an exception
        catch (ArgumentNullException e)
        { 
            Console.Error.WriteLine($"No number was entered: {e.Message}");
            return 1;
        } 
        catch (FormatException e) 
        {
            Console.Error.WriteLine($"The specified value is not a valid number: {e.Message}");
            return 2;
        } 
        catch (OverflowException e) 
        {
            Console.Error.WriteLine($"The specified number is too big: {e.Message}");
            return 3;
        } 
        catch (Exception ex)
        {
            Console.Error.WriteLine($"An unknown exception occurred: {e.Message}");
            return -1;
        }
        return 0;
}
```

```mw
' Visual Basic .NET example

Public Function Main() As Integer
    Try
        Dim s As String = System.Console.[In].ReadLine()
        Dim number As Double = Double.Parse(s)
        System.Console.Out.WriteLine("Number is: {0:F3}", number)
        Return 0

    ' If Parse() threw an exception
    Catch ex As System.ArgumentNullException
        System.Console.[Error].WriteLine("No number was entered!")
    Catch ex2 As System.FormatException
        System.Console.[Error].WriteLine("The specified value is not a valid number!")
    Catch ex3 As System.OverflowException
        System.Console.[Error].WriteLine("The specified number is too big!")
    End Try

    Return -1
End Function
```

When applying the `System.Diagnostics.Process` class one can use the instance properties `StandardInput`, `StandardOutput`, and `StandardError` of that class to access the standard streams of the process.

### 2000s onward: Python, C++

The following example, written in Python, shows how to redirect the standard input both to the standard output and to a text file.

```mw
#!/usr/bin/env python

import sys
from typing import TextIO

if __name__ == "__main__":
    # Save the current stdout so that we can revert sys.stdout
    # after we complete our redirection
    stdin_fileno: TextIO = sys.stdin
    stdout_fileno: TextIO = sys.stdout

    # Redirect sys.stdout to the file
    sys.stdout: TextIO = open("myfile.txt", "w")

    ctr: int = 0
    for inps in stdin_fileno:
        ctrs: str = str(ctr)
        # Prints to the redirected stdout ()
        sys.stdout.write(f"{ctrs}) this is to the redirected --->{inps}\n")
        # Prints to the actual saved stdout handler
        stdout_fileno.write(f"{ctrs}) this is to the actual  --->{inps}\n")
        ctr = ctr + 1

    # Close the file
    sys.stdout.close()
    # Restore sys.stdout to our old saved file handler
    sys.stdout = stdout_fileno
```

In C++23, an updated printing interface was created for writing to the output stream, using `std::print` functions.

```mw
import std;

using std::string;

int main() {
    string s = "Hello, world!";
    std::println(stdout, "My string: {}", s);
    std::println(stderr, "String to error stream: {}", s);
}
```

### GUIs

Graphical user interfaces (GUIs) do not always make use of the standard streams; they do when GUIs are wrappers of underlying scripts and/or console programs, for instance the Synaptic package manager GUI, which wraps apt commands in Debian and/or Ubuntu. GUIs created with scripting tools like Zenity and KDialog by KDE project make use of stdin, stdout, and stderr, and are based on simple scripts rather than a complete GUI programmed and compiled in C/C++ using Qt, GTK, or other equivalent proprietary widget framework.

The Services menu, as implemented on NeXTSTEP and Mac OS X, is also analogous to standard streams. On these operating systems, graphical applications can provide functionality through a system-wide menu that operates on the current selection in the GUI, no matter in what application.

Some GUI programs, primarily on Unix, still write debug information to standard error. Others (such as many Unix media players) may read files from standard input. Popular Windows programs that open a separate console window in addition to their GUI windows are the emulators pSX and DOSBox.

GTK-server can use stdin as a communication interface with an interpreted program to realize a GUI.

The Common Lisp Interface Manager paradigm "presents" GUI elements sent to an extended output stream.
