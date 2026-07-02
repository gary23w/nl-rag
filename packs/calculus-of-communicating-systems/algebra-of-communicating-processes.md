---
title: "Algebra of communicating processes"
source: https://en.wikipedia.org/wiki/Algebra_of_Communicating_Processes
domain: calculus-of-communicating-systems
license: CC-BY-SA-4.0
tags: calculus of communicating systems, labelled transition system, process algebra, structural congruence
fetched: 2026-07-02
---

# Algebra of communicating processes

(Redirected from

Algebra of Communicating Processes

)

The **algebra of communicating processes** (ACP) is an algebraic approach to reasoning about concurrent systems. It is a member of the family of mathematical theories of concurrency known as process algebras or process calculi. ACP was initially developed by Jan Bergstra and Jan Willem Klop in 1982, as part of an effort to investigate the solutions of unguarded recursive equations. More so than the other seminal process calculi (CCS and CSP), the development of ACP focused on the algebra of processes, and sought to create an abstract, generalized axiomatic system for processes, and in fact the term *process algebra* was coined during the research that led to ACP.

## Informal description

ACP is fundamentally an algebra, in the sense of universal algebra. This algebra is a way to describe systems in terms of algebraic process expressions that define compositions of other processes, or of certain primitive elements.

### Primitives

ACP uses instantaneous, *atomic actions* ( ${\mathit {a,b,c,...}}$ ) as its primitives. Some actions have special meaning, such as the action $\delta$ , which represents deadlock or stagnation, and the action $\tau$ , which represents a *silent action* (abstracted actions that have no specific identity).

### Algebraic operators

Actions can be combined to form *processes* using a variety of operators. These operators can be roughly categorized as providing a *basic process algebra*, *concurrency*, and *communication*.

- **Choice and sequencing** – the most fundamental of algebraic operators are the *alternative* operator ( + ), which provides a choice between actions, and the *sequencing operator* ( $\cdot$ ), which specifies an ordering on actions. So, for example, the process

$(a+b)\cdot c$

first chooses to perform either

${\mathit {a}}$

or

${\mathit {b}}$

, and then performs action

${\mathit {c}}$

. How the choice between

${\mathit {a}}$

and

${\mathit {b}}$

is made does not matter and is left unspecified. Note that alternative composition is commutative but sequential composition is not (because time flows forward).

- **Concurrency** – to allow the description of concurrency, ACP provides the *merge* and *left-merge* operators. The merge operator, $\vert \vert$ , represents the parallel composition of two processes, the individual actions of which are interleaved. The left-merge operator, $\vert \lfloor$ , is an auxiliary operator with similar semantics to the merge, but a commitment to always choose its initial step from the left-hand process. As an example, the process

$(a\cdot b)\vert \vert (c\cdot d)$

may perform the actions

$a,b,c,d$

in any of the sequences

$abcd,acbd,acdb,cabd,cadb,cdab$

. On the other hand, the process

$(a\cdot b)\vert \lfloor (c\cdot d)$

may only perform the sequences

$abcd,acbd,acdb$

since the left-merge operators ensure that the action

${\mathit {a}}$

occurs first.

- **Communication** — interaction (or communication) between processes is represented using the binary communications operator, $\vert$ . For example, the actions $r(d)$ and $w(d)$ might be interpreted as the reading and writing of a data item $d\in D=\{1,2,3,\ldots \}$ , respectively. Then the process

$\left(\sum _{d\in D}r(d)\cdot y\right)\vert (w(1)\cdot z)$

will communicate the value

1

from the right component process to the left component process (

i.e.

the identifier

${\mathit {d}}$

is bound to the value

1

, and free instances of

${\mathit {d}}$

in the process

${\mathit {y}}$

take on that value), and then behave as the merge of

${\mathit {y}}$

and

${\mathit {z}}$

.

- **Abstraction** — the abstraction operator, $\tau _{I}$ , is a way to "hide" certain actions, and treat them as events that are internal to the systems being modelled. Abstracted actions are converted to the *silent step* action $\tau$ . In some cases, these silent steps can also be removed from the process expression as part of the abstraction process. For example,

$\tau _{\{c\}}((a+b)\cdot c)=(a+b)\cdot \tau$

which, in this case, can be reduced to

$a+b$

since the event

${\mathit {c}}$

is no longer observable and has no observable effects.

## Formal definition

ACP fundamentally adopts an axiomatic, algebraic approach to the formal definition of its various operators. The axioms presented below comprise the full axiomatic system for ACP $\tau$ (ACP with abstraction).

### Basic process algebra

Using the alternative and sequential composition operators, ACP defines a *basic process algebra* which satisfies the axioms

${\begin{matrix}x+y&=&y+x\\(x+y)+z&=&x+(y+z)\\x+x&=&x\\(x+y)\cdot z&=&(x\cdot z)+(y\cdot z)\\(x\cdot y)\cdot z&=&x\cdot (y\cdot z)\end{matrix}}$

### Deadlock

Beyond the basic algebra, two additional axioms define the relationships between the alternative and sequencing operators, and the *deadlock* action, $\delta$

${\begin{matrix}\delta +x&=&x\\\delta \cdot x&=&\delta \end{matrix}}$

### Concurrency and interaction

The axioms associated with the merge, left-merge, and communication operators are

${\begin{matrix}x\vert \vert y&=&x\vert \lfloor y+y\vert \lfloor x+x\vert y\\a\cdot x\vert \lfloor y&=&a\cdot (x\vert \vert y)\\a\vert \lfloor y&=&a\cdot y\\(x+y)\vert \lfloor z&=&(x\vert \lfloor z)+(y\vert \lfloor z)\\a\cdot x\vert b&=&(a\vert b)\cdot x\\a\vert b\cdot x&=&(a\vert b)\cdot x\\a\cdot x\vert b\cdot y&=&(a\vert b)\cdot (x\vert \vert y)\\(x+y)\vert z&=&x\vert z+y\vert z\\x\vert (y+z)&=&x\vert y+x\vert z\end{matrix}}$

When the communications operator is applied to actions alone, rather than processes, it is interpreted as a binary function from actions to actions, $\vert :A\times A\rightarrow A$ . The definition of this function defines the possible interactions between processes — those pairs of actions that do not constitute interactions are mapped to the deadlock action, $\delta$ , while permitted interaction pairs are mapped to corresponding single actions representing the occurrence of an interaction. For example, the communications function might specify that

$a\vert a\rightarrow c$

which indicates that a successful interaction $a\vert a$ will be reduced to the action c . ACP also includes an encapsulation operator, $\partial _{H}$ for some $H\subseteq A$ , which is used to convert unsuccessful communication attempts (i.e. elements of H that have not been reduced via the communication function) to the deadlock action. The axioms associated with the communications function and encapsulation operator are

${\begin{matrix}a\vert b&=&b\vert a\\(a\vert b)\vert c&=&a\vert (b\vert c)\\a\vert \delta &=&\delta \\\partial _{H}(a)&=&a{\mbox{ if }}a\notin H\\\partial _{H}(a)&=&\delta {\mbox{ if }}a\in H\\\partial _{H}(x+y)&=&\partial _{H}(x)+\partial _{H}(y)\\\partial _{H}(x\cdot y)&=&\partial _{H}(x)\cdot \partial _{H}(y)\\\end{matrix}}$

### Abstraction

The axioms associated with the abstraction operator are

${\begin{matrix}\tau _{I}(\tau )&=&\tau \\\tau _{I}(a)&=&a{\mbox{ if }}a\notin I\\\tau _{I}(a)&=&\tau {\mbox{ if }}a\in I\\\tau _{I}(x+y)&=&\tau _{I}(x)+\tau _{I}(y)\\\tau _{I}(x\cdot y)&=&\tau _{I}(x)\cdot \tau _{I}(y)\\\partial _{H}(\tau )&=&\tau \\x\cdot \tau &=&x\\\tau \cdot x&=&\tau \cdot x+x\\a\cdot (\tau \cdot x+y)&=&a\cdot (\tau \cdot x+y)+a\cdot x\\\tau \cdot x\vert \lfloor y&=&\tau \cdot (x\vert \vert y)\\\tau \vert \lfloor x&=&\tau \cdot x\\\tau \vert x&=&\delta \\x\vert \tau &=&\delta \\\tau \cdot x\vert y&=&x\vert y\\x\vert \tau \cdot y&=&x\vert y\end{matrix}}$

Note that the action *a* in the above list may take the value δ (but of course, δ cannot belong to the abstraction set *I*).

ACP has served as the basis or inspiration for several other formalisms that can be used to describe and analyze concurrent systems, including:

- PSF Archived 2014-10-16 at the Wayback Machine
- μCRL
- mCRL2
- HyPA — a process algebra for hybrid systems
