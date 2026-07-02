---
title: "Aho–Corasick algorithm"
source: https://en.wikipedia.org/wiki/Aho–Corasick_algorithm
domain: aho-corasick-algorithm
license: CC-BY-SA-4.0
tags: aho corasick algorithm, multi pattern matching, trie data structure, finite state machine
fetched: 2026-07-02
---

# Aho–Corasick algorithm

In computer science, the **Aho–Corasick algorithm** is a string-searching algorithm invented by Alfred V. Aho and Margaret J. Corasick in 1975. It is a kind of dictionary-matching algorithm that locates elements of a finite set of strings (the "dictionary") within an input text. It matches all strings simultaneously. The complexity of the algorithm is linear in the length of the strings plus the length of the searched text plus the number of output matches. Because all matches are found, multiple matches will be returned for one string location if multiple strings from the dictionary match at that location (e.g. dictionary = a, aa, aaa, aaaa and input string is aaaa).

Informally, the algorithm creates a trie using the strings in the dictionary and then constructs a finite-state machine from the trie by adding additional links between the nodes. These extra links allow fast transitions between failed string matches (e.g. a search for cart in a trie that does not contain cart, but contains art, and thus would fail at the node prefixed by car), to other branches of the trie that share a common suffix (e.g., in the previous case, a branch for attribute might be the best lateral transition). This allows the automaton to transition between string matches without the need for backtracking.

When the string dictionary is known in advance (e.g. a computer virus database), the construction of the automaton can be performed once off-line and the compiled automaton stored for later use. In this case, its run time is linear in the length of the input plus the number of matched entries.

The Aho—Corasick string-matching algorithm formed the basis of the original Unix command fgrep.

## History

Like many inventions at Bell Labs at the time, the Aho–Corasick algorithm was created serendipitously with a conversation between the two after a seminar by Aho. Corasick was an information scientist who got her PhD a year earlier at Lehigh University. There, she did her dissertation on securing proprietary data within open systems, through the lens of both the commercial, legal, and government structures and the technical tools that were emerging at the time. In a similar realm, at Bell Labs, she was building a tool for researchers to learn about current work being done by government contractors by searching government-provided tapes of publications.

She had written a primitive keyword-by-keyword search program to find chosen keywords within the tapes, but it scaled poorly with many keywords; One of the bibliographers using her algorithm hit the $600 usage limit on the Bell Labs machines before their search finished.

She ended up attending a seminar on algorithm design by Aho, and afterwards they got to speaking about her work and this problem. Aho suggested improving the efficiency of the program using the approach of the now Aho–Corasick algorithm, and Corasick designed a program based on those insights. This lowered the running cost of that bibliographer's search from over $600 to just $25.

## Example

In this example, we will consider a dictionary consisting of the following words: {a, ab, bab, bc, bca, c, caa}.

The graph below is the Aho–Corasick data structure constructed from the specified dictionary, with each row in the table representing a node in the trie, with the column path indicating the (unique) sequence of characters from the root to the node.

The data structure has one node for every prefix of every string in the dictionary. So if (bca) is in the dictionary, then there will be nodes for (bca), (bc), (b), and (). If a node is in the dictionary then it is a blue node. Otherwise it is a grey node.

There is a black directed "child" arc from each node to a node whose name is found by appending one character. So there is a black arc from (bc) to (bca).

There is a blue directed "suffix" arc from each node to the node that is the longest possible strict suffix of it in the graph. For example, for node (caa), its strict suffixes are (aa) and (a) and (). The longest of these that exists in the graph is (a). So there is a blue arc from (caa) to (a). The blue arcs can be computed in linear time by performing a breadth-first search [potential suffix node will always be at lower level] starting from the root. The target for the blue arc of a visited node can be found by following its parent's blue arc to its longest suffix node and searching for a child of the suffix node whose character matches that of the visited node. If the character does not exist as a child, we can find the next longest suffix (following the blue arc again) and then search for the character. We can do this until we either find the character (as child of a node) or we reach the root (which will always be a suffix of every string).

There is a green "dictionary suffix" arc from each node to the next node in the dictionary that can be reached by following blue arcs. For example, there is a green arc from (bca) to (a) because (a) is the first node in the dictionary (i.e. a blue node) that is reached when following the blue arcs to (ca) and then on to (a). The green arcs can be computed in linear time by repeatedly traversing blue arcs until a blue node is found, and memoizing this information.

| Path | In dictionary | Suffix link | Dict suffix link |
|---|---|---|---|
| () | – |   |   |
| (a) | + | () |   |
| (ab) | + | (b) |   |
| (b) | – | () |   |
| (ba) | – | (a) | (a) |
| (bab) | + | (ab) | (ab) |
| (bc) | + | (c) | (c) |
| (bca) | + | (ca) | (a) |
| (c) | + | () |   |
| (ca) | – | (a) | (a) |
| (caa) | + | (a) | (a) |

At each step, the current node is extended by finding its child, and if that doesn't exist, finding its suffix's child, and if that doesn't work, finding its suffix's suffix's child, and so on, finally ending in the root node if nothing's seen before.

When the algorithm reaches a node, it outputs all the dictionary entries that end at the current character position in the input text. This is done by printing every node reached by following the dictionary suffix links, starting from that node, and continuing until it reaches a node with no dictionary suffix link. In addition, the node itself is printed, if it is a dictionary entry.

Execution on input string abccab yields the following steps:

| Node | Remaining string | Output:end position | Transition | Output |
|---|---|---|---|---|
| () | abccab |   | start at root |   |
| (a) | bccab | a:1 | () to child (a) | Current node |
| (ab) | ccab | ab:2 | (a) to child (ab) | Current node |
| (bc) | cab | bc:3, c:3 | (ab) to suffix (b) to child (bc) | Current Node, Dict suffix node |
| (c) | ab | c:4 | (bc) to suffix (c) to suffix () to child (c) | Current node |
| (ca) | b | a:5 | (c) to child (ca) | Dict suffix node |
| (ab) |   | ab:6 | (ca) to suffix (a) to child (ab) | Current node |

The original Aho–Corasick algorithm assumes that the set of search strings is fixed. It does not directly apply to applications in which new search strings are added during application of the algorithm. An example is an interactive indexing program, in which the user goes through the text and highlights new words or phrases to index as they see them. Bertrand Meyer introduced an incremental version of the algorithm in which the search string set can be incrementally extended during the search, retaining the algorithmic complexity of the original.
