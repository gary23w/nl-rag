---
title: "3SUM"
source: https://en.wikipedia.org/wiki/3SUM
domain: fine-grained-complexity
license: CC-BY-SA-4.0
tags: fine grained complexity, fine grained reduction, strong exponential time hypothesis, 3sum conjecture
fetched: 2026-07-02
---

# 3SUM

Unsolved problem in computer science

Is there an algorithm to solve the 3SUM problem in time

$O(n^{2-\epsilon })$

, for some

$\epsilon >0$

?

More unsolved problems in computer science

In computational complexity theory, the **3SUM** problem asks if a given set of n real numbers contains three elements that sum to zero. A generalized version, k -SUM, asks the same question on k elements, rather than simply 3. 3SUM can be easily solved in $O(n^{2})$ time, and matching $\Omega (n^{\lceil k/2\rceil })$ lower bounds are known in some specialized models of computation (Erickson 1999).

It was conjectured that any deterministic algorithm for the 3SUM requires $\Omega (n^{2})$ time. In 2014, the original 3SUM conjecture was refuted by Allan Grønlund and Seth Pettie who gave a deterministic algorithm that solves 3SUM in $O(n^{2}/({\log n}/{\log \log n})^{2/3})$ time. Additionally, Grønlund and Pettie showed that the 4-linear decision tree complexity of 3SUM is $O(n^{3/2}{\sqrt {\log n}})$ . These bounds were subsequently improved. The current best known algorithm for 3SUM runs in $O(n^{2}(\log \log n)^{O(1)}/{\log ^{2}n})$ time. Kane, Lovett, and Moran showed that the 6-linear decision tree complexity of 3SUM is $O(n{\log ^{2}n})$ . The latter bound is tight (up to a logarithmic factor). It is still conjectured that 3SUM is unsolvable in $O(n^{2-\Omega (1)})$ expected time.

When the elements are integers in the range $[-N,\dots ,N]$ , 3SUM can be solved in $O(n+N\log N)$ time by representing the input set S as a bit vector, computing the set $S+S$ of all pairwise sums as a discrete convolution using the fast Fourier transform, and finally comparing this set to S .

## Quadratic algorithm

Suppose the input array is $S[0..n-1]$ . In integer (word RAM) models of computing, 3SUM can be solved in $O(n^{2})$ time on average by inserting each number $S[i]$ into a hash table, and then, for each index i and j , checking whether the hash table contains the integer $-(S[i]+S[j])$ .

It is also possible to solve the problem in the same time in a comparison-based model of computing or real RAM, for which hashing is not allowed. The algorithm below first sorts the input array and then tests all possible pairs in a careful order that avoids the slowdown of a binary search per pair, achieving worst-case $O(n^{2})$ time, as follows.

```
sort(S);
for i = 0 to n - 2 do
    a = S[i];
    start = i + 1;
    end = n - 1;
    while (start < end) do
        b = S[start]
        c = S[end];
        if (a + b + c == 0) then
            output a, b, c;
            // Continue search for all triplet combinations summing to zero.
            // We need to update both end and start together since the array values are distinct.
            start = start + 1;
            end = end - 1;
        else if (a + b + c > 0) then
            end = end - 1;
        else
            start = start + 1;
    end
end
```

The following example shows this algorithm's execution on a small sorted array. Current values of **a** are shown in red, values of **b** and **c** are shown in magenta.

```
 -25 -10 -7 -3 2 4 8 10  (a+b+c==-25)
 -25 -10 -7 -3 2 4 8 10  (a+b+c==-22)
 . . .
 -25 -10 -7 -3 2 4 8 10  (a+b+c==-7)
 -25 -10 -7 -3 2 4 8 10  (a+b+c==-7)
 -25 -10 -7 -3 2 4 8 10  (a+b+c==-3)
 -25 -10 -7 -3 2 4 8 10  (a+b+c==2)
 -25 -10 -7 -3 2 4 8 10  (a+b+c==0)
```

The correctness of the algorithm can be seen as follows. Suppose we have a solution a + b + c = 0. Since the pointers only move in one direction, we can run the algorithm until the leftmost pointer points to a. Run the algorithm until either one of the remaining pointers points to b or c, whichever occurs first. Then the algorithm will run until the last pointer points to the remaining term, giving the affirmative solution.

## Variants

### Non-zero sum

Instead of looking for numbers whose sum is 0, it is possible to look for numbers whose sum is any constant *C*. The simplest way would be to modify the original algorithm to search the hash table for the integer ⁠ $(C-(S[i]+S[j]))$ ⁠.

Another method:

- Subtract *C*/3 from all elements of the input array.
- In the modified array, find 3 elements whose sum is 0.

For example, if A=[1,2,3,4] and if you are asked to find 3SUM for *C*=4, then subtract 4/3 from all the elements of A, and solve it in the usual 3sum way, i.e., ⁠ $(a-C/3)+(b-C/3)+(c-C/3)=0$ ⁠.

### Three different arrays

Instead of searching for the 3 numbers in a single array, we can search for them in 3 different arrays. I.e., given three arrays X, Y and Z, find three numbers *a*∈*X*, *b*∈*Y*, *c*∈*Z*, such that ⁠ $a+b+c=0$ ⁠. Call the 1-array variant 3SUM×1 and the 3-array variant 3SUM×3.

Given a solver for 3SUM×1, the 3SUM×3 problem can be solved in the following way (assuming all elements are integers):

- For every element in *X*, *Y* and *Z*, set: ⁠ $X[i]\gets X[i]*10+1$ ⁠, ⁠ $Y[i]\gets Y[i]*10+2$ ⁠, ⁠ $Z[i]\gets Z[i]*10-3$ ⁠.
- Let *S* be a concatenation of the arrays *X*, *Y* and *Z*.
- Use the 3SUM×1 oracle to find three elements ⁠ $a'\in S,\ b'\in S,\ c'\in S$ ⁠ such that ⁠ $a'+b'+c'=0$ ⁠.
- Return ⁠ $a\gets (a'-1)/10,\ b\gets (b'-2)/10,\ c\gets (c'+3)/10$ ⁠.

By the way we transformed the arrays, it is guaranteed that *a*∈*X*, *b*∈*Y*, *c*∈*Z*.

### Convolution sum

Instead of looking for arbitrary elements of the array such that:

$S[k]=S[i]+S[j]$

the *convolution 3sum* problem (Conv3SUM) looks for elements in specific locations:

$S[i+j]=S[i]+S[j]$

#### Reduction from Conv3SUM to 3SUM

Given a solver for 3SUM, the Conv3SUM problem can be solved in the following way.

- Define a new array *T*, such that for every index *i*: $T[i]=2nS[i]+i$ (where *n* is the number of elements in the array, and the indices run from 0 to *n*-1).
- Solve 3SUM on the array *T*.

Correctness proof:

- If in the original array there is a triple with $S[i+j]=S[i]+S[j]$ , then $T[i+j]=2nS[i+j]+i+j=(2nS[i]+i)+(2nS[j]+j)=T[i]+T[j]$ , so this solution will be found by 3SUM on *T*.
- Conversely, if in the new array there is a triple with $T[k]=T[i]+T[j]$ , then $2nS[k]+k=2n(S[i]+S[j])+(i+j)$ . Because $i+j<2n$ , necessarily $S[k]=S[i]+S[j]$ and $k=i+j$ , so this is a valid solution for Conv3SUM on *S*.

#### Reduction from 3SUM to Conv3SUM

Given a solver for Conv3SUM, the 3SUM problem can be solved in the following way.

The reduction uses a hash function. As a first approximation, assume that we have a linear hash function, i.e. a function *h* such that:

$h(x+y)=h(x)+h(y)$

Suppose that all elements are integers in the range: 0...*N*−1, and that the function *h* maps each element to an element in the smaller range of indices: 0...*n*−1. Create a new array *T* and send each element of *S* to its hash value in *T*, i.e., for every *x* in *S*(⁠ $\forall x\in S$ ⁠):

$T[h(x)]=x$

Initially, suppose that the mappings are unique (i.e. each cell in *T* accepts only a single element from *S*). Solve Conv3SUM on *T*. Now:

- If there is a solution for 3SUM: $z=x+y$ , then: $T[h(z)]=T[h(x)]+T[h(y)]$ and $h(z)=h(x)+h(y)$ , so this solution will be found by the Conv3SUM solver on *T*.
- Conversely, if a Conv3SUM is found on *T*, then obviously it corresponds to a 3SUM solution on *S* since *T* is just a permutation of *S*.

This idealized solution doesn't work, because any hash function might map several distinct elements of *S* to the same cell of *T*. The trick is to create an array ⁠ $T^{*}$ ⁠ by selecting a single random element from each cell of *T*, and run Conv3SUM on ⁠ $T^{*}$ ⁠. If a solution is found, then it is a correct solution for 3SUM on *S*. If no solution is found, then create a different random ⁠ $T^{*}$ ⁠ and try again. Suppose there are at most *R* elements in each cell of *T*. Then the probability of finding a solution (if a solution exists) is the probability that the random selection will select the correct element from each cell, which is $(1/R)^{3}$ . By running Conv3SUM $R^{3}$ times, the solution will be found with a high probability.

Unfortunately, we do not have linear perfect hashing, so we have to use an almost linear hash function, i.e. a function *h* such that:

$h(x+y)=h(x)+h(y)$

or

$h(x+y)=h(x)+h(y)+1$

This requires to duplicate the elements of *S* when copying them into *T*, i.e., put every element $x\in S$ both in $T[h(x)]$ (as before) and in $T[h(x)]-1$ . So each cell will have 2*R* elements, and we will have to run Conv3SUM $(2R)^{3}$ times.

## 3SUM-hardness

A problem is called **3SUM-hard** if solving it in subquadratic time implies a subquadratic-time algorithm for 3SUM. The concept of 3SUM-hardness was introduced by Gajentaan & Overmars (1995). They proved that a large class of problems in computational geometry are 3SUM-hard, including the following ones. (The authors acknowledge that many of these problems are contributed by other researchers.)

- Given a set of lines in the plane, are there three that meet in a point?
- Given a set of non-intersecting axis-parallel line segments, is there a line that separates them into two non-empty subsets?
- Given a set of infinite strips in the plane, do they fully cover a given rectangle?
- Given a set of triangles in the plane, compute their measure.
- Given a set of triangles in the plane, does their union have a hole?
- A number of visibility and motion planning problems, e.g.,
  - Given a set of horizontal triangles in space, can a particular triangle be seen from a particular point?
  - Given a set of non-intersecting axis-parallel line segment obstacles in the plane, can a given rod be moved by translations and rotations between a start and finish positions without colliding with the obstacles?

By now there are a multitude of other problems that fall into this category. An example is the decision version of X + Y sorting: given sets of numbers X and Y of n elements each, are there *n*² distinct *x* + *y* for *x* ∈ *X*, *y* ∈ *Y*?
