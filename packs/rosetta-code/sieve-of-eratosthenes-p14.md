---
title: "Sieve of Eratosthenes (part 14/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 14/21
---

## Mojo

Tested with Mojo version 24.4.0:

```mw
from memory import memset_zero
from memory.unsafe import (DTypePointer)
from time import (now)

alias cLIMIT: Int = 1_000_000_000

struct SoEBasic(Sized):
    var len: Int
    var cmpsts: DTypePointer[DType.bool] # because DynamicVector has deep copy bug in mojo version 0.7
    var sz: Int
    var ndx: Int
    fn __init__(inout self, limit: Int):
        self.len = limit - 1
        self.sz = limit - 1
        self.ndx = 0
        self.cmpsts = DTypePointer[DType.bool].alloc(limit - 1)
        memset_zero(self.cmpsts, limit - 1)
        for i in range(limit - 1):
            var s = i * (i + 4) + 2
            if s >= limit - 1: break
            if self.cmpsts[i]: continue
            var bp = i + 2
            for c in range(s, limit - 1, bp):
                self.cmpsts[c] = True
        for i in range(limit - 1):
            if self.cmpsts[i]: self.sz -= 1
    fn __del__(owned self):
        self.cmpsts.free()
    fn __copyinit__(inout self, existing: Self):
        self.len = existing.len
        self.cmpsts = DTypePointer[DType.bool].alloc(self.len)
        for i in range(self.len):
            self.cmpsts[i] = existing.cmpsts[i]
        self.sz = existing.sz
        self.ndx = existing.ndx
    fn __moveinit__(inout self, owned existing: Self):
        self.len = existing.len
        self.cmpsts = existing.cmpsts
        self.sz = existing.sz
        self.ndx = existing.ndx
    fn __len__(self: Self) -> Int: return self.sz
    fn __iter__(self: Self) -> Self: return self
    fn __next__(inout self: Self) -> Int:
        if self.ndx >= self.len: return 0
        while (self.ndx < self.len) and (self.cmpsts[self.ndx]):
            self.ndx += 1
        var rslt = self.ndx + 2; self.sz -= 1; self.ndx += 1
        return rslt

fn main():
    print("The primes to 100 are:")
    for prm in SoEBasic(100): print(prm, " ",end="")
    print()
    var strt0 = now()
    var answr0 = len(SoEBasic(1_000_000))
    var elpsd0 = (now() - strt0) / 1000000
    print("Found", answr0, "primes up to 1,000,000 in", elpsd0, "milliseconds.")
    var strt1 = now()
    var answr1 = len(SoEBasic(cLIMIT))
    var elpsd1 = (now() - strt1) / 1000000
    print("Found", answr1, "primes up to", cLIMIT, "in", elpsd1, "milliseconds.")
```

**Output:**

```
The primes to 100 are:
2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97  
Found 78498 primes up to 1,000,000 in 1.2642770000000001 milliseconds.
Found 50847534 primes up to 1000000000 in 6034.328751 milliseconds.
```

as run on an AMD 7840HS CPU at 5.1 GHz.

Note that due to the huge memory array used, when large ranges are selected, the speed is disproportional in speed slow down by about four times.

This solution uses an iterator struct which seems to be the Mojo-preferred way to do this, and normally a might have been used the the culling array but here the raw unsafe pointer type is used.

### Odds-Only with Optimizations

This version does three significant improvements to the above code as follows: 1) It is trivial to skip the processing to store representations for and cull the even composite numbers other than the prime number two, saving half the storage space and reducing the culling time to about 40 percent. 2) There is a repeating pattern of culling composite representations over a bit-packed byte array (which reduces the storage requirement by another eight times) that repeats every eight culling operations, which can be encapsulated by a extreme loop unrolling technique with compiler generated constants as done here. 3) Further, there is a further extreme optimization technique of dense culling for small base prime values whose culling span is less than one register in size where the loaded register is repeatedly culled for different base prime strides before being written out (with such optimization done by the compiler), again using compiler generated modification constants. This technique is usually further optimized by modern compilers to use efficient auto-vectorization and the use of SIMD registers available to the architecture to reduce these culling operations to an average of a tiny fraction of a CPU clock cycle per cull.

Mojo version 24.4.0 was tested:

```mw
from memory import (memset_zero, memcpy)
from memory.unsafe import (DTypePointer)
from bit import pop_count
from time import (now)

alias cLIMIT: Int = 1_000_000_000

alias cBufferSize: Int = 262144 # bytes
alias cBufferBits: Int = cBufferSize * 8

alias UnrollFunc = fn(DTypePointer[DType.uint8], Int, Int, Int) -> None

@always_inline
fn extreme[OFST: Int, BP: Int](pcmps: DTypePointer[DType.uint8], bufsz: Int, s: Int, bp: Int):
  var cp = pcmps + (s >> 3)
  var r1: Int = ((s + bp) >> 3) - (s >> 3)
  var r2: Int = ((s + 2 * bp) >> 3) - (s >> 3)
  var r3: Int = ((s + 3 * bp) >> 3) - (s >> 3)
  var r4: Int = ((s + 4 * bp) >> 3) - (s >> 3)
  var r5: Int = ((s + 5 * bp) >> 3) - (s >> 3)
  var r6: Int = ((s + 6 * bp) >> 3) - (s >> 3)
  var r7: Int = ((s + 7 * bp) >> 3) - (s >> 3)
  var plmt: DTypePointer[DType.uint8] = pcmps + bufsz - r7
  while cp < plmt:
    cp.store(cp.load() | (1 << OFST))
    (cp + r1).store((cp + r1).load() | (1 << ((OFST + BP) & 7)))
    (cp + r2).store((cp + r2).load() | (1 << ((OFST + 2 * BP) & 7)))
    (cp + r3).store((cp + r3).load() | (1 << ((OFST + 3 * BP) & 7)))
    (cp + r4).store((cp + r4).load() | (1 << ((OFST + 4 * BP) & 7)))
    (cp + r5).store((cp + r5).load() | (1 << ((OFST + 5 * BP) & 7)))
    (cp + r6).store((cp + r6).load() | (1 << ((OFST + 6 * BP) & 7)))
    (cp + r7).store((cp + r7).load() | (1 << ((OFST + 7 * BP) & 7)))
    cp += bp
  var eplmt: DTypePointer[DType.uint8] = plmt + r7
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << OFST))
  cp += r1
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + BP) & 7)))
  cp += r2 - r1
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + 2 * BP) & 7)))
  cp += r3 - r2
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + 3 * BP) & 7)))
  cp += r4 - r3
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + 4 * BP) & 7)))
  cp += r5 - r4
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + 5 * BP) & 7)))
  cp += r6 - r5
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + 6 * BP) & 7)))
  cp += r7 - r6
  if eplmt == cp or eplmt < cp: return
  cp.store(cp.load() | (1 << ((OFST + 7 * BP) & 7)))

fn mkExtremeFuncs[SIZE: Int]() -> UnsafePointer[UnrollFunc, 0]:
  var jmptbl = UnsafePointer[UnrollFunc, 0].alloc(SIZE)
  @parameter
  for i in range(SIZE):
    alias OFST = i >> 2
    alias BP = ((i & 3) << 1) + 1
    jmptbl[i] = extreme[OFST, BP]
  return jmptbl
  
alias DenseFunc = fn(DTypePointer[DType.uint64], Int, Int) -> DTypePointer[DType.uint64]

@always_inline
fn denseCullFunc[BP: Int](pcmps: DTypePointer[DType.uint64], bufsz: Int, s: Int) -> DTypePointer[DType.uint64]:
  var cp: DTypePointer[DType.uint64] = pcmps + (s >> 6)
  var plmt = pcmps + (bufsz >> 3) - BP
  while cp < plmt:
    @parameter
    for n in range(64):
      alias MUL = n * BP
      var cop = cp.offset(MUL >> 6)
      cop.store(cop.load() | (1 << (MUL & 63)))
    cp += BP
  return cp

fn mkDenseFuncs[SIZE: Int]() -> UnsafePointer[DenseFunc, 0]:
  var jmptbl = UnsafePointer[DenseFunc, 0].alloc(SIZE)
  @parameter
  for i in range(SIZE):
    alias BP = (i << 1) + 3
    jmptbl[i] = denseCullFunc[BP]
  return jmptbl

@always_inline
fn cullPass(dfs: UnsafePointer[DenseFunc, 0], efs: UnsafePointer[UnrollFunc, 0],
            cmpsts: DTypePointer[DType.uint8], bytesz: Int, s: Int, bp: Int):
    if bp <= 129: # dense culling
        var sm = s
        while (sm >> 3) < bytesz and (sm & 63) != 0:
            cmpsts[sm >> 3] |= (1 << (sm & 7))
            sm += bp
        var bcp = dfs[(bp - 3) >> 1](cmpsts.bitcast[DType.uint64](), bytesz, sm)
        var ns = 0
        var ncp = bcp
        var cmpstslmtp = (cmpsts + bytesz).bitcast[DType.uint64]()
        while ncp < cmpstslmtp:
            ncp[0] |= (1 << (ns & 63))
            ns += bp
            ncp = bcp + (ns >> 6)
    else: # extreme loop unrolling culling
        efs[((s & 7) << 2) + ((bp & 7) >> 1)](cmpsts, bytesz, s, bp)
#    for c in range(s, bytesz * 8, bp): # slow bit twiddling way
#        cmpsts[c >> 3] |= (1 << (c & 7))

fn countPagePrimes(ptr: DTypePointer[DType.uint8], bitsz: Int) -> Int:
    var wordsz: Int = (bitsz + 63) // 64  # round up to nearest 64 bit boundary 
    var rslt: Int = wordsz * 64
    var bigcmps = ptr.bitcast[DType.uint64]()        
    for i in range(wordsz - 1):
       rslt -= int(pop_count(bigcmps[i]))
    rslt -= int(pop_count(bigcmps[wordsz - 1] | (-2 << ((bitsz - 1) & 63))))
    return rslt

struct SoEOdds(Sized):
    var len: Int
    var cmpsts: DTypePointer[DType.uint8] # because DynamicVector has deep copy bug in Mojo version 0.7
    var sz: Int
    var ndx: Int
    fn __init__(inout self, limit: Int):
        self.len = 0 if limit < 2 else (limit - 3) // 2 + 1
        self.sz = 0 if limit < 2 else self.len + 1 # for the unprocessed only even prime of two
        self.ndx = -1
        var bytesz = 0 if limit < 2 else ((self.len + 63) & -64) >> 3 # round up to nearest 64 bit boundary
        self.cmpsts = DTypePointer[DType.uint8].alloc(bytesz)
        memset_zero(self.cmpsts, bytesz)
        var denseFuncs : UnsafePointer[DenseFunc, 0] = mkDenseFuncs[64]()
        var extremeFuncs: UnsafePointer[UnrollFunc, 0] = mkExtremeFuncs[32]()
        for i in range(self.len):
            var s = (i + i) * (i + 3) + 3
            if s >= self.len: break
            if (self.cmpsts[i >> 3] >> (i & 7)) & 1 != 0: continue
            var bp = i + i + 3
            cullPass(denseFuncs, extremeFuncs, self.cmpsts, bytesz, s, bp)
        self.sz = countPagePrimes(self.cmpsts, self.len) + 1 # add one for only even prime of two
    fn __del__(owned self):
        self.cmpsts.free()
    fn __copyinit__(inout self, existing: Self):
        self.len = existing.len
        var bytesz = (self.len + 7) // 8
        self.cmpsts = DTypePointer[DType.uint8].alloc(bytesz)
        memcpy(self.cmpsts, existing.cmpsts, bytesz)
        self.sz = existing.sz
        self.ndx = existing.ndx
    fn __moveinit__(inout self, owned existing: Self):
        self.len = existing.len
        self.cmpsts = existing.cmpsts
        self.sz = existing.sz
        self.ndx = existing.ndx
    fn __len__(self: Self) -> Int: return self.sz
    fn __iter__(self: Self) -> Self: return self
    @always_inline
    fn __next__(inout self: Self) -> Int:
        if self.ndx < 0:
            self.ndx = 0; self.sz -= 1; return 2
        while (self.ndx < self.len) and ((self.cmpsts[self.ndx >> 3] >> (self.ndx & 7)) & 1 != 0):
            self.ndx += 1
        var rslt = (self.ndx << 1) + 3; self.sz -= 1; self.ndx += 1; return rslt

fn main():
    print("The primes to 100 are:")
    for prm in SoEOdds(100): print(prm, " ", end="")
    print()
    var strt0 = now()
    var answr0 = len(SoEOdds(1_000_000))
    var elpsd0 = (now() - strt0) / 1000000
    print("Found", answr0, "primes up to 1,000,000 in", elpsd0, "milliseconds.")
    var strt1 = now()
    var answr1 = len(SoEOdds(cLIMIT))
    var elpsd1 = (now() - strt1) / 1000000
    print("Found", answr1, "primes up to", cLIMIT, "in", elpsd1, "milliseconds.")
```

**Output:**

```
The primes to 100 are:
2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97  
Found 78498 primes up to 1,000,000 in 0.085067000000000004 milliseconds.
Found 50847534 primes up to 1000000000 in 1204.866606 milliseconds.
```

This was run on the same computer as the above example; notice that while this is much faster than that version, it is still very slow as the sieving range gets large such that the relative processing time for a range that is 1000 times as large is about ten times slower than as might be expected by simple scaling. This is due to the "one huge sieving buffer" algorithm that gets very large with increasing range (and in fact will eventually limit the sieving range that can be used) to exceed the size of CPU cache buffers and thus greatly slow average memory access times.

### Page-Segmented Odds-Only with Optimizations

While the above version performs reasonably well for small sieving ranges that fit within the CPU caches of a few tens of millions, as one can see it gets much slower with larger ranges and as well its huge RAM memory consumption limits the maximum range over which it can be used. This version solves these problems be breaking the huge sieving array into "pages" that each fit within the CPU cache size and processing each "page" sequentially until the target range is reached. This technique also greatly reduces memory requirements to only that required to store the base prime value representations up to the square root of the range limit (about O(n/log n) storage plus a fixed size page buffer. In this case, the storage for the base primes has been reduced by a constant factor by storing them as single byte deltas from the previous value, which works for ranges up to the 64-bit number range where the biggest gap is two times 192 and since we store only for odd base primes, the gap values are all half values to fit in a single byte.

Currently, Mojo has problems with some functions in the standard libraries such as the integer square root function is not accurate nor does it work for the required integer types so a custom integer square root function is supplied. As well, current Mojo does not support recursion for hardly any useful cases (other than compile time global function recursion), so the `SoEOdds` structure from the previous answer had to be kept to generate the base prime representation table (or this would have had to be generated from scratch within the new `SoEOddsPaged` structure). Finally, it didn't seem to be worth using the `Sized` trait for the new structure as this would seem to sometimes require processing the pages twice, one to obtain the size and once if iteration across the prime values is required.

Tested with Mojo version 25.6.1:

```mw
from memory import (memset_zero, memcpy)
from bit import pop_count
from time import monotonic

alias cLIMIT: Int = 1_000_000_000

alias cBufferSize: Int = 262144 # bytes
alias cBufferBits: Int = cBufferSize * 8

fn Intsqrt(n: UInt64) -> UInt64:
  if n < 4:
    if n < 1: return 0 else: return 1
  var x: UInt64 = n; var qn: UInt64 = 0; var r: UInt64 = 0
  while qn < 64 and (1 << qn) <= n:
    qn += 2
  var q: UInt64 = 1 << qn
  while q > 1:
    if qn >= 64:
      q = 1 << (qn - 2); qn = 0
    else:
      q >>= 2
    var t: UInt64 =  r + q
    r >>= 1
    if x >= t:
      x -= t; r += q
  return r

alias UnrollFunc = fn(UnsafePointer[UInt8], Int64, Int64, Int64) -> None

@always_inline
fn extreme[OFST: Int64, BP: Int64](pcmps: UnsafePointer[UInt8], bufsz: Int64, s: Int64, bp: Int64):
  var cp = pcmps + (s >> 3)
  var r1: Int64 = ((s + bp) >> 3) - (s >> 3)
  var r2: Int64 = ((s + 2 * bp) >> 3) - (s >> 3)
  var r3: Int64 = ((s + 3 * bp) >> 3) - (s >> 3)
  var r4: Int64 = ((s + 4 * bp) >> 3) - (s >> 3)
  var r5: Int64 = ((s + 5 * bp) >> 3) - (s >> 3)
  var r6: Int64 = ((s + 6 * bp) >> 3) - (s >> 3)
  var r7: Int64 = ((s + 7 * bp) >> 3) - (s >> 3)
  var plmt: UnsafePointer[UInt8] = pcmps + bufsz - r7
  while cp < plmt:
    cp[] |= UInt8(1 << OFST)
    cp[r1] |= UInt8(1 << ((OFST + BP) & 7))
    cp[r2] |= UInt8(1 << ((OFST + 2 * BP) & 7))
    cp[r3] |= UInt8(1 << ((OFST + 3 * BP) & 7))
    cp[r4] |= UInt8(1 << ((OFST + 4 * BP) & 7))
    cp[r5] |= UInt8(1 << ((OFST + 5 * BP) & 7))
    cp[r6] |= UInt8(1 << ((OFST + 6 * BP) & 7))
    cp[r7] |= UInt8(1 << ((OFST + 7 * BP) & 7))
    cp += bp
  var eplmt: UnsafePointer[UInt8] = plmt + r7
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << OFST)
  cp += r1
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + BP) & 7))
  cp += r2 - r1
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + 2 * BP) & 7))
  cp += r3 - r2
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + 3 * BP) & 7))
  cp += r4 - r3
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + 4 * BP) & 7))
  cp += r5 - r4
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + 5 * BP) & 7))
  cp += r6 - r5
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + 6 * BP) & 7))
  cp += r7 - r6
  if eplmt == cp or eplmt < cp: return
  cp[] |= UInt8(1 << ((OFST + 7 * BP) & 7))
 
fn mkExtremeFuncs[SIZE: Int64]() -> UnsafePointer[UnrollFunc]:
  var jmptbl = UnsafePointer[UnrollFunc].alloc(Int(SIZE))
  @parameter
  for i in range(SIZE):
    alias OFST = i >> 2
    alias BP = ((i & 3) << 1) + 1
    jmptbl[i] = extreme[OFST, BP]
  return jmptbl
  
alias DenseFunc = fn(UnsafePointer[UInt64], Int64, Int64) -> UnsafePointer[UInt64]

@always_inline
fn denseCullFunc[BP: Int](pcmps: UnsafePointer[UInt64], bufsz: Int64, s: Int64) -> UnsafePointer[UInt64]:
  var cp: UnsafePointer[UInt64] = pcmps + (s >> 6)
  var plmt = pcmps + (bufsz >> 3) - BP
  while cp < plmt:
    @parameter
    for n in range(64):
      alias MUL = n * BP
      var cop = cp.offset(MUL >> 6)
      cop.store(cop.load() | (1 << (MUL & 63)))
    cp += BP
  return cp

fn mkDenseFuncs[SIZE: Int64]() -> UnsafePointer[DenseFunc]:
  var jmptbl = UnsafePointer[DenseFunc].alloc(Int(SIZE))
  @parameter
  for i in range(SIZE):
    alias BP = (i << 1) + 3
    jmptbl[i] = denseCullFunc[Int(BP)]
  return jmptbl

@always_inline
fn cullPass(dfs: UnsafePointer[DenseFunc], efs: UnsafePointer[UnrollFunc],
            cmpsts: UnsafePointer[UInt8], bytesz: Int64, s: Int64, bp: Int64):
    if bp <= 129: # dense culling
        var sm = s
        while (sm >> 3) < bytesz and (sm & 63) != 0:
            cmpsts[sm >> 3] |= UInt8(1 << (sm & 7))
            sm += bp
        var bcp = dfs[(bp - 3) >> 1](cmpsts.bitcast[UInt64](), bytesz, sm)
        var ns: Int64 = 0
        var ncp = bcp
        var cmpstslmtp = (cmpsts + bytesz).bitcast[UInt64]()
        while ncp < cmpstslmtp:
            ncp[0] |= UInt64(1 << (ns & 63))
            ns += bp
            ncp = bcp + (ns >> 6)
    else: # extreme loop unrolling culling
        efs[((s & 7) << 2) + ((bp & 7) >> 1)](cmpsts, bytesz, s, bp)
#    else:
#        for c in range(s, bytesz * 8, bp): # slow bit twiddling way
#            cmpsts[c >> 3] |= (1 << (c & 7))

fn cullPage(dfs: UnsafePointer[DenseFunc], efs: UnsafePointer[UnrollFunc],
            lwi: Int64, lmt: Int64, cmpsts: UnsafePointer[UInt8], bsprmrps: UnsafePointer[UInt8]):
    var bp: Int64 = 1; var ndx = 0
    while True:
        bp += Int64(bsprmrps[ndx]) << 1
        var i = (bp - 3) >> 1
        var s = (i + i) * (i + 3) + 3
        if s >= lmt: break
        if s >= lwi: s -= lwi
        else:
            s = (lwi - s) % bp
            if s: s = bp - s
        cullPass(dfs, efs, cmpsts, cBufferSize, s, bp)
        ndx += 1

fn countPagePrimes(ptr: UnsafePointer[UInt8], bitsz: Int64) -> Int64:
    var wordsz: Int64 = (bitsz + 63) // 64  # round up to nearest 64 bit boundary 
    var rslt: Int64 = wordsz * 64
    var bigcmps = ptr.bitcast[UInt64]()        
    for i in range(wordsz - 1):
       rslt -= Int64(pop_count(bigcmps[i]))
    rslt -= Int64(pop_count(bigcmps[wordsz - 1] | UInt64(-2 << ((bitsz - 1) & 63))))
    return rslt

struct SoEOdds(ImplicitlyCopyable, Movable, Sized, Iterable, Iterator):
    alias __copyinit__is_trivial = False
    alias __moveinit__is_trivial = False
    alias __del__is_trivial = False
    alias IteratorType[
          iterable_mut: Bool, //, iterable_origin: Origin[iterable_mut]
      ]: Iterator = SoEOdds
    alias Element = UInt64
    var len: Int64
    var cmpsts: UnsafePointer[UInt8] # because DynamicVector has deep copy bug in Mojo version 0.7
    var sz: Int64
    var ndx: Int64
    fn __init__(out self, limit: Int64):
        self.len = 0 if limit < 2 else (limit - 3) // 2 + 1
        self.sz = 0 if limit < 2 else self.len + 1 # for the unprocessed only even prime of two
        self.ndx = -1
        var bytesz = 0 if limit < 2 else ((self.len + 63) & -64) >> 3 # round up to nearest 64 bit boundary
        self.cmpsts = UnsafePointer[UInt8].alloc(Int(bytesz))
        memset_zero(self.cmpsts, Int(bytesz))
        var denseFuncs : UnsafePointer[DenseFunc] = mkDenseFuncs[64]()
        var extremeFuncs: UnsafePointer[UnrollFunc] = mkExtremeFuncs[32]()
        for i in range(self.len):
            var s = (i + i) * (i + 3) + 3
            if s >= self.len: break
            if (self.cmpsts[i >> 3] >> UInt8(i & 7)) & 1: continue
            var bp = i + i + 3
            cullPass(denseFuncs, extremeFuncs, self.cmpsts, bytesz, s, bp)
        self.sz = countPagePrimes(self.cmpsts, self.len) + 1 # add one for only even prime of two
    fn __del__(deinit self):
        self.cmpsts.free()
    fn __copyinit__(out self, existing: Self):
        self.len = existing.len
        var bytesz = (self.len + 7) // 8
        self.cmpsts = UnsafePointer[UInt8].alloc(Int(bytesz))
        memcpy(self.cmpsts, existing.cmpsts, Int(bytesz))
        self.sz = existing.sz
        self.ndx = existing.ndx
    fn __moveinit__(out self, deinit existing: Self):
        self.len = existing.len
        self.cmpsts = existing.cmpsts
        self.sz = existing.sz
        self.ndx = existing.ndx
    fn __len__(self: Self) -> Int: return Int(self.sz)
    fn __iter__(ref self: Self) -> Self: return self
    @always_inline
    fn __has_next__(self: Self) -> Bool:
      return self.sz > 0
    @always_inline
    fn __next__(mut self: Self) -> Self.Element:
        if self.ndx < 0:
            self.ndx = 0; self.sz -= 1; return 2
        while (self.ndx < self.len) and ((self.cmpsts[self.ndx >> 3] >> UInt8(self.ndx & 7)) & 1):
            self.ndx += 1
        var rslt = (UInt64(self.ndx) << 1) + 3; self.sz -= 1; self.ndx += 1; return rslt

struct SoEOddsPaged(ImplicitlyCopyable, Movable, Iterable, Iterator):
    alias __copyinit__is_trivial = False
    alias __moveinit__is_trivial = False
    alias __del__is_trivial = False
    alias IteratorType[
          iterable_mut: Bool, //, iterable_origin: Origin[iterable_mut]
      ]: Iterator = SoEOddsPaged
    alias Element = UInt64
    var denseFuncs : UnsafePointer[DenseFunc]
    var extremeFuncs: UnsafePointer[UnrollFunc]
    var len: Int64
    var cmpsts: UnsafePointer[UInt8] # because DynamicVector has deep copy bug in Mojo version 0.7
    var sz: Int64 # 0 means finished; otherwise contains number of odd base primes
    var ndx: Int64
    var lwi: Int64
    var bsprmrps: UnsafePointer[UInt8] # contains deltas between odd base primes starting from zero
    fn __init__(out self, limit: UInt64):
        self.denseFuncs = mkDenseFuncs[64]()
        self.extremeFuncs = mkExtremeFuncs[32]()
        self.len = 0 if limit < 2 else Int(((limit - 3) // 2 + 1))
        self.sz = 0 if limit < 2 else 1 # means iterate until this is set to zero
        self.ndx = -1 # for unprocessed only even prime of two
        self.lwi = 0
        if self.len < cBufferBits:
            var bytesz = ((self.len + 63) & -64) >> 3 # round up to nearest 64 bit boundary
            self.cmpsts = UnsafePointer[UInt8].alloc(Int(bytesz))
            self.bsprmrps = UnsafePointer[UInt8].alloc(Int(self.sz))
        else:
            self.cmpsts = UnsafePointer[UInt8].alloc(Int(cBufferSize))
            var bsprmitr = SoEOdds(Int(Intsqrt(limit)))
            self.sz = len(bsprmitr)
            self.bsprmrps = UnsafePointer[UInt8].alloc(Int(self.sz))
            var ndx = -1; var oldbp: UInt64 = 1
            for bsprm in bsprmitr:
                if ndx < 0: ndx += 1; continue # skip over the 2 prime
                self.bsprmrps[ndx] = UInt8(bsprm - oldbp) >> 1
                oldbp = bsprm; ndx += 1
            self.bsprmrps[ndx] = 255 # one extra value to go beyond the necessary cull space
    fn __del__(deinit self):
        self.cmpsts.free(); self.bsprmrps.free()
    fn __copyinit__(out self, existing: Self):
        self.denseFuncs = existing.denseFuncs
        self.extremeFuncs = existing.extremeFuncs
        self.len = existing.len
        self.sz = existing.sz
        var bytesz = cBufferSize if self.len >= cBufferBits
                     else ((self.len + 63) & -64) >> 3 # round up to nearest 64 bit boundary
        self.cmpsts = UnsafePointer[UInt8].alloc(Int(bytesz))
        memcpy(self.cmpsts, existing.cmpsts, Int(bytesz))
        self.ndx = existing.ndx
        self.lwi = existing.lwi
        self.bsprmrps = UnsafePointer[UInt8].alloc(Int(self.sz))
        memcpy(self.bsprmrps, existing.bsprmrps, Int(self.sz))
    fn __moveinit__(out self, deinit existing: Self):
        self.denseFuncs = existing.denseFuncs
        self.extremeFuncs = existing.extremeFuncs
        self.len = existing.len
        self.cmpsts = existing.cmpsts
        self.sz = existing.sz
        self.ndx = existing.ndx
        self.lwi = existing.lwi
        self.bsprmrps = existing.bsprmrps
    fn countPrimes(self) -> Int64:
        if self.len <= cBufferBits: return len(SoEOdds(2 * self.len + 1))
        var cnt: Int64 = 1; var lwi: Int64 = 0
        var cmpsts = UnsafePointer[UInt8].alloc(Int(cBufferSize))
        memset_zero(cmpsts, Int(cBufferSize))
        cullPage(self.denseFuncs, self.extremeFuncs, 0, cBufferBits, cmpsts, self.bsprmrps)
        while lwi + cBufferBits <= self.len:
            cnt += countPagePrimes(cmpsts, cBufferBits)
            lwi += cBufferBits
            memset_zero(cmpsts, Int(cBufferSize))
            var lmt = lwi + cBufferBits if lwi + cBufferBits <= self.len else self.len
            cullPage(self.denseFuncs, self.extremeFuncs, lwi, lmt, cmpsts, self.bsprmrps)
        cnt += countPagePrimes(cmpsts, self.len - lwi)
        return cnt
    fn __len__(self: Self) -> Int: return Int(self.sz)
    fn __iter__(ref self: Self) -> Self: return self
    @always_inline
    fn __has_next__(self: Self) -> Bool:
      return self.sz > 0
    fn __next__(mut self: Self) -> Self.Element: # don't count number of primes by Interating - slooow
        if self.ndx < 0:
            self.ndx = 0; self.lwi = 0
            if self.len < 2: self.sz = 0
            elif self.len <= cBufferBits:
                var bytesz = ((self.len + 63) & -64) >> 3 # round up to nearest 64 bit boundary
                memset_zero(self.cmpsts, Int(bytesz))
                for i in range(self.len):
                    var s = (i + i) * (i + 3) + 3
                    if s >= self.len: break
                    if (self.cmpsts[i >> 3] >> UInt8(i & 7)) & 1: continue
                    var bp = i + i + 3
                    cullPass(self.denseFuncs, self.extremeFuncs, self.cmpsts, bytesz, s, bp)
            else:
                memset_zero(self.cmpsts, Int(cBufferSize))
                cullPage(self.denseFuncs, self.extremeFuncs, 0, cBufferBits, self.cmpsts, self.bsprmrps)
            return 2
        var rslt = (UInt64(self.lwi + self.ndx) << 1) + 3; self.ndx += 1
        if self.lwi + cBufferBits >= self.len:
            while (self.lwi + self.ndx < self.len) and ((self.cmpsts[self.ndx >> 3] >> UInt8(self.ndx & 7)) & 1):
                self.ndx += 1
        else:
            while (self.ndx < cBufferBits) and ((self.cmpsts[self.ndx >> 3] >> UInt8(self.ndx & 7)) & 1):
                self.ndx += 1
            while (self.ndx >= cBufferBits) and (self.lwi + cBufferBits <= self.len):
                self.ndx = 0; self.lwi += cBufferBits; memset_zero(self.cmpsts, Int(cBufferSize))
                var lmt = self.lwi + cBufferBits if self.lwi + cBufferBits <= self.len else self.len
                cullPage(self.denseFuncs, self.extremeFuncs, self.lwi, lmt, self.cmpsts, self.bsprmrps)
                var buflmt = cBufferBits if self.lwi + cBufferBits <= self.len else self.len - self.lwi
                while (self.ndx < buflmt) and ((self.cmpsts[self.ndx >> 3] >> UInt8(self.ndx & 7)) & 1):
                    self.ndx += 1
        if self.lwi + self.ndx >= self.len: self.sz = 0
        return rslt

fn main():
    print("The primes to 100 are:")
    for prm in SoEOddsPaged(100): print(prm, " ", end="")
    print()
    var strt0 = monotonic()
    var answr0 = SoEOddsPaged(1_000_000).countPrimes()
    var elpsd0 = (monotonic() - strt0) / 1000000
    print("Found", answr0, "primes up to 1,000,000 in", elpsd0, "milliseconds.")
    var strt1 = monotonic()
    var answr1 = SoEOddsPaged(cLIMIT).countPrimes()
    var elpsd1 = (monotonic() - strt1) / 1000000
    print("Found", answr1, "primes up to", cLIMIT, "in", elpsd1, "milliseconds.")
```

**Output:**

```
The primes to 100 are:
2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97  
Found 78498 primes up to 1,000,000 in 0.084122000000000002 milliseconds.
Found 50847534 primes up to 1000000000 in 139.509275 milliseconds.
```

This was tested on the same computer as the previous Mojo versions. Note that the time now scales quite well with range since there are no longer the huge RAM access time bottleneck's. This version is only about 2.25 times slower than Kim Walich's primesieve program written in C++ when run single-threaded and the mostly constant factor difference will be made up if one adds wheel factorization to the same level as he uses (basic wheel factorization ratio of 48/105 plus some other more minor optimizations). This version can count the number of primes to 100 million in about 21.85 seconds on this machine. It will work reasonably efficiently up to a range of about 1e14 before other optimization techniques such as "bucket sieving" should be used.

For counting the number of primes to a billion (1e9), this version has reduced the time by about a factor of 40 from the original version and over eight times from the odds-only version above. Adding wheel factorization will make it almost two and a half times faster yet for a gain in speed of about a hundred times over the original version.


## MUMPS

```mw
ERATO1(HI)
 ;performs the Sieve of Erotosethenes up to the number passed in.
 ;This version sets an array containing the primes
 SET HI=HI\1
 KILL ERATO1 ;Don't make it new - we want it to remain after we quit the function
 NEW I,J,P
 FOR I=2:1:(HI**.5)\1 FOR J=I*I:I:HI SET P(J)=1
 FOR I=2:1:HI S:'$DATA(P(I)) ERATO1(I)=I
 KILL I,J,P
 QUIT
```

Example:

```
USER>SET MAX=100,C=0 DO ERATO1^ROSETTA(MAX) 
USER>WRITE !,"PRIMES BETWEEN 1 AND ",MAX,! FOR  SET I=$ORDER(ERATO1(I)) Q:+I<1  WRITE I,", "

PRIMES BETWEEN 1 AND 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79, 83, 89, 97,
```


## Neko

```mw
/* The Computer Language Shootout
   http://shootout.alioth.debian.org/

   contributed by Nicolas Cannasse
*/
fmt = function(i) {
        var s = $string(i);
        while( $ssize(s) < 8 )
                s = " "+s;
        return s;
}
nsieve = function(m) {
        var a = $amake(m);
        var count = 0;
        var i = 2;
        while( i < m ) {
                if $not(a[i]) {
                        count += 1;
                        var j = (i << 1);
                        while( j < m ) {
                                if( $not(a[j]) ) a[j] = true;
                                j += i;
                        }
                }
                i += 1;
        }
        $print("Primes up to ",fmt(m)," ",fmt(count),"\n");
}

var n = $int($loader.args[0]);
if( n == null ) n = 2;
var i = 0;
while( i < 3 ) {
        nsieve(10000 << (n - i));
        i += 1;
}
```

**Output:**

```
prompt$ nekoc nsieve.neko
prompt$ time -p neko nsieve.n
Primes up to    40000     4203
Primes up to    20000     2262
Primes up to    10000     1229
real 0.02
user 0.01
sys 0.00
```


## NetRexx

### Version 1 (slow)

```mw
/* NetRexx */

options replace format comments java crossref savelog symbols binary

parse arg loWatermark hiWatermark .
if loWatermark = '' | loWatermark = '.' then loWatermark = 1
if hiWatermark = '' | hiWatermark = '.' then hiWatermark = 200

do
  if \loWatermark.datatype('w') | \hiWatermark.datatype('w') then -
    signal NumberFormatException('arguments must be whole numbers')
  if loWatermark > hiWatermark then -
    signal IllegalArgumentException('the start value must be less than the end value')

  seive = sieveOfEratosthenes(hiWatermark)
  primes = getPrimes(seive, loWatermark, hiWatermark).strip

  say 'List of prime numbers from' loWatermark 'to' hiWatermark 'via a "Sieve of Eratosthenes" algorithm:'
  say '  'primes.changestr(' ', ',')
  say '  Count of primes:' primes.words
catch ex = Exception
  ex.printStackTrace
end

return

method sieveOfEratosthenes(hn = long) public static binary returns Rexx

  sv = Rexx(isTrue)
  sv[1] = isFalse
  ix = long
  jx = long

  loop ix = 2 while ix * ix <= hn
    if sv[ix] then loop jx = ix * ix by ix while jx <= hn
      sv[jx] = isFalse
      end jx
    end ix

  return sv

method getPrimes(seive = Rexx, lo = long, hi = long) private constant binary returns Rexx

  primes = Rexx('')
  loop p_ = lo to hi
    if \seive[p_] then iterate p_
    primes = primes p_
    end p_

  return primes

method isTrue public constant binary returns boolean
  return 1 == 1

method isFalse public constant binary returns boolean
  return \isTrue
```

**Output**

```
List of prime numbers from 1 to 200 via a "Sieve of Eratosthenes" algorithm:
  2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199
  Count of primes: 46
```

### Version 2 (significantly, i.e. 10 times faster)

```mw
/* NetRexx ************************************************************
* Essential improvements:Use boolean instead of Rexx for sv
*                        and remove methods isTrue and isFalse
* 24.07.2012 Walter Pachl courtesy Kermit Kiser
**********************************************************************/

options replace format comments java crossref savelog symbols binary

parse arg loWatermark hiWatermark .
if loWatermark = '' | loWatermark = '.' then loWatermark = 1
if hiWatermark = '' | hiWatermark = '.' then hiWatermark = 200000

startdate=Date Date()
do
  if \loWatermark.datatype('w') | \hiWatermark.datatype('w') then -
    signal NumberFormatException('arguments must be whole numbers')
  if loWatermark > hiWatermark then -
    signal IllegalArgumentException(-
                 'the start value must be less than the end value')
  sieve = sieveOfEratosthenes(hiWatermark)
  primes = getPrimes(sieve, loWatermark, hiWatermark).strip
  if hiWatermark = 200 Then do
    say 'List of prime numbers from' loWatermark 'to' hiWatermark
    say '  'primes.changestr(' ', ',')
  end
catch ex = Exception
  ex.printStackTrace
end
enddate=Date Date()
Numeric Digits 20
say (enddate.getTime-startdate.getTime)/1000 'seconds elapsed'
say '  Count of primes:' primes.words

return

method sieveOfEratosthenes(hn = int) -
                                  public static binary returns boolean[]
  true  = boolean 1
  false = boolean 0
  sv = boolean[hn+1]
  sv[1] = false

  ix = int
  jx = int

  loop ix=2 to hn
    sv[ix]=true
    end ix

  loop ix = 2 while ix * ix <= hn
    if sv[ix] then loop jx = ix * ix by ix while jx <= hn
      sv[jx] = false
      end jx
    end ix

  return sv

method getPrimes(sieve = boolean[], lo = int, hi = int) -
                                    private constant binary Returns Rexx
  p_ = int
  primes = Rexx('')
  loop p_ = lo to hi
    if \sieve[p_] then iterate p_
    primes = primes p_
    end p_

  return primes
```


## newLISP

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** This version uses rem (division) testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

This version is maybe a little different because it no longer stores the primes after they've been generated and sent to the main output. Lisp has very convenient list editing, so we don't really need the Boolean flag arrays you'd tend find in the Algol-like languages. We can just throw away the multiples of each prime from an initial list of integers. The implementation is easier if we delete every multiple, including the prime number itself: the list always contains only the numbers that haven't been processed yet, starting with the next prime, and the program is finished when the list becomes empty.

Note that the lambda expression in the following script does not involve a closure; newLISP has dynamic scope, so it matters that the same variable names will not be reused for some other purpose (at runtime) before the anonymous function is called.

```mw
(set 'upper-bound 1000)

; The initial sieve is a list of all the numbers starting at 2.
(set 'sieve (sequence 2 upper-bound))

; Keep working until the list is empty.
(while sieve

   ; The first number in the list is always prime
   (set 'new-prime (sieve 0))
   (println new-prime)

   ; Filter the list leaving only the non-multiples of each number.
   (set 'sieve
      (filter
         (lambda (each-number)
            (not (zero? (% each-number new-prime))))
         sieve)))

(exit)
```

**Output:**

```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
251
257
263
269
271
277
281
283
293
307
311
313
317
331
337
347
349
353
359
367
373
379
383
389
397
401
409
419
421
431
433
439
443
449
457
461
463
467
479
487
491
499
503
509
521
523
541
547
557
563
569
571
577
587
593
599
601
607
613
617
619
631
641
643
647
653
659
661
673
677
683
691
701
709
719
727
733
739
743
751
757
761
769
773
787
797
809
811
821
823
827
829
839
853
857
859
863
877
881
883
887
907
911
919
929
937
941
947
953
967
971
977
983
991
997
```


## Nial

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** It uses rem testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

```
primes is sublist [ each (2 = sum eachright (0 = mod) [pass,count]), pass ] rest count
```

Using it

```
|primes 10
=2 3 5 7
```
