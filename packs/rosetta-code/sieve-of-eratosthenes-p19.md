---
title: "Sieve of Eratosthenes (part 19/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 19/21
---

## Scala

### Genuine Eratosthenes sieve

```mw
import scala.annotation.tailrec
import scala.collection.parallel.mutable
import scala.compat.Platform

object GenuineEratosthenesSieve extends App {
  def sieveOfEratosthenes(limit: Int) = {
    val (primes: mutable.ParSet[Int], sqrtLimit) = (mutable.ParSet.empty ++ (2 to limit), math.sqrt(limit).toInt)
    @tailrec
    def prim(candidate: Int): Unit = {
      if (candidate <= sqrtLimit) {
        if (primes contains candidate) primes --= candidate * candidate to limit by candidate
        prim(candidate + 1)
      }
    }
    prim(2)
    primes
  }
  // BitSet toList is shuffled when using the ParSet version. So it has to be sorted before using it as a sequence.

  assert(sieveOfEratosthenes(15099480).size == 976729)
  println(s"Successfully completed without errors. [total ${Platform.currentTime - executionStart} ms]")
}
```

**Output:**

```
Successfully completed without errors. [total 39807 ms]

Process finished with exit code 0
```

While concise, the above code is quite slow but a little faster not using the ParSet (**take out the '.par' for speed**), in which case the sorting ('sorted') is not necessary for an additional small gain in speed; the above code is slow because of all the overhead in processing the bit packed "BitSet" bib-by-bit using complex "higher-order" method calls.

The following '''odds-only''' code is written in a very concise functional style (no mutable state other than the contents of the composites buffer and "higher order functions" for clarity), in this case using a Scala mutable BitSet:

```mw
object SoEwithBitSet {
  def makeSoE_PrimesTo(top: Int): Iterator[Int] = {
    val topNdx = (top - 3) / 2 //odds composite BitSet buffer offset down to 3
    val cmpsts = new scala.collection.mutable.BitSet(topNdx + 1) //size includes topNdx
    @inline def cullPrmCmpsts(prmNdx: Int) = {
      val prm = prmNdx + prmNdx + 3; cmpsts ++= ((prm * prm - 3) >>> 1 to topNdx by prm) }
    (0 to (Math.sqrt(top).toInt - 3) / 2).filterNot { cmpsts }.foreach { cullPrmCmpsts }
    Iterator.single(2) ++ (0 to topNdx).filterNot { cmpsts }.map { pi => pi + pi + 3 } }
}
```

In spite of being very concise, it is very much faster than the above code converted to odds-only due to the use of the BitSet instead of the hash table based Set (or ParSet), taking only a few seconds to enumerate the primes to 100 million as compared to the 10's of seconds to count the primes to above 15 million above.

### Using tail recursion

The below '''odds-only''' code using a primitive array (bit packed) and tail recursion to avoid some of the enumeration delays due to nested complex "higher order" function calls is almost eight times faster than the above more functional code:

```mw
object SoEwithArray {
  def makeSoE_PrimesTo(top: Int) = {
    import scala.annotation.tailrec
    val topNdx = (top - 3) / 2 + 1 //odds composite BitSet buffer offset down to 3 plus 1 for overflow
    val (cmpsts, sqrtLmtNdx) = (new Array[Int]((topNdx >>> 5) + 1), (Math.sqrt(top).toInt - 3) / 2)

    @inline def isCmpst(ci: Int): Boolean = (cmpsts(ci >>> 5) & (1 << (ci & 31))) != 0

    @inline def setCmpst(ci: Int): Unit = cmpsts(ci >>> 5) |= 1 << (ci & 31)

    @tailrec def forCndNdxsFrom(cndNdx: Int): Unit =
      if (cndNdx <= sqrtLmtNdx) {
        if (!isCmpst(cndNdx)) { //is prime
          val p = cndNdx + cndNdx + 3
          
          @tailrec def cullPrmCmpstsFrom(cmpstNdx: Int): Unit =
            if (cmpstNdx <= topNdx) { setCmpst(cmpstNdx); cullPrmCmpstsFrom(cmpstNdx + p) }
          
          cullPrmCmpstsFrom((p * p - 3) >>> 1) }
        
        forCndNdxsFrom(cndNdx + 1) }; forCndNdxsFrom(0)

    @tailrec def getNxtPrmFrom(cndNdx: Int): Int =
      if ((cndNdx > topNdx) || !isCmpst(cndNdx)) cndNdx + cndNdx + 3 else getNxtPrmFrom(cndNdx + 1)

    Iterator.single(2) ++ Iterator.iterate(3)(p => getNxtPrmFrom(((p + 2) - 3) >>> 1)).takeWhile(_ <= top)
  }
}
```

It can be tested with the following code:

```mw
object Main extends App {
  import SoEwithArray._
  val top_num = 100000000
  val strt = System.nanoTime()
  val count = makeSoE_PrimesTo(top_num).size
  val end = System.nanoTime()
  println(s"Successfully completed without errors. [total ${(end - strt) / 1000000} ms]")
  println(f"Found $count primes up to $top_num" + ".")
  println("Using one large mutable Array and tail recursive loops.")
}
```

To produce the following output:

**Output:**

```
Successfully completed without errors. [total 661 ms]
Found 5761455 primes up to 100000000.
Using one large mutable Array and tail recursive loops.
```

### Odds-only page-segmented "infinite" generator version using tail recursion

The above code still uses an amount of memory proportional to the range of the sieve (although bit-packed as 8 values per byte). As well as only sieving odd candidates, the following code uses a fixed range buffer that is about the size of the CPU L2 cache plus only storage for the base primes up to the square root of the range for a large potential saving in RAM memory used as well as greatly reducing memory access times. The use of innermost tail recursive loops for critical loops where the majority of the execution time is spent rather than "higher order" functions from iterators also greatly reduces execution time, with much of the remaining time used just to enumerate the primes output:

```mw
object APFSoEPagedOdds {
  import scala.annotation.tailrec
  
  private val CACHESZ = 1 << 18 //used cache buffer size
  private val PGSZ = CACHESZ / 4 //number of int's in cache
  private val PGBTS = PGSZ * 32 //number of bits in buffer
  
  //processing output type is a tuple of low bit (odds) address,
  // bit range size, and the actual culled page segment buffer.
  private type Chunk = (Long, Int, Array[Int])
  
  //produces an iteration of all the primes from an iteration of Chunks
  private def enumChnkPrms(chnks: Stream[Chunk]): Iterator[Long] = {
    def iterchnk(chnk: Chunk) = { //iterating primes per Chunk
      val (lw, rng, bf) = chnk
      @tailrec def nxtpi(i: Int): Int = { //find next prime index not composite
        if (i < rng && (bf(i >>> 5) & (1 << (i & 31))) != 0) nxtpi(i + 1) else i }
      Iterator.iterate(nxtpi(0))(i => nxtpi(i + 1)).takeWhile { _ < rng }
        .map { i => ((lw + i) << 1) + 3 } } //map from index to prime value
    chnks.toIterator.flatMap { iterchnk } }
  
  //culls the composite number bit representations from the bit-packed page buffer
  //using a given source of a base primes iterator
  private def cullPg(bsprms: Iterator[Long],
                     lowi: Long, buf: Array[Int]): Unit = {
    //cull for all base primes until square >= nxt
    val rng = buf.length * 32; val nxt = lowi + rng
    @tailrec def cull(bps: Iterator[Long]): Unit = {
      //given prime then calculate the base start address for prime squared
      val bp = bps.next(); val s = (bp * bp - 3) / 2
      //almost all of the execution time is spent in the following tight loop
      @tailrec def cullp(j: Int): Unit = { //cull the buffer for given prime
        if (j < rng) { buf(j >>> 5) |= 1 << (j & 31); cullp(j + bp.toInt) } }
      if (s < nxt) { //only cull for primes squared less than max
        //calculate the start address within this given page segment
        val strt = if (s >= lowi) (s - lowi).toInt else {
          val b = (lowi - s) % bp
          if (b == 0) 0 else (bp - b).toInt }
        cullp(strt); if (bps.hasNext) cull(bps) } } //loop for all primes in range
    //for the first page, use own bit pattern as a source of base primes
    //if another source is not given
    if (lowi <= 0 && bsprms.isEmpty)
      cull(enumChnkPrms(Stream((0, buf.length << 5, buf))))
    //otherwise use the given source of base primes
    else if (bsprms.hasNext) cull(bsprms) }
  
  //makes a chunk given a low address in (odds) bits
  private def mkChnk(lwi: Long): Chunk = {
    val rng = PGBTS; val buf = new Array[Int](rng / 32);
    val bps = if (lwi <= 0) Iterator.empty else enumChnkPrms(basePrms)
    cullPg(bps, lwi, buf); (lwi, rng, buf) }
  
  //new independent source of base primes in a stream of packed-bit arrays
  //memoized by converting it to a Stream and retaining a reference here
  private val basePrms: Stream[Chunk] =
    Stream.iterate(mkChnk(0)) { case (lw, rng, bf) => { mkChnk(lw + rng) } }
  
  //produces an infinite iterator over all the chunk results
  private def itrRslts[R](rsltf: Chunk => R): Iterator[R] = {
    def mkrslt(lwi: Long) = { //makes tuple of result and next low index
      val c = mkChnk(lwi); val (_, rng, _) = c; (rsltf(c), lwi + rng) }
    Iterator.iterate(mkrslt(0)) { case (_, nlwi) => mkrslt(nlwi) }
            .map { case (rslt, _) => rslt} } //infinite iteration of results
  
  //iterates across the "infinite" produced output primes
  def enumSoEPrimes(): Iterator[Long] = //use itrRsltsMP to produce Chunks iteration
    Iterator.single(2L) ++ enumChnkPrms(itrRslts { identity }.toStream)
 
  //counts the number of remaining primes in a page segment buffer
  //using a very fast bitcount per integer element
  //with special treatment for the last page
  private def countpgto(top: Long, b: Array[Int], nlwp: Long) = {
    val numbts = b.length * 32; val prng = numbts * 2
    @tailrec def cnt(i: Int, c: Int): Int = { //tight int bitcount loop
      if (i >= b.length) c else cnt (i + 1, c - Integer.bitCount(b(i))) }
    if (nlwp > top) { //for top in page, calculate int address containing top
      val bi = ((top - nlwp + prng) >>> 1).toInt
      val w = bi >>> 5; b(w) |= -2 << (bi & 31) //mark all following as composite
      for (i <- w + 1 until b.length) b(i) = -1 } //for all int's to end of buffer
    cnt(0, numbts) } //counting the entire buffer in every case
  
  //counts all the primes up to a top value
  def countSoEPrimesTo(top: Long): Long = {
    if (top < 2) return 0L else if (top < 3) return 1L //no work necessary
    //count all Chunks using multi-processing
    val gen = itrRslts { case (lwi, rng, bf) =>
      val nlwp = (lwi + rng) * 2 + 3; (countpgto(top, bf, nlwp), nlwp) }
    //a loop to take Chunk's up to including top limit but not past it
    @tailrec def takeUpto(acc: Long): Long = {
      val (cnt, nlwp) = gen.next(); val nacc = acc + cnt
      if (nlwp <= top) takeUpto(nacc) else nacc }; takeUpto(1) }
}
```

As the above and all following sieves are "infinite", they all require an extra range limiting condition to produce a finite output, such as the addition of ".takeWhile(_ <= topLimit)" where "topLimit" is the specified range as is done in the following code:

```mw
object MainSoEPagedOdds extends App {
  import APFSoEPagedOdds._
  countSoEPrimesTo(100)
  val top = 1000000000
  val strt = System.currentTimeMillis()
  val cnt = enumSoEPrimes().takeWhile { _ <= top }.length
//  val cnt = countSoEPrimesTo(top)
  val elpsd = System.currentTimeMillis() - strt
  println(f"Found $cnt primes up to $top in $elpsd milliseconds.")
}
```

which outputs the following:

**Output:**

```
Found 50847534 primes up to 1000000000 in 5867 milliseconds.
```

While the above code is reasonably fast, much of the execution time is consumed by the use of the built-in functions and iterators for concise code, especially in the use of iterators for primes output. To show this, the code includes a "countSoEPrimesTo" function/method that can be uncommented in the above code (commenting out the "takeWhile" line) to produce the following output:

**Output:**

```
Found 50847534 primes up to 1000000000 in 2623 milliseconds.
```

This shows that it takes somewhat longer to enumerate the primes than it does to actually produce them; this could be improved with a "roll-your-own" enumeration Iterator implementation at considerable increased complexity, but enumeration time will still be a significant portion of the execution time. Further improvements to the code using extreme wheel factorization and multi-processing will make enumeration time an even higher percentage of the total; this is why for large ranges one writes functions/methods similar to "countSoEPrimesTo" to (say) sum the primes, to find the nth prime, etc.

### Odds-Only "infinite" generator sieve using Streams and Co-Inductive Streams

The following code uses delayed recursion via Streams to implement the Richard Bird algorithm mentioned in the last part (the Epilogue) of M.O'Neill's paper, which is **a true incremental Sieve of Eratosthenes**. It is nowhere near as fast as the array based solutions due to the overhead of functionally chasing the merging of the prime multiple streams; this also means that the empirical performance is not according to the usual Sieve of Eratosthenes approximations due to this overhead increasing as the log of the sieved range, but it is much better than the "unfaithful" sieve.

```mw
  def birdPrimes() = {
    def oddPrimes: Stream[Int] = {
      def merge(xs: Stream[Int], ys: Stream[Int]): Stream[Int] = {
        val (x, y) = (xs.head, ys.head)
   
        if (y > x) x #:: merge(xs.tail, ys) else if (x > y) y #:: merge(xs, ys.tail) else x #:: merge(xs.tail, ys.tail)
      }
   
      def primeMltpls(p: Int): Stream[Int] = Stream.iterate(p * p)(_ + p + p)
   
      def allMltpls(ps: Stream[Int]): Stream[Stream[Int]] = primeMltpls(ps.head) #:: allMltpls(ps.tail)
   
      def join(ams: Stream[Stream[Int]]): Stream[Int] = ams.head.head #:: merge(ams.head.tail, join(ams.tail))
   
      def oddPrms(n: Int, composites: Stream[Int]): Stream[Int] =
        if (n >= composites.head) oddPrms(n + 2, composites.tail) else n #:: oddPrms(n + 2, composites)
   
      //following uses a new recursive source of odd base primes
      3 #:: oddPrms(5, join(allMltpls(oddPrimes)))
    }
    2 #:: oddPrimes
  }
```

Now this algorithm doesn't really need the memoization and full laziness as offered by Streams, so an implementation and use of a Co-Inductive Stream (CIS) class is sufficient and reduces execution time by almost a factor of two:

```mw
  class CIS[A](val start: A, val continue: () => CIS[A])

  def primesBirdCIS: Iterator[Int] = {
    def merge(xs: CIS[Int], ys: CIS[Int]): CIS[Int] = {
      val (x, y) = (xs.start, ys.start)

      if (y > x) new CIS(x, () => merge(xs.continue(), ys))
      else if (x > y) new CIS(y, () => merge(xs, ys.continue()))
      else new CIS(x, () => merge(xs.continue(), ys.continue()))
    }

    def primeMltpls(p: Int): CIS[Int] = {
      def nextCull(cull: Int): CIS[Int] = new CIS[Int](cull, () => nextCull(cull + 2 * p))
      nextCull(p * p)
    }

    def allMltpls(ps: CIS[Int]): CIS[CIS[Int]] =
      new CIS[CIS[Int]](primeMltpls(ps.start), () => allMltpls(ps.continue()))
    def join(ams: CIS[CIS[Int]]): CIS[Int] = {
      new CIS[Int](ams.start.start, () => merge(ams.start.continue(), join(ams.continue())))
    }

    def oddPrimes(): CIS[Int] = {
      def oddPrms(n: Int, composites: CIS[Int]): CIS[Int] = { //"minua"
        if (n >= composites.start) oddPrms(n + 2, composites.continue())
        else new CIS[Int](n, () => oddPrms(n + 2, composites))
      }
      //following uses a new recursive source of odd base primes
      new CIS(3, () => oddPrms(5, join(allMltpls(oddPrimes()))))
    }

    Iterator.single(2) ++ Iterator.iterate(oddPrimes())(_.continue()).map(_.start)
  }
```

Further gains in performance for these last two implementations can be had by using further wheel factorization and "tree folding/merging" as per this Haskell implementation.

### Odds-Only "infinite" generator sieve using a hash table (HashMap)

As per the "unfaithful sieve" article linked above, the incremental "infinite" Sieve of Eratosthenes can be implemented using a hash table instead of a Priority Queue or Map (Binary Heap) as were used in that article. The following implementation postpones the adding of base prime representations to the hash table until necessary to keep the hash table small:

```mw
  def SoEInc: Iterator[Int] = {
    val nextComposites = scala.collection.mutable.HashMap[Int, Int]()
    def oddPrimes: Iterator[Int] = {
      val basePrimes = SoEInc
      basePrimes.next()
      basePrimes.next() // skip the two and three prime factors
      @tailrec def makePrime(state: (Int, Int, Int)): (Int, Int, Int) = {
        val (candidate, nextBasePrime, nextSquare) = state
        if (candidate >= nextSquare) {
          val adv = nextBasePrime << 1
          nextComposites += ((nextSquare + adv) -> adv)
          val np = basePrimes.next()
          makePrime((candidate + 2, np, np * np))
        } else if (nextComposites.contains(candidate)) {
          val adv = nextComposites(candidate)
          nextComposites -= (candidate) += (Iterator.iterate(candidate + adv)(_ + adv)
            .dropWhile(nextComposites.contains(_)).next() -> adv)
          makePrime((candidate + 2, nextBasePrime, nextSquare))
        } else (candidate, nextBasePrime, nextSquare)
      }
      Iterator.iterate((5, 3, 9)) { case (c, p, q) => makePrime((c + 2, p, q)) }
        .map { case (p, _, _) => p }
    }
    List(2, 3).toIterator ++ oddPrimes
  }
```

The above could be implemented using Streams or Co-Inductive Streams to pass the continuation parameters as passed here in a tuple but there would be no real difference in speed and there is no need to use the implied laziness. As compared to the versions of the Bird (or tree folding) Sieve of Eratosthenes, this has the expected same computational complexity as the array based versions, but is about 20 times slower due to the constant overhead of processing the key value hashing. Memory use is quite low, only being the hash table entries for each of the base prime values less than the square root of the last prime enumerated multiplied by the size of each hash entry (about 12 bytes in this case) plus a "load factor" percentage overhead in hash table size to minimize hash collisions (about twice as large as entries actually used by default on average).

The Scala implementable of a mutable HashMap is slower than the java.util.HashMap one by a factor of almost two, but the Scala version is used here to keep the code more portable (as to CLR). One can also quite easily convert this code to use the immutable Scala HashMap, but the code runs about four times slower due to the required "copy on update" operations for immutable objects.

This algorithm is very responsive to further application of wheel factorization, which can make it run up to about four times faster for the composite number culling operations; however, that is not enough to allow it to catch up to the array based sieves.


## Scheme

### Tail-recursive solution

Works with

:

Scheme

version R

${\displaystyle ^{5}}$

RS

```mw
; Tail-recursive solution :
(define (sieve n)
  (define (aux u v)
    (let ((p (car v)))
      (if (> (* p p) n)
        (let rev-append ((u u) (v v))
          (if (null? u) v (rev-append (cdr u) (cons (car u) v))))
        (aux (cons p u)
          (let wheel ((u '()) (v (cdr v)) (a (* p p)))
            (cond ((null? v) (reverse u))
                  ((= (car v) a) (wheel u (cdr v) (+ a p)))
                  ((> (car v) a) (wheel u v (+ a p)))
                  (else (wheel (cons (car v) u) (cdr v) a))))))))
  (aux '(2)
    (let range ((v '()) (k (if (odd? n) n (- n 1))))
      (if (< k 3) v (range (cons k v) (- k 2))))))

; > (sieve 100)
; (2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
; > (length (sieve 10000000))
; 664579
```

### Simpler, non-tail-recursive solution

```mw
; Simpler solution, with the penalty that none of 'iota, 'strike or 'sieve is tail-recursive :
(define (iota start stop stride)
  (if (> start stop)
      (list)
      (cons start (iota (+ start stride) stop stride))))

(define (strike lst start stride)
  (cond ((null? lst) lst)
        ((= (car lst) start) (strike (cdr lst) (+ start stride) stride))
        ((> (car lst) start) (strike lst (+ start stride) stride))
        (else (cons (car lst) (strike (cdr lst) start stride)))))

(define (primes limit)
  (let ((stop (sqrt limit)))
    (define (sieve lst)
      (let ((p (car lst)))
        (if (> p stop)
            lst
            (cons p (sieve (strike (cdr lst) (* p p) p))))))
    (sieve (iota 2 limit 1))))

(display (primes 100))
(newline)
```

Output:

```mw
(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
```

### Optimised using an odds-wheel

Optimised using a pre-computed wheel based on 2 (i.e. odds only):

```mw
(define (primes-wheel-2 limit)
  (let ((stop (sqrt limit)))
    (define (sieve lst)
      (let ((p (car lst)))
        (if (> p stop)
            lst
            (cons p (sieve (strike (cdr lst) (* p p) (* 2 p)))))))
    (cons 2 (sieve (iota 3 limit 2)))))

(display (primes-wheel-2 100))
(newline)
```

Output:

```mw
(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
```

### Vector-based

Vector-based (faster), works with R ${\displaystyle ^{5}}$ RS:

```mw
; initialize v to vector of sequential integers
(define (initialize! v)
  (define (iter v n) (if (>= n (vector-length v)) 
                         (values) 
                         (begin (vector-set! v n n) (iter v (+ n 1)))))
  (iter v 0))

; set every nth element of vector v to 0,
; starting with element m
(define (strike! v m n)
  (cond ((>= m (vector-length v)) (values))
        (else (begin
                (vector-set! v m 0)
                (strike! v (+ m n) n)))))

; lowest non-zero index of vector v >= n
(define (nextprime v n)
  (if (zero? (vector-ref v n))
      (nextprime v (+ n 1))
      (vector-ref v n)))

; remove elements satisfying pred? from list lst
(define (remove pred? lst)
  (cond 
    ((null? lst) '())
    ((pred? (car lst))(remove pred? (cdr lst)))
    (else (cons (car lst) (remove pred? (cdr lst))))))

; the sieve itself
(define (sieve n)
  (define stop (sqrt n))
  (define (iter v p)
    (cond 
      ((> p stop) v)
      (else 
       (begin
         (strike! v (* p p) p)
         (iter v (nextprime v (+ p 1)))))))
  
  (let ((v (make-vector (+ n 1))))
    (initialize! v)
    (vector-set! v 1 0) ; 1 is not a prime
    (remove zero? (vector->list (iter v 2)))))
```

### SICP-style streams

Using SICP-style *head*-forced streams. Works with MIT-Scheme, Chez Scheme, – or any other Scheme, if writing out by hand the expansion of the only macro here, `s-cons`, with explicit lambda. Common functions:

```mw
 ;;;; Stream Implementation
 (define (head s) (car s))   
 (define (tail s) ((cdr s)))  
 (define-syntax s-cons
   (syntax-rules () ((s-cons h t) (cons h (lambda () t))))) 

 ;;;; Stream Utility Functions
 (define (from-By x s)
   (s-cons x (from-By (+ x s) s)))
 (define (take n s) 
   (cond 
     ((> n 1) (cons (head s) (take (- n 1) (tail s))))
     ((= n 1) (list (head s)))      ;; don't force it too soon!!
     (else '())))     ;; so (take 4 (s-map / (from-By 4 -1))) works
 (define (drop n s)
   (cond 
     ((> n 0) (drop (- n 1) (tail s)))
     (else s)))
 (define (s-map f s)
   (s-cons (f (head s)) (s-map f (tail s))))
 (define (s-diff s1 s2)
   (let ((h1 (head s1)) (h2 (head s2)))
    (cond
     ((< h1 h2) (s-cons h1 (s-diff  (tail s1)       s2 )))
     ((< h2 h1)            (s-diff        s1  (tail s2)))
     (else                 (s-diff  (tail s1) (tail s2))))))
 (define (s-union s1 s2)
   (let ((h1 (head s1)) (h2 (head s2)))
    (cond
     ((< h1 h2) (s-cons h1 (s-union (tail s1)       s2 )))
     ((< h2 h1) (s-cons h2 (s-union       s1  (tail s2))))
     (else      (s-cons h1 (s-union (tail s1) (tail s2)))))))
```

#### The simplest, naive sieve

Very slow, running at ~ *n2.2*, empirically, and worsening:

```mw
 (define (sieve s) 
   (let ((p (head s))) 
     (s-cons p 
             (sieve (s-diff s (from-By p p))))))
 (define primes (sieve (from-By 2 1)))
```

#### Bounded, stopping early

Stops at the square root of the upper limit *m*, running at about ~ *n1.4* in *n* primes produced, empirically. Returns infinite stream of numbers which is only valid up to *m*, includes composites above it:

```mw
 (define (primes-To m)
   (define (sieve s) 
     (let ((p (head s))) 
       (cond ((> (* p p) m) s) 
             (else (s-cons p 
                (sieve (s-diff (tail s) 
                        (from-By (* p p) p))))))))
   (sieve (from-By 2 1)))
```

#### Combined multiples sieve

Archetypal, straightforward approach by Richard Bird, presented in Melissa E. O'Neill article. Uses `s-linear-join`, i.e. right fold, which is less efficient and of worse time complexity than the *tree*-folding that follows. Does not attempt to conserve space by arranging for the additional inner feedback loop, as is done in the tree-folding variant below.

```mw
 (define (primes-stream-ala-Bird)
   (define (mults p) (from-By (* p p) p))
   (define primes                                          ;; primes are 
       (s-cons 2 (s-diff (from-By 3 1)                     ;;  numbers > 1, without 
                  (s-linear-join (s-map mults primes)))))  ;;   multiples of primes
   primes)

 ;;;; join streams using linear structure
 (define (s-linear-join sts)
   (s-cons (head (head sts)) 
           (s-union (tail (head sts)) 
                    (s-linear-join (tail sts)))))
```

Here is a version of the same sieve, which is self contained with all the requisite functions wrapped in the overall function; optimized further. It works with odd primes only, and arranges for a separate primes feed for the base primes separate from the output stream, *calculated recursively* by the recursive call to "oddprms" in forming "cmpsts". It also *"fuses"* two functions, `s-diff` and `from-By`, into one, `minusstrtat`:

```mw
(define (birdPrimes)
  (define (mltpls p)
    (define pm2 (* p 2))
    (let nxtmltpl ((cmpst (* p p)))
      (cons cmpst (lambda () (nxtmltpl (+ cmpst pm2))))))
  (define (allmltpls ps)
    (cons (mltpls (car ps)) (lambda () (allmltpls ((cdr ps))))))
  (define (merge xs ys)
    (let ((x (car xs)) (xt (cdr xs)) (y (car ys)) (yt (cdr ys)))
      (cond ((< x y) (cons x (lambda () (merge (xt) ys))))
            ((> x y) (cons y (lambda () (merge xs (yt)))))
            (else (cons x (lambda () (merge (xt) (yt))))))))
  (define (mrgmltpls mltplss)
    (cons (car (car mltplss))
          (lambda () (merge ((cdr (car mltplss)))
                            (mrgmltpls ((cdr mltplss)))))))
  (define (minusstrtat n cmps)
    (if (< n (car cmps))
      (cons n (lambda () (minusstrtat (+ n 2) cmps)))
      (minusstrtat (+ n 2) ((cdr cmps)))))
  (define (cmpsts) (mrgmltpls (allmltpls (oddprms)))) ;; internal define's are mutually recursive
  (define (oddprms) (cons 3 (lambda () (minusstrtat 5 (cmpsts)))))  
  (cons 2 (lambda () (oddprms))))
```

It can be tested with the following code:

```mw
(define (nthPrime n)
  (let nxtprm ((cnt 0) (ps (birdPrimes)))
    (if (< cnt n) (nxtprm (+ cnt 1) ((cdr ps))) (car ps))))
(nthPrime 1000000)
```

**Output:**

15485863

The same code can easily be modified to perform the folded tree case just by writing and integrating a "pairs" function to do the folding along with the merge, which has been done as an alternate tree folding case below.

#### Tree-folding

The most efficient. Finds composites as a tree of unions of each prime's multiples.

```mw
 ;;;; all primes' multiples are removed, merged through a tree of unions
 ;;;;  runs in ~ n^1.15 run time in producing n = 100K .. 1M primes
 (define (primes-stream)
   (define (mults p) (from-By (* p p) (* 2 p)))
   (define (odd-primes-From from)              ;; odd primes from (odd) f are
       (s-diff (from-By from 2)                ;; all odds from f without the
               (s-tree-join (s-map mults odd-primes))))  ;; multiples of odd primes
   (define odd-primes 
       (s-cons 3 (odd-primes-From 5)))         ;; inner feedback loop
   (s-cons 2 (odd-primes-From 3)))             ;; result stream

 ;;;; join an ordered stream of streams (here, of primes' multiples)
 ;;;; into one ordered stream, via an infinite right-deepening tree
 (define (s-tree-join sts)
   (s-cons (head (head sts))
           (s-union (tail (head sts))
                    (s-tree-join (pairs (tail sts))))))

 (define (pairs sts)                        ;; {a.(b.t)} -> (a+b).{t}
     (s-cons (s-cons (head (head sts)) 
                     (s-union (tail (head sts)) 
                              (head (tail sts))))
             (pairs (tail (tail sts)))))
```

Print 10 last primes of the first thousand primes:

```
(display (take 10 (drop 990 (primes-stream)))) 
;
(7841 7853 7867 7873 7877 7879 7883 7901 7907 7919)
```

This can be also accomplished by the following self contained code which follows the format of the `birdPrimes` code above with the added "pairs" function integrated into the "mrgmltpls" function:

```mw
(define (treemergePrimes)
  (define (mltpls p)
    (define pm2 (* p 2))
    (let nxtmltpl ((cmpst (* p p)))
      (cons cmpst (lambda () (nxtmltpl (+ cmpst pm2))))))
  (define (allmltpls ps)
    (cons (mltpls (car ps)) (lambda () (allmltpls ((cdr ps))))))
  (define (merge xs ys)
    (let ((x (car xs)) (xt (cdr xs)) (y (car ys)) (yt (cdr ys)))
      (cond ((< x y) (cons x (lambda () (merge (xt) ys))))
            ((> x y) (cons y (lambda () (merge xs (yt)))))
            (else (cons x (lambda () (merge (xt) (yt))))))))
  (define (pairs mltplss)
    (let ((tl ((cdr mltplss))))
      (cons (merge (car mltplss) (car tl))
            (lambda () (pairs ((cdr tl)))))))
  (define (mrgmltpls mltplss)
    (cons (car (car mltplss))
          (lambda () (merge ((cdr (car mltplss)))
                            (mrgmltpls (pairs ((cdr mltplss))))))))
  (define (minusstrtat n cmps)
    (if (< n (car cmps))
      (cons n (lambda () (minusstrtat (+ n 2) cmps)))
      (minusstrtat (+ n 2) ((cdr cmps)))))
  (define (cmpsts) (mrgmltpls (allmltpls (oddprms)))) ;; internal define's are mutually recursive
  (define (oddprms) (cons 3 (lambda () (minusstrtat 5 (cmpsts)))))  
  (cons 2 (lambda () (oddprms))))
```

It can be tested with the same code as the self-contained Richard Bird sieve, just by calling `treemergePrimes` instead of `birdPrimes`.

### Generators

```mw
(define (integers n)
  (lambda ()
    (let ((ans n))
      (set! n (+ n 1))
      ans)))

(define natural-numbers (integers 0)) 

(define (remove-multiples g n)
  (letrec ((m (+ n n))
           (self
              (lambda ()
                 (let loop ((x (g)))
                    (cond ((< x m) x)
                          ((= x m) (set! m (+ m n)) (self))
                          (else (set! m (+ m n)) (loop x)))))))
     self))

(define (sieve g)
  (lambda ()
    (let ((x (g)))
      (set! g (remove-multiples g x))
      x)))

(define primes (sieve (integers 2)))
```


## Scilab

```mw
function a = sieve(n)
    a = ~zeros(n, 1)
    a(1) = %f
    for i = 1:n
        if a(i)
            j = i*i
            if j > n
                return
            end
            a(j:i:n) = %f
        end
    end
endfunction

find(sieve(100))
// [2 3 5 ... 97]

sum(sieve(1000))
// 168, the number of primes below 1000
```


## Scratch

```mw
when clicked
    broadcast: fill list with zero (0) and wait
    broadcast: put one (1) in list of multiples and wait
    broadcast: fill primes where zero (0 in list

when I receive: fill list with zero (0)
    delete all of primes
    delete all of list
    set i to 0
    set maximum to 25
    repeat maximum
        add 0 to list
        change i by 1
    {end repeat}

when I receive: put ones (1) in list of multiples
    set S to sqrt of maximum
    set i to 2
    set k to 0
    repeat S
        change J by 1
        set i to 2
        repeat until i > 100
            if not (i = J) then
                if item i of list = 0 then
                    set m to (i mod J)
                    if (m = 0) then
                        replace item i of list with 1
        {end repeat until}
        change i by 1
        set k to 1
        delete all of primes
    {end repeat}
    set J to 1

when I receive: fill primes where zeros (0) in list
    repeat maximum
        if (item k of list) = 0 then
            add k to primes
        set k to (k + 1)
    {end repeat}
```

Scratch is a graphical drag and drop language designed to teach children an introduction to programming. It has easy to use multimedia and animation features. The code listed above was not entered into the Scratch IDE but faithfully represents the graphical code blocks used to run the sieve algorithm. The actual Scratch graphical code blocks cannot be represented on this web site due to its inability to directly represent graphical code. The actual code and output can be seen or downloaded at an external URL web link:

Scratch Code and Output


## Seed7

The program below computes the number of primes between 1 and 10000000:

```mw
$ include "seed7_05.s7i";

const func set of integer: eratosthenes (in integer: n) is func
  result
    var set of integer: sieve is EMPTY_SET;
  local
    var integer: i is 0;
    var integer: j is 0;
  begin
    sieve := {2 .. n};
    for i range 2 to sqrt(n) do
      if i in sieve then
        for j range i ** 2 to n step i do
          excl(sieve, j);
        end for;
      end if;
    end for;
  end func;

const proc: main is func
  begin
    writeln(card(eratosthenes(10000000)));
  end func;
```

Original source: [1]


## SETL

```mw
program eratosthenes;
    print(sieve 100);

    op sieve(n);
        numbers := [1..n];
        numbers(1) := om;
        loop for i in [2..floor sqrt n] do
            loop for j in [i*i, i*i+i..n] do
                numbers(j) := om;
            end loop;
        end loop;
        return [n : n in numbers | n /= om];
    end op;
end program;
```

**Output:**

```
[2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]
```


## Sidef

Translation of

:

Raku

```mw
func sieve(limit) {
    var sieve_arr = [false, false, (limit-1).of(true)...]
    gather {
        sieve_arr.each_kv { |number, is_prime|
            if (is_prime) {
                take(number)
                for i in (number**2 .. limit `by` number) {
                    sieve_arr[i] = false
                }
            }
        }
    }
}

say sieve(100).join(",")
```

**Output:**

```
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
```

Alternative implementation:

```mw
func sieve(limit) {
    var composite = []
    for n in (2 .. limit.isqrt) {
        for i in (n**2 .. limit `by` n) {
            composite[i] = true
        }
    }
    2..limit -> grep{ !composite[_] }
}

say sieve(100).join(",")
```


## Simula

Works with

:

Simula-67

```mw
BEGIN
    INTEGER ARRAY t(0:1000);
    INTEGER i,j,k;
    FOR i:=0 STEP 1 UNTIL 1000 DO t(i):=1;
    t(0):=0; t(1):=0;
    i:=0;
    FOR i:=i WHILE i<1000 DO
    BEGIN
        FOR i:=i WHILE i<1000 AND t(i)=0 DO i:=i+1;
        IF i<1000 THEN
        BEGIN
            j:=2;
            k:=j*i;
            FOR k:=k WHILE k<1000 DO
            BEGIN
                t(k):=0;
                j:=j+1;
                k:=j*i
            END;
            i:=i+1
        END
    END;
    FOR i:=0 STEP 1 UNTIL 999 DO
       IF t(i)<>0  THEN
       BEGIN
           OutInt(i,5); OutImage
       END
END
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
...
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

### A Concurrent Prime Sieve

```mw
! A CONCURRENT PRIME SIEVE ;

BEGIN

BOOLEAN DEBUG;

CLASS FILTER(INPUT, OUTPUT, PRIME); REF(FILTER) INPUT, OUTPUT; INTEGER PRIME;
BEGIN
    INTEGER NUM;
    IF PRIME = 0 AND INPUT == NONE THEN
    BEGIN
        ! SEND THE SEQUENCE 2, 3, 4, ... TO CHANNEL 'CH'. ;
        DETACH;
        NUM := 2;
        WHILE TRUE DO
        BEGIN
            IF OUTPUT == NONE THEN
            BEGIN
                IF DEBUG THEN
                BEGIN
                    OUTTEXT("GENERATE SENDS ");
                    OUTINT(NUM, 0);
                    OUTIMAGE;
                END;
                DETACH; ! SEND 'NUM' ;
            END ELSE
            BEGIN
                IF DEBUG THEN
                BEGIN
                    OUTTEXT("GENERATE SENDS ");
                    OUTINT(NUM, 0);
                    OUTTEXT(" TO FILTER("); OUTINT(OUTPUT.PRIME, 0);
                    OUTTEXT(")");
                    OUTIMAGE;
                END;
                OUTPUT.NUM := NUM;
                RESUME(OUTPUT);
            END;
            NUM := NUM + 1;
        END;
    END ELSE
    BEGIN
        ! COPY THE VALUES FROM CHANNEL 'IN' TO CHANNEL 'OUT', ;
        ! REMOVING THOSE DIVISIBLE BY 'PRIME'. ;
        DETACH;
        ! FILTER ;
        WHILE TRUE DO
        BEGIN
            INTEGER I;
            RESUME(INPUT);
            I := INPUT.NUM; ! RECEIVE VALUE FROM 'INPUT'. ;
            IF DEBUG THEN
            BEGIN
                OUTTEXT("FILTER("); OUTINT(PRIME, 0); OUTTEXT(") RECEIVES ");
                OUTINT(I, 0);
                OUTIMAGE;
            END;
            IF NOT MOD(I, PRIME) = 0 THEN
            BEGIN
                IF OUTPUT == NONE THEN
                BEGIN
                    IF DEBUG THEN
                    BEGIN
                        OUTTEXT("FILTER("); OUTINT(PRIME, 0);
                        OUTTEXT(") SENDS ");
                        OUTINT(I, 0);
                        OUTIMAGE;
                    END;
                    DETACH;
                END ELSE
                BEGIN
                    IF DEBUG THEN
                    BEGIN
                        OUTTEXT("FILTER("); OUTINT(PRIME, 0);
                        OUTTEXT(") SENDS ");
                        OUTINT(I, 0);
                        OUTTEXT(" TO FILTER("); OUTINT(OUTPUT.PRIME, 0);
                        OUTTEXT(")");
                        OUTIMAGE;
                    END;
                    OUTPUT.NUM := I; ! SEND 'I' TO 'OUT'. ;
                    RESUME(OUTPUT);
                END;
            END;
        END;
    END;
END;

! THE PRIME SIEVE: DAISY-CHAIN FILTER PROCESSES. ;
! MAIN BLOCK ;
    REF(FILTER) CH;
    INTEGER I, PRIME;
    DEBUG := TRUE;
    CH :- NEW FILTER(NONE, NONE, 0); ! LAUNCH GENERATE GOROUTINE. ;
    FOR I := 1 STEP 1 UNTIL 5 DO
    BEGIN
        REF(FILTER) CH1;
        RESUME(CH);
        PRIME := CH.NUM;
        IF DEBUG THEN OUTTEXT("MAIN BLOCK RECEIVES ");
        OUTINT(PRIME,0);
        OUTIMAGE;
        CH1 :- NEW FILTER(CH, NONE, PRIME);
        CH.OUTPUT :- CH1;
        CH :- CH1;
    END;
END;
```

Output:

```
GENERATE SENDS 2
MAIN BLOCK RECEIVES 2
GENERATE SENDS 3 TO FILTER(2)
FILTER(2) RECEIVES 3
FILTER(2) SENDS 3
MAIN BLOCK RECEIVES 3
GENERATE SENDS 4 TO FILTER(2)
FILTER(2) RECEIVES 4
GENERATE SENDS 5 TO FILTER(2)
FILTER(2) RECEIVES 5
FILTER(2) SENDS 5 TO FILTER(3)
FILTER(3) RECEIVES 5
FILTER(3) SENDS 5
MAIN BLOCK RECEIVES 5
GENERATE SENDS 6 TO FILTER(2)
FILTER(2) RECEIVES 6
GENERATE SENDS 7 TO FILTER(2)
FILTER(2) RECEIVES 7
FILTER(2) SENDS 7 TO FILTER(3)
FILTER(3) RECEIVES 7
FILTER(3) SENDS 7 TO FILTER(5)
FILTER(5) RECEIVES 7
FILTER(5) SENDS 7
MAIN BLOCK RECEIVES 7
GENERATE SENDS 8 TO FILTER(2)
FILTER(2) RECEIVES 8
GENERATE SENDS 9 TO FILTER(2)
FILTER(2) RECEIVES 9
FILTER(2) SENDS 9 TO FILTER(3)
FILTER(3) RECEIVES 9
GENERATE SENDS 10 TO FILTER(2)
FILTER(2) RECEIVES 10
GENERATE SENDS 11 TO FILTER(2)
FILTER(2) RECEIVES 11
FILTER(2) SENDS 11 TO FILTER(3)
FILTER(3) RECEIVES 11
FILTER(3) SENDS 11 TO FILTER(5)
FILTER(5) RECEIVES 11
FILTER(5) SENDS 11 TO FILTER(7)
FILTER(7) RECEIVES 11
FILTER(7) SENDS 11
MAIN BLOCK RECEIVES 11
```


## Smalltalk

A simple implementation that you can run in a workspace. It finds all the prime numbers up to and including *limit*—for the sake of example, up to and including 100.

```mw
| potentialPrimes limit |
limit := 100.
potentialPrimes := Array new: limit.
potentialPrimes atAllPut: true.
2 to: limit sqrt do: [:testNumber |
    (potentialPrimes at: testNumber) ifTrue: [
        (testNumber * 2) to: limit by: testNumber do: [:nonPrime |
            potentialPrimes at: nonPrime put: false
        ]
    ]
].
2 to: limit do: [:testNumber |
    (potentialPrimes at: testNumber) ifTrue: [
        Transcript show: testNumber asString; cr
    ]
]
```


## SNOBOL4

Using strings instead of arrays, and the square/sqrt optimizations.

```mw
        define('sieve(n)i,j,k,p,str,res') :(sieve_end)
sieve   i = lt(i,n - 1) i + 1 :f(sv1)
        str = str (i + 1) ' ' :(sieve)
sv1     str break(' ') . j span(' ') = :f(return)
        sieve = sieve j ' '
        sieve = gt(j ^ 2,n) sieve str :s(return) ;* Opt1
        res = ''
        str (arb ' ') @p ((j ^ 2) ' ') ;* Opt2
        str len(p) . res = ;* Opt2
sv2     str break(' ') . k  span(' ') = :f(sv3)
        res = ne(remdr(k,j),0) res k ' ' :(sv2)
sv3     str = res :(sv1)
sieve_end

*       # Test and display        
        output = sieve(100)
end
```

Output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## SparForte

As a structured script.

```mw
#!/usr/local/bin/spar
pragma annotate( summary, "sieve" );
pragma annotate( description, "The Sieve of Eratosthenes is a simple algorithm that" );
pragma annotate( description, "finds the prime numbers up to a given integer. Implement ");
pragma annotate( description, "this algorithm, with the only allowed optimization that" );
pragma annotate( description, "the outer loop can stop at the square root of the limit," );
pragma annotate( description, "and the inner loop may start at the square of the prime" );
pragma annotate( description, "just found. That means especially that you shouldn't" );
pragma annotate( description, "optimize by using pre-computed wheels, i.e. don't assume" );
pragma annotate( description, "you need only to cross out odd numbers (wheel based on" );
pragma annotate( description, "2), numbers equal to 1 or 5 modulo 6 (wheel based on 2" );
pragma annotate( description, "and 3), or similar wheels based on low primes." );
pragma annotate( see_also, "http://rosettacode.org/wiki/Sieve_of_Eratosthenes" );
pragma annotate( author, "Ken O. Burtch" );
pragma license( unrestricted );

pragma restriction( no_external_commands );

procedure sieve is 
   last_bool : constant positive := 20;
   type bool_array is array(2..last_bool) of boolean;
   a : bool_array;
 
   test_num : positive;  
   -- limit    : positive := positive(numerics.sqrt(float(arrays.last(a))));

   -- n : positive := 2;  
begin
   for i in arrays.first(a)..last_bool loop
     a(i) := true;
   end loop;

   for num in arrays.first(a)..last_bool loop
     if a(num) then
        test_num := num * num;
        while test_num <= last_bool loop
          a(test_num) := false;
          test_num := @ + num;
        end loop;
     end if;
   end loop;
 
   for i in arrays.first(a)..last_bool loop
     if a(i) then
       put_line(i);
     end if;
   end loop;
end sieve;
```
