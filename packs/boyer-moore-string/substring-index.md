---
title: "Substring index"
source: https://en.wikipedia.org/wiki/Substring_index
domain: boyer-moore-string
license: CC-BY-SA-4.0
tags: boyer moore algorithm, string searching algorithm, bad character rule, pattern matching
fetched: 2026-07-02
---

# Substring index

In computer science, a **substring index** is a data structure which gives substring search in a text or text collection in sublinear time. Once constructed from a document or set of documents, a substring index can be used to locate all occurrences of a pattern in time linear or near-linear in the pattern size, with no dependence or only logarithmic dependence on the document size.

The phrase **full-text index** is often used for substring indexes. But this is ambiguous, as it is also used for regular word indexes such as inverted files and document retrieval. See full text search.

## General considerations

These data structures typically treat their text and pattern as strings over a fixed alphabet, and search for locations where the pattern occurs as a substring of the text. The symbols of the alphabet may be characters (for instance in Unicode) but in practical applications for text retrieval it may be preferable to treat the (stemmed) words of a document as the symbols of its alphabet, because doing this reduces the lengths of both the text and pattern as measured in numbers of symbols.

## Examples

Specific data structures that can be used as substring indexes include:

- The suffix tree, a radix tree of the suffixes of the string, allowing substring search to be performed symbol-by-symbol
- The suffix automaton, the minimal deterministic finite automaton that recognizes substrings of a given text, closely related to the suffix tree and constructable by variants of the same algorithms.
- The suffix array, a sorted array of the starting positions of suffixes of the string, allowing substring search to be performed by binary search Augmenting a suffix array with an LCP array of the lengths of common prefixes of consecutive suffixes allows the search to be performed symbol-by-symbol, matching the search time of the suffix tree.
- The compressed suffix array, a data structure that combines data compression with the suffix array, allowing the structure to be stored in space sublinear in the text length
- The FM-index, another compressed substring index based on the Burrows–Wheeler transform and closely related to the suffix array
