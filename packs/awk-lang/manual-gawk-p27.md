---
title: "The GNU Awk User’s Guide (part 27/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 27/38
---

# The GNU Awk User’s Guide

**`awk_value_t index;`**

**`awk_value_t value;`**

**`} awk_element_t;`**

The `awk_element_t` is a “flattened” array element. `awk` produces an array of these inside the `awk_flat_array_t` (see the next item). Individual elements may be marked for deletion. New elements must be added individually, one at a time, using the separate API for that purpose. The fields are as follows:

**`struct awk_element *next;`**

This pointer is for the convenience of extension writers. It allows an extension to create a linked list of new elements that can then be added to an array in a loop that traverses the list.

**`enum { … } flags;`**

A set of flag values that convey information between the extension and `gawk`. Currently there is only one: `AWK_ELEMENT_DELETE`. Setting it causes `gawk` to delete the element from the original array upon release of the flattened array.

**`index`**

**`value`**

The index and value of the element, respectively. *All* memory pointed to by `index` and `value` belongs to `gawk`.

**`typedef struct awk_flat_array {`**

**`awk_const void *awk_const opaque1;    /* for use by gawk */`**

**`awk_const void *awk_const opaque2;    /* for use by gawk */`**

**`awk_const size_t count;     /* how many elements */`**

**`awk_element_t elements[1];  /* will be extended */`**

**`} awk_flat_array_t;`**

This is a flattened array. When an extension gets one of these from `gawk`, the `elements` array is of actual size `count`. The `opaque1` and `opaque2` pointers are for use by `gawk`; therefore they are marked `awk_const` so that the extension cannot modify them.

#### 17.4.12.2 Array Functions

The following functions relate to individual array elements:

**`awk_bool_t get_element_count(awk_array_t a_cookie, size_t *count);`**

For the array represented by `a_cookie`, place in `*count` the number of elements it contains. A subarray counts as a single element. Return false if there is an error.

**`awk_bool_t get_array_element(awk_array_t a_cookie,`**

**`const awk_value_t *const index,`**

**`awk_valtype_t wanted,`**

**`awk_value_t *result);`**

For the array represented by `a_cookie`, return in `*result` the value of the element whose index is `index`. `wanted` specifies the type of value you wish to retrieve. Return false if `wanted` does not match the actual type or if `index` is not in the array (see Table 17.2).

The value for `index` can be numeric, in which case `gawk` converts it to a string. Using nonintegral values is possible, but requires that you understand how such values are converted to strings (see Conversion of Strings and Numbers); thus, using integral values is safest.

As with *all* strings passed into `gawk` from an extension, the string value of `index` must come from `gawk_malloc()`, `gawk_calloc()`, or `gawk_realloc()`, and `gawk` releases the storage.

**`awk_bool_t set_array_element(awk_array_t a_cookie,`**

**`const awk_value_t *const index,`**

**`const awk_value_t *const value);`**

In the array represented by `a_cookie`, create or modify the element whose index is given by `index`. The `ARGV` and `ENVIRON` arrays may not be changed, although the `PROCINFO` array can be. Note that `index` should be string value. However, `gawk` will force a conversion to string if necessary.

**`awk_bool_t set_array_element_by_elem(awk_array_t a_cookie,`**

**`awk_element_t element);`**

Like `set_array_element()`, but take the `index` and `value` from `element`. This is a convenience macro.

**`awk_bool_t del_array_element(awk_array_t a_cookie,`**

**`const awk_value_t* const index);`**

Remove the element with the given index from the array represented by `a_cookie`. Return true if the element was removed, or false if the element did not exist in the array.

The following functions relate to arrays as a whole:

**`awk_array_t create_array(void);`**

Create a new array to which elements may be added. See How To Create and Populate Arrays for a discussion of how to create a new array and add elements to it.

**`awk_bool_t clear_array(awk_array_t a_cookie);`**

Clear the array represented by `a_cookie`. Return false if there was some kind of problem, true otherwise. The array remains an array, but after calling this function, it has no elements. This is equivalent to using the `delete` statement (see The `delete` Statement).

**`awk_bool_t destroy_array(awk_array_t a_cookie);`**

Clear the array represented by `a_cookie` and release the array allocated by `create_array`. Return false if there was some kind of problem, true otherwise. The array will no longer exist and cannot be used again.

**`awk_bool_t flatten_array_typed(awk_array_t a_cookie,`**

**`awk_flat_array_t **data,`**

**`awk_valtype_t index_type,`**

**`awk_valtype_t value_type);`**

For the array represented by `a_cookie`, create an `awk_flat_array_t` structure and fill it in with indices and values of the requested types. Set the pointer whose address is passed as `data` to point to this structure. Return true upon success, or false otherwise. See Working With All The Elements of an Array, for a discussion of how to flatten an array and work with it.

**`awk_bool_t flatten_array(awk_array_t a_cookie, awk_flat_array_t **data);`**

For the array represented by `a_cookie`, create an `awk_flat_array_t` structure and fill it in with `AWK_STRING` indices and `AWK_UNDEFINED` values. This is superseded by `flatten_array_typed()`. It is provided as a macro, and remains for convenience and for source code compatibility with the previous version of the API.

**`awk_bool_t release_flattened_array(awk_array_t a_cookie,`**

**`awk_flat_array_t *data);`**

When done with a flattened array, release the storage using this function. You must pass in both the original array cookie and the address of the created `awk_flat_array_t` structure. The function returns true upon success, false otherwise.

#### 17.4.12.3 Working With All The Elements of an Array

To *flatten* an array is to create a structure that represents the full array in a fashion that makes it easy for C code to traverse the entire array. Some of the code in extension/testext.c does this, and also serves as a nice example showing how to use the APIs.

We walk through that part of the code one step at a time. First, the `gawk` script that drives the test extension:

```
@load "testext"
BEGIN {
    n = split("blacky rusty sophie raincloud lucky", pets)
    printf("pets has %d elements\n", length(pets))
    ret = dump_array_and_delete("pets", "3")
    printf("dump_array_and_delete(pets) returned %d\n", ret)
    if ("3" in pets)
        printf("dump_array_and_delete() did NOT remove index \"3\"!\n")
    else
        printf("dump_array_and_delete() did remove index \"3\"!\n")
    print ""
}
```

This code creates an array with `split()` (see String-Manipulation Functions) and then calls `dump_array_and_delete()`. That function looks up the array whose name is passed as the first argument, and deletes the element at the index passed in the second argument. The `awk` code then prints the return value and checks if the element was indeed deleted. Here is the C code that implements `dump_array_and_delete()`. It has been edited slightly for presentation.

The first part declares variables, sets up the default return value in `result`, and checks that the function was called with the correct number of arguments:

```
static awk_value_t *
dump_array_and_delete(int nargs, awk_value_t *result)
{
    awk_value_t value, value2, value3;
    awk_flat_array_t *flat_array;
    size_t count;
    char *name;
    int i;

    assert(result != NULL);
    make_number(0.0, result);

    if (nargs != 2) {
        printf("dump_array_and_delete: nargs not right "
               "(%d should be 2)\n", nargs);
        goto out;
    }
```

The function then proceeds in steps, as follows. First, retrieve the name of the array, passed as the first argument, followed by the array itself. If either operation fails, print an error message and return:

```
    /* get argument named array as flat array and print it */
    if (get_argument(0, AWK_STRING, & value)) {
        name = value.str_value.str;
        if (sym_lookup(name, AWK_ARRAY, & value2))
            printf("dump_array_and_delete: sym_lookup of %s passed\n",
                   name);
        else {
            printf("dump_array_and_delete: sym_lookup of %s failed\n",
                   name);
            goto out;
        }
    } else {
        printf("dump_array_and_delete: get_argument(0) failed\n");
        goto out;
    }
```

For testing purposes and to make sure that the C code sees the same number of elements as the `awk` code, the second step is to get the count of elements in the array and print it:

```
    if (! get_element_count(value2.array_cookie, & count)) {
        printf("dump_array_and_delete: get_element_count failed\n");
        goto out;
    }

    printf("dump_array_and_delete: incoming size is %lu\n",
           (unsigned long) count);
```

The third step is to actually flatten the array, and then to double-check that the count in the `awk_flat_array_t` is the same as the count just retrieved:

```
    if (! flatten_array_typed(value2.array_cookie, & flat_array,
                              AWK_STRING, AWK_UNDEFINED)) {
        printf("dump_array_and_delete: could not flatten array\n");
        goto out;
    }

    if (flat_array->count != count) {
        printf("dump_array_and_delete: flat_array->count (%lu)"
               " != count (%lu)\n",
                (unsigned long) flat_array->count,
                (unsigned long) count);
        goto out;
    }
```

The fourth step is to retrieve the index of the element to be deleted, which was passed as the second argument. Remember that argument counts passed to `get_argument()` are zero-based, and thus the second argument is numbered one:

```
    if (! get_argument(1, AWK_STRING, & value3)) {
        printf("dump_array_and_delete: get_argument(1) failed\n");
        goto out;
    }
```

The fifth step is where the “real work” is done. The function loops over every element in the array, printing the index and element values. In addition, upon finding the element with the index that is supposed to be deleted, the function sets the `AWK_ELEMENT_DELETE` bit in the `flags` field of the element. When the array is released, `gawk` traverses the flattened array, and deletes any elements that have this flag bit set:

```
    for (i = 0; i < flat_array->count; i++) {
        printf("\t%s[\"%.*s\"] = %s\n",
            name,
            (int) flat_array->elements[i].index.str_value.len,
            flat_array->elements[i].index.str_value.str,
            valrep2str(& flat_array->elements[i].value));

        if (strcmp(value3.str_value.str,
                   flat_array->elements[i].index.str_value.str) == 0) {
            flat_array->elements[i].flags |= AWK_ELEMENT_DELETE;
            printf("dump_array_and_delete: marking element \"%s\" "
                   "for deletion\n",
                flat_array->elements[i].index.str_value.str);
        }
    }
```

The sixth step is to release the flattened array. This tells `gawk` that the extension is no longer using the array, and that it should delete any elements marked for deletion. `gawk` also frees any storage that was allocated, so you should not use the pointer (`flat_array` in this code) once you have called `release_flattened_array()`:

```
    if (! release_flattened_array(value2.array_cookie, flat_array)) {
        printf("dump_array_and_delete: could not release flattened array\n");
        goto out;
    }
```

Finally, because everything was successful, the function sets the return value to success, and returns:

```
    make_number(1.0, result);
out:
    return result;
}
```

Here is the output from running this part of the test:

```
pets has 5 elements
dump_array_and_delete: sym_lookup of pets passed
dump_array_and_delete: incoming size is 5
        pets["1"] = "blacky"
        pets["2"] = "rusty"
        pets["3"] = "sophie"
dump_array_and_delete: marking element "3" for deletion
        pets["4"] = "raincloud"
        pets["5"] = "lucky"
dump_array_and_delete(pets) returned 1
dump_array_and_delete() did remove index "3"!
```

#### 17.4.12.4 How To Create and Populate Arrays

Besides working with arrays created by `awk` code, you can create arrays and populate them as you see fit, and then `awk` code can access them and manipulate them.

There are two important points about creating arrays from extension code:

- You must install a new array into `gawk`’s symbol table immediately upon creating it. Once you have done so, you can then populate the array. Similarly, if installing a new array as a subarray of an existing array, you must add the new array to its parent before adding any elements to it. Thus, the correct way to build an array is to work “top down.” Create the array, and immediately install it in `gawk`’s symbol table using `sym_update()`, or install it as an element in a previously existing array using `set_array_element()`. We show example code shortly.
- Due to `gawk` internals, after using `sym_update()` to install an array into `gawk`, you have to retrieve the array cookie from the value passed in to `sym_update()` before doing anything else with it, like so: awk_value_t val; awk_array_t new_array; new_array = create_array(); val.val_type = AWK_ARRAY; val.array_cookie = new_array; /* install array in the symbol table */ sym_update("array", & val); new_array = val.array_cookie; /* YOU MUST DO THIS */ If installing an array as a subarray, you must also retrieve the value of the array cookie after the call to `set_element()`.

The following C code is a simple test extension to create an array with two regular elements and with a subarray. The leading `#include` directives and boilerplate variable declarations (see Boilerplate Code) are omitted for brevity. The first step is to create a new array and then install it in the symbol table:

```
/* create_new_array --- create a named array */

static void
create_new_array()
{
    awk_array_t a_cookie;
    awk_array_t subarray;
    awk_value_t index, value;

    a_cookie = create_array();
    value.val_type = AWK_ARRAY;
    value.array_cookie = a_cookie;

    if (! sym_update("new_array", & value))
        printf("create_new_array: sym_update(\"new_array\") failed!\n");
    a_cookie = value.array_cookie;
```

Note how `a_cookie` is reset from the `array_cookie` field in the `value` structure.

The second step is to install two regular values into `new_array`:

```
    (void) make_const_string("hello", 5, & index);
    (void) make_const_string("world", 5, & value);
    if (! set_array_element(a_cookie, & index, & value)) {
        printf("fill_in_array: set_array_element failed\n");
        return;
    }

    (void) make_const_string("answer", 6, & index);
    (void) make_number(42.0, & value);
    if (! set_array_element(a_cookie, & index, & value)) {
        printf("fill_in_array: set_array_element failed\n");
        return;
    }
```

The third step is to create the subarray and install it:

```
    (void) make_const_string("subarray", 8, & index);
    subarray = create_array();
    value.val_type = AWK_ARRAY;
    value.array_cookie = subarray;
    if (! set_array_element(a_cookie, & index, & value)) {
        printf("fill_in_array: set_array_element failed\n");
        return;
    }
    subarray = value.array_cookie;
```

The final step is to populate the subarray with its own element:

```
    (void) make_const_string("foo", 3, & index);
    (void) make_const_string("bar", 3, & value);
    if (! set_array_element(subarray, & index, & value)) {
        printf("fill_in_array: set_array_element failed\n");
        return;
    }
}
```

Here is a sample script that loads the extension and then dumps the array:

```
@load "subarray"

function dumparray(name, array,     i)
{
    for (i in array)
        if (isarray(array[i]))
            dumparray(name "[\"" i "\"]", array[i])
        else
            printf("%s[\"%s\"] = %s\n", name, i, array[i])
}

BEGIN {
    dumparray("new_array", new_array);
}
```

Here is the result of running the script:

```
$ AWKLIBPATH=$PWD gawk -f subarray.awk
-| new_array["subarray"]["foo"] = bar
-| new_array["hello"] = world
-| new_array["answer"] = 42
```

(See How `gawk` Finds Extensions for more information on the `AWKLIBPATH` environment variable.)

#### 17.4.13 Accessing and Manipulating Redirections

The following function allows extensions to access and manipulate redirections.

**`awk_bool_t get_file(const char *name,`**

**`size_t name_len,`**

**`const char *filetype,`**

**`int fd,`**

**`const awk_input_buf_t **ibufp,`**

**`const awk_output_buf_t **obufp);`**

Look up file `name` in `gawk`’s internal redirection table. If `name` is `NULL` or `name_len` is zero, return data for the currently open input file corresponding to `FILENAME`. (This does not access the `filetype` argument, so that may be undefined). If the file is not already open, attempt to open it. The `filetype` argument must be zero-terminated and should be one of:

**`">"`**

A file opened for output.

**`">>"`**

A file opened for append.

**`"<"`**

A file opened for input.

**`"|>"`**

A pipe opened for output.

**`"|<"`**

A pipe opened for input.

**`"|&"`**

A two-way coprocess.

On error, return `awk_false`. Otherwise, return `awk_true`, and return additional information about the redirection in the `ibufp` and `obufp` pointers.

For input redirections, the `*ibufp` value should be non-`NULL`, and `*obufp` should be `NULL`. For output redirections, the `*obufp` value should be non-`NULL`, and `*ibufp` should be `NULL`. For two-way coprocesses, both values should be non-`NULL`.

In the usual case, the extension is interested in `(*ibufp)->fd` and/or `fileno((*obufp)->fp)`. If the file is not already open, and the `fd` argument is nonnegative, `gawk` will use that file descriptor instead of opening the file in the usual way. If `fd` is nonnegative, but the file exists already, `gawk` ignores `fd` and returns the existing file. It is the caller’s responsibility to notice that neither the `fd` in the returned `awk_input_buf_t` nor the `fd` in the returned `awk_output_buf_t` matches the requested value.

Note that supplying a file descriptor is currently *not* supported for pipes. However, supplying a file descriptor should work for input, output, append, and two-way (coprocess) sockets. If `filetype` is two-way, `gawk` assumes that it is a socket! Note that in the two-way case, the input and output file descriptors may differ. To check for success, you must check whether either matches.

It is anticipated that this API function will be used to implement I/O multiplexing and a socket library.

#### 17.4.14 API Variables

The API provides two sets of variables. The first provides information about the version of the API (both with which the extension was compiled, and with which `gawk` was compiled). The second provides information about how `gawk` was invoked.

#### 17.4.14.1 API Version Constants and Variables

The API provides both a “major” and a “minor” version number. The API versions are available at compile time as C preprocessor defines to support conditional compilation, and as enum constants to facilitate debugging:

| API Version | C Preprocessor Define | enum constant |
|---|---|---|
| Major | `gawk_api_major_version` | `GAWK_API_MAJOR_VERSION` |
| Minor | `gawk_api_minor_version` | `GAWK_API_MINOR_VERSION` |

**Table 17.3:**gawk API version constants

The minor version increases when new functions are added to the API. Such new functions are always added to the end of the API `struct`.

The major version increases (and the minor version is reset to zero) if any of the data types change size or member order, or if any of the existing functions change signature.

It could happen that an extension may be compiled against one version of the API but loaded by a version of `gawk` using a different version. For this reason, the major and minor API versions of the running `gawk` are included in the API `struct` as read-only constant integers:

**`api->major_version`**

The major version of the running `gawk`.

**`api->minor_version`**

The minor version of the running `gawk`.

It is up to the extension to decide if there are API incompatibilities. Typically, a check like this is enough:

```
if (   api->major_version != GAWK_API_MAJOR_VERSION
    || api->minor_version < GAWK_API_MINOR_VERSION) {
        fprintf(stderr, "foo_extension: version mismatch with gawk!\n");
        fprintf(stderr, "\tmy version (%d, %d), gawk version (%d, %d)\n",
                GAWK_API_MAJOR_VERSION, GAWK_API_MINOR_VERSION,
                api->major_version, api->minor_version);
        exit(1);
}
```

Such code is included in the boilerplate `dl_load_func()` macro provided in gawkapi.h (discussed in Boilerplate Code).

#### 17.4.14.2 GMP and MPFR Version Information

The API also includes information about the versions of GMP and MPFR with which the running `gawk` was compiled (if any). They are included in the API `struct` as read-only constant integers:

**`api->gmp_major_version`**

The major version of the GMP library used to compile `gawk`.

**`api->gmp_minor_version`**

The minor version of the GMP library used to compile `gawk`.

**`api->mpfr_major_version`**

The major version of the MPFR library used to compile `gawk`.

**`api->mpfr_minor_version`**

The minor version of the MPFR library used to compile `gawk`.

These fields are set to zero if `gawk` was compiled without MPFR support.

You can check if the versions of MPFR and GMP that you are using match those of `gawk` with the following macro:

**`check_mpfr_version(extension)`**

The `extension` is the extension id passed to all the other macros and functions defined in gawkapi.h. If you have not included the `<mpfr.h>` header file, then this macro will be defined to do nothing.

If you have included that file, then this macro compares the MPFR and GMP major and minor versions against those of the library you are compiling against. If your libraries are newer than `gawk`’s, it produces a fatal error message.

The `dl_load_func()` macro (see Boilerplate Code) calls `check_mpfr_version()`.

#### 17.4.14.3 Informational Variables

The API provides access to several variables that describe whether the corresponding command-line options were enabled when `gawk` was invoked. The variables are:

**`do_csv`**

This variable is true if `gawk` was invoked with --csv option.

**`do_debug`**

This variable is true if `gawk` was invoked with --debug option.

**`do_lint`**

This variable is true if `gawk` was invoked with --lint option.

**`do_mpfr`**

This variable is true if `gawk` was invoked with --bignum option.

**`do_profile`**

This variable is true if `gawk` was invoked with --profile option.

**`do_sandbox`**

This variable is true if `gawk` was invoked with --sandbox option.

**`do_traditional`**

This variable is true if `gawk` was invoked with --traditional option.

The value of `do_lint` can change if `awk` code modifies the `LINT` predefined variable (see Predefined Variables). The others should not change during execution.

#### 17.4.15 Boilerplate Code

As mentioned earlier (see How It Works at a High Level), the function definitions as presented are really macros. To use these macros, your extension must provide a small amount of boilerplate code (variables and functions) toward the top of your source file, using predefined names as described here. The boilerplate needed is also provided in comments in the gawkapi.h header file:

```
/* Boilerplate code: */
int plugin_is_GPL_compatible;

static gawk_api_t *const api;
```

```
static awk_ext_id_t ext_id;
static const char *ext_version = NULL; /* or ... = "some string" */

static awk_ext_func_t func_table[] = {
    { "name", do_name, 1, 0, awk_false, NULL },
    /* ... */
};

/* EITHER: */

static awk_bool_t (*init_func)(void) = NULL;

/* OR: */

static awk_bool_t
init_my_extension(void)
{
    ...
}

static awk_bool_t (*init_func)(void) = init_my_extension;

dl_load_func(func_table, some_name, "name_space_in_quotes")
```

These variables and functions are as follows:

**`int plugin_is_GPL_compatible;`**

This asserts that the extension is compatible with the GNU GPL (see GNU General Public License). If your extension does not have this, `gawk` will not load it (see Extension Licensing).

**`static gawk_api_t *const api;`**

This global `static` variable should be set to point to the `gawk_api_t` pointer that `gawk` passes to your `dl_load()` function. This variable is used by all of the macros.

**`static awk_ext_id_t ext_id;`**

This global static variable should be set to the `awk_ext_id_t` value that `gawk` passes to your `dl_load()` function. This variable is used by all of the macros.

**`static const char *ext_version = NULL; /* or … = "some string" */`**

This global `static` variable should be set either to `NULL`, or to point to a string giving the name and version of your extension.

**`static awk_ext_func_t func_table[] = { … };`**

This is an array of one or more `awk_ext_func_t` structures, as described earlier (see Registering An Extension Function). It can then be looped over for multiple calls to `add_ext_func()`.

**`static awk_bool_t (*init_func)(void) = NULL;`**

**`*OR*`**

**`static awk_bool_t init_my_extension(void) { … }`**

**`static awk_bool_t (*init_func)(void) = init_my_extension;`**

If you need to do some initialization work, you should define a function that does it (creates variables, opens files, etc.) and then define the `init_func` pointer to point to your function. The function should return `awk_false` upon failure, or `awk_true` if everything goes well.

If you don’t need to do any initialization, define the pointer and initialize it to `NULL`.

**`dl_load_func(func_table, some_name, "name_space_in_quotes")`**

This macro expands to a `dl_load()` function that performs all the necessary initializations.

The point of all the variables and arrays is to let the `dl_load()` function (from the `dl_load_func()` macro) do all the standard work. It does the following:

1. Check the API versions. If the extension major version does not match `gawk`’s, or if the extension minor version is greater than `gawk`’s, it prints a fatal error message and exits.
2. Check the MPFR and GMP versions. If there is a mismatch, it prints a fatal error message and exits.
3. Load the functions defined in `func_table`. If any of them fails to load, it prints a warning message but continues on.
4. If the `init_func` pointer is not `NULL`, call the function it points to. If it returns `awk_false`, print a warning message.
5. If `ext_version` is not `NULL`, register the version string with `gawk`.

#### 17.4.16 Changes From Version 1 of the API

The current API is *not* binary compatible with version 1 of the API. You will have to recompile your extensions in order to use them with the current version of `gawk`.

Fortunately, at the possible expense of some compile-time warnings, the API remains source-code–compatible with the previous API. The major differences are the additional members in the `awk_ext_func_t` structure, and the addition of the third argument to the C implementation function (see Registering An Extension Function).

Here is a list of individual features that changed from version 1 to version 2 of the API:

- Numeric values can now have MPFR/MPZ variants (see General-Purpose Data Types).
- There are new string types: `AWK_REGEX` and `AWK_STRNUM` (see General-Purpose Data Types).
- The `ezalloc()` macro is new (see Memory Allocation Functions and Convenience Macros).
- The `awk_ext_func_t` structure changed. Instead of `num_expected_args`, it now has `max_expected` and `min_required` (see Registering An Extension Function).
- For `get_record()`, an input parser can now specify field widths (see Customized Input Parsers).
- Extensions can now produce nonfatal error messages (see Printing Messages).
- When flattening an array, you can now specify the index and value types (see Array Functions).
- The `get_file()` API is new (see Accessing and Manipulating Redirections).

### 17.5 How `gawk` Finds Extensions

Compiled extensions have to be installed in a directory where `gawk` can find them. If `gawk` is configured and built in the default fashion, the directory in which to find extensions is /usr/local/lib/gawk. You can also specify a search path with a list of directories to search for compiled extensions. See The `AWKLIBPATH` Environment Variable for more information.

### 17.6 Example: Some File Functions

> *No matter where you go, there you are.*

—

Buckaroo Banzai

Two useful functions that are not in `awk` are `chdir()` (so that an `awk` program can change its directory) and `stat()` (so that an `awk` program can gather information about a file). In order to illustrate the API in action, this section implements these functions for `gawk` in an extension.

#### 17.6.1 Using `chdir()` and `stat()`

This section shows how to use the new functions at the `awk` level once they’ve been integrated into the running `gawk` interpreter. Using `chdir()` is very straightforward. It takes one argument, the new directory to change to:

```
@load "filefuncs"
...
newdir = "/home/arnold/funstuff"
ret = chdir(newdir)
if (ret < 0) {
    printf("could not change to %s: %s\n", newdir, ERRNO) > "/dev/stderr"
    exit 1
}
...
```

The return value is negative if the `chdir()` failed, and `ERRNO` (see Predefined Variables) is set to a string indicating the error.

Using `stat()` is a bit more complicated. The C `stat()` function fills in a structure that has a fair amount of information. The right way to model this in `awk` is to fill in an associative array with the appropriate information:

```
file = "/home/arnold/.profile"
ret = stat(file, fdata)
if (ret < 0) {
    printf("could not stat %s: %s\n",
             file, ERRNO) > "/dev/stderr"
    exit 1
}
printf("size of %s is %d bytes\n", file, fdata["size"])
```

The `stat()` function always clears the data array, even if the `stat()` fails. It fills in the following elements:

**`"name"`**

The name of the file that was `stat()`ed.

**`"dev"`**

**`"ino"`**

The file’s device and inode numbers, respectively.

**`"mode"`**

The file’s mode, as a numeric value. This includes both the file’s type and its permissions.

**`"nlink"`**

The number of hard links (directory entries) the file has.

**`"uid"`**

**`"gid"`**

The numeric user and group ID numbers of the file’s owner.

**`"size"`**

The size in bytes of the file.

**`"blocks"`**

The number of disk blocks the file actually occupies. This may not be a function of the file’s size if the file has holes.

**`"atime"`**

**`"mtime"`**

**`"ctime"`**

The file’s last access, modification, and inode update times, respectively. These are numeric timestamps, suitable for formatting with `strftime()` (see Time Functions).

**`"pmode"`**

The file’s “printable mode.” This is a string representation of the file’s type and permissions, such as is produced by ‘ls -l’—for example, `"drwxr-xr-x"`.

**`"type"`**

A printable string representation of the file’s type. The value is one of the following:

**`"blockdev"`**

**`"chardev"`**

The file is a block or character device (“special file”).

**`"directory"`**

The file is a directory.

**`"fifo"`**

The file is a named pipe (also known as a FIFO).

**`"file"`**

The file is just a regular file.

**`"socket"`**

The file is an `AF_UNIX` (“Unix domain”) socket in the filesystem.

**`"symlink"`**

The file is a symbolic link.

**`"devbsize"`**

The size of a block for the element indexed by `"blocks"`. This information is derived from either the `DEV_BSIZE` constant defined in `<sys/param.h>` on most systems, or the `S_BLKSIZE` constant in `<sys/stat.h>` on BSD systems. For some other systems, *a priori* knowledge is used to provide a value. Where no value can be determined, it defaults to 512.

Several additional elements may be present, depending upon the operating system and the type of the file. You can test for them in your `awk` program by using the `in` operator (see Referring to an Array Element):

**`"blksize"`**

The preferred block size for I/O to the file. This field is not present on all POSIX-like systems in the C `stat` structure.

**`"linkval"`**

If the file is a symbolic link, this element is the name of the file the link points to (i.e., the value of the link).

**`"rdev"`**

**`"major"`**

**`"minor"`**
