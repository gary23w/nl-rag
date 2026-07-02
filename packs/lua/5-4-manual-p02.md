---
title: "Lua 5.4 Reference Manual (part 2/6)"
source: https://www.lua.org/manual/5.4/manual.html
domain: lua
license: MIT / CC-BY-SA-4.0
tags: lua, lua scripting, lua manual, programming in lua
fetched: 2026-07-02
part: 2/6
---

# Lua 5.4 Reference Manual

The loop starts by evaluating once the three control expressions. Their values are called respectively the *initial value*, the *limit*, and the *step*. If the step is absent, it defaults to 1.

If both the initial value and the step are integers, the loop is done with integers; note that the limit may not be an integer. Otherwise, the three values are converted to floats and the loop is done with floats. Beware of floating-point accuracy in this case.

After that initialization, the loop body is repeated with the value of the control variable going through an arithmetic progression, starting at the initial value, with a common difference given by the step. A negative step makes a decreasing sequence; a step equal to zero raises an error. The loop continues while the value is less than or equal to the limit (greater than or equal to for a negative step). If the initial value is already greater than the limit (or less than, if the step is negative), the body is not executed.

For integer loops, the control variable never wraps around; instead, the loop ends in case of an overflow.

You should not change the value of the control variable during the loop. If you need its value after the loop, assign it to another variable before exiting the loop. The generic **for** loop

The generic **for** statement works over functions, called *iterators*. On each iteration, the iterator function is called to produce a new value, stopping when this new value is **nil**. The generic **for** loop has the following syntax: stat ::= **for** namelist **in** explist **do** block **end** namelist ::= Name {‘**,**’ Name}

A **for** statement like for *var_1*, ···, *var_n* in *explist* do *body* end

works as follows.

The names *var_i* declare loop variables local to the loop body. The first of these variables is the *control variable*.

The loop starts by evaluating *explist* to produce four values: an *iterator function*, a *state*, an initial value for the control variable, and a *closing value*.

Then, at each iteration, Lua calls the iterator function with two arguments: the state and the control variable. The results from this call are then assigned to the loop variables, following the rules of multiple assignments (see §3.3.3). If the control variable becomes **nil**, the loop terminates. Otherwise, the body is executed and the loop goes to the next iteration.

The closing value behaves like a to-be-closed variable (see §3.3.8), which can be used to release resources when the loop ends. Otherwise, it does not interfere with the loop.

You should not change the value of the control variable during the loop. 3.3.6 – Function Calls as Statements

To allow possible side-effects, function calls can be executed as statements: stat ::= functioncall

In this case, all returned values are thrown away. Function calls are explained in §3.4.10. 3.3.7 – Local Declarations

Local variables can be declared anywhere inside a block. The declaration can include an initialization: stat ::= **local** attnamelist [‘**=**’ explist] attnamelist ::= Name attrib {‘**,**’ Name attrib}

If present, an initial assignment has the same semantics of a multiple assignment (see §3.3.3). Otherwise, all variables are initialized with **nil**.

Each variable name may be postfixed by an attribute (a name between angle brackets): attrib ::= [‘**<**’ Name ‘**>**’]

There are two possible attributes: `const`, which declares a constant variable, that is, a variable that cannot be assigned to after its initialization; and `close`, which declares a to-be-closed variable (see §3.3.8). A list of variables can contain at most one to-be-closed variable.

A chunk is also a block (see §3.3.2), and so local variables can be declared in a chunk outside any explicit block.

The visibility rules for local variables are explained in §3.5. 3.3.8 – To-be-closed Variables

A to-be-closed variable behaves like a constant local variable, except that its value is *closed* whenever the variable goes out of scope, including normal block termination, exiting its block by **break**/**goto**/**return**, or exiting by an error.

Here, to *close* a value means to call its `__close` metamethod. When calling the metamethod, the value itself is passed as the first argument and the error object that caused the exit (if any) is passed as a second argument; if there was no error, the second argument is **nil**.

The value assigned to a to-be-closed variable must have a `__close` metamethod or be a false value. (**nil** and **false** are ignored as to-be-closed values.)

If several to-be-closed variables go out of scope at the same event, they are closed in the reverse order that they were declared.

If there is any error while running a closing method, that error is handled like an error in the regular code where the variable was defined. After an error, the other pending closing methods will still be called.

If a coroutine yields and is never resumed again, some variables may never go out of scope, and therefore they will never be closed. (These variables are the ones created inside the coroutine and in scope at the point where the coroutine yielded.) Similarly, if a coroutine ends with an error, it does not unwind its stack, so it does not close any variable. In both cases, you can either use finalizers or call `coroutine.close` to close the variables. However, if the coroutine was created through `coroutine.wrap`, then its corresponding function will close the coroutine in case of errors. 3.4 – Expressions

The basic expressions in Lua are the following: exp ::= prefixexp exp ::= **nil** | **false** | **true** exp ::= Numeral exp ::= LiteralString exp ::= functiondef exp ::= tableconstructor exp ::= ‘**...**’ exp ::= exp binop exp exp ::= unop exp prefixexp ::= var | functioncall | ‘**(**’ exp ‘**)**’

Numerals and literal strings are explained in §3.1; variables are explained in §3.2; function definitions are explained in §3.4.11; function calls are explained in §3.4.10; table constructors are explained in §3.4.9. Vararg expressions, denoted by three dots ('`...`'), can only be used when directly inside a variadic function; they are explained in §3.4.11.

Binary operators comprise arithmetic operators (see §3.4.1), bitwise operators (see §3.4.2), relational operators (see §3.4.4), logical operators (see §3.4.5), and the concatenation operator (see §3.4.6). Unary operators comprise the unary minus (see §3.4.1), the unary bitwise NOT (see §3.4.2), the unary logical **not** (see §3.4.5), and the unary *length operator* (see §3.4.7). 3.4.1 – Arithmetic Operators

Lua supports the following arithmetic operators: **`+`:**addition **`-`:**subtraction **`*`:**multiplication **`/`:**float division **`//`:**floor division **`%`:**modulo **`^`:**exponentiation **`-`:**unary minus

With the exception of exponentiation and float division, the arithmetic operators work as follows: If both operands are integers, the operation is performed over integers and the result is an integer. Otherwise, if both operands are numbers, then they are converted to floats, the operation is performed following the machine's rules for floating-point arithmetic (usually the IEEE 754 standard), and the result is a float. (The string library coerces strings to numbers in arithmetic operations; see §3.4.3 for details.)

Exponentiation and float division (`/`) always convert their operands to floats and the result is always a float. Exponentiation uses the ISO C function `pow`, so that it works for non-integer exponents too.

Floor division (`//`) is a division that rounds the quotient towards minus infinity, resulting in the floor of the division of its operands.

Modulo is defined as the remainder of a division that rounds the quotient towards minus infinity (floor division).

In case of overflows in integer arithmetic, all operations *wrap around*. 3.4.2 – Bitwise Operators

Lua supports the following bitwise operators: **`&`:**bitwise AND **`|`:**bitwise OR **`~`:**bitwise exclusive OR **`>>`:**right shift **`<<`:**left shift **`~`:**unary bitwise NOT

All bitwise operations convert its operands to integers (see §3.4.3), operate on all bits of those integers, and result in an integer.

Both right and left shifts fill the vacant bits with zeros. Negative displacements shift to the other direction; displacements with absolute values equal to or higher than the number of bits in an integer result in zero (as all bits are shifted out). 3.4.3 – Coercions and Conversions

Lua provides some automatic conversions between some types and representations at run time. Bitwise operators always convert float operands to integers. Exponentiation and float division always convert integer operands to floats. All other arithmetic operations applied to mixed numbers (integers and floats) convert the integer operand to a float. The C API also converts both integers to floats and floats to integers, as needed. Moreover, string concatenation accepts numbers as arguments, besides strings.

In a conversion from integer to float, if the integer value has an exact representation as a float, that is the result. Otherwise, the conversion gets the nearest higher or the nearest lower representable value. This kind of conversion never fails.

The conversion from float to integer checks whether the float has an exact representation as an integer (that is, the float has an integral value and it is in the range of integer representation). If it does, that representation is the result. Otherwise, the conversion fails.

Several places in Lua coerce strings to numbers when necessary. In particular, the string library sets metamethods that try to coerce strings to numbers in all arithmetic operations. If the conversion fails, the library calls the metamethod of the other operand (if present) or it raises an error. Note that bitwise operators do not do this coercion.

It is always a good practice not to rely on the implicit coercions from strings to numbers, as they are not always applied; in particular, `"1"==1` is false and `"1"<1` raises an error (see §3.4.4). These coercions exist mainly for compatibility and may be removed in future versions of the language.

A string is converted to an integer or a float following its syntax and the rules of the Lua lexer. The string may have also leading and trailing whitespaces and a sign. All conversions from strings to numbers accept both a dot and the current locale mark as the radix character. (The Lua lexer, however, accepts only a dot.) If the string is not a valid numeral, the conversion fails. If necessary, the result of this first step is then converted to a specific number subtype following the previous rules for conversions between floats and integers.

The conversion from numbers to strings uses a non-specified human-readable format. To convert numbers to strings in any specific way, use the function `string.format`. 3.4.4 – Relational Operators

Lua supports the following relational operators: **`==`:**equality **`~=`:**inequality **`<`:**less than **`>`:**greater than **`<=`:**less or equal **`>=`:**greater or equal

These operators always result in **false** or **true**.

Equality (`==`) first compares the type of its operands. If the types are different, then the result is **false**. Otherwise, the values of the operands are compared. Strings are equal if they have the same byte content. Numbers are equal if they denote the same mathematical value.

Tables, userdata, and threads are compared by reference: two objects are considered equal only if they are the same object. Every time you create a new object (a table, a userdata, or a thread), this new object is different from any previously existing object. A function is always equal to itself. Functions with any detectable difference (different behavior, different definition) are always different. Functions created at different times but with no detectable differences may be classified as equal or not (depending on internal caching details).

You can change the way that Lua compares tables and userdata by using the `__eq` metamethod (see §2.4).

Equality comparisons do not convert strings to numbers or vice versa. Thus, `"0"==0` evaluates to **false**, and `t[0]` and `t["0"]` denote different entries in a table.

The operator `~=` is exactly the negation of equality (`==`).

The order operators work as follows. If both arguments are numbers, then they are compared according to their mathematical values, regardless of their subtypes. Otherwise, if both arguments are strings, then their values are compared according to the current locale. Otherwise, Lua tries to call the `__lt` or the `__le` metamethod (see §2.4). A comparison `a > b` is translated to `b < a` and `a >= b` is translated to `b <= a`.

Following the IEEE 754 standard, the special value NaN is considered neither less than, nor equal to, nor greater than any value, including itself. 3.4.5 – Logical Operators

The logical operators in Lua are **and**, **or**, and **not**. Like the control structures (see §3.3.4), all logical operators consider both **false** and **nil** as false and anything else as true.

The negation operator **not** always returns **false** or **true**. The conjunction operator **and** returns its first argument if this value is **false** or **nil**; otherwise, **and** returns its second argument. The disjunction operator **or** returns its first argument if this value is different from **nil** and **false**; otherwise, **or** returns its second argument. Both **and** and **or** use short-circuit evaluation; that is, the second operand is evaluated only if necessary. Here are some examples: 10 or 20 --> 10 10 or error() --> 10 nil or "a" --> "a" nil and 10 --> nil false and error() --> false false and nil --> false false or nil --> nil 10 and 20 --> 20 3.4.6 – Concatenation

The string concatenation operator in Lua is denoted by two dots ('`..`'). If both operands are strings or numbers, then the numbers are converted to strings in a non-specified format (see §3.4.3). Otherwise, the `__concat` metamethod is called (see §2.4). 3.4.7 – The Length Operator

The length operator is denoted by the unary prefix operator `#`.

The length of a string is its number of bytes. (That is the usual meaning of string length when each character is one byte.)

The length operator applied on a table returns a border in that table. A *border* in a table `t` is any non-negative integer that satisfies the following condition: (border == 0 or t[border] ~= nil) and (t[border + 1] == nil or border == math.maxinteger)

In words, a border is any positive integer index present in the table that is followed by an absent index, plus two limit cases: zero, when index 1 is absent; and the maximum value for an integer, when that index is present. Note that keys that are not positive integers do not interfere with borders.

A table with exactly one border is called a *sequence*. For instance, the table `{10, 20, 30, 40, 50}` is a sequence, as it has only one border (5). The table `{10, 20, 30, nil, 50}` has two borders (3 and 5), and therefore it is not a sequence. (The **nil** at index 4 is called a *hole*.) The table `{nil, 20, 30, nil, nil, 60, nil}` has three borders (0, 3, and 6), so it is not a sequence, too. The table `{}` is a sequence with border 0.

When `t` is a sequence, `#t` returns its only border, which corresponds to the intuitive notion of the length of the sequence. When `t` is not a sequence, `#t` can return any of its borders. (The exact one depends on details of the internal representation of the table, which in turn can depend on how the table was populated and the memory addresses of its non-numeric keys.)

The computation of the length of a table has a guaranteed worst time of *O(log n)*, where *n* is the largest integer key in the table.

A program can modify the behavior of the length operator for any value but strings through the `__len` metamethod (see §2.4). 3.4.8 – Precedence

Operator precedence in Lua follows the table below, from lower to higher priority: or and < > <= >= ~= == | ~ & << >> .. + - * / // % unary operators (not # - ~) ^

As usual, you can use parentheses to change the precedences of an expression. The concatenation ('`..`') and exponentiation ('`^`') operators are right associative. All other binary operators are left associative. 3.4.9 – Table Constructors

Table constructors are expressions that create tables. Every time a constructor is evaluated, a new table is created. A constructor can be used to create an empty table or to create a table and initialize some of its fields. The general syntax for constructors is tableconstructor ::= ‘**{**’ [fieldlist] ‘**}**’ fieldlist ::= field {fieldsep field} [fieldsep] field ::= ‘**[**’ exp ‘**]**’ ‘**=**’ exp | Name ‘**=**’ exp | exp fieldsep ::= ‘**,**’ | ‘**;**’

Each field of the form `[exp1] = exp2` adds to the new table an entry with key `exp1` and value `exp2`. A field of the form `name = exp` is equivalent to `["name"] = exp`. Fields of the form `exp` are equivalent to `[i] = exp`, where `i` are consecutive integers starting with 1; fields in the other formats do not affect this counting. For example, a = { [f(1)] = g; "x", "y"; x = 1, f(x), [30] = 23; 45 }

is equivalent to do local t = {} t[f(1)] = g t[1] = "x" -- 1st exp t[2] = "y" -- 2nd exp t.x = 1 -- t["x"] = 1 t[3] = f(x) -- 3rd exp t[30] = 23 t[4] = 45 -- 4th exp a = t end

The order of the assignments in a constructor is undefined. (This order would be relevant only when there are repeated keys.)

If the last field in the list has the form `exp` and the expression is a multires expression, then all values returned by this expression enter the list consecutively (see §3.4.12).

The field list can have an optional trailing separator, as a convenience for machine-generated code. 3.4.10 – Function Calls

A function call in Lua has the following syntax: functioncall ::= prefixexp args

In a function call, first prefixexp and args are evaluated. If the value of prefixexp has type *function*, then this function is called with the given arguments. Otherwise, if present, the prefixexp `__call` metamethod is called: its first argument is the value of prefixexp, followed by the original call arguments (see §2.4).

The form functioncall ::= prefixexp ‘**:**’ Name args

can be used to emulate methods. A call `v:name(*args*)` is syntactic sugar for `v.name(v,*args*)`, except that `v` is evaluated only once.

Arguments have the following syntax: args ::= ‘**(**’ [explist] ‘**)**’ args ::= tableconstructor args ::= LiteralString

All argument expressions are evaluated before the call. A call of the form `f{*fields*}` is syntactic sugar for `f({*fields*})`; that is, the argument list is a single new table. A call of the form `f'*string*'` (or `f"*string*"` or `f[[*string*]]`) is syntactic sugar for `f('*string*')`; that is, the argument list is a single literal string.

A call of the form `return *functioncall*` not in the scope of a to-be-closed variable is called a *tail call*. Lua implements *proper tail calls* (or *proper tail recursion*): In a tail call, the called function reuses the stack entry of the calling function. Therefore, there is no limit on the number of nested tail calls that a program can execute. However, a tail call erases any debug information about the calling function. Note that a tail call only happens with a particular syntax, where the **return** has one single function call as argument, and it is outside the scope of any to-be-closed variable. This syntax makes the calling function return exactly the returns of the called function, without any intervening action. So, none of the following examples are tail calls: return (f(x)) -- results adjusted to 1 return 2 * f(x) -- result multiplied by 2 return x, f(x) -- additional results f(x); return -- results discarded return x or f(x) -- results adjusted to 1 3.4.11 – Function Definitions

The syntax for function definition is functiondef ::= **function** funcbody funcbody ::= ‘**(**’ [parlist] ‘**)**’ block **end**

The following syntactic sugar simplifies function definitions: stat ::= **function** funcname funcbody stat ::= **local** **function** Name funcbody funcname ::= Name {‘**.**’ Name} [‘**:**’ Name]

The statement function f () *body* end

translates to f = function () *body* end

The statement function t.a.b.c.f () *body* end

translates to t.a.b.c.f = function () *body* end

The statement local function f () *body* end

translates to local f; f = function () *body* end

not to local f = function () *body* end

(This only makes a difference when the body of the function contains references to `f`.)

A function definition is an executable expression, whose value has type *function*. When Lua precompiles a chunk, all its function bodies are precompiled too, but they are not created yet. Then, whenever Lua executes the function definition, the function is *instantiated* (or *closed*). This function instance, or *closure*, is the final value of the expression.

Parameters act as local variables that are initialized with the argument values: parlist ::= namelist [‘**,**’ ‘**...**’] | ‘**...**’

When a Lua function is called, it adjusts its list of arguments to the length of its list of parameters (see §3.4.12), unless the function is a *variadic function*, which is indicated by three dots ('`...`') at the end of its parameter list. A variadic function does not adjust its argument list; instead, it collects all extra arguments and supplies them to the function through a *vararg expression*, which is also written as three dots. The value of this expression is a list of all actual extra arguments, similar to a function with multiple results (see §3.4.12).

As an example, consider the following definitions: function f(a, b) end function g(a, b, ...) end function r() return 1,2,3 end

Then, we have the following mapping from arguments to parameters and to the vararg expression: CALL PARAMETERS f(3) a=3, b=nil f(3, 4) a=3, b=4 f(3, 4, 5) a=3, b=4 f(r(), 10) a=1, b=10 f(r()) a=1, b=2 g(3) a=3, b=nil, ... --> (nothing) g(3, 4) a=3, b=4, ... --> (nothing) g(3, 4, 5, 8) a=3, b=4, ... --> 5 8 g(5, r()) a=5, b=1, ... --> 2 3

Results are returned using the **return** statement (see §3.3.4). If control reaches the end of a function without encountering a **return** statement, then the function returns with no results.

There is a system-dependent limit on the number of values that a function may return. This limit is guaranteed to be greater than 1000.

The *colon* syntax is used to emulate *methods*, adding an implicit extra parameter `self` to the function. Thus, the statement function t.a.b.c:f (*params*) *body* end

is syntactic sugar for t.a.b.c.f = function (self, *params*) *body* end 3.4.12 – Lists of expressions, multiple results, and adjustment

Both function calls and vararg expressions can result in multiple values. These expressions are called *multires expressions*.

When a multires expression is used as the last element of a list of expressions, all results from the expression are added to the list of values produced by the list of expressions. Note that a single expression in a place that expects a list of expressions is the last expression in that (singleton) list.

These are the places where Lua expects a list of expressions: A **return** statement, for instance `return e1, e2, e3` (see §3.3.4). A table constructor, for instance `{e1, e2, e3}` (see §3.4.9). The arguments of a function call, for instance `foo(e1, e2, e3)` (see §3.4.10). A multiple assignment, for instance `a , b, c = e1, e2, e3` (see §3.3.3). A local declaration, for instance `local a , b, c = e1, e2, e3` (see §3.3.7). The initial values in a generic **for** loop, for instance `for k in e1, e2, e3 do ... end` (see §3.3.5).

In the last four cases, the list of values from the list of expressions must be *adjusted* to a specific length: the number of parameters in a call to a non-variadic function (see §3.4.11), the number of variables in a multiple assignment or a local declaration, and exactly four values for a generic **for** loop. The *adjustment* follows these rules: If there are more values than needed, the extra values are thrown away; if there are fewer values than needed, the list is extended with **nil**'s. When the list of expressions ends with a multires expression, all results from that expression enter the list of values before the adjustment.

When a multires expression is used in a list of expressions without being the last element, or in a place where the syntax expects a single expression, Lua adjusts the result list of that expression to one element. As a particular case, the syntax expects a single expression inside a parenthesized expression; therefore, adding parentheses around a multires expression forces it to produce exactly one result.

We seldom need to use a vararg expression in a place where the syntax expects a single expression. (Usually it is simpler to add a regular parameter before the variadic part and use that parameter.) When there is such a need, we recommend assigning the vararg expression to a single variable and using that variable in its place.

Here are some examples of uses of mutlres expressions. In all cases, when the construction needs "the n-th result" and there is no such result, it uses a **nil**. print(x, f()) -- prints x and all results from f(). print(x, (f())) -- prints x and the first result from f(). print(f(), x) -- prints the first result from f() and x. print(1 + f()) -- prints 1 added to the first result from f(). local x = ... -- x gets the first vararg argument. x,y = ... -- x gets the first vararg argument, -- y gets the second vararg argument. x,y,z = w, f() -- x gets w, y gets the first result from f(), -- z gets the second result from f(). x,y,z = f() -- x gets the first result from f(), -- y gets the second result from f(), -- z gets the third result from f(). x,y,z = f(), g() -- x gets the first result from f(), -- y gets the first result from g(), -- z gets the second result from g(). x,y,z = (f()) -- x gets the first result from f(), y and z get nil. return f() -- returns all results from f(). return x, ... -- returns x and all received vararg arguments. return x,y,f() -- returns x, y, and all results from f(). {f()} -- creates a list with all results from f(). {...} -- creates a list with all vararg arguments. {f(), 5} -- creates a list with the first result from f() and 5. 3.5 – Visibility Rules

Lua is a lexically scoped language. The scope of a local variable begins at the first statement after its declaration and lasts until the last non-void statement of the innermost block that includes the declaration. (*Void statements* are labels and empty statements.) Consider the following example: x = 10 -- global variable do -- new block local x = x -- new 'x', with value 10 print(x) --> 10 x = x+1 do -- another block local x = x+1 -- another 'x' print(x) --> 12 end print(x) --> 11 end print(x) --> 10 (the global one)

Notice that, in a declaration like `local x = x`, the new `x` being declared is not in scope yet, and so the second `x` refers to the outside variable.

Because of the lexical scoping rules, local variables can be freely accessed by functions defined inside their scope. A local variable used by an inner function is called an *upvalue* (or *external local variable*, or simply *external variable*) inside the inner function.

Notice that each execution of a **local** statement defines new local variables. Consider the following example: a = {} local x = 20 for i = 1, 10 do local y = 0 a[i] = function () y = y + 1; return x + y end end

The loop creates ten closures (that is, ten instances of the anonymous function). Each of these closures uses a different `y` variable, while all of them share the same `x`. 4 – The Application Program Interface

This section describes the C API for Lua, that is, the set of C functions available to the host program to communicate with Lua. All API functions and related types and constants are declared in the header file `lua.h`.

Even when we use the term "function", any facility in the API may be provided as a macro instead. Except where stated otherwise, all such macros use each of their arguments exactly once (except for the first argument, which is always a Lua state), and so do not generate any hidden side-effects.

As in most C libraries, the Lua API functions do not check their arguments for validity or consistency. However, you can change this behavior by compiling Lua with the macro `LUA_USE_APICHECK` defined.

The Lua library is fully reentrant: it has no global variables. It keeps all information it needs in a dynamic structure, called the *Lua state*.

Each Lua state has one or more threads, which correspond to independent, cooperative lines of execution. The type `lua_State` (despite its name) refers to a thread. (Indirectly, through the thread, it also refers to the Lua state associated to the thread.)

A pointer to a thread must be passed as the first argument to every function in the library, except to `lua_newstate`, which creates a Lua state from scratch and returns a pointer to the *main thread* in the new state. 4.1 – The Stack

Lua uses a *virtual stack* to pass values to and from C. Each element in this stack represents a Lua value (**nil**, number, string, etc.). Functions in the API can access this stack through the Lua state parameter that they receive.

Whenever Lua calls C, the called function gets a new stack, which is independent of previous stacks and of stacks of C functions that are still active. This stack initially contains any arguments to the C function and it is where the C function can store temporary Lua values and must push its results to be returned to the caller (see `lua_CFunction`).

For convenience, most query operations in the API do not follow a strict stack discipline. Instead, they can refer to any element in the stack by using an *index*: A positive index represents an absolute stack position, starting at 1 as the bottom of the stack; a negative index represents an offset relative to the top of the stack. More specifically, if the stack has *n* elements, then index 1 represents the first element (that is, the element that was pushed onto the stack first) and index *n* represents the last element; index -1 also represents the last element (that is, the element at the top) and index *-n* represents the first element. 4.1.1 – Stack Size

When you interact with the Lua API, you are responsible for ensuring consistency. In particular, *you are responsible for controlling stack overflow*. When you call any API function, you must ensure the stack has enough room to accommodate the results.

There is one exception to the above rule: When you call a Lua function without a fixed number of results (see `lua_call`), Lua ensures that the stack has enough space for all results. However, it does not ensure any extra space. So, before pushing anything on the stack after such a call you should use `lua_checkstack`.

Whenever Lua calls C, it ensures that the stack has space for at least `LUA_MINSTACK` extra elements; that is, you can safely push up to `LUA_MINSTACK` values into it. `LUA_MINSTACK` is defined as 20, so that usually you do not have to worry about stack space unless your code has loops pushing elements onto the stack. Whenever necessary, you can use the function `lua_checkstack` to ensure that the stack has enough space for pushing new elements. 4.1.2 – Valid and Acceptable Indices

Any function in the API that receives stack indices works only with *valid indices* or *acceptable indices*.

A *valid index* is an index that refers to a position that stores a modifiable Lua value. It comprises stack indices between 1 and the stack top (`1 ≤ abs(index) ≤ top`) plus *pseudo-indices*, which represent some positions that are accessible to C code but that are not in the stack. Pseudo-indices are used to access the registry (see §4.3) and the upvalues of a C function (see §4.2).

Functions that do not need a specific mutable position, but only a value (e.g., query functions), can be called with acceptable indices. An *acceptable index* can be any valid index, but it also can be any positive index after the stack top within the space allocated for the stack, that is, indices up to the stack size. (Note that 0 is never an acceptable index.) Indices to upvalues (see §4.2) greater than the real number of upvalues in the current C function are also acceptable (but invalid). Except when noted otherwise, functions in the API work with acceptable indices.

Acceptable indices serve to avoid extra tests against the stack top when querying the stack. For instance, a C function can query its third argument without the need to check whether there is a third argument, that is, without the need to check whether 3 is a valid index.

For functions that can be called with acceptable indices, any non-valid index is treated as if it contains a value of a virtual type `LUA_TNONE`, which behaves like a nil value. 4.1.3 – Pointers to strings

Several functions in the API return pointers (`const char*`) to Lua strings in the stack. (See `lua_pushfstring`, `lua_pushlstring`, `lua_pushstring`, and `lua_tolstring`. See also `luaL_checklstring`, `luaL_checkstring`, and `luaL_tolstring` in the auxiliary library.)

In general, Lua's garbage collection can free or move internal memory and then invalidate pointers to internal strings. To allow a safe use of these pointers, the API guarantees that any pointer to a string in a stack index is valid while the string value at that index is not removed from the stack. (It can be moved to another index, though.) When the index is a pseudo-index (referring to an upvalue), the pointer is valid while the corresponding call is active and the corresponding upvalue is not modified.

Some functions in the debug interface also return pointers to strings, namely `lua_getlocal`, `lua_getupvalue`, `lua_setlocal`, and `lua_setupvalue`. For these functions, the pointer is guaranteed to be valid while the caller function is active and the given closure (if one was given) is in the stack.

Except for these guarantees, the garbage collector is free to invalidate any pointer to internal strings. 4.2 – C Closures

When a C function is created, it is possible to associate some values with it, thus creating a *C closure* (see `lua_pushcclosure`); these values are called *upvalues* and are accessible to the function whenever it is called.

Whenever a C function is called, its upvalues are located at specific pseudo-indices. These pseudo-indices are produced by the macro `lua_upvalueindex`. The first upvalue associated with a function is at index `lua_upvalueindex(1)`, and so on. Any access to `lua_upvalueindex(*n*)`, where *n* is greater than the number of upvalues of the current function (but not greater than 256, which is one plus the maximum number of upvalues in a closure), produces an acceptable but invalid index.

A C closure can also change the values of its corresponding upvalues. 4.3 – Registry

Lua provides a *registry*, a predefined table that can be used by any C code to store whatever Lua values it needs to store. The registry table is always accessible at pseudo-index `LUA_REGISTRYINDEX`. Any C library can store data into this table, but it must take care to choose keys that are different from those used by other libraries, to avoid collisions. Typically, you should use as key a string containing your library name, or a light userdata with the address of a C object in your code, or any Lua object created by your code. As with variable names, string keys starting with an underscore followed by uppercase letters are reserved for Lua.

The integer keys in the registry are used by the reference mechanism (see `luaL_ref`) and by some predefined values. Therefore, integer keys in the registry must not be used for other purposes.

When you create a new Lua state, its registry comes with some predefined values. These predefined values are indexed with integer keys defined as constants in `lua.h`. The following constants are defined: **`LUA_RIDX_MAINTHREAD`:** At this index the registry has the main thread of the state. (The main thread is the one created together with the state.) **`LUA_RIDX_GLOBALS`:** At this index the registry has the global environment. 4.4 – Error Handling in C

Internally, Lua uses the C `longjmp` facility to handle errors. (Lua will use exceptions if you compile it as C++; search for `LUAI_THROW` in the source code for details.) When Lua faces any error, such as a memory allocation error or a type error, it *raises* an error; that is, it does a long jump. A *protected environment* uses `setjmp` to set a recovery point; any error jumps to the most recent active recovery point.

Inside a C function you can raise an error explicitly by calling `lua_error`.

Most functions in the API can raise an error, for instance due to a memory allocation error. The documentation for each function indicates whether it can raise errors.

If an error happens outside any protected environment, Lua calls a *panic function* (see `lua_atpanic`) and then calls `abort`, thus exiting the host application. Your panic function can avoid this exit by never returning (e.g., doing a long jump to your own recovery point outside Lua).

The panic function, as its name implies, is a mechanism of last resort. Programs should avoid it. As a general rule, when a C function is called by Lua with a Lua state, it can do whatever it wants on that Lua state, as it should be already protected. However, when C code operates on other Lua states (e.g., a Lua-state argument to the function, a Lua state stored in the registry, or the result of `lua_newthread`), it should use them only in API calls that cannot raise errors.

The panic function runs as if it were a message handler (see §2.3); in particular, the error object is on the top of the stack. However, there is no guarantee about stack space. To push anything on the stack, the panic function must first check the available space (see §4.1.1). 4.4.1 – Status Codes

Several functions that report errors in the API use the following status codes to indicate different kinds of errors or other conditions: **`LUA_OK` (0):** no errors. **`LUA_ERRRUN`:** a runtime error. **`LUA_ERRMEM`:** memory allocation error. For such errors, Lua does not call the message handler. **`LUA_ERRERR`:** error while running the message handler. **`LUA_ERRSYNTAX`:** syntax error during precompilation. **`LUA_YIELD`:** the thread (coroutine) yields. **`LUA_ERRFILE`:** a file-related error; e.g., it cannot open or read the file.

These constants are defined in the header file `lua.h`. 4.5 – Handling Yields in C

Internally, Lua uses the C `longjmp` facility to yield a coroutine. Therefore, if a C function `foo` calls an API function and this API function yields (directly or indirectly by calling another function that yields), Lua cannot return to `foo` any more, because the `longjmp` removes its frame from the C stack.

To avoid this kind of problem, Lua raises an error whenever it tries to yield across an API call, except for three functions: `lua_yieldk`, `lua_callk`, and `lua_pcallk`. All those functions receive a *continuation function* (as a parameter named `k`) to continue execution after a yield.

We need to set some terminology to explain continuations. We have a C function called from Lua which we will call the *original function*. This original function then calls one of those three functions in the C API, which we will call the *callee function*, that then yields the current thread. This can happen when the callee function is `lua_yieldk`, or when the callee function is either `lua_callk` or `lua_pcallk` and the function called by them yields.

Suppose the running thread yields while executing the callee function. After the thread resumes, it eventually will finish running the callee function. However, the callee function cannot return to the original function, because its frame in the C stack was destroyed by the yield. Instead, Lua calls a *continuation function*, which was given as an argument to the callee function. As the name implies, the continuation function should continue the task of the original function.

As an illustration, consider the following function: int original_function (lua_State *L) { ... /* code 1 */ status = lua_pcall(L, n, m, h); /* calls Lua */ ... /* code 2 */ }

Now we want to allow the Lua code being run by `lua_pcall` to yield. First, we can rewrite our function like here: int k (lua_State *L, int status, lua_KContext ctx) { ... /* code 2 */ } int original_function (lua_State *L) { ... /* code 1 */ return k(L, lua_pcall(L, n, m, h), ctx); }

In the above code, the new function `k` is a *continuation function* (with type `lua_KFunction`), which should do all the work that the original function was doing after calling `lua_pcall`. Now, we must inform Lua that it must call `k` if the Lua code being executed by `lua_pcall` gets interrupted in some way (errors or yielding), so we rewrite the code as here, replacing `lua_pcall` by `lua_pcallk`: int original_function (lua_State *L) { ... /* code 1 */ return k(L, lua_pcallk(L, n, m, h, ctx2, k), ctx1); }

Note the external, explicit call to the continuation: Lua will call the continuation only if needed, that is, in case of errors or resuming after a yield. If the called function returns normally without ever yielding, `lua_pcallk` (and `lua_callk`) will also return normally. (Of course, instead of calling the continuation in that case, you can do the equivalent work directly inside the original function.)

Besides the Lua state, the continuation function has two other parameters: the final status of the call and the context value (`ctx`) that was passed originally to `lua_pcallk`. Lua does not use this context value; it only passes this value from the original function to the continuation function. For `lua_pcallk`, the status is the same value that would be returned by `lua_pcallk`, except that it is `LUA_YIELD` when being executed after a yield (instead of `LUA_OK`). For `lua_yieldk` and `lua_callk`, the status is always `LUA_YIELD` when Lua calls the continuation. (For these two functions, Lua will not call the continuation in case of errors, because they do not handle errors.) Similarly, when using `lua_callk`, you should call the continuation function with `LUA_OK` as the status. (For `lua_yieldk`, there is not much point in calling directly the continuation function, because `lua_yieldk` usually does not return.)

Lua treats the continuation function as if it were the original function. The continuation function receives the same Lua stack from the original function, in the same state it would be if the callee function had returned. (For instance, after a `lua_callk` the function and its arguments are removed from the stack and replaced by the results from the call.) It also has the same upvalues. Whatever it returns is handled by Lua as if it were the return of the original function. 4.6 – Functions and Types

Here we list all functions and types from the C API in alphabetical order. Each function has an indicator like this: [-o, +p, *x*]

The first field, `o`, is how many elements the function pops from the stack. The second field, `p`, is how many elements the function pushes onto the stack. (Any function always pushes its results after popping its arguments.) A field in the form `x|y` means the function can push (or pop) `x` or `y` elements, depending on the situation; an interrogation mark '`?`' means that we cannot know how many elements the function pops/pushes by looking only at its arguments. (For instance, they may depend on what is in the stack.) The third field, `x`, tells whether the function may raise errors: '`-`' means the function never raises any error; '`m`' means the function may raise only out-of-memory errors; '`v`' means the function may raise the errors explained in the text; '`e`' means the function can run arbitrary Lua code, either directly or through metamethods, and therefore may raise any errors. `lua_absindex`

[-0, +0, –] int lua_absindex (lua_State *L, int idx);

Converts the acceptable index `idx` into an equivalent absolute index (that is, one that does not depend on the stack size). `lua_Alloc` typedef void * (*lua_Alloc) (void *ud, void *ptr, size_t osize, size_t nsize);

The type of the memory-allocation function used by Lua states. The allocator function must provide a functionality similar to `realloc`, but not exactly the same. Its arguments are `ud`, an opaque pointer passed to `lua_newstate`; `ptr`, a pointer to the block being allocated/reallocated/freed; `osize`, the original size of the block or some code about what is being allocated; and `nsize`, the new size of the block.

When `ptr` is not `NULL`, `osize` is the size of the block pointed by `ptr`, that is, the size given when it was allocated or reallocated.

When `ptr` is `NULL`, `osize` encodes the kind of object that Lua is allocating. `osize` is any of `LUA_TSTRING`, `LUA_TTABLE`, `LUA_TFUNCTION`, `LUA_TUSERDATA`, or `LUA_TTHREAD` when (and only when) Lua is creating a new object of that type. When `osize` is some other value, Lua is allocating memory for something else.

Lua assumes the following behavior from the allocator function:

When `nsize` is zero, the allocator must behave like `free` and then return `NULL`.

When `nsize` is not zero, the allocator must behave like `realloc`. In particular, the allocator returns `NULL` if and only if it cannot fulfill the request.

Here is a simple implementation for the allocator function. It is used in the auxiliary library by `luaL_newstate`. static void *l_alloc (void *ud, void *ptr, size_t osize, size_t nsize) { (void)ud; (void)osize; /* not used */ if (nsize == 0) { free(ptr); return NULL; } else return realloc(ptr, nsize); }

Note that ISO C ensures that `free(NULL)` has no effect and that `realloc(NULL,size)` is equivalent to `malloc(size)`. `lua_arith`

[-(2|1), +1, *e*] void lua_arith (lua_State *L, int op);

Performs an arithmetic or bitwise operation over the two values (or one, in the case of negations) at the top of the stack, with the value on the top being the second operand, pops these values, and pushes the result of the operation. The function follows the semantics of the corresponding Lua operator (that is, it may call metamethods).

The value of `op` must be one of the following constants: **`LUA_OPADD`:** performs addition (`+`) **`LUA_OPSUB`:** performs subtraction (`-`) **`LUA_OPMUL`:** performs multiplication (`*`) **`LUA_OPDIV`:** performs float division (`/`) **`LUA_OPIDIV`:** performs floor division (`//`) **`LUA_OPMOD`:** performs modulo (`%`) **`LUA_OPPOW`:** performs exponentiation (`^`) **`LUA_OPUNM`:** performs mathematical negation (unary `-`) **`LUA_OPBNOT`:** performs bitwise NOT (`~`) **`LUA_OPBAND`:** performs bitwise AND (`&`) **`LUA_OPBOR`:** performs bitwise OR (`|`) **`LUA_OPBXOR`:** performs bitwise exclusive OR (`~`) **`LUA_OPSHL`:** performs left shift (`<<`) **`LUA_OPSHR`:** performs right shift (`>>`) `lua_atpanic`

[-0, +0, –] lua_CFunction lua_atpanic (lua_State *L, lua_CFunction panicf);

Sets a new panic function and returns the old one (see §4.4). `lua_call`

[-(nargs+1), +nresults, *e*] void lua_call (lua_State *L, int nargs, int nresults);

Calls a function. Like regular Lua calls, `lua_call` respects the `__call` metamethod. So, here the word "function" means any callable value.
