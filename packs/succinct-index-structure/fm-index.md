---
title: "FM-index"
source: https://en.wikipedia.org/wiki/FM-index
domain: succinct-index-structure
license: CC-BY-SA-4.0
tags: succinct data structure, wavelet tree, range minimum query, compact index
fetched: 2026-07-02
---

# FM-index

In computer science, an **FM-index** is a compressed full-text substring index based on the Burrows–Wheeler transform, with some similarities to the suffix array. It was created by Paolo Ferragina and Giovanni Manzini, who describe it as an opportunistic data structure as it allows compression of the input text while still permitting fast substring queries. The name stands for Full-text index in Minute space.

It can be used to efficiently find the number of occurrences of a pattern within the compressed text, as well as locate the position of each occurrence. The query time, as well as the required storage space, has a sublinear complexity with respect to the size of the input data.

The original authors have devised improvements to their original approach and dubbed it "FM-Index version 2". A further improvement, the alphabet-friendly FM-index, combines the use of compression boosting and wavelet trees to significantly reduce the space usage for large alphabets.

The FM-index has found use in, among other places, bioinformatics.

## Background

Using an index is a common strategy to efficiently search a large body of text. When the text is larger than what reasonably fits within a computer's main memory, there is a need to compress not only the text but also the index. When the FM-index was introduced, there were several suggested solutions that were based on traditional compression methods and tried to solve the compressed matching problem. In contrast, the FM-index is a compressed self-index, which means that it compresses the data and indexes it at the same time.

## FM-index data structure

An FM-index is created by first taking the Burrows–Wheeler transform (BWT) of the input text. For example, the BWT of the string T = "abracadabra$" is "ard$rcaaaabb", and here it is represented by the matrix M where each row is a rotation of the text, and the rows have been sorted lexicographically. The transform corresponds to the concatenation of the characters from the last column (labeled L).

| I | FabracadabrL |
|---|---|
| 1 | $abracadabra |
| 2 | a$abracadabr |
| 3 | abra$abracad |
| 4 | abracadabra$ |
| 5 | acadabra$abr |
| 6 | adabra$abrac |
| 7 | bra$abracada |
| 8 | bracadabra$a |
| 9 | cadabra$abra |
| 10 | dabra$abraca |
| 11 | ra$abracadab |
| 12 | racadabra$ab |

The BWT in itself allows for some compression with, for instance, move to front and Huffman encoding, but the transform has even more uses. The rows in the matrix are essentially the sorted suffixes of the text and the first column F of the matrix shares similarities with suffix arrays. How the suffix array relates to the BWT lies at the heart of the FM-index.

| c | $ | a | b | c | d | r |
|---|---|---|---|---|---|---|
| C[c] | 0 | 1 | 6 | 8 | 9 | 10 |

Occ(c, k)

of "

ard$rcaaaabb

"

a

r

d

$

r

c

a

a

a

a

b

b

1

2

3

4

5

6

7

8

9

10

11

12

$

0

0

0

1

1

1

1

1

1

1

1

1

a

1

1

1

1

1

1

2

3

4

5

5

5

b

0

0

0

0

0

0

0

0

0

0

1

2

c

0

0

0

0

0

1

1

1

1

1

1

1

d

0

0

1

1

1

1

1

1

1

1

1

1

r

0

1

1

1

2

2

2

2

2

2

2

2

It is possible to make a last-to-first column mapping LF(i) from an index i to an index j, such that F[j] = L[i], with the help of a table C[c] and a function Occ(c, k).

- C[c] is a table that, for each character c in the alphabet, contains the number of occurrences of lexically (strictly) smaller characters in the text.
- The function Occ(c, k) is the number of occurrences of character c in the prefix L[1..k]. Ferragina and Manzini showed that it is possible to compute Occ(c, k) in constant time.

The last-to-first mapping can now be defined as LF(i) = C[L[i]] + Occ(L[i], i). For instance, on row 9, L is a and the same a can be found on row 5 in the first column F, so LF(9) should be 5 and LF(9) = C[a] + Occ(a, 9) = 5. For any row i of the matrix, the character in the last column L[i] precedes the character in the first column F[i] also in T. Finally, if L[i] = T[k], then L[LF(i)] = T[k - 1], and using the equality it is possible to extract a string of T from L.

The FM-index itself is a compression of the string L together with C and Occ in some form, as well as information that maps a selection of indices in L to positions in the original string T.

## Count

The operation *count* takes a pattern P[1..p] and returns the number of occurrences of that pattern in the original text T. Since the rows of matrix M are sorted, and it contains every suffix of T, the occurrences of pattern P will be next to each other in a single continuous range. The operation iterates backwards over the pattern. For every character in the pattern, the range that has the character as a suffix is found. For example, the count of the pattern "bra" in "abracadabra" follows these steps:

1. The first character we look for is a, the last character in the pattern. The initial range is set to [C[a] + 1 .. C[a+1]] = [2..6]. This range over L represents every character of T that has a suffix beginning with *a*.
2. The next character to look for is r. The new range is [C[r] + Occ(r, start-1) + 1 .. C[r] + Occ(r, end)] = [10 + 0 + 1 .. 10 + 2] = [11..12], if start is the index of the beginning of the range and end is the end. This range over L is all the characters of T that have suffixes beginning with *ra*.
3. The last character to look at is b. The new range is [C[b] + Occ(b, start-1) + 1 .. C[b] + Occ(b, end)] = [6 + 0 + 1 .. 6 + 2] = [7..8]. This range over L is all the characters that have a suffix that begins with *bra*. Now that the whole pattern has been processed, the count is the same as the size of the range: 8 - 7 + 1 = 2.

If the range becomes empty or the range boundaries cross each other before the whole pattern has been looked up, the pattern does not occur in T. Because Occ(c, k) can be performed in constant time, count can complete in linear time in the length of the pattern: O(p) time.

## Locate

The operation *locate* takes as input an index of a character in L and returns its position i in T. For instance locate(7) = 8. To locate every occurrence of a pattern, first the range of character is found whose suffix is the pattern in the same way the *count* operation found the range. Then the position of every character in the range can be located.

To map an index in L to one in T, a subset of the indices in L are associated with a position in T. If L[j] has a position associated with it, locate(j) is trivial. If it's not associated, the string is followed with LF(i) until an associated index is found. By associating a suitable number of indices, an upper bound can be found. *Locate* can be implemented to find *occ* occurrences of a pattern P[1..*p*] in a text T[1..*u*] in O(*p* + *occ* logε *u*) time with $O\left(H_{k}(T)+{{\log \log u} \over {\log ^{\epsilon }u}}\right)$ bits per input symbol for any *k* ≥ 0.

## Applications

### DNA read mapping

FM index with backtracking has been successfully (>2000 citations) applied to approximate string matching/sequence alignment, See Bowtie https://bowtie-bio.sourceforge.net/index.shtml

## Implementations

The FM-Index is available in multiple languages, including C++, Java and Rust. Despite all of them being an implementation of the FM-Index, some feature different data structures for compressing the input text, e.g. with the Rust version being available as both a standard FM-Index and a run-length encoded FM-Index or the Java version using fixed block boosting compression wavelet trees.
