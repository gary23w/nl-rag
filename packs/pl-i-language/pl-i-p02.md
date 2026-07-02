---
title: "PL/I (part 2/2)"
source: https://en.wikipedia.org/wiki/PL/I
domain: pl-i-language
license: CC-BY-SA-4.0
tags: pl i language, structured programming, mainframe computer, ibm system, punched card
fetched: 2026-07-02
part: 2/2
---

## Criticisms

### Implementation issues

Though the language is easy to learn and use, implementing a PL/I compiler is difficult and time-consuming. A language as large as PL/I needed subsets that most vendors could produce and most users master. This was not resolved until "ANSI G" was published. The compile time facilities, unique to PL/I, took added implementation effort and additional compiler passes. A PL/I compiler was two to four times as large as comparable Fortran or COBOL compilers, and also that much slower—supposedly offset by gains in programmer productivity. This was anticipated in IBM before the first compilers were written.

Some argue that PL/I is unusually hard to parse. The PL/I *keywords* are not reserved so programmers can use them as variable or procedure names in programs. Because the original PL/I(F) compiler attempts *auto-correction* when it encounters a keyword used in an incorrect context, it often assumes it is a variable name. This leads to "cascading diagnostics", a problem solved by later compilers.

The effort needed to produce good object code was perhaps underestimated during the initial design of the language. Program optimization (needed to compete with the excellent program optimization carried out by available Fortran compilers) is unusually complex owing to side effects and pervasive problems with aliasing of variables. Unpredictable modification can occur asynchronously in exception handlers, which may be provided by "ON statements" in (unseen) callers. Together, these make it difficult to reliably predict when a program's variables might be modified at runtime. In typical use, however, user-written error handlers (the ON-unit) often do not make assignments to variables. In spite of the aforementioned difficulties, IBM produced the PL/I Optimizing Compiler in 1971.

PL/I contains many rarely used features, such as multitasking support (an IBM extension to the language) which add cost and complexity to the compiler, and its co-processing facilities require a multi-programming environment with support for non-blocking multiple threads for processes by the operating system. Compiler writers were free to select whether to implement these features.

An undeclared variable is, by default, declared by first occurrence—thus misspelling might lead to unpredictable results. This "implicit declaration" is no different from FORTRAN programs. For PL/I(F), however, an attribute listing enables the programmer to detect any misspelled or undeclared variable.

### Programmer issues

Many programmers were slow to move from COBOL or Fortran due to a perceived complexity of the language and immaturity of the PL/I F compiler. Programmers were sharply divided into scientific programmers (who used Fortran) and business programmers (who used COBOL), with significant tension and even dislike between the groups. PL/I syntax borrowed from both COBOL and Fortran syntax. So instead of noticing features that would make their job easier, Fortran programmers of the time noticed COBOL syntax and had the opinion that it was a business language, while COBOL programmers noticed Fortran syntax and looked upon it as a scientific language.

Both COBOL and Fortran programmers viewed it as a "bigger" version of their own language, and both were somewhat intimidated by the language and disinclined to adopt it. Another factor was *pseudo*-similarities to COBOL, Fortran, and ALGOL. These were PL/I elements that looked similar to one of those languages, but worked differently in PL/I. Such frustrations left many experienced programmers with a jaundiced view of PL/I, and often an active dislike for the language. An early UNIX fortune file contained the following tongue-in-cheek description of the language:

> Speaking as someone who has delved into the intricacies of PL/I, I am sure that only Real Men could have written such a machine-hogging, cycle-grabbing, all-encompassing monster. Allocate an array and free the middle third? Sure! Why not? Multiply a character string times a bit string and assign the result to a float decimal? Go ahead! Free a controlled variable procedure parameter and reallocate it before passing it back? Overlay three different types of variable on the same memory location? Anything you say! Write a recursive macro? Well, no, but Real Men use rescan. How could a language so obviously designed and written by Real Men not be intended for Real Man use?

On the positive side, full support for pointers to all data types (including pointers to structures), recursion, multitasking, string handling, and extensive built-in functions meant PL/I was indeed quite a leap forward compared to the programming languages of its time. However, these were not enough to persuade a majority of programmers or shops to switch to PL/I.

The PL/I F compiler's compile time preprocessor was unusual (outside the Lisp world) in using its target language's syntax and semantics (*e.g.* as compared to the C preprocessor's "#" directives).


## Special topics in PL/I

### Storage classes

PL/I provides several 'storage classes' to indicate how the lifetime of variables' storage is to be managed – `STATIC`, `AUTOMATIC`, `CONTROLLED`, and `BASED`, and `AREA`.

`STATIC` data is allocated and initialized at load-time, as is done in COBOL "working-storage" and early Fortran. This is the default for `EXTERNAL` variables (similar to C “extern” or Fortran “named common"),

`AUTOMATIC` is PL/I's default storage class for `INTERNAL` variables, similar to that of other block-structured languages influenced by ALGOL, like the "auto" storage class in the C language, the default storage allocation in Pascal, and "local-storage" in IBM COBOL. Storage for `AUTOMATIC` variables is allocated upon entry into the procedure, `BEGIN`-block, or `ON`-unit in which they are declared. The compiler and runtime system allocate memory for a stack frame to contain them and other housekeeping information. If a variable is declared with an `INITIAL`-attribute, code to set it to an initial value is executed at this time. Care is required to manage the use of initialization properly. Large amounts of code can be executed to initialize variables every time a scope is entered, especially if the variable is an array or structure. Storage for `AUTOMATIC` variables is freed at block exit.

`STATIC`, `CONTROLLED`, or `BASED` variables are used to retain variables' contents between invocations of a procedure or block.

`CONTROLLED` storage is managed using a stack, but the pushing and popping of allocations on the stack is managed by the programmer, using `ALLOCATE` and `FREE` statements.

Storage for `BASED` variables is also managed using `ALLOCATE`/`FREE`, but instead of a stack these allocations have independent lifetimes and are addressed through `OFFSET` or `POINTER` variables. `BASED` variables can also be used to address arbitrary storage areas by setting the associated `POINTER` variable, for example following a linked list.

The `AREA` attribute is used to declare programmer-defined heaps. Data can be allocated and freed within a specific area, and the area can be deleted, read, and written as a unit.

### Storage type sharing

There are several ways of accessing allocated storage through different data declarations. Some of these are well defined and safe, some can be used safely with careful programming, and some are inherently unsafe or machine dependent.

Passing a variable as an argument to a parameter by reference allows the argument's allocated storage to be referenced using the parameter. The DEFINED attribute (e.g., `DCL A(10,10), B(2:9,2:9) DEFINED A`) allows part or all of a variable's storage to be used with a different, but consistent, declaration. The language definition includes a CELL attribute (later renamed UNION) to allow different definitions of data to share the same storage. This was not supported by many early IBM compilers. These usages are safe and machine independent.

Record I/O and list processing produce situations where the programmer needs to fit a declaration to the storage of the next record or item, before knowing what type of data structure it has. Based variables and pointers are key to such programs. The data structures must be designed appropriately, typically using fields in a data structure to encode information about its type and size. The fields can be held in the preceding structure or, with some constraints, in the current one. Where the encoding is in the preceding structure, the program needs to allocate a based variable with a declaration that matches the current item (using expressions for extents where needed). Where the type and size information are to be kept in the current structure ("self defining structures") the type-defining fields must be ahead of the type dependent items and in the same place in every version of the data structure. The REFER-option is used for self-defining extents (e.g., string lengths as in `DCL 1 A BASED, 2 N BINARY, 2 B CHAR(LENGTH REFER A.N.)`, etc  – where LENGTH is used to allocate instances of the data structure. For self-defining structures, any typing and REFERred fields are placed ahead of the "real" data. If the records in a data set, or the items in a list of data structures, are organised this way they can be handled safely in a machine independent way.

PL/I implementations do not (except for the PL/I Checkout compiler) keep track of the data structure used when storage is first allocated. Any BASED declaration can be used with a pointer into the storage to access the storage – inherently unsafe and machine dependent. However, this usage has become important for "pointer arithmetic" (typically adding a certain amount to a known address). This has been a contentious subject in computer science. In addition to the problem of wild references and buffer overruns, issues arise due to the alignment and length for data types used with particular machines and compilers. Many cases where pointer arithmetic might be needed involve finding a pointer to an element inside a larger data structure. The ADDR function computes such pointers, safely and machine independently.

Pointer arithmetic may be accomplished by aliasing a binary variable with a pointer as in

```
DCL P POINTER, N FIXED BINARY(31) BASED(ADDR(P));
N=N+255;
```

It relies on pointers being the same length as `FIXED BINARY(31)` integers and aligned on the same boundaries.

With the prevalence of C and its free and easy attitude to pointer arithmetic, recent IBM PL/I compilers allow pointers to be used with the addition and subtraction operators to giving the simplest syntax (but compiler options can disallow these practices where safety and machine independence are paramount).

### ON-units and exception handling

When PL/I was designed, programs only ran in batch mode, with no possible intervention from the programmer at a terminal. An exceptional condition such as division by zero would abort the program yielding only a hexadecimal core dump. PL/I exception handling, via ON-units, allowed the program to stay in control in the face of hardware or operating system exceptions and to recover debugging information before closing down more gracefully. As a program became properly debugged, most of the exception handling could be removed or disabled: this level of control became less important when conversational execution became commonplace.

Computational exception handling is enabled and disabled by condition prefixes on statements, blocks (including ON-units) and procedures. – e.g., `(SIZE, NOSUBSCRIPTRANGE): A(I)=B(I)*C;`. Operating system exceptions for Input/Output and storage management are always enabled.

The ON-unit is a single statement or BEGIN-block introduced by an ON-statement. Executing the ON statement enables the condition specified, e.g., `ON ZERODIVIDE ON`-unit. When the exception for this condition occurs and the condition is enabled, the ON-unit for the condition is executed. ON-units are inherited down the call chain. When a block, procedure or ON-unit is activated, the ON-units established by the invoking activation are inherited by the new activation. They may be over-ridden by another ON-statement and can be reestablished by the REVERT-statement. The exception can be simulated using the SIGNAL-statement – e.g., to help debug the exception handlers. The dynamic inheritance principle for ON-units allows a routine to handle the exceptions occurring within the subroutines it uses.

If no ON-unit is in effect when a condition is raised a standard system action is taken (often this is to raise the ERROR condition). The system action can be reestablished using the SYSTEM option of the ON-statement. With some conditions it is possible to complete executing an ON-unit and return to the point of interrupt (e.g., the STRINGRANGE, UNDERFLOW, CONVERSION, OVERFLOW, AREA, and FILE conditions) and resume normal execution. With other conditions such as `(SUBSCRIPTRANGE)`, the ERROR condition is raised when this is attempted. An ON-unit may be terminated with a `GO TO` preventing a return to the point of interrupt, but permitting the program to continue execution elsewhere as determined by the programmer.

An ON-unit needs to be designed to deal with exceptions that occur in the ON-unit itself. The `ON ERROR SYSTEM;` statement allows a nested error trap; if an error occurs within an ON-unit, control might pass to the operating system where a system dump might be produced, or, for some computational conditions, continue execution (as mentioned above).

The PL/I RECORD I/O statements have relatively simple syntax as they do not offer options for the many situations from end-of-file to record transmission errors that can occur when a record is read or written. Instead, these complexities are handled in the ON-units for the various file conditions. The same approach was adopted for AREA sub-allocation and the AREA condition.

The existence of exception handling ON-units can have an effect on optimization, because variables can be inspected or altered in ON-units. Values of variables that might otherwise be kept in registers between statements, may need to be returned to storage between statements. This is discussed in the section on Implementation Issues above.

### GO TO with a non-fixed target

PL/I has counterparts for COBOL and FORTRAN's specialized GO TO statements.

Syntax for both COBOL and FORTRAN exist for coding two special two types of GO TO, each of which has a target that is not always the same.

- ALTER (COBOL), ASSIGN (FORTRAN):
  - `ALTER paragraph_name_xxx TO PROCEED TO para_name_zzz` (“altered go to”). There are other/helpful restrictions on these, especially "in programs ... RECURSIVE attribute, in methods, or .. THREAD option."
  - `ASSIGN 1860 TO IGOTTAGO` (“assigned go to”) `GO TO IGOTTAGO` One enhancement, which adds built-in documentation, is `GO TO IGOTTAGO (1860, 1914, 1939)` (which restricts the variable's value to "one of the labels in the list.")
- GO TO ... based on a variable's subscript-like value.
  - `GO TO (1914, 1939, 2140), MYCHOICE` (“computed go to”)
  - `GO TO para_One para_Two para_Three DEPENDING ON IDECIDE` (“go to depending on”).

PL/I has statement label variables (with the LABEL attribute), which can store the value of a statement label, and later be used in a GOTO statement.

```
LABL1: ....
.
.
LABL2: ...
.
.
.
MY_DEST = LABL1;
.
GO TO MY_DEST;
```

The programmer can also create an array of static label constants by subscripting the statement labels.

```
GO TO HERE(LUCKY_NUMBER); /* minus 1, zero, or ... */
```

```
HERE(-1): PUT LIST ("I O U"); GO TO Lottery;
HERE(0): PUT LIST ("No Cash"); GO TO Lottery;
HERE(1): PUT LIST ("Dollar Bill"); GO TO Lottery;
HERE(2): PUT LIST ("TWO DOLLARS"); GO TO Lottery;
```

Statement label variables can be passed to called procedures, and used to return to a different statement in the calling routine.


## Sample programs

### Hello world program

```mw
Hello2: proc options(main);
     put list ('Hello, World!');
end Hello2;
```

```mw
/* Read in a line, which contains a string,
/* and then print every subsequent line that contains that string. */

find_strings: procedure options (main);
   declare pattern character (100) varying;
   declare line character (100) varying;
   declare line_no fixed binary;

   on endfile (sysin) stop;

   get edit (pattern) (L);
   line_no = 1;
   do forever;
      get edit (line) (L);
      if index(line, pattern) > 0 then
         put skip list (line_no, line);
      line_no = line_no + 1;
   end;

end find_strings;
```
