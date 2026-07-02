---
title: "LL parser"
source: https://en.wikipedia.org/wiki/LL_parser
domain: antlr-parser
license: CC-BY-SA-4.0
tags: antlr parser generator, ll star parsing, grammar parser generator, recursive descent parsing
fetched: 2026-07-02
---

# LL parser

In computer science, an **LL parser** is a top-down parser for a restricted context-free language. It parses the input from **L**eft to right, performing **L**eftmost derivation of the sentence.

An LL parser is called an LL(*k*) parser if it uses *k* tokens of lookahead when parsing a sentence. A grammar is called an LL(*k*) grammar if an LL(*k*) parser can be constructed from it. A formal language is called an LL(*k*) language if it has an LL(*k*) grammar. The set of LL(*k*) languages is properly contained in that of LL(*k*+1) languages, for each *k* ≥ 0. A corollary of this is that not all context-free languages can be recognized by an LL(*k*) parser.

An LL parser is called LL-regular (LLR) if it parses an LL-regular language. The class of LLR grammars contains every LL(*k*) grammar for every *k*. For every LLR grammar there exists an LLR parser that parses the grammar in linear time.

Two nomenclative outlier parser types are LL(*) and LL(finite). A parser is called LL(*)/LL(finite) if it uses the LL(*)/LL(finite) parsing strategy. LL(*) and LL(finite) parsers are functionally closer to PEG parsers. An LL(finite) parser can parse an arbitrary LL(*k*) grammar optimally in the amount of lookahead and lookahead comparisons. The class of grammars parsable by the LL(*) strategy encompasses some context-sensitive languages due to the use of syntactic and semantic predicates and has not been identified. It has been suggested that LL(*) parsers are better thought of as TDPL parsers. Against the popular misconception, LL(*) parsers are not LLR in general, and are guaranteed by construction to perform worse on average (super-linear against linear time) and far worse in the worst-case (exponential against linear time).

LL grammars, particularly LL(1) grammars, are of great practical interest, as parsers for these grammars are easy to construct, and many computer languages are designed to be LL(1) for this reason. LL parsers may be table-based, i.e. similar to LR parsers, but LL grammars can also be parsed by recursive descent parsers. According to Waite and Goos (1984), LL(*k*) grammars were introduced by Stearns and Lewis (1969).

## Overview

For a given context-free grammar, the parser attempts to find the leftmost derivation. Given an example grammar *G*:

1. $S\to E$
2. $E\to (E+E)$
3. $E\to i$

the leftmost derivation for $w=((i+i)+i)$ is:

$S\ {\overset {(1)}{\Rightarrow }}\ E\ {\overset {(2)}{\Rightarrow }}\ (E+E)\ {\overset {(2)}{\Rightarrow }}\ ((E+E)+E)\ {\overset {(3)}{\Rightarrow }}\ ((i+E)+E)\ {\overset {(3)}{\Rightarrow }}\ ((i+i)+E)\ {\overset {(3)}{\Rightarrow }}\ ((i+i)+i)$

Generally, there are multiple possibilities when selecting a rule to expand the leftmost non-terminal. In step 2 of the previous example, the parser must choose whether to apply rule 2 or rule 3:

$S\ {\overset {(1)}{\Rightarrow }}\ E\ {\overset {(?)}{\Rightarrow }}\ ?$

To be efficient, the parser must be able to make this choice deterministically when possible, without backtracking. For some grammars, it can do this by peeking on the unread input (without reading). In our example, if the parser knows that the next unread symbol is **(**, the only correct rule that can be used is 2.

Generally, an LL(*k*) parser can look ahead at *k* symbols. However, given a grammar, the problem of determining if there exists a LL(*k*) parser for some *k* that recognizes it is undecidable. For each *k*, there is a language that cannot be recognized by an LL(*k*) parser, but can be by an LL(*k* + 1) parser.

We can use the above analysis to give the following formal definition:

Let *G* be a context-free grammar and *k* ≥ 1. We say that *G* is LL(*k*), if for any two leftmost derivations:

1. $S\ \Rightarrow \ \cdots \ \Rightarrow \ wA\alpha \ \Rightarrow \ \cdots \ \Rightarrow \ w\beta \alpha \ \Rightarrow \ \cdots \ \Rightarrow \ wu$
2. $S\ \Rightarrow \ \cdots \ \Rightarrow \ wA\alpha \ \Rightarrow \ \cdots \ \Rightarrow \ w\gamma \alpha \ \Rightarrow \ \cdots \ \Rightarrow \ wv$

the following condition holds: the prefix of the string u of length k equals the prefix of the string v of length *k* implies $\beta =\gamma$ .

In this definition, S is the start symbol and A any non-terminal. The already derived input w , and yet unread u and v are strings of terminals. The Greek letters $\alpha$ , $\beta$ and $\gamma$ represent any string of both terminals and non-terminals (possibly empty). The prefix length corresponds to the lookahead buffer size, and the definition says that this buffer is enough to distinguish between any two derivations of different words.

## Parser

The LL(*k*) parser is a deterministic pushdown automaton with the ability to peek on the next *k* input symbols without reading. This peek capability can be emulated by storing the lookahead buffer contents in the finite state space, since both buffer and input alphabet are finite in size. As a result, this does not make the automaton more powerful, but is a convenient abstraction.

The stack alphabet is $\Gamma =N\cup \Sigma$ , where:

- N is the set of non-terminals;
- $\Sigma$ the set of terminal (input) symbols with a special end-of-input (EOI) symbol **$**.

The parser stack initially contains the starting symbol above the EOI: [ S **$** ]. During operation, the parser repeatedly replaces the symbol X on top of the stack:

- with some $\alpha$ , if $X\in N$ and there is a rule $X\to \alpha$ ;
- with $\epsilon$ (in some notations $\lambda$ ), i.e. X is popped off the stack, if $X\in \Sigma$ . In this case, an input symbol x is read and if $x\neq X$ , the parser rejects the input.

If the last symbol to be removed from the stack is the EOI, the parsing is successful; the automaton accepts via an empty stack.

The states and the transition function are not explicitly given; they are specified (generated) using a more convenient *parse table* instead. The table provides the following mapping:

- row: top-of-stack symbol X
- column: |*w*| ≤ *k* lookahead buffer contents
- cell: rule number for $X\to \alpha$ or $\epsilon$

If the parser cannot perform a valid transition, the input is rejected (empty cells). To make the table more compact, only the non-terminal rows are commonly displayed, since the action is the same for terminals.

## Concrete example

### Set up

To explain an LL(1) parser's workings we will consider the following small LL(1) grammar:

1. S → F
2. S → **(** S **+** F **)**
3. F → **a**

and parse the following input:

(

a

+

a

)

An LL(1) parsing table for a grammar has a row for each of the non-terminals and a column for each terminal (including the special terminal, represented here as **$**, that is used to indicate the end of the input stream).

Each cell of the table may point to at most one rule of the grammar (identified by its number). For example, in the parsing table for the above grammar, the cell for the non-terminal 'S' and terminal '**(**' points to the rule number 2:

|   | ( | ) | a | + | $ |
|---|---|---|---|---|---|
| S | 2 | — | 1 | — | — |
| F | — | — | 3 | — | — |

The algorithm to construct a parsing table is described in a later section, but first let's see how the parser uses the parsing table to process its input.

### Parsing procedure

In each step, the parser reads the next-available symbol from the input stream, and the top-most symbol from the stack. If the input symbol and the stack-top symbol match, the parser discards them both by moving to the next input symbol and popping the top-most symbol off the stack. This is repeated until the input symbol and top-most symbol on the stack do not match.

Thus, in its first step, the parser reads the input symbol '**(**' and the stack-top symbol 'S'. The parsing table instruction comes from the column headed by the input symbol '**(**' and the row headed by the stack-top symbol 'S'; this cell contains '2', which instructs the parser to apply rule (2). The parser has to rewrite 'S' to '**(** S **+** F **)**' on the stack by removing 'S' from stack and pushing ')', 'F', '**+**', 'S', '**(**' onto the stack, and this writes the rule number 2 to the output. The stack then becomes:

```
[ (, S, +, F, ), $ ]
```

In the second step, the parser removes the '**(**' from its input stream and from its stack, since they now match. The stack now becomes:

```
[ S, +, F, ), $ ]
```

Now the parser has an '**a'** on its input stream and an 'S' as its stack top. The parsing table instructs it to apply rule (1) from the grammar and write the rule number 1 to the output stream. The stack becomes:

```
[ F, +, F, ), $ ]
```

The parser now has an '**a'** on its input stream and an 'F' as its stack top. The parsing table instructs it to apply rule (3) from the grammar and write the rule number 3 to the output stream. The stack becomes:

```
[ a, +, F, ), $ ]
```

The parser now has an '**a'** on the input stream and an '**a**' at its stack top. Because they are the same, it removes it from the input stream and pops it from the top of the stack. The parser then has an '**+**' on the input stream and '**+**' is at the top of the stack meaning, like with 'a', it is popped from the stack and removed from the input stream. This results in:

```
[ F, ), $ ]
```

In the next three steps the parser will replace 'F' on the stack by '**a**', write the rule number 3 to the output stream and remove the '**a**' and '**)**' from both the stack and the input stream. The parser thus ends with '**$**' on both its stack and its input stream.

In this case the parser will report that it has accepted the input string and write the following list of rule numbers to the output stream:

[ 2, 1, 3, 3 ]

This is indeed a list of rules for a leftmost derivation of the input string, which is:

S →

(

S

+

F

)

→

(

F

+

F

)

→

(

a

+

F

)

→

(

a

+

a

)

### Parser implementation in C++

Below follows a C++ implementation of a table-based LL parser for the example language:

```mw
# include <iostream>
# include <map>
# include <stack>

enum Symbols {
	// the symbols:
	// Terminal symbols:
	TS_L_PARENS,	// (
	TS_R_PARENS,	// )
	TS_A,		// a
	TS_PLUS,	// +
	TS_EOS,		// $, in this case corresponds to '\0'
	TS_INVALID,	// invalid token

	// Non-terminal symbols:
	NTS_S,		// S
	NTS_F		// F
};

/*
Converts a valid token to the corresponding terminal symbol
*/
Symbols lexer(char c)
{
	switch (c)
	{
		case '(':  return TS_L_PARENS;
		case ')':  return TS_R_PARENS;
		case 'a':  return TS_A;
		case '+':  return TS_PLUS;
		case '\0': return TS_EOS; // end of stack: the $ terminal symbol
		default:   return TS_INVALID;
	}
}

int main(int argc, char **argv)
{
	using namespace std;

	if (argc < 2)
	{
		cout << "usage:\n\tll '(a+a)'" << endl;
		return 0;
	}

	// LL parser table, maps < non-terminal, terminal> pair to action
	map< Symbols, map<Symbols, int> > table;
	stack<Symbols>	ss;	// symbol stack
	char *p;	// input buffer

	// initialize the symbols stack
	ss.push(TS_EOS);	// terminal, $
	ss.push(NTS_S);		// non-terminal, S

	// initialize the symbol stream cursor
	p = &argv[1][0];

	// set up the parsing table
	table[NTS_S][TS_L_PARENS] = 2;
	table[NTS_S][TS_A] = 1;
	table[NTS_F][TS_A] = 3;

	while (ss.size() > 0)
	{
		if (lexer(*p) == ss.top())
		{
			cout << "Matched symbols: " << lexer(*p) << endl;
			p++;
			ss.pop();
		}
		else
		{
			cout << "Rule " << table[ss.top()][lexer(*p)] << endl;
			switch (table[ss.top()][lexer(*p)])
			{
				case 1:	// 1. S → F
					ss.pop();
					ss.push(NTS_F);	// F
					break;

				case 2:	// 2. S → ( S + F )
					ss.pop();
					ss.push(TS_R_PARENS);	// )
					ss.push(NTS_F);		// F
					ss.push(TS_PLUS);	// +
					ss.push(NTS_S);		// S
					ss.push(TS_L_PARENS);	// (
					break;

				case 3:	// 3. F → a
					ss.pop();
					ss.push(TS_A);	// a
					break;

				default:
					cout << "parsing table defaulted" << endl;
					return 0;
			}
		}
	}

	cout << "finished parsing" << endl;

	return 0;
}
```

### Parser implementation in Python

```mw
from enum import Enum
from collections.abc import Generator

class Term(Enum):
    pass

class Rule(Enum):
    pass

# All constants are indexed from 0
class Terminal(Term):
    LPAR = 0
    RPAR = 1
    A = 2
    PLUS = 3
    END = 4
    INVALID = 5

    def __str__(self):
        return f"T_{self.name}"

class NonTerminal(Rule):
    S = 0
    F = 1

    def __str__(self):
        return f"N_{self.name}"

# Parse table
table = [[1, -1, 0, -1, -1, -1], [-1, -1, 2, -1, -1, -1]]

RULES = [
    [NonTerminal.F],
    [
        Terminal.LPAR,
        NonTerminal.S,
        Terminal.PLUS,
        NonTerminal.F,
        Terminal.RPAR,
    ],
    [Terminal.A],
]

stack = [Terminal.END, NonTerminal.S]

def lexical_analysis(input_string: str) -> Generator[Terminal]:
    print("Lexical analysis")
    for c in input_string:
        match c:
            case "a":
                yield Terminal.A
            case "+":
                yield Terminal.PLUS
            case "(":
                yield Terminal.LPAR
            case ")":
                yield Terminal.RPAR
            case _:
                yield Terminal.INVALID
    yield Terminal.END

def syntactic_analysis(tokens: list[Terminal]) -> None:
    print("tokens:", end=" ")
    print(*tokens, sep=", ")
    print("Syntactic analysis")
    position = 0
    while stack:
        svalue = stack.pop()
        token = tokens[position]
        if isinstance(svalue, Term):
            if svalue == token:
                position += 1
                print("pop", svalue)
                if token == Terminal.END:
                    print("input accepted")
            else:
                raise ValueError("bad term on input:", str(token))
        elif isinstance(svalue, Rule):
            print(f"{svalue = !s}, {token = !s}")
            rule = table[svalue.value][token.value]
            print(f"{rule = }")
            for r in reversed(RULES[rule]):
                stack.append(r)
        print("stacks:", end=" ")
        print(*stack, sep=", ")

if __name__ == "__main__":
    inputstring = "(a+a)"
    syntactic_analysis(list(lexical_analysis(inputstring)))
```

Outputs:

```mw
Lexical analysis
tokens: T_LPAR, T_A, T_PLUS, T_A, T_RPAR, T_END
Syntactic analysis
svalue = N_S, token = T_LPAR
rule = 1
stacks: T_END, T_RPAR, N_F, T_PLUS, N_S, T_LPAR
pop T_LPAR
stacks: T_END, T_RPAR, N_F, T_PLUS, N_S
svalue = N_S, token = T_A
rule = 0
stacks: T_END, T_RPAR, N_F, T_PLUS, N_F
svalue = N_F, token = T_A
rule = 2
stacks: T_END, T_RPAR, N_F, T_PLUS, T_A
pop T_A
stacks: T_END, T_RPAR, N_F, T_PLUS
pop T_PLUS
stacks: T_END, T_RPAR, N_F
svalue = N_F, token = T_A
rule = 2
stacks: T_END, T_RPAR, T_A
pop T_A
stacks: T_END, T_RPAR
pop T_RPAR
stacks: T_END
pop T_END
input accepted
stacks:
```

## Remarks

As can be seen from the example, the parser performs three types of steps depending on whether the top of the stack is a nonterminal, a terminal or the special symbol **$**:

- If the top is a nonterminal then the parser looks up in the parsing table, on the basis of this nonterminal and the symbol on the input stream, which rule of the grammar it should use to replace nonterminal on the stack. The number of the rule is written to the output stream. If the parsing table indicates that there is no such rule then the parser reports an error and stops.
- If the top is a terminal then the parser compares it to the symbol on the input stream and if they are equal they are both removed. If they are not equal the parser reports an error and stops.
- If the top is **$** and on the input stream there is also a **$** then the parser reports that it has successfully parsed the input, otherwise it reports an error. In both cases the parser will stop.

These steps are repeated until the parser stops, and then it will have either completely parsed the input and written a leftmost derivation to the output stream or it will have reported an error.

## Constructing an LL(1) parsing table

In order to fill the parsing table, we have to establish what grammar rule the parser should choose if it sees a nonterminal *A* on the top of its stack and a symbol *a* on its input stream. It is easy to see that such a rule should be of the form *A* → *w* and that the language corresponding to *w* should have at least one string starting with *a*. For this purpose we define the *First-set* of *w*, written here as **Fi**(*w*), as the set of terminals that can be found at the start of some string in *w*, plus ε if the empty string also belongs to *w*. Given a grammar with the rules *A*1 → *w*1, ..., *A**n* → *w**n*, we can compute the **Fi**(*w**i*) and **Fi**(*A**i*) for every rule as follows:

1. initialize every **Fi**(*A**i*) with the empty set
2. add Fi(*w**i*) to **Fi**(*A**i*) for every rule *A**i* → *w**i*, where Fi is defined as follows:
  - Fi(*aw′*) = { *a* } for every terminal *a*
  - Fi(*Aw′*) = **Fi**(*A*) for every nonterminal *A* with ε not in **Fi**(*A*)
  - Fi(*Aw′*) = (**Fi**(*A*) ∖ { ε }) ∪ Fi(*w'*) for every nonterminal *A* with ε in **Fi**(*A*)
  - Fi(ε) = { ε }
3. add Fi(*w**i*) to **Fi**(*A**i*) for every rule *A**i* → *w**i*
4. do steps 2 and 3 until all **Fi** sets stay the same.

The result is the least fixed point solution to the following system:

- **Fi**(*A*) ⊇ **Fi**(*w*) for each rule A → *w*
- **Fi**(*a*) ⊇ { *a* }, for each terminal *a*
- **Fi**(*w*0 *w*1) ⊇ **Fi**(*w*0)·**Fi**(*w*1), for all words *w*0 and *w*1
- **Fi**(*ε*) ⊇ {*ε*}

where, for sets of words *U* and *V*, the truncated product is defined by $U\cdot V=\{(uv):1\mid u\in U,v\in V\}$ , and w:1 denotes the initial length-1 prefix of words w of length 2 or more, or *w*, itself, if w has length 0 or 1.

Unfortunately, the First-sets are not sufficient to compute the parsing table. This is because a right-hand side *w* of a rule might ultimately be rewritten to the empty string. So the parser should also use the rule *A* → *w* if *ε* is in **Fi**(*w*) and it sees on the input stream a symbol that could follow *A*. Therefore, we also need the *Follow-set* of *A*, written as **Fo**(*A*) here, which is defined as the set of terminals *a* such that there is a string of symbols *αAaβ* that can be derived from the start symbol. We use **$** as a special terminal indicating end of input stream, and *S* as start symbol.

Computing the Follow-sets for the nonterminals in a grammar can be done as follows:

1. initialize **Fo**(*S*) with { **$** } and every other **Fo**(*A**i*) with the empty set
2. if there is a rule of the form *A**j* → *wAiw′*, then
  - if the terminal *a* is in **Fi**(*w′*), then add *a* to **Fo**(*A**i*)
  - if ε is in **Fi**(*w′*), then add **Fo**(*A**j*) to **Fo**(*A**i*)
  - if *w'* has length 0, then add **Fo**(*A**j*) to **Fo**(*A**i*)
3. repeat step 2 until all **Fo** sets stay the same.

This provides the least fixed point solution to the following system:

- **Fo**(*S*) ⊇ {**$**}
- **Fo**(*A*) ⊇ **Fi**(*w*)·**Fo**(*B*) for each rule of the form ⁠ $B\to \dots Aw$ ⁠

Now we can define exactly which rules will appear where in the parsing table. If *T*[*A*, *a*] denotes the entry in the table for nonterminal *A* and terminal *a*, then

T

[

A

,

a

] contains the rule

A

→

w

if and only if

a

is in

Fi

(

w

) or

ε is in

Fi

(

w

) and

a

is in

Fo

(

A

).

Equivalently: *T*[*A*, *a*] contains the rule *A* → *w* for each *a* ∈ **Fi**(*w*)·**Fo**(*A*).

If the table contains at most one rule in every one of its cells, then the parser will always know which rule it has to use and can therefore parse strings without backtracking. It is in precisely this case that the grammar is called an *LL(1) grammar*.

## Constructing an LL(*k*) parsing table

The construction for LL(1) parsers can be adapted to LL(*k*) for *k* > 1 with the following modifications:

- the truncated product is defined $U\cdot V=\{(uv):k\mid u\in U,v\in V\}$ , where *w*:*k* denotes the initial length-*k* prefix of words of length > *k*, or *w*, itself, if *w* has length *k* or less,
- **Fo**(*S*) = {**$**k}
- Apply **Fi**(*αβ*) = **Fi**(*α*) ⋅ **Fi**(*β*) also in step 2 of the **Fi** construction given for LL(1).
- In step 2 of the **Fo** construction, for *Aj* → *wAiw*′ simply add **Fi**(*w′*)·**Fo**(*Aj*) to **Fo**(*Ai*).

where an input is suffixed by *k* end-markers **$**, to fully account for the *k* lookahead context. This approach eliminates special cases for ε, and can be applied equally well in the LL(1) case.

Until the mid-1990s, it was widely believed that LL(*k*) parsing (for *k* > 1) was impractical, since the parser table would have exponential size in *k* in the worst case. This perception changed gradually after the release of the Purdue Compiler Construction Tool Set around 1992, when it was demonstrated that many programming languages can be parsed efficiently by an LL(*k*) parser without triggering the worst-case behavior of the parser. Moreover, in certain cases LL parsing is feasible even with unlimited lookahead. By contrast, traditional parser generators like yacc use LALR(1) parser tables to construct a restricted LR parser with a fixed one-token lookahead.

## Conflicts

As described in the introduction, LL(1) parsers recognize languages that have LL(1) grammars, which are a special case of context-free grammars; LL(1) parsers cannot recognize all context-free languages. The LL(1) languages are a proper subset of the LR(1) languages, which in turn are a proper subset of all context-free languages. In order for a context-free grammar to be an LL(1) grammar, certain conflicts must not arise.

### Terminology

Let *A* be a non-terminal. FIRST(*A*) is defined as the set of terminals that can appear in the first position of any string derived from *A*. FOLLOW(*A*) is the union over:

1. FIRST(*B*) where *B* is any non-terminal that immediately follows *A* in the right-hand side of a production rule.
2. FOLLOW(*B*) where *B* is any head of a rule of the form *B* → *wA*.

### LL(1) conflicts

There are two main types of LL(1) conflicts:

#### FIRST/FIRST conflict

The FIRST sets of two different grammar rules for the same non-terminal intersect. An example of an LL(1) FIRST/FIRST conflict:

```
S -> E | E 'a'
E -> 'b' | ε
```

FIRST(*E*) = {*b*, ε} and FIRST(*E* *a*) = {*b*, *a*}, so when the table is drawn, there is conflict under terminal *b* of production rule *S*.

##### Special case: left recursion

Left recursion will cause a FIRST/FIRST conflict with all alternatives.

```
E -> E '+' term | alt1 | alt2
```

#### FIRST/FOLLOW conflict

The FIRST and FOLLOW set of a grammar rule overlap. With an empty string (ε) in the FIRST set, it is unknown which alternative to select. An example of an LL(1) conflict:

```
S -> A 'a' 'b'
A -> 'a' | ε
```

The FIRST set of *A* is {*a*, ε}, and the FOLLOW set is {*a*}.

### Solutions to LL(1) conflicts

#### Left factoring

A common left-factor is "factored out".

```
A -> X | X Y Z
```

becomes

```
A -> X B
B -> Y Z | ε
```

Can be applied when two alternatives start with the same symbol like a FIRST/FIRST conflict.

Another example (more complex) using above FIRST/FIRST conflict example:

```
S -> E | E 'a'
E -> 'b' | ε
```

becomes (merging into a single non-terminal)

```
S -> 'b' | ε | 'b' 'a' | 'a'
```

then through left-factoring, becomes

```
S -> 'b' E | E
E -> 'a' | ε
```

#### Substitution

Substituting a rule into another rule to remove indirect or FIRST/FOLLOW conflicts. Note that this may cause a FIRST/FIRST conflict.

#### Left recursion removal

See

For a general method, see removing left recursion. A simple example for left recursion removal: The following production rule has left recursion on E

```
E -> E '+' T
E -> T
```

This rule is nothing but list of Ts separated by '+'. In a regular expression form T ('+' T)*. So the rule could be rewritten as

```
E -> T Z
Z -> '+' T Z
Z -> ε
```

Now there is no left recursion and no conflicts on either of the rules.

However, not all context-free grammars have an equivalent LL(k)-grammar, e.g.:

```
S -> A | B
A -> 'a' A 'b' | ε
B -> 'a' B 'b' 'b' | ε
```

It can be shown that there does not exist any LL(k)-grammar accepting the language generated by this grammar.
