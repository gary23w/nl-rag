---
title: "Boolean algebra (part 2/2)"
source: https://en.wikipedia.org/wiki/Boolean_algebra
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
part: 2/2
---

## Applications

Boolean algebra as the calculus of two values is fundamental to computer circuits, computer programming, and mathematical logic, and is also used in other areas of mathematics such as set theory and statistics.

### Computers

In the early 20th century, several electrical engineers intuitively recognized that Boolean algebra was analogous to the behavior of certain types of electrical circuits. Claude Shannon formally proved such behavior was logically equivalent to Boolean algebra in his 1937 master's thesis, *A Symbolic Analysis of Relay and Switching Circuits*.

Today, all modern general-purpose computers perform their functions using two-value Boolean logic; that is, their electrical circuits are a physical manifestation of two-value Boolean logic. They achieve this in various ways: as voltages on wires in high-speed circuits and capacitive storage devices, as orientations of a magnetic domain in ferromagnetic storage devices, as holes in punched cards or paper tape, and so on. (Some early computers used decimal circuits or mechanisms instead of two-valued logic circuits.)

Of course, it is possible to code more than two symbols in any given medium. For example, one might use respectively 0, 1, 2, and 3 volts to code a four-symbol alphabet on a wire, or holes of different sizes in a punched card. In practice, the tight constraints of high speed, small size, and low power combine to make noise a major factor. This makes it hard to distinguish between symbols when there are several possible symbols that could occur at a single site. Rather than attempting to distinguish between four voltages on one wire, digital designers have settled on two voltages per wire, high and low.

Computers use two-value Boolean circuits for the above reasons. The most common computer architectures use ordered sequences of Boolean values, called bits, of 32 or 64 values, e.g. 01101000110101100101010101001011. When programming in machine code, assembly language, and certain other programming languages, programmers work with the low-level digital structure of the data registers. These registers operate on voltages, where zero volts represents Boolean 0, and a reference voltage (often +5 V, +3.3 V, or +1.8 V) represents Boolean 1. Such languages support both numeric operations and logical operations. In this context, "numeric" means that the computer treats sequences of bits as binary numbers (base two numbers) and executes arithmetic operations like add, subtract, multiply, or divide. "Logical" refers to the Boolean logical operations of disjunction, conjunction, and negation between two sequences of bits, in which each bit in one sequence is simply compared to its counterpart in the other sequence. Programmers therefore have the option of working in and applying the rules of either numeric algebra or Boolean algebra as needed. A core differentiating feature between these families of operations is the existence of the carry operation in the first but not the second.

### Two-valued logic

Other areas where two values is a good choice are the law and mathematics. In everyday relaxed conversation, nuanced or complex answers such as "maybe" or "only on the weekend" are acceptable. In more focused situations such as a court of law or theorem-based mathematics, however, it is deemed advantageous to frame questions so as to admit a simple yes-or-no answer—is the defendant guilty or not guilty, is the proposition true or false—and to disallow any other answer. However limiting this might prove in practice for the respondent, the principle of the simple yes–no question has become a central feature of both judicial and mathematical logic, making two-valued logic deserving of organization and study in its own right.

A central concept of set theory is membership. An organization may permit multiple degrees of membership, such as novice, associate, and full. With sets, however, an element is either in or out. The candidates for membership in a set work just like the wires in a digital computer: each candidate is either a member or a nonmember, just as each wire is either high or low.

Algebra being a fundamental tool in any area amenable to mathematical treatment, these considerations combine to make the algebra of two values of fundamental importance to computer hardware, mathematical logic, and set theory.

Two-valued logic can be extended to multi-valued logic, notably by replacing the Boolean domain {0, 1} with the unit interval [0,1], in which case rather than only taking values 0 or 1, any value between and including 0 and 1 can be assumed. Algebraically, negation (NOT) is replaced with 1 − *x*, conjunction (AND) is replaced with multiplication (*xy*), and disjunction (OR) is defined via De Morgan's law. Interpreting these values as logical truth values yields a multi-valued logic, which forms the basis for fuzzy logic and probabilistic logic. In these interpretations, a value is interpreted as the "degree" of truth – to what extent a proposition is true, or the probability that the proposition is true.

### Boolean operations

The original application for Boolean operations was mathematical logic, where it combines the truth values, true or false, of individual formulas.

#### Natural language

Natural languages such as English have words for several Boolean operations, in particular conjunction (*and*), disjunction (*or*), negation (*not*), and implication (*implies*). *But not* is synonymous with *and not*. When used to combine situational assertions such as "the block is on the table" and "cats drink milk", which naïvely are either true or false, the meanings of these logical connectives often have the meaning of their logical counterparts. However, with descriptions of behavior such as "Jim walked through the door", one starts to notice differences such as failure of commutativity, for example, the conjunction of "Jim opened the door" with "Jim walked through the door" in that order is not equivalent to their conjunction in the other order, since *and* usually means *and then* in such cases. Questions can be similar: the order "Is the sky blue, and why is the sky blue?" makes more sense than the reverse order. Conjunctive commands about behavior are like behavioral assertions, as in *get dressed and go to school*. Disjunctive commands such *love me or leave me* or *fish or cut bait* tend to be asymmetric via the implication that one alternative is less preferable. Conjoined nouns such as *tea and milk* generally describe aggregation as with set union while *tea or milk* is a choice. However, context can reverse these senses, as in *your choices are coffee and tea* which usually means the same as *your choices are coffee or tea* (alternatives). Double negation, as in "I don't not like milk", rarely means literally "I do like milk" but rather conveys some sort of hedging, as though to imply that there is a third possibility. "Not not P" can be loosely interpreted as "surely P", and although *P* necessarily implies "not not *P*," the converse is suspect in English, much as with intuitionistic logic. In view of the highly idiosyncratic usage of conjunctions in natural languages, Boolean algebra cannot be considered a reliable framework for interpreting them.

#### Digital logic

Boolean operations are used in digital logic to combine the bits carried on individual wires, thereby interpreting them over {0,1}. When a vector of *n* identical binary gates are used to combine two bit vectors each of *n* bits, the individual bit operations can be understood collectively as a single operation on values from a Boolean algebra with 2*n* elements.

#### Naive set theory

Naive set theory interprets Boolean operations as acting on subsets of a given set *X*. As we saw earlier this behavior exactly parallels the coordinate-wise combinations of bit vectors, with the union of two sets corresponding to the disjunction of two bit vectors and so on.

#### Video cards

The 256-element free Boolean algebra on three generators is deployed in computer displays based on raster graphics, which use bit blit to manipulate whole regions consisting of pixels, relying on Boolean operations to specify how the source region should be combined with the destination, typically with the help of a third region called the mask. Modern video cards offer all 223 = 256 ternary operations for this purpose, with the choice of operation being a one-byte (8-bit) parameter. The constants SRC = 0xaa or 0b10101010, DST = 0xcc or 0b11001100, and MSK = 0xf0 or 0b11110000 allow Boolean operations such as `(SRC^DST)&MSK` (meaning XOR the source and destination and then AND the result with the mask) to be written directly as a constant denoting a byte calculated at compile time, 0x80 in the `(SRC^DST)&MSK` example, 0x88 if just `SRC^DST`, etc. At run time the video card interprets the byte as the raster operation indicated by the original expression in a uniform way that requires remarkably little hardware and which takes time completely independent of the complexity of the expression.

#### Modeling and CAD

Solid modeling systems for computer aided design offer a variety of methods for building objects from other objects, combination by Boolean operations being one of them. In this method the space in which objects exist is understood as a set *S* of voxels (the three-dimensional analogue of pixels in two-dimensional graphics) and shapes are defined as subsets of *S*, allowing objects to be combined as sets via union, intersection, etc. One obvious use is in building a complex shape from simple shapes simply as the union of the latter. Another use is in sculpting understood as removal of material: any grinding, milling, routing, or drilling operation that can be performed with physical machinery on physical materials can be simulated on the computer with the Boolean operation *x* ∧ ¬*y* or *x* − *y*, which in set theory is set difference, remove the elements of *y* from those of *x*. Thus given two shapes one to be machined and the other the material to be removed, the result of machining the former to remove the latter is described simply as their set difference.

#### Boolean searches

Search engine queries also employ Boolean logic. For this application, each web page on the Internet may be considered to be an "element" of a "set." The following examples use a syntax supported by Google.

- Doublequotes are used to combine whitespace-separated words into a single search term.
- Whitespace is used to specify logical AND, as it is the default operator for joining search terms:

```
"Search term 1" "Search term 2"
```

- The OR keyword is used for logical OR:

```
"Search term 1" OR "Search term 2"
```

- A prefixed minus sign is used for logical NOT:

```
"Search term 1" −"Search term 2"
```

- Parentheses can help broaden search: when terms 2 and 3 are similar terms/synonyms:

```
"Search term 1” and ("Search term 2” or "Search term 3”)
```
