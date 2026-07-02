---
title: "Rank (J programming language)"
source: https://en.wikipedia.org/wiki/Rank_(J_programming_language)
domain: apl-j-k
license: CC-BY-SA-4.0
tags: j language, k language, array programming language, iverson notation, apl language
fetched: 2026-07-02
---

# Rank (J programming language)

**Rank** is a generalization of looping as used in scalar (non-array-oriented) programming languages. It is also a generalization of *mapcar* in the language *Lisp* and *map* in modern functional programming languages, and a generalization of scalar extension, inner (matrix) product, and outer product in APL\360. The canonical implementation of rank may be the language *J*, but it is also available in Dyalog APL, the International Organization for Standardization (ISO) technical standard on Extended APL, and NARS2000.

Rank has several different meanings. In general, the concept of *rank* is used to treat an orthogonal array in terms of its subarrays. For example, a two-dimensional array may be dealt with at rank 2 as the entire matrix, or at rank 1 to work with its implicit one-dimensional columns or rows, or at rank 0 to work at the level of its individual atoms.

- *Noun rank* – The rank of a noun is a nonnegative integer.
- *Verb rank* – The rank of a verb is a list of three integers.
- *The rank conjunction* – The rank conjunction (`"`) is used to derive a verb with a specific rank.

## Rank as a generalization of looping

Understanding rank requires knowing some very basic array-oriented programming concepts. In most array-based languages, reduction is denoted with a forward slash `/`. In J, the slash takes a left argument of the function and a right argument of the array to be reduced by that function.

```mw
   +/ 1 2 3
6
```

The result is `1 + 2 + 3`, as expected.

An N-dimensional integer array can also be created with `i.` which takes a vector of integers as its arguments. The number of integers defines the dimension and the absolute value of each integer defines the length of the corresponding dimension.

```mw
   i. 3
0 1 2

   i. 2 3
0 1 2
3 4 5

   i. 2 3 4
 0  1  2  3
 4  5  6  7
 8  9 10 11

12 13 14 15
16 17 18 19
20 21 22 23
```

Now let's reduce a two-dimensional array by addition.

```mw
   +/ i. 2 3
3 5 7
```

The result is `0 1 2 + 3 4 5`, as expected. Reduction runs down each column, adding together all the numbers in that column.

This application of `+/` to a two-dimensional array corresponds to the C code fragment:

```mw
for(j = 0; j < 3; ++j) {
    sum[j] = 0;
}
for(i = 0; i < 2; ++i) {
    for(j = 0; j < 3; ++j) {
        sum[j] += array[i][j];
    }
}
```

Suppose we wanted to add up the items of each row, as in the C code fragment:

```mw
for(i = 0; i < 2; ++i) {
    sum[i] = 0;
    for(j = 0; j < 3; ++j) {
        sum[i] += array[i][j];
    }
}
```

To produce the result `3 12`. We can do this in J without looping simply by using rank.

```mw
   +/"1 i. 2 3
3 12
```

To illustrate further how rank works in J, we can see the original expression is rank 2. The operator is mapped at the highest rank to the array.

```mw
   +/"2 i. 2 3
3 5 7
```

It is common to refer to the lower-dimensional arrays by these names, though they are disputed sometimes.

| Name | Rank |
|---|---|
| Atom or scalar | 0 |
| Vector or list | 1 |
| Table or matrix | 2 |
| Tensor or cube | 3 |

## Noun rank

Nouns, in J, are arrays. The rank of a noun is the number of dimensions of that array. The derived verb `#@$` determines the rank of a noun.

## Verb rank

Verbs, in J, are functions which take noun arguments and produce noun results. The rank of a verb controls how the verb is applied to nouns with ranks greater than 0. This verb rank is expressed as three numbers:

1. Rank for the monad case; for example, `−y` uses `−` as a monad
2. Rank for the left argument for the dyad case; for example, `x−y` uses `−` as a dyad
3. Rank for the right argument for the dyad case

In all cases, there is some underlying verb definition which applies to *cells*, which are subarrays of the indicated rank. Or, if the argument does not have that many dimensions, the entire argument.

In verbs, negative rank is interpreted as the rank of the noun supplied for that argument less the indicated value. (But never less than zero.)

For example, a verb with monadic rank of negative one when given an argument of rank 3, breaks the argument down into a list of rank 2 arrays. The verb's body is applied once to each of these two-dimensional subarrays.

In the context of a specific verb and a specific noun, the dimensions of that noun are divided into the sequence of prefix dimensions, called the *frame*, and the sequence of suffix dimensions, called the *cells*. Positive verb ranks indicate the number of cell dimensions, negative verb ranks indicate the number of frame dimensions.

In the dyadic case, there are two frames: one for the left argument, and one for the right argument. These frames must agree. If the frames are not identical, one must be a prefix of the other; e.g. `(i. 2 3) *"0 1 i. 2 3 4` multiplies each scalar (zero-dimensional item) on the left by each vector (one-dimensional item) on the right. The result of evaluating this verb will have the dimensions of the longest frame as the prefix dimensions of its result. Trailing result dimensions, if any, would be the result of the verb applied to the relevant cell(s). In degenerate cases, where the arguments do not have sufficient dimensions, the rank of the verb is effectively reduced (which would influence its result).

For example,

```mw
   10 + 4 5 6
 14 15 16
```

Here, the verb `+` has a rank of 0 0 0, the left argument has a rank of 0, and the right argument has a rank of 1 (with a dimension of 3). Thus, the left argument has a rank 0 frame and the right argument has a rank 1 frame (with a dimension 3). The left argument's (empty) frame is a valid suffix for the right argument's frame, so this is a valid operation. The result has a rank of 1 and a dimension of 3.

## The rank conjunction

The rank conjunction takes a verb left argument and a noun right argument to create a new verb. The noun right argument consists of up to three numbers specifying the monadic rank, the dyadic left rank, and the dyadic right rank, respectively.

If the right argument is only two numbers, they are taken as the ranks for the dyadic case: the first number is the rank of the left argument and the second number is the rank of the right argument. So, if we want to add a vector to each vector in a matrix:

```mw
   1 2 3 +"1 1 i. 3 3
1 3  5
4 6  8
7 9 11
```

If we want instead to add each scalar on the left to each vector on the right, we would do it this way:

```mw
   1 2 3 +"0 1 i. 3 3
1  2  3
5  6  7
9 10 11
```

If the right argument is only one number, it is taken as the rank for all three cases.

If the right argument is a verb, its rank is used. For example, these all derive the same verb:

- `+"0 0 0`
- `+"0 0`
- `+"0`
- `+"+`

If the left argument to the rank conjunction is a noun, a constant verb is created. The body of this verb ignores the values of any arguments and always produces a result which is that noun.
