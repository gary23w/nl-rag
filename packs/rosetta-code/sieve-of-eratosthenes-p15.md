---
title: "Sieve of Eratosthenes (part 15/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 15/21
---

## Nim

```mw
from math import sqrt
 
iterator primesUpto(limit: int): int =
  let sqrtLimit = int(sqrt(float64(limit)))
  var composites = newSeq[bool](limit + 1)
  for n in 2 .. sqrtLimit: # cull to square root of limit
    if not composites[n]: # if prime -> cull its composites
      for c in countup(n * n, limit, n): # start at ``n`` squared
        composites[c] = true
  for n in 2 .. limit: # separate iteration over results
    if not composites[n]:
      yield n
 
stdout.write "The primes up to 100 are:  "
for x in primesUpto(100):
   stdout.write(x, " ")
echo()
 
var count = 0
for p in primesUpto(1000000):
  count += 1
echo "There are ", count, " primes up to 1000000."
```

**Output:**

```
Primes are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
There are 78498 primes up to 1000000.
```

**Alternate odds-only bit-packed version**

The above version wastes quite a lot of memory by using a sequence of boolean values to sieve the composite numbers and sieving all numbers when two is the only even prime. The below code uses a bit-packed sequence to save a factor of eight in memory and also sieves only odd primes for another memory saving by a factor of two; it is also over two and a half times faster due to reduced number of culling operations and better use of the CPU cache as a little cache goes a lot further - this better use of cache is more than enough to make up for the extra bit-packing shifting operations:

```mw
iterator isoe_upto(top: uint): uint =
  let topndx = int((top - 3) div 2)
  let sqrtndx = (int(sqrt float64(top)) - 3) div 2
  var cmpsts = newSeq[uint32](topndx div 32 + 1)
  for i in 0 .. sqrtndx: # cull composites for primes
    if (cmpsts[i shr 5] and (1u32 shl (i and 31))) == 0:
      let p = i + i + 3
      for j in countup((p * p - 3) div 2, topndx, p):
        cmpsts[j shr 5] = cmpsts[j shr 5] or (1u32 shl (j and 31))
  yield 2 # separate culling above and iteration here
  for i in 0 .. topndx:
    if (cmpsts[i shr 5] and (1u32 shl (i and 31))) == 0:
      yield uint(i + i + 3)
```

The above code can be used with the same output functions as in the first code, just replacing the name of the iterator "iprimes_upto" with this iterator's name "isoe_upto" in two places. The output will be identical.

### Nim Unbounded Versions

For many purposes, one doesn't know the exact upper limit desired to easily use the above versions; in addition, those versions use an amount of memory proportional to the range sieved. In contrast, unbounded versions continuously update their range as they progress and only use memory proportional to the secondary base primes stream, which is only proportional to the square root of the range. One of the most basic functional versions is the TreeFolding sieve which is based on merging lazy streams as per Richard Bird's contribution to incremental sieves in Haskell, but which has a much better asymptotic execution complexity due to the added tree folding. The following code is a version of that in Nim (odds-only):

```mw
import sugar
from times import epochTime

type PrimeType = int
iterator primesTreeFolding(): PrimeType {.closure.} =
  # needs a Co Inductive Stream - CIS...
  type
    CIS[T] = ref object
      head: T
      tail: () -> CIS[T]

  proc merge(xs, ys: CIS[PrimeType]): CIS[PrimeType] =
    let x = xs.head;
    let y = ys.head
    if x < y:
      CIS[PrimeType](head: x, tail: () => merge(xs.tail(), ys))
    elif y < x:
      CIS[PrimeType](
        head: y,
        tail: () => merge(xs, ys.tail()))
    else:
      CIS[PrimeType](
        head: x,
        tail: () => merge(xs.tail(), ys.tail()))

  proc pmults(p: PrimeType): CIS[PrimeType] =
    let inc = p + p
    proc mlts(c: PrimeType): CIS[PrimeType] =
      CIS[PrimeType](head: c, tail: () => mlts(c + inc))
    mlts(p * p)

  proc allmults(ps: CIS[PrimeType]): CIS[CIS[PrimeType]] =
    CIS[CIS[PrimeType]](
      head: pmults(ps.head),
      tail: () => allmults(ps.tail()))

  proc pairs(css: CIS[CIS[PrimeType]]): CIS[CIS[PrimeType]] =
    let cs0 = css.head;
    let rest0 = css.tail()
    CIS[CIS[PrimeType]](
      head: merge(cs0, rest0.head),
      tail: () => pairs(rest0.tail()))

  proc cmpsts(css: CIS[CIS[PrimeType]]): CIS[PrimeType] =
    let cs0 = css.head
    CIS[PrimeType](
      head: cs0.head,
      tail: () => merge(cs0.tail(), css.tail().pairs.cmpsts))

  proc minusAt(n: PrimeType, cs: CIS[PrimeType]): CIS[PrimeType] =
    var nn = n;
    var ncs = cs
    while nn >= ncs.head:
      nn += 2;
      ncs = ncs.tail()
    CIS[PrimeType](head: nn, tail: () => minusAt(nn + 2, ncs))

  proc oddprms(): CIS[PrimeType] =
    CIS[PrimeType](
      head: 3.PrimeType,
      tail: () => minusAt(5.PrimeType, oddprms().allmults.cmpsts))

  var prms = CIS[PrimeType](head: 2.PrimeType, tail: () => oddprms())
  while true:
    yield prms.head;
    prms = prms.tail()

stdout.write "The first 25 primes are:  "
var counter = 0
for p in primesTreeFolding():
  if counter >= 25: break
  stdout.write(p, " "); counter += 1
echo()

let start = epochTime()
counter = 0
for p in primesTreeFolding():
  if p > 1000000: break
  else: counter += 1
let elapsed = epochTime() - start
echo "There are ", counter, " primes up to 1000000."
echo "This test took ", elapsed, " seconds."
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
There are 78498 primes up to 1000000.
This test took 0.2780287265777588 seconds.
```

With Nim 1.4, it takes about 0.4s (in release or danger mode) to compute the primes until one million, better than the time needed in previous versions. With option "--gc arc", this time drops to 0.28s on a small laptop. This is still slow compared to bound algorithm which is due to the many small memory allocations/de-allocations required, which is a characteristic of functional forms of code. Is is purely functional in that everything is immutable other than that Nim does not have Tail Call Optimization (TCO) so that we can freely use function recursion with no execution time cost; therefore, where necessary this is implemented with imperative loops, which is what TCO is generally turned into such forms "under the covers". It is also slow due to the algorithm being only O(n (log n) (log (log n))) rather than without the extra "log n" factor as some version have. This slowness makes it only moderately useful for ranges up to a few million.

Since the algorithm does not require the memoization of a full lazy list, it uses an internal Co Inductive Stream of deferred execution states, finally outputting an iterator to enumerate over the lazily computed stream of primes.

**A faster alternative using a mutable hash table (odds-only)**

To show the cost of functional forms of code, the following code is written embracing mutability, both by using a mutable hash table to store the state of incremental culling by the secondary stream of base primes and by using mutable values to store the state wherever possible, as per the following code:

```mw
import tables, times

type PrimeType = int
proc primesHashTable(): iterator(): PrimeType {.closure.} =
  iterator output(): PrimeType {.closure.} =
    # some initial values to avoid race and reduce initializations...
    yield 2.PrimeType; yield 3.PrimeType; yield 5.PrimeType; yield 7.PrimeType
    var h = initTable[PrimeType,PrimeType]()
    var n = 9.PrimeType
    let bps = primesHashTable()
    var bp = bps()  # advance past 2
    bp = bps()
    var q = bp * bp # to initialize with 3
    while true:
      if n >= q:
        let incr = bp + bp
        h[n + incr] = incr
        bp = bps()
        q = bp * bp
      elif h.hasKey(n):
        var incr: PrimeType
        discard h.take(n, incr)
        var nxt = n + incr
        while h.hasKey(nxt):
          nxt += incr # ensure no duplicates
        h[nxt] = incr
      else:
        yield n
      n += 2.PrimeType
  output

stdout.write "The first 25 primes are:  "
var counter = 0
var iter = primesHashTable()
for p in iter():
  if counter >= 25:
    break
  else:
    stdout.write(p, " ")
    counter += 1
echo ""
let start = epochTime()
counter = 0
iter = primesHashTable()
for p in iter():
  if p > 1000000: break
  else: counter += 1
let elapsed = epochTime() - start
echo "The number of primes up to a million is:  ", counter
stdout.write("This test took ", elapsed, " seconds.\n")
```

**Output:**

Time for version compiled with “-d:danger” option.

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
The number of primes up to a million is:  78498
This test took 0.05106830596923828 seconds.
```

The output is identical to the first unbounded version, other than, in danger mode, it is over about eight times faster sieving to a million. For larger ranges it will continue to pull further ahead of the above version due to only O(n (log (log n))) performance because of the hash table having an average of O(1) access, and it is only so slow due to the large constant overhead of doing the hashing calculations and look-ups.

**Very fast Page Segmented version using a bit-packed mutable array (odds-only)**

Note: This version is used as a very fast alternative in Extensible_prime_generator#Nim

For the highest speeds, one needs to use page segmented mutable arrays as in the bit-packed version here:

```mw
# a Page Segmented Odd-Only Bit-Packed Sieve of Eratosthenes...

from times import epochTime # for testing
from bitops import popCount

type Prime = uint64

let LIMIT = 1_000_000_000.Prime
let CPUL1CACHE = 16384 # in bytes

const FRSTSVPRM = 3.Prime

type
  BasePrime = uint32
  BasePrimeArray = seq[BasePrime]
  SieveBuffer = seq[byte] # byte size gives the most potential efficiency...

# define a general purpose lazy list to use as secondary base prime arrays feed
# NOT thread safe; needs a Mutex gate to make it so, but not threaded (yet)...
type
  BasePrimeArrayLazyList = ref object
    head: BasePrimeArray
    tailf: proc (): BasePrimeArrayLazyList {.closure.}
    tail: BasePrimeArrayLazyList
template makeBasePrimeArrayLazyList(hd: BasePrimeArray;
                      body: untyped): untyped = # factory constructor
  let thnk = proc (): BasePrimeArrayLazyList {.closure.} = body
  BasePrimeArrayLazyList(head: hd, tailf: thnk)
proc rest(lzylst: sink BasePrimeArrayLazyList): BasePrimeArrayLazyList {.inline.} =
  if lzylst.tailf != nil: lzylst.tail = lzylst.tailf(); lzylst.tailf = nil
  return lzylst.tail
iterator items(lzylst: BasePrimeArrayLazyList): BasePrime {.inline.} =
  var ll = lzylst
  while ll != nil:
    for bp in ll.head: yield bp
    ll = ll.rest

# count the number of zero bits (primes) in a SieveBuffer,
# uses native popCount for extreme speed;
# counts up to the bit index of the last bit to be counted...
proc countSieveBuffer(lsti: int; cmpsts: SieveBuffer): int =
  let lstw = (lsti shr 3) and -8; let lstm = lsti and 63 # last word and bit index!
  result = (lstw shl 3) + 64 # preset for all ones!
  let cmpstsa = cast[int](cmpsts[0].unsafeAddr)
  let cmpstslsta = cmpstsa + lstw
  for csa in countup(cmpstsa, cmpstslsta - 1, 8):
    result -= cast[ptr uint64](csa)[].popCount # subtract number of found ones!
  let msk = (0'u64 - 2'u64) shl lstm # mask for the unused bits in last word!
  result -= (cast[ptr uint64](cmpstslsta)[] or msk).popCount
 
# a fast fill SieveBuffer routine using pointers...
proc fillSieveBuffer(sb: var SieveBuffer) = zeroMem(sb[0].unsafeAddr, sb.len)

const BITMASK = [1'u8, 2, 4, 8, 16, 32, 64, 128] # faster than shifting!

# do sieving work, based on low starting value for the given buffer and
# the given lazy list of base prime arrays...
proc cullSieveBuffer(lwi: int; bpas: BasePrimeArrayLazyList;
                               sb: var SieveBuffer) =
  let len = sb.len; let szbits = len shl 3; let nxti = lwi + szbits
  for bp in bpas:
    let bpwi = ((bp.Prime - FRSTSVPRM) shr 1).int
    var s = (bpwi shl 1) * (bpwi + FRSTSVPRM.int) + FRSTSVPRM.int
    if s >= nxti: break
    if s >= lwi: s -= lwi
    else:
      let r = (lwi - s) mod bp.int
      s = (if r == 0: 0 else: bp.int - r)
    let clmt = szbits - (bp.int shl 3)
#    if len == CPUL1CACHE: continue
    if s < clmt:
      let slmt = s + (bp.int shl 3)
      while s < slmt:
        let msk = BITMASK[s and 7]
        for c in countup(s shr 3, len - 1, bp.int):
          sb[c] = sb[c] or msk
        s += bp.int
      continue
    while s < szbits:
      let w = s shr 3; sb[w] = sb[w] or BITMASK[s and 7]; s += bp.int # (1'u8 shl (s and 7))

proc makeBasePrimeArrays(): BasePrimeArrayLazyList # forward reference!

# an iterator over successive sieved buffer composite arrays,
# returning whatever type the cnvrtr produces from
# the low index and the culled SieveBuffer...
proc makePrimePages[T](
    strtwi, sz: int; cnvrtrf: proc (li: int; sb: var SieveBuffer): T {.closure.}
      ): (iterator(): T {.closure.}) =
  var lwi = strtwi; let bpas = makeBasePrimeArrays(); var cmpsts = newSeq[byte](sz)
  return iterator(): T {.closure.} =
    while true:
      fillSieveBuffer(cmpsts); cullSieveBuffer(lwi, bpas, cmpsts)
      yield cnvrtrf(lwi, cmpsts); lwi += cmpsts.len shl 3
 
# starts the secondary base primes feed with minimum size in bits set to 4K...
# thus, for the first buffer primes up to 8293,
# the seeded primes easily cover it as 97 squared is 9409.
proc makeBasePrimeArrays(): BasePrimeArrayLazyList =
  # converts an entire sieved array of bytes into an array of base primes,
  # to be used as a source of base primes as part of the Lazy List...
  proc sb2bpa(li: int; sb: var SieveBuffer): BasePrimeArray =
    let szbits = sb.len shl 3; let len = countSieveBuffer(szbits - 1, sb)
    result = newSeq[BasePrime](len); var j = 0
    for i in 0 ..< szbits:
      if (sb[i shr 3] and BITMASK[i and 7]) == 0'u8:
        result[j] = FRSTSVPRM.BasePrime + ((li + i) shl 1).BasePrime; j.inc
  proc nxtbparr(
      pgen: iterator (): BasePrimeArray {.closure.}): BasePrimeArrayLazyList =
    return makeBasePrimeArrayLazyList(pgen()): nxtbparr(pgen)
  # pre-seeding first array breaks recursive race,
  # dummy primes of all odd numbers starting at FRSTSVPRM (unculled)...
  var cmpsts = newSeq[byte](512)
  let dummybparr = sb2bpa(0, cmpsts)
  let fakebps = makeBasePrimeArrayLazyList(dummybparr): nil # used just once here!
  cullSieveBuffer(0, fakebps, cmpsts)
  return makeBasePrimeArrayLazyList(sb2bpa(0, cmpsts)):
    nxtbparr(makePrimePages(4096, 512, sb2bpa)) # lazy recursive call breaks race!
 
# iterator over primes from above page iterator;
# takes at least as long to enumerate the primes as sieve them...
iterator primesPaged(): Prime {.inline.} =
  yield 2
  proc mkprmarr(li: int; sb: var SieveBuffer): seq[Prime] =
    let szbits = sb.len shl 3; let low = FRSTSVPRM + (li + li).Prime; var j = 0
    let len = countSieveBuffer(szbits - 1, sb); result = newSeq[Prime](len)
    for i in 0 ..< szbits:
      if (sb[i shr 3] and BITMASK[i and 7]) == 0'u8:
        result[j] = low + (i + i).Prime; j.inc
  let gen = makePrimePages(0, CPUL1CACHE, mkprmarr)
  for prmpg in gen():
    for prm in prmpg: yield prm
 
proc countPrimesTo(range: Prime): int64 =
  if range < FRSTSVPRM: return (if range < 2: 0 else: 1)
  result = 1; let rngi = ((range - FRSTSVPRM) shr 1).int
  proc cntr(li: int; sb: var SieveBuffer): (int, int) {.closure.} =
    let szbits = sb.len shl 3; let nxti = li + szbits; result = (0, nxti)
    if nxti <= rngi: result[0] += countSieveBuffer(szbits - 1, sb)
    else: result[0] += countSieveBuffer(rngi - li, sb)
  let gen = makePrimePages(0, CPUL1CACHE, cntr)
  for count, nxti in gen():
    result += count; if nxti > rngi: break

# showing results...
echo "Page Segmented Bit-Packed Odds-Only Sieve of Eratosthenes"
echo "Needs at least ", CPUL1CACHE, " bytes of CPU L1 cache memory.\n"

stdout.write "First 25 primes:  "
var counter0 = 0
for p in primesPaged():
  if counter0 >= 25: break
  stdout.write(p, " "); counter0.inc
echo ""

stdout.write "The number of primes up to a million is:  "
var counter1 = 0
for p in primesPaged():
  if p > 1_000_000.Prime: break else: counter1.inc
stdout.write counter1, " - these both found by (slower) enumeration.\n"

let start = epochTime()
#[ # slow way to count primes takes as long to enumerate as sieve!
var counter = 0
for p in primesPaged():
  if p > LIMIT: break else: counter.inc
# ]#
let counter = countPrimesTo LIMIT # the fast way using native popCount!
let elpsd = epochTime() - start

echo "Found ", counter, " primes up to ", LIMIT, " in ", elpsd, " seconds."
```

**Output:**

Time is obtained with Nim 1.4 with options `-d:danger --gc:arc`.

```
Page Segmented Bit-Packed Odds-Only Sieve of Eratosthenes
Needs at least 16384 bytes of CPU L1 cache memory.

First 25 primes:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
The number of primes up to a million is:  78498 - these both found by (slower) enumeration.
Found 50847534 primes up to 1000000000 in 0.7931935787200928 seconds.
```

The above version approaches a hundred times faster than the incremental style versions above due to the high efficiency of direct mutable memory operations in modern CPU's, and is useful for ranges of billions. This version maintains its efficiency using the CPU L1 cache to a range of over 16 billion and then gets a little slower for ranges of a trillion or more using the CPU's L2 cache. It takes an average of only about 3.5 CPU clock cycles per composite number cull, or about 70 CPU clock cycles per prime found.

Note that the fastest performance is realized by using functions that directly manipulate the output "seq" (array) of culled bit number representations such as the `countPrimesTo` function provided, as enumeration using the `primesPaged` iterator takes about as long to enumerate the found primes as it takes to cull the composites.

Many further improvements in speed can be made, as in tuning the medium ranges to more efficiently use the CPU caches for an improvement in the middle ranges of up to a factor of about two, full maximum wheel factorization for a further improvement of about four, extreme loop unrolling for a further improvement of approximately two, multi-threading for an improvement of the factor of effective CPU cores used, etc. However, these improvements are of little point when used with enumeration; for instance, if one successfully reduced the time to sieve the composite numbers to zero, it would still take about a second just to enumerate the resulting primes over a range of a billion.


## Niue

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** It uses rem testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

```mw
[ dup 2 < ] '<2 ;
[ 1 + 'count ; [ <2 [ , ] when ] count times ] 'fill-stack ;

0 'n ; 0 'v ;

[ .clr 0 'n ; 0 'v ; ] 'reset ;
[ len 1 - n - at 'v ; ] 'set-base ;
[ n 1 + 'n ; ] 'incr-n ;
[ mod 0 = ] 'is-factor ;
[ dup * ] 'sqr ;

[ set-base
  v sqr 2 at > not 
  [ [ dup v = not swap v is-factor and ] remove-if incr-n run ] when ] 'run ;

[ fill-stack run ] 'sieve ;

( tests )

10 sieve .s ( => 2 3 5 7 9 ) reset newline
30 sieve .s ( => 2 3 5 7 11 13 17 19 23 29 )
```


## Oberon-2

```mw
MODULE Primes;

   IMPORT Out, Math;

   CONST N = 1000;

   VAR a: ARRAY N OF BOOLEAN;
      i, j, m: INTEGER;

BEGIN
   (* Set all elements of a to TRUE. *)
   FOR i := 1 TO N - 1 DO
      a[i] := TRUE;
   END;

   (* Compute square root of N and convert back to INTEGER. *)
   m := ENTIER(Math.Sqrt(N));

   FOR i := 2 TO m DO
      IF a[i] THEN
         FOR j := 2 TO (N - 1) DIV i DO 
            a[i*j] := FALSE;
         END;
      END;
   END;

   (* Print all the elements of a that are TRUE. *)
   FOR i := 2 TO N - 1 DO
      IF a[i] THEN
         Out.Int(i, 4);
      END;
   END;
   Out.Ln;
END Primes.
```


## OCaml

### Imperative

```mw
let sieve n =
  let is_prime = Array.create n true in
  let limit = truncate(sqrt (float (n - 1))) in
  for i = 2 to limit do
    if is_prime.(i) then
      let j = ref (i*i) in
      while !j < n do
        is_prime.(!j) <- false;
        j := !j + i;
      done
  done;
  is_prime.(0) <- false;
  is_prime.(1) <- false;
  is_prime
```

```mw
let primes n =
  let primes, _ =
    let sieve = sieve n in
    Array.fold_right
      (fun is_prime (xs, i) -> if is_prime then (i::xs, i-1) else (xs, i-1))
      sieve
      ([], Array.length sieve - 1)
  in
  primes
```

in the top-level:

```
# primes 100 ;;
- : int list =
[2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 53; 59; 61; 67; 71;
 73; 79; 83; 89; 97]
```

### Functional

```mw
(* first define some iterators *)
let fold_iter f init a b =
  let rec aux acc i =
    if i > b
    then (acc)
    else aux (f acc i) (succ i)
  in
  aux init a
(* val fold_iter : ('a -> int -> 'a) -> 'a -> int -> int -> 'a *)

let fold_step f init a b step =
  let rec aux acc i =
    if i > b
    then (acc)
    else aux (f acc i) (i + step)
  in
  aux init a
(* val fold_step : ('a -> int -> 'a) -> 'a -> int -> int -> int -> 'a *)

(* remove a given value from a list *)
let remove li v =
  let rec aux acc = function
    | hd::tl when hd = v -> (List.rev_append acc tl)
    | hd::tl -> aux (hd::acc) tl
    | [] -> li
  in
  aux [] li
(* val remove : 'a list -> 'a -> 'a list *)

(* the main function *)
let primes n =
  let li =
    (* create a list [from 2; ... until n] *)
    List.rev(fold_iter (fun acc i -> (i::acc)) [] 2 n)
  in
  let limit = truncate(sqrt(float n)) in
  fold_iter (fun li i ->
      if List.mem i li  (* test if (i) is prime *)
      then (fold_step remove li (i*i) n i)
      else li)
    li 2 (pred limit)
(* val primes : int -> int list *)
```

in the top-level:

```mw
# primes 200 ;;
- : int list =
[2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 53; 59; 61; 67; 71;
 73; 79; 83; 89; 97; 101; 103; 107; 109; 113; 127; 131; 137; 139; 149; 151;
 157; 163; 167; 173; 179; 181; 191; 193; 197; 199]
```

### Another functional version

This uses zero to denote struck-out numbers. It is slightly inefficient as it strikes-out multiples above p rather than p2

```mw
let rec strike_nth k n l = match l with
  | [] -> []
  | h :: t ->
    if k = 0 then 0 :: strike_nth (n-1) n t
    else h :: strike_nth (k-1) n t
(* val strike_nth : int -> int -> int list -> int list *)

let primes n =
  let limit = truncate(sqrt(float n)) in
  let rec range a b = if a > b then [] else a :: range (a+1) b in
  let rec sieve_primes l = match l with
    | [] -> []
    | 0 :: t -> sieve_primes t
    | h :: t -> if h > limit then List.filter ((<) 0) l else
        h :: sieve_primes (strike_nth (h-1) h t) in
  sieve_primes (range 2 n)
(* val primes : int -> int list *)
```

in the top-level:

```mw
# primes 200;;
- : int list =
[2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 53; 59; 61; 67; 71;
 73; 79; 83; 89; 97; 101; 103; 107; 109; 113; 127; 131; 137; 139; 149; 151;
 157; 163; 167; 173; 179; 181; 191; 193; 197; 199]
```

### Yet Another Functional Version

The problem with the above two "functional" versions using OCaml list's is that they aren't written to be Tail Call Recursive and will thus blow stack for more than trivial ranges; the following "incremental" (as in each new value depends on some previous state) "infinite series" (is a generator function that produces a continuous stream or actually a Co-Inductive Stream - CIS - of prime values) Sieve of Eratosthenes code based on adding "infinite tree folding" to a sieve by Richard Bird doesn't have the above limitations:

```mw
let cLIMIT = 1_000_000

type 'a cis = CIS of 'a * (unit -> 'a cis)

let primesTF() =
  let rec merge (CIS(x, xtl) as xs) (CIS(y, ytl) as ys) =
    if x < y then CIS(x, fun() -> merge (xtl()) ys)
    else if y < x then  CIS(y, fun() -> merge xs (ytl()))
    else  CIS(x, fun() -> merge (xtl()) (ytl()))
  in let bpmults bp =
       let adv = bp + bp in
       let rec pmlt vr = CIS(vr, fun() -> pmlt (vr + adv))
       in pmlt (bp * bp)
  in let rec allmlts = function
       | CIS(bp, bptf) -> CIS(bpmults bp, fun() -> allmlts (bptf()))
  in let rec pairs = function
       | CIS(mcs, cstf) ->
         let CIS(nmcs, ncstf) = cstf() in
         CIS(merge mcs nmcs, fun() -> pairs (ncstf()))
  in let rec cmpsts = function
       | CIS(CIS(cr, ctfr), cstf) ->
           CIS(cr, fun() -> merge (ctfr()) (cstf() |> pairs |> cmpsts))
  in let rec testAt n csr =      
       match csr with
         | CIS(cr, ctlr) ->
             if n >= cr then testAt (n + 2) (ctlr())
             else CIS(n, fun() -> testAt (n + 2) csr)
  in let rec oddprms() = CIS(3, fun() -> oddprms() |> allmlts |> cmpsts |> testAt 5)
  in CIS(2, fun() -> oddprms())

let showprmsTo lmt pcis =
  let rec loop lst = function
    | CIS(p, ptf) -> if p > lmt then List.rev lst |> List.map string_of_int
                                       |> String.concat "; "|> print_endline
                     else loop (p :: lst) (ptf())
  in loop [] pcis

let countprmsTo lmt pcis =
  let rec loop cnt = function
    | CIS(p, ptf) -> if p > lmt then cnt else loop (cnt + 1) (ptf())
  in loop 0 pcis

let _ = showprmsTo 100 (primesTF())
let strt = Sys.time()
let answr = countprmsTo cLIMIT (primesTF())
let elpsd = (Sys.time() -. strt) *. 1000.
let _ = Printf.printf "Found %d primes to %d in %f milliseconds.\r\n" answr cLIMIT elpsd
```

**Output:**

```
2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 53; 59; 61; 67; 71; 73; 79; 83; 89; 97
Found 78498 primes to 1000000 in 71.197000 milliseconds.
```

This is actually an odds-only sieve since two is the only even prime, and works recursively in feeding a secondary version of the resulting odd primes back into the sieving mechanism to avoid the size of the "infinite folded tree" of merged base prime multiples from being as large as the range currently sieved but rather to only the square root of the current range. It takes the base primes stream and generates an infinite (as required) stream containing the streams (a stream of streams) of the multiples of each of the base primes generated by `allmults` and `bpmults, then merges this stream of streams using the `pairs` function (thereby doing the "infinite tree folding") and the `merge` function into a single stream of odd composite numbers (`cmpsts`). This works as written because the first value (the square of the base prime) is always less than the first value of the next multiples stream (the next base prime's square). Finally, the `testAt` function compares all of the odd numbers with the stream of composites (only needing to check the first value of the composites stream being consumed) and if not included, adds the current odd test value to the output stream, skipping over any numbers that are found in the composites stream. The odd primes stream as generated by the function `oddprms` has a first value set as three and the testing starts at five in order to avoid the data race due to the recursion so that there are always composite values starting at nine in place before the `testAt` comparisons start with five.

This algorithm using CIS's does have the overhead of needing to generate closures (functions that capture external values that are not function parameters) for every step of new prime generated, but this is quite well optimized for OCaml.

This function is of O(n (log n) log log n) complexity due to the (binary) folded merge tree comparisons, but the OCaml List versions above don't have the ideal O(n log log n) complexity either since they need to scan the lists from the start for every culling pass, as well as being limited by generating stack overflows...

### Yet another (mostly) functional version

This sieve is just "almost"/mostly a purely functional algorithm because it still mutates the contents of the sieving array.

```mw
let sieve limit =
    let p = Array.make (limit + 1) true in
        let rec sieve_outer d =
            if d * d > limit then p
            else if p.(d) then
                let rec sieve_inner m =
                    if m > limit then sieve_outer (d + 1)
                    else ((p.(m) <- false); sieve_inner (m + d))
                in sieve_inner (d * d)
            else sieve_outer (d + 1)
        in sieve_outer 2

let primes limit = 
    let s = (sieve limit) in
        List.init (limit - 1) (fun i -> i + 2)
        |> List.filter (fun x -> s.(x))
```

In the top-level:

```mw
# primes 200;;
- : int list =
[2; 3; 5; 7; 11; 13; 17; 19; 23; 29; 31; 37; 41; 43; 47; 53; 59; 61; 67; 71; 73; 79; 83; 89; 97; 101; 103; 107; 109; 113; 127; 131; 137; 139; 149; 151; 157; 163; 167; 173; 179; 181; 191; 193; 197; 199]
```


## Odin

```mw
#+feature dynamic-literals
package main

import "core:fmt"
import "core:math"
import "core:os"
import "core:strconv"

main :: proc() {

    // start with sieve.exe 120 to get primes until 120
    n:=0
    ok:=false
    assert(len(os.args)==2,"Give integer as argument!")
    if len(os.args) == 2 {
        argument := os.args[1]
        n, ok = strconv.parse_int(argument)
        assert(ok, "Second argument was not an integer")
        assert(n>2, "n must be bigger than two")
    }

    result := [dynamic]i64{0}
    defer delete(result)

    for i:=1;i<n;i+=1 {
        append(&result, 0)
    }

    // outer loop with square root as limit
    limit := i64(math.round_f64(math.sqrt_f64(f64(n))))
    
   

    // some_array : [n]i32
    // fill array with values
    for i:=1;i<n;i+=1 {
        result[i] = i64(i)
    }
    // start from two
    j:=2
    for i:=2; i<= int(limit); i+=1 {
       // set multiples as zero
        for j=2; j*i<int(n); j+=1 {
            result[j*i]=0
        }

    }
    // print primes or numbers that aren't multiples
   for i:=2;i<n;i+=1 {
        if(result[i]!=0) {
           
            fmt.print(result[i])
           fmt.print(" ")
        }
        
    }
  
}
```

**Output:**

```
.\sieve.exe 10
2 3 5 7
.\sieve.exe 100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Oforth

```mw
: eratosthenes(n)
| i j |
   ListBuffer newSize(n) dup add(null) seqFrom(2, n) over addAll
   2 n sqrt asInteger for: i [
      dup at(i) ifNotNull: [ i sq n i step: j [ dup put(j, null) ] ]
      ]
   filter(#notNull) ;
```

**Output:**

```
>100 eratosthenes println
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## Ol

```mw
(define all (iota 999 2))

(print
   (let main ((left '()) (right all))
      (if (null? right)
         (reverse left)
         (unless (car right)
            (main left (cdr right))
            (let loop ((l '()) (r right) (n 0) (every (car right)))
               (if (null? r)
                  (let ((l (reverse l)))
                     (main (cons (car l) left) (cdr l)))
                  (if (eq? n every)
                     (loop (cons #false l) (cdr r) 1 every)
                     (loop (cons (car r) l) (cdr r) (+ n 1) every)))))))
)
```

Output:

```
(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997)
```


## ooRexx

```mw
/*ooRexx program generates & displays primes via the sieve of Eratosthenes.
*                       derived from first Rexx version
*                       uses an array rather than a stem for the list
*                       uses string methods rather than BIFs
*                       uses new ooRexx keyword LOOP, extended assignment
*                         and line comments
*                       uses meaningful variable names and restructures code
*                         layout for improved understandability
****************************************************************************/
  arg highest                       --get highest number to use.
  if \highest~datatype('W') then
    highest = 200                   --use default value.
  isPrime = .array~new(highest)     --container for all numbers.
  isPrime~fill(1)                   --assume all numbers are prime.
  w = highest~length                --width of the biggest number,
                                    --  it's used for aligned output.
  out1 = 'prime'~right(20)          --first part of output messages.
  np = 0                            --no primes so far.
  loop j = 2 for highest - 1        --all numbers up through highest.
    if isPrime[j] = 1 then do       --found one.
      np += 1                       --bump the prime counter.
      say out1 np~right(w) ' --> ' j~right(w)   --display output.
      loop m = j * j to highest by j
        isPrime[m] = ''             --strike all multiples: not prime.
      end
    end
  end
  say
  say np~right(out1~length + 1 + w) 'primes found up to and including ' highest
  exit
```

**Output:**

```
               prime   1  -->    2
               prime   2  -->    3
               prime   3  -->    5
               prime   4  -->    7
               prime   5  -->   11
               prime   6  -->   13
               prime   7  -->   17
               prime   8  -->   19
               prime   9  -->   23
               prime  10  -->   29
               prime  11  -->   31
               prime  12  -->   37
               prime  13  -->   41
               prime  14  -->   43
               prime  15  -->   47
               prime  16  -->   53
               prime  17  -->   59
               prime  18  -->   61
               prime  19  -->   67
               prime  20  -->   71
               prime  21  -->   73
               prime  22  -->   79
               prime  23  -->   83
               prime  24  -->   89
               prime  25  -->   97
               prime  26  -->  101
               prime  27  -->  103
               prime  28  -->  107
               prime  29  -->  109
               prime  30  -->  113
               prime  31  -->  127
               prime  32  -->  131
               prime  33  -->  137
               prime  34  -->  139
               prime  35  -->  149
               prime  36  -->  151
               prime  37  -->  157
               prime  38  -->  163
               prime  39  -->  167
               prime  40  -->  173
               prime  41  -->  179
               prime  42  -->  181
               prime  43  -->  191
               prime  44  -->  193
               prime  45  -->  197
               prime  46  -->  199

                      46 primes found up to and including  200
```

### Wheel Version

```mw
/*ooRexx program generates primes via sieve of Eratosthenes algorithm.
*                       wheel version, 2 handled as special case
*                       loops optimized: outer loop stops at the square root of
*                         the limit, inner loop starts at the square of the
*                         prime just found
*                       use a list rather than an array and remove composites
*                         rather than just mark them
*                       convert list of primes to a list of output messages and
*                         display them with one say statement
*******************************************************************************/
    arg highest                             -- get highest number to use.
    if \highest~datatype('W') then
        highest = 200                       -- use default value.
    w = highest~length                      -- width of the biggest number,
                                            --  it's used for aligned output.
    thePrimes = .list~of(2)                 -- the first prime is 2.
    loop j = 3 to highest by 2              -- populate the list with odd nums.
        thePrimes~append(j)
    end

    j = 3                                   -- first prime (other than 2)
    ix = thePrimes~index(j)                 -- get the index of 3 in the list.
    loop while j*j <= highest               -- strike multiples of odd ints.
                                            --  up to sqrt(highest).
        loop jm = j*j to highest by j+j     -- start at J squared, incr. by 2*J.
            thePrimes~removeItem(jm)        -- delete it since it's composite.
        end
        ix = thePrimes~next(ix)             -- the index of the next prime.
        j = thePrimes[ix]                   -- the next prime.
    end
    np = thePrimes~items                    -- the number of primes since the
                                            --  list is now only primes.
    out1 = '           prime number'        -- first part of output messages.
    out2 = ' --> '                          -- middle part of output messages.
    ix = thePrimes~first
    loop n = 1 to np                        -- change the list of primes
                                            --  to output messages.
        thePrimes[ix] = out1 n~right(w) out2 thePrimes[ix]~right(w)
        ix = thePrimes~next(ix)
    end
    last = np~right(out1~length+1+w) 'primes found up to and including ' highest
    thePrimes~append(.endofline || last)    -- add blank line and summary line.
    say thePrimes~makearray~toString        -- display the output.
    exit
```

**Output:**

when using the limit of 100

```
           prime number    1  -->     2
           prime number    2  -->     3
           prime number    3  -->     5
           prime number    4  -->     7
           prime number    5  -->    11
           prime number    6  -->    13
           prime number    7  -->    17
           prime number    8  -->    19
           prime number    9  -->    23
           prime number   10  -->    29
           prime number   11  -->    31
           prime number   12  -->    37
           prime number   13  -->    41
           prime number   14  -->    43
           prime number   15  -->    47
           prime number   16  -->    53
           prime number   17  -->    59
           prime number   18  -->    61
           prime number   19  -->    67
           prime number   20  -->    71
           prime number   21  -->    73
           prime number   22  -->    79
           prime number   23  -->    83
           prime number   24  -->    89
           prime number   25  -->    97

                          25 primes found up to and including  100
```


## Oz

Translation of

:

Haskell

```mw
declare
  fun {Sieve N}
     S = {Array.new 2 N true}
     M = {Float.toInt {Sqrt {Int.toFloat N}}}
  in
     for I in 2..M do
   if S.I then
      for J in I*I..N;I do
         S.J := false
      end
   end
     end
     S
  end

  fun {Primes N}
     S = {Sieve N}
  in
     for I in 2..N collect:C do
   if S.I then {C I} end
     end
  end
in
  {Show {Primes 30}}
```


## PARI/GP

```mw
Eratosthenes(lim)={
  my(v=Vecsmall(lim\1,unused,1));
  forprime(p=2,sqrt(lim),
    forstep(i=p^2,lim,p,
      v[i]=0
    )
  );
  for(i=1,lim,if(v[i],print1(i", ")))
};
```

An alternate version:

```mw
Sieve(n)=
{
v=vector(n,unused,1);
for(i=2,sqrt(n),
    if(v[i],
       forstep(j=i^2,n,i,v[j]=0)));
for(i=2,n,if(v[i],print1(i",")))
};
```


## Pascal

Note: Some Pascal implementations put quite low limits on the size of a set (e.g. Turbo Pascal doesn't allow more than 256 members). To compile on such an implementation, reduce the constant PrimeLimit accordingly.

```mw
program primes(output);

const
 PrimeLimit = 1000;

var
 primes: set of 1 .. PrimeLimit;
 n, k: integer;
 needcomma: boolean;

begin
 { calculate the primes }
 primes := [2 .. PrimeLimit];
 for n := 1 to trunc(sqrt(PrimeLimit)) do
  begin
   if n in primes
    then
     begin
      k := n*n;
      while k < PrimeLimit do
       begin
        primes := primes - [k];
        k := k + n
       end
     end
  end;

  { output the primes }
  needcomma := false;
  for n := 1 to PrimeLimit do
   if n in primes
    then
     begin
      if needcomma
       then
        write(', ');
      write(n);
      needcomma := true
     end
end.
```

### Free Pascal

### alternative using wheel

Using growing wheel to fill array for sieving for minimal unmark operations. Sieving only with possible-prime factors.

```mw
program prim(output);
//Sieve of Erathosthenes with fast elimination of multiples of small primes
{$IFNDEF FPC}
  {$APPTYPE CONSOLE}
{$ENDIF}
const
  PrimeLimit = 100*1000*1000;//1;
type
  tLimit = 1..PrimeLimit;
var
  //always initialized with 0 => false at startup
  primes: array [tLimit] of boolean;

function BuildWheel: longInt;
//fill primfield with no multiples of small primes
//returns next sieveprime
//speedup ~1/3
var
  //wheelprimes = 2,3,5,7,11... ;
  //wheelsize = product [i= 0..wpno-1]wheelprimes[i] > Uint64 i> 13
  wheelprimes :array[0..13] of byte;
  wheelSize,wpno,
  pr,pw,i, k: LongWord;
begin
  //the mother of all numbers 1 ;-)
  //the first wheel = generator of numbers
  //not divisible by the small primes first found primes
  pr := 1;
  primes[1]:= true;
  WheelSize := 1;

  wpno := 0;
  repeat
    inc(pr);
    //pw = pr projected in wheel of wheelsize
    pw := pr;
    if pw > wheelsize then
      dec(pw,wheelsize);
    If Primes[pw] then
    begin
//      writeln(pr:10,pw:10,wheelsize:16);
      k := WheelSize+1;
      //turn the wheel (pr-1)-times
      for i := 1 to pr-1 do
      begin
        inc(k,WheelSize);
        if k<primeLimit then
          move(primes[1],primes[k-WheelSize],WheelSize)
        else
        begin
          move(primes[1],primes[k-WheelSize],PrimeLimit-WheelSize*i);
          break;
        end;
      end;
      dec(k);
      IF k > primeLimit then
        k := primeLimit;
      wheelPrimes[wpno] := pr;
      primes[pr] := false;

      inc(wpno);
      //the new wheelsize
      WheelSize := k;

      //sieve multiples of the new found prime
      i:= pr;
      i := i*i;
      while i <= k do
      begin
        primes[i] := false;
        inc(i,pr);
      end;
    end;
  until WheelSize >= PrimeLimit;

  //re-insert wheel-primes
  // 1 still stays prime
  while wpno > 0 do
  begin
    dec(wpno);
    primes[wheelPrimes[wpno]] := true;
  end;
  BuildWheel  := pr+1;
end;

procedure Sieve;
var
  sieveprime,
  fakt : LongWord;
begin
//primes[1] = true is needed to stop for sieveprime = 2
// at //Search next smaller possible prime
  sieveprime := BuildWheel;
//alternative here
  //fillchar(primes,SizeOf(Primes),chr(ord(true)));sieveprime := 2;
  repeat
    if primes[sieveprime] then
    begin
      //eliminate 'possible prime' multiples of sieveprime
      //must go downwards
      //2*2 would unmark 4 -> 4*2 = 8 wouldnt be unmarked
      fakt := PrimeLimit DIV sieveprime;
      IF fakt < sieveprime then
        BREAK;
      repeat
        //Unmark
        primes[sieveprime*fakt] := false;
        //Search next smaller possible prime
        repeat
          dec(fakt);
        until primes[fakt];
      until fakt < sieveprime;
    end;
    inc(sieveprime);
  until false;
  //remove 1
  primes[1] := false;
end;

var
  prCnt,
  i : LongWord;
Begin
  Sieve;
  {count the primes }
  prCnt := 0;
  for i:= 1 to PrimeLimit do
    inc(prCnt,Ord(primes[i]));
  writeln(prCnt,' primes up to ',PrimeLimit);
end.
```

**output**

( i3 4330 Haswell 3.5 Ghz fpc 2.6.4 -O3 ):

```
5761455 primes up to 100000000
real  0m0.204s user  0m0.193s sys   0m0.013s 
```


## PascalABC.NET

```mw
function Eratosthenes(N: integer): List<integer>;
type primetype = (nonprime,prime);
begin
  var sieve := |nonprime|*2 + |prime|*(N-1);
  for var i:=2 to N.Sqrt.Trunc do
    if sieve[i] = prime then
      for var j := i*i to N step i do
        sieve[j] := nonprime;
  Result := new List<integer>;
  for var i:=2 to N do
    if sieve[i] = prime then
      Result.Add(i);
end;

begin
  Eratosthenes(1000).Println
end.
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997
```
