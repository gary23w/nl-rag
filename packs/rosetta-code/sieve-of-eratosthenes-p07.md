---
title: "Sieve of Eratosthenes (part 7/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 7/21
---

## ERRE

```mw
PROGRAM SIEVE_ORG
  ! --------------------------------------------------
  ! Eratosthenes Sieve Prime Number Program in BASIC
  ! (da 3 a SIZE*2)   from Byte September 1981
  !---------------------------------------------------
  CONST SIZE%=8190

  DIM FLAGS%[SIZE%]

BEGIN
  PRINT("Only 1 iteration")
  COUNT%=0
  FOR I%=0 TO SIZE% DO
     IF FLAGS%[I%]=TRUE THEN
         !$NULL
       ELSE
         PRIME%=I%+I%+3
         K%=I%+PRIME%
         WHILE NOT (K%>SIZE%) DO
            FLAGS%[K%]=TRUE
            K%=K%+PRIME%
         END WHILE
         PRINT(PRIME%;)
         COUNT%=COUNT%+1
     END IF
  END FOR
  PRINT
  PRINT(COUNT%;" PRIMES")
END PROGRAM
```

**Output:**

last lines of the output screen

```
 15749  15761  15767  15773  15787  15791  15797  15803  15809  15817  15823 
 15859  15877  15881  15887  15889  15901  15907  15913  15919  15923  15937 
 15959  15971  15973  15991  16001  16007  16033  16057  16061  16063  16067 
 16069  16073  16087  16091  16097  16103  16111  16127  16139  16141  16183 
 16187  16189  16193  16217  16223  16229  16231  16249  16253  16267  16273 
 16301  16319  16333  16339  16349  16361  16363  16369  16381 
 1899  PRIMES
```


## Euler

The original Euler doesn't have loops built-in. Loops can easily be added by defining and calling suitable procedures with literal procedures as parameters. In this sample, a C-style "for" loop procedure is defined and used to sieve and print the primes.

```
begin
    new sieve; new for; new prime; new i;

    for   <- ` formal init; formal test; formal incr; formal body;
               begin
                 label again;
                 init;
again:           if test then begin body; incr; goto again end else 0
               end
             '
           ;

    sieve <- ` formal n;
               begin
                 new primes; new i; new i2; new j;
                 primes <- list n;
                 for( ` i <- 1 ', ` i <= n ', ` i <- i + 1 '
                    , ` primes[ i ] <- true '
                    );
                 primes[ 1 ] <- false;
                 for( ` i <- 2 '
                    , ` [ i2 <- i * i ] <= n '
                    , ` i <- i + 1 '
                    , ` if primes[ i ] then
                          for( ` j <- i2 ', ` j <= n ', ` j <- j + i '
                             , ` primes[ j ] <- false '
                             )
                        else 0
                      '
                    );
                 primes
               end
             '
           ;

    prime <- sieve( 30 );
    for( ` i <- 1 ', ` i <= length prime ', ` i <- i + 1 '
       , ` if prime[ i ] then out i else 0 '
       )

end $
```

**Output:**

```
    NUMBER                   2
    NUMBER                   3
    NUMBER                   5
    NUMBER                   7
    NUMBER                  11
    NUMBER                  13
    NUMBER                  17
    NUMBER                  19
    NUMBER                  23
    NUMBER                  29
```


## Euphoria

```mw
constant limit = 1000
sequence flags,primes
flags = repeat(1, limit)
for i = 2 to sqrt(limit) do
    if flags[i] then
        for k = i*i to limit by i do
            flags[k] = 0
        end for
    end if
end for

primes = {}
for i = 2 to limit do
    if flags[i] = 1 then
        primes &= i
    end if
end for
? primes
```

Output:

```
{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,
97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,
277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,
383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,
487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,
601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,
709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,
827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,
947,953,967,971,977,983,991,997}
```


## F

### Short with mutable state

```mw
let primes max =
    let mutable xs = [|2..max|]
    let limit = max |> float |> sqrt |> int
    for x in [|2..limit|] do
        xs <- xs |> Array.except [|x*x..x..max|]
    xs
```

### Short Sweet Functional and Idiotmatic

Well lists may not be lazy, but if you call it a sequence then it's a lazy list!

```mw
(*
  An interesting implementation of The Sieve of Eratosthenes.
  Nigel Galloway April 7th., 2017.
*)
let SofE =
  let rec fn n g = seq{ match n with
                        |1 -> yield false; yield! fn g g 
                        |_ -> yield  true; yield! fn (n - 1) g}
  let rec fg ng = seq {
    let g = (Seq.findIndex(id) ng) + 2 // decreasingly inefficient with range at O(n)!
    yield g; yield! fn (g - 1) g |> Seq.map2 (&&) ng |> Seq.cache |> fg }
  Seq.initInfinite (fun x -> true) |> fg
```

**Output:**

```
> SofE |> Seq.take 10 |> Seq.iter(printfn "%d");;
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
```

Although interesting intellectually, and although the algorithm is more Sieve of Eratosthenes (SoE) than not in that it uses a progression of composite number representations separated by base prime gaps to cull, it isn't really SoE in performance due to several used functions that aren't linear with range, such as the "findIndex" that scans from the beginning of all primes to find the next un-culled value as the next prime in the sequence and the general slowness and inefficiency of F# nested sequence generation.

It is so slow that it takes in the order of seconds just to find the primes to a thousand!

For practical use, one would be much better served by any of the other functional sieves below, which can sieve to a million in less time than it takes this one to sieve to ten thousand. Those other functional sieves aren't all that many lines of code than this one.

### Functional

**Richard Bird Sieve**

This is the idea behind Richard Bird's unbounded code presented in the Epilogue of M. O'Neill's article in Haskell. It is about twice as much code as the Haskell code because F# does not have a built-in lazy list so that the effect must be constructed using a Co-Inductive Stream (CIS) type since no memoization is required, along with the use of recursive functions in combination with sequences. The type inference needs some help with the new CIS type (including selecting the generic type for speed). Note the use of recursive functions to implement multiple non-sharing delayed generating base primes streams, which along with these being non-memoizing means that the entire primes stream is not held in memory as for the original Bird code:

```mw
type 'a CIS = CIS of 'a * (unit -> 'a CIS) //'Co Inductive Stream for laziness

let primesBird() =
  let rec (^^) (CIS(x, xtlf) as xs) (CIS(y, ytlf) as ys) = // stream merge function
    if x < y then CIS(x, fun() -> xtlf() ^^ ys)
    elif y < x then CIS(y, fun() -> xs ^^ ytlf())
    else CIS(x, fun() -> xtlf() ^^ ytlf()) // no duplication
  let pmltpls p = let rec nxt c = CIS(c, fun() -> nxt (c + p)) in nxt (p * p)
  let rec allmltps (CIS(p, ptlf)) = CIS(pmltpls p, fun() -> allmltps (ptlf()))
  let rec cmpsts (CIS(CIS(c, ctlf), amstlf)) =
    CIS(c, fun() -> (ctlf()) ^^ (cmpsts (amstlf())))
  let rec minusat n (CIS(c, ctlf) as cs) =
    if n < c then CIS(n, fun() -> minusat (n + 1u) cs)
    else minusat (n + 1u) (ctlf())
  let rec baseprms() = CIS(2u, fun() -> baseprms() |> allmltps |> cmpsts |> minusat 3u)
  Seq.unfold (fun (CIS(p, ptlf)) -> Some(p, ptlf())) (baseprms())
```

The above code sieves all numbers of two and up including all even numbers as per the page specification; the following code makes the very minor changes for an odds-only sieve, with a speedup of over a factor of two:

```mw
type 'a CIS = CIS of 'a * (unit -> 'a CIS) //'Co Inductive Stream for laziness

let primesBirdOdds() =
  let rec (^^) (CIS(x, xtlf) as xs) (CIS(y, ytlf) as ys) = // stream merge function
    if x < y then CIS(x, fun() -> xtlf() ^^ ys)
    elif y < x then CIS(y, fun() -> xs ^^ ytlf())
    else CIS(x, fun() -> xtlf() ^^ ytlf()) // no duplication
  let pmltpls p = let adv = p + p
                  let rec nxt c = CIS(c, fun() -> nxt (c + adv)) in nxt (p * p)
  let rec allmltps (CIS(p, ptlf)) = CIS(pmltpls p, fun() -> allmltps (ptlf()))
  let rec cmpsts (CIS(CIS(c, ctlf), amstlf)) =
    CIS(c, fun() -> ctlf() ^^ cmpsts (amstlf()))
  let rec minusat n (CIS(c, ctlf) as cs) =
    if n < c then CIS(n, fun() -> minusat (n + 2u) cs)
    else minusat (n + 2u) (ctlf())
  let rec oddprms() = CIS(3u, fun() -> oddprms() |> allmltps |> cmpsts |> minusat 5u)
  Seq.unfold (fun (CIS(p, ptlf)) -> Some(p, ptlf())) (CIS(2u, fun() -> oddprms()))
```

**Tree Folding Sieve**

The above code is still somewhat inefficient as it operates on a linear right extending structure that deepens linearly with increasing base primes (those up to the square root of the currently sieved number); the following code changes the structure into an infinite binary tree-like folding by combining each pair of prime composite streams before further processing as usual - this decreases the processing by approximately a factor of log n:

```mw
type 'a CIS = CIS of 'a * (unit -> 'a CIS) //'Co Inductive Stream for laziness

let primesTreeFold() =
  let rec (^^) (CIS(x, xtlf) as xs) (CIS(y, ytlf) as ys) = // stream merge function
    if x < y then CIS(x, fun() -> xtlf() ^^ ys)
    elif y < x then CIS(y, fun() -> xs ^^ ytlf())
    else CIS(x, fun() -> xtlf() ^^ ytlf()) // no duplication
  let pmltpls p = let adv = p + p
                  let rec nxt c = CIS(c, fun() -> nxt (c + adv)) in nxt (p * p)
  let rec allmltps (CIS(p, ptlf)) = CIS(pmltpls p, fun() -> allmltps (ptlf()))
  let rec pairs (CIS(cs0, cs0tlf)) =
    let (CIS(cs1, cs1tlf)) = cs0tlf() in CIS(cs0 ^^ cs1, fun() -> pairs (cs1tlf()))
  let rec cmpsts (CIS(CIS(c, ctlf), amstlf)) =
    CIS(c, fun() -> ctlf() ^^ (cmpsts << pairs << amstlf)())
  let rec minusat n (CIS(c, ctlf) as cs) =
    if n < c then CIS(n, fun() -> minusat (n + 2u) cs)
    else minusat (n + 2u) (ctlf())
  let rec oddprms() = CIS(3u, fun() -> oddprms() |> allmltps |> cmpsts |> minusat 5u)
  Seq.unfold (fun (CIS(p, ptlf)) -> Some(p, ptlf())) (CIS(2u, fun() -> oddprms()))
```

The above code is over four times faster than the "BirdOdds" version (at least 10x faster than the first, "primesBird", producing the millionth prime) and is moderately useful for a range of the first million primes or so.

**Priority Queue Sieve**

In order to investigate Priority Queue Sieves as espoused by O'Neill in the referenced article, one must find an equivalent implementation of a Min Heap Priority Queue as used by her. There is such an purely functional implementation in RosettaCode translated from the Haskell code she used, from which the essential parts are duplicated here (Note that the key value is given an integer type in order to avoid the inefficiency of F# in generic comparison):

```mw
[<RequireQualifiedAccess>]
module MinHeap =

  type HeapEntry<'V> = struct val k:uint32 val v:'V new(k,v) = {k=k;v=v} end
  [<CompilationRepresentation(CompilationRepresentationFlags.UseNullAsTrueValue)>]
  [<NoEquality; NoComparison>]
  type PQ<'V> =
         | Mt
         | Br of HeapEntry<'V> * PQ<'V> * PQ<'V>

  let empty = Mt

  let peekMin = function | Br(kv, _, _) -> Some(kv.k, kv.v)
                         | _            -> None

  let rec push wk wv = 
    function | Mt -> Br(HeapEntry(wk, wv), Mt, Mt)
             | Br(vkv, ll, rr) ->
                 if wk <= vkv.k then
                   Br(HeapEntry(wk, wv), push vkv.k vkv.v rr, ll)
                 else Br(vkv, push wk wv rr, ll)

  let private siftdown wk wv pql pqr =
    let rec sift pl pr =
      match pl with
        | Mt -> Br(HeapEntry(wk, wv), Mt, Mt)
        | Br(vkvl, pll, plr) ->
            match pr with
              | Mt -> if wk <= vkvl.k then Br(HeapEntry(wk, wv), pl, Mt)
                      else Br(vkvl, Br(HeapEntry(wk, wv), Mt, Mt), Mt)
              | Br(vkvr, prl, prr) ->
                  if wk <= vkvl.k && wk <= vkvr.k then Br(HeapEntry(wk, wv), pl, pr)
                  elif vkvl.k <= vkvr.k then Br(vkvl, sift pll plr, pr)
                  else Br(vkvr, pl, sift prl prr)
    sift pql pqr                                        

  let replaceMin wk wv = function | Mt -> Mt
                                  | Br(_, ll, rr) -> siftdown wk wv ll rr
```

Except as noted for any individual code, all of the following codes need the following prefix code in order to implement the non-memoizing Co-Inductive Streams (CIS's) and to set the type of particular constants used in the codes to the same time as the "Prime" type:

```mw
type CIS<'T> = struct val v: 'T val cont: unit -> CIS<'T> new(v,cont) = {v=v;cont=cont} end
type Prime = uint32
let frstprm = 2u
let frstoddprm = 3u
let inc1 = 1u
let inc = 2u
```

The F# equivalent to O'Neill's "odds-only" code is then implemented as follows, which needs the included changed prefix in order to change the primes type to a larger one to prevent overflow (as well the key type for the MinHeap needs to be changed from uint32 to uint64); it is functionally the same as the O'Neill code other than for minor changes to suit the use of CIS streams and the option output of the "peekMin" function:

```mw
type CIS<'T> = struct val v: 'T val cont: unit -> CIS<'T> new(v,cont) = {v=v;cont=cont} end
type Prime = uint64
let frstprm = 2UL
let frstoddprm = 3UL
let inc = 2UL

let primesPQ() =
  let pmult p (xs: CIS<Prime>) = // does map (* p) xs
    let rec nxtm (cs: CIS<Prime>) =
      CIS(p * cs.v, fun() -> nxtm (cs.cont())) in nxtm xs
  let insertprime p xs table =
    MinHeap.push (p * p) (pmult p xs) table
  let rec sieve' (ns: CIS<Prime>) table =
    let nextcomposite = match MinHeap.peekMin table with
                          | None -> ns.v // never happens
                          | Some (k, _) -> k
    let rec adjust table =
      let (n, advs) = match MinHeap.peekMin table with
                        | None -> (ns.v, ns.cont()) // never happens
                        | Some kv -> kv
      if n <= ns.v then adjust (MinHeap.replaceMin advs.v (advs.cont()) table)
      else table
    if nextcomposite <= ns.v then sieve' (ns.cont()) (adjust table)
    else let n = ns.v in CIS(n, fun() ->
           let nxtns = ns.cont() in sieve' nxtns (insertprime n nxtns table))
  let rec sieve (ns: CIS<Prime>) = let n = ns.v in CIS(n, fun() ->
      let nxtns = ns.cont() in sieve' nxtns (insertprime n nxtns MinHeap.empty))
  let odds = // is the odds CIS from 3 up
    let rec nxto i = CIS(i, fun() -> nxto (i + inc)) in nxto frstoddprm
  Seq.unfold (fun (cis: CIS<Prime>) -> Some(cis.v, cis.cont()))
             (CIS(frstprm, fun() -> (sieve odds)))
```

However, that algorithm suffers in speed and memory use due to over-eager adding of prime composite streams to the queue such that the queue used is much larger than it needs to be and a much larger range of primes number must be used in order to avoid numeric overflow on the square of the prime added to the queue. The following code corrects that by using a secondary (actually a multiple of) base primes streams which are constrained to be based on a prime that is no larger than the square root of the currently sieved number - this permits the use of much smaller Prime types as per the default prefix:

```mw
let primesPQx() =
  let rec nxtprm n pq q (bps: CIS<Prime>) =
    if n >= q then let bp = bps.v in let adv = bp + bp
                   let nbps = bps.cont() in let nbp = nbps.v
                   nxtprm (n + inc) (MinHeap.push (n + adv) adv pq) (nbp * nbp) nbps
    else let ck, cv = match MinHeap.peekMin pq with
                        | None -> (q, inc) // only happens until first insertion
                        | Some kv -> kv
         if n >= ck then let rec adjpq ck cv pq =
                             let npq = MinHeap.replaceMin (ck + cv) cv pq
                             match MinHeap.peekMin npq with
                               | None -> npq // never happens
                               | Some(nk, nv) -> if n >= nk then adjpq nk nv npq
                                                 else npq
                         nxtprm (n + inc) (adjpq ck cv pq) q bps
         else CIS(n, fun() -> nxtprm (n + inc) pq q bps)
  let rec oddprms() = CIS(frstoddprm, fun() ->
      nxtprm (frstoddprm + inc) MinHeap.empty (frstoddprm * frstoddprm) (oddprms()))
  Seq.unfold (fun (cis: CIS<Prime>) -> Some(cis.v, cis.cont()))
             (CIS(frstprm, fun() -> (oddprms())))
```

The above code is well over five times faster than the previous translated O'Neill version for the given variety of reasons.

Although slightly faster than the Tree Folding code, this latter code is also limited in practical usefulness to about the first one to ten million primes or so.

All of the above codes can be tested in the F# REPL with the following to produce the millionth prime (the "nth" function is zero based):

```
> primesXXX() |> Seq.nth 999999;;
```

where primesXXX() is replaced by the given primes generating function to be tested, and which all produce the following output (after a considerable wait in some cases):

**Output:**

```
val it : Prime = 15485863u
```

### Imperative

The following code is written in functional style other than it uses a mutable bit array to sieve the composites:

```mw
let primes limit =
  let buf = System.Collections.BitArray(int limit + 1, true)
  let cull p = { p * p .. p .. limit } |> Seq.iter (fun c -> buf.[int c] <- false)
  { 2u .. uint32 (sqrt (double limit)) } |> Seq.iter (fun c -> if buf.[int c] then cull c)
  { 2u .. limit } |> Seq.map (fun i -> if buf.[int i] then i else 0u) |> Seq.filter ((<>) 0u)

[<EntryPoint>]
let main argv =
  if argv = null || argv.Length = 0 then failwith "no command line argument for limit!!!"
  printfn "%A" (primes (System.UInt32.Parse argv.[0]) |> Seq.length)
  0 // return an integer exit code
```

Substituting the following minor changes to the code for the "primes" function will only deal with the odd prime candidates for a speed up of over a factor of two as well as a reduction of the buffer size by a factor of two:

```mw
let primes limit =
  let lmtb,lmtbsqrt = (limit - 3u) / 2u, (uint32 (sqrt (double limit)) - 3u) / 2u
  let buf = System.Collections.BitArray(int lmtb + 1, true)
  let cull i = let p = i + i + 3u in let s = p * (i + 1u) + i in
               { s .. p .. lmtb } |> Seq.iter (fun c -> buf.[int c] <- false)
  { 0u .. lmtbsqrt } |> Seq.iter (fun i -> if buf.[int i] then cull i )
  let oddprms = { 0u .. lmtb } |> Seq.map (fun i -> if buf.[int i] then i + i + 3u else 0u)
                |> Seq.filter ((<>) 0u)
  seq { yield 2u; yield! oddprms }
```

The following code uses other functional forms for the inner culling loops of the "primes function" to reduce the use of inefficient sequences so as to reduce the execution time by another factor of almost three:

```mw
let primes limit =
  let lmtb,lmtbsqrt = (limit - 3u) / 2u, (uint32 (sqrt (double limit)) - 3u) / 2u
  let buf = System.Collections.BitArray(int lmtb + 1, true)
  let rec culltest i = if i <= lmtbsqrt then
                         let p = i + i + 3u in let s = p * (i + 1u) + i in
                         let rec cullp c = if c <= lmtb then buf.[int c] <- false; cullp (c + p)
                         (if buf.[int i] then cullp s); culltest (i + 1u) in culltest 0u
  seq {yield 2u; for i = 0u to lmtb do if buf.[int i] then yield i + i + 3u }
```

Now much of the remaining execution time is just the time to enumerate the primes as can be seen by turning "primes" into a primes counting function by substituting the following for the last line in the above code doing the enumeration; this makes the code run about a further five times faster:

```mw
  let rec count i acc =
    if i > int lmtb then acc else if buf.[i] then count (i + 1) (acc + 1) else count (i + 1) acc
  count 0 1
```

Since the final enumeration of primes is the main remaining bottleneck, it is worth using a "roll-your-own" enumeration implemented as an object expression so as to save many inefficiencies in the use of the built-in seq computational expression by substituting the following code for the last line of the previous codes, which will decrease the execution time by a factor of over three (instead of almost five for the counting-only version, making it almost as fast):

```mw
  let nmrtr() =
    let i = ref -2
    let rec nxti() = i:=!i + 1;if !i <= int lmtb && not buf.[!i] then nxti() else !i <= int lmtb
    let inline curr() = if !i < 0 then (if !i= -1 then 2u else failwith "Enumeration not started!!!")
                        else let v = uint32 !i in v + v + 3u
    { new System.Collections.Generic.IEnumerator<_> with
        member this.Current = curr()
      interface System.Collections.IEnumerator with
        member this.Current = box (curr())
        member this.MoveNext() = if !i< -1 then i:=!i+1;true else nxti()
        member this.Reset() = failwith "IEnumerator.Reset() not implemented!!!"a
      interface System.IDisposable with
        member this.Dispose() = () }
  { new System.Collections.Generic.IEnumerable<_> with
      member this.GetEnumerator() = nmrtr()
    interface System.Collections.IEnumerable with
      member this.GetEnumerator() = nmrtr() :> System.Collections.IEnumerator }
```

The various optimization techniques shown here can be used "jointly and severally" on any of the basic versions for various trade-offs between code complexity and performance. Not shown here are other techniques of making the sieve faster, including extending wheel factorization to much larger wheels such as 2/3/5/7, pre-culling the arrays, page segmentation, and multi-processing.

### Almost functional Unbounded

the following **odds-only** implmentations are written in an almost functional style avoiding the use of mutability except for the contents of the data structures uses to hold the state of the and any mutability necessary to implement a "roll-your-own" IEnumberable iterator interface for speed.

#### Unbounded Dictionary (Mutable Hash Table) Based Sieve

The following code uses the DotNet Dictionary class instead of the above functional Priority Queue to implement the sieve; as average (amortized) hash table access is O(1) rather than O(log n) as for the priority queue, this implementation is slightly faster than the priority queue version for the first million primes and will always be faster for any range above some low range value:

```mw
type Prime = uint32
let frstprm = 2u
let frstoddprm = 3u
let inc = 2u
let primesDict() =
  let dct = System.Collections.Generic.Dictionary()
  let rec nxtprm n q (bps: CIS<Prime>) =
    if n >= q then let bp = bps.v in let adv = bp + bp
                   let nbps = bps.cont() in let nbp = nbps.v
                   dct.Add(n + adv, adv)
                   nxtprm (n + inc) (nbp * nbp) nbps
    else if dct.ContainsKey(n) then
           let adv = dct.[n]
           dct.Remove(n) |> ignore
//           let mutable nn = n + adv // ugly imperative code
//           while dct.ContainsKey(nn) do nn <- nn + adv
//           dct.Add(nn, adv)
           let rec nxtmt k = // advance to next empty spot
             if dct.ContainsKey(k) then nxtmt (k + adv)
             else dct.Add(k, adv) in nxtmt (n + adv)
           nxtprm (n + inc) q bps
         else CIS(n, fun() -> nxtprm (n + inc) q bps)
  let rec oddprms() = CIS(frstoddprm, fun() ->
      nxtprm (frstoddprm + inc) (frstoddprm * frstoddprm) (oddprms()))
  Seq.unfold (fun (cis: CIS<Prime>) -> Some(cis.v, cis.cont()))
             (CIS(frstprm, fun() -> (oddprms())))
```

The above code uses functional forms of code (with the imperative style commented out to show how it could be done imperatively) and also uses a recursive non-sharing secondary source of base primes just as for the Priority Queue version. As for the functional codes, the Primes type can easily be changed to "uint64" for wider range of sieving.

In spite of having true O(n log log n) Sieve of Eratosthenes computational complexity where n is the range of numbers to be sieved, the above code is still not particularly fast due to the time required to compute the hash values and manipulations of the hash table.

#### Unbounded Page-Segmented Bit-Packed Odds-Only Mutable Array Sieve

Note that the following code is used for the F# entry Extensible_prime_generator#Unbounded_Mutable_Array_Generator of the Extensible prime generator page.

All of the above unbounded implementations including the above Dictionary based version are quite slow due to their large constant factor computational overheads, making them more of an intellectual exercise than something practical, especially when larger sieving ranges are required. The following code implements an unbounded page segmented version of the sieve in not that many more lines of code, yet runs about 25 times faster than the Dictionary version for larger ranges of sieving such as to one billion; it uses functional forms without mutability other than for the contents of the arrays and the `primes` enumeration generator function that must use mutability for speed:

```mw
type Prime = float // use uint64/int64 for regular 64-bit F#
type private PrimeNdx = float // they are slow in JavaScript polyfills

let inline private prime n = float n // match these convenience conversions
let inline private primendx n = float n // with the types above!

let private cPGSZBTS = (1 <<< 14) * 8 // sieve buffer size in bits = CPUL1CACHE

type private SieveBuffer = uint8[]

/// a Co-Inductive Stream (CIS) of an "infinite" non-memoized series...
type private CIS<'T> = CIS of 'T * (unit -> CIS<'T>) //' apostrophe formatting adjustment

/// lazy list (memoized) series of base prime page arrays...
type private BasePrime = uint32
type private BasePrimeArr = BasePrime[]
type private BasePrimeArrs = BasePrimeArrs of BasePrimeArr * Option<Lazy<BasePrimeArrs>>

/// Masking array is faster than bit twiddle bit shifts!
let private cBITMASK = [| 1uy; 2uy; 4uy; 8uy; 16uy; 32uy; 64uy; 128uy |]

let private cullSieveBuffer lwi (bpas: BasePrimeArrs) (sb: SieveBuffer) =
  let btlmt = (sb.Length <<< 3) - 1 in let lmti = lwi + primendx btlmt
  let rec loopbp (BasePrimeArrs(bpa, bpatl) as ibpas) i =
    if i >= bpa.Length then
      match bpatl with
      | None -> ()
      | Some lv -> loopbp lv.Value 0 else
    let bp = prime bpa.[i] in let bpndx = primendx ((bp - prime 3) / prime 2)
    let s = (bpndx * primendx 2) * (bpndx + primendx 3) + primendx 3 in let bpint = int bp
    if s <= lmti then
      let s0 = // page cull start address calculation...
        if s >= lwi then int (s - lwi) else
        let r = (lwi - s) % (primendx bp)
        if r = primendx 0 then 0 else int (bp - prime r)
      let slmt = min btlmt (s0 - 1 + (bpint <<< 3))
      let rec loopc c = // loop "unpeeling" is used so
        if c <= slmt then // a constant mask can be used over the inner loop
          let msk = cBITMASK.[c &&& 7]
          let rec loopw w =
            if w < sb.Length then sb.[w] <- sb.[w] ||| msk; loopw (w + bpint)
          loopw (c >>> 3); loopc (c + bpint)
      loopc s0; loopbp ibpas (i + 1) in loopbp bpas 0

/// fast Counting Look Up Table (CLUT) for pop counting...
let private cCLUT =
  let arr = Array.zeroCreate 65536
  let rec popcnt n cnt = if n > 0 then popcnt (n &&& (n - 1)) (cnt + 1) else uint8 cnt
  let rec loop i = if i < 65536 then arr.[i] <- popcnt i 0; loop (i + 1)
  loop 0; arr

let countSieveBuffer ndxlmt (sb: SieveBuffer): int =
  let lstw = (ndxlmt >>> 3) &&& -2
  let msk = (-2 <<< (ndxlmt &&& 15)) &&& 0xFFFF
  let inline cntem i m =
    int cCLUT.[int (((uint32 sb.[i + 1]) <<< 8) + uint32 sb.[i]) ||| m]
  let rec loop i cnt =
    if i >= lstw then cnt - cntem lstw msk else loop (i + 2) (cnt - cntem i 0)
  loop 0 ((lstw <<< 3) + 16)

/// a CIS series of pages from the given start index with the given SieveBuffer size,
/// and provided with a polymorphic converter function to produce
/// and type of result from the culled page parameters...
let rec private makePrimePages strtwi btsz
                               (cnvrtrf: PrimeNdx -> SieveBuffer -> 'T): CIS<'T> =
  let bpas = makeBasePrimes() in let sb = Array.zeroCreate (btsz >>> 3)
  let rec nxtpg lwi =
    Array.fill sb 0 sb.Length 0uy; cullSieveBuffer lwi bpas sb
    CIS(cnvrtrf lwi sb, fun() -> nxtpg (lwi + primendx btsz))
  nxtpg strtwi

/// secondary feed of lazy list of memoized pages of base primes...
and private makeBasePrimes(): BasePrimeArrs =
  let sb2bpa lwi (sb: SieveBuffer) =
    let bsbp = uint32 (primendx 3 + lwi + lwi)
    let arr = Array.zeroCreate <| countSieveBuffer 255 sb
    let rec loop i j =
      if i < 256 then
        if sb.[i >>> 3] &&& cBITMASK.[i &&& 7] <> 0uy then loop (i + 1) j
        else arr.[j] <- bsbp + uint32 (i + i); loop (i + 1) (j + 1)
    loop 0 0; arr
  // finding the first page as not part of the loop and making succeeding
  // pages lazy breaks the recursive data race!
  let frstsb = Array.zeroCreate 32
  let fkbpas = BasePrimeArrs(sb2bpa (primendx 0) frstsb, None)
  cullSieveBuffer (primendx 0) fkbpas frstsb
  let rec nxtbpas (CIS(bpa, tlf)) = BasePrimeArrs(bpa, Some(lazy (nxtbpas (tlf()))))
  BasePrimeArrs(sb2bpa (primendx 0) frstsb,
                Some(lazy (nxtbpas <| makePrimePages (primendx 256) 256 sb2bpa)))

/// produces a generator of primes; uses mutability for better speed...
let primes(): unit -> Prime =
  let sb2prms lwi (sb: SieveBuffer) = lwi, sb in let mutable ndx = -1
  let (CIS((nlwi, nsb), npgtlf)) = // use page generator function above!
    makePrimePages (primendx 0) cPGSZBTS sb2prms
  let mutable lwi = nlwi in let mutable sb = nsb
  let mutable pgtlf = npgtlf
  let mutable baseprm = prime 3 + prime (lwi + lwi) 
  fun() -> 
    if ndx < 0 then ndx <- 0; prime 2 else
    let inline notprm i = sb.[i >>> 3] &&& cBITMASK.[i &&& 7] <> 0uy
    while ndx < cPGSZBTS && notprm ndx do ndx <- ndx + 1
    if ndx >= cPGSZBTS then // get next page if over
      let (CIS((nlwi, nsb), npgtlf)) = pgtlf() in ndx <- 0
      lwi <- nlwi; sb <- nsb; pgtlf <- npgtlf
      baseprm <- prime 3 + prime (lwi + lwi) 
      while notprm ndx do ndx <- ndx + 1
    let ni = ndx in ndx <- ndx + 1 // ready for next call!
    baseprm + prime (ni + ni)

let countPrimesTo (limit: Prime): int = // much faster!
  if limit < prime 3 then (if limit < prime 2 then 0 else 1) else
  let topndx = (limit - prime 3) / prime 2 |> primendx
  let sb2cnt lwi (sb: SieveBuffer) =
    let btlmt = (sb.Length <<< 3) - 1 in let lmti = lwi + primendx btlmt
    countSieveBuffer
      (if lmti < topndx then btlmt else int (topndx - lwi)) sb, lmti
  let rec loop (CIS((cnt, nxti), tlf)) count =
    if nxti < topndx then loop (tlf()) (count + cnt)
    else count + cnt
  loop <| makePrimePages (primendx 0) cPGSZBTS sb2cnt <| 1

/// sequences are convenient but slow...
let primesSeq() = primes() |> Seq.unfold (fun gen -> Some(gen(), gen))
printfn "The first 25 primes are:  %s"
  ( primesSeq() |> Seq.take 25
      |> Seq.fold (fun s p -> s + string p + " ") "" )
printfn "There are %d primes up to a million." 
  ( primesSeq() |> Seq.takeWhile ((>=) (prime 1000000)) |> Seq.length )

let rec cntto gen lmt cnt = // faster than seq's but still slow
  if gen() > lmt then cnt else cntto gen lmt (cnt + 1)

let limit = prime 1_000_000_000
let start = System.DateTime.Now.Ticks
// let answr = cntto (primes()) limit 0 // slower way!
let answr = countPrimesTo limit // over twice as fast way!
let elpsd = (System.DateTime.Now.Ticks - start) / 10000L
printfn "Found %d primes to %A in %d milliseconds." answr limit elpsd
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
There are 78498 primes up to a million.
Found 50847534 primes to 1000000000 in 2161 milliseconds.
```

As with all of the efficient unbounded sieves, the above code uses a secondary enumerator of the base primes less than the square root of the currently culled range, which is this case is a lazy (deferred memoized evaluation) binding by small pages of base primes which also uses the laziness of the deferral of subsequent pages so as to avoid a race condition.

The above code is written to output the "uint64" type for very large ranges of primes since there is little computational cost to doing this for this algorithm when used with 64-bit compilation; however, for the Fable transpiled to JavaScript, the largest contiguous integer that can be represented is the 64-bit floating point mantissa of 52 bits and thus the large numbers can be represented by floats in this case since a 64-bit polyfill is very slow. As written, the practical range for this sieve is about 16 billion, however, it can be extended to about 10^14 (a week or two of execution time) by setting the "PGSZBTS" constant to the size of the CPU L2 cache rather than the L1 cache (L2 is up to about two Megabytes for modern high end desktop CPU's) at a slight loss of efficiency (a factor of up to two or so) per composite number culling operation due to the slower memory access time. When the Fable compilation option is used, execution speed is roughly the same as using F# with DotNet Core.

Even with the custom `primes` enumerator generator (the F#/Fable built-in sequence operators are terribly inefficient), the time to enumerate the resulting primes takes longer than the time to actually cull the composite numbers from the sieving arrays. The time to do the actual culling is thus over 50 times faster than done using the Dictionary version. The slowness of enumeration, no matter what further tweaks are done to improve it (each value enumerated will always take a function calls and a scan loop that will always take something in the order of 100 CPU clock cycles per value), means that further gains in speed using extreme wheel factorization and multi-processing have little point unless the actual work on the resulting primes is done through use of auxiliary functions not using iteration. Such a function is provided here to count the primes by pages using a "pop count" look up table to reduce the counting time to only a small fraction of a second.


## Factor

Factor already contains two implementations of the sieve of Eratosthenes in `math.primes.erato` and `math.primes.erato.fast`. It is suggested to use one of them for real use, as they use faster types, faster unsafe arithmetic, and/or wheels to speed up the sieve further. Shown here is a more straightforward implementation that adheres to the restrictions given by the task (namely, no wheels).

Factor is pleasantly multiparadigm. Usually, it's natural to write more functional or declarative code in Factor, but this is an instance where it is more natural to write imperative code. Lexical variables are useful here for expressing the necessary mutations in a clean way.

```mw
USING: bit-arrays io kernel locals math math.functions
math.ranges prettyprint sequences ;
IN: rosetta-code.sieve-of-erato

<PRIVATE

: init-sieve ( n -- seq )   ! Include 0 and 1 for easy indexing.
    1 - <bit-array> dup set-bits ?{ f f } prepend ;

! Given the sieve and a prime starting index, create a range of
! values to mark composite. Start at the square of the prime.
: to-mark ( seq n -- range )
    [ length 1 - ] [ dup dup * ] bi* -rot <range> ;

! Mark multiples of prime n as composite.
: mark-nths ( seq n -- ) 
    dupd to-mark [ swap [ f ] 2dip set-nth ] with each ;

: next-prime ( index seq -- n ) [ t = ] find-from drop ;

PRIVATE>

:: sieve ( n -- seq )
    n sqrt 2 n init-sieve :> ( limit i! s )
    [ i limit < ]             ! sqrt optimization 
    [ s i mark-nths i 1 + s next-prime i! ] while t s indices ;

: sieve-demo ( -- )
    "Primes up to 120 using sieve of Eratosthenes:" print
    120 sieve . ;

MAIN: sieve-demo
```


## FOCAL

```mw
1.1 T "PLEASE ENTER LIMIT"
1.2 A N
1.3 I (2047-N)5.1
1.4 D 2
1.5 Q

2.1 F X=2,FSQT(N); D 3
2.2 F W=2,N; I (SIEVE(W)-2)4.1

3.1 I (-SIEVE(X))3.3
3.2 F Y=X*X,X,N; S SIEVE(Y)=2
3.3 R

4.1 T %4.0,W,!

5.1 T "PLEASE ENTER A NUMBER LESS THAN 2048."!; G 1.1
```

Note that with the 4k paper tape version of FOCAL, the program will run out of memory for N>190 or so.
