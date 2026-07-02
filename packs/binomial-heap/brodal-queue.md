---
title: "Brodal queue"
source: https://en.wikipedia.org/wiki/Brodal_queue
domain: binomial-heap
license: CC-BY-SA-4.0
tags: binomial heap, mergeable heap, priority queue, meldable heap
fetched: 2026-07-02
---

# Brodal queue

In computer science, the **Brodal queue** is a heap/priority queue structure with very low worst case time bounds: $O(1)$ for insertion, find-minimum, meld (merge two queues) and decrease-key and $O(\mathrm {log} (n))$ for delete-minimum and general deletion. They are the first heap variant to achieve these bounds without resorting to amortization of operational costs. Brodal queues are named after their inventor Gerth Stølting Brodal.

While having better asymptotic bounds than other priority queue structures, they are, in the words of Brodal himself, "quite complicated" and "[not] applicable in practice." Brodal and Okasaki describe a persistent (purely functional) version of Brodal queues.

## Definition

A Brodal queue is a set of two trees $T_{1}$ and $T_{2}$ and 5 *guides*. The definition of the guide data structure can be found in the following section. For both trees, each node has a *rank*, this rank is useful for later operations and intuitively corresponds to the logarithm of the size of the subtree rooted in the node. We note ${\text{arity}}_{i}(x)$ the number of children of the node x with rank i . We will also use $t_{1}$ for the root of tree $T_{1}$ and $t_{2}$ for the root of tree $T_{2}$ . At each given time, every subtree rooted in a node needs to fulfill these 5 invariants (which will be later called ${\text{RANK}}$ invariants):

- ${\text{LEAF-RANK}}$  : If x is a leaf, then ${\text{rank}}(x)=0$ ,
- ${\text{PARENT-RANK}}$  : ${\text{rank}}(x)<{\text{rank}}({\text{parent}}(x))$ ,
- ${\text{NEXT-RANK-ARITY}}$  : If ${\text{rank}}(x)>0$ , then ${\text{arity}}_{{\text{rank}}(x)-1}(x)\geqslant 2$ ,
- ${\text{ARITY-BOUND}}$ : ${\text{arity}}_{i}(x)\in \{0,2,3,\dots ,7\}$ we highlight that ${\text{arity}}_{i}(x)\neq 1$ ,
- ${\text{ROOT-RANK}}$  : $T_{2}=\emptyset$ or ${\text{rank}}(t_{1})\leqslant {\text{rank}}(t_{2})$ .

Here ${\text{NEXT-RANK-ARITY}}$ guarantees us that the size of the subtree rooted in a node is at least exponential to the rank of that node. In addition, ${\text{ARITY-BOUND}}$ bounds the number of children of each rank for a given node, this implies that all nodes have rank and degrees in $O(\log n)$ .

In a Brodal queue, not every node will have a bigger value than its parent, the nodes vialoating this condition will be called *violating nodes*. However, we want to keep the number of *violating nodes* relatively small. To keep track of violating nodes, we create for each node two sets $V(x)$ and $W(x)$ of nodes larger than x . Intuitively, $V(x)$ are the nodes larger of x with large rank (such that $y\in V(x)$ if ${\text{rank}}(y)\geqslant {\text{rank}}(t_{1})$ ), and $W(x)$ are the nodes with small rank ( ${\text{rank}}(y)<{\text{rank}}(t_{1})$ ). These sets are implemented using doubly linked list meaning they have an order. In particular, all violating nodes added to $V(x)$ are added at the front of the list, and all violating nodes added to $W(x)$ are inserted next to a node of same rank. We let $w_{i}(x)$ denote the number of nodes in $W(x)$ of rank i The $V(x)$ and $W(x)$ lists fulfill these 5 invariants (we will call the ${\text{SETS}}$ invariants):

- ${\text{MINIMUM-NODE}}$  : $t_{1}=\min(T_{1}\cup T_{2})$
- ${\text{VIOLATING-CONDITION}}$  : If $y\in V(x)\cup W(x)$ then $y\geqslant x$
- ${\text{PARENT-VIOLATING}}$ : If $y<{\text{parent}}(y)$ then there exist a node $x\neq y$ such that $y\in V(x)\cup W(x)$
- ${\text{W-RANK-BOUND}}$ : $w_{i}(x)\leqslant 6$
- ${\text{V-RANK-BOUND}}$ : By denoting $V(x)=(v_{|V(x)|},\dots ,v_{2},v_{1})$ , we have: ${\text{rank}}(v_{i})\geqslant \left\lfloor {\frac {i-1}{\alpha }}\right\rfloor$ for a certain constant $\alpha$ .

Since all nodes have rank in $O(\log n)$ the ${\text{W-RANK-BOUND}}$ and ${\text{V-RANK-BOUND}}$ , all $V(x)$ and $W(x)$ are in size $O(\log n)$ .

We also have some invariants of the roots of the trees $T_{1}$ and $T_{2}$ : $t_{1}$ and $t_{2}$ (called the ${\text{ROOTS}}$ invariants).

- ${\text{ROOT-ARITY}}$  : $t_{i}\in \{2,3,\dots ,7\}{\text{ for }}i\in \{0,1,\dots ,{\text{rank}}(t_{i})-1\}$ ,
- ${\text{V-SIZE-BOUND}}$ : $|V(x)|\leqslant \alpha {\text{ rank}}(t_{1})$ ,
- ${\text{W-ELEMENTS-RANK}}$ : if $y\in W(t_{1})$ , then ${\text{rank}}(y)<{\text{rank}}(t_{1})$ .

The ${\text{V-SIZE-BOUND}}$ invariant essentially tells us that if we increase the rank of $t_{1}$ by one, we have at most $\alpha$ new "large" violations (here large means having a high rank) without violating the ${\text{V-RANK-BOUND}}$ invariant. On the other hand, the ${\text{W-ELEMENTS-RANK}}$ invariant tells us that all violations in $W(x)$ are "small", this invariant is true per the definition of W . Maintaining the invariants ${\text{W-RANK-BOUND}}$ and ${\text{ROOT-ARITY}}$ is not trivial, to maintain these we will use the ${\text{DecreaseKey}}$ operation which can be implemented using a *guide* as defined in the next section. Each time we will call the ${\text{DecreaseKey}}$ operation, we will essentially :

1. Add the new violation to $V(t_{1})$ or $W(t_{1})$ depending on the rank of that violation.
2. To avoid $V(t_{1})$ and $W(t_{1})$ from getting too large, we incrementally do two kinds of transformations:
  1. Moving the sons of $t_{2}$ to $t_{1}$ to increase the rank of $t_{1}$
  2. Reducing the number of violations in $W(t_{1})$ by replacing two violations of rank k to one violation of rank $k+1$

## The guide data structure

This definition is based on the definition from Brodal's paper.

We assume that we have a sequence of variables $x_{k},\dots ,x_{1}$ and we want to make sure that $\forall i\leqslant k,x_{i}\leqslant T$ for some threshold T . The only operation allowed is ${\text{REDUCE}}(i)$ which decreases $x_{i}$ by at least 2 and increases $x_{i+1}$ by at most 1. We can assume without loss of generality that ${\text{REDUCE}}(i)$ reduces $x_{i}$ by 2 and increases $x_{i+1}$ by 1.

If a $x_{j}$ is increased by one, the goal of the guide is to tell us on which indices i to apply ${\text{REDUCE}}(i)$ in order to respect the threshold. The guide is only allowed to make $O(1)$ calls to the ${\text{REDUCE}}$ function for each increase.

The guide has access to another sequence $x'_{k},\dots ,x'_{1}$ such that $x_{i}\leqslant x'_{i}$ and $x'_{i}\in \{T-2,T-1,T\}$ . As long as after the increase of $x_{j}$ we have $x_{j}\leqslant x'_{j}$ we do not need to ask help from our guide since $x_{j}$ is "far" bellow T . However, if $x_{j}=x'_{j}$ before the increase, then we have $x_{j}+1>x'_{j}$ after the change.

To simplify the explanation, we can assume that $T=2$ , so that $x'_{i}\in \{0,1,2\}$ . The guide will create *blocks* in the sequence of $x'_{i}$ of form $2,1,1,\dots ,1,0$ where we allow there to be no 1 . The guide maintains the invariant that each element which isn't in a block is either a 1 or a 0 . For example, here are the blocks for a sequence of $x'_{i}$ .

${\textstyle 1,{\underline {2,1,1,0}},1,1,{\underline {2,0}},{\underline {2,0}},1,0,{\underline {2,1,0}}}$

The guide is composed of 3 arrays :

- x the array of $x_{k},\dots ,x_{1}$
- $x'$ the array of $x'_{k},\dots ,x'_{1}$
- p an array of pointers where all the $p_{i}$ for which $x'_{i}$ are in the same block will point to the same memory cell containing a value. If a $x'_{i}$ is not in a block, then $p_{i}$ points to a memory cell containing $\bot$ .

With this definition, a guide has two important properties :

1. For each element in a block, we can find the most left element of the block in time $O(1)$ .
2. We can destroy a block in time $O(1)$ by assigning $\bot$ to the memory cell pointed to by each element of the block.

This way, the guide is able to decide which indices to ${\text{REDUCE}}$ in time $O(1)$ . Here is an example :

${\begin{array}{ll}{\underline {2,1,1,0}},{\underline {2,1,1,1,0}}&\\{\underline {2,1,1,0}},{\underline {2,{\color {red}2},1,1,0}}&{\text{Increment }}x'_{i}\\{\underline {2,1,1,{\color {green}1}}},{\underline {{\color {blue}0},2,1,1,0}}&{\text{REDUCE}}\\{\underline {2,1,1,1}},{\underline {{\color {green}1},{\color {blue}0},1,1,0}}&{\text{REDUCE}}\\{\underline {2,1,1,1,1,0}},1,1,0&{\text{reestablish blocks}}\\\end{array}}$

To reestablish the blocks, the pointers of the 1 and 0 added to the first block now point to the same cell as all the other elements from the first block, and the value of the second block's cell is changed to $\bot$ . In the previous example, only two ${\text{REDUCE}}$ operations were needed, this is actually the case for all instances. Therefore, the queue only needs $O(1)$ operations to reestablish the property.

## Operations of a Brodal Queue

To implement the different priority queue operations we first need to describe some essential transformations for the trees.

### Transformations

#### Linking trees

To link trees, we need three nodes $x_{1},x_{2}{\text{ and }}x_{3}$ of equal rank. We can calculate the minimum of these three nodes with two comparisons. Here we assume that $x_{1}$ is the minimum but the process is similar for all $x_{i}$ . We can now make the nodes $x_{2}$ and $x_{3}$ the two leftmost sons of $x_{1}$ and increase the rank of $x_{1}$ by one. This preserves all the ${\text{RANK}}$ and ${\text{SETS}}$ invariants.

#### Delinking trees

If x has exactly two or three sons of rank ${\text{rank}}(x)-1$ , we can remove these sons and x gets the rank of its new largest son plus one. From the ${\text{ARITY-BOUND}}$ condition, we know that that the ${\text{NEXT-RANK-ARITY}}$ invariant will be preserved. Then, all the ${\text{RANK}}$ and ${\text{SETS}}$ invariants remain satisfied. If x has 4 or more children, we can simply cut of two of them and all the invariants remain true. Therefore, the delinking of a tree of rank k will always result in two or three trees of rank $k-1$ (from the 2 or 3 children cut off) and one additional tree of rank at most k .

#### Maintaining the sons of a root

When we add and remove sons of a root, we want to keep the ${\text{ROOT-RANK}}$ invariant true. For this purpose, we use 4 guides, two for each roots $t_{1}$ and $t_{2}$ . To have constant time access to the son of $t_{1}$ we create an extendible array of pointed that has for each rank $i\in \{0,\dots ,{\text{rank}}(t_{1})-1\}$ a pointer to a son of $t_{1}$ of rank i . One guide will maintain the condition that ${\text{arity}}_{i}(t_{1})\leqslant 7$ and the other maintains ${\text{arity}}_{i}(t_{1})\geqslant 2$ both for $i\in \{0,\dots ,{\text{rank}}(t_{1})-3\}$ . The sons of $t_{1}$ of rank ${\text{rank}}(t_{1})-1$ and ${\text{rank}}(t_{1})-2$ are treated separately in a straight forward way to maintant their number between 2 and 7. The equivalent to the $x'_{i}$ variable in the definition of the guide will have the values $\{5,6,7\}$ for the higher bound guide and $\{4,3,2\}$ for the lower bound.

In this context, when we add a child of rank i to the root, we increase $x'_{i}$ by one, and apply the ${\text{REDUCE}}$ operations. The ${\text{RECUCE}}(i)$ operation here consists of linking three trees of rank i which creates a new child of rank $i+1$ . Therefore, we decrease ${\text{arity}}_{i}(t_{1})$ by three and increase ${\text{arity}}_{i+1}(t_{1})$ by one. If this increase results in too many sons of rank ${\text{rank}}(t_{1})-2$ or ${\text{rank}}(t_{1})-1$ we link some of these sons together and possibly increase the rank of $t_{1}$ . If we increase the rank of $t_{1}$ , we have to increase the length of the extendible array managed by the guides.

Cutting off a son from $t_{1}$ is very similar, except here the ${\text{REDUCE}}$ operation corresponds to the delinking of a tree.

For the root $t_{2}$ the situation is nearly the same. However, since ${\text{MINIMUM-NODE}}$ guarantees us that $t_{1}$ is the minimum element, we know that we won't create any violation by linking or delinking children of $t_{1}$ . The same cannot be said for $t_{2}$ . Linking sons will never create new violations but the delinking of sons can create up to three new violations. The tree left over by a delinking is made a son of $t_{1}$ if it has rank less than ${\text{rank}}(t_{1})$ and otherwise it becomes a son of $t_{2}$ . The new violations which have rank larger than ${\text{rank}}(t_{1})$ are added to $V(t_{1})$ . To maintain the invariants on the $V(t_{1})$ set (namely ${\text{V-RANK-BOUND}}$ and ${\text{V-SIZE-BOUND}}$ ), we have to guarantee that the rank of $t_{1}$ will be increased and that $\alpha$ in those invariants is chosen large enough.

#### Violation reducing

The goal of this transformation is to reduce the total amount of potential violations, meaning reducing $\left|\bigcup _{x\in T_{1}\cup T_{2}}V(x)\cup W(x)\right|$ .

We assume we have two potential violations $x_{1}$ and $x_{2}$ of equal rank k . We then have several cases:

1. If one of the nodes turns out not to be a violation, we just remove it from its corresponding violation set.
2. Otherwise, both nodes are violations. Because of ${\text{ARITY-BOUND}}$ , we know that both $x_{1}$ and $x_{2}$ have at least one brother. Then:
  1. If $x_{1}$ and $x_{2}$ are not brothers, then we can assume without losing generality that ${\text{parent}}(x_{1})\leqslant {\text{parent}}(x_{2})$ , we can then swap the subtrees rooted in $x_{1}$ and $x_{2}$ . The number of violations can only go down during that swap.
  2. Else, $x_{1}$ and $x_{2}$ are brothers of a node we will call y .
    1. If $x_{1}$ has more than one brother of rank k , we can just cut off $x_{1}$ and make it a non violating node of $t_{1}$ as described in the previous subsection.
    2. Else, $x_{1}$ and $x_{2}$ are the only children of rank k of y ..
      1. If ${\text{rank}}(y)>k+1$ , we can cut off both $x_{1}$ and $x_{2}$ nodes from y and make them non violating nodes of $t_{1}$ as described in the previous subsection
      2. Else, ${\text{rank}}(y)=k+1$ . We will cut off $x_{1},x_{2}{\text{ and }}y$ , the new rank of y will be one plus the rank of its leftmost son, We replace y by a son on $t_{1}$ of rank $k+1$ , which can be cut off as described in the previous subsection. If the replacement for y becomes a violating node of rank $k+1$ , we add it to $W(t_{1})$ . Finally we make $x_{1},x_{2}{\text{ and }}y$ new sons of $t_{1}$ as described above.

#### Avoiding too many violations

The only violation sets where we will add violations are $V(t_{1})$ and $W(t_{1})$ . As described above, the invariants on those sets are maintained using guides. When we add a violation to $W(t_{1})$ we have two cases:

1. If there are exactly 6 violations of the given rank and there are at least two violating nodes which aren't sons of $t_{2}$ , we apply the ${\text{REDUCE}}$ operations given by the guide.
2. If there are more than 4 violations which are sons of $t_{2}$ , we cut the additional violations off and link them below $t_{1}$ . This removes the violation created by these nodes and doesn't affect the guide maintaining the sons of $t_{2}$ .

For each priority queue operation that is performed, we increase the rank of $t_{1}$ by at least one by moving a constant number of sons of $t_{2}$ to $t_{1}$ (provided that $T_{2}\neq \emptyset$ ). Increasing the rank of $t_{1}$ allows us to add violations to $V(t_{1})$ while still maintaining all our invariants. If $T_{2}\neq \emptyset$ and ${\text{rank}}(t_{2})\leqslant {\text{rank}}(t_{1})+2$ we can cut the largest sons of $t_{2}$ , link them to $t_{1}$ and then make $t_{2}$ a son of $t_{1}$ . This satisfies all the invariants. Otherwise, we cut off a son of $t_{2}$ of rank ${\text{rank}}(t_{1})+2$ , delink this son and add the resulting trees to $t_{1}$ . If $T_{2}=\emptyset$ , we know that $t_{1}$ is the node of largest rank, therefore we know that no large violations can be created.

### Priority queue operations

#### MakeQueue

${\text{MakeQueue}}()$ just returns a pair of empty trees.

#### FindMin

${\text{FindMin}}(Q)$ returns $t_{1}$ .

#### Insert

${\text{Insert}}(Q,e)$ is only a special case of ${\text{Meld}}(Q_{1},Q_{2})$ where $Q_{2}$ is a queue only containing e and $Q_{1}=Q$ .

#### Meld

${\text{Meld}}(Q_{1},Q_{2})$ involves four trees (two for each queue). The tree having the minimum root becomes the new $T_{1}$ tree. If this tree is also the tree of maximum rank, we can add all the other trees below as described previously. In this case, no violating node is created so no transformation is done on violating nodes. Otherwise, the tree of maximum rank becomes the new $T_{2}$ tree and the other trees are added below as described in the section "Maintaining the sons of a root". If some trees have equal rank to this new $T_{2}$ , we can delink them before adding them. The violations created are handled as explained in the section : "Avoiding too many violations".

#### DecreaseKey

${\text{DecreaseKey}}(Q,e,e')$ replaces the element of e by $e'$ (with $e'\leqslant e$ ). If $e'<t_{1}$ , we swap the two nodes, otherwise, we handle the potential new violation as explained in the section "Avoiding too many violations".

#### DeleteMin

${\text{DeleteMin}}(Q)$ is allowed to take worst case time $O(\log n)$ . First, we completely empty $T_{2}$ by moving all the sons of $t_{2}$ to $t_{1}$ then making $t_{2}$ a rank 0 son of $t_{1}$ . Then, $t_{1}$ is deleted, this leaves us with at most $O(\log n)$ independent trees. The new minimum is then found by looking at the violating sets of the old root and looking at all the roots of the new trees. If the minimum element is not a root, we can swap a root from a tree of equal rank to it. This creates at most one violation. Then, we make the independent trees sons of the new minimum element by performing $O(\log n)$ linking and delinking operations. This reestablishes the ${\text{RANK}}$ and ${\text{ROOTS}}$ invariants. By merging the V and W sets of the new root along with the V and W sets of the old root together, we get one new violation set of size $O(\log n)$ . By doing at most $O(\log n)$ violation reducing transformations we can make the violation set only contain at most one element of each rank. This set will be our new W set and the new V set is empty. This reestablishes the ${\text{SETS}}$ invariants. We also have to initialise a new guide for the new root $t_{1}$ .

#### Delete

Here, $-\infty$ denotes the smallest possible element. ${\text{Delete}}(Q,e)$ can simply be implemented by calling ${\text{DecreaseKey}}(Q,e,-\infty )$ followed by ${\text{DeleteMin}}(Q)$ .

## Implementation details

In this section, we summarize some implementation details for the Brodal Queue data structure.

In each tree, each node is a record having the following fields:

- The element associated with the node (its value),
- The rank of the node,
- pointers to the node's left and right brothers,
- a pointer to the father node,
- a pointer to the leftmost son,
- pointers to the first element of the node's V and W sets,
- pointers to the following and previous element in the violation set the node belongs to. If this node is the first node of the violation set $V(x)$ or $W(x)$ it belongs to, the previous pointer points to x .
- an array of pointers to sons of $t_{1}$ of rank i (with $i\in \{0,\dots ,{\text{rank}}(t_{1})-1\}$ ),
- a similar array for $t_{2}$ ,
- an array of pointers to nodes in $W(t_{1})$ of rank i (with $i\in \{0,\dots ,{\text{rank}}(t_{1})-1\}$ ).

Finally, we have 5 guides: three to maintain the upper bounds on ${\text{arity}}_{i}(t_{1})$ , ${\text{arity}}_{i}(t_{2})$ and $w_{i}(t_{1})$ and two to maintain the lower bounds on ${\text{arity}}_{i}(t_{1})$ and ${\text{arity}}_{i}(t_{2})$ .

Due to its high amount of pointers and sets to keep track of, the Brodal Queue is extremely hard to implement. For this reason it is best described as a purely theoretical object to lower time complexity on algorithms like Dijkstra's algorithm. However, the Brodal has been implemented in Scala (the GitHub repository can be found here: https://github.com/ruippeixotog/functional-brodal-queues). In his paper, Gerth Stølting Brodal mentions that: "An important issue for further work is to simplify the construction to make it applicable in practice".

## Summary of running times

Here are time complexities of various heap data structures. The abbreviation am. indicates that the given complexity is amortized, otherwise it is a worst-case complexity. For the meaning of "*O*(*f*)" and "*Θ*(*f*)" see Big O notation. Names of operations assume a min-heap.

| Operation | find-min | delete-min | decrease-key | insert | meld | make-heap |
|---|---|---|---|---|---|---|
| Binary | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(*n*) | *Θ*(*n*) |
| Skew | *Θ*(1) | *O*(log *n*) am. | *O*(log *n*) am. | *O*(log *n*) am. | *O*(log *n*) am. | *Θ*(*n*) am. |
| Leftist | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(*n*) |
| Binomial | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(1) am. | *Θ*(log *n*) | *Θ*(*n*) |
| Skew binomial | *Θ*(1) | *Θ*(log *n*) | *Θ*(log *n*) | *Θ*(1) | *Θ*(log *n*) | *Θ*(*n*) |
| 2–3 heap | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) | *Θ*(1) am. | *O*(log *n*) | *Θ*(*n*) |
| Bottom-up skew | *Θ*(1) | *O*(log *n*) am. | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) am. | *Θ*(*n*) am. |
| Pairing | *Θ*(1) | *O*(log *n*) am. | *o*(log *n*) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Rank-pairing | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Fibonacci | *Θ*(1) | *O*(log *n*) am. | *Θ*(1) am. | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Strict Fibonacci | *Θ*(1) | *Θ*(log *n*) | *Θ*(1) | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |
| Brodal | *Θ*(1) | *Θ*(log *n*) | *Θ*(1) | *Θ*(1) | *Θ*(1) | *Θ*(*n*) |

1. *make-heap* is the operation of building a heap from a sequence of *n* unsorted elements. It can be done in *Θ*(*n*) time whenever *meld* runs in *O*(log *n*) time (where both complexities can be amortized). Another algorithm achieves *Θ*(*n*) for binary heaps.
2. For persistent heaps (not supporting *decrease-key*), a generic transformation reduces the cost of *meld* to that of *insert*, while the new cost of *delete-min* is the sum of the old costs of *delete-min* and *meld*. Here, it makes *meld* run in *Θ*(1) time (amortized, if the cost of *insert* is) while *delete-min* still runs in *O*(log *n*). Applied to skew binomial heaps, it yields Brodal-Okasaki queues, persistent heaps with optimal worst-case complexities.
3. Lower bound of $\Omega (\log \log n),$ upper bound of $O(2^{2{\sqrt {\log \log n}}}).$
4. Brodal queues and strict Fibonacci heaps achieve optimal worst-case complexities for heaps. They were first described as imperative data structures. The Brodal-Okasaki queue is a persistent data structure achieving the same optimum, except that *decrease-key* is not supported.

## Gerth Stølting Brodal

Gerth Stølting Brodal is a professor at the University of Aarhus, Denmark. He is best known for the Brodal queue.
