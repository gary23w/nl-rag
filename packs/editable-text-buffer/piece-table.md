---
title: "Piece table"
source: https://en.wikipedia.org/wiki/Piece_table
domain: editable-text-buffer
license: CC-BY-SA-4.0
tags: rope data structure, gap buffer, piece table, text sequence structure
fetched: 2026-07-02
---

# Piece table

In computing, a **piece table** is a data structure typically used to represent a text document while it is edited in a text editor. Initially a reference (or "span") to the whole of the original file is created, which represents the as yet unchanged file. Subsequent inserts and deletes replace a span by combinations of one, two, or three references to sections of either the original document or to a buffer holding inserted text.

Typically the text of the original document is held in one immutable block, and the text of each subsequent insert is stored in new immutable blocks. Because even deleted text is still included in the piece table, this makes multi-level or unlimited undo easier to implement with a piece table than with alternative data structures such as a gap buffer.

This data structure was invented by J Strother Moore.

## Description

For this description, we use buffer as the immutable block to hold the contents.

A piece table consists of three columns:

- Which buffer
- Start index in the buffer
- Length in the buffer

In addition to the table, two buffers are used to handle edits:

- "*Original buffer*": A buffer to the original text document. This buffer is read-only.
- "*Add buffer*": A buffer to a temporary file. This buffer is append-only.

## Operations

### Index

> *Definition:* `Index(i)`: return the character at position *i* in the pieced-together document (PTD).

To retrieve the *i*-th character of the PTD, the appropriate entry in a piece table is read.

#### Example

Given the following buffers and piece table:

| Buffer | Content |
|---|---|
| Original file | `ipsum sit amet` |
| Add file | `Lorem deletedtext dolor` |

| Which | Start index | Length | PTD indices |
|---|---|---|---|
| Add | 0 | 6 | 0–5 |
| Original | 0 | 5 | 6–10 |
| Add | 17 | 6 | 11–16 |
| Original | 5 | 9 | 17–25 |

A real implementation of a piece table will not include a PTD indices ("pieced-together document") column due to the column containing information that can be deduced from the piece table's start index, length, and row position, but it is shown above for educational purposes.

The piece table's ordering of rows implicitly describes the ordering of characters to use from the available buffers. I.e., the first row of the piece table (e.g., <Add,0,6>) describes the first sequence of characters in the PTD (e.g., PTD indices 0–5). The second row of the piece table (e.g., <Original,0,5>) describes the sequence of characters from a possibly different buffer that will immediately follow the characters chosen from the first sequence (e.g., PTD indices 6–10). This continues to the end of the PTD. In the above example, the piece table indicates that the PTD will have 6 + 5 + 6 + 9 = 26 characters.

To get the (character) value `Index(15)`, we first find the entry (row) in the piece table that corresponds to the PTD index 15. The first entry describes characters in PTD indices 0 to 5, the second entry PTD indices 6 to 10, and the 3rd entry PTD indices 11–16. Since the 3rd entry of the piece table corresponds to PTD index 15 (11 ≤ 15 ≤ 16), the 3rd entry is retrieved. The piece table's 3rd entry instructs the program to look for the characters in the "*add file*" buffer, starting at index 17 in that buffer. The relative index in that entry is PTD_SoughtIndex − PTD_StartIndexOfEntry = 15 − 11 = 4, which is added to the start position of the entry in the buffer to obtain the index of the letter: 4 + 17 = 21. The value of `Index(15)` is the 21st character of the "add file" buffer, which is the character "o". In general and in the above example,

```
Buffer_IdxOfSoughtChar = PTD_SoughtIndex − PTD_StartIdxOfEntry + Buffer_StartIdxOfEntry
                    21 = 15              − 11                  + 17
SoughtChar = Entry_NameOfBuffer[Buffer_IdxOfSoughtChar]
       'o' = AddFileBuf[21]
---------------------------
So,    'o' = Index(15)
```

For the buffers and piece table given above, the following PTD is shown:

```
 "Lorem "    (from piece table entry 1)
+"ipsum"     (from piece table entry 2)
+" dolor"    (from piece table entry 3)
+" sit amet" (from piece table entry 4)
--------------------------
Lorem ipsum dolor sit amet
```

### Insert

Inserting characters to the text consists of:

- Appending characters to the "add file" buffer, and
- Updating the entry in piece table (breaking an entry into two or three)

### Delete

Single character deletion can be one of two possible conditions:

- The deletion is at the start or end of a piece entry, in which case the appropriate entry in piece table is modified.
- The deletion is in the middle of a piece entry, in which case the entry is split then one of the successor entries is modified as above.

## Usage

Several text editors use an in-RAM piece table internally, including Bravo, Abiword, Atom and Visual Studio Code.

The "fast save" feature in some versions of Microsoft Word uses a piece table for the on-disk file format.

The on-disk representation of text files in the Oberon System uses a **piece chain** technique that allows pieces of one document to point to text stored in some other document, similar to transclusion.
