---
title: "ALGOL W"
source: https://en.wikipedia.org/wiki/ALGOL_W
domain: algol-family
license: CC-BY-SA-4.0
tags: algol language, john backus, imperative programming, structured programming, backus naur form
fetched: 2026-07-02
---

# ALGOL W

**ALGOL W** is a programming language. It is based on a proposal for ALGOL X by Niklaus Wirth and Tony Hoare as a successor to ALGOL 60. ALGOL W is a relatively simple upgrade of the original ALGOL 60, adding string, bitstring, complex number and reference to record data types and call-by-result passing of parameters, introducing the `while` statement, replacing `switch` with the `case` statement, and generally tightening up the language.

Wirth's entry was considered too little of an advance over ALGOL 60, and the more complex entry from Adriaan van Wijngaarden that would later become ALGOL 68 was selected in a highly contentious meeting. Wirth later published his version as *A contribution to the development of ALGOL*. With a number of small additions, this eventually became ALGOL W.

Wirth supervised a high-quality implementation for the IBM System/360 at Stanford University that was widely distributed. The implementation was written in PL360, an ALGOL-like assembly language designed by Wirth. The implementation includes influential debugging and profiling abilities.

ALGOL W served as the basis for the Pascal language, and the syntax of ALGOL W will be immediately familiar to anyone with Pascal experience. The key differences are improvements to record handling in Pascal, and, oddly, the loss of ALGOL W's ability to define the length of an array at runtime, which is one of Pascal's most-complained-about features.

## Syntax and semantics

ALGOL W's syntax is built on a subset of the EBCDIC character encoding set. In ALGOL 60, reserved words are distinct lexical items, but in ALGOL W, they are only sequences of characters, and do not need to be stropped. Reserved words and identifiers are separated by spaces. In these ways, ALGOL W's syntax resembles that of Pascal and later languages.

The *ALGOL W Language Description* defines ALGOL W in an affix grammar that resembles Backus–Naur form (BNF). This formal grammar was a precursor of the Van Wijngaarden grammar.

Much of ALGOL W's semantics is defined grammatically:

- Identifiers are distinguished by their definition within the current scope. For example, a `⟨procedure identifier⟩` is an identifier that has been defined by a procedure declaration, a `⟨label identifier⟩` is an identifier that is being used as a goto label.
- The types of variables and expressions are represented by affixes. For example, `⟨τ function identifier⟩` is the syntactic entity for a function that returns a value of type `τ`, if an identifier has been declared as an integer function in the current scope, then that is expanded to `⟨integer function identifier⟩`.
- Type errors are grammatical errors. For example, `⟨integer expression⟩ / ⟨integer expression⟩` and `⟨real expression⟩ / ⟨real expression⟩` are valid but distinct syntactic entities that represent expressions, but `⟨real expression⟩ DIV ⟨integer expression⟩` (i.e., integer division performed on a floating-point value) is an invalid syntactic entity.

## Example

This demonstrates ALGOL W's record type facility, including use of the null reference.

```mw
RECORD PERSON (
    STRING(20) NAME; 
    INTEGER AGE; 
    LOGICAL MALE; 
    REFERENCE(PERSON) FATHER, MOTHER, YOUNGESTOFFSPRING, ELDERSIBLING
);

REFERENCE(PERSON) PROCEDURE YOUNGESTUNCLE (REFERENCE(PERSON) R);
    BEGIN
        REFERENCE(PERSON) P, M;
        P := YOUNGESTOFFSPRING(FATHER(FATHER(R)));
        WHILE (P ¬= NULL) AND (¬ MALE(P)) OR (P = FATHER(R)) DO
            P := ELDERSIBLING(P);
        M := YOUNGESTOFFSPRING(MOTHER(MOTHER(R)));
        WHILE (M ¬= NULL) AND (¬ MALE(M)) DO
            M := ELDERSIBLING(M);
        IF P = NULL THEN 
            M 
        ELSE IF M = NULL THEN 
            P 
        ELSE 
            IF AGE(P) < AGE(M) THEN P ELSE M
    END
```
