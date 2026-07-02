---
title: "Dynamic programming (part 2/2)"
source: https://en.wikipedia.org/wiki/Dynamic_programming
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
part: 2/2
---

## Examples: computer algorithms

### Dijkstra's algorithm for the shortest path problem

From a dynamic programming point of view, Dijkstra's algorithm for the shortest path problem is a successive approximation scheme that solves the dynamic programming functional equation for the shortest path problem by the **Reaching** method.

In fact, Dijkstra's explanation of the logic behind the algorithm, namely

> **Problem 2.** Find the path of minimum total length between two given nodes P {\displaystyle P} ({\displaystyle P}) and Q {\displaystyle Q} ({\displaystyle Q}).
> 
> We use the fact that, if R {\displaystyle R} ({\displaystyle R}) is a node on the minimal path from P {\displaystyle P} ({\displaystyle P}) to Q {\displaystyle Q} ({\displaystyle Q}), knowledge of the latter implies the knowledge of the minimal path from P {\displaystyle P} ({\displaystyle P}) to R {\displaystyle R} ({\displaystyle R}).

is a paraphrasing of Bellman's famous Principle of Optimality in the context of the shortest path problem.

### Fibonacci sequence

Using dynamic programming in the calculation of the *n*th member of the Fibonacci sequence improves its performance greatly. Here is a naïve implementation, based directly on the mathematical definition:

```
function fib(n)
    if n <= 1 return n
    return fib(n − 1) + fib(n − 2)
```

Notice that if we call, say, `fib(5)`, we produce a call tree that calls the function on the same value many different times:

1. `fib(5)`
2. `fib(4) + fib(3)`
3. `(fib(3) + fib(2)) + (fib(2) + fib(1))`
4. `((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))`
5. `(((fib(1) + fib(0)) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))`

In particular, `fib(2)` was calculated three times from scratch. In larger examples, many more values of `fib`, or *subproblems*, are recalculated, leading to an exponential time algorithm.

Now, suppose we have a simple map object, *m*, which maps each value of `fib` that has already been calculated to its result, and we modify our function to use it and update it. The resulting function requires only O(*n*) time instead of exponential time (but requires O(*n*) space):

```
var m := map(0 → 0, 1 → 1)
function fib(n)
    if key n is not in map m 
        m[n] := fib(n − 1) + fib(n − 2)
    return m[n]
```

This technique of saving values that have already been calculated is called *memoization*; this is the top-down approach, since we first break the problem into subproblems and then calculate and store values.

In the **bottom-up** approach, we calculate the smaller values of `fib` first, then build larger values from them. This method also uses O(*n*) time since it contains a loop that repeats n − 1 times, but it only takes constant (O(1)) space, in contrast to the top-down approach which requires O(*n*) space to store the map.

```
function fib(n)
    if n = 0
        return 0
    else
        var previousFib := 0, currentFib := 1
        repeat n − 1 times // loop is skipped if n = 1
            var newFib := previousFib + currentFib
            previousFib := currentFib
            currentFib  := newFib
        return currentFib
```

In both examples, we only calculate `fib(2)` one time, and then use it to calculate both `fib(4)` and `fib(3)`, instead of computing it every time either of them is evaluated.

### A type of balanced 0–1 matrix

Consider the problem of assigning values, either zero or one, to the positions of an *n* × *n* matrix, with *n* even, so that each row and each column contains exactly *n* / 2 zeros and *n* / 2 ones. We ask how many different assignments there are for a given n. For example, when *n* = 4, five possible solutions are

[

0

1

0

1

1

0

1

0

0

1

0

1

1

0

1

0

]

and

[

0

0

1

1

0

0

1

1

1

1

0

0

1

1

0

0

]

and

[

1

1

0

0

0

0

1

1

1

1

0

0

0

0

1

1

]

and

[

1

0

0

1

0

1

1

0

0

1

1

0

1

0

0

1

]

and

[

1

1

0

0

1

1

0

0

0

0

1

1

0

0

1

1

]

.

{\displaystyle {\begin{bmatrix}0&1&0&1\\1&0&1&0\\0&1&0&1\\1&0&1&0\end{bmatrix}}{\text{ and }}{\begin{bmatrix}0&0&1&1\\0&0&1&1\\1&1&0&0\\1&1&0&0\end{bmatrix}}{\text{ and }}{\begin{bmatrix}1&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&1\end{bmatrix}}{\text{ and }}{\begin{bmatrix}1&0&0&1\\0&1&1&0\\0&1&1&0\\1&0&0&1\end{bmatrix}}{\text{ and }}{\begin{bmatrix}1&1&0&0\\1&1&0&0\\0&0&1&1\\0&0&1&1\end{bmatrix}}.}

There are at least three possible approaches: brute force, backtracking, and dynamic programming.

Brute force consists of checking all assignments of zeros and ones and counting those that have balanced rows and columns (*n* / 2 zeros and *n* / 2 ones). As there are 2 n 2 {\displaystyle 2^{n^{2}}} ({\displaystyle 2^{n^{2}}}) possible assignments and ( n n / 2 ) n {\displaystyle {\tbinom {n}{n/2}}^{n}} ({\displaystyle {\tbinom {n}{n/2}}^{n}}) sensible assignments, this strategy is not practical for arbitrarily large values of n {\displaystyle n} ({\displaystyle n}).

Backtracking for this problem consists of choosing some order of the matrix elements and recursively placing ones or zeros, while checking that in every row and column the number of elements that have not been assigned plus the number of ones or zeros are both at least *n* / 2. While more sophisticated than brute force, this approach will visit every solution once, making it impractical for *n* larger than six, since the number of solutions is already 116963796250 for *n* = 8, as we shall see.

Dynamic programming makes it possible to count the number of solutions without visiting them all. Imagine backtracking values for the first row – what information would we require about the remaining rows, in order to be able to accurately count the solutions obtained for each first row value? We consider *k* × *n* boards, where 1 ≤ *k* ≤ *n*, whose k rows contain n / 2 {\displaystyle n/2} ({\displaystyle n/2}) zeros and n / 2 {\displaystyle n/2} ({\displaystyle n/2}) ones. The function *f* to which memoization is applied maps vectors of *n* pairs of integers to the number of admissible boards (solutions). There is one pair for each column, and its two components indicate respectively the number of zeros and ones that have yet to be placed in that column. We seek the value of f ( ( n / 2 , n / 2 ) , ( n / 2 , n / 2 ) , … ( n / 2 , n / 2 ) ) {\displaystyle f((n/2,n/2),(n/2,n/2),\ldots (n/2,n/2))} ({\displaystyle f((n/2,n/2),(n/2,n/2),\ldots (n/2,n/2))}) (n arguments or one vector of n elements). The process of subproblem creation involves iterating over every one of ( n n / 2 ) {\displaystyle {\tbinom {n}{n/2}}} ({\displaystyle {\tbinom {n}{n/2}}}) possible assignments for the top row of the board, and going through every column, subtracting one from the appropriate element of the pair for that column, depending on whether the assignment for the top row contained a zero or a one at that position. If any one of the results is negative, then the assignment is invalid and does not contribute to the set of solutions (recursion stops). Otherwise, we have an assignment for the top row of the *k* × *n* board and recursively compute the number of solutions to the remaining (*k* − 1) × *n* board, adding the numbers of solutions for every admissible assignment of the top row and returning the sum, which is being memoized. The base case is the trivial subproblem, which occurs for a 1 × *n* board. The number of solutions for this board is either zero or one, depending on whether the vector is a permutation of *n* / 2 (0, 1) and *n* / 2 (1, 0) pairs or not.

For example, in the first two boards shown above the sequences of vectors would be

```
((2, 2) (2, 2) (2, 2) (2, 2))       ((2, 2) (2, 2) (2, 2) (2, 2))     k = 4
  0      1      0      1              0      0      1      1

((1, 2) (2, 1) (1, 2) (2, 1))       ((1, 2) (1, 2) (2, 1) (2, 1))     k = 3
  1      0      1      0              0      0      1      1

((1, 1) (1, 1) (1, 1) (1, 1))       ((0, 2) (0, 2) (2, 0) (2, 0))     k = 2
  0      1      0      1              1      1      0      0

((0, 1) (1, 0) (0, 1) (1, 0))       ((0, 1) (0, 1) (1, 0) (1, 0))     k = 1
  1      0      1      0              1      1      0      0

((0, 0) (0, 0) (0, 0) (0, 0))       ((0, 0) (0, 0), (0, 0) (0, 0))
```

The number of solutions (sequence A058527 in the OEIS) is

1, 2, 90,

297

200

,

116

963

796

250

,

6

736

218

287

430

460

752

, ...

Links to the MAPLE implementation of the dynamic programming approach may be found among the external links.

### Checkerboard

Consider a checkerboard with *n* × *n* squares and a cost function `c(i, j)` which returns a cost associated with square `(i,j)` (`*i*` being the row, `*j*` being the column). For instance (on a 5 × 5 checkerboard),

| 5 | 6 | 7 | 4 | 7 | 8 |
|---|---|---|---|---|---|
| 4 | 7 | 6 | 1 | 1 | 4 |
| 3 | 3 | 5 | 7 | 8 | 2 |
| 2 | – | 6 | 7 | 0 | – |
| 1 | – | – | **5** | – | – |
|   | 1 | 2 | 3 | 4 | 5 |

Thus `c(1, 3) = 5`

Let us say there was a checker that could start at any square on the first rank (i.e., row) and you wanted to know the shortest path (the sum of the minimum costs at each visited rank) to get to the last rank; assuming the checker could move only diagonally left forward, diagonally right forward, or straight forward. That is, a checker on `(1,3)` can move to `(2,2)`, `(2,3)` or `(2,4)`.

| 5 |   |   |   |   |   |
|---|---|---|---|---|---|
| 4 |   |   |   |   |   |
| 3 |   |   |   |   |   |
| 2 |   | x | x | x |   |
| 1 |   |   | o |   |   |
|   | 1 | 2 | 3 | 4 | 5 |

This problem exhibits **optimal substructure**. That is, the solution to the entire problem relies on solutions to subproblems. Let us define a function `q(i, j)` as

q

(

i

,

j

) = the minimum cost to reach square (

i

,

j

).

Starting at rank `n` and descending to rank `1`, we compute the value of this function for all the squares at each successive rank. Picking the square that holds the minimum value at each rank gives us the shortest path between rank `n` and rank `1`.

The function `q(i, j)` is equal to the minimum cost to get to any of the three squares below it (since those are the only squares that can reach it) plus `c(i, j)`. For instance:

| 5 |   |   |   |   |   |
|---|---|---|---|---|---|
| 4 |   |   | A |   |   |
| 3 |   | B | C | D |   |
| 2 |   |   |   |   |   |
| 1 |   |   |   |   |   |
|   | 1 | 2 | 3 | 4 | 5 |

q

(

A

)

=

min

(

q

(

B

)

,

q

(

C

)

,

q

(

D

)

)

+

c

(

A

)

{\displaystyle q(A)=\min(q(B),q(C),q(D))+c(A)\,}

Now, let us define `q(i, j)` in somewhat more general terms:

q

(

i

,

j

)

=

{

∞

j

<

1

or

j

>

n

c

(

i

,

j

)

i

=

1

min

(

q

(

i

−

1

,

j

−

1

)

,

q

(

i

−

1

,

j

)

,

q

(

i

−

1

,

j

+

1

)

)

+

c

(

i

,

j

)

otherwise.

{\displaystyle q(i,j)={\begin{cases}\infty &j<1{\text{ or }}j>n\\c(i,j)&i=1\\\min(q(i-1,j-1),q(i-1,j),q(i-1,j+1))+c(i,j)&{\text{otherwise.}}\end{cases}}}

The first line of this equation deals with a board modeled as squares indexed on `1` at the lowest bound and `n` at the highest bound. The second line specifies what happens at the first rank; providing a base case. The third line, the recursion, is the important part. It represents the `A,B,C,D` terms in the example. From this definition we can derive straightforward recursive code for `q(i, j)`. In the following pseudocode, `n` is the size of the board, `c(i, j)` is the cost function, and `min()` returns the minimum of a number of values:

```
function minCost(i, j)
    if j < 1 or j > n
        return infinity
    else if i = 1
        return c(i, j)
    else
        return min( minCost(i-1, j-1), minCost(i-1, j), minCost(i-1, j+1) ) + c(i, j)
```

This function only computes the path cost, not the actual path. We discuss the actual path below. This, like the Fibonacci-numbers example, is horribly slow because it too exhibits the **overlapping sub-problems** attribute. That is, it recomputes the same path costs over and over. However, we can compute it much faster in a bottom-up fashion if we store path costs in a two-dimensional array `q[i, j]` rather than using a function. This avoids recomputation; all the values needed for array `q[i, j]` are computed ahead of time only once. Precomputed values for `(i,j)` are simply looked up whenever needed.

We also need to know what the actual shortest path is. To do this, we use another array `p[i, j]`; a *predecessor array*. This array records the path to any square `s`. The predecessor of `s` is modeled as an offset relative to the index (in `q[i, j]`) of the precomputed path cost of `s`. To reconstruct the complete path, we lookup the predecessor of `s`, then the predecessor of that square, then the predecessor of that square, and so on recursively, until we reach the starting square. Consider the following pseudocode:

```
function computeShortestPathArrays()
    for x from 1 to n
        q[1, x] := c(1, x)
    for y from 1 to n
        q[y, 0]     := infinity
        q[y, n + 1] := infinity
    for y from 2 to n
        for x from 1 to n
            m := min(q[y-1, x-1], q[y-1, x], q[y-1, x+1])
            q[y, x] := m + c(y, x)
            if m = q[y-1, x-1]
                p[y, x] := -1
            else if m = q[y-1, x]
                p[y, x] :=  0
            else
                p[y, x] :=  1
```

Now the rest is a simple matter of finding the minimum and printing it.

```
function computeShortestPath()
    computeShortestPathArrays()
    minIndex := 1
    min := q[n, 1]
    for i from 2 to n
        if q[n, i] < min
            minIndex := i
            min := q[n, i]
    printPath(n, minIndex)
```

```
function printPath(y, x)
    print(x)
    print("<-")
    if y = 2
        print(x + p[y, x])
    else
        printPath(y-1, x + p[y, x])
```

### Sequence alignment

In genetics, sequence alignment is an important application where dynamic programming is essential. Typically, the problem consists of transforming one sequence into another using edit operations that replace, insert, or remove an element. Each operation has an associated cost, and the goal is to find the sequence of edits with the lowest total cost.

The problem can be stated naturally as a recursion, a sequence A is optimally edited into a sequence B by either:

1. inserting the first character of B, and performing an optimal alignment of A and the tail of B
2. deleting the first character of A, and performing the optimal alignment of the tail of A and B
3. replacing the first character of A with the first character of B, and performing optimal alignments of the tails of A and B.

The partial alignments can be tabulated in a matrix, where cell (i,j) contains the cost of the optimal alignment of A[1..i] to B[1..j]. The cost in cell (i,j) can be calculated by adding the cost of the relevant operations to the cost of its neighboring cells, and selecting the optimum.

Different variants exist, see Smith–Waterman algorithm and Needleman–Wunsch algorithm.

### Tower of Hanoi puzzle

The **Tower of Hanoi** or **Towers of Hanoi** is a mathematical game or puzzle. It consists of three rods, and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:

- Only one disk may be moved at a time.
- Each move consists of taking the upper disk from one of the rods and sliding it onto another rod, on top of the other disks that may already be present on that rod.
- No disk may be placed on top of a smaller disk.

The dynamic programming solution consists of solving the functional equation

S(n,h,t) = S(n-1,h, not(h,t)) ; S(1,h,t) ; S(n-1,not(h,t),t)

where n denotes the number of disks to be moved, h denotes the home rod, t denotes the target rod, not(h,t) denotes the third rod (neither h nor t), ";" denotes concatenation, and

S(n, h, t) := solution to a problem consisting of n disks that are to be moved from rod h to rod t.

For n=1 the problem is trivial, namely S(1,h,t) = "move a disk from rod h to rod t" (there is only one disk left).

The number of moves required by this solution is 2*n* − 1. If the objective is to **maximize** the number of moves (without cycling) then the dynamic programming functional equation is slightly more complicated and 3*n* − 1 moves are required.

### Egg dropping puzzle

A famous puzzle relates to dropping eggs from a building to determine at which height they start to break. The following is a description involving N=2 eggs and a building with H=36 floors:

Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing (using

U.S. English

terminology, in which the first floor is at ground level). We make a few assumptions:

- An egg that survives a fall can be used again.
- A broken egg must be discarded.
- The effect of a fall is the same for all eggs.
- If an egg breaks when dropped, then it would break if dropped from a higher window.
- If an egg survives a fall, then it would survive a shorter fall.
- It is not ruled out that the first-floor windows break eggs, nor is it ruled out that eggs can survive the 36th-floor windows.

If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second-floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the lowest number of egg-droppings that is guaranteed to work in all cases?

To derive a dynamic programming functional equation for this puzzle, let the **state** of the dynamic programming model be a pair s = (n,k), where

n

= number of test eggs available,

n

= 0, 1, 2, 3, ...,

N

− 1.

k

= number of (consecutive) floors yet to be tested,

k

= 0, 1, 2, ...,

H

− 1.

For instance, *s* = (2,6) indicates that two test eggs are available and 6 (consecutive) floors are yet to be tested. The initial state of the process is *s* = (*N*,*H*) where *N* denotes the number of test eggs available at the commencement of the experiment. The process terminates either when there are no more test eggs (*n* = 0) or when *k* = 0, whichever occurs first. If termination occurs at state *s* = (0,*k*) and *k* > 0, then the test failed.

Now, let

W

(

n

,

k

) = minimum number of trials required to identify the value of the critical floor under the worst-case scenario given that the process is in state

s

= (

n

,

k

).

Then it can be shown that

W

(

n

,

k

) = 1 + min{max(

W

(

n

− 1,

x

− 1),

W

(

n

,

k

−

x

)):

x

= 1, 2, ...,

k

}

with *W*(*n*,0) = 0 for all *n* > 0 and *W*(1,*k*) = *k* for all *k*. It is easy to solve this equation iteratively by systematically increasing the values of *n* and *k*.

#### Faster DP solution using a different parametrization

Notice that the above solution takes O ( n k 2 ) {\displaystyle O(nk^{2})} ({\displaystyle O(nk^{2})}) time with a DP solution. This can be improved to O ( n k log ⁡ k ) {\displaystyle O(nk\log k)} ({\displaystyle O(nk\log k)}) time by binary searching on the optimal x {\displaystyle x} ({\displaystyle x}) in the above recurrence, since W ( n − 1 , x − 1 ) {\displaystyle W(n-1,x-1)} ({\displaystyle W(n-1,x-1)}) is increasing in x {\displaystyle x} ({\displaystyle x}) while W ( n , k − x ) {\displaystyle W(n,k-x)} ({\displaystyle W(n,k-x)}) is decreasing in x {\displaystyle x} ({\displaystyle x}), thus a local minimum of max ( W ( n − 1 , x − 1 ) , W ( n , k − x ) ) {\displaystyle \max(W(n-1,x-1),W(n,k-x))} ({\displaystyle \max(W(n-1,x-1),W(n,k-x))}) is a global minimum. Also, by storing the optimal x {\displaystyle x} ({\displaystyle x}) for each cell in the DP table and referring to its value for the previous cell, the optimal x {\displaystyle x} ({\displaystyle x}) for each cell can be found in constant time, improving it to O ( n k ) {\displaystyle O(nk)} ({\displaystyle O(nk)}) time. However, there is an even faster solution that involves a different parametrization of the problem:

Let k {\displaystyle k} ({\displaystyle k}) be the total number of floors such that the eggs break when dropped from the k {\displaystyle k} ({\displaystyle k})th floor (The example above is equivalent to taking k = 37 {\displaystyle k=37} ({\displaystyle k=37})).

Let m {\displaystyle m} ({\displaystyle m}) be the minimum floor from which the egg must be dropped to be broken.

Let f ( t , n ) {\displaystyle f(t,n)} ({\displaystyle f(t,n)}) be the maximum number of values of m {\displaystyle m} ({\displaystyle m}) that are distinguishable using t {\displaystyle t} ({\displaystyle t}) tries and n {\displaystyle n} ({\displaystyle n}) eggs.

Then f ( t , 0 ) = f ( 0 , n ) = 1 {\displaystyle f(t,0)=f(0,n)=1} ({\displaystyle f(t,0)=f(0,n)=1}) for all t , n ≥ 0 {\displaystyle t,n\geq 0} ({\displaystyle t,n\geq 0}).

Let a {\displaystyle a} ({\displaystyle a}) be the floor from which the first egg is dropped in the optimal strategy.

If the first egg broke, m {\displaystyle m} ({\displaystyle m}) is from 1 {\displaystyle 1} ({\displaystyle 1}) to a {\displaystyle a} ({\displaystyle a}) and distinguishable using at most t − 1 {\displaystyle t-1} ({\displaystyle t-1}) tries and n − 1 {\displaystyle n-1} ({\displaystyle n-1}) eggs.

If the first egg did not break, m {\displaystyle m} ({\displaystyle m}) is from a + 1 {\displaystyle a+1} ({\displaystyle a+1}) to k {\displaystyle k} ({\displaystyle k}) and distinguishable using t − 1 {\displaystyle t-1} ({\displaystyle t-1}) tries and n {\displaystyle n} ({\displaystyle n}) eggs.

Therefore, f ( t , n ) = f ( t − 1 , n − 1 ) + f ( t − 1 , n ) {\displaystyle f(t,n)=f(t-1,n-1)+f(t-1,n)} ({\displaystyle f(t,n)=f(t-1,n-1)+f(t-1,n)}).

Then the problem is equivalent to finding the minimum x {\displaystyle x} ({\displaystyle x}) such that f ( x , n ) ≥ k {\displaystyle f(x,n)\geq k} ({\displaystyle f(x,n)\geq k}).

To do so, we could compute { f ( t , i ) : 0 ≤ i ≤ n } {\displaystyle \{f(t,i):0\leq i\leq n\}} ({\displaystyle \{f(t,i):0\leq i\leq n\}}) in order of increasing t {\displaystyle t} ({\displaystyle t}), which would take O ( n x ) {\displaystyle O(nx)} ({\displaystyle O(nx)}) time.

Thus, if we separately handle the case of n = 1 {\displaystyle n=1} ({\displaystyle n=1}), the algorithm would take O ( n k ) {\displaystyle O(n{\sqrt {k}})} ({\displaystyle O(n{\sqrt {k}})}) time.

But the recurrence relation can in fact be solved, giving f ( t , n ) = ∑ i = 0 n ( t i ) {\displaystyle f(t,n)=\sum _{i=0}^{n}{\binom {t}{i}}} ({\displaystyle f(t,n)=\sum _{i=0}^{n}{\binom {t}{i}}}), which can be computed in O ( n ) {\displaystyle O(n)} ({\displaystyle O(n)}) time using the identity ( t i + 1 ) = ( t i ) t − i i + 1 {\displaystyle {\binom {t}{i+1}}={\binom {t}{i}}{\frac {t-i}{i+1}}} ({\displaystyle {\binom {t}{i+1}}={\binom {t}{i}}{\frac {t-i}{i+1}}}) for all i ≥ 0 {\displaystyle i\geq 0} ({\displaystyle i\geq 0}).

Since f ( t , n ) ≤ f ( t + 1 , n ) {\displaystyle f(t,n)\leq f(t+1,n)} ({\displaystyle f(t,n)\leq f(t+1,n)}) for all t ≥ 0 {\displaystyle t\geq 0} ({\displaystyle t\geq 0}), we can binary search on t {\displaystyle t} ({\displaystyle t}) to find x {\displaystyle x} ({\displaystyle x}), giving an O ( n log ⁡ k ) {\displaystyle O(n\log k)} ({\displaystyle O(n\log k)}) algorithm.

### Matrix chain multiplication

Matrix chain multiplication is a well-known example that demonstrates utility of dynamic programming. For example, engineering applications often have to multiply a chain of matrices. It is not surprising to find matrices of large dimensions, for example 100×100. Therefore, our task is to multiply matrices ⁠ A 1 , A 2 , . . . . A n {\displaystyle A_{1},A_{2},....A_{n}} ({\displaystyle A_{1},A_{2},....A_{n}})⁠. Matrix multiplication is not commutative, but is associative; and we can multiply only two matrices at a time. So, we can multiply this chain of matrices in many different ways, for example:

((

A

1

×

A

2

) ×

A

3

) × ...

A

n

A

1

×(((

A

2

×

A

3

)× ... ) ×

A

n

)

(

A

1

×

A

2

) × (

A

3

× ...

A

n

)

and so on. There are numerous ways to multiply this chain of matrices. They will all produce the same final result, however they will take more or less time to compute, based on which particular matrices are multiplied. If matrix A has dimensions m×n and matrix B has dimensions n×q, then matrix C=A×B will have dimensions m×q, and will require m*n*q scalar multiplications (using a simplistic matrix multiplication algorithm for purposes of illustration).

For example, let us multiply matrices A, B and C. Let us assume that their dimensions are m×n, n×p, and p×s, respectively. Matrix A×B×C will be of size m×s and can be calculated in two ways shown below:

1. Ax(B×C) This order of matrix multiplication will require nps + mns scalar multiplications.
2. (A×B)×C This order of matrix multiplication will require mnp + mps scalar calculations.

Let us assume that m = 10, n = 100, p = 10 and s = 1000. So, the first way to multiply the chain will require 1,000,000 + 1,000,000 calculations. The second way will require only 10,000 + 100,000 calculations. Obviously, the second way is faster, and we should multiply the matrices using that arrangement of parenthesis.

Therefore, our conclusion is that the order of parenthesis matters, and that our task is to find the optimal order of parenthesis.

At this point, we have several choices, one of which is to design a dynamic programming algorithm that will split the problem into overlapping problems and calculate the optimal arrangement of parenthesis. The dynamic programming solution is presented below.

Let's call m[i,j] the minimum number of scalar multiplications needed to multiply a chain of matrices from matrix i to matrix j (i.e. Ai × .... × Aj, i.e. i<=j). We split the chain at some matrix k, such that i <= k < j, and try to find out which combination produces minimum m[i,j].

The formula is:

```
       if i = j, m[i,j]= 0
       if i < j, m[i,j]= min over all possible values of k (m[i,k]+m[k+1,j] + 
  
    
      
        
          p
          
            i
            −
            1
          
        
        ∗
        
          p
          
            k
          
        
        ∗
        
          p
          
            j
          
        
      
    
    {\displaystyle p_{i-1}*p_{k}*p_{j}}
  
) 
```

where *k* ranges from *i* to *j* − 1.

- ⁠ p i − 1 {\displaystyle p_{i-1}} ({\displaystyle p_{i-1}})⁠ is the row dimension of matrix i,
- ⁠ p k {\displaystyle p_{k}} ({\displaystyle p_{k}})⁠ is the column dimension of matrix k,
- ⁠ p j {\displaystyle p_{j}} ({\displaystyle p_{j}})⁠ is the column dimension of matrix j.

This formula can be coded as shown below, where input parameter "chain" is the chain of matrices, i.e. ⁠ A 1 , A 2 , . . . A n {\displaystyle A_{1},A_{2},...A_{n}} ({\displaystyle A_{1},A_{2},...A_{n}})⁠:

```
function OptimalMatrixChainParenthesis(chain)
    n = length(chain)
    for i = 1, n
        m[i,i] = 0    // Since it takes no calculations to multiply one matrix
    for len = 2, n
        for i = 1, n - len + 1
            j = i + len -1
            m[i,j] = infinity      // So that the first calculation updates
            for k = i, j-1
                q = m[i, k] + m[k+1, j] + 
  
    
      
        
          p
          
            i
            −
            1
          
        
        ∗
        
          p
          
            k
          
        
        ∗
        
          p
          
            j
          
        
      
    
    {\displaystyle p_{i-1}*p_{k}*p_{j}}
  

                if q < m[i, j]     // The new order of parentheses is better than what we had
                    m[i, j] = q    // Update
                    s[i, j] = k    // Record which k to split on, i.e. where to place the parenthesis
```

So far, we have calculated values for all possible *m*[*i*, *j*], the minimum number of calculations to multiply a chain from matrix *i* to matrix *j*, and we have recorded the corresponding "split point"*s*[*i*, *j*]. For example, if we are multiplying chain *A*1×*A*2×*A*3×*A*4, and it turns out that *m*[1, 3] = 100 and *s*[1, 3] = 2, that means that the optimal placement of parenthesis for matrices 1 to 3 is ⁠ ( A 1 × A 2 ) × A 3 {\displaystyle (A_{1}\times A_{2})\times A_{3}} ({\displaystyle (A_{1}\times A_{2})\times A_{3}})⁠ and to multiply those matrices will require 100 scalar calculations.

This algorithm will produce "tables" *m*[, ] and *s*[, ] that will have entries for all possible values of i and j. The final solution for the entire chain is m[1, n], with corresponding split at s[1, n]. Unraveling the solution will be recursive, starting from the top and continuing until we reach the base case, i.e. multiplication of single matrices.

Therefore, the next step is to actually split the chain, i.e. to place the parenthesis where they (optimally) belong. For this purpose we could use the following algorithm:

```
function PrintOptimalParenthesis(s, i, j)
    if i = j
        print "A"i
    else
        print "(" 
        PrintOptimalParenthesis(s, i, s[i, j]) 
        PrintOptimalParenthesis(s, s[i, j] + 1, j) 
        print ")"
```

Of course, this algorithm is not useful for actual multiplication. This algorithm is just a user-friendly way to see what the result looks like.

To actually multiply the matrices using the proper splits, we need the following algorithm:

```mw
   function MatrixChainMultiply(chain from 1 to n)       // returns the final matrix, i.e. A1×A2×... ×An
      OptimalMatrixChainParenthesis(chain from 1 to n)   // this will produce s[ . ] and m[ . ] "tables"
      OptimalMatrixMultiplication(s, chain from 1 to n)  // actually multiply

   function OptimalMatrixMultiplication(s, i, j)   // returns the result of multiplying a chain of matrices from Ai to Aj in optimal way
      if i < j
         // keep on splitting the chain and multiplying the matrices in left and right sides
         LeftSide = OptimalMatrixMultiplication(s, i, s[i, j])
         RightSide = OptimalMatrixMultiplication(s, s[i, j] + 1, j)
         return MatrixMultiply(LeftSide, RightSide) 
      else if i = j
         return Ai   // matrix at position i
      else 
         print "error, i <= j must hold"

    function MatrixMultiply(A, B)    // function that multiplies two matrices
      if columns(A) = rows(B) 
         for i = 1, rows(A)
            for j = 1, columns(B)
               C[i, j] = 0
               for k = 1, columns(A)
                   C[i, j] = C[i, j] + A[i, k]*B[k, j] 
               return C 
      else 
          print "error, incompatible dimensions."
```


## History of the name

The term *dynamic programming* was originally used in the 1940s by Richard Bellman to describe the process of solving problems where one needs to find the best decisions one after another. By 1953, he refined this to the modern meaning, referring specifically to nesting smaller decision problems inside larger decisions, and the field was thereafter recognized by the IEEE as a systems analysis and engineering topic. Bellman's contribution is remembered in the name of the Bellman equation, a central result of dynamic programming which restates an optimization problem in recursive form.

Bellman explains the reasoning behind the term *dynamic programming* in his autobiography, *Eye of the Hurricane: An Autobiography*:

> I spent the Fall quarter (of 1950) at RAND. My first task was to find a name for multistage decision processes. An interesting question is, "Where did the name, dynamic programming, come from?" The 1950s were not good years for mathematical research. We had a very interesting gentleman in Washington named Wilson. He was Secretary of Defense, and he actually had a pathological fear and hatred of the word "research". I'm not using the term lightly; I'm using it precisely. His face would suffuse, he would turn red, and he would get violent if people used the term research in his presence. You can imagine how he felt, then, about the term mathematical. The RAND Corporation was employed by the Air Force, and the Air Force had Wilson as its boss, essentially. Hence, I felt I had to do something to shield Wilson and the Air Force from the fact that I was really doing mathematics inside the RAND Corporation. What title, what name, could I choose? In the first place I was interested in planning, in decision making, in thinking. But planning, is not a good word for various reasons. I decided therefore to use the word "programming". I wanted to get across the idea that this was dynamic, this was multistage, this was time-varying. I thought, let's kill two birds with one stone. Let's take a word that has an absolutely precise meaning, namely dynamic, in the classical physical sense. It also has a very interesting property as an adjective, and that is it's impossible to use the word dynamic in a pejorative sense. Try thinking of some combination that will possibly give it a pejorative meaning. It's impossible. Thus, I thought dynamic programming was a good name. It was something not even a Congressman could object to. So I used it as an umbrella for my activities.

— Richard Bellman, *Eye of the Hurricane: An Autobiography* (1984, page 159)

The word *dynamic* was chosen by Bellman to capture the time-varying aspect of the problems, and because it sounded impressive. The word *programming* referred to the use of the method to find an optimal *program*, in the sense of a military schedule for training or logistics. This usage is the same as that in the phrases *linear programming* and *mathematical programming*, a synonym for mathematical optimization.

The above explanation of the origin of the term may be inaccurate: According to Russell and Norvig, the above story "cannot be strictly true, because his first paper using the term (Bellman, 1952) appeared before Wilson became Secretary of Defense in 1953." Also, Harold J. Kushner stated in a speech that, "On the other hand, when I asked [Bellman] the same question, he replied that he was trying to upstage Dantzig's linear programming by adding dynamic. Perhaps both motivations were true."
