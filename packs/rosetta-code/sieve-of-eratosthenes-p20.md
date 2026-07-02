---
title: "Sieve of Eratosthenes (part 20/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 20/21
---

## Standard ML

Works with SML/NJ. This uses BitArrays which are available in SML/NJ. The algorithm is the one on wikipedia, referred to above. Limit: Memory, normally. When more than 20 petabyte of memory available, this code will have its limitation at a maximum integer around 1.44*10E17, due to the maximum list length in SMLNJ. Using two extra loops, however, bit arrays can simply be stored to disk and processed in multiple lists. With a tail recursive wrapper function as well, the upper limit will be determined by available disk space only.

```mw
val segmentedSieve =  fn N =>
(* output : list of {segment=bit segment, start=number at startposition segment} *)

let

val NSegmt= 120000000;                                                                                  (* segment size *)

val inf2i = IntInf.toInt ;
val i2inf = IntInf.fromInt ;
val isInt = fn m => m <= IntInf.fromInt (valOf Int.maxInt);

val sweep = fn (bits, step, k, up) =>                                                                   (* strike off bits up to limit *)
       (while (  !k < up  andalso 0 <= !k  ) do
             (  BitArray.clrBit( bits, !k ) ; k:= !k +  step ; ()) ) handle Overflow => ()

val rec nextPrimebit =                                                                                  (* find next 1-bit within segment *)
     fn Bits =>
     fn pos  =>
        if pos+1 >= BitArray.length Bits
     then    NONE
          else    ( if BitArray.sub ( Bits,pos) then SOME (i2inf pos) else nextPrimebit Bits (pos+1) );

val sieveEratosthenes =  fn n: int =>                                                             (* Eratosthenes sieve , up to+incl n *)

 let
  val nums= BitArray.bits(n,[] );
  val i=ref 2;
  val k=ref (!i * (!i) -1);

 in

  ( BitArray.complement nums;
    BitArray.clrBit( nums, 0 );
    while ( !k <n ) do (  if ( BitArray.sub (nums, !i - 1) ) then  sweep (nums, !i, k, n) else ();
      i:= !i+1;
      k:= !i * (!i) - 1 
    );
    [ { start= i2inf 1, segment=nums } ]                                                                              
  )

 end;

val sieveThroughSegment =

 fn ( primes : { segment:BitArray.array, start:IntInf.int } list, low : IntInf.int, up ) =>
                                                                                                        (* second segment and on *)
 let
  val n      = inf2i (up-low+1)
  val nums   = BitArray.bits(n,[] ); 
  val itdone = low div i2inf NSegmt

  val rec oldprimes = fn c =>  fn                                                                 (* use segment B to sweep current one *)
                 []                       => ()
      | ctlist as {start=st,segment=B}::t =>
       let
       
        val nxt  = nextPrimebit B c ;
        val p    = st +  Option.getOpt( nxt,~10)  
        val modp = ( i2inf NSegmt * itdone ) mod p
        val i    = inf2i ( if( isInt( p - modp ) ) then p - modp else 0 )                               (* i = 0 breaks off *)
        val k    = ref   ( if Option.isSome nxt  then  (i - 1)  else ~2 )
        val step = if (isInt(p)) then inf2i(p) else valOf Int.maxInt                                    (* !k+maxInt > n *)

       in
       
          ( sweep (nums, step, k, n) ;
       if ( p*p <= up  andalso  Option.isSome nxt )
          then    oldprimes ( inf2i (p-st+1) ) ctlist
          else    oldprimes 0 t                                                                    (* next segment B *)
          ) 

       end

 in
  (  BitArray.complement nums;
     oldprimes 0 primes;
     rev ( {start = low, segment = nums } :: rev (primes) )
  )
 end;

val rec workSegmentsDown = fn firstFn =>
               fn nextFns =>
            fn sizeSeg : int =>
            fn upLimit : IntInf.int =>
 let
   val residual = upLimit mod i2inf sizeSeg
 in

   if ( upLimit <= i2inf sizeSeg ) then firstFn (  inf2i upLimit )
   else
     if ( residual > 0 ) then
           nextFns ( workSegmentsDown firstFn nextFns sizeSeg (upLimit - residual ),     upLimit - residual      + 1, upLimit )
     else
           nextFns ( workSegmentsDown firstFn nextFns sizeSeg (upLimit - i2inf sizeSeg), upLimit - i2inf sizeSeg + 1, upLimit ) 
 end;

in

  workSegmentsDown  sieveEratosthenes  sieveThroughSegment  NSegmt  N

end;
```

Example, segment size 120 million, prime numbers up to 2.5 billion:

```mw
-val writeSegment = fn  L : {segment:BitArray.array, start:IntInf.int} list =>   fn NthSegment =>
         let
              val M=List.nth (L , NthSegment - 1 )
         in
              List.map (fn x=> x + #start M)  (map IntInf.fromInt (BitArray.getBits ( #segment M)) ) 
         end;
- val primesInBits = segmentedSieve 2500000000 ;
val primesInBits =
  [{segment=-,start=1},{segment=-,start=120000001},
   {segment=-,start=240000001},{segment=-,start=360000001},
   {segment=-,start=480000001},..  <skipped> ,...]
  : {segment:BitArray.array, start:IntInf.int} list
- writeSegment primesInBits 21 ;
val it =
  [2400000011,2400000017,2400000023,2400000047,2400000061,2400000073,
   2400000091,2400000103,2400000121,2400000133,2400000137,2400000157,...]
  : IntInf.int list
- writeSegment primesInBits 1 ;
val it = [2,3,5,7,11,13,17,19,23,29,31,37,...] : IntInf.int list
```


## Stata

A program to create a dataset with a variable p containing primes up to a given number.

```mw
prog def sieve
   args n
   clear
   qui set obs `n'
   gen long p=_n
   gen byte a=_n>1
   forv i=2/`n' {
      if a[`i'] {
         loc j=`i'*`i'
         if `j'>`n' {
            continue, break
         }
         forv k=`j'(`i')`n' {
            qui replace a=0 in `k'
         }
      }
   }
   qui keep if a
   drop a
end
```

Example call

```mw
sieve 100
list in 1/10 // show only the first ten primes

     +----+
     |  p |
     |----|
  1. |  2 |
  2. |  3 |
  3. |  5 |
  4. |  7 |
  5. | 11 |
     |----|
  6. | 13 |
  7. | 17 |
  8. | 19 |
  9. | 23 |
 10. | 29 |
     +----+
```

### Mata

```mw
mata
real colvector sieve(real scalar n) {
   real colvector a
   real scalar i, j
   if (n < 2) return(J(0, 1, .))
   a = J(n, 1, 1)
   a[1] = 0
   for (i = 1; i <= n; i++) {
      if (a[i]) {
         j = i*i
         if (j > n) return(select(1::n, a))
         for (; j <= n; j = j+i) a[j] = 0
      }
   }
}

sieve(10)
       1
    +-----+
  1 |  2  |
  2 |  3  |
  3 |  5  |
  4 |  7  |
    +-----+
end
```


## Swift

```mw
import Foundation // for sqrt() and Date()

let max = 1_000_000
let maxroot = Int(sqrt(Double(max)))
let startingPoint = Date()

var isprime = [Bool](repeating: true, count: max+1 )
for i in 2...maxroot {
    if isprime[i] {
        for k in stride(from: max/i, through: i, by: -1) {
            if isprime[k] {
                isprime[i*k] = false }
        }
    }
}

var count = 0
for i in 2...max {
    if isprime[i] {
        count += 1
    }
}
print("\(count) primes found under \(max)")

print("\(startingPoint.timeIntervalSinceNow * -1) seconds")
```

**Output:**

```
78498 primes found under 1000000
0.01282501220703125 seconds
```

iMac 3,2 GHz Intel Core i5

**Alternative odds-only version**

The most obvious two improvements are to sieve for only odds as two is the only even prime and to make the sieving array bit-packed so that instead of a whole 8-bit byte per number representation there, each is represented by just one bit; these two changes improved memory use by a factor of 16 and the better CPU cache locality more than compensates for the extra code required to implement bit packing as per the following code:

```mw
func soePackedOdds(_ n: Int) ->
    LazyMapSequence<UnfoldSequence<Int, (Int?, Bool)>, Int> {
 
  let lmti = (n - 3) / 2
  let size = lmti / 8 + 1
  var sieve = Array<UInt8>(repeating: 0, count: size)
  let sqrtlmti = (Int(sqrt(Double(n))) - 3) / 2
 
  for i in 0...sqrtlmti {
    if sieve[i >> 3] & (1 << (i & 7)) == 0 {
      let p = i + i + 3
      for c in stride(from: (i*(i+3)<<1)+3, through: lmti, by: p) {
        sieve[c >> 3] |= 1 << (c & 7)
      }
    }
  }

  return sequence(first: -1, next: { (i:Int) -> Int? in
      var ni = i + 1
      while ni <= lmti && sieve[ni >> 3] & (1 << (ni & 7)) != 0 { ni += 1}
      return ni > lmti ? nil : ni
    }).lazy.map { $0 < 0 ? 2 : $0 + $0 + 3 }
}
```

the output for the same testing (with `soePackedOdds` substituted for `primes`) is the same except that it is about 1.5 times faster or only 1200 cycles per prime.

These "one huge sieving array" algorithms are never going to be very fast for extended ranges (past about the CPU L2 cache size for this processor supporting a range of about eight million), and a page segmented approach should be taken as per the last of the unbounded algorithms below.

### Unbounded (Odds-Only) Versions

To use Swift's "higher order functions" on the generated `Sequence`'s effectively, one needs unbounded (or only by the numeric range chosen for the implementation) sieves. Many of these are incremental sieves that, instead of buffering a series of culled arrays, records the culling structure of the culling base primes (which should be a secondary stream of primes for efficiency) and produces the primes incrementally through reference and update of that structure. Various structures may be chosen for this, as in a MinHeap Priority Queue, a Hash Dictionary, or a simple List tree structure as used in the following code:

```mw
import Foundation

func soeTreeFoldingOdds() -> UnfoldSequence<Int, (Int?, Bool)> {
  class CIS<T> {
    let head: T
    let rest: (() -> CIS<T>)
    init(_ hd: T, _ rst: @escaping (() -> CIS<T>)) {
      self.head = hd; self.rest = rst
    }
  }

  func merge(_ xs: CIS<Int>, _ ys: CIS<Int>) -> CIS<Int> {
    let x = xs.head; let y = ys.head
    if x < y { return CIS(x, {() in merge(xs.rest(), ys) }) }
    else { if y < x { return CIS(y, {() in merge(xs, ys.rest()) }) }
    else { return CIS(x, {() in merge(xs.rest(), ys.rest()) }) } }
  }

  func smults(_ p: Int) -> CIS<Int> {
    let inc = p + p
    func smlts(_ c: Int) -> CIS<Int> {
      return CIS(c, { () in smlts(c + inc) })
    }
    return smlts(p * p)
  }

  func allmults(_ ps: CIS<Int>) -> CIS<CIS<Int>> {
    return CIS(smults(ps.head), { () in allmults(ps.rest()) })
  }

  func pairs(_ css: CIS<CIS<Int>>) -> CIS<CIS<Int>> {
    let cs0 = css.head; let ncss = css.rest()
    return CIS(merge(cs0, ncss.head), { () in pairs(ncss.rest()) })
  }

  func cmpsts(_ css: CIS<CIS<Int>>) -> CIS<Int> {
    let cs0 = css.head
    return CIS(cs0.head, { () in merge(cs0.rest(), cmpsts(pairs(css.rest()))) })
  }

  func minusAt(_ n: Int, _ cs: CIS<Int>) -> CIS<Int> {
    var nn = n; var ncs = cs
    while nn >= ncs.head { nn += 2; ncs = ncs.rest() }
    return CIS(nn, { () in minusAt(nn + 2, ncs) })
  }

  func oddprms() -> CIS<Int> {
    return CIS(3, { () in minusAt(5, cmpsts(allmults(oddprms()))) })
  }

  var odds = oddprms()
  return sequence(first: 2, next: { _ in
    let p = odds.head; odds = odds.rest()
    return p
  })
}

let range = 100000000

print("The primes up to 100 are:")
soeTreeFoldingOdds().prefix(while: { $0 <= 100 })
  .forEach { print($0, "", terminator: "") }
print()

print("Found \(soeTreeFoldingOdds().lazy.prefix(while: { $0 <= 1000000 })
                .reduce(0) { (a, _) in a + 1 }) primes to 1000000.")

let start = NSDate()
let answr = soeTreeFoldingOdds().prefix(while: { $0 <= range })
              .reduce(0) { (a, _) in a + 1 }
let elpsd = -start.timeIntervalSinceNow

print("Found \(answr) primes to \(range).")

print(String(format: "This test took %.3f milliseconds.", elpsd * 1000))
```

The output is the same as for the above except that it is much slower at about 56,000 CPU clock cycles per prime even just sieving to ten million due to the many memory allocations/de-allocations. It also has a O(n (log n) (log (log n))) asymptotic computational complexity (with the extra "log n" factor) that makes it slower with increasing range. This makes this algorithm only useful up to ranges of a few million although it is adequate to solve trivial problems such as Euler Problem 10 of summing all the primes to two million.

Note that the above code is almost a pure functional version using immutability other than for the use of loops because Swift doesn't support Tail Call Optimization (TCO) in function recursion: the loops do what TCO usually automatically does "under the covers".

**Alternative version using a (mutable) Hash Dictionary**

As the above code is slow due to memory allocations/de-allocations and the inherent extra "log n" term in the complexity, the following code uses a Hash Dictionary which has an average of O(1) access time (without the "log n" and uses mutability for increased seed so is in no way purely functional:

```mw
func soeDictOdds() -> UnfoldSequence<Int, Int> {
  var bp = 5; var q = 25
  var bps: UnfoldSequence<Int, Int>.Iterator? = nil
  var dict = [9: 6] // Dictionary<Int, Int>(9 => 6)
  return sequence(state: 2, next: { n in
    if n < 9 { if n < 3 { n = 3; return 2 }; defer {n += 2}; return n }
    while n >= q || dict[n] != nil {
      if n >= q {
        let inc = bp + bp
        dict[n + inc] = inc
        if bps == nil {
          bps = soeDictOdds().makeIterator()
          bp = (bps?.next())!; bp = (bps?.next())!; bp = (bps?.next())! // skip 2/3/5...
        }
        bp = (bps?.next())!; q = bp * bp // guaranteed never nil
      } else {
        let inc = dict[n] ?? 0
        dict[n] = nil
        var next = n + inc
        while dict[next] != nil { next += inc }
        dict[next] = inc
      }
      n += 2
    }
    defer { n += 2 }; return n
  })
}
```

It can be substituted in the above code just by substituting the `soeDictOdds` in three places in the testing code with the same output other than it is over four times faster or about 12,500 CPU clock cycles per prime.

**Fast Bit-Packed Page-Segmented Version**

An unbounded array-based algorithm can be written that combines the excellent cache locality of the second bounded version above but is unbounded by producing a sequence of sieved bit-packed arrays that are CPU cache size as required with a secondary stream of base primes used in culling produced in the same fashion, as in the following code:

```mw
import Foundation

typealias Prime = UInt64
typealias BasePrime = UInt32
typealias SieveBuffer = [UInt8]
typealias BasePrimeArray = [UInt32]

// the lazy list decribed problems don't affect its use here as
// it is only used here for its memoization properties and not consumed...
// In fact a consumed deferred list would be better off to use a CIS as above!

// a lazy list to memoize the progression of base prime arrays...
// there is some bug in Swift 4.2 that generating a LazyList<T> with a
// function and immediately using an extension method on it without
// first storing it to a variable results in mem seg fault for large
// ranges in the order of a million; in order to write a consuming
// function, one must write a function passing in a generator thunk, and
// immediately call a `makeIterator()` on it before storing, then doing a
// iteration on the iterator; doing a for on the immediately produced
// LazyList<T> (without storing it) also works, but this means we have to
// implement the "higher order functions" ourselves.
// this bug may have something to do with "move sematics".
class LazyList<T> : LazySequenceProtocol {
  internal typealias Thunk<T> = () -> T
  let head : T
  internal var _thnk: Thunk<LazyList<T>?>?
  lazy var tail: LazyList<T>? = {
    let tl = self._thnk?(); self._thnk = nil
    return tl
  }()
  init(_ hd: T, _ thnk: @escaping Thunk<LazyList<T>?>) {
    self.head = hd; self._thnk = thnk
  }
  struct LLSeqIter : IteratorProtocol, LazySequenceProtocol {
    @usableFromInline
    internal var _isfirst: Bool = true
    @usableFromInline
    internal var _current: LazyList<T>
    @inlinable // ensure that reference is not released by weak reference
    init(_ base: LazyList<T>) { self._current = base }
    @inlinable // can't be called by multiple threads on same LLSeqIter...
    mutating func next() -> T? {
      let curll = self._current
      if (self._isfirst) { self._isfirst = false; return curll.head }
      let ncur = curll.tail
      if (ncur == nil) { return nil }
      self._current = ncur!
      return ncur!.head
    }
    @inlinable
    func makeIterator() -> LLSeqIter {
      return LLSeqIter(self._current)
    }
  }
  @inlinable
  func makeIterator() -> LLSeqIter {
    return LLSeqIter(self)
  }
}

internal func makeCLUT() -> Array<UInt8> {
  var clut = Array(repeating: UInt8(0), count: 65536)
  for i in 0..<65536 {
    let v0 = ~i & 0xFFFF
    let v1 = v0 - ((v0 & 0xAAAA) >> 1)
    let v2 = (v1 & 0x3333) + ((v1 & 0xCCCC) >> 2)
    let v3 = (((((v2 & 0x0F0F) + ((v2 & 0xF0F0) >> 4)) &* 0x0101)) >> 8) & 31
    clut[i] = UInt8(v3)
  }
  return clut
}

internal let CLUT = makeCLUT()

internal func countComposites(_ cmpsts: SieveBuffer) -> Int {
  let len = cmpsts.count >> 1
  let clutp = UnsafePointer(CLUT) // for faster un-bounds checked access
  var bufp = UnsafeRawPointer(UnsafePointer(cmpsts))
                .assumingMemoryBound(to: UInt16.self)
  let plmt = bufp + len
  var count: Int = 0
  while (bufp < plmt) {
    count += Int(clutp[Int(bufp.pointee)])
    bufp += 1
  }
  return count
}

// converts an entire sieved array of bytes into an array of UInt32 primes,
// to be used as a source of base primes...
internal func composites2BasePrimeArray(_ low: BasePrime, _ cmpsts: SieveBuffer)
                                                          -> BasePrimeArray {
  let lmti = cmpsts.count << 3
  let len = countComposites(cmpsts)
  var rslt = BasePrimeArray(repeating: BasePrime(0), count: len)
  var j = 0
  for i in 0..<lmti {
    if (cmpsts[i >> 3] & (1 << (i & 7)) == UInt8(0)) {
      rslt[j] = low + BasePrime(i + i); j += 1
    }
  }
  return rslt
}

// do sieving work based on low starting value for the given buffer and
// the given lazy list of base prime arrays...
// uses pointers to avoid bounds checking for speed, but bounds are checked in code.
// uses an improved algorithm to maximize simple culling loop speed for
// the majority of cases of smaller base primes, only reverting to normal
// bit-packing operations for larger base primes...
// NOTE: a further optimization of maximum loop unrolling can later be
// implemented when warranted after maximum wheel factorization is implemented.
internal func sieveComposites(
      _ low: Prime, _ buf: SieveBuffer,
      _ bpas: LazyList<BasePrimeArray>) {
  let lowi = Int64((low - 3) >> 1)
  let len = buf.count
  let lmti = Int64(len << 3)
  let bufp = UnsafeMutablePointer(mutating: buf)
  let plen = bufp + len
  let nxti = lowi + lmti
  for bpa in bpas {
    for bp in bpa {
      let bp64 = Int64(bp)
      let bpi64 = (bp64 - 3) >> 1
      var strti = (bpi64 * (bpi64 + 3) << 1) + 3
      if (strti >= nxti) { return }
      if (strti >= lowi) { strti -= lowi }
      else {
        let r = (lowi - strti) % bp64
        strti = r == 0 ? 0 : bp64 - r
      }
      if (bp <= UInt32(len >> 3) && strti <= (lmti - 20 * bp64)) {
        let slmti = min(lmti, strti + (bp64 << 3))
        while (strti < slmti) {
          let msk = UInt8(1 << (strti & 7))
          var cp = bufp + Int(strti >> 3)
          while (cp < plen) {
              cp.pointee |= msk; cp += Int(bp64)
          }
          strti &+= bp64
        }
      }
      else {
        var c = strti
        let nbufp = UnsafeMutableRawPointer(bufp)
                      .assumingMemoryBound(to: Int32.self)
        while (c < lmti) {
            nbufp[Int(c >> 5)] |= 1 << (c & 31)
            c &+= bp64
        }
      }
    }
  }
}

// starts the secondary base primes feed with minimum size in bits set to 4K...
// thus, for the first buffer primes up to 8293,
// the seeded primes easily cover it as 97 squared is 9409...
// following used for fast clearing of SieveBuffer of multiple base size...
internal let clrbpseg = SieveBuffer(repeating: UInt8(0), count: 512)
internal func makeBasePrimeArrays() -> LazyList<BasePrimeArray> {
  var cmpsts = SieveBuffer(repeating: UInt8(0), count: 512)
  func nextelem(_ low: BasePrime, _ bpas: LazyList<BasePrimeArray>)
                                                -> LazyList<BasePrimeArray> {
    // calculate size so that the bit span is at least as big as the
    // maximum culling prime required, rounded up to minsizebits blocks...
    let rqdsz = 2 + Int(sqrt(Double(1 + low)))
    let sz = ((rqdsz >> 12) + 1) << 9 // size in bytes, blocks of 512 bytes
    if (sz > cmpsts.count) {
      cmpsts = SieveBuffer(repeating: UInt8(0), count: sz)
    }
    // fast clearing of the SieveBuffer array?
    for i in stride(from: 0, to: cmpsts.count, by: 512) {
      cmpsts.replaceSubrange(i..<i+512, with: clrbpseg)
    }
    sieveComposites(Prime(low), cmpsts, bpas)
    let arr = composites2BasePrimeArray(low, cmpsts)
    let nxt = low + BasePrime(cmpsts.count << 4)
    return LazyList(arr, { nextelem(nxt, bpas) })
  }
  // pre-seeding breaks recursive race,
  // as only known base primes used for first page...
  let preseedarr: [BasePrime] = [
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
    , 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
  return
    LazyList(
      preseedarr,
      { nextelem(BasePrime(101), makeBasePrimeArrays()) })
}

// an iterable sequence over successive sieved buffer composite arrays,
// returning a tuple of the value represented by the lowest possible prime
// in the sieved composites array and the array itself;
// the array has a 16 Kilobytes minimum size (CPU L1 cache), but
// will grow so that the bit span is larger than the
// maximum culling base prime required, possibly making it larger than
// the L1 cache for large ranges, but still reasonably efficient using
// the L2 cache: very efficient up to about 16e9 range;
// reasonably efficient to about 2.56e14 for two Megabyte L2 cache = > 1 day...
internal let clrseg = SieveBuffer(repeating: UInt8(0), count: 16384)
func makeSievePages()
    -> UnfoldSequence<(Prime, SieveBuffer), ((Prime, SieveBuffer)?, Bool)> {
  let bpas = makeBasePrimeArrays()
  let cmpsts = SieveBuffer(repeating: UInt8(0), count: 16384)
  let low = Prime(3)
  sieveComposites(low, cmpsts, bpas)
  return sequence(first: (low, cmpsts), next: { (low, cmpsts) in
    var ncmpsts = cmpsts
    let rqdsz = 2 + Int(sqrt(Double(1 + low))) // problem with sqrt not exact past about 10^12!!!!!!!!!
    let sz = ((rqdsz >> 17) + 1) << 14 // size iin bytes, by chunks of 16384
    if (sz > ncmpsts.count) {
      ncmpsts = SieveBuffer(repeating: UInt8(0), count: sz)
    }
    // fast clearing of the SieveBuffer array?
    for i in stride(from: 0, to: ncmpsts.count, by: 16384) {
      ncmpsts.replaceSubrange(i..<i+16384, with: clrseg)
    }
    let nlow = low + Prime(ncmpsts.count << 4)
    sieveComposites(nlow, ncmpsts, bpas)
    return (nlow, ncmpsts)
  })
}

func countPrimesTo(_ range: Prime) -> Int64 {
  if (range < 3) { if (range < 2) { return Int64(0) }
                   else { return Int64(1) } }
  let rngi = Int64(range - 3) >> 1
  let clutp = UnsafePointer(CLUT) // for faster un-bounds checked access
  var count: Int64 = 1
  for sp in makeSievePages() {
    let (low, cmpsts) = sp; let lowi = Int64(low - 3) >> 1
    if ((lowi + Int64(cmpsts.count << 3)) > rngi) {
      let lsti = Int(rngi - lowi); let lstw = lsti >> 4
      let msk = UInt16(-2 << (lsti & 15))
      var bufp = UnsafeRawPointer(UnsafePointer(cmpsts))
                    .assumingMemoryBound(to: UInt16.self)
      let plmt = bufp + lstw
      while (bufp < plmt) {
        count += Int64(clutp[Int(bufp.pointee)]); bufp += 1
      }
      count += Int64(clutp[Int(bufp.pointee | msk)]);
      break;
    } else {
      count += Int64(countComposites(cmpsts))
    }
  }
  return count
}

// iterator of primes from the generated culled page segments...
struct PagedPrimesSeqIter: LazySequenceProtocol, IteratorProtocol {
  @inlinable
  init() {
    self._pgs = makeSievePages().makeIterator()
    self._cmpstsp = UnsafePointer(self._pgs.next()!.1)
  }
  @usableFromInline
  internal var _pgs: UnfoldSequence<(Prime, SieveBuffer), ((Prime, SieveBuffer)?, Bool)>
  @usableFromInline
  internal var _i = -2
  @usableFromInline
  internal var _low = Prime(3)
  @usableFromInline
  internal var _cmpstsp: UnsafePointer<UInt8>
  @usableFromInline
  internal var _lmt = 131072
  @inlinable
  mutating func next() -> Prime? {
    if self._i < -1 { self._i = -1; return Prime(2) }
    while true {
      repeat { self._i += 1 }
      while self._i < self._lmt &&
              (Int(self._cmpstsp[self._i >> 3]) & (1 << (self._i & 7))) != 0
      if self._i < self._lmt { break }
      let pg = self._pgs.next(); self._low = pg!.0
      let cmpsts = pg!.1; self._lmt = cmpsts.count << 3
      self._cmpstsp = UnsafePointer(cmpsts); self._i = -1
    }
    return self._low + Prime(self._i + self._i)
  }
  @inlinable
  func makeIterator() -> PagedPrimesSeqIter {
    return PagedPrimesSeqIter()
  }
  @inlinable
  var elements: PagedPrimesSeqIter {
    return PagedPrimesSeqIter()
  }
}
 
// sequence over primes using the above prime iterator from page iterator;
// unless doing something special with individual primes, usually unnecessary;
// better to do manipulations based on the composites bit arrays...
// takes at least as long to enumerate the primes as to sieve them...
func primesPaged() -> PagedPrimesSeqIter { return PagedPrimesSeqIter() }

let range = Prime(1000000000)

print("The first 25 primes are:")
primesPaged().prefix(25).forEach { print($0, "", terminator: "") }
print()

let start = NSDate()

let answr =
  countPrimesTo(range) // fast way, following enumeration way is slower...
//  primesPaged().prefix(while: { $0 <= range }).reduce(0, { a, _ in a + 1 })

let elpsd = -start.timeIntervalSinceNow

print("Found \(answr) primes up to \(range).")

print(String(format: "This test took %.3f milliseconds.", elpsd * 1000))
```

**Output:**

```
The first 25 primes are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
Found 50847534 primes up to 1000000000.
This test took 2004.007 milliseconds.
```

This produces similar output but is many many times times faster at about 75 CPU clock cycles per prime as used here to count the primes to a billion. If one were to produce the answer by enumeration using the commented out `primesPaged()` function, the time to enumerate the results is about the same as the time to actually do the work of culling, so the example `countPrimesTo` function that does high-speed counting of found packed bits is implemented to eliminate the enumeration. For most problems over larger ranges, this approach is recommended, and could be used for summing the primes, finding first instances of maximum prime gaps, prime pairs, triples, etc.

Further optimizations as in maximum wheel factorization (a further about five times faster), multi-threading (for a further multiple of the effective number of cores used), maximum loop unrolling (about a factor of two for smaller base primes), and other techniques for higher ranges (above 16 billion in this case) can be used with increasing code complexity, but there is little point when using prime enumeration as output: ie. one could reduce the composite number culling time to zero but it would still take about 2.8 seconds to enumerate the results over the billion range in the case of this processor.


## Tailspin

```mw
templates sieve
  def limit: $;
  @: [ 2..$limit ];
  1 -> #
  $@ !

  when <..$@::length ?($@($) * $@($) <..$limit>)> do
    templates sift
      def prime: $;
      @: $prime * $prime;
      @sieve: [ $@sieve... -> # ];
      when <..~$@> do
        $ !
      when <$@~..> do
        @: $@ + $prime;
        $ -> #
    end sift

    $@($) -> sift !
    $ + 1 -> #
end sieve

1000 -> sieve ...->  '$; ' -> !OUT::write
```

v0.5

```mw
sieve templates
  limit is $;
  @ set [ 2..$limit ];
  1 -> !#
  $@ !

  when <|..$@::length ?($@($) * $@($) matches <|..$limit>)> do
    sift sink
      prime is $;
      @ set $prime * $prime;
      @sieve set [ $@sieve... -> # ];
      when <|..~$@> do
        $ !
      when <|$@~..> do
        @ set $@ + $prime;
        $ -> #!
    end sift

    $@($) -> !sift
    $ + 1 -> !#
end sieve

1000 -> sieve ...->  '$; ' !
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997 
```

Better version using the mutability of the @-state to just update a primality flag

```mw
templates sieve
  def limit: $;
  @: [ 1..$limit -> 1 ];
  @(1): 0;
  2..$limit -> #
  $@ -> \[i](<=1> $i !\) !

  when <?($@($) <=1>)> do
    def prime2: $ * $;
    $prime2..$limit:$ -> @sieve($): 0;
end sieve

1000 -> sieve... ->  '$; ' -> !OUT::write
```

v0.5

```mw
sieve templates
  limit is $;
  @ set [ 1..$limit -> 1 ];
  @(1) set 0;
  2..$limit -> !#
  $@(.. as i; -> if <|=1> -> $i) !

  when <|?($@($) matches <|=1>)> do
    prime2 is $ * $;
    $prime2..$limit:$ -> @sieve($) set 0;
end sieve

1000 -> sieve... ->  '$; ' !
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997 
```


## Tcl

```mw
package require Tcl 8.5

proc sieve n {
    if {$n < 2} {return {}}
    
    # create a container to hold the sequence of numbers.
    # use a dictionary for its speedy access (like an associative array) 
    # and for its insertion order preservation (like a list)
    set nums [dict create]
    for {set i 2} {$i <= $n} {incr i} {
        # the actual value is never used
        dict set nums $i ""
    }
    
    set primes [list]
    while {[set nextPrime [lindex [dict keys $nums] 0]] <= sqrt($n)} {
        dict unset nums $nextPrime
        for {set i [expr {$nextPrime ** 2}]} {$i <= $n} {incr i $nextPrime} {
            dict unset nums $i
        }
        lappend primes $nextPrime
    }
    return [concat $primes [dict keys $nums]]
}

puts [sieve 100]   ;# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

Summary :/* TI-83 BASIC */


## TI-83 BASIC

```mw
Input "Limit:",N
N→Dim(L1)
For(I,2,N)
1→L1(I)
End
For(I,2,SQRT(N))
If L1(I)=1
Then
For(J,I*I,N,I)
0→L1(J)
End
End
End
For(I,2,N)
If L1(I)=1
Then
Disp i
End
End
ClrList L1
```


## UNIX Shell

### With array

Works with

:

Bourne Again SHell

Works with

:

Korn Shell

Works with

:

Zsh

```mw
function primes {
  typeset -a a
  typeset i j
  a[1]=""
  for (( i = 2; i <= $1; i++ )); do
    a[$i]=$i
  done
  for (( i = 2; i * i <= $1; i++ )); do
    if [[ ! -z ${a[$i]} ]]; then
      for (( j = i * i; j <= $1; j += i )); do
        a[$j]=""
      done
    fi
  done
  printf '%s' "${a[2]}"
  printf ' %s' ${a[*]:3}
  printf '\n'
}

primes 1000
```

**Output:**

Output is a single long line:

```
2 3 5 7 11 13 17 19 23 ... 971 977 983 991 997
```

### Using variables as fake array

Bourne Shell and Almquist Shell have no arrays. This script works with bash or dash (standard shell in Ubuntu), but uses no specifics of the shells, so it works with plain Bourne Shell as well.

Works with

:

Bourne Shell

```mw
#! /bin/sh

LIMIT=1000

# As a workaround for missing arrays, we use variables p2, p3, ...,
# p$LIMIT, to represent the primes. Values are true or false.
#   eval p$i=true     # Set value.
#   eval \$p$i        # Run command: true or false.
#
# A previous version of this script created a temporary directory and
# used files named 2, 3, ..., $LIMIT to represent the primes. We now use
# variables so that a killed script does not leave extra files. About
# performance, variables are about as slow as files.

i=2
while [ $i -le $LIMIT ]
do
    eval p$i=true               # was touch $i
    i=`expr $i + 1`
done

i=2
while
    j=`expr $i '*' $i`
    [ $j -le $LIMIT ]
do
    if eval \$p$i               # was if [ -f $i ]
    then
        while [ $j -le $LIMIT ]
        do
            eval p$j=false      # was rm -f $j
            j=`expr $j + $i`
        done
    fi
    i=`expr $i + 1`
done

# was echo `ls|sort -n`
echo `i=2
      while [ $i -le $LIMIT ]; do
          eval \\$p$i && echo $i
          i=\`expr $i + 1\`
      done`
```

### With piping

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** This version uses rem testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

Note: McIlroy misunderstood the Sieve of Eratosthenes as did many of his day including David Turner (1975); see Sieve of Eratosthenes article on Wikipedia

This is an elegant script by M. Douglas McIlroy, one of the founding fathers of UNIX.

This implementation is explained in his paper "Coroutine prime number sieve" (2014).

Works with

:

Bourne Shell

```mw
sourc() {
    seq 2 1000
}

cull() {
    while
        read p || exit
    do
        (($p % $1 != 0)) && echo $p
    done
}

sink() {
    read p || exit
    echo $p
    cull $p | sink &
}

sourc | sink
```

This version works by piping 1s and 0s through *sed*. The string of 1s and 0s represents the array of primes.

Works with

:

Bourne Shell

```mw
# Fill $1 characters with $2.
fill () {
   # This pipeline would begin
   #   head -c $1 /dev/zero | ...
   # but some systems have no head -c. Use dd.
   dd if=/dev/zero bs=$1 count=1 2>/dev/null | tr '\0' $2
}

filter () {
   # Use sed to put an 'x' after each multiple of $1, remove
   # first 'x', and mark non-primes with '0'.
   sed -e s/$2/\&x/g -e s/x// -e s/.x/0/g | {
      if expr $1 '*' $1 '<' $3 > /dev/null; then
         filter `expr $1 + 1` .$2 $3
      else
         cat
      fi
   }
}

# Generate a sequence of 1s and 0s indicating primality.
oz () {
   fill $1 1 | sed s/1/0/ | filter 2 .. $1
}

# Echo prime numbers from 2 to $1.
prime () {
   # Escape backslash inside backquotes. sed sees one backslash.
   echo `oz $1 | sed 's/./&\\
/g' | grep -n 1 | sed s/:1//`
}

prime 1000
```

### C Shell

Translation of

:

CMake

```mw
# Sieve of Eratosthenes: Echoes all prime numbers through $limit.
@ limit = 80

if ( ( $limit * $limit ) / $limit != $limit ) then
   echo limit is too large, would cause integer overflow.
   exit 1
endif

# Use $prime[2], $prime[3], ..., $prime[$limit] as array of booleans.
# Initialize values to 1 => yes it is prime.
set prime=( `repeat $limit echo 1` )

# Find and echo prime numbers.
@ i = 2
while ( $i <= $limit )
   if ( $prime[$i] ) then
      echo $i

      # For each multiple of i, set 0 => no it is not prime.
      # Optimization: start at i squared.
      @ m = $i * $i
      while ( $m <= $limit )
         set prime[$m] = 0
         @ m += $i
      end
   endif
   @ i += 1
end
```


## Ursala

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** It probably (remainder) uses rem testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

with no optimizations

```mw
#import nat

sieve = ~<{0,1}&& iota; @NttPX ~&r->lx ^/~&rhPlC remainder@rlX~|@r
```

test program:

```mw
#cast %nL

example = sieve 50
```

**Output:**

```
<2,3,5,7,11,13,17,19,23,29,31,37,41,43,47>
```


## Vala

Library:

Gee

Without any optimizations:

```mw
using Gee;

ArrayList<int> primes(int limit){
   var sieve = new ArrayList<bool>();
   var prime_list = new ArrayList<int>();
   
   for(int i = 0; i <= limit; i++){
      sieve.add(true);
   }
   
   sieve[0] = false;
   sieve[1] = false;
   
   for (int i = 2; i <= limit/2; i++){
      if (sieve[i] != false){
         for (int j = 2; i*j <= limit; j++){
            sieve[i*j] = false;
         }
      }
   }

   for (int i = 0; i < sieve.size; i++){
      if (sieve[i] != false){
         prime_list.add(i);
      }
   }
   
   return prime_list;
} // end primes

public static void main(){
   var prime_list = primes(50);
   
   foreach(var prime in prime_list)
      stdout.printf("%s ", prime.to_string());
   
   stdout.printf("\n");
}
```

{{out}

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```


## VAX Assembly

```mw
                           000F4240  0000     1 n=1000*1000
                               0000  0000     2 .entry   main,0
                            7E 7CFD  0002     3    clro  -(sp)       ;result buffer
                            5E   DD  0005     4    pushl sp       ;pointer to buffer
                            10   DD  0007     5    pushl #16         ;descriptor -> len of buffer
                                     0009     6 
                            02   DD  0009     7    pushl #2       ;1st candidate
                                     000B     8 test:
                 09 46'AF   6E   E1  000B     9    bbc   (sp), b^bits, found  ;bc - bit clear
                                     0010    10 next:
           F3 6E   000F4240 8F   F2  0010    11         aoblss  #n, (sp), test      ;+1: limit,index
                                 04  0018    12         ret
                                     0019    13 found:
                         04 AE   7F  0019    14    pushaq   4(sp)       ;-> descriptor by ref
                         04 AE   DF  001C    15    pushal   4(sp)       ;-> prime on stack by ref
              00000000'GF   02   FB  001F    16    calls #2, g^ots$cvt_l_ti   ;convert integer to string
                         04 AE   7F  0026    17    pushaq   4(sp)       ;
              00000000'GF   01   FB  0029    18    calls #1, g^lib$put_output ;show result
                                     0030    19 
                       53   6E   D0  0030    20    movl  (sp), r3
                                     0033    21 mult:
    0002 53   6E   000F4240 8F   F1  0033    22    acbl    #n, (sp), r3, set_mult   ;limit,add,index
                            D1   11  003D    23    brb   next
                                     003F    24 set_mult:            ;set bits for multiples
                 EF 46'AF   53   E2  003F    25    bbss  r3, b^bits, mult  ;branch on bit set & set
                            ED   11  0044    26    brb   mult
                                     0046    27 
                           0001E892  0046    28 bits: .blkl <n+2+31>/32
                                     E892    29 .end  main
```


## VBA

Using Excel

```mw
 Sub primes()
'BRRJPA
'Prime calculation for VBA_Excel
'p is the superior limit of the range calculation
'This example calculates from 2 to 100000 and print it
'at the collum A

p = 100000

Dim nprimes(1 To 100000) As Integer
b = Sqr(p)

For n = 2 To b

    For k = n * n To p Step n
        nprimes(k) = 1
        
    Next k
Next n

For a = 2 To p
    If nprimes(a) = 0 Then
      c = c + 1
      Range("A" & c).Value = a
        
    End If
 Next a

End Sub
```


## VBScript

To run in console mode with cscript.

```mw
    Dim sieve()
   If WScript.Arguments.Count>=1 Then
       n = WScript.Arguments(0)
   Else 
       n = 99
   End If
    ReDim sieve(n)
    For i = 1 To n
        sieve(i) = True
    Next
    For i = 2 To n
        If sieve(i) Then
            For j = i * 2 To n Step i
                sieve(j) = False
            Next
        End If
    Next
    For i = 2 To n
        If sieve(i) Then WScript.Echo i
    Next
```


## Vedit macro language

This implementation uses an edit buffer as an array for flags. After the macro has been run, you can see how the primes are located in the array. Primes are marked with 'P' and non-primes with '-'. The first character position represents number 0.

```
#10 = Get_Num("Enter number to search to: ", STATLINE)
Buf_Switch(Buf_Free)                    // Use edit buffer as flags array
Ins_Text("--")                          // 0 and 1 are not primes
Ins_Char('P', COUNT, #10-1)             // init rest of the flags to "prime"
for (#1 = 2; #1*#1 < #10; #1++) {
    Goto_Pos(#1)
    if (Cur_Char=='P') {                // this is a prime number
        for (#2 = #1*#1; #2 <= #10; #2 += #1) {
            Goto_Pos(#2)
            Ins_Char('-', OVERWRITE)
        }
    }
}
```

Sample output showing numbers in range 0 to 599.

```
--PP-P-P---P-P---P-P---P-----P-P-----P---P-P---P-----P-----P
-P-----P---P-P-----P---P-----P-------P---P-P---P-P---P------
-------P---P-----P-P---------P-P-----P-----P---P-----P-----P
-P---------P-P---P-P-----------P-----------P---P-P---P-----P
-P---------P-----P-----P-----P-P-----P---P-P---------P------
-------P---P-P---P-------------P-----P---------P-P---P-----P
-------P-----P-----P---P-----P-------P---P-------P---------P
-P---------P-P-----P---P-----P-------P---P-P---P-----------P
-------P---P-------P---P-----P-----------P-P----------------
-P-----P---------P-----P-----P-P-----P---------P-----P-----P
```


## Visual Basic

**Works with:** VB6

```mw
Sub Eratost()
    Dim sieve() As Boolean
    Dim n As Integer, i As Integer, j As Integer
    n = InputBox("limit:", n)
    ReDim sieve(n)
    For i = 1 To n
        sieve(i) = True
    Next i
    For i = 2 To n
        If sieve(i) Then
            For j = i * 2 To n Step i
                sieve(j) = False
            Next j
        End If
    Next i
    For i = 2 To n
        If sieve(i) Then Debug.Print i
    Next i
End Sub 'Eratost
```


## Visual Basic .NET

```mw
Dim n As Integer, k As Integer, limit As Integer
Console.WriteLine("Enter number to search to: ")
limit = Console.ReadLine
Dim flags(limit) As Integer
For n = 2 To Math.Sqrt(limit)
    If flags(n) = 0 Then
        For k = n * n To limit Step n
            flags(k) = 1
        Next k
    End If
Next n
 
' Display the primes
For n = 2 To limit
    If flags(n) = 0 Then
        Console.WriteLine(n)
    End If
Next n
```

### Alternate

Since the sieves are being removed only above the current iteration, the separate loop for display is unnecessary. And no **Math.Sqrt()** needed. Also, input is from command line parameter instead of Console.ReadLine(). Consolidated *If* block with *For* statement into two *Do* loops.

```mw
Module Module1
    Sub Main(args() As String)
        Dim lmt As Integer = 500, n As Integer = 2, k As Integer
        If args.Count > 0 Then Integer.TryParse(args(0), lmt)
        Dim flags(lmt + 1) As Boolean   ' non-primes are true in this array.
        Do                              ' a prime was found, 
            Console.Write($"{n} ")      ' so show it,
            For k = n * n To lmt Step n ' and eliminate any multiple of it at it's square and beyond.
                flags(k) = True
            Next
            Do                          ' skip over non-primes.
                n += If(n = 2, 1, 2)
            Loop While flags(n)
        Loop while n <= lmt
    End Sub
End Module
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 
```


## V (Vlang)

Translation of

:

go

### Basic sieve of array of booleans

```mw
fn main() {
    limit := 201 // means sieve numbers < 201
 
    // sieve
    mut c := []bool{len: limit} // c for composite.  false means prime candidate
    c[1] = true              // 1 not considered prime
    mut p := 2
    for {
        // first allowed optimization:  outer loop only goes to sqrt(limit)
        p2 := p * p
        if p2 >= limit {
            break
        }
        // second allowed optimization:  inner loop starts at sqr(p)
        for i := p2; i < limit; i += p {
            c[i] = true // it's a composite
        }
        // scan to get next prime for outer loop
        for {
            p++
            if !c[p] {
                break
            }
        }
    }
 
    // sieve complete.  now print a representation.
    for n in 1..limit {
        if c[n] {
            print("  .")
        } else {
            print("${n:3}")
        }
        if n%20 == 0 {
            println("")
        }
    }
}
```

Output:

```
  .  2  3  .  5  .  7  .  .  . 11  . 13  .  .  . 17  . 19  .
  .  . 23  .  .  .  .  . 29  . 31  .  .  .  .  . 37  .  .  .
 41  . 43  .  .  . 47  .  .  .  .  . 53  .  .  .  .  . 59  .
 61  .  .  .  .  . 67  .  .  . 71  . 73  .  .  .  .  . 79  .
  .  . 83  .  .  .  .  . 89  .  .  .  .  .  .  . 97  .  .  .
101  .103  .  .  .107  .109  .  .  .113  .  .  .  .  .  .  .
  .  .  .  .  .  .127  .  .  .131  .  .  .  .  .137  .139  .
  .  .  .  .  .  .  .  .149  .151  .  .  .  .  .157  .  .  .
  .  .163  .  .  .167  .  .  .  .  .173  .  .  .  .  .179  .
181  .  .  .  .  .  .  .  .  .191  .193  .  .  .197  .199  .
```


## Vorpal

```mw
self.print_primes = method(m){
   p = new()
   p.fill(0, m, 1, true)

   count = 0
   i = 2
   while(i < m){
      if(p[i] == true){
         p.fill(i+i, m, i, false)
         count = count + 1
      }
      i = i + 1
   }
   ('primes: ' + count + ' in ' + m).print()
   for(i = 2, i < m, i = i + 1){
      if(p[i] == true){
         ('' + i + ', ').put()
      }
   }
   ''.print()
}

self.print_primes(100)
```

**Result:**

```
primes: 25 in 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
```


## WebAssembly

```
(module
 (import "js" "print" (func $print (param i32)))
 (memory 4096)
 
 (func $sieve (export "sieve") (param $n i32)
   (local $i i32)
   (local $j i32)
 
   (set_local $i (i32.const 0))
   (block $endLoop
     (loop $loop
       (br_if $endLoop (i32.ge_s (get_local $i) (get_local $n)))
       (i32.store8 (get_local $i) (i32.const 1))
       (set_local $i (i32.add (get_local $i) (i32.const 1)))
       (br $loop)))
 
   (set_local $i (i32.const 2))
   (block $endLoop
     (loop $loop
       (br_if $endLoop (i32.ge_s (i32.mul (get_local $i) (get_local $i)) 
                                 (get_local $n)))
       (if (i32.eq (i32.load8_s (get_local $i)) (i32.const 1))
         (then
           (set_local $j (i32.mul (get_local $i) (get_local $i)))
           (block $endInnerLoop
             (loop $innerLoop
               (i32.store8 (get_local $j) (i32.const 0))
               (set_local $j (i32.add (get_local $j) (get_local $i)))
               (br_if $endInnerLoop (i32.ge_s (get_local $j) (get_local $n)))
               (br $innerLoop)))))
       (set_local $i (i32.add (get_local $i) (i32.const 1)))
       (br $loop)))
 
   (set_local $i (i32.const 2))
   (block $endLoop
     (loop $loop
       (if (i32.eq (i32.load8_s (get_local $i)) (i32.const 1))
         (then
           (call $print (get_local $i))))
       (set_local $i (i32.add (get_local $i) (i32.const 1)))
       (br_if $endLoop (i32.ge_s (get_local $i) (get_local $n)))
       (br $loop)))))
```
