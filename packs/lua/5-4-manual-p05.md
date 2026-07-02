---
title: "Lua 5.4 Reference Manual (part 5/6)"
source: https://www.lua.org/manual/5.4/manual.html
domain: lua
license: MIT / CC-BY-SA-4.0
tags: lua, lua scripting, lua manual, programming in lua
fetched: 2026-07-02
part: 5/6
---

# Lua 5.4 Reference Manual

Emits a warning with a message composed by the concatenation of all its arguments (which should be strings).

By convention, a one-piece message starting with '`@`' is intended to be a *control message*, which is a message to the warning system itself. In particular, the standard warning function in Lua recognizes the control messages "`@off`", to stop the emission of warnings, and "`@on`", to (re)start the emission; it ignores unknown control messages.

`xpcall (f, msgh [, arg1, ···])`

This function is similar to `pcall`, except that it sets a new message handler `msgh`. 6.2 – Coroutine Manipulation

This library comprises the operations to manipulate coroutines, which come inside the table `coroutine`. See §2.6 for a general description of coroutines.

`coroutine.close (co)`

Closes coroutine `co`, that is, closes all its pending to-be-closed variables and puts the coroutine in a dead state. The given coroutine must be dead or suspended. In case of error (either the original error that stopped the coroutine or errors in closing methods), returns **false** plus the error object; otherwise returns **true**.

`coroutine.create (f)`

Creates a new coroutine, with body `f`. `f` must be a function. Returns this new coroutine, an object with type `"thread"`.

`coroutine.isyieldable ([co])`

Returns **true** when the coroutine `co` can yield. The default for `co` is the running coroutine.

A coroutine is yieldable if it is not the main thread and it is not inside a non-yieldable C function.

`coroutine.resume (co [, val1, ···])`

Starts or continues the execution of coroutine `co`. The first time you resume a coroutine, it starts running its body. The values `val1`, ... are passed as the arguments to the body function. If the coroutine has yielded, `resume` restarts it; the values `val1`, ... are passed as the results from the yield.

If the coroutine runs without any errors, `resume` returns **true** plus any values passed to `yield` (when the coroutine yields) or any values returned by the body function (when the coroutine terminates). If there is any error, `resume` returns **false** plus the error message.

`coroutine.running ()`

Returns the running coroutine plus a boolean, **true** when the running coroutine is the main one.

`coroutine.status (co)`

Returns the status of the coroutine `co`, as a string: `"running"`, if the coroutine is running (that is, it is the one that called `status`); `"suspended"`, if the coroutine is suspended in a call to `yield`, or if it has not started running yet; `"normal"` if the coroutine is active but not running (that is, it has resumed another coroutine); and `"dead"` if the coroutine has finished its body function, or if it has stopped with an error.

`coroutine.wrap (f)`

Creates a new coroutine, with body `f`; `f` must be a function. Returns a function that resumes the coroutine each time it is called. Any arguments passed to this function behave as the extra arguments to `resume`. The function returns the same values returned by `resume`, except the first boolean. In case of error, the function closes the coroutine and propagates the error.

`coroutine.yield (···)`

Suspends the execution of the calling coroutine. Any arguments to `yield` are passed as extra results to `resume`. 6.3 – Modules

The package library provides basic facilities for loading modules in Lua. It exports one function directly in the global environment: `require`. Everything else is exported in the table `package`.

`require (modname)`

Loads the given module. The function starts by looking into the `package.loaded` table to determine whether `modname` is already loaded. If it is, then `require` returns the value stored at `package.loaded[modname]`. (The absence of a second result in this case signals that this call did not have to load the module.) Otherwise, it tries to find a *loader* for the module.

To find a loader, `require` is guided by the table `package.searchers`. Each item in this table is a search function, that searches for the module in a particular way. By changing this table, we can change how `require` looks for a module. The following explanation is based on the default configuration for `package.searchers`.

First `require` queries `package.preload[modname]`. If it has a value, this value (which must be a function) is the loader. Otherwise `require` searches for a Lua loader using the path stored in `package.path`. If that also fails, it searches for a C loader using the path stored in `package.cpath`. If that also fails, it tries an *all-in-one* loader (see `package.searchers`).

Once a loader is found, `require` calls the loader with two arguments: `modname` and an extra value, a *loader data*, also returned by the searcher. The loader data can be any value useful to the module; for the default searchers, it indicates where the loader was found. (For instance, if the loader came from a file, this extra value is the file path.) If the loader returns any non-nil value, `require` assigns the returned value to `package.loaded[modname]`. If the loader does not return a non-nil value and has not assigned any value to `package.loaded[modname]`, then `require` assigns **true** to this entry. In any case, `require` returns the final value of `package.loaded[modname]`. Besides that value, `require` also returns as a second result the loader data returned by the searcher, which indicates how `require` found the module.

If there is any error loading or running the module, or if it cannot find any loader for the module, then `require` raises an error.

`package.config`

A string describing some compile-time configurations for packages. This string is a sequence of lines: The first line is the directory separator string. Default is '`\`' for Windows and '`/`' for all other systems. The second line is the character that separates templates in a path. Default is '`;`'. The third line is the string that marks the substitution points in a template. Default is '`?`'. The fourth line is a string that, in a path in Windows, is replaced by the executable's directory. Default is '`!`'. The fifth line is a mark to ignore all text after it when building the `luaopen_` function name. Default is '`-`'.

`package.cpath`

A string with the path used by `require` to search for a C loader.

Lua initializes the C path `package.cpath` in the same way it initializes the Lua path `package.path`, using the environment variable `LUA_CPATH_5_4`, or the environment variable `LUA_CPATH`, or a default path defined in `luaconf.h`.

`package.loaded`

A table used by `require` to control which modules are already loaded. When you require a module `modname` and `package.loaded[modname]` is not false, `require` simply returns the value stored there.

This variable is only a reference to the real table; assignments to this variable do not change the table used by `require`. The real table is stored in the C registry (see §4.3), indexed by the key `LUA_LOADED_TABLE`, a string.

`package.loadlib (libname, funcname)`

Dynamically links the host program with the C library `libname`.

If `funcname` is "`*`", then it only links with the library, making the symbols exported by the library available to other dynamically linked libraries. Otherwise, it looks for a function `funcname` inside the library and returns this function as a C function. So, `funcname` must follow the `lua_CFunction` prototype (see `lua_CFunction`).

This is a low-level function. It completely bypasses the package and module system. Unlike `require`, it does not perform any path searching and does not automatically adds extensions. `libname` must be the complete file name of the C library, including if necessary a path and an extension. `funcname` must be the exact name exported by the C library (which may depend on the C compiler and linker used).

This functionality is not supported by ISO C. As such, it is only available on some platforms (Windows, Linux, Mac OS X, Solaris, BSD, plus other Unix systems that support the `dlfcn` standard).

This function is inherently insecure, as it allows Lua to call any function in any readable dynamic library in the system. (Lua calls any function assuming the function has a proper prototype and respects a proper protocol (see `lua_CFunction`). Therefore, calling an arbitrary function in an arbitrary dynamic library more often than not results in an access violation.)

`package.path`

A string with the path used by `require` to search for a Lua loader.

At start-up, Lua initializes this variable with the value of the environment variable `LUA_PATH_5_4` or the environment variable `LUA_PATH` or with a default path defined in `luaconf.h`, if those environment variables are not defined. A "`;;`" in the value of the environment variable is replaced by the default path.

`package.preload`

A table to store loaders for specific modules (see `require`).

This variable is only a reference to the real table; assignments to this variable do not change the table used by `require`. The real table is stored in the C registry (see §4.3), indexed by the key `LUA_PRELOAD_TABLE`, a string.

`package.searchers`

A table used by `require` to control how to find modules.

Each entry in this table is a *searcher function*. When looking for a module, `require` calls each of these searchers in ascending order, with the module name (the argument given to `require`) as its sole argument. If the searcher finds the module, it returns another function, the module *loader*, plus an extra value, a *loader data*, that will be passed to that loader and returned as a second result by `require`. If it cannot find the module, it returns a string explaining why (or **nil** if it has nothing to say).

Lua initializes this table with four searcher functions.

The first searcher simply looks for a loader in the `package.preload` table.

The second searcher looks for a loader as a Lua library, using the path stored at `package.path`. The search is done as described in function `package.searchpath`.

The third searcher looks for a loader as a C library, using the path given by the variable `package.cpath`. Again, the search is done as described in function `package.searchpath`. For instance, if the C path is the string "./?.so;./?.dll;/usr/local/?/init.so"

the searcher for module `foo` will try to open the files `./foo.so`, `./foo.dll`, and `/usr/local/foo/init.so`, in that order. Once it finds a C library, this searcher first uses a dynamic link facility to link the application with the library. Then it tries to find a C function inside the library to be used as the loader. The name of this C function is the string "`luaopen_`" concatenated with a copy of the module name where each dot is replaced by an underscore. Moreover, if the module name has a hyphen, its suffix after (and including) the first hyphen is removed. For instance, if the module name is `a.b.c-v2.1`, the function name will be `luaopen_a_b_c`.

The fourth searcher tries an *all-in-one loader*. It searches the C path for a library for the root name of the given module. For instance, when requiring `a.b.c`, it will search for a C library for `a`. If found, it looks into it for an open function for the submodule; in our example, that would be `luaopen_a_b_c`. With this facility, a package can pack several C submodules into one single library, with each submodule keeping its original open function.

All searchers except the first one (preload) return as the extra value the file path where the module was found, as returned by `package.searchpath`. The first searcher always returns the string "`:preload:`".

Searchers should raise no errors and have no side effects in Lua. (They may have side effects in C, for instance by linking the application with a library.)

`package.searchpath (name, path [, sep [, rep]])`

Searches for the given `name` in the given `path`.

A path is a string containing a sequence of *templates* separated by semicolons. For each template, the function replaces each interrogation mark (if any) in the template with a copy of `name` wherein all occurrences of `sep` (a dot, by default) were replaced by `rep` (the system's directory separator, by default), and then tries to open the resulting file name.

For instance, if the path is the string "./?.lua;./?.lc;/usr/local/?/init.lua"

the search for the name `foo.a` will try to open the files `./foo/a.lua`, `./foo/a.lc`, and `/usr/local/foo/a/init.lua`, in that order.

Returns the resulting name of the first file that it can open in read mode (after closing the file), or **fail** plus an error message if none succeeds. (This error message lists all file names it tried to open.) 6.4 – String Manipulation

This library provides generic functions for string manipulation, such as finding and extracting substrings, and pattern matching. When indexing a string in Lua, the first character is at position 1 (not at 0, as in C). Indices are allowed to be negative and are interpreted as indexing backwards, from the end of the string. Thus, the last character is at position -1, and so on.

The string library provides all its functions inside the table `string`. It also sets a metatable for strings where the `__index` field points to the `string` table. Therefore, you can use the string functions in object-oriented style. For instance, `string.byte(s,i)` can be written as `s:byte(i)`.

The string library assumes one-byte character encodings.

`string.byte (s [, i [, j]])` Returns the internal numeric codes of the characters `s[i]`, `s[i+1]`, ..., `s[j]`. The default value for `i` is 1; the default value for `j` is `i`. These indices are corrected following the same rules of function `string.sub`.

Numeric codes are not necessarily portable across platforms.

`string.char (···)` Receives zero or more integers. Returns a string with length equal to the number of arguments, in which each character has the internal numeric code equal to its corresponding argument.

Numeric codes are not necessarily portable across platforms.

`string.dump (function [, strip])`

Returns a string containing a binary representation (a *binary chunk*) of the given function, so that a later `load` on this string returns a copy of the function (but with new upvalues). If `strip` is a true value, the binary representation may not include all debug information about the function, to save space.

Functions with upvalues have only their number of upvalues saved. When (re)loaded, those upvalues receive fresh instances. (See the `load` function for details about how these upvalues are initialized. You can use the debug library to serialize and reload the upvalues of a function in a way adequate to your needs.)

`string.find (s, pattern [, init [, plain]])`

Looks for the first match of `pattern` (see §6.4.1) in the string `s`. If it finds a match, then `find` returns the indices of `s` where this occurrence starts and ends; otherwise, it returns **fail**. A third, optional numeric argument `init` specifies where to start the search; its default value is 1 and can be negative. A **true** as a fourth, optional argument `plain` turns off the pattern matching facilities, so the function does a plain "find substring" operation, with no characters in `pattern` being considered magic.

If the pattern has captures, then in a successful match the captured values are also returned, after the two indices.

`string.format (formatstring, ···)`

Returns a formatted version of its variable number of arguments following the description given in its first argument, which must be a string. The format string follows the same rules as the ISO C function `sprintf`. The only differences are that the conversion specifiers and modifiers `F`, `n`, `*`, `h`, `L`, and `l` are not supported and that there is an extra specifier, `q`. Both width and precision, when present, are limited to two digits.

The specifier `q` formats booleans, nil, numbers, and strings in a way that the result is a valid constant in Lua source code. Booleans and nil are written in the obvious way (`true`, `false`, `nil`). Floats are written in hexadecimal, to preserve full precision. A string is written between double quotes, using escape sequences when necessary to ensure that it can safely be read back by the Lua interpreter. For instance, the call string.format('%q', 'a string with "quotes" and \n new line')

may produce the string: "a string with \"quotes\" and \ new line"

This specifier does not support modifiers (flags, width, precision).

The conversion specifiers `A`, `a`, `E`, `e`, `f`, `G`, and `g` all expect a number as argument. The specifiers `c`, `d`, `i`, `o`, `u`, `X`, and `x` expect an integer. When Lua is compiled with a C89 compiler, the specifiers `A` and `a` (hexadecimal floats) do not support modifiers.

The specifier `s` expects a string; if its argument is not a string, it is converted to one following the same rules of `tostring`. If the specifier has any modifier, the corresponding string argument should not contain embedded zeros.

The specifier `p` formats the pointer returned by `lua_topointer`. That gives a unique string identifier for tables, userdata, threads, strings, and functions. For other values (numbers, nil, booleans), this specifier results in a string representing the pointer `NULL`.

`string.gmatch (s, pattern [, init])` Returns an iterator function that, each time it is called, returns the next captures from `pattern` (see §6.4.1) over the string `s`. If `pattern` specifies no captures, then the whole match is produced in each call. A third, optional numeric argument `init` specifies where to start the search; its default value is 1 and can be negative.

As an example, the following loop will iterate over all the words from string `s`, printing one per line: s = "hello world from Lua" for w in string.gmatch(s, "%a+") do print(w) end

The next example collects all pairs `key=value` from the given string into a table: t = {} s = "from=world, to=Lua" for k, v in string.gmatch(s, "(%w+)=(%w+)") do t[k] = v end

For this function, a caret '`^`' at the start of a pattern does not work as an anchor, as this would prevent the iteration.

`string.gsub (s, pattern, repl [, n])` Returns a copy of `s` in which all (or the first `n`, if given) occurrences of the `pattern` (see §6.4.1) have been replaced by a replacement string specified by `repl`, which can be a string, a table, or a function. `gsub` also returns, as its second value, the total number of matches that occurred. The name `gsub` comes from *Global SUBstitution*.

If `repl` is a string, then its value is used for replacement. The character `%` works as an escape character: any sequence in `repl` of the form `%*d*`, with *d* between 1 and 9, stands for the value of the *d*-th captured substring; the sequence `%0` stands for the whole match; the sequence `%%` stands for a single `%`.

If `repl` is a table, then the table is queried for every match, using the first capture as the key.

If `repl` is a function, then this function is called every time a match occurs, with all captured substrings passed as arguments, in order.

In any case, if the pattern specifies no captures, then it behaves as if the whole pattern was inside a capture.

If the value returned by the table query or by the function call is a string or a number, then it is used as the replacement string; otherwise, if it is **false** or **nil**, then there is no replacement (that is, the original match is kept in the string).

Here are some examples: x = string.gsub("hello world", "(%w+)", "%1 %1") --> x="hello hello world world" x = string.gsub("hello world", "%w+", "%0 %0", 1) --> x="hello hello world" x = string.gsub("hello world from Lua", "(%w+)%s*(%w+)", "%2 %1") --> x="world hello Lua from" x = string.gsub("home = $HOME, user = $USER", "%$(%w+)", os.getenv) --> x="home = /home/roberto, user = roberto" x = string.gsub("4+5 = $return 4+5$", "%$(.-)%$", function (s) return load(s)() end) --> x="4+5 = 9" local t = {name="lua", version="5.4"} x = string.gsub("$name-$version.tar.gz", "%$(%w+)", t) --> x="lua-5.4.tar.gz"

`string.len (s)`

Receives a string and returns its length. The empty string `""` has length 0. Embedded zeros are counted, so `"a\000bc\000"` has length 5.

`string.lower (s)`

Receives a string and returns a copy of this string with all uppercase letters changed to lowercase. All other characters are left unchanged. The definition of what an uppercase letter is depends on the current locale.

`string.match (s, pattern [, init])`

Looks for the first *match* of the `pattern` (see §6.4.1) in the string `s`. If it finds one, then `match` returns the captures from the pattern; otherwise it returns **fail**. If `pattern` specifies no captures, then the whole match is returned. A third, optional numeric argument `init` specifies where to start the search; its default value is 1 and can be negative.

`string.pack (fmt, v1, v2, ···)`

Returns a binary string containing the values `v1`, `v2`, etc. serialized in binary form (packed) according to the format string `fmt` (see §6.4.2).

`string.packsize (fmt)`

Returns the length of a string resulting from `string.pack` with the given format. The format string cannot have the variable-length options '`s`' or '`z`' (see §6.4.2).

`string.rep (s, n [, sep])`

Returns a string that is the concatenation of `n` copies of the string `s` separated by the string `sep`. The default value for `sep` is the empty string (that is, no separator). Returns the empty string if `n` is not positive.

(Note that it is very easy to exhaust the memory of your machine with a single call to this function.)

`string.reverse (s)`

Returns a string that is the string `s` reversed.

`string.sub (s, i [, j])`

Returns the substring of `s` that starts at `i` and continues until `j`; `i` and `j` can be negative. If `j` is absent, then it is assumed to be equal to -1 (which is the same as the string length). In particular, the call `string.sub(s,1,j)` returns a prefix of `s` with length `j`, and `string.sub(s, -i)` (for a positive `i`) returns a suffix of `s` with length `i`.

If, after the translation of negative indices, `i` is less than 1, it is corrected to 1. If `j` is greater than the string length, it is corrected to that length. If, after these corrections, `i` is greater than `j`, the function returns the empty string.

`string.unpack (fmt, s [, pos])`

Returns the values packed in string `s` (see `string.pack`) according to the format string `fmt` (see §6.4.2). An optional `pos` marks where to start reading in `s` (default is 1). After the read values, this function also returns the index of the first unread byte in `s`.

`string.upper (s)`

Receives a string and returns a copy of this string with all lowercase letters changed to uppercase. All other characters are left unchanged. The definition of what a lowercase letter is depends on the current locale. 6.4.1 – Patterns

Patterns in Lua are described by regular strings, which are interpreted as patterns by the pattern-matching functions `string.find`, `string.gmatch`, `string.gsub`, and `string.match`. This section describes the syntax and the meaning (that is, what they match) of these strings. Character Class:

A *character class* is used to represent a set of characters. The following combinations are allowed in describing a character class: ***x*:** (where *x* is not one of the *magic characters* `^$()%.[]*+-?`) represents the character *x* itself. **`.`:** (a dot) represents all characters. **`%a`:** represents all letters. **`%c`:** represents all control characters. **`%d`:** represents all digits. **`%g`:** represents all printable characters except space. **`%l`:** represents all lowercase letters. **`%p`:** represents all punctuation characters. **`%s`:** represents all space characters. **`%u`:** represents all uppercase letters. **`%w`:** represents all alphanumeric characters. **`%x`:** represents all hexadecimal digits. **`%*x*`:** (where *x* is any non-alphanumeric character) represents the character *x*. This is the standard way to escape the magic characters. Any non-alphanumeric character (including all punctuation characters, even the non-magical) can be preceded by a '`%`' to represent itself in a pattern. **`[*set*]`:** represents the class which is the union of all characters in *set*. A range of characters can be specified by separating the end characters of the range, in ascending order, with a '`-`'. All classes `%`*x* described above can also be used as components in *set*. All other characters in *set* represent themselves. For example, `[%w_]` (or `[_%w]`) represents all alphanumeric characters plus the underscore, `[0-7]` represents the octal digits, and `[0-7%l%-]` represents the octal digits plus the lowercase letters plus the '`-`' character. You can put a closing square bracket in a set by positioning it as the first character in the set. You can put a hyphen in a set by positioning it as the first or the last character in the set. (You can also use an escape for both cases.) The interaction between ranges and classes is not defined. Therefore, patterns like `[%a-z]` or `[a-%%]` have no meaning. **`[^*set*]`:** represents the complement of *set*, where *set* is interpreted as above.

For all classes represented by single letters (`%a`, `%c`, etc.), the corresponding uppercase letter represents the complement of the class. For instance, `%S` represents all non-space characters.

The definitions of letter, space, and other character groups depend on the current locale. In particular, the class `[a-z]` may not be equivalent to `%l`. Pattern Item:

A *pattern item* can be a single character class, which matches any single character in the class; a single character class followed by '`*`', which matches sequences of zero or more characters in the class. These repetition items will always match the longest possible sequence; a single character class followed by '`+`', which matches sequences of one or more characters in the class. These repetition items will always match the longest possible sequence; a single character class followed by '`-`', which also matches sequences of zero or more characters in the class. Unlike '`*`', these repetition items will always match the shortest possible sequence; a single character class followed by '`?`', which matches zero or one occurrence of a character in the class. It always matches one occurrence if possible; `%*n*`, for *n* between 1 and 9; such item matches a substring equal to the *n*-th captured string (see below); `%b*xy*`, where *x* and *y* are two distinct characters; such item matches strings that start with *x*, end with *y*, and where the *x* and *y* are *balanced*. This means that, if one reads the string from left to right, counting *+1* for an *x* and *-1* for a *y*, the ending *y* is the first *y* where the count reaches 0. For instance, the item `%b()` matches expressions with balanced parentheses. `%f[*set*]`, a *frontier pattern*; such item matches an empty string at any position such that the next character belongs to *set* and the previous character does not belong to *set*. The set *set* is interpreted as previously described. The beginning and the end of the subject are handled as if they were the character '`\0`'. Pattern:

A *pattern* is a sequence of pattern items. A caret '`^`' at the beginning of a pattern anchors the match at the beginning of the subject string. A '`$`' at the end of a pattern anchors the match at the end of the subject string. At other positions, '`^`' and '`$`' have no special meaning and represent themselves. Captures:

A pattern can contain sub-patterns enclosed in parentheses; they describe *captures*. When a match succeeds, the substrings of the subject string that match captures are stored (*captured*) for future use. Captures are numbered according to their left parentheses. For instance, in the pattern `"(a*(.)%w(%s*))"`, the part of the string matching `"a*(.)%w(%s*)"` is stored as the first capture, and therefore has number 1; the character matching "`.`" is captured with number 2, and the part matching "`%s*`" has number 3.

As a special case, the capture `()` captures the current string position (a number). For instance, if we apply the pattern `"()aa()"` on the string `"flaaap"`, there will be two captures: 3 and 5. Multiple matches:

The function `string.gsub` and the iterator `string.gmatch` match multiple occurrences of the given pattern in the subject. For these functions, a new match is considered valid only if it ends at least one byte after the end of the previous match. In other words, the pattern machine never accepts the empty string as a match immediately after another match. As an example, consider the results of the following code: > string.gsub("abc", "()a*()", print); --> 1 2 --> 3 3 --> 4 4

The second and third results come from Lua matching an empty string after '`b`' and another one after '`c`'. Lua does not match an empty string after '`a`', because it would end at the same position of the previous match. 6.4.2 – Format Strings for Pack and Unpack

The first argument to `string.pack`, `string.packsize`, and `string.unpack` is a format string, which describes the layout of the structure being created or read.

A format string is a sequence of conversion options. The conversion options are as follows: **`<`:**sets little endian **`>`:**sets big endian **`=`:**sets native endian **`![*n*]`:**sets maximum alignment to `n` (default is native alignment) **`b`:**a signed byte (`char`) **`B`:**an unsigned byte (`char`) **`h`:**a signed `short` (native size) **`H`:**an unsigned `short` (native size) **`l`:**a signed `long` (native size) **`L`:**an unsigned `long` (native size) **`j`:**a `lua_Integer` **`J`:**a `lua_Unsigned` **`T`:**a `size_t` (native size) **`i[*n*]`:**a signed `int` with `n` bytes (default is native size) **`I[*n*]`:**an unsigned `int` with `n` bytes (default is native size) **`f`:**a `float` (native size) **`d`:**a `double` (native size) **`n`:**a `lua_Number` **`c*n*`:**a fixed-sized string with `n` bytes **`z`:**a zero-terminated string **`s[*n*]`:**a string preceded by its length coded as an unsigned integer with `n` bytes (default is a `size_t`) **`x`:**one byte of padding **`X*op*`:**an empty item that aligns according to option `op` (which is otherwise ignored) **'':**(space) ignored

(A "`[*n*]`" means an optional integral numeral.) Except for padding, spaces, and configurations (options "`xX <=>!`"), each option corresponds to an argument in `string.pack` or a result in `string.unpack`.

For options "`!*n*`", "`s*n*`", "`i*n*`", and "`I*n*`", `n` can be any integer between 1 and 16. All integral options check overflows; `string.pack` checks whether the given value fits in the given size; `string.unpack` checks whether the read value fits in a Lua integer. For the unsigned options, Lua integers are treated as unsigned values too.

Any format string starts as if prefixed by "`!1=`", that is, with maximum alignment of 1 (no alignment) and native endianness.

Native endianness assumes that the whole system is either big or little endian. The packing functions will not emulate correctly the behavior of mixed-endian formats.

Alignment works as follows: For each option, the format gets extra padding until the data starts at an offset that is a multiple of the minimum between the option size and the maximum alignment; this minimum must be a power of 2. Options "`c`" and "`z`" are not aligned; option "`s`" follows the alignment of its starting integer.

All padding is filled with zeros by `string.pack` and ignored by `string.unpack`. 6.5 – UTF-8 Support

This library provides basic support for UTF-8 encoding. It provides all its functions inside the table `utf8`. This library does not provide any support for Unicode other than the handling of the encoding. Any operation that needs the meaning of a character, such as character classification, is outside its scope.

Unless stated otherwise, all functions that expect a byte position as a parameter assume that the given position is either the start of a byte sequence or one plus the length of the subject string. As in the string library, negative indices count from the end of the string.

Functions that create byte sequences accept all values up to `0x7FFFFFFF`, as defined in the original UTF-8 specification; that implies byte sequences of up to six bytes.

Functions that interpret byte sequences only accept valid sequences (well formed and not overlong). By default, they only accept byte sequences that result in valid Unicode code points, rejecting values greater than `10FFFF` and surrogates. A boolean argument `lax`, when available, lifts these checks, so that all values up to `0x7FFFFFFF` are accepted. (Not well formed and overlong sequences are still rejected.)

`utf8.char (···)`

Receives zero or more integers, converts each one to its corresponding UTF-8 byte sequence and returns a string with the concatenation of all these sequences.

`utf8.charpattern`

The pattern (a string, not a function) "`[\0-\x7F\xC2-\xFD][\x80-\xBF]*`" (see §6.4.1), which matches exactly one UTF-8 byte sequence, assuming that the subject is a valid UTF-8 string.

`utf8.codes (s [, lax])`

Returns values so that the construction for p, c in utf8.codes(s) do *body* end

will iterate over all UTF-8 characters in string `s`, with `p` being the position (in bytes) and `c` the code point of each character. It raises an error if it meets any invalid byte sequence.

`utf8.codepoint (s [, i [, j [, lax]]])`

Returns the code points (as integers) from all characters in `s` that start between byte position `i` and `j` (both included). The default for `i` is 1 and for `j` is `i`. It raises an error if it meets any invalid byte sequence.

`utf8.len (s [, i [, j [, lax]]])`

Returns the number of UTF-8 characters in string `s` that start between positions `i` and `j` (both inclusive). The default for `i` is 1 and for `j` is -1. If it finds any invalid byte sequence, returns **fail** plus the position of the first invalid byte.

`utf8.offset (s, n [, i])`

Returns the position (in bytes) where the encoding of the `n`-th character of `s` (counting from position `i`) starts. A negative `n` gets characters before position `i`. The default for `i` is 1 when `n` is non-negative and `#s + 1` otherwise, so that `utf8.offset(s, -n)` gets the offset of the `n`-th character from the end of the string. If the specified character is neither in the subject nor right after its end, the function returns **fail**.

As a special case, when `n` is 0 the function returns the start of the encoding of the character that contains the `i`-th byte of `s`.

This function assumes that `s` is a valid UTF-8 string. 6.6 – Table Manipulation

This library provides generic functions for table manipulation. It provides all its functions inside the table `table`.

Remember that, whenever an operation needs the length of a table, all caveats about the length operator apply (see §3.4.7). All functions ignore non-numeric keys in the tables given as arguments.

`table.concat (list [, sep [, i [, j]]])`

Given a list where all elements are strings or numbers, returns the string `list[i]..sep..list[i+1] ··· sep..list[j]`. The default value for `sep` is the empty string, the default for `i` is 1, and the default for `j` is `#list`. If `i` is greater than `j`, returns the empty string.

`table.insert (list, [pos,] value)`

Inserts element `value` at position `pos` in `list`, shifting up the elements `list[pos], list[pos+1], ···, list[#list]`. The default value for `pos` is `#list+1`, so that a call `table.insert(t,x)` inserts `x` at the end of the list `t`.

`table.move (a1, f, e, t [,a2])`

Moves elements from the table `a1` to the table `a2`, performing the equivalent to the following multiple assignment: `a2[t],··· = a1[f],···,a1[e]`. The default for `a2` is `a1`. The destination range can overlap with the source range. The number of elements to be moved must fit in a Lua integer.

Returns the destination table `a2`.

`table.pack (···)`

Returns a new table with all arguments stored into keys 1, 2, etc. and with a field "`n`" with the total number of arguments. Note that the resulting table may not be a sequence, if some arguments are **nil**.

`table.remove (list [, pos])`

Removes from `list` the element at position `pos`, returning the value of the removed element. When `pos` is an integer between 1 and `#list`, it shifts down the elements `list[pos+1], list[pos+2], ···, list[#list]` and erases element `list[#list]`; The index `pos` can also be 0 when `#list` is 0, or `#list + 1`.

The default value for `pos` is `#list`, so that a call `table.remove(l)` removes the last element of the list `l`.

`table.sort (list [, comp])`

Sorts the list elements in a given order, *in-place*, from `list[1]` to `list[#list]`. If `comp` is given, then it must be a function that receives two list elements and returns true when the first element must come before the second in the final order, so that, after the sort, `i <= j` implies `not comp(list[j],list[i])`. If `comp` is not given, then the standard Lua operator `<` is used instead.

The `comp` function must define a consistent order; more formally, the function must define a strict weak order. (A weak order is similar to a total order, but it can equate different elements for comparison purposes.)

The sort algorithm is not stable: Different elements considered equal by the given order may have their relative positions changed by the sort.

`table.unpack (list [, i [, j]])`

Returns the elements from the given list. This function is equivalent to return list[i], list[i+1], ···, list[j]

By default, `i` is 1 and `j` is `#list`. 6.7 – Mathematical Functions

This library provides basic mathematical functions. It provides all its functions and constants inside the table `math`. Functions with the annotation "`integer/float`" give integer results for integer arguments and float results for non-integer arguments. The rounding functions `math.ceil`, `math.floor`, and `math.modf` return an integer when the result fits in the range of an integer, or a float otherwise.

`math.abs (x)`

Returns the maximum value between `x` and `-x`. (integer/float)

`math.acos (x)`

Returns the arc cosine of `x` (in radians).

`math.asin (x)`

Returns the arc sine of `x` (in radians).

`math.atan (y [, x])`

Returns the arc tangent of `y/x` (in radians), using the signs of both arguments to find the quadrant of the result. It also handles correctly the case of `x` being zero.

The default value for `x` is 1, so that the call `math.atan(y)` returns the arc tangent of `y`.

`math.ceil (x)`

Returns the smallest integral value greater than or equal to `x`.

`math.cos (x)`

Returns the cosine of `x` (assumed to be in radians).

`math.deg (x)`

Converts the angle `x` from radians to degrees.

`math.exp (x)`

Returns the value *ex* (where `e` is the base of natural logarithms).

`math.floor (x)`

Returns the largest integral value less than or equal to `x`.

`math.fmod (x, y)`

Returns the remainder of the division of `x` by `y` that rounds the quotient towards zero. (integer/float)

`math.huge`

The float value `HUGE_VAL`, a value greater than any other numeric value.

`math.log (x [, base])`

Returns the logarithm of `x` in the given base. The default for `base` is *e* (so that the function returns the natural logarithm of `x`).

`math.max (x, ···)`

Returns the argument with the maximum value, according to the Lua operator `<`.

`math.maxinteger` An integer with the maximum value for an integer.

`math.min (x, ···)`

Returns the argument with the minimum value, according to the Lua operator `<`.

`math.mininteger` An integer with the minimum value for an integer.

`math.modf (x)`

Returns the integral part of `x` and the fractional part of `x`. Its second result is always a float.

`math.pi`

The value of *π*.

`math.rad (x)`

Converts the angle `x` from degrees to radians.

`math.random ([m [, n]])`

When called without arguments, returns a pseudo-random float with uniform distribution in the range *[0,1)*. When called with two integers `m` and `n`, `math.random` returns a pseudo-random integer with uniform distribution in the range *[m, n]*. The call `math.random(n)`, for a positive `n`, is equivalent to `math.random(1,n)`. The call `math.random(0)` produces an integer with all bits (pseudo)random.

This function uses the `xoshiro256**` algorithm to produce pseudo-random 64-bit integers, which are the results of calls with argument 0. Other results (ranges and floats) are unbiased extracted from these integers.

Lua initializes its pseudo-random generator with the equivalent of a call to `math.randomseed` with no arguments, so that `math.random` should generate different sequences of results each time the program runs.

`math.randomseed ([x [, y]])`

When called with at least one argument, the integer parameters `x` and `y` are joined into a 128-bit *seed* that is used to reinitialize the pseudo-random generator; equal seeds produce equal sequences of numbers. The default for `y` is zero.

When called with no arguments, Lua generates a seed with a weak attempt for randomness.

This function returns the two seed components that were effectively used, so that setting them again repeats the sequence.

To ensure a required level of randomness to the initial state (or contrarily, to have a deterministic sequence, for instance when debugging a program), you should call `math.randomseed` with explicit arguments.

`math.sin (x)`

Returns the sine of `x` (assumed to be in radians).

`math.sqrt (x)`

Returns the square root of `x`. (You can also use the expression `x^0.5` to compute this value.)

`math.tan (x)`

Returns the tangent of `x` (assumed to be in radians).

`math.tointeger (x)`

If the value `x` is convertible to an integer, returns that integer. Otherwise, returns **fail**.

`math.type (x)`

Returns "`integer`" if `x` is an integer, "`float`" if it is a float, or **fail** if `x` is not a number.

`math.ult (m, n)`

Returns a boolean, **true** if and only if integer `m` is below integer `n` when they are compared as unsigned integers. 6.8 – Input and Output Facilities

The I/O library provides two different styles for file manipulation. The first one uses implicit file handles; that is, there are operations to set a default input file and a default output file, and all input/output operations are done over these default files. The second style uses explicit file handles.

When using implicit file handles, all operations are supplied by table `io`. When using explicit file handles, the operation `io.open` returns a file handle and then all operations are supplied as methods of the file handle.

The metatable for file handles provides metamethods for `__gc` and `__close` that try to close the file when called.

The table `io` also provides three predefined file handles with their usual meanings from C: `io.stdin`, `io.stdout`, and `io.stderr`. The I/O library never closes these files.

Unless otherwise stated, all I/O functions return **fail** on failure, plus an error message as a second result and a system-dependent error code as a third result, and some non-false value on success. On non-POSIX systems, the computation of the error message and error code in case of errors may be not thread safe, because they rely on the global C variable `errno`.

`io.close ([file])`

Equivalent to `file:close()`. Without a `file`, closes the default output file.

`io.flush ()`

Equivalent to `io.output():flush()`.

`io.input ([file])`

When called with a file name, it opens the named file (in text mode), and sets its handle as the default input file. When called with a file handle, it simply sets this file handle as the default input file. When called without arguments, it returns the current default input file.

In case of errors this function raises the error, instead of returning an error code.

`io.lines ([filename, ···])`

Opens the given file name in read mode and returns an iterator function that works like `file:lines(···)` over the opened file. When the iterator function fails to read any value, it automatically closes the file. Besides the iterator function, `io.lines` returns three other values: two **nil** values as placeholders, plus the created file handle. Therefore, when used in a generic **for** loop, the file is closed also if the loop is interrupted by an error or a **break**.

The call `io.lines()` (with no file name) is equivalent to `io.input():lines("l")`; that is, it iterates over the lines of the default input file. In this case, the iterator does not close the file when the loop ends.

In case of errors opening the file, this function raises the error, instead of returning an error code.

`io.open (filename [, mode])`

This function opens a file, in the mode specified in the string `mode`. In case of success, it returns a new file handle.

The `mode` string can be any of the following: **"`r`":** read mode (the default); **"`w`":** write mode; **"`a`":** append mode; **"`r+`":** update mode, all previous data is preserved; **"`w+`":** update mode, all previous data is erased; **"`a+`":** append update mode, previous data is preserved, writing is only allowed at the end of file.

The `mode` string can also have a '`b`' at the end, which is needed in some systems to open the file in binary mode.

`io.output ([file])`

Similar to `io.input`, but operates over the default output file.

`io.popen (prog [, mode])`

This function is system dependent and is not available on all platforms.

Starts the program `prog` in a separated process and returns a file handle that you can use to read data from this program (if `mode` is `"r"`, the default) or to write data to this program (if `mode` is `"w"`).

`io.read (···)`

Equivalent to `io.input():read(···)`.

`io.tmpfile ()`

In case of success, returns a handle for a temporary file. This file is opened in update mode and it is automatically removed when the program ends.

`io.type (obj)`

Checks whether `obj` is a valid file handle. Returns the string `"file"` if `obj` is an open file handle, `"closed file"` if `obj` is a closed file handle, or **fail** if `obj` is not a file handle.

`io.write (···)`

Equivalent to `io.output():write(···)`.

`file:close ()`

Closes `file`. Note that files are automatically closed when their handles are garbage collected, but that takes an unpredictable amount of time to happen.

When closing a file handle created with `io.popen`, `file:close` returns the same values returned by `os.execute`.

`file:flush ()`

Saves any written data to `file`.

`file:lines (···)`

Returns an iterator function that, each time it is called, reads the file according to the given formats. When no format is given, uses "`l`" as a default. As an example, the construction for c in file:lines(1) do *body* end

will iterate over all characters of the file, starting at the current position. Unlike `io.lines`, this function does not close the file when the loop ends.

`file:read (···)`

Reads the file `file`, according to the given formats, which specify what to read. For each format, the function returns a string or a number with the characters read, or **fail** if it cannot read data with the specified format. (In this latter case, the function does not read subsequent formats.) When called without arguments, it uses a default format that reads the next line (see below).
