---
title: "COBOL (part 3/3)"
source: https://en.wikipedia.org/wiki/COBOL
domain: legacy-languages
license: CC-BY-SA-4.0
tags: fortran, cobol, ada language, pascal, smalltalk, prolog, forth language, apl
fetched: 2026-07-02
part: 3/3
---

## Reception

### Lack of structure

In the 1970s, adoption of the structured programming paradigm was becoming increasingly widespread. Edsger Dijkstra, a preeminent computer scientist, wrote a letter to the editor of Communications of the ACM, published in 1975 entitled "How do we tell truths that might hurt?", in which he was critical of COBOL and several other contemporary languages, remarking that "the use of COBOL cripples the mind".

In a published dissent to Dijkstra's remarks, the computer scientist Howard E. Tompkins claimed that unstructured COBOL tended to be "written by programmers that have never had the benefit of structured COBOL taught well", arguing that the issue was primarily one of training.

One cause of spaghetti code was the `GO TO` statement. Attempts to remove `GO TO`s from COBOL code, however, resulted in convoluted programs and reduced code quality. `GO TO`s were largely replaced by the `PERFORM` statement and procedures, which promoted modular programming and gave easy access to powerful looping facilities. However, `PERFORM` could be used only with procedures so loop bodies were not located where they were used, making programs harder to understand. Since the adoption of the 1985 standard, the need for `GO TO` has been completely obliviated by rich features of the `PERFORM` verb; however, `GO TO` remains for backwards compatibility, as it does in many other languages.

COBOL programs were infamous for being monolithic and lacking modularization. COBOL code could be modularized only through procedures, which were found to be inadequate for large systems. Otherwise, it was required to `CALL` separately compiled programs for modularity. It was impossible to restrict access to data until the COBOL-85 standard, meaning a procedure could access and modify *any* data item. Furthermore, there was no way to pass parameters to a procedure, an omission Jean Sammet regarded as the committee's biggest mistake.. This problem was removed in the COBOL-85 standard with the introduction of the nested subprogram which allowed for modularity and locally isolated data items.

Another complication stemmed from the ability to `PERFORM THRU` a specified sequence of procedures. This meant that control could jump to and return from any procedure, creating convoluted control flow and permitting a programmer to break the single-entry single-exit rule.

This situation improved as COBOL adopted more features. COBOL-74 added subprograms, giving programmers the ability to control the data each part of the program could access. COBOL-85 then added nested subprograms, allowing programmers to hide subprograms. Further control over data and code came in 2002 when object-oriented programming, user-defined functions and user-defined data types were included.

Nevertheless, much important legacy COBOL software uses unstructured code, which has become practically unmaintainable. It can be too risky and costly to modify even a simple section of code, since it may be used from unknown places in unknown ways.

### Compatibility issues

COBOL was intended to be a highly portable, "common" language. However, by 2001, around 300 dialects had been created. One source of dialects was the standard itself: the 1974 standard was composed of one mandatory nucleus and eleven functional modules, each containing two or three levels of support. This permitted 104,976 possible variants.

COBOL-85 was not fully compatible with earlier versions, and its development was controversial. Joseph T. Brophy, the CIO of Travelers Insurance, spearheaded an effort to inform COBOL users of the heavy reprogramming costs of implementing the new standard. As a result, the ANSI COBOL Committee received more than 2,200 letters from the public, mostly negative, requiring the committee to make changes. On the other hand, conversion to COBOL-85 was thought to increase productivity in future years, thus justifying the conversion costs.

### Verbose syntax

COBOL: /koh′bol/, n.

> A weak, verbose, and flabby language used by code grinders to do boring mindless things on dinosaur mainframes. [...] Its very name is seldom uttered without ritual expressions of disgust or horror.

—

The Jargon File

4.4.8.

COBOL syntax has often been criticized for its verbosity. Proponents say that this was intended to make the code self-documenting, easing program maintenance. COBOL was also intended to be easy for programmers to learn and use, while still being readable to non-technical staff such as managers.

The desire for readability led to the use of English-like syntax and structural elements, such as nouns, verbs, clauses, sentences, sections, and divisions. Yet by 1984, maintainers of COBOL programs were struggling to deal with "incomprehensible" code and the main changes in COBOL-85 were there to help ease maintenance.

Jean Sammet, a short-range committee member, noted that "little attempt was made to cater to the professional programmer, in fact people whose main interest is programming tend to be very unhappy with COBOL" which she attributed to COBOL's verbose syntax.

> The academic world tends to regard COBOL as verbose, clumsy and inelegant, and tries to ignore it, although there are probably more COBOL programs and programmers in the world than there are for FORTRAN, ALGOL and PL/I combined. For the most part, only schools with an immediate vocational objective provide instruction in COBOL.

—

Richard Conway

and

David Gries

, 1973

Later, COBOL suffered from a shortage of material covering it; it took until 1963 for introductory books to appear (with Richard D. Irwin publishing a college textbook on COBOL in 1966). Donald Nelson, chair of the CODASYL COBOL committee, said in 1984 that "academics ... hate COBOL" and that computer science graduates "had 'hate COBOL' drilled into them".

By the mid-1980s, there was also significant condescension towards COBOL in the business community from users of other languages, for example FORTRAN or assembler, implying that COBOL could be used only for non-challenging problems.

In 2003, COBOL featured in 80% of information systems curricula in the United States, the same proportion as C++ and Java. Ten years later, a poll by Micro Focus found that 20% of university academics thought COBOL was outdated or dead and that 55% believed their students thought COBOL was outdated or dead. The same poll also found that only 25% of academics had COBOL programming on their curriculum even though 60% thought they should teach it.

### Concerns about the design process

Doubts have been raised about the competence of the standards committee. Short-term committee member Howard Bromberg said that there was "little control" over the development process and that it was "plagued by discontinuity of personnel and ... a lack of talent." Jean Sammet and Jerome Garfunkel also noted that changes introduced in one revision of the standard would be reverted in the next, due as much to changes in who was in the standard committee as to objective evidence.

COBOL standards have repeatedly suffered from delays: COBOL-85 arrived five years later than hoped, COBOL 2002 was five years late, and COBOL 2014 was six years late. To combat delays, the standard committee allowed the creation of optional addenda which would add features more quickly than by waiting for the next standard revision. However, some committee members raised concerns about incompatibilities between implementations and frequent modifications of the standard.

### Influences on other languages

COBOL's data structures influenced subsequent programming languages. Its record and file structure influenced PL/I and Pascal, and the `REDEFINES` clause was a predecessor to Pascal's variant records. Explicit file structure definitions preceded the development of database management systems and aggregated data was a significant advance over Fortran's arrays.

`PICTURE` data declarations were incorporated into PL/I, with minor changes.

COBOL's `COPY` facility, although considered "primitive", influenced the development of include directives.

The focus on portability and standardization meant programs written in COBOL could be portable and facilitated the spread of the language to a wide variety of hardware platforms and operating systems. Additionally, the well-defined division structure restricts the definition of external references to the Environment Division, which simplifies platform changes in particular.
