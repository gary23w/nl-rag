---
title: "COBOL (part 2/3)"
source: https://en.wikipedia.org/wiki/COBOL
domain: cobol
license: CC-BY-SA-4.0
tags: cobol
fetched: 2026-07-03
part: 2/3
---

## Features

### Syntax

COBOL has an English-like syntax, which is used to describe nearly everything in COBOL programs. For example, a condition can be expressed as  `x IS GREATER THAN y` or more concisely as  `x GREATER y`  or  `x > y`. More complex conditions can be abbreviated by removing repeated conditions and variables. For example,  `a > b AND a > c OR a = d`  can be shortened to `a > b AND c OR = d`. To support this syntax, COBOL has over 300 keywords. Some of the keywords are simple alternative or pluralized spellings of the same word, which provides for more grammatically appropriate statements and clauses; e.g., the `IN` and `OF` keywords can be used interchangeably, as can `TIME` and `TIMES`, and `VALUE` and `VALUES`.

Each COBOL program is made up of four basic lexical items: words, literals, picture character-strings and separators. Words include reserved words and user-defined identifiers. They are up to 31 characters long and may include letters, digits, hyphens and underscores. Literals include numerals (e.g. `12`) and strings (e.g. `'Hello!'`). Separators include the space character and commas and semi-colons followed by a space.

A COBOL program is split into four divisions: the identification division, the environment division, the data division and the procedure division. The identification division specifies the name and type of the source element and is where classes and interfaces are specified. The environment division specifies any program features that depend on the system running it, such as files and character sets. The data division is used to declare variables and parameters. The procedure division contains the program's statements. Each division is sub-divided into sections, which are made up of paragraphs.

#### Metalanguage

COBOL's syntax is usually described with a unique metalanguage using braces, brackets, bars and underlining. The metalanguage was developed for the original COBOL specifications.

| Element | Appearance | Function |
|---|---|---|
| All capitals | EXAMPLE | Reserved word |
| Underlining | EXAMPLE | The reserved word is compulsory |
| Braces | { } | Only one option may be selected |
| Brackets | [] | Zero or one options may be selected |
| Ellipsis | ... | The preceding element may be repeated |
| Bars | {\| \|} | One or more options may be selected. Any option may only be selected once. |
| [\| \|] | Zero or more options may be selected. Any option may only be selected once. |   |

As an example, consider the following description of an `ADD` statement:

```
 
  
    
      
        
          
            
              
                
                  
                    
                      ADD
                    
                    _
                  
                
                
                
                  
                    {
                    
                      
                        
                          
                            identifier-1
                          
                        
                      
                      
                        
                          
                            literal-1
                          
                        
                      
                    
                    }
                  
                
                …
                
                
                  
                    
                      TO
                    
                    _
                  
                
                
                
                  {
                  
                    
                      identifier-2
                    
                    
                    
                      [
                      
                        
                        
                          
                            
                              ROUNDED
                            
                            _
                          
                        
                        
                      
                      ]
                    
                  
                  }
                
                …
              
            
            
              
                
                
                  [
                  
                    |
                    
                      
                        
                          
                            
                              
                                ON
                              
                            
                            
                            
                              
                                
                                  SIZE
                                
                                _
                              
                            
                            
                            
                              
                                
                                  ERROR
                                
                                _
                              
                            
                            
                            
                              imperative-statement-1
                            
                          
                        
                        
                          
                            
                              
                                
                                  NOT
                                
                                _
                              
                            
                            
                            
                              
                                ON
                              
                            
                            
                            
                              
                                
                                  SIZE
                                
                                _
                              
                            
                            
                            
                              
                                
                                  ERROR
                                
                                _
                              
                            
                            
                            
                              imperative-statement-2
                            
                          
                        
                      
                    
                    |
                  
                  ]
                
              
            
            
              
                
                
                  [
                  
                    
                    
                      
                        
                          END-ADD
                        
                        _
                      
                    
                    
                  
                  ]
                
              
            
          
        
      
    
    {\displaystyle {\begin{array}{l}{\underline {\texttt {ADD}}}\,{\begin{Bmatrix}{\text{identifier-1}}\\{\text{literal-1}}\end{Bmatrix}}\dots \;{\underline {\texttt {TO}}}\,\left\{{\text{identifier-2}}\,\left[\,{\underline {\texttt {ROUNDED}}}\,\right]\right\}\dots \\[1em]\quad \left[\left|{\begin{array}{l}{\texttt {ON}}\,{\underline {\texttt {SIZE}}}\,{\underline {\texttt {ERROR}}}\,{\text{imperative-statement-1}}\\{\underline {\texttt {NOT}}}\,{\texttt {ON}}\,{\underline {\texttt {SIZE}}}\,{\underline {\texttt {ERROR}}}\,{\text{imperative-statement-2}}\end{array}}\right|\right]\\[1em]\quad \left[\,{\underline {\texttt {END-ADD}}}\,\right]\end{array}}}
  
```

This description permits the following variants:

```mw
ADD 1 TO x
ADD 1, a, b TO x ROUNDED, y, z ROUNDED

ADD a, b TO c
    ON SIZE ERROR
        DISPLAY "Error"
END-ADD

ADD a TO b
    NOT SIZE ERROR
        DISPLAY "No error"
    ON SIZE ERROR
        DISPLAY "Error"
```

### Code format

The height of COBOL's popularity coincided with the era of keypunch machines and punched cards. The program itself was written onto punched cards, then read in and compiled, and the data fed into the program was sometimes on cards as well.

COBOL can be written in two formats: fixed (the default) or free. In fixed-format, code must be aligned to fit in certain areas (a holdover from using punched cards). Until COBOL 2002, these were:

| Name | Column(s) | Usage |
|---|---|---|
| Sequence number area | 1–6 | Originally used for card/line numbers (facilitating mechanical punched card sorting to assure intended program code sequence after manual editing/handling), this area is ignored by the compiler |
| Indicator area | 7 | The following characters are allowed here: `*` – Comment line `/` – Comment line that will be printed on a new page of a source listing `-` – Continuation line, where words or literals from the previous line are continued `D` – Line enabled in debugging mode, which is otherwise ignored |
| Area A | 8–11 | This contains: `DIVISION`, `SECTION` and procedure headers; 01 and 77 level numbers and file/report descriptors |
| Area B | 12–72 | Any other code not allowed in Area A |
| Program name area | 73– | Historically up to column 80 for punched cards, it is used to identify the program or sequence the card belongs to |

In COBOL 2002, Areas A and B were merged to form the program-text area, which now ends at an implementor-defined column.

COBOL 2002 also introduced free-format code. Free-format code can be placed in any column of the file, as in newer programming languages. Comments are specified using `*>`, which can be placed anywhere and can also be used in fixed-format source code. Continuation lines are not present, and the `>>PAGE` directive replaces the `/` indicator.

### Identification division

The identification division identifies the following code entity and contains the definition of a class or interface.

#### Object-oriented programming

Classes and interfaces have been in COBOL since 2002. Classes have factory objects, containing class methods and variables, and instance objects, containing instance methods and variables. Inheritance and interfaces provide polymorphism. Support for generic programming is provided through parameterized classes, which can be instantiated to use any class or interface. Objects are stored as references which may be restricted to a certain type. There are two ways of calling a method: the `INVOKE` statement, which acts similarly to `CALL`, or through inline method invocation, which is analogous to using functions.

```mw
*> These are equivalent.
INVOKE my-class "foo" RETURNING var
MOVE my-class::"foo" TO var *> Inline method invocation
```

COBOL does not provide a way to hide methods. Class data can be hidden, however, by declaring it without a `PROPERTY` clause, which leaves external code no way to access it. Method overloading was added in COBOL 2014.

### Environment division

The environment division contains the configuration section and the input-output section. The configuration section is used to specify variable features such as currency signs, locales and character sets. The input-output section contains file-related information.

#### Files

COBOL supports three file formats, or **organizations**: sequential, indexed and relative. In sequential files, records are contiguous and must be traversed sequentially, similarly to a linked list. Indexed files have one or more indexes which allow records to be randomly accessed and which can be sorted on them. Each record must have a unique key, but other, **alternate**, record keys need not be unique. Implementations of indexed files vary between vendors, although common implementations, such as C-ISAM and VSAM, are based on IBM's ISAM. Other implementations are Record Management Services on OpenVMS and Enscribe on HPE NonStop (Tandem). Relative files, like indexed files, have a unique record key, but they do not have alternate keys. A relative record's key is its ordinal position; for example, the 10th record has a key of 10. This means that creating a record with a key of 5 may require the creation of (empty) preceding records. Relative files also allow for both sequential and random access.

A common non-standard extension is the **line sequential** organization, used to process text files. Records in a file are terminated by a newline and may be of varying length.

### Data division

The data division is split into six sections which declare different items: the file section, for file records; the working-storage section, for static variables; the local-storage section, for automatic variables; the linkage section, for parameters and the return value; the report section and the screen section, for text-based user interfaces.

#### Aggregated data

Data items in COBOL are declared hierarchically through the use of level-numbers which indicate if a data item is part of another. An item with a higher level-number is subordinate to an item with a lower one. Top-level data items, with a level-number of 1, are called **records**. Items that have subordinate aggregate data are called **group items**; those that do not are called **elementary items**. Level-numbers used to describe standard data items are between 1 and 49.

```mw
       01  some-record.                   *> Aggregate group record item
           05  num            PIC 9(10).  *> Elementary item
           05  the-date.                  *> Aggregate (sub)group record item
               10  the-year   PIC 9(4).   *> Elementary item
               10  the-month  PIC 99.     *> Elementary item
               10  the-day    PIC 99.     *> Elementary item
```

In the above example, elementary item `num` and group item `the-date` are subordinate to the record `some-record`, while elementary items `the-year`, `the-month`, and `the-day` are part of the group item `the-date`.

Subordinate items can be disambiguated with the `IN` (or `OF`) keyword. For example, consider the example code above along with the following example:

```mw
       01  sale-date.
           05  the-year       PIC 9(4).
           05  the-month      PIC 99.
           05  the-day        PIC 99.
```

The names `the-year`, `the-month`, and `the-day` are ambiguous by themselves, since more than one data item is defined with those names. To specify a particular data item, for instance one of the items contained within the `sale-date` group, the programmer would use `the-year IN sale-date` (or the equivalent `the-year OF sale-date`). This syntax is similar to the "dot notation" supported by most contemporary languages.

#### Other data levels

A level-number of 66 is used to declare a re-grouping of previously defined items, irrespective of how those items are structured. This data level, also referred to by the associated *`RENAMES` clause*, is rarely used and, circa 1988, was usually found in old programs. Its ability to ignore the hierarchical and logical structure data meant its use was not recommended and many installations forbade its use.

```mw
       01  customer-record.
           05  cust-key            PIC X(10).
           05  cust-name.
               10  cust-first-name PIC X(30).
               10  cust-last-name  PIC X(30).
           05  cust-dob            PIC 9(8).
           05  cust-balance        PIC 9(7)V99.
           
       66  cust-personal-details   RENAMES cust-name THRU cust-dob.
       66  cust-all-details        RENAMES cust-name THRU cust-balance.
```

A 77 level-number indicates the item is stand-alone, and in such situations is equivalent to the level-number 01. For example, the following code declares two 77-level data items, `property-name` and `sales-region`, which are non-group data items that are independent of (not subordinate to) any other data items:

```mw
       77  property-name      PIC X(80).
       77  sales-region       PIC 9(5).
```

An 88 level-number declares a **condition name** (a so-called 88-level) which is true when its parent data item contains one of the values specified in its `VALUE` clause. For example, the following code defines two 88-level condition-name items that are true or false depending on the current character data value of the `wage-type` data item. When the data item contains a value of `'H'`, the condition-name `wage-is-hourly` is true, whereas when it contains a value of `'S'` or `'Y'`, the condition-name `wage-is-yearly` is true. If the data item contains some other value, both of the condition-names are false.

```mw
       01  wage-type          PIC X.
           88  wage-is-hourly VALUE "H".
           88  wage-is-yearly VALUE "S", "Y".
```

#### Data types

Standard COBOL provides the following data types:

| Data type | Sample declaration | Notes |
|---|---|---|
| Alphabetic | `PIC A(30)` | May contain only letters or spaces. |
| Alphanumeric | `PIC X(30)` | May contain any characters. |
| Boolean | `PIC 1 USAGE BIT` | Data stored in the form of 0s and 1s, as a binary number. |
| Index | `USAGE INDEX` | Used to reference table elements. |
| National | `PIC N(30)` | Similar to alphanumeric, but using an extended character set, e.g. UTF-8. |
| Numeric | `PIC 9(5)V9(2)` | Contains exactly 7 digits (7=5+2). 'V' locates the implicit decimal in a fixed point number. |
| Object | `USAGE OBJECT REFERENCE` | May reference either an object or `NULL`. |
| Pointer | `USAGE POINTER` |   |

Type safety is variable in COBOL. Numeric data is converted between different representations and sizes silently and alphanumeric data can be placed in any data item that can be stored as a string, including numeric and group data. In contrast, object references and pointers may only be assigned from items of the same type and their values may be restricted to a certain type.

#### PICTURE clause

A `PICTURE` (or `PIC`) clause is a string of characters, each of which represents a portion of the data item and what it may contain. Some picture characters specify the type of the item and how many characters or digits it occupies in memory. For example, a `9` indicates a decimal digit, and an `S` indicates that the item is signed. Other picture characters (called **insertion** and **editing** characters) specify how an item should be formatted. For example, a series of `+` characters define character positions as well as how a leading sign character is to be positioned within the final character data; the rightmost non-numeric character will contain the item's sign, while other character positions corresponding to a `+` to the left of this position will contain a space. Repeated characters can be specified more concisely by specifying a number in parentheses after a picture character; for example, `9(7)` is equivalent to `9999999`. Picture specifications containing only digit (`9`) and sign (`S`) characters define purely **numeric** data items, while picture specifications containing alphabetic (`A`) or alphanumeric (`X`) characters define **alphanumeric** data items. The presence of other formatting characters define **edited numeric** or **edited alphanumeric** data items.

| `PICTURE` clause | Value in | Value out |
|---|---|---|
| `PIC 9(5)` | `100` | `00100` |
| `"Hello"` | `"Hello"` (this is legal, but results in undefined behavior) |   |
| `PIC +++++` | `-10` | `"  -10"` (note leading spaces) |
| `PIC 99/99/9(4)` | `30042003` | `"30/04/2003"` |
| `PIC *(4)9.99` | `100.50` | `"**100.50"` |
| `0` | `"****0.00"` |   |
| `PIC X(3)BX(3)BX(3)` | `"ABCDEFGHI"` | `"ABC DEF GHI"` |

#### USAGE clause

The `USAGE` clause declares the format in which data is stored. Depending on the data type, it can either complement or be used instead of a `PICTURE` clause. While it can be used to declare pointers and object references, it is mostly geared towards specifying numeric types. These numeric formats are:

- Binary, where a minimum size is either specified by the `PICTURE` clause or by a `USAGE` clause such as `BINARY-LONG`
- `USAGE COMPUTATIONAL`, where data may be stored in whatever format the implementation provides; often equivalent to  `USAGE BINARY`
- `USAGE DISPLAY`, the default format, where data is stored as a string
- Floating-point, in either an implementation-dependent format or according to IEEE 754
- `USAGE NATIONAL`, where data is stored as a string using an extended character set
- `USAGE PACKED-DECIMAL`, where data is stored in the smallest possible decimal format (typically packed binary-coded decimal)

#### Report writer

The report writer is a declarative facility for creating reports. The programmer need only specify the report layout and the data required to produce it, freeing them from having to write code to handle things like page breaks, data formatting, and headings and footings.

Reports are associated with report files, which are files which may only be written to through report writer statements.

```mw
       FD  report-out REPORT sales-report.
```

Each report is defined in the report section of the data division. A report is split into report groups which define the report's headings, footings and details. Reports work around hierarchical **control breaks**. Control breaks occur when a key variable changes it value; for example, when creating a report detailing customers' orders, a control break could occur when the program reaches a different customer's orders. Here is an example report description for a report which gives a salesperson's sales and which warns of any invalid records:

```mw
       RD  sales-report
           PAGE LIMITS 60 LINES
           FIRST DETAIL 3
           CONTROLS seller-name.

       01  TYPE PAGE HEADING.
           03  COL 1                    VALUE "Sales Report".
           03  COL 74                   VALUE "Page".
           03  COL 79                   PIC Z9 SOURCE PAGE-COUNTER.

       01  sales-on-day TYPE DETAIL, LINE + 1.
           03  COL 3                    VALUE "Sales on".
           03  COL 12                   PIC 99/99/9999 SOURCE sales-date.
           03  COL 21                   VALUE "were".
           03  COL 26                   PIC $$$$9.99 SOURCE sales-amount.

       01  invalid-sales TYPE DETAIL, LINE + 1.
           03  COL 3                    VALUE "INVALID RECORD:".
           03  COL 19                   PIC X(34) SOURCE sales-record.

       01  TYPE CONTROL HEADING seller-name, LINE + 2.
           03  COL 1                    VALUE "Seller:".
           03  COL 9                    PIC X(30) SOURCE seller-name.
```

The above report description describes the following layout:

```mw
Sales Report                                                             Page  1

Seller: Howard Bromberg
  Sales on 10/12/2008 were $1000.00
  Sales on 12/12/2008 were    $0.00
  Sales on 13/12/2008 were   $31.47
  INVALID RECORD: Howard Bromberg             XXXXYY

Seller: Howard Discount
...
Sales Report                                                            Page 12

  Sales on 08/05/2014 were  $543.98
  INVALID RECORD: William Selden      12052014FOOFOO
  Sales on 30/05/2014 were    $0.00
```

Four statements control the report writer: `INITIATE`, which prepares the report writer for printing; `GENERATE`, which prints a report group; `SUPPRESS`, which suppresses the printing of a report group; and `TERMINATE`, which terminates report processing. For the above sales report example, the procedure division might look like this:

```mw
           OPEN INPUT sales, OUTPUT report-out
           INITIATE sales-report
 
           PERFORM UNTIL 1 <> 1
               READ sales
                   AT END
                       EXIT PERFORM
               END-READ
 
               VALIDATE sales-record
               IF valid-record
                   GENERATE sales-on-day
               ELSE
                   GENERATE invalid-sales
               END-IF
           END-PERFORM
 
           TERMINATE sales-report
           CLOSE sales, report-out
           .
```

Use of the Report Writer facility tends to vary considerably; some organizations use it extensively and some not at all. In addition, implementations of Report Writer ranged in quality, with those at the lower end sometimes using excessive amounts of memory at runtime.

### Procedure division

#### Procedures

The sections and paragraphs in the procedure division (collectively called procedures) can be used as labels and as simple subroutines. Unlike in other divisions, paragraphs do not need to be in sections.

Execution goes down through the procedures of a program until it is terminated. To use procedures as subroutines, the `PERFORM` verb is used.

A `PERFORM` statement somewhat resembles a procedure call in a newer languages in the sense that execution returns to the code following the `PERFORM` statement at the end of the called code; however, it does not provide a mechanism for parameter passing or for returning a result value. If a subroutine is invoked using a simple statement like `PERFORM subroutine`, then control returns at the end of the called procedure. However, `PERFORM` is unusual in that it may be used to call a range spanning a sequence of several adjacent procedures. This is done with the `PERFORM sub-1 THRU sub-n` construct:

```mw
PROCEDURE so-and-so.
    PERFORM ALPHA
    PERFORM ALPHA THRU GAMMA
    STOP RUN.
ALPHA.
    DISPLAY 'A'.
BETA.
    DISPLAY 'B'.
GAMMA.
    DISPLAY 'C'.
```

The output of this program will be: "A A B C".

`PERFORM` also differs from conventional procedure calls in that there is, at least traditionally, no notion of a call stack. As a consequence, nested invocations are possible (a sequence of code being `PERFORM`'ed may execute a `PERFORM` statement itself), but require extra care if parts of the same code are executed by both invocations. The problem arises when the code in the inner invocation reaches the exit point of the outer invocation. More formally, if control passes through the exit point of a `PERFORM` invocation that was called earlier but has not yet completed, the COBOL 2002 standard stipulates that the behavior is undefined.

The reason is that COBOL, rather than a "return address", operates with what may be called a continuation address. When control flow reaches the end of any procedure, the continuation address is looked up and control is transferred to that address. Before the program runs, the continuation address for every procedure is initialized to the start address of the procedure that comes next in the program text so that, if no `PERFORM` statements happen, control flows from top to bottom through the program. But when a `PERFORM` statement executes, it modifies the continuation address of the called procedure (or the last procedure of the called range, if `PERFORM THRU` was used), so that control will return to the call site at the end. The original value is saved and is restored afterwards, but there is only one storage position. If two nested invocations operate on overlapping code, they may interfere which each other's management of the continuation address in several ways.

The following example (taken from Veerman & Verhoeven 2006) illustrates the problem:

```mw
LABEL1.
    DISPLAY '1'
    PERFORM LABEL2 THRU LABEL3
    STOP RUN.
LABEL2.
    DISPLAY '2'
    PERFORM LABEL3 THRU LABEL4.
LABEL3.
    DISPLAY '3'.
LABEL4.
    DISPLAY '4'.
```

One might expect that the output of this program would be "1 2 3 4 3": After displaying "2", the second `PERFORM` causes "3" and "4" to be displayed, and then the first invocation continues on with "3". In traditional COBOL implementations, this is not the case. Rather, the first `PERFORM` statement sets the continuation address at the end of `LABEL3` so that it will jump back to the call site inside `LABEL1`. The second `PERFORM` statement sets the return at the end of `LABEL4` but does not modify the continuation address of `LABEL3`, expecting it to be the default continuation. Thus, when the inner invocation arrives at the end of `LABEL3`, it jumps back to the outer `PERFORM` statement, and the program stops having printed just "1 2 3". On the other hand, in some COBOL implementations like the open-source TinyCOBOL compiler, the two `PERFORM` statements do not interfere with each other and the output is indeed "1 2 3 4 3". Therefore, the behavior in such cases is not only (perhaps) surprising, it is also not portable.

A special consequence of this limitation is that `PERFORM` cannot be used to write recursive code. To write recursive routines, one must use a nested subprogram. Another simple example to illustrate this (slightly simplified from Veerman & Verhoeven 2006):

```mw
    MOVE 1 TO A
    PERFORM LABEL
    STOP RUN.
LABEL.
    DISPLAY A
    IF A < 3
        ADD 1 TO A
        PERFORM LABEL
    END-IF
    DISPLAY 'END'.
```

One might expect that the output is "1 2 3 END END END", and in fact that is what some COBOL compilers will produce. But other compilers, like IBM COBOL, will produce code that prints "1 2 3 END END END END ..." and so on, printing "END" over and over in an endless loop. Since there is limited space to store backup continuation addresses, the backups get overwritten in the course of recursive invocations, and all that can be restored is the jump back to `DISPLAY 'END'`.

#### Statements

COBOL 2014 has 47 statements (also called **verbs**), which can be grouped into the following broad categories: control flow, I/O, data manipulation and the report writer. The report writer statements are covered in the report writer section.

#### Control flow

COBOL's conditional statements are `IF` and `EVALUATE`. `EVALUATE` is a switch-like statement with the added capability of evaluating multiple values and conditions. This can be used to implement decision tables. For example, the following might be used to control a CNC lathe:

```mw
EVALUATE TRUE ALSO desired-speed ALSO current-speed
    WHEN lid-closed ALSO min-speed THRU max-speed ALSO LESS THAN desired-speed
        PERFORM speed-up-machine
    WHEN lid-closed ALSO min-speed THRU max-speed ALSO GREATER THAN desired-speed
        PERFORM slow-down-machine
    WHEN lid-open ALSO ANY ALSO NOT ZERO
        PERFORM emergency-stop
    WHEN OTHER
        CONTINUE
END-EVALUATE
```

The `PERFORM` statement is used to define loops which are executed *until* a condition is true (not *while* true, which is more common in other languages). It is also used to call procedures or ranges of procedures (see the procedures section for more details). `CALL` and `INVOKE` call subprograms and methods, respectively. The name of the subprogram/method is contained in a string which may be a literal or a data item. Parameters can be passed by reference, by content (where a copy is passed by reference) or by value (but only if a prototype is available). `CANCEL` unloads subprograms from memory. `GO TO` causes the program to jump to a specified procedure.

The `GOBACK` statement is a return statement and the `STOP` statement stops the program. The `EXIT` statement has six different formats: it can be used as a return statement, a break statement, a continue statement, an end marker or to leave a procedure.

Exceptions are raised by a `RAISE` statement and caught with a handler, or **declarative**, defined in the `DECLARATIVES` portion of the procedure division. Declaratives are sections beginning with a `USE` statement which specify the errors to handle. Exceptions can be names or objects. `RESUME` is used in a declarative to jump to the statement after the one that raised the exception or to a procedure outside the `DECLARATIVES`. Unlike other languages, uncaught exceptions may not terminate the program and the program can proceed unaffected.

#### I/O

File I/O is handled by the self-describing `OPEN`, `CLOSE`, `READ`, and `WRITE` statements along with a further three: `REWRITE`, which updates a record; `START`, which selects subsequent records to access by finding a record with a certain key; and `UNLOCK`, which releases a lock on the last record accessed.

User interaction is done using `ACCEPT` and `DISPLAY`.

#### Data manipulation

The following verbs manipulate data:

- `INITIALIZE`, which sets data items to their default values.
- `MOVE`, which assigns values to data items ; *MOVE CORRESPONDING* assigns corresponding like-named fields.
- `SET`, which has 15 formats: it can modify indices, assign object references and alter table capacities, among other functions.
- `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, and `COMPUTE`, which handle arithmetic (with `COMPUTE` assigning the result of a formula to a variable).
- `ALLOCATE` and `FREE`, which handle dynamic memory.
- `VALIDATE`, which validates and distributes data as specified in an item's description in the data division.
- `STRING` and `UNSTRING`, which concatenate and split strings, respectively.
- `INSPECT`, which tallies or replaces instances of specified substrings within a string.
- `SEARCH`, which searches a table for the first entry satisfying a condition.

Files and tables are sorted using `SORT` and the `MERGE` verb merges and sorts files. The `RELEASE` verb provides records to sort and `RETURN` retrieves sorted records in order.

#### Scope termination

Some statements, such as `IF` and `READ`, may themselves contain statements. Such statements may be terminated in two ways: by a period (**implicit termination**), which terminates *all* unterminated statements contained, or by a scope terminator, which terminates the nearest matching open statement.

```mw
*> Terminator period ("implicit termination")
IF invalid-record
    IF no-more-records
        NEXT SENTENCE
    ELSE
        READ record-file
            AT END SET no-more-records TO TRUE.

*> Scope terminators ("explicit termination")
IF invalid-record
    IF no-more-records
        CONTINUE
    ELSE
        READ record-file
            AT END SET no-more-records TO TRUE
        END-READ
    END-IF
END-IF
```

Nested statements terminated with a period are a common source of bugs. For example, examine the following code:

```mw
IF x
    DISPLAY y.
    DISPLAY z.
```

Here, the intent is to display `y` and `z` if condition `x` is true. However, `z` will be displayed whatever the value of `x` because the `IF` statement is terminated by an erroneous period after `DISPLAY y`.

Another bug is a result of the dangling else problem, when two `IF` statements can associate with an `ELSE`.

```mw
IF x
    IF y
        DISPLAY a
ELSE
    DISPLAY b.
```

In the above fragment, the `ELSE` associates with the  `IF y`  statement instead of the  `IF x`  statement, causing a bug. Prior to the introduction of explicit scope terminators, preventing it would require  `ELSE NEXT SENTENCE`  to be placed after the inner `IF`.

#### Self-modifying code

The original (1960) COBOL specification supported the infamous  `ALTER X TO PROCEED TO Y`  statement, for which many compilers generated self-modifying code. `X` and `Y` are procedure labels, and the single  `GO TO`  statement in procedure `X` executed after such an `ALTER` statement means  `GO TO Y`  instead. Many compilers still support it, but it was deemed obsolete in the COBOL 1985 standard and deleted in 2002.

The `ALTER` statement was poorly regarded because it undermined "locality of context" and made a program's overall logic difficult to comprehend. As textbook author Daniel D. McCracken wrote in 1976, when "someone who has never seen the program before must become familiar with it as quickly as possible, sometimes under critical time pressure because the program has failed ... the sight of a GO TO statement in a paragraph by itself, signaling as it does the existence of an unknown number of ALTER statements at unknown locations throughout the program, strikes fear in the heart of the bravest programmer."

### Hello, world

A "Hello, World!" program in COBOL:

```mw
       IDENTIFICATION DIVISION.
       PROGRAM-ID. hello-world.
       PROCEDURE DIVISION.
           DISPLAY "Hello, world!"
           .
```

When the now famous "Hello, World!" program example in *The C Programming Language* was first published in 1978 a similar mainframe COBOL program sample would have been submitted through JCL, very likely using a punch card reader, and 80 column punch cards. The listing below, *with an empty `DATA DIVISION`*, was tested using Linux and the System/370 Hercules emulator running MVS 3.8J. The JCL, written in July 2015, is derived from the Hercules tutorials and samples hosted by Jay Moseley. In keeping with COBOL programming of that era, HELLO, WORLD is displayed in all capital letters.

```mw
//COBUCLG  JOB (001),'COBOL BASE TEST',                                
//             CLASS=A,MSGCLASS=A,MSGLEVEL=(1,1)                       
//BASETEST EXEC COBUCLG                                                
//COB.SYSIN DD *                                                       
 00000* VALIDATION OF BASE COBOL INSTALL                               
 01000 IDENTIFICATION DIVISION.                                        
 01100 PROGRAM-ID. 'HELLO'.                                            
 02000 ENVIRONMENT DIVISION.                                           
 02100 CONFIGURATION SECTION.                                          
 02110 SOURCE-COMPUTER.  GNULINUX.                                     
 02120 OBJECT-COMPUTER.  HERCULES.                                     
 02200 SPECIAL-NAMES.                                                  
 02210     CONSOLE IS CONSL.                                           
 03000 DATA DIVISION.                                                  
 04000 PROCEDURE DIVISION.                                             
 04100 00-MAIN.                                                        
 04110     DISPLAY 'HELLO, WORLD' UPON CONSL.                          
 04900     STOP RUN.                                                   
//LKED.SYSLIB DD DSNAME=SYS1.COBLIB,DISP=SHR                           
//            DD DSNAME=SYS1.LINKLIB,DISP=SHR                          
//GO.SYSPRINT DD SYSOUT=A                                              
//
```

After submitting the JCL, the MVS console displayed:

```mw
    19.52.48 JOB    3  $HASP100 COBUCLG  ON READER1     COBOL BASE TEST
    19.52.48 JOB    3  IEF677I WARNING MESSAGE(S) FOR JOB COBUCLG  ISSUED
    19.52.48 JOB    3  $HASP373 COBUCLG  STARTED - INIT 1 - CLASS A - SYS BSP1
    19.52.48 JOB    3  IEC130I SYSPUNCH DD STATEMENT MISSING
    19.52.48 JOB    3  IEC130I SYSLIB   DD STATEMENT MISSING
    19.52.48 JOB    3  IEC130I SYSPUNCH DD STATEMENT MISSING
    19.52.48 JOB    3  IEFACTRT - Stepname  Procstep  Program   Retcode
    19.52.48 JOB    3  COBUCLG    BASETEST  COB       IKFCBL00  RC= 0000
    19.52.48 JOB    3  COBUCLG    BASETEST  LKED      IEWL      RC= 0000
    19.52.48 JOB    3  +HELLO, WORLD
    19.52.48 JOB    3  COBUCLG    BASETEST  GO        PGM=*.DD  RC= 0000
    19.52.48 JOB    3  $HASP395 COBUCLG  ENDED
```

*Line 10 of the console listing above is highlighted for effect; the highlighting is not part of the actual console output*.

The associated compiler listing generated over four pages of technical detail and job run information, for the single line of output from the 14 lines of COBOL.
