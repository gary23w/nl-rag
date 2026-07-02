---
title: "True quantified Boolean formula"
source: https://en.wikipedia.org/wiki/True_quantified_Boolean_formula
domain: polynomial-hierarchy
license: CC-BY-SA-4.0
tags: polynomial hierarchy, oracle machine, quantified boolean formula, sigma level
fetched: 2026-07-02
---

# True quantified Boolean formula

In computational complexity theory, the language **TQBF** is a formal language consisting of the **true quantified Boolean formulas**. A (fully) quantified Boolean formula is a formula in quantified propositional logic (also known as Second-order propositional logic) where every variable is quantified (or bound), using either existential or universal quantifiers, at the beginning of the sentence. Such a formula is equivalent to either true or false (since there are no free variables). If such a formula evaluates to true, then that formula is in the language TQBF. It is also known as **QSAT** (Quantified SAT).

## Overview

In computational complexity theory, the **quantified Boolean formula problem** (**QBF**) is a generalization of the Boolean satisfiability problem in which both existential quantifiers and universal quantifiers can be applied to each variable. Put another way, it asks whether a quantified sentential form over a set of Boolean variables is true or false. For example, the following is an instance of QBF:

$\forall x\ \exists y\ \exists z\ ((x\lor z)\land y)$

QBF is the canonical complete problem for PSPACE, the class of problems solvable by a deterministic or nondeterministic Turing machine in polynomial space and unlimited time. Given the formula in the form of an abstract syntax tree, the problem can be solved easily by a set of mutually recursive procedures which evaluate the formula. Such an algorithm uses space proportional to the height of the tree, which is linear in the worst case, but uses time exponential in the number of quantifiers.

Provided that MA ⊊ PSPACE, which is widely believed, QBF cannot be solved, nor can a given solution even be verified, in either deterministic or probabilistic polynomial time (in fact, unlike the satisfiability problem, there's no known way to specify a solution succinctly). It can be solved using an alternating Turing machine in linear time, since AP = PSPACE, where AP is the class of problems alternating machines can solve in polynomial time.

When the seminal result IP = PSPACE was shown (see interactive proof system), it was done by exhibiting an interactive proof system that could solve QBF by solving a particular arithmetization of the problem.

QBF formulas have a number of useful canonical forms. For example, it can be shown that there is a polynomial-time many-one reduction that will move all quantifiers to the front of the formula and make them alternate between universal and existential quantifiers. There is another reduction that proved useful in the IP = PSPACE proof where no more than one universal quantifier is placed between each variable's use and the quantifier binding that variable. This was critical in limiting the number of products in certain subexpressions of the arithmetization.

## Prenex normal form

A fully quantified Boolean formula can be assumed to have a very specific form, called prenex normal form. It has two basic parts: a portion containing only quantifiers and a portion containing an unquantified Boolean formula usually denoted as $\displaystyle \phi$ . If there are $\displaystyle n$ Boolean variables, the entire formula can be written as

$\displaystyle \exists x_{1}\forall x_{2}\exists x_{3}\cdots Q_{n}x_{n}\phi (x_{1},x_{2},x_{3},\dots ,x_{n})$

where every variable falls within the scope of some quantifier. By introducing dummy variables, any formula in prenex normal form can be converted into a sentence where existential and universal quantifiers alternate. Using the dummy variable $\displaystyle y_{1}$ ,

$\displaystyle \exists x_{1}\exists x_{2}\phi (x_{1},x_{2})\quad \mapsto \quad \exists x_{1}\forall y_{1}\exists x_{2}\phi (x_{1},x_{2})$

The second sentence has the same truth value but follows the restricted syntax. Assuming fully quantified Boolean formulas to be in prenex normal form is a frequent feature of proofs.

## QBF solvers

### Naive

There is a simple recursive algorithm for determining whether a QBF is in TQBF (i.e. is true). Given some QBF

$Q_{1}x_{1}Q_{2}x_{2}\cdots Q_{n}x_{n}\phi (x_{1},x_{2},\dots ,x_{n}).$

If the formula contains no quantifiers, we can just return the formula. Otherwise, we take off the first quantifier and check both possible values for the first variable:

$A=Q_{2}x_{2}\cdots Q_{n}x_{n}\phi (0,x_{2},\dots ,x_{n}),$

$B=Q_{2}x_{2}\cdots Q_{n}x_{n}\phi (1,x_{2},\dots ,x_{n}).$

If $Q_{1}=\exists$ , then return $A\lor B$ . If $Q_{1}=\forall$ , then return $A\land B$ .

How fast does this algorithm run? For every quantifier in the initial QBF, the algorithm makes two recursive calls on only a linearly smaller subproblem. This gives the algorithm an exponential runtime O(2*n*).

How much space does this algorithm use? Within each invocation of the algorithm, it needs to store the intermediate results of computing A and B. Every recursive call takes off one quantifier, so the total recursive depth is linear in the number of quantifiers. Formulas that lack quantifiers can be evaluated in space logarithmic in the number of variables. The initial QBF was fully quantified, so there are at least as many quantifiers as variables. Thus, this algorithm uses *O*(*n* + log *n*) = *O*(*n*) space. This makes the TQBF language part of the PSPACE complexity class.

### State of the art

Despite the PSPACE-completeness of QBF, many solvers have been developed to solve these instances (This is analogous to the situation with SAT, the single existential quantifier version; even though it is NP-complete, it is still possible to solve many SAT instances heuristically). The case where there are only 2 quantifiers, known as 2QBF, has received special attention.

The QBF solver competition QBFEVAL has been running more-or-less annually since 2004; solvers are required to read instances in QDIMACS format and either the QCIR or QAIGER formats. High-performing QBF solvers generally use QDPLL (a generalization of DPLL) or CEGAR. Research into QBF solving began with the development of backtracking DPLL for QBF in 1998, followed by the introduction of clause learning and variable elimination in 2002; thus, as compared to SAT solving, which has been under development since the 1960s, QBF is a relatively young field of research as of 2017.

Some prominent QBF solvers include:

- CADET, which solves quantified Boolean formulas restricted to one quantifier alternation (with the ability to compute Skolem functions), based on *incremental determinization* and with the ability to prove its answers.
- CAQE - a CEGAR-based solver for quantified Boolean formulas; winner of the recent editions of QBFEVAL as of 2021.
- DepQBF - a search-based solver for quantified Boolean formulas
- sKizzo - the first solver ever to use symbolic skolemization, extract certificates of satisfiability, use a hybrid inference engine, implement abstract branching, deal with limited quantifiers, and enumerate valid assignments, and winner of QBFEVAL 2005, 2006, and 2007.

## Applications

QBF solvers can be applied to planning (in artificial intelligence), including safe planning; the latter is critical in applications of robotics. QBF solvers can also be applied to bounded model checking as they provide a shorter encoding than would be needed for a SAT-based solver.

The evaluation of a QBF can be seen as a two-player game between a player who controls existentially quantified variables and a player who controls universally quantified variables. This makes QBFs suitable for encoding reactive synthesis problems. Similarly, QBF solvers can be used to model adversarial games in game theory. For example, QBF solvers can be used to find winning strategies for games of geography, which can then be automatically played interactively.

QBF solvers can be used for formal equivalence checking, and can also be used to synthesize Boolean functions.

Other types of problems that can be encoded as QBFs include:

- Detecting whether a clause in an unsatisfiable formula in conjunctive normal form belongs to some minimally unsatisfiable subset and whether a clause in a satisfiable formula belongs to a maximally satisfiable subset
- Encodings of conformant planning
- ASP-related problems
- Abstract argumentation
- Linear temporal logic model checking
- Nondeterministic finite automaton language inclusion
- Synthesis and reliability of distributed systems

## Extensions

The Stochastic Satisfiability problem (known as SSAT) is an extension of TQBF that adds a randomizing R quantifier, views universal quantification as minimization, and existential quantification as maximization, and asks, whether the probability represented by the formula exceeds a given threshold.

QBF can be also extended to have Henkin quantifiers.

## PSPACE-completeness

The TQBF language serves in complexity theory as the canonical PSPACE-complete problem. Being PSPACE-complete means that a language is in PSPACE and that the language is also PSPACE-hard. The algorithm above shows that TQBF is in PSPACE. Showing that TQBF is PSPACE-hard requires showing that any language in the complexity class PSPACE can be reduced to TQBF in polynomial time. I.e.,

$\forall L\in {\mathsf {PSPACE}},L\leq _{p}\mathrm {TQBF} .$

This means that, for a PSPACE language L, whether an input x is in L can be decided by checking whether $f(x)$ is in TQBF, for some function f that is required to run in polynomial time (relative to the length of the input). Symbolically,

$x\in L\iff f(x)\in \mathrm {TQBF} .$

Proving that TQBF is PSPACE-hard, requires specification of f.

So, suppose that L is a PSPACE language. This means that L can be decided by a polynomial space deterministic Turing machine (DTM). This is very important for the reduction of L to TQBF, because the configurations of any such Turing Machine can be represented as Boolean formulas, with Boolean variables representing the state of the machine as well as the contents of each cell on the Turing Machine tape, with the position of the Turing Machine head encoded in the formula by the formula's ordering. In particular, our reduction will use the variables $c_{1}$ and $c_{2}$ , which represent two possible configurations of the DTM for L, and a natural number t, in constructing a QBF $\phi _{c_{1},c_{2},t}$ which is true if and only if the DTM for L can go from the configuration encoded in $c_{1}$ to the configuration encoded in $c_{2}$ in no more than t steps. The function f, then, will construct from the DTM for L a QBF $\phi _{c_{\text{start}},c_{\text{accept}},T}$ , where $c_{start}$ is the DTM's starting configuration, $c_{\text{accept}}$ is the DTM's accepting configuration, and T is the maximum number of steps the DTM could need to move from one configuration to the other. We know that *T* = *O*(exp(*n*k)) for some *k*, where *n* is the length of the input, because this bounds the total number of possible configurations of the relevant DTM. Of course, it cannot take the DTM more steps than there are possible configurations to reach $c_{\mathrm {accept} }$ unless it enters a loop, in which case it will never reach $c_{\mathrm {accept} }$ anyway.

At this stage of the proof, we have already reduced the question of whether an input formula w (encoded, of course, in $c_{\text{start}}$ ) is in L to the question of whether the QBF $\phi _{c_{\text{start}},c_{\text{accept}},T}$ , i.e., $f(w)$ , is in TQBF. The remainder of this proof proves that f can be computed in polynomial time.

For $t=1$ , computation of $\phi _{c_{1},c_{2},t}$ is straightforward—either one of the configurations changes to the other in one step or it does not. Since the Turing Machine that our formula represents is deterministic, this presents no problem.

For $t>1$ , computation of $\phi _{c_{1},c_{2},t}$ involves a recursive evaluation, looking for a so-called "middle point" $m_{1}$ . In this case, we rewrite the formula as follows:

$\phi _{c_{1},c_{2},t}=\exists m_{1}(\phi _{c_{1},m_{1},\lceil t/2\rceil }\wedge \phi _{m_{1},c_{2},\lceil t/2\rceil }).$

This converts the question of whether $c_{1}$ can reach $c_{2}$ in t steps to the question of whether $c_{1}$ reaches a middle point $m_{1}$ in $t/2$ steps, which itself reaches $c_{2}$ in $t/2$ steps. The answer to the latter question of course gives the answer to the former.

Now, t is only bounded by T, which is exponential (and so not polynomial) in the length of the input. Additionally, each recursive layer virtually doubles the length of the formula. (The variable $m_{1}$ is only one midpoint—for greater t, there are more stops along the way, so to speak.) So the time required to recursively evaluate $\phi _{c_{1},c_{2},t}$ in this manner could be exponential as well, simply because the formula could become exponentially large. This problem is solved by universally quantifying using variables $c_{3}$ and $c_{4}$ over the configuration pairs (e.g., $\{(c_{1},m_{1}),(m_{1},c_{2})\}$ ), which prevents the length of the formula from expanding due to recursive layers. This yields the following interpretation of $\phi _{c_{1},c_{2},t}$ :

$\phi _{c_{1},c_{2},t}=\exists m_{1}\forall (c_{3},c_{4})\in \{(c_{1},m_{1}),(m_{1},c_{2})\}(\phi _{c_{3},c_{4},\lceil t/2\rceil }).$

This version of the formula can indeed be computed in polynomial time, since any one instance of it can be computed in polynomial time. The universally quantified ordered pair simply tells us that whichever choice of $(c_{3},c_{4})$ is made, $\phi _{c_{1},c_{2},t}\iff \phi _{c_{3},c_{4},\lceil t/2\rceil }$ .

Thus, $\forall L\in {\mathsf {PSPACE}},L\leq _{p}\mathrm {TQBF}$ , so TQBF is PSPACE-hard. Together with the above result that TQBF is in PSPACE, this completes the proof that TQBF is a PSPACE-complete language.

(This proof follows Sipser 2006 pp. 310–313 in all essentials. Papadimitriou 1994 also includes a proof.)

This construction can be run in logspace, meaning that TQBF is PSPACE-complete in he sense of logspace many-one reduction.

## Miscellany

- One important subproblem in TQBF is the Boolean satisfiability problem. In this problem, you wish to know whether a given Boolean formula $\phi$ can be made true with some assignment of variables. This is equivalent to the TQBF using only existential quantifiers: $\exists x_{1}\cdots \exists x_{n}\phi (x_{1},\ldots ,x_{n})$ This is also an example of the larger result NP ⊆ PSPACE which follows directly from the observation that a polynomial time verifier for a proof of a language accepted by a NTM (Non-deterministic Turing machine) requires polynomial space to store the proof.
- Any class in the polynomial hierarchy (PH) has TQBF as a hard problem. In other words, for the class comprising all languages L for which there exists a poly-time TM V, a verifier, such that for all input x and some constant i, $x\in L\Leftrightarrow \exists y_{1}\forall y_{2}\cdots Q_{i}y_{i}\ V(x,y_{1},y_{2},\dots ,y_{i})\ =\ 1$ which has a specific QBF formulation that is given as $\exists \phi$ such that $\exists {\vec {x_{1}}}\forall {\vec {x_{2}}}\cdots Q_{i}{\vec {x_{i}}}\ \phi ({\vec {x_{1}}},{\vec {x_{2}}},\dots ,{\vec {x_{i}}})\ =\ 1$ where the ${\vec {x_{i}}}$ 's are vectors of Boolean variables.
- It is important to note that while TQBF the language is defined as the collection of true quantified Boolean formulas, the abbreviation TQBF is often used (even in this article) to stand for a totally quantified Boolean formula, often simply called a QBF (quantified Boolean formula, understood as "fully" or "totally" quantified). It is important to distinguish contextually between the two uses of the abbreviation TQBF in reading the literature.
- A TQBF can be thought of as a game played between two players, with alternating moves. Existentially quantified variables are equivalent to the notion that a move is available to a player at a turn. Universally quantified variables mean that the outcome of the game does not depend on what move a player makes at that turn. Also, a TQBF whose first quantifier is existential corresponds to a formula game in which the first player has a winning strategy.
- A TQBF for which the quantified formula is in 2-CNF may be solved in linear time, by an algorithm involving strong connectivity analysis of its implication graph. The 2-satisfiability problem is a special case of TQBF for these formulas, in which every quantifier is existential.
- There is a systematic treatment of restricted versions of quantified Boolean formulas (giving Schaefer-type classifications) provided in an expository paper by Hubie Chen.
- Planar TQBF, generalizing Planar SAT, was proved PSPACE-complete by D. Lichtenstein.

## Notes and references

1. *M. Garey & D. Johnson (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman, San Francisco, California. ISBN 0-7167-1045-5.*
2. *A. Chandra, D. Kozen, and L. Stockmeyer (1981). "Alternation". *Journal of the ACM*. **28** (1): 114–133. doi:10.1145/322234.322243. S2CID 238863413.*
3. *Adi Shamir (1992). "Ip = Pspace". *Journal of the ACM*. **39** (4): 869–877. doi:10.1145/146585.146609. S2CID 315182.*
4. *Arora, Sanjeev; Barak, Boaz (2009), "Space complexity", *Computational Complexity*, Cambridge: Cambridge University Press, pp. 78–94, doi:10.1017/cbo9780511804090.007, ISBN 978-0-511-80409-0, S2CID 262800930, retrieved 2021-05-26*
5. *"QBFEVAL Home Page". *www.qbflib.org*. Retrieved 2021-02-13.*
6. *"QBF Solvers | Beyond NP". *beyondnp.org*. Retrieved 2021-02-13.*
7. *Balabanov, Valeriy; Roland Jiang, Jie-Hong; Scholl, Christoph; Mishchenko, Alan; K. Brayton, Robert (2016). "2QBF: Challenges and Solutions" (PDF). *International Conference on Theory and Applications of Satisfiability Testing*: 453–459. Archived (PDF) from the original on 13 February 2021 – via SpringerLink.*
8. *"QBFEVAL'20". *www.qbflib.org*. Retrieved 2021-05-29.*
9. *Lonsing, Florian (December 2017). "An Introduction to QBF Solving" (PDF). *www.florianlonsing.com*. Retrieved 29 May 2021.*
10. *Rabe, Markus N. (2021-04-15), *MarkusRabe/cadet*, retrieved 2021-05-06*
11. *Tentrup, Leander (2021-05-06), *ltentrup/caqe*, retrieved 2021-05-06*
12. *"DepQBF Solver". *lonsing.github.io*. Retrieved 2021-05-06.*
13. *"sKizzo - a QBF solver". *www.skizzo.site*. Retrieved 2021-05-06.*
14. *Shukla, Ankit; Biere, Armin; Seidl, Martina; Pulina, Luca (2019). *A Survey on Applications of Quantified Boolean Formulas* (PDF). 2019 IEEE 31st International Conference on Tools for Artificial Intelligence. pp. 78–84. doi:10.1109/ICTAI.2019.00020. Retrieved 29 May 2021.*
15. *Shen, Zhihe. *Using QBF Solvers to Solve Games and Puzzles* (PDF) (Thesis). Boston College.*
16. *Janota, Mikoláš; Marques-Silva, Joao (2011). *On Deciding MUS Membership with QBF*. Principles and Practice of Constraint Programming – CP 2011. Vol. 6876. pp. 414–428. doi:10.1007/978-3-642-23786-7_32. ISBN 978-3-642-23786-7.*
17. Christor Papadimitriou. Games Against Nature, Journal for Computer and system Sciences 31, pages 288-301, 1985.
18. *"CS 221: Computational Complexity" (PDF). Archived from the original (PDF) on 2010-07-20.*
19. *Krom, Melven R. (1967). "The Decision Problem for a Class of First-Order Formulas in Which all Disjunctions are Binary". *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*. **13** (1–2): 15–20. doi:10.1002/malq.19670130104.*.
20. *Aspvall, Bengt; Plass, Michael F.; Tarjan, Robert E. (1979). "A linear-time algorithm for testing the truth of certain quantified boolean formulas" (PDF). *Information Processing Letters*. **8** (3): 121–123. doi:10.1016/0020-0190(79)90002-4.*.
21. *Chen, Hubie (December 2009). "A Rendezvous of Logic, Complexity, and Algebra". *ACM Computing Surveys*. **42** (1). ACM: 1–32. arXiv:cs/0611018. doi:10.1145/1592451.1592453. S2CID 11975818.*
22. *Lichtenstein, David (1982-05-01). "Planar Formulae and Their Uses". *SIAM Journal on Computing*. **11** (2): 329–343. doi:10.1137/0211025. ISSN 0097-5397. S2CID 207051487.*

- Fortnow & Homer (2003) provides some historical background for PSPACE and TQBF.
- Zhang (2003) provides some historical background of Boolean formulas.
- Arora, Sanjeev. (2001). *COS 522: Computational Complexity*. Lecture Notes, Princeton University. Retrieved October 10, 2005.
- Fortnow, Lance & Steve Homer. (2003, June). A short history of computational complexity. *Bulletin of the European Association for Theoretical Computer Science*, The Computational Complexity Column, 80. Retrieved May 14, 2024.
- Papadimitriou, C. H. (1994). *Computational Complexity.* Reading: Addison-Wesley.
- Sipser, Michael. (2006). *Introduction to the Theory of Computation.* Boston: Thomson Course Technology.
- Zhang, Lintao. (2003). *Searching for truth: Techniques for satisfiability of Boolean formulas*. Retrieved October 10, 2005.
