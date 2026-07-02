---
title: "Cantor's theorem"
source: https://en.wikipedia.org/wiki/Cantor%27s_theorem
domain: set-theory
license: CC-BY-SA-4.0
tags: set theory, set cardinality, ordinal number, axiom of choice
fetched: 2026-07-02
---

# Cantor's theorem

In mathematical set theory, **Cantor's theorem** is a fundamental result which states that, for any set A , the set of all subsets of $A,$ known as the power set of $A,$ has a strictly greater cardinality than A itself.

For finite sets, Cantor's theorem can be seen to be true by simple enumeration of the number of subsets. Counting the empty set as a subset, a set with n elements has a total of $2^{n}$ subsets, and the theorem holds because $2^{n}>n$ for all non-negative integers.

Much more significant is Cantor's discovery of an argument that is applicable to any set, and shows that the theorem holds for infinite sets also. As a consequence, the cardinality of the real numbers, which is the same as that of the power set of the integers, is strictly larger than the cardinality of the integers; see Cardinality of the continuum for details.

The theorem is named for Georg Cantor, who first stated and proved it at the end of the 19th century. Cantor's theorem had immediate and important consequences for the philosophy of mathematics. For instance, by iteratively taking the power set of an infinite set and applying Cantor's theorem, we obtain an endless hierarchy of infinite cardinals, each strictly larger than the one before it. Consequently, the theorem implies that there is no largest cardinal number (colloquially, "there's no largest infinity").

## Proof

Cantor's argument is elegant and remarkably simple. The complete proof is presented below, with detailed explanations to follow.

**Theorem (Cantor)**—Let f be a map from set A to its power set ${\mathcal {P}}(A)$ . Then $f:A\to {\mathcal {P}}(A)$ is not surjective. As a consequence, $\operatorname {card} (A)<\operatorname {card} ({\mathcal {P}}(A))$ holds for any set A .

Proof

The set $B=\{x\in A\mid x\notin f(x)\}$ exists via the axiom schema of specification, and $B\in {\mathcal {P}}(A)$ because $B\subseteq A$ . Suppose towards a contradiction that f is surjective. Then there exists a $\xi \in A$ such that $f(\xi )=B$ . By the definition of B , we have $\xi \in B$ if and only if $\xi \notin f(\xi )=B$ . Having derived a contradiction by assuming an arbitrary map f is surjective, we conclude that no map from A to ${\mathcal {P}}(A)$ is surjective. However, there exist injections from A to ${\mathcal {P}}(A)$ , for instance $g:x\mapsto \{x\}$ . Consequently, $\operatorname {card} (A)<\operatorname {card} ({\mathcal {P}}(A))$ . $\blacksquare$

By definition of cardinality, we have $\operatorname {card} (X)<\operatorname {card} (Y)$ for any two sets X and Y if and only if there is an injective function but no bijective function from X to Y . It suffices to show that there is no surjection from X to Y . This is the heart of Cantor's theorem: there is no surjective function from any set A to its power set. To establish this, it is enough to show that no function f (that maps elements in A to subsets of A ) can reach every possible subset, i.e., we just need to demonstrate the existence of a subset of A that is not equal to $f(x)$ for any $x\in A$ . Recalling that each $f(x)$ is a subset of A , such a subset is given by the following construction, sometimes called the Cantor diagonal set of f :

$B=\{x\in A\mid x\not \in f(x)\}.$

This means, by definition, that for all $x\in A$ , $x\in B$ if and only if $x\notin f(x)$ . For all x the sets B and $f(x)$ cannot be equal because B was constructed from elements of A whose images under f did not include themselves. For all $x\in A$ either $x\in f(x)$ or $x\notin f(x)$ . If $x\in f(x)$ then $f(x)$ cannot equal B because $x\in f(x)$ by assumption and $x\notin B$ by definition. If $x\notin f(x)$ then $f(x)$ cannot equal B because $x\notin f(x)$ by assumption and $x\in B$ by the definition of B .

Equivalently, and slightly more formally, we have just proved that the existence of $\xi \in A$ such that $f(\xi )=B$ implies the following contradiction:

${\begin{aligned}\xi \in B&\iff \xi \notin f(\xi )&&{\text{(by definition of }}B{\text{)}};\\\xi \in B&\iff \xi \in f(\xi )&&{\text{(by assumption that }}f(\xi )=B{\text{)}}.\\\end{aligned}}$

Therefore, by reductio ad absurdum, the assumption must be false. Thus there is no $\xi \in A$ such that $f(\xi )=B$  ; in other words, B is not in the image of f and f does not map onto every element of the power set of A , i.e., f is not surjective.

Finally, to complete the proof, we need to exhibit an injective function from A to its power set. Finding such a function is trivial: just map x to the singleton set $\{x\}$ . The argument is now complete, and we have established the strict inequality for any set A that $\operatorname {card} (A)<\operatorname {card} ({\mathcal {P}}(A))$ .

Another way to think of the proof is that B , empty or non-empty, is always in the power set of A . For f to be onto, some element of A must map to B . But that leads to a contradiction: no element of B can map to B because that would contradict the criterion of membership in B , thus the element mapping to B must not be an element of B meaning that it satisfies the criterion for membership in B , another contradiction. So the assumption that an element of A maps to B must be false; and f cannot be onto.

Because of the double occurrence of x in the expression " $x\in f(x)$ ", this is a diagonal argument. For a countable (or finite) set, the argument of the proof given above can be illustrated by constructing a table in which

1. each row is labelled by a unique x from $A=\{x_{1},x_{2},\ldots \}$ , in this order. A is assumed to admit a linear order so that such table can be constructed.
2. each column of the table is labelled by a unique y from the power set of A ; the columns are ordered by the argument to f , i.e. the column labels are $f(x_{1}),f(x_{2})$ , ..., in this order.
3. the intersection of each row x and column y records a true/false bit whether $x\in y$ .

Given the order chosen for the row and column labels, the main diagonal D of this table thus records whether $x\in f(x)$ for each $x\in A$ . One such table will be the following: ${\begin{array}{cccccc}&f(x_{1})&f(x_{2})&f(x_{3})&f(x_{4})&\cdots \\\hline x_{1}&{\color {red}T}&T&F&T&\cdots \\x_{2}&T&{\color {red}F}&F&F&\cdots \\x_{3}&F&F&{\color {red}T}&T&\cdots \\x_{4}&F&T&T&{\color {red}T}&\cdots \\\vdots &\vdots &\vdots &\vdots &\vdots &\ddots \end{array}}$ The set B constructed in the previous paragraphs coincides with the row labels for the subset of entries on this main diagonal D (which in above example, coloured red) where the table records that $x\in f(x)$ is false. Each row records the values of the indicator function of the set corresponding to the column. The indicator function of B coincides with the logically negated (swap "true" and "false") entries of the main diagonal. Thus the indicator function of B does not agree with any column in at least one entry. Consequently, no column represents B .

Despite the simplicity of the above proof, it is rather difficult for an automated theorem prover to produce it. The main difficulty lies in an automated discovery of the Cantor diagonal set. Lawrence Paulson noted in 1992 that Otter could not do it, whereas Isabelle could, albeit with a certain amount of direction in terms of tactics that might perhaps be considered cheating.

## When *A* is countably infinite

Let us examine the proof for the specific case when A is countably infinite. Without loss of generality, we may take $A=\mathbb {N} =\{1,2,3,\ldots \}$ , the set of natural numbers.

Suppose that $\mathbb {N}$ is equinumerous with its power set ${\mathcal {P}}(\mathbb {N} )$ . Let us see a sample of what ${\mathcal {P}}(\mathbb {N} )$ looks like:

${\mathcal {P}}(\mathbb {N} )=\{\varnothing ,\{1,2\},\{1,2,3\},\{4\},\{1,5\},\{3,4,6\},\{2,4,6,\dots \},\dots \}.$

Indeed, ${\mathcal {P}}(\mathbb {N} )$ contains infinite subsets of $\mathbb {N}$ , e.g. the set of all positive even numbers $\{2,4,6,\ldots \}=\{2k:k\in \mathbb {N} \}$ , along with the empty set $\varnothing$ .

Now that we have an idea of what the elements of ${\mathcal {P}}(\mathbb {N} )$ are, let us attempt to pair off each element of $\mathbb {N}$ with each element of ${\mathcal {P}}(\mathbb {N} )$ to show that these infinite sets are equinumerous. In other words, we will attempt to pair off each element of $\mathbb {N}$ with an element from the infinite set ${\mathcal {P}}(\mathbb {N} )$ , so that no element from either infinite set remains unpaired. Such an attempt to pair elements would look like this:

$\mathbb {N} {\begin{Bmatrix}1&\longleftrightarrow &\{4,5\}\\2&\longleftrightarrow &\{1,2,3\}\\3&\longleftrightarrow &\{4,5,6\}\\4&\longleftrightarrow &\{1,3,5\}\\\vdots &\vdots &\vdots \end{Bmatrix}}{\mathcal {P}}(\mathbb {N} ).$

Given such a pairing, some natural numbers are paired with subsets that contain the very same number. For instance, in our example the number 2 is paired with the subset {1, 2, 3}, which contains 2 as a member. Let us call such numbers *selfish*. Other natural numbers are paired with subsets that do not contain them. For instance, in our example the number 1 is paired with the subset {4, 5}, which does not contain the number 1. Call these numbers *non-selfish*. Likewise, 3 and 4 are non-selfish.

Using this idea, let us build a special set of natural numbers. This set will provide the contradiction we seek. Let B be the set of *all* non-selfish natural numbers. By definition, the power set ${\mathcal {P}}(\mathbb {N} )$ contains all sets of natural numbers, and so it contains this set B as an element. If the mapping is bijective, B must be paired off with some natural number, say b . However, this causes a problem. If b is in B , then b is selfish because it is in the corresponding set, which contradicts the definition of B . If b is not in B , then it is non-selfish and it should instead be a member of B . Therefore, no such element b which maps to B can exist.

Since there is no natural number which can be paired with B , we have contradicted our original supposition, that there is a bijection between $\mathbb {N}$ and ${\mathcal {P}}(\mathbb {N} )$ .

Note that the set B may be empty. This would mean that every natural number x maps to a subset of natural numbers that contains x . Then, every number maps to a nonempty set and no number maps to the empty set. But the empty set is a member of ${\mathcal {P}}(\mathbb {N} )$ , so the mapping still does not cover ${\mathcal {P}}(\mathbb {N} )$ .

Through this proof by contradiction we have proven that the cardinality of $\mathbb {N}$ and ${\mathcal {P}}(\mathbb {N} )$ cannot be equal. We also know that the cardinality of ${\mathcal {P}}(\mathbb {N} )$ cannot be less than the cardinality of $\mathbb {N}$ because ${\mathcal {P}}(\mathbb {N} )$ contains all singletons, by definition, and these singletons form a "copy" of $\mathbb {N}$ inside of ${\mathcal {P}}(\mathbb {N} )$ . Therefore, only one possibility remains, and that is that the cardinality of ${\mathcal {P}}(\mathbb {N} )$ is strictly greater than the cardinality of $\mathbb {N}$ , proving Cantor's theorem.

Cantor's theorem and its proof are closely related to two paradoxes of set theory.

Cantor's paradox is the name given to a contradiction following from Cantor's theorem together with the assumption that there is a set containing all sets, the universal set V . By Cantor's theorem $|{\mathcal {P}}(X)|>|X|$ for any set X . On the other hand, all elements of ${\mathcal {P}}(V)$ are sets, and thus contained in V , therefore $|{\mathcal {P}}(V)|\leq |V|$ .

Another paradox can be derived from the proof of Cantor's theorem by instantiating the function *f* with the identity function; this turns Cantor's diagonal set into what is sometimes called the *Russell set* of a given set *A*:

$R_{A}=\left\{\,x\in A:x\not \in x\,\right\}.$

The proof of Cantor's theorem is straightforwardly adapted to show that assuming a set of all sets *U* exists, then considering its Russell set *R**U* leads to the contradiction:

$R_{U}\in R_{U}\iff R_{U}\notin R_{U}.$

This argument is known as Russell's paradox. As a point of subtlety, the version of Russell's paradox we have presented here is actually a theorem of Zermelo; we can conclude from the contradiction obtained that we must reject the hypothesis that *R**U*∈*U*, thus disproving the existence of a set containing all sets. This was possible because we have used restricted comprehension (as featured in ZFC) in the definition of *R**A* above, which in turn entailed that

$R_{U}\in R_{U}\iff (R_{U}\in U\wedge R_{U}\notin R_{U}).$

Had we used unrestricted comprehension (as in Frege's system for instance) by defining the Russell set simply as $R=\left\{\,x:x\not \in x\,\right\}$ , then the axiom system itself would have entailed the contradiction, with no further hypotheses needed.

Despite the syntactical similarities between the Russell set (in either variant) and the Cantor diagonal set, Alonzo Church emphasized that Russell's paradox is independent of considerations of cardinality and its underlying notions like one-to-one correspondence.

## History

Cantor gave essentially this proof in a paper published in 1891 "Über eine elementare Frage der Mannigfaltigkeitslehre", where the diagonal argument for the uncountability of the reals also first appears (he had earlier proved the uncountability of the reals by other methods). The version of this argument he gave in that paper was phrased in terms of indicator functions on a set rather than subsets of a set. He showed that if *f* is a function defined on *X* whose values are 2-valued functions on *X*, then the 2-valued function *G*(*x*) = 1 − *f*(*x*)(*x*) is not in the range of *f*.

Bertrand Russell has a very similar proof in *Principles of Mathematics* (1903, section 348), where he shows that there are more propositional functions than objects. "For suppose a correlation of all objects and some propositional functions to have been affected, and let phi-*x* be the correlate of *x*. Then "not-phi-*x*(*x*)," i.e. "phi-*x* does not hold of *x*" is a propositional function not contained in this correlation; for it is true or false of *x* according as phi-*x* is false or true of *x*, and therefore it differs from phi-*x* for every value of *x*." He attributes the idea behind the proof to Cantor.

Ernst Zermelo has a theorem (which he calls "Cantor's Theorem") that is identical to the form above in the paper that became the foundation of modern set theory ("Untersuchungen über die Grundlagen der Mengenlehre I"), published in 1908. See Zermelo set theory.

## Generalizations

Lawvere's fixed-point theorem provides for a broad generalization of Cantor's theorem to any category with finite products in the following way: let ${\mathcal {C}}$ be such a category, and let 1 be a terminal object in ${\mathcal {C}}$ . Suppose that Y is an object in ${\mathcal {C}}$ and that there exists an endomorphism $\alpha :Y\to Y$ that does not have any fixed points; that is, there is no morphism $y:1\to Y$ that satisfies $\alpha \circ y=y$ . Then there is no object T of ${\mathcal {C}}$ such that a morphism $f:T\times T\to Y$ can parameterize all morphisms $T\to Y$ . In other words, for every object T and every morphism $f:T\times T\to Y$ , an attempt to write maps $T\to Y$ as maps of the form $f(-,x):T\to Y$ must leave out at least one map $T\to Y$ .
