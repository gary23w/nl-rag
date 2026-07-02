---
title: "ALGOL 60"
source: https://en.wikipedia.org/wiki/ALGOL_60
domain: algol-family
license: CC-BY-SA-4.0
tags: algol language, john backus, imperative programming, structured programming, backus naur form
fetched: 2026-07-02
---

# ALGOL 60

**ALGOL 60** (short for *Algorithmic Language 1960*) is a member of the ALGOL family of computer programming languages. It followed on from ALGOL 58 which had introduced code blocks and the `begin` and `end` pairs for delimiting them, representing a key advance in the rise of structured programming. ALGOL 60 was one of the first languages implementing function definitions (that could be invoked recursively). ALGOL 60 function definitions could be nested within one another (a feature introduced by ALGOL 60) with lexical scope. It gave rise to many other languages, including CPL, PL/I, Simula, BCPL, B, Pascal, and C. Practically every computer of the era had a systems programming language based on ALGOL 60 concepts.

Niklaus Wirth based his own ALGOL W on ALGOL 60 before moving to develop Pascal. Algol-W was intended to be the next generation ALGOL but the ALGOL 68 committee decided on a design that was more complex and advanced rather than a cleaned simplified ALGOL 60. The official ALGOL versions are named after the year they were first published. ALGOL 68 is substantially different from ALGOL 60 and was criticised partially for being so, so that in general "ALGOL" refers to dialects of ALGOL 60.

## Standardization

ALGOL 60 – with COBOL – were the first languages to seek standardization.

- ISO 1538:1984 Programming languages – ALGOL 60 (stabilized)
- ISO/TR 1672:1977 Hardware representation of ALGOL basic symbols ... (now withdrawn)

## History

ALGOL 60 was used mostly by research computer scientists in the United States and in Europe. Its use in commercial applications was hindered by the absence of standard input/output facilities in its description and the lack of interest in the language by large computer vendors. ALGOL 60 did however become the standard for the publication of algorithms and had a profound effect on future language development.

John Backus developed the Backus normal form method of describing programming languages specifically for ALGOL 58. It was revised and expanded by Peter Naur for ALGOL 60, and at Donald Knuth's suggestion renamed Backus–Naur form.

Peter Naur: "As editor of the ALGOL Bulletin I was drawn into the international discussions of the language and was selected to be member of the European language design group in November 1959. In this capacity I was the editor of the ALGOL 60 report, produced as the result of the ALGOL 60 meeting in Paris in January 1960."

The following people attended the meeting in Paris (from January 11 to 16):

- Friedrich Ludwig Bauer, Peter Naur, Heinz Rutishauser, Klaus Samelson, Bernard Vauquois, Adriaan van Wijngaarden, and Michael Woodger (from Europe)
- John Warner Backus, Julien Green, Charles Katz, John McCarthy, Alan Jay Perlis, and Joseph Henry Wegstein (from the USA).

Alan Perlis gave a vivid description of the meeting: "The meetings were exhausting, interminable, and exhilarating. One became aggravated when one's good ideas were discarded along with the bad ones of others. Nevertheless, diligence persisted during the entire period. The chemistry of the 13 was excellent."

The language originally did not include recursion. It was inserted into the specification at the last minute, against the wishes of some of the committee.

Several authors of the original report met in April 1962 to resolve issues that had arisen. Their work resulted in the publication of the "Revised report on the algorithmic language ALGOL 60".

Further clarifications and the inclusion of I/O procedures were made by the Working Group 2.1 of IFIP Technical Committee 2. These efforts were published as the "Modified Report on the algorithmic language ALGOL 60" in 1975.

ALGOL 60 inspired many languages that followed it. Tony Hoare remarked: "Here is a language so far ahead of its time that it was not only an improvement on its predecessors but also on nearly all its successors."

### ALGOL 60 implementations timeline

To date there have been at least 70 augmentations, extensions, derivations and sublanguages of ALGOL 60.

| Name | Year | Author | State | Description | Target CPU |
|---|---|---|---|---|---|
| X1 ALGOL 60 | August 1960 | Edsger W. Dijkstra and Jaap A. Zonneveld | Netherlands | First implementation of ALGOL 60 | Electrologica X1 |
| Algol | 1960 | Edgar T. Irons | USA | ALGOL 60 | CDC 1604 |
| Burroughs Algol (Several variants) | 1961 | Burroughs Corporation (with participation by Hoare, Dijkstra, and others) | USA | Basis of the Burroughs (and now Unisys MCP based) computers | Burroughs Large Systems and midrange systems |
| Case ALGOL | 1961 |   | USA | Simula was originally contracted as a simulation extension of the Case ALGOL | UNIVAC 1107 |
| GOGOL | 1961 | William M. McKeeman | USA | For ODIN time-sharing system | PDP-1 |
| DASK ALGOL | 1961 | Peter Naur, Jørn Jensen | Denmark | ALGOL 60 | DASK at Regnecentralen |
| SMIL ALGOL | 1962 | Torgil Ekman, Carl-Erik Fröberg | Sweden | ALGOL 60 | SMIL at Lund University |
| GIER ALGOL | 1962 | Peter Naur, Jørn Jensen | Denmark | ALGOL 60 | GIER at Regnecentralen |
| Dartmouth ALGOL 30 | 1962 | Thomas Eugene Kurtz, Stephen J. Garland, Robert F. Hargraves, Anthony W. Knapp, Jorge LLacer | USA | ALGOL 60 | LGP-30 |
| Alcor Mainz 2002 | 1962 | Ursula Hill-Samelson, Hans Langmaack | Germany |   | Siemens 2002 |
| ALCOR-Illinois 7090 | 1962 | Manfred Paul, Hans Rüdiger Wiehle, David Gries, and Rudolf Bayer | USA, West Germany | ALGOL 60 Implemented at Illinois and the TH München, 1962–1964 | IBM 7090 |
| USS 90 Algol | 1962 | L. Petrone | Italy |   |   |
| Elliott ALGOL | 1962 | C. A. R. Hoare | UK | Discussed in his 1980 Turing Award lecture | Elliott 803 & the Elliott 503 |
| ALGOL 60 | 1962 | Roland Strobel | East Germany | Implemented by the Institute for Applied Mathematics, German Academy of Sciences at Berlin | Zeiss-Rechenautomat ZRA 1 |
| ALGOL 60 | 1962 | Bernard Vauquois, Louis Bolliet | France | Institut d'Informatique et Mathématiques Appliquées de Grenoble (IMAG) and Compagnie des Machines Bull | Bull Gamma 60 |
| Algol Translator | 1962 | G. van der Mey and W.L. van der Poel | Netherlands | Staatsbedrijf der Posterijen, Telegrafie en Telefonie | ZEBRA |
| Kidsgrove Algol | 1963 | F. G. Duncan | UK |   | English Electric Company KDF9 |
| SCALP | 1963 | Stephen J. Garland, Anthony W. Knapp, Thomas Eugene Kurtz | USA | *Self-Contained ALgol Processor* for a subset of ALGOL 60 | LGP-30 |
| VALGOL | 1963 | Val Schorre | USA | A test of the META II compiler compiler |   |
| FP6000 Algol | 1963 | Roger Moore | Canada | written for Saskatchewan Power Corp | FP6000 |
| Whetstone | 1964 | Brian Randell and Lawford John Russell | UK | Atomic Power Division of English Electric Company. Precursor to Ferranti Pegasus, National Physical Laboratories ACE and English Electric DEUCE implementations | English Electric Company KDF9 |
| ALGOL 60 | 1964 | Jean-Claude Boussard | France | Institut d'informatique et mathématiques appliquées de Grenoble | IBM 7090 |
| ALGOL-GENIUS | 1964 | Börje Langefors | Sweden | Added COBOL-inspired data records and I/O | Datasaab D-21 |
| ALGOL 60 | 1965 | Claude Pair | France | Centre de calcul de la Faculté des Sciences de Nancy | IBM 1620 |
| Dartmouth ALGOL | 1965 | Stephen J. Garland, Sarr Blumson, Ron Martin | USA | ALGOL 60 | Dartmouth Time-Sharing System for the GE 235 |
| NU ALGOL | 1965 |   | Norway |   | UNIVAC |
| ALGOL 60 | 1965 | F.E.J. Kruseman Aretz | Netherlands | MC compiler for the EL-X8 | Electrologica X8 |
| ALGEK | 1965 |   | Soviet Union | Minsk-22 | АЛГЭК, based on ALGOL 60 and COBOL support, for economical tasks |
| MALGOL | 1966 | publ. A. Viil, M Kotli & M. Rakhendi, | Estonian SSR | Minsk-22 |   |
| ALGAMS | 1967 | GAMS group (ГАМС, группа автоматизации программирования для машин среднего класса), cooperation of Comecon Academies of Science | Comecon | Minsk-22, later ES EVM, BESM |   |
| ALGOL/ZAM | 1967 |   | Poland |   | Polish ZAM computer |
| Chinese Algol | 1972 |   | China | Chinese characters, expressed via the Symbol system |   |
| DG/L | 1972 |   | USA |   | DG Eclipse family of Computers |
| NASE | 1990 | Erik Schoenfelder | Germany | Interpreter | Linux and MS Windows |
| MARST | 2000 | Andrew Makhorin | Russia | ALGOL 60 to C translator | All CPUs supported by the GNU Compiler Collection; MARST is part of the GNU project |

The Burroughs dialects included special system programming dialects such as ESPOL and NEWP.

## Properties

ALGOL 60 as officially defined had no I/O facilities; implementations defined their own in ways that were rarely compatible with each other. In contrast, ALGOL 68 offered an extensive library of *transput* (ALGOL 68 parlance for input/output) facilities.

ALGOL 60 provided two evaluation strategies for parameter passing: the common call-by-value, and call-by-name. The procedure declaration specified, for each formal parameter, which was to be used: *value* specified for call-by-value, and omitted for call-by-name. Call-by-name recomputes every parameter when it is used in an expression, so has certain effects in contrast to call-by-reference. For example, without specifying the parameters as *value* or *reference*, it is impossible to develop a procedure that will swap the values of two parameters if the actual parameters that are passed in are an integer variable and an array that is indexed by that same integer variable. Think of passing a pointer to swap(i, A[i]) in to a function. Now that every time swap is referenced, it's reevaluated. Say i := 1 and A[i] := 2, so every time swap is referenced it'll return the other combination of the values ([1,2], [2,1], [1,2] and so on). A similar situation occurs with a random function passed as actual argument.

Call-by-name is known by many compiler designers for the interesting "thunks" that are used to implement it. Donald Knuth devised the "man or boy test" to separate compilers that correctly implemented "recursion and non-local references." This test contains an example of call-by-name.

### Language levels

The ALGOL 60 reports recognize three different levels of language, i.e., a Reference Language, a Publication Language, and several Hardware Representations. The Reference and Publication languages have no reserved words, however the reports do recommend reserving some identifiers for standard functions. The Reference Language has lower case letters and other characters not available in the 6-bit character sets typical of ALGOL 60's era.

The reports briefly describe hardware representations. Implementations differ in their hardware representations of underlined independent basic symbols.

1. Reserved words
2. Stropping

They also differ in their hardware representation of delimiters.

### ALGOL 60 Reserved words and restricted identifiers

There are 24 basic symbols in the Modified Report that are words in boldface. Although those words are not reserved in the reference and publication languages, some hardware implementations may reserve them. There are 24 such words in the Modified Report:

- `**ARRAY**`
- `**BEGIN**`
- `**BOOLEAN**`
- `**COMMENT**`
- `**DO**`
- `**ELSE**`
- `**END**`
- `**FALSE**`
- `**FOR**`
- `**GOTO**`
- `**IF**`
- `**INTEGER**`
- `**LABEL**`
- `**OWN**`
- `**PROCEDURE**`
- `**REAL**`
- `**STEP**`
- `**STRING**`
- `**SWITCH**`
- `**THEN**`
- `**TRUE**`
- `**UNTIL**`
- `**VALUE**`
- `**WHILE**`

There are 35 such reserved words in the standard Burroughs Large Systems sub-language:

- `ALPHA`
- `ARRAY`
- `BEGIN`
- `BOOLEAN`
- `COMMENT`
- `CONTINUE`
- `DIRECT`
- `DO`
- `DOUBLE`
- `ELSE`
- `END`
- `EVENT`
- `FALSE`
- `FILE`
- `FOR`
- `FORMAT`
- `GO`
- `IF`
- `INTEGER`
- `LABEL`
- `LIST`
- `LONG`
- `OWN`
- `POINTER`
- `PROCEDURE`
- `REAL`
- `STEP`
- `SWITCH`
- `TASK`
- `THEN`
- `TRUE`
- `UNTIL`
- `VALUE`
- `WHILE`
- `ZIP`

There are 71 such restricted identifiers in the standard Burroughs Large Systems sub-language:

- `ACCEPT`
- `AND`
- `ATTACH`
- `BY`
- `CALL`
- `CASE`
- `CAUSE`
- `CLOSE`
- `DEALLOCATE`
- `DEFINE`
- `DETACH`
- `DISABLE`
- `DISPLAY`
- `DIV`
- `DUMP`
- `ENABLE`
- `EQL`
- `EQV`
- `EXCHANGE`
- `EXTERNAL`
- `FILL`
- `FORWARD`
- `GEQ`
- `GTR`
- `IMP`
- `IN`
- `INTERRUPT`
- `IS`
- `LB`
- `LEQ`
- `LIBERATE`
- `LINE`
- `LOCK`
- `LSS`
- `MERGE`
- `MOD`
- `MONITOR`
- `MUX`
- `NEQ`
- `NO`
- `NOT`
- `ON`
- `OPEN`
- `OR`
- `OUT`
- `PICTURE`
- `PROCESS`
- `PROCURE`
- `PROGRAMDUMP`
- `RB`
- `READ`
- `RELEASE`
- `REPLACE`
- `RESET`
- `RESIZE`
- `REWIND`
- `RUN`
- `SCAN`
- `SEEK`
- `SET`
- `SKIP`
- `SORT`
- `SPACE`
- `SWAP`
- `THRU`
- `TIMES`
- `TO`
- `WAIT`
- `WHEN`
- `WITH`
- `WRITE`

and also the names of all the intrinsic functions.

#### Standard operators

| Priority | Operator |   |
|---|---|---|
| first arithmetic | first | ↑ (power) |
| second | ×, / (real), ÷ (integer) |   |
| third | +, - |   |
| second | <, ≤, =, ≥, >, ≠ |   |
| third | ¬ (not) |   |
| fourth | ∧ (and) |   |
| fifth | ∨ (or) |   |
| sixth | ⊃ (implication) |   |
| seventh | ≡ (equivalence) |   |

## Examples and portability issues

### Code sample comparisons

#### ALGOL 60

```
procedure Absmax(a) Size:(n, m) Result:(y) Subscripts:(i, k);
    value n, m; array a; integer n, m, i, k; real y;
comment The absolute greatest element of the matrix a, of size n by m,
    is copied to y, and the subscripts of this element to i and k;
begin
    integer p, q;
    y := 0; i := k := 1;
    for p := 1 step 1 until n do
        for q := 1 step 1 until m do
            if abs(a[p, q]) > y then
                begin y := abs(a[p, q]);
                    i := p; k := q
                end
end Absmax;
```

Implementations differ in how the text in bold must be written. For example, the word 'INTEGER', including the quotation marks, must be used in some implementations in place of **integer**, above, thereby designating it as a special ALGOL symbol.

The following version uses the hardware representation supported by the ALCOR compiler for the IBM 7090. The ALGOL symbols are stropped. Additionally, it uses `..` to represent the colon character, `.=` for assignment, `(/ and )/` instead of brackets, and `.,` for semicolon. Lower case characters were not supported, so upper case is used:

```
'PROCEDURE' ABSMAX(A) SIZE..(N, M) RESULT..(Y) SUBSCRIPTS..(I, K).,
    'VALUE' N, M., 'ARRAY' A., 'INTEGER' N, M, I, K., 'REAL' Y.,
'COMMENT' THE ABSOLUTE GREATEST ELEMENT OF THE MATRIX A, OF SIZE N BY M,
    IS COPIED TO Y, AND THE SUBSCRIPTS OF THIS ELEMENT TO I AND K.,
'BEGIN'
    'INTEGER' P, Q.,
    Y .= 0; I .= K .= 1.,
    'FOR' P .= 1 'STEP' 1 'UNTIL' N 'DO'
        'FOR' Q .= 1 'STEP' 1 'UNTIL' M 'DO'
            'IF' ABS(A(/P, Q/)) 'GREATER' Y 'THEN'
                'BEGIN' Y .= ABS(A(/P, Q/)).,
                    I .= P; K .= Q
                'END'
'END' ABSMAX.,
```

Following is an example of how to produce a table using Elliott 803 ALGOL:

```
 FLOATING POINT ALGOL TEST'
 BEGIN REAL A,B,C,D'

 READ D'

 FOR A:= 0.0 STEP D UNTIL 6.3 DO
 BEGIN
   PRINT PUNCH(3),££L??'
   B := SIN(A)'
   C := COS(A)'
   PRINT PUNCH(3),SAMELINE,ALIGNED(1,6),A,B,C'
 END'
 END'
```

#### ALGOL 60 family

Since ALGOL 60 had no I/O facilities, there is no portable hello world program in ALGOL. The following program could (and still will) compile and run on an ALGOL implementation for a Unisys A-Series mainframe, and is a straightforward simplification of code taken from The Language Guide at the University of Michigan-Dearborn Computer and Information Science Department Hello world! ALGOL Example Program page.

```
BEGIN
  FILE F(KIND=REMOTE);
  EBCDIC ARRAY E[0:11];
  REPLACE E BY "HELLO WORLD!";
  WRITE(F, *, E);
END.
```

Where * etc. represented a format specification as used in FORTRAN, e.g.

A simpler program using an inline format:

```mw
 BEGIN
   FILE F(KIND=REMOTE);
   WRITE(F, <"HELLO WORLD!">);
 END.
```

An even simpler program using the Display statement:

```mw
BEGIN DISPLAY("HELLO WORLD!") END.
```

An alternative example, using Elliott Algol I/O is as follows. Elliott Algol used different characters for "open-string-quote" and "close-string-quote", represented here by   ‘  and   ’ .

```mw
 program HiFolks;
 begin
    print ‘Hello world’
 end;
```

Here's a version for the Elliott 803 Algol (A104) The standard Elliott 803 used 5-hole paper tape and thus only had upper case. The code lacked any quote characters so £ (pound sign) was used for open quote and ? (question mark) for close quote. Special sequences were placed in double quotes (e.g£., L?? produced a new line on the teleprinter).

```
  HIFOLKS'
  BEGIN
     PRINT £HELLO WORLD£L??'
  END'
```

The ICT 1900 series Algol I/O version allowed input from paper tape or punched card. Paper tape 'full' mode allowed lower case. Output was to a line printer. Note use of '(', ')', and %.

```
  'PROGRAM' (HELLO)
  'BEGIN'
     'COMMENT' OPEN QUOTE IS '(', CLOSE IS ')', PRINTABLE SPACE HAS TO
               BE WRITTEN AS % BECAUSE SPACES ARE IGNORED;
     WRITE TEXT('('HELLO%WORLD')');
  'END'
  'FINISH'
```

This example uses the `outstring` procedure as defined in the Modified Report:

```
 begin
   comment Uses I/O from the Modified Report.  It compiles and runs with the gnu marst compiler;
   outstring (1, "hello world!\n")
 end
```

## LEAP

LEAP is an extension to the ALGOL 60 programming language which provides an associative memory of triples. The three items in a triple denote the association that an Attribute of an Object has a specific Value. LEAP was created by Jerome Feldman (University of California Berkeley) and Paul Rovner (MIT Lincoln Lab) in 1967. LEAP was also implemented in SAIL.
