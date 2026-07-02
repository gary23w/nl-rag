---
title: "Jacobi eigenvalue algorithm"
source: https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm
domain: eigenvalue-algorithms
license: CC-BY-SA-4.0
tags: eigenvalue algorithm, power iteration, rayleigh quotient iteration, jacobi eigenvalue algorithm
fetched: 2026-07-02
---

# Jacobi eigenvalue algorithm

In numerical linear algebra, the **Jacobi eigenvalue algorithm** is an iterative method for the calculation of the eigenvalues and eigenvectors of a real symmetric matrix (a process known as diagonalization). It is named after Carl Gustav Jacob Jacobi, who first proposed the method in 1846, but it only became widely used in the 1950s with the advent of computers.

This algorithm is inherently a dense matrix algorithm: it draws little or no advantage from being applied to a sparse matrix, and it will destroy sparseness by creating fill-in. Similarly, it will not preserve structures such as being banded of the matrix on which it operates.

## Description

Let S be a symmetric matrix, and $G=G(i,j,\theta )$ be a Givens rotation matrix. Then:

$S'=G^{\top }SG\,$

is symmetric and similar to S .

Furthermore, $S^{\prime }$ has entries:

${\begin{aligned}S'_{ii}&=c^{2}\,S_{ii}-2\,sc\,S_{ij}+s^{2}\,S_{jj}\\S'_{jj}&=s^{2}\,S_{ii}+2sc\,S_{ij}+c^{2}\,S_{jj}\\S'_{ij}&=S'_{ji}=(c^{2}-s^{2})\,S_{ij}+sc\,(S_{ii}-S_{jj})\\S'_{ik}&=S'_{ki}=c\,S_{ik}-s\,S_{jk}&k\neq i,j\\S'_{jk}&=S'_{kj}=s\,S_{ik}+c\,S_{jk}&k\neq i,j\\S'_{kl}&=S_{kl}&k,l\neq i,j\end{aligned}}$

where $s=\sin(\theta )$ and $c=\cos(\theta )$ .

Since G is orthogonal, S and $S^{\prime }$ have the same Frobenius norm $||\cdot ||_{F}$ (the square-root sum of squares of all components), however we can choose $\theta$ such that $S_{ij}^{\prime }=0$ , in which case $S^{\prime }$ has a larger sum of squares on the diagonal:

$S'_{ij}=\cos(2\theta )S_{ij}+{\tfrac {1}{2}}\sin(2\theta )(S_{ii}-S_{jj})$

Set this equal to 0, and rearrange:

$\tan(2\theta )={\frac {2S_{ij}}{S_{jj}-S_{ii}}}$

if $S_{jj}=S_{ii}$

$\theta ={\frac {\pi }{4}}$

In order to optimize this effect, *S**ij* should be the off-diagonal element with the largest absolute value, called the *pivot*.

The Jacobi eigenvalue method repeatedly performs rotations until the matrix becomes almost diagonal. Then the elements in the diagonal are approximations of the (real) eigenvalues of *S*.

## Convergence

If $p=S_{kl}$ is a pivot element, then by definition $|S_{ij}|\leq |p|$ for $1\leq i,j\leq n,i\neq j$ . Let $\Gamma (S)^{2}$ denote the sum of squares of all off-diagonal entries of S . Since S has exactly $2N:=n(n-1)$ off-diagonal elements, we have $p^{2}\leq \Gamma (S)^{2}\leq 2Np^{2}$ or $2p^{2}\geq \Gamma (S)^{2}/N$ . Now $\Gamma (S^{J})^{2}=\Gamma (S)^{2}-2p^{2}$ . This implies $\Gamma (S^{J})^{2}\leq (1-1/N)\Gamma (S)^{2}$ or $\Gamma (S^{J})\leq (1-1/N)^{1/2}\Gamma (S)$ ; that is, the sequence of Jacobi rotations converges at least linearly by a factor $(1-1/N)^{1/2}$ to a diagonal matrix.

A number of N Jacobi rotations is called a sweep; let $S^{\sigma }$ denote the result. The previous estimate yields

$\Gamma (S^{\sigma })\leq \left(1-{\frac {1}{N}}\right)^{N/2}\Gamma (S)$

;

that is, the sequence of sweeps converges at least linearly with a factor ≈ $e^{1/2}$ .

However the following result of Schönhage yields locally quadratic convergence. To this end let *S* have *m* distinct eigenvalues $\lambda _{1},...,\lambda _{m}$ with multiplicities $\nu _{1},...,\nu _{m}$ and let *d* > 0 be the smallest distance of two different eigenvalues. Let us call a number of

$N_{S}:={\frac {n(n-1)}{2}}-\sum _{\mu =1}^{m}{\frac {1}{2}}\nu _{\mu }(\nu _{\mu }-1)\leq N$

Jacobi rotations a Schönhage-sweep. If $S^{s}$ denotes the result then

$\Gamma (S^{s})\leq {\sqrt {{\frac {n}{2}}-1}}\left({\frac {\gamma ^{2}}{d-2\gamma }}\right),\quad \gamma :=\Gamma (S)$

.

Thus convergence becomes quadratic as soon as $\Gamma (S)<{\frac {d}{2+{\sqrt {{\frac {n}{2}}-1}}}}$

## Cost

Each Givens rotation can be done in $O(n)$ steps when the pivot element *p* is known. However the search for *p* requires inspection of all *N* ≈ ⁠1/2⁠ *n*2 off-diagonal elements, which means this search dominates the overall complexity and pushes the computational complexity of a sweep in the classical Jacobi algorithm to $O(n^{4})$ . Competing algorithms attain $O(n^{3})$ complexity for a full diagonalisation.

### Caching row maximums

We can reduce the complexity of finding the pivot element from O(*N*) to O(*n*) if we introduce an additional index array $m_{1},\,\dots \,,\,m_{n-1}$ with the property that $m_{i}$ is the index of the largest element in row *i*, (*i* = 1, ..., *n* − 1) of the current *S*. Then the indices of the pivot (*k*, *l*) must be one of the pairs $(i,m_{i})$ . Also the updating of the index array can be done in O(*n*) average-case complexity: First, the maximum entry in the updated rows *k* and *l* can be found in O(*n*) steps. In the other rows *i*, only the entries in columns *k* and *l* change. Looping over these rows, if $m_{i}$ is neither *k* nor *l*, it suffices to compare the old maximum at $m_{i}$ to the new entries and update $m_{i}$ if necessary. If $m_{i}$ should be equal to *k* or *l* and the corresponding entry decreased during the update, the maximum over row *i* has to be found from scratch in O(*n*) complexity. However, this will happen on average only once per rotation. Thus, each rotation has O(*n*) and one sweep O(*n*3) average-case complexity, which is equivalent to one matrix multiplication. Additionally the $m_{i}$ must be initialized before the process starts, which can be done in *n*2 steps.

Typically the Jacobi method converges within numerical precision after a small number of sweeps. Note that multiple eigenvalues reduce the number of iterations since $N_{S}<N$ .

### Cyclic and parallel Jacobi

An alternative approach is to forego the search entirely, and simply have each sweep pivot every off-diagonal element once, in some predetermined order. It has been shown that this *cyclic Jacobi* attains quadratic convergence, just like the classical Jacobi.

The opportunity for parallelisation that is particular to Jacobi is based on combining cyclic Jacobi with the observation that Givens rotations for disjoint sets of indices commute, so that several can be applied in parallel. Concretely, if $G_{1}$ pivots between indices $i_{1},j_{1}$ and $G_{2}$ pivots between indices $i_{2},j_{2}$ , then from $\{i_{1},j_{1}\}\cap \{i_{2},j_{2}\}=\varnothing$ follows $G_{1}G_{2}=G_{2}G_{1}$ because in computing $G_{1}G_{2}A$ or $G_{2}G_{1}A$ the $G_{1}$ rotation only needs to access rows $i_{1},j_{1}$ and the $G_{2}$ rotation only needs to access rows $i_{2},j_{2}$ . Two processors can perform both rotations in parallel, because no matrix element is accessed for both.

Partitioning the set of index pairs of a sweep into classes that are pairwise disjoint is equivalent to partitioning the edge set of a complete graph into matchings, which is the same thing as edge colouring it; each colour class then becomes a round within the sweep. The minimal number of rounds is the chromatic index of the complete graph, and equals n for odd n but $n-1$ for even n . A simple rule for odd n is to handle the pairs $\{i_{1},j_{1}\}$ and $\{i_{2},j_{2}\}$ in the same round if $i_{1}+j_{1}\equiv i_{2}+j_{2}\textstyle {\pmod {n}}$ . For even n one may create $n-1$ rounds $k=0,1,\dotsc ,n-2$ where a pair $\{i,j\}$ for $1\leqslant i<j\leqslant n-1$ goes into round $(i+j){\bmod {(}}n-1)$ and additionally a pair $\{i,n\}$ for $1\leqslant i\leqslant n-1$ goes into round $2i{\bmod {(}}n-1)$ . This brings the time complexity of a sweep down from $O(n^{3})$ to $O(n^{2})$ , if $n/2$ processors are available.

A round would consist of each processor first calculating $(c,s)$ for its rotation, and then applying the rotation from the left (rotating between rows). Next, the processors synchronise before applying the transpose rotation from the right (rotating between columns), and finally synchronising again. A matrix element may be accessed by two processors during a round, but not by both during the same half of this round.

Further parallelisation is possible by dividing the work for a single rotation between several processors, but that might be getting too fine-grained to be practical.

## Algorithm

The following algorithm is a description of the Jacobi method in math-like notation. It calculates a vector *e* which contains the eigenvalues and a matrix *E* which contains the corresponding eigenvectors; that is, $e_{i}$ is an eigenvalue and the column $E_{i}$ an orthonormal eigenvector for $e_{i}$ , *i* = 1, ..., *n*.

```
procedure jacobi(S ∈ Rn×n; out e ∈ Rn; out E ∈ Rn×n)
  var
    i, k, l, m, state ∈ N
    s, c, t, p, y, d, r ∈ R
    ind ∈ Nn
    changed ∈ Ln

  function maxind(k ∈ N) ∈ N ! index of largest off-diagonal element in row k
    m := k+1
    for i := k+2 to n do
      if │Ski│ > │Skm│ then m := i endif
    endfor
    return m
  endfunc

  procedure update(k ∈ N; t ∈ R) ! update ek and its status
    y := ek; ek := y+t
    if changedk and (y=ek) then changedk := false; state := state−1
    elsif (not changedk) and (y≠ek) then changedk := true; state := state+1
    endif
  endproc

  procedure rotate(k,l,i,j ∈ N) ! perform rotation of Sij, Skl
    ┌   ┐    ┌     ┐┌   ┐
    │Skl│    │c  −s││Skl│
    │   │ := │     ││   │
    │Sij│    │s   c││Sij│
    └   ┘    └     ┘└   ┘
  endproc

  ! init e, E, and arrays ind, changed
  E := I; state := n
  for k := 1 to n do indk := maxind(k); ek := Skk; changedk := true endfor
  while state≠0 do ! next rotation
    m := 1 ! find index (k,l) of pivot p
    for k := 2 to n−1 do
      if │Sk indk│ > │Sm indm│ then m := k endif
    endfor
    k := m; l := indm; p := Skl
    ! calculate c = cos φ, s = sin φ
    y := (el−ek)/2; d := │y│+√(p2+y2)
    r := √(p2+d2); c := d/r; s := p/r; t := p2/d
    if y<0 then s := −s; t := −t endif
    Skl := 0.0; update(k,−t); update(l,t)
    ! rotate rows and columns k and l
    for i := 1 to k−1 do rotate(i,k,i,l) endfor
    for i := k+1 to l−1 do rotate(k,i,i,l) endfor
    for i := l+1 to n do rotate(k,i,l,i) endfor
    ! rotate eigenvectors
    for i := 1 to n do
      ┌   ┐    ┌     ┐┌   ┐
      │Eik│    │c  −s││Eik│
      │   │ := │     ││   │
      │Eil│    │s   c││Eil│
      └   ┘    └     ┘└   ┘
    endfor
    ! update all potentially changed indi
    for i := 1 to n do indi := maxind(i) endfor
  loop
endproc
```
