---
title: "The GNU Awk User’s Guide (part 6/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 6/38
---

# The GNU Awk User’s Guide

Starting in version 4.2, each field width may optionally be preceded by a colon-separated value specifying the number of characters to skip before the field starts. Thus, the preceding program could be rewritten to specify `FIELDWIDTHS` like so:

```
BEGIN  { FIELDWIDTHS = "8 1:5 4:7 6 1:6 1:6 2:33" }
```

This strips away some of the white space separating the fields. With such a change, the program produces the following results:

```
hzang    ttyV3 50
eklye    ttyV5 0
dportein ttyV6 107
gierd    ttyD3 1
dave     ttyD4 0
brent    ttyp0 286
dave     ttyq4 1296000
```

#### 4.6.3 Capturing Optional Trailing Data

There are times when fixed-width data may be followed by additional data that has no fixed length. Such data may or may not be present, but if it is, it should be possible to get at it from an `awk` program.

Starting with version 4.2, in order to provide a way to say “anything else in the record after the defined fields,” `gawk` allows you to add a final ‘*’ character to the value of `FIELDWIDTHS`. There can only be one such character, and it must be the final non-whitespace character in `FIELDWIDTHS`. For example:

```
$ cat fw.awk                         Show the program
-| BEGIN { FIELDWIDTHS = "2 2 *" }
-| { print NF, $1, $2, $3 }
$ cat fw.in                          Show sample input
-| 1234abcdefghi
$ gawk -f fw.awk fw.in               Run the program
-| 3 12 34 abcdefghi
```

#### 4.6.4 Field Values With Fixed-Width Data

So far, so good. But what happens if there isn’t as much data as there should be based on the contents of `FIELDWIDTHS`? Or, what happens if there is more data than expected?

For many years, what happens in these cases was not well defined. Starting with version 4.2, the rules are as follows:

**Enough data for some fields**

For example, if `FIELDWIDTHS` is set to `"2 3 4"` and the input record is ‘aabbb’. In this case, `NF` is set to two.

**Not enough data for a field**

For example, if `FIELDWIDTHS` is set to `"2 3 4"` and the input record is ‘aab’. In this case, `NF` is set to two and `$2` has the value `"b"`. The idea is that even though there aren’t as many characters as were expected, there are some, so the data should be made available to the program.

**Too much data**

For example, if `FIELDWIDTHS` is set to `"2 3 4"` and the input record is ‘aabbbccccddd’. In this case, `NF` is set to three and the extra characters (‘ddd’) are ignored. If you want `gawk` to capture the extra characters, supply a final ‘*’ in the value of `FIELDWIDTHS`.

**Too much data, but with ‘*’ supplied**

For example, if `FIELDWIDTHS` is set to `"2 3 4 *"` and the input record is ‘aabbbccccddd’. In this case, `NF` is set to four, and `$4` has the value `"ddd"`.

### 4.7 Defining Fields by Content

This section discusses an advanced feature of `gawk`. If you are a novice `awk` user, you might want to skip it on the first reading.

Normally, when using `FS`, `gawk` defines the fields as the parts of the record that occur in between each field separator. In other words, `FS` defines what a field *is not*, instead of what a field *is*. However, there are times when we really want to define the fields by what they are, and not by what they are not.

The `FPAT` variable offers a solution for cases like this. The value of `FPAT` should be a string that provides a regular expression. This regular expression describes the contents of each field.

We can explore the strengths, and some limitations, of `FPAT` using the case of comma-separated values (CSV) data. This case is somewhat obsolete as `gawk` now has built-in CSV parsing (see Working With Comma Separated Value Files). Nonetheless, it remains useful as an example of what `FPAT`-based field parsing can do. It is also useful for versions of `gawk` prior to version 5.3.

Many spreadsheet programs, for example, can export their data into text files, where each record is terminated with a newline, and fields are separated by commas. If commas only separated the data, there wouldn’t be an issue with using ‘FS = ","’ to split the data into fields. The problem comes when one of the fields contains an *embedded* comma. In such cases, most programs embed the field in double quotes.27 So, we might have data like this:

```
Robbins,Arnold,,"1234 A Pretty Street, NE",MyTown,MyState,12345-6789,USA
```

In the case of CSV data as presented here, each field is either “anything that is not a comma,” or “a double quote, anything that is not a double quote, and a closing double quote.” We also need to bear in mind that some fields may be empty. If written as a regular expression constant (see Regular Expressions), we would have `/([^,]*)|("[^"]+")/`. Writing this as a string requires us to escape the double quotes, leading to:

```
FPAT = "([^,]*)|(\"[^\"]+\")"
```

Putting this to use, here is a simple program to parse the data:

```
BEGIN {
    FPAT = "([^,]*)|(\"[^\"]+\")"
}
```

```
{
    print "NF =", NF
    for (i = 1; i <= NF; i++) {
        printf("$%d = <%s>\n", i, $i)
    }
}
```

When run, we get the following:

```
$ gawk -f simple-csv.awk addresses.csv
-| NF = 8
-| $1 = <Robbins>
-| $2 = <Arnold>
-| $3 = <>
-| $4 = <"1234 A Pretty Street, NE">
-| $5 = <MyTown>
-| $6 = <MyState>
-| $7 = <12345-6789>
-| $8 = <USA>
```

Note the empty data field in the value of `$3` and the embedded comma in the value of `$4`, in which the data remains wrapped in its enclosing double quotes.

The use of enclosing double quotes has a consequence for fields that contain double quotes as part of the data itself. For those fields, a double quote appearing inside a field must be escaped by preceding it with another double quote, as shown in the third and fourth lines of the following example:

```
1,2,3
p,"q,r",s
p,"q""r",s
p,"q,""r",s
p,"",s
p,,s
```

Manuel Collado suggests that the simplest `FPAT` expression that recognizes this kind of CSV field is `/([^,]*)|("([^"]|"")+")/`.

The following program uses this improved `FPAT` expression to split the example CSV fields above, extracts the underlying data from any double-quoted fields, and finally prints the data as tab-separated values. The latter is accomplished by setting `OFS` to a TAB character.

```
BEGIN {
    FPAT = "([^,]*)|(\"([^\"]|\"\")+\")"
    OFS = "\t"    # Print tab-separated values
}
```

```
{
    for (i = 1; i <= NF; i++) {
        # Extract data from double-quoted fields
        if (substr($i, 1, 1) == "\"") {
            gsub(/^"|"$/, "", $i)    # Remove enclosing quotes
            gsub(/""/, "\"", $i)    # Convert "" to "
        }
    }
    $1 = $1    # force rebuild of the record
    print
}
```

When run, it produces:

```
$ gawk -f quoted-csv.awk sample.csv
-| 1       2       3
-| p       q,r     s
-| p       q"r     s
-| p       q,"r    s
-| p               s
-| p               s
```

Some programs export CSV data that contain *embedded newlines* between the double quotes, and here we run into a limitation of `FPAT`: it provides no way to deal with this. Hence, using `FPAT` to do your own CSV parsing is an elegant approach for the majority of cases, but not all.

For a more general solution to working with CSV data, see Working With Comma Separated Value Files. If your version of `gawk` is prior to version 5.3, we recommend that you use Manuel Collado’s `CSVMODE` library for `gawk`.

As with `FS`, the `IGNORECASE` variable (see Built-in Variables That Control `awk`) affects field splitting with `FPAT`.

Assigning a value to `FPAT` overrides field splitting with `FS` and with `FIELDWIDTHS`.

Finally, the `patsplit()` function makes the same functionality available for splitting regular strings (see String-Manipulation Functions).

#### 4.7.1 `FS` Versus `FPAT`: A Subtle Difference

As we discussed earlier, `FS` describes the data between fields (“what fields are not”) and `FPAT` describes the fields themselves (“what fields are”). This leads to a subtle difference in how fields are found when using regexps as the value for `FS` or `FPAT`.

In order to distinguish one field from another, there must be a non-empty separator between each field. This makes intuitive sense—otherwise one could not distinguish fields from separators.

Thus, regular expression matching as done when splitting fields with `FS` is not allowed to match the null string; it must always match at least one character, in order to be able to proceed through the entire record.

On the other hand, regular expression matching with `FPAT` can match the null string, and the non-matching intervening characters function as the separators.

This same difference is reflected in how matching is done with the `split()` and `patsplit()` functions (see String-Manipulation Functions).

### 4.8 Checking How `gawk` Is Splitting Records

As we’ve seen, `gawk` provides three independent methods to split input records into fields. The mechanism used is based on which of the three variables—`FS`, `FIELDWIDTHS`, or `FPAT`—was last assigned to. In addition, an API input parser may choose to override the record parsing mechanism; please refer to Customized Input Parsers for further information about this feature.

To restore normal field splitting after using `FIELDWIDTHS` and/or `FPAT`, simply assign a value to `FS`. You can use ‘FS = FS’ to do this, without having to know the current value of `FS`.

In order to tell which kind of field splitting is in effect, use `PROCINFO["FS"]` (see Built-in Variables That Convey Information). The value is `"FS"` if regular field splitting is being used, `"FIELDWIDTHS"` if fixed-width field splitting is being used, or `"FPAT"` if content-based field splitting is being used:

```
if ("CSV" in PROCINFO)
    CSV-based field splitting ...
else if (PROCINFO["FS"] == "FS")
    regular field splitting ...
else if (PROCINFO["FS"] == "FIELDWIDTHS")
    fixed-width field splitting ...
else if (PROCINFO["FS"] == "FPAT")
    content-based field splitting ...
else
    API input parser field splitting ... (advanced feature)
```

This information is useful when writing a function that needs to temporarily change `FS`, `FIELDWIDTHS`, or `FPAT`, read some records, and then restore the original settings (see Reading the User Database for an example of such a function).

### 4.9 Multiple-Line Records

In some databases, a single line cannot conveniently hold all the information in one entry. In such cases, you can use multiline records. The first step in doing this is to choose your data format.

One technique is to use an unusual character or string to separate records. For example, you could use the formfeed character (written ‘\f’ in `awk`, as in C) to separate them, making each record a page of the file. To do this, just set the variable `RS` to `"\f"` (a string containing the formfeed character). Any other character could equally well be used, as long as it won’t be part of the data in a record.

Another technique is to have blank lines separate records. By a special dispensation, an empty string as the value of `RS` indicates that records are separated by one or more blank lines. When `RS` is set to the empty string, each record always ends at the first blank line encountered. The next record doesn’t start until the first nonblank line that follows. No matter how many blank lines appear in a row, they all act as one record separator. (Blank lines must be completely empty; lines that contain only whitespace do not count.)

You can achieve the same effect as ‘RS = ""’ by assigning the string `"\n\n+"` to `RS`. This regexp matches the newline at the end of the record and one or more blank lines after the record. In addition, a regular expression always matches the longest possible sequence when there is a choice (see How Much Text Matches?). So, the next record doesn’t start until the first nonblank line that follows—no matter how many blank lines appear in a row, they are considered one record separator.

However, there is an important difference between ‘RS = ""’ and ‘RS = "\n\n+"’. In the first case, leading newlines in the input data file are ignored, and if a file ends without extra blank lines after the last record, the final newline is removed from the record. In the second case, this special processing is not done. (d.c.)

Now that the input is separated into records, the second step is to separate the fields in the records. One way to do this is to divide each of the lines into fields in the normal manner. This happens by default as the result of a special feature. When `RS` is set to the empty string *and* `FS` is set to a single character, the newline character *always* acts as a field separator. This is in addition to whatever field separations result from `FS`.

> **NOTE:** When `FS` is the null string (`""`) or a regexp, this special feature of `RS` does not apply. It does apply to the default field separator of a single space: ‘FS = " "’.
> 
> Note that language in the POSIX specification implies that this special feature should apply when `FS` is a regexp. However, Unix `awk` has never behaved that way, nor has `gawk`. This is essentially a bug in POSIX.

The original motivation for this special exception was probably to provide useful behavior in the default case (i.e., `FS` is equal to `" "`). This feature can be a problem if you really don’t want the newline character to separate fields, because there is no way to prevent it. However, you can work around this by using the `split()` function to break up the record manually (see String-Manipulation Functions). If you have a single-character field separator, you can work around the special feature in a different way, by making `FS` into a regexp for that single character. For example, if the field separator is a percent character, instead of ‘FS = "%"’, use ‘FS = "[%]"’.

Another way to separate fields is to put each field on a separate line: to do this, just set the variable `FS` to the string `"\n"`. (This single-character separator matches a single newline.) A practical example of a data file organized this way might be a mailing list, where blank lines separate the entries. Consider a mailing list in a file named addresses, which looks like this:

```
Jane Doe
123 Main Street
Anywhere, SE 12345-6789

John Smith
456 Tree-lined Avenue
Smallville, MW 98765-4321
...
```

A simple program to process this file is as follows:

```
# addrs.awk --- simple mailing list program

# Records are separated by blank lines.
# Each line is one field.
BEGIN { RS = "" ; FS = "\n" }

{
      print "Name is:", $1
      print "Address is:", $2
      print "City and State are:", $3
      print ""
}
```

Running the program produces the following output:

```
$ awk -f addrs.awk addresses
-| Name is: Jane Doe
-| Address is: 123 Main Street
-| City and State are: Anywhere, SE 12345-6789
-|
-| Name is: John Smith
-| Address is: 456 Tree-lined Avenue
-| City and State are: Smallville, MW 98765-4321
-|
...
```

See Printing Mailing Labels for a more realistic program dealing with address lists. The following list summarizes how records are split, based on the value of `RS`:

**`RS == "\n"`**

Records are separated by the newline character (‘\n’). In effect, every line in the data file is a separate record, including blank lines. This is the default.

**`RS == *any single character*`**

Records are separated by each occurrence of the character. Multiple successive occurrences delimit empty records.

**`RS == ""`**

Records are separated by runs of blank lines. When `FS` is a single character, then the newline character always serves as a field separator, in addition to whatever value `FS` may have. Leading and trailing newlines in a file are ignored.

**`RS == *regexp*`**

Records are separated by occurrences of characters that match *regexp*. Leading and trailing matches of *regexp* delimit empty records. (This is a `gawk` extension; it is not specified by the POSIX standard.)

If not in compatibility mode (see Command-Line Options), `gawk` sets `RT` to the input text that matched the value specified by `RS`. But if the input file ended without any text that matches `RS`, then `gawk` sets `RT` to the null string.

### 4.10 Explicit Input with `getline`

So far we have been getting our input data from `awk`’s main input stream—either the standard input (usually your keyboard, sometimes the output from another program) or the files specified on the command line. The `awk` language has a special built-in function called `getline` that can be used to read input under your explicit control.

The `getline` function is used in several different ways and should *not* be used by beginners. The examples that follow the explanation of the `getline` function include material that has not been covered yet. Therefore, come back and study the `getline` function *after* you have reviewed the rest of this Web page and have a good knowledge of how `awk` works.

The `getline` function returns 1 if it finds a record and 0 if it encounters the end of the file. If there is some error in getting a record, such as a file that cannot be opened, then `getline` returns −1. In this case, `gawk` sets the variable `ERRNO` to a string describing the error that occurred.

If `ERRNO` indicates that the I/O operation may be retried, and `PROCINFO["*input*", "RETRY"]` is set, then `getline` returns −2 instead of −1, and further calls to `getline` may be attempted. See Retrying Reads After Certain Input Errors for further information about this feature.

In the following examples, *command* stands for a string value that represents a shell command.

> **NOTE:** When --sandbox is specified (see Command-Line Options), reading lines from files, pipes, and coprocesses is disabled.

#### 4.10.1 Using `getline` with No Arguments

The `getline` function can be used without arguments to read input from the current input file. All it does in this case is read the next input record and split it up into fields. This is useful if you’ve finished processing the current record, but want to do some special processing on the next record *right now*. For example:

```
# Remove text between /* and */, inclusive
{
    while ((start = index($0, "/*")) != 0) {
        out = substr($0, 1, start - 1)  # leading part of the string
        rest = substr($0, start + 2)    # ... */ ...
        while ((end = index(rest, "*/")) == 0) {  # is */ in trailing part?
            # get more text
            if (getline <= 0) {
                print("unexpected EOF or error:", ERRNO) > "/dev/stderr"
                exit
            }
            # build up the line using string concatenation
            rest = rest $0
        }
        rest = substr(rest, end + 2)  # remove comment
        # build up the output line using string concatenation
        $0 = out rest
    }
    print $0
}
```

This `awk` program deletes C-style comments (‘/* … */’) from the input. It uses a number of features we haven’t covered yet, including string concatenation (see String Concatenation) and the `index()` and `substr()` built-in functions (see String-Manipulation Functions). By replacing the ‘print $0’ with other statements, you could perform more complicated processing on the decommented input, such as searching for matches of a regular expression.

Here is some sample input:

```
mon/*comment*/key
rab/*commen
t*/bit
horse /*comment*/more text
part 1 /*comment*/part 2 /*comment*/part 3
no comment
```

When run, the output is:

```
$ awk -f strip_comments.awk example_text
-| monkey
-| rabbit
-| horse more text
-| part 1 part 2 part 3
-| no comment
```

This form of the `getline` function sets `NF`, `NR`, `FNR`, `RT`, and the value of `$0`.

> **NOTE:** The new value of `$0` is used to test the patterns of any subsequent rules. The original value of `$0` that triggered the rule that executed `getline` is lost. By contrast, the `next` statement reads a new record but immediately begins processing it normally, starting with the first rule in the program. See The `next` Statement.

#### 4.10.2 Using `getline` into a Variable

You can use ‘getline *var*’ to read the next record from `awk`’s input into the variable *var*. No other processing is done. For example, suppose the next line is a comment or a special string, and you want to read it without triggering any rules. This form of `getline` allows you to read that line and store it in a variable so that the main read-a-line-and-check-each-rule loop of `awk` never sees it. The following example swaps every two lines of input:

```
{
     if ((getline tmp) > 0) {
          print tmp
          print $0
     } else
          print $0
}
```

It takes the following list:

```
wan
tew
free
phore
```

and produces these results:

```
tew
wan
phore
free
```

The `getline` function used in this way sets only the variables `NR`, `FNR`, and `RT` (and, of course, *var*). The record is not split into fields, so the values of the fields (including `$0`) and the value of `NF` do not change.

#### 4.10.3 Using `getline` from a File

Use ‘getline < *file*’ to read the next record from *file*. Here, *file* is a string-valued expression that specifies the file name. ‘< *file*’ is called a *redirection* because it directs input to come from a different place. For example, the following program reads its input record from the file secondary.input when it encounters a first field with a value equal to 10 in the current input file:

```
{
    if ($1 == 10) {
         getline < "secondary.input"
         print
    } else
         print
}
```

Because the main input stream is not used, the values of `NR` and `FNR` are not changed. However, the record it reads is split into fields in the normal manner, so the values of `$0` and the other fields are changed, resulting in a new value of `NF`. `RT` is also set.

According to POSIX, ‘getline < *expression*’ is ambiguous if *expression* contains unparenthesized operators other than ‘$’; for example, ‘getline < dir "/" file’ is ambiguous because the concatenation operator (not discussed yet; see String Concatenation) is not parenthesized. You should write it as ‘getline < (dir "/" file)’ if you want your program to be portable to all `awk` implementations.

#### 4.10.4 Using `getline` into a Variable from a File

Use ‘getline *var* < *file*’ to read input from the file *file*, and put it in the variable *var*. As earlier, *file* is a string-valued expression that specifies the file from which to read.

In this version of `getline`, none of the predefined variables are changed and the record is not split into fields. The only variable changed is *var*.28 For example, the following program copies all the input files to the output, except for records that say ‘@include *filename*’. Such a record is replaced by the contents of the file *filename*:

```
{
     if (NF == 2 && $1 == "@include") {
          while ((getline line < $2) > 0)
               print line
          close($2)
     } else
          print
}
```

Note here how the name of the extra input file is not built into the program; it is taken directly from the data, specifically from the second field on the `@include` line.

The `close()` function is called to ensure that if two identical `@include` lines appear in the input, the entire specified file is included twice. See Closing Input and Output Redirections.

One deficiency of this program is that it does not process nested `@include` directives (i.e., `@include` directives in included files) the way a true macro preprocessor would. See An Easy Way to Use Library Functions for a program that does handle nested `@include` directives.

#### 4.10.5 Using `getline` from a Pipe

> *Omniscience has much to recommend it. Failing that, attention to details would be useful.*

—

Brian Kernighan

The output of a command can also be piped into `getline`, using ‘*command* | getline’. In this case, the string *command* is run as a shell command and its output is piped into `awk` to be used as input. This form of `getline` reads one record at a time from the pipe. For example, the following program copies its input to its output, except for lines that begin with ‘@execute’, which are replaced by the output produced by running the rest of the line as a shell command:

```
{
     if ($1 == "@execute") {
          tmp = substr($0, 10)        # Remove "@execute"
          while ((tmp | getline) > 0)
               print
          close(tmp)
     } else
          print
}
```

The `close()` function is called to ensure that if two identical ‘@execute’ lines appear in the input, the command is run for each one. See Closing Input and Output Redirections. Given the input:

```
foo
bar
baz
@execute who
bletch
```

the program might produce:

```
foo
bar
baz
arnold     ttyv0   Jul 13 14:22
miriam     ttyp0   Jul 13 14:23     (murphy:0)
bill       ttyp1   Jul 13 14:23     (murphy:0)
bletch
```

Notice that this program ran the command `who` and printed the result. (If you try this program yourself, you will of course get different results, depending upon who is logged in on your system.)

This variation of `getline` splits the record into fields, sets the value of `NF`, and recomputes the value of `$0`. The values of `NR` and `FNR` are not changed. `RT` is set.

According to POSIX, ‘*expression* | getline’ is ambiguous if *expression* contains unparenthesized operators other than ‘$’—for example, ‘"echo " "date" | getline’ is ambiguous because the concatenation operator is not parenthesized. You should write it as ‘("echo " "date") | getline’ if you want your program to be portable to all `awk` implementations.

> **NOTE:** Unfortunately, `gawk` has not been consistent in its treatment of a construct like ‘"echo " "date" | getline’. Most versions, including the current version, treat it as ‘("echo " "date") | getline’. (This is also how BWK `awk` behaves.) Some versions instead treat it as ‘"echo " ("date" | getline)’. (This is how `mawk` behaves.) In short, *always* use explicit parentheses, and then you won’t have to worry.

#### 4.10.6 Using `getline` into a Variable from a Pipe

When you use ‘*command* | getline *var*’, the output of *command* is sent through a pipe to `getline` and into the variable *var*. For example, the following program reads the current date and time into the variable `current_time`, using the `date` utility, and then prints it:

```
BEGIN {
     "date" | getline current_time
     close("date")
     print "Report printed on " current_time
}
```

In this version of `getline`, none of the predefined variables are changed and the record is not split into fields. However, `RT` is set.

#### 4.10.7 Using `getline` from a Coprocess

Reading input into `getline` from a pipe is a one-way operation. The command that is started with ‘*command* | getline’ only sends data *to* your `awk` program.

On occasion, you might want to send data to another program for processing and then read the results back. `gawk` allows you to start a *coprocess*, with which two-way communications are possible. This is done with the ‘|&’ operator. Typically, you write data to the coprocess first and then read the results back, as shown in the following:

```
print "some query" |& "db_server"
"db_server" |& getline
```

which sends a query to `db_server` and then reads the results.

The values of `NR` and `FNR` are not changed, because the main input stream is not used. However, the record is split into fields in the normal manner, thus changing the values of `$0`, of the other fields, and of `NF` and `RT`.

Coprocesses are an advanced feature. They are discussed here only because this is the section on `getline`. See Two-Way Communications with Another Process, where coprocesses are discussed in more detail.

#### 4.10.8 Using `getline` into a Variable from a Coprocess

When you use ‘*command* |& getline *var*’, the output from the coprocess *command* is sent through a two-way pipe to `getline` and into the variable *var*.

In this version of `getline`, none of the predefined variables are changed and the record is not split into fields. The only variable changed is *var*. However, `RT` is set.

#### 4.10.9 Points to Remember About `getline`

Here are some miscellaneous points about `getline` that you should bear in mind:

- When `getline` changes the value of `$0` and `NF`, `awk` does *not* automatically jump to the start of the program and start testing the new record against every pattern. However, the new record is tested against any subsequent rules.
- Some very old `awk` implementations limit the number of pipelines that an `awk` program may have open to just one. In `gawk`, there is no such limit. You can open as many pipelines (and coprocesses) as the underlying operating system permits.
- An interesting side effect occurs if you use `getline` without a redirection inside a `BEGIN` rule. Because an unredirected `getline` reads from the command-line data files, the first `getline` function causes `awk` to set the value of `FILENAME`. Normally, `FILENAME` does not have a value inside `BEGIN` rules, because you have not yet started to process the command-line data files. (d.c.) (See The `BEGIN` and `END` Special Patterns; also see Built-in Variables That Convey Information.)
- Using `FILENAME` with `getline` (‘getline < FILENAME’) is likely to be a source of confusion. `awk` opens a separate input stream from the current input file. However, by not using a variable, `$0` and `NF` are still updated. If you’re doing this, it’s probably by accident, and you should reconsider what it is you’re trying to accomplish.
- Summary of `getline` Variants, presents a table summarizing the `getline` variants and which variables they can affect. It is worth noting that those variants that do not use redirection can cause `FILENAME` to be updated if they cause `awk` to start reading a new input file.
- `getline` is not a statement (unlike `print`), it’s an expression. It has a result value, and can be used as part as a larger expression, in control statements, and so on. Here are examples of the “read until EOF/error” idiom: while ("sort FILE" | getline line > 0) print line while (getline line < "file.txt" > 0) print line If you need to test the error code for being less than zero, you need to enclose `getline` in parentheses, to avoid it being interpreted as input redirection: if ((getline VAR) < 0) print "Read error"; It is, in fact, best to parenthesize calls to `getline` in all control expressions, as some versions of `awk` require this. Thus, the previous examples are best written this way: while (("sort FILE" | getline line) > 0) print line while ((getline line < "file.txt") > 0) print line
- If the variable being assigned is an expression with side effects, different versions of `awk` behave differently upon encountering end-of-file. Some versions don’t evaluate the expression; many versions (including `gawk`) do. Here is an example, courtesy of Duncan Moore: BEGIN { system("echo 1 > f") while ((getline a[++c] < "f") > 0) { } print c } Here, the side effect is the ‘++c’. Is `c` incremented if end-of-file is encountered before the element in `a` is assigned? Despite the lack of parentheses when calling `getline`, `gawk` evaluates the expression ‘a[++c]’ before attempting to read from f. However, some versions of `awk` only evaluate the expression once they know that there is a string value to be assigned.

#### 4.10.10 Summary of `getline` Variants

Table 4.2 summarizes the eight variants of `getline`, listing which predefined variables are set by each one, and whether the variant is standard or a `gawk` extension. Note: for each variant, `gawk` sets the `RT` predefined variable.

| Variant | Effect | `awk` / `gawk` |
|---|---|---|
| `getline` | Sets `$0`, `NF`, `FNR`, `NR`, and `RT` | `awk` |
| `getline` *var* | Sets *var*, `FNR`, `NR`, and `RT` | `awk` |
| `getline <` *file* | Sets `$0`, `NF`, and `RT` | `awk` |
| `getline *var* < *file*` | Sets *var* and `RT` | `awk` |
| *command* `\| getline` | Sets `$0`, `NF`, and `RT` | `awk` |
| *command* `\| getline` *var* | Sets *var* and `RT` | `awk` |
| *command* `\|& getline` | Sets `$0`, `NF`, and `RT` | `gawk` |
| *command* `\|& getline` *var* | Sets *var* and `RT` | `gawk` |

**Table 4.2:**`getline` variants and what they set

### 4.11 Reading Input with a Timeout

This section describes a feature that is specific to `gawk`.

You may specify a timeout in milliseconds for reading input from the keyboard, a pipe, or two-way communication, including TCP/IP sockets. This can be done on a per-input, per-command, or per-connection basis, by setting a special element in the `PROCINFO` array (see Built-in Variables That Convey Information):

```
PROCINFO["input_name", "READ_TIMEOUT"] = timeout in milliseconds
```

When set, this causes `gawk` to time out and return failure if no data is available to read within the specified timeout period. For example, a TCP client can decide to give up on receiving any response from the server after a certain amount of time:

```
Service = "/inet/tcp/0/localhost/daytime"
PROCINFO[Service, "READ_TIMEOUT"] = 100
if ((Service |& getline) > 0)
    print $0
else if (ERRNO != "")
    print ERRNO
```

Here is how to read interactively from the user29 without waiting for more than five seconds:

```
PROCINFO["/dev/stdin", "READ_TIMEOUT"] = 5000
while ((getline < "/dev/stdin") > 0)
    print $0
```

`gawk` terminates the read operation if input does not arrive after waiting for the timeout period, returns failure, and sets `ERRNO` to an appropriate string value. A negative or zero value for the timeout is the same as specifying no timeout at all.

A timeout can also be set for reading from the keyboard in the implicit loop that reads input records and matches them against patterns, like so:

```
$ gawk 'BEGIN { PROCINFO["-", "READ_TIMEOUT"] = 5000 }
> { print "You entered: " $0 }'
gawk
-| You entered: gawk
```

In this case, failure to respond within five seconds results in the following error message:

```
error→ gawk: cmd. line:2: (FILENAME=- FNR=1) fatal: error reading input file `-': Connection timed out
```

The timeout can be set or changed at any time, and will take effect on the next attempt to read from the input device. In the following example, we start with a timeout value of one second, and progressively reduce it by one-tenth of a second until we wait indefinitely for the input to arrive:

```
PROCINFO[Service, "READ_TIMEOUT"] = 1000
while ((Service |& getline) > 0) {
    print $0
    PROCINFO[Service, "READ_TIMEOUT"] -= 100
}
```

> **NOTE:** You should not assume that the read operation will block exactly after the tenth record has been printed. It is possible that `gawk` will read and buffer more than one record’s worth of data the first time. Because of this, changing the value of timeout like in the preceding example is not very useful.

If the `PROCINFO` element is not present and the `GAWK_READ_TIMEOUT` environment variable exists, `gawk` uses its value to initialize the timeout value. The exclusive use of the environment variable to specify timeout has the disadvantage of not being able to control it on a per-command or per-connection basis.

`gawk` considers a timeout event to be an error even though the attempt to read from the underlying device may succeed in a later attempt. This is a limitation, and it also means that you cannot use this to multiplex input from two or more sources. See Retrying Reads After Certain Input Errors for a way to enable later I/O attempts to succeed.

Assigning a timeout value prevents read operations from being blocked indefinitely. But bear in mind that there are other ways `gawk` can stall waiting for an input device to be ready. A network client can sometimes take a long time to establish a connection before it can start reading any data, or the attempt to open a FIFO special file for reading can be blocked indefinitely until some other process opens it for writing.

### 4.12 Retrying Reads After Certain Input Errors

This section describes a feature that is specific to `gawk`.

When `gawk` encounters an error while reading input, by default `getline` returns −1, and subsequent attempts to read from that file result in an end-of-file indication. However, you may optionally instruct `gawk` to allow I/O to be retried when certain errors are encountered by setting a special element in the `PROCINFO` array (see Built-in Variables That Convey Information):

```
PROCINFO["input_name", "RETRY"] = 1
```

When this element exists, `gawk` checks the value of the system (C language) `errno` variable when an I/O error occurs. If `errno` indicates a subsequent I/O attempt may succeed, `getline` instead returns −2 and further calls to `getline` may succeed. This applies to the `errno` values `EAGAIN`, `EWOULDBLOCK`, `EINTR`, or `ETIMEDOUT`.

This feature is useful in conjunction with `PROCINFO["*input_name*", "READ_TIMEOUT"]` or situations where a file descriptor has been configured to behave in a non-blocking fashion.

### 4.13 Directories on the Command Line

According to the POSIX standard, files named on the `awk` command line must be text files; it is a fatal error if they are not. Most versions of `awk` treat a directory on the command line as a fatal error.

By default, `gawk` produces a warning for a directory on the command line, but otherwise ignores it. This makes it easier to use shell wildcards with your `awk` program:

```
$ gawk -f whizprog.awk *        Directories could kill this program
```

If either of the --posix or --traditional options is given, then `gawk` reverts to treating a directory on the command line as a fatal error.

See Reading Directories for a way to treat directories as usable data from an `awk` program.

### 4.14 Summary

- Input is split into records based on the value of `RS`. The possibilities are as follows: Value of `RS`Records are split on …`awk` / `gawk` Any single characterThat character`awk` The empty string (`""`)Runs of two or more newlines`awk` A regexpText that matches the regexp`gawk`
- `FNR` indicates how many records have been read from the current input file; `NR` indicates how many records have been read in total.
- `gawk` sets `RT` to the text matched by `RS`.
- After splitting the input into records, `awk` further splits the records into individual fields, named `$1`, `$2`, and so on. `$0` is the whole record, and `NF` indicates how many fields there are. The default way to split fields is between whitespace characters.
- Fields may be referenced using a variable, as in `$NF`. Fields may also be assigned values, which causes the value of `$0` to be recomputed when it is later referenced. Assigning to a field with a number greater than `NF` creates the field and rebuilds the record, using `OFS` to separate the fields. Incrementing `NF` does the same thing. Decrementing `NF` throws away fields and rebuilds the record.
- Field splitting is more complicated than record splitting: Field separator valueFields are split …`awk` / `gawk` `FS == " "`On runs of whitespace`awk` `FS == *any single character*`On that character`awk` `FS == *regexp*`On text matching the regexp`awk` `FS == ""`Such that each individual character is a separate field`gawk` `FIELDWIDTHS == *list of columns*`Based on character position`gawk` `FPAT == *regexp*`On the text surrounding text matching the regexp`gawk`
- Using ‘FS = "\n"’ causes the entire record to be a single field (assuming that newlines separate records).
- `FS` may be set from the command line using the -F option. This can also be done using command-line variable assignment.
- Use `PROCINFO["FS"]` to see how fields are being split.
- Use `getline` in its various forms to read additional records from the default input stream, from a file, or from a pipe or coprocess.
- Use `PROCINFO[*file*, "READ_TIMEOUT"]` to cause reads to time out for *file*.
- Directories on the command line are fatal for standard `awk`; `gawk` ignores them if not in POSIX mode.

### 4.15 Exercises

1. Using the `FIELDWIDTHS` variable (see Reading Fixed-Width Data), write a program to read election data, where each record represents one voter’s votes. Come up with a way to define which columns are associated with each ballot item, and print the total votes, including abstentions, for each item.
