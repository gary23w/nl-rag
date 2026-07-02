---
title: "Truth table"
source: https://en.wikipedia.org/wiki/Truth_table
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
---

# Truth table

A **truth table** is a mathematical table used in logic—specifically in connection with Boolean algebra, Boolean functions, and propositional calculus—which sets out the functional values of logical expressions on each of their functional arguments, that is, for each combination of values taken by their logical variables. In particular, truth tables can be used to show whether a propositional expression is true for all legitimate input values, that is, logically valid.

A truth table has one column for each input variable (for example, A and B), and one final column showing the result of the logical operation that the table represents (for example, A XOR B). Each row of the truth table contains one possible configuration of the input variables (for instance, A=true, B=false), and the result of the operation for those values.

A proposition's truth table is a graphical representation of its truth function. The truth function can be more useful for mathematical purposes, although the same information is encoded in both.

Ludwig Wittgenstein is generally credited with inventing and popularizing the truth table in his *Tractatus Logico-Philosophicus*, which was completed in 1918 and published in 1921. Such a system was also independently proposed in 1921 by Emil Leon Post.

## History

Irving Anellis's research shows that C.S. Peirce appears to be the earliest logician (in 1883) to devise a truth table matrix.

From the summary of Anellis's paper:

> In 1997, John Shosky discovered, on the verso of a page of the typed transcript of Bertrand Russell's 1912 lecture on "The Philosophy of Logical Atomism" truth table matrices. The matrix for negation is Russell's, alongside of which is the matrix for material implication in the hand of Ludwig Wittgenstein. It is shown that an unpublished manuscript identified as composed by Peirce in 1893 includes a truth table matrix that is equivalent to the matrix for material implication discovered by John Shosky. An unpublished manuscript by Peirce identified as having been composed in 1883–84 in connection with the composition of Peirce's "On the Algebra of Logic: A Contribution to the Philosophy of Notation" that appeared in the *American Journal of Mathematics* in 1885 includes an example of an indirect truth table for the conditional.

## Applications

Truth tables can be used to prove many other logical equivalences. For example, consider the following truth table:

| p | q | $\neg p$ | $\neg p\vee q$ | $p\rightarrow q$ |
|---|---|---|---|---|
| T | T | F | T | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

This demonstrates the fact that $p\rightarrow q$ is logically equivalent to $\neg p\vee q$ .

### Truth table for logic gates

Here is a truth table that gives definitions of each of the 6 possible 2-input logic gate functions of two Boolean variables P and Q:

| P | Q | $P\land Q$ | $P\vee Q$ | $P\uparrow Q$ | $P\downarrow Q$ | $P\nleftrightarrow Q$ | $P\leftrightarrow Q$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | F | F | F | T |
| T | F | F | T | T | F | T | F |
| F | T | F | T | T | F | T | F |
| F | F | F | F | T | T | F | T |
| Name (function) | AND (conjunction) | OR (disjunction) | NAND (non-conjunction) | NOR (non-disjunction) | XOR (non-equivalence) | XNOR (equivalence) |   |
| *where*  T  *means* **true** *and*  F  *means* **false** |   |   |   |   |   |   |   |

### Condensed truth tables for binary operators

For binary operators, a condensed form of truth table is also used, where the row headings and the column headings specify the operands and the table cells specify the result. For example, Boolean logic uses this condensed truth table notation:

|   | ∧ T F T T F F F F |   | ∨ T F T T T F T F |
|---|---|---|---|

This notation is useful especially if the operations are commutative, although one can additionally specify that the rows are the first operand and the columns are the second operand. This condensed notation is particularly useful in discussing multi-valued extensions of logic, as it significantly cuts down on combinatoric explosion of the number of rows otherwise needed. It also provides for quickly recognizable characteristic "shape" of the distribution of the values in the table which can assist the reader in grasping the rules more quickly.

### Truth tables in digital logic

Truth tables are also used to specify the function of hardware look-up tables (LUTs) in digital logic circuitry. For an n-input LUT, the truth table will have ⁠ $2^{n}$ ⁠ values (or rows in the above tabular format), completely specifying a Boolean function for the LUT. By representing each Boolean value as a bit in a binary number, truth table values can be efficiently encoded as integer values in electronic design automation (EDA) software. For example, a 32-bit integer can encode the truth table for a LUT with up to 5 inputs.

When using an integer representation of a truth table, the output value of the LUT can be obtained by calculating a bit index *k* based on the input values of the LUT, in which case the LUT's output value is the *k*th bit of the integer. For example, to evaluate the output value of a LUT given an array of *n* Boolean input values, the bit index of the truth table's output value can be computed as follows: if the *i*th input is true, let $V_{i}=1$ , else let $V_{i}=0$ . Then the *k*th bit of the binary representation of the truth table is the LUT's output value, where $k=V_{0}\times 2^{0}+V_{1}\times 2^{1}+V_{2}\times 2^{2}+\dots +V_{n-1}\times 2^{n-1}.$

Truth tables are a simple and straightforward way to encode Boolean functions, however given the exponential growth in size as the number of inputs increase, they are not suitable for functions with a large number of inputs. Other representations which are more memory efficient are text equations and binary decision diagrams.

### Applications of truth tables in digital electronics

In digital electronics and computer science (fields of applied logic engineering and mathematics), truth tables can be used to reduce basic Boolean operations to simple correlations of inputs to outputs, without the use of logic gates or code. For example, a binary addition can be represented with the truth table:

| A | B | C | R |
|---|---|---|---|
| T | T | T | F |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

where A is the first operand, B is the second operand, C is the carry digit, and R is the result.

This truth table is read left to right:

- Value pair (A, B) equals value pair (C, R).
- Or for this example, A plus B equal result R, with the Carry C.

This table does not describe the logic operations necessary to implement this operation, rather it simply specifies the function of inputs to output values.

With respect to the result, this example may be arithmetically viewed as modulo 2 binary addition, and as logically equivalent to the exclusive-or (exclusive disjunction) binary logic operation.

In this case it can be used for only very simple inputs and outputs, such as 1s and 0s. However, if the number of types of values one can have on the inputs increases, the size of the truth table will increase.

For instance, in an addition operation, one needs two operands, A and B. Each can have one of two values, zero or one. The number of combinations of these two values is 2 × 2, or four. So the result is four possible outputs of C and R. If one were to use base 3, the size would increase to 3 × 3, or nine possible outputs.

The first "addition" example above is called a half-adder. A full-adder is when the carry from the previous operation is provided as input to the next adder. Thus, a truth table of eight rows would be needed to describe a full adder's logic:

```
A B C* | C R
0 0 0  | 0 0
0 1 0  | 0 1
1 0 0  | 0 1
1 1 0  | 1 0
0 0 1  | 0 1
0 1 1  | 1 0
1 0 1  | 1 0
1 1 1  | 1 1

Same as previous, but..
C* = Carry from previous adder
```

## Methods of writing truth tables

Regarding the *guide columns* to the left of a table, which represent propositional variables, different authors have different recommendations about how to fill them in, although this is of no logical significance.

### Alternating method

Lee Archie, a professor at Lander University, recommends this procedure, which is commonly followed in published truth-tables:

1. Write out the number of variables (corresponding to the number of statements) in alphabetical order.
2. The number of lines needed is 2*n* where n is the number of variables. (E. g., with three variables, 23 = 8).
3. Start in the right-hand column and alternate **T**'s and **F**'s until you run out of lines.
4. Then move left to the next column and alternate pairs of **T**'s and **F**'s until you run out of lines.
5. Then continue to the next left-hand column and double the numbers of **T**'s and **F**'s until completed.

This method results in truth-tables such as the following table for *P* → (*Q* ∨ *R* → (*R* → ¬*P*)), produced by Stephen Cole Kleene:

| P | Q | R | $P\rightarrow (Q\vee R\rightarrow (R\rightarrow \neg P))$ |
|---|---|---|---|
| T | T | T | F |
| T | T | F | T |
| T | F | T | F |
| T | F | F | T |
| F | T | T | T |
| F | T | F | T |
| F | F | T | T |
| F | F | F | T |

### Combinatorial method

Colin Howson, on the other hand, believes that "it is a good practical rule" to do the following:

> to start with all Ts, then all the ways (three) two Ts can be combined with one F, then all the ways (three) one T can be combined with two Fs, and then finish with all Fs. If a compound is built up from n distinct sentence letters, its truth table will have 2n rows, since there are two ways of assigning T or F to the first letter, and for each of these there will be two ways of assigning T or F to the second, and for each of these there will be two ways of assigning T or F to the third, and so on, giving 2.2.2. …, n times, which is equal to 2n.

This results in truth tables like this table "showing that (*A*→*C*)∧(*B*→*C*) and (*A*∨*B*)→*C* are truth-functionally equivalent", modeled after a table produced by Howson:

| A | B | C | $(A\rightarrow C)\land (B\rightarrow C)$ | $(A\vee B)\rightarrow C$ |
|---|---|---|---|---|
| T | T | T | T | T |
| T | T | F | F | F |
| T | F | T | T | T |
| F | T | T | T | T |
| F | F | T | T | T |
| F | T | F | F | F |
| T | F | F | F | F |
| F | F | F | T | T |

## Size of truth tables

If there are *n* input variables then there are 2*n* possible combinations of their truth values. A given function may produce true or false for each combination so the number of different functions of *n* variables is the double exponential 22*n*.

| *n* | 2*n* | 22*n* |   |
|---|---|---|---|
| 0 | 1 | 2 |   |
| 1 | 2 | 4 |   |
| 2 | 4 | 16 |   |
| 3 | 8 | 256 |   |
| 4 | 16 | 65,536 |   |
| 5 | 32 | 4,294,967,296 | ≈ 4.3×109 |
| 6 | 64 | 18,446,744,073,709,551,616 | ≈ 1.8×1019 |
| 7 | 128 | 340,282,366,920,938,463,463,374,607,431,768,211,456 | ≈ 3.4×1038 |
| 8 | 256 | 115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,936 | ≈ 1.2×1077 |

Truth tables for functions of three or more variables are rarely given.

## Function Tables

It can be useful to have the output of a truth table expressed as a function of some variable values, instead of just a literal truth or false value. These may be called "function tables" to differentiate them from the more general "truth tables". For example, one value, G, may be used with an XOR gate to conditionally invert another value, X. In other words, when G is false, the output is X, and when G is true, the output is ${\textstyle \neg X}$ . The function table for this would look like:

| G | $G\nleftrightarrow X$ |
|---|---|
| F | X |
| T | $\neg X$ |

Similarly, a 4-to-1 multiplexer with select inputs $S_{0}$ and $S_{1}$ , data inputs A, B, C and D, and output Z (as displayed in the image) would have this function table:

| $S_{1}$ | $S_{0}$ | Z |
|---|---|---|
| F | F | A |
| F | T | B |
| T | F | C |
| T | T | D |

## Sentential operator truth tables

### Overview table

Here is an extended truth table giving definitions of all sixteen possible truth functions of two Boolean variables ***p*** and ***q***:

p

q

$\bot$

$p\downarrow q$

$p\nleftarrow q$

$\neg p$

$p\nrightarrow q$

$\neg q$

$p\nleftrightarrow q$

$p\uparrow q$

$p\land q$

$p\leftrightarrow q$

q

$p\rightarrow q$

p

$p\leftarrow q$

$p\vee q$

$\top$

T

T

F

F

F

F

F

F

F

F

T

T

T

T

T

T

T

T

T

F

F

F

F

F

T

T

T

T

F

F

F

F

T

T

T

T

F

T

F

F

T

T

F

F

T

T

F

F

T

T

F

F

T

T

F

F

F

T

F

T

F

T

F

T

F

T

F

T

F

T

F

T

Com

Assoc

Adj

$\bot$

$p\downarrow q$

$p\nrightarrow q$

$\neg q$

$p\nleftarrow q$

$\neg p$

$p\nleftrightarrow q$

$p\uparrow q$

$p\land q$

$p\leftrightarrow q$

p

$p\leftarrow q$

q

$p\rightarrow q$

$p\vee q$

$\top$

Neg

$\top$

$p\vee q$

$p\leftarrow q$

p

$p\rightarrow q$

q

$p\leftrightarrow q$

$p\land q$

$p\uparrow q$

$p\nleftrightarrow q$

$\neg q$

$p\nrightarrow q$

$\neg p$

$p\nleftarrow q$

$p\downarrow q$

$\bot$

Dual

$\top$

$p\uparrow q$

$p\rightarrow q$

$\neg p$

$p\leftarrow q$

$\neg q$

$p\leftrightarrow q$

$p\downarrow q$

$p\vee q$

$p\nleftrightarrow q$

q

$p\nleftarrow q$

p

$p\nrightarrow q$

$p\land q$

$\bot$

L id

F

F

T

T

T, F

T

F

R id

F

F

T

T

T, F

T

F

where

T = true.

F = false.

The

Com

row indicates whether an operator,

op

, is

commutative

–

P

op

Q

=

Q

op

P

.

The

Assoc

row indicates whether an operator,

op

, is

associative

–

(

P

op

Q

) op

R

=

P

op (

Q

op

R

)

.

The

Adj

row shows the operator

op2

such that

P

op

Q

=

Q

op2

P

.

The

Neg

row shows the operator

op2

such that

P

op

Q

= ¬(

P

op2

Q

)

.

The

Dual

row shows the

dual operation

obtained by interchanging T with F, and AND with OR.

The

L id

row shows the operator's

left identities

if it has any values

I

such that

I

op

Q

=

Q

.

The

R id

row shows the operator's

right identities

if it has any values

I

such that

P

op

I

=

P

.

### Wittgenstein table

In proposition 5.101 of the *Tractatus Logico-Philosophicus*, Wittgenstein listed the table above as follows:

|   | Truthvalues |   | Operator | Operation name | Tractatus |   |
|---|---|---|---|---|---|---|
| 0 | (F F F F)(p, q) | ⊥ | false | **Opq** | Contradiction | p and not p; and q and not q |
| 1 | (F F F T)(p, q) | NOR | **p** ↓ **q** | **Xpq** | Logical NOR | neither *p* nor *q* |
| 2 | (F F T F)(p, q) | ↚ | **p** ↚ **q** | **Mpq** | Converse nonimplication | *q* and not *p* |
| 3 | (F F T T)(p, q) | **¬p**, **~p** | **¬p** | **Np**, **Fpq** | Negation | not *p* |
| 4 | (F T F F)(p, q) | ↛ | **p** ↛ **q** | **Lpq** | Material nonimplication | *p* and not *q* |
| 5 | (F T F T)(p, q) | **¬q**, **~q** | **¬q** | **Nq**, **Gpq** | Negation | not *q* |
| 6 | (F T T F)(p, q) | XOR | **p** ⊕ **q** | **Jpq** | Exclusive disjunction | *p* or *q*, but not both |
| 7 | (F T T T)(p, q) | NAND | **p** ↑ **q** | **Dpq** | Logical NAND | not both *p* and *q* |
| 8 | (T F F F)(p, q) | AND | **p** ∧ **q** | **Kpq** | Logical conjunction | *p* and *q* |
| 9 | (T F F T)(p, q) | XNOR | **p** iff **q** | **Epq** | Logical biconditional | if *p* then *q*; and if *q* then *p* |
| 10 | (T F T F)(p, q) | **q** | **q** | **Hpq** | Projection function | *q* |
| 11 | (T F T T)(p, q) | **p** → **q** | if **p** then **q** | **Cpq** | Material implication | if *p* then *q* |
| 12 | (T T F F)(p, q) | **p** | **p** | **Ipq** | Projection function | *p* |
| 13 | (T T F T)(p, q) | **p** ← **q** | if **q** then **p** | **Bpq** | Converse implication | if *q* then *p* |
| 14 | (T T T F)(p, q) | OR | **p** ∨ **q** | **Apq** | Logical disjunction | *p* or *q* |
| 15 | (T T T T)(p, q) | ⊤ | true | **Vpq** | Tautology | if p then p; and if q then q |

The truth table represented by each row is obtained by appending the sequence given in **Truthvalues**row to the table

| *p* | T | T | F | F |
|---|---|---|---|---|
| *q* | T | F | T | F |

For example, the table

| *p* | T | T | F | F |
|---|---|---|---|---|
| *q* | T | F | T | F |
| *11* | T | F | T | T |

represents the truth table for Material implication. Logical operators can also be visualized using Venn diagrams.

### Nullary operations

There are 2 nullary operations:

- Always true
- Never true, unary *falsum*

#### Logical true

The output value is always true, because this operator has zero operands and therefore no input values

| *p* | *T* |
|---|---|
| T | T |
| F | T |

#### Logical false

The output value is never true: that is, always false, because this operator has zero operands and therefore no input values

| *p* | *F* |
|---|---|
| T | F |
| F | F |

### Unary operations

There are 2 unary operations:

- Unary *identity*
- Unary *negation*

#### Logical identity

Logical identity is an operation on one logical value p, for which the output value remains p.

The truth table for the logical identity operator is as follows:

| *p* | *p* |
|---|---|
| T | T |
| F | F |

#### Logical negation

Logical negation is an operation on one logical value, typically the value of a proposition, that produces a value of *true* if its operand is false and a value of *false* if its operand is true.

The truth table for **NOT p** (also written as **¬p**, **Np**, **Fpq**, or **~p**) is as follows:

| *p* | *¬p* |
|---|---|
| T | F |
| F | T |

### Binary operations

There are 16 possible truth functions of two binary variables, each operator has its own name.

#### Logical conjunction (AND)

Logical conjunction is an operation on two logical values, typically the values of two propositions, that produces a value of *true* if both of its operands are true.

The truth table for **p AND q** (also written as **p ∧ q**, **Kpq**, **p & q**, or **p** $\cdot$ **q**) is as follows:

| *p* | *q* | *p* ∧ *q* |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

In ordinary language terms, if both *p* and *q* are true, then the conjunction *p* ∧ *q* is true. For all other assignments of logical values to *p* and to *q* the conjunction *p* ∧ *q* is false.

It can also be said that if *p*, then *p* ∧ *q* is *q*, otherwise *p* ∧ *q* is *p*.

#### Logical disjunction (OR)

Logical disjunction is an operation on two logical values, typically the values of two propositions, that produces a value of *true* if at least one of its operands is true.

The truth table for **p OR q** (also written as **p ∨ q**, **Apq**, **p || q**, or **p + q**) is as follows:

| *p* | *q* | *p* ∨ *q* |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

Stated in English, if *p*, then *p* ∨ *q* is *p*, otherwise *p* ∨ *q* is *q*.

#### Logical implication

Logical implication and the material conditional are both associated with an operation on two logical values, typically the values of two propositions, which produces a value of *false* if the first operand is true and the second operand is false, and a value of *true* otherwise.

The truth table associated with the logical implication **p implies q** (symbolized as **p ⇒ q**, or more rarely **Cpq**) is as follows:

| *p* | *q* | *p* ⇒ *q* |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

The truth table associated with the material conditional **if p then q** (symbolized as **p → q**) is as follows:

| *p* | *q* | *p* → *q* |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**p ⇒ q** and **p → q** are equivalent to **¬p ∨ q**.

#### Logical equality

Logical equality (also known as biconditional or exclusive nor) is an operation on two logical values, typically the values of two propositions, that produces a value of *true* if both operands are false or both operands are true.

The truth table for **p XNOR q** (also written as **p ↔ q**, **Epq**, **p = q**, or **p ≡ q**) is as follows:

| *p* | *q* | *p* ↔ *q* |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

So p EQ q is true if p and q have the same truth value (both true or both false), and false if they have different truth values.

#### Exclusive disjunction

Exclusive disjunction is an operation on two logical values, typically the values of two propositions, that produces a value of *true* if one but not both of its operands is true.

The truth table for **p XOR q** (also written as **Jpq**, or **p ⊕ q**) is as follows:

| *p* | *q* | **p** ⊕ **q** |
|---|---|---|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

For two propositions, **XOR** can also be written as (p ∧ ¬q) ∨ (¬p ∧ q).

#### Logical NAND

The logical NAND is an operation on two logical values, typically the values of two propositions, that produces a value of *false* if both of its operands are true. In other words, it produces a value of *true* if at least one of its operands is false.

The truth table for **p NAND q** (also written as **p ↑ q**, **Dpq**, or **p | q**) is as follows:

| *p* | *q* | *p* ↑ *q* |
|---|---|---|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | T |

It is frequently useful to express a logical operation as a compound operation, that is, as an operation that is built up or composed from other operations. Many such compositions are possible, depending on the operations that are taken as basic or "primitive" and the operations that are taken as composite or "derivative".

In the case of logical NAND, it is clearly expressible as a compound of NOT and AND.

The negation of a conjunction: ¬(*p* ∧ *q*), and the disjunction of negations: (¬*p*) ∨ (¬*q*) can be tabulated as follows:

| *p* | *q* | *p* ∧ *q* | ¬(*p* ∧ *q*) | ¬*p* | ¬*q* | (¬*p*) ∨ (¬*q*) |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

#### Logical NOR

The logical NOR is an operation on two logical values, typically the values of two propositions, that produces a value of *true* if both of its operands are false. In other words, it produces a value of *false* if at least one of its operands is true. ↓ is also known as the Peirce arrow after its inventor, Charles Sanders Peirce, and is a Sole sufficient operator.

The truth table for **p NOR q** (also written as **p ↓ q**, or **Xpq**) is as follows:

| *p* | *q* | *p* ↓ *q* |
|---|---|---|
| T | T | F |
| T | F | F |
| F | T | F |
| F | F | T |

The negation of a disjunction ¬(*p* ∨ *q*), and the conjunction of negations (¬*p*) ∧ (¬*q*) can be tabulated as follows:

| *p* | *q* | *p* ∨ *q* | ¬(*p* ∨ *q*) | ¬*p* | ¬*q* | (¬*p*) ∧ (¬*q*) |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | T | F | F | T | F |
| F | T | T | F | T | F | F |
| F | F | F | T | T | T | T |

Inspection of the tabular derivations for NAND and NOR, under each assignment of logical values to the functional arguments *p* and *q*, produces the identical patterns of functional values for ¬(*p* ∧ *q*) as for (¬*p*) ∨ (¬*q*), and for ¬(*p* ∨ *q*) as for (¬*p*) ∧ (¬*q*). Thus the first and second expressions in each pair are logically equivalent, and may be substituted for each other in all contexts that pertain solely to their logical values.

This equivalence is one of De Morgan's laws.
