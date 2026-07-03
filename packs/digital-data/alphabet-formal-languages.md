---
title: "Alphabet (formal languages)"
source: https://en.wikipedia.org/wiki/Alphabet_(formal_languages)
domain: digital-data
license: CC-BY-SA-4.0
tags: digital data
fetched: 2026-07-03
---

# Alphabet (formal languages)

In formal language theory, an **alphabet**, often called a **vocabulary** in the context of terminal and nonterminal symbols, is a non-empty set of indivisible symbols/characters/glyphs, typically thought of as representing letters, characters, digits, phonemes, or even words. The definition is used in a diverse range of fields including logic, mathematics, computer science, and linguistics. An alphabet may have any cardinality ("size") and, depending on its purpose, may be finite (e.g., the alphabet of letters "a" through "z"), countable (e.g., $\{v_{1},v_{2},\ldots \}$ ), or even uncountable (e.g., $\{v_{x}:x\in \mathbb {R} \}$ ).

Strings, also known as "words" or "sentences", over an alphabet are defined as a sequence of the symbols from the alphabet set. For example, the alphabet of lowercase letters "a" through "z" can be used to form English words like "iceberg" while the alphabet of both upper and lower case letters can also be used to form proper names like "Wikipedia". A common alphabet is {0,1}, the **binary alphabet**, and "00101111" is an example of a binary string. Infinite sequences of symbols may be considered as well (see Omega language).

Strings are often written as the concatenation of their symbols, and when using this notational convention it is convenient for practical purposes to restrict the symbols in an alphabet so that this notation is unambiguous. For instance, if the two-member alphabet is {00,0}, a string written in concatenated form as "000" is ambiguous because it is unclear if it is a sequence of three "0" symbols, a "00" followed by a "0", or a "0" followed by a "00". However, this is a limitation on the notation for writing strings, not on their underlying definitions. Like any finite set, {00,0} can be used as an alphabet, whose strings can be written unambiguously in a different notational convention with commas separating their elements: 0,00 ≠ 0,0,0 ≠ 00,0.

## Notation

By definition, the *alphabet* of a formal language L over $\Sigma$ is the set $\Sigma$ , which can be **any** non-empty set of symbols from which every string in L is built. For example, the set $\Sigma =\{\_,\mathrm {a} ,\dots ,\mathrm {z} ,\mathrm {A} ,\dots ,\mathrm {Z} ,0,\mathrm {1} ,\dots ,\mathrm {9} \}$ can be the alphabet of the formal language L that means "all variable identifiers in the C programming language". It is not required to use every symbol in the alphabet of L for its strings.

Given an alphabet $\Sigma$ , the set of all strings of length n over the alphabet $\Sigma$ is indicated by $\Sigma ^{n}$ . The set ${\textstyle \bigcup _{i\in \mathbb {N} }\Sigma ^{i}}$ of all finite strings (regardless of their length) is indicated by the Kleene star operator as $\Sigma ^{*}$ , and is also called the Kleene closure of $\Sigma$ . The notation $\Sigma ^{\omega }$ indicates the set of all infinite sequences over the alphabet $\Sigma$ , and $\Sigma ^{\infty }$ indicates the set $\Sigma ^{\ast }\cup \Sigma ^{\omega }$ of all finite or infinite sequences.

For example, using the binary alphabet {0,1}, the strings ε, 0, 1, 00, 01, 10, 11, 000, etc. are all in the Kleene closure of the alphabet (where ε represents the empty string).

## Applications

Alphabets are important in the use of formal languages, automata and semiautomata. In most cases, for defining instances of automata, such as deterministic finite automata (DFAs), it is required to specify an alphabet from which the input strings for the automaton are built. In these applications, an alphabet is usually required to be a finite set, but is not otherwise restricted.

When using automata, regular expressions, or formal grammars as part of string-processing algorithms, the alphabet may be assumed to be the character set of the text to be processed by these algorithms, or a subset of allowable characters from the character set.
