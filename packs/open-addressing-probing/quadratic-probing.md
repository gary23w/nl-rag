---
title: "Quadratic probing"
source: https://en.wikipedia.org/wiki/Quadratic_probing
domain: open-addressing-probing
license: CC-BY-SA-4.0
tags: open addressing, linear probing, quadratic probing, double hashing
fetched: 2026-07-02
---

# Quadratic probing

**Quadratic probing** is an open addressing scheme in computer programming for resolving hash collisions in hash tables. Quadratic probing operates by taking the original hash index and adding successive values of an arbitrary quadratic polynomial until an open slot is found.

An example sequence using quadratic probing is:

$H+1^{2},H+2^{2},H+3^{2},H+4^{2},...,H+k^{2}$

Quadratic probing is often recommended as an alternative to linear probing because it incurs less clustering. Quadratic probing exhibits better locality of reference than many other hash table such as chaining; however, for queries, quadratic probing does not have as good locality as linear probing, causing the latter to be faster in some settings.

## History

Quadratic probing was first introduced by Ward Douglas Maurer in 1968. Several subsequent variations of the data structure were proposed in the 1970s in order to guarantee that the probe sequence hits every slot without cycling prematurely. Quadratic probing is widely believed to avoid the clustering effects that make linear probing slow at high load factors. It serves as the basis for many widely used high-performance hash-tables, including Google's open-source Abseil hash table.

It is conjectured that quadratic probing, when filled to $1-\epsilon$ full, supports insertions in expected time $O(\epsilon ^{-1})$ . Proving this, or even proving *any* non-trivial time bound for quadratic probing remains open. The closest result, due to Kuszmaul and Xi, shows that, at load factors of less than $\approx 0.089$ , insertions take $O(1)$ expected time.

## Quadratic function

Let *h*(*k*) be a hash function that maps an element *k* to an integer in [0, *m*−1], where *m* is the size of the table. Let the *i*th probe position for a value *k* be given by the function

$h(k,i)=h(k)+c_{1}i+c_{2}i^{2}{\pmod {m}}$

where *c*2 ≠ 0 (If *c*2 = 0, then *h*(*k*,*i*) degrades to a linear probe). For a given hash table, the values of *c*1 and *c*2 remain constant.

**Examples:**

- If $h(k,i)=(h(k)+i+i^{2}){\pmod {m}}$ , then the probe sequence will be $h(k),h(k)+2,h(k)+6,...$
- For *m* = 2*n*, a good choice for the constants are *c*1 = *c*2 = 1/2, as the values of *h*(*k*,*i*) for *i* in [0, *m*−1] are all distinct (in fact, it is a permutation on [0, *m*−1]). This leads to a probe sequence of $h(k),h(k)+1,h(k)+3,h(k)+6,...$ (the triangular numbers) where the values increase by 1, 2, 3, ...
- For prime *m* > 2, most choices of *c*1 and *c*2 will make *h*(*k*,*i*) distinct for *i* in [0, (*m*−1)/2]. Such choices include *c*1 = *c*2 = 1/2, *c*1 = *c*2 = 1, and *c*1 = 0, *c*2 = 1. However, there are only *m*/2 distinct probes for a given element, requiring other techniques to guarantee that insertions will succeed when the load factor exceeds 1/2.
- For $m=n^{p}$ , where *m*, *n*, and *p* are integer greater or equal 2 (degrades to linear probe when *p* = 1), then $h(k,i)=(h(k)+i+ni^{2}){\pmod {m}}$ gives cycle of all distinct probes. It can be computed in loop as: $h(k,0)=h(k)$ , and $h(k,i+1)=(h(k,i)+2in+n+1){\pmod {m}}$
- For any *m*, full cycle with quadratic probing can be achieved by rounding up *m* to closest power of 2, compute probe index: $h(k,i)=h(k)+((i^{2}+i)/2){\pmod {roundUp2(m)}}$ , and skip iteration when $h(k,i)>=m$ . There is maximum $roundUp2(m)-m<m/2$ skipped iterations, and these iterations do not refer to memory, so it is fast operation on most modern processors. Rounding up *m* can be computed by:

```mw
uint64_t roundUp2(uint64_t v){
	v--;
	v |= v >> 1;
	v |= v >> 2;
	v |= v >> 4;
	v |= v >> 8;
	v |= v >> 16;
	v |= v >> 32;
	v++;
	return v;
}
```

## Limitations

### Alternating signs

If the sign of the offset is alternated (e.g. +1, −4, +9, −16, etc.), and if the number of buckets is a prime number p congruent to 3 modulo 4 (e.g. 3, 7, 11, 19, 23, 31, etc.), then the first p offsets will be unique (modulo p ). In other words, a permutation of 0 through $p-1$ is obtained, and, consequently, a free bucket will always be found as long as at least one exists.
