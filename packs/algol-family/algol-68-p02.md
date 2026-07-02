---
title: "ALGOL 68 (part 2/2)"
source: https://en.wikipedia.org/wiki/ALGOL_68
domain: algol-family
license: CC-BY-SA-4.0
tags: algol language, john backus, imperative programming, structured programming, backus naur form
fetched: 2026-07-02
part: 2/2
---

## Program representation

A feature of ALGOL 68, inherited from the ALGOL tradition, is its different representations. Programs in the *strict language* (which is rigorously defined in the Report) denote production trees in the form of a sequence of grammar symbols, and should be represented using some *representation language*, of which there are many and tailored to different purposes.

- Representation languages that are intended to describe algorithms in printed works are known as *publication languages* and typically make use of rich typography to denote bold words and operator indications.
- Representation languages that are intended to be used in compiler input, what we would call *programming languages*, are limited by the restrictions imposed by input methods and character sets and have to resort to *stropping regimes* to distinguish between bold and non bold letters and digits.
- Representation languages that are intended to be both produced and consumed by computers, known as *hardware languages*, would typically use a binary compact representation.

The Revised Report defines a *reference language* and it is recommended for representation languages that are intended to be read by humans to be close enough to the reference language so symbols can be distinguished "without further elucidation". These representation languages are called *implementations of the reference language*.

For example, the construct in the strict language **bold-begin-symbol** could be represented as **begin** in a publication language, as *BEGIN* in a programming language or as the bytes 0xC000 in some hardware language. Similarly, the strict language **differs from symbol** could be represented as ≠ or as /=.

ALGOL 68's reserved words are effectively in a different namespace from identifiers, and spaces are allowed in identifiers in most stropping regimes, so this next fragment is legal:

```
 INT a real int = 3 ;
```

The programmer who writes executable code does not always have an option of **BOLD** typeface or underlining in the code as this may depend on hardware and cultural issues. Different methods to denote these identifiers have been devised. This is called a *stropping regime*. For example, all or some of the following may be available *programming representations*:

```
'INT'A REAL INT = 3; # QUOTE stropping style #
.INT A REAL INT = 3; # POINT stropping style #
 INT a real int = 3; # UPPER stropping style #
 int a_real_int = 3; # RES stropping style, there are 61 accepted reserved words #
```

All implementations must recognize at least POINT, UPPER and RES inside PRAGMAT sections. Of these, POINT and UPPER stropping are quite common. QUOTE (single apostrophe quoting) was the original recommendation.

It may seem that RES stropping is a contradiction to the specification, as there are no reserved words in Algol 68. This is not so. In RES stropping the representation of the bold word (or keyword) **begin** is *begin*, and the representation of the identifier *begin* is *begin_*. Note that the underscore character is just a representation artifact and not part of the represented identifier. In contrast, in non-stropped languages with reserved words, like for example C, it is not possible to represent an identifier *if*, since the representation *if_* represents the identifier *if_*, not *if*.

The following characters were recommended for portability, and termed "worthy characters" in the Report on the Standard Hardware Representation of Algol 68 :

- **^**Worthy Characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "#$%'()*+,-./:;<=>@[ ]_|

This reflected a problem in the 1960s where some hardware didn't support lower-case, nor some other non-ASCII characters, indeed in the 1973 report it was written: "Four worthy characters — "|", "_", "[", and "]" — are often coded differently, even at installations which nominally use the same character set."

- Base characters: "Worthy characters" are a subset of "base characters".

### Example of different program representations

| Representation | Code |
|---|---|
| Algol68 as typically published | *¢ underline or* *bold typeface ¢* **mode** **xint** = **int**; **xint** sum sq:=0; **for** i **while** sum sq≠70×70 **do** sum sq+:=i↑2 **od** |
| Quote stropping (like wikitext) | 'pr' quote 'pr' 'mode' 'xint' = 'int'; 'xint' sum sq:=0; 'for' i 'while' sum sq≠70×70 'do' sum sq+:=i↑2 'od' |
| For a 7-bit character code compiler | PR UPPER PR MODE XINT = INT; XINT sum sq:=0; FOR i WHILE sum sq/=70*70 DO sum sq+:=i**2 OD |
| For a 6-bit character code compiler | .PR POINT .PR .MODE .XINT = .INT; .XINT SUM SQ:=0; .FOR I .WHILE SUM SQ .NE 70*70 .DO SUM SQ .PLUSAB I .UP 2 .OD |
| Algol68 using **RES** stropping (reserved word) | .PR RES .PR mode .xint = int; .xint sum sq:=0; for i while sum sq≠70×70 do sum sq+:=i↑2 od |
| Algol68 using **SUPPER** stropping (GNU extension) | mode Int = int; Int sum sq:=0; for i while sum sq ≠70×70 do sum sq+:=i↑2 od |

ALGOL 68 allows for every natural language to define its own set of keywords Algol-68. As a result, programmers are able to write programs using keywords from their native language. Below is an example of a simple procedure that calculates "the day following", the code is in two languages: English and German.

```
 # Next day date - English variant #
 MODE DATE = STRUCT(INT day, STRING month, INT year);
 PROC the day following = (DATE x) DATE:
      IF day OF  x < length of month (month OF x, year OF x)
      THEN (day OF x + 1, month OF x, year OF x)
      ELIF month OF x = "December"
      THEN (1, "January", year OF x + 1)
      ELSE (1, successor of month (month OF x), year OF x)
      FI;
```

```
 # Nachfolgetag - Deutsche Variante #
 MENGE DATUM = TUPEL(GANZ tag, WORT monat, GANZ jahr);
 FUNKTION naechster tag nach = (DATUM x) DATUM:
          WENN tag VON x < monatslaenge(monat VON x, jahr VON x)
          DANN (tag VON x + 1, monat VON x, jahr VON x)
          WENNABER monat VON x = "Dezember"
          DANN (1, "Januar", jahr VON x + 1)
          ANSONSTEN (1, nachfolgemonat(monat VON x), jahr VON x)
          ENDEWENN;
```

*Russian/Soviet example:* In English Algol68's case statement reads **CASE** ~ **IN** ~ **OUT** ~ **ESAC**, in Cyrillic this reads **выб** ~ **в** ~ **либо** ~ **быв**.


## Revisions

Except where noted (with a superscript), the language described above is that of the "Revised Report(r1)".

### The language of the unrevised report

The original language (As per the "Final Report"r0) differs in syntax of the *mode cast*, and it had the feature of *proceduring*, i.e. coercing the value of a term into a procedure which evaluates the term. Proceduring would be intended to make evaluations *lazy*. The most useful application could have been the short-circuited evaluation of Boolean operators. In:

```
OP ANDF = (BOOL a,PROC BOOL b)BOOL:(a | b | FALSE);
OP ORF = (BOOL a,PROC BOOL b)BOOL:(a | TRUE | b);
```

*b* is only evaluated if *a* is true.

As defined in ALGOL 68, it did not work as expected, for example in the code:

```
IF FALSE ANDF CO proc bool: CO ( print ("Should not be executed"); TRUE)
THEN ...
```

against the programmers naïve expectations the print *would* be executed as it is only the *value* of the elaborated enclosed-clause after **ANDF** that was procedured. Textual insertion of the commented-out **PROC** **BOOL**: makes it work.

Some implementations emulate the expected behaviour for this special case by extension of the language.

Before revision, the programmer could decide to have the arguments of a procedure evaluated serially instead of collaterally by using semicolons instead of commas (*gomma*s).

For example in:

```
PROC test = (REAL a; REAL b) :...
...
test (x PLUS 1, x);
```

The first argument to test is guaranteed to be evaluated before the second, but in the usual:

```
PROC test = (REAL a, b) :...
...
test (x PLUS 1, x);
```

then the compiler could evaluate the arguments in whatever order it felt like.

### Extension proposals from IFIP WG 2.1

After the revision of the report, some extensions to the language have been proposed to widen the applicability:

- *partial parametrisation* (aka Currying): creation of functions (with fewer parameters) by specification of some, but not all parameters for a call, e.g. a function logarithm of two parameters, base and argument, could be specialised to natural, binary or decadic log,.
- *module extension*: for support of external linkage, two mechanisms were proposed, bottom-up *definition modules*, a more powerful version of the facilities from ALGOL 68-R and top-down *holes*, similar to the `ENVIRON` and `USING` clauses from ALGOL 68C
- *mode parameters*: for implementation of limited parametrical polymorphism (most operations on data structures like lists, trees or other data containers can be specified without touching the pay load).

So far, partial parametrisation has been implemented in Algol 68 Genie, and a subset of the Modules and Separated Compilation facility has been implemented in GCC.

### True ALGOL 68s specification and implementation timeline

| Name | Year | Purpose | State | Description | Target CPU | Licensing | Implementation language |
|---|---|---|---|---|---|---|---|
| Generalized ALGOL | 1962 | Scientific | NLD | ALGOL for generalised grammars |   |   |   |
| ALGOL YY | 1966 | Draft proposal | Intl | First version of ALGOL 68 | Specification | ACM |   |
| ALGOL 68DR | 1968 | Draft proposal | Intl | IFIP WG 2.1 Draft Report | Specification – March | ACM |   |
| ALGOL 68r0 | 1968 | Standard | Intl | IFIP WG 2.1 Final Report | Specification – August | ACM |   |
| ALGOL 68-RR | 1970 | Military | UK |   | ICL 1900 |   | ALGOL 60 |
| EPOS ALGOLE | 1971 | Scientific |   |   |   |   |   |
| ALGOL 68RSRS | 1972 | Multi-purpose | UK | Portable compiler system | ICL 2900/Series 39, Multics, VMS & C generator (1993) | Crown Copyright | ALGOL 68RS |
| ALGOL 68 with areas | 1972 | Experimental & other | UK | Areas added to ALGOL 68 |   |   |   |
| Mini ALGOL 68 | 1973 | Research | NLD | Interpreter for ALGOL 68 subset | Portable interpreter | Mathematisch Centrum | ALGOL 60 |
| OREGANO | 1973 | Research | US | "The importance of implementation models." |   | UCLA |   |
| ALGOL 68CC | 1975 | Scientific | UK | Cambridge ALGOL 68 | ICL, IBM 360, PDP-10 & Unix, Telefunken, TESLA 200, Z80 (1980) | Cambridge | ALGOL 68C |
| **ALGOL 68 Revised Report**r1 | 1975 | Standard | Intl | IFIP WG 2.1 Revised Report | Specification | ACM |   |
| ALGOL HH | 1975 | Experimental & other | UK | Proposed extensions to ALGOL 68 mode system | Specification |   | ALGOL W |
| Odra ALGOL 68 | 1976 | practical uses | Soviet Union/ Poland |   | Odra 1204/IL | Soviet | ALGOL 60 |
| Oklahoma ALGOL 68 | 1976 | programming instruction | USA | Oklahoma State University implementation | IBM 1130 and System/370/158 | Unknown | ANSI Fortran 66. |
| Berlin ALGOL 68 | 1977 | Research | DE | Portable compiler for System/370, Siemens S4004, and PDP-11 | Machine-independent compiler | Technische Universität Berlin | CDL 2 |
| FLACCF | 1977 | Multi-purpose | CAN | Revised Report complete implementation with debug features | System/370 | lease, Chion Corporation | Assembler |
| ALGOL 68-RTRT | 1979 | Scientific | UK | Parallel ALGOL 68-R |   |   |   |
| RS Algolrs | 1979 | Scientific | UK |   |   |   |   |
| ALGOL 68+ | 1980 | Scientific | NLD | Proposed superlanguage of ALGOL 68 |   |   |   |
| M-220 ALGOL 68 |   |   | Soviet Union |   | M-220 | Soviet | EPSILON |
| Leningrad ALGOL 68L | 1980 | Telecommunications | Soviet Union | Full language + modules | IBM, DEC, CAMCOH, PS 1001 & PC | Soviet |   |
| Interactive ALGOL 68I | 1983 |   | UK | Incremental compilation | PC | Noncommercial shareware |   |
| ALGOL 68SS | 1985 | Scientific | Intl | Sun version of ALGOL 68 | Sun-3, Sun SPARC (under SunOS 4.1 & Solaris 2), Atari ST (under GEMDOS), Acorn Archimedes (under RISC OS), VAX-11 under Ultrix-32 |   |   |
| ALGOL68toC (ctrans) | 1985 | Electronics | UK | ctrans from ELLA ALGOL 68RS | Portable C generator | Open-source (1995) | ALGOL 68RS |
| MK2 Interactive ALGOL 68 | 1992 |   | UK | Incremental compilation | PC | Noncommercial shareware |   |
| ALGOL 68 GenieG | 2001 | Full language | NLD | Includes standard collateral clause | Portable interpreter | GPL | C |
| ALGOL 68 Genie version 2.0.0 | 2010 | Full language | NLD |   | Portable interpreter; optional compilation of selected units | GPL | C |
| GCC (ga68) | 2025 | Full language | ESP | GCC Front-End | Portable compiler | GPL | C++ |

The S3 language that was used to write the ICL VME operating system and much other system software on the ICL 2900 Series was a direct derivative of ALGOL 68. However, it omitted many of the more complex features, and replaced the basic modes with a set of data types that mapped directly to the 2900 Series hardware architecture.

### Implementation specific extensions

ALGOL 68R from RRE was the first ALGOL 68 subset implementation, running on the ICL 1900. Based on the original language, the main subset restrictions were *definition before use* and no parallel processing. This compiler was popular in UK universities in the 1970s, where many computer science students learnt ALGOL 68 as their first programming language; the compiler was renowned for good error messages.

ALGOL 68RS(RS) from RSRE was a portable compiler system written in ALGOL 68RS (bootstrapped from ALGOL 68R), and implemented on a variety of systems including the ICL 2900/Series 39, Multics and DEC VAX/VMS. The language was based on the Revised Report, but with similar subset restrictions to ALGOL 68R. This compiler survives in the form of an Algol68-to-C compiler.

In ALGOL 68S(S) from Carnegie Mellon University the power of parallel processing was improved by adding an orthogonal extension, *eventing*. Any variable declaration containing keyword **EVENT** made assignments to this variable eligible for parallel evaluation, i.e. the right hand side was made into a procedure which was moved to one of the processors of the C.mmp multiprocessor system. Accesses to such variables were delayed after termination of the assignment.

Cambridge ALGOL 68C(C) was a portable compiler that implemented a subset of ALGOL 68, restricting operator definitions and omitting garbage collection, flexible rows and formatted transput.

Algol 68 Genie(G) by Marcel van der Veer is an ALGOL 68 implementation for today's computers and operating systems. The interpreter implements one extension - Charles Lindsey’s partial parametrization proposal published in 1976, that gives the imperative language Algol 68 a functional sub-language.

The GNU Compiler Collection's GNU Algol 68 implements several GNU extensions to the language, providing a strict superlanguage of ALGOL 68, as is explicitly allowed by the Revised Report.

"Despite good intentions, a programmer may violate portability by inadvertently employing a local extension. To guard against this, each implementation should provide a PORTCHECK pragmat option. While this option is in force, the compiler prints a message for each construct that it recognizes as violating some portability constraint."


## Quotes

- *... The scheme of type composition adopted by C owes considerable debt to Algol 68, although it did not, perhaps, emerge in a form that Algol's adherents would approve of. The central notion I captured from Algol was a type structure based on atomic types (including structures), composed into arrays, pointers (references), and functions (procedures). Algol 68's concept of unions and casts also had an influence that appeared later.* Dennis Ritchie Apr 1993.
- *... C does not descend from Algol 68 is true, yet there was influence, much of it so subtle that it is hard to recover even when I think hard. In particular, the union type (a late addition to C) does owe to A68, not in any details, but in the idea of having such a type at all. More deeply, the type structure in general and even, in some strange way, the declaration syntax (the type-constructor part) was inspired by A68. And yes, of course, "long".* Dennis Ritchie, 18 June 1988
- "Congratulations, your Master has done it" – Niklaus Wirth
- *The more I see of it, the more unhappy I become* – E. W. Dijkstra, 1968
- *[...] it was said that A68's popularity was inversely proportional to [...] the distance from Amsterdam* – Guido van Rossum
- *[...] The best we could do was to send with it a minority report, stating our considered view that, "... as a tool for the reliable creation of sophisticated programs, the language was a failure." [...]* – C. A. R. Hoare in his Oct 1980 Turing Award Lecture
- *"[...] More than ever it will be required from an adequate programming tool that it assists, by structure, the programmer in the most difficult aspects of his job, viz. in the reliable creation of sophisticated programs. In this respect we fail to see how the language proposed here is a significant step forward: on the contrary, we feel that its implicit view of the programmer's task is very much the same as, say, ten years ago. This forces upon us the conclusion that, regarded as a programming tool, the language must be regarded as obsolete. [...]"* 1968 Working Group minority report on 23 December 1968.
