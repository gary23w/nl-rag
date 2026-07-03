---
title: "Fortran (part 1/2)"
source: https://en.wikipedia.org/wiki/Fortran
domain: fortran
license: CC-BY-SA-4.0
tags: fortran
fetched: 2026-07-03
part: 1/2
---

# Fortran

Checked


## Page version status

This is an accepted version of this page

This is the

latest accepted revision

,

reviewed

on

14 June 2026

.

**Fortran** (/ˈfɔːrtræn/; formerly **FORTRAN**) is a third-generation, compiled, imperative programming language designed for numeric computation and scientific computing.

Fortran was originally developed by IBM with a reference manual being released in 1956; however, the first compilers only began to produce accurate code two years later. Fortran computer programs have been written to support scientific and engineering applications, such as numerical weather prediction, finite element analysis, computational fluid dynamics, plasma physics, geophysics, computational physics, crystallography and computational chemistry. It is a popular language for high-performance computing and is used for programs that benchmark and rank the world's fastest supercomputers.

Fortran has evolved through numerous versions and dialects. The two most important early versions were FORTRAN II and FORTRAN IV. In 1966, the American National Standards Institute (ANSI) developed a standard for Fortran to limit proliferation of compilers using slightly different syntax. Successive versions have added support for a character data type, structured programming (Fortran 77), array programming, modular programming, generic programming (Fortran 90), parallel computing (Fortran 95), object-oriented programming (Fortran 2003), and concurrent programming (Fortran 2008).


## Naming

The first manual for FORTRAN describes it as a *Formula Translating System*, and printed the name with small caps, Fortran. Other sources suggest the name stands for *Formula Translator*, or, most commonly, *Formula Translation*.

Early IBM computers did not support lowercase letters, and the names of versions of the language through FORTRAN 77 were usually spelled in all-uppercase. FORTRAN 77 was the last version in which the Fortran character set included only uppercase letters.

The Fortran 90 standard changed the language name from "FORTRAN" with all-caps to "Fortran" with initial caps.


## Origins

In late 1953, John W. Backus submitted a proposal to his superiors at IBM to develop a more practical alternative to assembly language for programming their IBM 704 mainframe computer. Backus' historic FORTRAN team consisted of programmers Richard Goldberg, Sheldon F. Best, Harlan Herrick, Peter Sheridan, Roy Nutt, Robert Nelson, Irving Ziller, Harold Stern, Lois Haibt, and David Sayre. Its concepts included easier entry of equations into a computer, an idea developed by J. Halcombe Laning and demonstrated in the Laning and Zierler system of 1952. As with other developments in the early days of computing, there were several parallel, independent efforts along these lines, with other instances of proto-Fortran languages including the A-0 System for the UNIVAC I and its follow-on MATH-MATIC, under the direction of Grace Murray Hopper; the high-level language work developed by Heinz Rutishauser for the Zuse 4 computer; and the Mark 1 Autocode work done by R. A. Brooker for the Ferranti Mercury.

A draft specification for *The IBM Mathematical Formula Translating System* was completed by November 1954. The first manual for FORTRAN appeared in October 1956, with the first FORTRAN compiler delivered in April 1957. Fortran produced efficient enough code for assembly language programmers to accept a high-level programming language replacement.

John Backus said during a 1979 interview with *Think*, the IBM employee magazine, "Much of my work has come from being lazy. I didn't like writing programs, and so, when I was working on the IBM 701, writing programs for computing missile trajectories, I started work on a programming system to make it easier to write programs."

The language was widely adopted by scientists for writing numerically intensive programs, which encouraged compiler writers to produce compilers that could generate faster and more efficient code. The inclusion of a complex number data type in the language made Fortran especially suited to technical applications such as electrical engineering.

By 1960, versions of FORTRAN were available for the IBM 709, 650, 1620, and 7090 computers. Significantly, the increasing popularity of FORTRAN spurred competing computer manufacturers to provide FORTRAN compilers for their machines, so that by 1963 over 40 FORTRAN compilers existed. So pervasive was the language within the computing industry that by that time, over 220,000 Fortran manuals of all kinds had been distributed.

FORTRAN was provided for the IBM 1401 computer by an innovative 63-phase compiler that ran entirely in its core memory of only 8000 (six-bit) characters. The compiler could be run from tape, or from a 2200-card deck; it used no further tape or disk storage. It kept the program in memory and loaded overlays that gradually transformed it, in place, into executable form, as described by Haines. This article was reprinted, edited, in both editions of *Anatomy of a Compiler* and in the IBM manual "Fortran Specifications and Operating Procedures, IBM 1401". The executable form was not entirely machine language; rather, floating-point arithmetic, sub-scripting, input/output, and function references were interpreted, preceding UCSD Pascal P-code by two decades. GOTRAN, a simplified, interpreted version of FORTRAN I (with only 12 types of statements not 32) for "load and go" operation was available (at least for the early IBM 1620 computer). Modern Fortran, and almost all later versions, are fully compiled, as done for other high-performance languages.

The development of Fortran paralleled the early evolution of compiler technology, and many advances in the theory and design of compilers were specifically motivated by the need to generate efficient code for Fortran programs. Indeed, the Fortran compiler was one of the most complicated programs of any kind in existence at the time, and it was used by IBM's Product Test group in Poughkeepsie, New York, as part of acceptance testing for newly built computers.

### FORTRAN

The initial release of FORTRAN for the IBM 704 contained 32 types of statements, including:

- `DIMENSION` and `EQUIVALENCE` statements
- Assignment statements
- Three-way *arithmetic* `IF` statement (since deprecated), which passed control to one of three locations in the program depending on whether the result of the arithmetic expression was negative, zero, or positive
- Control statements for checking exceptions (`IF ACCUMULATOR OVERFLOW`, `IF QUOTIENT OVERFLOW`, and `IF DIVIDE CHECK`); and control statements for manipulating sense switches and sense lights (`IF (SENSE SWITCH)`, `IF (SENSE LIGHT)`, and `SENSE LIGHT`)
- `GO TO`, computed `GO TO`, `ASSIGN`, and assigned `GO TO`
- `DO` loops
- Formatted I/O: `FORMAT`, `READ`, `READ INPUT TAPE`, `WRITE OUTPUT TAPE`, `PRINT`, and `PUNCH`
- Unformatted I/O: `READ TAPE`, `READ DRUM`, `WRITE TAPE`, and `WRITE DRUM`
- Other I/O: `END FILE`, `REWIND`, and `BACKSPACE`
- `PAUSE`, `STOP`, and `CONTINUE`
- `FREQUENCY` statement (for providing optimization hints to the compiler).

The arithmetic `IF` statement was reminiscent of (but not readily implementable by) a three-way comparison instruction (CAS—Compare Accumulator with Storage) available on the 704. The statement provided the only way to compare numbers—by testing their difference, with an attendant risk of overflow. This deficiency was later overcome by "logical" facilities introduced in FORTRAN IV.

The `FREQUENCY` statement was used originally (and optionally) to give branch probabilities for the three branch cases of the arithmetic `IF` statement. It could also be used to suggest how many iterations a `DO` loop might run. The first FORTRAN compiler used this weighting to perform *at compile time* a Monte Carlo simulation of the generated code, the results of which were used to optimize the placement of basic blocks in memory—a very sophisticated optimization for its time. The Monte Carlo technique is documented in Backus et al.'s paper on this original implementation, *The FORTRAN Automatic Coding System*:

> The fundamental unit of program is the basic block; a basic block is a stretch of program which has one entry point and one exit point. The purpose of section 4 is to prepare for section 5 a table of predecessors (PRED table) which enumerates the basic blocks and lists for every basic block each of the basic blocks which can be its immediate predecessor in flow, together with the absolute frequency of each such basic block link. This table is obtained by running the program once in Monte-Carlo fashion, in which the outcome of conditional transfers arising out of IF-type statements and computed GO TO's is determined by a random number generator suitably weighted according to whatever FREQUENCY statements have been provided.

The first FORTRAN compiler reported diagnostic information by halting the program when an error was found and outputting an error code on its console. That code could be looked up by the programmer in an error messages table in the operator's manual, providing them with a brief description of the problem. Later, an error-handling subroutine to handle user errors such as division by zero, developed by NASA, was incorporated, informing users of which line of code contained the error.

#### Fixed layout and punched cards

Before the development of disk files, text editors and terminals, programs were most often entered on a keypunch keyboard onto 80-column punched cards, one line to a card. The resulting deck of cards would be fed into a card reader to be compiled. Punched card codes included no lower-case letters or many special characters, and special versions of the IBM 026 keypunch were offered that would correctly print the re-purposed special characters used in FORTRAN.

Reflecting punched card input practice, Fortran programs were originally written in a fixed-column format. A letter "C" in column 1 caused the entire card to be treated as a comment and ignored by the compiler. Otherwise, the columns of the card were divided into four fields:

- 1 to 5 were the label field: a sequence of digits here was taken as a label for use in DO or control statements such as GO TO and IF, or to identify a FORMAT statement referred to in a WRITE or READ statement. Leading zeros are ignored and 0 is not a valid label number.
- 6 was a continuation field: a character other than a blank or a zero here caused the card to be taken as a continuation of the statement on the prior card. The continuation cards were usually numbered 1, 2, *etc.* and the starting card might therefore have zero in its continuation column—which is not a continuation of its preceding card.
- 7 to 72 contained the statement field.
- 73 to 80 were ignored (the card reader for the IBM 704, the computer on which Fortran was developed, could only read 72 columns, placing them into twenty-four 36-bit words).

Columns 73 to 80 could therefore be used for identification information, such as punching a sequence number or text, which could be used to re-order cards if a stack of cards was dropped; though in practice this was reserved for stable, production programs. An IBM 519 could be used to copy a program deck and add sequence numbers. Some early compilers, e.g., the IBM 650's, had additional restrictions due to limitations on their card readers. Keypunches could be programmed to tab to column 7 and skip out after column 72. Later compilers relaxed most fixed-format restrictions, and the requirement was eliminated in the Fortran 90 standard.

Within the statement field, whitespace characters (blanks) were ignored outside a text literal. This allowed omitting spaces between tokens for brevity or including spaces within identifiers for clarity. For example, `AVG OF X` was a valid identifier, equivalent to `AVGOFX`, and `101010DO101I=1,101` was a valid statement, equivalent to `10101 DO 101 I = 1, 101` because the zero in column 6 is treated as if it were a space, while `101010DO101I=1.101` was instead `10101 DO101I = 1.101`, the assignment of 1.101 to a variable called `DO101I`. Note the slight visual difference between a comma and a period.

Hollerith strings, originally allowed only in FORMAT and DATA statements, were prefixed by a character count and the letter H (e.g., `26HTHIS IS ALPHANUMERIC DATA.`), allowing blanks to be retained within the character string. Miscounts were a problem.


## Evolution

| Year | Informal name | Official Standard |
|---|---|---|
| 1957 | FORTRAN | —N/a |
| 1958 | FORTRAN II | —N/a |
| 1958 | FORTRAN III | —N/a |
| 1961 | FORTRAN IV | —N/a |
| 1966 | FORTRAN 66 | ANSI X3.9-1966 |
| 1978 | FORTRAN 77 | ANSI X3.9-1978 ISO 1539:1980 |
| 1991 | Fortran 90 | ANSI X3.198-1992 ISO/IEC 1539:1991 |
| 1997 | Fortran 95 | ISO/IEC 1539-1:1997 |
| 2004 | Fortran 2003 | ISO/IEC 1539-1:2004 |
| 2010 | Fortran 2008 | ISO/IEC 1539-1:2010 |
| 2018 | Fortran 2018 | ISO/IEC 1539-1:2018 |
| 2023 | Fortran 2023 | ISO/IEC 1539-1:2023 |

### FORTRAN II

IBM's *FORTRAN II* appeared in 1958. The main enhancement was to support procedural programming by allowing user-written subroutines and functions which returned values with parameters passed by reference. The COMMON statement provided a way for subroutines to access common (or global) variables. Six new statements were introduced:

- `SUBROUTINE`, `FUNCTION`, and `END`
- `CALL` and `RETURN`
- `COMMON`

In the view of computing pioneer Robert Bemer, the addition of separately compiled subroutines to the language was "a development equivalent in importance to the original FORTRAN."

Over the next few years, FORTRAN II added support for the `DOUBLE PRECISION` and `COMPLEX` data types.

Early FORTRAN compilers supported no recursion in subroutines. Early computer architectures supported no concept of a stack, and when they did directly support subroutine calls, the return location was often stored in one fixed location adjacent to the subroutine code (e.g. the IBM 1130) or a specific machine register (IBM 360 *et seq*), which only allows recursion if a stack is maintained by software and the return address is stored on the stack before the call is made and restored after the call returns. The lack of recursion was a significant detriment to the language being used in conjunction with certain algorithms and applications, and indeed limited how programmers could think about such things. Although not specified in FORTRAN 77, many F77 compilers supported recursion as an option, and the Burroughs mainframes, designed with recursion built-in, did so by default. It became a standard in Fortran 90 via the new keyword RECURSIVE.

#### Simple FORTRAN II program

This program, for Heron's formula, reads data on a tape reel containing three 5-digit integers A, B, and C as input. There are no "type" declarations available: variables whose name starts with I, J, K, L, M, or N are "fixed-point" (i.e. integers), otherwise floating-point. Since integers are to be processed in this example, the names of the variables start with the letter "I". The name of a variable must start with a letter and can continue with both letters and digits, up to a limit of six characters in FORTRAN II. If A, B, and C cannot represent the sides of a triangle in plane geometry, then the program's execution will end with an error code of "STOP 1". Otherwise, an output line will be printed showing the input values for A, B, and C, followed by the computed AREA of the triangle as a floating-point number occupying ten spaces along the line of output and showing 2 digits after the decimal point, the .2 in F10.2 of the FORMAT statement with label 601.

```mw
C AREA OF A TRIANGLE WITH A STANDARD SQUARE ROOT FUNCTION
C INPUT - TAPE READER UNIT 5, INTEGER INPUT
C OUTPUT - LINE PRINTER UNIT 6, REAL OUTPUT
C INPUT ERROR DISPLAY ERROR OUTPUT CODE 1 IN JOB CONTROL LISTING
      READ INPUT TAPE 5, 501, IA, IB, IC
  501 FORMAT (3I5)
C IA, IB, AND IC MAY NOT BE NEGATIVE OR ZERO
C FURTHERMORE, THE SUM OF TWO SIDES OF A TRIANGLE
C MUST BE GREATER THAN THE THIRD SIDE, SO WE CHECK FOR THAT, TOO
      IF (IA) 777, 777, 701
  701 IF (IB) 777, 777, 702
  702 IF (IC) 777, 777, 703
  703 IF (IA+IB-IC) 777, 777, 704
  704 IF (IA+IC-IB) 777, 777, 705
  705 IF (IB+IC-IA) 777, 777, 799
  777 STOP 1
C USING HERON'S FORMULA WE CALCULATE THE
C AREA OF THE TRIANGLE
  799 S = FLOATF (IA + IB + IC) / 2.0
      AREA = SQRTF( S * (S - FLOATF(IA)) * (S - FLOATF(IB)) *
     +     (S - FLOATF(IC)))
      WRITE OUTPUT TAPE 6, 601, IA, IB, IC, AREA
  601 FORMAT (4H A= ,I5,5H  B= ,I5,5H  C= ,I5,8H  AREA= ,F10.2,
     +        13H SQUARE UNITS)
      STOP
      END
```

### FORTRAN III

IBM also developed a *FORTRAN III* in 1958 that allowed for inline assembly code among other features; however, this version was never released as a product. Like the 704 FORTRAN and FORTRAN II, FORTRAN III included machine-dependent features that made code written in it unportable from machine to machine, as well as Boolean expression support. Early versions of FORTRAN provided by other vendors suffered from the same disadvantage.

### FORTRAN IV

IBM began development of **FORTRAN IV** in 1961 as a result of customer demands. FORTRAN IV removed the machine-dependent features of FORTRAN II (such as `READ INPUT TAPE`), while adding new features such as a `LOGICAL` data type, logical Boolean expressions, and the *logical IF statement* as an alternative to the *arithmetic IF statement.* Type declarations were added, along with an `IMPLICIT` statement to override earlier conventions that variables are `INTEGER` if their name begins with `I`, `J`, `K`, `L`, `M`, or `N`; and `REAL` otherwise.

FORTRAN IV was eventually released in 1962, first for the IBM 7030 ("Stretch") computer, followed by versions for the IBM 7090/7094 in 1963 and later for the IBM 1401 in 1966.

By 1965, FORTRAN IV was supposed to be compliant with the *standard* being developed by the American Standards Association X3.4.3 FORTRAN Working Group.

Between 1966 and 1968, IBM offered several FORTRAN IV compilers for its System/360, each named by letters that indicated the minimum amount of memory the compiler needed to run. The letters (F, G, H) matched the codes used with System/360 model numbers to indicate memory size, each letter increment being a factor of two larger:

- 1966 : FORTRAN IV F for DOS/360 (64K bytes)
- 1966 : FORTRAN IV G for OS/360 (128K bytes)
- 1968 : FORTRAN IV H for OS/360 (256K bytes)

In particular, the FORTRAN H compiler played an important role in the development of certain kinds of optimization approaches, such as allocating a specific set of registers to hold the values of variables while in a loop. Overall, the compiler had three levels of possible optimization, as Fortran compiler developers had learned early on that the ability to turn off optimization was a necessity, since it drove up compilation times considerability for program runs that often were not going to work anyway. Even with the larger amount of main memory available to it, the FORTRAN H compiler was still organized via a number of overlays. Overall, Fortran compilers were a significant source of revenue for IBM, with sales of some $300 million in 1966 (equivalent to $2,977 million in 2025).

Digital Equipment Corporation maintained DECSYSTEM-10 Fortran IV (F40) for PDP-10 from 1967 to 1975. Compilers were also available for the UNIVAC 1100 series and the Control Data 6000 series and 7000 series systems.

In the FORTRAN IV programming environment of the era, except for that used on Control Data Corporation (CDC) systems, only one instruction was placed per line. The CDC version allowed for multiple instructions per line if separated by a $ (dollar) character. The FORTRAN sheet was divided into four fields, as described above.

Two compilers of the time, IBM "G" and UNIVAC, allowed comments to be written on the same line as instructions, separated by a special character: "master space": V (perforations 7 and 8) for UNIVAC and perforations 12/11/0/7/8/9 (hexadecimal FF) for IBM. These comments were not to be inserted in the middle of continuation cards.

### FORTRAN 66

Perhaps the most significant development in the early history of FORTRAN was the decision by the *American Standards Association* (now American National Standards Institute (ANSI)) to form a committee sponsored by the Business Equipment Manufacturers Association (BEMA) to develop an *American Standard Fortran*. The resulting two standards, approved in March 1966, defined two languages, *FORTRAN* (based on FORTRAN IV, which had served as a de facto standard), and *Basic FORTRAN* (based on FORTRAN II, but stripped of its machine-dependent features). The FORTRAN defined by the first standard, officially denoted X3.9-1966, became known as *FORTRAN 66* (although many continued to term it FORTRAN IV, the language on which the standard was largely based). FORTRAN 66 effectively became the first industry-standard version of FORTRAN. FORTRAN 66 included:

- Main program, `SUBROUTINE`, `FUNCTION`, and `BLOCK DATA` program units
- `INTEGER`, `REAL`, `DOUBLE PRECISION`, `COMPLEX`, and `LOGICAL` data types
- `COMMON`, `DIMENSION`, and `EQUIVALENCE` statements
- `DATA` statement for specifying initial values
- Intrinsic and `EXTERNAL` (e.g., library) functions
- Assignment statement
- `GO TO`, computed `GO TO`, assigned `GO TO`, and `ASSIGN` statements
- Logical `IF` and arithmetic (three-way) `IF` statements
- `DO` loop statement
- `READ`, `WRITE`, `BACKSPACE`, `REWIND`, and `ENDFILE` statements for sequential I/O
- `FORMAT` statement and assigned format
- `CALL`, `RETURN`, `PAUSE`, and `STOP` statements
- Hollerith constants in `DATA` and `FORMAT` statements, and as arguments to procedures
- Identifiers of up to six characters in length
- Comment lines
- `END` line

The above Fortran II version of the Heron program needs several modifications to compile as a Fortran 66 program. Modifications include using the more machine independent versions of the `READ` and `WRITE` statements, and removal of the unneeded `FLOATF` type conversion functions. Though not required, the arithmetic `IF` statements can be re-written to use logical `IF` statements and expressions in a more structured fashion.

```mw
C AREA OF A TRIANGLE WITH A STANDARD SQUARE ROOT FUNCTION
C INPUT - TAPE READER UNIT 5, INTEGER INPUT
C OUTPUT - LINE PRINTER UNIT 6, REAL OUTPUT
C INPUT ERROR DISPLAY ERROR OUTPUT CODE 1 IN JOB CONTROL LISTING
      READ (5, 501) IA, IB, IC
  501 FORMAT (3I5)
C
C IA, IB, AND IC MAY NOT BE NEGATIVE OR ZERO
C FURTHERMORE, THE SUM OF TWO SIDES OF A TRIANGLE
C MUST BE GREATER THAN THE THIRD SIDE, SO WE CHECK FOR THAT, TOO
      IF (IA .GT. 0 .AND. IB .GT. 0 .AND. IC .GT. 0) GOTO 10
        WRITE (6, 602)
  602   FORMAT (42H IA, IB, AND IC MUST BE GREATER THAN ZERO.)
        STOP 1
   10 CONTINUE
C
      IF (IA+IB-IC .GT. 0
     +    .AND. IA+IC-IB .GT. 0
     +    .AND. IB+IC-IA .GT. 0) GOTO 20
        WRITE (6, 603)
  603   FORMAT (50H SUM OF TWO SIDES MUST BE GREATER THAN THIRD SIDE.)
        STOP 1
   20 CONTINUE
C
C USING HERON'S FORMULA WE CALCULATE THE
C AREA OF THE TRIANGLE
      S = (IA + IB + IC) / 2.0
      AREA = SQRT ( S * (S - IA) * (S - IB) * (S - IC))
      WRITE (6, 601) IA, IB, IC, AREA
  601 FORMAT (4H A= ,I5,5H  B= ,I5,5H  C= ,I5,8H  AREA= ,F10.2,
     +        13H SQUARE UNITS)
      STOP
      END
```

Although ill-suited for most military-related applications, Fortran was nonetheless one of only a few high-level languages approved for use by the U.S. Department of Defense in the 1970s. The intent was that these would all be replaced by the Defense Department-sponsored Ada programming language, but that did not happen, and the rationale for the Ada 9X revision of the language indicated that since much mathematical software still existed and was still being written in Fortran, there needed to be support in Ada for explicitly interfacing to Fortran routines.

### FORTRAN 77

After the release of the FORTRAN 66 standard, compiler vendors introduced several extensions to *Standard Fortran*, prompting ANSI committee X3J3 in 1969 to begin work on revising the 1966 standard, under sponsorship of CBEMA, the Computer Business Equipment Manufacturers Association (formerly BEMA). Final drafts of this revised standard circulated in 1977, leading to formal approval of the new FORTRAN standard in April 1978. The new standard, called *FORTRAN 77* and officially denoted X3.9-1978, added a number of significant features to address many of the shortcomings of FORTRAN 66:

- Block `IF` and `END IF` statements, with optional `ELSE IF` and `ELSE` clauses, to provide improved language support for structured programming
- `DO` loop extensions, including parameter expressions, negative increments, and zero trip counts
- `OPEN`, `CLOSE`, and `INQUIRE` statements for improved I/O capability
- Direct-access file I/O
- `CHARACTER` data type, replacing Hollerith strings with vastly expanded facilities for character input and output and processing of character-based data
- `PARAMETER` statement for specifying constants
- `SAVE` statement for persistent local variables
- Generic names for intrinsic functions (e.g. `SQRT` also accepts arguments of other types, such as `COMPLEX` or `REAL*16`).
- A set of intrinsics (`LGE`, `LGT`, `LLE`, `LLT`) for *lexical* comparison of strings, based upon the ASCII collating sequence. (These ASCII functions were demanded by the U.S. Department of Defense, in their conditional approval vote.)
- A maximum of seven dimensions in arrays, rather than three. Allowed subscript expressions were also generalized.

In this revision of the standard, a number of features were removed or altered in a manner that might invalidate formerly standard-conforming programs. (Removal was the only allowable alternative to X3J3 at that time, since the concept of "deprecation" was not yet available for ANSI standards.) While most of the 24 items in the conflict list (see Appendix A2 of X3.9-1978) addressed loopholes or pathological cases permitted by the prior standard but rarely used, a small number of specific capabilities were deliberately removed, such as:

- Hollerith constants and Hollerith data, such as `GREET = 12HHELLO THERE!`
- Reading into an H edit (Hollerith field) descriptor in a FORMAT specification
- Overindexing of array bounds by subscripts DIMENSION A(10,5) Y = A(11,1)
- Transfer of control out of and back into the range of a DO loop (also known as "Extended Range")

A Fortran 77 version of the Heron program requires no modifications to the Fortran 66 version. However this example demonstrates additional cleanup of the I/O statements, including using list-directed I/O, and replacing the Hollerith edit descriptors in the `FORMAT` statements with quoted strings. It also uses structured `IF` and `END IF` statements, rather than `GOTO`/`CONTINUE`.

```mw
      PROGRAM HERON
C AREA OF A TRIANGLE WITH A STANDARD SQUARE ROOT FUNCTION
C INPUT - DEFAULT STANDARD INPUT UNIT, INTEGER INPUT
C OUTPUT - DEFAULT STANDARD OUTPUT UNIT, REAL OUTPUT
C INPUT ERROR DISPLAY ERROR OUTPUT CODE 1 IN JOB CONTROL LISTING
      READ (*, *) IA, IB, IC
C
C IA, IB, AND IC MAY NOT BE NEGATIVE OR ZERO
C FURTHERMORE, THE SUM OF TWO SIDES OF A TRIANGLE
C MUST BE GREATER THAN THE THIRD SIDE, SO WE CHECK FOR THAT, TOO
      IF (IA .LE. 0 .OR. IB .LE. 0 .OR. IC .LE. 0) THEN
        WRITE (*, *) 'IA, IB, and IC must be greater than zero.'
        STOP 1
      END IF
C
      IF (IA+IB-IC .LE. 0
     +    .OR. IA+IC-IB .LE. 0
     +    .OR. IB+IC-IA .LE. 0) THEN
        WRITE (*, *) 'Sum of two sides must be greater than third side.'
        STOP 1
      END IF
C
C USING HERON'S FORMULA WE CALCULATE THE
C AREA OF THE TRIANGLE
      S = (IA + IB + IC) / 2.0
      AREA = SQRT ( S * (S - IA) * (S - IB) * (S - IC))
      WRITE (*, 601) IA, IB, IC, AREA
  601 FORMAT ('A= ', I5, '  B= ', I5, '  C= ', I5, '  AREA= ', F10.2,
     +        ' square units')
      STOP
      END
```

### Transition to ANSI Standard Fortran

The development of a revised standard to succeed FORTRAN 77 would be repeatedly delayed as the standardization process struggled to keep up with rapid changes in computing and programming practice. In the meantime, as the "Standard FORTRAN" for nearly fifteen years, FORTRAN 77 would become the historically most important dialect.

An important practical extension to FORTRAN 77 was the release of MIL-STD-1753 in 1978. This specification, developed by the U.S. Department of Defense, standardized a number of features implemented by most FORTRAN 77 compilers but not included in the ANSI FORTRAN 77 standard. These features would eventually be incorporated into the Fortran 90 standard.

- `DO WHILE` and `END DO` statements
- `INCLUDE` statement
- `IMPLICIT NONE` variant of the `IMPLICIT` statement
- Bit manipulation intrinsic functions, based on similar functions included in Industrial Real-Time Fortran (ANSI/ISA S61.1 (1976))

The IEEE 1003.9 POSIX Standard, released in 1991, provided a simple means for FORTRAN 77 programmers to issue POSIX system calls. Over 100 calls were defined in the document – allowing access to POSIX-compatible process control, signal handling, file system control, device control, procedure pointing, and stream I/O in a portable manner.

### Fortran 90

The much-delayed successor to FORTRAN 77, informally known as *Fortran 90* (and prior to that, *Fortran 8X*), was finally released as ISO/IEC standard 1539:1991 in 1991 and an ANSI Standard in 1992. In addition to changing the official spelling from FORTRAN to Fortran, this major revision added many new features to reflect the significant changes in programming practice that had evolved since the 1978 standard:

- Free-form source input removes the need to skip the first six character positions before entering statements. Line continuations are specified by the `&` character at the end of the line, rather than in column 6 of the next line. Blanks also become significant. Typically files with names ending in `.f90` signify free-format source code. The older fixed-form source form is still defined, but considered obsolescent.
- Lowercase Fortran keywords
- Identifiers up to 31 characters in length (in the previous standard, it was only six characters).
- Inline comments
- Ability to operate on arrays (or array sections) as a whole, thus greatly simplifying math and engineering computations.
  - whole, partial and masked array assignment statements and array expressions, such as `X(1:N)=R(1:N)*COS(A(1:N))`
  - `WHERE` statement for selective array assignment
  - array-valued constants and expressions,
  - user-defined array-valued functions and array constructors.
- `RECURSIVE` procedures
- Modules, to group related procedures and data together, and make them available to other program units, including the capability to limit the accessibility to only specific parts of the module.
- A vastly improved argument-passing mechanism, allowing interfaces to be checked at compile time
- User-written interfaces for generic procedures
- Operator overloading
- Derived (structured) data types
- New data type declaration syntax, to specify the data type and other attributes of variables
- Dynamic memory allocation by means of the `ALLOCATABLE` attribute and the `ALLOCATE` and `DEALLOCATE` statements
- `POINTER` attribute, pointer assignment, and `NULLIFY` statement to facilitate the creation and manipulation of dynamic data structures
- Structured looping constructs, with an `END DO` statement for loop termination, and `EXIT` and `CYCLE` statements for terminating normal `DO` loop iterations in an orderly way
- `SELECT CASE`, `CASE`, . . . `CASE DEFAULT`, `END SELECT` construct for multi-way selection
- Portable specification of numerical precision under the user's control
- New and enhanced intrinsic procedures.

#### Obsolescence and deletions

Unlike the prior revision, Fortran 90 removed no features. Any standard-conforming FORTRAN 77 program was also standard-conforming under Fortran 90, and either standard should have been usable to define its behavior.

A small set of features were identified as "obsolescent" and were expected to be removed in a future standard. All of the functionalities of these early-version features can be performed by newer Fortran features. Some are kept to simplify porting of old programs but many were deleted in Fortran 95.

| Obsolescent feature | Current status |
|---|---|
| Arithmetic IF-statement | Obsolescent in F90, deleted in F2018 |
| Non-integer DO parameters or control variables | Obsolescent in F90, deleted in F95 |
| Shared DO-loop termination or termination with a statement other than END DO or CONTINUE | Obsolescent in F90, deleted in F2018 |
| Branching to END IF from outside a block | Obsolescent in F90, deleted in F95 |
| PAUSE statement | Obsolescent in F90, deleted in F95 |
| ASSIGN statement and assigned GO TO statement | Obsolescent in F90, deleted in F95 |
| Assigned statement numbers and FORMAT specifiers | Obsolescent in F90, deleted in F95 |
| H edit descriptor | Obsolescent in F90, deleted in F95 |
| Vertical format control | Deleted in F2003 |
| Alternate return | Obsolescent in F90 |
| Computed GO TO statement | Obsolescent in F90 |
| Statement functions | Obsolescent in F90 |
| DATA statements among executable statements | Obsolescent in F90 |
| Assumed length character functions | Obsolescent in F90 |
| Fixed form source code | Obsolescent in F90 |
| CHARACTER* form of CHARACTER declaration | Obsolescent in F90 |
| ENTRY statements | Obsolescent in F2008 |
| Label form of DO statement | Obsolescent in F2018 |
| COMMON and EQUIVALENCE statements, and the BLOCK DATA program unit | Obsolescent in F2018 |
| Specific names for intrinsic function | Obsolescent in F2018 |
| FORALL construct and statement | Obsolescent in F2018 |

#### "Hello, World!" example

```mw
program helloworld
     print *, "Hello, World!"
end program helloworld
```

### Fortran 95

*Fortran 95*, published officially as ISO/IEC 1539-1:1997, was a minor revision, mostly to resolve some outstanding issues from the Fortran 90 standard. Nevertheless, Fortran 95 also added a number of extensions, notably from the High Performance Fortran specification:

- `FORALL` and nested `WHERE` constructs to aid vectorization
- User-defined `PURE` and `ELEMENTAL` procedures
- Default initialization of derived type components, including pointer initialization
- Expanded the ability to use initialization expressions for data objects
- Initialization of pointers to `NULL()`
- Clearly defined that `ALLOCATABLE` arrays are automatically deallocated when they go out of scope.

A number of intrinsic functions were extended (for example a `dim` argument was added to the `maxloc` intrinsic).

Several features noted in Fortran 90 to be "obsolescent" were removed from Fortran 95:

- `DO` statements using `REAL` and `DOUBLE PRECISION` index variables
- Branching to an `END IF` statement from outside its block
- `PAUSE` statement
- `ASSIGN` and assigned `GO TO` statement, and assigned format specifiers
- `H` Hollerith edit descriptor.

An important supplement to Fortran 95 was the ISO technical report *TR-15581: Enhanced Data Type Facilities*, informally known as the *Allocatable TR.* This specification defined enhanced use of `ALLOCATABLE` arrays, prior to the availability of fully Fortran 2003-compliant Fortran compilers. Such uses include `ALLOCATABLE` arrays as derived type components, in procedure dummy argument lists, and as function return values. (`ALLOCATABLE` arrays are preferable to `POINTER`-based arrays because `ALLOCATABLE` arrays are guaranteed by Fortran 95 to be deallocated automatically when they go out of scope, eliminating the possibility of memory leakage. In addition, elements of allocatable arrays are contiguous, and aliasing is not an issue for optimization of array references, allowing compilers to generate faster code than in the case of pointers.)

Another important supplement to Fortran 95 was the ISO technical report *TR-15580: Floating-point exception handling*, informally known as the *IEEE TR.* This specification defined support for IEEE floating-point arithmetic and floating-point exception handling.

#### Conditional compilation and varying length strings

In addition to the mandatory "Base language" (defined in ISO/IEC 1539-1 : 1997), the Fortran 95 language also included two optional modules:

- Varying length character strings (ISO/IEC 1539-2 : 2000)
- Conditional compilation (ISO/IEC 1539-3 : 1998)

which, together, compose the multi-part International Standard (ISO/IEC 1539).

According to the standards developers, "the optional parts describe self-contained features which have been requested by a substantial body of users and/or implementors, but which are not deemed to be of sufficient generality for them to be required in all standard-conforming Fortran compilers." Nevertheless, if a standard-conforming Fortran does provide such options, then they "must be provided in accordance with the description of those facilities in the appropriate Part of the Standard".


## Modern Fortran

The language defined by the twenty-first century standards, in particular because of its incorporation of object-oriented programming support and subsequently Coarray Fortran, is often referred to as 'Modern Fortran', and the term is increasingly used in the literature.

### Fortran 2003

*Fortran 2003,* officially published as ISO/IEC 1539-1:2004, was a major revision introducing many new features. A comprehensive summary of the new features of Fortran 2003 is available at the Fortran Working Group (ISO/IEC JTC1/SC22/WG5) official Web site.

From that article, the major enhancements for this revision include:

- Derived type enhancements: parameterized derived types, improved control of accessibility, improved structure constructors, and finalizers
- Object-oriented programming support: type extension and inheritance, polymorphism, dynamic type allocation, and type-bound procedures, providing complete support for abstract data types
- Data manipulation enhancements: allocatable components (incorporating TR 15581), deferred type parameters, `VOLATILE` attribute, explicit type specification in array constructors and allocate statements, pointer enhancements, extended initialization expressions, and enhanced intrinsic procedures
- Input/output enhancements: asynchronous transfer, stream access, user specified transfer operations for derived types, user specified control of rounding during format conversions, named constants for preconnected units, the `FLUSH` statement, regularization of keywords, and access to error messages
- Procedure pointers
- Support for IEEE floating-point arithmetic and floating-point exception handling (incorporating TR 15580)
- Interoperability with the C programming language
- Support for international usage: access to ISO 10646 4-byte characters and choice of decimal or comma in numeric formatted input/output
- Enhanced integration with the host operating system: access to command-line arguments, environment variables, and processor error messages

An important supplement to Fortran 2003 was the ISO technical report *TR-19767: Enhanced module facilities in Fortran.* This report provided *sub-modules,* which make Fortran modules more similar to Modula-2 modules. They are similar to Ada private child sub-units. This allows the specification and implementation of a module to be expressed in separate program units, which improves packaging of large libraries, allows preservation of trade secrets while publishing definitive interfaces, and prevents compilation cascades.

### Fortran 2008

ISO/IEC 1539-1:2010, informally known as Fortran 2008, was approved in September 2010. As with Fortran 95, this is a minor upgrade, incorporating clarifications and corrections to Fortran 2003, as well as introducing some new capabilities. The new capabilities include:

- Sub-modules – additional structuring facilities for modules; supersedes ISO/IEC TR 19767:2005
- Coarray Fortran – a parallel execution model
- The DO CONCURRENT construct – for loop iterations with no interdependencies
- The CONTIGUOUS attribute – to specify storage layout restrictions
- The BLOCK construct – can contain declarations of objects with construct scope
- Recursive allocatable components – as an alternative to recursive pointers in derived types

The Final Draft international Standard (FDIS) is available as document N1830.

A supplement to Fortran 2008 is the International Organization for Standardization (ISO) Technical Specification (TS) 29113 on *Further Interoperability of Fortran with C*, which has been submitted to ISO in May 2012 for approval. The specification adds support for accessing the array descriptor from C and allows ignoring the type and rank of arguments.

### Fortran 2018

The Fortran 2018 revision of the language was earlier referred to as Fortran 2015. It was a significant revision and was released on November 28, 2018.

Fortran 2018 incorporates two previously published Technical Specifications:

- ISO/IEC TS 29113:2012 Further Interoperability with C
- ISO/IEC TS 18508:2015 Additional Parallel Features in Fortran

Additional changes and new features include support for ISO/IEC/IEEE 60559:2011 (the version of the IEEE floating-point standard before the latest minor revision IEEE 754–2019), hexadecimal input/output, IMPLICIT NONE enhancements and other changes.

Fortran 2018 deleted the arithmetic IF statement. It also deleted non-block DO constructs - loops which do not end with an END DO or CONTINUE statement. These had been an obsolescent part of the language since Fortran 90.

New obsolescences are: COMMON and EQUIVALENCE statements and the BLOCK DATA program unit, labelled DO loops, specific names for intrinsic functions, and the FORALL statement and construct.

### Fortran 2023

Fortran 2023 (ISO/IEC 1539-1:2023) was published in November 2023, and can be purchased from the ISO. Fortran 2023 is a minor extension of Fortran 2018 that focuses on correcting errors and omissions in Fortran 2018. It also adds several small features, including conditional expressions and arguments, simple procedures, and an enumerated type capability. Degree- and half revolution based trig functions were also added. Degree-based trig functions were previously a very common vendor extension.


## Language features

A full description of the Fortran language features brought by Fortran 95 is covered in the related article, *Fortran 95 language features*. The language versions defined by later standards are often referred to collectively as 'Modern Fortran' and are described in the literature.


## Science and engineering

Although a 1968 journal article by the authors of BASIC already described FORTRAN as "old-fashioned", programs have been written in Fortran for many decades and there is a vast body of Fortran software in daily use throughout the scientific and engineering communities. Jay Pasachoff wrote in 1984 that "physics and astronomy students simply have to learn FORTRAN. So much exists in FORTRAN that it seems unlikely that scientists will change to Pascal, Modula-2, or whatever." In 1993, Cecil E. Leith called FORTRAN the "mother tongue of scientific computing", adding that its replacement by any other possible language "may remain a forlorn hope".

It is the primary language for some of the most intensive super-computing tasks, such as in astronomy, climate modeling, computational chemistry, computational economics, computational fluid dynamics, computational physics, data analysis, hydrological modeling, numerical linear algebra and numerical libraries (LAPACK, IMSL and NAG), optimization, satellite simulation, structural engineering, and weather prediction. Many of the floating-point benchmarks to gauge the performance of new computer processors, such as the floating-point components of the SPEC benchmarks (e.g., CFP2006, CFP2017) are written in Fortran. Math algorithms are well documented in Numerical Recipes.

Apart from this, more modern codes in computational science generally use large program libraries, such as METIS for graph partitioning, PETSc or Trilinos for linear algebra capabilities, deal.II or FEniCS for mesh and finite element support, and other generic libraries. Since the early 2000s, many of the widely used support libraries have also been implemented in C and more recently, in C++. On the other hand, high-level languages such as the Wolfram Language, MATLAB, Python, and R have become popular in particular areas of computational science. Consequently, a growing fraction of scientific programs are also written in such higher-level scripting languages. For this reason, facilities for inter-operation with C were added to Fortran 2003 and enhanced by the ISO/IEC technical specification 29113, which was incorporated into Fortran 2018 to allow more flexible interoperation with other programming languages.


## Portability

Portability was a problem in the early days because there was no agreed upon standard—not even IBM's reference manual—and computer companies vied to differentiate their offerings from others by providing incompatible features. Standards have improved portability. The 1966 standard provided a reference syntax and semantics, but vendors continued to provide incompatible extensions. Although careful programmers were coming to realize that use of incompatible extensions caused expensive portability problems, and were therefore using programs such as *The PFORT Verifier,* it was not until after the 1977 standard, when the National Bureau of Standards (now NIST) published *FIPS PUB 69*, that processors purchased by the U.S. Government were required to diagnose extensions of the standard. Rather than offer two processors, essentially every compiler eventually had at least an option to diagnose extensions.

Incompatible extensions were not the only portability problem. For numerical calculations, it is important to take account of the characteristics of the arithmetic. This was addressed by Fox et al. in the context of the 1966 standard by the *PORT* library. The ideas therein became widely used, and were eventually incorporated into the 1990 standard by way of intrinsic inquiry functions. The widespread (now almost universal) adoption of the IEEE 754 standard for binary floating-point arithmetic has essentially removed this problem.

Access to the computing environment (e.g., the program's command line, environment variables, textual explanation of error conditions) remained a problem until it was addressed by the 2003 standard.

Large collections of library software that could be described as being loosely related to engineering and scientific calculations, such as graphics libraries, have been written in C, and therefore access to them presented a portability problem. This has been addressed by incorporation of C interoperability into the 2003 standard.

It is now possible (and relatively easy) to write an entirely portable program in Fortran, even without recourse to a preprocessor.
