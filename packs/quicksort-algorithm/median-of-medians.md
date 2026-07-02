---
title: "Median of medians"
source: https://en.wikipedia.org/wiki/Median_of_medians
domain: quicksort-algorithm
license: CC-BY-SA-4.0
tags: quicksort algorithm, divide and conquer, partition scheme, quickselect algorithm
fetched: 2026-07-02
---

# Median of medians

In computer science, the **median of medians** is an approximate median selection algorithm, frequently used to supply a good pivot for an exact selection algorithm, most commonly quickselect, that selects the *k*th smallest element of an initially unsorted array. Median of medians finds an approximate median in linear time. Using this approximate median as an improved pivot, the worst-case complexity of quickselect reduces from quadratic to *linear*, which is also the asymptotically optimal worst-case complexity of any selection algorithm. In other words, the median of medians is an approximate median-selection algorithm that helps building an asymptotically optimal, exact general selection algorithm (especially in the sense of worst-case complexity), by producing good pivot elements.

Median of medians can also be used as a pivot strategy in quicksort, yielding an optimal algorithm, with worst-case complexity $O(n\log n)$ . The median of medians algorithm guarantees a worst-case runtime of O(n) by recursively selecting good pivot elements, discarding at least 30% of elements at each step. Although this approach optimizes the asymptotic worst-case complexity quite well, it is typically outperformed in practice by instead choosing random pivots for its average $O(n)$ complexity for selection and average $O(n\log n)$ complexity for sorting, without any overhead of computing the pivot.

Similarly, median of medians is used in the hybrid introselect algorithm as a fallback for pivot selection at each iteration until kth smallest is found. This again ensures a worst-case linear performance, in addition to average-case linear performance: introselect starts with quickselect (with random pivot, default), to obtain good average performance, and then falls back to modified quickselect with pivot obtained from median of medians if the progress is too slow. Even though asymptotically similar, such a hybrid algorithm will have a lower complexity than a straightforward introselect up to a constant factor (both in average-case and worst-case), at any finite length.

The algorithm was published in 1973 and is sometimes called **BFPRT** after the last names of the authors (Blum, Floyd, Pratt, Rivest, Tarjan). In the original paper, the algorithm was referred to as **PICK**, referring to quickselect as *FIND*.

## Motivation

Quickselect is linear-time on average, but it can require quadratic time with poor pivot choices. This is because quickselect is a divide and conquer algorithm, with each step taking $O(n)$ time in the size of the remaining search set. If the search set decreases exponentially quickly in size (by a fixed proportion), this yields a geometric series times the $O(n)$ factor of a single step, and thus linear overall time. However, if the search set decreases slowly in size, such as linearly (by a fixed number of elements, in the worst case only reducing by one element each time), then a linear sum of linear steps yields quadratic overall time (formally, triangular numbers grow quadratically). For example, the worst-case occurs when pivoting on the smallest element at each step, such as applying quickselect for the maximum element to already sorted data and taking the first element as pivot each time.

If one instead consistently chooses "good" pivots, this is avoided and one always gets linear performance even in the worst case. A "good" pivot is one for which we can establish that a constant proportion of elements fall both below and above it, as then the search set decreases at least by a constant proportion at each step, hence exponentially quickly, and the overall time remains linear. The median is a good pivot – the best for sorting, and the best overall choice for selection – decreasing the search set by half at each step. Thus if one can compute the median in linear time, this only adds linear time to each step, and thus the overall complexity of the algorithm remains linear.

The median-of-medians algorithm computes an approximate median, namely a point that is guaranteed to be between the 30th and 70th percentiles (in the middle 4 deciles). Thus the search set decreases by at least 30%. The problem is reduced to 70% of the original size, which is a fixed proportion smaller. Applying the same algorithm on the now smaller set recursively until only one or two elements remain results in a cost of ${\frac {n}{1-0.7}}\approx 3.33{n}$

## Algorithm

As stated before, median-of-medians is used as a pivot selection strategy in the quickselect algorithm, which in pseudocode looks as follows.

```
function median(list)
   if length(list) is odd then
       value := nthSmallest(list, length(list) / 2)
   else
       value := 0.5 * (nthSmallest(list, length(list) / 2 - 1) +
                       nthSmallest(list, length(list) / 2))
   return value
```

```
function nthSmallest(list, n)
    index := select(list, 1, length(list), n)
    return list[index]
```

Be careful to handle `left`, `right` and `n` when implementing. The following pseudocode assumes that `left`, `right`, and the list use one-based numbering and that `select` is initially called with 1 as the argument to `left` and the length of the list as the argument to `right`. Note that this returns the index of the n'th smallest number after rearranging the list, rather than the actual value of the n'th smallest number.

```
function select(list, left, right, n)
    loop
        if left = right then
            return left
        pivotIndex := pivot(list, left, right)
        pivotIndex := partition(list, left, right, pivotIndex, n)
        if n = pivotIndex then
            return n
        else if n < pivotIndex then
            right := pivotIndex - 1
        else
            left := pivotIndex + 1
```

Subroutine pivot is the actual median-of-medians algorithm. It divides its input (a list of length n) into groups of at most five elements, computes the median of each of those groups using some subroutine, then recursively computes the true median of the ${\frac {n}{5}}$ medians found in the previous step:. Note that pivot calls select; this is an instance of mutual recursion.

```
function pivot(list, left, right)
    // for 5 or less elements just get median
    if right − left < 5 then
        return partition5(list, left, right)
    // otherwise move the medians of five-element subgroups to the first n/5 positions
    for i from left to right in steps of 5
        // get the median position of the i'th five-element subgroup
        subRight := i + 4
        if subRight > right then
            subRight := right
        median5 := partition5(list, i, subRight)
        swap list[median5] and list[left + floor((i − left) / 5)]

    // compute the median of the n/5 medians-of-five
    mid := floor((right − left) / 10) + left + 1
    return select(list, left, left + floor((right − left) / 5), mid)
```

### Partition helper functions

There is a subroutine called partition that can, in linear time, group a list (ranging from indices `left` to `right`) into three parts, those less than a certain element, those equal to it, and those greater than the element (a three-way partition). The grouping into three parts ensures that the median-of-medians maintains linear execution time in a case of many or all coincident elements. Here is pseudocode that performs a partition about the element `list[pivotIndex]`:

```
function partition(list, left, right, pivotIndex, n)
    pivotValue := list[pivotIndex]
    swap list[pivotIndex] and list[right]  // Move pivot to end
    storeIndex := left
    // Move all elements smaller than the pivot to the left of the pivot
    for i from left to right − 1 do
        if list[i] < pivotValue then
            swap list[storeIndex] and list[i]
            increment storeIndex
    // Move all elements equal to the pivot right after
    // the smaller elements
    storeIndexEq := storeIndex
    for i from storeIndex to right − 1 do
        if list[i] = pivotValue then
            swap list[storeIndexEq] and list[i]
            increment storeIndexEq
    swap list[right] and list[storeIndexEq]  // Move pivot to its final place
    // Return location of pivot considering the desired location n
    if n < storeIndex then
        return storeIndex  // n is in the group of smaller elements
    if n ≤ storeIndexEq then
        return n  // n is in the group equal to pivot
    return storeIndexEq // n is in the group of larger elements
```

The partition5 subroutine selects the median of a group of at most five elements; an easy way to implement this is insertion sort, as shown below. It can also be implemented as a decision tree.

```
function partition5(list, left, right)
    i := left + 1
    while i ≤ right do
        j := i
        while j > left and list[j−1] > list[j] do
            swap list[j−1] and list[j]
            j := j − 1
        i :=  i + 1

    return left + (right - left) / 2
```

## Properties of pivot

Of the ${\frac {n}{5}}$ groups, half the number of groups $\left({\frac {1}{2}}\times {\frac {n}{5}}={\frac {n}{10}}\right)$ have their median less than the pivot (Median of Medians). Also, another half the number of groups $\left({\frac {1}{2}}\times {\frac {n}{5}}={\frac {n}{10}}\right)$ , again have their median greater than the pivot. In each of the ${\frac {n}{10}}$ groups with median less than the pivot, there are two elements that are smaller than their respective medians, which are smaller than the pivot. Thus, each of the ${\frac {n}{10}}$ groups have at least 3 elements that are smaller than the pivot. Similarly, in each of the ${\frac {n}{10}}$ groups with median greater than the pivot, there are two elements that are greater than their respective medians, which are greater than the pivot. Thus, each of the ${\frac {n}{10}}$ groups have at least 3 elements that are greater than the pivot. Hence, the pivot is less than $3\times {\frac {n}{10}}$ elements and greater than another $3\times {\frac {n}{10}}$ elements. Thus the chosen median splits the ordered elements somewhere between 30%/70% and 70%/30%, which assures worst-case linear behavior of the algorithm. To visualize:

One iteration on a randomized set of 100 elements from 0 to 99

12

15

11

2

9

5

0

7

3

21

44

40

1

18

20

32

19

35

37

39

13

16

14

8

10

26

6

33

4

27

49

46

52

25

51

34

43

56

72

79

Medians

17

23

24

28

29

30

31

36

42

47

50

55

58

60

63

65

66

67

81

83

22

45

38

53

61

41

62

82

54

48

59

57

71

78

64

80

70

76

85

87

96

95

94

86

89

69

68

97

73

92

74

88

99

84

75

90

77

93

98

91

(red = "(one of the two possible) median of medians", gray = "number < red", white = "number > red")

5-tuples are shown here sorted by median, for clarity. Sorting the tuples is not necessary because we only need the median for use as pivot element.

Note that all elements above/left of the red (30% of the 100 elements) are less, and all elements below/right of the red (another 30% of the 100 elements) are greater.

## Proof of linear running time

The median-calculating recursive call does not exceed worst-case linear behavior because the list of medians has size ${\frac {n}{5}}$ , while the other recursive call recurses on at most 70% of the list. Let $T(n)$ be the time it takes to run a median-of-medians Quickselect algorithm on an array of size n . Then we know this time is:

$T(n)\leq T(n/5)+T(n\cdot 7/10)+c\cdot n,$

where

- the $T\left({\frac {n}{5}}\right)$ part is for finding the *true* median of the ${\frac {n}{5}}$ medians, by running an (independent) Quickselect on them (since finding the median is just a special case of selecting a *k*-smallest element)
- the $O(n)$ term $c\cdot n$ is for the partitioning work to create the two sides, one of which our Quickselect will recurse (we visited each element a constant number of times in order to form them into n/5 groups and take each median in $O(1)$ time).
- the $T\left({\frac {7n}{10}}\right)$ part is for the actual Quickselect recursion (for the worst case, in which the *k*-th element is in the bigger partition that can be of size ${\frac {7n}{10}}$ maximally)

By induction: Assume $\exists c'\in \mathbb {R} _{+}$ such that $\forall k<n$ it $T(k)\leq c'\cdot k$ holds. Now,

$T(n)\leq T(n/5)+T(n\cdot 7/10)+c\cdot n\leq _{\textrm {I.H}}c'\cdot \left({\frac {n}{5}}\right)+c'\cdot \left({\frac {7n}{10}}\right)+cn$

holds by the Induction hypothesis. This yields

$T(n)\leq c'\cdot {\frac {9n}{10}}+cn\leq c'n$ for our chosen constant $c'\geq 10c$ .

## Analysis

The key step is reducing the problem to selecting in two lists whose total length is shorter than the original list, plus a linear factor for the reduction step. This allows a simple induction to show that the overall running time is linear.

The specific choice of groups of five elements is explained as follows. Firstly, computing median of an odd list is faster and simpler; while one could use an even list, this requires taking the average of the two middle elements, which is slower than simply selecting the single exact middle element. Secondly, five is the smallest odd number such that median of medians works. With groups of only three elements, the resulting list of medians to search in is length ${\frac {n}{3}}$ , and reduces the list to recurse into length ${\frac {2}{3}}n$ , since it is greater than 1/2 × 2/3 = 1/3 of the elements and less than 1/2 × 2/3 = 1/3 of the elements. Thus this still leaves n elements to search in, not reducing the problem sufficiently. The individual lists are shorter, however, and one can bound the resulting complexity to $O(n\log n)$ by the Akra–Bazzi method, but it does not prove linearity.

Conversely, one may instead group by g = seven, nine, or more elements, and this does work. This reduces the size of the list of medians to ${\frac {n}{g}}$ *,* and the size of the list to recurse into asymptotes at 3*n*/4 (75%), as the quadrants in the above table approximate 25%, as the size of the overlapping lines decreases proportionally. This reduces the scaling factor from 10 asymptotically to 4, but accordingly raises the c term for the partitioning work. Finding the median of a larger group takes longer, but is a constant factor (depending only on g ), and thus does not change the overall performance as *n* grows. In fact, considering the number of comparisons in the worst case, the constant factor is ${\frac {2g(g-1)}{g-3}}$ and this is minimized over odd integers greater than three at 20 when $g=5$ .

If one instead groups the other way, say dividing the n element list into 5 lists, computing the median of each, and then computing the median of these – i.e., grouping by a constant fraction, not a constant number – one does not as clearly reduce the problem, since it requires computing 5 medians, each in a list of ${\frac {n}{5}}$ elements, and then recursing on a list of length at most ${\frac {7}{10}}n$ . As with grouping by 3, the individual lists are shorter, but the overall length is no shorter – in fact longer – and thus one can only prove superlinear bounds. Grouping into a square of ${\sqrt {n}}$ lists of length ${\sqrt {n}}$ is similarly complicated.
