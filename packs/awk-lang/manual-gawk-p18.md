---
title: "The GNU Awk User’s Guide (part 18/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 18/38
---

## 11 Practical `awk` Programs

A Library of `awk` Functions, presents the idea that reading programs in a language contributes to learning that language. This chapter continues that theme, presenting a potpourri of `awk` programs for your reading enjoyment. There are three sections. The first describes how to run the programs presented in this chapter.

The second presents `awk` versions of several common POSIX utilities. These are programs that you are hopefully already familiar with, and therefore whose problems are understood. By reimplementing these programs in `awk`, you can focus on the `awk`-related aspects of solving the programming problems.

The third is a grab bag of interesting programs. These solve a number of different data-manipulation and management problems. Many of the programs are short, which emphasizes `awk`’s ability to do a lot in just a few lines of code.

Many of these programs use library functions presented in A Library of `awk` Functions.

### 11.1 Running the Example Programs

To run a given program, you would typically do something like this:

```
awk -f program -- options files
```

Here, *program* is the name of the `awk` program (such as cut.awk), *options* are any command-line options for the program that start with a ‘-’, and *files* are the actual data files.

If your system supports the ‘#!’ executable interpreter mechanism (see Executable `awk` Programs), you can instead run your program directly:

```
cut.awk -c1-8 myfiles > results
```

If your `awk` is not `gawk`, you may instead need to use this:

```
cut.awk -- -c1-8 myfiles > results
```

### 11.2 Reinventing Wheels for Fun and Profit

This section presents a number of POSIX utilities implemented in `awk`. Reinventing these programs in `awk` is often enjoyable, because the algorithms can be very clearly expressed, and the code is usually very concise and simple. This is true because `awk` does so much for you.

It should be noted that these programs are not necessarily intended to replace the installed versions on your system. Nor may all of these programs be fully compliant with the most recent POSIX standard. This is not a problem; their purpose is to illustrate `awk` language programming for “real-world” tasks.

The programs are presented in alphabetical order.

#### 11.2.1 Cutting Out Fields and Columns

The `cut` utility selects, or “cuts,” characters or fields from its standard input and sends them to its standard output. Fields are separated by TABs by default, but you may supply a command-line option to change the field *delimiter* (i.e., the field-separator character). `cut`’s definition of fields is less general than `awk`’s.

A common use of `cut` might be to pull out just the login names of logged-on users from the output of `who`. For example, the following pipeline generates a sorted, unique list of the logged-on users:

```
who | cut -c1-8 | sort | uniq
```

The options for `cut` are:

**`-c *list*`**

Use *list* as the list of characters to cut out. Items within the list may be separated by commas, and ranges of characters can be separated with dashes. The list ‘1-8,15,22-35’ specifies characters 1 through 8, 15, and 22 through 35.

**`-d *delim*`**

Use *delim* as the field-separator character instead of the TAB character.

**`-f *list*`**

Use *list* as the list of fields to cut out.

**`-s`**

Suppress printing of lines that do not contain the field delimiter.

The `awk` implementation of `cut` uses the `getopt()` library function (see Processing Command-Line Options) and the `join()` library function (see Merging an Array into a String).

The current POSIX version of `cut` has options to cut fields based on both bytes and characters. This version does not attempt to implement those options, as `awk` works exclusively in terms of characters.

The program begins with a comment describing the options, the library functions needed, and a `usage()` function that prints out a usage message and exits. `usage()` is called if invalid arguments are supplied:

```
# cut.awk --- implement cut in awk

# Options:
#    -c list     Cut characters
#    -f list     Cut fields
#    -d c        Field delimiter character
#
#    -s          Suppress lines without the delimiter
#
# Requires getopt() and join() library functions
```

```
function usage()
{
    print("usage: cut [-f list] [-d c] [-s] [files...]") > "/dev/stderr"
    print("       cut [-c list] [files...]") > "/dev/stderr"
    exit 1
}
```

Next comes a `BEGIN` rule that parses the command-line options. It sets `FS` to a single TAB character, because that is `cut`’s default field separator. The rule then sets the output field separator to be the same as the input field separator. A loop using `getopt()` steps through the command-line options. Exactly one of the variables `by_fields` or `by_chars` is set to true, to indicate that processing should be done by fields or by characters, respectively. When cutting by characters, the output field separator is set to the null string:

```
BEGIN {
    FS = "\t"    # default
    OFS = FS
    while ((c = getopt(ARGC, ARGV, "sf:c:d:")) != -1) {
        if (c == "f") {
            by_fields = 1
            fieldlist = Optarg
        } else if (c == "c") {
            by_chars = 1
            fieldlist = Optarg
            OFS = ""
        } else if (c == "d") {
            if (length(Optarg) > 1) {
                printf("cut: using first character of %s" \
                       " for delimiter\n", Optarg) > "/dev/stderr"
                Optarg = substr(Optarg, 1, 1)
            }
            fs = FS = Optarg
            OFS = FS
            if (FS == " ")    # defeat awk semantics
                FS = "[ ]"
        } else if (c == "s")
            suppress = 1
        else
            usage()
    }

    # Clear out options
    for (i = 1; i < Optind; i++)
        ARGV[i] = ""
```

The code must take special care when the field delimiter is a space. Using a single space (`" "`) for the value of `FS` is incorrect—`awk` would separate fields with runs of spaces, TABs, and/or newlines, and we want them to be separated with individual spaces. To this end, we save the original space character in the variable `fs` for later use; after setting `FS` to `"[ ]"` we can’t use it directly to see if the field delimiter character is in the string.

Also remember that after `getopt()` is through (as described in Processing Command-Line Options), we have to clear out all the elements of `ARGV` from 1 to `Optind`, so that `awk` does not try to process the command-line options as file names.

After dealing with the command-line options, the program verifies that the options make sense. Only one or the other of -c and -f should be used, and both require a field list. Then the program calls either `set_fieldlist()` or `set_charlist()` to pull apart the list of fields or characters:

```
    if (by_fields && by_chars)
        usage()

    if (by_fields == 0 && by_chars == 0)
        by_fields = 1    # default
```

```
    if (fieldlist == "") {
        print "cut: needs list for -c or -f" > "/dev/stderr"
        exit 1
    }
```

```
    if (by_fields)
        set_fieldlist()
    else
        set_charlist()
}
```

`set_fieldlist()` splits the field list apart at the commas into an array. Then, for each element of the array, it looks to see if the element is actually a range, and if so, splits it apart. The function checks the range to make sure that the first number is smaller than the second. Each number in the list is added to the `flist` array, which simply lists the fields that will be printed. Normal field splitting is used. The program lets `awk` handle the job of doing the field splitting:

```
function set_fieldlist(        n, m, i, j, k, f, g)
{
    n = split(fieldlist, f, ",")
    j = 1    # index in flist
    for (i = 1; i <= n; i++) {
        if (index(f[i], "-") != 0) { # a range
            m = split(f[i], g, "-")
```

```
            if (m != 2 || g[1] >= g[2]) {
                printf("cut: bad field list: %s\n",
                                  f[i]) > "/dev/stderr"
                exit 1
            }
```

```
            for (k = g[1]; k <= g[2]; k++)
                flist[j++] = k
        } else
            flist[j++] = f[i]
    }
    nfields = j - 1
}
```

The `set_charlist()` function is more complicated than `set_fieldlist()`. The idea here is to use `gawk`’s `FIELDWIDTHS` variable (see Reading Fixed-Width Data), which describes constant-width input. When using a character list, that is exactly what we have.

Setting up `FIELDWIDTHS` is more complicated than simply listing the fields that need to be printed. We have to keep track of the fields to print and also the intervening characters that have to be skipped. For example, suppose you wanted characters 1 through 8, 15, and 22 through 35. You would use ‘-c 1-8,15,22-35’. The necessary value for `FIELDWIDTHS` is `"8 6 1 6 14"`. This yields five fields, and the fields to print are `$1`, `$3`, and `$5`. The intermediate fields are *filler*, which is stuff in between the desired data. `flist` lists the fields to print, and `t` tracks the complete field list, including filler fields:

```
function set_charlist(    field, i, j, f, g, n, m, t,
                          filler, last, len)
{
    field = 1   # count total fields
    n = split(fieldlist, f, ",")
    j = 1       # index in flist
    for (i = 1; i <= n; i++) {
        if (index(f[i], "-") != 0) { # range
            m = split(f[i], g, "-")
            if (m != 2 || g[1] >= g[2]) {
                printf("cut: bad character list: %s\n",
                               f[i]) > "/dev/stderr"
                exit 1
            }
            len = g[2] - g[1] + 1
            if (g[1] > 1)  # compute length of filler
                filler = g[1] - last - 1
            else
                filler = 0
```

```
            if (filler)
                t[field++] = filler
```

```
            t[field++] = len  # length of field
            last = g[2]
            flist[j++] = field - 1
        } else {
            if (f[i] > 1)
                filler = f[i] - last - 1
            else
                filler = 0
            if (filler)
                t[field++] = filler
            t[field++] = 1
            last = f[i]
            flist[j++] = field - 1
        }
    }
    FIELDWIDTHS = join(t, 1, field - 1)
    nfields = j - 1
}
```

Next is the rule that processes the data. If the -s option is given, then `suppress` is true. The first `if` statement makes sure that the input record does have the field separator. If `cut` is processing fields, `suppress` is true, and the field separator character is not in the record, then the record is skipped.

If the record is valid, then `gawk` has split the data into fields, either using the character in `FS` or using fixed-length fields and `FIELDWIDTHS`. The loop goes through the list of fields that should be printed. The corresponding field is printed if it contains data. If the next field also has data, then the separator character is written out between the fields:

```
{
    if (by_fields && suppress && index($0, fs) == 0)
        next

    for (i = 1; i <= nfields; i++) {
        if ($flist[i] != "") {
            printf "%s", $flist[i]
            if (i < nfields && $flist[i+1] != "")
                printf "%s", OFS
        }
    }
    print ""
}
```

This version of `cut` relies on `gawk`’s `FIELDWIDTHS` variable to do the character-based cutting. It is possible in other `awk` implementations to use `substr()` (see String-Manipulation Functions), but it is also extremely painful. The `FIELDWIDTHS` variable supplies an elegant solution to the problem of picking the input line apart by characters.

#### 11.2.2 Searching for Regular Expressions in Files

The `grep` family of programs searches files for patterns. These programs have an unusual history. Initially there was `grep` (Global Regular Expression Print), which used what are now called Basic Regular Expressions (BREs). Later there was `egrep` (Extended `grep`) which used what are now called Extended Regular Expressions (EREs). (These are almost identical to those available in `awk`; see Regular Expressions). There was also `fgrep` (Fast `grep`), which searched for matches of one or more fixed strings.

POSIX chose to combine these three programs into one, simply named `grep`. On a POSIX system, `grep`’s default behavior is to search using BREs. You use `-E` to specify the use of EREs, and -F to specify searching for fixed strings.

In practice, systems continue to come with separate `egrep` and `fgrep` utilities, for backwards compatibility. This section provides an `awk` implementation of `egrep`, which supports all of the POSIX-mandated options. You invoke it as follows:

```
egrep [options] 'pattern' files ...
```

The *pattern* is a regular expression. In typical usage, the regular expression is quoted to prevent the shell from expanding any of the special characters as file name wildcards. Normally, `egrep` prints the lines that matched. If multiple file names are provided on the command line, each output line is preceded by the name of the file and a colon.

The options to `egrep` are as follows:

**`-c`**

Print a count of the lines that matched the pattern, instead of the lines themselves.

**`-e *pattern*`**

Use *pattern* as the regexp to match. The purpose of the -e option is to allow patterns that start with a ‘-’.

**`-i`**

Ignore case distinctions in both the pattern and the input data.

**`-l`**

Only print (list) the names of the files that matched, not the lines that matched.

**`-q`**

Be quiet. No output is produced and the exit value indicates whether the pattern was matched.

**`-s`**

Be silent. Do not print error messages for files that could not be opened.

**`-v`**

Invert the sense of the test. `egrep` prints the lines that do *not* match the pattern and exits successfully if the pattern is not matched.

**`-x`**

Match the entire input line in order to consider the match as having succeeded.

This version uses the `getopt()` library function (see Processing Command-Line Options) and `gawk`’s `BEGINFILE` and `ENDFILE` special patterns (see The `BEGINFILE` and `ENDFILE` Special Patterns).

The program begins with descriptive comments and then a `BEGIN` rule that processes the command-line arguments with `getopt()`. The -i (ignore case) option is particularly easy with `gawk`; we just use the `IGNORECASE` predefined variable (see Predefined Variables):

```
# egrep.awk --- simulate egrep in awk

# Options:
#    -c    count of lines
#    -e    argument is pattern
#    -i    ignore case
#    -l    print filenames only
#    -n    add line number to output
#    -q    quiet - use exit value
#    -s    silent - don't print errors
#    -v    invert test, success if no match
#    -x    the entire line must match
#
# Requires getopt library function
# Uses IGNORECASE, BEGINFILE and ENDFILE
# Invoke using gawk -f egrep.awk -- options ...

BEGIN {
    while ((c = getopt(ARGC, ARGV, "ce:ilnqsvx")) != -1) {
        if (c == "c")
            count_only++
        else if (c == "e")
            pattern = Optarg
        else if (c == "i")
            IGNORECASE = 1
        else if (c == "l")
            filenames_only++
        else if (c == "n")
            line_numbers++
        else if (c == "q")
            no_print++
        else if (c == "s")
            no_errors++
        else if (c == "v")
            invert++
        else if (c == "x")
            full_line++
        else
            usage()
    }
```

Note the comment about invocation: Because several of the options overlap with `gawk`’s, a -- is needed to tell `gawk` to stop looking for options.

Next comes the code that handles the `egrep`-specific behavior. `egrep` uses the first nonoption on the command line if no pattern is supplied with -e. If the pattern is empty, that means no pattern was supplied, so it’s necessary to print an error message and exit. The command-line arguments up to `ARGV[Optind]` are cleared, so that `gawk` won’t try to process them as files. If no files are specified, the standard input is used, and if multiple files are specified, we make sure to note this so that the file names can precede the matched lines in the output:

```
    if (pattern == "")
        pattern = ARGV[Optind++]

    if (pattern == "")
      usage()

    for (i = 1; i < Optind; i++)
        ARGV[i] = ""

    if (Optind >= ARGC) {
        ARGV[1] = "-"
        ARGC = 2
    } else if (ARGC - Optind > 1)
        do_filenames++
}
```

The `BEGINFILE` rule executes when each new file is processed. In this case, it is fairly simple; it initializes a variable `fcount` to zero. `fcount` tracks how many lines in the current file matched the pattern.

Here also is where we implement the -s option. We check if `ERRNO` has been set, and if -s was supplied. In that case, it’s necessary to move on to the next file. Otherwise `gawk` would exit with an error:

```
BEGINFILE {
    fcount = 0
    if (ERRNO && no_errors)
        nextfile
}
```

The `ENDFILE` rule executes after each file has been processed. It affects the output only when the user wants a count of the number of lines that matched. `no_print` is true only if the exit status is desired. `count_only` is true if line counts are desired. `egrep` therefore only prints line counts if printing and counting are enabled. The output format must be adjusted depending upon the number of files to process. Finally, `fcount` is added to `total`, so that we know the total number of lines that matched the pattern:

```
ENDFILE {
    if (! no_print && count_only) {
        if (do_filenames)
            print file ":" fcount
        else
            print fcount
    }
```

```
    total += fcount
}
```

The following rule does most of the work of matching lines. The variable `matches` is true (non-zero) if the line matched the pattern. If the user specified that the entire line must match (with -x), the code checks this condition by looking at the values of `RSTART` and `RLENGTH`. If those indicate that the match is not over the full line, `matches` is set to zero (false).

If the user wants lines that did not match, we invert the sense of `matches` using the ‘!’ operator. We then increment `fcount` with the value of `matches`, which is either one or zero, depending upon a successful or unsuccessful match. If the line does not match, the `next` statement just moves on to the next input line.

We make a number of additional tests, but only if we are not counting lines. First, if the user only wants the exit status (`no_print` is true), then it is enough to know that *one* line in this file matched, and we can skip on to the next file with `nextfile`. Similarly, if we are only printing file names, we can print the file name, and then skip to the next file with `nextfile`. Finally, each line is printed, with a leading file name, optional colon and line number, and the final colon if necessary:

```
{
    matches = match($0, pattern)
    if (matches && full_line && (RSTART != 1 || RLENGTH != length()))
         matches = 0

    if (invert)
        matches = ! matches

    fcount += matches    # 1 or 0

    if (! matches)
        next

    if (! count_only) {
        if (no_print)
            nextfile

        if (filenames_only) {
            print FILENAME
            nextfile
        }

        if (do_filenames)
            if (line_numbers)
               print FILENAME ":" FNR ":" $0
            else
               print FILENAME ":" $0
        else
            print
    }
}
```

The `END` rule takes care of producing the correct exit status. If there are no matches, the exit status is one; otherwise, it is zero:

```
END {
    exit (total == 0)
}
```

The `usage()` function prints a usage message in case of invalid options, and then exits:

```
function usage()
{
    print("Usage:\tegrep [-cilnqsvx] [-e pat] [files ...]") > "/dev/stderr"
    print("\tegrep [-cilnqsvx] pat [files ...]") > "/dev/stderr"
    exit 1
}
```

#### 11.2.3 Printing Out User Information

The `id` utility lists a user’s real and effective user ID numbers, real and effective group ID numbers, and the user’s group set, if any. `id` only prints the effective user ID and group ID if they are different from the real ones. If possible, `id` also supplies the corresponding user and group names. The output might look like this:

```
$ id
-| uid=1000(arnold) gid=1000(arnold) groups=1000(arnold),4(adm),7(lp),27(sudo)
```

This information is part of what is provided by `gawk`’s `PROCINFO` array (see Predefined Variables). However, the `id` utility provides a more palatable output than just individual numbers.

The POSIX version of `id` takes several options that give you control over the output’s format, such as printing only real ids, or printing only numbers or only names. Additionally, you can print the information for a specific user, instead of that of the current user.

Here is a version of POSIX `id` written in `awk`. It uses the `getopt()` library function (see Processing Command-Line Options), the user database library functions (see Reading the User Database), and the group database library functions (see Reading the Group Database) from A Library of `awk` Functions.

The program is moderately straightforward. All the work is done in the `BEGIN` rule. It starts with explanatory comments, a list of options, and then a `usage()` function:

```
# id.awk --- implement id in awk
#
# Requires user and group library functions and getopt

# output is:
# uid=12(foo) euid=34(bar) gid=3(baz) \
#             egid=5(blat) groups=9(nine),2(two),1(one)

# Options:
#   -G Output all group ids as space separated numbers (ruid, euid, groups)
#   -g Output only the euid as a number
#   -n Output name instead of the numeric value (with -g/-G/-u)
#   -r Output ruid/rguid instead of effective id
#   -u Output only effective user id, as a number
```

```
function usage()
{
    printf("Usage:\n" \
           "\tid [user]\n" \
           "\tid -G [-n] [user]\n" \
           "\tid -g [-nr] [user]\n" \
           "\tid -u [-nr] [user]\n") > "/dev/stderr"

    exit 1
}
```

The first step is to parse the options using `getopt()`, and to set various flag variables according to the options given:

```
BEGIN {
    # parse args
    while ((c = getopt(ARGC, ARGV, "Ggnru")) != -1) {
        if (c == "G")
            groupset_only++
        else if (c == "g")
            egid_only++
        else if (c == "n")
            names_not_groups++
        else if (c == "r")
            real_ids_only++
        else if (c == "u")
            euid_only++
        else
            usage()
    }
```

The next step is to check that no conflicting options were provided. -G and -r are mutually exclusive. It is also not allowed to provide more than one user name on the command line:

```
    if (groupset_only && real_ids_only)
        usage()
    else if (ARGC - Optind > 1)
        usage()
```

The user and group ID numbers are obtained from `PROCINFO` for the current user, or from the user and password databases for a user supplied on the command line. In the latter case, `real_ids_only` is set, since it’s not possible to print information about the effective user and group IDs:

```
    if (ARGC - Optind == 0) {
        # gather info for current user
        uid = PROCINFO["uid"]
        euid = PROCINFO["euid"]
        gid = PROCINFO["gid"]
        egid = PROCINFO["egid"]
        for (i = 1; ("group" i) in PROCINFO; i++)
            groupset[i] = PROCINFO["group" i]
    } else {
        fill_info_for_user(ARGV[ARGC-1])
        real_ids_only++
    }
```

The test in the `for` loop is worth noting. Any supplementary groups in the `PROCINFO` array have the indices `"group1"` through `"group*N*"` for some *N* (i.e., the total number of supplementary groups). However, we don’t know in advance how many of these groups there are.

This loop works by starting at one, concatenating the value with `"group"`, and then using `in` to see if that value is in the array (see Referring to an Array Element). Eventually, `i` increments past the last group in the array and the loop exits.

The loop is also correct if there are *no* supplementary groups; then the condition is false the first time it’s tested, and the loop body never executes.

Now, based on the options, we decide what information to print. For -G (print just the group set), we then select whether to print names or numbers. In either case, when done we exit:

```
    if (groupset_only) {
        if (names_not_groups) {
            for (i = 1; i in groupset; i++) {
                entry = getgrgid(groupset[i])
                name = get_first_field(entry)
                printf("%s", name)
                if ((i + 1) in groupset)
                    printf(" ")
            }
        } else {
            for (i = 1; i in groupset; i++) {
                printf("%u", groupset[i])
                if ((i + 1) in groupset)
                    printf(" ")
            }
        }

        print ""    # final newline
        exit 0
    }
```

Otherwise, for -g (effective group ID only), we check if -r was also provided, in which case we use the real group ID. Then based on -n, we decide whether to print names or numbers. Here too, when done, we exit:

```
    else if (egid_only) {
        id = real_ids_only ? gid : egid
        if (names_not_groups) {
            entry = getgrgid(id)
            name = get_first_field(entry)
            printf("%s\n", name)
        } else {
            printf("%u\n", id)
        }

        exit 0
    }
```

The `get_first_field()` function extracts the group name from the group database entry for the given group ID.

Similar processing logic applies to -u (effective user ID only), combined with -r and -n:

```
    else if (euid_only) {
        id = real_ids_only ? uid : euid
        if (names_not_groups) {
            entry = getpwuid(id)
            name = get_first_field(entry)
            printf("%s\n", name)
        } else {
            printf("%u\n", id)
        }

        exit 0
    }
```

At this point, we haven’t exited yet, so we print the regular, default output, based either on the current user’s information, or that of the user whose name was provided on the command line. We start with the real user ID:

```
    printf("uid=%d", uid)
    pw = getpwuid(uid)
    print_first_field(pw)
```

The `print_first_field()` function prints the user’s login name from the password file entry, surrounded by parentheses. It is shown soon. Printing the effective user ID is next:

```
    if (euid != uid && ! real_ids_only) {
        printf(" euid=%d", euid)
        pw = getpwuid(euid)
        print_first_field(pw)
    }
```

Similar logic applies to the real and effective group IDs:

```
    printf(" gid=%d", gid)
    pw = getgrgid(gid)
    print_first_field(pw)

    if (egid != gid && ! real_ids_only) {
        printf(" egid=%d", egid)
        pw = getgrgid(egid)
        print_first_field(pw)
    }
```

Finally, we print the group set and the terminating newline:

```
    for (i = 1; i in groupset; i++) {
        if (i == 1)
            printf(" groups=")
        group = groupset[i]
        printf("%d", group)
        pw = getgrgid(group)
        print_first_field(pw)
        if ((i + 1) in groupset)
            printf(",")
    }

    print ""
}
```

The `get_first_field()` function extracts the first field from a password or group file entry for use as a user or group name. Fields are separated by ‘:’ characters:

```
function get_first_field(str,  a)
{
    if (str != "") {
        split(str, a, ":")
        return a[1]
    }
}
```

This function is then used by `print_first_field()` to output the given name surrounded by parentheses:

```
function print_first_field(str)
{
    first = get_first_field(str)
    printf("(%s)", first)
}
```

These two functions simply isolate out some code that is used repeatedly, making the whole program shorter and cleaner. In particular, moving the check for the empty string into `get_first_field()` saves several lines of code.

Finally, `fill_info_for_user()` fetches user, group, and group set information for the user named on the command. The code is fairly straightforward, merely requiring that we exit if the given user doesn’t exist:

```
function fill_info_for_user(user,
                            pwent, fields, groupnames, grent, groups, i)
{
    pwent = getpwnam(user)
    if (pwent == "") {
        printf("id: '%s': no such user\n", user) > "/dev/stderr"
        exit 1
    }

    split(pwent, fields, ":")
    uid = fields[3] + 0
    gid = fields[4] + 0
```

Getting the group set is a little awkward. The library routine `getgruser()` returns a list of group *names*. These have to be gone through and turned back into group numbers, so that the rest of the code will work as expected:

```
    groupnames = getgruser(user)
    split(groupnames, groups, " ")
    for (i = 1; i in groups; i++) {
        grent = getgrnam(groups[i])
        split(grent, fields, ":")
        groupset[i] = fields[3] + 0
    }
}
```

#### 11.2.4 Splitting a Large File into Pieces

The `split` utility splits large text files into smaller pieces. The usage follows the POSIX standard for `split` and is as follows:

```
split [-l count] [-a suffix-len] [file [outname]]
split -b N[k|m]] [-a suffix-len] [file [outname]]
```

By default, the output files are named xaa, xab, and so on. Each file has 1,000 lines in it, with the likely exception of the last file.

The `split` program has evolved over time, and the current POSIX version is more complicated than the original Unix version. The options and what they do are as follows:

**-a *suffix-len***

Use *suffix-len* characters for the suffix. For example, if *suffix-len* is four, the output files would range from xaaaa to xzzzz.

**-b *N*[`k`|`m`]]**

Instead of each file containing a specified number of lines, each file should have (at most) *N* bytes. Supplying a trailing ‘k’ multiplies *N* by 1,024, yielding kilobytes. Supplying a trailing ‘m’ multiplies *N* by 1,048,576 (*1,024 * 1,024*) yielding megabytes. (This option is mutually exclusive with -l).

**-l *count***

Each file should have at most *count* lines, instead of the default 1,000. (This option is mutually exclusive with -b).

If supplied, *file* is the input file to read. Otherwise standard input is processed. If supplied, *outname* is the leading prefix to use for file names, instead of ‘x’.

In order to use the -b option, `gawk` should be invoked with its -b option (see Command-Line Options), or with the environment variable `LC_ALL` set to ‘C’, so that each input byte is treated as a separate character.79

Here is an implementation of `split` in `awk`. It uses the `getopt()` function presented in Processing Command-Line Options.

The program begins with a standard descriptive comment and then a `usage()` function describing the options. The variable `common` keeps the function’s lines short so that they look nice on the page:

```
# split.awk --- do split in awk
#
# Requires getopt() library function.

function usage(     common)
{
    common = "[-a suffix-len] [file [outname]]"
    printf("usage: split [-l count]  %s\n", common) > "/dev/stderr"
    printf("       split [-b N[k|m]] %s\n", common) > "/dev/stderr"
    exit 1
}
```

Next, in a `BEGIN` rule we set the default values and parse the arguments. After that we initialize the data structures used to cycle the suffix from ‘aa…’ to ‘zz…’. Finally we set the name of the first output file:

```
BEGIN {
    # Set defaults:
    Suffix_length = 2
    Line_count = 1000
    Byte_count = 0
    Outfile = "x"

    parse_arguments()

    init_suffix_data()

    Output = (Outfile compute_suffix())
}
```

Parsing the arguments is straightforward. The program follows our convention (see Naming Library Function Global Variables) of having important global variables start with an uppercase letter:

```
function parse_arguments(   i, c, l, modifier)
{
    while ((c = getopt(ARGC, ARGV, "a:b:l:")) != -1) {
        if (c == "a")
            Suffix_length = Optarg + 0
        else if (c == "b") {
            Byte_count = Optarg + 0
            Line_count = 0

            l = length(Optarg)
            modifier = substr(Optarg, l, 1)
            if (modifier == "k")
                Byte_count *= 1024
            else if (modifier == "m")
                Byte_count *= 1024 * 1024
        } else if (c == "l") {
            Line_count = Optarg + 0
            Byte_count = 0
        } else
            usage()
    }

    # Clear out options
    for (i = 1; i < Optind; i++)
        ARGV[i] = ""

    # Check for filename
    if (ARGV[Optind]) {
        Optind++

        # Check for different prefix
        if (ARGV[Optind]) {
            Outfile = ARGV[Optind]
            ARGV[Optind] = ""

            if (++Optind < ARGC)
                usage()
        }
    }
}
```

Managing the file name suffix is interesting. Given a suffix of length three, say, the values go from ‘aaa’, ‘aab’, ‘aac’ and so on, all the way to ‘zzx’, ‘zzy’, and finally ‘zzz’. There are two important aspects to this:

- We have to be able to easily generate these suffixes, and in particular easily handle “rolling over”; for example, going from ‘abz’ to ‘aca’.
- We have to tell when we’ve finished with the last file, so that if we still have more input data we can print an error message and exit. The trick is to handle this *after* using the last suffix, and not when the final suffix is created.

The computation is handled by `compute_suffix()`. This function is called every time a new file is opened.

The flow here is messy, because we want to generate ‘zzzz’ (say), and use it, and only produce an error after all the file name suffixes have been used up. The logical steps are as follows:

1. Generate the suffix, saving the value in `result` to return. To do this, the supplementary array `Suffix_ind` contains one element for each letter in the suffix. Each element ranges from 1 to 26, acting as the index into a string containing all the lowercase letters of the English alphabet. It is initialized by `init_suffix_data()`. `result` is built up one letter at a time, using each `substr()`.
2. Prepare the data structures for the next time `compute_suffix()` is called. To do this, we loop over `Suffix_ind`, *backwards*. If the current element is less than 26, it’s incremented and the loop breaks (‘abq’ goes to ‘abr’). Otherwise, the element is reset to one and we move down the list (‘abz’ to ‘aca’). Thus, the `Suffix_ind` array is always “one step ahead” of the actual file name suffix to be returned.
3. Check if we’ve gone past the limit of possible file names. If `Reached_last` is true, print a message and exit. Otherwise, check if `Suffix_ind` describes a suffix where all the letters are ‘z’. If that’s the case we’re about to return the final suffix. If so, we set `Reached_last` to true so that the *next* call to `compute_suffix()` will cause a failure.

Physically, the steps in the function occur in the order 3, 1, 2:

```
function compute_suffix(    i, result, letters)
{
    # Logical step 3
    if (Reached_last) {
        printf("split: too many files!\n") > "/dev/stderr"
        exit 1
    } else if (on_last_file())
        Reached_last = 1    # fail when wrapping after 'zzz'

    # Logical step 1
    result = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for (i = 1; i <= Suffix_length; i++)
        result = result substr(letters, Suffix_ind[i], 1)

    # Logical step 2
    for (i = Suffix_length; i >= 1; i--) {
        if (++Suffix_ind[i] > 26) {
            Suffix_ind[i] = 1
        } else
            break
    }

    return result
}
```

The `Suffix_ind` array and `Reached_last` are initialized by `init_suffix_data()`:

```
function init_suffix_data(  i)
{
    for (i = 1; i <= Suffix_length; i++)
        Suffix_ind[i] = 1

    Reached_last = 0
}
```

The function `on_last_file()` returns true if `Suffix_ind` describes a suffix where all the letters are ‘z’ by checking that all the elements in the array are equal to 26:

```
function on_last_file(  i, on_last)
{
    on_last = 1
    for (i = 1; i <= Suffix_length; i++) {
        on_last = on_last && (Suffix_ind[i] == 26)
    }

    return on_last
}
```

The actual work of splitting the input file is done by the next two rules. Since splitting by line count and splitting by byte count are mutually exclusive, we simply use two separate rules, one for when `Line_count` is greater than zero, and another for when `Byte_count` is greater than zero.

The variable `tcount` counts how many lines have been processed so far. When it exceeds `Line_count`, it’s time to close the previous file and switch to a new one:

```
Line_count > 0 {
    if (++tcount > Line_count) {
        close(Output)
        Output = (Outfile compute_suffix())
        tcount = 1
    }
    print > Output
}
```

The rule for handling bytes is more complicated. Since lines most likely vary in length, the `Byte_count` boundary may be hit in the middle of an input record. In that case, `split` has to write enough of the first bytes of the input record to finish up `Byte_count` bytes, close the file, open a new file, and write the rest of the record to the new file. The logic here does all that:

```
Byte_count > 0 {
    # `+ 1' is for the final newline
    if (tcount + length($0) + 1 > Byte_count) { # would overflow
        # compute leading bytes
        leading_bytes = Byte_count - tcount

        # write leading bytes
        printf("%s", substr($0, 1, leading_bytes)) > Output

        # close old file, open new file
        close(Output)
        Output = (Outfile compute_suffix())

        # set up first bytes for new file
        $0 = substr($0, leading_bytes + 1)  # trailing bytes
        tcount = 0
    }

    # write full record or trailing bytes
    tcount += length($0) + 1
    print > Output
}
```

Finally, the `END` rule cleans up by closing the last output file:

```
END {
    close(Output)
}
```

#### 11.2.5 Duplicating Output into Multiple Files

The `tee` program is known as a “pipe fitting.” `tee` copies its standard input to its standard output and also duplicates it to the files named on the command line. Its usage is as follows:

```
tee [-a] file ...
```

The -a option tells `tee` to append to the named files, instead of truncating them and starting over.

The `BEGIN` rule first makes a copy of all the command-line arguments into an array named `copy`. `ARGV[0]` is not needed, so it is not copied. `tee` cannot use `ARGV` directly, because `awk` attempts to process each file name in `ARGV` as input data.

If the first argument is -a, then the flag variable `append` is set to true, and both `ARGV[1]` and `copy[1]` are deleted. If `ARGC` is less than two, then no file names were supplied and `tee` prints a usage message and exits. Finally, `awk` is forced to read the standard input by setting `ARGV[1]` to `"-"` and `ARGC` to two:

```
# tee.awk --- tee in awk
#
# Copy standard input to all named output files.
# Append content if -a option is supplied.

BEGIN {
    for (i = 1; i < ARGC; i++)
        copy[i] = ARGV[i]

    if (ARGV[1] == "-a") {
        append = 1
        delete ARGV[1]
        delete copy[1]
        ARGC--
    }
    if (ARGC < 2) {
        print "usage: tee [-a] file ..." > "/dev/stderr"
        exit 1
    }
    ARGV[1] = "-"
    ARGC = 2
}
```

The following single rule does all the work. Because there is no pattern, it is executed for each line of input. The body of the rule simply prints the line into each file on the command line, and then to the standard output:

```
{
    # moving the if outside the loop makes it run faster
    if (append)
        for (i in copy)
            print >> copy[i]
    else
        for (i in copy)
            print > copy[i]
    print
}
```

It is also possible to write the loop this way:

```
for (i in copy)
    if (append)
        print >> copy[i]
```

```
    else
        print > copy[i]
```

This is more concise, but it is also less efficient. The ‘if’ is tested for each record and for each output file. By duplicating the loop body, the ‘if’ is only tested once for each input record. If there are *N* input records and *M* output files, the first method only executes *N* ‘if’ statements, while the second executes *N*`*`*M* ‘if’ statements.

Finally, the `END` rule cleans up by closing all the output files:

```
END {
    for (i in copy)
        close(copy[i])
}
```

#### 11.2.6 Printing Nonduplicated Lines of Text

The `uniq` utility reads sorted lines of data on its standard input, and by default removes duplicate lines. In other words, it only prints unique lines—hence the name. `uniq` has a number of options. The usage is as follows:

```
uniq [-udc [-f n] [-s n]] [inputfile [outputfile]]
```

The options for `uniq` are:

**`-d`**

Print only repeated (duplicated) lines.

**`-u`**

Print only nonrepeated (unique) lines.

**`-c`**

Count lines. This option overrides -d and -u. Both repeated and nonrepeated lines are counted.

**`-f *n*`**

Skip *n* fields before comparing lines. The definition of fields is similar to `awk`’s default: nonwhitespace characters separated by runs of spaces and/or TABs.

**`-s *n*`**

Skip *n* characters before comparing lines. Any fields specified with -f are skipped first.

**`*inputfile*`**

Data is read from the input file named on the command line, instead of from the standard input.

**`*outputfile*`**

The generated output is sent to the named output file, instead of to the standard output.

Normally `uniq` behaves as if both the -d and -u options are provided.

`uniq` uses the `getopt()` library function (see Processing Command-Line Options) and the `join()` library function (see Merging an Array into a String).

The program begins with a `usage()` function and then a brief outline of the options and their meanings in comments:

```
# uniq.awk --- do uniq in awk
#
# Requires getopt() and join() library functions
```

```
function usage()
{
    print("Usage: uniq [-udc [-f fields] [-s chars]] " \
          "[ in [ out ]]") > "/dev/stderr"
    exit 1
}

# -c    count lines. overrides -d and -u
# -d    only repeated lines
# -u    only nonrepeated lines
# -f n  skip n fields
# -s n  skip n characters, skip fields first
```

The POSIX standard for `uniq` allows options to start with ‘+’ as well as with ‘-’. An initial `BEGIN` rule traverses the arguments changing any leading ‘+’ to ‘-’ so that the `getopt()` function can parse the options:

```
# As of 2020, '+' can be used as the option character in addition to '-'
# Previously allowed use of -N to skip fields and +N to skip
# characters is no longer allowed, and not supported by this version.

BEGIN {
    # Convert + to - so getopt can handle things
    for (i = 1; i < ARGC; i++) {
        first = substr(ARGV[i], 1, 1)
        if (ARGV[i] == "--" || (first != "-" && first != "+"))
            break
        else if (first == "+")
            # Replace "+" with "-"
            ARGV[i] = "-" substr(ARGV[i], 2)
    }
}
```

The next `BEGIN` rule deals with the command-line arguments and options. If no options are supplied, then the default is taken, to print both repeated and nonrepeated lines. The output file, if provided, is assigned to `outputfile`. Early on, `outputfile` is initialized to the standard output, /dev/stdout:

```
BEGIN {
    count = 1
    outputfile = "/dev/stdout"
    opts = "udcf:s:"
    while ((c = getopt(ARGC, ARGV, opts)) != -1) {
        if (c == "u")
            non_repeated_only++
        else if (c == "d")
            repeated_only++
        else if (c == "c")
            do_count++
        else if (c == "f")
            fcount = Optarg + 0
        else if (c == "s")
            charcount = Optarg + 0
        else
            usage()
    }

    for (i = 1; i < Optind; i++)
        ARGV[i] = ""

    if (repeated_only == 0 && non_repeated_only == 0)
        repeated_only = non_repeated_only = 1

    if (ARGC - Optind == 2) {
        outputfile = ARGV[ARGC - 1]
        ARGV[ARGC - 1] = ""
    }
}
```

The following function, `are_equal()`, compares the current line, `$0`, to the previous line, `last`. It handles skipping fields and characters. If no field count and no character count are specified, `are_equal()` returns one or zero depending upon the result of a simple string comparison of `last` and `$0`.

Otherwise, things get more complicated. If fields have to be skipped, each line is broken into an array using `split()` (see String-Manipulation Functions); the desired fields are then joined back into a line using `join()`. The joined lines are stored in `clast` and `cline`. If no fields are skipped, `clast` and `cline` are set to `last` and `$0`, respectively. Finally, if characters are skipped, `substr()` is used to strip off the leading `charcount` characters in `clast` and `cline`. The two strings are then compared and `are_equal()` returns the result:

```
function are_equal(    n, m, clast, cline, alast, aline)
{
    if (fcount == 0 && charcount == 0)
        return (last == $0)
```

```
    if (fcount > 0) {
        n = split(last, alast)
        m = split($0, aline)
        clast = join(alast, fcount+1, n)
        cline = join(aline, fcount+1, m)
    } else {
        clast = last
        cline = $0
    }
    if (charcount) {
        clast = substr(clast, charcount + 1)
        cline = substr(cline, charcount + 1)
    }
```

```
    return (clast == cline)
}
```

The following two rules are the body of the program. The first one is executed only for the very first line of data. It sets `last` equal to `$0`, so that subsequent lines of text have something to be compared to.

The second rule does the work. The variable `equal` is one or zero, depending upon the results of `are_equal()`’s comparison. If `uniq` is counting repeated lines, and the lines are equal, then it increments the `count` variable. Otherwise, it prints the line and resets `count`, because the two lines are not equal.

If `uniq` is not counting, and if the lines are equal, `count` is incremented. Nothing is printed, as the point is to remove duplicates. Otherwise, if `uniq` is counting repeated lines and more than one line is seen, or if `uniq` is counting nonrepeated lines and only one line is seen, then the line is printed, and `count` is reset.

Finally, similar logic is used in the `END` rule to print the final line of input data:

```
NR == 1 {
    last = $0
    next
}

{
    equal = are_equal()

    if (do_count) {    # overrides -d and -u
        if (equal)
            count++
        else {
            printf("%4d %s\n", count, last) > outputfile
            last = $0
            count = 1    # reset
        }
        next
    }

    if (equal)
        count++
    else {
        if ((repeated_only && count > 1) ||
            (non_repeated_only && count == 1))
                print last > outputfile
        last = $0
        count = 1
    }
}

END {
    if (do_count)
        printf("%4d %s\n", count, last) > outputfile
```

```
    else if ((repeated_only && count > 1) ||
            (non_repeated_only && count == 1))
        print last > outputfile
    close(outputfile)
}
```

As a side note, this program does not follow our recommended convention of naming global variables with a leading capital letter. Doing that would make the program a little easier to follow.

#### 11.2.7 Counting Things

The `wc` (word count) utility counts lines, words, characters and bytes in one or more input files.

#### 11.2.7.1 Modern Character Sets

In the early days of computing, single bytes were used for storing characters. The most common character sets were ASCII and EBCDIC, which each provided all the English upper- and lowercase letters, the 10 Hindu-Arabic numerals from 0 through 9, and a number of other standard punctuation and control characters.

Today, the most popular character set in use is Unicode (of which ASCII is a pure subset). Unicode provides tens of thousands of unique characters (called *code points*) to cover most existing human languages, living and dead. (Sadly, proposals to add some nonhuman ones, such as Klingon and J.R.R. Tolkien’s Elvish languages, were not accepted).

To save space in files, Unicode code points are *encoded*, where each character takes from one to four bytes in the file. UTF-8 is possibly the most popular of such *multibyte encodings*.

The POSIX standard requires that `awk` function in terms of characters, not bytes. Thus in `gawk`, `length()`, `substr()`, `split()`, `match()` and the other string functions (see String-Manipulation Functions) all work in terms of characters in the local character set, and not in terms of bytes. (Not all `awk` implementations do so, though).

There is no standard, built-in way to distinguish characters from bytes in an `awk` program. For an `awk` implementation of `wc`, which needs to make such a distinction, we will have to use an external extension.

#### 11.2.7.2 A Brief Introduction To Extensions

Loadable extensions are presented in full detail in Writing Extensions for `gawk`. They provide a way to add functions to `gawk` which can call out to other facilities written in C or C++.

For the purposes of wc.awk, it’s enough to know that the extension is loaded with the `@load` directive, and the additional function we will use is called `mbs_length()`. This function returns the number of bytes in a string, not the number of characters.

The `"mbs"` extension comes from the `gawkextlib` project. See The `gawkextlib` Project for more information.

#### 11.2.7.3 Code for wc.awk

The usage for `wc` is as follows:

```
wc [-lwcm] [files ...]
```

If no files are specified on the command line, `wc` reads its standard input. If there are multiple files, it also prints total counts for all the files. The options and their meanings are as follows:

**`-c`**

Count only bytes. Once upon a time, the ‘c’ in this option stood for “characters.” But, as explained earlier, bytes and character are no longer synonymous with each other.
