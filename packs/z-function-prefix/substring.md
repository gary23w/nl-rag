---
title: "Substring"
source: https://en.wikipedia.org/wiki/Substring
domain: z-function-prefix
license: CC-BY-SA-4.0
tags: z algorithm, z array, prefix substring matching, linear pattern search
fetched: 2026-07-02
---

# Substring

In formal language theory and computer science, a **substring** is a contiguous sequence of characters within a string. For instance, "*the best of*" is a substring of "*It was the best of times*". In contrast, "*Itwastimes*" is a subsequence of "*It was the best of times*", but not a substring.

**Prefixes** and **suffixes** are special cases of substrings. A prefix of a string S is a substring of S that occurs at the beginning of S ; likewise, a suffix of a string S is a substring that occurs at the end of S .

The substrings of the string "apple" would be: "a", "ap", "app", "appl", "apple", "p", "pp", "ppl", "pple", "pl", "ple", "l", "le" "e", "" (note the empty string at the end).

## Substring

A string u is a substring (or factor) of a string t if there exists two strings p and s such that $t=pus$ . In particular, the empty string is a substring of every string.

Example: The string $u={\texttt {ana}}$ is equal to substrings (and subsequences) of $t={\texttt {banana}}$ at two different offsets:

```
banana
 |||||
 ana||
   |||
   ana
```

The first occurrence is obtained with $p={\texttt {b}}$ and $s={\texttt {na}}$ , while the second occurrence is obtained with $p={\texttt {ban}}$ and s being the empty string.

A substring of a string is a prefix of a suffix of the string, and equivalently a suffix of a prefix; for example, `nan` is a prefix of `nana`, which is in turn a suffix of `banana`. If u is a substring of t , it is also a subsequence, which is a more general concept. The occurrences of a given pattern in a given string can be found with a string searching algorithm. Finding the longest string which is equal to a substring of two or more strings is known as the longest common substring problem. In the mathematical literature, substrings are also called **subwords** (in America) or **factors** (in Europe).

## Prefix

A string p is a prefix of a string t if there exists a string s such that $t=ps$ . A *proper prefix* of a string is not equal to the string itself; some sources in addition restrict a proper prefix to be non-empty. A prefix can be seen as a special case of a substring.

Example: The string `ban` is equal to a prefix (and substring and subsequence) of the string `banana`:

```
banana
|||
ban
```

The square subset symbol is sometimes used to indicate a prefix, so that $p\sqsubseteq t$ denotes that p is a prefix of t . This defines a binary relation on strings, called the prefix relation, which is a particular kind of prefix order.

## Suffix

A string s is a suffix of a string t if there exists a string p such that $t=ps$ . A *proper suffix* of a string is not equal to the string itself. A more restricted interpretation is that it is also not empty. A suffix can be seen as a special case of a substring.

Example: The string `nana` is equal to a suffix (and substring and subsequence) of the string `banana`:

```
banana
  ||||
  nana
```

A suffix tree for a string is a trie data structure that represents all of its suffixes. Suffix trees have large numbers of applications in string algorithms. The suffix array is a simplified version of this data structure that lists the start positions of the suffixes in alphabetically sorted order; it has many of the same applications.

## Border

A border is suffix and prefix of the same string, e.g. " ${\texttt {bab}}$ " is a border of " ${\texttt {babab}}$ " (and also of " ${\texttt {baboon}}\,\,{\texttt {eating}}\,\,{\texttt {a}}\,\,{\texttt {kebab}}$ ").

## Superstring

A **superstring** of a finite set P of strings is a single string that contains every string in P as a substring. For example, ${\texttt {bcclabccefab}}$ is a superstring of $P=\{{\texttt {abcc}},{\texttt {efab}},{\texttt {bccla}}\}$ , and ${\texttt {efabccla}}$ is a shorter one. Concatenating all members of P , in arbitrary order, always obtains a trivial superstring of P . Finding superstrings whose length is as small as possible is a more interesting problem.

A string that contains every possible permutation of a specified character set is called a superpermutation.
