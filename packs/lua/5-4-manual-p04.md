---
title: "Lua 5.4 Reference Manual (part 4/6)"
source: https://www.lua.org/manual/5.4/manual.html
domain: lua
license: MIT / CC-BY-SA-4.0
tags: lua, lua scripting, lua manual, programming in lua
fetched: 2026-07-02
part: 4/6
---

# Lua 5.4 Reference Manual

The fields of `lua_Debug` have the following meaning: **`source`:** the source of the chunk that created the function. If `source` starts with a '`@`', it means that the function was defined in a file where the file name follows the '`@`'. If `source` starts with a '`=`', the remainder of its contents describes the source in a user-dependent manner. Otherwise, the function was defined in a string where `source` is that string. **`srclen`:** The length of the string `source`. **`short_src`:** a "printable" version of `source`, to be used in error messages. **`linedefined`:** the line number where the definition of the function starts. **`lastlinedefined`:** the line number where the definition of the function ends. **`what`:** the string `"Lua"` if the function is a Lua function, `"C"` if it is a C function, `"main"` if it is the main part of a chunk. **`currentline`:** the current line where the given function is executing. When no line information is available, `currentline` is set to -1. **`name`:** a reasonable name for the given function. Because functions in Lua are first-class values, they do not have a fixed name: some functions can be the value of multiple global variables, while others can be stored only in a table field. The `lua_getinfo` function checks how the function was called to find a suitable name. If it cannot find a name, then `name` is set to `NULL`. **`namewhat`:** explains the `name` field. The value of `namewhat` can be `"global"`, `"local"`, `"method"`, `"field"`, `"upvalue"`, or `""` (the empty string), according to how the function was called. (Lua uses the empty string when no other option seems to apply.) **`istailcall`:** true if this function invocation was called by a tail call. In this case, the caller of this level is not in the stack. **`nups`:** the number of upvalues of the function. **`nparams`:** the number of parameters of the function (always 0 for C functions). **`isvararg`:** true if the function is a variadic function (always true for C functions). **`ftransfer`:** the index in the stack of the first value being "transferred", that is, parameters in a call or return values in a return. (The other values are in consecutive indices.) Using this index, you can access and modify these values through `lua_getlocal` and `lua_setlocal`. This field is only meaningful during a call hook, denoting the first parameter, or a return hook, denoting the first value being returned. (For call hooks, this value is always 1.) **`ntransfer`:** The number of values being transferred (see previous item). (For calls of Lua functions, this value is always equal to `nparams`.) `lua_gethook`

[-0, +0, –] lua_Hook lua_gethook (lua_State *L);

Returns the current hook function. `lua_gethookcount`

[-0, +0, –] int lua_gethookcount (lua_State *L);

Returns the current hook count. `lua_gethookmask`

[-0, +0, –] int lua_gethookmask (lua_State *L);

Returns the current hook mask. `lua_getinfo`

[-(0|1), +(0|1|2), *m*] int lua_getinfo (lua_State *L, const char *what, lua_Debug *ar);

Gets information about a specific function or function invocation.

To get information about a function invocation, the parameter `ar` must be a valid activation record that was filled by a previous call to `lua_getstack` or given as argument to a hook (see `lua_Hook`).

To get information about a function, you push it onto the stack and start the `what` string with the character '`>`'. (In that case, `lua_getinfo` pops the function from the top of the stack.) For instance, to know in which line a function `f` was defined, you can write the following code: lua_Debug ar; lua_getglobal(L, "f"); /* get global 'f' */ lua_getinfo(L, ">S", &ar); printf("%d\n", ar.linedefined);

Each character in the string `what` selects some fields of the structure `ar` to be filled or a value to be pushed on the stack. (These characters are also documented in the declaration of the structure `lua_Debug`, between parentheses in the comments following each field.) **'`f`':** pushes onto the stack the function that is running at the given level; **'`l`':** fills in the field `currentline`; **'`n`':** fills in the fields `name` and `namewhat`; **'`r`':** fills in the fields `ftransfer` and `ntransfer`; **'`S`':** fills in the fields `source`, `short_src`, `linedefined`, `lastlinedefined`, and `what`; **'`t`':** fills in the field `istailcall`; **'`u`':** fills in the fields `nups`, `nparams`, and `isvararg`; **'`L`':** pushes onto the stack a table whose indices are the lines on the function with some associated code, that is, the lines where you can put a break point. (Lines with no code include empty lines and comments.) If this option is given together with option '`f`', its table is pushed after the function. This is the only option that can raise a memory error.

This function returns 0 to signal an invalid option in `what`; even then the valid options are handled correctly. `lua_getlocal`

[-0, +(0|1), –] const char *lua_getlocal (lua_State *L, const lua_Debug *ar, int n);

Gets information about a local variable or a temporary value of a given activation record or a given function.

In the first case, the parameter `ar` must be a valid activation record that was filled by a previous call to `lua_getstack` or given as argument to a hook (see `lua_Hook`). The index `n` selects which local variable to inspect; see `debug.getlocal` for details about variable indices and names.

`lua_getlocal` pushes the variable's value onto the stack and returns its name.

In the second case, `ar` must be `NULL` and the function to be inspected must be on the top of the stack. In this case, only parameters of Lua functions are visible (as there is no information about what variables are active) and no values are pushed onto the stack.

Returns `NULL` (and pushes nothing) when the index is greater than the number of active local variables. `lua_getstack`

[-0, +0, –] int lua_getstack (lua_State *L, int level, lua_Debug *ar);

Gets information about the interpreter runtime stack.

This function fills parts of a `lua_Debug` structure with an identification of the *activation record* of the function executing at a given level. Level 0 is the current running function, whereas level *n+1* is the function that has called level *n* (except for tail calls, which do not count in the stack). When called with a level greater than the stack depth, `lua_getstack` returns 0; otherwise it returns 1. `lua_getupvalue`

[-0, +(0|1), –] const char *lua_getupvalue (lua_State *L, int funcindex, int n);

Gets information about the `n`-th upvalue of the closure at index `funcindex`. It pushes the upvalue's value onto the stack and returns its name. Returns `NULL` (and pushes nothing) when the index `n` is greater than the number of upvalues.

See `debug.getupvalue` for more information about upvalues. `lua_Hook` typedef void (*lua_Hook) (lua_State *L, lua_Debug *ar);

Type for debugging hook functions.

Whenever a hook is called, its `ar` argument has its field `event` set to the specific event that triggered the hook. Lua identifies these events with the following constants: `LUA_HOOKCALL`, `LUA_HOOKRET`, `LUA_HOOKTAILCALL`, `LUA_HOOKLINE`, and `LUA_HOOKCOUNT`. Moreover, for line events, the field `currentline` is also set. To get the value of any other field in `ar`, the hook must call `lua_getinfo`.

For call events, `event` can be `LUA_HOOKCALL`, the normal value, or `LUA_HOOKTAILCALL`, for a tail call; in this case, there will be no corresponding return event.

While Lua is running a hook, it disables other calls to hooks. Therefore, if a hook calls back Lua to execute a function or a chunk, this execution occurs without any calls to hooks.

Hook functions cannot have continuations, that is, they cannot call `lua_yieldk`, `lua_pcallk`, or `lua_callk` with a non-null `k`.

Hook functions can yield under the following conditions: Only count and line events can yield; to yield, a hook function must finish its execution calling `lua_yield` with `nresults` equal to zero (that is, with no values). `lua_sethook`

[-0, +0, –] void lua_sethook (lua_State *L, lua_Hook f, int mask, int count);

Sets the debugging hook function.

Argument `f` is the hook function. `mask` specifies on which events the hook will be called: it is formed by a bitwise OR of the constants `LUA_MASKCALL`, `LUA_MASKRET`, `LUA_MASKLINE`, and `LUA_MASKCOUNT`. The `count` argument is only meaningful when the mask includes `LUA_MASKCOUNT`. For each event, the hook is called as explained below: **The call hook:** is called when the interpreter calls a function. The hook is called just after Lua enters the new function. **The return hook:** is called when the interpreter returns from a function. The hook is called just before Lua leaves the function. **The line hook:** is called when the interpreter is about to start the execution of a new line of code, or when it jumps back in the code (even to the same line). This event only happens while Lua is executing a Lua function. **The count hook:** is called after the interpreter executes every `count` instructions. This event only happens while Lua is executing a Lua function.

Hooks are disabled by setting `mask` to zero. `lua_setlocal`

[-(0|1), +0, –] const char *lua_setlocal (lua_State *L, const lua_Debug *ar, int n);

Sets the value of a local variable of a given activation record. It assigns the value on the top of the stack to the variable and returns its name. It also pops the value from the stack.

Returns `NULL` (and pops nothing) when the index is greater than the number of active local variables.

Parameters `ar` and `n` are as in the function `lua_getlocal`. `lua_setupvalue`

[-(0|1), +0, –] const char *lua_setupvalue (lua_State *L, int funcindex, int n);

Sets the value of a closure's upvalue. It assigns the value on the top of the stack to the upvalue and returns its name. It also pops the value from the stack.

Returns `NULL` (and pops nothing) when the index `n` is greater than the number of upvalues.

Parameters `funcindex` and `n` are as in the function `lua_getupvalue`. `lua_upvalueid`

[-0, +0, –] void *lua_upvalueid (lua_State *L, int funcindex, int n);

Returns a unique identifier for the upvalue numbered `n` from the closure at index `funcindex`.

These unique identifiers allow a program to check whether different closures share upvalues. Lua closures that share an upvalue (that is, that access a same external local variable) will return identical ids for those upvalue indices.

Parameters `funcindex` and `n` are as in the function `lua_getupvalue`, but `n` cannot be greater than the number of upvalues. `lua_upvaluejoin`

[-0, +0, –] void lua_upvaluejoin (lua_State *L, int funcindex1, int n1, int funcindex2, int n2);

Make the `n1`-th upvalue of the Lua closure at index `funcindex1` refer to the `n2`-th upvalue of the Lua closure at index `funcindex2`. 5 – The Auxiliary Library

The *auxiliary library* provides several convenient functions to interface C with Lua. While the basic API provides the primitive functions for all interactions between C and Lua, the auxiliary library provides higher-level functions for some common tasks.

All functions and types from the auxiliary library are defined in header file `lauxlib.h` and have a prefix `luaL_`.

All functions in the auxiliary library are built on top of the basic API, and so they provide nothing that cannot be done with that API. Nevertheless, the use of the auxiliary library ensures more consistency to your code.

Several functions in the auxiliary library use internally some extra stack slots. When a function in the auxiliary library uses less than five slots, it does not check the stack size; it simply assumes that there are enough slots.

Several functions in the auxiliary library are used to check C function arguments. Because the error message is formatted for arguments (e.g., "`bad argument #1`"), you should not use these functions for other stack values.

Functions called `luaL_check*` always raise an error if the check is not satisfied. 5.1 – Functions and Types

Here we list all functions and types from the auxiliary library in alphabetical order. `luaL_addchar`

[-?, +?, *m*] void luaL_addchar (luaL_Buffer *B, char c);

Adds the byte `c` to the buffer `B` (see `luaL_Buffer`). `luaL_addgsub`

[-?, +?, *m*] const void luaL_addgsub (luaL_Buffer *B, const char *s, const char *p, const char *r);

Adds a copy of the string `s` to the buffer `B` (see `luaL_Buffer`), replacing any occurrence of the string `p` with the string `r`. `luaL_addlstring`

[-?, +?, *m*] void luaL_addlstring (luaL_Buffer *B, const char *s, size_t l);

Adds the string pointed to by `s` with length `l` to the buffer `B` (see `luaL_Buffer`). The string can contain embedded zeros. `luaL_addsize`

[-?, +?, –] void luaL_addsize (luaL_Buffer *B, size_t n);

Adds to the buffer `B` a string of length `n` previously copied to the buffer area (see `luaL_prepbuffer`). `luaL_addstring`

[-?, +?, *m*] void luaL_addstring (luaL_Buffer *B, const char *s);

Adds the zero-terminated string pointed to by `s` to the buffer `B` (see `luaL_Buffer`). `luaL_addvalue`

[-?, +?, *m*] void luaL_addvalue (luaL_Buffer *B);

Adds the value on the top of the stack to the buffer `B` (see `luaL_Buffer`). Pops the value.

This is the only function on string buffers that can (and must) be called with an extra element on the stack, which is the value to be added to the buffer. `luaL_argcheck`

[-0, +0, *v*] void luaL_argcheck (lua_State *L, int cond, int arg, const char *extramsg);

Checks whether `cond` is true. If it is not, raises an error with a standard message (see `luaL_argerror`). `luaL_argerror`

[-0, +0, *v*] int luaL_argerror (lua_State *L, int arg, const char *extramsg);

Raises an error reporting a problem with argument `arg` of the C function that called it, using a standard message that includes `extramsg` as a comment: bad argument #*arg* to '*funcname*' (*extramsg*)

This function never returns. `luaL_argexpected`

[-0, +0, *v*] void luaL_argexpected (lua_State *L, int cond, int arg, const char *tname);

Checks whether `cond` is true. If it is not, raises an error about the type of the argument `arg` with a standard message (see `luaL_typeerror`). `luaL_Buffer` typedef struct luaL_Buffer luaL_Buffer;

Type for a *string buffer*.

A string buffer allows C code to build Lua strings piecemeal. Its pattern of use is as follows: First declare a variable `b` of type `luaL_Buffer`. Then initialize it with a call `luaL_buffinit(L, &b)`. Then add string pieces to the buffer calling any of the `luaL_add*` functions. Finish by calling `luaL_pushresult(&b)`. This call leaves the final string on the top of the stack.

If you know beforehand the maximum size of the resulting string, you can use the buffer like this: First declare a variable `b` of type `luaL_Buffer`. Then initialize it and preallocate a space of size `sz` with a call `luaL_buffinitsize(L, &b, sz)`. Then produce the string into that space. Finish by calling `luaL_pushresultsize(&b, sz)`, where `sz` is the total size of the resulting string copied into that space (which may be less than or equal to the preallocated size).

During its normal operation, a string buffer uses a variable number of stack slots. So, while using a buffer, you cannot assume that you know where the top of the stack is. You can use the stack between successive calls to buffer operations as long as that use is balanced; that is, when you call a buffer operation, the stack is at the same level it was immediately after the previous buffer operation. (The only exception to this rule is `luaL_addvalue`.) After calling `luaL_pushresult`, the stack is back to its level when the buffer was initialized, plus the final string on its top. `luaL_buffaddr`

[-0, +0, –] char *luaL_buffaddr (luaL_Buffer *B);

Returns the address of the current content of buffer `B` (see `luaL_Buffer`). Note that any addition to the buffer may invalidate this address. `luaL_buffinit`

[-0, +?, –] void luaL_buffinit (lua_State *L, luaL_Buffer *B);

Initializes a buffer `B` (see `luaL_Buffer`). This function does not allocate any space; the buffer must be declared as a variable. `luaL_bufflen`

[-0, +0, –] size_t luaL_bufflen (luaL_Buffer *B);

Returns the length of the current content of buffer `B` (see `luaL_Buffer`). `luaL_buffinitsize`

[-?, +?, *m*] char *luaL_buffinitsize (lua_State *L, luaL_Buffer *B, size_t sz);

Equivalent to the sequence `luaL_buffinit`, `luaL_prepbuffsize`. `luaL_buffsub`

[-?, +?, –] void luaL_buffsub (luaL_Buffer *B, int n);

Removes `n` bytes from the buffer `B` (see `luaL_Buffer`). The buffer must have at least that many bytes. `luaL_callmeta`

[-0, +(0|1), *e*] int luaL_callmeta (lua_State *L, int obj, const char *e);

Calls a metamethod.

If the object at index `obj` has a metatable and this metatable has a field `e`, this function calls this field passing the object as its only argument. In this case this function returns true and pushes onto the stack the value returned by the call. If there is no metatable or no metamethod, this function returns false without pushing any value on the stack. `luaL_checkany`

[-0, +0, *v*] void luaL_checkany (lua_State *L, int arg);

Checks whether the function has an argument of any type (including **nil**) at position `arg`. `luaL_checkinteger`

[-0, +0, *v*] lua_Integer luaL_checkinteger (lua_State *L, int arg);

Checks whether the function argument `arg` is an integer (or can be converted to an integer) and returns this integer. `luaL_checklstring`

[-0, +0, *v*] const char *luaL_checklstring (lua_State *L, int arg, size_t *l);

Checks whether the function argument `arg` is a string and returns this string; if `l` is not `NULL` fills its referent with the string's length.

This function uses `lua_tolstring` to get its result, so all conversions and caveats of that function apply here. `luaL_checknumber`

[-0, +0, *v*] lua_Number luaL_checknumber (lua_State *L, int arg);

Checks whether the function argument `arg` is a number and returns this number converted to a `lua_Number`. `luaL_checkoption`

[-0, +0, *v*] int luaL_checkoption (lua_State *L, int arg, const char *def, const char *const lst[]);

Checks whether the function argument `arg` is a string and searches for this string in the array `lst` (which must be NULL-terminated). Returns the index in the array where the string was found. Raises an error if the argument is not a string or if the string cannot be found.

If `def` is not `NULL`, the function uses `def` as a default value when there is no argument `arg` or when this argument is **nil**.

This is a useful function for mapping strings to C enums. (The usual convention in Lua libraries is to use strings instead of numbers to select options.) `luaL_checkstack`

[-0, +0, *v*] void luaL_checkstack (lua_State *L, int sz, const char *msg);

Grows the stack size to `top + sz` elements, raising an error if the stack cannot grow to that size. `msg` is an additional text to go into the error message (or `NULL` for no additional text). `luaL_checkstring`

[-0, +0, *v*] const char *luaL_checkstring (lua_State *L, int arg);

Checks whether the function argument `arg` is a string and returns this string.

This function uses `lua_tolstring` to get its result, so all conversions and caveats of that function apply here. `luaL_checktype`

[-0, +0, *v*] void luaL_checktype (lua_State *L, int arg, int t);

Checks whether the function argument `arg` has type `t`. See `lua_type` for the encoding of types for `t`. `luaL_checkudata`

[-0, +0, *v*] void *luaL_checkudata (lua_State *L, int arg, const char *tname);

Checks whether the function argument `arg` is a userdata of the type `tname` (see `luaL_newmetatable`) and returns the userdata's memory-block address (see `lua_touserdata`). `luaL_checkversion`

[-0, +0, *v*] void luaL_checkversion (lua_State *L);

Checks whether the code making the call and the Lua library being called are using the same version of Lua and the same numeric types. `luaL_dofile`

[-0, +?, *m*] int luaL_dofile (lua_State *L, const char *filename);

Loads and runs the given file. It is defined as the following macro: (luaL_loadfile(L, filename) || lua_pcall(L, 0, LUA_MULTRET, 0))

It returns 0 (`LUA_OK`) if there are no errors, or 1 in case of errors. `luaL_dostring`

[-0, +?, –] int luaL_dostring (lua_State *L, const char *str);

Loads and runs the given string. It is defined as the following macro: (luaL_loadstring(L, str) || lua_pcall(L, 0, LUA_MULTRET, 0))

It returns 0 (`LUA_OK`) if there are no errors, or 1 in case of errors. `luaL_error`

[-0, +0, *v*] int luaL_error (lua_State *L, const char *fmt, ...);

Raises an error. The error message format is given by `fmt` plus any extra arguments, following the same rules of `lua_pushfstring`. It also adds at the beginning of the message the file name and the line number where the error occurred, if this information is available.

This function never returns, but it is an idiom to use it in C functions as `return luaL_error(*args*)`. `luaL_execresult`

[-0, +3, *m*] int luaL_execresult (lua_State *L, int stat);

This function produces the return values for process-related functions in the standard library (`os.execute` and `io.close`). `luaL_fileresult`

[-0, +(1|3), *m*] int luaL_fileresult (lua_State *L, int stat, const char *fname);

This function produces the return values for file-related functions in the standard library (`io.open`, `os.rename`, `file:seek`, etc.). `luaL_getmetafield`

[-0, +(0|1), *m*] int luaL_getmetafield (lua_State *L, int obj, const char *e);

Pushes onto the stack the field `e` from the metatable of the object at index `obj` and returns the type of the pushed value. If the object does not have a metatable, or if the metatable does not have this field, pushes nothing and returns `LUA_TNIL`. `luaL_getmetatable`

[-0, +1, *m*] int luaL_getmetatable (lua_State *L, const char *tname);

Pushes onto the stack the metatable associated with the name `tname` in the registry (see `luaL_newmetatable`), or **nil** if there is no metatable associated with that name. Returns the type of the pushed value. `luaL_getsubtable`

[-0, +1, *e*] int luaL_getsubtable (lua_State *L, int idx, const char *fname);

Ensures that the value `t[fname]`, where `t` is the value at index `idx`, is a table, and pushes that table onto the stack. Returns true if it finds a previous table there and false if it creates a new table. `luaL_gsub`

[-0, +1, *m*] const char *luaL_gsub (lua_State *L, const char *s, const char *p, const char *r);

Creates a copy of string `s`, replacing any occurrence of the string `p` with the string `r`. Pushes the resulting string on the stack and returns it. `luaL_len`

[-0, +0, *e*] lua_Integer luaL_len (lua_State *L, int index);

Returns the "length" of the value at the given index as a number; it is equivalent to the '`#`' operator in Lua (see §3.4.7). Raises an error if the result of the operation is not an integer. (This case can only happen through metamethods.) `luaL_loadbuffer`

[-0, +1, –] int luaL_loadbuffer (lua_State *L, const char *buff, size_t sz, const char *name);

Equivalent to `luaL_loadbufferx` with `mode` equal to `NULL`. `luaL_loadbufferx`

[-0, +1, –] int luaL_loadbufferx (lua_State *L, const char *buff, size_t sz, const char *name, const char *mode);

Loads a buffer as a Lua chunk. This function uses `lua_load` to load the chunk in the buffer pointed to by `buff` with size `sz`.

This function returns the same results as `lua_load`. `name` is the chunk name, used for debug information and error messages. The string `mode` works as in the function `lua_load`. `luaL_loadfile`

[-0, +1, *m*] int luaL_loadfile (lua_State *L, const char *filename);

Equivalent to `luaL_loadfilex` with `mode` equal to `NULL`. `luaL_loadfilex`

[-0, +1, *m*] int luaL_loadfilex (lua_State *L, const char *filename, const char *mode);

Loads a file as a Lua chunk. This function uses `lua_load` to load the chunk in the file named `filename`. If `filename` is `NULL`, then it loads from the standard input. The first line in the file is ignored if it starts with a `#`.

The string `mode` works as in the function `lua_load`.

This function returns the same results as `lua_load` or `LUA_ERRFILE` for file-related errors.

As `lua_load`, this function only loads the chunk; it does not run it. `luaL_loadstring`

[-0, +1, –] int luaL_loadstring (lua_State *L, const char *s);

Loads a string as a Lua chunk. This function uses `lua_load` to load the chunk in the zero-terminated string `s`.

This function returns the same results as `lua_load`.

Also as `lua_load`, this function only loads the chunk; it does not run it. `luaL_newlib`

[-0, +1, *m*] void luaL_newlib (lua_State *L, const luaL_Reg l[]);

Creates a new table and registers there the functions in the list `l`.

It is implemented as the following macro: (luaL_newlibtable(L,l), luaL_setfuncs(L,l,0))

The array `l` must be the actual array, not a pointer to it. `luaL_newlibtable`

[-0, +1, *m*] void luaL_newlibtable (lua_State *L, const luaL_Reg l[]);

Creates a new table with a size optimized to store all entries in the array `l` (but does not actually store them). It is intended to be used in conjunction with `luaL_setfuncs` (see `luaL_newlib`).

It is implemented as a macro. The array `l` must be the actual array, not a pointer to it. `luaL_newmetatable`

[-0, +1, *m*] int luaL_newmetatable (lua_State *L, const char *tname);

If the registry already has the key `tname`, returns 0. Otherwise, creates a new table to be used as a metatable for userdata, adds to this new table the pair `__name = tname`, adds to the registry the pair `[tname] = new table`, and returns 1.

In both cases, the function pushes onto the stack the final value associated with `tname` in the registry. `luaL_newstate`

[-0, +0, –] lua_State *luaL_newstate (void);

Creates a new Lua state. It calls `lua_newstate` with an allocator based on the ISO C allocation functions and then sets a warning function and a panic function (see §4.4) that print messages to the standard error output.

Returns the new state, or `NULL` if there is a memory allocation error. `luaL_openlibs`

[-0, +0, *e*] void luaL_openlibs (lua_State *L);

Opens all standard Lua libraries into the given state. `luaL_opt`

[-0, +0, –] T luaL_opt (L, func, arg, dflt);

This macro is defined as follows: (lua_isnoneornil(L,(arg)) ? (dflt) : func(L,(arg)))

In words, if the argument `arg` is nil or absent, the macro results in the default `dflt`. Otherwise, it results in the result of calling `func` with the state `L` and the argument index `arg` as arguments. Note that it evaluates the expression `dflt` only if needed. `luaL_optinteger`

[-0, +0, *v*] lua_Integer luaL_optinteger (lua_State *L, int arg, lua_Integer d);

If the function argument `arg` is an integer (or it is convertible to an integer), returns this integer. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error. `luaL_optlstring`

[-0, +0, *v*] const char *luaL_optlstring (lua_State *L, int arg, const char *d, size_t *l);

If the function argument `arg` is a string, returns this string. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error.

If `l` is not `NULL`, fills its referent with the result's length. If the result is `NULL` (only possible when returning `d` and `d == NULL`), its length is considered zero.

This function uses `lua_tolstring` to get its result, so all conversions and caveats of that function apply here. `luaL_optnumber`

[-0, +0, *v*] lua_Number luaL_optnumber (lua_State *L, int arg, lua_Number d);

If the function argument `arg` is a number, returns this number as a `lua_Number`. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error. `luaL_optstring`

[-0, +0, *v*] const char *luaL_optstring (lua_State *L, int arg, const char *d);

If the function argument `arg` is a string, returns this string. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error. `luaL_prepbuffer`

[-?, +?, *m*] char *luaL_prepbuffer (luaL_Buffer *B);

Equivalent to `luaL_prepbuffsize` with the predefined size `LUAL_BUFFERSIZE`. `luaL_prepbuffsize`

[-?, +?, *m*] char *luaL_prepbuffsize (luaL_Buffer *B, size_t sz);

Returns an address to a space of size `sz` where you can copy a string to be added to buffer `B` (see `luaL_Buffer`). After copying the string into this space you must call `luaL_addsize` with the size of the string to actually add it to the buffer. `luaL_pushfail`

[-0, +1, –] void luaL_pushfail (lua_State *L);

Pushes the **fail** value onto the stack (see §6). `luaL_pushresult`

[-?, +1, *m*] void luaL_pushresult (luaL_Buffer *B);

Finishes the use of buffer `B` leaving the final string on the top of the stack. `luaL_pushresultsize`

[-?, +1, *m*] void luaL_pushresultsize (luaL_Buffer *B, size_t sz);

Equivalent to the sequence `luaL_addsize`, `luaL_pushresult`. `luaL_ref`

[-1, +0, *m*] int luaL_ref (lua_State *L, int t);

Creates and returns a *reference*, in the table at index `t`, for the object on the top of the stack (and pops the object).

A reference is a unique integer key. As long as you do not manually add integer keys into the table `t`, `luaL_ref` ensures the uniqueness of the key it returns. You can retrieve an object referred by the reference `r` by calling `lua_rawgeti(L, t, r)`. The function `luaL_unref` frees a reference.

If the object on the top of the stack is **nil**, `luaL_ref` returns the constant `LUA_REFNIL`. The constant `LUA_NOREF` is guaranteed to be different from any reference returned by `luaL_ref`. `luaL_Reg` typedef struct luaL_Reg { const char *name; lua_CFunction func; } luaL_Reg;

Type for arrays of functions to be registered by `luaL_setfuncs`. `name` is the function name and `func` is a pointer to the function. Any array of `luaL_Reg` must end with a sentinel entry in which both `name` and `func` are `NULL`. `luaL_requiref`

[-0, +1, *e*] void luaL_requiref (lua_State *L, const char *modname, lua_CFunction openf, int glb);

If `package.loaded[modname]` is not true, calls the function `openf` with the string `modname` as an argument and sets the call result to `package.loaded[modname]`, as if that function has been called through `require`.

If `glb` is true, also stores the module into the global `modname`.

Leaves a copy of the module on the stack. `luaL_setfuncs`

[-nup, +0, *m*] void luaL_setfuncs (lua_State *L, const luaL_Reg *l, int nup);

Registers all functions in the array `l` (see `luaL_Reg`) into the table on the top of the stack (below optional upvalues, see next).

When `nup` is not zero, all functions are created with `nup` upvalues, initialized with copies of the `nup` values previously pushed on the stack on top of the library table. These values are popped from the stack after the registration.

A function with a `NULL` value represents a placeholder, which is filled with **false**. `luaL_setmetatable`

[-0, +0, –] void luaL_setmetatable (lua_State *L, const char *tname);

Sets the metatable of the object on the top of the stack as the metatable associated with name `tname` in the registry (see `luaL_newmetatable`). `luaL_Stream` typedef struct luaL_Stream { FILE *f; lua_CFunction closef; } luaL_Stream;

The standard representation for file handles used by the standard I/O library.

A file handle is implemented as a full userdata, with a metatable called `LUA_FILEHANDLE` (where `LUA_FILEHANDLE` is a macro with the actual metatable's name). The metatable is created by the I/O library (see `luaL_newmetatable`).

This userdata must start with the structure `luaL_Stream`; it can contain other data after this initial structure. The field `f` points to the corresponding C stream (or it can be `NULL` to indicate an incompletely created handle). The field `closef` points to a Lua function that will be called to close the stream when the handle is closed or collected; this function receives the file handle as its sole argument and must return either a true value, in case of success, or a false value plus an error message, in case of error. Once Lua calls this field, it changes the field value to `NULL` to signal that the handle is closed. `luaL_testudata`

[-0, +0, *m*] void *luaL_testudata (lua_State *L, int arg, const char *tname);

This function works like `luaL_checkudata`, except that, when the test fails, it returns `NULL` instead of raising an error. `luaL_tolstring`

[-0, +1, *e*] const char *luaL_tolstring (lua_State *L, int idx, size_t *len);

Converts any Lua value at the given index to a C string in a reasonable format. The resulting string is pushed onto the stack and also returned by the function (see §4.1.3). If `len` is not `NULL`, the function also sets `*len` with the string length.

If the value has a metatable with a `__tostring` field, then `luaL_tolstring` calls the corresponding metamethod with the value as argument, and uses the result of the call as its result. `luaL_traceback`

[-0, +1, *m*] void luaL_traceback (lua_State *L, lua_State *L1, const char *msg, int level);

Creates and pushes a traceback of the stack `L1`. If `msg` is not `NULL`, it is appended at the beginning of the traceback. The `level` parameter tells at which level to start the traceback. `luaL_typeerror`

[-0, +0, *v*] int luaL_typeerror (lua_State *L, int arg, const char *tname);

Raises a type error for the argument `arg` of the C function that called it, using a standard message; `tname` is a "name" for the expected type. This function never returns. `luaL_typename`

[-0, +0, –] const char *luaL_typename (lua_State *L, int index);

Returns the name of the type of the value at the given index. `luaL_unref`

[-0, +0, –] void luaL_unref (lua_State *L, int t, int ref);

Releases the reference `ref` from the table at index `t` (see `luaL_ref`). The entry is removed from the table, so that the referred object can be collected. The reference `ref` is also freed to be used again.

If `ref` is `LUA_NOREF` or `LUA_REFNIL`, `luaL_unref` does nothing. `luaL_where`

[-0, +1, *m*] void luaL_where (lua_State *L, int lvl);

Pushes onto the stack a string identifying the current position of the control at level `lvl` in the call stack. Typically this string has the following format: *chunkname*:*currentline*:

Level 0 is the running function, level 1 is the function that called the running function, etc.

This function is used to build a prefix for error messages. 6 – The Standard Libraries

The standard Lua libraries provide useful functions that are implemented in C through the C API. Some of these functions provide essential services to the language (e.g., `type` and `getmetatable`); others provide access to outside services (e.g., I/O); and others could be implemented in Lua itself, but that for different reasons deserve an implementation in C (e.g., `table.sort`).

All libraries are implemented through the official C API and are provided as separate C modules. Unless otherwise noted, these library functions do not adjust its number of arguments to its expected parameters. For instance, a function documented as `foo(arg)` should not be called without an argument.

The notation **fail** means a false value representing some kind of failure. (Currently, **fail** is equal to **nil**, but that may change in future versions. The recommendation is to always test the success of these functions with `(not status)`, instead of `(status == nil)`.)

Currently, Lua has the following standard libraries: basic library (§6.1); coroutine library (§6.2); package library (§6.3); string manipulation (§6.4); basic UTF-8 support (§6.5); table manipulation (§6.6); mathematical functions (§6.7) (sin, log, etc.); input and output (§6.8); operating system facilities (§6.9); debug facilities (§6.10).

Except for the basic and the package libraries, each library provides all its functions as fields of a global table or as methods of its objects.

To have access to these libraries, the C host program should call the `luaL_openlibs` function, which opens all standard libraries. Alternatively, the host program can open them individually by using `luaL_requiref` to call `luaopen_base` (for the basic library), `luaopen_package` (for the package library), `luaopen_coroutine` (for the coroutine library), `luaopen_string` (for the string library), `luaopen_utf8` (for the UTF-8 library), `luaopen_table` (for the table library), `luaopen_math` (for the mathematical library), `luaopen_io` (for the I/O library), `luaopen_os` (for the operating system library), and `luaopen_debug` (for the debug library). These functions are declared in `lualib.h`. 6.1 – Basic Functions

The basic library provides core functions to Lua. If you do not include this library in your application, you should check carefully whether you need to provide implementations for some of its facilities.

`assert (v [, message])`

Raises an error if the value of its argument `v` is false (i.e., **nil** or **false**); otherwise, returns all its arguments. In case of error, `message` is the error object; when absent, it defaults to "`assertion failed!`"

`collectgarbage ([opt [, arg]])`

This function is a generic interface to the garbage collector. It performs different functions according to its first argument, `opt`: **"`collect`":** Performs a full garbage-collection cycle. This is the default option. **"`stop`":** Stops automatic execution of the garbage collector. The collector will run only when explicitly invoked, until a call to restart it. **"`restart`":** Restarts automatic execution of the garbage collector. **"`count`":** Returns the total memory in use by Lua in Kbytes. The value has a fractional part, so that it multiplied by 1024 gives the exact number of bytes in use by Lua. **"`step`":** Performs a garbage-collection step. The step "size" is controlled by `arg`. With a zero value, the collector will perform one basic (indivisible) step. For non-zero values, the collector will perform as if that amount of memory (in Kbytes) had been allocated by Lua. Returns **true** if the step finished a collection cycle. **"`isrunning`":** Returns a boolean that tells whether the collector is running (i.e., not stopped). **"`incremental`":** Change the collector mode to incremental. This option can be followed by three numbers: the garbage-collector pause, the step multiplier, and the step size (see §2.5.1). A zero means to not change that value. **"`generational`":** Change the collector mode to generational. This option can be followed by two numbers: the garbage-collector minor multiplier and the major multiplier (see §2.5.2). A zero means to not change that value.

See §2.5 for more details about garbage collection and some of these options.

This function should not be called by a finalizer.

`dofile ([filename])` Opens the named file and executes its content as a Lua chunk. When called without arguments, `dofile` executes the content of the standard input (`stdin`). Returns all values returned by the chunk. In case of errors, `dofile` propagates the error to its caller. (That is, `dofile` does not run in protected mode.)

`error (message [, level])` Raises an error (see §2.3) with `message` as the error object. This function never returns.

Usually, `error` adds some information about the error position at the beginning of the message, if the message is a string. The `level` argument specifies how to get the error position. With level 1 (the default), the error position is where the `error` function was called. Level 2 points the error to where the function that called `error` was called; and so on. Passing a level 0 avoids the addition of error position information to the message.

`_G` A global variable (not a function) that holds the global environment (see §2.2). Lua itself does not use this variable; changing its value does not affect any environment, nor vice versa.

`getmetatable (object)`

If `object` does not have a metatable, returns **nil**. Otherwise, if the object's metatable has a `__metatable` field, returns the associated value. Otherwise, returns the metatable of the given object.

`ipairs (t)`

Returns three values (an iterator function, the table `t`, and 0) so that the construction for i,v in ipairs(t) do *body* end

will iterate over the key–value pairs (`1,t[1]`), (`2,t[2]`), ..., up to the first absent index.

`load (chunk [, chunkname [, mode [, env]]])`

Loads a chunk.

If `chunk` is a string, the chunk is this string. If `chunk` is a function, `load` calls it repeatedly to get the chunk pieces. Each call to `chunk` must return a string that concatenates with previous results. A return of an empty string, **nil**, or no value signals the end of the chunk.

If there are no syntactic errors, `load` returns the compiled chunk as a function; otherwise, it returns **fail** plus the error message.

When you load a main chunk, the resulting function will always have exactly one upvalue, the `_ENV` variable (see §2.2). However, when you load a binary chunk created from a function (see `string.dump`), the resulting function can have an arbitrary number of upvalues, and there is no guarantee that its first upvalue will be the `_ENV` variable. (A non-main function may not even have an `_ENV` upvalue.)

Regardless, if the resulting function has any upvalues, its first upvalue is set to the value of `env`, if that parameter is given, or to the value of the global environment. Other upvalues are initialized with **nil**. All upvalues are fresh, that is, they are not shared with any other function.

`chunkname` is used as the name of the chunk for error messages and debug information (see §4.7). When absent, it defaults to `chunk`, if `chunk` is a string, or to "`=(load)`" otherwise.

The string `mode` controls whether the chunk can be text or binary (that is, a precompiled chunk). It may be the string "`b`" (only binary chunks), "`t`" (only text chunks), or "`bt`" (both binary and text). The default is "`bt`".

It is safe to load malformed binary chunks; `load` signals an appropriate error. However, Lua does not check the consistency of the code inside binary chunks; running maliciously crafted bytecode can crash the interpreter.

`loadfile ([filename [, mode [, env]]])`

Similar to `load`, but gets the chunk from file `filename` or from the standard input, if no file name is given.

`next (table [, index])`

Allows a program to traverse all fields of a table. Its first argument is a table and its second argument is an index in this table. A call to `next` returns the next index of the table and its associated value. When called with **nil** as its second argument, `next` returns an initial index and its associated value. When called with the last index, or with **nil** in an empty table, `next` returns **nil**. If the second argument is absent, then it is interpreted as **nil**. In particular, you can use `next(t)` to check whether a table is empty.

The order in which the indices are enumerated is not specified, *even for numeric indices*. (To traverse a table in numerical order, use a numerical **for**.)

You should not assign any value to a non-existent field in a table during its traversal. You may however modify existing fields. In particular, you may set existing fields to nil.

`pairs (t)`

If `t` has a metamethod `__pairs`, calls it with `t` as argument and returns the first three results from the call.

Otherwise, returns three values: the `next` function, the table `t`, and **nil**, so that the construction for k,v in pairs(t) do *body* end

will iterate over all key–value pairs of table `t`.

See function `next` for the caveats of modifying the table during its traversal.

`pcall (f [, arg1, ···])`

Calls the function `f` with the given arguments in *protected mode*. This means that any error inside `f` is not propagated; instead, `pcall` catches the error and returns a status code. Its first result is the status code (a boolean), which is **true** if the call succeeds without errors. In such case, `pcall` also returns all results from the call, after this first result. In case of any error, `pcall` returns **false** plus the error object. Note that errors caught by `pcall` do not call a message handler.

`print (···)` Receives any number of arguments and prints their values to `stdout`, converting each argument to a string following the same rules of `tostring`.

The function `print` is not intended for formatted output, but only as a quick way to show a value, for instance for debugging. For complete control over the output, use `string.format` and `io.write`.

`rawequal (v1, v2)` Checks whether `v1` is equal to `v2`, without invoking the `__eq` metamethod. Returns a boolean.

`rawget (table, index)` Gets the real value of `table[index]`, without using the `__index` metavalue. `table` must be a table; `index` may be any value.

`rawlen (v)` Returns the length of the object `v`, which must be a table or a string, without invoking the `__len` metamethod. Returns an integer.

`rawset (table, index, value)` Sets the real value of `table[index]` to `value`, without using the `__newindex` metavalue. `table` must be a table, `index` any value different from **nil** and NaN, and `value` any Lua value.

This function returns `table`.

`select (index, ···)`

If `index` is a number, returns all arguments after argument number `index`; a negative number indexes from the end (-1 is the last argument). Otherwise, `index` must be the string `"#"`, and `select` returns the total number of extra arguments it received.

`setmetatable (table, metatable)`

Sets the metatable for the given table. If `metatable` is **nil**, removes the metatable of the given table. If the original metatable has a `__metatable` field, raises an error.

This function returns `table`.

To change the metatable of other types from Lua code, you must use the debug library (§6.10).

`tonumber (e [, base])`

When called with no `base`, `tonumber` tries to convert its argument to a number. If the argument is already a number or a string convertible to a number, then `tonumber` returns this number; otherwise, it returns **fail**.

The conversion of strings can result in integers or floats, according to the lexical conventions of Lua (see §3.1). The string may have leading and trailing spaces and a sign.

When called with `base`, then `e` must be a string to be interpreted as an integer numeral in that base. The base may be any integer between 2 and 36, inclusive. In bases above 10, the letter '`A`' (in either upper or lower case) represents 10, '`B`' represents 11, and so forth, with '`Z`' representing 35. If the string `e` is not a valid numeral in the given base, the function returns **fail**.

`tostring (v)`

Receives a value of any type and converts it to a string in a human-readable format.

If the metatable of `v` has a `__tostring` field, then `tostring` calls the corresponding value with `v` as argument, and uses the result of the call as its result. Otherwise, if the metatable of `v` has a `__name` field with a string value, `tostring` may use that string in its final result.

For complete control of how numbers are converted, use `string.format`.

`type (v)`

Returns the type of its only argument, coded as a string. The possible results of this function are "`nil`" (a string, not the value **nil**), "`number`", "`string`", "`boolean`", "`table`", "`function`", "`thread`", and "`userdata`".

`_VERSION`

A global variable (not a function) that holds a string containing the running Lua version. The current value of this variable is "`Lua 5.4`".

`warn (msg1, ···)`
