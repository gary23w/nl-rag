---
title: "Forth (programming language)"
source: https://en.wikipedia.org/wiki/Forth_(programming_language)
domain: forth-lang
license: CC-BY-SA-4.0
tags: forth language, forth lang, gforth, forth stack
fetched: 2026-07-02
---

# Forth (programming language)

**Forth** is a stack-oriented programming language and interactive integrated development environment designed by Charles H. "Chuck" Moore and first used by other programmers in 1970. Although not an acronym, the language's name in its early years was often spelled in all capital letters as *FORTH*. The FORTH-79 and FORTH-83 implementations, which were not written by Moore, became *de facto* standards, and an official technical standard of the language was published in 1994 as ANS Forth. A wide range of Forth derivatives existed before and after ANS Forth. The free and open-source software Gforth implementation is actively maintained, as are several commercially supported systems.

Forth typically combines a compiler with an integrated command shell, where the user interacts via subroutines called *words*.

Words can be defined, tested, redefined, and debugged without recompiling or restarting the whole program. All syntactic elements, including variables, operators, and control flow, are defined as words. A stack is used to pass parameters between words, leading to a Reverse Polish notation style.

For much of Forth's existence, the standard technique was to compile to threaded code, which can be interpreted faster than bytecode. One of the early benefits of Forth was size: an entire development environment—including compiler, editor, and user programs—could fit in memory on an 8-bit or similarly limited system. No longer constrained by space, there are modern implementations that generate optimized machine code like other language compilers.

The relative simplicity of creating a basic Forth system has led to many personal and proprietary variants, such as the custom Forth used to implement the bestselling 1986 video game *Starflight* from Electronic Arts. Forth is used in the Open Firmware boot loader, in spaceflight applications such as the *Philae* spacecraft, and in other embedded systems which involve interaction with hardware.

Beginning in the early 1980s, Moore developed a series of microprocessors for executing compiled Forth-like code directly and experimented with smaller languages based on Forth concepts, including cmForth and colorForth. Most of these languages were created to support Moore's own projects, such as chip design.

## Uses

Forth has a niche in astronomical and space applications as well as a history in embedded systems. The Open Firmware boot ROMs used by Apple, IBM, Sun, and OLPC XO-1 contain a Forth environment.

Forth has often been used to bring up new hardware. Forth was the first resident software on the new Intel 8086 chip in 1978, and MacFORTH was the first resident development system for the Macintosh 128K in 1984.

Circa 1982, Atari, Inc. used an elaborate, self-running demo written in Forth to showcase capabilities of the Atari 8-bit computers in department stores. Electronic Arts published multiple video games in the 1980s that were written in Forth, including *Worms?* (1983), *Adventure Construction Set* (1984), *Amnesia* (1986), *Starflight* (1986), and *Lords of Conquest* (1986). Robot coding game *ChipWits* (1984) was developed in MacFORTH for the Macintosh 128K, while the Commodore 64 port was written with SuperForth 64. The prototype of *Boulder Dash* (1984) was implemented in Forth before being rewritten in 6502 assembly language.

Ashton-Tate's RapidFile (1986), a flat-file database program, and VP-Planner from Paperback Software International (1983), a spreadsheet program competing with Lotus 1-2-3, were written in Forth.

The Canon Cat (1987) uses Forth for its system programming.

Rockwell produced single-chip microcomputers with resident Forth kernels: the R65F11 and R65F12.

ASYST was a Forth expansion for measuring and controlling on PCs.

## History

Forth evolved from Charles H. Moore's personal programming system, which had been in continuous development since 1968. Forth was first exposed to other programmers in the early 1970s, starting with Elizabeth Rather at the United States National Radio Astronomy Observatory (NRAO). After their work at NRAO, Charles Moore and Elizabeth Rather formed FORTH, Inc. in 1973, refining and porting Forth systems to dozens of other platforms in the next decade.

Moore saw Forth as a successor to compile-link-go third-generation programming languages, or software for "fourth generation" hardware. He recalls how the name was coined:

> At Mohasco ["in the late 1960s"] I also worked directly on an IBM 1130 interfaced with an IBM 2250 graphics display. The 1130 was a very important computer: it had the first cartridge disk, as well as a card reader, a card punch (as backup for the disk), and a console typewriter. The 1130 let the programmer, for the first time, totally control the computer interactively.

> FORTH first appeared as an entity on that 1130. It was called F-O-R-T-H, a five-letter abbreviation of FOURTH, standing for fourth-generation computer language. That was the day, you may remember, of third-generation computers and I was going to leapfrog. But because FORTH ran on the 1130 (which permitted only five-character identifiers), the name was shortened.

FORTH, Inc.'s microFORTH was developed for the Intel 8080, Motorola 6800, Zilog Z80, and RCA 1802 microprocessors, starting in 1976. MicroFORTH was later used by hobbyists to generate Forth systems for other architectures, such as the 6502 in 1978. The Forth Interest Group was formed in 1978. It promoted and distributed its own version of the language, FIG-Forth, for most makes of home computer.

Forth was popular in the early 1980s, because it was well suited to the limited memory of microcomputers. The ease of implementing the language led to many implementations. The Jupiter ACE home computer has Forth in its ROM-resident operating system. Insoft GraFORTH is a version of Forth with graphics extensions for the Apple II.

Common practice was codified in the de facto standards FORTH-79 and FORTH-83 in the years 1979 and 1983, respectively. These standards were unified by ANSI in 1994, commonly referred to as ANS Forth.

As of 2018, the source for the original 1130 version of FORTH has been recovered, and is now being updated to run on a restored or emulated 1130 system.

## Overview

Forth emphasizes the use of small, simple functions called *words*. Words for bigger tasks call upon many smaller words that each accomplish a distinct sub-task. A large Forth program is a hierarchy of words. These words, being distinct modules that communicate implicitly via a stack mechanism, can be prototyped, built and tested independently. The highest level of Forth code may resemble an English-language description of the application. Forth has been called a *meta-application language*: a language that can be used to create problem-oriented languages.

Forth relies on implicit use of a data stack and reverse Polish notation which is commonly used in calculators from Hewlett-Packard. In RPN, the operator is placed after its operands, as opposed to the more common infix notation where the operator is placed between its operands. Postfix notation makes the language easier to parse and extend; Forth's flexibility makes a static BNF grammar inappropriate, and it does not have a monolithic compiler. Extending the compiler only requires writing a new word, instead of modifying a grammar and changing the underlying implementation.

Using RPN, one can compute the value of the arithmetic expression (25 × 10) + 50 in the following way:

```mw
 25 10 * 50 + CR .
 300 ok
```

First the numbers 25 and 10 are put on the stack.

The word `*` takes the top two numbers from the stack, multiplies them, and puts the product back on the stack.

Then the number 50 is placed on the stack.

The word `+` takes the top two numbers from the stack, adds them, and puts the sum back on the stack. `CR` (carriage return) starts the output on a new line. Finally, `.` prints the result. As everything has completed successfully, the Forth system prints `OK`.

Even Forth's structural features are stack-based. For example:

```mw
 : FLOOR5 ( n -- n' )   DUP 6 < IF DROP 5 ELSE 1 - THEN ;
```

The colon indicates the beginning of a new definition, in this case a new word (again, *word* is the term used for a subroutine) called `FLOOR5`. The text in parentheses is a comment, advising that this word expects a number on the stack and will return a possibly changed number (on the stack).

The subroutine uses the following commands: `DUP` duplicates the number on the stack; `6` pushes a 6 on top of the stack; `<` compares the top two numbers on the stack (6 and the `DUP`ed input), and replaces them with a true-or-false value; `IF` takes a true-or-false value and chooses to execute commands immediately after it or to skip to the `ELSE`; `DROP` discards the value on the stack; `5` pushes a 5 on top of the stack; and `THEN` ends the conditional.

The `FLOOR5` word is equivalent to this function written in the C programming language using the conditional operator '?:'

```mw
int floor5(int v) {
  return (v < 6) ? 5 : (v - 1);
}
```

This function is written more succinctly as:

```mw
 : FLOOR5 ( n -- n' ) 1- 5 MAX ;
```

This can be run as follows:

```mw
 1 FLOOR5 CR .
 5 ok
 8 FLOOR5 CR .
 7 ok
```

First a number (1 or 8) is pushed onto the stack, `FLOOR5` is called, which pops the number again and pushes the result. `CR` moves the output to a new line (again, this is only here for readability). Finally, a call to `.` pops the result and prints.

## Facilities

Forth's grammar has no official specification. Instead, it is defined by a simple algorithm. The interpreter reads a line of input from the user input device, which is then parsed for a word using spaces as a delimiter; some systems recognise additional whitespace characters. When the interpreter finds a word, it looks the word up in the *dictionary*. If the word is found, the interpreter executes the code associated with the word, and then returns to parse the rest of the input stream. If the word isn't found, the word is assumed to be a number and an attempt is made to convert it into a number and push it on the stack; if successful, the interpreter continues parsing the input stream. Otherwise, if both the lookup and the number conversion fail, the interpreter prints the word followed by an error message indicating that the word is not recognised, flushes the input stream, and waits for new user input.

The definition of a new word is started with the word `:` (colon) and ends with the word `;` (semi-colon). For example,

```mw
 : X DUP 1+ . . ;
```

will compile the word `X`, and makes the name findable in the dictionary. When executed by typing `10 X` at the console this will print `11 10`.

Most Forth systems include an assembler to write words using the processor's facilities. Forth assemblers often use a reverse Polish syntax in which the parameters of an instruction precede the instruction. A typical reverse Polish assembler prepares the operands on the stack and the mnemonic copies the whole instruction into memory as the last step. A Forth assembler is by nature a macro assembler, so that it is easy to define an alias for registers according to their role in the Forth system: e.g. "dsp" for the register used as the data stack pointer.

### Operating system, files, and multitasking

Most Forth systems run under a host operating system such as Microsoft Windows, Linux or a version of Unix and use the host operating system's file system for source and data files; the ANS Forth Standard describes the words used for I/O. All modern Forth systems use normal text files for source, even if they are embedded. An embedded system with a resident compiler gets its source via a serial line.

Classic Forth systems traditionally use neither operating system nor file system. Instead of storing code in files, source code is stored in disk blocks written to physical disk addresses. The word `BLOCK` is employed to translate the number of a 1K-sized block of disk space into the address of a buffer containing the data, which is managed automatically by the Forth system. Block use has become rare since the mid-1990s. In a hosted system those blocks too are allocated in a normal file in any case.

Multitasking, most commonly cooperative round-robin scheduling, is normally available (although multitasking words and support are not covered by the ANS Forth Standard). The word `PAUSE` is used to save the current task's execution context, to locate the next task, and restore its execution context. Each task has its own stacks, private copies of some control variables and a scratch area. Swapping tasks is simple and efficient; as a result, Forth multitaskers are available even on very simple microcontrollers, such as the Intel 8051, Atmel AVR, and TI MSP430.

Other non-standard facilities include a mechanism for issuing calls to the host OS or windowing systems, and many provide extensions that employ the scheduling provided by the operating system. Typically they have a larger and different set of words from the stand-alone Forth's `PAUSE` word for task creation, suspension, destruction and modification of priority.

### Self-compilation and cross compilation

A full-featured Forth system with all source code will compile itself, a technique commonly called meta-compilation or self-hosting, by Forth programmers (although the term doesn't exactly match meta-compilation as it is normally defined). The usual method is to redefine the handful of words that place compiled bits into memory. The compiler's words use specially named versions of fetch and store that can be redirected to a buffer area in memory. The buffer area simulates or accesses a memory area beginning at a different address than the code buffer. Such compilers define words to access both the target computer's memory, and the host (compiling) computer's memory.

After the fetch and store operations are redefined for the code space, the compiler, assembler, etc. are recompiled using the new definitions of fetch and store. This effectively reuses all the code of the compiler and interpreter. Then, the Forth system's code is compiled, but this version is stored in the buffer. The buffer in memory is written to disk, and ways are provided to load it temporarily into memory for testing. When the new version appears to work, it is written over the previous version.

Numerous variations of such compilers exist for different environments. For embedded systems, the code may instead be written to another computer, a technique known as cross compilation, over a serial port or even a single TTL bit, while keeping the word names and other non-executing parts of the dictionary in the original compiling computer. The minimum definitions for such a Forth compiler are the words that fetch and store a byte, and the word that commands a Forth word to be executed. Often the most time-consuming part of writing a remote port is constructing the initial program to implement fetch, store and execute, but many modern microprocessors have integrated debugging features (such as the Motorola CPU32) that eliminate this task.

## Structure of the language

The basic data structure of Forth is the "dictionary" which maps "words" to executable code or named data structures. The dictionary is laid out in memory as a tree of linked lists with the links proceeding from the latest (most recently) defined word to the oldest, until a sentinel value, usually a NULL pointer, is found. A context switch causes a list search to start at a different leaf. A linked list search continues as the branch merges into the main trunk leading eventually back to the sentinel, the root. There can be several dictionaries. In rare cases such as meta-compilation a dictionary might be isolated and stand-alone. The effect resembles that of nesting namespaces and can overload keywords depending on the context.

A defined word generally consists of *head* and *body* with the head consisting of the *name field* (NF) and the *link field* (LF), and body consisting of the *code field* (CF) and the *parameter field* (PF).

Head and body of a dictionary entry are treated separately because they may not be contiguous. For example, when a Forth program is recompiled for a new platform, the head may remain on the compiling computer, while the body goes to the new platform. In some environments (such as embedded systems) the heads occupy memory unnecessarily. However, some cross-compilers may put heads in the target if the target itself is expected to support an interactive Forth.

The exact format of a dictionary entry is not prescribed, and implementations vary.

### Structure of the compiler

The compiler itself is not a monolithic program. It consists of Forth words visible to the system, and usable by a programmer. This allows a programmer to change the compiler's words for special purposes. Compilation in traditional Forth systems is straightforward and does not involve building and optimizing an abstract representation of the code. (Some newer Forth compilers use more elaborate compilation methods, as common in other languages.)

The "compile time" flag in the name field is set for words with "compile time" behavior. Most simple words execute the same code whether they are typed on a command line, or embedded in code. When compiling these, the compiler simply places code or a threaded pointer to the word.

The classic examples of compile-time words are the control structures such as `IF` and `WHILE`. Almost all of Forth's control structures and almost all of its compiler are implemented as compile-time words. Apart from some rarely used control flow words only found in a few implementations, such as the conditional return word `?EXIT` used in Ulrich Hoffmann's preForth, all of Forth's control flow words are executed during compilation to compile various combinations of primitive words along with their branch addresses.

For instance, `IF` and `WHILE`, and the words that match with those, set up `BRANCH` (unconditional branch) and `?BRANCH` (pop a value off the stack, and branch if it is false). Counted loop control flow words work similarly but set up combinations of primitive words that work with a counter, and so on. During compilation, the data stack is used to support control structure balancing, nesting, and back-patching of branch addresses. The snippet:

```mw
 ... DUP 6 < IF DROP 5 ELSE 1 - THEN ...
```

would often be compiled to the following sequence inside a definition:

```mw
 ... DUP LIT 6 < ?BRANCH 5  DROP LIT 5  BRANCH 3  LIT 1 - ...
```

The numbers after `BRANCH` represent relative jump addresses. `LIT` is the primitive word for pushing a "literal" number onto the data stack. (Faster, shorter code would be compiled using pointers to constants instead of `LIT` and embedded data, if any of the numbers involved have been separately defined as constants. There would be similar changes if yet other words were used instead of constants, and so on.)

#### Compilation state and interpretation state

The word `:` (colon) parses a name as a parameter, creates a dictionary entry (a *colon definition*) and enters compilation state. The interpreter continues to read space-delimited words from the user input device. If a word is found, the interpreter executes the *compilation semantics* associated with the word, instead of the *interpretation semantics*. The default compilation semantics of a word are to append its interpretation semantics to the current definition.

The word `;` (semi-colon) finishes the current definition and returns to interpretation state. It is an example of a word whose compilation semantics differ from the default. The interpretation semantics of `;` (semi-colon), most control flow words, and several other words are undefined in ANS Forth, meaning that they must only be used inside of definitions and not on the interactive command line.

The interpreter state can be changed manually with the words `[` (left-bracket) and `]` (right-bracket) which enter interpretation state or compilation state, respectively. These words can be used with the word `LITERAL` to calculate a value during a compilation and to insert the calculated value into the current colon definition. `LITERAL` has the compilation semantics to take an object from the data stack and to append semantics to the current colon definition to place that object on the data stack.

In ANS Forth, the current state of the interpreter can be read from the flag `STATE` which contains the value true when in compilation state and false otherwise. This allows the implementation of so-called *state-smart words* with behavior that changes according to the current state of the interpreter.

#### Immediate words

The word `IMMEDIATE` marks the most recent colon definition as an *immediate word*, effectively replacing its compilation semantics with its interpretation semantics. Immediate words are normally executed during compilation, not compiled, but this can be overridden by the programmer in either state. `;` is an example of an immediate word. In ANS Forth, the word `POSTPONE` takes a name as a parameter and appends the compilation semantics of the named word to the current definition even if the word was marked immediate. Forth-83 defined separate words `COMPILE` and `[COMPILE]` to force the compilation of non-immediate and immediate words, respectively.

Instead of reserving space for an Immediate flag in every definition, some implementations of Forth use an Immediates Dictionary which is checked first when in compile mode.

#### Unnamed words and execution tokens

In ANS Forth, unnamed words can be defined with the word `:NONAME` which compiles the following words up to the next `;` (semi-colon) and leaves an *execution token* on the data stack. The execution token provides an opaque handle for the compiled semantics, similar to the function pointers of the C programming language.

Execution tokens can be stored in variables. The word `EXECUTE` takes an execution token from the data stack and performs the associated semantics. The word `COMPILE,` (compile-comma) takes an execution token from the data stack and appends the associated semantics to the current definition.

The word `'` (tick) takes the name of a word as a parameter and returns the execution token associated with that word on the data stack. In interpretation state, `' RANDOM-WORD EXECUTE` is equivalent to `RANDOM-WORD`.

The words `:` (colon), `POSTPONE`, `'` (tick) are examples of *parsing words* that take their arguments from the user input device instead of the data stack. Another example is the word `(` (paren) which reads and ignores the following words up to and including the next right parenthesis and is used to place comments in a colon definition. Similarly, the word `\` (backslash) is used for comments that continue to the end of the current line. To be parsed correctly, `(` (paren) and `\` (backslash) must be separated by whitespace from the following comment text.

### Structure of code

In most Forth systems, the body of a code definition consists of either machine language, or some form of threaded code. The original Forth which follows the informal FIG standard (Forth Interest Group), is a TIL (Threaded Interpretive Language). This is also called indirect-threaded code, but direct-threaded and subroutine threaded Forths have also become popular in modern times. The fastest modern Forths, such as SwiftForth, VFX Forth, and iForth, compile Forth to native machine code.

### Data objects

When a word is a variable or other data object, the CF points to the runtime code associated with the defining word that created it. A defining word has a characteristic "defining behavior" (creating a dictionary entry plus possibly allocating and initializing data space) and also specifies the behavior of an instance of the class of words constructed by this defining word. Examples include:

**`VARIABLE`**

Names an uninitialized, one-cell memory location. Instance behavior of a

VARIABLE

returns its address on the stack.

**`CONSTANT`**

Names a value (specified as an argument to

CONSTANT

). Instance behavior returns the value.

**`CREATE`**

Names a location; space may be allocated at this location, or it can be set to contain a string or other initialized value. Instance behavior returns the address of the beginning of this space.

Forth also provides a facility by which a programmer can define new application-specific defining words, specifying both a custom defining behavior and instance behavior. Some examples include circular buffers, named bits on an I/O port, and automatically indexed arrays.

Data objects defined by these and similar words are global in scope. The function provided by local variables in other languages is provided by the data stack in Forth (although Forth also has real local variables). Forth programming style uses very few named data objects compared with other languages; typically such data objects are used to contain data which is used by a number of words or tasks (in a multitasked implementation).

Forth does not enforce consistency of data type usage; it is the programmer's responsibility to use appropriate operators to fetch and store values or perform other operations on data.

## Examples

### “Hello, World!”

```mw
 : HELLO  ( -- )  CR ." Hello, World!" ;
```

```
HELLO <cr>
Hello, World!
```

The word `CR` (Carriage Return) causes the output following `CR` to be displayed on a new line. The parsing word `."` (dot-quote) reads a double-quote delimited string and appends code to the current definition so that the parsed string will be displayed upon execution. The space character separating the word `."` from the string `Hello, World!` is not included as part of the string. It is needed so that the parser recognizes `."` as a Forth word.

A standard Forth system is also an interpreter, and the same output can be obtained by typing the following code fragment into the Forth console:

```mw
 CR .( Hello, World!)
```

`.(` (dot-paren) is an immediate word that parses a parenthesis-delimited string and displays it. As with the word `."` the space character separating `.(` from `Hello, World!` is not part of the string.

The word `CR` comes before the text to print. By convention, the Forth interpreter does not start output on a new line. Also by convention, the interpreter waits for input at the end of the previous line, after an `ok` prompt. There is no implied "flush-buffer" action in Forth's `CR`, as sometimes is in other programming languages.

### Mixing states of compiling and interpreting

Here is the definition of a word `EMIT-Q` which when executed emits the single character `Q`:

```mw
 : EMIT-Q   81 ( the ASCII value for the character 'Q' ) EMIT ;
```

This definition was written to use the ASCII value of the `Q` character (81) directly. The text between the parentheses is a comment and is ignored by the compiler. The word `EMIT` takes a value from the data stack and displays the corresponding character.

The following redefinition of `EMIT-Q` uses the words `[` (left-bracket), `]` (right-bracket), `CHAR` and `LITERAL` to temporarily switch to interpreter state, calculate the ASCII value of the `Q` character, return to compilation state and append the calculated value to the current colon definition:

```mw
 : EMIT-Q   [ CHAR Q ]  LITERAL  EMIT ;
```

The parsing word `CHAR` takes a space-delimited word as parameter and places the value of its first character on the data stack. The word `[CHAR]` is an immediate version of `CHAR`. Using `[CHAR]`, the example definition for `EMIT-Q` could be rewritten like this:

```mw
 : EMIT-Q   [CHAR] Q  EMIT ; \ Emit the single character 'Q'
```

This definition used `\` (backslash) for the describing comment.

Both `CHAR` and `[CHAR]` are predefined in ANS Forth. Using `IMMEDIATE` and `POSTPONE`, `[CHAR]` could have been defined like this:

```mw
 : [CHAR]   CHAR  POSTPONE LITERAL ; IMMEDIATE
```

### RC4 cipher program

In 1987, Ron Rivest developed the RC4 cipher-system for RSA Data Security, Inc. Its description follows:

> We have an array of 256 bytes, all different. Every time the array is used it changes by swapping two bytes. The swaps are controlled by counters *i* and *j*, each initially 0. To get a new *i*, add 1. To get a new *j*, add the array byte at the new *i*. Exchange the array bytes at *i* and *j*. The code is the array byte at the sum of the array bytes at *i* and *j*. This is XORed with a byte of the plaintext to encrypt, or the ciphertext to decrypt. The array is initialized by first setting it to 0 through 255. Then step through it using *i* and *j*, getting the new *j* by adding to it the array byte at *i* and a key byte, and swapping the array bytes at *i* and *j*. Finally, *i* and *j* are set to 0. All additions are modulo 256.

The following Standard Forth version uses Core and Core Extension words only.

```mw
0 value ii        0 value jj
0 value KeyAddr   0 value KeyLen
create SArray   256 allot   \ state array of 256 bytes
: KeyArray      KeyLen mod   KeyAddr ;

: get_byte      + c@ ;
: set_byte      + c! ;
: as_byte       255 and ;
: reset_ij      0 TO ii   0 TO jj ;
: i_update      1 +   as_byte TO ii ;
: j_update      ii SArray get_byte +   as_byte TO jj ;
: swap_s_ij
    jj SArray get_byte
       ii SArray get_byte  jj SArray set_byte
    ii SArray set_byte
;

: rc4_init ( KeyAddr KeyLen -- )
    256 min TO KeyLen   TO KeyAddr
    256 0 DO   i i SArray set_byte   LOOP
    reset_ij
    BEGIN
        ii KeyArray get_byte   jj +  j_update
        swap_s_ij
        ii 255 < WHILE
        ii i_update
    REPEAT
    reset_ij
;
: rc4_byte
    ii i_update   jj j_update
    swap_s_ij
    ii SArray get_byte   jj SArray get_byte +   as_byte SArray get_byte  xor
;
```

This is one way to test the code:

```mw
hex
create AKey   61 c, 8A c, 63 c, D2 c, FB c,
: test   cr   0 DO  rc4_byte . LOOP  cr ;
AKey 5 rc4_init
2C F9 4C EE DC  5 test   \ output should be: F1 38 29 C9 DE
```

## Forth engines

A processor designed to support a specific programming language is called a language "engine".

Forth engines are hardware platforms specifically designed to support developing and running programs written in Forth. (Likewise, Lisp machines were specifically designed to support developing and running programs written in Lisp, the Pascal MicroEngine was specifically designed to support developing and running programs written in Pascal, etc.).

The first commercially available single-chip Forth engine was the Rockwell R65F11, a chip that includes a Forth kernel in ROM, an enhanced 6502, SRAM, and various interface circuits that previously required peripheral chips.

Many other commercial CPUs (Harris RTX-2000, Novix NC4016, F21, MARC4, KimKlone, etc.) and many homebrew CPUs (My4TH, J1, H2, Mark 1 FORTH Computer, etc.) are specifically designed to run Forth. Typically they implement common Forth primitives such as the "Forth NEXT" as single instructions.

## Implementations

Because Forth is simple to implement and has no standard reference implementation, there are numerous versions of the language. In addition to supporting the standard varieties of desktop computer systems (POSIX, Microsoft Windows, macOS), many of these Forth systems also target a variety of embedded systems. Listed here are some of the systems which conform to the 1994 ANS Forth standard.

- ASYST, a Forth-like system for data collection and analysis
- Gforth, a portable ANS Forth implementation from the GNU Project
- noForth, an ANS Forth implementation (as far as possible) for Flash microcontrollers (MSP430, RISC-V & RP2040)
- Open Firmware, a bootloader and firmware standard based on ANS Forth
- pForth, portable Forth written in C
- SP-Forth, ANS Forth implementation from the Russian Forth Interest Group (RuFIG)
- Swift Forth, machine code generating implementation from Forth, Inc.
- VFX Forth, optimizing native code Forth
- Firth, an adaptation of Forth for the Little Man Stack Machine computer
- Shi, a fast and tiny embeddable Forth implementation written for the Thumb-2 ISA (ARMv7-M and newer).
