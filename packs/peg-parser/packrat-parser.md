---
title: "Packrat parser"
source: https://en.wikipedia.org/wiki/Packrat_parser
domain: peg-parser
license: CC-BY-SA-4.0
tags: parsing expression grammar, peg parser, packrat parsing, top-down parsing
fetched: 2026-07-02
---

# Packrat parser

The **Packrat parser** is a type of parser that shares similarities with the recursive descent parser in its construction. However, it differs because it takes parsing expression grammars (PEGs) as input rather than LL grammars.

In 1970, Alexander Birman laid the groundwork for packrat parsing by introducing the "TMG recognition scheme" (TS), and "generalized TS" (gTS). TS was based upon Robert M. McClure's TMG compiler-compiler, and gTS was based upon Dewey Val Schorre's META compiler-compiler. Birman's work was later refined by Aho and Ullman; and renamed as Top-Down Parsing Language (TDPL), and Generalized TDPL (GTDPL), respectively. These algorithms were the first of their kind to employ deterministic top-down parsing with backtracking.

Bryan Ford developed PEGs as an expansion of GTDPL and TS. Unlike CFGs, PEGs are unambiguous and can match well with machine-oriented languages. PEGs, similar to GTDPL and TS, can also express all LL(k) and LR(k). Ford also introduced Packrat as a parser that uses memoization techniques on top of a simple PEG parser. This was done because PEGs have an unlimited lookahead capability resulting in a parser with exponential time performance in the worst case.

Packrat keeps track of the intermediate results for all mutually recursive parsing functions. Each parsing function is only called once at a specific input position. In some instances of packrat implementation, if there is insufficient memory, certain parsing functions may need to be called multiple times at the same input position, causing the parser to take longer than linear time.

## Syntax

The packrat parser takes in input the same syntax as PEGs: a simple PEG is composed of terminal and nonterminal symbols, possibly interleaved with operators that compose one or several derivation rules.

### Symbols

- Nonterminal symbols are indicated with capital letters (e.g., $\{S,E,F,D\}$ )
- Terminal symbols are indicated with lowercase (e.g., $\{a,b,z,e,g\}$ )
- Expressions are indicated with lower-case Greek letter (e.g., $\{\alpha ,\beta ,\gamma ,\omega ,\tau \}$ )
  - Expressions can be a mix of terminal symbols, nonterminal symbols and operators

### Operators

| Operator | Semantics |
|---|---|
| Sequence $\alpha \beta$ | **Success:** If $\alpha$ and $\beta$ are recognized **Failure:** If $\alpha$ or $\beta$ are not recognized **Consumed:** $\alpha$ and $\beta$ in case of success |
| Ordered choice $\alpha /\beta /\gamma$ | **Success:** If any of $\{\alpha ,\beta ,\gamma \}$ is recognized starting from the left **Failure:** All of $\{\alpha ,\beta ,\gamma \}$ do not match **Consumed:** The atomic expression that has generated a success so if multiple succeed the first one is always returned |
| And predicate $\&\alpha$ | **Success:** If $\alpha$ is recognized **Failure:** If $\alpha$ is not recognized **Consumed:** No input is consumed |
| Not predicate ${\displaystyle$ | **Success:** If $\alpha$ is not recognized **Failure:** If $\alpha$ is recognized **Consumed:** No input is consumed |
| One or more $\alpha +$ | **Success:** Try to recognize $\alpha$ one or multiple time **Failure:** If $\alpha$ is not recognized **Consumed:** The maximum number that $\alpha$ is recognized |
| Zero or more $\alpha *$ | **Success:** Try to recognize $\alpha$ zero or multiple time **Failure:** Cannot fail **Consumed:** The maximum number that $\alpha$ is recognized |
| Zero or one ${\displaystyle \alpha$ | **Success:** Try to recognize $\alpha$ zero or once **Failure:** Cannot fail **Consumed:** $\alpha$ if it is recognized |
| Terminal range [ $a-b$ ] | **Success:** Recognize any terminal c that are inside the range $[a-b]$ . In the case of $[{\textbf {'}}h{\textbf {'}}-{\textbf {'}}z{\textbf {'}}]$ , c can be any letter from h to z **Failure:** If no terminal inside of $[a-b]$ can be recognized **Consumed:** c if it is recognized |
| Any character . | **Success:** Recognize any character in the input **Failure:** If no character in the input **Consumed:** any character in the input |

### Rules

A derivation rule is composed by a nonterminal symbol and an expression $S\rightarrow \alpha$ .

A special expression $\alpha _{s}$ is the starting point of the grammar. In case no $\alpha _{s}$ is specified, the first expression of the first rule is used.

An input string is considered accepted by the parser if the $\alpha _{s}$ is recognized. As a side-effect, a string x can be recognized by the parser even if it was not fully consumed.

An extreme case of this rule is that the grammar $S\rightarrow x*$ matches any string.

This can be avoided by rewriting the grammar as $S\rightarrow x*!.$

### Example

${\begin{cases}S\rightarrow A/B/D\\A\rightarrow {\texttt {'a'}}\ S\ {\texttt {'a'}}\\B\rightarrow {\texttt {'b'}}\ S\ {\texttt {'b'}}\\D\rightarrow ({\texttt {'0'}}-{\texttt {'9'}})?\end{cases}}$

This grammar recognizes some palindromes over the alphabet $\{a,b\}$ , with an optional digit in the middle.

Example strings accepted by the grammar include: ${\texttt {'aa'}}$ and ${\texttt {'aba3aba'}}$ . But it fails to accept ${\texttt {'aaaa'}}$ .

### Left recursion

Left recursion happens when a grammar production refers to itself as its left-most element, either directly or indirectly. Since Packrat is a recursive descent parser, it cannot handle left recursion directly. During the early stages of development, it was found that a production that is left-recursive can be transformed into a right-recursive production. This modification significantly simplifies the task of a Packrat parser. Nonetheless, if there is an indirect left recursion involved, the process of rewriting can be quite complex and challenging. If the time complexity requirements are loosened from linear to superlinear, it is possible to modify the memoization table of a Packrat parser to permit left recursion, without altering the input grammar.

### Iterative combinator

The iterative combinators $\alpha +$ and $\alpha *$ need special attention when used in a Packrat parser: these combinators introduce a *secret* recursion that does not record intermediate results in the outcome matrix, which can lead to the parser operating with a superlinear behaviour. This problem can be resolved by applying the following transformation:

| Original | Translated |
|---|---|
| $S\rightarrow \alpha +$ | $S\rightarrow \alpha S/\alpha$ |
| $S\rightarrow \alpha *$ | $S\rightarrow \alpha S/\epsilon$ |

With this transformation, the intermediate results can be properly memoized.

## Memoization technique

Memoization is an optimization technique in computing that aims to speed up programs by storing the results of expensive function calls. This technique essentially works by caching the results so that when the same inputs occur again, the cached result is simply returned, thus avoiding the time-consuming process of re-computing. When using packrat parsing and memoization, it's noteworthy that the parsing function for each nonterminal is solely based on the input string. It does not depend on any information gathered during the parsing process. Essentially, memoization table entries do not affect or rely on the parser's specific state at any given time.

Packrat parsing stores results in a matrix or similar data structure that allows for quick look-ups and insertions. When a production is encountered, the matrix is checked to see if it has already occurred. If it has, the result is retrieved from the matrix. If not, the production is evaluated, the result is inserted into the matrix, and then returned. When evaluating the entire $m*n$ matrix in a tabular approach, it would require $\Theta (mn)$ space. Here, m represents the number of nonterminals, and n represents the input string size.

In a naïve implementation, the entire table can be derived from the input string starting from the end of the string.

The Packrat parser can be improved to update only the necessary cells in the matrix through a depth-first visit of each subexpression tree. Consequently, using a matrix with dimensions of $m*n$ is often wasteful, as most entries would remain empty. These cells are linked to the input string, not to the nonterminals of the grammar. This means that increasing the input string size would always increase memory consumption, while the number of parsing rules changes only the worst space complexity.

### Cut operator

Another operator called *cut* has been introduced to Packrat to reduce its average space complexity even further. This operator utilizes the formal structures of many programming languages to eliminate impossible derivations. For instance, control statements parsing in a standard programming language is mutually exclusive from the first recognized token, e.g., $\{{\mathtt {if,do,while,switch}}\}$ .

| Operator | Semantics |
|---|---|
| Cut ${\begin{array}{l}\alpha \uparrow \beta /\gamma \\(\alpha \uparrow \beta )*\end{array}}$ | if $\alpha$ is recognized but $\beta$ is not, skip the evaluation of the alternative. In the first case don't evaluate $\gamma$ if $\alpha$ was recognized The second rule is can be rewritten as $N\rightarrow \alpha \uparrow \beta N/\epsilon$ and the same rules can be applied. |

When a Packrat parser uses cut operators, it effectively clears its backtracking stack. This is because a cut operator reduces the number of possible alternatives in an ordered choice. By adding cut operators in the right places in a grammar's definition, the resulting Packrat parser only needs a nearly constant amount of space for memoization. However, the fundamental problem that packrat parsers require O(n) space has not been resolved.

## The algorithm

Sketch of an implementation of a Packrat algorithm in a Lua-like pseudocode.

```mw
INPUT(n) -- return the character at position n

RULE(R : Rule, P : Position )
    entry = GET_MEMO(R,P) -- return the number of elements previously matched in rule R at position P
    if entry == nil then
        return EVAL(R, P);
    end
    return entry;

EVAL(R : Rule, P : Position )
    start = P;   
    for choice in R.choices -- Return a list of choice
        acc=0;
        for symbol in choice then -- Return each element of a rule, terminal and nonterminal
            if symbol.is_terminal then
                if INPUT(start+acc) == symbol.terminal then
                    acc = acc + 1; --Found correct terminal skip pass it
                else
                    break;                
                end
            else 
                res = RULE(symbol.nonterminal , start+acc ); -- try to recognize a nonterminal in position start+acc
                SET_MEMO(symbol.nonterminal , start+acc, res ); -- we memoize also the failure with special value fail
                if res == fail then  
                    break; 
                end
                acc = acc + res;
            end
            if symbol == choice.last -- check if we have matched the last symbol in a choice if so return
                return acc;
        end
    end
    return fail; --if no choice match return fail
```

## Example

Given the following context, a free grammar that recognizes simple arithmetic expressions composed of single digits interleaved by sum, multiplication, and parenthesis.

${\begin{cases}S\rightarrow A\\A\rightarrow M\ {\texttt {'+'}}\ A\ /\ M\\M\rightarrow P\ {\texttt {'*'}}\ M\ /\ P\\P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}\ /\ D\\D\rightarrow ({\texttt {'0'}}-{\texttt {'9'}})\end{cases}}$

Denoted with ⊣ the line terminator we can apply the *packrat algorithm*

| Syntax tree | Action | Packrat Table |
|---|---|---|
|   | Derivation Rules Input shifted ${\begin{array}{l}S\rightarrow A\\A\rightarrow M\ {\texttt {'+'}}\ A\\M\rightarrow P\ {\texttt {'*'}}\ M\\P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}\end{array}}$ ɛ Notes Input left Input doesn't match the first element in the derivation. Backtrack to the first grammar rule with unexplored alternative ${\textstyle P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}\ /\ {\underline {D}}}$ 2*(3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** **P** **D** 2 * ( 3 + 4 ) No update because no terminal was recognized |
|   | Derivation Rules Input shifted $P\rightarrow D$ $D\rightarrow 2$ 2 Notes Input left Shift input by one after deriving terminal 2 *(3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** **P** 1 **D** 1 2 * ( 3 + 4 ) **Update:** D(1) = 1; P(1) = 1; |
|   | Derivation Rules Input shifted $M\rightarrow P\ {\texttt {'*'}}\ M$ $P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}$ 2*( Notes Input left Shift input by two terminal $\{{\texttt {*}},{\texttt {(}}\}$ 3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** **P** 1 **D** 1 2 * ( 3 + 4 ) No update because no nonterminal was fully recognized |
|   | Derivation Rules Input shifted $A\rightarrow M\ {\texttt {'+'}}\ A$ $M\rightarrow P\ {\texttt {'*'}}\ M$ $P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}$ 2*( Notes Input left Input doesn't match the first element in the derivation. Backtrack to the first grammar rule with unexplored alternative ${\textstyle P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}\ /\ {\underline {D}}}$ 3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** **P** 1 **D** 1 2 * ( 3 + 4 ) No update because no terminal was recognized |
|   | Derivation Rules Input shifted $P\rightarrow D$ $D\rightarrow 3$ 2*( Notes Input left Shift input by one after deriving terminal 3 but the new input will not match inside $M\rightarrow P\ {\texttt {'*'}}\ M$ so an unroll is necessary to $M\rightarrow P\ {\texttt {'*'}}\ M\ /\ {\underline {P}}$ 3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** **P** 1 1 **D** 1 1 2 * ( 3 + 4 ) **Update:** D(4) = 1; P(4) = 1; |
|   | Derivation Rules Input shifted $M\rightarrow P$ 2*(3+ Notes Input left Roll Back to $M\rightarrow P\ {\texttt {'*'}}\ M\ /\ {\underline {P}}$ And we don't expand it has we have an hit in the memoization table P(4) ≠ 0 so shift the input by P(4). Shift also the + from $A\rightarrow M\ {\texttt {'+'}}\ A$ 4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** 1 **P** 1 1 **D** 1 1 2 * ( 3 + 4 ) Hit on P(4) Update M(4) = 1 as M was recognized |
|   | Derivation Rules Input shifted $A\rightarrow M\ {\texttt {'+'}}\ A$ $M\rightarrow P\ {\texttt {'*'}}\ M$ $P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}$ 2*(3+ Notes Input left Input doesn't match the first element in the derivation. Backtrack to the first grammar rule with unexplored alternative ${\textstyle P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}\ /\ {\underline {D}}}$ 4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** 1 **P** 1 1 **D** 1 1 2 * ( 3 + 4 ) No update because no terminal was recognized |
|   | Derivation Rules Input shifted $P\rightarrow D$ $D\rightarrow 4$ 2*(3+ Notes Input left Shift input by one after deriving terminal 4 but the new input will not match inside $M\rightarrow P\ {\texttt {'*'}}\ M$ so an unroll is necessary 4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** 1 **P** 1 1 1 **D** 1 1 1 2 * ( 3 + 4 ) **Update:** D(6) = 1; P(6) = 1; |
|   | Derivation Rules Input shifted $M\rightarrow P$ 2*(3+ Notes Input left Roll Back to $M\rightarrow P\ {\texttt {'*'}}\ M\ /\ {\underline {P}}$ And we don't expand it has we have an hit in the memoization table P(6) ≠ 0 so shift the input by P(6). but the new input will not match + inside $A\rightarrow M\ {\texttt {'+'}}\ A$ so an unroll is necessary 4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** **M** 1 1 **P** 1 1 1 **D** 1 1 1 2 * ( 3 + 4 ) Hit on P(6) Update M(6) = 1 as M was recognized |
|   | Derivation Rules Input shifted $A\rightarrow M$ 2*(3+4) Notes Input left Roll Back to $A\rightarrow M\ {\texttt {'+'}}\ A\ /\ {\underline {M}}$ And we don't expand it has we have an hit in the memoization table M(6) ≠ 0 so shift the input by M(6). Also shift ) from $P\rightarrow {\texttt {'('}}\ A\ {\texttt {')'}}$ ⊣ | Index 1 2 3 4 5 6 7 **S** **A** 3 **M** 1 1 **P** 1 5 1 1 **D** 1 1 1 2 * ( 3 + 4 ) Hit on M(6) Update A(4) = 3 as A was recognized Update P(3)=5 as P was recognized |
|   | Derivation Rules Input shifted 2* Notes Input left Roll Back to $M\rightarrow P\ {\texttt {'*'}}\ M\ /\ {\underline {P}}$ as terminal $*\neq \dashv$ (3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** 3 **M** 1 1 **P** 1 5 1 1 **D** 1 1 1 2 * ( 3 + 4 ) No update because no terminal was recognized |
|   | Derivation Rules Input shifted $M\rightarrow P$ 2*(3+4) Notes Input left we don't expand it as we have a hit in the memoization table P(3) ≠ 0, so shift the input by P(3). ⊣ | Index 1 2 3 4 5 6 7 **S** **A** 3 **M** 7 1 1 **P** 1 5 1 1 **D** 1 1 1 2 * ( 3 + 4 ) Hit on P(3) Update M(1)=7 as M was recognized |
|   | Derivation Rules Input shifted Notes Input left Roll Back to $A\rightarrow M\ {\texttt {'+'}}\ A\ /\ {\underline {M}}$ as terminal $+\neq \dashv$ 2*(3+4)⊣ | Index 1 2 3 4 5 6 7 **S** **A** 3 **M** 7 1 1 **P** 1 5 1 1 **D** 1 1 1 2 * ( 3 + 4 ) No update because no terminal was recognized |
|   | Derivation Rules Input shifted $A\rightarrow M$ 2*(3+4)⊣ Notes Input left We don't expand it as we have a hit in the memoization table M(1) ≠ 0, so shift the input by M(1). S was totally reduced, so the input string is recognized. | Index 1 2 3 4 5 6 7 **S** 7 **A** 7 3 **M** 7 1 1 **P** 1 5 1 1 **D** 1 1 1 2 * ( 3 + 4 ) Hit on M(1) Update A(1)=7 as A was recognized Update S(1)=7 as S was recognized |

## Implementation

| Name | Parsing algorithm | Output languages | Grammar, code | Development platform | License |
|---|---|---|---|---|---|
| AustenX | Packrat (modified) | Java | Separate | All | Free, BSD |
| Aurochs | Packrat | C, OCaml, Java | Mixed | All | Free, GNU GPL |
| Canopy | Packrat | Java, JavaScript, Python, Ruby | Separate | All | Free, GNU GPL |
| CL-peg | Packrat | Common Lisp | Mixed | All | Free, MIT |
| Drat! | Packrat | D | Mixed | All | Free, GNU GPL |
| Frisby | Packrat | Haskell | Mixed | All | Free, BSD |
| grammar::peg | Packrat | Tcl | Mixed | All | Free, BSD |
| IronMeta | Packrat | C# | Mixed | Windows | Free, BSD |
| PEGParser | Packrat (supporting left-recursion and grammar ambiguity) | C++ | Identical | All | Free, BSD |
| Narwhal | Packrat | C | Mixed | POSIX, Windows | Free, BSD |
| neotoma | Packrat | Erlang | Separate | All | Free, MIT |
| OMeta | Packrat (modified, partial memoization) | JavaScript, Squeak, Python | Mixed | All | Free, MIT |
| PackCC | Packrat (modified, left-recursion support) | C | Mixed | All | Free, MIT |
| Packrat | Packrat | Scheme | Mixed | All | Free, MIT |
| Pappy | Packrat | Haskell | Mixed | All | Free, BSD |
| Parsnip | Packrat | C++ | Mixed | Windows | Free, GNU GPL |
| PEG.js | Packrat (partial memoization) | JavaScript | Mixed | All | Free, MIT |
| Peggy | Packrat (partial memoization) | JavaScript | Mixed | All | Free, MIT |
| Pegasus | Recursive descent, Packrat (selectively) | C# | Mixed | Windows | Free, MIT |
| PetitParser | Packrat | Smalltalk, Java, Dart | Mixed | All | Free, MIT |
| PyPy rlib | Packrat | Python | Mixed | All | Free, MIT |
| Rats! | Packrat | Java | Mixed | Java virtual machine | Free, GNU LGPL |
| go-packrat | Packrat | Go | Identical | All | Free, GPLv3 |
