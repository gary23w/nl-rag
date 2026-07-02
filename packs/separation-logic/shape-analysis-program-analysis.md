---
title: "Shape analysis (program analysis)"
source: https://en.wikipedia.org/wiki/Shape_analysis_(program_analysis)
domain: separation-logic
license: CC-BY-SA-4.0
tags: separation logic, separating conjunction, heap assertion, frame rule
fetched: 2026-07-02
---

# Shape analysis (program analysis)

In program analysis, **shape analysis** is a static code analysis technique that discovers and verifies properties of linked, dynamically allocated data structures in (usually imperative) computer programs. It is typically used at compile time to find software bugs or to verify high-level correctness properties of programs. In Java programs, it can be used to ensure that a sort method correctly sorts a list. For C programs, it might look for places where a block of memory is not properly freed.

## Applications

Shape analysis has been applied to a variety of problems:

- Memory safety: finding memory leaks, dereferences of dangling pointers, and discovering cases where a block of memory is freed more than once.
- Finding array out-of-bounds errors
- Checking type-state properties (for example, ensuring that a file is `open()` before it is `read()`)
- Ensuring that a method to reverse a linked list does not introduce cycles into the list

## Example

Shape analysis is a form of pointer analysis, although it is more precise than typical pointer analysis. Pointer analysis attempts to determine the set of objects to which a pointer can point (called the points-to set of the pointer). Unfortunately, these analysis are necessarily approximate (since a perfectly precise static analysis could solve the halting problem). Shape analysis can determine smaller (more precise) points-to sets.

Consider the following simple C++ program.

```mw
Item *items[10];

for (int i = 0; i < 10; ++i) {
    items[i] = new Item(...); // line [1]
}

process_items(items); // line [2]

for (int i = 0; i < 10; ++i) {
    delete items[i]; // line [3]
}
```

This program builds an array of objects, processes them in some arbitrary way, and then deletes them. Assuming that the `process_items` function is free of errors, it is clear that the program is safe: it never references freed memory, and it deletes all the objects that it has constructed.

Unfortunately, most pointer analyses have difficulty analyzing this program precisely. In order to determine points-to sets, a pointer analysis must be able to *name* a program's objects. In general, programs can allocate an unbounded number of objects; but in order to terminate, a pointer analysis can only use a finite set of names. A typical approximation is to give all the objects allocated on a given line of the program the same name. In the example above, all the objects constructed at line [1] would have the same name. Therefore, when the `delete` statement is analyzed for the first time, the analysis determines that one of the objects named [1] is being deleted. The second time the statement is analyzed (since it is in a loop) the analysis warns of a possible error: since it is unable to distinguish the objects in the array, it may be that the second `delete` is deleting the same object as the first `delete`. This warning is spurious, and the goal of shape analysis is to avoid such warnings.

## Summarization and materialization

Shape analysis overcomes the problems of pointer analysis by using a more flexible naming system for objects. Rather than giving an object the same name throughout a program, objects can change names depending on the program's actions. Sometimes, several distinct objects with different names may be *summarized,* or merged, so that they have the same name. Then, when a summarized object is about to be used by the program, it can be *materialized*—that is, the summarized object is split into two objects with distinct names, one representing a single object and the other representing the remaining summarized objects. The basic heuristic of shape analysis is that objects that are being used by the program are represented using unique materialized objects, while objects not in use are summarized.

The array of objects in the example above is summarized in separate ways at lines [1], [2], and [3]. At line [1], the array has been only partly constructed. The array elements 0..i-1 contain constructed objects. The array element i is about to be constructed, and the following elements are uninitialized. Shape analysis can approximate this situation using a summary for the first set of elements, a materialized memory location for element i, and a summary for the remaining uninitialized locations, as follows:

| 0 .. i−1 | i | i+1 .. 9 |
|---|---|---|
| pointer to constructed object (summary) | uninitialized | uninitialized (summary) |

After the loop terminates, at line [2], there is no need to keep anything materialized. The shape analysis determines at this point that all the array elements have been initialized:

| 0 .. 9 |
|---|
| pointer to constructed object (summary) |

At line [3], however, the array element `i` is in use again. Therefore, the analysis splits the array into three segments as in line [1]. This time, though, the first segment before `i` has been deleted, and the remaining elements are still valid (assuming the `delete` statement hasn't executed yet).

| 0 .. i−1 | i | i+1 .. 9 |
|---|---|---|
| free (summary) | pointer to constructed object | pointer to constructed object (summary) |

Notice that in this case, the analysis recognizes that the pointer at index `i` has not been deleted yet. Therefore, it doesn't warn of a double deletion.
