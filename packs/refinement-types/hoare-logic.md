---
title: "Hoare logic"
source: https://en.wikipedia.org/wiki/Hoare_logic
domain: refinement-types
license: CC-BY-SA-4.0
tags: refinement type, liquid types, predicate subtyping, dependent refinement
fetched: 2026-07-02
---

# Hoare logic

**Hoare logic** (also known as **Floyd–Hoare logic** or **Hoare rules**) is a formal system with a set of logical rules for reasoning rigorously about the correctness of computer programs. It was proposed in 1969 by the British computer scientist and logician Tony Hoare, and subsequently refined by Hoare and other researchers. The original ideas were seeded by the work of Robert W. Floyd, who had published a similar system for flowcharts.

## Hoare triple

The central feature of **Hoare logic** is the **Hoare triple**. A triple describes how the execution of a piece of code changes the state of the computation. A Hoare triple is of the form

$\{P\}C\{Q\}$

where P and Q are *assertions* and C is a *command*. P is named the *precondition* and Q the *postcondition*: when the precondition is met, executing the command establishes the postcondition. Assertions are formulae in predicate logic.

Hoare logic provides axioms and inference rules for all the constructs of a simple imperative programming language. In addition to the rules for the simple language in Hoare's original paper, rules for other language constructs have been developed since then by Hoare and many other researchers. There are rules for concurrency, procedures, jumps, and pointers.

## Partial and total correctness

Using standard Hoare logic, only partial correctness can be proven. Total correctness additionally requires termination, which can be proven separately or with an extended version of the While rule. Thus, the intuitive reading of a Hoare triple is: Whenever P holds of the state before the execution of C , then Q will hold afterwards, or C does not terminate. In the latter case, there is no "after", so Q can be any statement at all. Indeed, one can choose Q to be false to express that C does not terminate.

"Termination" here and in the rest of this article is meant in the broader sense that computation will eventually be finished, that is, it implies the absence of infinite loops; it does not imply the absence of implementation limit violations (e.g., division by zero), stopping the program prematurely. In his 1969 paper, Hoare used a narrower notion of termination, which also entailed the absence of implementation limit violations, and expressed his preference for the broader notion of termination as it keeps assertions implementation-independent:

> Another deficiency in the axioms and rules quoted above is that they give no basis for a proof that a program successfully terminates. Failure to terminate may be due to an infinite loop; or it may be due to violation of an implementation-defined limit, for example, the range of numeric operands, the size of storage, or an operating system time limit. Thus the notation “ $P\{Q\}R$ ” should be interpreted “provided that the program successfully terminates, the properties of its results are described by R .” It is fairly easy to adapt the axioms so that they cannot be used to predict the “results” of nonterminating programs; but the actual use of the axioms would now depend on knowledge of many implementation-dependent features, for example, the size and speed of the computer, the range of numbers, and the choice of overflow technique. Apart from proofs of the avoidance of infinite loops, it is probably better to prove the “conditional” correctness of a program and rely on an implementation to give a warning if it has had to abandon execution of the program as a result of violation of an implementation limit.

— Hoare 1969, pp. 578–579

## Rules

### Empty statement axiom schema

The empty statement rule asserts that the skip statement does not change the state of the program, thus whatever holds true before skip also holds true afterwards.

${\dfrac {}{\{P\}{\texttt {skip}}\{P\}}}$

### Assignment axiom schema

The assignment axiom states that, after the assignment, any predicate that was previously true for the right-hand side of the assignment now holds for the variable. Formally, let P be an assertion in which the variable x is free. Then:

${\dfrac {}{\{P[E/x]\}x:=E\{P\}}}$

where $P[E/x]$ denotes the assertion P in which each free occurrence of x has been replaced by the expression E.

The assignment axiom scheme means that the truth of $P[E/x]$ is equivalent to the after-assignment truth of P. Thus, were $P[E/x]$ true before the assignment, by the assignment axiom, then P would be true afterwards. Conversely, were $P[E/x]$ false (i.e. $\neg P[E/x]$ true) prior to the assignment statement, P must then be false afterwards.

Examples of valid triples include:

- $\{x+1=43\}y:=x+1\{y=43\}$
- $\{x+1\leq N\}x:=x+1\{x\leq N\}$

All preconditions that are not modified by the expression can be carried over to the postcondition. In the first example, assigning $y:=x+1$ does not change the fact that $x+1=43$ , so both statements may appear in the postcondition. Formally, this result is obtained by applying the axiom schema with P being ( $y=43$ and $x+1=43$ ), which yields $P[(x+1)/y]$ being ( $x+1=43$ and $x+1=43$ ), which can in turn be simplified to the given precondition $x+1=43$ .

The assignment axiom scheme is equivalent to saying that to find the precondition, first take the post-condition and replace all occurrences of the left-hand side of the assignment with the right-hand side of the assignment. Be careful not to try to do this backwards by following this *incorrect* way of thinking: $\{P\}x:=E\{P[E/x]\}$ ; this rule leads to nonsensical examples like:

$\{x=5\}x:=3\{3=5\}$

Another *incorrect* rule looking tempting at first glance is $\{P\}x:=E\{P\wedge x=E\}$ ; it leads to nonsensical examples like:

$\{x=5\}x:=x+1\{x=5\wedge x=x+1\}$

While a given postcondition P uniquely determines the precondition $P[E/x]$ , the converse is not true. For example:

- $\{0\leq y\cdot y\wedge y\cdot y\leq 9\}x:=y\cdot y\{0\leq x\wedge x\leq 9\}$ ,
- $\{0\leq y\cdot y\wedge y\cdot y\leq 9\}x:=y\cdot y\{0\leq x\wedge y\cdot y\leq 9\}$ ,
- $\{0\leq y\cdot y\wedge y\cdot y\leq 9\}x:=y\cdot y\{0\leq y\cdot y\wedge x\leq 9\}$ , and
- $\{0\leq y\cdot y\wedge y\cdot y\leq 9\}x:=y\cdot y\{0\leq y\cdot y\wedge y\cdot y\leq 9\}$

are valid instances of the assignment axiom scheme.

The assignment axiom proposed by Hoare *does not apply* when more than one name may refer to the same stored value. For example,

$\{y=3\}x:=2\{y=3\}$

is wrong if x and y refer to the same variable (aliasing), although it is a proper instance of the assignment axiom scheme (with both $\{P\}$ and $\{P[2/x]\}$ being $\{y=3\}$ ).

### Rule of composition

| Verifying swap-code without auxiliary variables |
|---|
| The three statements below (line 2, 4, 6) exchange the values of the variables a and b, without needing an auxiliary variable. In the verification proof, the initial value of a and b is denoted by the constant A and B, respectively. The proof is best read backwards, starting from line 7; for example, line 5 is obtained from line 7 by replacing a (target expression in line 6) by $a-b$ (source expression in line 6). Some arithmetical simplifications are used tacitly, viz. $a-(a-b)=b$ (line 5→3), and $a+b-b=a$ (line 3→1). **Nr** **Code** **Assertions** **1:**       $\{a=A\wedge b=B\}$ **2:** $a:=a+b;$       **3:** $\{a-b=A\wedge b=B\}$ **4:** $b:=a-b;$ **5:** $\{b=A\wedge a-b=B\}$ **6:** $a:=a-b$ **7:** $\{b=A\wedge a=B\}$ |

Hoare's rule of composition applies to sequentially executed programs S and T, where S executes prior to T and is written $S;T$ (Q is called the *midcondition*):

${\dfrac {\{P\}S\{Q\}\quad ,\quad \{Q\}T\{R\}}{\{P\}S;T\{R\}}}$

For example, consider the following two instances of the assignment axiom:

$\{x+1=43\}y:=x+1\{y=43\}$

and

$\{y=43\}z:=y\{z=43\}$

By the sequencing rule, one concludes:

$\{x+1=43\}y:=x+1;z:=y\{z=43\}$

Another example is shown in the right box.

### Conditional rule

${\dfrac {\{B\wedge P\}S\{Q\}\quad ,\quad \{\neg B\wedge P\}T\{Q\}}{\{P\}{\texttt {if}}\ B\ {\texttt {then}}\ S\ {\texttt {else}}\ T\ {\texttt {endif}}\{Q\}}}$

The conditional rule states that a postcondition Q common to then and else part is also a postcondition of the whole if...endif statement. In the then and the else part, the unnegated and negated condition B can be added to the precondition P, respectively. The condition, B, must not have side effects. An example is given in the next section.

This rule was not contained in Hoare's original publication. However, since a statement

${\texttt {if}}\ B\ {\texttt {then}}\ S\ {\texttt {else}}\ T\ {\texttt {endif}}$

has the same effect as a one-time loop construct

${\texttt {bool}}\ b:={\texttt {true}};{\texttt {while}}\ B\wedge b\ {\texttt {do}}\ S;b:={\texttt {false}}\ {\texttt {done}};b:={\texttt {true}};{\texttt {while}}\ \neg B\wedge b\ {\texttt {do}}\ T;b:={\texttt {false}}\ {\texttt {done}}$

the conditional rule can be derived from the other Hoare rules. In a similar way, rules for other derived program constructs, like for loop, do...until loop, switch, break, continue can be reduced by program transformation to the rules from Hoare's original paper.

### Consequence rule

${\dfrac {P_{1}\rightarrow P_{2}\quad ,\quad \{P_{2}\}S\{Q_{2}\}\quad ,\quad Q_{2}\rightarrow Q_{1}}{\{P_{1}\}S\{Q_{1}\}}}$

This rule permits strengthening the precondition $P_{2}$ and/or to weaken the postcondition $Q_{2}$ . It is used, e.g., to achieve literally identical postconditions for the then and the else part.

For example, a proof of

$\{0\leq x\leq 15\}{\texttt {if}}\ x<15\ {\texttt {then}}\ x:=x+1\ {\texttt {else}}\ x:=0\ {\texttt {endif}}\{0\leq x\leq 15\}$

needs to apply the conditional rule, which in turn requires to prove

$\{0\leq x\leq 15\wedge x<15\}x:=x+1\{0\leq x\leq 15\}$

,   or simplified

$\{0\leq x<15\}x:=x+1\{0\leq x\leq 15\}$

for the then part, and

$\{0\leq x\leq 15\wedge x\geq 15\}x:=0\{0\leq x\leq 15\}$

,   or simplified

$\{x=15\}x:=0\{0\leq x\leq 15\}$

for the else part.

However, the assignment rule for the then part requires to choose P as $0\leq x\leq 15$ ; rule application hence yields

$\{0\leq x+1\leq 15\}x:=x+1\{0\leq x\leq 15\}$

,   which is logically equivalent to

$\{-1\leq x<15\}x:=x+1\{0\leq x\leq 15\}$

.

The consequence rule is needed to strengthen the precondition $\{-1\leq x<15\}$ obtained from the assignment rule to $\{0\leq x<15\}$ required for the conditional rule.

Similarly, for the else part, the assignment rule yields

$\{0\leq 0\leq 15\}x:=0\{0\leq x\leq 15\}$

,   or equivalently

$\{{\texttt {true}}\}x:=0\{0\leq x\leq 15\}$

,

hence the consequence rule has to be applied with $P_{1}$ and $P_{2}$ being $\{x=15\}$ and $\{{\texttt {true}}\}$ , respectively, to strengthen again the precondition. Informally, the effect of the consequence rule is to "forget" that $\{x=15\}$ is known at the entry of the else part, since the assignment rule used for the else part doesn't need that information.

### While rule

${\dfrac {\{P\wedge B\}S\{P\}}{\{P\}{\texttt {while}}\ B\ {\texttt {do}}\ S\ {\texttt {done}}\{\neg B\wedge P\}}}$

Here P is the loop invariant, which is to be preserved by the loop body S. After the loop is finished, this invariant P still holds, and moreover $\neg B$ must have caused the loop to end. As in the conditional rule, B must not have side effects.

For example, a proof of

$\{x\leq 10\}{\texttt {while}}\ x<10\ {\texttt {do}}\ x:=x+1\ {\texttt {done}}\{\neg x<10\wedge x\leq 10\}$

by the while rule requires to prove

$\{x\leq 10\wedge x<10\}x:=x+1\{x\leq 10\}$

,   or simplified

$\{x<10\}x:=x+1\{x\leq 10\}$

,

which is easily obtained by the assignment rule. Finally, the postcondition $\{\neg x<10\wedge x\leq 10\}$ can be simplified to $\{x=10\}$ .

For another example, the while rule can be used to formally verify the following strange program to compute the exact square root x of an arbitrary number a—even if x is an integer variable and a is not a square number:

$\{{\texttt {true}}\}{\texttt {while}}\ x\cdot x\neq a\ {\texttt {do}}\ {\texttt {skip}}\ {\texttt {done}}\{x\cdot x=a\wedge {\texttt {true}}\}$

After applying the while rule with P being true, it remains to prove

$\{{\texttt {true}}\wedge x\cdot x\neq a\}{\texttt {skip}}\{{\texttt {true}}\}$

,

which follows from the skip rule and the consequence rule.

In fact, the strange program is *partially* correct: if it happened to terminate, it is certain that x must have contained (by chance) the value of a's square root. In all other cases, it will not terminate; therefore, it is not *totally* correct.

### While rule for total correctness

If the above ordinary while rule is replaced by the following one, the Hoare calculus can also be used to prove total correctness, i.e., termination as well as partial correctness. Commonly, square brackets are used here instead of curly braces to indicate the different notion of program correctness.

${\dfrac {<\ {\text{is a well-founded ordering on the set}}\ D\quad ,\quad [P\wedge B\wedge t\in D\wedge t=z]S[P\wedge t\in D\wedge t<z]}{[P\wedge t\in D]{\texttt {while}}\ B\ {\texttt {do}}\ S\ {\texttt {done}}[\neg B\wedge P\wedge t\in D]}}$

In this rule, in addition to maintaining the loop invariant, one also proves termination by way of an expression t, called the loop variant, whose value strictly decreases with respect to a well-founded relation < on some domain set D during each iteration. Since < is well-founded, a strictly decreasing chain of members of D can have only finite length, so t cannot keep decreasing forever. (For example, the usual order < is well-founded on positive integers $\mathbb {N}$ , but neither on the integers $\mathbb {Z}$ nor on positive real numbers $\mathbb {R} ^{+}$ ; all these sets are meant in the mathematical, not in the computing sense, they are all infinite in particular.)

Given the loop invariant P, the condition B must imply that t is not a minimal element of D, for otherwise the body S could not decrease t any further, i.e. the premise of the rule would be false. (This is one of various notations for total correctness.)

Resuming the first example of the previous section, for a total-correctness proof of

$[x\leq 10]{\texttt {while}}\ x<10\ {\texttt {do}}\ x:=x+1\ {\texttt {done}}[\neg x<10\wedge x\leq 10]$

the while rule for total correctness can be applied with e.g. D being the non-negative integers with the usual order, and the expression t being $10-x$ , which then in turn requires to prove

$[x\leq 10\wedge x<10\wedge 10-x\geq 0\wedge 10-x=z]x:=x+1[x\leq 10\wedge 10-x\geq 0\wedge 10-x<z]$

Informally speaking, we have to prove that the distance $10-x$ decreases in every loop cycle, while it always remains non-negative; this process can go on only for a finite number of cycles.

The previous proof goal can be simplified to

$[x<10\wedge 10-x=z]x:=x+1[x\leq 10\wedge 10-x<z]$

,

which can be proven as follows:

$[x+1\leq 10\wedge 10-x-1<z]x:=x+1[x\leq 10\wedge 10-x<z]$

is obtained by the assignment rule, and

$[x+1\leq 10\wedge 10-x-1<z]$

can be strengthened to

$[x<10\wedge 10-x=z]$

by the consequence rule.

For the second example of the previous section, of course, no expression t can be found that is decreased by the empty loop body, hence termination cannot be proved.
