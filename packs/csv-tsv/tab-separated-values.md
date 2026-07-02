---
title: "Tab-separated values"
source: https://en.wikipedia.org/wiki/Tab-separated_values
domain: csv-tsv
license: CC-BY-SA-4.0
tags: csv format, comma-separated values, tab-separated values, tabular text format
fetched: 2026-07-02
---

# Tab-separated values

**Tab-separated values** (**TSV**) is a plain text data format for storing tabular data where the values of a record are separated by a tab character and each record is a line (i.e. newline separated). The TSV format is a form of delimiter-separated values (DSV) and is similar to the commonly-used comma-separated values (CSV) format.

TSV is a relatively simple format and is widely supported for data exchange by software that generally deals with tabular data. For example, a TSV file might be used to transfer information from a database to a spreadsheet.

## Example

The following are records of the Iris flower data set in TSV format. Since a tab is not a printable character (is invisible), an arrow (→) is used for demonstration here to denote a tab character.

```
Sepal length→Sepal width→Petal length→Petal width→Species
5.1→3.5→1.4→0.2→I. setosa
4.9→3.0→1.4→0.2→I. setosa
4.7→3.2→1.3→0.2→I. setosa
4.6→3.1→1.5→0.2→I. setosa
5.0→3.6→1.4→0.2→I. setosa
```

The following is the same data rendered as a table.

| Sepal length | Sepal width | Petal length | Petal width | Species |
|---|---|---|---|---|
| 5.1 | 3.5 | 1.4 | 0.2 | I. setosa |
| 4.9 | 3.0 | 1.4 | 0.2 | I. setosa |
| 4.7 | 3.2 | 1.3 | 0.2 | I. setosa |
| 4.6 | 3.1 | 1.5 | 0.2 | I. setosa |
| 5.0 | 3.6 | 1.4 | 0.2 | I. setosa |

If a text editor that supports Dynamic tab stops (aka. "elastic tabstops") is used to view the contents of a TSV file, the layout will look like the table rendering just without cell borders and header row formatting (though the latter can be achieved using Unicode characters).

## Known problems in comparison to CSV

1. Unlike for CSV, there is no widely agreed-upon specification for TSV which can lead to inconsistent behaviors when dealing with backslashes or quotation marks or the disallowed tabs and line breaks. For TSV there is only a mime-type assignment. Escaping rules for line breaks and tabs are inconsistent among implementations. Some use backslash (\) notation from C, some the quoting rules from CSV, some simply can not store tabs and line breaks.
2. If backslash escaping is used backslashes also need to be escaped and line breaks in fields could become "\r\n" on Windows which may add another layer of line break handling
3. Non-technical users, who are editing TSV with a text editor, sometimes mix up tabs and spaces, corrupting the data. Empty fields may also be difficult to count in editors where tabs are merely shown as whitespace.
4. Despite lower complexity, fewer applications implement it.
5. The file size increase of quoting both commas and quotes in CSV is usually insignificant on modern systems.
6. Terminal emulators often render tabs as multiple spaces which prevents copying a tab correctly, thus preventing copying TSV formatted data directly from a selection on the terminal without combining all fields into one.

## Delimiter collision

As a form of delimiter collision, if a field (record value) contained a tab character, the data format would become meaningless since tabs were no longer *only* used between fields. To prevent this situation, the IANA media type standard for TSV simply disallows a tab within a field. Similarly, a value cannot contain a line terminator. To represent a value with an embedded tab or line terminator character, a commonly-used mechanism is to replace the character with the corresponding escape sequence as shown in the following table.

| sequence | represents |
|---|---|
| `\t` | tab |
| `\n` | line feed |
| `\r` | carriage return |
| `\\` | backslash |

Another commonly-used convention, borrowed from CSV (RFC 4180), is to enclose a value that contains a tab or line terminator character in quotes. Among others it's used by LibreOffice Calc where the backslash (\) notation is not implemented and TSV is simply treated as a variant of CSV with tab delimiters instead of comma.

## Line terminator

As for any text file, the character(s) used for line terminator varies. On a Microsoft-based system, normally it's a carriage return (CR) and line feed (LF) sequence. On a Unix-based system, it's just LF. The de-facto specification uses the term "EOL" which is an ambiguous term like line terminator and newline. Software often is designed to either handle the line terminator for the platform on which it runs or to handle either terminator.
