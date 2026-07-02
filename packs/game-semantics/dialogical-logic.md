---
title: "Dialogical logic"
source: https://en.wikipedia.org/wiki/Dialogical_logic
domain: game-semantics
license: CC-BY-SA-4.0
tags: game semantics, dialogical logic, full abstraction, strategy (game theory)
fetched: 2026-07-02
---

# Dialogical logic

**Dialogical logic** (German: *dialogische Logik*, also known as the **logic of dialogues**) is a pragmatic approach to the semantics of logic developed in the 1950s by Paul Lorenzen and Kuno Lorenz. It models logical reasoning as a dialogue game between two participants—a "Proponent" who asserts and defends a thesis and an "Opponent" who challenges it—using concepts from game theory such as "winning a play" and "winning strategy." In this framework, a formula is considered logically valid if the Proponent has a winning strategy for its defense against all possible challenges.

Though dialogical logic was among the first approaches to logical semantics using game-theoretical concepts, it should be distinguished from broader concept of game semantics. While both share game-theoretical foundations, they differ in philosophical background and technical development. Dialogical logic emphasizes the normative practice of reasoning and argumentation, drawing inspiration from constructivist philosophy, whereas other game-semantic approaches like Jaakko Hintikka's game-theoretical semantics (GTS) have different theoretical motivations and formal implementations.

Originally focused on providing alternative semantics for classical logic and intuitionistic logic, dialogical logic has evolved into a general framework for studying meaning, knowledge, and inference in interactive contexts. Recent developments include the study of cooperative dialogues beyond strictly adversarial games, and dialogues deploying a fully interpreted language (referred to as "dialogues with content"), extending its applications to philosophy of language, epistemology, and argumentation theory.

## Origins and further developments

The philosopher and mathematician Paul Lorenzen (Erlangen-Nürnberg-Universität) was the first to introduce a semantics of games for logic in the late 1950s. Lorenzen called this semantics 'dialogische Logik', or dialogic logic. Later, it was developed extensively by his pupil Kuno Lorenz (Erlangen-Nürnberg Universität, then Saarland). Jaakko Hintikka (Helsinki, Boston) developed a little later to Lorenzen a model-theoretical approach known as GTS.

Since then, a significant number of different game semantics have been studied in logic. Since 1993, Shahid Rahman and his collaborators have developed dialogical logic within a general framework aimed at the study of the logical and philosophical issues related to logical pluralism. More precisely, by 1995 a kind of revival of dialogical logic was generated that opened new and unexpected possibilities for logical and philosophical research. The philosophical development of dialogical logic continued especially in the fields of argumentation theory, legal reasoning, computer science, applied linguistics, and artificial intelligence.

The new results in dialogical logic began on one side, with the works of Jean-Yves Girard in linear logic and interaction; on the other, with the study of the interface of logic, mathematical game theory and argumentation, argumentation frameworks and defeasible reasoning, by researchers such as Samson Abramsky, Johan van Benthem, Andreas Blass, Nicolas Clerbout, Frans H. van Eemeren, Mathieu Fontaine, Dov Gabbay, Rob Grootendorst, Giorgi Japaridze, Laurent Keiff, Erik Krabbe, Alain Leconte, Rodrigo Lopez-Orellana, Sébasten Magnier, Mathieu Marion, Zoe McConaughey, Henry Prakken, Juan Redmond, Helge Rückert, Gabriel Sandu, Giovanni Sartor, Douglas N. Walton, and John Woods among others, who have contributed to place dialogical interaction and games at the center of a new perspective of logic, where logic is defined as an instrument of dynamic inference.

Five research programs address the interface of meaning, knowledge, and logic in the context of dialogues, games, or more generally interaction:

1. The constructivist approach of Paul Lorenzen and Kuno Lorenz, who sought to overcome the limitations of operative logic by providing dialogical foundations to it. The method of semantic tableaux for classical and intuitionistic logic as introduced by Evert W. Beth (1955) could thus be identified as a method for the notation of winning strategies of particular dialogue games (Lorenzen/Lorenz 1978, Lorenz 1981, Felscher 1986). This, as mentioned above has been extended by Shahid Rahman and collaborators to a general framework for the study of classical and non-classical logics. Rahman and his team of Lille, in order to develop dialogues with content, enriched the dialogical framework with fully interpreted languages (as implemented within Per Martin-Löf's constructive type theory).
2. The game-theoretical approach of Jaakko Hintikka, called GTS. This approach shares the game-theoretical tenets of dialogical logic for logical constants; but turns to standard model theory when the analysis process reaches the level of elementary statements. At this level standard truth-functional formal semantics comes into play. Whereas in the *formal plays* of dialogical logic P will loose both plays on an elementary proposition, namely the play where the thesis states this proposition and the play where he states its negation; in GTS one of both will be won by the defender. A subsequent development was launched by Johan van Benthem (and his group in Amsterdam) in his book *Logic in Games*, which combines the game-theoretical approaches with epistemic logic.
3. The argumentation theory approach of Else M. Barth and Erik Krabbe (1982), who sought to link dialogical logic with the informal logic or critical reasoning originated by the seminal work of Chaïm Perelman (Perelman/Olbrechts-Tyteca 1958), Stephen Toulmin (1958), Arne Næss (1966) and Charles Leonard Hamblin (1970) and developed further by Ralph Johnson (1999), Douglas N. Walton (1984), John Woods (1988) and associates. Further developments include the argumentation framework of P.D. Dung and others, the defeasible reasoning approach of Henry Prakken and Giovanni Sartor, and pragma-dialectics by Frans H. van Eemeren and Rob Grootendorst.
4. The ludics approach, initiated by Jean-Yves Girard, which provides an overall theory of proof-theoretical meaning based on interactive computation.
5. The alternative perspective on proof theory and meaning theory, advocating that Wittgenstein's "meaning as use" paradigm as understood in the context of proof theory, where the so-called reduction rules (showing the effect of elimination rules on the result of introduction rules) should be seen as appropriate to formalise the explanation of the (immediate) consequences one can draw from a proposition, thus showing the function/purpose/usefulness of its main connective in the calculus of language (de Queiroz (1988), de Queiroz (1991), de Queiroz (1994), de Queiroz (2001), de Queiroz (2008)).

According to the dialogical perspective, knowledge, meaning, and truth are conceived as a result of social interaction, where normativity is not understood as a type of pragmatic operator acting on a propositional nucleus destined to express knowledge and meaning, but on the contrary: the type of normativity that emerges from the social interaction associated with knowledge and meaning is constitutive of these notions. In other words, according to the conception of the dialogical framework, the intertwining of the right to ask for reasons, on the one hand, and the obligation to give them, on the other, provides the roots of knowledge, meaning and truth.

## Local and global meaning

As hinted by its name, this framework studies dialogues, but it also takes the form of dialogues. In a dialogue, two parties (players) argue on a thesis (a certain statement that is the subject of the whole argument) and follow certain fixed rules in their argument. The player who states the thesis is the Proponent, called **P**, and his rival, the player who challenges the thesis, is the Opponent, called **O**. In challenging the Proponent's thesis, the Opponent is requiring of the Proponent that he defends his statement.

The interaction between the two players **P** and **O** is spelled out by challenges and defences, implementing Robert Brandom's take on meaning as a game of giving and asking for reasons. Actions in a dialogue are called moves; they are often understood as speech-acts involving declarative utterances (*assertions*) and interrogative utterances (*requests*). The rules for dialogues thus never deal with expressions isolated from the act of uttering them.

The rules in the dialogical framework are divided into two kinds of rules*: particle rules* and *structural rules*. Whereas the first determine *local meaning*, the second determine *global meaning*.

Local meaning explains the meaning of an expression, independently of the rules setting the development of a dialogue. Global meaning sets the meaning of an expression in the context of some specific form of developing a dialogue.

More precisely:

- Particle rules (*Partikelregeln*), or rules for logical constants, determine the legal moves in a play and regulate interaction by establishing the relevant moves constituting *challenges*: moves that are an appropriate attack to a previous move (a statement) and thus require that the challenged player play the appropriate defence to the attack. If the challenged player defends his statement, he has answered the challenge.
- Structural rules (*Rahmenregeln*) on the other hand determine the general course of a dialogue game, such as how a game is initiated, how to play it, how it ends, and so on. The point of these rules is not so much to spell out the meaning of the logical constants by specifying how to act in an appropriate way (this is the role of the particle rules); it is rather to specify according to what structure interactions will take place. It is one thing to determine the meaning of the logical constants as a set of appropriate challenges and defences, it is another to define whose turn it is to play and when a player is allowed to play a move.

In the most basic case, the particle rules set the local meaning of the logical constants of first-order classical and intuitionistic logic. More precisely the local meaning is set by the following distribution of choices:

- If the defender **X** states "A and B", the challenger **Y** has the right to choose between asking the defender to state A or to state B.
- If the defender **X** states "A or B", the challenger **Y** has the right to ask him to choose between stating A or stating B.
- If the defender **X** states that "if A then B", the challenger **Y** has the right to ask for B by conceding herself (the challenger) A.
- If the defender **X** states "no-A", then the challenger **Y** has the right to state A (and then she has the obligation to defend this assertion).
- If the defender **X** states for "all the x's it is the case that A[x]", the challenger **Y** has the right to choose a singular term t and ask the defender to substitute this term for the free variables in A[x].
- If the defender **X** states "there is at least one x, for which it is the case that A[x]", the challenger **Y** has the right to ask him to choose a singular term and substitute this term for the free variables in A[x].

The next section furnishes a brief overview of the rules for intuitionist logic and classical logic. For a complete formal formulation see Clerbout (2014), Rahman et al. (2018), Rahman & Keiff (2005).

## The rules of the dialogical framework

### The local meaning of the logical constants

- **X** A ∨ B  (A or B)

Challenge: **Y** ?

Defense: **X** A/**X** B

(Defender has the choice to defend A or to defend B)

- **X** A ∧ B  (A and B)

Challenge: **Y** ?L (for left)

Defense **X** A

Challenge: **Y** ?R (for right)

Defense **X** B

(Challenger has the choice to ask for A or to ask for B)

- **X** A⊃B  (If A then B)

Challenge: **Y** A

Defense: **X** B

(Challenger has the right to ask for A by conceding herself A)

- **X** ~A  (No A)

Challenge: **Y** A

Defense: (No defense is possible)

- **X** ∀xA[x]  (All x are A)

Challenge: **Y** ?t

Defense: **X** A[x/t]

(The challenger chooses)

- **X** ∃xA[x]  (At least one x is A)

Challenge: **Y** ?

Defense: **X** A[x/t]

(The defender chooses)

### Structural rules: global meaning

#### RS 1 (Launching a dialogue or play)

Any play (dialogue) starts with the Proponent **P** stating a thesis (labelled move 0) and the Opponent O bringing forward some initial statement (if any). The first move of **O**, labelled with 1, is an attack to the thesis of the dialogue.

Each subsequent move consists of one of the two interlocutors, bringing forward in turn either an attack against a previous statement of the opponent, or a defense of a previous attack of the antagonist.

#### RS 2i (Intuitionist rule)

**X** can attack any statement brought forward by **Y**, so far as the particle rules and the remaining structural rules allow it, or respond only to the ***last non-answered*** challenge of the other player.

*Note: This last clause is known as the*Last Duty First*condition, and makes dialogical games suitable for intuitionistic logic (hence this rule's name).*

#### RS 2c (Classical rule)

**X** can attack any statement brought forward by **Y**, so far as the particle rules and the remaining structural rules allow it, or defend himself against any attack of **Y** (so far as the particle rules and the remaining structural rules allow it,)

#### RS 3 (Finiteness of plays)

##### *Intuitionist rule*

**O** can attack the same statement at most once.

**P** can attack the same statement some finite number of times.

##### *Classic rule*

**O** can attack the same statement or defend himself against an attack at most once.

**P** can an attack the same statement some finite number of times. The same restriction also holds for **P'**s defences.

#### RS 4 (Formal rule)

**P** can state an elementary proposition only if **O** has stated it before.

**O** always has the right to state elementary propositions (so far the rules of logical constants and other structural rules allow it).

Elementary propositions (in a formal dialogue) cannot be attacked.

**RS5 (Winning and end of a play**)

The play ends when it is a player's turn to make a move but that player has no available move left. That player loses, the other player wins.

### Validity and valid inferences

The notion of a winning a play is not enough to render the notion of inference or of logical validity.

In the following example, the thesis is of course not valid. However, **P** wins because **O** made the wrong choice. In fact, **O** loses the play since the structural rules do not allow her to challenge twice the same move.

|   | O | P |   |
|---|---|---|---|
|   |   | A ∧ (A⊃A) | 0. |
| 1. | ?D [0] | A⊃A | 2. |
| 3. | A [2] | A | 4. |

In move 0 *P* states the thesis. In move 2, *O* challenges the thesis by asking *P* to state the right component of the conjunction – the notation "[n]" indicates the number of the challenged move. In move 3 *O* challenges the 'implication by granting the antecedent. *P* responds to this challenge by stating the consequentn the just granted proposition A, and, since there are no other possible moves for **O**, **P** wins.

There is obviously another play, where **O** wins, namely, asking for the left side of the conjunction.

Dually a valid thesis can be lost because **P** this time, makes the wrong choice. In the following example **P** loses the play (played according to the intuitionistic rules) by choosing the left side of the disjunction A ∨(A⊃A), since the intuitionistic rule SR 2i prevents him to come back and revise his choice:

|   | O | P |   |
|---|---|---|---|
|   |   | (A ∧ B) ∨ (A⊃A) | 0. |
| 1. | ?∨ [0] | A ∧ B | 2. |
| 3. | ?G [2] | ... |   |

Hence, winning a play does not ensure validity. In order to cast the notion of validity within the dialogical framework we need to define what a winning strategy is. In fact, there are several ways to do it. For the sake of a simple presentation we will yield a variation of Felscher (1985), however; different to his approach, we will not transform dialogues into tableaux but keep the distinction between play (a dialogue) and the tree of plays constituting a winning strategy.

#### Winning strategy

- A player **X** has a winning strategy if for every move made by the other player **Y**, player **X** can make another move, such that each resulting play is eventually won by **X**.

In dialogical logic validity is defined in relation to winning strategies for the proponent **P**.

- A proposition is valid if **P** has a winning strategy for a thesis stating this proposition
- A *winning strategy for* **P** *for* a thesis *A* is a tree ***S*** the branches of which are plays won by **P**, where the nodes are those moves, such that

1. ***S*** has the move **P** *A* as root node (with depth 0),
2. if the node is an **O**-move (i.e. if the depth of a node is odd), then it has exactly one successor node (which is a **P**-move),
3. if the node is a **P**-move (i.e. if the depth of a node is even), then it has as many successor nodes as there are possible moves for **O** at this position.

Branches are introduced by **O'**s choices such as when she challenges a conjunction or when she defends a disjunction.

##### Finite winning strategies

Winning strategies for quantifier-free formulas are always finite trees, whereas winning strategies for first-order formulas can, in general, be trees of countably infinitely many finite branches (each branch is a play).

For example, if one player states some universal quantifier, then each choice of the adversary triggers a different play. In the following example the thesis is an existential that triggers infinite branches, each of them constituted by a choice of **P**:

| 0. |   | **P**∃x(A(x)⊃∀y A(y)) |   |   |   |
|---|---|---|---|---|---|
| 1. |   | **O** ?∃ |   |   |   |
| 2. | **P**A(t1)⊃∀y A(y) | **P** A(t2)⊃∀y A(y) | **P**A(t3)⊃∀y A(y) | **P**A(t4)⊃∀y A(y) | ... |

Infinite winning strategies for **P** can be avoided by introducing some restriction grounded on the following rationale

- Because of the formal rule, **O'**s optimal move is to always choose a new term when she has the chance to choose, that is, when she challenges a universal or when she defends an existential.
- On the contrary **P**, who will do his best to force O to state the elementary proposition she asked **P** for, will copy **O'**s choices for a term (if **O'**s provided already such a term), when he challenges a universal of **O** or defends an existential.

These lead to the following restrictions:

1. If the depth of a node *n* is even such that **P** stated a universal at *n*, and if among the possible choice for **O** she can choose a new term, then this move counts as the only immediate successor node of *n*.
2. If the depth of a node *n*is odd such that **O** stated an existential at *n*, and if among the possible choices for **O** she can choose a new term, then this move counts as the only immediate successor node of *m,* i.e. the node where **P** launched the attack on *n*.
3. If it is **P** who has the choice, then only one of the plays triggered by the choice will be kept.

The rules for local and global meaning plus the notion of winning strategy mentioned above set the dialogical conception of classical and intuitionistic logic.

Herewith an example of a winning strategy for a thesis valid in classical logic and non-valid in intuitionistic logic

|   |   |
|---|---|
| 0. | **P**∃x(A(x)⊃∀y A(y)) (**P** sets the thesis) |
| 1. | **O** ?∃ (**O** challenges the thesis) |
| 2. | **P** A(t1)⊃∀y A(y) (**P** chooses "t1") |
| 3. | **O** A(t1) (**O** challenges the implication by granting the antecedent) |
| 4. | **P** ∀y A(x) (**P** answers by stating the consequent) |
| 5. | **O** ?t2 (**O** challenges the universal by choosing the new singular term "t2") |
| 6. | **P** A(t2)⊃∀y A(y) (**P** cames back to his response to the challenge launched in move 1 chooses to defend the existential this time with the term "t2") |
| 7 | **O** A(t2) (**O** challenges the implication by granting the antecedent) |
| 8 | **P** A(t2) (**P** ''uses''the last move of the Opponent to respond to the challenge upon the universal in move 5) |

**P** has a winning strategy since the SR 2c allows him to defend twice the challenge on the existential. This further allows him to defend himself in move 8 against the challenge launched by the Opponent in move 5.

Defending twice is not allowed by the intuitionistic rule SR 2i and accordingly, there is no winning strategy for **P**:

|   |   |
|---|---|
| 0. | **P**∃x(A(x)⊃∀y A(y)) (**P** sets the thesis) |
| 1. | **O** ?∃ (**O** challenges the thesis) |
| 2. | **P** A(t1)⊃∀y A(y) (**P** chooses "t1") |
| 3. | **O** A(t1) (**O** challenges the implication by granting the antecedent) |
| 4. | **P** ∀y A(x) (**P** answers by stating the consequent ) |
| 5. | **O** ?t2 (**O** challenges the universal by choosing the new singular term "t2") |

## Further developments

Shahid Rahman (first at Universität des Saarlandes, then at Université de Lille) and collaborators in Saarbrücken and Lille developed dialogical logic in a general framework for the historic and the systematic study of several forms of inferences and non-classical logics such as free logic, (normal and non-normal) modal logic, hybrid logic, first-order modal logic, paraconsistent logic, linear logic, relevance logic, connexive logic, belief revision, argumentation theory and legal reasoning.

Most of these developments are a result of studying the semantic and epistemological consequences of modifying the structural rules and/or of the logical constants. In fact, they show how to implement the *dialogical conception of the structural rules for inference*, such as *weakening* and *contraction*.

Further publications show how to develop *material dialogues* (i.e., dialogues based on fully interpreted languages) that than dialogues restricted to logical validity. This new approach to dialogues with content, called *immanent reasoning*, is one of the results of the dialogical perspective on Per Martin-Löf's constructive type theory. Among the most prominent results of *immanent reasoning* are: the elucidation of the role of dialectics in Aristotle's theory of syllogism, the reconstruction of logic and argumentation within the Arabic tradition, and the formulation of *cooperative dialogues* for legal reasoning and more generally for reasoning by parallelism and analogy.
