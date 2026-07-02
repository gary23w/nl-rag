---
title: "The GNU Awk User’s Guide (part 15/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 15/38
---

# The GNU Awk User’s Guide

When run, this program produces the following output:

```
At level 4, index 3 is not found in a
At level 4, index 4 is found in a

At level 3, index 2 is not found in a
At level 3, index 3 is found in a

At level 2, index 1 is not found in a
At level 2, index 2 is found in a
```

#### 9.2.3.3 Passing Function Arguments by Value Or by Reference

In `awk`, when you declare a function, there is no way to declare explicitly whether the arguments are passed *by value* or *by reference*.

Instead, the passing convention is determined at runtime when the function is called, according to the following rule: if the argument is an array variable, then it is passed by reference. Otherwise, the argument is passed by value.

Passing an argument by value means that when a function is called, it is given a *copy* of the value of this argument. The caller may use a variable as the expression for the argument, but the called function does not know this—it only knows what value the argument had. For example, if you write the following code:

```
foo = "bar"
z = myfunc(foo)
```

then you should not think of the argument to `myfunc()` as being “the variable `foo`.” Instead, think of the argument as the string value `"bar"`. If the function `myfunc()` alters the values of its local variables, this has no effect on any other variables. Thus, if `myfunc()` does this:

```
function myfunc(str)
{
   print str
   str = "zzz"
   print str
}
```

to change its first argument variable `str`, it does *not* change the value of `foo` in the caller. The role of `foo` in calling `myfunc()` ended when its value (`"bar"`) was computed. If `str` also exists outside of `myfunc()`, the function body cannot alter this outer value, because it is shadowed during the execution of `myfunc()` and cannot be seen or changed from there.

However, when arrays are the parameters to functions, they are *not* copied. Instead, the array itself is made available for direct manipulation by the function. This is usually termed *call by reference*. Changes made to an array parameter inside the body of a function *are* visible outside that function.

> **NOTE:** Changing an array parameter inside a function can be very dangerous if you do not watch what you are doing. For example:
> 
> ```
> function changeit(array, ind, nvalue)
> {
>      array[ind] = nvalue
> }
> 
> BEGIN {
>     a[1] = 1; a[2] = 2; a[3] = 3
>     changeit(a, 2, "two")
>     printf "a[1] = %s, a[2] = %s, a[3] = %s\n",
>             a[1], a[2], a[3]
> }
> ```
> 
> prints ‘a[1] = 1, a[2] = two, a[3] = 3’, because `changeit()` stores `"two"` in the second element of `a`.

#### 9.2.3.4 Other Points About Calling Functions

Some `awk` implementations allow you to call a function that has not been defined. They only report a problem at runtime, when the program actually tries to call the function. For example:

```
BEGIN {
    if (0)
        foo()
    else
        bar()
}
function bar() { ... }
# note that `foo' is not defined
```

Because the ‘if’ statement will never be true, it is not really a problem that `foo()` has not been defined. Usually, though, it is a problem if a program calls an undefined function.

If --lint is specified (see Command-Line Options), `gawk` reports calls to undefined functions.

Some `awk` implementations generate a runtime error if you use either the `next` statement or the `nextfile` statement (see The `next` Statement, and see The `nextfile` Statement) inside a user-defined function. `gawk` does not have this limitation.

You can call a function and pass it more parameters than it was declared with, like so:

```
function foo(p1, p2)
{
    ...
}

BEGIN {
    foo(1, 2, 3, 4)
}
```

Doing so is bad practice, however. The called function cannot do anything with the additional values being passed to it, so `awk` evaluates the expressions but then just throws them away.

More importantly, such a call is confusing for whoever will next read your program.67 Function parameters generally are input items that influence the computation performed by the function. Calling a function with more parameters than it accepts gives the false impression that those values are important to the function, when in fact they are not.

Because this is such a bad practice, `gawk` *unconditionally* issues a warning whenever it executes such a function call. (If you don’t like the warning, fix your code! It’s incorrect, after all.)

#### 9.2.4 The `return` Statement

As seen in several earlier examples, the body of a user-defined function can contain a `return` statement. This statement returns control to the calling part of the `awk` program. It can also be used to return a value for use in the rest of the `awk` program. It looks like this:

```
return [expression]
```

The *expression* part is optional. Due most likely to an oversight, POSIX does not define what the return value is if you omit the *expression*. Technically speaking, this makes the returned value undefined, and therefore, unpredictable. In practice, though, all versions of `awk` simply return the null string, which acts like zero if used in a numeric context.

A `return` statement without an *expression* is assumed at the end of every function definition. So, if control reaches the end of the function body, then technically the function returns an unpredictable value. In practice, it returns the empty string. `awk` does *not* warn you if you use the return value of such a function.

Sometimes, you want to write a function for what it does, not for what it returns. Such a function corresponds to a `void` function in C, C++, or Java, or to a `procedure` in Ada. Thus, it may be appropriate to not return any value; simply bear in mind that you should not be using the return value of such a function.

The following is an example of a user-defined function that returns a value for the largest number among the elements of an array:

```
function maxelt(vec,   i, ret)
{
     for (i in vec) {
          if (ret == "" || vec[i] > ret)
               ret = vec[i]
     }
     return ret
}
```

You call `maxelt()` with one argument, which is an array name. The local variables `i` and `ret` are not intended to be arguments; there is nothing to stop you from passing more than one argument to `maxelt()` but the results would be strange. The extra space before `i` in the function parameter list indicates that `i` and `ret` are local variables. You should follow this convention when defining functions.

The following program uses the `maxelt()` function. It loads an array, calls `maxelt()`, and then reports the maximum number in that array:

```
function maxelt(vec,   i, ret)
{
     for (i in vec) {
          if (ret == "" || vec[i] > ret)
               ret = vec[i]
     }
     return ret
}
```

```
# Load all fields of each record into nums.
{
     for(i = 1; i <= NF; i++)
          nums[NR, i] = $i
}
```

```
END {
     print maxelt(nums)
}
```

Given the following input:

```
 1 5 23 8 16
44 3 5 2 8 26
256 291 1396 2962 100
-6 467 998 1101
99385 11 0 225
```

the program reports (predictably) that 99,385 is the largest value in the array.

### 9.3 Variable Typing Is Dynamic

> *It’s a desert topping! It’s a floor wax!*

—

Saturday Night Live (back when it used to be funny)

`awk` is a very fluid language. It is possible that `awk` can’t tell if an identifier represents a scalar variable or an array until runtime.

#### 9.3.1 Dynamic Typing In Standard `awk`

Let’s first discuss standard `awk`. Here is an annotated sample program:

```
function foo(a)
{
    a[1] = 1   # parameter is an array
}

BEGIN {
    b = 1
    foo(b)  # invalid: fatal type mismatch

    foo(x)  # x uninitialized, becomes an array dynamically
    x = 1   # now not allowed, runtime error
}
```

In this example, the first call to `foo()` generates a fatal error, so `awk` will not report the second error. If you comment out that call, though, then `awk` does report the second error.

Here is a more extreme example:

```
BEGIN {
    funky(a)
    if (A == 0)
        print "<" a ">"
    else
        print a[1]
}

function funky(arr)
{
    if (A == 0)
        arr = 1
    else
        arr[1] = 1
}
```

Here, the function uses its parameter differently depending upon the value of the global variable `A`. If `A` is zero, the parameter `arr` is treated as a scalar. Otherwise it’s treated as an array.

There are two ways this program might behave. `awk` could notice that in the main program, `a` is subscripted, and so mark it as an array before the program even begins to run. BWK `awk`, `mawk`, and possibly others do this:

```
$ nawk -v A=0 -f funky.awk
error→ nawk: can't assign to a; it's an array name.
error→  source line number 11
$ nawk -v A=1 -f funky.awk
-| 1
```

Or `awk` could wait until runtime to set the type of `a`. In this case, since `a` was never used before being passed to the function, how the function uses it forces the type to be resolved to either scalar or array. `gawk` and the MKS `awk` do this:

```
$ gawk -v A=0 -f funky.awk
-| <>
$ gawk -v A=1 -f funky.awk 
-| 1
```

POSIX does not specify the correct behavior, so be aware that different implementations work differently.

#### 9.3.2 Dynamic Typing In `gawk`

> *Hc Svnt Dracones* (“Here be dragons”)

—

The Lenox Globe

Things in `gawk` can be a little more unexpected. Because `gawk` allows arrays of arrays, the same dynamic typing can be applied to array elements that have been created but not used.

```
BEGIN {
    funky(a[1])
    if (A == 0)
        print "<" a[1] ">"
    else
        print a[1][1]
}

function funky(arr)
{
    if (A == 0)
        arr = 1
    else
        arr[1] = 1
}
```

When run, the results are the same as in the earlier case:

```
$ gawk -v A=0 -f funky2.awk
-| <>
$ gawk -v A=1 -f funky2.awk
-| 1
```

The `typeof()` function provides us a “window” into `gawk`’s inner workings. Let’s see how using a variable or array element can change its type dynamically. Let’s start with using a variable as a scalar:

```
BEGIN {
    print typeof(a)         # we don't know what a is yet
    printf("a = %d\n", a)   # use it as a scalar
    print typeof(a)         # now we know it's not an array
}
```

When run:

```
$ gawk -f typing1.awk
-| untyped
-| a = 0
-| unassigned
```

Initially, `a` is `untyped`, since we don’t know yet if it’s an array or scalar. After using it in the call to `printf()`, we know it’s a scalar. However, since it was never given a concrete value (number, string, or regexp), its type is `unassigned`.

`gawk` is peculiar in that we can do the same thing, but change `a` into an array:

```
BEGIN {
    print typeof(a)               # we don't know what a is yet
    a[1]                          # make a into an array
    print typeof(a[1])            # but we don't know what a[1] is yet
    printf("a[1] = %d\n", a[1])   # use it as a scalar
    print typeof(a[1])            # now we know it's not an array
}
```

When run:

```
$ gawk -f typing2.awk
-| untyped
-| untyped
-| a[1] = 0
-| unassigned
```

Normally, passing a variable that has never been used to a built-in function causes it to become a scalar variable (`unassigned`). However, `isarray()` and `typeof()` are different; they do not change their arguments from `untyped` to `unassigned`.

As we saw, this applies to both variables denoted by simple identifiers and array elements that come into existence simply by referencing them:

```
$ gawk 'BEGIN { print typeof(x) }'
-| untyped
$ gawk 'BEGIN { print typeof(x["foo"]) }'
-| untyped
```

Note that prior to version 5.2, array elements that come into existence simply by referencing them were different, they were automatically forced to be scalars:

```
$ gawk-5.1.1 'BEGIN { print typeof(x) }'
-| untyped
$ gawk-5.1.1 'BEGIN { print typeof(x["foo"]) }'
-| unassigned
```

To sum up, variables and array elements get their nature (array or scalar) “fixed” upon first use. This can lead to some weird cases, and it is best to avoid taking advantage of `gawk`’s dynamic nature, other than in the standard manner of passing untyped variables and array elements as function parameters.

### 9.4 A Note On Shadowed Variables

This section discusses some aspects of variable shadowing. Feel free to skip it upon first reading.

The “shadowing” concept is important to know for several reasons.

***Name confusion***

Using global identifiers (names) locally can lead to very difficult debugging, it complicates writing, reading and maintaining source code, and it decreases the portability, (sharing or reuse) of a library of `awk` functions.

***Preventing shadowing in functions***

It is a best practice to consistently use a naming convention, such as “global variable and function names start with a capital letter and local names begin with lowercase one.” This also makes programs easier to follow (see Naming Library Function Global Variables).

***Circumventing shadow restrictions in functions***

The `gawk` extension `SYMTAB` provides indirect access to global variables that are or may be shadowed (see `SYMTAB` in Built-in Variables That Convey Information). For example:

```
...
foo = "global value"
...

function test(x,   foo)
{
    # use global value of foo as default
    foo = (x > 0) ? SYMTAB["foo"] : "local value"
    ...
}
```

***Solving complex shadowing problems***

The `gawk` namespace extension provides robust handling of potential name collisions with global variables and functions (see Namespaces in `gawk`). Namespaces are useful to prevent shadowing by providing identifiers that are common to a group of functions and effectively shadowed from being referenced by global functions (See `FUNCTAB` in Built-in Variables That Convey Information.)

Finally, a shadowing caveat: Variables local to a function are *not* “global” to anything. `SYMTAB` elements refer to all *global* variables and arrays, but not to *local* variables and arrays. If a function `A(argA, localA)` calls another function `B()`, the two variables local to `A()` are *not* accessible in function `B()` or any other function. The global/local distinction is also important to remember when passing arguments to a function called indirectly (see Indirect Function Calls).

### 9.5 Indirect Function Calls

This section describes an advanced, `gawk`-specific extension.

Often, you may wish to defer the choice of function to call until runtime. For example, you may have different kinds of records, each of which should be processed differently.

Normally, you would have to use a series of `if`-`else` statements to decide which function to call. By using *indirect* function calls, you can specify the name of the function to call as a string variable, and then call the function. Let’s look at an example.

Suppose you have a file with your test scores for the classes you are taking, and you wish to get the sum and the average of your test scores. The first field is the class name. The following fields are the functions to call to process the data, up to a “marker” field ‘data:’. Following the marker, to the end of the record, are the various numeric test scores.

Here is the initial file:

```
Biology_101 sum average data: 87.0 92.4 78.5 94.9
Chemistry_305 sum average data: 75.2 98.3 94.7 88.2
English_401 sum average data: 100.0 95.6 87.1 93.4
```

To process the data, you might write initially:

```
{
    class = $1
    for (i = 2; $i != "data:"; i++) {
        if ($i == "sum")
            sum()   # processes the whole record
        else if ($i == "average")
            average()
        ...           # and so on
    }
}
```

This style of programming works, but can be awkward. With *indirect* function calls, you tell `gawk` to use the *value* of a variable as the *name* of the function to call.

The syntax is similar to that of a regular function call: an identifier immediately followed by an opening parenthesis, any arguments, and then a closing parenthesis, with the addition of a leading ‘@’ character:

```
the_function = "sum"
result = @the_function()   # calls the sum() function
```

Here is a full program that processes the previously shown data, using indirect function calls:

```
# indirectcall.awk --- Demonstrate indirect function calls

# average --- return the average of the values in fields $first - $last

function average(first, last,   sum, i)
{
    sum = 0;
    for (i = first; i <= last; i++)
        sum += $i

    return sum / (last - first + 1)
}

# sum --- return the sum of the values in fields $first - $last

function sum(first, last,   ret, i)
{
    ret = 0;
    for (i = first; i <= last; i++)
        ret += $i

    return ret
}
```

These two functions expect to work on fields; thus, the parameters `first` and `last` indicate where in the fields to start and end. Otherwise, they perform the expected computations and are not unusual:

```
# For each record, print the class name and the requested statistics
{
    class_name = $1
    gsub(/_/, " ", class_name)  # Replace _ with spaces

    # find start
    for (i = 1; i <= NF; i++) {
        if ($i == "data:") {
            start = i + 1
            break
        }
    }

    printf("%s:\n", class_name)
    for (i = 2; $i != "data:"; i++) {
        the_function = $i
        printf("\t%s: <%s>\n", $i, @the_function(start, NF) "")
    }
    print ""
}
```

This is the main processing for each record. It prints the class name (with underscores replaced with spaces). It then finds the start of the actual data, saving it in `start`. The last part of the code loops through each function name (from `$2` up to the marker, ‘data:’), calling the function named by the field. The indirect function call itself occurs as a parameter in the call to `printf`. (The `printf` format string uses ‘%s’ as the format specifier so that we can use functions that return strings, as well as numbers. Note that the result from the indirect call is concatenated with the empty string, in order to force it to be a string value.)

Here is the result of running the program:

```
$ gawk -f indirectcall.awk class_data1
-| Biology 101:
-|     sum: <352.8>
-|     average: <88.2>
-|
-| Chemistry 305:
-|     sum: <356.4>
-|     average: <89.1>
-|
-| English 401:
-|     sum: <376.1>
-|     average: <94.025>
```

The ability to use indirect function calls is more powerful than you may think at first. The C and C++ languages provide “function pointers,” which are a mechanism for calling a function chosen at runtime. One of the most well-known uses of this ability is the C `qsort()` function, which sorts an array using the famous “quicksort” algorithm (see the Wikipedia article for more information). To use this function, you supply a pointer to a comparison function. This mechanism allows you to sort arbitrary data in an arbitrary fashion.

We can do something similar using `gawk`, like this:

```
# quicksort.awk --- Quicksort algorithm, with user-supplied
#                   comparison function

# quicksort --- C.A.R. Hoare's quicksort algorithm. See Wikipedia
#               or almost any algorithms or computer science text.

function quicksort(data, left, right, less_than,    i, last)
{
    if (left >= right)  # do nothing if array contains fewer
        return          # than two elements

    quicksort_swap(data, left, int((left + right) / 2))
    last = left
    for (i = left + 1; i <= right; i++)
        if (@less_than(data[i], data[left]))
            quicksort_swap(data, ++last, i)
    quicksort_swap(data, left, last)
    quicksort(data, left, last - 1, less_than)
    quicksort(data, last + 1, right, less_than)
}

# quicksort_swap --- helper function for quicksort, should really be inline

function quicksort_swap(data, i, j,      temp)
{
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
}
```

The `quicksort()` function receives the `data` array, the starting and ending indices to sort (`left` and `right`), and the name of a function that performs a “less than” comparison. It then implements the quicksort algorithm.

To make use of the sorting function, we return to our previous example. The first thing to do is write some comparison functions:

```
# num_lt --- do a numeric less than comparison

function num_lt(left, right)
{
    return ((left + 0) < (right + 0))
}
```

```
# num_ge --- do a numeric greater than or equal to comparison

function num_ge(left, right)
{
    return ((left + 0) >= (right + 0))
}
```

The `num_ge()` function is needed to perform a descending sort; when used to perform a “less than” test, it actually does the opposite (greater than or equal to), which yields data sorted in descending order.

Next comes a sorting function. It is parameterized with the starting and ending field numbers and the comparison function. It builds an array with the data and calls `quicksort()` appropriately, and then formats the results as a single string:

```
# do_sort --- sort the data according to `compare'
#             and return it as a string

function do_sort(first, last, compare,      data, i, retval)
{
    delete data
    for (i = 1; first <= last; first++) {
        data[i] = $first
        i++
    }

    quicksort(data, 1, i-1, compare)

    retval = data[1]
    for (i = 2; i in data; i++)
        retval = retval " " data[i]

    return retval
}
```

Finally, the two sorting functions call `do_sort()`, passing in the names of the two comparison functions:

```
# sort --- sort the data in ascending order and return it as a string

function sort(first, last)
{
    return do_sort(first, last, "num_lt")
}
```

```
# rsort --- sort the data in descending order and return it as a string

function rsort(first, last)
{
    return do_sort(first, last, "num_ge")
}
```

Here is an extended version of the data file:

```
Biology_101 sum average sort rsort data: 87.0 92.4 78.5 94.9
Chemistry_305 sum average sort rsort data: 75.2 98.3 94.7 88.2
English_401 sum average sort rsort data: 100.0 95.6 87.1 93.4
```

Finally, here are the results when the enhanced program is run:

```
$ gawk -f quicksort.awk -f indirectcall.awk class_data2
-| Biology 101:
-|     sum: <352.8>
-|     average: <88.2>
-|     sort: <78.5 87.0 92.4 94.9>
-|     rsort: <94.9 92.4 87.0 78.5>
-|
-| Chemistry 305:
-|     sum: <356.4>
-|     average: <89.1>
-|     sort: <75.2 88.2 94.7 98.3>
-|     rsort: <98.3 94.7 88.2 75.2>
-|
-| English 401:
-|     sum: <376.1>
-|     average: <94.025>
-|     sort: <87.1 93.4 95.6 100.0>
-|     rsort: <100.0 95.6 93.4 87.1>
```

Another example where indirect functions calls are useful can be found in processing arrays. This is described in Traversing Arrays of Arrays.

Remember that you must supply a leading ‘@’ in front of an indirect function call.

Starting with version 4.1.2 of `gawk`, indirect function calls may also be used with built-in functions and with extension functions (see Writing Extensions for `gawk`). There are some limitations when calling built-in functions indirectly, as follows.

- You cannot pass a regular expression constant to a built-in function through an indirect function call. This applies to the `sub()`, `gsub()`, `gensub()`, `match()`, `split()` and `patsplit()` functions. However, you can pass a strongly typed regexp constant (see Strongly Typed Regexp Constants).
- If calling `sub()` or `gsub()`, you may only pass two arguments, since those functions are unusual in that they update their third argument. This means that `$0` will be updated.
- You cannot indirectly call built-in functions that can take `$0` as a default parameter; you must supply an argument instead. For example, you must pass an argument to `length()` if calling it indirectly.
- Calling a built-in function indirectly with the wrong number of arguments for that function causes a fatal error. For example, calling `length()` with two arguments. These errors are found at runtime instead of when `gawk` parses your program, since `gawk` doesn’t know until runtime if you have passed the correct number of arguments or not.

`gawk` does its best to make indirect function calls efficient. For example, in the following case:

```
for (i = 1; i <= n; i++)
    @the_function()
```

`gawk` looks up the actual function to call only once.

### 9.6 Summary

- `awk` provides built-in functions and lets you define your own functions.
- POSIX `awk` provides three kinds of built-in functions: numeric, string, and I/O. `gawk` provides functions that sort arrays, work with values representing time, do bit manipulation, determine variable type (array versus scalar), and internationalize and localize programs. `gawk` also provides several extensions to some of standard functions, typically in the form of additional arguments.
- Functions accept zero or more arguments and return a value. The expressions that provide the argument values are completely evaluated before the function is called. Order of evaluation is not defined. The return value can be ignored.
- The handling of backslash in `sub()` and `gsub()` is not simple. It is more straightforward in `gawk`’s `gensub()` function, but that function still requires care in its use.
- User-defined functions provide important capabilities but come with some syntactic inelegancies. In a function call, there cannot be any space between the function name and the opening left parenthesis of the argument list. Also, there is no provision for local variables, so the convention is to add extra parameters, and to separate them visually from the real parameters by extra whitespace.
- User-defined functions may call other user-defined (and built-in) functions and may call themselves recursively. Function parameters “hide” any global variables of the same names. You cannot use the name of a reserved variable (such as `ARGC`) as the name of a parameter in user-defined functions.
- Scalar values are passed to user-defined functions by value. Array parameters are passed by reference; any changes made by the function to array parameters are thus visible after the function has returned.
- Use the `return` statement to return from a user-defined function. An optional expression becomes the function’s return value. Only scalar values may be returned by a function.
- If a variable that has never been used is passed to a user-defined function, how that function treats the variable can set its nature: either scalar or array.
- `gawk` is even more fluid in its designation of variables and array elements as scalars or arrays. However, this can lead to weird situations, so you should tread carefully.
- `gawk` provides indirect function calls using a special syntax. By setting a variable to the name of a function, you can determine at runtime what function will be called at that point in the program. This is equivalent to function pointers in C and C++.

# Part II: Problem Solving with `awk`
