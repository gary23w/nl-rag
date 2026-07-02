---
title: "Permutation (part 2/2)"
source: https://en.wikipedia.org/wiki/Permutation
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
part: 2/2
---

## Permutations in computing

### Numbering permutations

One way to represent permutations of *n* things is by an integer *N* with 0 ≤ *N* < *n*!, provided convenient methods are given to convert between the number and the representation of a permutation as an ordered arrangement (sequence). This gives the most compact representation of arbitrary permutations, and in computing is particularly attractive when *n* is small enough that *N* can be held in a machine word; for 32-bit words this means *n* ≤ 12, and for 64-bit words this means *n* ≤ 20. The conversion can be done via the intermediate form of a sequence of numbers *d**n*, *d**n*−1, ..., *d*2, *d*1, where *d**i* is a non-negative integer less than *i* (one may omit *d*1, as it is always 0, but its presence makes the subsequent conversion to a permutation easier to describe). The first step then is to simply express *N* in the *factorial number system*, which is just a particular mixed radix representation, where, for numbers less than *n*!, the bases (place values or multiplication factors) for successive digits are (*n* − 1)!, (*n* − 2)!, ..., 2!, 1!. The second step interprets this sequence as a Lehmer code or (almost equivalently) as an inversion table.

Rothe diagram for

$\sigma =(6,3,8,1,4,9,7,2,5)$

σ

i

i

1

2

3

4

5

6

7

8

9

Lehmer code

1

×

×

×

×

×

•

d

9

= 5

2

×

×

•

d

8

= 2

3

×

×

×

×

×

•

d

7

= 5

4

•

d

6

= 0

5

×

•

d

5

= 1

6

×

×

×

•

d

4

= 3

7

×

×

•

d

3

= 2

8

•

d

2

= 0

9

•

d

1

= 0

Inversion table

3

6

1

2

4

0

2

0

0

In the **Lehmer code** for a permutation *σ*, the number *d**n* represents the choice made for the first term *σ*1, the number *d**n*−1 represents the choice made for the second term *σ*2 among the remaining *n* − 1 elements of the set, and so forth. More precisely, each *d**n*+1−*i* gives the number of *remaining* elements strictly less than the term *σ**i*. Since those remaining elements are bound to turn up as some later term *σ**j*, the digit *d**n*+1−*i* counts the *inversions* (*i*,*j*) involving *i* as smaller index (the number of values *j* for which *i* < *j* and *σ**i* > *σ**j*). The **inversion table** for *σ* is quite similar, but here *d**n*+1−*k* counts the number of inversions (*i*,*j*) where *k* = *σ**j* occurs as the smaller of the two values appearing in inverted order.

Both encodings can be visualized by an *n* by *n* **Rothe diagram** (named after Heinrich August Rothe) in which dots at (*i*,*σ**i*) mark the entries of the permutation, and a cross at (*i*,*σ**j*) marks the inversion (*i*,*j*); by the definition of inversions a cross appears in any square that comes both before the dot (*j*,*σ**j*) in its column, and before the dot (*i*,*σ**i*) in its row. The Lehmer code lists the numbers of crosses in successive rows, while the inversion table lists the numbers of crosses in successive columns; it is just the Lehmer code for the inverse permutation, and vice versa.

To effectively convert a Lehmer code *d**n*, *d**n*−1, ..., *d*2, *d*1 into a permutation of an ordered set *S*, one can start with a list of the elements of *S* in increasing order, and for *i* increasing from 1 to *n* set *σ**i* to the element in the list that is preceded by *d**n*+1−*i* other ones, and remove that element from the list. To convert an inversion table *d**n*, *d**n*−1, ..., *d*2, *d*1 into the corresponding permutation, one can traverse the numbers from *d*1 to *d**n* while inserting the elements of *S* from largest to smallest into an initially empty sequence; at the step using the number *d* from the inversion table, the element from *S* inserted into the sequence at the point where it is preceded by *d* elements already present. Alternatively one could process the numbers from the inversion table and the elements of *S* both in the opposite order, starting with a row of *n* empty slots, and at each step place the element from *S* into the empty slot that is preceded by *d* other empty slots.

Converting successive natural numbers to the factorial number system produces those sequences in lexicographic order (as is the case with any mixed radix number system), and further converting them to permutations preserves the lexicographic ordering, provided the Lehmer code interpretation is used (using inversion tables, one gets a different ordering, where one starts by comparing permutations by the *place* of their entries 1 rather than by the value of their first entries). The sum of the numbers in the factorial number system representation gives the number of inversions of the permutation, and the parity of that sum gives the signature of the permutation. Moreover, the positions of the zeroes in the inversion table give the values of left-to-right maxima of the permutation (in the example 6, 8, 9) while the positions of the zeroes in the Lehmer code are the positions of the right-to-left minima (in the example positions the 4, 8, 9 of the values 1, 2, 5); this allows computing the distribution of such extrema among all permutations. A permutation with Lehmer code *d**n*, *d**n*−1, ..., *d*2, *d*1 has an ascent *n* − *i* if and only if *d**i* ≥ *d**i*+1.

### Algorithms to generate permutations

In computing it may be required to generate permutations of a given sequence of values. The methods best adapted to do this depend on whether one wants some randomly chosen permutations, or all permutations, and in the latter case if a specific ordering is required. Another question is whether possible equality among entries in the given sequence is to be taken into account; if so, one should only generate distinct multiset permutations of the sequence.

An obvious way to generate permutations of *n* is to generate values for the Lehmer code (possibly using the factorial number system representation of integers up to *n*!), and convert those into the corresponding permutations. However, the latter step, while straightforward, is hard to implement efficiently, because it requires *n* operations each of selection from a sequence and deletion from it, at an arbitrary position; of the obvious representations of the sequence as an array or a linked list, both require (for different reasons) about *n*2/4 operations to perform the conversion. With *n* likely to be rather small (especially if generation of all permutations is needed) that is not too much of a problem, but it turns out that both for random and for systematic generation there are simple alternatives that do considerably better. For this reason it does not seem useful, although certainly possible, to employ a special data structure that would allow performing the conversion from Lehmer code to permutation in *O*(*n* log *n*) time.

#### Random generation of permutations

For generating random permutations of a given sequence of *n* values, it makes no difference whether one applies a randomly selected permutation of *n* to the sequence, or chooses a random element from the set of distinct (multiset) permutations of the sequence. This is because, even though in case of repeated values there can be many distinct permutations of *n* that result in the same permuted sequence, the number of such permutations is the same for each possible result. Unlike for systematic generation, which becomes unfeasible for large *n* due to the growth of the number *n*!, there is no reason to assume that *n* will be small for random generation.

The basic idea to generate a random permutation is to generate at random one of the *n*! sequences of integers *d*1,*d*2,...,*d**n* satisfying 0 ≤ *d**i* < *i* (since *d*1 is always zero it may be omitted) and to convert it to a permutation through a bijective correspondence. For the latter correspondence one could interpret the (reverse) sequence as a Lehmer code, and this gives a generation method first published in 1938 by Ronald Fisher and Frank Yates. While at the time computer implementation was not an issue, this method suffers from the difficulty sketched above to convert from Lehmer code to permutation efficiently. This can be remedied by using a different bijective correspondence: after using *d**i* to select an element among *i* remaining elements of the sequence (for decreasing values of *i*), rather than removing the element and compacting the sequence by shifting down further elements one place, one swaps the element with the final remaining element. Thus the elements remaining for selection form a consecutive range at each point in time, even though they may not occur in the same order as they did in the original sequence. The mapping from sequence of integers to permutations is somewhat complicated, but it can be seen to produce each permutation in exactly one way, by an immediate induction. When the selected element happens to be the final remaining element, the swap operation can be omitted. This does not occur sufficiently often to warrant testing for the condition, but the final element must be included among the candidates of the selection, to guarantee that all permutations can be generated.

The resulting algorithm for generating a random permutation of `*a*[0], *a*[1], ..., *a*[*n* − 1]` can be described as follows in pseudocode:

```
for i from n downto 2 do
    di ← random element of { 0, ..., i − 1 }
    swap a[di] and a[i − 1]
```

This can be combined with the initialization of the array `*a*[*i*] = *i*` as follows

```
for i from 0 to n−1 do
    di+1 ← random element of { 0, ..., i }
    a[i] ← a[di+1]
    a[di+1] ← i
```

If *d**i*+1 = *i*, the first assignment will copy an uninitialized value, but the second will overwrite it with the correct value *i*.

However, Fisher-Yates is not the fastest algorithm for generating a permutation, because Fisher-Yates is essentially a sequential algorithm and "divide and conquer" procedures can achieve the same result in parallel.

#### Generation in lexicographic order

There are many ways to systematically generate all permutations of a given sequence. One classic, simple, and flexible algorithm is based upon finding the next permutation in lexicographic ordering, if it exists. It can handle repeated values, for which case it generates each distinct multiset permutation once. Even for ordinary permutations it is significantly more efficient than generating values for the Lehmer code in lexicographic order (possibly using the factorial number system) and converting those to permutations. It begins by sorting the sequence in (weakly) increasing order (which gives its lexicographically minimal permutation), and then repeats advancing to the next permutation as long as one is found. The method goes back to Narayana Pandita in 14th century India, and has been rediscovered frequently.

The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

1. Find the largest index *k* such that *a*[*k*] < *a*[*k* + 1]. If no such index exists, the permutation is the last permutation.
2. Find the largest index *l* greater than *k* such that *a*[*k*] < *a*[*l*].
3. Swap the value of *a*[*k*] with that of *a*[*l*].
4. Reverse the sequence from *a*[*k* + 1] up to and including the final element *a*[*n*].

For example, given the sequence [1, 2, 3, 4] (which is in increasing order), and given that the index is zero-based, the steps are as follows:

1. Index *k* = 2, because 3 is placed at an index that satisfies condition of being the largest index that is still less than *a*[*k* + 1] which is 4.
2. Index *l* = 3, because 4 is the only value in the sequence that is greater than 3 in order to satisfy the condition *a*[*k*] < *a*[*l*].
3. The values of *a*[2] and *a*[3] are swapped to form the new sequence [1, 2, 4, 3].
4. The sequence after *k*-index *a*[2] to the final element is reversed. Because only one value lies after this index (the 3), the sequence remains unchanged in this instance. Thus the lexicographic successor of the initial state is permuted: [1, 2, 4, 3].

Following this algorithm, the next lexicographic permutation will be [1, 3, 2, 4], and the 24th permutation will be [4, 3, 2, 1] at which point *a*[*k*] < *a*[*k* + 1] does not exist, indicating that this is the last permutation.

This method uses about 3 comparisons and 1.5 swaps per permutation, amortized over the whole sequence, not counting the initial sort.

#### Generation with minimal changes

An alternative to the above algorithm, the Steinhaus–Johnson–Trotter algorithm, generates an ordering on all the permutations of a given sequence with the property that any two consecutive permutations in its output differ by swapping two adjacent values. This ordering on the permutations was known to 17th-century English bell ringers, among whom it was known as "plain changes". One advantage of this method is that the small amount of change from one permutation to the next allows the method to be implemented in constant time per permutation. The same can also easily generate the subset of even permutations, again in constant time per permutation, by skipping every other output permutation.

An alternative to Steinhaus–Johnson–Trotter is Heap's algorithm, said by Robert Sedgewick in 1977 to be the fastest algorithm of generating permutations in applications.

The following figure shows the output of all three aforementioned algorithms for generating all permutations of length $n=4$ , and of six additional algorithms described in the literature.

1. Lexicographic ordering;
2. Steinhaus–Johnson–Trotter algorithm;
3. Heap's algorithm;
4. Ehrlich's star-transposition algorithm: in each step, the first entry of the permutation is exchanged with a later entry;
5. Zaks' prefix reversal algorithm: in each step, a prefix of the current permutation is reversed to obtain the next permutation;
6. Sawada-Williams' algorithm: each permutation differs from the previous one either by a cyclic left-shift by one position, or an exchange of the first two entries;
7. Corbett's algorithm: each permutation differs from the previous one by a cyclic left-shift of some prefix by one position;
8. Single-track ordering: each column is a cyclic shift of the other columns;
9. Single-track Gray code: each column is a cyclic shift of the other columns, plus any two consecutive permutations differ only in one or two transpositions.
10. Nested swaps generating algorithm in steps connected to the nested subgroups $S_{k}\subset S_{k+1}$ . Each permutation is obtained from the previous by a transposition multiplication to the left. Algorithm is connected to the Factorial number system of the index.

#### Generation of permutations in nested swap steps

Explicit sequence of swaps (transpositions, 2-cycles $(pq)$ ), is described here, each swap applied (on the left) to the previous chain providing a new permutation, such that all the permutations can be retrieved, each only once. This counting/generating procedure has an additional structure (call it nested), as it is given in steps: after completely retrieving $S_{k-1}$ , continue retrieving $S_{k}\backslash S_{k-1}$ by cosets $S_{k-1}\tau _{i}$ of $S_{k-1}$ in $S_{k}$ , by appropriately choosing the coset representatives $\tau _{i}$ to be described below. Since each $S_{m}$ is sequentially generated, there is a *last element* $\lambda _{m}\in S_{m}$ . So, after generating $S_{k-1}$ by swaps, the next permutation in $S_{k}\backslash S_{k-1}$ has to be $\tau _{1}=(p_{1}k)\lambda _{k-1}$ for some $1\leq p_{1}<k$ . Then all swaps that generated $S_{k-1}$ are repeated, generating the whole coset $S_{k-1}\tau _{1}$ , reaching the last permutation in that coset $\lambda _{k-1}\tau _{1}$ ; the next swap has to move the permutation to representative of another coset $\tau _{2}=(p_{2}k)\lambda _{k-1}\tau _{1}$ .

Continuing the same way, one gets coset representatives $\tau _{j}=(p_{j}k)\lambda _{k-1}\cdots$ $\lambda _{k-1}(p_{i}k)\lambda _{k-1}$ $\cdots \lambda _{k-1}(p_{1}k)\lambda _{k-1}$ for the cosets of $S_{k-1}$ in $S_{k}$ ; the ordered set $(p_{1},\ldots ,p_{k-1})$ ( $0\leq p_{i}<k$ ) is called the set of coset beginnings. Two of these representatives are in the same coset if and only if $\tau _{j}(\tau _{i})^{-1}=$ $(p_{j}k)\lambda _{k-1}(p_{j-1}k)\lambda _{k-1}\cdots$ $\lambda _{k-1}(p_{i+1}k)=$ $\varkappa _{ij}\in S_{k-1}$ , that is, $\varkappa _{ij}(k)=k$ . Concluding, permutations $\tau _{i}\in S_{k}-S_{k-1}$ are all representatives of distinct cosets if and only if for any $k>j>i\geq 1$ , $(\lambda _{k-1})^{j-i}p_{i}\neq p_{j}$ (no repeat condition). In particular, for all generated permutations to be distinct it is not necessary for the $p_{i}$ values to be distinct. In the process, one gets that $\lambda _{k}=\lambda _{k-1}(p_{k-1}k)$ $\lambda _{k-1}(p_{k-2}k)$ $\lambda _{k-1}\cdots$ $\lambda _{k-1}(p_{1}k)$ $\lambda _{k-1}$ and this provides the recursion procedure.

EXAMPLES: obviously, for $\lambda _{2}$ one has $\lambda _{2}=(12)$ ; to build $\lambda _{3}$ there are only two possibilities for the coset beginnings satisfying the no repeat condition; the choice $p_{1}=p_{2}=1$ leads to $\lambda _{3}=\lambda _{2}(13)\lambda _{2}(13)\lambda _{2}=(13)$ . To continue generating $S_{4}$ one needs appropriate coset beginnings (satisfying the no repeat condition): there is a convenient choice: $p_{1}=1,p_{2}=2,p_{3}=3$ , leading to $\lambda _{4}=(13)(1234)(13)=(1432)$ . Then, to build $\lambda _{5}$ a convenient choice for the coset beginnings (satisfying the no repeat condition) is $p_{1}=p_{2}=p_{3}=p_{4}=1$ , leading to $\lambda _{5}=(15)$ .

From examples above one can inductively go to higher k in a similar way, choosing coset beginnings of $S_{k}$ in $S_{k+1}$ , as follows: for k even choosing all coset beginnings equal to 1 and for k odd choosing coset beginnings equal to $(1,2,\dots ,k)$ . With such choices the "last" permutation is $\lambda _{k}=(1k)$ for k odd and $\lambda _{k}=(1k_{-})(12\cdots k)(1k_{-})$ for k even ( $k_{-}=k-1$ ). Using these explicit formulae one can easily compute the permutation of certain index in the counting/generation steps with minimum computation. For this, writing the index in factorial base is useful. For example, the permutation for index $699=5(5!)+4(4!)+1(2!)+1(1!)$ is: $\sigma =\lambda _{2}(13)$ $\lambda _{2}(15)$ $\lambda _{4}(15)$ $\lambda _{4}(15)$ $\lambda _{4}(15)$ $\lambda _{4}(56)$ $\lambda _{5}(46)$ $\lambda _{5}(36)$ $\lambda _{5}(26)$ $\lambda _{5}(16)$ $\lambda _{5}=$ $\lambda _{2}(13)\lambda _{2}((15)\lambda _{4})^{4}(\lambda _{5})^{-1}\lambda _{6}=(23)$ $(14325)^{-1}$ $(15)$ $(15)$ $(123456)$ $(15)=$ $(23)$ $(15234)$ $(123456)(15)$ , yielding finally, $\sigma =(1653)(24)$ .

Because multiplying by swap permutation takes short computing time and every new generated permutation requires only one such swap multiplication, this generation procedure is quite efficient. Moreover, as there is a simple formula, having the last permutation in each $S_{k}$ can save even more time to go directly to a permutation with certain index in fewer steps than expected as it can be done in blocks of subgroups rather than swap by swap.

### Applications

Permutations are used in the interleaver component of the error detection and correction algorithms, such as turbo codes, for example 3GPP Long Term Evolution mobile telecommunication standard uses these ideas (see 3GPP technical specification 36.212). Such applications raise the question of fast generation of permutations satisfying certain desirable properties. One of the methods is based on the permutation polynomials. Also as a base for optimal hashing in Unique Permutation Hashing.
