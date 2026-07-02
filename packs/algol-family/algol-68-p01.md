---
title: "ALGOL 68 (part 1/2)"
source: https://en.wikipedia.org/wiki/ALGOL_68
domain: algol-family
license: CC-BY-SA-4.0
tags: algol language, john backus, imperative programming, structured programming, backus naur form
fetched: 2026-07-02
part: 1/2
---

# ALGOL 68

**ALGOL 68** (short for *Algorithmic Language 1968*) is an imperative programming language member of the ALGOL family that was conceived as a successor to the ALGOL 60 language, designed with the goal of a much wider scope of application and more rigorously defined syntax and semantics.

The complexity of the language's definition, which runs to several hundred pages filled with non-standard terminology, made compiler implementation difficult and it was said it had "no implementations and no users". This was only partly true; ALGOL 68 did find use in several niche markets, notably in the United Kingdom where it was popular on International Computers Limited (ICL) machines, and in teaching roles. Outside these fields, use was relatively limited.

Nevertheless, the contributions of ALGOL 68 to the field of computer science have been deep, wide-ranging and enduring, although many of these contributions were only publicly identified when they had reappeared in subsequently developed programming languages. Many languages were developed specifically as a response to the perceived complexity of the language, the most notable being Pascal, or were reimplementations for specific roles, like Ada.

Many languages of the 1970s trace their design specifically to ALGOL 68, selecting some features while abandoning others that were considered too complex or out-of-scope for given roles. Most modern languages trace at least some of their syntax to either C or Pascal, and thus directly or indirectly to ALGOL 68.


## Overview

ALGOL 68 features include expression-based syntax, user-declared types and structures/tagged-unions, a reference model of variables and reference parameters, string, array and matrix slicing, and concurrency.

ALGOL 68 was designed by the International Federation for Information Processing (IFIP) IFIP Working Group 2.1 on Algorithmic Languages and Calculi. On 20 December 1968, the language was formally adopted by the group, and then approved for publication by the General Assembly of IFIP.

ALGOL 68 was defined using a formalism, a two-level formal grammar, invented by Adriaan van Wijngaarden. Van Wijngaarden grammars use a context-free grammar to generate an infinite set of productions that will recognize a particular ALGOL 68 program; notably, they are able to express the kind of requirements that in many other programming language technical standards are labelled *semantics*, and must be expressed in ambiguity-prone natural language prose, and then implemented in compilers as *ad hoc* code attached to the formal language parser.

> ALGOL 68 was the first (and possibly one of the last) major language for which a full formal definition was made before it was implemented.

—

C. H. A. Koster

The main aims and principles of design of ALGOL 68 are:

1. Completeness and clarity of description
2. Orthogonality of design
3. Security
4. Efficiency:
  - Static mode checking
  - Mode-independent parsing
  - Independent compiling
  - Loop optimizing
  - Representations – in minimal & larger character sets

ALGOL 68 has been criticized, most prominently by some members of its design committee such as C. A. R. Hoare and Edsger Dijkstra, for abandoning the simplicity of ALGOL 60, becoming a vehicle for complex or overly general ideas, and doing little to make the compiler writer's task easier, in contrast to deliberately simple contemporaries (and competitors) such as C, S-algol and Pascal.

In 1970, ALGOL 68-R became the first working compiler for ALGOL 68.

In the 1973 revision, certain features — such as proceduring, gommas and formal bounds — were omitted. Cf. The language of the unrevised report.r0

Though European defence agencies (in Britain Royal Signals and Radar Establishment (RSRE)) promoted the use of ALGOL 68 for its expected security advantages, the American side of the NATO alliance decided to develop a different project, the language Ada, making its use obligatory for US defense contracts.

ALGOL 68 also had a notable influence in the Soviet Union, details of which can be found in Andrey Terekhov's 2014 paper: "ALGOL 68 and Its Impact on the USSR and Russian Programming", and "Алгол 68 и его влияние на программирование в СССР и России".

Steve Bourne, who was on the ALGOL 68 revision committee, took some of its ideas to his Bourne shell (and thereby, to descendant Unix shells such as Bash) and to C (and thereby to descendants such as C++). The source of Bourne shell, while written in C, uses macros to make it look more like ALGOL. This has been nicknamed "Bournegol".

The complete history of the project can be found in C. H. Lindsey's "A History of ALGOL 68".

For a full-length treatment of the language, see "Programming ALGOL 68 Made Easy" by Dr. Sian Mountbatten, or "Learning ALGOL 68 Genie" by Marcel van der Veer which includes the Revised Report.


## History

### Origins

ALGOL 68, as the name implies, is a follow-on to the ALGOL language that was first formalized in 1960. That same year the International Federation for Information Processing (IFIP) formed and started the Working Group on ALGOL, or WG2.1. This group released an updated ALGOL 60 specification in Rome in April 1962. At a follow-up meeting in March 1964, it was agreed that the group should begin work on two follow-on standards, ALGOL X, which would be a redefinition of the language with some additions, and ALGOL Y, which would have the ability to modify its own programs in the style of the language LISP.

### Definition process

The first meeting of the ALGOL X group was held in Princeton University in May 1965. A report of the meeting noted two broadly supported themes, the introduction of strong typing and interest in Euler's concepts of 'trees' or 'lists' for handling collections. Although intended as a "short-term solution to existing difficulties", ALGOL X got as far as having a compiler made for it. This compiler was written by Douglas T. Ross of the Massachusetts Institute of Technology (MIT) with the *Automated Engineering Design* (AED-0) system, also termed *ALGOL Extended for Design*.

At the second meeting in October in France, three formal proposals were presented, Niklaus Wirth's ALGOL W along with comments about record structures by C.A.R. (Tony) Hoare, a similar language by Gerhard Seegmüller, and a paper by Adriaan van Wijngaarden on "Orthogonal design and description of a formal language". The latter, written in almost indecipherable "W-Grammar", proved to be a decisive shift in the evolution of the language. The meeting closed with an agreement that van Wijngaarden would re-write the Wirth/Hoare submission using his W-Grammar.

This seemingly simple task ultimately proved more difficult than expected, and the follow-up meeting had to be delayed six months. When it met in April 1966 in Kootwijk, van Wijngaarden's draft remained incomplete and Wirth and Hoare presented a version using more traditional descriptions. It was generally agreed that their paper was "the right language in the wrong formalism". As these approaches were explored, it became clear there was a difference in the way parameters were described that would have real-world effects, and while Wirth and Hoare protested that further delays might become endless, the committee decided to wait for van Wijngaarden's version. Wirth then implemented their current definition as ALGOL W.

At the next meeting in Warsaw in October 1966, there was an initial report from the I/O Subcommittee who had met at the Oak Ridge National Laboratory and the University of Illinois but had not yet made much progress. The two proposals from the previous meeting were again explored, and this time a new debate emerged about the use of pointers; ALGOL W used them only to refer to records, while van Wijngaarden's version could point to any object. To add confusion, John McCarthy presented a new proposal for operator overloading and the ability to string together *and* and *or* constructs, and Klaus Samelson wanted to allow anonymous functions. In the resulting confusion, there was some discussion of abandoning the entire effort. The confusion continued through what was supposed to be the ALGOL Y meeting in Zandvoort in May 1967.

### Publication

A draft report was finally published in February 1968. This was met by "shock, horror and dissent", mostly due to the hundreds of pages of unreadable grammar and odd terminology. Charles H. Lindsey attempted to figure out what "language was hidden inside of it", a process that took six man-weeks of effort. The resulting paper, "ALGOL 68 with fewer tears", was widely circulated. At a wider information processing meeting in Zürich in May 1968, attendees complained that the language was being forced upon them and that IFIP was "the true villain of this unreasonable situation" as the meetings were mostly closed and there was no formal feedback mechanism. Wirth and Peter Naur formally resigned their authorship positions in WG2.1 at that time.

The next WG2.1 meeting took place in Tirrenia in June 1968. It was supposed to discuss the release of compilers and other issues, but instead devolved into a discussion on the language. van Wijngaarden responded by saying (or threatening) that he would release only one more version of the report. By this point Naur, Hoare, and Wirth had left the effort, and several more were threatening to do so. Several more meetings followed, North Berwick in August 1968, Munich in December which produced the release of the official Report in January 1969 but also resulted in a contentious Minority Report being written. Finally, at Banff, Alberta in September 1969, the project was generally considered complete and the discussion was primarily on errata and a greatly expanded Introduction to the Report.

The effort took five years, burned out many of the greatest names in computer science, and on several occasions became deadlocked over issues both in the definition and the group as a whole. Hoare released a "Critique of ALGOL 68" almost immediately, which has been widely referenced in many works. Wirth went on to further develop the ALGOL W concept and released this as Pascal in 1970.

### Implementations

#### ALGOL 68-R

The first implementation of the standard, based on the late-1968 draft Report, was introduced by the Royal Radar Establishment in the UK as ALGOL 68-R in July 1970. This was, however, a subset of the full language, and Barry Mailloux, the final editor of the Report, joked that "It is a question of morality. We have a Bible and you are sinning!" This version nevertheless became very popular on the ICL machines, and became a widely used language in military coding, especially in the UK.

Among the changes in 68-R was the requirement for all variables to be declared before their first use. This had a significant advantage that it allowed the compiler to be one-pass, as space for the variables in the activation record was set aside before it was used. However, this change also had the side-effect of demanding the **PROC**s be declared twice, once as a declaration of the types, and then again as the body of code. Another change was to eliminate the assumed **VOID** mode, an expression that returns no value (named a *statement* in other languages) and demanding the word **VOID** be added where it would have been assumed. Further, 68-R eliminated the explicit parallel processing commands based on **PAR**.

#### Others

The first full implementation of the language was introduced in 1974 by CDC Netherlands for the Control Data mainframe series. This saw limited use, mostly teaching in Germany and the Netherlands.

A version similar to 68-R was introduced from Carnegie Mellon University in 1976 as 68S, and was again a one-pass compiler based on various simplifications of the original and intended for use on smaller machines like the DEC PDP-11. It too was used mostly for teaching purposes.

A version for IBM mainframes did not become available until 1978, when one was released from Cambridge University. This was "nearly complete". Lindsey released a version for small machines including the IBM PC in 1984.

Three open source Algol 68 implementations are known:

- **a68g**, GPLv3, written by Marcel van der Veer.
- **algol68toc**, an open-source software port of ALGOL 68RS.
- **ga68**, a frontend for GCC, written by Jose E. Marchesi.

### Timeline

| Year | Event | Contributor |
|---|---|---|
| March 1959 | ALGOL Bulletin Issue 1 (First) | Peter Naur / ACM |
| February 1968 | Draft Report(DR) Published | IFIP Working Group 2.1 |
| March 1968 | Algol 68 Final Reportr0 Presented at Munich Meeting | IFIP Working Group 2.1 |
| June 1968 | Meeting in Tirrenia, Italy | IFIP Working Group 2.1 |
| Aug 1968 | Meeting in North Berwick, Scotland | IFIP Working Group 2.1 |
| December 1968 | ALGOL 68 Final Reportr0 Presented at Munich Meeting | IFIP Working Group 2.1 |
| April 1970 | ALGOL 68-R under GEORGE 3 on an ICL 1907F | Royal Signals and Radar Est. |
| July 1970 | ALGOL 68 for the Dartmouth Time-Sharing System | Sidney Marshall |
| September 1973 | Algol 68 Revised Reportr1 Published | IFIP Working Group 2.1 |
| 1975 | ALGOL 68C(C) – transportable compiler (zcode VM) | S. Bourne, Andrew Birrell, and Michael Guy |
| June 1975 | G. E. Hedrick and Alan Robertson. The Oklahoma State ALGOL 68 Subset Compiler. 1975 International Conference on ALGOL 68. |   |
| June 1977 | Strathclyde ALGOL 68 conference, Scotland | ACM |
| May 1978 | Proposals for ALGOL H – A Superlanguage of ALGOL 68 | A. P. Black, V. J. Rayward-Smith |
| 1984 | Full ALGOL 68S(S) compiler for Sun, SPARC, and PCs | C. H. Lindsey et al, Manchester |
| August 1988 | ALGOL Bulletin Issue 52 (last) | Ed. C. H. Lindsey / ACM |
| May 1997 | Algol68 S(S) published on the internet | Charles H. Lindsey |
| November 2001 | Algol 68 Genie(G) published on the internet (GNU GPL open source licensing) | Marcel van der Veer |
| January 2025 | GCC Front-End (GNU GPL) | Jose E. Marchesi |

- "A Shorter History of Algol 68"
- ALGOL 68 – 3rd generation ALGOL

### The Algorithmic Language ALGOL 68 Reports and Working Group members

- March 1968: Draft Report on the Algorithmic Language ALGOL 68 – Edited by: Adriaan van Wijngaarden, Barry J. Mailloux, John Peck and Cornelis H. A. Koster.

> "Van Wijngaarden once characterized the four authors, somewhat tongue-in-cheek, as: Koster: transputter, Peck: syntaxer, Mailloux: implementer, Van Wijngaarden: party ideologist." – Koster.

- October 1968: Penultimate Draft Report on the Algorithmic Language ALGOL 68 — Chapters 1–9 Chapters 10–12 — Edited by: A. van Wijngaarden, B.J. Mailloux, J. E. L. Peck and C. H. A. Koster.
- December 1968: Report on the Algorithmic Language ALGOL 68 — Offprint from Numerische Mathematik, 14, 79–218 (1969); Springer-Verlag. — Edited by: A. van Wijngaarden, B. J. Mailloux, J. E. L. Peck and C. H. A. Koster.
- March 1970: Minority report, ALGOL Bulletin AB31.1.1 — signed by Edsger Dijkstra, Fraser Duncan, Jan Garwick, Tony Hoare, Brian Randell, Gerhard Seegmüller, Wlad Turski, and Mike Woodger.
- September 1973: Revised Report on the Algorithmic Language Algol 68 — Springer-Verlag 1976 — Edited by: A. van Wijngaarden, B. Mailloux, J. Peck, K. Koster, Michel Sintzoff, Charles H. Lindsey, Lambert Meertens and Richard G. Fisker.
- other WG 2.1 members active in ALGOL 68 design: Friedrich L. Bauer • Hans Bekic • Gerhard Goos • Peter Zilahy Ingerman • Peter Landin • John McCarthy • Jack Merner • Peter Naur • Manfred Paul • Willem van der Poel • Doug Ross • Klaus Samelson • Niklaus Wirth • Nobuo Yoneda.

### Timeline of standardization

1968: On 20 December 1968, the "Final Report" (MR 101) was adopted by the Working Group, then subsequently approved by the General Assembly of UNESCO's IFIP for publication. Translations of the standard were made for Russian, German, French and Bulgarian, and then later Japanese and Chinese. The standard was also made available in Braille.

1984: TC 97 considered ALGOL 68 for standardisation as "New Work Item" TC97/N1642 [1][2]. West Germany, Belgium, Netherlands, USSR and Czechoslovakia willing to participate in preparing the standard but the USSR and Czechoslovakia "were not the right kinds of member of the right ISO committees"[3] and Algol 68's ISO standardisation stalled.[4]

1988: Subsequently ALGOL 68 became one of the GOST standards in Russia.

- GOST 27974-88 Programming language ALGOL 68 — Язык программирования АЛГОЛ 68
- GOST 27975-88 Programming language ALGOL 68 extended — Язык программирования АЛГОЛ 68 расширенный


## Notable language elements

### Bold symbols and reserved words

The standard language contains about sixty reserved words, typically bolded in print, and some with "brief symbol" equivalents:

```
MODE, OP, PRIO, PROC,
FLEX, HEAP, LOC, LONG, REF, SHORT,
BITS, BOOL, BYTES, CHAR, COMPL, INT, REAL, SEMA, STRING, VOID,
CHANNEL, FILE, FORMAT, STRUCT, UNION,
AT "@", EITHERr0, IS ":=:", ISNT  IS NOTr0 ":/=:" ":≠:", OF "→"r0, TRUE, FALSE, EMPTY, NIL "○", SKIP "~",
CO "¢", COMMENT "¢", PR, PRAGMAT,
CASE ~ IN ~ OUSE ~ IN ~ OUT ~ ESAC "( ~ | ~ |: ~ | ~ | ~ )",
FOR ~ FROM ~ TO ~ BY ~ WHILE ~ DO ~ OD,
IF ~ THEN ~ ELIF ~ THEN ~ ELSE ~ FI "( ~ | ~ |: ~ | ~ | ~ )",
PAR BEGIN ~ END "( ~ )", GO TO, GOTO, EXIT "□"r0.
```

### Units: Expressions

The basic language construct is the *unit*. A unit may be a *formula*, an *enclosed clause*, a *routine text* or one of several technically needed constructs (assignation, jump, skip, nihil). The technical term *enclosed clause* unifies some of the inherently bracketing constructs known as *block*, *do statement*, *switch statement* in other contemporary languages. When keywords are used, generally the reversed character sequence of the introducing keyword is used for terminating the enclosure, e.g. ( **IF** ~ **THEN** ~ **ELSE** ~ **FI**, **CASE** ~ **IN** ~ **OUT** ~ **ESAC**, **FOR** ~ **WHILE** ~ **DO** ~ **OD** ). This Guarded Command syntax was reused by Stephen Bourne in the common Unix Bourne shell. An expression may also yield a *multiple value*, which is constructed from other values by a *collateral clause*. This construct just looks like the parameter pack of a procedure call.

### mode: Declarations

The basic data types (called `mode`s in Algol 68 parlance) are `real`, `int`, `compl` (complex number), `bool`, `char`, `bits` and `bytes`. For example:

```
INT n = 2;
CO n is fixed as a constant of 2. CO
INT m := 3;
CO m is a newly created local variable whose value is initially set to 3. CO
CO    This is short for ref int m = loc int := 3; CO
REAL avogadro = 6.0221415⏨23; CO Avogadro number CO
long long real long long pi = 3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510;
COMPL square root of minus one = 0 ⊥ 1;
```

However, the declaration `**REAL** x;` is just syntactic sugar for `**REF** **REAL** x = **LOC** **REAL**;`. That is, `x` is really the *constant identifier* for a *reference to* a newly generated local **REAL** variable.

Furthermore, instead of defining both `float` and `double`, or `int` and `long` and `short`, etc., ALGOL 68 provides *modifiers*, so that the presently common `double` would be written as **LONG** **REAL** or **LONG** **LONG** **REAL** instead, for example. The *prelude constants* `max real` and `min long int` are provided to adapt programs to different implementations.

All variables need to be declared, but declaration does not have to precede the first use.

primitive-declarer: **INT**, **REAL**, **COMPL**, **COMPLEX**G, **BOOL**, **CHAR**, **STRING**, **BITS**, **BYTES**, **FORMAT**, **FILE**, **PIPE**G, **CHANNEL**, **SEMA**

- **BITS** – a "packed vector" of **BOOL**.
- **BYTES** – a "packed vector" of **CHAR**.
- **STRING** – a **FLEX**ible array of **CHAR**.
- **SEMA** – a **SEMA**phore which can be initialised with the **OP**erator **LEVEL**.

Complex types can be created from simpler ones using various type constructors:

- **REF** *mode* – a reference to a value of type *mode*, similar to **&** in C/C++ and **REF** in Pascal
- **STRUCT** – used to build structures, like **STRUCT** in C/C++ and **RECORD** in Pascal
- **UNION** – used to build unions, like in C/C++ and Pascal
- **PROC** – used to specify procedures, like functions in C/C++ and procedures/functions in Pascal

Other declaration symbols include: **FLEX**, **HEAP**, **LOC**, **REF**, **LONG**, **SHORT**, **EVENT**S

- **FLEX** – declare the array to be flexible, i.e. it can grow in length on demand.
- **HEAP** – allocate variable some free space from the global heap.
- **LOC** – allocate variable some free space of the local stack.
- **LONG** – declare an **INT**, **REAL** or **COMPL** to be of a **LONG**er size.
- **SHORT** – declare an **INT**, **REAL** or **COMPL** to be of a **SHORT**er size.

A name for a mode (type) can be declared using a **MODE** declaration, which is similar to **TYPEDEF** in C/C++ and **TYPE** in Pascal:

```
 INT max=99;
 MODE NEWMODE = [0:9][0:max]STRUCT (
     LONG REAL a, b, c, SHORT INT i, j, k, REF REAL r
 );
```

This is similar to the following C code:

```mw
  const int max=99;
  typedef struct {
      double a, b, c; short i, j, k; float *r;
  } newmode[9+1][max+1];
```

For ALGOL 68, only the **NEWMODE** mode-indication appears to the left of the equals symbol, and most notably the construction is made, and can be read, from left to right without regard to priorities. Also, the **lower bound** of Algol 68 arrays is one by default, but can be any integer from -*max int* to *max int*.

Mode declarations allow types to be recursive: defined directly or indirectly in terms of themselves. This is subject to some restrictions – for instance, these declarations are illegal:

```
 MODE A = REF A
 MODE A = STRUCT (A a, B b)
 MODE A = PROC (A a) A
```

while these are valid:

```
 MODE A = STRUCT (REF A a, B b)
 MODE A = PROC (REF A a) REF A
```

### Coercions: casting

The coercions produce a coercee from a coercend according to three criteria: the a priori mode of the coercend before the application of any coercion, the a posteriori mode of the coercee required after those coercions, and the syntactic position or "sort" of the coercee. Coercions may be cascaded.

The six possible coercions are termed *deproceduring*, *dereferencing*, *uniting*, *widening*, *rowing*, and *voiding*. Each coercion, except for *uniting*, prescribes a corresponding dynamic effect on the associated values. Hence, many primitive actions can be programmed implicitly by coercions.

Context strength – allowed coercions:

- soft – deproceduring
- weak – dereferencing or deproceduring, yielding a name
- meek – dereferencing or deproceduring
- firm – meek, followed by uniting
- strong – firm, followed by widening, rowing or voiding

#### Coercion hierarchy with examples

ALGOL 68 has a hierarchy of contexts which determine the kind of coercions available at a particular point in the program. These contexts are:

| Context | Context location | Coercions available | Coercion examples in the context |   |   |   |   |
|---|---|---|---|---|---|---|---|
| **Soft** | **Weak** | **Meek** | **Firm** | **Strong** |   |   |   |
| **Strong** | Right hand side of: Identity-declarations, as "~" in: `**REAL** x = ~` Initialisations, as "~" in: `**REAL** x := ~` Also: Actual-parameters of calls, as "~" in:`**PROC**: sin(~)` Enclosed clauses of casts, as "~" in: `**REAL**(~)` Units of routine-texts Statements yielding **VOID** All parts (but one) of a balanced clause One side of an identity relation, as "~" in: `~ **IS** ~` | deproceduring | All **SOFT** then weak dereferencing (dereferencing or deproceduring, yielding a name) | All **WEAK** then dereferencing (dereferencing or deproceduring) | All **MEEK** then uniting | All **FIRM** then widening, rowing or voiding | Widening is always applied in the **INT** to **REAL** to **COMPL** direction, provided the modes have the same size. For example: An **INT** will be coerced to a **REAL**, but not vice versa. Examples: to **REAL** from **INT** to **COMPL** from **REAL** to []**BOOL** from **BITS** to []**CHAR** from **BYTES** A coercend can also be coerced (rowed) to a multiple of length 1. For example: to [1]**INT** from **INT** to [1]**REAL** from **REAL** etc. |
| **Firm** | Operands of formulas as "~" in:`~ **OP** ~` Parameters of transput calls | Example: `**UNION**(**INT**,**REAL**) var := 1` |   |   |   |   |   |
| **Meek** | Trimscripts (yielding **INT**) Enquiries: e.g. as "~" in the following `**IF** ~ **THEN** ... **FI**` and `**FROM** ~ **BY** ~ **TO** ~ **WHILE** ~ **DO** ... **OD** etc` Primaries of calls (e.g. sin in sin(x)) | Examples: to **BOOL** from **REF** **REF** **BOOL** to **INT** from **REF** **REF** **REF** **INT** |   |   |   |   |   |
| **Weak** | Primaries of slices, as in "~" in: `~[1:99]` Secondaries of selections, as "~" in: `value **OF** ~` | Examples: to **REF** **INT** from **REF** **REF** **INT** to **REF** **REAL** from **REF** **REF** **REF** **REAL** to **REF** **STRUCT** from **REF** **REF** **REF** **REF** **STRUCT** |   |   |   |   |   |
| **Soft** | The LHS of assignments, as "~" in: `~ := ...` | Example: deproceduring of: `**PROC** **REAL** random: e.g. random` |   |   |   |   |   |

For more details about Primaries, Secondaries, Tertiary & Quaternaries refer to Operator precedence.

Pragmats (from "pragmatic remarks") are directives in the program, typically hints to the compiler; in newer languages these are called "pragmas" (no 't'). e.g.

```
PRAGMAT heap=32 PRAGMAT
PR heap=32 PR
```

Comments can be inserted in a variety of ways:

```
¢ The original way of adding your 2 cents worth to a program ¢
COMMENT "bold" comment COMMENT
CO Style i comment CO
# Style ii comment #
£ This is a hash/pound comment for a UK keyboard £
```

Normally, comments cannot be nested in ALGOL 68. This restriction can be circumvented by using different comment delimiters (e.g. use hash only for temporary code deletions).

### Expressions and compound statements

ALGOL 68 being an expression-oriented programming language, the value returned by an assignment statement is a reference to the destination. Thus, the following is valid ALGOL 68 code:

```
 REAL half pi, one pi; one pi := 2 * ( half pi := 2 * arc tan(1) )
```

This notion is present in C and Perl, among others. Note that as in earlier languages such as Algol 60 and FORTRAN, spaces are allowed in identifiers, so that `half pi` is a *single* identifier (thus avoiding the *underscores* versus *camel case* versus *all lower-case* issues).

As another example, to express the mathematical idea of a *sum* of `f(i)` from i=1 to n, the following ALGOL 68 *integer expression* suffices:

```
 (INT sum := 0; FOR i TO n DO sum +:= f(i) OD; sum)
```

Note that, being an integer expression, the former block of code can be used in *any context where an integer value can be used*. A block of code returns the value of the last expression it evaluated; this idea is present in Lisp, among other languages.

Compound statements are all terminated by distinctive closing brackets:

- **IF** choice clauses:

```
 IF condition THEN statements [ ELSE statements ] FI
 "brief" form:  ( condition | statements | statements )
```

```
 IF condition1 THEN statements ELIF condition2 THEN statements [ ELSE statements ] FI
 "brief" form:  ( condition1 | statements |: condition2 | statements | statements )
```

This scheme not only avoids the dangling else problem but also avoids having to use `**BEGIN**` and `**END**` in embedded statement sequences.

- **CASE** choice clauses:

```
 CASE switch IN statements, statements,... [ OUT statements ] ESAC
 "brief" form:  ( switch | statements,statements,... | statements )
```

```
 CASE switch1 IN statements, statements,... OUSE switch2 IN statements, statements,... [ OUT statements ] ESAC
 "brief" form of CASE statement:  ( switch1 | statements,statements,... |: switch2 | statements,statements,... | statements )
```

Choice clause example with *Brief* symbols:

```
PROC days in month = (INT year, month)INT:
  (month|
    31,
    (year÷×4=0 ∧ year÷×100≠0  ∨  year÷×400=0 | 29 | 28 ),
    31, 30, 31, 30, 31, 31, 30, 31, 30, 31
  );
```

Choice clause example with *Bold* symbols:

```
PROC days in month = (INT year, month)INT:
  CASE month IN
    31,
    IF year MOD 4 EQ 0 AND year MOD 100 NE 0  OR  year MOD 400 EQ 0 THEN 29 ELSE 28 FI,
    31, 30, 31, 30, 31, 31, 30, 31, 30, 31
  ESAC;
```

Choice clause example mixing *Bold* and *Brief* symbols:

```
PROC days in month = (INT year, month)INT:
  CASE month IN
¢Jan¢ 31,
¢Feb¢ ( year MOD 4 = 0 AND year MOD 100 ≠ 0  OR  year MOD 400 = 0 | 29 | 28 ),
¢Mar¢ 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ¢ to Dec. ¢
  ESAC;
```

Algol68 allowed the switch to be of either type **INT** *or* (uniquely) **UNION**. The latter allows the enforcing strong typing onto **UNION** variables. cf. **union** below for example.

- **do** loop clause:

```
 [ FOR index ] [ FROM first ] [ BY increment ] [ TO last ] [ WHILE condition ] DO statements OD
 The minimum form of a "loop clause" is thus: DO statements OD
```

This was considered *the* "universal" loop, the full syntax is:

```
FOR i FROM 1 BY -22 TO -333 WHILE i×i≠4444 DO ~ OD
```

The construct has several unusual aspects:

- only the ***DO** ~ **OD*** portion was compulsory, in which case the loop will iterate indefinitely.
- thus the clause ***TO** 100 **DO** ~ **OD***, will iterate only 100 times.
- the **WHILE** "syntactic element" allowed a programmer to break from a **FOR** loop early. e.g.

```
INT sum sq:=0;
FOR i
WHILE
  print(("So far:",i,newline));
  sum sq≠70↑2
DO
  sum sq+:=i↑2
OD
```

Subsequent "extensions" to the standard Algol68 allowed the **TO** syntactic element to be replaced with **UPTO** and **DOWNTO** to achieve a small optimisation. The same compilers also incorporated:

- **UNTIL**(C) – for late loop termination.
- **FOREACH**(S) – for working on arrays in parallel.

Further examples can be found in the code examples below.

### struct, union & `[:]`: Structures, unions and arrays

ALGOL 68 supports arrays with any number of dimensions, and it allows for the *slicing* of whole or partial rows or columns.

```
 MODE VECTOR = [1:3]    REAL;   # vector MODE declaration (typedef)  #
 MODE MATRIX = [1:3,1:3]REAL;   # matrix MODE declaration (typedef)  #
 VECTOR v1  := (1,2,3);         # array variable initially (1,2,3)   #
 []REAL v2   = (4,5,6);         # constant array, type equivalent to VECTOR, bounds are implied  #
 OP + = (VECTOR a,b) VECTOR:    # binary OPerator definition         #
   (VECTOR out; FOR i FROM ⌊a TO ⌈a DO out[i] := a[i]+b[i] OD; out);
 MATRIX m := (v1, v2, v1+v2);
 print ((m[,2:]));              # a slice of the 2nd and 3rd columns #
```

Matrices can be sliced either way, e.g.:

```
 REF VECTOR row = m[2,];  # define a REF (pointer) to the 2nd row #
 REF VECTOR col = m[,2];  # define a REF (pointer) to the 2nd column #
```

ALGOL 68 supports multiple field structures (**STRUCT**) and **united modes**. Reference variables may point to any **MODE** including array slices and structure fields.

For an example of all this, here is the traditional linked list declaration:

```
 MODE NODE = UNION (VOID, REAL, INT, COMPL, STRING);
 MODE LIST = STRUCT (NODE val, REF LIST next);
```

Usage example for **UNION** **CASE** of ***NODE***:

| Algol68r0 as in the 1968 Final Report | Algol68r1 as in the 1973 Revised Report |
|---|---|
| **NODE** n := "1234"; **REAL** r; **INT** i; **COMPL** c; **STRING** s **CASE** r,i,c,s::=n **IN** print(("real:", r)), print(("int:", i)), print(("compl:", c)), print(("string:", s)) **OUT** print(("?:", n)) **ESAC** | **NODE** n := "1234"; # or n := EMPTY; # **CASE** n **IN** (**VOID**): print(("void:", "EMPTY")), (**REAL** r): print(("real:", r)), (**INT** i): print(("int:", i)), (**COMPL** c): print(("compl:", c)), (**STRING** s): print(("string:", s)) **OUT** print(("?:", n)) **ESAC** |

### proc: Procedures

Procedure (**PROC**) declarations require type specifications for both the parameters and the result (**VOID** if none):

```
 PROC max of real = (REAL a, b) REAL:
    IF a > b THEN a ELSE b FI;
```

or, using the "brief" form of the conditional statement:

```
 PROC max of real = (REAL a, b) REAL: (a>b | a | b);
```

The return value of a `proc` is the value of the last expression evaluated in the procedure. References to procedures (**ref proc**) are also permitted. Call-by-reference parameters are provided by specifying references (such as `**ref real**`) in the formal argument list. The following example defines a procedure that applies a function (specified as a parameter) to each element of an array:

```
 PROC apply = (REF [] REAL a, PROC (REAL) REAL f):
  
    FOR i FROM LWB a TO UPB a DO a[i] := f(a[i]) OD
```

This simplicity of code was unachievable in ALGOL 68's predecessor ALGOL 60.

### op: Operators

The programmer may define new **operators** and *both* those and the pre-defined ones may be overloaded and their priorities may be changed by the coder. The following example defines operator `**MAX**` with both dyadic and monadic versions (scanning across the elements of an array).

```
 PRIO MAX = 9;
  
 OP MAX = (INT a,b) INT: ( a>b | a | b );
 OP MAX = (REAL a,b) REAL: ( a>b | a | b );
 OP MAX = (COMPL a,b) COMPL: ( ABS a > ABS b | a | b );
  
 OP MAX = ([]REAL a) REAL:
    (REAL out := a[LWB a];
     FOR i FROM LWB a + 1 TO UPB a DO ( a[i]>out | out:=a[i] ) OD;
     out)
```

#### Array, Procedure, Dereference and coercion operations

| **PRIO**rity | Operation r0&r1 | +Algol68r0 | +Algol68G |
|---|---|---|---|
| Effectively 12 (Primary) | dereferencing, deproceduring(~,~), subscripting[~], rowing[~,], slicing[~:~], size denotations **LONG** & **SHORT** | proceduring | currying(~,,,), **DIAG**, **TRNSP**, **ROW**, **COL** |
| Effectively 11 (Secondary) | **OF** (selection), **LOC** & **HEAP** (generators) | → (selection) | **NEW** (generators) |

These are technically not operators, rather they are considered "units associated with names"

#### Monadic operators

| **PRIO**rity (Tertiary) | Algol68 "Worthy characters[5]"r0&r1 | +Algol68r0&r1 | +Algol68C,G | +Algol68r0 |
|---|---|---|---|---|
| 10 | **NOT** ~, **UP**, **DOWN**, **LWB**, **UPB**, -, **ABS**, **ARG**, **BIN**, **ENTIER**, **LENG**, **LEVEL**, **ODD**, **REPR**, **ROUND**, **SHORTEN** | ¬, ↑, ↓, ⌊, ⌈ | **NORM**, **TRACE**, **T**, **DET**, **INV** | **LWS**, **UPS**, ⎩, ⎧, **BTB**, **CTB** |

#### Dyadic operators with associated priorities

| **PRIO**rity (Tertiary) | Algol68 "Worthy characters"r0&r1 | +Algol68r0&r1 | +Algol68C,G | +Algol68r0 |
|---|---|---|---|---|
| 9 | +*, **I** | +×, ⊥ |   | ! |
| 8 | **SHL**, **SHR**, **, **UP**, **DOWN**, **LWB**, **UPB** | ↑, ↓, ⌊, ⌈ |   | ××, ^, **LWS**, **UPS**, ⎩, ⎧ |
| 7 | *, /,  %, **OVER**,  %*, **MOD**, **ELEM** | ×, ÷, ÷×, ÷*, %×, □ |   | ÷: |
| 6 | -, + |   |   |   |
| 5 | <, **LT**, <=, **LE**, >=, **GE**, >, **GT** | ≤, ≥ |   |   |
| 4 | **EQ** =, **NE** ~= /= | ≠, ¬= |   |   |
| 3 | &, **AND** | ∧ |   | /\ |
| 2 | **OR** | ∨ |   | \/ |
| 1 | **MINUSAB**, **PLUSAB**, **TIMESAB**, **DIVAB**, **OVERAB**, **MODAB**, **PLUSTO**, -:=, +:=, *:=, /:=, %:=, %*:=, +=: | ×:=, ÷:=, ÷×:=, ÷*:=,  %×:= |   | **MINUS**, **PLUS**, **DIV**, **OVERB**, **MODB**, ÷::=, **PRUS** |

Specific details:

- Tertiaries include names **NIL** and ○.
- **LWS**: In Algol68r0 the operators **LWS** and ⎩ ... both return **TRUE** if the *lower state* of the dimension of an array is fixed.
- The **UPS** and ⎧ operators are similar on the *upper state*.
- The **LWB** and **UPB** operators are automatically available on **UNION**s of different orders (and **MODE**s) of arrays. eg. **UPB** of **`union([]int, [,]real, flex[,,,]char)`**

#### Assignation and identity relations, etc.

These are technically not operators, rather they are considered "units associated with names"

| **PRIO**rity (Quaternaries) | Algol68 "Worthy characters"r0&r1 | +Algol68r0&r1 | +Algol68C,G,R | +Algol68r0 |
|---|---|---|---|---|
| Effectively 0 | :=, **IS** :=:, **ISNT** :/=: :~=:, **AT** @, ":", ";" | :≠: :¬=: | :=:=C, =:=R | ..=, .=, **CT**, ::, **CTAB**, ::=, .., **is not**, "..", ".," |

Note: Quaternaries include names **SKIP** and ~.

`:=:` (alternatively **IS**) tests if two pointers are equal; `:/=:` (alternatively **ISNT**) tests if they are unequal.

##### Why `:=:` and `:/=:` are needed

Consider trying to compare two pointer values, such as the following variables, declared as pointers-to-integer:

REF

INT

ip, jp

Now consider how to decide whether these two are pointing to the same location, or whether one of them is pointing to **NIL**. The following expression

ip = jp

will dereference both pointers down to values of type **INT**, and compare those, since the = operator is defined for **INT**, but not **REF** **INT**. It is *not legal* to define = for operands of type **REF** **INT** and **INT** at the same time, because then calls become ambiguous, due to the implicit coercions that can be applied: should the operands be left as **REF** **INT** and that version of the operator called? Or should they be dereferenced further to **INT** and that version used instead? Therefore the following expression can never be made legal:

ip =

NIL

Hence the need for separate constructs not subject to the normal coercion rules for operands to operators. But there is a gotcha. The following expressions:

ip :=: jp

ip :=:

NIL

while legal, will probably not do what might be expected. They will always return **FALSE**, because they are comparing the *actual addresses of the variables*`ip`*and*`jp`*, rather than what they point to*. To achieve the right effect, one would have to write

ip :=:

REF

INT

(jp)

ip :=:

REF

INT

(

NIL

)

#### Special characters

Most of Algol's "special" characters (⊂, ≡, ␣, ×, ÷, ≤, ≥, ≠, ¬, ⊃, ≡, ∨, ∧, →, ↓, ↑, ⌊, ⌈, ⎩, ⎧, ⊥, ⏨, ¢, ○ and □) can be found on the IBM 2741 keyboard with the APL "golf-ball" print head inserted; these became available in the mid-1960s while ALGOL 68 was being drafted. These characters are also part of the Unicode standard and most of them are available in several popular fonts.

### transput: Input and output

**Transput** is the term used to refer to ALGOL 68's input and output facilities. It includes pre-defined procedures for unformatted, formatted and binary transput. Files and other transput devices are handled in a consistent and machine-independent manner. The following example prints out some unformatted output to the **standard output** device:

```
  print ((newpage, "Title", newline, "Value of i is ",
    i, "and x[i] is ", x[i], newline))
```

Note the predefined procedures `newpage` and `newline` passed as arguments.

#### Books, channels and files

The **TRANSPUT** is considered to be of **BOOKS**, **CHANNELS** and **FILES**:

- **Books** are made up of pages, lines and characters, and may be backed up by files.
  - A specific book can be located by name with a call to `match`.
- **CHANNEL**s correspond to physical devices. e.g. card punches and printers.
  - Three standard channels are distinguished: *stand in* channel, *stand out* channel, *stand back* channel.
- A **FILE** is a means of communicating between a program and a book that has been opened via some channel.
  - The **MOOD** of a file may be read, write, char, bin, and opened.
  - transput procedures include: `establish, create, open, associate, lock, close, scratch`.
  - position enquires: `char number, line number, page number`.
  - layout routines include:
    - `space`, `backspace`, `newline`, `newpage`.
    - `get good line, get good page, get good book`, and `**PROC** set=(**REF** **FILE** f, **INT** page,line,char)**VOID**:`
  - A file has **event routines**. e.g. `on logical file end, on physical file end, on page end, on line end, on format end, on value error, on char error`.

#### formatted transput

"Formatted transput" in ALGOL 68's transput has its own syntax and patterns (functions), with **FORMAT**s embedded between two $ characters.

Examples:

```
 printf (($2l"The sum is:"x, g(0)$, m + n)); ¢ prints the same as: ¢
 print ((new line, new line, "The sum is:", space, whole (m + n, 0))
```

### par: Parallel processing

*ALGOL 68* supports programming of parallel processing. Using the keyword **PAR**, a *collateral clause* is converted to a *parallel clause*, where the synchronisation of actions is controlled using semaphores. In A68G the parallel actions are mapped to threads when available on the hosting operating system. In A68S a different paradigm of parallel processing was implemented (see below).

```
PROC
    eat = VOID: ( muffins-:=1; print(("Yum!",new line))),
    speak = VOID: ( words-:=1; print(("Yak...",new line)));
 
INT muffins := 4, words := 8;
SEMA mouth = LEVEL 1;
 
PAR BEGIN
    WHILE muffins > 0 DO
        DOWN mouth;
        eat;
        UP mouth
    OD,
    WHILE words > 0 DO
        DOWN mouth;
        speak;
        UP mouth
    OD
END
```

### Miscellaneous

For its technical intricacies, ALGOL 68 needs a cornucopia of methods to deny the existence of something:

```
SKIP, "~" or "?"C – an undefined value always syntactically valid,
EMPTY – the only value admissible to VOID, needed for selecting VOID in a UNION,
VOID – syntactically like a MODE, but not one,
NIL or "○" – a name not denoting anything, of an unspecified reference mode,
() or specifically [1:0]INT – a vacuum is an empty array (here specifically of MODE []INT).
undefined – a standards reports procedure raising an exception in the runtime system.
ℵ – Used in the standards report to inhibit introspection of certain types. e.g. SEMA
```

The term **NIL** **IS** *var* always evaluates to **TRUE** for any variable (but see above for correct use of **IS** :/=:), whereas it is not known to which value a comparison *x* < **SKIP** evaluates for any integer *x*.

ALGOL 68 leaves intentionally undefined what happens in case of integer overflow, the integer bit representation, and the degree of numerical accuracy for floating point.

Both official reports included some advanced features that were not part of the standard language. These were indicated with an ℵ and considered effectively private. Examples include "≮" and "≯" for templates, the **OUTTYPE**/**INTYPE** for crude duck typing, and the **STRAIGHTOUT** and **STRAIGHTIN** operators for "straightening" nested arrays and structures


## Examples of use

### Code sample

This sample program implements the Sieve of Eratosthenes to find all the prime numbers that are less than 100. **NIL** is the ALGOL 68 analogue of the *null pointer* in other languages. The notation *x* **OF** *y* accesses a member *x* of a **STRUCT** *y*.

```
BEGIN # Algol-68 prime number sieve, functional style #
  
  PROC error = (STRING s) VOID:
     (print(( newline, " error: ", s, newline)); GOTO stop);
  PROC one to = (INT n) LIST:
     (PROC f = (INT m,n) LIST: (m>n | NIL | cons(m, f(m+1,n))); f(1,n));
  
  MODE LIST = REF NODE;
  MODE NODE = STRUCT (INT h, LIST t);
  PROC cons = (INT n, LIST l) LIST: HEAP NODE := (n,l);
  PROC hd   = (LIST l) INT: ( l IS NIL | error("hd NIL"); SKIP | h OF l );
  PROC tl   = (LIST l) LIST: ( l IS NIL | error("tl NIL"); SKIP | t OF l );
  PROC show = (LIST l) VOID: ( l ISNT NIL | print((" ",whole(hd(l),0))); show(tl(l)));
  
  PROC filter = (PROC (INT) BOOL p, LIST l) LIST:
     IF l IS NIL THEN NIL
     ELIF p(hd(l)) THEN cons(hd(l), filter(p,tl(l)))
     ELSE filter(p, tl(l))
     FI;
  
  PROC sieve = (LIST l) LIST:
     IF l IS NIL THEN NIL
     ELSE
        PROC not multiple = (INT n) BOOL: n MOD hd(l) ~= 0;
        cons(hd(l), sieve( filter( not multiple, tl(l) )))
     FI;
  
  PROC primes = (INT n) LIST: sieve( tl( one to(n) ));
  
  show( primes(100) )
END
```

### Operating systems written in ALGOL 68

- Cambridge CAP computer – All procedures constituting the operating system were written in ALGOL 68C, although several other closely associated protected procedures, such as a paginator, are written in BCPL.
- Eldon 3 – Developed at Leeds University for the ICL 1900 was written in ALGOL 68-R.
- Flex machine – The hardware was custom and microprogrammable, with an operating system, (modular) compiler, editor, garbage collector and filing system all written in ALGOL 68RS. The command shell Curt was designed to access typed data similar to Algol-68 modes.
- VME – S3 was the implementation language of the operating system VME. S3 was based on ALGOL 68 but with data types and operators aligned to those offered by the ICL 2900 Series.

Note: The Soviet Era computers Эльбрус-1 (Elbrus-1) and Эльбрус-2 were created using high-level language Эль-76 (AL-76), rather than the traditional assembly. Эль-76 resembles Algol-68, The main difference is the dynamic binding types in Эль-76 supported at the hardware level. Эль-76 is used for application, job control, system programming.

### Applications

Both ALGOL 68C and ALGOL 68-R are written in ALGOL 68, effectively making ALGOL 68 an application of itself. Other applications include:

- ELLA – a hardware description language and support toolset. Developed by the Royal Signals and Radar Establishment during the 1980s and 1990s.
- RAF Strike Command System – "... 400K of error-free ALGOL 68-RT code was produced with three man-years of work. ..."

### Libraries and APIs

- NAG Numerical Libraries – a software library of numerical analysis routines. Supplied in ALGOL 68 during the 1980s.
- TORRIX – a programming system for operations on vectors and matrices over arbitrary fields and of variable size by S. G. van der Meulen and M. Veldhorst.
