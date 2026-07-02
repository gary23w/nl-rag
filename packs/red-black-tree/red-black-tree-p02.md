---
title: "Red–black tree (part 2/2)"
source: https://en.wikipedia.org/wiki/Red–black_tree
domain: red-black-tree
license: CC-BY-SA-4.0
tags: red-black tree, balanced binary tree, self-balancing tree, left-leaning red-black tree
fetched: 2026-07-02
part: 2/2
---

## Parallel algorithms

Parallel algorithms for constructing red–black trees from sorted lists of items can run in constant time or $O(\log \log n)$ time, depending on the computer model, if the number of processors available is asymptotically proportional to the number n of items where $n\to \infty$ . Fast search, insertion, and deletion parallel algorithms are also known.

The join-based algorithms for red–black trees are parallel for bulk operations, including union, intersection, construction, filter, map-reduce, and so on.

### Parallel bulk operations

Basic operations like insertion, removal or update can be parallelised by defining operations that process bulks of multiple elements. It is also possible to process bulks with several basic operations, for example bulks may contain elements to insert and also elements to remove from the tree.

The algorithms for bulk operations aren't just applicable to the red–black tree, but can be adapted to other sorted sequence data structures also, like the 2–3 tree, 2–3–4 tree and (a,b)-tree. In the following different algorithms for bulk insert will be explained, but the same algorithms can also be applied to removal and update. Bulk insert is an operation that inserts each element of a sequence I into a tree T .

#### Join-based

This approach can be applied to every sorted sequence data structure that supports efficient join- and split-operations. The general idea is to split I and T in multiple parts and perform the insertions on these parts in parallel.

1. First the bulk I of elements to insert must be sorted.
2. After that, the algorithm splits I into $k\in \mathbb {N} ^{+}$ parts $\langle I_{1},\cdots ,I_{k}\rangle$ of about equal sizes.
3. Next the tree T must be split into k parts $\langle T_{1},\cdots ,T_{k}\rangle$ in a way, so that the ranges of $I_{m}$ and $T_{n}$ overlap for corresponding parts only ( $m=n$ ); in other words, thanks to the ordering, for every $j\in \mathbb {N} ^{+}|\,1\leq j<k$ following constraints hold:
  1. ${\text{last}}(I_{j})<{\text{first}}(T_{j+1})$
  2. ${\text{last}}(T_{j})<{\text{first}}(I_{j+1})$
4. Now the algorithm inserts each element of $I_{j}$ into $T_{j}$ sequentially. This step must be performed for every j, which can be done by up to k processors in parallel.
5. Finally, the resulting trees will be joined to form the final result of the entire operation.

Note that in Step 3 the constraints for splitting I assure that in Step 5 the trees can be joined again and the resulting sequence is sorted.

- (initial tree) initial tree
- (split I and T) split I and T
- (insert into the split T) insert into the split T
- (join T) join T

The pseudo code shows a simple divide-and-conquer implementation of the join-based algorithm for bulk-insert. Both recursive calls can be executed in parallel. The join operation used here differs from the version explained in this article, instead join2 is used, which misses the second parameter k.

```
bulkInsert(T, I, k):
    I.sort()
    bulklInsertRec(T, I, k)

bulkInsertRec(T, I, k):
    if k = 1:
        forall e in I: T.insert(e)
    else
        m := ⌊size(I) / 2⌋
        (T1, _, T2) := split(T, I[m])
        bulkInsertRec(T1, I[0 .. m], ⌈k / 2⌉)
            || bulkInsertRec(T2, I[m + 1 .. size(I) - 1], ⌊k / 2⌋)
        T ← join2(T1, T2)
```

##### Execution time

Sorting I is not considered in this analysis.

| #recursion levels | $\in O(\log k)$ |
|---|---|
| T(split) + T(join) | $\in O(\log \|T\|)$ |
| insertions per thread | $\in O\left({\frac {\|I\|}{k}}\right)$ |
| T(insert) | $\in O(\log \|T\|)$ |
| **T(bulkInsert) with k = #processors** | $\in O\left(\log k\log \|T\|+{\frac {\|I\|}{k}}\log \|T\|\right)$ |

This can be improved by using parallel algorithms for splitting and joining. In this case the execution time is $\in O\left(\log |T|+{\frac {|I|}{k}}\log |T|\right)$ .

##### Work

| #splits, #joins | $\in O(k)$ |
|---|---|
| W(split) + W(join) | $\in O(\log \|T\|)$ |
| #insertions | $\in O(\|I\|)$ |
| W(insert) | $\in O(\log \|T\|)$ |
| **W(bulkInsert)** | $\in O(k\log \|T\|+\|I\|\log \|T\|)$ |

#### Pipelining

Another method of parallelizing bulk operations is to use a pipelining approach. This can be done by breaking the task of processing a basic operation up into a sequence of subtasks. For multiple basic operations the subtasks can be processed in parallel by assigning each subtask to a separate processor.

1. First the bulk I of elements to insert must be sorted.
2. For each element in I the algorithm locates the according insertion position in T. This can be done in parallel for each element $\in I$ since T won't be mutated in this process. Now I must be divided into subsequences S according to the insertion position of each element. For example $s_{n,{\mathit {left}}}$ is the subsequence of I that contains the elements whose insertion position would be to the left of node n.
3. The middle element $m_{n,{\mathit {dir}}}$ of every subsequence $s_{n,{\mathit {dir}}}$ will be inserted into T as a new node $n'$ . This can be done in parallel for each $m_{n,{\mathit {dir}}}$ since by definition the insertion position of each $m_{n,{\mathit {dir}}}$ is unique. If $s_{n,{\mathit {dir}}}$ contains elements to the left or to the right of $m_{n,{\mathit {dir}}}$ , those will be contained in a new set of subsequences S as $s_{n',{\mathit {left}}}$ or $s_{n',{\mathit {right}}}$ .
4. Now T possibly contains up to two consecutive red nodes at the end of the paths form the root to the leaves, which needs to be repaired. Note that, while repairing, the insertion position of elements $\in S$ have to be updated, if the corresponding nodes are affected by rotations.
  - If two nodes have different nearest black ancestors, they can be repaired in parallel. Since at most four nodes can have the same nearest black ancestor, the nodes at the lowest level can be repaired in a constant number of parallel steps.
  - This step will be applied successively to the black levels above until T is fully repaired.
5. The steps 3 to 5 will be repeated on the new subsequences until S is empty. At this point every element $\in I$ has been inserted. Each application of these steps is called a *stage*. Since the length of the subsequences in S is $\in O(|I|)$ and in every stage the subsequences are being cut in half, the number of stages is $\in O(\log |I|)$ .
  - Since all stages move up the black levels of the tree, they can be parallelised in a pipeline. Once a stage has finished processing one black level, the next stage is able to move up and continue at that level.

- (Initial tree) Initial tree
- (Find insert positions) Find insert positions
- (Stage 1 inserts elements) Stage 1 inserts elements
- (Stage 1 begins to repair nodes) Stage 1 begins to repair nodes
- (Stage 2 inserts elements) Stage 2 inserts elements
- (Stage 2 begins to repair nodes) Stage 2 begins to repair nodes
- (Stage 3 inserts elements) Stage 3 inserts elements
- (Stage 3 begins to repair nodes) Stage 3 begins to repair nodes
- (Stage 3 continues to repair nodes) Stage 3 continues to repair nodes

##### Execution time

Sorting I is not considered in this analysis. Also, $|I|$ is assumed to be smaller than $|T|$ , otherwise it would be more efficient to construct the resulting tree from scratch.

| T(find insert position) | $\in O(\log \|T\|)$ |
|---|---|
| #stages | $\in O(\log \|I\|)$ |
| T(insert) + T(repair) | $\in O(\log \|T\|)$ |
| **T(bulkInsert) with $\|I\|$ ~ #processors** | $\in O(\log \|I\|+2\cdot \log \|T\|)$ $=O(\log \|T\|)$ |

##### Work

| W(find insert positions) | $\in O(\|I\|\log \|T\|)$ |
|---|---|
| #insertions, #repairs | $\in O(\|I\|)$ |
| W(insert) + W(repair) | $\in O(\log \|T\|)$ |
| **W(bulkInsert)** | $\in O(2\cdot \|I\|\log \|T\|)$ $=O(\|I\|\log \|T\|)$ |
