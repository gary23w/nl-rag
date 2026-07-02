---
title: "Literate programming"
source: https://en.wikipedia.org/wiki/Literate_programming
domain: paradigms
license: CC-BY-SA-4.0
tags: programming paradigm, object-oriented, functional programming, declarative, imperative programming
fetched: 2026-07-02
---

# Literate programming

**Literate programming** (**LP**) is a programming paradigm introduced in 1984 by Donald Knuth in which a computer program is given as an explanation of how it works in a natural language, such as English, interspersed (embedded) with snippets of macros and traditional source code, from which compilable source code can be generated. The approach is used in scientific computing and in data science routinely for reproducible research and open access purposes. Literate programming tools are used by millions of programmers today.

The literate programming paradigm, as conceived by Donald Knuth, represents a move away from writing computer programs in the manner and order imposed by the compiler, and instead gives programmers macros to develop programs in the order demanded by the logic and flow of their thoughts. Literate programs are written as an exposition of logic in more natural language in which macros are used to hide abstractions and traditional source code, more like the text of an essay.

Literate programming tools are used to obtain two representations from a source file: one understandable by a compiler or interpreter, the "tangled" code, and another for viewing as formatted documentation, which is said to be "woven" from the literate source. While the first generation of literate programming tools were computer language-specific, the later ones are language-agnostic and exist beyond the individual programming languages.

## History and philosophy

Literate programming was first introduced in 1984 by Donald Knuth, who intended it to create programs that were suitable literature for human beings. He implemented it at Stanford University as a part of his research on algorithms and digital typography. The implementation was called "WEB" since he believed that it was one of the few three-letter words of English that had not yet been applied to computing. However, it resembles the complicated nature of software delicately pieced together from simple materials. The practice of literate programming has seen an important resurgence in the 2010s with the use of computational notebooks, especially in data science.

## Concept

Literate programming is writing out the program logic in a human language with included (separated by a primitive markup) code snippets and macros. Macros in a literate source file are simply title-like or explanatory phrases in a human language that describe human abstractions created while solving the programming problem, and hiding chunks of code or lower-level macros. These macros are similar to the algorithms in pseudocode typically used in teaching computer science. These arbitrary explanatory phrases become precise new operators, created on the fly by the programmer, forming a *meta-language* on top of the underlying programming language.

A preprocessor is used to substitute arbitrary hierarchies, or rather "interconnected 'webs' of macros", to produce the compilable source code with one command ("tangle"), and documentation with another ("weave"). The preprocessor also provides an ability to write out the content of the macros and to add to already created macros in any place in the text of the literate program source file, thereby disposing of the need to keep in mind the restrictions imposed by traditional programming languages or to interrupt the flow of thought.

### Advantages

According to Knuth, literate programming provides higher-quality programs, since it forces programmers to explicitly state the thoughts behind the program, making poorly thought-out design decisions more obvious. Knuth also claims that literate programming provides a first-rate documentation system, which is not an add-on, but is grown naturally in the process of exposition of one's thoughts during a program's creation. The resulting documentation allows the author to restart their own thought processes at any later time, and allows other programmers to understand the construction of the program more easily. This differs from traditional documentation, in which a programmer is presented with source code that follows a compiler-imposed order, and must decipher the thought process behind the program from the code and its associated comments. The meta-language capabilities of literate programming are also claimed to facilitate thinking, giving a higher "bird's eye view" of the code and increasing the number of concepts the mind can successfully retain and process. Applicability of the concept to programming on a large scale, that of commercial-grade programs, is proven by an edition of TeX code as a literate program.

Knuth also claims that literate programming can lead to easy porting of software to multiple environments, and even cites the implementation of TeX as an example.

### Contrast with documentation generation

Literate programming is very often misunderstood to refer only to formatted documentation produced from a common file with both source code and comments – which is properly called documentation generation – or to voluminous commentaries included with code. This is the converse of literate programming: well-documented code or documentation extracted from code follows the structure of the code, with documentation embedded in the code; while in literate programming, code is embedded in documentation, with the code following the structure of the documentation.

This misconception has led to claims that comment-extraction tools, such as the Perl Plain Old Documentation or Java Javadoc systems, are "literate programming tools". However, because these tools do not implement the "web of abstract concepts" hiding behind the system of natural-language macros, or provide an ability to change the order of the source code from a machine-imposed sequence to one convenient to the human mind, they cannot properly be called literate programming tools in the sense intended by Knuth.

## Workflow

Implementing literate programming consists of two steps:

1. Weaving: Generating a comprehensive document about the program and its maintenance.
2. Tangling: Generating machine executable code

Weaving and tangling are done on the same source so that they are consistent with each other.

## Example

A classic example of literate programming is the literate implementation of the standard Unix `wc` word counting program. Knuth presented a CWEB version of this example in Chapter 12 of his *Literate Programming* book. The same example was later rewritten for the noweb literate programming tool. This example provides a good illustration of the basic elements of literate programming.

### Creation of macros

The following snippet of the `wc` literate program shows how arbitrary descriptive phrases in a natural language are used in a literate program to create macros, which act as new "operators" in the literate programming language, and hide chunks of code or other macros. The mark-up notation consists of double angle brackets (`<<...>>`) that indicate macros. The `@` symbol which, in a noweb file, indicates the beginning of a documentation chunk. The `<<*>>` symbol stands for the "root", topmost node the literate programming tool will start expanding the web of macros from. Actually, writing out the expanded source code can be done from any section or subsection (i.e. a piece of code designated as `<<name of the chunk>>=`, with the equal sign), so one literate program file can contain several files with machine source code.

```mw
The purpose of wc is to count lines, words, and/or characters in a list of files. The
number of lines in a file is ......../more explanations/

Here, then, is an overview of the file wc.c that is defined by the noweb program wc.nw:
    <<*>>=
    <<Header files to include>>
    <<Definitions>>
    <<Global variables>>
    <<Functions>>
    <<The main program>>
    @

We must include the standard I/O definitions, since we want to send formatted output
to stdout and stderr.
    <<Header files to include>>=
    #include <stdio.h>
    @
```

The unraveling of the chunks can be done in any place in the literate program text file, not necessarily in the order they are sequenced in the enclosing chunk, but as is demanded by the logic reflected in the explanatory text that envelops the whole program.

### Program as a web

Macros are not the same as "section names" in standard documentation. Literate programming macros hide the real code behind themselves, and be used inside any low-level machine language operators, often inside logical operators such as `if`, `while` or `case`. This can be seen in the following `wc` literate program.

```mw
The present chunk, which does the counting, was actually one of
the simplest to write. We look at each character and change state if it begins or ends
a word.

    <<Scan file>>=
    while (1) {
      <<Fill buffer if it is empty; break at end of file>>
      c = *ptr++;
      if (c > ' ' && c < 0177) {
        /* visible ASCII codes */
        if (!in_word) {
          word_count++;
          in_word = 1;
        }
        continue;
      }
      if (c == '\n') line_count++;
      else if (c != ' ' && c != '\t') continue;
      in_word = 0;
        /* c is newline, space, or tab */
    }
    @
```

The macros stand for any chunk of code or other macros, and are more general than top-down or bottom-up "chunking", or than subsectioning. Donald Knuth said that when he realized this, he began to think of a program as a *web* of various parts.

### Order of human logic, not that of the compiler

In a noweb literate program besides the free order of their exposition, the chunks behind macros, once introduced with `<<...>>=`, can be grown later in any place in the file by simply writing `<<name of the chunk>>=` and adding more content to it, as the following snippet illustrates (`+` is added by the document formatter for readability, and is not in the code).

```mw
The grand totals must be initialized to zero at the beginning of the program.
If we made these variables local to main, we would have to do this  initialization
explicitly; however, C globals are automatically zeroed. (Or rather,``statically
zeroed.'⁠' (Get it?)

    <<Global variables>>+=
    long tot_word_count, tot_line_count,
         tot_char_count;
      /* total number of words, lines, chars */
    @
```

### Record of the train of thought

The documentation for a literate program is produced as part of writing the program. Instead of comments provided as side notes to source code a literate program contains the explanation of concepts on each level, with lower level concepts deferred to their appropriate place, which allows better communication of thought. The snippets of the literate `wc` above show how an explanation of the program and its source code are interwoven. Such exposition of ideas creates the flow of thought that is like a literary work. Knuth wrote a "novel" which explains the code of the interactive fiction game Colossal Cave Adventure.

### Remarkable examples

- TeX and METAFONT, Knuth's respective typesetting and font description languages. Written in WEB, these were literate programming's proofs of concept.
- Physically Based Rendering "describes both the mathematical theory behind a modern photorealistic rendering system and its practical implementation." This book won an Academy Award.
- Understanding MP3, a complete implementation of MPEG bit streams that is also an excellent tutorial. (See also Ruckert's literate programs related to HINT.)
- Principia Softwarica, a literate version of Plan 9 from Bell Labs.
- The Stanford GraphBase, 30 short CWEB essays from Knuth that define a combinatorial computing platform, describe state-of-the-art algorithms and data structures, and provide examples of their use.
- MMIXware, Knuth's software to support MMIX programming and run simulations on different architectures.
- C Interfaces and Implementations, a demonstration of the titular design methodology in 24 examples.
- A Retargetable C Compiler, describes the little C compiler LCC.
- Data Structures and Algorithms in C++: Pocket Primer, a concise pedagogic tour.
- Inform, a language and system for writing interactive fiction. One of the largest literate programs to date, Inform is written in inweb (itself a remarkable example).
- Axiom, which is evolved from scratchpad, a computer algebra system developed by IBM. It is now being developed by Tim Daly, one of the developers of scratchpad, Axiom is totally written as a literate program.

## Literate programming practices

The first published literate programming environment was WEB, introduced by Knuth in 1981 for his TeX typesetting system; it uses Pascal as its underlying programming language and TeX for typesetting of the documentation. The complete commented TeX source code was published in Knuth's *TeX: The program*, volume B of his 5-volume *Computers and Typesetting*. Knuth had privately used a literate programming system called DOC as early as 1979. He was inspired by the ideas of Pierre-Arnoul de Marneffe. The free CWEB, written by Knuth and Silvio Levy, is WEB adapted for C and C++, runs on most operating systems, and can produce TeX and PDF documentation.

There are various other implementations of the literate programming concept as given below. Many of the newer among these do not have macros and hence do not comply with the order of human logic principle, which makes them perhaps "semi-literate" tools. These, however, allow cellular execution of code which makes them more along the lines of exploratory programming tools.

| Name | Supported languages | Written in | Markup language | Macros & custom order | Cellular execution | Comments |
|---|---|---|---|---|---|---|
| WEB | Pascal | Pascal | TeX | Yes | No | The first published literate programming environment. |
| CWEB | C++ and C | C | TeX | Yes | No | Is WEB adapted for C and C++. |
| NoWEB | Any | C, AWK, and Icon | LaTeX, TeX, HTML and troff | Yes | No | It is well known for its simplicity and for allowing text formatting in HTML rather than going through the TeX system. |
| Emacs org-mode | Any | Emacs Lisp | Plain text |   |   | Requires Babel, which allows embedding blocks of source code from multiple programming languages within one text document. Blocks of code can share data with each other, display images inline, or be parsed into pure source code using the noweb reference syntax. |
| CoffeeScript | CoffeeScript | CoffeeScript, JavaScript | Markdown |   |   | CoffeeScript supports a "literate" mode, which enables programs to be compiled from a source document written in Markdown with indented blocks of code. |
| Maple worksheets | Maple (software) |   | XML |   |   | Maple worksheets are a platform-agnostic literate programming environment that combines text and graphics with live code for symbolic computation.*"Maple Worksheets". *MapleSoft.com*. Retrieved May 30, 2020.* |
| Wolfram Notebooks | Wolfram Language |   | Wolfram Language |   |   | Wolfram notebooks are a platform-agnostic literate programming method that combines text and graphics with live code. |
| Jupyter Notebook, formerly IPython Notebook | Python and any with a Jupyter Kernel |   | JSON format Specification for ipynb | No | Yes | Works in the format of notebooks, which combine headings, text (including LaTeX), plots, etc. with the written code. |
| nbdev | Python and Jupyter Notebook |   | `nbdev` is a library that allows developing a python library in Jupyter Notebooks, putting all code, tests and documentation in one place. |   |   |   |
| Julia |   |   |   | Pluto.jl is a reactive notebook environment allowing custom order. But web-like macros aren't supported. | Yes | Supports the iJulia mode of development which was inspired by iPython. |
| Agda |   |   |   |   |   | Supports a limited form of literate programming out of the box. |
| Sweave | R |   | PDF |   |   |   |
| Knitr | R |   | LaTeX, PDF, LyX, HTML, Markdown, AsciiDoc, and reStructuredText |   |   |   |
| Literate | Any | D | Markdown | Yes | No | Supports TeX equations. Compatible with Vim. |

Other useful tools include:

- The Leo text editor is an *outlining* editor which supports optional noweb and CWEB markup. The author of Leo mixes two different approaches: first, Leo is an outlining editor, which helps with management of large texts; second, Leo incorporates some of the ideas of literate programming, which in its pure form (i.e., the way it is used by Knuth Web tool or tools like "noweb") is possible only with some degree of inventiveness and the use of the editor in a way not exactly envisioned by its author (in modified @root nodes). However, this and other extensions (@file nodes) make outline programming and text management successful and easy and in some ways similar to literate programming.
- The Haskell language has native support for semi-literate programming. The compiler–interpreter supports two file name extensions: `.hs` and `.lhs`; the latter stands for literate Haskell. The literate scripts can be full LaTeX source text, at the same time it can be compiled, with no changes, because the interpreter only compiles the text in a code environment, for example: % here text describing the function: \begin{code} fact 0 = 1 fact (n+1) = (n+1) * fact n \end{code} here more text The code can be also marked in the Richard Bird style, starting each line with a greater than symbol and a space, preceding and ending the piece of code with blank lines. The LaTeX `listings` package provides a `lstlisting` environment which can be used to embellish the source code. It can be used to define a `code` environment to use within Haskell to print the symbols in the following manner: \newenvironment{code}{\lstlistings[language=Haskell]}{\endlstlistings} \begin{code} comp :: (beta -> gamma) -> (alpha -> beta) -> (alpha -> gamma) (g `comp` f) x = g(f x) \end{code} which can be configured to yield: ${\begin{aligned}&comp::(\beta \to \gamma )\to (\alpha \to \beta )\to (\alpha \to \gamma )\\&(g\operatorname {comp} f)x=g(fx)\end{aligned}}$ Although the package provides no means to organize chunks of code, LaTeX source code can be divided in different files.
- The Web 68 Literate Programming system used ALGOL 68 as the underlying language, although there was nothing in the pre-processor 'tang' to force such use.
- The customization mechanism of the Text Encoding Initiative (TEI) which enables constraining, modifying, or extending the TEI scheme, enables mixing prose documentation with fragments of schema specification in the One Document Does-it-all format. From this prose documentation, schemas, and processing model pipelines can be generated and Knuth's Literate Programming paradigm is cited as the inspiration for this way of working.
