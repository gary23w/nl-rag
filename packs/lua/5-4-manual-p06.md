---
title: "Lua 5.4 Reference Manual (part 6/6)"
source: https://www.lua.org/manual/5.4/manual.html
domain: lua
license: MIT / CC-BY-SA-4.0
tags: lua, lua scripting, lua manual, programming in lua
fetched: 2026-07-02
part: 6/6
---

# Lua 5.4 Reference Manual

The available formats are **"`n`":** reads a numeral and returns it as a float or an integer, following the lexical conventions of Lua. (The numeral may have leading whitespaces and a sign.) This format always reads the longest input sequence that is a valid prefix for a numeral; if that prefix does not form a valid numeral (e.g., an empty string, "`0x`", or "`3.4e-`") or it is too long (more than 200 characters), it is discarded and the format returns **fail**. **"`a`":** reads the whole file, starting at the current position. On end of file, it returns the empty string; this format never fails. **"`l`":** reads the next line skipping the end of line, returning **fail** on end of file. This is the default format. **"`L`":** reads the next line keeping the end-of-line character (if present), returning **fail** on end of file. ***number*:** reads a string with up to this number of bytes, returning **fail** on end of file. If `number` is zero, it reads nothing and returns an empty string, or **fail** on end of file.

The formats "`l`" and "`L`" should be used only for text files.

`file:seek ([whence [, offset]])`

Sets and gets the file position, measured from the beginning of the file, to the position given by `offset` plus a base specified by the string `whence`, as follows: **"`set`":** base is position 0 (beginning of the file); **"`cur`":** base is current position; **"`end`":** base is end of file;

In case of success, `seek` returns the final file position, measured in bytes from the beginning of the file. If `seek` fails, it returns **fail**, plus a string describing the error.

The default value for `whence` is `"cur"`, and for `offset` is 0. Therefore, the call `file:seek()` returns the current file position, without changing it; the call `file:seek("set")` sets the position to the beginning of the file (and returns 0); and the call `file:seek("end")` sets the position to the end of the file, and returns its size.

`file:setvbuf (mode [, size])`

Sets the buffering mode for a file. There are three available modes: **"`no`":** no buffering. **"`full`":** full buffering. **"`line`":** line buffering.

For the last two cases, `size` is a hint for the size of the buffer, in bytes. The default is an appropriate size.

The specific behavior of each mode is non portable; check the underlying ISO C function `setvbuf` in your platform for more details.

`file:write (···)`

Writes the value of each of its arguments to `file`. The arguments must be strings or numbers.

In case of success, this function returns `file`. 6.9 – Operating System Facilities

This library is implemented through table `os`.

`os.clock ()`

Returns an approximation of the amount in seconds of CPU time used by the program, as returned by the underlying ISO C function `clock`.

`os.date ([format [, time]])`

Returns a string or a table containing date and time, formatted according to the given string `format`.

If the `time` argument is present, this is the time to be formatted (see the `os.time` function for a description of this value). Otherwise, `date` formats the current time.

If `format` starts with '`!`', then the date is formatted in Coordinated Universal Time. After this optional character, if `format` is the string "`*t`", then `date` returns a table with the following fields: `year`, `month` (1–12), `day` (1–31), `hour` (0–23), `min` (0–59), `sec` (0–61, due to leap seconds), `wday` (weekday, 1–7, Sunday is 1), `yday` (day of the year, 1–366), and `isdst` (daylight saving flag, a boolean). This last field may be absent if the information is not available.

If `format` is not "`*t`", then `date` returns the date as a string, formatted according to the same rules as the ISO C function `strftime`.

If `format` is absent, it defaults to "`%c`", which gives a human-readable date and time representation using the current locale.

On non-POSIX systems, this function may be not thread safe because of its reliance on C function `gmtime` and C function `localtime`.

`os.difftime (t2, t1)`

Returns the difference, in seconds, from time `t1` to time `t2` (where the times are values returned by `os.time`). In POSIX, Windows, and some other systems, this value is exactly `t2`*-*`t1`.

`os.execute ([command])`

This function is equivalent to the ISO C function `system`. It passes `command` to be executed by an operating system shell. Its first result is **true** if the command terminated successfully, or **fail** otherwise. After this first result the function returns a string plus a number, as follows: **"`exit`":** the command terminated normally; the following number is the exit status of the command. **"`signal`":** the command was terminated by a signal; the following number is the signal that terminated the command.

When called without a `command`, `os.execute` returns a boolean that is true if a shell is available.

`os.exit ([code [, close]])`

Calls the ISO C function `exit` to terminate the host program. If `code` is **true**, the returned status is `EXIT_SUCCESS`; if `code` is **false**, the returned status is `EXIT_FAILURE`; if `code` is a number, the returned status is this number. The default value for `code` is **true**.

If the optional second argument `close` is true, the function closes the Lua state before exiting (see `lua_close`).

`os.getenv (varname)`

Returns the value of the process environment variable `varname` or **fail** if the variable is not defined.

`os.remove (filename)`

Deletes the file (or empty directory, on POSIX systems) with the given name. If this function fails, it returns **fail** plus a string describing the error and the error code. Otherwise, it returns true.

`os.rename (oldname, newname)`

Renames the file or directory named `oldname` to `newname`. If this function fails, it returns **fail**, plus a string describing the error and the error code. Otherwise, it returns true.

`os.setlocale (locale [, category])`

Sets the current locale of the program. `locale` is a system-dependent string specifying a locale; `category` is an optional string describing which category to change: `"all"`, `"collate"`, `"ctype"`, `"monetary"`, `"numeric"`, or `"time"`; the default category is `"all"`. The function returns the name of the new locale, or **fail** if the request cannot be honored.

If `locale` is the empty string, the current locale is set to an implementation-defined native locale. If `locale` is the string "`C`", the current locale is set to the standard C locale.

When called with **nil** as the first argument, this function only returns the name of the current locale for the given category.

This function may be not thread safe because of its reliance on C function `setlocale`.

`os.time ([table])`

Returns the current time when called without arguments, or a time representing the local date and time specified by the given table. This table must have fields `year`, `month`, and `day`, and may have fields `hour` (default is 12), `min` (default is 0), `sec` (default is 0), and `isdst` (default is **nil**). Other fields are ignored. For a description of these fields, see the `os.date` function.

When the function is called, the values in these fields do not need to be inside their valid ranges. For instance, if `sec` is -10, it means 10 seconds before the time specified by the other fields; if `hour` is 1000, it means 1000 hours after the time specified by the other fields.

The returned value is a number, whose meaning depends on your system. In POSIX, Windows, and some other systems, this number counts the number of seconds since some given start time (the "epoch"). In other systems, the meaning is not specified, and the number returned by `time` can be used only as an argument to `os.date` and `os.difftime`.

When called with a table, `os.time` also normalizes all the fields documented in the `os.date` function, so that they represent the same time as before the call but with values inside their valid ranges.

`os.tmpname ()`

Returns a string with a file name that can be used for a temporary file. The file must be explicitly opened before its use and explicitly removed when no longer needed.

In POSIX systems, this function also creates a file with that name, to avoid security risks. (Someone else might create the file with wrong permissions in the time between getting the name and creating the file.) You still have to open the file to use it and to remove it (even if you do not use it).

When possible, you may prefer to use `io.tmpfile`, which automatically removes the file when the program ends. 6.10 – The Debug Library

This library provides the functionality of the debug interface (§4.7) to Lua programs. You should exert care when using this library. Several of its functions violate basic assumptions about Lua code (e.g., that variables local to a function cannot be accessed from outside; that userdata metatables cannot be changed by Lua code; that Lua programs do not crash) and therefore can compromise otherwise secure code. Moreover, some functions in this library may be slow.

All functions in this library are provided inside the `debug` table. All functions that operate over a thread have an optional first argument which is the thread to operate over. The default is always the current thread.

`debug.debug ()`

Enters an interactive mode with the user, running each string that the user enters. Using simple commands and other debug facilities, the user can inspect global and local variables, change their values, evaluate expressions, and so on. A line containing only the word `cont` finishes this function, so that the caller continues its execution.

Note that commands for `debug.debug` are not lexically nested within any function and so have no direct access to local variables.

`debug.gethook ([thread])`

Returns the current hook settings of the thread, as three values: the current hook function, the current hook mask, and the current hook count, as set by the `debug.sethook` function.

Returns **fail** if there is no active hook.

`debug.getinfo ([thread,] f [, what])`

Returns a table with information about a function. You can give the function directly or you can give a number as the value of `f`, which means the function running at level `f` of the call stack of the given thread: level 0 is the current function (`getinfo` itself); level 1 is the function that called `getinfo` (except for tail calls, which do not count in the stack); and so on. If `f` is a number greater than the number of active functions, then `getinfo` returns **fail**.

The returned table can contain all the fields returned by `lua_getinfo`, with the string `what` describing which fields to fill in. The default for `what` is to get all information available, except the table of valid lines. The option '`f`' adds a field named `func` with the function itself. The option '`L`' adds a field named `activelines` with the table of valid lines, provided the function is a Lua function. If the function has no debug information, the table is empty.

For instance, the expression `debug.getinfo(1,"n").name` returns a name for the current function, if a reasonable name can be found, and the expression `debug.getinfo(print)` returns a table with all available information about the `print` function.

`debug.getlocal ([thread,] f, local)`

This function returns the name and the value of the local variable with index `local` of the function at level `f` of the stack. This function accesses not only explicit local variables, but also parameters and temporary values.

The first parameter or local variable has index 1, and so on, following the order that they are declared in the code, counting only the variables that are active in the current scope of the function. Compile-time constants may not appear in this listing, if they were optimized away by the compiler. Negative indices refer to vararg arguments; -1 is the first vararg argument. The function returns **fail** if there is no variable with the given index, and raises an error when called with a level out of range. (You can call `debug.getinfo` to check whether the level is valid.)

Variable names starting with '`(`' (open parenthesis) represent variables with no known names (internal variables such as loop control variables, and variables from chunks saved without debug information).

The parameter `f` may also be a function. In that case, `getlocal` returns only the name of function parameters.

`debug.getmetatable (value)`

Returns the metatable of the given `value` or **nil** if it does not have a metatable.

`debug.getregistry ()`

Returns the registry table (see §4.3).

`debug.getupvalue (f, up)`

This function returns the name and the value of the upvalue with index `up` of the function `f`. The function returns **fail** if there is no upvalue with the given index.

(For Lua functions, upvalues are the external local variables that the function uses, and that are consequently included in its closure.)

For C functions, this function uses the empty string `""` as a name for all upvalues.

Variable name '`?`' (interrogation mark) represents variables with no known names (variables from chunks saved without debug information).

`debug.getuservalue (u, n)`

Returns the `n`-th user value associated to the userdata `u` plus a boolean, **false** if the userdata does not have that value.

`debug.sethook ([thread,] hook, mask [, count])`

Sets the given function as the debug hook. The string `mask` and the number `count` describe when the hook will be called. The string mask may have any combination of the following characters, with the given meaning: **'`c`':** the hook is called every time Lua calls a function; **'`r`':** the hook is called every time Lua returns from a function; **'`l`':** the hook is called every time Lua enters a new line of code.

Moreover, with a `count` different from zero, the hook is called also after every `count` instructions.

When called without arguments, `debug.sethook` turns off the hook.

When the hook is called, its first parameter is a string describing the event that has triggered its call: `"call"`, `"tail call"`, `"return"`, `"line"`, and `"count"`. For line events, the hook also gets the new line number as its second parameter. Inside a hook, you can call `getinfo` with level 2 to get more information about the running function. (Level 0 is the `getinfo` function, and level 1 is the hook function.)

`debug.setlocal ([thread,] level, local, value)`

This function assigns the value `value` to the local variable with index `local` of the function at level `level` of the stack. The function returns **fail** if there is no local variable with the given index, and raises an error when called with a `level` out of range. (You can call `getinfo` to check whether the level is valid.) Otherwise, it returns the name of the local variable.

See `debug.getlocal` for more information about variable indices and names.

`debug.setmetatable (value, table)`

Sets the metatable for the given `value` to the given `table` (which can be **nil**). Returns `value`.

`debug.setupvalue (f, up, value)`

This function assigns the value `value` to the upvalue with index `up` of the function `f`. The function returns **fail** if there is no upvalue with the given index. Otherwise, it returns the name of the upvalue.

See `debug.getupvalue` for more information about upvalues.

`debug.setuservalue (udata, value, n)`

Sets the given `value` as the `n`-th user value associated to the given `udata`. `udata` must be a full userdata.

Returns `udata`, or **fail** if the userdata does not have that value.

`debug.traceback ([thread,] [message [, level]])`

If `message` is present but is neither a string nor **nil**, this function returns `message` without further processing. Otherwise, it returns a string with a traceback of the call stack. The optional `message` string is appended at the beginning of the traceback. An optional `level` number tells at which level to start the traceback (default is 1, the function calling `traceback`).

`debug.upvalueid (f, n)`

Returns a unique identifier (as a light userdata) for the upvalue numbered `n` from the given function.

These unique identifiers allow a program to check whether different closures share upvalues. Lua closures that share an upvalue (that is, that access a same external local variable) will return identical ids for those upvalue indices.

`debug.upvaluejoin (f1, n1, f2, n2)`

Make the `n1`-th upvalue of the Lua closure `f1` refer to the `n2`-th upvalue of the Lua closure `f2`. 7 – Lua Standalone

Although Lua has been designed as an extension language, to be embedded in a host C program, it is also frequently used as a standalone language. An interpreter for Lua as a standalone language, called simply `lua`, is provided with the standard distribution. The standalone interpreter includes all standard libraries. Its usage is: lua [options] [script [args]]

The options are: **`-e *stat*`:** execute string *stat*; **`-i`:** enter interactive mode after running *script*; **`-l *mod*`:** "require" *mod* and assign the result to global *mod*; **`-l *g=mod*`:** "require" *mod* and assign the result to global *g*; **`-v`:** print version information; **`-E`:** ignore environment variables; **`-W`:** turn warnings on; **`--`:** stop handling options; **`-`:** execute `stdin` as a file and stop handling options.

(The form `-l *g=mod*` was introduced in release 5.4.4.)

After handling its options, `lua` runs the given *script*. When called without arguments, `lua` behaves as `lua -v -i` when the standard input (`stdin`) is a terminal, and as `lua -` otherwise.

When called without the option `-E`, the interpreter checks for an environment variable `LUA_INIT_5_4` (or `LUA_INIT` if the versioned name is not defined) before running any argument. If the variable content has the format `@*filename*`, then `lua` executes the file. Otherwise, `lua` executes the string itself.

When called with the option `-E`, Lua does not consult any environment variables. In particular, the values of `package.path` and `package.cpath` are set with the default paths defined in `luaconf.h`. To signal to the libraries that this option is on, the stand-alone interpreter sets the field `"LUA_NOENV"` in the registry to a true value. Other libraries may consult this field for the same purpose.

The options `-e`, `-l`, and `-W` are handled in the order they appear. For instance, an invocation like $ lua -e 'a=1' -llib1 script.lua

will first set `a` to 1, then require the library `lib1`, and finally run the file `script.lua` with no arguments. (Here `$` is the shell prompt. Your prompt may be different.)

Before running any code, `lua` collects all command-line arguments in a global table called `arg`. The script name goes to index 0, the first argument after the script name goes to index 1, and so on. Any arguments before the script name (that is, the interpreter name plus its options) go to negative indices. For instance, in the call $ lua -la b.lua t1 t2

the table is like this: arg = { [-2] = "lua", [-1] = "-la", [0] = "b.lua", [1] = "t1", [2] = "t2" }

If there is no script in the call, the interpreter name goes to index 0, followed by the other arguments. For instance, the call $ lua -e "print(arg[1])"

will print "`-e`". If there is a script, the script is called with arguments `arg[1]`, ···, `arg[#arg]`. Like all chunks in Lua, the script is compiled as a variadic function.

In interactive mode, Lua repeatedly prompts and waits for a line. After reading a line, Lua first try to interpret the line as an expression. If it succeeds, it prints its value. Otherwise, it interprets the line as a statement. If you write an incomplete statement, the interpreter waits for its completion by issuing a different prompt.

If the global variable `_PROMPT` contains a string, then its value is used as the prompt. Similarly, if the global variable `_PROMPT2` contains a string, its value is used as the secondary prompt (issued during incomplete statements).

In case of unprotected errors in the script, the interpreter reports the error to the standard error stream. If the error object is not a string but has a metamethod `__tostring`, the interpreter calls this metamethod to produce the final message. Otherwise, the interpreter converts the error object to a string and adds a stack traceback to it. When warnings are on, they are simply printed in the standard error output.

When finishing normally, the interpreter closes its main Lua state (see `lua_close`). The script can avoid this step by calling `os.exit` to terminate.

To allow the use of Lua as a script interpreter in Unix systems, Lua skips the first line of a file chunk if it starts with `#`. Therefore, Lua scripts can be made into executable programs by using `chmod +x` and the `#!` form, as in #!/usr/local/bin/lua

Of course, the location of the Lua interpreter may be different in your machine. If `lua` is in your `PATH`, then #!/usr/bin/env lua

is a more portable solution. 8 – Incompatibilities with the Previous Version

Here we list the incompatibilities that you may find when moving a program from Lua 5.3 to Lua 5.4.

You can avoid some incompatibilities by compiling Lua with appropriate options (see file `luaconf.h`). However, all these compatibility options will be removed in the future. More often than not, compatibility issues arise when these compatibility options are removed. So, whenever you have the chance, you should try to test your code with a version of Lua compiled with all compatibility options turned off. That will ease transitions to newer versions of Lua.

Lua versions can always change the C API in ways that do not imply source-code changes in a program, such as the numeric values for constants or the implementation of functions as macros. Therefore, you should never assume that binaries are compatible between different Lua versions. Always recompile clients of the Lua API when using a new version.

Similarly, Lua versions can always change the internal representation of precompiled chunks; precompiled chunks are not compatible between different Lua versions.

The standard paths in the official distribution may change between versions. 8.1 – Incompatibilities in the Language The coercion of strings to numbers in arithmetic and bitwise operations has been removed from the core language. The string library does a similar job for arithmetic (but not for bitwise) operations using the string metamethods. However, unlike in previous versions, the new implementation preserves the implicit type of the numeral in the string. For instance, the result of `"1" + "2"` now is an integer, not a float. Literal decimal integer constants that overflow are read as floats, instead of wrapping around. You can use hexadecimal notation for such constants if you want the old behavior (reading them as integers with wrap around). The use of the `__lt` metamethod to emulate `__le` has been removed. When needed, this metamethod must be explicitly defined. The semantics of the numerical **for** loop over integers changed in some details. In particular, the control variable never wraps around. A label for a **goto** cannot be declared where a label with the same name is visible, even if this other label is declared in an enclosing block. When finalizing an object, Lua does not ignore `__gc` metamethods that are not functions. Any value will be called, if present. (Non-callable values will generate a warning, like any other error when calling a finalizer.) 8.2 – Incompatibilities in the Libraries The function `print` does not call `tostring` to format its arguments; instead, it has this functionality hardwired. You should use `__tostring` to modify how values are printed. The pseudo-random number generator used by the function `math.random` now starts with a somewhat random seed. Moreover, it uses a different algorithm. By default, the decoding functions in the `utf8` library do not accept surrogates as valid code points. An extra parameter in these functions makes them more permissive. The options "`setpause`" and "`setstepmul`" of the function `collectgarbage` are deprecated. You should use the new option "`incremental`" to set them. The function `io.lines` now returns four values, instead of just one. That can be a problem when it is used as the sole argument to another function that has optional parameters, such as in `load(io.lines(filename, "L"))`. To fix that issue, you can wrap the call into parentheses, to adjust its number of results to one. 8.3 – Incompatibilities in the API Full userdata now has an arbitrary number of associated user values. Therefore, the functions `lua_newuserdata`, `lua_setuservalue`, and `lua_getuservalue` were replaced by `lua_newuserdatauv`, `lua_setiuservalue`, and `lua_getiuservalue`, which have an extra argument. For compatibility, the old names still work as macros assuming one single user value. Note, however, that userdata with zero user values are more efficient memory-wise. The function `lua_resume` has an extra parameter. This out parameter returns the number of values on the top of the stack that were yielded or returned by the coroutine. (In previous versions, those values were the entire stack.) The function `lua_version` returns the version number, instead of an address of the version number. The Lua core should work correctly with libraries using their own static copies of the same core, so there is no need to check whether they are using the same address space. The constant `LUA_ERRGCMM` was removed. Errors in finalizers are never propagated; instead, they generate a warning. The options `LUA_GCSETPAUSE` and `LUA_GCSETSTEPMUL` of the function `lua_gc` are deprecated. You should use the new option `LUA_GCINC` to set them. 9 – The Complete Syntax of Lua

Here is the complete syntax of Lua in extended BNF. As usual in extended BNF, {A} means 0 or more As, and [A] means an optional A. (For operator precedences, see §3.4.8; for a description of the terminals Name, Numeral, and LiteralString, see §3.1.) chunk ::= block block ::= {stat} [retstat] stat ::= ‘**;**’ | varlist ‘**=**’ explist | functioncall | label | **break** | **goto** Name | **do** block **end** | **while** exp **do** block **end** | **repeat** block **until** exp | **if** exp **then** block {**elseif** exp **then** block} [**else** block] **end** | **for** Name ‘**=**’ exp ‘**,**’ exp [‘**,**’ exp] **do** block **end** | **for** namelist **in** explist **do** block **end** | **function** funcname funcbody | **local** **function** Name funcbody | **local** attnamelist [‘**=**’ explist] attnamelist ::= Name attrib {‘**,**’ Name attrib} attrib ::= [‘**<**’ Name ‘**>**’] retstat ::= **return** [explist] [‘**;**’] label ::= ‘**::**’ Name ‘**::**’ funcname ::= Name {‘**.**’ Name} [‘**:**’ Name] varlist ::= var {‘**,**’ var} var ::= Name | prefixexp ‘**[**’ exp ‘**]**’ | prefixexp ‘**.**’ Name namelist ::= Name {‘**,**’ Name} explist ::= exp {‘**,**’ exp} exp ::= **nil** | **false** | **true** | Numeral | LiteralString | ‘**...**’ | functiondef | prefixexp | tableconstructor | exp binop exp | unop exp prefixexp ::= var | functioncall | ‘**(**’ exp ‘**)**’ functioncall ::= prefixexp args | prefixexp ‘**:**’ Name args args ::= ‘**(**’ [explist] ‘**)**’ | tableconstructor | LiteralString functiondef ::= **function** funcbody funcbody ::= ‘**(**’ [parlist] ‘**)**’ block **end** parlist ::= namelist [‘**,**’ ‘**...**’] | ‘**...**’ tableconstructor ::= ‘**{**’ [fieldlist] ‘**}**’ fieldlist ::= field {fieldsep field} [fieldsep] field ::= ‘**[**’ exp ‘**]**’ ‘**=**’ exp | Name ‘**=**’ exp | exp fieldsep ::= ‘**,**’ | ‘**;**’ binop ::= ‘**+**’ | ‘**-**’ | ‘*****’ | ‘**/**’ | ‘**//**’ | ‘**^**’ | ‘**%**’ | ‘**&**’ | ‘**~**’ | ‘**|**’ | ‘**>>**’ | ‘**<<**’ | ‘**..**’ | ‘**<**’ | ‘**<=**’ | ‘**>**’ | ‘**>=**’ | ‘**==**’ | ‘**~=**’ | **and** | **or** unop ::= ‘**-**’ | **not** | ‘**#**’ | ‘**~**’
