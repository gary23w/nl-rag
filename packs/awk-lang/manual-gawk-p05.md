---
title: "The GNU Awk User’s Guide (part 5/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 5/38
---

## 4 Reading Input Files

In the typical `awk` program, `awk` reads all input either from the standard input (by default, this is the keyboard, but often it is a pipe from another command) or from files whose names you specify on the `awk` command line. If you specify input files, `awk` reads them in order, processing all the data from one before going on to the next. The name of the current input file can be found in the predefined variable `FILENAME` (see Predefined Variables).

The input is read in units called *records*, and is processed by the rules of your program one record at a time. By default, each record is one line. Each record is automatically split into chunks called *fields*. This makes it more convenient for programs to work on the parts of a record.

On rare occasions, you may need to use the `getline` function. The `getline` function is valuable both because it can do explicit input from any number of files, and because the files used with it do not have to be named on the `awk` command line (see Explicit Input with `getline`).

### 4.1 How Input Is Split into Records

`awk` divides the input for your program into records and fields. It keeps track of the number of records that have been read so far from the current input file. This value is stored in a predefined variable called `FNR`, which is reset to zero every time a new file is started. Another predefined variable, `NR`, records the total number of input records read so far from all data files. It starts at zero, but is never automatically reset to zero.

Normally, records are separated by newline characters. You can control how records are separated by assigning values to the built-in variable `RS`. If `RS` is any single character, that character separates records. Otherwise (in `gawk`), `RS` is treated as a regular expression. This mechanism is explained in greater detail shortly.

> **NOTE:** When `gawk` is invoked with the --csv option, nothing in this section applies. See Working With Comma Separated Value Files, for the details.

#### 4.1.1 Record Splitting with Standard `awk`

Records are separated by a character called the *record separator*. By default, the record separator is the newline character. This is why records are, by default, single lines. To use a different character for the record separator, simply assign that character to the predefined variable `RS`.

Like any other variable, the value of `RS` can be changed in the `awk` program with the assignment operator, ‘=’ (see Assignment Expressions). The new record-separator character should be enclosed in quotation marks, which indicate a string constant. Often, the right time to do this is at the beginning of execution, before any input is processed, so that the very first record is read with the proper separator. To do this, use the special `BEGIN` pattern (see The `BEGIN` and `END` Special Patterns). For example:

```
awk 'BEGIN { RS = "u" }
     { print $0 }' mail-list
```

changes the value of `RS` to ‘u’, before reading any input. The new value is a string whose first character is the letter “u”; as a result, records are separated by the letter “u”. Then the input file is read, and the second rule in the `awk` program (the action with no pattern) prints each record. Because each `print` statement adds a newline at the end of its output, this `awk` program copies the input with each ‘u’ changed to a newline. Here are the results of running the program on mail-list:

```
$ awk 'BEGIN { RS = "u" }
>      { print $0 }' mail-list
```

```
-| Amelia       555-5553     amelia.zodiac
-| sq
-| e@gmail.com    F
-| Anthony      555-3412     anthony.assert
-| ro@hotmail.com   A
-| Becky        555-7685     becky.algebrar
-| m@gmail.com      A
-| Bill         555-1675     bill.drowning@hotmail.com       A
-| Broderick    555-0542     broderick.aliq
-| otiens@yahoo.com R
-| Camilla      555-2912     camilla.inf
-| sar
-| m@skynet.be     R
-| Fabi
-| s       555-1234     fabi
-| s.
-| ndevicesim
-| s@
-| cb.ed
-|     F
-| J
-| lie        555-6699     j
-| lie.perscr
-| tabor@skeeve.com   F
-| Martin       555-6480     martin.codicib
-| s@hotmail.com    A
-| Sam
-| el       555-3430     sam
-| el.lanceolis@sh
-| .ed
-|         A
-| Jean-Pa
-| l    555-2127     jeanpa
-| l.campanor
-| m@ny
-| .ed
-|      R
-|
```

Note that the entry for the name ‘Bill’ is not split. In the original data file (see Data files for the Examples), the line looks like this:

```
Bill         555-1675     bill.drowning@hotmail.com       A
```

It contains no ‘u’, so there is no reason to split the record, unlike the others, which each have one or more occurrences of the ‘u’. In fact, this record is treated as part of the previous record; the newline separating them in the output is the original newline in the data file, not the one added by `awk` when it printed the record!

Another way to change the record separator is on the command line, using the variable-assignment feature (see Other Command-Line Arguments):

```
awk '{ print $0 }' RS="u" mail-list
```

This sets `RS` to ‘u’ before processing mail-list.

Using an alphabetic character such as ‘u’ for the record separator is highly likely to produce strange results. Using an unusual character such as ‘/’ is more likely to produce correct behavior in the majority of cases, but there are no guarantees. The moral is: Know Your Data.

`gawk` allows `RS` to be a full regular expression (discussed shortly; see Record Splitting with `gawk`). Even so, using a regular expression metacharacter, such as ‘.’ as the single character in the value of `RS` has no special effect: it is treated literally. This is required for backwards compatibility with both Unix `awk` and with POSIX.

Reaching the end of an input file terminates the current input record, even if the last character in the file is not the character in `RS`. (d.c.)

The empty string `""` (a string without any characters) has a special meaning as the value of `RS`. It means that records are separated by one or more blank lines and nothing else. See Multiple-Line Records for more details.

If you change the value of `RS` in the middle of an `awk` run, the new value is used to delimit subsequent records, but the record currently being processed, as well as records already processed, are not affected.

After the end of the record has been determined, `gawk` sets the variable `RT` to the text in the input that matched `RS`.

#### 4.1.2 Record Splitting with `gawk`

When using `gawk`, the value of `RS` is not limited to a one-character string. If it contains more than one character, it is treated as a regular expression (see Regular Expressions). (c.e.) In general, each record ends at the next string that matches the regular expression; the next record starts at the end of the matching string. This general rule is actually at work in the usual case, where `RS` contains just a newline: a record ends at the beginning of the next matching string (the next newline in the input), and the following record starts just after the end of this string (at the first character of the following line). The newline, because it matches `RS`, is not part of either record.

When `RS` is a single character, `RT` contains the same single character. However, when `RS` is a regular expression, `RT` contains the actual input text that matched the regular expression.

If the input file ends without any text matching `RS`, `gawk` sets `RT` to the null string.

The following example illustrates both of these features. It sets `RS` equal to a regular expression that matches either a newline or a series of one or more uppercase letters with optional leading and/or trailing whitespace:

```
$ echo record 1 AAAA record 2 BBBB record 3 |
> gawk 'BEGIN { RS = "\n|( *[[:upper:]]+ *)" }
>             { print "Record =", $0,"and RT = [" RT "]" }'
```

```
-| Record = record 1 and RT = [ AAAA ]
-| Record = record 2 and RT = [ BBBB ]
-| Record = record 3 and RT = [
-| ]
```

The square brackets delineate the contents of `RT`, letting you see the leading and trailing whitespace. The final value of `RT` is a newline. See A Simple Stream Editor for a more useful example of `RS` as a regexp and `RT`.

If you set `RS` to a regular expression that allows optional trailing text, such as ‘RS = "abc(XYZ)?"’, it is possible, due to implementation constraints, that `gawk` may match the leading part of the regular expression, but not the trailing part, particularly if the input text that could match the trailing part is fairly long. `gawk` attempts to avoid this problem, but currently, there’s no guarantee that this will never happen.

| Caveats When Using Regular Expressions for `RS` |
|---|
| Remember that in `awk`, the ‘^’ and ‘$’ anchor metacharacters match the beginning and end of a *string*, and not the beginning and end of a *line*. As a result, something like ‘RS = "^[[:upper:]]"’ can only match at the beginning of a file. This is because `gawk` views the input file as one long string that happens to contain newline characters. It is thus best to avoid anchor metacharacters in the value of `RS`. Record splitting with regular expressions works differently than regexp matching with the `sub()`, `gsub()`, and `gensub()` (see String-Manipulation Functions). Those functions allow a regexp to match the empty string; record splitting does not. Thus, for example ‘RS = "()"’ does *not* split records between characters. |

The use of `RS` as a regular expression and the `RT` variable are `gawk` extensions; they are not available in compatibility mode (see Command-Line Options). In compatibility mode, only the first character of the value of `RS` determines the end of the record.

`mawk` has allowed `RS` to be a regexp for decades. As of October, 2019, BWK `awk` also supports it. Neither version supplies `RT`, however.

| `RS = "\0"` Is Not Portable |
|---|
| There are times when you might want to treat an entire data file as a single record. The only way to make this happen is to give `RS` a value that you know doesn’t occur in the input file. This is hard to do in a general way, such that a program always works for arbitrary input files. You might think that for text files, the NUL character, which consists of a character with all bits equal to zero, is a good value to use for `RS` in this case: BEGIN { RS = "\0" } # whole file becomes one record? `gawk` in fact accepts this, and uses the NUL character for the record separator. This works for certain special files, such as /proc/environ on GNU/Linux systems, where the NUL character is in fact the record separator. However, this usage is *not* portable to most other `awk` implementations. Almost all other `awk` implementations22 store strings internally as C-style strings. C strings use the NUL character as the string terminator. In effect, this means that ‘RS = "\0"’ is the same as ‘RS = ""’. (d.c.) It happens that recent versions of `mawk` can use the NUL character as a record separator. However, this is a special case: `mawk` does not allow embedded NUL characters in strings. (This may change in a future version of `mawk`.) See Reading a Whole File at Once for an interesting way to read whole files. If you are using `gawk`, see Reading an Entire File for another option. |

### 4.2 Examining Fields

When `awk` reads an input record, the record is automatically *parsed* or separated by the `awk` utility into chunks called *fields*. By default, fields are separated by *whitespace*, like words in a line. Whitespace in `awk` means any string of one or more spaces, TABs, or newlines; other characters that are considered whitespace by other languages (such as formfeed, vertical tab, etc.) are *not* considered whitespace by `awk`.

The purpose of fields is to make it more convenient for you to refer to these pieces of the record. You don’t have to use them—you can operate on the whole record if you want—but fields are what make simple `awk` programs so powerful.

You use a dollar sign (‘$’) to refer to a field in an `awk` program, followed by the number of the field you want. Thus, `$1` refers to the first field, `$2` to the second, and so on. (Unlike in the Unix shells, the field numbers are not limited to single digits. `$127` is the 127th field in the record.) For example, suppose the following is a line of input:

```
This seems like a pretty nice example.
```

Here the first field, or `$1`, is ‘This’, the second field, or `$2`, is ‘seems’, and so on. Note that the last field, `$7`, is ‘example.’. Because there is no space between the ‘e’ and the ‘.’, the period is considered part of the seventh field.

`NF` is a predefined variable whose value is the number of fields in the current record. `awk` automatically updates the value of `NF` each time it reads a record. No matter how many fields there are, the last field in a record can be represented by `$NF`. So, `$NF` is the same as `$7`, which is ‘example.’. If you try to reference a field beyond the last one (such as `$8` when the record has only seven fields), you get the empty string. If used in a numeric operation, you get zero.23

The use of `$0`, which looks like a reference to the “zeroth” field, is a special case: it represents the whole input record. Use it when you are not interested in specific fields. Here are some more examples:

```
$ awk '$1 ~ /li/ { print $0 }' mail-list
-| Amelia       555-5553     amelia.zodiacusque@gmail.com    F
-| Julie        555-6699     julie.perscrutabor@skeeve.com   F
```

This example prints each record in the file mail-list whose first field contains the string ‘li’.

By contrast, the following example looks for ‘li’ in *the entire record* and prints the first and last fields for each matching input record:

```
$ awk '/li/ { print $1, $NF }' mail-list
-| Amelia F
-| Broderick R
-| Julie F
-| Samuel A
```

### 4.3 Nonconstant Field Numbers

A field number need not be a constant. Any expression in the `awk` language can be used after a ‘$’ to refer to a field. The value of the expression specifies the field number. If the value is a string, rather than a number, it is converted to a number. Consider this example:

```
awk '{ print $NR }'
```

Recall that `NR` is the number of records read so far: one in the first record, two in the second, and so on. So this example prints the first field of the first record, the second field of the second record, and so on. For the twentieth record, field number 20 is printed; most likely, the record has fewer than 20 fields, so this prints a blank line. Here is another example of using expressions as field numbers:

```
awk '{ print $(2*2) }' mail-list
```

`awk` evaluates the expression ‘(2*2)’ and uses its value as the number of the field to print. The ‘*’ represents multiplication, so the expression ‘2*2’ evaluates to four. The parentheses are used so that the multiplication is done before the ‘$’ operation; they are necessary whenever there is a binary operator24 in the field-number expression. This example, then, prints the type of relationship (the fourth field) for every line of the file mail-list. (All of the `awk` operators are listed, in order of decreasing precedence, in Operator Precedence (How Operators Nest).)

If the field number you compute is zero, you get the entire record. Thus, ‘$(2-2)’ has the same value as `$0`. Similarly, string expressions that evaluate to zero also yield the entire record. For example, ‘$"answer"’, ‘$"0foo"’, or even ‘$("foo" "bar")’.

Negative field numbers are not allowed; trying to reference one usually terminates the program. (The POSIX standard does not define what happens when you reference a negative field number. `gawk` notices this and terminates your program. Other `awk` implementations may behave differently.)

As mentioned in Examining Fields, `awk` stores the current record’s number of fields in the built-in variable `NF` (also see Predefined Variables). Thus, the expression `$NF` is not a special feature—it is the direct consequence of evaluating `NF` and using its value as a field number.

The contents of a field, as seen by `awk`, can be changed within an `awk` program; this changes what `awk` perceives as the current input record. (The actual input is untouched; `awk` *never* modifies the input file.) Consider the following example and its output:

```
$ awk '{ nboxes = $3 ; $3 = $3 - 10
>        print nboxes, $3 }' inventory-shipped
-| 25 15
-| 32 22
-| 24 14
...
```

The program first saves the original value of field three in the variable `nboxes`. The ‘-’ sign represents subtraction, so this program reassigns field three, `$3`, as the original value of field three minus ten: ‘$3 - 10’. (See Arithmetic Operators.) Then it prints the original and new values for field three. (Someone in the warehouse made a consistent mistake while inventorying the red boxes.)

For this to work, the text in `$3` must make sense as a number; the string of characters must be converted to a number for the computer to do arithmetic on it. The number resulting from the subtraction is converted back to a string of characters that then becomes field three. See Conversion of Strings and Numbers.

When the value of a field is changed (as perceived by `awk`), the text of the input record is recalculated to contain the new field where the old one was. In other words, `$0` changes to reflect the altered field. Thus, this program prints a copy of the input file, with 10 subtracted from the second field of each line:

```
$ awk '{ $2 = $2 - 10; print $0 }' inventory-shipped
-| Jan 3 25 15 115
-| Feb 5 32 24 226
-| Mar 5 24 34 228
...
```

It is also possible to assign contents to fields that are out of range. For example:

```
$ awk '{ $6 = ($5 + $4 + $3 + $2)
>        print $6 }' inventory-shipped
-| 168
-| 297
-| 301
...
```

We’ve just created `$6`, whose value is the sum of fields `$2`, `$3`, `$4`, and `$5`. The ‘+’ sign represents addition. For the file inventory-shipped, `$6` represents the total number of parcels shipped for a particular month.

Creating a new field changes `awk`’s internal copy of the current input record, which is the value of `$0`. Thus, if you do ‘print $0’ after adding a field, the record printed includes the new field, with the appropriate number of field separators between it and the previously existing fields.

This recomputation affects and is affected by `NF` (the number of fields; see Examining Fields). For example, the value of `NF` is set to the number of the highest field you create. The exact format of `$0` is also affected by a feature that has not been discussed yet: the *output field separator*, `OFS`, used to separate the fields (see Output Separators).

Note, however, that merely *referencing* an out-of-range field does *not* change the value of either `$0` or `NF`. Referencing an out-of-range field only produces an empty string. For example:

```
if ($(NF+1) != "")
    print "can't happen"
else
    print "everything is normal"
```

should print ‘everything is normal’, because `NF+1` is certain to be out of range. (See The `if`-`else` Statement for more information about `awk`’s `if-else` statements. See Variable Typing and Comparison Expressions for more information about the ‘!=’ operator.)

It is important to note that making an assignment to an existing field changes the value of `$0` but does not change the value of `NF`, even when you assign the empty string to a field. For example:

```
$ echo a b c d | awk '{ OFS = ":"; $2 = ""
>                       print $0; print NF }'
-| a::c:d
-| 4
```

The field is still there; it just has an empty value, delimited by the two colons between ‘a’ and ‘c’. This example shows what happens if you create a new field:

```
$ echo a b c d | awk '{ OFS = ":"; $2 = ""; $6 = "new"
>                       print $0; print NF }'
-| a::c:d::new
-| 6
```

The intervening field, `$5`, is created with an empty value (indicated by the second pair of adjacent colons), and `NF` is updated with the value six.

Decrementing `NF` throws away the values of the fields after the new value of `NF` and recomputes `$0`. (d.c.) Here is an example:

```
$ echo a b c d e f | awk '{ print "NF =", NF;
>                           NF = 3; print $0 }'
-| NF = 6
-| a b c
```

> **CAUTION:** Some versions of `awk` don’t rebuild `$0` when `NF` is decremented. Until August, 2018, this included BWK `awk`; fortunately his version now handles this correctly.

Finally, there are times when it is convenient to force `awk` to rebuild the entire record, using the current values of the fields and `OFS`. To do this, use the seemingly innocuous assignment:

```
$1 = $1   # force record to be reconstituted
print $0  # or whatever else with $0
```

This forces `awk` to rebuild the record. It does help to add a comment, as we’ve shown here.

There is a flip side to the relationship between `$0` and the fields. Any assignment to `$0` causes the record to be reparsed into fields using the *current* value of `FS`. This also applies to any built-in function that updates `$0`, such as `sub()` and `gsub()` (see String-Manipulation Functions).

| Understanding `$0` |
|---|
| It is important to remember that `$0` is the *full* record, exactly as it was read from the input. This includes any leading or trailing whitespace, and the exact whitespace (or other characters) that separates the fields. It is a common error to try to change the field separators in a record simply by setting `FS` and `OFS`, and then expecting a plain ‘print’ or ‘print $0’ to print the modified record. But this does not work, because nothing was done to change the record itself. Instead, you must force the record to be rebuilt, typically with a statement such as ‘$1 = $1’, as described earlier. |

### 4.5 Specifying How Fields Are Separated

The *field separator*, which is either a single character or a regular expression, controls the way `awk` splits an input record into fields. `awk` scans the input record for character sequences that match the separator; the fields themselves are the text between the matches.

In the examples that follow, we use the bullet symbol (•) to represent spaces in the output. If the field separator is ‘oo’, then the following line:

```
moo goo gai pan
```

is split into three fields: ‘m’, ‘•g’, and ‘•gai•pan’. Note the leading spaces in the values of the second and third fields.

The field separator is represented by the predefined variable `FS`. Shell programmers take note: `awk` does *not* use the name `IFS` that is used by the POSIX-compliant shells (such as the Unix Bourne shell, `sh`, or Bash).

The value of `FS` can be changed in the `awk` program with the assignment operator, ‘=’ (see Assignment Expressions). Often, the right time to do this is at the beginning of execution before any input has been processed, so that the very first record is read with the proper separator. To do this, use the special `BEGIN` pattern (see The `BEGIN` and `END` Special Patterns). For example, here we set the value of `FS` to the string `":"`:

```
awk 'BEGIN { FS = ":" } ; { print $2 }'
```

Given the input line:

```
John Q. Smith: 29 Oak St.: Walamazoo: MI 42139
```

this `awk` program extracts and prints the string ‘•29•Oak•St.’.

Sometimes the input data contains separator characters that don’t separate fields the way you thought they would. For instance, the person’s name in the example we just used might have a title or suffix attached, such as:

```
John Q. Smith: LXIX: 29 Oak St.: Walamazoo: MI 42139
```

The same program would extract ‘•LXIX’ instead of ‘•29•Oak•St.’. If you were expecting the program to print the address, you would be surprised. The moral is to choose your data layout and separator characters carefully to prevent such problems. (If the data is not in a form that is easy to process, perhaps you can massage it first with a separate `awk` program.)

#### 4.5.1 Whitespace Normally Separates Fields

Fields are normally separated by whitespace sequences (spaces, TABs, and newlines), not by single spaces. Two spaces in a row do not delimit an empty field. The default value of the field separator `FS` is a string containing a single space, `" "`. If `awk` interpreted this value in the usual way, each space character would separate fields, so two spaces in a row would make an empty field between them. The reason this does not happen is that a single space as the value of `FS` is a special case—it is taken to specify the default manner of delimiting fields.

If `FS` is any other single character, such as `","`, then each occurrence of that character separates two fields. Two consecutive occurrences delimit an empty field. If the character occurs at the beginning or the end of the line, that too delimits an empty field. The space character is the only single character that does not follow these rules.

#### 4.5.2 Using Regular Expressions to Separate Fields

The previous subsection discussed the use of single characters or simple strings as the value of `FS`. More generally, the value of `FS` may be a string containing any regular expression. In this case, each match in the record for the regular expression separates fields. For example, the assignment:

```
FS = ", \t"
```

makes every area of an input line that consists of a comma followed by a space and a TAB into a field separator.

For a less trivial example of a regular expression, try using single spaces to separate fields the way single commas are used. `FS` can be set to `"[ ]"` (left bracket, space, right bracket). This regular expression matches a single space and nothing else (see Regular Expressions).

There is an important difference between the two cases of ‘FS = " "’ (a single space) and ‘FS = "[ \t\n]+"’ (a regular expression matching one or more spaces, TABs, or newlines). For both values of `FS`, fields are separated by *runs* (multiple adjacent occurrences) of spaces, TABs, and/or newlines. However, when the value of `FS` is `" "`, `awk` first strips leading and trailing whitespace from the record and then decides where the fields are. For example, the following pipeline prints ‘b’:

```
$ echo ' a b c d ' | awk '{ print $2 }'
-| b
```

However, this pipeline prints ‘a’ (note the extra spaces around each letter):

```
$ echo ' a  b  c  d ' | awk 'BEGIN { FS = "[ \t\n]+" }
>                                  { print $2 }'
-| a
```

In this case, the first field is null, or empty.

The stripping of leading and trailing whitespace also comes into play whenever `$0` is recomputed. For instance, study this pipeline:

```
$ echo '   a b c d' | awk '{ print; $2 = $2; print }'
-|    a b c d
-| a b c d
```

The first `print` statement prints the record as it was read, with leading whitespace intact. The assignment to `$2` rebuilds `$0` by concatenating `$1` through `$NF` together, separated by the value of `OFS` (which is a space by default). Because the leading whitespace was ignored when finding `$1`, it is not part of the new `$0`. Finally, the last `print` statement prints the new `$0`.

There is an additional subtlety to be aware of when using regular expressions for field splitting. It is not well specified in the POSIX standard, or anywhere else, what ‘^’ means when splitting fields. Does the ‘^’ match only at the beginning of the entire record? Or is each field separator a new string? It turns out that different `awk` versions answer this question differently, and you should not rely on any specific behavior in your programs. (d.c.)

As a point of information, BWK `awk` allows ‘^’ to match only at the beginning of the record. `gawk` also works this way. For example:

```
$ echo 'xxAA  xxBxx  C' |
> gawk -F '(^x+)|( +)' '{ for (i = 1; i <= NF; i++)
>                             printf "-->%s<--\n", $i }'
-| --><--
-| -->AA<--
-| -->xxBxx<--
-| -->C<--
```

Finally, field splitting with regular expressions works differently than regexp matching with the `sub()`, `gsub()`, and `gensub()` (see String-Manipulation Functions). Those functions allow a regexp to match the empty string; field splitting does not. Thus, for example ‘FS = "()"’ does *not* split fields between characters.

#### 4.5.3 Making Each Character a Separate Field

There are times when you may want to examine each character of a record separately. This can be done in `gawk` by simply assigning the null string (`""`) to `FS`. (c.e.) In this case, each individual character in the record becomes a separate field. For example:

```
$ echo a b | gawk 'BEGIN { FS = "" }
>                  {
>                      for (i = 1; i <= NF; i = i + 1)
>                          print "Field", i, "is", $i
>                  }'
-| Field 1 is a
-| Field 2 is
-| Field 3 is b
```

Traditionally, the behavior of `FS` equal to `""` was not defined. In this case, most versions of Unix `awk` simply treat the entire record as only having one field. (d.c.) In compatibility mode (see Command-Line Options), if `FS` is the null string, then `gawk` also behaves this way.

#### 4.5.4 Working With Comma Separated Value Files

Many commonly-used tools use a comma to separate fields, instead of whitespace. This is particularly true of popular spreadsheet programs. There is no universally accepted standard for the format of these files, although RFC 4180 lists the common practices.

For decades, anyone wishing to work with CSV files and `awk` had to “roll their own” solution. (For an example, see Defining Fields by Content). In 2023, Brian Kernighan decided to add CSV support to his version of `awk`. In order to keep up, `gawk` too provides the same support as his version. To use CSV data, invoke `gawk` with either of the -k or --csv options.

Fields in CSV files are separated by commas. In order to allow a comma to appear inside a field (i.e., as data), the field may be quoted by beginning and ending it with double quotes. In order to allow a double quote inside a field, the field *must* be quoted, and two double quotes represent an actual double quote. The double quote that starts a quoted field must be the first character after the comma. Table 4.1 shows some examples.

| Input | Field Contents |
|---|---|
| `abc def` | `abc def` |
| `"quoted data"` | `quoted data` |
| `"quoted, data"` | `quoted, data` |
| `"She said ""Stop!""."` | `She said "Stop!".` |

**Table 4.1:**Examples of CSV data

Additionally, and here’s where it gets messy, newlines are also allowed inside double-quoted fields! In order to deal with such things, when processing CSV files, `gawk` scans the input data looking for newlines that are not enclosed in double quotes. Thus, use of the --csv option totally overrides normal record processing with `RS` (see How Input Is Split into Records), as well as field splitting with any of `FS`, `FIELDWIDTHS`, or `FPAT`.

| Carriage-Return–Line-Feed Line Endings In CSV Files |
|---|
| `\r\n` *is the invention of the devil.* — *Brian Kernighan* Many CSV files are imported from systems where the line terminator for text files is a carriage-return–line-feed pair (CR-LF, ‘\r’ followed by ‘\n’). For ease of use, when processing CSV files, `gawk` converts CR-LF pairs into a single newline. That is, the ‘\r’ is removed. This occurs only when a CR is paired with an LF; a standalone CR is left alone. This behavior is consistent with Windows systems which automatically convert CR-LF in files into a plain LF in memory, and also with the commonly available `unix2dos` utility program. |

The behavior of the `split()` function (not formally discussed yet, see String-Manipulation Functions) differs slightly when processing CSV files. When called with two arguments (‘split(*string*, *array*)’), `split()` does CSV-based splitting. Otherwise, it behaves normally.

If --csv has been used, `PROCINFO["CSV"]` will exist. Otherwise, it will not. See Built-in Variables That Convey Information.

Finally, if --csv has been used, assigning a value to any of `FS`, `FIELDWIDTHS`, `FPAT`, or `RS` generates a warning message.

To be clear, `gawk` takes RFC 4180 as its specification for CSV input data. There are no mechanisms for accepting nonstandard CSV data, such as files that use a semicolon instead of a comma as the separator.

#### 4.5.5 Setting `FS` from the Command Line

`FS` can be set on the command line. Use the -F option to do so. For example:

```
awk -F, 'program' input-files
```

sets `FS` to the ‘,’ character. Notice that the option uses an uppercase ‘F’ instead of a lowercase ‘f’. The latter option (-f) specifies a file containing an `awk` program.

The value used for the argument to -F is processed in exactly the same way as assignments to the predefined variable `FS`. Any special characters in the field separator must be escaped appropriately. For example, to use a ‘\’ as the field separator on the command line, you would have to type:

```
# same as FS = "\\"
awk -F\\\\ '...' files ...
```

Because ‘\’ is used for quoting in the shell, `awk` sees ‘-F\\’. Then `awk` processes the ‘\\’ for escape characters (see Escape Sequences), finally yielding a single ‘\’ to use for the field separator.

As a special case, in compatibility mode (see Command-Line Options), if the argument to -F is ‘t’, then `FS` is set to the TAB character. If you type ‘-F\t’ at the shell, without any quotes, the ‘\’ gets deleted, so `awk` figures that you really want your fields to be separated with TABs and not ‘t’s. Use ‘-v FS="t"’ or ‘-F"[t]"’ on the command line if you really do want to separate your fields with ‘t’s. Use ‘-F '\t'’ when not in compatibility mode to specify that TABs separate fields.

As an example, let’s use an `awk` program file called edu.awk that contains the pattern `/edu/` and the action ‘print $1’:

```
/edu/   { print $1 }
```

Let’s also set `FS` to be the ‘-’ character and run the program on the file mail-list. The following command prints a list of the names of the people that work at or attend a university, and the first three digits of their phone numbers:

```
$ awk -F- -f edu.awk mail-list
-| Fabius       555
-| Samuel       555
-| Jean
```

Note the third line of output. The third line in the original file looked like this:

```
Jean-Paul    555-2127     jeanpaul.campanorum@nyu.edu     R
```

The ‘-’ as part of the person’s name was used as the field separator, instead of the ‘-’ in the phone number that was originally intended. This demonstrates why you have to be careful in choosing your field and record separators.

Perhaps the most common use of a single character as the field separator occurs when processing the Unix system password file. On many Unix systems, each user has a separate entry in the system password file, with one line per user. The information in these lines is separated by colons. The first field is the user’s login name and the second is the user’s encrypted or shadow password. (A shadow password is indicated by the presence of a single ‘x’ in the second field.) A password file entry might look like this:

```
arnold:x:2076:10:Arnold Robbins:/home/arnold:/bin/bash
```

The following program searches the system password file and prints the entries for users whose full name is not indicated:

```
awk -F: '$5 == ""' /etc/passwd
```

#### 4.5.6 Making the Full Line Be a Single Field

Occasionally, it’s useful to treat the whole input line as a single field. This can be done easily and portably simply by setting `FS` to `"\n"` (a newline):25

```
awk -F'\n' 'program' files ...
```

When you do this, `$1` is the same as `$0`.

| Changing `FS` Does Not Affect the Fields |
|---|
| According to the POSIX standard, `awk` is supposed to behave as if each record is split into fields at the time it is read. In particular, this means that if you change the value of `FS` after a record is read, the values of the fields (i.e., how they were split) should reflect the old value of `FS`, not the new one. However, many older implementations of `awk` do not work this way. Instead, they defer splitting the fields until a field is actually referenced. The fields are split using the *current* value of `FS`! (d.c.) This behavior can be difficult to diagnose. The following example illustrates the difference between the two methods: sed 1q /etc/passwd \| awk '{ FS = ":" ; print $1 }' which usually prints: root on an incorrect implementation of `awk`, while `gawk` prints the full first line of the file, something like: root:x:0:0:Root:/: (The `sed`26 command prints just the first line of /etc/passwd.) |

#### 4.5.7 Field-Splitting Summary

It is important to remember that when you assign a string constant as the value of `FS`, it undergoes normal `awk` string processing. For example, with Unix `awk` and `gawk`, the assignment ‘FS = "\.."’ assigns the character string `".."` to `FS` (the backslash is stripped). This creates a regexp meaning “fields are separated by occurrences of any two characters.” If instead you want fields to be separated by a literal period followed by any single character, use ‘FS = "\\.."’.

The following list summarizes how fields are split, based on the value of `FS` (‘==’ means “is equal to”):

**`gawk` was invoked with --csv**

Field splitting follows the rules given in Working With Comma Separated Value Files. The value of `FS` is ignored.

**`FS == " "`**

Fields are separated by runs of whitespace. Leading and trailing whitespace are ignored. This is the default.

**`FS == *any other single character*`**

Fields are separated by each occurrence of the character. Multiple successive occurrences delimit empty fields, as do leading and trailing occurrences. The character can even be a regexp metacharacter; it does not need to be escaped.

**`FS == *regexp*`**

Fields are separated by occurrences of characters that match *regexp*. Leading and trailing matches of *regexp* delimit empty fields.

**`FS == ""`**

Each individual character in the record becomes a separate field. (This is a common extension; it is not specified by the POSIX standard.)

| `FS` and `IGNORECASE` |
|---|
| The `IGNORECASE` variable (see Built-in Variables That Control `awk`) affects field splitting *only* when the value of `FS` is a regexp. It has no effect when `FS` is a single character, even if that character is a letter. Thus, in the following code: FS = "c" IGNORECASE = 1 $0 = "aCa" print $1 The output is ‘aCa’. If you really want to split fields on an alphabetic character while ignoring case, use a regexp that will do it for you (e.g., ‘FS = "[c]"’). In this case, `IGNORECASE` will take effect. |

### 4.6 Reading Fixed-Width Data

This section discusses an advanced feature of `gawk`. If you are a novice `awk` user, you might want to skip it on the first reading.

`gawk` provides a facility for dealing with fixed-width fields with no distinctive field separator. We discuss this feature in the following subsections.

#### 4.6.1 Processing Fixed-Width Data

An example of fixed-width data would be the input for old Fortran programs where numbers are run together, or the output of programs that did not anticipate the use of their output as input for other programs.

An example of the latter is a table where all the columns are lined up by the use of a variable number of spaces and *empty fields are just spaces*. Clearly, `awk`’s normal field splitting based on `FS` does not work well in this case. Although a portable `awk` program can use a series of `substr()` calls on `$0` (see String-Manipulation Functions), this is awkward and inefficient for a large number of fields.

The splitting of an input record into fixed-width fields is specified by assigning a string containing space-separated numbers to the built-in variable `FIELDWIDTHS`. Each number specifies the width of the field, *including* columns between fields. If you want to ignore the columns between fields, you can specify the width as a separate field that is subsequently ignored. It is a fatal error to supply a field width that has a negative value.

The following data is the output of the Unix `w` utility. It is useful to illustrate the use of `FIELDWIDTHS`:

```
 10:06pm  up 21 days, 14:04,  23 users
User     tty       login  idle   JCPU   PCPU  what
hzuo     ttyV0     8:58pm            9      5  vi p24.tex
hzang    ttyV3     6:37pm    50                -csh
eklye    ttyV5     9:53pm            7      1  em thes.tex
dportein ttyV6     8:17pm  1:47                -csh
gierd    ttyD3    10:00pm     1                elm
dave     ttyD4     9:47pm            4      4  w
brent    ttyp0    26Jun91  4:46  26:46   4:41  bash
dave     ttyq4    26Jun9115days     46     46  wnewmail
```

The following program takes this input, converts the idle time to number of seconds, and prints out the first two fields and the calculated idle time:

```
BEGIN  { FIELDWIDTHS = "9 6 10 6 7 7 35" }
NR > 2 {
    idle = $4
    sub(/^ +/, "", idle)   # strip leading spaces
    if (idle == "")
        idle = 0
    if (idle ~ /:/) {      # hh:mm
        split(idle, t, ":")
        idle = t[1] * 60 + t[2]
    }
    if (idle ~ /days/)
        idle *= 24 * 60 * 60

    print $1, $2, idle
}
```

> **NOTE:** The preceding program uses a number of `awk` features that haven’t been introduced yet.

Running the program on the data produces the following results:

```
hzuo      ttyV0  0
hzang     ttyV3  50
eklye     ttyV5  0
dportein  ttyV6  107
gierd     ttyD3  1
dave      ttyD4  0
brent     ttyp0  286
dave      ttyq4  1296000
```

Another (possibly more practical) example of fixed-width input data is the input from a deck of balloting cards. In some parts of the United States, voters mark their choices by punching holes in computer cards. These cards are then processed to count the votes for any particular candidate or on any particular issue. Because a voter may choose not to vote on some issue, any column on the card may be empty. An `awk` program for processing such data could use the `FIELDWIDTHS` feature to simplify reading the data. (Of course, getting `gawk` to run on a system with card readers is another story!)

#### 4.6.2 Skipping Intervening Fields
