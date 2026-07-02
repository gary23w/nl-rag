---
title: "LCP array"
source: https://en.wikipedia.org/wiki/LCP_array
domain: suffix-array-index
license: CC-BY-SA-4.0
tags: suffix array, lcp array, fm-index, burrows-wheeler transform
fetched: 2026-07-02
---

# LCP array

In computer science, the **longest common prefix array** (**LCP array**) is an auxiliary data structure to the suffix array. It stores the lengths of the longest common prefixes (LCPs) between all pairs of consecutive suffixes in a sorted suffix array.

For example, if *A* := [aab, ab, abaab, b, baab] is a suffix array, the longest common prefix between *A*[1] = aab and *A*[2] = ab is *a* which has length 1, so *H*[2] = 1 in the LCP array *H*. Likewise, the LCP of *A*[2] = ab and *A*[3] = abaab is ab, so *H*[3] = 2.

Augmenting the suffix array with the LCP array allows one to efficiently simulate top-down and bottom-up traversals of the suffix tree, speeds up pattern matching on the suffix array and is a prerequisite for compressed suffix trees.

## History

The LCP array was introduced in 1993, by Udi Manber and Gene Myers alongside the suffix array in order to improve the running time of their string search algorithm.

## Definition

Let A be the suffix array of the string $S=s_{1},s_{2},\ldots s_{n-1}\$$ of length n , where $\$$ is a sentinel letter that is unique and lexicographically smaller than any other character. Let $S[i,j]$ denote the substring of S ranging from i to j . Thus, $S[A[i],n]$ is the i th smallest suffix of S .

Let $\operatorname {lcp} (v,w)$ denote the length of the longest common prefix between two strings v and w . Then the LCP array $H[1,n]$ is an integer array of size n such that $H[1]$ is undefined and $H[i]=\operatorname {lcp} (S[A[i-1],n],S[A[i],n])$ for every $1<i\leq n$ . Thus $H[i]$ stores the length of longest common prefix of the lexicographically i th smallest suffix and its predecessor in the suffix array.

Difference between LCP array and suffix array:

- Suffix array: Represents the lexicographic rank of each suffix of an array.
- LCP array: Contains the maximum length prefix match between two consecutive suffixes, after they are sorted lexicographically.

## Example

Consider the string $S={\textrm {banana\$}}$ :

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| S[i] | b | a | n | a | n | a | $ |

and its corresponding sorted suffix array A  :

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| A[i] | 7 | 6 | 4 | 2 | 1 | 5 | 3 |

Suffix array with suffixes written out underneath vertically:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| A[i] | 7 | 6 | 4 | 2 | 1 | 5 | 3 |
| S[A[i], n][1] | $ | a | a | a | b | n | n |
| S[A[i], n][2] |   | $ | n | n | a | a | a |
| S[A[i], n][3] |   |   | a | a | n | $ | n |
| S[A[i], n][4] |   |   | $ | n | a |   | a |
| S[A[i], n][5] |   |   |   | a | n |   | $ |
| S[A[i], n][6] |   |   |   | $ | a |   |   |
| S[A[i], n][7] |   |   |   |   | $ |   |   |

Then the LCP array H is constructed by comparing lexicographically consecutive suffixes to determine their longest common prefix:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| H[i] | undefined | 0 | 1 | 3 | 0 | 0 | 2 |

So, for example, $H[4]=3$ is the length of the longest common prefix ${\text{ana}}$ shared by the suffixes $A[3]=S[4,7]={\textrm {ana\$}}$ and $A[4]=S[2,7]={\textrm {anana\$}}$ . Note that $H[1]$ is undefined, since there is no lexicographically smaller suffix.

## Efficient construction algorithms

LCP array construction algorithms can be divided into two different categories: algorithms that compute the LCP array as a byproduct to the suffix array and algorithms that use an already constructed suffix array in order to compute the LCP values.

Manber & Myers (1993) provide an algorithm to compute the LCP array alongside the suffix array in $O(n\log n)$ time. Kärkkäinen & Sanders (2003) show that it is also possible to modify their $O(n)$ time algorithm such that it computes the LCP array as well. Kasai et al. (2001) present the first $O(n)$ time algorithm (FLAAP) that computes the LCP array given the text and the suffix array.

Assuming that each text symbol takes one byte and each entry of the suffix or LCP array takes 4 bytes, the major drawback of their algorithm is a large space occupancy of $13n$ bytes, while the original output (text, suffix array, LCP array) only occupies $9n$ bytes. Therefore, Manzini (2004) created a refined version of the algorithm of Kasai et al. (2001) (lcp9) and reduced the space occupancy to $9n$ bytes. Kärkkäinen, Manzini & Puglisi (2009) provide another refinement of Kasai's algorithm ( $\Phi$ -algorithm) that improves the running time. Rather than the actual LCP array, this algorithm builds the *permuted* LCP (PLCP) array, in which the values appear in text order rather than lexicographical order.

Gog & Ohlebusch (2011) provide two algorithms that although being theoretically slow ( $O(n^{2})$ ) were faster than the above-mentioned algorithms in practice.

As of 2012, the currently fastest linear-time LCP array construction algorithm is due to Fischer (2011), which in turn is based on one of the fastest suffix array construction algorithms (SA-IS) by Nong, Zhang & Chan (2009). Fischer & Kurpicz (2017) based on Yuta Mori's DivSufSort is even faster.

## Applications

As noted by Abouelhoda, Kurtz & Ohlebusch (2004) several string processing problems can be solved by the following kinds of tree traversals:

- bottom-up traversal of the complete suffix tree
- top-down traversal of a subtree of the suffix tree
- suffix tree traversal using the suffix links.

Kasai et al. (2001) show how to simulate a bottom-up traversal of the suffix tree using only the suffix array and LCP array. Abouelhoda, Kurtz & Ohlebusch (2004) enhance the suffix array with the LCP array and additional data structures and describe how this *enhanced suffix array* can be used to simulate *all three kinds* of suffix tree traversals. Fischer & Heun (2007) reduce the space requirements of the enhanced suffix array by preprocessing the LCP array for range minimum queries. Thus, *every* problem that can be solved by suffix tree algorithms can also be solved using the *enhanced suffix array*.

Deciding if a pattern P of length m is a substring of a string S of length n takes $O(m\log n)$ time if only the suffix array is used. By additionally using the LCP information, this bound can be improved to $O(m+\log n)$ time. Abouelhoda, Kurtz & Ohlebusch (2004) show how to improve this running time even further to achieve optimal $O(m)$ time. Thus, using suffix array and LCP array information, the decision query can be answered as fast as using the suffix tree.

The LCP array is also an essential part of compressed suffix trees which provide full suffix tree functionality like suffix links and lowest common ancestor queries. Furthermore, it can be used together with the suffix array to compute the Lempel-Ziv LZ77 factorization in $O(n)$ time.

The longest repeated substring problem for a string S of length n can be solved in $\Theta (n)$ time using both the suffix array A and the LCP array. It is sufficient to perform a linear scan through the LCP array in order to find its maximum value $v_{max}$ and the corresponding index i where $v_{max}$ is stored. The longest substring that occurs at least twice is then given by $S[A[i],A[i]+v_{max}-1]$ .

The remainder of this section explains two applications of the LCP array in more detail: How the suffix array and the LCP array of a string can be used to construct the corresponding suffix tree and how it is possible to answer LCP queries for arbitrary suffixes using range minimum queries on the LCP array.

### Find the number of occurrences of a pattern

In order to find the number of occurrences of a given string P (length m ) in a text T (length N ),

- We use binary search against the suffix array of T to find the starting and end position of all occurrences of P .
- Now to speed up the search, we use LCP array, specifically a special version of the LCP array (LCP-LR below).

The issue with using standard binary search (without the LCP information) is that in each of the $O(\log N)$ comparisons needed to be made, we compare P to the current entry of the suffix array, which means a full string comparison of up to m characters. So the complexity is $O(m\log N)$ .

The LCP-LR array helps improve this to $O(m+\log N)$ , in the following way:

At any point during the binary search algorithm, we consider, as usual, a range $(L,\dots ,R)$ of the suffix array and its central point M , and decide whether we continue our search in the left sub-range $(L,\dots ,M)$ or in the right sub-range $(M,\dots ,R)$ . In order to make the decision, we compare P to the string at M . If P is identical to M , our search is complete. But if not, we have already compared the first k characters of P and then decided whether P is lexicographically smaller or larger than M . Let's assume the outcome is that P is larger than M . So, in the next step, we consider $(M,\dots ,R)$ and a new central point $M'$ in the middle:

```
             M ...... M' ...... R
             |
      we know:
         lcp(P,M)==k
```

The trick now is that LCP-LR is precomputed such that an $O(1)$ -lookup tells us the longest common prefix of M and $M'$ , $\mathrm {lcp} (M,M')$ .

We already know (from the previous step) that M itself has a prefix of k characters in common with P : $\mathrm {lcp} (P,M)=k$ . Now there are three possibilities:

- Case 1: $k<\mathrm {lcp} (M,M')$ , i.e. P has fewer prefix characters in common with M than M has in common with M'. This means the (k+1)-th character of M' is the same as that of M, and since P is lexicographically larger than M, it must be lexicographically larger than M', too. So we continue in the right half (M',...,R).
- Case 2: $k>\mathrm {lcp} (M,M')$ , i.e. P has more prefix characters in common with M than M has in common with $M'$ . Consequently, if we were to compare P to $M'$ , the common prefix would be smaller than k , and $M'$ would be lexicographically larger than P , so, without actually making the comparison, we continue in the left half $(M,\dots ,M')$ .
- Case 3: $k=\mathrm {lcp} (M,M')$ . So M and M' are both identical with P in the first k characters. To decide whether we continue in the left or right half, it suffices to compare P to $M'$ starting from the $(k+1)$ th character.
- We continue recursively.

The overall effect is that no character of P is compared to any character of the text more than once (for details see ). The total number of character comparisons is bounded by m , so the total complexity is indeed $O(m+\log N)$ .

We still need to precompute LCP-LR so it is able to tell us in $O(1)$ time the lcp between any two entries of the suffix array. We know the standard LCP array gives us the lcp of consecutive entries only, i.e. $\mathrm {lcp} (i-1,i)$ for any i . However, M and $M'$ in the description above are not necessarily consecutive entries.

The key to this is to realize that only certain ranges $(L,\dots ,R)$ will ever occur during the binary search: It always starts with $(0,\dots ,N)$ and divides that at the center, and then continues either left or right and divide that half again and so forth. Another way of looking at it is : every entry of the suffix array occurs as central point of exactly one possible range during binary search. So there are exactly N distinct ranges $(L\dots M\dots R)$ that can possibly play a role during binary search, and it suffices to precompute $\mathrm {lcp} (L,M)$ and $\mathrm {lcp} (M,R)$ for those N possible ranges. So that is $2N$ distinct precomputed values, hence LCP-LR is $O(N)$ in size.

Moreover, there is a straightforward recursive algorithm to compute the $2N$ values of LCP-LR in $O(N)$ time from the standard LCP array.

To sum up:

- It is possible to compute LCP-LR in $O(N)$ time and $O(2N)=O(N)$ space from LCP.
- Using LCP-LR during binary search helps accelerate the search procedure from $O(M\log N)$ to $O(M+\log N)$ .
- We can use two binary searches to determine the left and right end of the match range for P , and the length of the match range corresponds with the number of occurrences for P.

### Suffix tree construction

Given the suffix array A and the LCP array H of a string $S=s_{1},s_{2},\ldots s_{n}\$$ of length $n+1$ , its suffix tree $ST$ can be constructed in $O(n)$ time based on the following idea: Start with the partial suffix tree for the lexicographically smallest suffix and repeatedly insert the other suffixes in the order given by the suffix array.

Let $ST_{i}$ be the partial suffix tree for $0\leq i\leq n$ . Further let $d(v)$ be the length of the concatenation of all path labels from the root of $ST_{i}$ to node v .

Start with $ST_{0}$ , the tree consisting only of the root. To insert $A[i+1]$ into $ST_{i}$ , walk up the *rightmost* path beginning at the recently inserted leaf $A[i]$ to the root, until the deepest node v with $d(v)\leq H[i+1]$ is reached.

We need to distinguish two cases:

- $d(v)=H[i+1]$ : This means that the concatenation of the labels on the root-to- v path equals the longest common prefix of suffixes $A[i]$ and $A[i+1]$ . In this case, insert $A[i+1]$ as a new leaf x of node v and label the edge $(v,x)$ with $S[A[i+1]+H[i+1],n]$ . Thus the edge label consists of the remaining characters of suffix $A[i+1]$ that are not already represented by the concatenation of the labels of the root-to- v path. This creates the partial suffix tree $ST_{i+1}$ .
- $d(v)<H[i+1]$ : This means that the concatenation of the labels on the root-to- v path displays less characters than the longest common prefix of suffixes $A[i]$ and $A[i+1]$ and the *missing* characters are contained in the edge label of v 's *rightmost* edge. Therefore, we have to *split up* that edge as follows: Let w be the child of v on $ST_{i}$ 's rightmost path.

1. Delete the edge $(v,w)$ .
2. Add a new internal node y and a new edge $(v,y)$ with label $S[A[i]+d(v),A[i]+H[i+1]-1]$ . The new label consists of the *missing* characters of the longest common prefix of $A[i]$ and $A[i+1]$ . Thus, the concatenation of the labels of the root-to- y path now displays the longest common prefix of $A[i]$ and $A[i+1]$ .
3. Connect w to the newly created internal node y by an edge $(y,w)$ that is labeled $S[A[i]+H[i+1],A[i]+d(w)-1]$ . The new label consists of the *remaining* characters of the deleted edge $(v,w)$ that were not used as the label of edge $(v,y)$ .
4. Add $A[i+1]$ as a new leaf x and connect it to the new internal node y by an edge $(y,x)$ that is labeled $S[A[i+1]+H[i+1],n]$ . Thus the edge label consists of the remaining characters of suffix $A[i+1]$ that are not already represented by the concatenation of the labels of the root-to- v path.
5. This creates the partial suffix tree $ST_{i+1}$ .

A simple amortization argument shows that the running time of this algorithm is bounded by $O(n)$ :

The nodes that are traversed in step i by walking up the *rightmost* path of $ST_{i}$ (apart from the last node v ) are removed from the *rightmost* path, when $A[i+1]$ is added to the tree as a new leaf. These nodes will never be traversed again for all subsequent steps $j>i$ . Therefore, at most $2n$ nodes will be traversed in total.

### LCP queries for arbitrary suffixes

The LCP array H only contains the length of the longest common prefix of every pair of consecutive suffixes in the suffix array A . However, with the help of the inverse suffix array $A^{-1}$ ( $A[i]=j\Leftrightarrow A^{-1}[j]=i$ , i.e. the suffix $S[j,n]$ that starts at position j in S is stored in position $A^{-1}[j]$ in A ) and constant-time range minimum queries on H , it is possible to determine the length of the longest common prefix of arbitrary suffixes in $O(1)$ time.

Because of the lexicographic order of the suffix array, every common prefix of the suffixes $S[i,n]$ and $S[j,n]$ has to be a common prefix of all suffixes between i 's position in the suffix array $A^{-1}[i]$ and j 's position in the suffix array $A^{-1}[j]$ . Therefore, the length of the longest prefix that is shared by *all* of these suffixes is the minimum value in the interval $H[A^{-1}[i]+1,A^{-1}[j]]$ . This value can be found in constant time if H is preprocessed for range minimum queries.

Thus given a string S of length n and two arbitrary positions $i,j$ in the string S with $A^{-1}[i]<A^{-1}[j]$ , the length of the longest common prefix of the suffixes $S[i,n]$ and $S[j,n]$ can be computed as follows: $\operatorname {LCP} (i,j)=H[\operatorname {RMQ} _{H}(A^{-1}[i]+1,A^{-1}[j])]$ .
