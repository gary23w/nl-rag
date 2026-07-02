---
title: "C Programming/Preprocessor directives and macros"
source: https://en.wikibooks.org/wiki/C_Programming/Preprocessor_directives_and_macros
domain: c-book
license: CC-BY-SA-4.0 (Wikibooks C Programming)
tags: c pointers, c arrays, c memory management, c strings
fetched: 2026-07-02
---

# C Programming/Preprocessor directives and macros

<

C Programming

Preprocessors are a way of making text processing with your C program before they are actually compiled. Before the actual compilation of every C program it is passed through a Preprocessor. The Preprocessor looks through the program trying to find out specific instructions called Preprocessor directives that it can understand. All Preprocessor directives begin with the # (hash) symbol. C++ compilers use the same C preprocessor.

The preprocessor is a part of the compiler which performs preliminary operations (conditionally compiling code, including files etc...) to your code before the compiler sees it. These transformations are lexical, meaning that the output of the preprocessor is still text.

| NOTE: Technically the output of the preprocessing phase for C consists of a sequence of tokens, rather than source text, but it is simple to output source text which is equivalent to the given token sequence, and that is commonly supported by compilers via a -E or /E option -- although command line options to C compilers aren't completely standard, many follow similar rules. |
|---|

## Directives

Directives are special instructions directed to the preprocessor (preprocessor directive) or to the compiler (compiler directive) on how it should process part or all of your source code or set some flags on the final object and are used to make writing source code easier (more portable for instance) and to make the source code more understandable. Directives are handled by the preprocessor, which is either a separate program invoked by the compiler or part of the compiler itself.

### #include

C has some features as part of the language and some others as part of a **standard library**, which is a repository of code that is available alongside every standard-conformant C compiler. When the C compiler compiles your program it usually also links it with the standard C library. For example, on encountering a `#include <stdio.h>` directive, it replaces the directive with the contents of the stdio.h header file.

When you use features from the library, C requires you to *declare* what you would be using. The first line in the program is a **preprocessing directive** which should look like this:

```mw
#include <stdio.h>
```

The above line causes the C declarations which are in the stdio.h header to be included for use in your program. Usually this is implemented by just inserting into your program the contents of a **header file** called stdio.h, located in a system-dependent location. The location of such files may be described in your compiler's documentation. A list of standard C header files is listed below in the Headers table.

The stdio.h header contains various declarations for input/output (I/O) using an abstraction of I/O mechanisms called **streams**. For example there is an output stream object called stdout which is used to output text to the standard output, which usually displays the text on the computer screen.

If using angle brackets like the example above, the preprocessor is instructed to search for the include file along the development environment path for the standard includes.

```mw
#include "other.h"
```

If you use quotation marks (" "), the preprocessor is expected to search in some additional, usually user-defined, locations for the header file, and to fall back to the standard include paths only if it is not found in those additional locations. It is common for this form to include searching in the same directory as the file containing the #include directive.

| NOTE: You should check the documentation of the development environment you are using for any vendor specific implementations of the #include directive. |
|---|

#### Headers

**The C90 standard headers list:**

| <assert.h> <ctype.h> <errno.h> <float.h> <limits.h> | <locale.h> <math.h> <setjmp.h> <signal.h> <stdarg.h> | <stddef.h> <stdio.h> <stdlib.h> <string.h> <time.h> |
|---|---|---|

**Headers added since C90:**

| <complex.h> <fenv.h> <inttypes.h> | <iso646.h> <stdbool.h> <stdint.h> | <tgmath.h> <wchar.h> <wctype.h> |
|---|---|---|

### #pragma

The **pragma** (pragmatic information) directive is part of the standard, but the meaning of any pragma depends on the software implementation of the standard that is used. The #pragma directive provides a way to request special behavior from the compiler. This directive is most useful for programs that are unusually large or that need to take advantage of the capabilities of a particular compiler.

Pragmas are used within the source program.

```mw
#pragma token(s)
```

1. pragma is usually followed by a single token, which represents a command for the compiler to obey. You should check the software implementation of the C standard you intend on using for a list of the supported tokens. Not surprisingly, the set of commands that can appear in #pragma directives is different for each compiler; you'll have to consult the documentation for your compiler to see which commands it allows and what those commands do.

For instance one of the most implemented preprocessor directives, `#pragma once` when placed at the beginning of a header file, indicates that the file where it resides will be skipped if included several times by the preprocessor.

| NOTE: Other methods exist to do this action that is commonly referred as using **include guards**. |
|---|

### #define

Each `#define` preprocessor instruction defines a macro. For example,

```mw
#define PI 3.14159265358979323846
```

A macro defined with a space immediately after the name is called a constant or literal. A macro defined with a parenthesis immediately after the name is called a function-like macro.

| WARNING: Preprocessor macros, although tempting, can produce quite unexpected results if not done right. Always keep in mind that macros are textual substitutions done to your source code before anything is compiled. The compiler does not know anything about the macros and never gets to see them. This can produce obscure errors, amongst other negative effects. Prefer to use language features, if there are equivalent. For example, use `const int` or `enum` instead of `#define`d constants). That said, there are cases, where macros are very useful (see the `debug` macro below for an example). |
|---|

The #define directive is used to define macros. Macros are used by the preprocessor to manipulate the program source code before it is compiled. Because preprocessor macro definitions are substituted before the compiler acts on the source code, any errors that are introduced by #define are difficult to trace.

By convention, macros defined using #define are named in uppercase. Although doing so is not a requirement, it is considered very bad practice to do otherwise. This allows the macros to be easily identified when reading the source code. (We mention many other common conventions for using `#define` in a later chapter, C Programming/Common practices).

Today, #define is primarily used to handle compiler and platform differences. E.g., a define might hold a constant which is the appropriate error code for a system call. The use of #define should thus be limited unless absolutely necessary; typedef statements and constant variables can often perform the same functions more safely.

Another feature of the #define command is that it can take arguments, making it rather useful as a pseudo-function creator. Consider the following code:

```mw
#define ABSOLUTE_VALUE( x ) ( ((x) < 0) ? -(x) : (x) )
...
int x = -1;
while( ABSOLUTE_VALUE( x ) ) {
...
}
```

It's generally a good idea to use extra parentheses when using complex macros. Notice that in the above example, the variable "x" is always within its own set of parentheses. This way, it will be evaluated in whole, before being compared to 0 or multiplied by -1. Also, the entire macro is surrounded by parentheses, to prevent it from being contaminated by other code. If you're not careful, you run the risk of having the compiler misinterpret your code.

Because of side-effects it is considered a very bad idea to use macro functions as described above.

```mw
int x = -10;
int y = ABSOLUTE_VALUE( x++ );
```

If ABSOLUTE_VALUE() were a real function 'x' would now have the value of '-9', but because it was an argument in a macro it was expanded twice and thus has a value of -8.

| Example: To illustrate the dangers of macros, consider this naive macro #define MAX(a,b) a>b?a:b and the code i = MAX(2,3)+5; j = MAX(3,2)+5; Take a look at this and consider what the value after execution might be. The statements are turned into int i = 2>3?2:3+5; int j = 3>2?3:2+5; Thus, after execution i=8 and j=3 instead of the expected result of i=j=8! This is why you were cautioned to use an extra set of parenthesis above, but even with these, the road is fraught with dangers. The alert reader might quickly realize that if `a` or `b` contains expressions, the definition must parenthesize every use of a,b in the macro definition, like this: #define MAX(a,b) ((a)>(b)?(a):(b)) This works, provided a,b have no side effects. Indeed, i = 2; j = 3; k = MAX(i++, j++); would result in k=4, i=3 and j=5. This would be highly surprising to anyone expecting MAX() to behave like a function. So what is the correct solution? The solution is not to use macro at all. A global, inline function, like this inline int max(int a, int b) { return a>b?a:b } has none of the pitfalls above, but will not work with all types. NOTE: The explicit `inline` declaration is not really necessary unless the definition is in a header file, since your compiler can inline functions for you (with gcc this can be done with `-finline-functions` or `-O3`). The compiler is often better than the programmer at predicting which functions are worth inlining. Also, function calls are not really expensive (they used to be). The compiler is actually free to ignore the `inline` keyword. It is only a hint (except that `inline` is necessary in order to allow a function to be defined in a header file without generating an error message due to the function being defined in more than one translation unit). |
|---|

(**#, ##**)

The **#** and **##** operators are used with the #define macro. Using # causes the first argument after the **#** to be returned as a string in quotes. For example, the command

```mw
#define as_string( s ) # s
```

will make the compiler turn this command

```mw
puts( as_string( Hello World! ) ) ;
```

into

```mw
puts( "Hello World!" );
```

Using **##** concatenates what's before the **##** with what's after it. For example, the command

```mw
#define concatenate( x, y ) x ## y
...
int xy = 10;
...
```

will make the compiler turn

```mw
printf( "%d", concatenate( x, y ));
```

into

```mw
printf( "%d", xy);
```

which will, of course, display 10 to standard output.

It is possible to concatenate a macro argument with a constant prefix or suffix to obtain a valid identifier as in

```mw
#define make_function( name ) int my_ ## name (int foo) {}
make_function( bar )
```

which will define a function called my_bar(). But it isn't possible to integrate a macro argument into a constant string using the concatenation operator. In order to obtain such an effect, one can use the ANSI C property that two or more consecutive string constants are considered equivalent to a single string constant when encountered. Using this property, one can write

```mw
#define eat( what ) puts( "I'm eating " #what " today." )
eat( fruit )
```

which the macro-processor will turn into

```mw
puts( "I'm eating " "fruit" " today." )
```

which in turn will be interpreted by the C parser as a single string constant.

The following trick can be used to turn a numeric constants into string literals

```mw
#define num2str(x) str(x)
#define str(x) #x
#define CONST 23
 
puts(num2str(CONST));
```

This is a bit tricky, since it is expanded in 2 steps. First `num2str(CONST)` is replaced with `str(23)`, which in turn is replaced with `"23"`. This can be useful in the following example:

```mw
#ifdef DEBUG
#define debug(msg) fputs(__FILE__ ":" num2str(__LINE__) " - " msg, stderr)
#else
#define debug(msg)
#endif
```

This will give you a nice debug message including the file and the line where the message was issued. If DEBUG is not defined however the debugging message will completely vanish from your code. Be careful not to use this sort of construct with anything that has side effects, since this can lead to bugs, that appear and disappear depending on the compilation parameters.

### macros

Macros aren't type-checked and so they do not evaluate arguments. Also, they do not obey scope properly, but simply take the string passed to them and replace each occurrence of the macro argument in the text of the macro with the actual string for that parameter (the code is literally copied into the location it was called from).

An example on how to use a macro:

```mw
#include <stdio.h>

#define SLICES 8
#define ADD(x) ( (x) / SLICES )

int main(void) 
{
  int a = 0, b = 10, c = 6;

  a = ADD(b + c);
  printf("%d\n", a);
  return 0;
}
```

-- the result of "a" should be "2" (b + c = 16 -> passed to ADD -> 16 / SLICES -> result is "2")

| NOTE: It is usually bad practice to define macros in headers. A macro should be defined only when it is not possible to achieve the same result with a function or some other mechanism. Some compilers are able to optimize code to where calls to small functions are replaced with inline code, negating any possible speed advantage. Using typedefs, enums, and inline (in C99) is often a better option. |
|---|

One of the few situations where inline functions won't work -- so you are pretty much forced to use function-like macros instead -- is to initialize compile time constants (static initialization of structs). This happens when the arguments to the macro are literals that the compiler can optimize to another literal.

### #error

The **#error** directive halts compilation. When one is encountered the standard specifies that the compiler should emit a diagnostic containing the remaining tokens in the directive. This is mostly used for debugging purposes.

Programmers use "#error" inside a conditional block, to immediately halt the compiler when the "#if" or "#ifdef" -- at the beginning of the block -- detects a compile-time problem. Normally the compiler skips the block (and the "#error" directive inside it) and the compilation proceeds.

```mw
#error message
```

### #warning

Many compilers support a **#warning** directive. When one is encountered, the compiler emits a diagnostic containing the remaining tokens in the directive.

```mw
#warning message
```

### #undef

The **#undef** directive undefines a macro. The identifier need not have been previously defined.

### #if,#else,#elif,#endif (conditionals)

The **#if** command checks whether a controlling conditional expression evaluates to zero or nonzero, and excludes or includes a block of code respectively. For example:

```mw
#if 1
   /* This block will be included */
#endif
#if 0
   /* This block will not be included */
#endif
```

The conditional expression could contain any C operator except for the assignment operators, the increment and decrement operators, the address-of operator, and the sizeof operator.

One unique operator used in preprocessing and nowhere else is the **defined** operator. It returns 1 if the macro name, optionally enclosed in parentheses, is currently defined; 0 if not.

The **#endif** command ends a block started by `#if`, `#ifdef`, or `#ifndef`.

The **#elif** command is similar to `#if`, except that it is used to extract one from a series of blocks of code. E.g.:

```mw
#if /* some expression */
  :
  :
  :
#elif /* another expression */
  :
/* imagine many more #elifs here ... */
  :
#else
/* The optional #else block is selected if none of the previous #if or
   #elif blocks are selected */
  :
  :
#endif /* The end of the #if block */
```

### #ifdef,#ifndef

The **#ifdef** command is similar to `#if`, except that the code block following it is selected if a macro name is defined. In this respect,

```mw
#ifdef NAME
```

is equivalent to

```mw
#if defined NAME
```

The **#ifndef** command is similar to **#ifdef**, except that the test is reversed:

```mw
#ifndef NAME
```

is equivalent to

```mw
#if !defined NAME
```

### #line

This preprocessor directive is used to set the file name and the line number of the line following the directive to new values. This is used to set the __FILE__ and __LINE__ macros.

## Useful preprocessor macros for debugging

ANSI C defines some useful preprocessor macros and variables, also called "magic constants", include:

__FILE__ => The name of the current file, as a string literal __LINE__ => Current line of the source file, as a numeric literal __DATE__ => Current system date, as a string __TIME__ => Current system time, as a string __TIMESTAMP__ => Date and time (non-standard) __cplusplus => undefined when your C code is being compiled by a C compiler; 199711L when your C code is being compiled by a C++ compiler compliant with 1998 C++ standard. __func__ => Current function name of the source file, as a string (part of C99) __PRETTY_FUNCTION__ => "decorated" Current function name of the source file, as a string (in GCC; non-standard)

#### Compile-time assertions

Compile-time assertions can help you debug faster than using only run-time assert() statements, because the compile-time assertions are all tested at compile time, while it is possible that a test run of a program may fail to exercise some run-time assert() statements.

Prior to the C11 standard, some people defined a preprocessor macro to allow compile-time assertions, something like:

```mw
#define COMPILE_TIME_ASSERT(pred) switch(0){case 0:case pred:;}

COMPILE_TIME_ASSERT( BOOLEAN CONDITION );
```

The `static_assert.hpp` Boost library defines a similar macro.

Since C11, such macros are obsolete, as `_Static_assert` and its macro equivalent `static_assert` are standardized and built-in to the language.
