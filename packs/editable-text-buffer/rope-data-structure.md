---
title: "Rope (data structure)"
source: https://en.wikipedia.org/wiki/Rope_(data_structure)
domain: editable-text-buffer
license: CC-BY-SA-4.0
tags: rope data structure, gap buffer, piece table, text sequence structure
fetched: 2026-07-02
---

# Rope (data structure)

In computer programming, a **rope**, or **cord**, is a data structure composed of smaller strings that is used to efficiently store and manipulate longer strings or entire texts. For example, a text editing program may use a rope to represent the text being edited, so that operations such as insertion, deletion, and random access can be done efficiently.

## Description

A rope is a type of binary tree where each leaf (end node) holds a string of manageable size and length (also known as a *weight*), and each node further up the tree holds the sum of the lengths of all the leaves in its left subtree. A node with two children thus divides the whole string into two parts: the left subtree stores the first part of the string, the right subtree stores the second part of the string, and a node's weight is the length of the first part.

For rope operations, the strings stored in nodes are assumed to be constant immutable objects in the typical nondestructive case, allowing for some copy-on-write behavior. Leaf nodes are usually implemented as basic fixed-length strings with a reference count attached for deallocation when no longer needed, although other garbage collection methods can be used as well.

## Operations

In the following definitions, *N* is the length of the rope, that is, the weight of the root node. These examples are defined in the Java programming language.

### Collect leaves

Definition:

Create a stack

S

and a list

L

. Traverse down the left-most spine of the tree until reaching a leaf l', adding each node

n

to

S

. Add l' to

L

. The parent of l' (

p

) is at the top of the stack. Repeat the procedure for p's right subtree.

```mw
package org.wikipedia.example;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

import jakarta.annotation.NonNull;

class RopeLike {
    private RopeLike left;
    private RopeLike right;

    public RopeLike(RopeLike left, RopeLike right) {
        this.left = left;
        this.right = right;
    }

    public RopeLike getLeft() {
        return left;
    }

    public RopeLike getRight() {
        return right;
    }
}

public final class InOrderRopeIterator implements Iterator<RopeLike> {
    private final Deque<RopeLike> stack;

    public InOrderRopeIterator(@NonNull RopeLike root) {
        stack = new ArrayDeque<>();
        RopeLike c = root;
        while (c != null) {
            stack.push(c);
            c = c.getLeft();
        }
    }

    @Override
    public boolean hasNext() {
        return stack.size() > 0;
    }

    @Override
    public RopeLike next() {
        RopeLike result = stack.pop();

        if (!stack.isEmpty()) {
            RopeLike parent = stack.pop();
            RopeLike right = parent.getRight();
            if (right != null) {
                stack.push(right);
                RopeLike cleft = right.getLeft();
                while (cleft != null) {
                    stack.push(cleft);
                    cleft = cleft.getLeft();
                }
            }
        }

        return result;
    }
}
```

### Rebalance

Definition:

Collect the set of leaves

L

and rebuild the tree from the bottom-up.

```mw
import java.util.List;

static boolean isBalanced(RopeLike r) {
    int depth = r.depth();
    if (depth >= FIBONACCI_SEQUENCE.length - 2) {
        return false;
    }
    return FIBONACCI_SEQUENCE[depth + 2] <= r.weight();
}

static RopeLike rebalance(RopeLike r) {
    if (!isBalanced(r)) {
        List<RopeLike> leaves = Ropes.collectLeaves(r);
        return merge(leaves, 0, leaves.size());
    }
    return r;
}

static RopeLike merge(List<RopeLike> leaves) {
    return merge(leaves, 0, leaves.size());
}

static RopeLike merge(List<RopeLike> leaves, int start, int end) {
    int range = end - start;
    switch (range) {
        case 1:
            return leaves.get(start);
        case 2:
            return new RopeLikeTree(leaves.get(start), leaves.get(start + 1));
        default:
            int mid = start + (range / 2);
            return new RopeLikeTree(merge(leaves, start, mid), merge(leaves, mid, end));
    }
}
```

### Insert

Definition:

Insert(i, S’)

: insert the string

S’

beginning at position

i

in the string

s

, to form a new string

C

1

, ...,

C

i

,

S'

,

C

i

+ 1

, ...,

C

m

.

Time complexity:

⁠

$O(\log N)$

⁠

.

This operation can be done by a `Split()` and two `Concat()` operations. The cost is the sum of the three.

```mw
import javafx.util.Pair;

public Rope insert(int idx, CharSequence sequence) {
    if (idx == 0) {
        return prepend(sequence);
    } else if (idx == length()) {
        return append(sequence);
    } else {
        Pair<RopeLike, RopeLike> lhs = base.split(idx);
        return new Rope(Ropes.concat(lhs.getKey().append(sequence), lhs.getValue()));
    }
}
```

### Index

Definition:

Index(i)

: return the character at position

i

Time complexity:

⁠

$O(\log N)$

⁠

To retrieve the *i*-th character, we begin a recursive search from the root node:

```mw
@Override
public int indexOf(char ch, int startIndex) {
    if (startIndex > weight) {
        return right.indexOf(ch, startIndex - weight);
    } else {
        return left.indexOf(ch, startIndex);
    }
}
```

For example, to find the character at `i=10` in Figure 2.1 shown on the right, start at the root node (A), find that 22 is greater than 10 and there is a left child, so go to the left child (B). 9 is less than 10, so subtract 9 from 10 (leaving `i=1`) and go to the right child (D). Then because 6 is greater than 1 and there's a left child, go to the left child (G). 2 is greater than 1 and there's a left child, so go to the left child again (J). Finally 2 is greater than 1 but there is no left child, so the character at index 1 of the short string "na" (ie "n") is the answer. (1-based index)

### Concat

Definition:

Concat(S1, S2)

: concatenate two ropes,

S

1

and

S

2

, into a single rope.

Time complexity:

⁠

$O(1)$

⁠

(or

⁠

$O(\log N)$

⁠

time to compute the root weight)

A concatenation can be performed simply by creating a new root node with left = S1 and right = S2, which is constant time. The weight of the parent node is set to the length of the left child *S*1, which would take ⁠ $O(\log N)$ ⁠ time, if the tree is balanced.

As most rope operations require balanced trees, the tree may need to be re-balanced after concatenation.

### Split

Definition:

Split (i, S)

: split the string

S

into two new strings

S

1

and

S

2

,

S

1

=

C

1

, ...,

C

i

and

S

2

=

C

i

+ 1

, ...,

C

m

.

Time complexity:

⁠

$O(\log N)$

⁠

There are two cases that must be dealt with:

1. The split point is at the end of a string (i.e. after the last character of a leaf node)
2. The split point is in the middle of a string.

The second case reduces to the first by splitting the string at the split point to create two new leaf nodes, then creating a new node that is the parent of the two component strings.

For example, to split the 22-character rope pictured in Figure 2.3 into two equal component ropes of length 11, query the 12th character to locate the node *K* at the bottom level. Remove the link between *K* and *G*. Go to the parent of *G* and subtract the weight of *K* from the weight of *D*. Travel up the tree and remove any right links to subtrees covering characters past position 11, subtracting the weight of *K* from their parent nodes (only node *D* and *A*, in this case). Finally, build up the newly orphaned nodes *K* and *H* by concatenating them and creating a new parent *P* with weight equal to the length of the left node *K*.

As most rope operations require balanced trees, the tree may need to be re-balanced after splitting.

```mw
import javafx.util.Pair;

public Pair<RopeLike, RopeLike> split(int index) {
    if (index < weight) {
        Pair<RopeLike, RopeLike> split = left.split(index);
        return Pair.of(rebalance(split.getKey()), rebalance(new RopeLikeTree(split.getValue(), right)));
    } else if (index > weight) {
        Pair<RopeLike, RopeLike> split = right.split(index - weight);
        return Pair.of(rebalance(new RopeLikeTree(left, split.getKey())), rebalance(split.getValue()));
    } else {
        return Pair.of(left, right);
    }
}
```

### Remove

Definition:

Remove(i, j)

: remove the substring

C

i

, …,

C

i

+

j

− 1

, from

s

to form a new string

C

1

, …,

C

i

− 1

,

C

i

+

j

, …,

C

m

.

Time complexity:

⁠

$O(\log N)$

⁠

.

This operation can be done by two `Split()` and one `Concat()` operation. First, split the rope in three, divided by *i*-th and *i+j*-th character respectively, which extracts the string to remove in a separate node. Then concatenate the other two nodes.

```mw
import javafx.util.Pair;

@Override
public RopeLike remove(int start, int length) {
    Pair<RopeLike, RopeLike> lhs = split(start);
    Pair<RopeLike, RopeLike> rhs = split(start + length);
    return rebalance(new RopeLikeTree(lhs.getKey(), rhs.getValue()));
}
```

### Report

Definition:

Report(i, j)

: output the string

C

i

, …,

C

i

+

j

− 1

.

Time complexity:

⁠

$O(j+\log N)$

⁠

To report the string *Ci*, …, *C**i* + *j* − 1, find the node *u* that contains *Ci* and `weight(u) >= j`, and then traverse *T* starting at node *u*. Output *Ci*, …, *C**i* + *j* − 1 by doing an in-order traversal of *T* starting at node *u*.

## Comparison with monolithic arrays

Advantages:

- Ropes enable much faster insertion and deletion of text than monolithic string arrays, on which operations have time complexity O(n).
- Ropes do not require O(n) extra memory when operated upon (arrays need that for copying operations).
- Ropes do not require large contiguous memory spaces.
- If only nondestructive versions of operations are used, rope is a persistent data structure. For the text editing program example, this leads to an easy support for multiple undo levels.

Disadvantages:

- Greater overall space use when not being operated on, mainly to store parent nodes. There is a trade-off between how much of the total memory is such overhead and how long pieces of data are being processed as strings. The strings in example figures above are unrealistically short for modern architectures. The overhead is always O(n), but the constant can be made arbitrarily small.
- Increase in time to manage the extra storage
- Increased complexity of source code; greater risk of bugs

This table compares the *algorithmic* traits of string and rope implementations, not their *raw speed*. Array-based strings have smaller overhead, so (for example) concatenation and split operations are faster on small datasets. However, when array-based strings are used for longer strings, time complexity and memory use for inserting and deleting characters becomes unacceptably large. In contrast, a rope data structure has stable performance regardless of data size. Further, the space complexity for ropes and arrays are both O(n). In summary, ropes are preferable when the data is large and modified often.

| Operation | Rope | String |
|---|---|---|
| Index | O(log n) | O(1) |
| Split | O(log n) | O(1) |
| Concatenate | O(1) amortized, O(log n) worst case | O(n) |
| Iterate over each character | O(n) | O(n) |
| Insert | O(log n) | O(n) |
| Append | O(1) amortized, O(log n) worst case | O(1) amortized, O(n) worst case |
| Remove | O(log n) | O(n) |
| Report | O(j + log n) | O(j) |
| Build | O(n) | O(n) |
