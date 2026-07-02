---
title: "Deterministic acyclic finite state automaton"
source: https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton
domain: trie-structure
license: CC-BY-SA-4.0
tags: prefix trie, digital tree, ternary search tree, radix tree
fetched: 2026-07-02
---

# Deterministic acyclic finite state automaton

In computer science, a **deterministic acyclic finite state automaton** (**DAFSA**), is a data structure that represents a set of strings, and allows for a query operation that tests whether a given string belongs to the set in time proportional to its length. Algorithms exist to construct and maintain such automata, while keeping them minimal. DAFSA is the rediscovery of a data structure called Directed Acyclic Word Graph (DAWG), although the same name had already been given to a different data structure which is related to suffix automaton.

A DAFSA is a special case of a finite state recognizer that takes the form of a directed acyclic graph with a single source vertex (a vertex with no incoming edges), in which each edge of the graph is labeled by a letter or symbol, and in which each vertex has at most one outgoing edge for each possible letter or symbol. The strings represented by the DAFSA are formed by the symbols on paths in the graph from the source vertex to any sink vertex (a vertex with no outgoing edges). In fact, a deterministic finite state automaton is acyclic if and only if it recognizes a finite set of strings.

## History

Blumer et al first defined terminology Directed Acyclic Word Graph (DAWG) in 1983. Appel and Jacobsen used the same naming for a different data structure in 1988. Independent of earlier work, Daciuk et al rediscovered the latter data structure in 2000 but called it DAFSA.

## Comparison to tries

By allowing the same vertices to be reached by multiple paths, a DAFSA may use significantly fewer vertices than the strongly related trie data structure. Consider, for example, the four English words "tap", "taps", "top", and "tops". A trie for those four words would have 12 vertices, one for each of the strings formed as a prefix of one of these words, or for one of the words followed by the end-of-string marker. However, a DAFSA can represent these same four words using only six vertices *vi* for 0 ≤ *i* ≤ 5, and the following edges: an edge from *v*0 to *v*1 labeled "t", two edges from *v*1 to *v*2 labeled "a" and "o", an edge from *v*2 to *v*3 labeled "p", an edge *v*3 to *v*4 labeled "s", and edges from *v*3 and *v*4 to *v*5 labeled with the end-of-string marker. There is a tradeoff between memory and functionality, because a standard DAFSA can tell you if a word exists within it, but it cannot point you to auxiliary information about that word, whereas a trie can.

The primary difference between DAFSA and trie is the elimination of suffix and infix redundancy in storing strings. The trie eliminates prefix redundancy since all common prefixes are shared between strings, such as between *doctors* and *doctorate* the *doctor* prefix is shared. In a DAFSA common suffixes are also shared, for words that have the same set of possible suffixes as each other. For dictionary sets of common English words, this translates into major memory usage reduction.

Because the terminal nodes of a DAFSA can be reached by multiple paths, a DAFSA cannot directly store auxiliary information relating to each path, e.g. a word's frequency in the English language. However, if for each node we store the number of unique paths through that point in the structure, we can use it to retrieve the index of a word, or a word given its index. The auxiliary information can then be stored in an array.
