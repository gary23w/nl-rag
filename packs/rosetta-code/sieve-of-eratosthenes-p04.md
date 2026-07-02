---
title: "Sieve of Eratosthenes (part 4/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/21
---

## Clojure

```mw
(defn primes< [n]
   (remove (set (mapcat #(range (* % %) n %)
                        (range 2 (Math/sqrt n))))
           (range 2 n)))
```

The above is **not strictly a Sieve of Eratosthenes** as the composite culling ranges (in the *mapcat*) include all of the multiples of all of the numbers and not just the multiples of primes. When tested with `(println (time (count (primes< 1000000))))`, it takes about 5.5 seconds just to find the number of primes up to a million, partly because of the extra work due to the use of the non-primes, and partly because of the constant enumeration using sequences with multiple levels of function calls. Although very short, this code is likely only useful up to about this range of a million.

It may be written using the *into #{}* function to run slightly faster due to the *set* function being concerned with only distinct elements whereas the *into #{}* only does the conjunction, and even at that doesn't do that much as it does the conjunction to an empty sequence, the code as follows:

```mw
(defn primes< [n]
   (remove (into #{}
                 (mapcat #(range (* % %) n %)
                         (range 2 (Math/sqrt n))))
           (range 2 n)))
```

The above code is slightly faster for the reasons given, but is still not strictly a Sieve of Eratosthenes due to sieving by all numbers and not just by the base primes.

The following code also uses the *into #{}* transducer but has been slightly wheel-factorized to sieve odds-only:

```mw
(defn primes< [n]
   (if (< n 2) ()
     (cons 2 (remove (into #{}
                           (mapcat #(range (* % %) n %)
                                   (range 3 (Math/sqrt n) 2)))
                     (range 3 n 2)))))
```

The above code is a little over twice as fast as the non-odds-only due to the reduced number of operations. It still isn't strictly a Sieve of Eratosthenes as it sieves by all odd base numbers and not only by the base primes.

The following code calculates primes up to and including *n* using a mutable boolean array but otherwise entirely functional code; it is tens (to a hundred) times faster than the purely functional codes due to the use of mutability in the boolean array:

```mw
(defn primes-to
  "Computes lazy sequence of prime numbers up to a given number using sieve of Eratosthenes"
  [n]
  (let [root (-> n Math/sqrt long),
        cmpsts (boolean-array (inc n)),
        cullp (fn [p]
                (loop [i (* p p)]
                  (if (<= i n)
                    (do (aset cmpsts i true)
                        (recur (+ i p))))))]
    (do (dorun (map #(cullp %) (filter #(not (aget cmpsts %))
                                       (range 2 (inc root)))))
        (filter #(not (aget cmpsts %)) (range 2 (inc n))))))
```

**Alternative implementation using Clojure's side-effect oriented list comprehension.**

```mw
 (defn primes-to
  "Returns a lazy sequence of prime numbers less than lim"
  [lim]
  (let [refs (boolean-array (+ lim 1) true)
        root (int (Math/sqrt lim))]
    (do (doseq [i (range 2 lim)
                :while (<= i root)
                :when (aget refs i)]
          (doseq [j (range (* i i) lim i)]
            (aset refs j false)))
        (filter #(aget refs %) (range 2 lim)))))
```

**Alternative implementation using Clojure's side-effect oriented list comprehension. Odds only.**

```mw
(defn primes-to
  "Returns a lazy sequence of prime numbers less than lim"
  [lim]
  (let [max-i (int (/ (- lim 1) 2))
        refs (boolean-array max-i true)
        root (/ (dec (int (Math/sqrt lim))) 2)]
    (do (doseq [i (range 1 (inc root))
                :when (aget refs i)]
          (doseq [j (range (* (+ i i) (inc i)) max-i (+ i i 1))]
            (aset refs j false)))
        (cons 2 (map #(+ % % 1) 
                  (filter #(aget refs %) (range 1 max-i)))))))
```

This implemantation is about twice as fast as the previous one and uses only half the memory. From the index of the array, it calculates the value it represents as (2*i + 1), the step between two indices that represent the multiples of primes to mark as composite is also (2*i + 1). The index of the square of the prime to start composite marking is 2*i*(i+1).

**Alternative very slow entirely functional implementation using lazy sequences**

```mw
(defn primes-to
  "Computes lazy sequence of prime numbers up to a given number using sieve of Eratosthenes"
  [n]
  (letfn [(nxtprm [cs] ; current candidates
            (let [p (first cs)]
              (if (> p (Math/sqrt n)) cs
                (cons p (lazy-seq (nxtprm (-> (range (* p p) (inc n) p)
                                              set (remove cs) rest)))))))]
    (nxtprm (range 2 (inc n)))))
```

The reason that the above code is so slow is that it has has a high constant factor overhead due to using a (hash) set to remove the composites from the future composites stream, each prime composite stream removal requires a scan across all remaining composites (compared to using an array or vector where only the culled values are referenced, and due to the slowness of Clojure sequence operations as compared to iterator/sequence operations in other languages.

**Version based on immutable Vector's**

Here is an immutable boolean vector based non-lazy sequence version other than for the lazy sequence operations to output the result:

```mw
(defn primes-to
  "Computes lazy sequence of prime numbers up to a given number using sieve of Eratosthenes"
  [max-prime]
  (let [sieve (fn [s n]
                (if (<= (* n n) max-prime)
                  (recur (if (s n)
                           (reduce #(assoc %1 %2 false) s 
                                   (range (* n n) (inc max-prime) n))
                           s)
                         (inc n))
                  s))]
    (->> (-> (reduce conj (vector-of :boolean) 
                     (map #(= % %) (range (inc max-prime))))
             (assoc 0 false)
             (assoc 1 false)
             (sieve 2))
         (map-indexed #(vector %2 %1)) (filter first) (map second))))
```

The above code is still quite slow due to the cost of the immutable copy-on-modify operations.

**Odds only bit packed mutable array based version**

The following code implements an odds-only sieve using a mutable bit packed long array, only using a lazy sequence for the output of the resulting primes:

```mw
(set! *unchecked-math* true)

(defn primes-to
  "Computes lazy sequence of prime numbers up to a given number using sieve of Eratosthenes"
  [n]
  (let [root (-> n Math/sqrt long),
        rootndx (long (/ (- root 3) 2)),
        ndx (long (/ (- n 3) 2)),
        cmpsts (long-array (inc (/ ndx 64))),
        isprm #(zero? (bit-and (aget cmpsts (bit-shift-right % 6))
                               (bit-shift-left 1 (bit-and % 63)))),
        cullp (fn [i]
                (let [p (long (+ i i 3))]
                   (loop [i (bit-shift-right (- (* p p) 3) 1)]
                     (if (<= i ndx)
                       (do (let [w (bit-shift-right i 6)]
                       (aset cmpsts w (bit-or (aget cmpsts w)
                                              (bit-shift-left 1 (bit-and i 63)))))
                           (recur (+ i p))))))),
        cull (fn [] (loop [i 0] (if (<= i rootndx)
                                  (do (if (isprm i) (cullp i)) 
                                      (recur (inc i))))))]
    (letfn [(nxtprm [i] (if (<= i ndx)
                          (cons (+ i i 3) 
                            (lazy-seq (nxtprm (loop [i (inc i)]
                                                (if (or (> i ndx) (isprm i)) i
                                                  (recur (inc i)))))))))]
      (if (< n 2) nil
        (cons 3 (if (< n 3) nil (do (cull) (lazy-seq (nxtprm 0)))))))))
```

The above code is about as fast as any "one large sieving array" type of program in any computer language with this level of wheel factorization other than the lazy sequence operations are quite slow: it takes about ten times as long to enumerate the results as it does to do the actual sieving work of culling the composites from the sieving buffer array. The slowness of sequence operations is due to nested function calls, but primarily due to the way Clojure implements closures by "boxing" all arguments (and perhaps return values) as objects in the heap space, which then need to be "un-boxed" as primitives as necessary for integer operations. Some of the facilities provided by lazy sequences are not needed for this algorithm, such as the automatic memoization which means that each element of the sequence is calculated only once; it is not necessary for the sequence values to be retraced for this algorithm.

If further levels of wheel factorization were used, the time to enumerate the resulting primes would be an even higher overhead as compared to the actual composite number culling time, would get even higher if page segmentation were used to limit the buffer size to the size of the CPU L1 cache for many times better memory access times, most important in the culling operations, and yet higher again if multi-processing were used to share to page segment processing across CPU cores.

The following code overcomes many of those limitations by using an internal (OPSeq) "deftype" which implements the ISeq interface as well as the Counted interface to provide immediate count returns (based on a pre-computed total), as well as the IReduce interface which can greatly speed some computations up based on the primes sequence (eased greatly using facilities provided by Clojure 1.7.0 and up):

```mw
(defn primes-tox
  "Computes lazy sequence of prime numbers up to a given number using sieve of Eratosthenes"
  [n]
  (let [root (-> n Math/sqrt long),
        rootndx (long (/ (- root 3) 2)),
        ndx (max (long (/ (- n 3) 2)) 0),
        lmt (quot ndx 64),
        cmpsts (long-array (inc lmt)),
        cullp (fn [i]
                (let [p (long (+ i i 3))]
                   (loop [i (bit-shift-right (- (* p p) 3) 1)]
                     (if (<= i ndx)
                       (do (let [w (bit-shift-right i 6)]
                            (aset cmpsts w (bit-or 
                                             (aget cmpsts w)
                                             (bit-shift-left 1 (bit-and i 63)))))
                          (recur (+ i p))))))),
        cull (fn [] (do (aset cmpsts lmt (bit-or 
                                           (aget cmpsts lmt)
                                           (bit-shift-left -2 (bit-and ndx 63))))
                        (loop [i 0]
                          (when (<= i rootndx)
                            (when (zero? (bit-and 
                                           (aget cmpsts (bit-shift-right i 6))
                                           (bit-shift-left 1 (bit-and i 63))))
                              (cullp i))
                            (recur (inc i))))))
        numprms (fn []
                  (let [w (dec (alength cmpsts))] ;; fast results count bit counter
                    (loop [i 0, cnt (bit-shift-left (alength cmpsts) 6)]
                      (if (> i w) cnt
                        (recur (inc i) 
                               (- cnt (java.lang.Long/bitCount (aget cmpsts i))))))))]
    (if (< n 2) nil
      (cons 2 
        (if (< n 3) nil
          (do 
            (cull)
            (deftype OPSeq [^long i ^longs cmpsa ^long cnt ^long tcnt] 
              ;; for arrays maybe need to embed the array so that it 
              ;; doesn't get garbage collected???
              clojure.lang.ISeq
                (first [_] (if (nil? cmpsa) nil (+ i i 3)))
                (next [_] 
                    (let [ncnt (inc cnt)] 
                      (if (>= ncnt tcnt) nil
                        (OPSeq.
                          (loop [j (inc i)]
                            (let [p? (zero? (bit-and 
                                              (aget cmpsa (bit-shift-right j 6))
                                              (bit-shift-left 1 (bit-and j 63))))]
                              (if p? j (recur (inc j)))))
                          cmpsa ncnt tcnt))))
                (more [this] (let [ncnt (inc cnt)] 
                               (if (>= ncnt tcnt) (OPSeq. 0 nil tcnt tcnt)
                                 (.next this))))
                (cons [this o] (clojure.core/cons o this))
                (empty [_] (if (= cnt tcnt) nil (OPSeq. 0 nil tcnt tcnt)))
                (equiv [this o] (if (or (not= (type this) (type o))
                                        (not= cnt (.cnt ^OPSeq o))
                                        (not= tcnt (.tcnt ^OPSeq o))
                                        (not= i (.i ^OPSeq o))) 
                                  false true))
              clojure.lang.Counted
                (count [_] (- tcnt cnt))
              clojure.lang.Seqable
                (clojure.lang.Seqable/seq [this] (if (= cnt tcnt) nil this))
              clojure.lang.IReduce
                (reduce [_ f v] 
                    (let [c (- tcnt cnt)]
                      (if (<= c 0) nil
                        (loop [ci i, n c, rslt v]
                          (if (zero? (bit-and 
                                       (aget cmpsa (bit-shift-right ci 6))
                                       (bit-shift-left 1 (bit-and ci 63))))
                            (let [rrslt (f rslt (+ ci ci 3)),
                                  rdcd (reduced? rrslt),
                                  nrslt (if rdcd @rrslt rrslt)]
                              (if (or (<= n 1) rdcd) nrslt
                                (recur (inc ci) (dec n) nrslt)))
                            (recur (inc ci) n rslt))))))
                (reduce [this f]
                    (if (nil? i) (f) 
                      (if (= (.count this) 1) (+ i i 3)
                        (.reduce ^clojure.lang.IReduce
                                 (.next this) f (+ i i 3)))))
              clojure.lang.Sequential
              Object
                (toString [this] (if (= cnt tcnt) "()"
                                   (.toString (seq (map identity this)))))) 
            (->OPSeq 0 cmpsts 0 (numprms))))))))
```

'(time (count (primes-tox 10000000)))' takes about 40 milliseconds (compiled) to produce 664579.

Due to the better efficiency of the custom CIS type, the primes to the above range can be enumerated in about the same 40 milliseconds that it takes to cull and count the sieve buffer array.

Under Clojure 1.7.0, one can use '(time (reduce (fn [] (+ (long sum) (long v))) 0 (primes-tox 2000000)))' to find "142913828922" as the sum of the primes to two million as per Euler Problem 10 in about 40 milliseconds total with about half the time used for sieving the array and half for computing the sum.

To show how sensitive Clojure is to forms of expression of functions, the simple form '(time (reduce + (primes-tox 2000000)))' takes about twice as long even though it is using the same internal routine for most of the calculation due to the function not having the type coercion's.

Before one considers that this code is suitable for larger ranges, it is still lacks the improvements of page segmentation with pages about the size of the CPU L1/L2 caches (produces about a four times speed up), maximal wheel factorization (to make it another about four times faster), and the use of multi-processing (for a further gain of about 4 times for a multi-core desktop CPU such as an Intel i7), will make the sieving/counting code about 50 times faster than this, although there will only be a moderate improvement in the time to enumerate/process the resulting primes. Using these techniques, the number of primes to one billion can be counted in a small fraction of a second.

### Unbounded Versions

For some types of problems such as finding the nth prime (rather than the sequence of primes up to m), a prime sieve with no upper bound is a better tool.

The following variations on an incremental Sieve of Eratosthenes are based on or derived from the Richard Bird sieve as described in the Epilogue of Melissa E. O'Neill's definitive paper:

**A Clojure version of Richard Bird's Sieve using Lazy Sequences (sieves odds only)**

```mw
(defn primes-Bird
  "Computes the unbounded sequence of primes using a Sieve of Eratosthenes algorithm by Richard Bird."
  []
  (letfn [(mltpls [p] (let [p2 (* 2 p)]
                        (letfn [(nxtmltpl [c]
                                  (cons c (lazy-seq (nxtmltpl (+ c p2)))))]
                          (nxtmltpl (* p p))))),
          (allmtpls [ps] (cons (mltpls (first ps)) (lazy-seq (allmtpls (next ps))))),
          (union [xs ys] (let [xv (first xs), yv (first ys)]
                           (if (< xv yv) (cons xv (lazy-seq (union (next xs) ys)))
                             (if (< yv xv) (cons yv (lazy-seq (union xs (next ys))))
                               (cons xv (lazy-seq (union (next xs) (next ys)))))))),
          (mrgmltpls [mltplss] (cons (first (first mltplss))
                                     (lazy-seq (union (next (first mltplss))
                                                      (mrgmltpls (next mltplss)))))),
          (minusStrtAt [n cmpsts] (loop [n n, cmpsts cmpsts]
                                    (if (< n (first cmpsts))
                                      (cons n (lazy-seq (minusStrtAt (+ n 2) cmpsts)))
                                      (recur (+ n 2) (next cmpsts)))))]
    (do (def oddprms (cons 3 
                       (lazy-seq 
                         (let [cmpsts (-> oddprms (allmtpls) (mrgmltpls))]
                           (minusStrtAt 5 cmpsts)))))
        (cons 2 (lazy-seq oddprms)))))
```

The above code is quite slow due to both that the data structure is a linear merging of prime multiples and due to the slowness of the Clojure sequence operations.

**A Clojure version of the tree folding sieve using Lazy Sequences**

The following code speeds up the above code by merging the linear sequence of sequences as above by pairs into a right-leaning tree structure:

```mw
(defn primes-treeFolding
  "Computes the unbounded sequence of primes using a Sieve of Eratosthenes algorithm modified from Bird."
  []
  (letfn [(mltpls [p] (let [p2 (* 2 p)]
                        (letfn [(nxtmltpl [c]
                                  (cons c (lazy-seq (nxtmltpl (+ c p2)))))]
                          (nxtmltpl (* p p))))),
          (allmtpls [ps] (cons (mltpls (first ps)) (lazy-seq (allmtpls (next ps))))),
          (union [xs ys] (let [xv (first xs), yv (first ys)]
                           (if (< xv yv) (cons xv (lazy-seq (union (next xs) ys)))
                             (if (< yv xv) (cons yv (lazy-seq (union xs (next ys))))
                               (cons xv (lazy-seq (union (next xs) (next ys)))))))),
          (pairs [mltplss] (let [tl (next mltplss)]
                             (cons (union (first mltplss) (first tl))
                                   (lazy-seq (pairs (next tl)))))),
          (mrgmltpls [mltplss] (cons (first (first mltplss))
                                 (lazy-seq (union
                                             (next (first mltplss))
                                             (mrgmltpls (pairs (next mltplss))))))),
          (minusStrtAt [n cmpsts] (loop [n n, cmpsts cmpsts]
                                    (if (< n (first cmpsts))
                                      (cons n (lazy-seq (minusStrtAt (+ n 2) cmpsts)))
                                      (recur (+ n 2) (next cmpsts)))))]
    (do (def oddprms (cons 3 
                       (lazy-seq 
                         (let [cmpsts (-> oddprms (allmtpls) (mrgmltpls))]
                           (minusStrtAt 5 cmpsts)))))
        (cons 2 (lazy-seq oddprms)))))
```

The above code is still slower than it should be due to the slowness of Clojure's sequence operations.

**A Clojure version of the above tree folding sieve using a custom Co Inductive Sequence**

The following code uses a custom "deftype" non-memoizing Co Inductive Stream/Sequence (CIS) implementing the ISeq interface to make the sequence operations more efficient and is about four times faster than the above code:

```mw
(deftype CIS [v cont]
  clojure.lang.ISeq
    (first [_] v)
    (next [_] (if (nil? cont) nil (cont)))
    (more [this] (let [nv (.next this)] (if (nil? nv) (CIS. nil nil) nv)))
    (cons [this o] (clojure.core/cons o this))
    (empty [_] (if (and (nil? v) (nil? cont)) nil (CIS. nil nil)))
    (equiv [this o] (loop [cis1 this, cis2 o] 
                        (if (nil? cis1) (if (nil? cis2) true false)
                          (if (or (not= (type cis1) (type cis2))
                                  (not= (.v cis1) (.v ^CIS cis2))
                                  (and (nil? (.cont cis1))
                                       (not (nil? (.cont ^CIS cis2))))
                                  (and (nil? (.cont ^CIS cis2))
                                       (not (nil? (.cont cis1)))))
                            false
                            (if (nil? (.cont cis1)) true
                              (recur ((.cont cis1)) ((.cont ^CIS cis2))))))))
    (count [this] (loop [cis this, cnt 0] 
                    (if (or (nil? cis) (nil? (.cont cis))) cnt
                      (recur ((.cont cis)) (inc cnt)))))
  clojure.lang.Seqable
    (seq [this] (if (and (nil? v) (nil? cont)) nil this))
  clojure.lang.Sequential
  Object
    (toString [this] (if (and (nil? v) (nil? cont)) "()" 
                       (.toString (seq (map identity this))))))

(defn primes-treeFoldingx
  "Computes the unbounded sequence of primes using a Sieve of Eratosthenes algorithm modified from Bird."
  []
  (letfn [(mltpls [p] (let [p2 (* 2 p)]
                        (letfn [(nxtmltpl [c]
                                  (->CIS c (fn [] (nxtmltpl (+ c p2)))))]
                          (nxtmltpl (* p p))))),
          (allmtpls [^CIS ps] (->CIS (mltpls (.v ps)) 
                                (fn [] (allmtpls ((.cont ps)))))),
          (union [^CIS xs ^CIS ys]
                  (let [xv (.v xs), yv (.v ys)]
                    (if (< xv yv) (->CIS xv (fn [] (union ((.cont xs)) ys)))
                      (if (< yv xv) (->CIS yv (fn [] (union xs ((.cont ys)))))
                        (->CIS xv (fn [] (union (next xs) ((.cont ys))))))))),
          (pairs [^CIS mltplss] (let [^CIS tl ((.cont mltplss))]
                                  (->CIS (union (.v mltplss) (.v tl))
                                         (fn [] (pairs ((.cont tl))))))),
          (mrgmltpls [^CIS mltplss] 
                  (->CIS (.v ^CIS (.v mltplss))
                         (fn [] (union ((.cont ^CIS (.v mltplss)))
                                       (mrgmltpls (pairs ((.cont mltplss)))))))),
          (minusStrtAt [n ^CIS cmpsts]
                  (loop [n n, cmpsts cmpsts]
                    (if (< n (.v cmpsts))
                      (->CIS n (fn [] (minusStrtAt (+ n 2) cmpsts)))
                      (recur (+ n 2) ((.cont cmpsts))))))]
    (do (def oddprms (->CIS 3
                         (fn [] 
                           (let [cmpsts (-> oddprms (allmtpls) (mrgmltpls))]
                             (minusStrtAt 5 cmpsts)))))
        (->CIS 2 (fn [] oddprms)))))
```

'(time (count (take-while #(<= (long %) 10000000) (primes-treeFoldingx))))' takes about 3.4 seconds for a range of 10 million.

The above code is useful for ranges up to about fifteen million primes, which is about the first million primes; it is comparable in speed to all of the bounded versions except for the fastest bit packed version which can reasonably be used for ranges about 100 times as large.

**Incremental Hash Map based unbounded "odds-only" version**

The following code is a version of the O'Neill Haskell code but does not use wheel factorization other than for sieving odds only (although it could be easily added) and uses a Hash Map (constant amortized access time) rather than a Priority Queue (log n access time for combined remove-and-insert-anew operations, which are the majority used for this algorithm) with a lazy sequence for output of the resulting primes; the code has the added feature that it uses a secondary base primes sequence generator and only adds prime culling sequences to the composites map when they are necessary, thus saving time and limiting storage to only that required for the map entries for primes up to the square root of the currently sieved number:

```mw
(defn primes-hashmap
  "Infinite sequence of primes using an incremental Sieve or Eratosthenes with a Hashmap"
  []
  (letfn [(nxtoddprm [c q bsprms cmpsts]
            (if (>= c q) ;; only ever equal
              (let [p2 (* (first bsprms) 2), nbps (next bsprms), nbp (first nbps)]
                (recur (+ c 2) (* nbp nbp) nbps (assoc cmpsts (+ q p2) p2)))
              (if (contains? cmpsts c)
                (recur (+ c 2) q bsprms
                       (let [adv (cmpsts c), ncmps (dissoc cmpsts c)]
                         (assoc ncmps
                                (loop [try (+ c adv)] ;; ensure map entry is unique
                                  (if (contains? ncmps try)
                                    (recur (+ try adv)) try)) adv)))
                (cons c (lazy-seq (nxtoddprm (+ c 2) q bsprms cmpsts))))))]
    (do (def baseoddprms (cons 3 (lazy-seq (nxtoddprm 5 9 baseoddprms {}))))
        (cons 2 (lazy-seq (nxtoddprm 3 9 baseoddprms {}))))))
```

The above code is slower than the best tree folding version due to the added constant factor overhead of computing the hash functions for every hash map operation even though it has computational complexity of (n log log n) rather than the worse (n log n log log n) for the previous incremental tree folding sieve. It is still about 100 times slower than the sieve based on the bit-packed mutable array due to these constant factor hashing overheads.

There is almost no benefit of converting the above code to use a CIS as most of the time is expended in the hash map functions.

**Incremental Priority Queue based unbounded "odds-only" version**

In order to implement the O'Neill Priority Queue incremental Sieve of Eratosthenes algorithm, one requires an efficient implementation of a Priority Queue, which is not part of standard Clojure. For this purpose, the most suitable Priority Queue is a binary tree heap based MinHeap algorithm. The following code implements a purely functional (using entirely immutable state) MinHeap Priority Queue providing the required functions of (emtpy-pq) initialization, (getMin-pq pq) to examinte the minimum key/value pair in the queue, (insert-pq pq k v) to add entries to the queue, and (replaceMinAs-pq pq k v) to replaace the minimum entry with a key/value pair as given (it is more efficient that if functions were provided to delete and then re-insert entries in the queue; there is therefore no "delete" or other queue functions supplied as the algorithm does not requrie them:

```mw
(deftype PQEntry [k, v]
  Object
    (toString [_] (str "<" k "," v ">")))
(deftype PQNode [ntry, lft, rght]
  Object
    (toString [_] (str "<" ntry " left: " (str lft) " right: " (str rght) ">")))

(defn empty-pq [] nil)

(defn getMin-pq [^PQNode pq]
  (if (nil? pq)
    nil
    (.ntry pq)))

(defn insert-pq [^PQNode opq ok v]
  (loop [^PQEntry kv (->PQEntry ok v), pq opq, cont identity]
    (if (nil? pq)
      (cont (->PQNode kv nil nil))
      (let [k (.k kv),
            ^PQEntry kvn (.ntry pq), kn (.k kvn),
            l (.lft pq), r (.rght pq)]
        (if (<= k kn)
          (recur kvn r #(cont (->PQNode kv % l)))
          (recur kv r #(cont (->PQNode kvn % l))))))))

(defn replaceMinAs-pq [^PQNode opq k v]
  (let [^PQEntry kv (->PQEntry k v)]
    (if (nil? opq) ;; if was empty or just an entry, just use current entry
      (->PQNode kv nil nil)
      (loop [pq opq, cont identity]
        (let [^PQNode l (.lft pq), ^PQNode r (.rght pq)]
          (cond ;; if left us empty, right must be too
            (nil? l)
              (cont (->PQNode kv nil nil)),
            (nil? r) ;; we only have a left...
              (let [^PQEntry kvl (.ntry l), kl (.k kvl)]
                    (if (<= k kl)
                      (cont (->PQNode kv l nil))
                      (recur l #(cont (->PQNode kvl % nil))))),
            :else (let [^PQEntry kvl (.ntry l), kl (.k kvl),
                        ^PQEntry kvr (.ntry r), kr (.k kvr)] ;; we have both
                    (if (and (<= k kl) (<= k kr))
                      (cont (->PQNode kv l r))
                      (if (<= kl kr)
                        (recur l #(cont (->PQNode kvl % r)))
                        (recur r #(cont (->PQNode kvr l %))))))))))))
```

Note that the above code is written partially using continuation passing style so as to leave the "recur" calls in tail call position as required for efficient looping in Clojure; for practical sieving ranges, the algorithm could likely use just raw function recursion as recursion depth is unlikely to be used beyond a depth of about ten or so, but raw recursion is said to be less code efficient.

The actual incremental sieve using the Priority Queue is as follows, which code uses the same optimizations of postponing the addition of prime composite streams to the queue until the square root of the currently sieved number is reached and using a secondary base primes stream to generate the primes composite stream markers in the queue as was used for the Hash Map version:

```mw
(defn primes-pq
  "Infinite sequence of primes using an incremental Sieve or Eratosthenes with a Priority Queue"
  []
  (letfn [(nxtoddprm [c q bsprms cmpsts]
            (if (>= c q) ;; only ever equal
              (let [p2 (* (first bsprms) 2), nbps (next bsprms), nbp (first nbps)]
                (recur (+ c 2) (* nbp nbp) nbps (insert-pq cmpsts (+ q p2) p2)))
              (let [mn (getMin-pq cmpsts)]
                (if (and mn (>= c (.k mn))) ;; never greater than
                  (recur (+ c 2) q bsprms
                         (loop [adv (.v mn), cmps cmpsts] 
                           ;; advance repeat composites for value
                           (let [ncmps (replaceMinAs-pq cmps (+ c adv) adv),
                                 nmn (getMin-pq ncmps)]
                             (if (and nmn (>= c (.k nmn)))
                               (recur (.v nmn) ncmps)
                               ncmps))))
                  (cons c (lazy-seq (nxtoddprm (+ c 2) q bsprms cmpsts)))))))]
    (do (def baseoddprms (cons 3 (lazy-seq (nxtoddprm 5 9 baseoddprms (empty-pq)))))
        (cons 2 (lazy-seq (nxtoddprm 3 9 baseoddprms (empty-pq)))))))
```

The above code is faster than the Hash Map version up to about a sieving range of fifteen million or so, but gets progressively slower for larger ranges due to having (n log n log log n) computational complexity rather than the (n log log n) for the Hash Map version, which has a higher constant factor overhead that is overtaken by the extra "log n" factor.

It is slower that the fastest of the tree folding versions (which has the same computational complexity) due to the higher constant factor overhead of the Priority Queue operations (although perhaps a more efficient implementation of the MinHeap Priority Queue could be developed).

Again, these non-mutable array based sieves are about a hundred times slower than even the "one large memory buffer array" version as implemented in the bounded section; a page segmented version of the mutable bit-packed memory array would be several times faster.

All of these algorithms will respond to maximum wheel factorization, getting up to approximately four times faster if this is applied as compared to the the "odds-only" versions.

It is difficult if not impossible to apply efficient multi-processing to the above versions of the unbounded sieves as the next values of the primes sequence are dependent on previous changes of state for the Bird and Tree Folding versions; however, with the addition of a "update the whole Priority Queue (and reheapify)" or "update the Hash Map" to a given page start state functions, it is possible to do for these letter two algorithms; however, even though it is possible and there is some benefit for these latter two implementations, the benefit is less than using mutable arrays due to that the results must be enumerated into a data structure of some sort in order to be passed out of the page function whereas they can be directly enumerated from the array for the mutable array versions.

**Bit packed page segmented array unbounded "odds-only" version**

To show that Clojure does not need to be particularly slow, the following version runs about twice as fast as the non-segmented unbounded array based version above (extremely fast compared to the non-array based versions) and only a little slower than other equivalent versions running on virtual machines: C# or F# on DotNet or Java and Scala on the JVM:

```mw
(set! *unchecked-math* true)

(def PGSZ (bit-shift-left 1 14)) ;; size of CPU cache
(def PGBTS (bit-shift-left PGSZ 3))
(def PGWRDS (bit-shift-right PGBTS 5))
(def BPWRDS (bit-shift-left 1 7)) ;; smaller page buffer for base primes
(def BPBTS (bit-shift-left BPWRDS 5))
(defn- count-pg
  "count primes in the culled page buffer, with test for limit"
  [lmt ^ints pg]
  (let [pgsz (alength pg),
        pgbts (bit-shift-left pgsz 5),
        cntem (fn [lmtw]
                (let [lmtw (long lmtw)]
             (loop [i (long 0), c (long 0)]
               (if (>= i lmtw) (- (bit-shift-left lmtw 5) c)
                 (recur (inc i)
                 (+ c (java.lang.Integer/bitCount (aget pg i))))))))]
    (if (< lmt pgbts)
      (let [lmtw (bit-shift-right lmt 5),
            lmtb (bit-and lmt 31)
            msk (bit-shift-left -2 lmtb)]
        (+ (cntem lmtw)
           (- 32 (java.lang.Integer/bitCount (bit-or (aget pg lmtw)
                                                      msk)))))
      (- pgbts
         (areduce pg i ret (long 0) 
                  (+ ret (java.lang.Integer/bitCount (aget pg i))))))))
;;      (cntem pgsz))))
(defn- primes-pages
  "unbounded Sieve of Eratosthenes producing a lazy sequence of culled page buffers."
  []
  (letfn [(make-pg [lowi pgsz bpgs]
            (let [lowi (long lowi),
                  pgbts (long (bit-shift-left pgsz 5)),
                  pgrng (long (+ (bit-shift-left (+ lowi pgbts) 1) 3)),
                  ^ints pg (int-array pgsz),
                  cull (fn [bpgs']
                         (loop [i (long 0), bpgs' bpgs']
                            (let [^ints fbpg (first bpgs'),
                                  bpgsz (long (alength fbpg))]
                              (if (>= i bpgsz)
                                (recur 0 (next bpgs'))
                                (let [p (long (aget fbpg i)),
                                      sqr (long (* p p))]
                                  (if (< sqr pgrng) (do
                   (loop [j (long (let [s (long (bit-shift-right (- sqr 3) 1))]
                                     (if (>= s lowi) (- s lowi)
                                       (let [m (long (rem (- lowi s) p))]
                                         (if (zero? m)
                                           0
                                           (- p m))))))]
                     (if (< j pgbts) ;; fast inner culling loop where most time is spent
                       (do
                         (let [w (bit-shift-right j 5)]
                           (aset pg w (int (bit-or (aget pg w)
                                                   (bit-shift-left 1 (bit-and j 31))))))
                         (recur (+ j p)))))
                     (recur (inc i) bpgs'))))))))]
              (do (if (nil? bpgs)
                    (letfn [(mkbpps [i]
                              (if (zero? (bit-and (aget pg (bit-shift-right i 5))
                                                  (bit-shift-left 1 (bit-and i 31))))
                                (cons (int-array 1 (+ i i 3)) (lazy-seq (mkbpps (inc i))))
                                (recur (inc i))))]
                      (cull (mkbpps 0)))
                    (cull bpgs))
                  pg))),
          (page-seq [lowi pgsz bps]
            (letfn [(next-seq [lwi]
                      (cons (make-pg lwi pgsz bps)
                            (lazy-seq (next-seq (+ lwi (bit-shift-left pgsz 5))))))]
              (next-seq lowi)))
          (pgs->bppgs [ppgs]
            (letfn [(nxt-pg [lowi pgs]
                      (let [^ints pg (first pgs),
                            cnt (count-pg BPBTS pg),
                            npg (int-array cnt)]
                        (do (loop [i 0, j 0]
                              (if (< i BPBTS)
                                (if (zero? (bit-and (aget pg (bit-shift-right i 5))
                                                    (bit-shift-left 1 (bit-and i 31))))
                                  (do (aset npg j (+ (bit-shift-left (+ lowi i) 1) 3))
                                      (recur (inc i) (inc j)))
                                  (recur (inc i) j))))
                            (cons npg (lazy-seq (nxt-pg (+ lowi BPBTS) (next pgs)))))))]
              (nxt-pg 0 ppgs))),
          (make-base-prms-pgs []
            (pgs->bppgs (cons (make-pg 0 BPWRDS nil)
                              (lazy-seq (page-seq BPBTS BPWRDS (make-base-prms-pgs))))))]
    (page-seq 0 PGWRDS (make-base-prms-pgs))))
(defn primes-paged
  "unbounded Sieve of Eratosthenes producing a lazy sequence of primes"
  []
  (do (deftype CIS [v cont]
        clojure.lang.ISeq
          (first [_] v)
          (next [_] (if (nil? cont) nil (cont)))
          (more [this] (let [nv (.next this)] (if (nil? nv) (CIS. nil nil) nv)))
          (cons [this o] (clojure.core/cons o this))
          (empty [_] (if (and (nil? v) (nil? cont)) nil (CIS. nil nil)))
          (equiv [this o] (loop [cis1 this, cis2 o] 
                            (if (nil? cis1) (if (nil? cis2) true false)
                              (if (or (not= (type cis1) (type cis2))
                                      (not= (.v cis1) (.v ^CIS cis2))
                                      (and (nil? (.cont cis1))
                                           (not (nil? (.cont ^CIS cis2))))
                                      (and (nil? (.cont ^CIS cis2))
                                           (not (nil? (.cont cis1)))))
                                  false
                                  (if (nil? (.cont cis1)) true
                                     (recur ((.cont cis1)) ((.cont ^CIS cis2))))))))
          (count [this] (loop [cis this, cnt 0] 
                          (if (or (nil? cis) (nil? (.cont cis))) cnt
                            (recur ((.cont cis)) (inc cnt)))))
        clojure.lang.Seqable
          (seq [this] (if (and (nil? v) (nil? cont)) nil this))
        clojure.lang.Sequential
        Object
          (toString [this] (if (and (nil? v) (nil? cont)) "()"
                             (.toString (seq (map identity this))))))
        (letfn [(next-prm [lowi i pgseq]
                  (let [lowi (long lowi),
                      i (long i),
                      ^ints pg (first pgseq),
                        pgsz (long (alength pg)),
                        pgbts (long (bit-shift-left pgsz 5)),
                        ni (long (loop [j (long i)]
                                   (if (or (>= j pgbts)
                                           (zero? (bit-and (aget pg (bit-shift-right j 5))
                                                     (bit-shift-left 1 (bit-and j 31)))))
                                     j
                                     (recur (inc j)))))]
                    (if (>= ni pgbts)
                      (recur (+ lowi pgbts) 0 (next pgseq))
                      (->CIS (+ (bit-shift-left (+ lowi ni) 1) 3)
                             (fn [] (next-prm lowi (inc ni) pgseq))))))]
          (->CIS 2 (fn [] (next-prm 0 0 (primes-pages)))))))
(defn primes-paged-count-to
  "counts primes generated by page segments by Sieve of Eratosthenes to the top limit"
  [top]
  (cond (< top 2) 0
        (< top 3) 1
        :else (letfn [(nxt-pg [lowi pgseq cnt]
                        (let [topi (bit-shift-right (- top 3) 1)
                              nxti (+ lowi PGBTS),
                              pg (first pgseq)]
                          (if (> nxti topi)
                            (+ cnt (count-pg (- topi lowi) pg))
                            (recur nxti
                                   (next pgseq)
                                   (+ cnt (count-pg PGBTS pg))))))]
                (nxt-pg 0 (primes-pages) 1))))
```

The above code runs just as fast as other virtual machine languages when run on a 64-bit JVM; however, when run on a 32-bit JVM it runs almost five times slower. This is likely due to Clojure only using 64-bit integers for integer operations and these operations getting JIT compiled to use library functions to simulate those operations using combined 32-bit operations under a 32-bit JVM whereas direct CPU operations can be used on a 64-bit JVM

Clojure does one thing very slowly, just as here: it enumerates extremely slowly as compared to using a more imperative iteration interface; it helps to use a roll-your-own ISeq interface as here, where enumeration of the primes reduces the time from about four times as long as the composite culling operations for those primes to only about one and a half times as long, although one must also write their own sequence handling functions (can't use "take-while" or "count", for instance) in order to enjoy that benefit. That is why the "primes-paged-count-to" function is provided so it takes a negligible percentage of the time to count the primes over a range as compared to the time for the composite culling operations.

The practical range of the above sieve is about 16 million due to the fixed size of the page buffers; in order to extend the range, a larger page buffer could be used up to the size of the CPU L2 or L3 caches. If a 2^20 buffer were used (one Megabyte, as many modern dexktop CPU's easily have in their L3 cache), then the range would be increased up to about 10^14 at a cost of about a factor of two or three in slower memory accesses per composite culling operation loop. The base primes culling page size is already adequate for this range. One could make the culling page size automatically expand with growing range by about the square root of the current prime range with not too many changes to the code.

As for many implementations of unbounded sieves, the base primes less than the square root of the current range are generated by a secondary generated stream of primes; in this case it is done recursively, so another secondary stream generates the base primes for the base primes and so on down to where the innermost generator has only one page in the stream; this only takes one or two recursions for this type of range.

The base primes culling page size is reduced from the page size for the main primes so that there is less overhead for smaller primes ranges; otherwise excess base primes are generated for fairly small sieve ranges.


## CLU

```mw
% Sieve of Eratosthenes
eratosthenes = proc (n: int) returns (array[bool])
    prime: array[bool] := array[bool]$fill(1, n, true)
    prime[1] := false

    for p: int in int$from_to(2, n/2) do
        if prime[p] then
            for c: int in int$from_to_by(p*p, n, p) do
                prime[c] := false
            end
        end
    end
    return(prime)
end eratosthenes

% Print primes up to 1000 using the sieve
start_up = proc ()
    po: stream := stream$primary_output()
    prime: array[bool] := eratosthenes(1000)
    col: int := 0

    for i: int in array[bool]$indexes(prime) do
        if prime[i] then
            col := col + 1
            stream$putright(po, int$unparse(i), 5)
            if col = 10 then
                col := 0
                stream$putc(po, '\n')
            end
        end
    end
end start_up
```

**Output:**

```
    2    3    5    7   11   13   17   19   23   29
   31   37   41   43   47   53   59   61   67   71
   73   79   83   89   97  101  103  107  109  113
  127  131  137  139  149  151  157  163  167  173
  179  181  191  193  197  199  211  223  227  229
  233  239  241  251  257  263  269  271  277  281
  283  293  307  311  313  317  331  337  347  349
  353  359  367  373  379  383  389  397  401  409
  419  421  431  433  439  443  449  457  461  463
  467  479  487  491  499  503  509  521  523  541
  547  557  563  569  571  577  587  593  599  601
  607  613  617  619  631  641  643  647  653  659
  661  673  677  683  691  701  709  719  727  733
  739  743  751  757  761  769  773  787  797  809
  811  821  823  827  829  839  853  857  859  863
  877  881  883  887  907  911  919  929  937  941
  947  953  967  971  977  983  991  997
```


## CMake

```mw
function(eratosthenes var limit)
  # Check for integer overflow. With CMake using 32-bit signed integer,
  # this check fails when limit > 46340.
  if(NOT limit EQUAL 0)         # Avoid division by zero.
    math(EXPR i "(${limit} * ${limit}) / ${limit}")
    if(NOT limit EQUAL ${i})
      message(FATAL_ERROR "limit is too large, would cause integer overflow")
    endif()
  endif()

  # Use local variables prime_2, prime_3, ..., prime_${limit} as array.
  # Initialize array to y => yes it is prime.
  foreach(i RANGE 2 ${limit})
    set(prime_${i} y)
  endforeach(i)

  # Gather a list of prime numbers.
  set(list)
  foreach(i RANGE 2 ${limit})
    if(prime_${i})
      # Append this prime to list.
      list(APPEND list ${i})

      # For each multiple of i, set n => no it is not prime.
      # Optimization: start at i squared.
      math(EXPR square "${i} * ${i}")
      if(NOT square GREATER ${limit})   # Avoid fatal error.
        foreach(m RANGE ${square} ${limit} ${i})
          set(prime_${m} n)
        endforeach(m)
      endif()
    endif(prime_${i})
  endforeach(i)
  set(${var} ${list} PARENT_SCOPE)
endfunction(eratosthenes)
```

```
# Print all prime numbers through 100.
eratosthenes(primes 100)
message(STATUS "${primes}")
```
