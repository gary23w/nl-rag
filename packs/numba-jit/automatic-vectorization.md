---
title: "Automatic vectorization"
source: https://en.wikipedia.org/wiki/Automatic_vectorization
domain: numba-jit
license: BSD-3-Clause
tags: numba compiler, just-in-time compilation, automatic vectorization, llvm backend
fetched: 2026-07-02
---

# Automatic vectorization

**Automatic vectorization**, in parallel computing, is a special case of automatic parallelization, where a computer program is converted from a scalar implementation, which processes a single pair of operands at a time, to a vector implementation, which processes one operation on multiple pairs of operands at once. For example, modern conventional computers, including specialized supercomputers, typically have vector operations that simultaneously perform operations such as the following four additions (via SIMD or SPMD hardware):

${\begin{aligned}c_{1}&=a_{1}+b_{1}\\c_{2}&=a_{2}+b_{2}\\c_{3}&=a_{3}+b_{3}\\c_{4}&=a_{4}+b_{4}\end{aligned}}$

However, in most programming languages one typically writes loops that sequentially perform additions of many numbers. Here is an example of such a loop, written in C:

```mw
for (i = 0; i < n; i++)
    c[i] = a[i] + b[i];
```

A vectorizing compiler transforms such loops into sequences of vector operations. These vector operations perform additions on blocks of elements from the arrays `a`, `b` and `c`. Automatic vectorization is a major research topic in computer science.

## Background

Early computers usually had one logic unit, which executed one instruction on one pair of operands at a time. Computer languages and programs therefore were designed to execute in sequence. Modern computers, though, can do many things at once. So, many optimizing compilers perform automatic vectorization, where parts of sequential programs are transformed into parallel operations.

**Loop vectorization** transforms procedural loops by assigning a processing unit to each pair of operands. Programs spend most of their time within such loops. Therefore, vectorization can significantly accelerate them, especially over large data sets. Loop vectorization is implemented in Intel's MMX, SSE, and AVX, in Power ISA's AltiVec, in ARM's NEON, SVE and SVE2, and in RISC-V's Vector Extension instruction sets.

Many constraints prevent or hinder vectorization. Sometimes vectorization can slow down execution, for example because of pipeline synchronization or data-movement timing. Loop dependence analysis identifies loops that can be vectorized, relying on the data dependence of the instructions inside loops.

## Guarantees

Automatic vectorization, like any loop optimization or other compile-time optimization, must exactly preserve program behavior.

### Data dependencies

All dependencies must be respected during execution to prevent incorrect results.

In general, loop invariant dependencies and lexically forward dependencies can be easily vectorized, and lexically backward dependencies can be transformed into lexically forward dependencies. However, these transformations must be done safely, in order to ensure that the dependence between **all statements** remain true to the original.

Cyclic dependencies must be processed independently of the vectorized instructions.

Sometimes the compiler may over-cautiously assume a dependency. Some compilers offer a directive named *ivdep* to instruct the compiler to ignore dependencies. Incorrectly applying such a directive would cause incorrect results.

### Data precision

Integer precision (bit-size) must be kept during vector instruction execution. The correct vector instruction must be chosen based on the size and behavior of the internal integers. Also, with mixed integer types, extra care must be taken to promote/demote them correctly without losing precision. Special care must be taken with sign extension (because multiple integers are packed inside the same register) and during shift operations, or operations with carry bits that would otherwise be taken into account.

#### Floating-point

By default floating-point semantics from IEEE-754 are kept, which often prevents vectorization altogether. Consider the following trivial loop that computes a sum over an array:

```mw
float sum(float *A, int n) {
  float sum = 0;
  for (int i = 0; i < n; ++i)
    sum += A[i];
  return sum;
}
```

Because floating-point operations are not associative (changing the order of summation changes the result), a compiler cannot be allowed to vectorize the loop. Only when the compiler is explicitly allowed to *reassociate* (re-order the operations as if they are associative), can it compile to something resembling:

```mw
float sum(float *A, int n) {
  float4 sum4 = {0}, *A4 = A;
  int n4 = n / 4;
  for (int i = 0; i < n4; ++i) {
    sum4 += A4[i];
  }

  float sum = sum4[0] + sum4[1] + sum4[2] + sum4[3];
  for (int i = n/4; i < n; ++i) {
    sum += A[i];
  }

  return sum;
}
```

In this case the results will vary slightly from the original, but the asymptotic round-off error is similar. This is an example of *reduction*.

Big variations, even ignoring IEEE-754, usually signify programmer error. A common cause is that full reassociation can defeat compensated summation algorithms. More restricted commands such as the *reduction* clause from OpenMP can provide more targeted setting.

## Theory

To vectorize a program, the compiler's optimizer must first understand the dependencies between statements and re-align them, if necessary. Once the dependencies are mapped, the optimizer must properly arrange the implementing instructions changing appropriate candidates to vector instructions, which operate on multiple data items.

### Building the dependency graph

The first step is to build the dependency graph, identifying which statements depend on which other statements. This involves examining each statement and identifying every data item that the statement accesses, mapping array access modifiers to functions and checking every access' dependency to all others in all statements. Alias analysis can be used to certify that the different variables access (or intersect) the same region in memory.

The dependency graph contains all local dependencies with distance not greater than the vector size. So, if the vector register is 128 bits, and the array type is 32 bits, the vector size is 128/32 = 4. All other non-cyclic dependencies should not invalidate vectorization, since there won't be any concurrent access in the same vector instruction.

Suppose the vector size is the same as 4 ints:

```mw
for (i = 0; i < 128; i++) {
    a[i] = a[i-16]; // 16 > 4, safe to ignore
    a[i] = a[i-1]; // 1 < 4, stays on dependency graph
}
```

### Clustering

Using the graph, the optimizer can then cluster the strongly connected components (SCC) and separate vectorizable statements from the rest.

For example, consider a program fragment containing three statement groups inside a loop: (SCC1+SCC2), SCC3 and SCC4, in that order, in which only the second group (SCC3) can be vectorized. The final program will then contain three loops, one for each group, with only the middle one vectorized. The optimizer cannot join the first with the last without violating statement execution order, which would invalidate the necessary guarantees.

### Detecting idioms

Some non-obvious dependencies can be further optimized based on specific idioms.

For instance, the following self-data-dependencies can be vectorized because the value of the right-hand values (RHS) are fetched and then stored on the left-hand value, so there is no way the data will change within the assignment.

```mw
a[i] = a[i] + a[i+1];
```

Self-dependence by scalars can be vectorized by variable elimination.

## General framework

The general framework for loop vectorization is split into four stages:

- **Prelude**: Where the loop-independent variables are prepared to be used inside the loop. This normally involves moving them to vector registers with specific patterns that will be used in vector instructions. This is also the place to insert the run-time dependence check. If the check decides vectorization is not possible, branch to **Cleanup**.
- **Loop(s)**: All vectorized (or not) loops, separated by SCCs clusters in order of appearance in the original code.
- **Postlude**: Return all loop-independent variables, inductions and reductions.
- **Cleanup**: Implement plain (non-vectorized) loops for iterations at the end of a loop that are not a multiple of the vector size or for when run-time checks prohibit vector processing.

## Run-time vs. compile-time

Some vectorizations cannot be fully checked at compile time. For example, library functions can defeat optimization if the data they process is supplied by the caller. Even in these cases, run-time optimization can still vectorize loops on-the-fly.

This run-time check is made in the **prelude** stage and directs the flow to vectorized instructions if possible, otherwise reverts to standard processing, depending on the variables that are being passed on the registers or scalar variables.

The following code can easily be vectorized at compile time, as it doesn't have any dependence on external parameters. Also, the language guarantees that neither will occupy the same region in memory as any other variable, as they are local variables and live only in the execution stack.

```mw
int a[128];
int b[128];
// initialize b

for (i = 0; i<128; i++)
    a[i] = b[i] + 5;
```

On the other hand, the code below has no information on memory positions, because the references are pointers and the memory they point to may overlap.

```mw
void compute(int *a, int *b)
{
    int i;
    for (i = 0; i < 128; i++, a++, b++)
        *a = *b + 5;
}
```

A quick run-time check on the address of both *a* and *b*, plus the loop iteration space (128) is enough to tell if the arrays overlap or not, thus revealing any dependencies. (Note that from C99, qualifying the parameters with the restrict keyword—here: `int *restrict a, int *restrict b`)—tells the compiler that the memory ranges pointed to by *a* and *b* do not overlap, leading to the same outcome as the example above.)

There exist some tools to dynamically analyze existing applications to assess the inherent latent potential for SIMD parallelism, exploitable through further compiler advances and/or via manual code changes.

## Techniques

An example would be a program to multiply two vectors of numeric data. A scalar approach would be something like:

```mw
for (i = 0; i < 1024; i++)
    c[i] = a[i] * b[i];
```

This could be vectorized to look something like:

```mw
for (i = 0; i < 1024; i += 4)
    c[i:i+3] = a[i:i+3] * b[i:i+3];
```

Here, c[i:i+3] represents the four array elements from c[i] to c[i+3] and the vector processor can perform four operations for a single vector instruction. Since the four vector operations complete in roughly the same time as one scalar instruction, the vector approach can run up to four times faster than the original code.

There are two distinct compiler approaches: one based on the conventional vectorization technique and the other based on loop unrolling.

### Loop-level automatic vectorization

This technique, used for conventional vector machines, tries to find and exploit SIMD parallelism at the loop level. It consists of two major steps as follows.

1. Find an innermost loop that can be vectorized
2. Transform the loop and generate vector codes

In the first step, the compiler looks for obstacles that can prevent vectorization. A major obstacle for vectorization is true data dependency shorter than the vector length. Other obstacles include function calls and short iteration counts.

Once the loop is determined to be vectorizable, the loop is stripmined by the vector length and each scalar instruction within the loop body is replaced with the corresponding vector instruction. Below, the component transformations for this step are shown using the above example.

- After stripmining

```mw
for (i = 0; i < 1024; i += 4)
    for (j = 0; j < 4; j++)
        c[i+j] = a[i+j] * b[i+j];
```

- After loop distribution using temporary arrays

```mw
for (i = 0; i < 1024; i += 4)
{
    for (j = 0; j < 4; j++) tA[j] = A[i+j];
    for (j = 0; j < 4; j++) tB[j] = B[i+j];
    for (j = 0; j < 4; j++) tC[j] = tA[j] * tB[j];
    for (j = 0; j < 4; j++) C[i+j] = tC[j];
}
```

- After replacing with vector codes

```mw
for (i = 0; i < 1024; i += 4)
{
    vA = vec_ld(&A[i]);
    vB = vec_ld(&B[i]);
    vC = vec_mul(vA, vB);
    vec_st(vC, &C[i]);
}
```

### Basic block level automatic vectorization

This relatively new technique specifically targets modern SIMD architectures with short vector lengths. Although loops can be unrolled to increase the amount of SIMD parallelism in basic blocks, this technique exploits SIMD parallelism within basic blocks rather than loops. The two major steps are as follows.

1. The innermost loop is unrolled by a factor of the vector length to form a large loop body.
2. Isomorphic scalar instructions (that perform the same operation) are packed into a vector instruction if dependencies do not prevent doing so.

To show step-by-step transformations for this approach, the same example is used again.

- After loop unrolling (by the vector length, assumed to be 4 in this case)

```mw
for (i = 0; i < 1024; i += 4)
{
    sA0 = ld(&A[i+0]);
    sB0 = ld(&B[i+0]);
    sC0 = sA0 * sB0;
    st(sC0, &C[i+0]);
          ...
    sA3 = ld(&A[i+3]);
    sB3 = ld(&B[i+3]);
    sC3 = sA3 * sB3;
    st(sC3, &C[i+3]);
}
```

- After packing

```mw
for (i = 0; i < 1024; i += 4)
{
    (sA0, sA1, sA2, sA3) = ld(&A[i+0:i+3]);
    (sB0, sB1, sB2, sB3) = ld(&B[i+0:i+3]);
    (sC0, sC1, sC2, sC3) = (sA0, sA1, sA2, sA3) * (sB0, sB1, sB2, sB3);
    st((sC0, sC1, sC2, sC3), &C[i+0:i+3]);
}
```

- After code generation

```mw
for (i = 0; i < 1024; i += 4)
{
    vA = vec_ld(&A[i]);
    vB = vec_ld(&B[i]);
    vC = vec_mul(vA, vB);
    vec_st(vC, &C[i]);
}
```

Here, sA1, sB1, ... represent scalar variables and vA, vB, and vC represent vector variables.

Most automatically vectorizing commercial compilers use the conventional loop-level approach except the IBM XL Compiler, which uses both.

### In the presence of control flow

The presence of if-statements in the loop body requires the execution of instructions in all control paths to merge the multiple values of a variable. One general approach is to go through a sequence of code transformations: predication → vectorization(using one of the above methods) → remove vector predicates → remove scalar predicates. If the following code is used as an example to show these transformations;

```mw
for (i = 0; i < 1024; i++)
    if (A[i] > 0)
        C[i] = B[i];
    else
        D[i] = D[i-1];
```

- After predication

```mw
for (i = 0; i < 1024; i++)
{
    P = A[i] > 0;
    NP = !P;
    C[i] = B[i];     (P)
    D[i] = D[i-1];   (NP)
}
```

where (P) denotes a predicate guarding the statement.

- After vectorization

```mw
for (i = 0; i < 1024; i += 4)
{
    vP  = A[i:i+3] > (0, 0, 0, 0);
    vNP = vec_not(vP);
    C[i:i+3] = B[i:i+3];     (vP)
    (NP1, NP2, NP3, NP4) = vNP;
    D[i+3] = D[i+2];         (NP4)
    D[i+2] = D[i+1];         (NP3)
    D[i+1] = D[i];           (NP2)
    D[i]   = D[i-1];         (NP1)
}
```

- After removing vector predicates

```mw
for (i = 0; i < 1024; i += 4)
{
    vP  = A[i:i+3] > (0, 0, 0, 0);
    vNP = vec_not(vP);
    C[i:i+3] = vec_sel(C[i:i+3], B[i:i+3], vP);
    (NP1, NP2, NP3, NP4) = vNP;
    D[i+3] = D[i+2];         (NP4)
    D[i+2] = D[i+1];         (NP3)
    D[i+1] = D[i];           (NP2)
    D[i]   = D[i-1];         (NP1)
}
```

- After removing scalar predicates

```mw
for (i = 0; i < 1024; i += 4)
{
    vP  = A[i:i+3] > (0, 0, 0, 0);
    vNP = vec_not(vP);
    C[i:i+3] = vec_sel(C[i:i+3], B[i:i+3], vP);
    (NP1, NP2, NP3, NP4) = vNP;
    if (NP4) D[i+3] = D[i+2];
    if (NP3) D[i+2] = D[i+1];
    if (NP2) D[i+1] = D[i];
    if (NP1) D[i]   = D[i-1];
}
```

### Reducing vectorization overhead in the presence of control flow

Having to execute the instructions in all control paths in vector code has been one of the major factors that slow down the vector code with respect to the scalar baseline. The more complex the control flow becomes and the more instructions are bypassed in the scalar code, the larger the vectorization overhead becomes. To reduce this vectorization overhead, vector branches can be inserted to bypass vector instructions similar to the way scalar branches bypass scalar instructions. Below, AltiVec predicates are used to show how this can be achieved.

- Scalar baseline (original code)

```mw
for (i = 0; i < 1024; i++)
{
    if (A[i] > 0)
    {
        C[i] = B[i];
        if (B[i] < 0)
            D[i] = E[i];
    }
}
```

- After vectorization in the presence of control flow

```mw
for (i = 0; i < 1024; i += 4)
{
    vPA = A[i:i+3] > (0, 0, 0, 0);
    C[i:i+3] = vec_sel(C[i:i+3], B[i:i+3], vPA);
    vT = B[i:i+3] < (0,0,0,0);
    vPB = vec_sel((0, 0, 0, 0), vT, vPA);
    D[i:i+3] = vec_sel(D[i:i+3], E[i:i+3], vPB);
}
```

- After inserting vector branches

```mw
for (i = 0; i < 1024; i += 4)
{
    if (vec_any_gt(A[i:i+3], (0, 0, 0, 0)))
    {
        vPA = A[i:i+3] > (0,0,0,0);
        C[i:i+3] = vec_sel(C[i:i+3], B[i:i+3], vPA);
        vT = B[i:i+3] < (0, 0, 0, 0);
        vPB = vec_sel((0, 0, 0, 0), vT, vPA);
        if (vec_any_ne(vPB, (0, 0, 0, 0)))
            D[i:i+3] = vec_sel(D[i:i+3], E[i:i+3], vPB);
    }
}
```

There are two things to note in the final code with vector branches; First, the predicate defining instruction for vPA is also included within the body of the outer vector branch by using vec_any_gt. Second, the profitability of the inner vector branch for vPB depends on the conditional probability of vPB having false values in all fields given vPA has false values in all fields.

Consider an example where the outer branch in the scalar baseline is always taken, bypassing most instructions in the loop body. The intermediate case above, without vector branches, executes all vector instructions. The final code, with vector branches, executes both the comparison and the branch in vector mode, potentially gaining performance over the scalar baseline.

## Manual vectorization

In most C and C++ compilers, it is possible to use intrinsic functions to manually use SIMD, at the expense of programmer effort, maintainability, and portability. Some languages (e.g. GNU C, C++ `std::experimental::simd`, Rust `std::simd`) include vector data types that compile to appropriate SIMD instructions, improving portability and reducing the effort required.

Another approach is SPMD: write a program that looks as if it operates only one element on the time, then have a compiler widen it to match the SIMD vector width. This is the approach used by graphics shaders and more recently adopted by CPU-oriented tools such as Intel IPSC. Unlike to auto-vectorization which may fail and fall back to scalar code (e.g. when there is a call to an external function in a loop), SPMD is guaranteed to result in vector code where applicable, much like manual use of intrinsics or vector datatypes.
