---
title: "GNU Debugger"
source: https://en.wikipedia.org/wiki/GNU_Debugger
domain: gdb-debugging
license: CC-BY-SA-4.0
tags: gdb, gdb debugging, gdb debugger, gdb breakpoint, core dump
fetched: 2026-07-02
---

# GNU Debugger

The **GNU Debugger** (**GDB**) is a portable debugger that runs on many Unix-like systems and works for many programming languages, including Ada, Assembly, C, C++, D, Fortran, Haskell, Go, Objective-C, OpenCL C, Modula-2, Pascal, Rust, and partially others. It detects problems in a program while letting it run and allows users to examine program variables and machine registers.

## History

GDB was first written by Richard Stallman in 1986 as part of his GNU system, after his GNU Emacs was "reasonably stable". GDB is free software released under the GNU General Public License (GPL). It was modeled after the DBX debugger, which came with Berkeley Unix distributions.

From 1990 to 1993 it was maintained by John Gilmore. Now it is maintained by the GDB Steering Committee which is appointed by the Free Software Foundation.

## Technical features

GDB offers extensive facilities for tracing, examining and altering the execution of computer programs. The user can monitor and modify the values of programs' internal variables, and even call functions independently of the program's normal behavior.

### Supported platforms

GDB target processors (as of 2003) include: Alpha, ARM, AVR, H8/300, Altera Nios/Nios II, System/370, System/390, x86 (32-bit and 64-bit), IA-64 "Itanium", Motorola 68k, MIPS, PA-RISC, PowerPC, RISC-V, SuperH, SPARC, and VAX. Lesser-known target processors supported in the standard release have included A29K, ARC, ETRAX CRIS, D10V, D30V, FR-30, FR-V, Intel i960, 68HC11, Motorola 88000, MCORE, MN10200, MN10300, NS32k, Stormy16, and Z8000 (newer releases will likely not support some of these).

GDB has compiled-in simulators for most targets.

### Stepping through code

Both the **next *n*** and **step *n*** command can be used to advance execution over the next n statements. If *n* is omitted it defaults to 1. The difference between the commands is that step will follow the flow of execution into the internals of any function call whereas next will execute the whole function and proceed to the next statement within the current routine.

The **jump *location*** command is used either to skip over a section of problematic code or go back to a previous statement in order to review execution again. The specified location may correspond to different parts of the executing program, but unexpected results may occur for those not accustomed to machine code.

### Printing values and expressions

When a program is halted in mid execution the **print** (abbreviated as **p**) command can be used to display the value of a variable or an expression using C or C++ syntax. The **x** command (meaning "examine") is similar but its argument is an address in memory including address expressions. Both commands use flags to indicate presentation format of the output though there are some differences as **x** allows one to specify the number of bytes.

e.g.:

```
print /f myVar  #Prints a double precision floating point number  
x     /8bx &foo #Print 8 bytes in hex format starting at the memory location of foo
```

Additionally the **call** command invokes both library and user written functions and the returned value will be displayed.

Values displayed are automatically assigned to special *value history* variables which begin with a $ sign followed by a sequence number which can then be redisplayed using **print**.

i.e.:

```
call getpid()
$1  = 23995
```

One can also use the **set** command to create *convenience variables* for use during a gdb session.

e.g.:

```
set $foo=i+42
```

If the argument of **print** is an array or struct all elements will be output. The following syntax can be used to show a sub range of the array:

i.e.:

```
print myArray[10]@10  #show 10 elements of the array starting at myArray[4]
```

### Breakpoints and watchpoints

Breakpoints and watchpoints are used when one needs to examine a program prior to a known situation where things are likely to go wrong. Both break and watchpoints issued integer identification numbers, 1, 2, 3... which can be used to enable, disable or delete them. The command **info break**|**watch** displays all breakpoints and their current status.

Breakpoints are set to halt the flow of execution either on specific line numbers in one's code or on entry to a function when run within the debugger i.e.: **break** *sourcefile*:42 will stop on line 42 of the specified file. If the file name is omitted the reference is to the current file.

A conditional breakpoint halts on a specified line when a specified expression is true, i.e.:

```
break sourcefile:275 if productNum=1275
```

The **condition** *breakNum* *expression* command allows one to add conditions to an established breakpoint.

Watchpoints halt the flow of execution when the value of a variable or an expression changes, irrespective of where in the program it occurs. By default, where possible, gdb monitors the memory location where the change takes place, a useful feature given that multiple pointers may refer to the same address. Conversely a software watchpoint, which are slower, track just the variables.

The rwatch and awatch commands will halt the program whenever the memory location or variable is read.

Another conditional feature of both watches and breakpoints is the command **ignore** *breakNum* *count* which disregards the halting criteria until count execution passes.

The display command primes gdb to automatically output the value of an expression each time it stops. Multiple display commands are cumulative and the output can be formatted using the same flags available to the x command.

### Framestacks

When a program is halted it may be several layers deep in function calls.  Each level of function call is called a frame and the collection of frames is called a frame stack.  When execution is halted one can navigate either up or down to a specific frame in order to examine the value of variables or expressions at a particular level which is useful to assist debugging programs. The **backtrace** command will provide a list of all of the frames in the stack. The **info args** command displays all of the arguments passed to the current frame and the **info local** command displays a list of the variables available to it along with their values.

### Scripting support

GDB includes the ability to define command routines that can be used to automate frequently repeated sets of gdb instructions. These consisting of gdb commands placed between define and end statements. Parameters to these routines are not declared by name however they are passed in special variables $arg1, $arg2, $arg3... with special variable $argc representing the number of command line arguments.

Additionally gdb includes if/else and while blocks terminated by end statements as well as loop_break and loop_continue statements to manage flow of control.

e.g.:

```
# Script to set the gdb prompt and set a breakpoint
define cmd
   set prompt "My debugger> "
   set print pretty # display structures on multiple lines
   if $argc==0
      print "There are no arguments to the command"
   else
      break $arg0
   end
end
```

Consider that one is debugging a C program with a generic linked list a leading value and next field pointing to the next element, the following command would use a while loop to display all the elements:

```
define p_generic_list
  set var $n = $arg0
  while $n
    print *($n)
    set var $n = $n->next
  end
end
```

Command definitions placed in the local file **.gdbinit** are automatically loaded at the beginning of the gdb session. Command definitions can also be saved in ordinary files and loaded using the source command.

As of version 7.0 new features include support for Python scripting and as of version 7.8 GNU Guile scripting as well which is based on the Scheme (programming language).

### Reversible debugging

Since version 7.0, support for "reversible debugging" — allowing a debugging session to step backward, much like rewinding a crashed program to see what happened — is available. The feature is highly memory intensive and slows execution with a default limit of 20,000 instructions. The recommended procedure is to set breakpoints before and after the suspected problem, then issue the **record** command when the program stops at first one. Continue execution to the 2nd breakpoint. The **reverse-step**, **reverse-next** and **reverse-continue** commands can then be used to backtrack execution, undoing changes in variables piecemeal, However reverse debugging does not undo actions such as console output nor does it reissue external events such as interrupts or incoming network packets.

### Remote debugging

GDB offers a "remote" mode often used when debugging embedded systems. Remote operation is when GDB runs on one machine and the program being debugged runs on another. GDB can communicate to the remote "stub" that understands GDB protocol through a serial device or TCP/IP. A stub program can be created by linking to the appropriate stub files provided with GDB, which implement the target side of the communication protocol. Alternatively, gdbserver can be used to remotely debug the program without needing to change it in any way.

The same mode is also used by KGDB for debugging a running Linux kernel on the source level with gdb. With KGDB, kernel developers can debug a kernel in much the same way as they debug application programs. It makes it possible to place breakpoints in kernel code, step through the code, and observe variables. On architectures where hardware debugging registers are available, watchpoints can be set which trigger breakpoints when specified memory addresses are executed or accessed. KGDB requires an additional machine which is connected to the machine to be debugged using a serial cable or Ethernet. On FreeBSD, it is also possible to debug using FireWire direct memory access (DMA).

### Graphical user interface

The debugger does not contain its own graphical user interface, and defaults to a command-line interface, although it does contain a text user interface. Several front-ends have been built for it, such as UltraGDB, Xxgdb, Data Display Debugger (DDD), Nemiver, KDbg, the Xcode debugger, GDBtk/Insight, Gede, Seer, and HP Wildebeest Debugger GUI (WDB GUI). IDEs such as Codelite, Code::Blocks, Dev-C++, Geany, GNAT Programming Studio (GPS), KDevelop, Qt Creator, Lazarus, MonoDevelop, Eclipse, NetBeans, and Visual Studio can interface with GDB. GNU Emacs has a "GUD mode" and tools for Vim exist (e.g. clewn). These offer facilities similar to debuggers found in IDEs.

Some other debugging tools have been designed to work with GDB, such as memory leak detectors.

### Internals

GDB uses a system call named ptrace (the name is an abbreviation of "process trace") to observe and control the execution of another process, and examine and change the process's memory and registers.

| Common gdb commands | Corresponding ptrace calls |
|---|---|
| `(gdb) start` | PTRACE_TRACEME – makes parent a tracer (called by a tracee) |
| `(gdb) attach PID` | PTRACE_ATTACH – attach to a running process |
| `(gdb) step` | PTRACE_SINGLESTEP – advance to the next instruction |
| `(gdb) stop` | `kill(child_pid, SIGSTOP)` (or PTRACE_INTERRUPT) |
| `(gdb) continue` | PTRACE_CONT |
| `(gdb) info registers` | PTRACE_GET(FP)REGS(ET) and PTRACE_SET(FP)REGS(ET) |
| `(gdb) x` | PTRACE_PEEKTEXT and PTRACE_POKETEXT |

A breakpoint is implemented by replacing an instruction at a given memory address with another special instruction. Executing breakpoint instruction causes SIGTRAP.
