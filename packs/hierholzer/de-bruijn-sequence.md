---
title: "De Bruijn sequence"
source: https://en.wikipedia.org/wiki/De_Bruijn_sequence
domain: hierholzer
license: CC-BY-SA-4.0
tags: hierholzer algorithm, euler tour construction, edge traversal, closed walk
fetched: 2026-07-02
---

# De Bruijn sequence

In combinatorial mathematics, a **de Bruijn sequence** of order *n* on a size-*k* alphabet *A* is a cyclic sequence in which every possible length-*n* string on *A* occurs exactly once as a substring (i.e., as a *contiguous* subsequence). Such a sequence is denoted by *B*(*k*, *n*) and has length *k**n*, which is also the number of distinct strings of length *n* on *A*. Each of these distinct strings, when taken as a substring of *B*(*k*, *n*), must start at a different position, because substrings starting at the same position are not distinct. Therefore, *B*(*k*, *n*) must have *at least* *k**n* symbols. And since *B*(*k*, *n*) has *exactly* *k**n* symbols, de Bruijn sequences are optimally short with respect to the property of containing every string of length *n* at least once.

The number of distinct de Bruijn sequences *B*(*k*, *n*) is

${\dfrac {\left(k!\right)^{k^{n-1}}}{k^{n}}}.$

For a binary alphabet this is $2^{2^{(n-1)}-n}$ , leading to the following sequence for positive n :   1, 1, 2, 16, 2048, 67108864... ((sequence A016031 in the OEIS))

The sequences are named after the Dutch mathematician Nicolaas Govert de Bruijn, who wrote about them in 1946. As he later wrote, the existence of de Bruijn sequences for each order together with the above properties were first proved, for the case of alphabets with two elements, by Camille Flye Sainte-Marie (1894). The generalization to larger alphabets is due to Tatyana van Aardenne-Ehrenfest and de Bruijn (1951). Automata for recognizing these sequences are denoted as de Bruijn automata.

In many applications, *A* = {0,1}.

## History

The earliest known example of a de Bruijn sequence comes from Sanskrit prosody where, since the work of Pingala, each possible three-syllable pattern of long and short syllables is given a name, such as 'y' for short–long–long and 'm' for long–long–long. To remember these names, the mnemonic *yamātārājabhānasalagām* is used, in which each three-syllable pattern occurs starting at its name: 'yamātā' has a short–long–long pattern, 'mātārā' has a long–long–long pattern, and so on, until 'salagām' which has a short–short–long pattern. This mnemonic, equivalent to a de Bruijn sequence on binary 3-tuples, is of unknown antiquity, but is at least as old as Charles Philip Brown's 1869 book on Sanskrit prosody that mentions it and considers it "an ancient line, written by Pāṇini".

In 1894, A. de Rivière raised the question in an issue of the French problem journal *L'Intermédiaire des Mathématiciens*, of the existence of a circular arrangement of zeroes and ones of size $2^{n}$ that contains all $2^{n}$ binary sequences of length n . The problem was solved (in the affirmative), along with the count of $2^{2^{n-1}-n}$ distinct solutions, by Camille Flye Sainte-Marie in the same year. This was largely forgotten, and Martin (1934) proved the existence of such cycles for general alphabet size in place of 2, with an algorithm for constructing them. Finally, when in 1944 Kees Posthumus conjectured the count $2^{2^{n-1}-n}$ for binary sequences, de Bruijn proved the conjecture in 1946, through which the problem became well known.

Karl Popper independently describes these objects in his *The Logic of Scientific Discovery* (1934), calling them "shortest random-like sequences".

## Examples

- Taking *A* = {0, 1}, there are two distinct *B*(2, 3): 00010111 and 11101000, one being the reverse or negation of the other.
- Two of the 16 possible *B*(2, 4) in the same alphabet are 0000100110101111 and 0000111101100101.
- Two of the 2048 possible *B*(2, 5) in the same alphabet are 00000100011001010011101011011111 and 00000101001000111110111001101011.

## Construction

The de Bruijn sequences can be constructed by taking a Hamiltonian path of an *n*-dimensional de Bruijn graph over *k* symbols (or equivalently, an Eulerian cycle of an (*n* − 1)-dimensional de Bruijn graph).

An alternative construction involves concatenating together, in lexicographic order, all the Lyndon words whose length divides *n*.

An inverse Burrows–Wheeler transform can be used to generate the required Lyndon words in lexicographic order.

de Bruijn sequences can also be constructed using shift registers or via finite fields.

### Example using de Bruijn graph

Goal: to construct a *B*(2, 4) de Bruijn sequence of length 24 = 16 using Eulerian (*n* − 1 = 4 − 1 = 3) 3-D de Bruijn graph cycle.

Each edge in this 3-dimensional de Bruijn graph corresponds to a sequence of four digits: the three digits that label the vertex that the edge is leaving followed by the one that labels the edge. If one traverses the edge labeled 1 from 000, one arrives at 001, thereby indicating the presence of the subsequence 0001 in the de Bruijn sequence. To traverse each edge exactly once is to use each of the 16 four-digit sequences exactly once.

For example, suppose we follow the following Eulerian path through these vertices:

000, 000, 001, 011, 111, 111, 110, 101, 011,

110, 100, 001, 010, 101, 010, 100, 000.

These are the output sequences of length *k*:

0 0 0 0

_ 0 0 0 1

_ _ 0 0 1 1

This corresponds to the following de Bruijn sequence:

0 0 0 0 1 1 1 1 0 1 1 0 0 1 0 1

The eight vertices appear in the sequence in the following way:

```
      {0  0  0  0} 1  1  1  1  0  1  1  0  0  1  0  1
       0 {0  0  0  1} 1  1  1  0  1  1  0  0  1  0  1
       0  0 {0  0  1  1} 1  1  0  1  1  0  0  1  0  1
       0  0  0 {0  1  1  1} 1  0  1  1  0  0  1  0  1
       0  0  0  0 {1  1  1  1} 0  1  1  0  0  1  0  1
       0  0  0  0  1 {1  1  1  0} 1  1  0  0  1  0  1
       0  0  0  0  1  1 {1  1  0  1} 1  0  0  1  0  1
       0  0  0  0  1  1  1 {1  0  1  1} 0  0  1  0  1
       0  0  0  0  1  1  1  1 {0  1  1  0} 0  1  0  1
       0  0  0  0  1  1  1  1  0 {1  1  0  0} 1  0  1
       0  0  0  0  1  1  1  1  0  1 {1  0  0  1} 0  1
       0  0  0  0  1  1  1  1  0  1  1 {0  0  1  0} 1
       0  0  0  0  1  1  1  1  0  1  1  0 {0  1  0  1}
       0} 0  0  0  1  1  1  1  0  1  1  0  0 {1  0  1 ...
   ... 0  0} 0  0  1  1  1  1  0  1  1  0  0  1 {0  1 ...
   ... 0  0  0} 0  1  1  1  1  0  1  1  0  0  1  0 {1 ...
```

...and then we return to the starting point. Each of the eight 3-digit sequences (corresponding to the eight vertices) appears exactly twice, and each of the sixteen 4-digit sequences (corresponding to the 16 edges) appears exactly once.

### Example using inverse Burrows—Wheeler transform

Mathematically, an inverse Burrows—Wheeler transform on a word w generates a multi-set of equivalence classes consisting of strings and their rotations. These equivalence classes of strings each contain a Lyndon word as a unique minimum element, so the inverse Burrows—Wheeler transform can be considered to generate a set of Lyndon words. It can be shown that if we perform the inverse Burrows—Wheeler transform on a word w consisting of the size-*k* alphabet repeated *k**n*−1 times (so that it will produce a word the same length as the desired de Bruijn sequence), then the result will be the set of all Lyndon words whose length divides *n*. It follows that arranging these Lyndon words in lexicographic order will yield a de Bruijn sequence *B*(*k*,*n*), and that this will be the first de Bruijn sequence in lexicographic order. The following method can be used to perform the inverse Burrows—Wheeler transform, using its *standard permutation*:

1. Sort the characters in the string w, yielding a new string w′
2. Position the string w′ above the string w, and map each letter's position in w′ to its position in w while preserving order. This process defines the Standard Permutation.
3. Write this permutation in cycle notation with the smallest position in each cycle first, and the cycles sorted in increasing order.
4. For each cycle, replace each number with the corresponding letter from string w′ in that position.
5. Each cycle has now become a Lyndon word, and they are arranged in lexicographic order, so dropping the parentheses yields the first de Bruijn sequence.

For example, to construct the smallest *B*(2,4) de Bruijn sequence of length 24 = 16, repeat the alphabet (ab) 8 times yielding *w*=abababababababab. Sort the characters in w, yielding *w′*=aaaaaaaabbbbbbbb. Position w′ above w as shown, and map each element in w′ to the corresponding element in w by drawing a line. Number the columns as shown so we can read the cycles of the permutation:

Starting from the left, the Standard Permutation notation cycles are: (1) (2 3 5 9) (4 7 13 10) (6 11) (8 15 14 12) (16). (Standard Permutation)

Then, replacing each number by the corresponding letter in w′ from that column yields: (a)(aaab)(aabb)(ab)(abbb)(b).

These are all of the Lyndon words whose length divides 4, in lexicographic order, so dropping the parentheses gives *B*(2,4) = aaaabaabbababbbb.

### Algorithm

The following Python code calculates a de Bruijn sequence, given *k* and *n*, based on an algorithm from Frank Ruskey's *Combinatorial Generation*.

```mw
from typing import Iterable, Any

def de_bruijn(k: Iterable[str] | int, n: int) -> str:
    """de Bruijn sequence for alphabet k and subsequences of length n,
    from the concatenation of Lyndon words with lengths that divide n.
    """
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..
    if isinstance(k, int):
        alphabet = list(map(str, range(k)))
    else:
        # While any sort of list becomes used as it is
        alphabet = k
        k = len(k)

    buffer = [0] * n
    sequence = []

    # Recursive method to iterate through Lyndon words in the buffer.
    def generate(word_len, period):
        if word_len >= n:
            if n % period == 0:
                # This Lyndon word divides n, so we join it to the end.
                sequence.extend(buffer[:period])

            # No word longer than n can divide n,
            # so there's no need to recurse further in this case.
            return
 
        # Extend the current word cyclically.
        # Except when initializing the very first entry with 0,
        # this does not produce a new Lyndon word by itself
        # because either the extended sequence is not lexicographically minimal
        # or it is periodic.
        buffer[word_len] = 0 if word_len == 0 else buffer[word_len - period]
        generate(word_len + 1, period)

        # Walk through the alphabet at the end of the word, breaking the old periodicity.
        while buffer[word_len] + 1 < k:
            buffer[word_len] += 1
            generate(word_len + 1, word_len + 1)

    generate(0, 1)

    return "".join(alphabet[i] for i in sequence)

print(de_bruijn(2, 3))
print(de_bruijn("abcd", 2))
```

which prints

```
00010111
aabacadbbcbdccdd
```

Note that these sequences are understood to "wrap around" in a cycle. For example, the first sequence contains 110 and 100 in this fashion.

## Uses

de Bruijn cycles are of general use in neuroscience and psychology experiments that examine the effect of stimulus order upon neural systems, and can be specially crafted for use with functional magnetic resonance imaging.

### Angle detection

The symbols of a de Bruijn sequence written around a circular object (such as a wheel of a robot) can be used to identify its angle by examining the *n* consecutive symbols facing a fixed point. This angle-encoding problem is known as the "rotating drum problem". Gray codes can be used as similar rotary positional encoding mechanisms, a method commonly found in rotary encoders.

### Finding least- or most-significant set bit in a word

A de Bruijn sequence can be used to quickly find the index of the least significant set bit ("right-most 1") or the most significant set bit ("left-most 1") in a word using bitwise operations and multiplication. The following example uses a de Bruijn sequence to determine the index of the least significant set bit (equivalent to counting the number of trailing '0' bits) in a 32 bit unsigned integer:

```mw
uint8_t lowestBitIndex(uint32_t v)
{       
  static const uint8_t BitPositionLookup[32] = // hash table
  {
    0, 1, 28, 2, 29, 14, 24, 3, 30, 22, 20, 15, 25, 17, 4, 8, 
    31, 27, 13, 23, 21, 19, 16, 7, 26, 12, 18, 6, 11, 5, 10, 9
  };
  return BitPositionLookup[((uint32_t)((v & -v) * 0x077CB531U)) >> 27];
}
```

The `lowestBitIndex()` function returns the index of the least-significant set bit in *v*, or zero if *v* has no set bits. The constant 0x077CB531U in the expression is the *B* (2, 5) sequence 0000 0111 0111 1100 1011 0101 0011 0001 (spaces added for clarity). The operation `(v & -v)` zeros all bits except the least-significant bit set, resulting in a new value which is a power of 2. This power of 2 is multiplied (arithmetic modulo 232) by the de Bruijn sequence, thus producing a 32-bit product in which the bit sequence of the 5 MSBs is unique for each power of 2. The 5 MSBs are shifted into the LSB positions to produce a hash code in the range [0, 31], which is then used as an index into hash table BitPositionLookup. The selected hash table value is the bit index of the least significant set bit in *v*.

The following example determines the index of the most significant bit set in a 32 bit unsigned integer:

```mw
uint32_t keepHighestBit(uint32_t n)
{
    n |= (n >>  1);
    n |= (n >>  2);
    n |= (n >>  4);
    n |= (n >>  8);
    n |= (n >> 16);
    return n - (n >> 1);
}

uint8_t highestBitIndex(uint32_t v)
{
    static const uint8_t BitPositionLookup[32] = { // hash table
         0,  1, 16,  2, 29, 17,  3, 22, 30, 20, 18, 11, 13,  4,  7, 23,
        31, 15, 28, 21, 19, 10, 12,  6, 14, 27,  9,  5, 26,  8, 25, 24,
    };
    return BitPositionLookup[(keepHighestBit(v) * 0x06EB14F9U) >> 27];
}
```

In the above example an alternative de Bruijn sequence (0x06EB14F9U) is used, with corresponding reordering of array values. The choice of this particular de Bruijn sequence is arbitrary, but the hash table values must be ordered to match the chosen de Bruijn sequence. The `keepHighestBit()` function zeros all bits except the most-significant set bit, resulting in a value which is a power of 2, which is then processed as in the previous example.

### Brute-force attacks on locks

A de Bruijn sequence can be used to shorten a brute-force attack on a PIN-like code lock that does not have an "enter" key and accepts the last *n* digits entered. For example, a digital door lock with a 4-digit code (each digit having 10 possibilities, from 0 to 9) would have *B* (10, 4) solutions, with length 10000. Therefore, only at most 10000 + 3 = 10003 (as the solutions are cyclic) presses are needed to open the lock, whereas trying all codes separately would require 4 × 10000 = 40000 presses.

## Multi de Bruijn sequences

Multi de Bruijn sequence: a cyclic or linear sequence that contains every k-mer over an alphabet of size q exactly m times . For example, over the binary alphabet {0, 1}, the cyclic sequence (00010111) and the linear sequence 000101110 each contain two instances of each 2-mer 00, 01, 10, 11. There are two sequences for multiplicity m=2, alphabet size q = 2, and word size k=1: (0011), and (0101), and 5 for k=2.

## de Bruijn torus

A de Bruijn torus is a toroidal array with the property that every *k*-ary *m*-by-*n* matrix occurs exactly once.

Such a pattern can be used for two-dimensional positional encoding in a fashion analogous to that described above for rotary encoding. Position can be determined by examining the *m*-by-*n* matrix directly adjacent to the sensor, and calculating its position on the de Bruijn torus.

## de Bruijn decoding

Computing the position of a particular unique tuple or matrix in a de Bruijn sequence or torus is known as the *de Bruijn decoding problem*. Efficient ⁠ $\color {Blue}O(n\log n)$ ⁠ decoding algorithms exist for special, recursively constructed sequences and extend to the two-dimensional case. de Bruijn decoding is of interest, e.g., in cases where large sequences or tori are used for positional encoding.
