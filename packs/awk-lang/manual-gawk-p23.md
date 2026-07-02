---
title: "The GNU Awk User’s Guide (part 23/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 23/38
---

## 14 Debugging `awk` Programs

It would be nice if computer programs worked perfectly the first time they were run, but in real life, this rarely happens for programs of any complexity. Thus, most programming languages have facilities available for “debugging” programs, and `awk` is no exception.

The `gawk` debugger is purposely modeled after the GNU Debugger (GDB) command-line debugger. If you are familiar with GDB, learning how to use `gawk` for debugging your programs is easy.

### 14.1 Introduction to the `gawk` Debugger

This section introduces debugging in general and begins the discussion of debugging in `gawk`.

#### 14.1.1 Debugging in General

(If you have used debuggers in other languages, you may want to skip ahead to `awk` Debugging.)

Of course, a debugging program cannot remove bugs for you, because it has no way of knowing what you or your users consider a “bug” versus a “feature.” (Sometimes, we humans have a hard time with this ourselves.) In that case, what can you expect from such a tool? The answer to that depends on the language being debugged, but in general, you can expect at least the following:

- The ability to watch a program execute its instructions one by one, giving you, the programmer, the opportunity to think about what is happening on a time scale of seconds, minutes, or hours, rather than the nanosecond time scale at which the code usually runs.
- The opportunity to not only passively observe the operation of your program, but to control it and try different paths of execution, without having to change your source files.
- The chance to see the values of data in the program at any point in execution, and also to change that data on the fly, to see how that affects what happens afterward. (This often includes the ability to look at internal data structures besides the variables you actually defined in your code.)
- The ability to obtain additional information about your program’s state or even its internal structure.

All of these tools provide a great amount of help in using your own skills and understanding of the goals of your program to find where it is going wrong (or, for that matter, to better comprehend a perfectly functional program that you or someone else wrote).

#### 14.1.2 Debugging Concepts

Before diving in to the details, we need to introduce several important concepts that apply to just about all debuggers. The following list defines terms used throughout the rest of this chapter:

***Stack frame* ¶**

Programs generally call functions during the course of their execution. One function can call another, or a function can call itself (recursion). You can view the chain of called functions (main program calls A, which calls B, which calls C), as a stack of executing functions: the currently running function is the topmost one on the stack, and when it finishes (returns), the next one down then becomes the active function. Such a stack is termed a *call stack*.

For each function on the call stack, the system maintains a data area that contains the function’s parameters, local variables, and return value, as well as any other “bookkeeping” information needed to manage the call stack. This data area is termed a *stack frame*.

`gawk` also follows this model, and gives you access to the call stack and to each stack frame. You can see the call stack, as well as from where each function on the stack was invoked. Commands that print the call stack print information about each stack frame (as detailed later on).

***Breakpoint* ¶**

During debugging, you often wish to let the program run until it reaches a certain point, and then continue execution from there one statement (or instruction) at a time. The way to do this is to set a *breakpoint* within the program. A breakpoint is where the execution of the program should break off (stop), so that you can take over control of the program’s execution. You can add and remove as many breakpoints as you like.

***Watchpoint* ¶**

A watchpoint is similar to a breakpoint. The difference is that breakpoints are oriented around the code: stop when a certain point in the code is reached. A watchpoint, however, specifies that program execution should stop when a *data value* is changed. This is useful, as sometimes it happens that a variable receives an erroneous value, and it’s hard to track down where this happens just by looking at the code. By using a watchpoint, you can stop whenever a variable is assigned to, and usually find the errant code quite quickly.

#### 14.1.3 `awk` Debugging

Debugging an `awk` program has some specific aspects that are not shared with programs written in other languages.

First of all, the fact that `awk` programs usually take input line by line from a file or files and operate on those lines using specific rules makes it especially useful to organize viewing the execution of the program in terms of these rules. As we will see, each `awk` rule is treated almost like a function call, with its own specific block of instructions.

In addition, because `awk` is by design a very concise language, it is easy to lose sight of everything that is going on “inside” each line of `awk` code. The debugger provides the opportunity to look at the individual primitive instructions carried out by the higher-level `awk` commands.99

### 14.2 Sample `gawk` Debugging Session

In order to illustrate the use of `gawk` as a debugger, let’s look at a sample debugging session. We will use the `awk` implementation of the POSIX `uniq` command presented earlier (see Printing Nonduplicated Lines of Text) as our example.

#### 14.2.1 How to Start the Debugger

Starting the debugger is almost exactly like running `gawk` normally, except you have to pass an additional option, --debug, or the corresponding short option, -D. The file(s) containing the program and any supporting code are given on the command line as arguments to one or more -f options. (`gawk` is not designed to debug command-line programs, only programs contained in files.) In our case, we invoke the debugger like this:

```
$ gawk -D -f getopt.awk -f join.awk -f uniq.awk -- -1 inputfile
```

where both getopt.awk and uniq.awk are in `$AWKPATH`. (Experienced users of GDB or similar debuggers should note that this syntax is slightly different from what you are used to. With the `gawk` debugger, you give the arguments for running the program in the command line to the debugger rather than as part of the `run` command at the debugger prompt.) The -- ends `gawk`’s command line options. It’s not strictly necessary here, but it is needed if an option to the `awk` program conflicts with a `gawk` option. The -1 is an option to uniq.awk.

Instead of immediately running the program on inputfile, as `gawk` would ordinarily do, the debugger merely loads all the program source files, compiles them internally, and then gives us a prompt:

```
gawk>
```

from which we can issue commands to the debugger. At this point, no code has been executed.

#### 14.2.2 Finding the Bug

Let’s say that we are having a problem using (a faulty version of) uniq.awk in “field-skipping” mode, and it doesn’t seem to be catching lines which should be identical when skipping the first field, such as:

```
awk is a wonderful program!
gawk is a wonderful program!
```

This could happen if we were thinking (C-like) of the fields in a record as being numbered in a zero-based fashion, so instead of the lines:

```
clast = join(alast, fcount+1, n)
cline = join(aline, fcount+1, m)
```

we wrote:

```
clast = join(alast, fcount, n)
cline = join(aline, fcount, m)
```

The first thing we usually want to do when trying to investigate a problem like this is to put a breakpoint in the program so that we can watch it at work and catch what it is doing wrong. A reasonable spot for a breakpoint in uniq.awk is at the beginning of the function `are_equal()`, which compares the current line with the previous one. To set the breakpoint, use the `b` (breakpoint) command:

```
gawk> b are_equal
-| Breakpoint 1 set at file `awklib/eg/prog/uniq.awk', line 63
```

The debugger tells us the file and line number where the breakpoint is. Now type ‘r’ or ‘run’ and the program runs until it hits the breakpoint for the first time:

```
gawk> r
-| Starting program:
-| Stopping in Rule ...
-| Breakpoint 1, are_equal(n, m, clast, cline, alast, aline)
         at `awklib/eg/prog/uniq.awk':63
-| 63          if (fcount == 0 && charcount == 0)
gawk>
```

Now we can look at what’s going on inside our program. First of all, let’s see how we got to where we are. At the prompt, we type ‘bt’ (short for “backtrace”), and the debugger responds with a listing of the current stack frames:

```
gawk> bt
-| #0  are_equal(n, m, clast, cline, alast, aline)
         at `awklib/eg/prog/uniq.awk':68
-| #1  in main() at `awklib/eg/prog/uniq.awk':88
```

This tells us that `are_equal()` was called by the main program at line 88 of uniq.awk. (This is not a big surprise, because this is the only call to `are_equal()` in the program, but in more complex programs, knowing who called a function and with what parameters can be the key to finding the source of the problem.)

Now that we’re in `are_equal()`, we can start looking at the values of some variables. Let’s say we type ‘p n’ (`p` is short for “print”). We would expect to see the value of `n`, a parameter to `are_equal()`. Actually, the debugger gives us:

```
gawk> p n
-| n = untyped variable
```

In this case, `n` is an uninitialized local variable, because the function was called without arguments (see Function Calls).

A more useful variable to display might be the current record:

```
gawk> p $0
-| $0 = "gawk is a wonderful program!"
```

This might be a bit puzzling at first, as this is the second line of our test input. Let’s look at `NR`:

```
gawk> p NR
-| NR = 2
```

So we can see that `are_equal()` was only called for the second record of the file. Of course, this is because our program contains a rule for ‘NR == 1’:

```
NR == 1 {
    last = $0
    next
}
```

OK, let’s just check that that rule worked correctly:

```
gawk> p last
-| last = "awk is a wonderful program!"
```

Everything we have done so far has verified that the program has worked as planned, up to and including the call to `are_equal()`, so the problem must be inside this function. To investigate further, we must begin “stepping through” the lines of `are_equal()`. We start by typing ‘n’ (for “next”):

```
gawk> n
-| 66          if (fcount > 0) {
```

This tells us that `gawk` is now ready to execute line 66, which decides whether to give the lines the special “field-skipping” treatment indicated by the -1 command-line option. (Notice that we skipped from where we were before, at line 63, to here, because the condition in line 63, ‘if (fcount == 0 && charcount == 0)’, was false.)

Continuing to step, we now get to the splitting of the current and last records:

```
gawk> n
-| 67              n = split(last, alast)
gawk> n
-| 68              m = split($0, aline)
```

At this point, we should be curious to see what our records were split into, so we try to look:

```
gawk> p n m alast aline
-| n = 5
-| m = untyped variable
-| alast = array, 5 elements
-| aline = untyped variable
```

(The `p` command can take more than one argument, similar to `awk`’s `print` statement.)

This is kind of disappointing, though. All we found out is that there are five elements in `alast`; `m` and `aline` don’t have values because we are at line 68 but haven’t executed it yet. This information is useful enough (we now know that none of the words were accidentally left out), but what if we want to see inside the array?

The first choice would be to use subscripts:

```
gawk> p alast[0]
-| "0" not in array `alast'
```

Oops!

```
gawk> p alast[1]
-| alast["1"] = "awk"
```

This would be kind of slow for a 100-member array, though, so `gawk` provides a shortcut (reminiscent of another language not to be mentioned):

```
gawk> p @alast
-| alast["1"] = "awk"
-| alast["2"] = "is"
-| alast["3"] = "a"
-| alast["4"] = "wonderful"
-| alast["5"] = "program!"
```

It looks like we got this far OK. Let’s take another step or two:

```
gawk> n
-| 69              clast = join(alast, fcount, n)
gawk> n
-| 70              cline = join(aline, fcount, m)
```

Well, here we are at our error (sorry to spoil the suspense). What we had in mind was to join the fields starting from the second one to make the virtual record to compare, and if the first field were numbered zero, this would work. Let’s look at what we’ve got:

```
gawk> p cline clast
-| cline = "gawk is a wonderful program!"
-| clast = "awk is a wonderful program!"
```

Hey, those look pretty familiar! They’re just our original, unaltered input records. A little thinking (the human brain is still the best debugging tool), and we realize that we were off by one!

We get out of the debugger:

```
gawk> q
-| The program is running. Exit anyway (y/n)? y
```

Then we get into an editor:

```
clast = join(alast, fcount+1, n)
cline = join(aline, fcount+1, m)
```

and problem solved!

### 14.3 Main Debugger Commands

The `gawk` debugger command set can be divided into the following categories:

- Breakpoint control
- Execution control
- Viewing and changing data
- Working with the stack
- Getting information
- Miscellaneous

Each of these are discussed in the following subsections. In the following descriptions, commands that may be abbreviated show the abbreviation on a second description line. A debugger command name may also be truncated if that partial name is unambiguous. The debugger has the built-in capability to automatically repeat the previous command just by hitting Enter. This works for the commands `list`, `next`, `nexti`, `step`, `stepi`, and `continue` executed without any argument.

#### 14.3.1 Control of Breakpoints

As we saw earlier, the first thing you probably want to do in a debugging session is to get your breakpoints set up, because your program will otherwise just run as if it was not under the debugger. The commands for controlling breakpoints are:

**`break` [[*filename*`:`]*n* | *function*] [`"*expression*"`]**

**`b` [[*filename*`:`]*n* | *function*] [`"*expression*"`]**

Without any argument, set a breakpoint at the next instruction to be executed in the selected stack frame. Arguments can be one of the following:

***n***

Set a breakpoint at line number *n* in the current source file.

***filename*`:`*n***

Set a breakpoint at line number *n* in source file *filename*.

***function***

Set a breakpoint at entry to (the first instruction of) function *function*.

Each breakpoint is assigned a number that can be used to delete it from the breakpoint list using the `delete` command.

With a breakpoint, you may also supply a condition. This is an `awk` expression (enclosed in double quotes) that the debugger evaluates whenever the breakpoint is reached. If the condition is true, then the debugger stops execution and prompts for a command. Otherwise, it continues executing the program.

**`clear` [[*filename*`:`]*n* | *function*]**

Without any argument, delete any breakpoint at the next instruction to be executed in the selected stack frame. If the program stops at a breakpoint, this deletes that breakpoint so that the program does not stop at that location again. Arguments can be one of the following:

***n***

Delete breakpoint(s) set at line number *n* in the current source file.

***filename*`:`*n***

Delete breakpoint(s) set at line number *n* in source file *filename*.

***function***

Delete breakpoint(s) set at entry to function *function*.

**`condition` *n* `"*expression*"`**

Add a condition to existing breakpoint or watchpoint *n*. The condition is an `awk` expression *enclosed in double quotes* that the debugger evaluates whenever the breakpoint or watchpoint is reached. If the condition is true, then the debugger stops execution and prompts for a command. Otherwise, the debugger continues executing the program. If the condition expression is not specified, any existing condition is removed (i.e., the breakpoint or watchpoint is made unconditional).

**`delete` [*n1 n2* …] [*n*–*m*]**

**`d` [*n1 n2* …] [*n*–*m*]**

Delete specified breakpoints or a range of breakpoints. Delete all defined breakpoints if no argument is supplied.

**`disable` [*n1 n2* … | *n*–*m*]**

Disable specified breakpoints or a range of breakpoints. Without any argument, disable all breakpoints.

**`enable` [`del` | `once`] [*n1 n2* …] [*n*–*m*] ¶**

**`e` [`del` | `once`] [*n1 n2* …] [*n*–*m*]**

Enable specified breakpoints or a range of breakpoints. Without any argument, enable all breakpoints. Optionally, you can specify how to enable the breakpoints:

**`del`**

Enable the breakpoints temporarily, then delete each one when the program stops at it.

**`once`**

Enable the breakpoints temporarily, then disable each one when the program stops at it.

**`ignore` *n* *count* ¶**

Ignore breakpoint number *n* the next *count* times it is hit.

**`tbreak` [[*filename*`:`]*n* | *function*] ¶**

**`t` [[*filename*`:`]*n* | *function*]**

Set a temporary breakpoint (enabled for only one stop). The arguments are the same as for `break`.

#### 14.3.2 Control of Execution

Now that your breakpoints are ready, you can start running the program and observing its behavior. There are more commands for controlling execution of the program than we saw in our earlier example:

**`commands` [*n*] ¶**

**`silent`**

**…**

**`end`**

Set a list of commands to be executed upon stopping at a breakpoint or watchpoint. *n* is the breakpoint or watchpoint number. Without a number, the last one set is used. The actual commands follow, starting on the next line, and terminated by the `end` command. If the command `silent` is in the list, the usual messages about stopping at a breakpoint and the source line are not printed. Any command in the list that resumes execution (e.g., `continue`) terminates the list (an implicit `end`), and subsequent commands are ignored. For example:

```
gawk> commands
> silent
> printf "A silent breakpoint; i = %d\n", i
> info locals
> set i = 10
> continue
> end
gawk>
```

**`continue` [*count*] ¶**

**`c` [*count*]**

Resume program execution. If continued from a breakpoint and *count* is specified, ignore the breakpoint at that location the next *count* times before stopping.

**`finish` ¶**

Execute until the selected stack frame returns. Print the returned value.

**`next` [*count*] ¶**

**`n` [*count*]**

Continue execution to the next source line, stepping over function calls. The argument *count* controls how many times to repeat the action, as in `step`.

**`nexti` [*count*] ¶**

**`ni` [*count*]**

Execute one (or *count*) instruction(s), stepping over function calls.

**`return` [*value*] ¶**

Cancel execution of a function call. If *value* (either a string or a number) is specified, it is used as the function’s return value. If used in a frame other than the innermost one (the currently executing function; i.e., frame number 0), discard all inner frames in addition to the selected one, and the caller of that frame becomes the innermost frame.

**`run` ¶**

**`r`**

Start/restart execution of the program. When restarting, the debugger retains the current breakpoints, watchpoints, command history, automatic display variables, and debugger options.

**`step` [*count*] ¶**

**`s` [*count*]**

Continue execution until control reaches a different source line in the current stack frame, stepping inside any function called within the line. If the argument *count* is supplied, steps that many times before stopping, unless it encounters a breakpoint or watchpoint.

**`stepi` [*count*] ¶**

**`si` [*count*]**

Execute one (or *count*) instruction(s), stepping inside function calls. (For illustration of what is meant by an “instruction” in `gawk`, see the output shown under `dump` in Miscellaneous Commands.)

**`until` [[*filename*`:`]*n* | *function*] ¶**

**`u` [[*filename*`:`]*n* | *function*]**

Without any argument, continue execution until a line past the current line in the current stack frame is reached. With an argument, continue execution until the specified location is reached, or the current stack frame returns.

#### 14.3.3 Viewing and Changing Data

The commands for viewing and changing variables inside of `gawk` are:

**`display` [*var* | `$`*n*] ¶**

Add variable *var* (or field `$*n*`) to the display list. The value of the variable or field is displayed each time the program stops. Each variable added to the list is identified by a unique number:

```
gawk> display x
-| 10: x = 1
```

This displays the assigned item number, the variable name, and its current value. If the display variable refers to a function parameter, it is silently deleted from the list as soon as the execution reaches a context where no such variable of the given name exists. Without argument, `display` displays the current values of items on the list.

**`eval "*awk statements*"` ¶**

Evaluate *awk statements* in the context of the running program. You can do anything that an `awk` program would do: assign values to variables, call functions, and so on.

> **NOTE:** You cannot use `eval` to execute a statement containing any of the following: `exit`, `getline`, `next`, `nextfile`, or `return`.

**`eval` *param*, …**

***awk statements***

**`end`**

This form of `eval` is similar, but it allows you to define “local variables” that exist in the context of the *awk statements*, instead of using variables or function parameters defined by the program.

**`print` *var1*[`,` *var2* …] ¶**

**`p` *var1*[`,` *var2* …]**

Print the value of a `gawk` variable or field. Fields must be referenced by constants:

```
gawk> print $3
```

This prints the third field in the input record (if the specified field does not exist, it prints ‘Null field’). A variable can be an array element, with the subscripts being constant string values. To print the contents of an array, prefix the name of the array with the ‘@’ symbol:

```
gawk> print @a
```

This prints the indices and the corresponding values for all elements in the array `a`.

**`printf` *format* [`,` *arg* …] ¶**

Print formatted text. The *format* may include escape sequences, such as ‘\n’ (see Escape Sequences). No newline is printed unless one is specified.

**`set` *var*`=`*value* ¶**

Assign a constant (number or string) value to an `awk` variable or field. String values must be enclosed between double quotes (`"`…`"`).

You can also set special `awk` variables, such as `FS`, `NF`, `NR`, and so on.

**`watch` *var* | `$`*n* [`"*expression*"`] ¶**

**`w` *var* | `$`*n* [`"*expression*"`]**

Add variable *var* (or field `$*n*`) to the watch list. The debugger then stops whenever the value of the variable or field changes. Each watched item is assigned a number that can be used to delete it from the watch list using the `unwatch` command.

With a watchpoint, you may also supply a condition. This is an `awk` expression (enclosed in double quotes) that the debugger evaluates whenever the watchpoint is reached. If the condition is true, then the debugger stops execution and prompts for a command. Otherwise, `gawk` continues executing the program.

**`undisplay` [*n*] ¶**

Remove item number *n* (or all items, if no argument) from the automatic display list.

**`unwatch` [*n*] ¶**

Remove item number *n* (or all items, if no argument) from the watch list.

#### 14.3.4 Working with the Stack

Whenever you run a program that contains any function calls, `gawk` maintains a stack of all of the function calls leading up to where the program is right now. You can see how you got to where you are, and also move around in the stack to see what the state of things was in the functions that called the one you are in. The commands for doing this are:

**`backtrace` [*count*] ¶**

**`bt` [*count*]**

**`where` [*count*]**

Print a backtrace of all function calls (stack frames), or innermost *count* frames if *count* > 0. Print the outermost *count* frames if *count* < 0. The backtrace displays the name and arguments to each function, the source file name, and the line number. The alias `where` for `backtrace` is provided for longtime GDB users who may be used to that command.

**`down` [*count*] ¶**

Move *count* (default 1) frames down the stack toward the innermost frame. Then select and print the frame.

**`frame` [*n*] ¶**

**`f` [*n*]**

Select and print stack frame *n*. Frame 0 is the currently executing, or *innermost*, frame (function call); frame 1 is the frame that called the innermost one. The highest-numbered frame is the one for the main program. The printed information consists of the frame number, function and argument names, source file, and the source line.

**`up` [*count*] ¶**

Move *count* (default 1) frames up the stack toward the outermost frame. Then select and print the frame.

#### 14.3.5 Obtaining Information About the Program and the Debugger State

Besides looking at the values of variables, there is often a need to get other sorts of information about the state of your program and of the debugging environment itself. The `gawk` debugger has one command that provides this information, appropriately called `info`. `info` is used with one of a number of arguments that tell it exactly what you want to know:

**`info` *what* ¶**

**`i` *what***

The value for *what* should be one of the following:

**`args` ¶**

List arguments of the selected frame.

**`break` ¶**

List all currently set breakpoints.

**`display` ¶**

List all items in the automatic display list.

**`frame` ¶**

Give a description of the selected stack frame.

**`functions` ¶**

List all function definitions including source file names and line numbers.

**`locals` ¶**

List local variables of the selected frame.

**`source` ¶**

Print the name of the current source file. Each time the program stops, the current source file is the file containing the current instruction. When the debugger first starts, the current source file is the first file included via the -f option. The ‘list *filename*:*lineno*’ command can be used at any time to change the current source.

**`sources` ¶**

List all program sources.

**`variables` ¶**

List all global variables.

**`watch` ¶**

List all items in the watch list.

Additional commands give you control over the debugger, the ability to save the debugger’s state, and the ability to run debugger commands from a file. The commands are:

**`option` [*name*[`=`*value*]]**

**`o` [*name*[`=`*value*]]**

Without an argument, display the available debugger options and their current values. ‘option *name*’ shows the current value of the named option. ‘option *name*=*value*’ assigns a new value to the named option. The available options are:

**`history_size` ¶**

Set the maximum number of lines to keep in the history file ./.gawk_history. The default is 100.

**`listsize` ¶**

Specify the number of lines that `list` prints. The default is 15.

**`outfile` ¶**

Send `gawk` output to a file; debugger output still goes to standard output. An empty string (`""`) resets output to standard output.

**`prompt` ¶**

Change the debugger prompt. The default is ‘gawk> ’.

**`save_history` [`on` | `off`] ¶**

Save command history to file ./.gawk_history. The default is `on`.

**`save_options` [`on` | `off`] ¶**

Save current options to file ./.gawkrc upon exit. The default is `on`. Options are read back into the next session upon startup.

**`trace` [`on` | `off`] ¶**

Turn instruction tracing on or off. The default is `off`.

**`save` *filename***

Save the commands from the current session to the given file name, so that they can be replayed using the `source` command.

**`source` *filename* ¶**

Run command(s) from a file; an error in any command does not terminate execution of subsequent commands. Comments (lines starting with ‘#’) are allowed in a command file. Empty lines are ignored; they do *not* repeat the last command. You can’t restart the program by having more than one `run` command in the file. Also, the list of commands may include additional `source` commands; however, the `gawk` debugger will not source the same file more than once in order to avoid infinite recursion.

In addition to, or instead of, the `source` command, you can use the -D *file* or --debug=*file* command-line options to execute commands from a file non-interactively (see Command-Line Options).

#### 14.3.6 Miscellaneous Commands

There are a few more commands that do not fit into the previous categories, as follows:

**`dump` [*filename*] ¶**

Dump byte code of the program to standard output or to the file named in *filename*. This prints a representation of the internal instructions that `gawk` executes to implement the `awk` commands in a program. This can be very enlightening, as the following partial dump of Davide Brini’s obfuscated code (see And Now for Something Completely Different) demonstrates:

```
gawk> dump
-|        # BEGIN
-|
-| [  1:0xfcd340] Op_rule           : [in_rule = BEGIN] [source_file = brini.awk]
```

```
-| [  1:0xfcc240] Op_push_i         : "~" [MALLOC|STRING|STRCUR]
-| [  1:0xfcc2a0] Op_push_i         : "~" [MALLOC|STRING|STRCUR]
-| [  1:0xfcc280] Op_match          :
-| [  1:0xfcc1e0] Op_store_var      : O
-| [  1:0xfcc2e0] Op_push_i         : "==" [MALLOC|STRING|STRCUR]
-| [  1:0xfcc340] Op_push_i         : "==" [MALLOC|STRING|STRCUR]
-| [  1:0xfcc320] Op_equal          :
-| [  1:0xfcc200] Op_store_var      : o
-| [  1:0xfcc380] Op_push           : o
-| [  1:0xfcc360] Op_plus_i         : 0 [MALLOC|NUMCUR|NUMBER]
-| [  1:0xfcc220] Op_push_lhs       : o [do_reference = true]
-| [  1:0xfcc300] Op_assign_plus    :
-| [   :0xfcc2c0] Op_pop            :
-| [  1:0xfcc400] Op_push           : O
-| [  1:0xfcc420] Op_push_i         : "" [MALLOC|STRING|STRCUR]
-| [   :0xfcc4a0] Op_no_op          :
-| [  1:0xfcc480] Op_push           : O
-| [   :0xfcc4c0] Op_concat         : [expr_count = 3] [concat_flag = 0]
-| [  1:0xfcc3c0] Op_store_var      : x
-| [  1:0xfcc440] Op_push_lhs       : X [do_reference = true]
-| [  1:0xfcc3a0] Op_postincrement  :
-| [  1:0xfcc4e0] Op_push           : x
-| [  1:0xfcc540] Op_push           : o
-| [  1:0xfcc500] Op_plus           :
-| [  1:0xfcc580] Op_push           : o
-| [  1:0xfcc560] Op_plus           :
-| [  1:0xfcc460] Op_leq            :
-| [   :0xfcc5c0] Op_jmp_false      : [target_jmp = 0xfcc5e0]
-| [  1:0xfcc600] Op_push_i         : "%c" [MALLOC|STRING|STRCUR]
-| [   :0xfcc660] Op_no_op          :
-| [  1:0xfcc520] Op_assign_concat  : c
-| [   :0xfcc620] Op_jmp            : [target_jmp = 0xfcc440]
...
-| [     2:0xfcc5a0] Op_K_printf         : [expr_count = 17] [redir_type = ""]
-| [      :0xfcc140] Op_no_op            :
-| [      :0xfcc1c0] Op_atexit           :
-| [      :0xfcc640] Op_stop             :
-| [      :0xfcc180] Op_no_op            :
-| [      :0xfcd150] Op_after_beginfile  :
```

```
-| [      :0xfcc160] Op_no_op            :
-| [      :0xfcc1a0] Op_after_endfile    :
gawk>
```

**`exit` ¶**

Exit the debugger. See the entry for ‘quit’, later in this list.

**`help` ¶**

**`h`**

Print a list of all of the `gawk` debugger commands with a short summary of their usage. ‘help *command*’ prints the information about the command *command*.

**`list` [`-` | `+` | *n* | *filename*`:`*n* | *n*–*m* | *function*] ¶**

**`l` [`-` | `+` | *n* | *filename*`:`*n* | *n*–*m* | *function*]**

Print the specified lines (default 15) from the current source file or the file named *filename*. The possible arguments to `list` are as follows:

**`-` (Minus)**

Print lines before the lines last printed.

**`+`**

Print lines after the lines last printed. `list` without any argument does the same thing.

***n***

Print lines centered around line number *n*.

***n*–*m***

Print lines from *n* to *m*.

***filename*`:`*n***

Print lines centered around line number *n* in source file *filename*. This command may change the current source file.

***function***

Print lines centered around the beginning of the function *function*. This command may change the current source file.

**`quit` ¶**

**`q`**

Exit the debugger. Debugging is great fun, but sometimes we all have to tend to other obligations in life, and sometimes we find the bug and are free to go on to the next one! As we saw earlier, if you are running a program, the debugger warns you when you type ‘q’ or ‘quit’, to make sure you really want to quit.

**`trace` [`on` | `off`] ¶**

Turn on or off continuous printing of the instructions that are about to be executed, along with the `awk` lines they implement. The default is `off`.

It is to be hoped that most of the “opcodes” in these instructions are fairly self-explanatory, and using `stepi` and `nexti` while `trace` is on will make them into familiar friends.

### 14.4 Readline Support

If `gawk` is compiled with the GNU Readline library, you can take advantage of that library’s command completion and history expansion features. The following types of completion are available:

**Command completion**

Command names.

**Source file name completion**

Source file names. Relevant commands are `break`, `clear`, `list`, `tbreak`, and `until`.

**Argument completion**

Non-numeric arguments to a command. Relevant commands are `enable` and `info`.

**Variable name completion**

Global variable names, and function arguments in the current context if the program is running. Relevant commands are `display`, `print`, `set`, and `watch`.

### 14.5 Limitations

We hope you find the `gawk` debugger useful and enjoyable to work with, but as with any program, especially in its early releases, it still has some limitations. A few that it’s worth being aware of are:

- At this point, the debugger does not give a detailed explanation of what you did wrong when you type in something it doesn’t like. Rather, it just responds ‘syntax error’. When you do figure out what your mistake was, though, you’ll feel like a real guru.
- If you perused the dump of opcodes in Miscellaneous Commands (or if you are already familiar with `gawk` internals), you will realize that much of the internal manipulation of data in `gawk`, as in many interpreters, is done on a stack. `Op_push`, `Op_pop`, and the like are the “bread and butter” of most `gawk` code. Unfortunately, as of now, the `gawk` debugger does not allow you to examine the stack’s contents. That is, the intermediate results of expression evaluation are on the stack, but cannot be printed. Rather, only variables that are defined in the program can be printed. Of course, a workaround for this is to use more explicit variables at the debugging stage and then change back to obscure, perhaps more optimal code later.
- There is no way to look “inside” the process of compiling regular expressions to see if you got it right. As an `awk` programmer, you are expected to know the meaning of `/[^[:alnum:][:blank:]]/`.
- The `gawk` debugger is designed to be used by running a program (with all its parameters) on the command line, as described in How to Start the Debugger. There is no way (as of now) to attach or “break into” a running program. This seems reasonable for a language that is used mainly for quickly executing, short programs.
- The `gawk` debugger only accepts source code supplied with the -f option. If you have a shell script that provides an `awk` program as a command line parameter, and you need to use the debugger, you can write the script to a temporary file, and use that as the program, with the -f option. This might look like this: cat << \EOF > /tmp/script.$$ ... *Your program here* EOF gawk -D -f /tmp/script.$$ rm /tmp/script.$$

### 14.6 Summary

- Programs rarely work correctly the first time. Finding bugs is called debugging, and a program that helps you find bugs is a debugger. `gawk` has a built-in debugger that works very similarly to the GNU Debugger, GDB.
- Debuggers let you step through your program one statement at a time, examine and change variable and array values, and do a number of other things that let you understand what your program is actually doing (as opposed to what it is supposed to do).
- Like most debuggers, the `gawk` debugger works in terms of stack frames, and lets you set both breakpoints (stop at a point in the code) and watchpoints (stop when a data value changes).
- The debugger command set is fairly complete, providing control over breakpoints, execution, viewing and changing data, working with the stack, getting information, and other tasks.
- If the GNU Readline library is available when `gawk` is compiled, it is used by the debugger to provide command-line history and editing.
- Usually, the debugger does not affect the program being debugged, but occasionally it can.
