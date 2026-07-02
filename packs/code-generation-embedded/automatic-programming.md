---
title: "Automatic programming"
source: https://en.wikipedia.org/wiki/Automatic_programming
domain: code-generation-embedded
license: CC-BY-SA-4.0
tags: embedded code generation, automatic programming, autocode toolchain, model to c
fetched: 2026-07-02
---

# Automatic programming

In computer science, **automatic programming** is a type of computer programming in which some mechanism generates a computer program, to allow human programmers to write the code at a higher abstraction level.

There has been little agreement on the precise definition of automatic programming, mostly because its meaning has changed over time. David Parnas, tracing the history of "automatic programming" in published research, noted that in the 1940s it described automation of the manual process of punching paper tape. Later it referred to translation of high-level programming languages like Fortran and ALGOL. One of the earliest programs identifiable as a compiler is named Autocode. Parnas concluded that "automatic programming has always been a euphemism for programming in a higher-level language than was then available to the programmer."

Program synthesis is one type of automatic programming where a procedure is created from scratch, based on mathematical requirements.

## Origin

Mildred Koss, an early UNIVAC programmer, explains: "Writing machine code involved several tedious steps—breaking down a process into discrete instructions, assigning specific memory locations to all the commands, and managing the I/O buffers. After following these steps to implement mathematical routines, a sub-routine library, and sorting programs, our task was to look at the larger programming process. We needed to understand how we might reuse tested code and have the machine help in programming. As we programmed, we examined the process and tried to think of ways to abstract these steps to incorporate them into higher-level language. This led to the development of interpreters, assemblers, compilers, and generators—programs designed to operate on or produce other programs, that is, *automatic programming*."

## Generative programming

*Generative programming* and the related term *metaprogramming* are concepts whereby programs can be written "to manufacture software components in an automated way" just as automation has improved "production of traditional commodities such as garments, automobiles, chemicals, and electronics."

The goal is to improve programmer productivity. It is often related to code-reuse topics such as component-based software engineering.

## Source-code generation

*Source code generation* is the process of generating source code based on a description of the problem or an ontological model such as a template and is accomplished with a programming tool such as a template processor or an integrated development environment (IDE). These tools allow generating source code via any of various means.

Modern programming languages are well supported by tools like Json4Swift (Swift) and Json2Kotlin (Kotlin).

Programs that could generate COBOL code include:

- the DYL250/DYL260/DYL270/DYL280 series
- Business Controls Corporation's SB-5
- Peat Marwick Mitchell's PMM2170 application-program-generator package

These application generators supported COBOL inserts and overrides.

A macro processor, such as the C preprocessor, which replaces patterns in source code according to relatively simple rules, is a simple form of source-code generator. Source-to-source code generation tools also exist.

Large language models such as ChatGPT are capable of generating a program's source code from a description of the program given in a natural language.

Many relational database management systems (RDBMS) provide a function that will export the content of the database as SQL data definition queries, which may then be executed to re-import the tables and their data, or migrate them to another RDBMS.

Some languages use *annotations* to generate source code and inject it. For example, this is done in Java and Kotlin using annotations, for example the Project Lombok library which runs at compile time with an annotation processor. There has been a C++ proposal to add token sequence injection using compile-time reflective programming (reflection).

## Low-code applications

A low-code development platform (LCDP) is software that provides an environment programmers use to create application software through graphical user interfaces and configuration instead of traditional computer programming.

## Vibe coding

Vibe coding is a software development practice assisted by artificial intelligence (AI) where the software developer describes a project or task in a prompt to a large language model (LLM) which generates source code automatically. Vibe coding may involve accepting AI-generated code without thorough review of the output, instead relying on results and follow-up prompts to guide changes.

The term was coined in February 2025 by computer scientist Andrej Karpathy, a co-founder of OpenAI and former AI leader at Tesla. Merriam-Webster listed the term in March 2025 as a "slang & trending" expression. It was named the *Collins English Dictionary* Word of the Year for 2025.

Advocates of vibe coding say that it allows even amateur programmers to produce software without the extensive training and skills required for software engineering. Critics point out a lack of accountability, maintainability, and an increased risk of introducing security vulnerabilities in the resulting software.
