---
title: "B (programming language)"
source: https://en.wikipedia.org/wiki/B_(programming_language)
domain: bcpl-b-language
license: CC-BY-SA-4.0
tags: bcpl language, b language, martin richards, bootstrapping compilers, systems programming
fetched: 2026-07-02
---

# B (programming language)

**B** is a programming language developed at Bell Labs circa 1969 by Ken Thompson and Dennis Ritchie.

B was designed for recursive, non-numeric, machine-independent applications, such as system and language software. It was a typeless language, with the only data type being the underlying machine's natural memory word format, whatever that might be. Depending on the context, the word was treated either as an integer or a memory address.

As machines with ASCII processing became common, notably the DEC PDP-11 that arrived at Bell Labs, support for character data stuffed in memory words became important. The typeless nature of the language was seen as a disadvantage, which led Thompson and Ritchie to develop an expanded version of the language supporting new internal and user-defined types, which became the ubiquitous C programming language.

## History

> BCPL semantics with a lot of SMALGOL syntax

— Ken Thompson,

Ken Thompson began developing B as a Fortran compiler for the PDP-7, but found that his initial implementation far exceeded available memory. Through several iterations of simplifying the compiler and adapting the language to his own tastes that were influenced by BCPL, he arrived at a language that expressed a subset of BCPL semantics in a distinct syntax. Thompson named the language B, which has been variously explained as an abbreviation of BCPL or Bon, another language he had developed, although he confirmed neither explanation.

Thompson added "two-address assignment operators" using `x =+ y` syntax to add y to x (in C the operator is written `+=`). This syntax came from Douglas McIlroy's implementation of TMG, in which B's compiler was first implemented (and it came to TMG from ALGOL 68's `x +:= y` syntax). Thompson went further by inventing the increment and decrement operators (`++` and `--`). Their prefix or postfix position determines whether the value is taken before or after alteration of the operand. This innovation was not in the earliest versions of B. According to Dennis Ritchie, people often assumed that they were created for the auto-increment and auto-decrement address modes of the DEC PDP-11, but this is historically impossible as the machine didn't exist when B was first developed.

B is typeless, or more precisely has one data type: the computer word. Most operators (e.g. `+`, `-`, `*`, `/`) treated this as an integer, but others treated it as a memory address to be dereferenced. In many other ways it looked a lot like an early version of C. It included a generalized for loop as later appeared in C, which Thompson adapted from earlier work by Stephen Johnson. There are a few library functions, including some that vaguely resemble functions from the standard I/O library in C. In Thompson's words: "B and the old old C were very very similar languages except for all the types [in C]".

Early implementations were for the DEC PDP-7 and PDP-11 minicomputers using early Unix, and Honeywell GE 645 36-bit mainframes running the operating system GCOS. The earliest PDP-7 implementations compiled to threaded code, and Ritchie wrote a compiler using TMG which produced machine code. In 1970 a PDP-11 was acquired and threaded code was used for the port; an assembler, dc, and the B language itself were written in B to bootstrap the computer. An early version of yacc was produced with this PDP-11 configuration. Ritchie took over maintenance during this period.

The typeless nature of B made sense on the Honeywell, PDP-7 and many older computers, but was a problem on the PDP-11 because it was difficult to elegantly access the character data type that the PDP-11 and most modern computers fully support. Starting in 1971 Ritchie made changes to the language while converting its compiler to produce machine code, most notably adding data typing for variables. During 1971 and 1972 B evolved into "New B" (NB) and then C.

B is almost extinct, having been superseded by the C language. However, it continues to see use on GCOS mainframes (as of 2014) and on certain embedded systems (as of 2000) for a variety of reasons: limited hardware in small systems, extensive libraries, tooling, licensing cost issues, and simply being good enough for the job. The highly influential AberMUD was originally written in B.

## Examples

The following examples are from the *Users' Reference to B* by Ken Thompson:

```mw
/* The following function will print a non-negative number, n, to
   the base b, where 2<=b<=10.  This routine uses the fact that
   in the ASCII character set, the digits 0 to 9 have sequential
   code values.  */

printn(n,b) {
   extrn putchar;
   auto a;
   /* Wikipedia note: the auto keyword declares a variable with
      automatic storage (lifetime is function scope), not
      "automatic typing" as in C++11 and C23 */

   if(a=n/b) /* assignment, not test for equality */
      printn(a, b); /* recursive */
   putchar(n%b + '0');
}
```

```mw
/* The following program will calculate the constant e-2 to about
   4000 decimal digits, and print it 50 characters to the line in
   groups of 5 characters.  The method is simple output conver-
   sion of the expansion
      1/2! + 1/3! + ... = .111...
   where the bases of the digits are 2, 3, 4, ... */

main() {
   extrn putchar, n, v;
   auto i, c, col, a;

   i = col = 0;
   while(i<n)
      v[i++] = 1;

   while(col<2*n) {
      a = n+1;
      c = i = 0;
      while(i<n) {
         c =+ v[i]*10;
         v[i++] = c%a;
         c =/ a--;
      }
      putchar(c+'0');
      if(!(++col%5))
         putchar(col%50?' ':'*n');
   }
   putchar('*n*n');
}

v[2000];
n 2000;
```
