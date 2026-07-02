---
title: "The GNU Awk User’s Guide (part 21/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 21/38
---

## 12 Advanced Features of `gawk`

> *Write documentation as if whoever reads it is a violent psychopath who knows where you live.*

—

Steve English, as quoted by Peter Langston

This chapter discusses advanced features in `gawk`. It’s a bit of a “grab bag” of items that are otherwise unrelated to each other. First, we look at a command-line option that allows `gawk` to recognize nondecimal numbers in input data, not just in `awk` programs. Then, `gawk`’s special features for sorting arrays are presented. Next, two-way I/O, discussed briefly in earlier parts of this Web page, is described in full detail, along with the basics of TCP/IP networking. We then see how `gawk` can *profile* an `awk` program, making it possible to tune it for performance. Next, we present an experimental feature that allows you to preserve the values of `awk` variables and arrays between runs of `gawk`. Finally, we discuss the philosophy behind `gawk`’s extension mechanism.

Additional advanced features are discussed in separate chapters of their own:

- Internationalization with `gawk`, discusses how to internationalize your `awk` programs, so that they can speak multiple national languages.
- Debugging `awk` Programs, describes `gawk`’s built-in command-line debugger for debugging `awk` programs.
- Arithmetic and Arbitrary-Precision Arithmetic with `gawk`, describes how you can use `gawk` to perform arbitrary-precision arithmetic.
- Writing Extensions for `gawk`, discusses the ability to dynamically add new built-in functions to `gawk`.

### 12.1 Allowing Nondecimal Input Data

If you run `gawk` with the --non-decimal-data option, you can have nondecimal values in your input data:

```
$ echo 0123 123 0x123 |
> gawk --non-decimal-data '{ printf "%d, %d, %d\n", $1, $2, $3 }'
-| 83, 123, 291
```

For this feature to work, write your program so that `gawk` treats your data as numeric:

```
$ echo 0123 123 0x123 | gawk '{ print $1, $2, $3 }'
-| 0123 123 0x123
```

The `print` statement treats its expressions as strings. Although the fields can act as numbers when necessary, they are still strings, so `print` does not try to treat them numerically. You need to add zero to a field to force it to be treated as a number. For example:

```
$ echo 0123 123 0x123 | gawk --non-decimal-data '
> { print $1, $2, $3
>   print $1 + 0, $2 + 0, $3 + 0 }'
-| 0123 123 0x123
-| 83 123 291
```

In Octal and Hexadecimal Numbers, we described how octal and hexadecimal values may be used in program source code to represent numeric values. That section also discussed hexadecimal floating-point values.

As of version 5.4 of `gawk`, the --non-decimal-data option and the `strtonum()` function accept such values and convert them correctly. For example:

```
$ echo 0x1p-3 | ./gawk -n '{ print $1 + 0 }'
-| 0.125
```

Because it is common to have decimal data with leading zeros, and because allowing nondecimal data could lead to surprising results, the default is to leave it disabled. If you want it, you must explicitly request it.

> **CAUTION:** *Use of this option is not recommended.* It can break old programs very badly. Instead, use the `strtonum()` function to convert your data (see String-Manipulation Functions). This makes your programs easier to write and easier to read, and leads to less surprising results.

### 12.2 Boolean Typed Values

Scalar values in `awk` are either numbers or strings. `gawk` also supports values of type `regexp` (see Strongly Typed Regexp Constants).

As described in True and False in `awk`, Boolean values in `awk` don’t have a separate type: a value counts as “true” if it is nonzero or non-null, and as “false” otherwise.

When interchanging data with languages that do have a real Boolean type, using a standard format such as JSON or XML, the lack of a true Boolean type in `awk` is problematic. (See, for example, the `json` extension provided by the `gawkextlib` project.)

It’s easy to import Boolean data into `awk`, but then the fact that it was originally Boolean is lost. Exporting data is even harder; there’s no way to indicate that a value is really Boolean.

To solve this problem, `gawk` provides a function named `mkbool()`. It takes one argument, which is any `awk` expression, and it returns a value of Boolean type.

The returned values are normal `awk` numeric values, with values of either one or zero, depending upon the truth value of the original expression passed in the call to `mkbool()`.

The `typeof()` function (see Getting Type Information) returns `"number|bool"` for these values.

Thus Boolean-typed values *are* numbers as far as `gawk` is concerned, except that extension code can treat them as Booleans if desired.

While it would have been possible to add two new built-in variables of Boolean type named `TRUE` and `FALSE`, doing so would undoubtedly have broken many existing `awk` programs. Instead, having a “generator” function that creates Boolean values gives flexibility, without breaking as much existing code.

### 12.3 Controlling Array Traversal and Array Sorting

`gawk` lets you control the order in which a ‘for (*indx* in *array*)’ loop traverses an array.

In addition, two built-in functions, `asort()` and `asorti()`, let you sort arrays based on the array values and indices, respectively. These two functions also provide control over the sorting criteria used to order the elements during sorting.

#### 12.3.1 Controlling Array Traversal

By default, the order in which a ‘for (*indx* in *array*)’ loop scans an array is not defined; it is generally based upon the internal implementation of arrays inside `awk`.

Often, though, it is desirable to be able to loop over the elements in a particular order that you, the programmer, choose. `gawk` lets you do this.

Using Predefined Array Scanning Orders with `gawk` describes how you can assign special, predefined values to `PROCINFO["sorted_in"]` in order to control the order in which `gawk` traverses an array during a `for` loop.

In addition, the value of `PROCINFO["sorted_in"]` can be a function name.86 This lets you traverse an array based on any custom criterion. The array elements are ordered according to the return value of this function. The comparison function should be defined with at least four arguments:

```
function comp_func(i1, v1, i2, v2)
{
    compare elements 1 and 2 in some fashion
    return < 0; 0; or > 0
}
```

Here, `i1` and `i2` are the indices, and `v1` and `v2` are the corresponding values of the two elements being compared. Either `v1` or `v2`, or both, can be arrays if the array being traversed contains subarrays as values. (See Arrays of Arrays for more information about subarrays.) The three possible return values are interpreted as follows:

**`comp_func(i1, v1, i2, v2) < 0`**

Index `i1` comes before index `i2` during loop traversal.

**`comp_func(i1, v1, i2, v2) == 0`**

Indices `i1` and `i2` come together, but the relative order with respect to each other is undefined.

**`comp_func(i1, v1, i2, v2) > 0`**

Index `i1` comes after index `i2` during loop traversal.

Our first comparison function can be used to scan an array in numerical order of the indices:

```
function cmp_num_idx(i1, v1, i2, v2)
{
     # numerical index comparison, ascending order
     return (i1 - i2)
}
```

Our second function traverses an array based on the string order of the element values rather than by indices:

```
function cmp_str_val(i1, v1, i2, v2)
{
    # string value comparison, ascending order
    v1 = v1 ""
    v2 = v2 ""
    if (v1 < v2)
        return -1
    return (v1 != v2)
}
```

The third comparison function makes all numbers, and numeric strings without any leading or trailing spaces, come out first during loop traversal:

```
function cmp_num_str_val(i1, v1, i2, v2,   n1, n2)
{
     # numbers before string value comparison, ascending order
     n1 = v1 + 0
     n2 = v2 + 0
     if (n1 == v1)
         return (n2 == v2) ? (n1 - n2) : -1
     else if (n2 == v2)
         return 1
     return (v1 < v2) ? -1 : (v1 != v2)
}
```

Here is a main program to demonstrate how `gawk` behaves using each of the previous functions:

```
BEGIN {
    data["one"] = 10
    data["two"] = 20
    data[10] = "one"
    data[100] = 100
    data[20] = "two"

    f[1] = "cmp_num_idx"
    f[2] = "cmp_str_val"
    f[3] = "cmp_num_str_val"
    for (i = 1; i <= 3; i++) {
        printf("Sort function: %s\n", f[i])
        PROCINFO["sorted_in"] = f[i]
        for (j in data)
            printf("\tdata[%s] = %s\n", j, data[j])
        print ""
    }
}
```

Here are the results when the program is run:

```
$ gawk -f compdemo.awk
-| Sort function: cmp_num_idx      Sort by numeric index
-|     data[two] = 20
-|     data[one] = 10              Both strings are numerically zero
-|     data[10] = one
-|     data[20] = two
-|     data[100] = 100
-|
-| Sort function: cmp_str_val      Sort by element values as strings
-|     data[one] = 10
-|     data[100] = 100             String 100 is less than string 20
-|     data[two] = 20
-|     data[10] = one
-|     data[20] = two
-|
-| Sort function: cmp_num_str_val  Sort all numeric values before all strings
-|     data[one] = 10
-|     data[two] = 20
-|     data[100] = 100
-|     data[10] = one
-|     data[20] = two
```

Consider sorting the entries of a GNU/Linux system password file according to login name. The following program sorts records by a specific field position and can be used for this purpose:

```
# passwd-sort.awk --- simple program to sort by field position
# field position is specified by the global variable POS

function cmp_field(i1, v1, i2, v2)
{
    # comparison by value, as string, and ascending order
    return v1[POS] < v2[POS] ? -1 : (v1[POS] != v2[POS])
}

{
    for (i = 1; i <= NF; i++)
        a[NR][i] = $i
}
```

```
END {
    PROCINFO["sorted_in"] = "cmp_field"
```

```
    if (POS < 1 || POS > NF)
        POS = 1

    for (i in a) {
        for (j = 1; j <= NF; j++)
            printf("%s%c", a[i][j], j < NF ? ":" : "")
        print ""
    }
}
```

The first field in each entry of the password file is the user’s login name, and the fields are separated by colons. Each record defines a subarray, with each field as an element in the subarray. Running the program produces the following output:

```
$ gawk -v POS=1 -F: -f sort.awk /etc/passwd
-| adm:x:3:4:adm:/var/adm:/sbin/nologin
-| apache:x:48:48:Apache:/var/www:/sbin/nologin
-| avahi:x:70:70:Avahi daemon:/:/sbin/nologin
...
```

The comparison should normally always return the same value when given a specific pair of array elements as its arguments. If inconsistent results are returned, then the order is undefined. This behavior can be exploited to introduce random order into otherwise seemingly ordered data:

```
function cmp_randomize(i1, v1, i2, v2)
{
    # random order (caution: this may never terminate!)
    return (2 - 4 * rand())
}
```

As already mentioned, the order of the indices is arbitrary if two elements compare equal. This is usually not a problem, but letting the tied elements come out in arbitrary order can be an issue, especially when comparing item values. The partial ordering of the equal elements may change the next time the array is traversed, if other elements are added to or removed from the array. One way to resolve ties when comparing elements with otherwise equal values is to include the indices in the comparison rules. Note that doing this may make the loop traversal less efficient, so consider it only if necessary. The following comparison functions force a deterministic order, and are based on the fact that the (string) indices of two elements are never equal:

```
function cmp_numeric(i1, v1, i2, v2)
{
    # numerical value (and index) comparison, descending order
    return (v1 != v2) ? (v2 - v1) : (i2 - i1)
}
```

```
function cmp_string(i1, v1, i2, v2)
{
    # string value (and index) comparison, descending order
    v1 = v1 i1
    v2 = v2 i2
    return (v1 > v2) ? -1 : (v1 != v2)
}
```

A custom comparison function can often simplify ordered loop traversal, and the sky is really the limit when it comes to designing such a function.

When string comparisons are made during a sort, either for element values where one or both aren’t numbers, or for element indices handled as strings, the value of `IGNORECASE` (see Predefined Variables) controls whether the comparisons treat corresponding upper- and lowercase letters as equivalent or distinct.

Another point to keep in mind is that in the case of subarrays, the element values can themselves be arrays; a production comparison function should use the `isarray()` function (see Getting Type Information) to check for this, and choose a defined sorting order for subarrays.

All sorting based on `PROCINFO["sorted_in"]` is disabled in POSIX mode, because the `PROCINFO` array is not special in that case.

As a side note, sorting the array indices before traversing the array has been reported to add a 15% to 20% overhead to the execution time of `awk` programs. For this reason, sorted array traversal is not the default.

#### 12.3.2 Sorting Array Values and Indices with `gawk`

In most `awk` implementations, sorting an array requires writing a `sort()` function. This can be educational for exploring different sorting algorithms, but usually that’s not the point of the program. `gawk` provides the built-in `asort()` and `asorti()` functions (see String-Manipulation Functions) for sorting arrays. For example:

```
populate the array data
n = asort(data)
for (i = 1; i <= n; i++)
    do something with data[i]
```

After the call to `asort()`, the array `data` is indexed from 1 to some number *n*, the total number of elements in `data`. (This count is `asort()`’s return value.) `data[1]` <= `data[2]` <= `data[3]`, and so on. The default comparison is based on the type of the elements (see Variable Typing and Comparison Expressions). All numeric values come before all string values, which in turn come before all subarrays.

An important side effect of calling `asort()` is that *the array’s original indices are irrevocably lost*. As this isn’t always desirable, `asort()` accepts a second argument:

```
populate the array source
n = asort(source, dest)
for (i = 1; i <= n; i++)
    do something with dest[i]
```

In this case, `gawk` copies the `source` array into the `dest` array and then sorts `dest`, destroying its indices. However, the `source` array is not affected.

Often, what’s needed is to sort on the values of the *indices* instead of the values of the elements. To do that, use the `asorti()` function. The interface and behavior are identical to that of `asort()`, except that the index values are used for sorting and become the values of the result array:

```
{ source[$0] = some_func($0) }

END {
    n = asorti(source, dest)
    for (i = 1; i <= n; i++) {
        Work with sorted indices directly:
        do something with dest[i]
        ...
        Access original array via sorted indices:
        do something with source[dest[i]]
    }
}
```

So far, so good. Now it starts to get interesting. Both `asort()` and `asorti()` accept a third string argument to control comparison of array elements. When we introduced `asort()` and `asorti()` in String-Manipulation Functions, we ignored this third argument; however, now is the time to describe how this argument affects these two functions.

Basically, the third argument specifies how the array is to be sorted. There are two possibilities. As with `PROCINFO["sorted_in"]`, this argument may be one of the predefined names that `gawk` provides (see Using Predefined Array Scanning Orders with `gawk`), or it may be the name of a user-defined function (see Controlling Array Traversal).

In the latter case, *the function can compare elements in any way it chooses*, taking into account just the indices, just the values, or both. This is extremely powerful.

Once the array is sorted, `asort()` takes the *values* in their final order and uses them to fill in the result array, whereas `asorti()` takes the *indices* in their final order and uses them to fill in the result array.

> **NOTE:** Copying array indices and elements isn’t expensive in terms of memory. Internally, `gawk` maintains *reference counts* to data. For example, when `asort()` copies the first array to the second one, there is only one copy of the original array elements’ data, even though both arrays use the values.

You may use the same array for both the first and second arguments to `asort()` and `asorti()`. Doing so only makes sense if you are also supplying the third argument, since `awk` doesn’t provide a way to pass that third argument without also passing the first and second ones.

Because `IGNORECASE` affects string comparisons, the value of `IGNORECASE` also affects sorting for both `asort()` and `asorti()`. Note also that the locale’s sorting order does *not* come into play; comparisons are based on character values only.87

The following example demonstrates the use of a comparison function with `asort()`. The comparison function, `case_fold_compare()`, maps both values to lowercase in order to compare them ignoring case.

```
# case_fold_compare --- compare as strings, ignoring case

function case_fold_compare(i1, v1, i2, v2,    l, r)
{
    l = tolower(v1)
```

```
    r = tolower(v2)

    if (l < r)
        return -1
    else if (l == r)
        return 0
    else
        return 1
}
```

And here is the test program for it:

```
# Test program

BEGIN {
    Letters = "abcdefghijklmnopqrstuvwxyz" \
              "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    split(Letters, data, "")

    asort(data, result, "case_fold_compare")

    j = length(result)
    for (i = 1; i <= j; i++) {
        printf("%s", result[i])
        if (i % (j/2) == 0)
            printf("\n")
        else
            printf(" ")
    }
}
```

When run, we get the following:

```
$ gawk -f case_fold_compare.awk
-| A a B b c C D d e E F f g G H h i I J j k K l L M m
-| n N O o p P Q q r R S s t T u U V v w W X x y Y z Z
```

> **NOTE:** “Under the hood,” `gawk` uses the C library `qsort()` function to manage the sorting. `qsort()` can call itself recursively. This means that when you write a comparison function, you should be careful to avoid the use of global variables and arrays; use only local variables and arrays that you declare as additional parameters to the comparison function. Otherwise, you are likely to cause unintentional memory corruption in your global arrays and possibly cause `gawk` itself to fail.

### 12.4 Two-Way Communications with Another Process

It is often useful to be able to send data to a separate program for processing and then read the result. This can always be done with temporary files:

```
# Write the data for processing
tempfile = ("mydata." PROCINFO["pid"])
while (not done with data)
    print data | ("subprogram > " tempfile)
close("subprogram > " tempfile)

# Read the results, remove tempfile when done
while ((getline newdata < tempfile) > 0)
    process newdata appropriately
close(tempfile)
system("rm " tempfile)
```

This works, but not elegantly. Among other things, it requires that the program be run in a directory that cannot be shared among users; for example, /tmp will not do, as another user might happen to be using a temporary file with the same name.88

However, with `gawk`, it is possible to open a *two-way* pipe to another process. The second process is termed a *coprocess*, as it runs in parallel with `gawk`. The two-way connection is created using the ‘|&’ operator (borrowed from the Korn shell, `ksh`):89

```
do {
    print data |& "subprogram"
    "subprogram" |& getline results
} while (data left to process)
close("subprogram")
```

The first time an I/O operation is executed using the ‘|&’ operator, `gawk` creates a two-way pipeline to a child process that runs the other program. Output created with `print` or `printf` is written to the program’s standard input, and output from the program’s standard output can be read by the `gawk` program using `getline`. As is the case with processes started by ‘|’, the subprogram can be any program, or pipeline of programs, that can be started by the shell.

There are some cautionary items to be aware of:

- As the code inside `gawk` currently stands, the coprocess’s standard error goes to the same place that the parent `gawk`’s standard error goes. It is not possible to read the child’s standard error separately.
- I/O buffering may be a problem. `gawk` automatically flushes all output down the pipe to the coprocess. However, if the coprocess does not flush its output, `gawk` may hang when doing a `getline` in order to read the coprocess’s results. This could lead to a situation known as *deadlock*, where each process is waiting for the other one to do something.

It is possible to close just one end of the two-way pipe to a coprocess, by supplying a second argument to the `close()` function of either `"to"` or `"from"` (see Closing Input and Output Redirections). These strings tell `gawk` to close the end of the pipe that sends data to the coprocess or the end that reads from it, respectively.

This is particularly necessary in order to use the system `sort` utility as part of a coprocess; `sort` must read *all* of its input data before it can produce any output. The `sort` program does not receive an end-of-file indication until `gawk` closes the write end of the pipe.

When you have finished writing data to the `sort` utility, you can close the `"to"` end of the pipe, and then start reading sorted data via `getline`. For example:

```
BEGIN {
    command = "LC_ALL=C sort"
    n = split("abcdefghijklmnopqrstuvwxyz", a, "")

    for (i = n; i > 0; i--)
        print a[i] |& command
    close(command, "to")

    while ((command |& getline line) > 0)
        print "got", line
    close(command)
}
```

This program writes the letters of the alphabet in reverse order, one per line, down the two-way pipe to `sort`. It then closes the write end of the pipe, so that `sort` receives an end-of-file indication. This causes `sort` to sort the data and write the sorted data back to the `gawk` program. Once all of the data has been read, `gawk` terminates the coprocess and exits.

As a side note, the assignment ‘LC_ALL=C’ in the `sort` command ensures traditional Unix (ASCII) sorting from `sort`. This is not strictly necessary here, but it’s good to know how to do this.

Be careful when closing the `"from"` end of a two-way pipe; in this case `gawk` waits for the child process to exit, which may cause your program to hang. (Thus, this particular feature is of much less use in practice than being able to close the `"to"` end.)

> **CAUTION:** Normally, it is a fatal error to write to the `"to"` end of a two-way pipe which has been closed, and it is also a fatal error to read from the `"from"` end of a two-way pipe that has been closed.
> 
> You may set `PROCINFO["*command*", "NONFATAL"]` to make such operations become nonfatal. If you do so, you then need to check `ERRNO` after each `print`, `printf`, or `getline`. See Enabling Nonfatal Output, for more information.

You may also use pseudo-ttys (ptys) for two-way communication instead of pipes, if your system supports them. This is done on a per-command basis, by setting a special element in the `PROCINFO` array (see Built-in Variables That Convey Information), like so:

```
command = "sort -nr"           # command, save in convenience variable
PROCINFO[command, "pty"] = 1   # update PROCINFO
print ... |& command           # start two-way pipe
...
```

If your system does not have ptys, or if all the system’s ptys are in use, `gawk` automatically falls back to using regular pipes.

Using ptys usually avoids the buffer deadlock issues described earlier, at some loss in performance. This is because the tty driver buffers and sends data line-by-line. On systems with the `stdbuf` (part of the GNU Coreutils package), you can use that program instead of ptys.
