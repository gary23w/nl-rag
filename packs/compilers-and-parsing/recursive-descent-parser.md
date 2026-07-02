---
title: "Recursive descent parser"
source: https://en.wikipedia.org/wiki/Recursive_descent_parser
domain: compilers-and-parsing
license: CC-BY-SA-4.0
tags: compiler construction, parser generator, syntax analysis, lexer, lexical analysis, abstract syntax tree
fetched: 2026-07-02
---

# Recursive descent parser

In computer science, a **recursive descent parser** is a kind of top-down parser built from a set of mutually recursive procedures (or a non-recursive equivalent) where each such procedure implements one of the nonterminals of the grammar. Thus the structure of the resulting program closely mirrors that of the grammar it recognizes.

A *predictive parser* is a recursive descent parser that does not require backtracking. Predictive parsing is possible only for the class of LL(*k*) grammars, which are the context-free grammars for which there exists some positive integer *k* that allows a recursive descent parser to decide which production to use by examining only the next *k* tokens of input. The LL(*k*) grammars therefore exclude all ambiguous grammars, as well as all grammars that contain left recursion. Any context-free grammar can be transformed into an equivalent grammar that has no left recursion, but removal of left recursion does not always yield an LL(*k*) grammar. A predictive parser runs in linear time.

Recursive descent with backtracking is a technique that determines which production to use by trying each production in turn. Recursive descent with backtracking is not limited to LL(*k*) grammars, but is not guaranteed to terminate unless the grammar is LL(*k*). Even when they terminate, parsers that use recursive descent with backtracking may require exponential time.

Although predictive parsers are widely used, and are frequently chosen if writing a parser by hand, programmers often prefer to use a table-based parser produced by a parser generator, either for an LL(*k*) language or using an alternative parser, such as LALR or LR. This is particularly the case if a grammar is not in LL(*k*) form, as transforming the grammar to LL to make it suitable for predictive parsing is involved. Predictive parsers can also be automatically generated, using tools like ANTLR.

Predictive parsers can be depicted using transition diagrams for each non-terminal symbol where the edges between the initial and the final states are labelled by the symbols (terminals and non-terminals) of the right side of the production rule.

## Example parser

The following EBNF-like grammar (for Niklaus Wirth's PL/0 programming language, from *Algorithms + Data Structures = Programs*) is in LL(1) form:

```mw
 program = block "." .
 
 block =
     ["const" ident "=" number {"," ident "=" number} ";"]
     ["var" ident {"," ident} ";"]
     {"procedure" ident ";" block ";"} statement .
 
 statement =
     ident ":=" expression
     | "call" ident
     | "begin" statement {";" statement } "end"
     | "if" condition "then" statement
     | "while" condition "do" statement .
 
 condition =
     "odd" expression
     | expression ("="|"#"|"<"|"<="|">"|">=") expression .
 
 expression = ["+"|"-"] term {("+"|"-") term} .
 
 term = factor {("*"|"/") factor} .
 
 factor =
     ident
     | number
     | "(" expression ")" .
```

Terminals are expressed in quotes. Each nonterminal is defined by a rule in the grammar, except for *ident* and *number*, which are assumed to be implicitly defined.

### C implementation

What follows is an implementation of a recursive descent parser for the above language in C. The parser reads in source code, and exits with an error message if the code fails to parse, exiting silently if the code parses correctly.

Notice how closely the predictive parser below mirrors the grammar above. There is a procedure for each nonterminal in the grammar. Parsing descends in a top-down manner until the final nonterminal has been processed.

The program fragment depends the functions `peeksym`, which peeks at the current symbol; `consumesym`, which consumes the symbol to move to the next; and `error`, which displays an error message. These functions are assumed to be provided by the lexer.

```mw
extern void error(const char msg[]);
extern void consumesym();

typedef enum Symbol {
    ident, number, lparen, rparen, times, slash, plus, minus, eql, neq, lss,
    leq, gtr, geq, callsym, beginsym, semicolon, endsym, ifsym, whilesym,
    becomes, thensym, dosym, constsym, comma, varsym, procsym, period, oddsym
} Symbol;
extern Symbol peeksym();

bool accept(Symbol s) {
    if (peeksym() == s) {
        consumesym();
        return true;
    }
    return false;
}

bool expect(Symbol s) {
    if (accept(s)) {
        return true;
    }
    error("expect: unexpected symbol");
    return false;
}

void factor() {
    if (accept(ident) || accept(number)) {
        return;
    }
    if (accept(lparen)) {
        expression();
        expect(rparen);
    } else {
        error("factor: syntax error");
        consumesym();
    }
}

void term() {
    factor();
    while (peeksym() == times || peeksym() == slash) {
        consumesym();
        factor();
    }
}

void expression() {
    if (peeksym() == plus || peeksym() == minus) {
        consumesym();
    }
    term();
    while (peeksym() == plus || peeksym() == minus) {
        consumesym();
        term();
    }
}

void condition() {
    if (accept(oddsym)) {
        expression();
        return;
    }
    expression();
    if (peeksym() == eql || peeksym() == neq || peeksym() == lss || peeksym() == leq || peeksym() == gtr || peeksym() == geq) {
        consumesym();
        expression();
    } else {
        error("condition: invalid operator");
        consumesym();
    }
}

void statement() {
    if (accept(ident)) {
        expect(becomes);
        expression();
    } else if (accept(callsym)) {
        expect(ident);
    } else if (accept(beginsym)) {
        do {
            statement();
        } while (accept(semicolon));
        expect(endsym);
    } else if (accept(ifsym)) {
        condition();
        expect(thensym);
        statement();
    } else if (accept(whilesym)) {
        condition();
        expect(dosym);
        statement();
    } else {
        error("statement: syntax error");
        consumesym();
    }
}

void block() {
    if (accept(constsym)) {
        do {
            expect(ident);
            expect(eql);
            expect(number);
        } while (accept(comma));
        expect(semicolon);
    }
    if (accept(varsym)) {
        do {
            expect(ident);
        } while (accept(comma));
        expect(semicolon);
    }
    while (accept(procsym)) {
        expect(ident);
        expect(semicolon);
        block();
        expect(semicolon);
    }
    statement();
}

void program() {
    block();
    expect(period);
}
```

## Examples

Some recursive descent parser generators:

- TMG – an early compiler-compiler used in the 1960s and early 1970s
- JavaCC
- Coco/R
- ANTLR
- Spirit Parser Framework – a C++ recursive descent parser generator framework requiring no pre-compile step
- parboiled (Java) – a recursive descent PEG parsing library for Java

The C++ front-end of the Clang compiler contains a hand-written parser based on the recursive-descent parsing algorithm.
