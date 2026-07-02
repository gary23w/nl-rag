---
title: "The GNU Awk User’s Guide (part 28/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 28/38
---

# The GNU Awk User’s Guide

If the file is a block or character device file, then these values represent the numeric device number and the major and minor components of that number, respectively.

#### 17.6.2 C Code for `chdir()` and `stat()`

Here is the C code for these extensions.116

The file includes a number of standard header files, and then includes the gawkapi.h header file, which provides the API definitions. Those are followed by the necessary variable declarations to make use of the API macros and boilerplate code (see Boilerplate Code):

```
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <stdio.h>
#include <assert.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>

#include "gawkapi.h"

#include "gettext.h"
#define _(msgid)  gettext(msgid)
#define N_(msgid) msgid

#include "gawkfts.h"
#include "stack.h"

static const gawk_api_t *api;    /* for convenience macros to work */
static awk_ext_id_t ext_id;
static awk_bool_t init_filefuncs(void);
static awk_bool_t (*init_func)(void) = init_filefuncs;
static const char *ext_version = "filefuncs extension: version 1.0";

int plugin_is_GPL_compatible;
```

By convention, for an `awk` function `foo()`, the C function that implements it is called `do_foo()`. The function should have two arguments. The first is an `int`, usually called `nargs`, that represents the number of actual arguments for the function. The second is a pointer to an `awk_value_t` structure, usually named `result`:

```
/*  do_chdir --- provide dynamically loaded chdir() function for gawk */

static awk_value_t *
do_chdir(int nargs, awk_value_t *result, struct awk_ext_func *unused)
```

```
{
    awk_value_t newdir;
    int ret = -1;

    assert(result != NULL);
```

The `newdir` variable represents the new directory to change to, which is retrieved with `get_argument()`. Note that the first argument is numbered zero.

If the argument is retrieved successfully, the function calls the `chdir()` system call. Otherwise, if the `chdir()` fails, it updates `ERRNO`:

```
    if (get_argument(0, AWK_STRING, & newdir)) {
        ret = chdir(newdir.str_value.str);
        if (ret < 0)
            update_ERRNO_int(errno);
    }
```

Finally, the function returns the return value to the `awk` level:

```
    return make_number(ret, result);
}
```

The `stat()` extension is more involved. First comes a function that turns a numeric mode into a printable representation (e.g., octal `0644` becomes ‘-rw-r--r--’). This is omitted here for brevity:

```
/* format_mode --- turn a stat mode field into something readable */

static char *
format_mode(unsigned long fmode)
{
    ...
}
```

Next comes a function for reading symbolic links, which is also omitted here for brevity:

```
/* read_symlink --- read a symbolic link into an allocated buffer.
   ... */

static char *
read_symlink(const char *fname, size_t bufsize, ssize_t *linksize)
{
    ...
}
```

Two helper functions simplify entering values in the array that will contain the result of the `stat()`:

```
/* array_set --- set an array element */

static void
array_set(awk_array_t array, const char *sub, awk_value_t *value)
{
    awk_value_t index;

    set_array_element(array,
                      make_const_string(sub, strlen(sub), & index),
                      value);

}

/* array_set_numeric --- set an array element with a number */

static void
array_set_numeric(awk_array_t array, const char *sub, double num)
{
    awk_value_t tmp;

    array_set(array, sub, make_number(num, & tmp));
}
```

The following function does most of the work to fill in the `awk_array_t` result array with values obtained from a valid `struct stat`. This work is done in a separate function to support the `stat()` function for `gawk` and also to support the `fts()` extension, which is included in the same file but whose code is not shown here (see File-Related Functions).

The first part of the function is variable declarations, including a table to map file types to strings:

```
/* fill_stat_array --- do the work to fill an array with stat info */

static int
fill_stat_array(const char *name, awk_array_t array, struct stat *sbuf)
{
    char *pmode;    /* printable mode */
    const char *type = "unknown";
    awk_value_t tmp;
    static struct ftype_map {
        unsigned int mask;
        const char *type;
    } ftype_map[] = {
        { S_IFREG, "file" },
        { S_IFBLK, "blockdev" },
        { S_IFCHR, "chardev" },
        { S_IFDIR, "directory" },
#ifdef S_IFSOCK
        { S_IFSOCK, "socket" },
#endif
#ifdef S_IFIFO
        { S_IFIFO, "fifo" },
#endif
#ifdef S_IFLNK
        { S_IFLNK, "symlink" },
#endif
#ifdef S_IFDOOR /* Solaris weirdness */
        { S_IFDOOR, "door" },
#endif
    };
    int j, k;
```

The destination array is cleared, and then code fills in various elements based on values in the `struct stat`:

```
    /* empty out the array */
    clear_array(array);

    /* fill in the array */
    array_set(array, "name", make_const_string(name, strlen(name),
                                               & tmp));
    array_set_numeric(array, "dev", sbuf->st_dev);
    array_set_numeric(array, "ino", sbuf->st_ino);
    array_set_numeric(array, "mode", sbuf->st_mode);
    array_set_numeric(array, "nlink", sbuf->st_nlink);
    array_set_numeric(array, "uid", sbuf->st_uid);
    array_set_numeric(array, "gid", sbuf->st_gid);
    array_set_numeric(array, "size", sbuf->st_size);
    array_set_numeric(array, "blocks", sbuf->st_blocks);
    array_set_numeric(array, "atime", sbuf->st_atime);
    array_set_numeric(array, "mtime", sbuf->st_mtime);
    array_set_numeric(array, "ctime", sbuf->st_ctime);

    /* for block and character devices, add rdev,
       major and minor numbers */
    if (S_ISBLK(sbuf->st_mode) || S_ISCHR(sbuf->st_mode)) {
        array_set_numeric(array, "rdev", sbuf->st_rdev);
        array_set_numeric(array, "major", major(sbuf->st_rdev));
        array_set_numeric(array, "minor", minor(sbuf->st_rdev));
    }
```

The latter part of the function makes selective additions to the destination array, depending upon the availability of certain members and/or the type of the file. It then returns zero, for success:

```
#ifdef HAVE_STRUCT_STAT_ST_BLKSIZE
    array_set_numeric(array, "blksize", sbuf->st_blksize);
#endif
```

```
    pmode = format_mode(sbuf->st_mode);
    array_set(array, "pmode", make_const_string(pmode, strlen(pmode),
                                                & tmp));

    /* for symbolic links, add a linkval field */
    if (S_ISLNK(sbuf->st_mode)) {
        char *buf;
        ssize_t linksize;

        if ((buf = read_symlink(name, sbuf->st_size,
                    & linksize)) != NULL)
            array_set(array, "linkval",
                      make_malloced_string(buf, linksize, & tmp));
        else
            warning(ext_id, _("stat: unable to read symbolic link `%s'"),
                    name);
    }

    /* add a type field */
    type = "unknown";   /* shouldn't happen */
    for (j = 0, k = sizeof(ftype_map)/sizeof(ftype_map[0]); j < k; j++) {
        if ((sbuf->st_mode & S_IFMT) == ftype_map[j].mask) {
            type = ftype_map[j].type;
            break;
        }
    }

    array_set(array, "type", make_const_string(type, strlen(type), & tmp));

    return 0;
}
```

The third argument to `stat()` was not discussed previously. This argument is optional. If present, it causes `do_stat()` to use the `stat()` system call instead of the `lstat()` system call. This is done by using a function pointer: `statfunc`. `statfunc` is initialized to point to `lstat()` (instead of `stat()`) to get the file information, in case the file is a symbolic link. However, if the third argument is included, `statfunc` is set to point to `stat()`, instead.

Here is the `do_stat()` function, which starts with variable declarations and argument checking:

```
/* do_stat --- provide a stat() function for gawk */

static awk_value_t *
do_stat(int nargs, awk_value_t *result, struct awk_ext_func *unused)
{
    awk_value_t file_param, array_param;
    char *name;
    awk_array_t array;
    int ret;
    struct stat sbuf;
    /* default is lstat() */
    int (*statfunc)(const char *path, struct stat *sbuf) = lstat;

    assert(result != NULL);
```

Then comes the actual work. First, the function gets the arguments. Next, it gets the information for the file. If the called function (`lstat()` or `stat()`) returns an error, the code sets `ERRNO` and returns:

```
    /* file is first arg, array to hold results is second */
    if (   ! get_argument(0, AWK_STRING, & file_param)
        || ! get_argument(1, AWK_ARRAY, & array_param)) {
        warning(ext_id, _("stat: bad parameters"));
        return make_number(-1, result);
    }

    if (nargs == 3) {
        statfunc = stat;
    }

    name = file_param.str_value.str;
    array = array_param.array_cookie;

    /* always empty out the array */
    clear_array(array);

    /* stat the file; if error, set ERRNO and return */
    ret = statfunc(name, & sbuf);
```

```
    if (ret < 0) {
        update_ERRNO_int(errno);
        return make_number(ret, result);
    }
```

The tedious work is done by `fill_stat_array()`, shown earlier. When done, the function returns the result from `fill_stat_array()`:

```
    ret = fill_stat_array(name, array, & sbuf);

    return make_number(ret, result);
}
```

Finally, it’s necessary to provide the “glue” that loads the new function(s) into `gawk`.

The `filefuncs` extension also provides an `fts()` function, which we omit here (see File-Related Functions). For its sake, there is an initialization function:

```
/* init_filefuncs --- initialization routine */

static awk_bool_t
init_filefuncs(void)
{
    ...
}
```

We are almost done. We need an array of `awk_ext_func_t` structures for loading each function into `gawk`:

```
static awk_ext_func_t func_table[] = {
    { "chdir", do_chdir, 1, 1, awk_false, NULL },
    { "stat",  do_stat, 3, 2, awk_false, NULL },
    ...
};
```

Each extension must have a routine named `dl_load()` to load everything that needs to be loaded. It is simplest to use the `dl_load_func()` macro in `gawkapi.h`:

```
/* define the dl_load() function using the boilerplate macro */

dl_load_func(func_table, filefuncs, "")
```

And that’s it!

#### 17.6.3 Integrating the Extensions

Now that the code is written, it must be possible to add it at runtime to the running `gawk` interpreter. First, the code must be compiled. Assuming that the functions are in a file named filefuncs.c, and *idir* is the location of the gawkapi.h header file, the following steps117 create a GNU/Linux shared library:

```
$ gcc -fPIC -shared -DHAVE_CONFIG_H -c -O -g -Iidir filefuncs.c
$ gcc -o filefuncs.so -shared filefuncs.o
```

Once the library exists, it is loaded by using the `@load` directive:

```
# file testff.awk
@load "filefuncs"

BEGIN {
    "pwd" | getline curdir  # save current directory
    close("pwd")

    chdir("/tmp")
    system("pwd")   # test it
    chdir(curdir)   # go back

    print "Info for testff.awk"
    ret = stat("testff.awk", data)
    print "ret =", ret
    for (i in data)
        printf "data[\"%s\"] = %s\n", i, data[i]
    print "testff.awk modified:",
        strftime("%m %d %Y %H:%M:%S", data["mtime"])

    print "\nInfo for JUNK"
    ret = stat("JUNK", data)
    print "ret =", ret
    for (i in data)
        printf "data[\"%s\"] = %s\n", i, data[i]
    print "JUNK modified:", strftime("%m %d %Y %H:%M:%S", data["mtime"])
}
```

The `AWKLIBPATH` environment variable tells `gawk` where to find extensions (see How `gawk` Finds Extensions). We set it to the current directory and run the program:

```
$ AWKLIBPATH=$PWD gawk -f testff.awk
-| /tmp
-| Info for testff.awk
-| ret = 0
-| data["blksize"] = 4096
-| data["devbsize"] = 512
-| data["mtime"] = 1412004710
-| data["mode"] = 33204
-| data["type"] = file
-| data["dev"] = 2053
-| data["gid"] = 1000
-| data["ino"] = 10358899
-| data["ctime"] = 1412004710
-| data["blocks"] = 8
-| data["nlink"] = 1
-| data["name"] = testff.awk
-| data["atime"] = 1412004716
-| data["pmode"] = -rw-rw-r--
-| data["size"] = 666
-| data["uid"] = 1000
-| testff.awk modified: 09 29 2014 18:31:50
-|
-| Info for JUNK
-| ret = -1
-| JUNK modified: 01 01 1970 02:00:00
```

### 17.7 The Sample Extensions in the `gawk` Distribution

This section provides a brief overview of the sample extensions that come in the `gawk` distribution. Some of them are intended for production use (e.g., the `filefuncs`, `readdir`, and `inplace` extensions). Others mainly provide example code that shows how to use the extension API.

#### 17.7.1 File-Related Functions

The `filefuncs` extension provides three different functions, as follows. The usage is:

**`@load "filefuncs"`**

This is how you load the extension.

**`result = chdir("/some/directory")` ¶**

The `chdir()` function is a direct hook to the `chdir()` system call to change the current directory. It returns zero upon success or a value less than zero upon error. In the latter case, it updates `ERRNO`.

**`result = stat("/some/path", statdata` [`, follow`]`)` ¶**

The `stat()` function provides a hook into the `stat()` system call. It returns zero upon success or a value less than zero upon error. In the latter case, it updates `ERRNO`.

By default, it uses the `lstat()` system call. However, if passed a third argument, it uses `stat()` instead.

In all cases, it clears the `statdata` array. When the call is successful, `stat()` fills the `statdata` array with information retrieved from the filesystem, as follows:

| Subscript | Field in `struct stat` | File type |
|---|---|---|
| `"name"` | The file name | All |
| `"dev"` | `st_dev` | All |
| `"ino"` | `st_ino` | All |
| `"mode"` | `st_mode` | All |
| `"nlink"` | `st_nlink` | All |
| `"uid"` | `st_uid` | All |
| `"gid"` | `st_gid` | All |
| `"size"` | `st_size` | All |
| `"atime"` | `st_atime` | All |
| `"mtime"` | `st_mtime` | All |
| `"ctime"` | `st_ctime` | All |
| `"rdev"` | `st_rdev` | Device files |
| `"major"` | `st_major` | Device files |
| `"minor"` | `st_minor` | Device files |
| `"blksize"` | `st_blksize` | All |
| `"pmode"` | A human-readable version of the mode value, like that printed by `ls` (for example, `"-rwxr-xr-x"`) | All |
| `"linkval"` | The value of the symbolic link | Symbolic links |
| `"type"` | The type of the file as a string—one of `"file"`, `"blockdev"`, `"chardev"`, `"directory"`, `"socket"`, `"fifo"`, `"symlink"`, `"door"`, or `"unknown"` (not all systems support all file types) | All |

**`flags = or(FTS_PHYSICAL, ...)` ¶**

**`result = fts(pathlist, flags, filedata)`**

Walk the file trees provided in `pathlist` and fill in the `filedata` array, as described next. `flags` is the bitwise OR of several predefined values, also described in a moment. Return zero if there were no errors, otherwise return −1.

The `fts()` function provides a hook to the C library `fts()` routines for traversing file hierarchies. Instead of returning data about one file at a time in a stream, it fills in a multidimensional array with data about each file and directory encountered in the requested hierarchies.

The arguments are as follows:

**`pathlist`**

An array of file names. The element values are used; the index values are ignored.

**`flags`**

This should be the bitwise OR of one or more of the following predefined constant flag values. At least one of `FTS_LOGICAL` or `FTS_PHYSICAL` must be provided; otherwise `fts()` returns an error value and sets `ERRNO`. The flags are:

**`FTS_LOGICAL`**

Do a “logical” file traversal, where the information returned for a symbolic link refers to the linked-to file, and not to the symbolic link itself. This flag is mutually exclusive with `FTS_PHYSICAL`.

**`FTS_PHYSICAL`**

Do a “physical” file traversal, where the information returned for a symbolic link refers to the symbolic link itself. This flag is mutually exclusive with `FTS_LOGICAL`.

**`FTS_NOCHDIR`**

As a performance optimization, the C library `fts()` routines change directory as they traverse a file hierarchy. This flag disables that optimization.

**`FTS_COMFOLLOW`**

Immediately follow a symbolic link named in `pathlist`, whether or not `FTS_LOGICAL` is set.

**`FTS_SEEDOT`**

By default, the C library `fts()` routines do not return entries for . (dot) and .. (dot-dot). This option causes entries for dot-dot to also be included. (The extension always includes an entry for dot; more on this in a moment.)

**`FTS_XDEV`**

During a traversal, do not cross onto a different mounted filesystem.

**`filedata`**

The `filedata` array holds the results. `fts()` first clears it. Then it creates an element in `filedata` for every element in `pathlist`. The index is the name of the directory or file given in `pathlist`. The element for this index is itself an array. There are two cases:

***The path is a file***

In this case, the array contains two or three elements:

**`"path"`**

The full path to this file, starting from the “root” that was given in the `pathlist` array.

**`"stat"`**

This element is itself an array, containing the same information as provided by the `stat()` function described earlier for its `statdata` argument. The element may not be present if the `stat()` system call for the file failed.

**`"error"`**

If some kind of error was encountered, the array will also contain an element named `"error"`, which is a string describing the error.

***The path is a directory***

In this case, the array contains one element for each entry in the directory. If an entry is a file, that element is the same as for files, just described. If the entry is a directory, that element is (recursively) an array describing the subdirectory. If `FTS_SEEDOT` was provided in the flags, then there will also be an element named `".."`. This element will be an array containing the data as provided by `stat()`.

In addition, there will be an element whose index is `"."`. This element is an array containing the same two or three elements as for a file: `"path"`, `"stat"`, and `"error"`.

The `fts()` function returns zero if there were no errors. Otherwise, it returns −1.

> **NOTE:** The `fts()` extension does not exactly mimic the interface of the C library `fts()` routines, choosing instead to provide an interface that is based on associative arrays, which is more comfortable to use from an `awk` program. This includes the lack of a comparison function, because `gawk` already provides powerful array sorting facilities. Although an `fts_read()`-like interface could have been provided, this felt less natural than simply creating a multidimensional array to represent the file hierarchy and its information.

See test/fts.awk in the `gawk` distribution for an example use of the `fts()` extension function.

#### 17.7.2 Interface to `fnmatch()`

This extension provides an interface to the C library `fnmatch()` function. The usage is:

**`@load "fnmatch"`**

This is how you load the extension.

**`result = fnmatch(pattern, string, flags)` ¶**

The return value is zero on success, `FNM_NOMATCH` if the string did not match the pattern, or a different nonzero value if an error occurred.

In addition to the `fnmatch()` function, the `fnmatch` extension adds one constant (`FNM_NOMATCH`), and an array of flag values named `FNM`.

The arguments to `fnmatch()` are:

**`pattern`**

The file name wildcard to match

**`string`**

The file name string

**`flag`**

Either zero, or the bitwise OR of one or more of the flags in the `FNM` array

The flags are as follows:

| Array element | Corresponding flag defined by `fnmatch()` |
|---|---|
| `FNM["CASEFOLD"]` | `FNM_CASEFOLD` |
| `FNM["FILE_NAME"]` | `FNM_FILE_NAME` |
| `FNM["LEADING_DIR"]` | `FNM_LEADING_DIR` |
| `FNM["NOESCAPE"]` | `FNM_NOESCAPE` |
| `FNM["PATHNAME"]` | `FNM_PATHNAME` |
| `FNM["PERIOD"]` | `FNM_PERIOD` |

Here is an example:

```
@load "fnmatch"
...
flags = or(FNM["PERIOD"], FNM["NOESCAPE"])
if (fnmatch("*.a", "foo.c", flags) == FNM_NOMATCH)
    print "no match"
```

#### 17.7.3 Interface to `fork()`, `wait()`, and `waitpid()`

The `fork` extension adds three functions, as follows:

**`@load "fork"`**

This is how you load the extension.

**`pid = fork()` ¶**

This function creates a new process. The return value is zero in the child and the process ID number of the child in the parent, or −1 upon error. In the latter case, `ERRNO` indicates the problem. In the child, `PROCINFO["pid"]` and `PROCINFO["ppid"]` are updated to reflect the correct values.

**`ret = waitpid(pid)` ¶**

This function takes a numeric argument, which is the process ID to wait for. The return value is that of the `waitpid()` system call.

**`ret = wait()` ¶**

This function waits for the first child to die. The return value is that of the `wait()` system call.

There is no corresponding `exec()` function.

Here is an example:

```
@load "fork"
...
if ((pid = fork()) == 0)
    print "hello from the child"
else
    print "hello from the parent"
```

#### 17.7.4 Enabling In-Place File Editing

The `inplace` extension emulates GNU `sed`’s -i option, which performs “in-place” editing of each input file. Like GNU `sed`, the `inplace` extension replaces links (both hard and symbolic) with new files. If you wish to affect the target, you must dereference it first, for example using `realpath` from GNU Coreutils. It uses the bundled inplace.awk include file to invoke the extension properly. This extension makes use of the namespace facility to place all the variables and functions in the `inplace` namespace (see Namespaces in `gawk`):

```
# inplace --- load and invoke the inplace extension.

@load "inplace"

# Please set inplace::suffix to make a backup copy.  For example, you may
# want to set inplace::suffix to .bak on the command line or in a BEGIN rule.

# Before there were namespaces in gawk, this extension used
# INPLACE_SUFFIX as the variable for making backup copies. We allow this
# too, so that any code that used the previous version continues to work.

# By default, each filename on the command line will be edited inplace.
# But you can selectively disable this by adding an inplace::enable=0 argument
# prior to files that you do not want to process this way.  You can then
# reenable it later on the commandline by putting inplace::enable=1 before files
# that you wish to be subject to inplace editing.

# N.B. We call inplace::end() in the BEGINFILE and END rules so that any
# actions in an ENDFILE rule will be redirected as expected.

@namespace "inplace"
```

```
BEGIN {
    enable = 1         # enabled by default
}
```

```
BEGINFILE {
    sfx = (suffix ? suffix : awk::INPLACE_SUFFIX)
    if (filename != "")
        end(filename, sfx)
    if (enable)
        begin(filename = FILENAME, sfx)
    else
        filename = ""
}
```

```
END {
    if (filename != "")
        end(filename, (suffix ? suffix : awk::INPLACE_SUFFIX))
}
```

For each regular file that is processed, the extension redirects standard output to a temporary file configured to have the same owner and permissions as the original. After the file has been processed, the extension restores standard output to its original destination. (Due to this implementation, it helps to redirect `gawk`’s standard output to /dev/null, instead of leaving it set to your terminal, so that output will be block-buffered instead of line-buffered.)

If `inplace::suffix` is not an empty string, the original file is linked to a backup file name created by appending that suffix. Finally, the temporary file is renamed to the original file name.

Note that the use of this feature can be controlled by placing ‘inplace::enable=0’ on the command-line prior to listing files that should not be processed this way. You can reenable inplace editing by adding an ‘inplace::enable=1’ argument prior to files that should be subject to inplace editing.

The `inplace::filename` variable serves to keep track of the current file name so as to not invoke `inplace::end()` before processing the first file.

If any error occurs, the extension issues a fatal error to terminate processing immediately without damaging the original file.

Here are some simple examples:

```
$ gawk -i inplace '{ gsub(/foo/, "bar") }; { print }' file1 file2 file3
```

To keep a backup copy of the original files, try this:

```
$ gawk -i inplace -v inplace::suffix=.bak '{ gsub(/foo/, "bar") }
> { print }' file1 file2 file3
```

Please note that, while the extension does attempt to preserve ownership and permissions, it makes no attempt to copy the ACLs from the original file.

If the program dies prematurely, as might happen if an unhandled signal is received, a temporary file may be left behind.

#### 17.7.5 Character and Numeric values: `ord()` and `chr()`

The `ordchr` extension adds two functions, named `ord()` and `chr()`, as follows:

**`@load "ordchr"`**

This is how you load the extension.

**`number = ord(string)` ¶**

Return the numeric value of the first character in `string`.

**`char = chr(number)` ¶**

Return a string whose first character is that represented by `number`.

These functions are inspired by the Pascal language functions of the same name. Here is an example:

```
@load "ordchr"
...
printf("The numeric value of 'A' is %d\n", ord("A"))
printf("The string value of 65 is %s\n", chr(65))
```

As of release 5.4 of `gawk`, the extension can handle multibyte / wide character sets. If given an invalid multibyte string, in a UTF-8 locale, `ord()` returns the Unicode “invalid character” value, `0xFFFD`. Otherwise, it returns the numeric value of the first byte in the string. In a single-byte locale, `ord()` always returns the numeric value of the first byte in the string.

#### 17.7.6 Reading Directories

The `readdir` extension adds an input parser for directories. The usage is as follows:

```
@load "readdir"
```

When this extension is in use, instead of skipping directories named on the command line (or with `getline`), they are read, with each entry returned as a record.

The record consists of three fields separated by forward slash characters. The first two are the inode number and the file name, and the third field is a single letter indicating the type of the file. The letters and their corresponding file types are shown in Table 17.4.

| Letter | File type |
|---|---|
| `b` | Block device |
| `c` | Character device |
| `d` | Directory |
| `f` | Regular file |
| `l` | Symbolic link |
| `p` | Named pipe (FIFO) |
| `s` | Socket |

**Table 17.4:**File types returned by the `readdir` extension

On systems where the directory entry contains the file type, the third field is filled in from that information. On systems without the file type information, the extension falls back to calling the `stat()` system call in order to provide the information. Thus the third field should never be ‘u’ (for “unknown”).

Normally, when reading directories, you should set `FS` equal to `"/"`. However, you may instead chose to create `PROCINFO["readdir_override"]` (with any value). If this element exists when the directory is opened, then the extension automatically sets the fields in each record for you.

By default, if a directory cannot be opened (due to permission problems, for example), `gawk` will exit. As with regular files, this situation can be handled using a `BEGINFILE` rule that checks `ERRNO` and prints an error or otherwise handles the problem.

Here is an example:

```
@load "readdir"
...
BEGIN { FS = "/" }
{ print "file name is", $2 }
```

#### 17.7.7 Reversing Output

The `revoutput` extension adds a simple output wrapper that reverses the characters in each output line. Its main purpose is to show how to write an output wrapper, although it may be mildly amusing for the unwary. Here is an example:

```
@load "revoutput"

BEGIN {
    REVOUT = 1
    print "don't panic" > "/dev/stdout"
}
```

The output from this program is ‘cinap t'nod’.

#### 17.7.8 Two-Way I/O Example

The `revtwoway` extension adds a simple two-way processor that reverses the characters in each line sent to it for reading back by the `awk` program. Its main purpose is to show how to write a two-way processor, although it may also be mildly amusing. The following example shows how to use it:

```
@load "revtwoway"

BEGIN {
    cmd = "/magic/mirror"
    print "don't panic" |& cmd
    cmd |& getline result
    print result
    close(cmd)
}
```

The output from this program also is: ‘cinap t'nod’.

#### 17.7.9 Dumping and Restoring an Array

The `rwarray` extension adds four functions, named `writea()`, `reada()`, `writeall()` and `readall()`, as follows:

**`@load "rwarray"`**

This is how you load the extension.

**`ret = writea(file, array)` ¶**

This function takes a string argument, which is the name of the file to which to dump the array, and the array itself as the second argument. `writea()` understands arrays of arrays. It returns one on success, or zero upon failure.

**`ret = reada(file, array)` ¶**

`reada()` is the inverse of `writea()`; it reads the file named as its first argument, filling in the array named as the second argument. It clears the array first. Here too, the return value is one on success, or zero upon failure.

**`ret = writeall(file)` ¶**

This function takes a string argument, which is the name of the file to which to dump the state of all variables. Calling this function is completely equivalent to calling `writea(file, SYMTAB)`. It returns one on success, or zero upon failure

**`ret = readall(file)` ¶**

This function takes a string argument, which is the name of the file from which to read the contents of various global variables. For each variable in the file, the data is loaded unless the variable has already been assigned a value or used as an array. In that case, the data for that variable in the file is ignored. It returns one on success, or zero upon failure.

The array created by `reada()` is identical to that written by `writea()` in the sense that the contents are the same. However, due to implementation issues, the array traversal order of the re-created array is likely to be different from that of the original array. As array traversal order in `awk` is by default undefined, this is (technically) not a problem. If you need to guarantee a particular traversal order, use the array sorting features in `gawk` to do so (see Controlling Array Traversal and Array Sorting).

The file contains binary data. All integral values are written in network byte order. However, double-precision floating-point values are written as native binary data. Thus, arrays containing only string data can theoretically be dumped on systems with one byte order and restored on systems with a different one, but this has not been tried.

Note that the `writeall()` and `readall()` functions provide a mechanism for maintaining persistent state across repeated invocations of a program. If, for example, a program calculates some statistics based on the data in a series of files, it could save state using `writeall()` after processing N files, and then reload the state using `readall()` when the N+1st file arrives to update the results.

Here is an example:

```
@load "rwarray"
...
ret = writea("arraydump.bin", array)
...
ret = reada("arraydump.bin", array)
...
ret = writeall("globalstate.bin")
...
ret = readall("globalstate.bin")
```

#### 17.7.10 Reading an Entire File

The `readfile` extension adds a single function named `readfile()`, and an input parser:

**`@load "readfile"`**

This is how you load the extension.

**`result = readfile("/some/path")` ¶**

The argument is the name of the file to read. The return value is a string containing the entire contents of the requested file. Upon error, the function returns the empty string and sets `ERRNO`.

**`BEGIN { PROCINFO["readfile"] = 1 }`**

In addition, the extension adds an input parser that is activated if `PROCINFO["readfile"]` exists. When activated, each input file is returned in its entirety as `$0`. `RT` is set to the null string.

Here is an example:

```
@load "readfile"
...
contents = readfile("/path/to/file");
if (contents == "" && ERRNO != "") {
    print("problem reading file", ERRNO) > "/dev/stderr"
    ...
}
```

#### 17.7.11 Extension Time Functions

The `time` extension adds three functions, named `gettimeofday()` `sleep()`, and `strptime()`, as follows:

**`@load "time"`**

This is how you load the extension.

**`the_time = gettimeofday()` ¶**

Return the time in seconds that has elapsed since 1970-01-01 UTC as a floating-point value. If the time is unavailable on this platform, return −1 and set `ERRNO`. The returned time should have sub-second precision, but the actual precision may vary based on the platform. If the standard C `gettimeofday()` system call is available on this platform, then it simply returns the value. Otherwise, if on MS-Windows, it tries to use `GetSystemTimeAsFileTime()`.

**`result = sleep(*seconds*)` ¶**

Attempt to sleep for *seconds* seconds. If *seconds* is negative, or the attempt to sleep fails, return −1 and set `ERRNO`. Otherwise, return zero after sleeping for the indicated amount of time. Note that *seconds* may be a floating-point (nonintegral) value. Implementation details: depending on platform availability, this function tries to use `nanosleep()` or `select()` to implement the delay.

**`timeval = strptime(*string*, *format*)` ¶**

This function takes two arguments, a string representing a date and time, and a format string describing the data in the string. It calls the C library `strptime()` function with the given values. If the parsing succeeds, the results are passed to the C library `mktime()` function, and its result is returned, expressing the time in seconds since the epoch in the current local timezone, regardless of any timezone specified in the string arguments. Otherwise it returns −1 upon error.

#### 17.7.12 API Tests

The `testext` extension exercises parts of the extension API that are not tested by the other samples. The extension/testext.c file contains both the C code for the extension and `awk` test code inside C comments that run the tests. The testing framework extracts the `awk` code and runs the tests. See the source file for more information.

### 17.8 The `gawkextlib` Project

The `gawkextlib` project provides a number of `gawk` extensions, including one for processing XML files. This is the evolution of the original `xgawk` (XML `gawk`) project.

There are a number of extensions. The list of available extensions as well as their on-line full documentation can be seen in the `gawkextlib` web pages.

Some of the more interesting extensions are:

- `abort` extension. It allows you to exit immediately from your `awk` program without running the `END` rules.
- `json` extension. This serializes a multidimensional array into a JSON string, and can deserialize a JSON string into a `gawk` array. This extension is interesting since it is written in C++ instead of C.
- MPFR library extension. This provides access to a number of MPFR functions that `gawk`’s native MPFR support does not.
- Select extension. It provides functionality based on the `select()` system call.
- XML parser extension, using the Expat XML parsing library

You can check out the code for the `gawkextlib` project using the Git distributed source code control system. The command is as follows:

```
git clone git://git.code.sf.net/p/gawkextlib/code gawkextlib-code
```

You will need to have the RapidJson JSON parser library installed in order to build and use the `json` extension.

You will need to have the Expat XML parser library installed in order to build and use the XML extension.

In addition, you must have the GNU Autotools installed (Autoconf, Automake, Libtool, and GNU `gettext`).

The simple recipe for building and testing `gawkextlib` is as follows. First, build and install `gawk`:

```
cd .../path/to/gawk/code
./configure --prefix=/tmp/newgawk     Install in /tmp/newgawk for now
make && make check                    Build and check that all is OK
make install                          Install gawk
```

Next, go to https://sourceforge.net/projects/gawkextlib/files to download `gawkextlib` and any extensions that you would like to build. The README file at that site explains how to build the code. If you installed `gawk` in a non-standard location, you will need to specify ‘./configure --with-gawk=*/path/to/gawk*’ to find it. You may need to use the `sudo` utility to install both `gawk` and `gawkextlib`, depending upon how your system works.

If you write an extension that you wish to share with other `gawk` users, consider doing so through the `gawkextlib` project. See the project’s website for more information.

### 17.9 Summary

- You can write extensions (sometimes called plug-ins) for `gawk` in C or C++ using the application programming interface (API) defined by the `gawk` developers.
- Extensions must have a license compatible with the GNU General Public License (GPL), and they must assert that fact by declaring a variable named `plugin_is_GPL_compatible`.
- Communication between `gawk` and an extension is two-way. `gawk` passes a `struct` to the extension that contains various data fields and function pointers. The extension can then call into `gawk` via the supplied function pointers to accomplish certain tasks.
- One of these tasks is to “register” the name and implementation of new `awk`-level functions with `gawk`. The implementation takes the form of a C function pointer with a defined signature. By convention, implementation functions are named `do_*XXXX*()` for some `awk`-level function `*XXXX*()`.
- The API is defined in a header file named gawkapi.h. You must include a number of standard header files *before* including it in your source file.
- API function pointers are provided for the following kinds of operations:
  - Allocating, reallocating, and releasing memory
  - Registration functions (you may register extension functions, exit callbacks, a version string, input parsers, output wrappers, and two-way processors)
  - Printing fatal, nonfatal, warning, and “lint” warning messages
  - Updating `ERRNO`, or unsetting it
  - Accessing parameters, including converting an undefined parameter into an array
  - Symbol table access (retrieving a global variable, creating one, or changing one)
  - Creating and releasing cached values; this provides an efficient way to use values for multiple variables and can be a big performance win
  - Manipulating arrays (retrieving, adding, deleting, and modifying elements; getting the count of elements in an array; creating a new array; clearing an array; and flattening an array for easy C-style looping over all its indices and elements)
- The API defines a number of standard data types for representing `awk` values, array elements, and arrays.
- The API provides convenience functions for constructing values. It also provides memory management functions to ensure compatibility between memory allocated by `gawk` and memory allocated by an extension.
- *All* memory passed from `gawk` to an extension must be treated as read-only by the extension.
- *All* memory passed from an extension to `gawk` must come from the API’s memory allocation functions. `gawk` takes responsibility for the memory and releases it when appropriate.
- The API provides information about the running version of `gawk` so that an extension can make sure it is compatible with the `gawk` that loaded it.
- It is easiest to start a new extension by copying the boilerplate code described in this chapter. Macros in the gawkapi.h header file make this easier to do.
- The `gawk` distribution includes a number of small but useful sample extensions. The `gawkextlib` project includes several more (larger) extensions. If you wish to write an extension and contribute it to the community of `gawk` users, the `gawkextlib` project is the place to do so.

### 17.10 Exercises

1. Add functions to implement system calls such as `chown()`, `chmod()`, and `umask()` to the file operations extension presented in C Code for `chdir()` and `stat()`.
2. Write an input parser that prints a prompt if the input is a from a “terminal” device. You can use the `isatty()` function to tell if the input file is a terminal. (Hint: this function is usually expensive to call; try to call it just once.) The content of the prompt should come from a variable settable by `awk`-level code. You can write the prompt to standard error. However, for best results, open a new file descriptor (or file pointer) on /dev/tty and print the prompt there, in case standard error has been redirected. Why is standard error a better choice than standard output for writing the prompt? Which reading mechanism should you replace, the one to get a record, or the one to read raw bytes?
3. Write a wrapper script that provides an interface similar to ‘sed -i’ for the “inplace” extension presented in Enabling In-Place File Editing.

# Part IV: Appendices
