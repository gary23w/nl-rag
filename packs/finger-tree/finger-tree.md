---
title: "Finger tree"
source: https://en.wikipedia.org/wiki/Finger_tree
domain: finger-tree
license: CC-BY-SA-4.0
tags: finger tree, functional data structure, persistent sequence, amortized analysis
fetched: 2026-07-02
---

# Finger tree

In computer science, a **finger tree** is a purely functional data structure that can be used to efficiently implement other functional data structures. A finger tree gives amortized constant time access to the "fingers" (leaves) of the tree, which is where data is stored, and concatenation and splitting logarithmic time in the size of the smaller piece. It also stores in each internal node the result of applying some associative operation to its descendants. This "summary" data stored in the internal nodes can be used to provide the functionality of data structures other than trees.

## Overview

Ralf Hinze and Ross Paterson state a finger tree is a functional representation of persistent sequences that can access the ends in amortized constant time. Concatenation and splitting can be done in logarithmic time in the size of the smaller piece. The structure can also be made into a general purpose data structure by defining the split operation in a general form, allowing it to act as a sequence, priority queue, search tree, or priority search queue, among other varieties of abstract data types.

A *finger* is a point where one can access *part* of a data structure; in imperative languages, this is called a pointer. In a finger tree, the fingers are structures that point to the ends of a sequence, or the leaf nodes. The fingers are added on to the original tree to allow for constant time access to fingers. In the images shown below, the fingers are the lines reaching out of the spine to the nodes.

A finger tree is composed of different *layers* which can be identified by the nodes along its *spine*. The spine of a tree can be thought of as the trunk in the same way trees have leaves and a root. Though finger trees are often shown with the spine and branches coming off the sides, there are actually two nodes on the spine at each level that have been paired to make this central spine. The *prefix* is on the left of the spine, while the *suffix* is on the right. Each of those nodes has a link to the next level of the spine until they reach the root.

The first level of the tree contains only values, the leaf nodes of the tree, and is of depth 0. The second level is of depth 1. The third is of depth 2 and so on. The closer to the root, the deeper the subtrees of the original tree (the tree before it was a finger tree) the nodes points to. In this way, working down the tree is going from the leaves to the root of the tree, which is the opposite of the typical tree data structure. To get this nice and unusual structure, we have to make sure the original tree has a uniform depth. To ensure that the depth is uniform, when declaring the node object, it must be parameterized by the type of the child. The nodes on the spine of depth 1 and above point to trees, and with this parameterization they can be represented by the nested nodes.

### Transforming a tree into a finger tree

We will start this process with a balanced 2–3 tree. For the finger tree to work, all the leaf nodes need to also be level.

A finger is "a structure providing efficient access to nodes of a tree near a distinguished location." To make a finger tree we need to put fingers to the right and left ends of the tree and transform it like a zipper. This gives us that constant amortized time access to the ends of a sequence.

To transform, start with the balanced 2–3 tree.

Take the leftmost and rightmost internal nodes of the tree and pull them up so the rest of the tree dangles between them as shown in the image to the right.

Combines the spines to make a standard 2–3 finger tree.

This can be described as:

```mw
data FingerTree a 
  = Empty 
  | Single a 
  | Deep (Digit a) (FingerTree (Node a)) (Digit a)

data Node a 
  = Node2 a a 
  | Node3 a a a
```

The digits in the examples shown are the nodes with letters. Each list is divided by the prefix or suffix of each node on the spine. In a transformed 2–3 tree it seems that the digit lists at the top level can have a length of two or three with the lower levels only having length of one or two. In order for some application of finger trees to run so efficiently, finger trees allow between one and four subtrees on each level.

The digits of the finger tree can be transformed into a list like so:

```mw
 
type Digit a = One a | Two a a | Three a a a | Four a a a a
```

And so on the image, the top level has elements of type *a*, the next has elements of type *Node a* because the node in between the spine and leaves, and this would go on meaning in general that the *n*th level of the tree has elements of type $Node^{n}$ *a*, or 2–3 trees of depth n. This means a sequence of *n* elements is represented by a tree of depth Θ(log *n*). Even better, an element *d* places from the nearest end is stored at a depth of Θ(log d) in the tree.

This process can also be done with other trees, like the 2–3–4 tree at right. This helps to see that the Digits are actually the annotations which were inside the tree, and each digit is conceptually associated with a subtree that may be empty.

#### Reductions

${\begin{aligned}\mathrm {instance} &\ Reduce\ Node\ \mathrm {where} &&\\&reducer\ (\prec )\ (Node2\ a\ b)\ z&=&\ a\ \prec (b\ \prec \ z)\\&reducer\ (\prec )\ (Node3\ a\ b\ c)\ z&=&\ a\ \prec (\ b\prec (c\ \prec \ z))\\\\&reducel\ (\succ )\ z\ (Node2\ b\ a)\ &=&\ (z\ \succ \ b)\ \succ \ a\\&reducel\ (\succ )\ z\ (Node3\ c\ b\ a)\ &=&\ ((z\ \succ \ c)\succ \ b)\succ \ a\\\end{aligned}}$ ${\begin{aligned}\mathrm {instance} &\ Reduce\ FingerTree\ \mathrm {where} &&\\&reducer\ (\prec )\ (Empty)\ z\ &=&\ z\\&reducer\ (\prec )\ (Single\ x)\ z&=&\ x\ \prec \ z\\&reducer\ (\prec )\ (Deep\ pr\ m\ sf)\ z&=&\ pr\ \prec '\ (m\ \prec ''\ (sf\ \prec '\ z))\\&\ \ \ \ where\\&\ \ \ \ \ \ \ \ (\prec ')\ =reducer\ (\prec )\\&\ \ \ \ \ \ \ \ (\prec '')\ =reducer\ (reducer\ (\prec ))\\\\&reducel\ (\succ )\ z\ (Empty)\ &=&\ z\\&reducel\ (\succ )\ z\ (Single\ \ x)\ &=&\ z\ \succ \ x\\&reducel\ (\succ )\ z\ (Deep\ \ pr\ m\ sf)\ &=&\ ((z\ \succ '\ pr)\ \succ ''\ m)\ \succ '\ sf)\\&\ \ \ \ where\\&\ \ \ \ \ \ \ \ (\succ ')\ =reducel\ (\succ )\\&\ \ \ \ \ \ \ \ (\succ '')\ =reducel\ (reducel\ (\succ ))\\\end{aligned}}$

### Deque operations

Finger trees also make efficient deques. Whether the structure is persistent or not, all operations take Θ(1) amortized time. The analysis can be compared to Okasaki's implicit deques, the only difference being that the FingerTree type stores Nodes instead of pairs.

## Application

Finger trees can be used to build other trees. For example, a priority queue can be implemented by labeling the internal nodes by the minimum priority of its children in the tree, or an indexed list/array can be implemented with a labeling of nodes by the count of the leaves in their children. Other applications are random-access sequences, described below, ordered sequences, and interval trees.

Finger trees can provide amortized O(1) pushing, reversing, popping, O(log n) append and split; and can be adapted to be indexed or ordered sequences. And like all functional data structures, it is inherently persistent; that is, older versions of the tree are always preserved.

### Random-access sequences

Finger trees can efficiently implement random-access sequences. This should support fast positional operations including accessing the *n*th element and splitting a sequence at a certain position. To do this, we annotate the finger tree with sizes.

```mw
newtype Size = Size{ getSize :: N }
  deriving (Eq, Ord)

instance Monoid Size where
  ∅ = Size 0
  Size m ⊕ Size n = Size (m + n)
```

The *N* is for natural numbers. The new type is needed because the type is the carrier of different monoids. Another new type is still needed for the elements in the sequence, shown below.

```mw
newtype Elem a = Elem{ getElem :: a }
newtype Seq a = Seq (FingerTree Size (Elem a))

instance Measured (Elem a) Size where
  ||Elem|| = Size 1
```

These lines of code show that instance works a base case for measuring the sizes and the elements are of size one. The use of **newtype**s doesn't cause a run-time penalty in Haskell because in a library, the *Size* and *Elem* types would be hidden from the user with wrapper functions.

With these changes, the length of a sequence can now be computed in constant time.

## First publication

Finger trees were first published in 1977 by Leonidas J. Guibas, and periodically refined since (e.g. a version using AVL trees, non-lazy finger trees, simpler 2–3 finger trees shown here, B-Trees and so on)

## Implementations

Finger trees have since been used in the Haskell core libraries (in the implementation of *Data.Sequence*), and an implementation in OCaml exists which was derived from a proven-correct Rocq implementation. There is also a verified implementation in Isabelle (proof assistant) from which programs in Haskell and other (functional) languages can be generated. Finger trees can be implemented with or without lazy evaluation, but laziness allows for simpler implementations.
