---
title: "Commentz-Walter algorithm"
source: https://en.wikipedia.org/wiki/Commentz-Walter_algorithm
domain: aho-corasick-deep
license: CC-BY-SA-4.0
tags: aho corasick automaton, multi pattern search, failure links, dictionary matching
fetched: 2026-07-02
---

# Commentz-Walter algorithm

In computer science, the **Commentz-Walter algorithm** is a string searching algorithm invented by Beate Commentz-Walter. Like the Aho–Corasick string matching algorithm, it can search for multiple patterns at once. It combines ideas from Aho–Corasick with the fast matching of the Boyer–Moore string-search algorithm. For a text of length *n* and maximum pattern length of *m*, its worst-case running time is O(*mn*), though the average case is often much better.

GNU grep once implemented a string matching algorithm very similar to Commentz-Walter.

## History

The paper on the algorithm was first published by Beate Commentz-Walter in 1979 through the Saarland University and typed by "R. Scherner". The paper detailed two differing algorithms she claimed combined the idea of the Aho-Corasick and Boyer-Moore algorithms, which she called algorithms B and B1. The paper mostly focuses on algorithm B, however.

## How the Algorithm Works

The Commentz-Walter algorithm combines two known algorithms in order to attempt to better address the multi-pattern matching problem. These two algorithms are the Boyer-Moore, which addresses single pattern matching using filtering, and the Aho-Corasick. To do this, the algorithm implements a suffix automaton to search through patterns within an input string, while also using reverse patterns, unlike in the Aho-Corasick.

Commentz-Walter has two phases it must go through, these being a pre-computing phase and a matching phase. For the first phase, the Commentz-Walter algorithm uses a reversed pattern to build a pattern tree, this is considered the pre-computing phase. The second phase, known as the matching phase, takes into account the other two algorithms. Using the Boyer-Moore’s technique of shifting and the Aho-Corasick's technique of finite automata, the Commentz-Walter algorithm can begin matching.

The Commentz-Walter algorithm will scan backwards throughout an input string, checking for a mismatch. If and when the algorithm does find a mismatch, the algorithm will already know some of the characters that are matches, and then use this information as an index. Using the index, the algorithm checks the pre-computed table to find a distance that it must shift, after this, the algorithm once more begins another matching attempt.

## Time Complexity

Comparing the Aho-Corasick to the Commentz-Walter Algorithm yields results with the idea of time complexity. Aho-Corasick is considered linear O(*m+n+k*) where k is the number of matches, n the haystack length, and m the pattern length. Commentz-Walter is O(*mn*), since Commentz-Walter was developed by adding the shifts within the Boyer–Moore string-search algorithm to the Aho-Corasick, thus it inherits the O(*mn*) complexity of Boyer-Moore. In both cases, this worst-case performance is only seen when matches are very frequent in the text. For infrequent matches, or no match at all, both algorithms approach linear performance.

According to a published average-time complexity analysis, Commentz-Walter seems to be generally faster than the Aho–Corasick string matching algorithm, but only when using long patterns. However, the journal does state that there is no critical analysis on this statement and that there is a lack of general agreement on the performance of the algorithm.

As seen in a visualization of the algorithm’s running time done in a study by “The International Journal of Advanced Computer Science and Information Technology” the performance of the algorithm increased linearly as the shortest pattern within the pattern set increased.

## Alternative Algorithm

In the original Commentz-Walter paper, an alternative algorithm was also created. This algorithm, known as B1, operates similarly to the main Commentz-Walter algorithm with the only difference being in the way the pattern tree is used during the scanning phase.

The paper also claims this algorithm performs better at the cost of increasing the running time and space of both the preprocessing phase and search phase. This algorithm has not been formally tested in other studies however, so its actual performance is unknown.
