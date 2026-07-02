---
title: "Fortran (part 2/2)"
source: https://en.wikipedia.org/wiki/Fortran
domain: pl-i-language
license: CC-BY-SA-4.0
tags: pl i language, structured programming, mainframe computer, ibm system, punched card
fetched: 2026-07-02
part: 2/2
---

## Historical variants

### Manufacturer versions

Until the Fortran 66 standard was developed, each compiler supported its own variant of Fortran. Some were more divergent from the mainstream than others. One of the most prominent textbooks of the time, Daniel D. McCracken's *A Guide to FORTRAN IV Programming* (1965), devoted a full two-page matrix of 24 feature differences versus 29 manufacturer-and-computer versions. Another textbook author from that era, John M. Blatt, despaired of doing the same, writing that "manufacturers tend to consider 'their own' FORTRAN as a selling point, and as soon as one dialect of FORTRAN acquire some 'gimmick' or other, other dialects try to go it one better." Nonetheless, Fortran programs were far more portable than assembly languages ones, and in practice those familiar with one manufacturer's Fortran could straighforwardly adapt themselves to that of a different manuacturer.

**Fortran 5** was marketed by Data General Corp from the early 1970s to the early 1980s, for the Nova, Eclipse, and MV line of computers. It had an optimizing compiler that was quite good for minicomputers of its time. The language most closely resembles FORTRAN 66.

**FORTRAN V** was distributed by Control Data Corporation in 1968 for the CDC 6600 series. The language was based upon FORTRAN IV.

Univac also offered a compiler for the 1100 series known as FORTRAN V. A spinoff of Univac Fortran V was Athena FORTRAN.

Specific variants produced by the vendors of high-performance scientific computers (e.g., Burroughs, Control Data Corporation (CDC), Cray, Honeywell, IBM, Texas Instruments, and UNIVAC) added extensions to Fortran to take advantage of special hardware features such as instruction cache, CPU pipelines, and vector arrays. For example, one of IBM's FORTRAN compilers (*H Extended IUP*) had a level of optimization which reordered the machine code instructions to keep multiple internal arithmetic units busy simultaneously. Another example is *CFD*, a special variant of FORTRAN designed specifically for the ILLIAC IV supercomputer, running at NASA's Ames Research Center. IBM Research Labs also developed an extended FORTRAN-based language called *VECTRAN* for processing vectors and matrices.

*Object-Oriented Fortran* was an object-oriented extension of Fortran, in which data items can be grouped into objects, which can be instantiated and executed in parallel. It was available for Solaris, IRIX, NeXTSTEP, iPSC, and nCUBE, but is no longer supported.

Such machine-specific extensions have either disappeared over time or have had elements incorporated into the main standards. The major remaining extension is OpenMP, which is a cross-platform extension for shared memory programming. One new extension, Coarray Fortran, is intended to support parallel programming.

*FOR TRANSIT* was the name of a reduced version of the IBM 704 FORTRAN language, which was implemented for the IBM 650, using a translator program developed at Carnegie in the late 1950s. The following comment appears in the IBM Reference Manual (*FOR TRANSIT Automatic Coding System* C28-4038, Copyright 1957, 1959 by IBM):

> The FORTRAN system was designed for a more complex machine than the 650, and consequently some of the 32 statements found in the FORTRAN Programmer's Reference Manual are not acceptable to the FOR TRANSIT system. In addition, certain restrictions to the FORTRAN language have been added. However, none of these restrictions make a source program written for FOR TRANSIT incompatible with the FORTRAN system for the 704.

The permissible statements were:

- Arithmetic assignment statements, e.g., `a = b`
- `GO to n`
- `GO TO (n1, n2, ..., nm), i`
- `IF (a) n1, n2, n3`
- `PAUSE`
- `STOP`
- `DO n i = m1, m2`
- `CONTINUE`
- `END`
- `READ n, list`
- `PUNCH n, list`
- `DIMENSION V, V, V, ...`
- `EQUIVALENCE (a,b,c), (d,c), ...`

Up to ten subroutines could be used in one program.

FOR TRANSIT statements were limited to columns 7 through 56, only. Punched cards were used for input and output on the IBM 650. Three passes were required to translate source code to the "IT" language, then to compile the IT statements into SOAP assembly language, and finally to produce the object program, which could then be loaded into the machine to run the program (using punched cards for data input, and outputting results onto punched cards).

Two versions existed for the 650s with a 2000 word memory drum: FOR TRANSIT I (S) and FOR TRANSIT II, the latter for machines equipped with indexing registers and automatic floating-point decimal (bi-quinary) arithmetic. Appendix A of the manual included wiring diagrams for the IBM 533 card reader/punch control panel.

### Student compilers

The first FORTRAN compiler set a high standard of efficiency for compiled code. This goal made it difficult to create a compiler so it was usually done by the computer manufacturers to support hardware sales. The requirement for execution efficiency remained the primary design criteria for the language through the early evolution of the language. This left an important niche: compilers that were fast in the compilation and loading phase and provided good diagnostics for the programmer, who was often a student as by this time FORTRAN IV had started to become an important educational tool.

WATFOR, introduced in the 1960s, was popularly used in colleges and universities. Developed, supported, and distributed by the University of Waterloo, WATFOR was based largely on FORTRAN IV. A student using WATFOR could submit their batch FORTRAN job and, if there were no syntax errors, the program would move straight to execution. This simplification allowed students to concentrate on their program's syntax and semantics, or execution logic flow, rather than dealing with submission Job Control Language (JCL), the compile/link-edit/execution successive process(es), or other complexities of a mainframe environment.

Moreover, WATFOR presented a superset of the Fortran language, in particular providing so-called "free" `READ` and `PRINT` commands as an alternative to the formatted `READ` and `WRITE>` statements of regular Fortran. The `FORMAT` statements of the latter allowed considerable flexibility but could be quite complicated, and were sometimes subject to manufacturer differences or site-specific guidelines. Since the formatted approach caused even experienced programmers difficulties, providing an alternative in a student compiler was a definite advantage. A down side to this simplified environment was that WATFOR was not a good choice for programmers needing the expanded abilities of their host processor(s), e.g., WATFOR typically had very limited access to I/O devices. WATFOR was succeeded by WATFIV and later versions.

Another student compiler was PUFFT, and on a smaller scale, FORGO, Wits Fortran, and Kingston Fortran 2.

### Fortran-based languages

Prior to FORTRAN 77, many preprocessors were commonly used to provide a friendlier language, with the advantage that the preprocessed code could be compiled on any machine with a standard FORTRAN compiler. These preprocessors would typically support structured programming, variable names longer than six characters, additional data types, conditional compilation, and even macro capabilities. Popular preprocessors included EFL, FLECS, iftran, MORTRAN, SFtran, S-Fortran, Ratfor, and Ratfiv. EFL, Ratfor and Ratfiv, for example, implemented C-like languages, outputting preprocessed code in standard FORTRAN 66. The PFORT preprocessor was often used to verify that code conformed to a portable subset of the language. Despite advances in the Fortran language, preprocessors continue to be used for conditional compilation and macro substitution.

```mw
program; s=0 i=1,n; s=s+1; stop i; s='s'  Stop
```

(line programming)

LRLTRAN was developed at the Lawrence Radiation Laboratory to provide support for vector arithmetic and dynamic storage, among other extensions to support systems programming. The distribution included the Livermore Time Sharing System (LTSS) operating system.

The Fortran-95 Standard includes an optional *Part 3* which defines an optional conditional compilation capability. This capability is often referred to as "CoCo".

Many Fortran compilers have integrated subsets of the C preprocessor into their systems.

SIMSCRIPT is an application specific Fortran preprocessor for modeling and simulating large discrete systems.

The F programming language was designed to be a clean subset of Fortran 95 that attempted to remove the redundant, unstructured, and deprecated features of Fortran, such as the `EQUIVALENCE` statement. F retains the array features added in Fortran 90, and removes control statements that were made obsolete by structured programming constructs added to both FORTRAN 77 and Fortran 90. F is described by its creators as "a compiled, structured, array programming language especially well suited to education and scientific computing". Essential Lahey Fortran 90 (ELF90) was a similar subset.

Lahey and Fujitsu teamed up to create Fortran for the Microsoft .NET Framework. Silverfrost FTN95 is also capable of creating .NET code.


## Code examples

The following program demonstrates dynamic memory allocation and array-based operations, two features introduced with Fortran 90. Particularly noteworthy is the absence of `DO` loops and `IF`/`THEN` statements in manipulating the array; mathematical operations are applied to the array as a whole. Also apparent is the use of descriptive variable names and general code formatting that conform with contemporary programming style. This example computes an average over data entered interactively.

```mw
program average

    ! Read in some numbers and take the average
    ! As written, if there are no data points, an average of zero is returned
    ! While this may not be desired behavior, it keeps this example simple

    implicit none

    real, allocatable :: points(:)
    integer           :: number_of_points
    real              :: average_points, positive_average, negative_average
    average_points   = 0.
    positive_average = 0.
    negative_average = 0.
    write (*,*) "Input number of points to average:"
    read  (*,*) number_of_points

    allocate (points(number_of_points))

    write (*,*) "Enter the points to average:"
    read  (*,*) points

    ! Take the average by summing points and dividing by number_of_points
    if (number_of_points > 0) average_points = sum(points) / number_of_points

    ! Now form average over positive and negative points only
    if (count(points > 0.) > 0) positive_average = sum(points, points > 0.) / count(points > 0.)
    if (count(points < 0.) > 0) negative_average = sum(points, points < 0.) / count(points < 0.)

    ! Print result to terminal stdout unit 6
    write (*,'(a,g12.4)') 'Average = ', average_points
    write (*,'(a,g12.4)') 'Average of positive points = ', positive_average
    write (*,'(a,g12.4)') 'Average of negative points = ', negative_average
    deallocate (points) ! free memory

end program average
```


## Humor

During the same FORTRAN standards committee meeting at which the name "FORTRAN 77" was chosen, a satirical technical proposal was incorporated into the official distribution bearing the title "Letter O Considered Harmful". This proposal purported to address the confusion that sometimes arises between the letter "O" and the numeral zero, by eliminating the letter from allowable variable names. However, the method proposed was to eliminate the letter from the character set entirely (thereby retaining 48 as the number of lexical characters, which the colon had increased to 49). This was considered beneficial in that it would promote structured programming, by making it impossible to use the notorious `GO TO` statement as before. (Troublesome `FORMAT` statements would also be eliminated.) It was noted that this "might invalidate some existing programs" but that most of these "probably were non-conforming, anyway".

When X3J3 debated whether the minimum trip count for a DO loop should be zero or one in Fortran 77, Loren Meissner suggested a minimum trip count of two—reasoning *(tongue-in-cheek)* that if it were less than two, then there would be no reason for a loop.

When assumed-length arrays were being added, there was a dispute as to the appropriate character to separate upper and lower bounds. In a comment examining these arguments, Walt Brainerd penned an article entitled "Astronomy vs. Gastroenterology" because some proponents had suggested using the star or asterisk ("*"), while others favored the colon (":").

Variable names beginning with the letters I–N have a default type of integer, while variables starting with any other letters defaulted to real, although programmers could override the defaults with an explicit declaration. This led to the joke: "In FORTRAN, GOD is REAL (unless declared INTEGER)."

The American Mathematical Monthly (November, 1978) printed a one-line review in verse: "A lively approach to seduce,/In manner quite sim'lar to Seuss./Handwritten, with drawings and lots of guffawings/Disposed to make Fortran transluce."
