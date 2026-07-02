---
title: "C Programming/Variables"
source: https://en.wikibooks.org/wiki/C_Programming/Variables
domain: c-book
license: CC-BY-SA-4.0 (Wikibooks C Programming)
tags: c pointers, c arrays, c memory management, c strings
fetched: 2026-07-02
---

# C Programming/Variables

<

C Programming

Like most programming languages, C uses and processes **variables**. In C, variables are human-readable names for the places where data used by a running program is stored.

Imagine variables as placeholders for values, much like in mathematics. You can think of a variable as being equivalent to its assigned value. So, if you have a variable x with the value 4 , then it follows that $x+1=5$ .

Before we can continue on this topic, though, we must first look at how C organizes memory.

## Data locations

Literals and other constants (explained later) may be loaded and used directly by the compiled machine code, or they might be loaded from a read-only *data segment* in your program that is created during the build process. Where does the rest of the information for your program go?

CPUs have a small number of low-capacity but high-speed *registers* for data storage. When you create a variable, your compiler will likely assign a register for it to live in while it exists. These registers are nowhere near large enough to contain all the information our programs need, though. The rest of the data for your variables lives in RAM, which the C runtime splits into two areas:

- the *stack*, a space for short-lived data that operates on a *first-in-last-out* model
- the *heap*, a space for longer-lived, typically larger data

Data is said to be *pushed* when it is added to the stack, and *popped* when it is removed.

In this section, the variables we create will exist in CPU registers and the stack.

## Introduction

### Declaring variables

Here is an example of declaring an integer, which we've called `some_number`.

```mw
int some_number;
```

| (Note) | Recall that statements must end with semicolons. |
|---|---|

This statement tells the compiler to create a variable called `some_number` and associate it with a location in memory, either in a register (if there is room) or on the stack. We also tell the compiler the type of the data that will be stored there, in this case an `int` for integer. This lets the compiler know how much total memory to set aside for the data. On most modern machines, an `int` is 4 bytes in length.

Multiple variables can be declared with one statement, like this:

```mw
int a_number, another_number, yet_another_number;
```

### Assignment

After declaring variables, you can assign a value to a variable later on using a statement like this:

```mw
some_number = 3;
```

The above statement directs the compiler to insert an integer representation of the number 3 into the memory location associated with `some_number`.

You can also assign variables to the value of other variable, like so:

```mw
some_number = another_number;
```

Or assign multiple variables the same value with one statement:

```mw
a_number = another_number = yet_another_number = 8;
```

### Initialization

We can save a bit of typing by declaring a variable and assigning it data at the same time:

```mw
int some_new_number = 4;
```

## Naming rules

Variable names in C are made up of letters (upper and lower case), digits, and underscores (`_`). Names must not begin with a digit.

| (Note) | Unlike some languages (such as Perl and some BASIC dialects), C does not use any special prefix characters on variable names. |
|---|---|

Some examples of valid (but not very descriptive) C variable names:

- `foo`
- `Bar`
- `BAZ`
- `foo_bar`
- `_foo42`
- `_`
- `QuUx`

Some examples of invalid C variable names:

- `2foo` (must not begin with a digit)
- `my foo` (spaces not allowed in names)
- `$foo` ($ not allowed—only letters, and _)
- `while` (language keywords cannot be used as names)

As the last example suggests, certain words are reserved as keywords in the language, and these cannot be used as variable names.

When working with other developers, you should take steps to avoid using the same name for global variables or function names. Some large projects adhere to naming guidelines to avoid duplicate names and for consistency.

There are certain sets of names that, while not language keywords, are reserved for one reason or another. For example, a C compiler might use certain names "behind the scenes", and this might cause problems for a program that attempts to use them. Also, some names are reserved for possible future use in the C standard library. The rules for determining exactly what names are reserved (and in what contexts they are reserved) are complex, and as a beginner you don't need to worry about them much anyway. For now, just avoid using names that begin with an underscore character.

| (Note) | The naming rules for C variables also apply to naming other language constructs such as function names, struct tags, and macros, all of which will be covered later. |
|---|---|

It is not allowed to use the same name for multiple variables in the same scope. What is a scope? Read on:

## Scope

*Scope* is the level at which a piece of data (or a function) is visible. Scopes are nested inside each other, and the outermost scope is the *global scope*. Something visible in a given scope is visible in all inner scopes, but no outer scopes. When something that is visible in a given scope is also defined in that same scope, we say that thing is *local* to that scope.

It is possible to give a variable in an inner scope the same name as one defined in an outer scope. In that inner scope, and all scopes inside it, the reused name refers to the new variable. But, outside that scope, the name refers to the old variable, which remains unaffected by anything that happened in the inner scope. It's as if the outer variable is invisible while in the inner scope. We say that the outer variable has been *shadowed* by the inner variable.

Let's look at an example to get a better idea of scope.

| (Example) | int main(void) { // This is the beginning of a block. int i = 6; // This is the first variable of this block, 'i'. { // This is a new block, which has its own scope. // This is also a variable called 'i', but in a different block. // It has the same name as the other 'i', but it's not the same variable! int i = 5; printf("%d\n", i); // This refers to the inner 'i'. } // Back in the scope of 'main', 'i' refers to the variable from the start of the function again. printf("%d\n", i); return 0; } Output: 5 6 |
|---|---|

## Constants

When you write C programs, you may be tempted to write code that will depend on certain numbers. For example, you may be writing a program for a grocery store. This complex program has thousands upon thousands of lines of code. The programmer decides to represent the cost of a can of corn, currently 99 cents, as a literal throughout the code. Now, assume the cost of a can of corn changes to 89 cents. The programmer must now go in and manually change each entry of 99 cents to 89. While this is not that big a problem, considering the "global find-replace" function of many text editors, consider another problem: the cost of a can of green beans is also initially 99 cents. To reliably change the price, you have to look at every occurrence of the number 99.

C possesses certain functionality to avoid these *magic numbers*. By declaring a *constant*...

```mw
const int corn_price = 89;
```

...a programmer can simply change that constant and not have to worry about setting the value elsewhere.

When the `const` qualifier is used, the declared variable must be initialized at declaration. It is then not allowed to be changed.

Constants are useful for most than just having a single source of truth for some data. For one thing, many compilers can perform some small optimizations on data when it knows that data will never change. The compiler might decide that it would be more performant to avoid accessing memory to read the constant and instead copy the value of the constant throughout the compiled program.

## `sizeof`

If you are curious how much space something takes in memory, use `sizeof`:

```mw
sizeof object
```

Or, for the size of anything of a certain type:

```mw
sizeof(type)
```

The two expressions above evaluate to the size of the object (or type) specified, in bytes. The return type is `size_t` (defined in the header `stddef.h`), which is an unsigned integer large enough to represent any possible object size.

This is not a function; when your program is compiled, the expression is replaced with a constant number of bytes. The C standard does not set in stone the data type sizes described earlier, but your compiler knows how much space each type takes on your system, and uses that knowledge to replace uses of `sizeof`.

## `static`

When you declare a local variable as `static`, it is created just like any other variable. However, when the variable goes out of scope—the block it was local to exits—the variable stays in memory, retaining its value. The variable stays in memory until the program ends. While this behavior resembles that of global variables, static variables still obey scope rules and therefore cannot be accessed outside of their scope. This is called *static storage duration*.

Variables declared `static` are initialized to zero by default. They can be initialized explicitly on declaration to any constant value. The initialization is made just once, at compile time.

Consider this example:

| (Example) | #include <stdio.h> void up(void) { /* k is set to 0 when the program starts. The line is then "ignored" * for the rest of the program (i.e. k is not set to 0 every time up() * is called) */ static int k = 0; k++; printf("up() called. k = %2d\n", k); } void down(void) { static int k = 0; k--; printf("down() called. k = %2d\n", k); } int main(void) { int i; for (i = 0; i < 3; i++) up(); for (i = 0; i < 2; i++) down(); return 0; } Output: up() called. k = 1 up() called. k = 2 up() called. k = 3 down() called. k = -1 down() called. k = -2 |
|---|---|

The `k` variables retain their value, but they are two different variables, one in each of their scopes.

## Other modifiers

Included here, for completeness, are more of the modifiers that standard C provides. *volatile* is more of interest to advanced programmers. *register* is deprecated and generally not of interest to either beginning or advanced programmers.

### volatile

**`volatile`** is a special type of modifier which informs the compiler that the value of the variable may be changed by external entities other than the program itself. This is necessary for certain programs compiled with optimizations – if a variable were not defined `volatile` then the compiler may assume that certain operations involving the variable are safe to optimize away when in fact they aren't. *volatile* is particularly relevant when working with embedded systems (where a program may not have complete control of a variable) and multi-threaded applications.

### auto

`**auto**` is a modifier which specifies an "automatic" variable that is automatically created when in scope and destroyed when out of scope. If you think this sounds like pretty much what you've been doing all along when you declare a variable, you're right: all declared items within a block are implicitly "automatic". For this reason, the *auto* keyword is more like the answer to a trivia question than a useful modifier, and there are lots of very competent programmers that are unaware of its existence.

### register

**`register`** is a hint to the compiler to attempt to optimize the storage of the given variable by storing it in a register of the computer's CPU when the program is run. Most optimizing compilers do this anyway, so use of this keyword is often unnecessary. In fact, ANSI C states that a compiler can ignore this keyword if it so desires – and many do. Microsoft Visual C++ is an example of an implementation that completely ignores the *register* keyword.
