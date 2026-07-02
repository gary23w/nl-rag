---
title: "Control-flow graph"
source: https://en.wikipedia.org/wiki/Control-flow_graph
domain: control-flow-integrity
license: CC-BY-SA-4.0
tags: control flow integrity, return oriented programming defense, shadow stack protection, indirect branch validation, exploit mitigation technique
fetched: 2026-07-02
---

# Control-flow graph

In computer science, a **control-flow graph** (**CFG**) is a representation, using graph notation, of all paths that might be traversed through a function during its execution, or control flow. The control-flow graph was conceived by Frances E. Allen, who noted that Reese T. Prosser used boolean connectivity matrices for flow analysis before.

The CFG is essential to many compiler optimizations and static-analysis tools.

## Definition

A control flow graph is the directed graph of the basic blocks of the function (the nodes of the graph) and the control flow between them (the edges of the graph).

The exact details vary between representations. Typically, a basic block consists of a straight-line sequence of instructions or statements. Only the last instruction or statement in each block can perform control flow, and control flow can only be directed to the first instruction or statement in a block.

In most CFG representations, there are two specially designated blocks: the *entry block*, through which control enters into the function, and the *exit block*, through which all control exits the function (typically by returning). Some representations permit multiple exit blocks, especially if there are different kinds of exit, or permit the exit block to be omitted if it is not reachable .

If there is a control-flow edge from block A to block B, then A is called a *predecessor* of B, and B is called a *successor* of A.

## Examples

As a simple example, consider the following C function definition:

```mw
void print_within_parentheses(const char *p) {
  printf("(");             // 1
  if (p != NULL) {         // 1
    printf("%s", p);       // 2
  }                        // 2
  printf(")");             // 3
}
```

This function has three basic blocks:

- Block 1 is the entry block. It runs from the start of the function until the end of the expression `p != NULL`. It ends with the `if` control flow, either entering block 2 if the condition is true or skipping ahead to block 3 if the condition is false.
- Block 2 is the body of the `if` statement. It ends by unconditionally falling into block 3.
- Block 3 is the exit block. It runs from the end of the `if` statement to the implicit `return` at the end of the function body.

The nested structure of the source program makes it a little hard to see the basic blocks. As an alternative representation that makes the blocks more obvious, we can flatten that structure into a sequence of labeled blocks. To make the control flow explicit, we will require each block to end in either `goto`, an `if`/`else` of `goto`s, or `return` (only in the exit block).

```mw
void print_within_parentheses(const char *p) {
  block1: {
    printf("(");
    if (p != NULL) { goto block2; } else { goto block3; }
  }

  block2: {
    printf("%s", p);
    goto block3;
  }

  block3: {
    printf(")");
    return;
  }
}
```

This is a source-level representation of the CFG. The basic blocks consist of sequences of C statements taken directly from the source program. Only the structured control flow has been eliminated.

Now consider a more complex example which includes a loop:

```mw
void print_as_ordered_tuple(const char * const *p) {
  printf("(");              // 1
  bool first = true;        // 1
  for (; *p != NULL; ++p) { // 2
    if (!first) {           // 3
      printf(",");          // 4
    }                       // 4
    first = false;          // 5
    printf("%s", *p);       // 5
  }                         // 5
  printf(")");              // 6
}
```

This function has six basic blocks, which can be clearly seen in our source-level representation of the CFG:

```mw
void print_as_ordered_tuple(const char *p) {
  bool first;

  block1: {
    printf("(");
    first = true;
    goto block2;
  }

  block2: {
    if (*p != NULL) { goto block3; } else { goto block6; }
  }

  block3: {
    if (!first) { goto block4; } else { goto block5; }
  }

  block4: {
    printf(",");
    goto block5;
  }

  block5: {
    first = false;
    printf("%s", *p);
    ++p;
    goto block2;
  }

  block6: {
    printf(")");
    return;
  }
}
```

This style of statement-level CFG representation is not commonly used, and it is shown here only for illustrative purposes. Not all programs can be easily represented this way, even in C. Notice how the local variable declaration has been raised to the top of function, and its initialization in `block1` has been turned into an assignment. This would cause difficulties for scope-driven features such as shadowing and variable-length arrays. Statements would also need to be significantly rewritten to deal with expression-level control flow, such as is introduced by the `&&`, `||`, and `? :` operators.

Most practical CFG representations use something other than complete source statements as the components of their basic blocks. For example, compiler frameworks such as LLVM use a CFG in which basic blocks consist of abstract static single-assignment instructions as their primary IR. Here is the above function translated into LLVM IR:

```mw
define void @print_as_ordered_tuple(ptr %0) {
block1:
  %p = alloca ptr
  %first = alloca i1
  store ptr %0, ptr %p
  call i32 (ptr, ...) @printf(ptr @"(")
  store i1 1, ptr %first
  br label %block2

block2:
  %1 = load ptr, ptr %p
  %2 = load ptr, ptr %1
  %3 = icmp ne ptr %2, null
  br i1 %1, label %block3, label %block4

block3:
  %4 = load i1, ptr %first
  br i1 %4, label %block4, label %block5

block4:
  call i32 (ptr, ...) @printf(ptr @",")
  br label %block5

block5:
  store i1 0, ptr %first
  %5 = load ptr, ptr %p
  %6 = load ptr, ptr %5
  call i32 (ptr, ...) @printf(ptr @"%s", ptr %6)
  %7 = load ptr, ptr %p
  %8 = getelementptr inbounds ptr, ptr %7, i32 1
  store ptr %8, ptr %p
  br label %block2

block6:
  call i32 (ptr, ...) @printf(ptr @")")
  ret void
}
```

Notice how the block structure is the same in the source-level and the LLVM CFGs. In both representations, the functions have the same basic semantics, performing the same sequence of operations and control flow. Only the representation of the individual operations is different.

## Construction

A very explicit control flow graph can be obtained from a source function by placing each statement into its own basic block. If the statement is not a control-flow statement, a "fall-through" jump to the block for the next statement is added to the block. Unfortunately, this tends to create a large number of unnecessary basic blocks and fall-through jumps, which makes subsequent analysis more cumbersome and expensive. It is usually desirable that successive statements be placed in the same basic block whenever possible. Another way to say this is that, across the entire CFG, every edge A→B should have the property that:

outdegree

(A) > 1 or

indegree

(B) > 1 (or both).

Such a graph can be derived from the one-statement-per-block CFG by performing an edge contraction for every edge that falsifies the predicate above, which is to say, by merging two blocks whenever the source block always jumps to the destination block and the destination block can only be jumped to by the source block. However, this contraction-based algorithm is of little practical importance except as a visualization aid for understanding CFG construction because of the expense of building the initial form. In typical implementations, the CFG is built directly from the program in a way that minimizes unnecessary blocks by construction, such as by scanning the program for necessary boundaries between basic blocks.

## Reachability

Reachability is a graph property useful in optimization. If a block cannot be reached by any path from the entry block, then it cannot possibly be executed, in which case it is called unreachable code. Unreachable code can usually be removed from the control flow graph without any negative consequences.

If the exit block cannot be reached by any path from the entry block, then control flow cannot leave the graph normally. This indicates the presence of either an infinite loop or, in representations that directly support these features, an abnormal exit or termination of the program. The exit block being reachable by some path does not mean that the program will necessarily reach it, and it is impossible to prove that it will be reached in a general graph; see Halting problem.

Optimization can reveal unreachable code and infinite loops that were not apparent in the original program. For example, consider the following LLVM function:

```mw
define void @double_until_odd(ptr %p) {
block1:
  br label %block2

block2:
  %0 = load i32, ptr %p     ; Load the current value from %p
  %1 = mul i32 %0, 2        ; Multiply it by 2
  store i32 %1, ptr %p      ; Store that back into %p
  %2 = and i32 %1, 1        ; Mask off the low bit of the product
  %3 = icmp eq i32 %2, 0    ; Check if that's 0
  br i1 %3, label %block2, label %block3   ; Loop if so

block3:
  ret void
}
```

In this form, the loop in this function is not an infinite loop because there is a path which leaves the loop: if `%3` is false, the program will branch to `block3` and return. However, a numerical analysis can prove that the product of any number and 2 will be even, which means that `%2` is always zero and `%3` can never be false. This function can therefore be optimized into this form:

```mw
define void @double_until_odd(ptr %p) {
block1:
  br label %block2

block2:
  %0 = load i32, ptr %p     ; Load the current value from %p
  %1 = mul i32 %0, 2        ; Multiply it by 2
  store i32 %1, ptr %p      ; Store that back into %p
  br label %block2

block3:                     ; unreachable
  ret void
}
```

There is now an infinite loop in the control flow graph, and the exit block can no longer be reached. Note that this optimization did not change the behavior of the program: it was always true that the loop would never exit. All that has changed is that the control flow graph is more accurately reflecting that truth.

## Dominance relationships

A block M *dominates* a block N if every path from the entry that reaches block N also has to visit block M. The entry block dominates all blocks. M is said to *properly dominate* N if M dominates N and they are different blocks. Furthermore, an individual statement or instruction X is said to properly dominate a statement or instruction Y if the block containing X dominates the block containing Y and, if those are the same block, X strictly precedes Y in the block.

It is said that a block M *immediately dominates* block N if M dominates N, and there is no intervening block P such that M dominates P and P dominates N. In other words, M is the last dominator on all paths from entry to N. Every reachable block has a unique immediate dominator except for the entry block, which has none.

The *dominator tree* is a directed graph representing the dominance relationships in the function. The nodes of the graph are the reachable basic blocks of the function, and there is an edge from block M to block N if M is an immediate dominator of N. Since each non-entry reachable block has a unique immediate dominator, this is a tree rooted at the entry block. The dominator tree can be calculated efficiently using Lengauer–Tarjan's algorithm.

In the reverse direction, block M *post-dominates* block N if every path from N to the exit also has to visit block M. (This is sometimes written without a hyphen: M *postdominates* N.) The exit block post-dominates all blocks. M is said to *properly post-dominate* N if it post-dominates N and they are different blocks. M is an *immediate post-dominator* of N if it post-dominates N and there is no block P such that M post-dominates P and P post-dominates N. Every block from which the exit block is reachable has a unique immediate post-dominator except for the exit block, which has none. This gives rise to a *post-dominator tree*, rooted at the exit block, over the blocks from which the exit block is reachable.

The standard definition of dominance includes unreachable blocks, and the standard definition of post-dominance includes blocks from which the exit block cannot be reached. However, such blocks have unique properties under these relationships: an unreachable block is dominated by all blocks, and a block from which the exit cannot be reached is post-dominated by all blocks. Most analyses relying on dominance or post-dominance will want to ignore them, and they are not included in dominator or post-dominator trees. Some representations require the addition of *impossible edges* to prevent these blocks from existing, at least formally.

## Special edges

A *critical edge* is an edge which is neither the only edge leaving its source block, nor the only edge entering its destination block. Some optimizations must *split* critical edges in order to insert instructions along the edge without affecting other paths through the program. An edge is split by creating a new block that contains only a jump to the destination block, then replacing the original branch destination with the new block.

A *retreating edge* is an edge for which there exists a simple path from the entry block to the source block of the edge (such as might be found by a depth-first traversal of the graph) which includes the destination block. A retreating edge indicates the presence of a cycle in the control flow graph. A retreating edge is called a *back edge* if the destination block is present on all possible paths to the source block, which is to say, if the destination block dominates the source block.

An *abnormal edge* is an edge whose destination is unknown. Exception handling constructs can produce them. These edges tend to inhibit optimization.

An *impossible edge* (also known as a *fake edge*) is an edge which cannot actually be traversed during execution and is only added to the graph to preserve some useful property. For example, some representations require the addition of impossible edges to ensure that the exit block is always reachable and post-dominates all blocks.

## Strongly-connected components

A strongly-connected component (SCC) of a control flow graph is a set of basic blocks which are all reachable from one another. The blocks that are part of a loop are always part of the same strongly-connected component. A block that is not part of a cycle is always in a strongly-connected component by itself. In particular, the entry and exit blocks are always their own strongly-connected components.

The strongly-connected components of a CFG form a directed acyclic graph called the *SCC tree*, where component A has an edge to component B if any block in A has an edge to any block in B. The SCC tree is isomorphic to the control flow graph if there are no cycles in the CFG; if there is a cycle, the SCC tree essentially collapses all blocks and edges in it into a single node. This can be useful for analyses that wish to treat all of the blocks in a cycle as equivalent. For example, when trying to find an object lifetime that covers a set of use-points as narrowly as possible, if one of those use-points is within a cyclic SCC, the lifetime must fully cover every block in that component.

## Loop management

A *loop header* (sometimes called the *entry point* of the loop) is a dominator that is the target of a loop-forming back edge. The loop header dominates all blocks in the loop body. A block may be a loop header for more than one loop. A loop may have multiple entry points, in which case it has no "loop header".

Suppose block M is a dominator with several incoming edges, some of them being back edges (so M is a loop header). It is advantageous to several optimization passes to break M up into two blocks Mpre and Mloop. The contents of M and back edges are moved to Mloop, the rest of the edges are moved to point into Mpre, and a new edge from Mpre to Mloop is inserted (so that Mpre is the immediate dominator of Mloop). In the beginning, Mpre would be empty, but passes like loop-invariant code motion could populate it. Mpre is called the *loop pre-header*, and Mloop would be the loop header.

## Reducibility

A control flow graph is called *reducible* if all its retreating edges are back edges. The other edges in such a CFG are called *forward edges*. The forward edges form a directed acyclic graph, and the back edges always lead to a basic block that control flow has already passed through. Reducible CFGs generally have stronger static properties and can be more easily analyzed and optimized. For example, many loop optimizations are designed to work only on reducible CFGs.

Structured programming languages are often designed such that all CFGs they produce are reducible, and common structured programming statements such as IF, FOR, WHILE, BREAK, and CONTINUE reliably produce reducible graphs. To directly produce an irreducible graph, statements such as GOTO are needed that can jump to an arbitrary point in the program, although not all uses of GOTO produce irreducible CFGs. Irreducible CFGs can also be produced by some compiler optimizations, such as jump threading. Irreducible CFGs can be converted to reducible CFGs, but this often requires duplicating code or introducing new variables to the program.

## Loop connectedness

The loop connectedness of a CFG is defined with respect to a given depth-first search tree (DFST) of the CFG. This DFST should be rooted at the start node and cover every node of the CFG.

In this context, edges in the CFG which run from a node to one of its DFST ancestors (including itself) are called back edges. This does not necessarily coincide with the usual definition of a back edge because a DFST ancestor need not dominate the source node of the edge.

The loop connectedness is the largest number of back edges found in any cycle-free path of the CFG. In a reducible CFG, the loop connectedness is independent of the DFST chosen.

Loop connectedness has been used to reason about the time complexity of data-flow analysis.

## Inter-procedural control-flow graph

While control-flow graphs represent the control flow of a single procedure, inter-procedural control-flow graphs represent the control flow of whole programs.
