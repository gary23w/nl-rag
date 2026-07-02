---
title: "Sieve of Eratosthenes (part 17/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 17/21
---

## Python

Note that the examples use range instead of xrange for Python 3 and Python 2 compatability, but when using Python 2 xrange is the nearest equivalent to Python 3's implementation of range and should be substituted for ranges with a very large number of items.

### Using set lookup

The version below uses a set to store the multiples. set objects are much faster (usually O(log n)) than lists (O(n)) for checking if a given object is a member. Using the set.update method avoids explicit iteration in the interpreter, giving a further speed improvement.

```mw
def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

print(list(eratosthenes2(100)))
```

### Using array lookup

The version below uses array lookup to test for primality. The function primes_upto() is a straightforward implementation of Sieve of Eratosthenesalgorithm. It returns prime numbers less than or equal to limit.

```mw
def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]
```

### Using generator

The following code may be slightly slower than using the array/list as above, but uses no memory for output:

```mw
def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in xrange(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): # start at ``n`` squared
                is_prime[i] = False
    for i in xrange(limit + 1):
        if is_prime[i]: yield i
```

**Example:**

```mw
>>> list(iprimes_upto(15))
[2, 3, 5, 7, 11, 13]
```

### Odds-only version of the array sieve above

The following code is faster than the above array version using only odd composite operations (for a factor of over two) and because it has been optimized to use slice operations for composite number culling to avoid extra work by the interpreter:

```mw
def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
```

Note that "range" needs to be changed to "xrange" for maximum speed with Python 2.

### Odds-only version of the generator version above

The following code is faster than the above generator version using only odd composite operations (for a factor of over two) and because it has been optimized to use slice operations for composite number culling to avoid extra work by the interpreter:

```mw
def iprimes2(limit):
    yield 2
    if limit < 3: return
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    for i in range(lmtbf + 1):
        if buf[i]: yield (i + i + 3)
```

Note that this version may actually run slightly faster than the equivalent array version with the advantage that the output doesn't require any memory.

Also note that "range" needs to be changed to "xrange" for maximum speed with Python 2.

### Factorization wheel235 version of the generator version

This uses a 235 factorial wheel for further reductions in operations; the same techniques can be applied to the array version as well; it runs slightly faster and uses slightly less memory as compared to the odds-only algorithms:

```mw
def primes235(limit):
    yield 2; yield 3; yield 5
    if limit < 7: return
    modPrms = [7,11,13,17,19,23,29,31]
    gaps = [4,2,4,2,4,6,2,6,4,2,4,2,4,6,2,6] # 2 loops for overflow
    ndxs = [0,0,0,0,1,1,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,7]
    lmtbf = (limit + 23) // 30 * 8 - 1 # integral number of wheels rounded up
    lmtsqrt = (int(limit ** 0.5) - 7)
    lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30] # round down on the wheel
    buf = [True] * (lmtbf + 1)
    for i in range(lmtsqrt + 1):
        if buf[i]:
            ci = i & 7; p = 30 * (i >> 3) + modPrms[ci]
            s = p * p - 7; p8 = p << 3
            for j in range(8):
                c = s // 30 * 8 + ndxs[s % 30]
                buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]; ci += 1
    for i in range(lmtbf - 6 + (ndxs[(limit - 7) % 30])): # adjust for extras
        if buf[i]: yield (30 * (i >> 3) + modPrms[i & 7])
```

Note: Much of the time (almost two thirds for this last case for Python 2.7.6) for any of these array/list or generator algorithms is used in the computation and enumeration of the final output in the last line(s), so any slight changes to those lines can greatly affect execution time. For Python 3 this enumeration is about twice as slow as Python 2 (Python 3.3 slow and 3.4 slower) for an even bigger percentage of time spent just outputting the results. This slow enumeration means that there is little advantage to versions that use even further wheel factorization, as the composite number culling is a small part of the time to enumerate the results.

If just the count of the number of primes over a range is desired, then converting the functions to prime counting functions by changing the final enumeration lines to "return buf.count(True)" will save a lot of time.

Note that "range" needs to be changed to "xrange" for maximum speed with Python 2 where Python 2's "xrange" is a better choice for very large sieve ranges. Timings were done primarily in Python 2 although source is Python 2/3 compatible (shows range and not xrange).

### Factorization wheel2357 version of the generator version

Note that this may be the maximum optimization that can be done for a "one large buffer array" version; this version gains the advantage of the extra wheel factorization (as for the previous version) by using Look Up Tables (LUT's) to do efficient convertsions between modulo prime values that are relatively prime as per the wheel to and from wheel and array position index values. As well as adding an extra factor of seven to the factorization wheel, this version also includes some further optimizations in memory access in using a specialized `bytearray` instead of a regular array/list for the culling array. As noted in the summary above, the time to actually do the composite number culling is such a small percentage (something about 20 percent) of the time required time to list the sieved prime values that further refinements are of little use for the algorithm other than for use as a prime counting function, and for prime counting over large ranges above say about a billion (10**9), there are much faster prime counting functions such as using LeGendre or derivative algorithms.

```mw
import time

def primes2357(limit, countonly = False):
    if countonly:
        if limit < 2: yield 0; return
        if limit < 11: yield (max(4, (limit + 1) // 2)); return
    else:
        if limit < 2: return
        yield 2;
        if limit >= 3 : yield 3
        if limit >= 5: yield 5
        if limit >= 7: yield 7
        if limit < 11: return
    # wheel size is 210 = 2 * 3 * 5 * 7 or 105 for only the odd values
    # table of one wheel size of values starting at the next value of 11 for
    # values culled of multiples of 2, 3, 5, and 7; this forms a look up table of
    # indexted relative modulo prime values...
    modPrms = [ 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
              , 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143
              , 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199, 209, 211 ]
    # table of gaps between the above values over one wheel (210)...
    gaps = [ 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2
           , 6, 4, 6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6
           , 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10
           , 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2
           , 6, 4, 6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6
           , 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10 ] # 2 loops to avoid overflow
    # table of indices of the next lowest modulo relative primes (modPrms), which
    # forms a reverse look up table from the 210 wheel indices to the `modPrm`
    # indices of the next lowest modulo relative prime value...
    ndxs = [ 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4
           , 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7
           , 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11
           , 11, 11, 11, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14
           , 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 18, 18, 18
           , 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20
           , 21, 21, 22, 22, 22, 22, 23, 23, 24, 24, 24, 24, 25, 25, 25
           , 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27
           , 28, 28, 28, 28, 28, 28, 29, 29, 30, 30, 30, 30, 31, 31, 31
           , 31, 31, 31, 32, 32, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34
           , 34, 34, 35, 35, 35, 35, 36, 36, 37, 37, 37, 37, 38, 38, 38
           , 38, 38, 38, 39, 39, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41
           , 42, 42, 43, 43, 43, 43, 44, 44, 45, 45, 45, 45, 45, 45, 45
           , 45, 45, 45, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47 ]
    lmtbf = (limit + 199) // 210 * 48 - 1 # integral number of wheels rounded up
    lmtsqrt = (int(limit ** 0.5) - 11)
    lmtsqrt = lmtsqrt // 210 * 48 + ndxs[lmtsqrt % 210] # round down on the wheel
    buf = bytearray(lmtbf + 1) # initialized to zeros
    for i in range(lmtsqrt + 1):
        if not buf[i]: # this makes the algorithm SoE and not Sieve of Sundaram...
            ci = i % 48; p = 210 * (i // 48) + modPrms[ci]
            s = p * p - 11; p8 = p * 48
            for _ in range(48):
                c = s // 210 * 48 + ndxs[s % 210]
                buf[c::p8] = [1] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]; ci += 1
    # clear primes above limit...
    lmtndx = limit - 11
    lmtndx = lmtndx // 210 * 48 + ndxs[lmtndx % 210]
    for i in range(lmtndx + 1, lmtbf + 1): buf[i] = 1
    if countonly:
        # return the count of primes...
        yield buf.count(0) + 4 # including the base primes of 2, 3, 5, and 7
    else:
        # following is slower because of generating individual primes...
        for i in range(0, lmtbf + 1, 48):
            for j in range(48):
                if not buf[i + j]: yield (210 * i + modPrms[j])

# USAGE
print("Primes to 100: ", list(primes2357(100)))
print("Number of primes to a million: ", (list(primes2357(1000000, True)))[0])
strt = time.time()
''' # slow counting of primes by iteration takes about six times longer...
gen = primes2357((n := 100000000))
primes = sum([1 for _ in gen])
'''
primes=list(primes2357((n:=100000000), True))[0]
stop = time.time()
print("Up to", n, "found", primes, "primes.")
print("This last took", stop - strt, "seconds.")
```

**Output:**

```
Primes to 100:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Number of primes to a million:  78498
Up to 100000000 found 5761455 primes.
This last took 0.22709441184997559 seconds.
```

### Page-Segmented Wheel-Factorized Faster Version

Just as the above version benefited from using a `bytearray` as compared to a regular list for the sieving array, further gains in culling and counting operations can be had by using the stable and well maintained "bitarray" package, which reduces the memory use by a factor of eight and thus gives better memory access performance due to better cache associativity and due to more efficient counting through the use of intrinsic CPU 64-bit "pop count" instructions based on bits, so this version uses "bitarray", imported as "pip install bitarray".

Another problem with the above version is the high memory use as sieving range goes up, with about 25 Gigabytes required to sieve to 1e11 and still about 3.2 Gigabytes even if a "bitarray" is used so about 32 Gigabytes to sieve to 1e12. Through using page segmentation, the memory use can be reduced to just the size of one "page" or only about 800 Megabytes in the case of the following version and that is enough to be able to sieve up to 1e12 or more on just about any machine. The reason that even such a large buffer as this needs be used is that, even though the actual culling operations are quite fast internal to the "bitarray" package, the overhead of computing the page start indices for every base culling prime for every bit plane for every page segment is still written in Python, so for CPython there is a benefit in quite a large buffer size even though this is not ideal in terms of cache associativity and therefore memory access time. By using a larger buffer size, there are less page segments over a given range and therefore the amount of Python computation is reduced.

```mw
# Page-Segmented Wheel-Factorized Sieve of Eratosthenes...

from bitarray import bitarray
from math import isqrt
from time import monotonic

# these primes have already been preculled...
whlprms = [ 2, 3, 5, 7, 11, 13, 17, 19 ]

# wheel size is 210 = 2 * 3 * 5 * 7 or 105 for only the odd values
# table of one wheel size of values starting at the first value of 11 for
# values culled of multiples of 2, 3, 5, and 7; this forms a look up table of
# indexed residual modulo prime values; note it still includes some non-primes as 121 = 11*2...
rsds = bytearray(
    [ 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
    , 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143
    , 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199, 209, 211 ])

# table of indices of the next lowest modulo relative primes (rsds), which
# forms a reverse look up table from the 105 odds wheel indices to the `modPrm`
# indices of the next lowest modulo relative prime value...
ndxs = bytearray(
    [ 0, 1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7
    , 8, 9, 9, 10, 10, 10, 11, 11, 11, 12, 13, 13, 13, 14, 14
    , 15, 16, 16, 16, 17, 17, 18, 18, 18, 19, 19, 19, 19, 20, 20
    , 21, 22, 22, 23, 24, 24, 25, 25, 25, 25, 26, 26, 26, 27, 27
    , 28, 28, 28, 29, 30, 30, 31, 31, 31, 32, 33, 33, 33, 34, 34
    , 34, 35, 35, 36, 37, 37, 38, 38, 38, 39, 40, 40, 40, 41, 41
    , 42, 43, 43, 44, 45, 45, 45, 45, 45, 46, 47, 47, 47, 47, 47 ])

# table of index look-ups rounded up to the next index
# used to ease start index per page calculation...
whlRndUps = bytearray(
    [ 0, 1, 3, 3, 4, 6, 6, 9, 9, 9, 10, 13, 13, 13, 15
    , 15, 16, 18, 18, 21, 21, 21, 24, 24, 24, 25, 28, 28, 28, 30
    , 30, 31, 34, 34, 34, 36, 36, 39, 39, 39, 43, 43, 43, 43, 45
    , 45, 46, 48, 48, 49, 51, 51, 55, 55, 55, 55, 58, 58, 58, 60
    , 60, 63, 63, 63, 64, 66, 66, 69, 69, 69, 70, 73, 73, 73, 76
    , 76, 76, 78, 78, 79, 81, 81, 84, 84, 84, 85, 88, 88, 88, 90
    , 90, 91, 93, 93, 94, 99, 99, 99, 99, 99, 100, 105, 105, 105, 105 ])
whlRndUps += bytearray(( ru + 105 for ru in whlRndUps )) + bytearray([210]) # two wheels for overflow!

# multi-level table index by residual bit plane, prime modulo, and
# cycle, indices to ease start index calculation per residual bit plane...
def mkstrts(): # immediately invoked anonymous function...
    buf = bytearray(48 * 48 * 48 * 2)
    mults = bytearray(48)
    for pi in range(48):
        p = rsds[pi]; s = (p * p - 11) >> 1
        for ci in range(48):
            rmlt = (rsds[(pi + ci) % 48] - rsds[pi]) >> 1
            rmlt += 105 if rmlt < 0 else 0; sn = s + p * rmlt
            snd = sn // 105; snr = sn - snd * 105
            mults[ndxs[snr]] = rmlt
        for si in range(48):
            s0 = (rsds[si] - 11) >> 1; sm0 = mults[si]
            for ci in range(48):
                smr = mults[ci]
                smr += (105 if smr < sm0 else 0) - sm0
                sn = s0 + p * smr; rofs = sn // 105
                addr = ((ci * 48 + pi) * 48 + si) << 1
                buf[addr] = smr << 1; buf[addr + 1] = rofs
    return buf
strts = mkstrts() # table too large for a literal; calculate it...

# fill from wheel pattern for each residual bit plane...
def fillBufFromFor(buf, low, fillmodsz): # fillsz is even number of 64-bit's
    modsz = len(buf) // 48; ptrnmodsz = len(whlptrn) // 48
    ptrnsz = 11 * 13 * 17 * 19 # in bits per bit plane
    lowi = (low - 11) // 210
    for ri in range(48):
        basedst = ri * modsz; basesrc = ri * ptrnmodsz
        for sri in range(0, fillmodsz, 131072):
            modndx = (lowi + sri) % ptrnsz; cpymodsz = min(131072, fillmodsz - sri)
            strt = basedst + sri; lmt = basedst + sri + cpymodsz
            pstrt = basesrc + modndx; plmt = basesrc + modndx + cpymodsz
            buf[strt:lmt] = whlptrn[pstrt:plmt]
    return

# cullsz is limit for each residual bit plane;
# bprps is a bytearray containing upper two bits of delta wheel, and
# lower six bits of the bit plane index...
def cullBufFromForBy(buf, low, cullsz, bprps):
    modsz = len(buf) // 48
    buflmt = low + cullsz * 210
    def bps(): # calculate residual plane start indices once per page
        oldbpwi = 0
        for bprp in bprps:
            oldbpwi += bprp >> 6; bpri = bprp & 0x3F
            bp = oldbpwi * 210 + rsds[bpri]; s = bp * bp
            if s >= buflmt: return
            # start index calculation for each base prime...
            if s > low: s -= low; s >>= 1
            else:
                wp = (rsds[bpri] - 11) >> 1
                s = ((low - s) >> 1) % (bp * 105)
                if s != 0:
                    s = bp * (whlRndUps[wp + (s + bp - 1) // bp] - wp) - s
            swi = s // 105; sri = ndxs[s - swi * 105]
            yield (bp, oldbpwi, bpri, swi, sri)
    bpsarr = list(bps())
    for ri in range(48): # this order improves cache associativity...
        base = ri * modsz
        for bp, bpwi, bpri, swi, sri in bpsarr:
            adji = ((ri * 48 + bpri) * 48 + sri) << 1
            adjmlt = strts[adji]; adjofst = strts[adji + 1]
            strt = base + swi + bpwi * adjmlt + adjofst; end = base + cullsz
            buf[strt:end:bp] = 1

# array of cull buffer culled of multiples of 11, 13, 17, and 19 with
# the multiples of 2, 3, 5, and 7, already eliminated due to the wheel;
# used as a wheel pattern to fill sieve buffers before further culling...
def mkwhlptrn():
    modsz = 11 * 13 * 17 * 19 + 131072
    buf = bitarray(modsz * 48)
    bprps = [ i for i in range(4)]
    cullBufFromForBy(buf, 11, modsz, bprps)
    buf[0] = 1; buf[modsz] = 1; buf[modsz * 2] = 1; buf[modsz * 3] = 1
    return buf
whlptrn = mkwhlptrn() # is 128K bits larger than the wheel size to avoid overflow...

# count the unset bits in the buffer representing numbers from `low` to `limit`...
def countBufFromFor(buf, low, limit):
    modsz = len(buf) // 48
    sizei = modsz - 1; sizej = 48
    if low + modsz * 210 - 1 > limit:
        sizei = (limit - low) // 210
        sizej = ndxs[(limit - low - sizei * 210) >> 1] + 1
    cnt = 0
    for ri in range(48):
        base = ri * modsz
        rilmt = base + sizei + (1 if ri < sizej else 0)
        cnt += buf[base:rilmt].count(0)
    return cnt

# takes a iterator of buf's and produces an iter of (i, j) values where
# i is the wheel index and j is the wheel modulo residue index...
def prmndxBufFromFor(buf, low, limit):
    modsz = len(buf) // 48
    sizei = modsz - 1; sizej = 48
    lowi = (low - 11) // 210
    if low * modsz * 210 - 1 > limit:
        sizei = (limit - low) // 210
        sizej = ndxs[(limit - low - sizei * 210) >> 1] + 1
    for i in range(sizei + 1):
        for j in range(48 if i < sizei else sizej):
            if not buf[i + j * modsz]: yield (lowi + i, j)

# produce bytearray of encoded bps, 2 bits delta whl ndx + 6 bits rsd ndx...
def bprpsToLimit(limit):
    def bprpsiter(buf, lmt): # non paged! buf wheels are a multiple of 64 bits rounded up...
        oldi = 0
        for i, j in prmndxBufFromFor(buf, 11, lmt):
            yield ((i - oldi) << 6) | j
            oldi = i
    if limit < 529: return bytearray(bprpsiter(whlptrn, limit))
    else:
        bprps = bprpsToLimit(isqrt(limit)) # recursively!
        modsz = ((limit - 11) // 210 + 127) & -64
        buf = bitarray(modsz * 48)
        fillBufFromFor(buf, 11, modsz)
        cullBufFromForBy(buf, 11, modsz, bprps)
        return bytearray(bprpsiter(buf, limit))

# produces an iterator of buffers with last one sized to fi, with the buffer
# the buffer passed into a provided function to produce iteration of result...
def bufsToLimit(limit, func):
    # 32 MegaBytes per module bit plane maximum size
    modsz = min(131072 * 8 * 64, ((limit - 11) // 210 + 127) & -64)
    bufsz = modsz * 210; buf = bitarray(modsz * 48)
    bprps = bprpsToLimit(isqrt(limit))
    for low in range(11, limit + 1, bufsz):
        fillmodsz = min(modsz, ((limit - low) // 210 + 127) & -64)
        # adjustable buffer size for efficiency
        fillBufFromFor(buf, low, fillmodsz)
        yield func(buf, low, modsz, bprps)

# produce and iterator of primes up to `limit`...
def primesTo(limit):
    if limit < 2: return
    for p in whlprms:
        if p <= limit: yield p
    if limit < 23: return
    def bufToPrimesIter(buf, low, modsz, bps):
        cullBufFromForBy(buf, low, modsz, bps)
        for i, j in prmndxBufFromFor(buf, low, limit):
            yield i * 210 + rsds[j]
    for bfrprms in bufsToLimit(limit, bufToPrimesIter):
        for prm in bfrprms: yield prm

# the result is the count of primes to the given `limit`...
def countPrimesTo(limit):
    if limit < 23:
        cnt = 0
        for p in whlprms:
            if p <= limit: cnt += 1
        return cnt
    def bufToCount(buf, low, cullmodsz, bprps):
        cullBufFromForBy(buf, low, cullmodsz, bprps)
        return countBufFromFor(buf, low, limit)
    return sum(bufsToLimit(limit, bufToCount)) + 8

# USAGE
print("Primes to 100: ", list(primesTo(100)))
print("Number of primes to a million: ", countPrimesTo(1_000_000))
strt = monotonic()
''' # slow counting of primes by iteration takes about six times longer...
gen = primesTo((n := 1_000_000_000))
primes = sum(( 1 for _ in gen ))
'''
for _ in range(n := 10): primes = countPrimesTo(limit := 1_000_000_000)
stop = monotonic()
print("Up to", limit, "repeated", n, "time(s), found", primes, "primes.")
print("This last took", stop - strt, "seconds.")
```

**Output:**

```
Primes to 100:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Number of primes to a million:  78498
Up to 1000000000 repeated 10 time(s), found 50847534 primes.
This last took 1.68718407896813 seconds.
```

As can be seen, when run on an AMD 7840HS CPU at 5.1 GHz (single threaded boosted), this version is very fast and is only about two and a half times as slow as Kim Walisch's highly optimized "primesieve" written in C++ for single threaded counting of primes taking only about 170 milliseconds compared to "primesieve"'s 62 milliseconds. If one did a Pull Request (PR) for the "bitarray" package to add the optimizations of extreme loop unrolling and the use of SIMD instructions, the number of CPU clock cycles per cull operation could be reduced to the same as that of "primesieve" but this Python version would still be a little slower due to the overhead of the Python supporting calculations.

This overhead calculating operations cost goes up with sieving range, with the time to count the primes to 1e11 about 2.5 times slower than "primesieve" and the time to count the primes to 1e12 almost three times as slow. In order to maintain about this ratio across the reasonably usable sieving range to 1e12, the buffer size is scaled according to the range to be sieved with a maximum size that seems adequate for fairly large sieving ranges, although this could likely be tuned further.

This is likely about the fastest single-threaded Sieve of Eratosthenes that can be written in CPython without "cheating" and just calling "primesieve" as a package or external library.

### Using numpy

Library:

NumPy

Below code adapted from literateprograms.org using numpy

```mw
import numpy
def primes_upto2(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]
```

**Performance note:** there is no point to add wheels here, due to execution of p[n*n::n] = 0 and nonzero() takes us almost all time.

Also see Prime numbers and Numpy – Python.

### Using wheels with numpy

Version with wheel based optimization:

```mw
from numpy import array, bool_, multiply, nonzero, ones, put, resize
#
def makepattern(smallprimes):
    pattern = ones(multiply.reduce(smallprimes), dtype=bool_)
    pattern[0] = 0
    for p in smallprimes:
        pattern[p::p] = 0
    return pattern
#
def primes_upto3(limit, smallprimes=(2,3,5,7,11)):    
    sp = array(smallprimes)
    if limit <= sp.max(): return sp[sp <= limit]
    #
    isprime = resize(makepattern(sp), limit + 1) 
    isprime[:2] = 0; put(isprime, sp, 1) 
    #
    for n in range(sp.max() + 2, int(limit**0.5 + 1.5), 2): 
        if isprime[n]:
            isprime[n*n::n] = 0 
    return nonzero(isprime)[0]
```

Examples:

```mw
>>> primes_upto3(10**6, smallprimes=(2,3)) # Wall time: 0.17
array([     2,      3,      5, ..., 999961, 999979, 999983])
>>> primes_upto3(10**7, smallprimes=(2,3))            # Wall time: '''2.13'''
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
>>> primes_upto3(15)
array([ 2,  3,  5,  7, 11, 13])
>>> primes_upto3(10**7, smallprimes=primes_upto3(15)) # Wall time: '''1.31'''
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
>>> primes_upto2(10**7)                               # Wall time: '''1.39''' <-- version ''without'' wheels
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
>>> primes_upto3(10**7)                               # Wall time: '''1.30'''
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
```

The above-mentioned examples demonstrate that the *given* wheel based optimization does not show significant performance gain.

### Infinite generator

A generator that will generate primes indefinitely (perhaps until it runs out of memory). Used as a library here.

Works with

:

Python

version 2.6+, 3.x

```mw
import heapq

# generates all prime numbers
def sieve():
    # priority queue of the sequences of non-primes
    # the priority queue allows us to get the "next" non-prime quickly
    nonprimes = []
    
    i = 2
    while True:
        if nonprimes and i == nonprimes[0][0]: # non-prime
            while nonprimes[0][0] == i:
                # for each sequence that generates this number,
                # have it go to the next number (simply add the prime)
                # and re-position it in the priority queue
                x = nonprimes[0]
                x[0] += x[1]
                heapq.heapreplace(nonprimes, x)
        
        else: # prime
            # insert a 2-element list into the priority queue:
            # [current multiple, prime]
            # the first element allows sorting by value of current multiple
            # we start with i^2
            heapq.heappush(nonprimes, [i*i, i])
            yield i
        
        i += 1
```

Example:

```
>>> foo = sieve()
>>> for i in range(8):
...     print(next(foo))
... 
2
3
5
7
11
13
17
19
```

### Infinite generator with a faster algorithm

The adding of each discovered prime's incremental step info to the mapping should be ***postponed*** until the prime's *square* is seen amongst the candidate numbers, as it is useless before that point. This drastically reduces the space complexity from *O(n)* to *O(sqrt(n/log(n)))*, in *`n`* primes produced, and also lowers the run time complexity quite low (this test entry in Python 2.7 and this test entry in Python 3.x shows about *~ n1.08* empirical order of growth which is very close to the theoretical value of *O(n log(n) log(log(n)))*, in *`n`* primes produced):

Works with

:

Python

version 2.6+, 3.x

```mw
def primes():
    yield 2; yield 3; yield 5; yield 7;
    bps = (p for p in primes())             # separate supply of "base" primes (b.p.)
    p = next(bps) and next(bps)             # discard 2, then get 3
    q = p * p                               # 9 - square of next base prime to keep track of,
    sieve = {}                              #                       in the sieve dict
    n = 9                                   # n is the next candidate number
    while True:
        if n not in sieve:                  # n is not a multiple of any of base primes,
            if n < q:                       # below next base prime's square, so
                yield n                     # n is prime
            else:
                p2 = p + p                  # n == p * p: for prime p, add p * p + 2 * p
                sieve[q + p2] = p2          #   to the dict, with 2 * p as the increment step
                p = next(bps); q = p * p    # pull next base prime, and get its square
        else:
            s = sieve.pop(n); nxt = n + s   # n's a multiple of some b.p., find next multiple
            while nxt in sieve: nxt += s    # ensure each entry is unique
            sieve[nxt] = s                  # nxt is next non-marked multiple of this prime
        n += 2                              # work on odds only
 
import itertools
def primes_up_to(limit):
    return list(itertools.takewhile(lambda p: p <= limit, primes()))
```

### Fast infinite generator using a wheel

Although theoretically over three times faster than odds-only, the following code using a 2/3/5/7 wheel is only about 1.5 times faster than the above odds-only code due to the extra overheads in code complexity. The test link for Python 2.7 and test link for Python 3.x show about the same empirical order of growth as the odds-only implementation above once the range grows enough so the dict operations become amortized to a constant factor.

Works with

:

Python

version 2.6+, 3.x

```mw
def primes():
    for p in [2,3,5,7]: yield p                 # base wheel primes
    gaps1 = [ 2,4,2,4,6,2,6,4,2,4,6,6,2,6,4,2,6,4,6,8,4,2,4,2,4,8 ]
    gaps = gaps1 + [ 6,4,6,2,4,6,2,6,6,4,2,4,6,2,6,4,2,4,2,10,2,10 ] # wheel2357
    def wheel_prime_pairs():
        yield (11,0); bps = wheel_prime_pairs() # additional primes supply
        p, pi = next(bps); q = p * p            # adv to get 11 sqr'd is 121 as next square to put
        sieve = {}; n = 13; ni = 1              #   into sieve dict; init cndidate, wheel ndx
        while True:
            if n not in sieve:                  # is not a multiple of previously recorded primes
                if n < q: yield (n, ni)         # n is prime with wheel modulo index
                else:
                    npi = pi + 1                # advance wheel index
                    if npi > 47: npi = 0
                    sieve[q + p * gaps[pi]] = (p, npi) # n == p * p: put next cull position on wheel
                    p, pi = next(bps); q = p * p  # advance next prime and prime square to put
            else:
                s, si = sieve.pop(n)
                nxt = n + s * gaps[si]          # move current cull position up the wheel
                si = si + 1                     # advance wheel index
                if si > 47: si = 0
                while nxt in sieve:             # ensure each entry is unique by wheel
                    nxt += s * gaps[si]
                    si = si + 1                 # advance wheel index
                    if si > 47: si = 0
                sieve[nxt] = (s, si)            # next non-marked multiple of a prime
            nni = ni + 1                        # advance wheel index
            if nni > 47: nni = 0
            n += gaps[ni]; ni = nni             # advance on the wheel
    for p, pi in wheel_prime_pairs(): yield p   # strip out indexes
```

Further gains of about 1.5 times in speed can be made using the same code by only changing the tables and a few constants for a further constant factor gain of about 1.5 times in speed by using a 2/3/5/7/11/13/17 wheel (with the gaps list 92160 elements long) computed for a slight constant overhead time as per the test link for Python 2.7 and test link for Python 3.x. Further wheel factorization will not really be worth it as the gains will be small (if any and not losses) and the gaps table huge - it is already too big for efficient use by 32-bit Python 3 and the wheel should likely be stopped at 13:

```mw
def primes():
    whlPrms = [2,3,5,7,11,13,17]                # base wheel primes
    for p in whlPrms: yield p
    def makeGaps():
        buf = [True] * (3 * 5 * 7 * 11 * 13 * 17 + 1) # all odds plus extra for o/f
        for p in whlPrms:
            if p < 3:
                continue              # no need to handle evens
            strt = (p * p - 19) >> 1            # start position (divided by 2 using shift)
            while strt < 0: strt += p
            buf[strt::p] = [False] * ((len(buf) - strt - 1) // p + 1) # cull for p
        whlPsns = [i + i for i,v in enumerate(buf) if v]
        return [whlPsns[i + 1] - whlPsns[i] for i in range(len(whlPsns) - 1)]
    gaps = makeGaps()                           # big wheel gaps
    def wheel_prime_pairs():
        yield (19,0); bps = wheel_prime_pairs() # additional primes supply
        p, pi = next(bps); q = p * p            # adv to get 11 sqr'd is 121 as next square to put
        sieve = {}; n = 23; ni = 1              #   into sieve dict; init cndidate, wheel ndx
        while True:
            if n not in sieve:                  # is not a multiple of previously recorded primes
                if n < q: yield (n, ni)         # n is prime with wheel modulo index
                else:
                    npi = pi + 1                # advance wheel index
                    if npi > 92159: npi = 0
                    sieve[q + p * gaps[pi]] = (p, npi) # n == p * p: put next cull position on wheel
                    p, pi = next(bps); q = p * p  # advance next prime and prime square to put
            else:
                s, si = sieve.pop(n)
                nxt = n + s * gaps[si]          # move current cull position up the wheel
                si = si + 1                     # advance wheel index
                if si > 92159: si = 0
                while nxt in sieve:             # ensure each entry is unique by wheel
                    nxt += s * gaps[si]
                    si = si + 1                 # advance wheel index
                    if si > 92159: si = 0
                sieve[nxt] = (s, si)            # next non-marked multiple of a prime
            nni = ni + 1                        # advance wheel index
            if nni > 92159: nni = 0
            n += gaps[ni]; ni = nni             # advance on the wheel
    for p, pi in wheel_prime_pairs(): yield p   # strip out indexes
```

### Iterative sieve on unbounded count from 2

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** The below linked extensible sieve uses rem testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

See Extensible prime generator: Iterative sieve on unbounded count from 2


## Quackery

```mw
  [ dup 1
    [ 2dup > while
      + 1 >>
      2dup / again ]
    drop nip ]                  is sqrt         ( n --> n )
 
  [ stack [ 3 ~ ] constant ]    is primes       (   --> s )
 
  ( If a number is prime, the corresponding bit on the
    number on the primes ancillary stack is set.
    Initially all the bits are set except for 0 and 1,
    which are not prime numbers by definition. 
    "eratosthenes" unsets all bits above those specified
    by it's argument. )
 
  [ bit ~
    primes take & primes put ]  is -composite   ( n -->   )
 
  [ bit primes share & 0 != ]   is isprime      ( n --> b )
 
  [ dup dup sqrt times
      [ i^ 1+
        dup isprime if
          [ dup 2 **
            [ dup -composite
              over +
              rot 2dup >
              dip unrot until ]
            drop ]
        drop ]
     drop 
     1+ bit 1 -
     primes take & 
     primes put ]                 is eratosthenes ( n -->   )
 
  100 eratosthenes
 
  100 times [ i^ isprime if [ i^ echo sp ] ]
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## R

```mw
sieve <- function(n) {
  if (n < 2) integer(0)
  else {
    primes <- rep(T, n)
    primes[[1]] <- F
    for(i in seq(sqrt(n))) {
      if(primes[[i]]) {
        primes[seq(i * i, n, i)] <- F
      }
    }
    which(primes)
  }
}

sieve(1000)
```

**Output:**

```
  [1]   2   3   5   7  11  13  17  19  23  29  31  37  41  43  47  53  59  61
 [19]  67  71  73  79  83  89  97 101 103 107 109 113 127 131 137 139 149 151
 [37] 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251
 [55] 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359
 [73] 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463
 [91] 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593
[109] 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701
[127] 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827
[145] 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953
[163] 967 971 977 983 991 997
```

**Alternate Odds-Only Version**

```mw
sieve <- function(n) {
  if (n < 2) return(integer(0))
  lmt <- (sqrt(n) - 1) / 2
  sz <- (n - 1) / 2
  buf <- rep(TRUE, sz)
  for(i in seq(lmt)) {
    if (buf[i]) {
      buf[seq((i + i) * (i + 1), sz, by=(i + i + 1))] <- FALSE
    }
  }
  cat(2, sep='')
  for(i in seq(sz)) {
    if (buf[i]) {
      cat(" ", (i + i + 1), sep='')
    }
  }
}

sieve(1000)
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997
```


## Racket

### Imperative versions

Ugly imperative version:

```mw
#lang racket

(define (sieve n)
  (define non-primes '())
  (define primes '())
  (for ([i (in-range 2 (add1 n))])
    (unless (member i non-primes)
      (set! primes (cons i primes))
      (for ([j (in-range (* i i) (add1 n) i)])
        (set! non-primes (cons j non-primes)))))
  (reverse primes))

(sieve 100)
```

A little nicer, but still imperative:

```mw
#lang racket
(define (sieve n)
  (define primes (make-vector (add1 n) #t))
  (for* ([i (in-range 2 (add1 n))]
         #:when (vector-ref primes i)
         [j (in-range (* i i) (add1 n) i)])
    (vector-set! primes j #f))
  (for/list ([n (in-range 2 (add1 n))]
             #:when (vector-ref primes n))
    n))
(sieve 100)
```

Imperative version using a bit vector:

```mw
#lang racket
(require data/bit-vector)
;; Returns a list of prime numbers up to natural number limit
(define (eratosthenes limit)
  (define bv (make-bit-vector (+ limit 1) #f))
  (bit-vector-set! bv 0 #t)
  (bit-vector-set! bv 1 #t)
  (for* ([i (in-range (add1 (sqrt limit)))] #:unless (bit-vector-ref bv i)
         [j (in-range (* 2 i) (bit-vector-length bv) i)])
    (bit-vector-set! bv j #t))
  ;; translate to a list of primes
  (for/list ([i (bit-vector-length bv)] #:unless (bit-vector-ref bv i)) i))
(eratosthenes 100)
```

**Output:**

'(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)

### Infinite list of primes Using laziness

These examples use infinite lists (streams) to implement the sieve of Eratosthenes in a functional way, and producing all prime numbers. The following functions are used as a prefix for pieces of code that follow:

```mw
#lang lazy
(define (ints-from i d) (cons i (ints-from (+ i d) d)))
(define (after n l f)
  (if (< (car l) n) (cons (car l) (after n (cdr l) f)) (f l)))
(define (diff l1 l2)
  (let ([x1 (car l1)] [x2 (car l2)])
    (cond [(< x1 x2) (cons x1 (diff (cdr l1)      l2 ))]
          [(> x1 x2)          (diff      l1  (cdr l2)) ]
          [else               (diff (cdr l1) (cdr l2)) ])))
(define (union l1 l2)        ; union of two lists
  (let ([x1 (car l1)] [x2 (car l2)])
    (cond [(< x1 x2) (cons x1 (union (cdr l1)      l2 ))]
          [(> x1 x2) (cons x2 (union      l1  (cdr l2)))]
          [else      (cons x1 (union (cdr l1) (cdr l2)))])))
```

#### Basic sieve

```mw
(define (sieve l)
  (define x (car l))
  (cons x (sieve (diff (cdr l) (ints-from (+ x x) x)))))
(define primes (sieve (ints-from 2 1)))
(!! (take 25 primes))
```

Runs at ~ n^2.1 empirically, for *n <= 1500* primes produced.

#### With merged composites

Note that the first number, 2, and its multiples stream `(ints-from 4 2)` are handled separately to ensure that the non-primes list is never empty, which simplifies the code for `union` which assumes non-empty infinite lists.

```mw
(define (sieve l non-primes)
  (let ([x (car l)] [np (car non-primes)])
    (cond [(= x np)     (sieve (cdr l) (cdr  non-primes))]    ; else x < np
          [else (cons x (sieve (cdr l) (union (ints-from (* x x) x)  
                                               non-primes)))]))) 
(define primes (cons 2 (sieve (ints-from 3 1) (ints-from 4 2))))
```

#### Basic sieve Optimized with postponed processing

Since a prime's multiples that count start from its square, we should only start removing them when we reach that square.

```mw
(define (sieve l prs)
  (define p (car prs))
  (define q (* p p))
  (after q l (λ(t) (sieve (diff t (ints-from q p)) (cdr prs)))))
(define primes (cons 2 (sieve (ints-from 3 1) primes)))
```

Runs at ~ n^1.4 up to n=10,000. The initial 2 in the self-referential primes definition is needed to prevent a "black hole".

#### Merged composites Optimized with postponed processing

Since prime's multiples that matter start from its square, we should only add them when we reach that square.

```mw
(define (composites l q primes)
  (after q l 
    (λ(t) 
      (let ([p (car primes)] [r (cadr primes)])
        (composites (union t (ints-from q p))   ; q = p*p
                    (* r r) (cdr primes))))))
(define primes (cons 2 
                 (diff (ints-from 3 1)
                       (composites (ints-from 4 2) 9 (cdr primes)))))
```

#### Implementation of Richard Bird's algorithm

Appears in M.O'Neill's paper. Achieves on its own the proper postponement that is specifically arranged for in the version above (with `after`), and is yet more efficient, because it folds to the right and so builds the right-leaning structure of merges at run time, where the more frequently-producing streams of multiples appear *higher* in that structure, so the composite numbers produced by them have less `merge` nodes to percolate through:

```mw
(define primes
  (cons 2 (diff (ints-from 3 1)
                (foldr (λ(p r) (define q (* p p))
                               (cons q (union (ints-from (+ q p) p) r)))
                       '() primes))))
```

### Using threads and channels

Same algorithm as "merged composites" above (without the postponement optimization), but now using threads and channels to produce a channel of all prime numbers (similar to newsqueak). The macro at the top is a convenient wrapper around definitions of channels using a thread that feeds them.

```mw
#lang racket
(define-syntax (define-thread-loop stx)
  (syntax-case stx ()
    [(_ (name . args) expr ...)
     (with-syntax ([out! (datum->syntax stx 'out!)])
       #'(define (name . args)
           (define out (make-channel))
           (define (out! x) (channel-put out x))
           (thread (λ() (let loop () expr ... (loop))))
           out))]))
(define-thread-loop (ints-from i d) (out! i) (set! i (+ i d)))
(define-thread-loop (merge c1 c2)
  (let loop ([x1 (channel-get c1)] [x2 (channel-get c2)])
    (cond [(> x1 x2) (out! x2) (loop x1 (channel-get c2))]
          [(< x1 x2) (out! x1) (loop (channel-get c1) x2)]
          [else      (out! x1) (loop (channel-get c1) (channel-get c2))])))
(define-thread-loop (sieve l non-primes)
  (let loop ([x (channel-get l)] [np (channel-get non-primes)])
    (cond [(> x np) (loop x (channel-get non-primes))]
          [(= x np) (loop (channel-get l) (channel-get non-primes))]
          [else     (out! x) 
                    (set! non-primes (merge (ints-from (* x x) x) non-primes))
                    (loop (channel-get l)  np)])))
(define-thread-loop (cons x l)
  (out! x) (let loop () (out! (channel-get l)) (loop)))
(define primes (cons 2 (sieve (ints-from 3 1) (ints-from 4 2))))
(for/list ([i 25] [x (in-producer channel-get eof primes)]) x)
```

### Using generators

Yet another variation of the same algorithm as above, this time using generators.

```mw
#lang racket
(require racket/generator)
(define (ints-from i d)
  (generator () (let loop ([i i]) (yield i) (loop (+ i d)))))
(define (merge g1 g2)
  (generator ()
    (let loop ([x1 (g1)] [x2 (g2)])
      (cond [(< x1 x2) (yield x1) (loop (g1) x2)]
            [(> x1 x2) (yield x2) (loop x1 (g2))]
            [else      (yield x1) (loop (g1) (g2))]))))
(define (sieve l non-primes)
  (generator ()
    (let loop ([x (l)] [np (non-primes)])
      (cond [(> x np) (loop x (non-primes))]
            [(= x np) (loop (l) (non-primes))]
            [else (yield x)
                  (set! non-primes (merge (ints-from (* x x) x) non-primes))
                  (loop (l) np)]))))
(define (cons x l) (generator () (yield x) (let loop () (yield (l)) (loop))))
(define primes (cons 2 (sieve (ints-from 3 1) (ints-from 4 2))))
(for/list ([i 25] [x (in-producer primes)]) x)
```
