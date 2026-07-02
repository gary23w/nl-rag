---
title: "LR parser (part 2/2)"
source: https://en.wikipedia.org/wiki/LR_parser
domain: compilers-and-parsing
license: CC-BY-SA-4.0
tags: compiler construction, parser generator, syntax analysis, lexer, lexical analysis, abstract syntax tree
fetched: 2026-07-02
part: 2/2
---

## Table construction

### Finding the reachable item sets and the transitions between them

The first step of constructing the tables consists of determining the transitions between the closed item sets. These transitions will be determined as if we are considering a finite automaton that can read terminals as well as nonterminals. The begin state of this automaton is always the closure of the first item of the added rule: S → • E eof:

Item set 0

S →

•

E eof

+

E →

•

E * B

+

E →

•

E + B

+

E →

•

B

+

B →

•

0

+

B →

•

1

The boldfaced "**+**" in front of an item indicates the items that were added for the closure (not to be confused with the mathematical '+' operator which is a terminal). The original items without a "**+**" are called the *kernel* of the item set.

Starting at the begin state (S0), all of the states that can be reached from this state are now determined. The possible transitions for an item set can be found by looking at the symbols (terminals and nonterminals) found following the dots; in the case of item set 0 those symbols are the terminals '0' and '1' and the nonterminals E and B. To find the item set that each symbol ${\textstyle x\in \{0,1,E,B\}}$ leads to, the following procedure is followed for each of the symbols:

1. Take the subset, *S*, of all items in the current item set where there is a dot in front of the symbol of interest, *x*.
2. For each item in *S*, move the dot to the right of *x*.
3. Close the resulting set of items.

For the terminal '0' (i.e. where x = '0') this results in:

Item set 1

B → 0

•

and for the terminal '1' (i.e. where x = '1') this results in:

Item set 2

B → 1

•

and for the nonterminal E (i.e. where x = E) this results in:

Item set 3

S → E

•

eof

E → E

•

* B

E → E

•

+ B

and for the nonterminal B (i.e. where x = B) this results in:

Item set 4

E → B

•

The closure does not add new items in all cases - in the new sets above, for example, there are no nonterminals following the dot.

Above procedure is continued until no more new item sets are found. For the item sets 1, 2, and 4 there will be no transitions since the dot is not in front of any symbol. For item set 3 though, we have dots in front of terminals '*' and '+'. For symbol ${\textstyle x={\texttt {*}}}$ the transition goes to:

Item set 5

E → E *

•

B

+

B →

•

0

+

B →

•

1

and for ${\textstyle x={\texttt {+}}}$ the transition goes to:

Item set 6

E → E +

•

B

+

B →

•

0

+

B →

•

1

Now, the third iteration begins.

For item set 5, the terminals '0' and '1' and the nonterminal B must be considered, but the resulting closed item sets for the terminals are equal to already found item sets 1 and 2, respectively. For the nonterminal B, the transition goes to:

Item set 7

E → E * B

•

For item set 6, the terminal '0' and '1' and the nonterminal B must be considered, but as before, the resulting item sets for the terminals are equal to the already found item sets 1 and 2. For the nonterminal B the transition goes to:

Item set 8

E → E + B

•

These final item sets 7 and 8 have no symbols beyond their dots so no more new item sets are added, so the item generating procedure is complete. The finite automaton, with item sets as its states is shown below.

The transition table for the automaton now looks as follows:

| Item Set | * | + | 0 | 1 | E | B |
|---|---|---|---|---|---|---|
| 0 |   |   | 1 | 2 | 3 | 4 |
| 1 |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |
| 3 | 5 | 6 |   |   |   |   |
| 4 |   |   |   |   |   |   |
| 5 |   |   | 1 | 2 |   | 7 |
| 6 |   |   | 1 | 2 |   | 8 |
| 7 |   |   |   |   |   |   |
| 8 |   |   |   |   |   |   |

### Constructing the action and goto tables

From this table and the found item sets, the action and goto table are constructed as follows:

1. The columns for nonterminals are copied to the goto table.
2. The columns for the terminals are copied to the action table as shift actions.
3. An extra column for '$' (end of input) is added to the action table. An *acc* action is added to the '$' column for each item set that contains an item of the form S → w • eof.
4. If an item set *i* contains an item of the form *A* → *w* • and *A* → *w* is rule *m* with *m* > 0 then the row for state *i* in the action table is completely filled with the reduce action r*m*.

The reader may verify that these steps produce the action and goto table presented earlier.

#### A note about LR(0) versus SLR and LALR parsing

Only step 4 of the above procedure produces reduce actions, and so all reduce actions must occupy an entire table row, causing the reduction to occur regardless of the next symbol in the input stream. This is why these are LR(0) parse tables: they don't do any lookahead (that is, they look ahead zero symbols) before deciding which reduction to perform. A grammar that needs lookahead to disambiguate reductions would require a parse table row containing different reduce actions in different columns, and the above procedure is not capable of creating such rows.

Refinements to the **LR**(0) table construction procedure (such as SLR and LALR) are capable of constructing reduce actions that do not occupy entire rows. Therefore, they are capable of parsing more grammars than LR(0) parsers.

### Conflicts in the constructed tables

The automaton is constructed in such a way that it is guaranteed to be deterministic. However, when reduce actions are added to the action table it can happen that the same cell is filled with a reduce action and a shift action (a *shift-reduce conflict*) or with two different reduce actions (a *reduce-reduce conflict*). However, it can be shown that when this happens the grammar is not an LR(0) grammar. A classic real-world example of a shift-reduce conflict is the dangling else problem.

A small example of a non-LR(0) grammar with a shift-reduce conflict is:

(1) E → 1 E

(2) E → 1

One of the item sets found is:

Item set 1

E → 1

•

E

E → 1

•

+

E →

•

1 E

+

E →

•

1

There is a shift-reduce conflict in this item set: when constructing the action table according to the rules above, the cell for [item set 1, terminal '1'] contains **s1** (shift to state 1) **and r2** (reduce with grammar rule 2).

A small example of a non-LR(0) grammar with a reduce-reduce conflict is:

(1) E → A 1

(2) E → B 2

(3) A → 1

(4) B → 1

In this case the following item set is obtained:

Item set 1

A → 1

•

B → 1

•

There is a reduce-reduce conflict in this item set because in the cells in the action table for this item set there will be both a reduce action for rule 3 and one for rule 4.

Both examples above can be solved by letting the parser use the follow set (see LL parser) of a nonterminal *A* to decide if it is going to use one of *A*s rules for a reduction; it will only use the rule *A* → *w* for a reduction if the next symbol on the input stream is in the follow set of *A*. This solution results in so-called Simple LR parsers.
