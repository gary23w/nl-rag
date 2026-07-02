---
title: "Double hashing"
source: https://en.wikipedia.org/wiki/Double_hashing
domain: open-addressing-probing
license: CC-BY-SA-4.0
tags: open addressing, linear probing, quadratic probing, double hashing
fetched: 2026-07-02
---

# Double hashing

**Double hashing** is a computer programming technique used in conjunction with open addressing in hash tables to resolve hash collisions, by using a secondary hash of the key as an offset when a collision occurs. Double hashing with open addressing is a classical data structure on a table T .

The double hashing technique uses one hash value as an index into the table and then repeatedly steps forward an interval until the desired value is located, an empty location is reached, or the entire table has been searched; but this interval is set by a second, independent hash function. Unlike the alternative collision-resolution methods of linear probing and quadratic probing, the interval depends on the data, so that values mapping to the same location have different bucket sequences; this minimizes repeated collisions and the effects of clustering.

Given two random, uniform, and independent hash functions $h_{1}$ and $h_{2}$ , the i th location in the bucket sequence for value x in a hash table of $|T|$ buckets is: $h(i,x)=(h_{1}(x)+i\cdot h_{2}(x)){\bmod {|}}T|.$ The locations can be conveniently calculated by incrementing the previous hash by $h_{2}(x)$ , i.e. $h(i+1,x)=(h(i,x)+h_{2}(x)){\bmod {|}}T|.$

Generally, $h_{1}$ and $h_{2}$ are selected from a set of universal hash functions; $h_{1}$ is selected to have a range of $\{0,|T|-1\}$ and $h_{2}$ to have a range of $\{1,|T|-1\}$ . Double hashing approximates a random distribution; more precisely, pair-wise independent hash functions yield a probability of $(n/|T|)^{2}$ that any pair of keys will follow the same bucket sequence.

## Selection of h2(x)

The secondary hash function $h_{2}(x)$ should have several characteristics:

1. It should never yield an index of zero. When 0 is returned, only one index is probed.
2. All $h_{2}(x)$ should be *relatively prime* to $|T|$ . Otherwise the number of indices probed over *k* items would be $\min(k,|T|/h_{2}(x))$ , which could be as small as 2.
3. It should cycle through the whole table.
4. It should be very fast to compute.
5. It should be pair-wise independent of $h_{1}(x)$ .

The distribution characteristics of $h_{2}$ are irrelevant. It is analogous to a random-number generator.

In practice:

- If division hashing is used for both functions, the divisors are chosen as primes.
- If $|T|$ is a power of 2, the first two requirements are usually satisfied by making $h_{2}(x)$ always return an odd number by setting the least significant bit to 1 ( $h_{2}(x)=h_{2,{\text{orig}}}(x)|1$ ). This has the side effect of doubling the chance of collision due to one wasted bit.

## Analysis

Suppose one selects two hash functions $h_{1}$ and $h_{2}$ and inserts $\alpha |T|$ elements into a hash table with $|T|$ slots. Suppose each insertion of a key x places the key in the first available slot from the sequence $h(0,x),h(1,x),h(2,x),\ldots$ defined by

$h(i,x)=(h_{1}(x)+i\cdot h_{2}(x)){\bmod {|}}T|.$

Given this setup, theoretical analyses seek to determine the time needed to perform an additional insertion (or, equivalently, the time needed to perform an unsuccessful search). Guibas and Szemerédi proved in 1978 that, if $h_{1}$ and $h_{2}$ are uniformly random, and $\alpha <0.319$ , then the expected time is $O(1)$ . Subsequent work by Lueker and Molodowitch proved a bound of $1/(1-\alpha )$ for any $\alpha$ , and established that the behavior of the hash table can be directly coupled to that of a standard random-probing based solution. Much more recently, in 2007, Bradford and Katehakis showed that even using universal hash functions, rather than fully random ones, suffices to get a $1/(1-\alpha )$ bound.

Like all other forms of open addressing, double hashing becomes linear as the hash table approaches maximum capacity. The usual heuristic is to limit the table loading to 75% of capacity. Eventually, rehashing to a larger size will be necessary, as with all other open addressing schemes.

## Variants

Peter Dillinger's PhD thesis points out that double hashing produces unwanted equivalent hash functions when the hash functions are treated as a set, as in Bloom filters: If $h_{2}(y)=-h_{2}(x)$ and $h_{1}(y)=h_{1}(x)+k\cdot h_{2}(x)$ , then $h(i,y)=h(k-i,x)$ and the sets of hashes $\left\{h(0,x),...,h(k,x)\right\}=\left\{h(0,y),...,h(k,y)\right\}$ are identical. This makes a collision twice as likely as the hoped-for $1/|T|^{2}$ .

There are additionally a significant number of mostly-overlapping hash sets; if $h_{2}(y)=h_{2}(x)$ and $h_{1}(y)=h_{1}(x)\pm h_{2}(x)$ , then $h(i,y)=h(i\pm 1,x)$ , and comparing additional hash values (expanding the range of i ) is of no help.

### Triple hashing

Adding a third hash as a quadratic term (**triple hashing**) makes the overlap a lot less likely, since equivalent classes now need to be generated by a collaboration of both $h_{2}(x)$ and $h_{3}(x)$ , at a cost of 50% more calculations due to the added hash function. Choices for the factor for this $h_{3}(x)$ include $i^{2}$ and the triangular numbers $i(i\pm 1)/2$ . The added hash function should obey the same requirements as listed above for $h_{2}(x)$ .

Using the triangular numbers make it easier to calculate the value by forward differencing: for the $i(i-2)/2$ variety,

```mw
from collections.abc import Iterator, Callable
from typing import TypeVar

T = TypeVar('T')
hashfunc = Callable[T, int]
# assume h1, h2, h3 are defined and of type hashfunc

MODULUS = (1 << 32)

def triple_hash(key: T, k: int) -> Iterator[int]:
    """Return k iterations of a triple hash."""
    x, y, z = h1(key), h2(key), h3(key)
    yield x
    for i in range(1, k-1):
        x = (x + y) % MODULUS
        y = (y + z) % MODULUS
        yield x
```

This kind of construction does not fully remove equivalent sets. If:

$h_{1}(y)=h_{1}(x)+k\cdot h_{2}(x)+k^{2}\cdot h_{3}(x),$

$h_{2}(y)=-h_{2}(x)-2k\cdot h_{3}(x),$

and

$h_{3}(y)=h_{3}(x).$

then

${\begin{aligned}h(k-i,y)&=h_{1}(y)+(k-i)\cdot h_{2}(y)+(k-i)^{2}\cdot h_{3}(y)\\&=h_{1}(y)+(k-i)(-h_{2}(x)-2kh_{3}(x))+(k-i)^{2}h_{3}(x)\\&=\ldots \\&=h_{1}(x)+kh_{2}(x)+k^{2}h_{3}(x)+(i-k)h_{2}(x)+(i^{2}-k^{2})h_{3}(x)\\&=h_{1}(x)+ih_{2}(x)+i^{2}h_{3}(x)\\&=h(i,x).\\\end{aligned}}$

### Enhanced double hashing

Adding a cubic term $i^{3}$ or $(i^{3}-i)/6$ (a tetrahedral number), does solve the problem, a technique known as **enhanced double hashing**. The tetrahedral number can be computed efficiently by forward differencing:

```mw
struct key;	/// Opaque
/// Replace "unsigned int" with other types as needed. (Must be unsigned for guaranteed wrapping.)
typedef unsigned int hashfunc(struct key const *);
extern hashfunc h1, h2;

/// Calculate k hash values from two underlying hash functions
/// h1() and h2() using enhanced double hashing.  On return,
///     hashes[i] = h1(x) + i*h2(x) + (i*i*i - i)/6.
/// Takes advantage of automatic wrapping (modular reduction)
/// of unsigned types in C.
void ext_dbl_hash(struct key const *x, unsigned int hashes[], unsigned int n)
{
	unsigned int a = h1(x), b = h2(x), i = 0;

    hashes[i] = a;
	for (i = 1; i < n; i++) {
		a += b;	// Add quadratic difference to get cubic
		b += i;	// Add linear difference to get quadratic
		       	// i++ adds constant difference to get linear
		hashes[i] = a;
	}
}
```

In addition to rectifying the collision problem, enhanced double hashing also removes double-hashing's numerical restrictions on $h_{2}(x)$ 's properties, allowing a hash function similar in property to (but still independent of) $h_{1}$ to be used. (Using the numbering in § Selection, the first two requirements are removed.)
