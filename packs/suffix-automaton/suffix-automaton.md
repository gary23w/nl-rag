---
title: "Suffix automaton"
source: https://en.wikipedia.org/wiki/Suffix_automaton
domain: suffix-automaton
license: CC-BY-SA-4.0
tags: suffix automaton, directed acyclic word graph, substring recognition, minimal automaton
fetched: 2026-07-02
---

# Suffix automaton

In computer science, a **suffix automaton** is an efficient data structure for representing the substring index of a given string which allows the storage, processing, and retrieval of compressed information about all its substrings. The suffix automaton of a string S is the smallest directed acyclic graph with a dedicated initial vertex and a set of "final" vertices, such that paths from the initial vertex to final vertices represent the suffixes of the string.

In terms of automata theory, a suffix automaton is the minimal partial deterministic finite automaton that recognizes the set of suffixes of a given string $S=s_{1}s_{2}\dots s_{n}$ . The state graph of a suffix automaton is called a directed acyclic word graph (DAWG), a term that is also sometimes used for any deterministic acyclic finite state automaton.

Suffix automata were introduced in 1983 by a group of scientists from the University of Denver and the University of Colorado Boulder. They suggested a linear time online algorithm for its construction and showed that the suffix automaton of a string S having length at least two characters has at most ${\textstyle 2|S|-1}$ states and at most ${\textstyle 3|S|-4}$ transitions. Further works have shown a close connection between suffix automata and suffix trees, and have outlined several generalizations of suffix automata, such as compacted suffix automaton obtained by compression of nodes with a single outgoing arc.

Suffix automata provide efficient solutions to problems such as substring search and computation of the largest common substring of two and more strings.

## History

The concept of suffix automaton was introduced in 1983 by a group of scientists from University of Denver and University of Colorado Boulder consisting of Anselm Blumer, Janet Blumer, Andrzej Ehrenfeucht, David Haussler and Ross McConnell, although similar concepts had earlier been studied alongside suffix trees in the works of Peter Weiner, Vaughan Pratt and Anatol Slissenko. In their initial work, Blumer *et al*. showed a suffix automaton built for the string S of length greater than 1 has at most $2|S|-1$ states and at most $3|S|-4$ transitions, and suggested a linear algorithm for automaton construction.

In 1983, Mu-Tian Chen and Joel Seiferas independently showed that Weiner's 1973 suffix-tree construction algorithm while building a suffix tree of the string S constructs a suffix automaton of the reversed string ${\textstyle S^{R}}$ as an auxiliary structure. In 1987, Blumer *et al*. applied the compressing technique used in suffix trees to a suffix automaton and invented the compacted suffix automaton, which is also called the compacted directed acyclic word graph (CDAWG). In 1997, Maxime Crochemore and Renaud Vérin developed a linear algorithm for direct CDAWG construction. In 2001, Shunsuke Inenaga *et al*. developed an algorithm for construction of CDAWG for a set of words given by a trie.

## Definitions

Usually when speaking about suffix automata and related concepts, some notions from formal language theory and automata theory are used, in particular:

- "Alphabet" is a finite set $\Sigma$ that is used to construct words. Its elements are called "characters";
- "Word" is a finite sequence of characters $\omega =\omega _{1}\omega _{2}\dots \omega _{n}$ . "Length" of the word $\omega$ is denoted as $|\omega |=n$ ;
- "Formal language" is a set of words over given alphabet;
- "Language of all words" is denoted as $\Sigma ^{*}$ (where the "*" character stands for Kleene star), "empty word" (the word of zero length) is denoted by the character $\varepsilon$ ;
- "Concatenation of words" $\alpha =\alpha _{1}\alpha _{2}\dots \alpha _{n}$ and $\beta =\beta _{1}\beta _{2}\dots \beta _{m}$ is denoted as $\alpha \cdot \beta$ or $\alpha \beta$ and corresponds to the word obtained by writing $\beta$ to the right of $\alpha$ , that is, $\alpha \beta =\alpha _{1}\alpha _{2}\dots \alpha _{n}\beta _{1}\beta _{2}\dots \beta _{m}$ ;
- "Concatenation of languages" A and B is denoted as $A\cdot B$ or $AB$ and corresponds to the set of pairwise concatenations $AB=\{\alpha \beta :\alpha \in A,\beta \in B\}$ ;
- If the word $\omega \in \Sigma ^{*}$ may be represented as $\omega =\alpha \gamma \beta$ , where $\alpha ,\beta ,\gamma \in \Sigma ^{*}$ , then words $\alpha$ , $\beta$ and $\gamma$ are called "prefix", "suffix" and "subword" (substring) of the word $\omega$ correspondingly;
- If $T=T_{1}\dots T_{n}$ and $T_{l}T_{l+1}\dots T_{r}=S$ (with $1\leq l\leq r\leq n$ ) then S is said to "occur" in T as a subword. Here l and r are called left and right positions of occurrence of S in T correspondingly.

## Automaton structure

Formally, deterministic finite automaton is determined by 5-tuple ${\mathcal {A}}=(\Sigma ,Q,q_{0},F,\delta )$ , where:

- $\Sigma$ is an "alphabet" that is used to construct words,
- Q is a set of automaton "states",
- $q_{0}\in Q$ is an "initial" state of automaton,
- $F\subset Q$ is a set of "final" states of automaton,
- $\delta :Q\times \Sigma \mapsto Q$ is a partial "transition" function of automaton, such that $\delta (q,\sigma )$ for $q\in Q$ and $\sigma \in \Sigma$ is either undefined or defines a transition from q over character $\sigma$ .

Most commonly, deterministic finite automaton is represented as a directed graph ("diagram") such that:

- Set of graph vertices corresponds to the state of states Q ,
- Graph has a specific marked vertex corresponding to initial state $q_{0}$ ,
- Graph has several marked vertices corresponding to the set of final states F ,
- Set of graph arcs corresponds to the set of transitions $\delta$ ,
- Specifically, every transition ${\textstyle \delta (q_{1},\sigma )=q_{2}}$ is represented by an arc from $q_{1}$ to $q_{2}$ marked with the character $\sigma$ . This transition also may be denoted as ${\textstyle q_{1}{\begin{smallmatrix}{\sigma }\\[-5pt]{\longrightarrow }\end{smallmatrix}}q_{2}}$ .

In terms of its diagram, the automaton recognizes the word $\omega =\omega _{1}\omega _{2}\dots \omega _{m}$ only if there is a path from the initial vertex $q_{0}$ to some final vertex $q\in F$ such that concatenation of characters on this path forms $\omega$ . The set of words recognized by an automaton forms a language that is set to be recognized by the automaton. In these terms, the language recognized by a suffix automaton of S is the language of its (possibly empty) suffixes.

### Automaton states

"Right context" of the word $\omega$ with respect to language L is a set $[\omega ]_{R}=\{\alpha :\omega \alpha \in L\}$ that is a set of words $\alpha$ such that their concatenation with $\omega$ forms a word from L . Right contexts induce a natural equivalence relation $[\alpha ]_{R}=[\beta ]_{R}$ on the set of all words. If language L is recognized by some deterministic finite automaton, there exists unique up to isomorphism automaton that recognizes the same language and has the minimum possible number of states. Such an automaton is called a minimal automaton for the given language L . Myhill–Nerode theorem allows it to define it explicitly in terms of right contexts:

**Theorem**—Minimal automaton recognizing language L over the alphabet $\Sigma$ may be explicitly defined in the following way:

- Alphabet $\Sigma$ stays the same,
- States Q correspond to right contexts $[\omega ]_{R}$ of all possible words $\omega \in \Sigma ^{*}$ ,
- Initial state $q_{0}$ corresponds to the right context of the empty word $[\varepsilon ]_{R}$ ,
- Final states F correspond to right contexts $[\omega ]_{R}$ of words from $\omega \in L$ ,
- Transitions $\delta$ are given by $[\omega ]_{R}{\begin{smallmatrix}{\sigma }\\[-5pt]{\longrightarrow }\end{smallmatrix}}[\omega \sigma ]_{R}$ , where $\omega \in \Sigma ^{*}$ and $\sigma \in \Sigma$ .

In these terms, a "suffix automaton" is the minimal deterministic finite automaton recognizing the language of suffixes of the word $S=s_{1}s_{2}\dots s_{n}$ . The right context of the word $\omega$ with respect to this language consists of words $\alpha$ , such that $\omega \alpha$ is a suffix of S . It allows to formulate the following lemma defining a bijection between the right context of the word and the set of right positions of its occurrences in S :

**Theorem**—Let $endpos(\omega )=\{r:\omega =s_{l}\dots s_{r}\}$ be the set of right positions of occurrences of $\omega$ in S .

There is a following bijection between $endpos(\omega )$ and $[\omega ]_{R}$ :

- If $x\in endpos(\omega )$ , then $s_{x+1}s_{x+2}\dots s_{n}\in [\omega ]_{R}$ ;
- If $\alpha \in [\omega ]_{R}$ , then $n-\vert \alpha \vert \in endpos(\omega )$ .

For example, for the word $S=abacaba$ and its subword $\omega =ab$ , it holds $endpos(ab)=\{2,6\}$ and $[ab]_{R}=\{a,acaba\}$ . Informally, $[ab]_{R}$ is formed by words that follow occurrences of $ab$ to the end of S and $endpos(ab)$ is formed by right positions of those occurrences. In this example, the element $x=2\in endpos(ab)$ corresponds with the word $s_{3}s_{4}s_{5}s_{6}s_{7}=acaba\in [ab]_{R}$ while the word $a\in [ab]_{R}$ corresponds with the element $7-|a|=6\in endpos(ab)$ .

It implies several structure properties of suffix automaton states. Let $|\alpha |\leq |\beta |$ , then:

- If $[\alpha ]_{R}$ and $[\beta ]_{R}$ have at least one common element x , then $endpos(\alpha )$ and $endpos(\beta )$ have a common element as well. It implies $\alpha$ is a suffix of $\beta$ and therefore $endpos(\beta )\subset endpos(\alpha )$ and $[\beta ]_{R}\subset [\alpha ]_{R}$ . In aforementioned example, $a\in [ab]_{R}\cap [cab]_{R}$ , so $ab$ is a suffix of $cab$ and thus $[cab]_{R}=\{a\}\subset \{a,acaba\}=[ab]_{R}$ and $endpos(cab)=\{6\}\subset \{2,6\}=endpos(ab)$ ;
- If $[\alpha ]_{R}=[\beta ]_{R}$ , then $endpos(\alpha )=endpos(\beta )$ , thus $\alpha$ occurs in S only as a suffix of $\beta$ . For example, for $\alpha =b$ and $\beta =ab$ it holds that $[b]_{R}=[ab]_{R}=\{a,acaba\}$ and $endpos(b)=endpos(ab)=\{2,6\}$ ;
- If $[\alpha ]_{R}=[\beta ]_{R}$ and $\gamma$ is a suffix of $\beta$ such that $|\alpha |\leq |\gamma |\leq |\beta |$ , then $[\alpha ]_{R}=[\gamma ]_{R}=[\beta ]_{R}$ . In the example above $[c]_{R}=[bac]_{R}=\{aba\}$ and it holds for "intermediate" suffix $\gamma =ac$ that $[ac]_{R}=\{aba\}$ .

Any state $q=[\alpha ]_{R}$ of the suffix automaton recognizes some continuous chain of nested suffixes of the longest word recognized by this state.

"Left extension" ${\overset {\scriptstyle {\leftarrow }}{\gamma }}$ of the string $\gamma$ is the longest string $\omega$ that has the same right context as $\gamma$ . Length $|{\overset {\scriptstyle {\leftarrow }}{\gamma }}|$ of the longest string recognized by $q=[\gamma ]_{R}$ is denoted by $len(q)$ . It holds:

**Theorem**—Left extension of $\gamma$ may be represented as ${\overleftarrow {\gamma }}=\beta \gamma$ , where $\beta$ is the longest word such that any occurrence of $\gamma$ in S is preceded by $\beta$ .

"Suffix link" $link(q)$ of the state $q=[\alpha ]_{R}$ is the pointer to the state p that contains the largest suffix of $\alpha$ that is not recognized by q .

In this terms it can be said $q=[\alpha ]_{R}$ recognizes exactly all suffixes of ${\overset {\scriptstyle {\leftarrow }}{\alpha }}$ that is longer than $len(link(q))$ and not longer than $len(q)$ . It also holds:

**Theorem**—Suffix links form a tree ${\mathcal {T}}(V,E)$ that may be defined explicitly in the following way:

1. Vertices V of the tree correspond to left extensions ${\overleftarrow {\omega }}$ of all S substrings,
2. Edges E of the tree connect pairs of vertices $({\overleftarrow {\omega }},{\overleftarrow {\alpha \omega }})$ , such that $\alpha \in \Sigma$ and ${\overleftarrow {\omega }}\neq {\overleftarrow {\alpha \omega }}$ .

### Connection with suffix trees

A "prefix tree" (or "trie") is a rooted directed tree in which arcs are marked by characters in such a way no vertex v of such tree has two out-going arcs marked with the same character. Some vertices in trie are marked as final. Trie is said to recognize a set of words defined by paths from its root to final vertices. In this way prefix trees are a special kind of deterministic finite automata if you perceive its root as an initial vertex. The "suffix trie" of the word S is a prefix tree recognizing a set of its suffixes. "A suffix tree" is a tree obtained from a suffix trie via the compaction procedure, during which consequent edges are merged if the degree of the vertex between them is equal to two.

By its definition, a suffix automaton can be obtained via minimization of the suffix trie. It may be shown that a compacted suffix automaton is obtained by both minimization of the suffix tree (if one assumes each string on the edge of the suffix tree is a solid character from the alphabet) and compaction of the suffix automaton. Besides this connection between the suffix tree and the suffix automaton of the same string there is as well a connection between the suffix automaton of the string $S=s_{1}s_{2}\dots s_{n}$ and the suffix tree of the reversed string $S^{R}=s_{n}s_{n-1}\dots s_{1}$ .

Similarly to right contexts one may introduce "left contexts" $[\omega ]_{L}=\{\beta \in \Sigma ^{*}:\beta \omega \in L\}$ , "right extensions" ${\overset {\scriptstyle {\rightarrow }}{\omega ~}}$ corresponding to the longest string having same left context as $\omega$ and the equivalence relation $[\alpha ]_{L}=[\beta ]_{L}$ . If one considers right extensions with respect to the language L of "prefixes" of the string S it may be obtained:

**Theorem**—Suffix tree of the string S may be defined explicitly in the following way:

- Vertices V of the tree correspond to right extensions ${\overrightarrow {\omega }}$ of all S substrings,
- Edges E correspond to triplets $({\overrightarrow {\omega }},x\alpha ,{\overrightarrow {\omega x}})$ such that $x\in \Sigma$ and ${\overrightarrow {\omega x}}={\overrightarrow {\omega }}x\alpha$ .

Here triplet $(v_{1},\omega ,v_{2})\in E$ means there is an edge from $v_{1}$ to $v_{2}$ with the string $\omega$ written on it

, which implies the suffix link tree of the string S and the suffix tree of the string $S^{R}$ are isomorphic:

| Suffix structures of words "abbcbc" and "cbcbba" |
|---|
| (Suffix automaton of the word "abbcbc") Suffix automaton of the word "abbcbc" (Suffix trie, suffix tree and CDAWG of the word "abbcbc") Suffix trie, suffix tree and CDAWG of the word "abbcbc" (Suffix tree of the word "cbcbba" (Suffix link tree of the word "abbcbc")) Suffix tree of the word "cbcbba" (Suffix link tree of the word "abbcbc") |

Similarly to the case of left extensions, the following lemma holds for right extensions:

**Theorem**—Right extension of the string $\gamma$ may be represented as ${\overrightarrow {\gamma }}=\gamma \alpha$ , where $\alpha$ is the longest word such that every occurrence of $\gamma$ in S is succeeded by $\alpha$ .

### Size

A suffix automaton of the string S of length $n>1$ has at most $2n-1$ states and at most $3n-4$ transitions. These bounds are reached on strings $abb\dots bb=ab^{n-1}$ and $abb\dots bc=ab^{n-2}c$ correspondingly. This may be formulated in a stricter way as $|\delta |\leq |Q|+n-2$ where $|\delta |$ and $|Q|$ are the numbers of transitions and states in automaton correspondingly.

| Maximal suffix automata |
|---|
| (Suffix automaton of '"`UNIQ--postMath-000000E2-QINU`"') Suffix automaton of $ab^{n-1}$ (Suffix automaton of '"`UNIQ--postMath-000000E3-QINU`"') Suffix automaton of $ab^{n-2}c$ |

## Construction

Initially the automaton only consists of a single state corresponding to the empty word, then characters of the string are added one by one and the automaton is rebuilt on each step incrementally.

### State updates

After a new character is appended to the string, some equivalence classes are altered. Let $[\alpha ]_{R_{\omega }}$ be the right context of $\alpha$ with respect to the language of $\omega$ suffixes. Then the transition from $[\alpha ]_{R_{\omega }}$ to $[\alpha ]_{R_{\omega x}}$ after x is appended to $\omega$ is defined by lemma:

**Theorem**—Let $\alpha ,\omega \in \Sigma ^{*}$ be some words over $\Sigma$ and $x\in \Sigma$ be some character from this alphabet. Then there is a following correspondence between $[\alpha ]_{R_{\omega }}$ and $[\alpha ]_{R_{\omega x}}$ :

- $[\alpha ]_{R_{\omega x}}=[\alpha ]_{R_{\omega }}x\cup \{\varepsilon \}$ if $\alpha$ is a suffix of $\omega x$ ;
- $[\alpha ]_{R_{\omega x}}=[\alpha ]_{R_{\omega }}x$ otherwise.

After adding x to the current word $\omega$ the right context of $\alpha$ may change significantly only if $\alpha$ is a suffix of $\omega x$ . It implies equivalence relation $\equiv _{R_{\omega x}}$ is a refinement of $\equiv _{R_{\omega }}$ . In other words, if $[\alpha ]_{R_{\omega x}}=[\beta ]_{R_{\omega x}}$ , then $[\alpha ]_{R_{\omega }}=[\beta ]_{R_{\omega }}$ . After the addition of a new character at most two equivalence classes of $\equiv _{R_{\omega }}$ will be split and each of them may split in at most two new classes. First, equivalence class corresponding to empty right context is always split into two equivalence classes, one of them corresponding to $\omega x$ itself and having $\{\varepsilon \}$ as a right context. This new equivalence class contains exactly $\omega x$ and all its suffixes that did not occur in $\omega$ , as the right context of such words was empty before and contains only empty word now.

Given the correspondence between states of the suffix automaton and vertices of the suffix tree, it is possible to find out the second state that may possibly split after a new character is appended. The transition from $\omega$ to $\omega x$ corresponds to the transition from $\omega ^{R}$ to $x\omega ^{R}$ in the reversed string. In terms of suffix trees it corresponds to the insertion of the new longest suffix $x\omega ^{R}$ into the suffix tree of $\omega ^{R}$ . At most two new vertices may be formed after this insertion: one of them corresponding to $x\omega ^{R}$ , while the other one corresponds to its direct ancestor if there was a branching. Returning to suffix automata, it means the first new state recognizes $\omega x$ and the second one (if there is a second new state) is its suffix link. It may be stated as a lemma:

**Theorem**—Let $\omega \in \Sigma ^{*}$ , $x\in \Sigma$ be some word and character over $\Sigma$ . Also let $\alpha$ be the longest suffix of $\omega x$ , which occurs in $\omega$ , and let $\beta ={\overset {\scriptstyle {\leftarrow }}{\alpha }}$ . Then for any substrings $u,v$ of $\omega$ it holds:

- If $[u]_{R_{\omega }}=[v]_{R_{\omega }}$ and $[u]_{R_{\omega }}\neq [\alpha ]_{R_{\omega }}$ , then $[u]_{R_{\omega x}}=[v]_{R_{\omega x}}$ ;
- If $[u]_{R_{\omega }}=[\alpha ]_{R_{\omega }}$ and $\vert u\vert \leq \vert \alpha \vert$ , then $[u]_{R_{\omega x}}=[\alpha ]_{R_{\omega x}}$ ;
- If $[u]_{R_{\omega }}=[\alpha ]_{R_{\omega }}$ and $\vert u\vert >\vert \alpha \vert$ , then $[u]_{R_{\omega x}}=[\beta ]_{R_{\omega x}}$ .

It implies that if $\alpha =\beta$ (for example, when x didn't occur in $\omega$ at all and $\alpha =\beta =\varepsilon$ ), then only the equivalence class corresponding to the empty right context is split.

Besides suffix links it is also needed to define final states of the automaton. It follows from structure properties that all suffixes of a word $\alpha$ recognized by $q=[\alpha ]_{R}$ are recognized by some vertex on *suffix path* $(q,link(q),link^{2}(q),\dots )$ of q . Namely, suffixes with length greater than $len(link(q))$ lie in q , suffixes with length greater than $len(link(link(q))$ but not greater than $len(link(q))$ lie in $link(q)$ and so on. Thus if the state recognizing $\omega$ is denoted by $last$ , then all final states (that is, recognizing suffixes of $\omega$ ) form up the sequence $(last,link(last),link^{2}(last),\dots )$ .

### Transitions and suffix links updates

After the character x is appended to $\omega$ possible new states of suffix automaton are $[\omega x]_{R_{\omega x}}$ and $[\alpha ]_{R_{\omega x}}$ . Suffix link from $[\omega x]_{R_{\omega x}}$ goes to $[\alpha ]_{R_{\omega x}}$ and from $[\alpha ]_{R_{\omega x}}$ it goes to $link([\alpha ]_{R_{\omega }})$ . Words from $[\omega x]_{R_{\omega x}}$ occur in $\omega x$ only as its suffixes therefore there should be no transitions at all from $[\omega x]_{R_{\omega x}}$ while transitions to it should go from suffixes of $\omega$ having length at least $\alpha$ and be marked with the character x . State $[\alpha ]_{R_{\omega x}}$ is formed by subset of $[\alpha ]_{R_{\omega }}$ , thus transitions from $[\alpha ]_{R_{\omega x}}$ should be same as from $[\alpha ]_{R_{\omega }}$ . Meanwhile, transitions leading to $[\alpha ]_{R_{\omega x}}$ should go from suffixes of $\omega$ having length less than $|\alpha |$ and at least $len(link([\alpha ]_{R_{\omega }}))$ , as such transitions have led to $[\alpha ]_{R_{\omega }}$ before and corresponded to seceded part of this state. States corresponding to these suffixes may be determined via traversal of suffix link path for $[\omega ]_{R_{\omega }}$ .

| Construction of the suffix automaton for the word *abbcbc* |   |
|---|---|
| ***∅ → a*** After first character is appended, only one state is created in suffix automaton. Similarly, only one leaf is added to the suffix tree. | ***a → ab*** New transitions are drawn from all previous final states as *b* didn't appear before. For the same reason another leaf is added to the root of the suffix tree. |
| ***ab → abb*** The state 2 recognizes words *ab* and *b*, but only *b* is the new suffix, therefore this word is separated into state 4. In the suffix tree it corresponds to the split of the edge leading to the vertex 2. | ***abb → abbc*** Character *c* occurs for the first time, so transitions are drawn from all previous final states. Suffix tree of reverse string has another leaf added to the root. |
| ***abbc → abbcb*** State 4 consists of the only word *b*, which is suffix, thus the state is not split. Correspondingly, new leaf is hanged on the vertex 4 in the suffix tree. | ***abbcb → abbcbc*** The state 5 recognizes words *abbc*, *bbc*, *bc* and *c*, but only last two are suffixes of new word, so they're separated into new state 8. Correspondingly, edge leading to the vertex 5 is split and vertex 8 is put in the middle of the edge. |

### Construction algorithm

Theoretical results above lead to the following algorithm that takes character x and rebuilds the suffix automaton of ω into the suffix automaton of $\omega x$ :

1. The state corresponding to the word ω is kept as last;
2. After x is appended, previous value of last is stored in the variable p and last itself is reassigned to the new state corresponding to $\omega x$ ;
3. States corresponding to suffixes of ω are updated with transitions to last. To do this one should go through $p,link(p),link^{2}(p),\dots$ , until there is a state that already has a transition by x;
4. Once the aforementioned loop is over, there are 3 cases:
  1. If none of states on the suffix path had a transition by x, then x never occurred in ω before and the suffix link from last should lead to $q_{0}$ ;
  2. If the transition by x is found and leads from the state p to the state q, such that $len(p)+1=len(q)$ , then q does not have to be split and it is a suffix link of last;
  3. If the transition is found but $len(q)>len(p)+1$ , then words from q having length at most $len(p)+1$ should be segregated into new "clone" state cl;
5. If the previous step was concluded with the creation of cl, transitions from it and its suffix link should copy those of q, at the same time cl is assigned to be common suffix link of both q and last;
6. Transitions that have led to q before but corresponded to words of the length at most $len(p)+1$ are redirected to cl. To do this, one continues going through the suffix path of p until the state is found such that transition by x from it doesn't lead to q.

The whole procedure is described by the following pseudo-code:

```
function add_letter(x):
    define p = last
    assign last = new_state()
    assign len(last) = len(p) + 1
    while δ(p, x) is undefined:
        assign δ(p, x) = last, p = link(p)
    define q = δ(p, x)
    if q = last:
        assign link(last) = q0
    else if len(q) = len(p) + 1:
        assign link(last) = q
    else:
        define cl = new_state()
        assign len(cl) = len(p) + 1
        assign δ(cl) = δ(q), link(cl) = link(q)
        assign link(last) = link(q) = cl
        while δ(p, x) = q:
            assign δ(p, x) = cl, p = link(p)
```

Here $q_{0}$ is the initial state of the automaton and `new_state()` is a function creating new state for it. It is assumed `*last*`, `*len*`, `*link*` and `δ` are stored as global variables. For convenience, `*link(q0)*` is defined to be $q_{0}$ .

### Complexity

Complexity of the algorithm may vary depending on the underlying structure used to store transitions of the automaton. It may be implemented in $O(n\log |\Sigma |)$ with $O(n)$ memory overhead or in $O(n)$ with $O(n|\Sigma |)$ memory overhead if one assumes that memory allocation is done in $O(1)$ . To obtain such complexity, one has to use the methods of amortized analysis. The value of $len(p)$ strictly reduces with each iteration of the cycle while it may only increase by as much as one after the first iteration of the cycle on the next *add_letter* call. Overall value of $len(p)$ never exceeds n and it is only increased by one between iterations of appending new letters that suggest total complexity is at most linear as well. The linearity of the second cycle is shown in a similar way.

## Generalizations

The suffix automaton is closely related to other suffix structures and substring indices. Given a suffix automaton of a specific string one may construct its suffix tree via compacting and recursive traversal in linear time. Similar transforms are possible in both directions to switch between the suffix automaton of S and the suffix tree of reversed string $S^{R}$ . Other than this several generalizations were developed to construct an automaton for the set of strings given by trie, compacted suffix automation (CDAWG), to maintain the structure of the automaton on the sliding window, and to construct it in a bidirectional way, supporting the insertion of a characters to both the beginning and the end of the string.

### Compacted suffix automaton

As was already mentioned above, a compacted suffix automaton is obtained via both compaction of a regular suffix automaton (by removing states which are non-final and have exactly one out-going arc) and the minimization of a suffix tree. Similarly to the regular suffix automaton, states of compacted suffix automaton may be defined in explicit manner. *A two-way extension* ${\overset {\scriptstyle {\longleftrightarrow }}{\gamma }}$ of a word $\gamma$ is the longest word $\omega =\beta \gamma \alpha$ , such that every occurrence of $\gamma$ in S is preceded by $\beta$ and succeeded by $\alpha$ . In terms of left and right extensions it means that two-way extension is the left extension of the right extension or, which is equivalent, the right extension of the left extension, that is ${\textstyle {\overset {\scriptstyle \longleftrightarrow }{\gamma }}={\overset {\scriptstyle \leftarrow }{\overset {\rightarrow }{\gamma }}}={\overset {\rightarrow }{\overset {\scriptstyle \leftarrow }{\gamma }}}}$ . In terms of two-way extensions compacted automaton is defined as follows:

**Theorem**—Compacted suffix automaton of the word S is defined by a pair $(V,E)$ , where:

- $V=\{{\overleftrightarrow {\omega }}:\omega \in \Sigma ^{*}\}$ is a set of automaton states;
- $E=\{({\overleftrightarrow {\omega }},x\alpha ,{\overleftrightarrow {\omega x}}):x\in \Sigma ,\alpha \in \Sigma ^{*},{\overleftrightarrow {\omega x}}={\overleftrightarrow {\omega }}x\alpha \}$ is a set of automaton transitions.

Two-way extensions induce an equivalence relation ${\textstyle {\overset {\scriptstyle \longleftrightarrow }{\alpha }}={\overset {\scriptstyle \longleftrightarrow }{\beta }}}$ which defines the set of words recognized by the same state of compacted automaton. This equivalence relation is a transitive closure of the relation defined by ${\textstyle ({\overset {\scriptstyle {\rightarrow }}{\alpha \,}}={\overset {\scriptstyle {\rightarrow }}{\beta \,}})\vee ({\overset {\scriptstyle {\leftarrow }}{\alpha }}={\overset {\scriptstyle {\leftarrow }}{\beta }})}$ , which highlights the fact that a compacted automaton may be obtained by both gluing suffix tree vertices equivalent via ${\overset {\scriptstyle {\leftarrow }}{\alpha }}={\overset {\scriptstyle {\leftarrow }}{\beta }}$ relation (minimization of the suffix tree) and gluing suffix automaton states equivalent via ${\overset {\scriptstyle {\rightarrow }}{\alpha \,}}={\overset {\scriptstyle {\rightarrow }}{\beta \,}}$ relation (compaction of suffix automaton). If words $\alpha$ and $\beta$ have same right extensions, and words $\beta$ and $\gamma$ have same left extensions, then cumulatively all strings $\alpha$ , $\beta$ and $\gamma$ have same two-way extensions. At the same time it may happen that neither left nor right extensions of $\alpha$ and $\gamma$ coincide. As an example one may take $S=\beta =ab$ , $\alpha =a$ and $\gamma =b$ , for which left and right extensions are as follows: ${\overset {\scriptstyle {\rightarrow }}{\alpha \,}}={\overset {\scriptstyle {\rightarrow }}{\beta \,}}=ab={\overset {\scriptstyle {\leftarrow }}{\beta }}={\overset {\scriptstyle {\leftarrow }}{\gamma }}$ , but ${\overset {\scriptstyle {\rightarrow }}{\gamma \,}}=b$ and ${\overset {\scriptstyle {\leftarrow }}{\alpha }}=a$ . That being said, while equivalence relations of one-way extensions were formed by some continuous chain of nested prefixes or suffixes, bidirectional extensions equivalence relations are more complex and the only thing one may conclude for sure is that strings with the same two-way extension are *substrings* of the longest string having the same two-way extension, but it may even happen that they don't have any non-empty substring in common. The total number of equivalence classes for this relation does not exceed $n+1$ which implies that compacted suffix automaton of the string having length n has at most $n+1$ states. The amount of transitions in such automaton is at most $2n-2$ .

### Suffix automaton of several strings

Consider a set of words $T=\{S_{1},S_{2},\dots ,S_{k}\}$ . It is possible to construct a generalization of suffix automaton that would recognize the language formed up by suffixes of all words from the set. Constraints for the number of states and transitions in such automaton would stay the same as for a single-word automaton if you put $n=|S_{1}|+|S_{2}|+\dots +|S_{k}|$ . The algorithm is similar to the construction of single-word automaton except instead of $last$ state, function *add_letter* would work with the state corresponding to the word $\omega _{i}$ assuming the transition from the set of words $\{\omega _{1},\dots ,\omega _{i},\dots ,\omega _{k}\}$ to the set $\{\omega _{1},\dots ,\omega _{i}x,\dots ,\omega _{k}\}$ .

This idea is further generalized to the case when T is not given explicitly but instead is given by a prefix tree with Q vertices. Mohri *et al*. showed such an automaton would have at most $2Q-2$ and may be constructed in linear time from its size. At the same time, the number of transitions in such automaton may reach $O(Q|\Sigma |)$ , for example for the set of words $T=\{\sigma _{1},a\sigma _{1},a^{2}\sigma _{1},\dots ,a^{n}\sigma _{1},a^{n}\sigma _{2},\dots ,a^{n}\sigma _{k}\}$ over the alphabet $\Sigma =\{a,\sigma _{1},\dots ,\sigma _{k}\}$ the total length of words is equal to ${\textstyle O(n^{2}+nk)}$ , the number of vertices in corresponding suffix trie is equal to $O(n+k)$ and corresponding suffix automaton is formed of $O(n+k)$ states and $O(nk)$ transitions. Algorithm suggested by Mohri mainly repeats the generic algorithm for building automaton of several strings but instead of growing words one by one, it traverses the trie in a breadth-first search order and append new characters as it meet them in the traversal, which guarantees amortized linear complexity.

### Sliding window

Some compression algorithms, such as LZ77 and RLE may benefit from storing suffix automaton or similar structure not for the whole string but for only last k its characters while the string is updated. This is because compressing data is usually expressively large and using $O(n)$ memory is undesirable. In 1985, Janet Blumer developed an algorithm to maintain a suffix automaton on a sliding window of size k in $O(nk)$ worst-case and $O(n\log k)$ on average, assuming characters are distributed independently and uniformly. She also showed $O(nk)$ complexity cannot be improved: if one considers words construed as a concatenation of several $(ab)^{m}c(ab)^{m}d$ words, where $k=6m+2$ , then the number of states for the window of size k would frequently change with jumps of order m , which renders even theoretical improvement of $O(nk)$ for regular suffix automata impossible.

The same should be true for the suffix tree because its vertices correspond to states of the suffix automaton of the reversed string but this problem may be resolved by not explicitly storing every vertex corresponding to the suffix of the whole string, thus only storing vertices with at least two out-going edges. A variation of McCreight's suffix tree construction algorithm for this task was suggested in 1989 by Edward Fiala and Daniel Greene; several years later a similar result was obtained with the variation of Ukkonen's algorithm by Jesper Larsson. The existence of such an algorithm, for compacted suffix automaton that absorbs some properties of both suffix trees and suffix automata, was an open question for a long time until it was discovered by Martin Senft and Tomasz Dvorak in 2008, that it is impossible if the alphabet's size is at least two.

One way to overcome this obstacle is to allow window width to vary a bit while staying $O(k)$ . It may be achieved by an approximate algorithm suggested by Inenaga et al. in 2004. The window for which suffix automaton is built in this algorithm is not guaranteed to be of length k but it is guaranteed to be at least k and at most $2k+1$ while providing linear overall complexity of the algorithm.

## Applications

Suffix automaton of the string S may be used to solve such problems as:

- Counting the number of distinct substrings of S in $O(|S|)$ on-line,
- Finding the longest substring of S occurring at least twice in $O(|S|)$ ,
- Finding the longest common substring of S and T in $O(|T|)$ ,
- Counting the number of occurrences of T in S in $O(|T|)$ ,
- Finding all occurrences of T in S in $O(|T|+k)$ , where k is the number of occurrences.

It is assumed here that T is given on the input after suffix automaton of S is constructed.

Suffix automata are also used in data compression, music retrieval and matching on genome sequences.
