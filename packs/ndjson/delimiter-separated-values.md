---
title: "Delimiter-separated values"
source: https://en.wikipedia.org/wiki/Delimiter-separated_values
domain: ndjson
license: CC-BY-SA-4.0
tags: newline-delimited json, ndjson format, json streaming, line-delimited records
fetched: 2026-07-02
---

# Delimiter-separated values

**Delimiter-separated values** (DSV) is a way of storing tabular data by separating the fields (values) of each row with a specific character as a delimiter. DSV is often used for data exchange and is commonly supported by database and spreadsheet software.

A **delimited text file** is a text file that stores data as DSV. Such a file can be classified as a flat-file database if, in fact, the data is database-like – accessing individual rows is meaningful.

A commonly used alternative for text data is fixed-width where each column has the same number of characters – limiting the length of each field value. In contrast, DSV supports field values of any length.

## Format

DSV is a categorization of data format, not a particular format. To be useful, a convention must be established that defines the precise format. In general a format is categorized as DSV if it is lines of delimiter-separated values (where lines are newline-separated). The first row is sometimes a special record containing the column names.

Any character may be used to separate field values, and the more commonly used include comma, tab, colon, vertical bar (a.k.a. pipe) and space. ASCII and Unicode include control characters that are intended to be used as delimiters: File Separator, Group Separator, Record Separator, and Unit Separator. Use of these in DSV data is relatively uncommon although the MARC 21 bibliographic data format does.

Two commonly-used sub-categories of DSV, comma-separated values (CSV) and tab-separated values (TSV), are supported by many software packages including many spreadsheet and statistical applications. Some can import such data even without the user describing the format – such as which character to use as the delimiter. Even though such an application may more directly support a more capable and possibly proprietary internal data model (for example, accdb or xlsx), they can map DSV data to their internal data model.

## Delimiter collision

A particular challenge of DSV is delimiter collision – what happens when the delimiter character is embedded in a field value without accommodation for doing so. The character is interpreted as a separator – splitting a single, logical value into two. Some DSV conventions simply disallow a delimiter in a value while others provide a mechanism that allows for embedding delimiters.

A commonly-used way to avoid delimiter collision is to enclose a field value in double quotes. A convention could require this for all values or it could be optional so that it might only be used for values that have an embedded delimiter.

Collision can be avoided if the convention disallows the delimiter in a field value; the tacit implication if the convention provides no way to avoid collision. Using a relatively unusual character (e.g. tilde `~`) limits the impact on possible field values. But, even though a character may seem unusual, in practice, it might be used and then result in a processing error.

## Example

In the following example, the table is formatted per typical CSV: fields separated by a comma. Each field value is enclosed in double quotes so that a field value can contain a comma. The comma in `"Bloggs, Fred"` is not a value separator because the text is enclosed in double-quotes. Some formats allow newline to be included in a value via this mechanism. To encode a double quote in a value, two double quotes are used where the first one acts as an escape character so that the second one is interpreted as a double quote instead of field begin or end. The value `"Muniz, Alvin ""Hank"""` is interpreted as `Muniz, Alvin "Hank"`.

```
"Date","Pupil","Grade"
"25 May","Bloggs, Fred","C"
"25 May","Doe, Jane","B"
"15 July","Bloggs, Fred","A"
"15 April","Muniz, Alvin ""Hank""","A"
```
