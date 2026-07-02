---
title: "Sieve of Eratosthenes (part 11/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 11/21
---

## Janet

### Simple, all primes below a limit

Janet has a builtin "buffer" type which is used as a mutable byte string. It has builtin utility methods to handle bit strings (see here :)

This is based off the Python version.

```mw
(defn primes-before
  "Gives all the primes < limit"
  [limit]
  (assert (int? limit))
  # Janet has a buffer type (mutable string) which has easy methods for use as bitset
  (def buf-size (math/ceil (/ limit 8)))
  (def is-prime (buffer/new-filled buf-size (bnot 0)))
  (print "Size" buf-size "is-prime: " is-prime)
  (buffer/bit-clear is-prime 0)
  (buffer/bit-clear is-prime 1)
  (for n 0 (math/ceil (math/sqrt limit))
    (if (buffer/bit is-prime n) (loop [i :range-to [(* n n) limit n]]
      (buffer/bit-clear is-prime i))))
  (def res @[]) # Result: Mutable array
  (for i 0 limit
    (if (buffer/bit is-prime i)
      (array/push res i)))
  (def res (array/new limit))
  (for i 0 limit
    (if (buffer/bit is-prime i)
      (array/push res i)))
  res)
```


## Java

Works with

:

Java

version 1.5+

```mw
import java.util.LinkedList;

public class Sieve{
       public static LinkedList<Integer> sieve(int n){
               if(n < 2) return new LinkedList<Integer>();
               LinkedList<Integer> primes = new LinkedList<Integer>();
               LinkedList<Integer> nums = new LinkedList<Integer>();

               for(int i = 2;i <= n;i++){ //unoptimized
                       nums.add(i);
               }

               while(nums.size() > 0){
                       int nextPrime = nums.remove();
                       for(int i = nextPrime * nextPrime;i <= n;i += nextPrime){
                               nums.removeFirstOccurrence(i);
                       }
                       primes.add(nextPrime);
               }
               return primes;
       }
}
```

To optimize by testing only odd numbers, replace the loop marked "unoptimized" with these lines:

```mw
nums.add(2);
for(int i = 3;i <= n;i += 2){
       nums.add(i);
}
```

Version using List:

```mw
import java.util.ArrayList;
import java.util.List;
 
public class Eratosthenes {
    public List<Integer> sieve(Integer n) {
        List<Integer> primes = new ArrayList<Integer>(n);
        boolean[] isComposite = new boolean[n + 1];
        for(int i = 2; i <= n; i++) {
            if(!isComposite[i]) {
                primes.add(i);
                for(int j = i * i; j <= n; j += i) {
                    isComposite[j] = true;
                }
            }
        }
        return primes;
    }
}
```

Version using a BitSet:

```mw
import java.util.LinkedList;
import java.util.BitSet;

public class Sieve{
    public static LinkedList<Integer> sieve(int n){
        LinkedList<Integer> primes = new LinkedList<Integer>();
        BitSet nonPrimes = new BitSet(n+1);
        
        for (int p = 2; p <= n ; p = nonPrimes.nextClearBit(p+1)) {
            for (int i = p * p; i <= n; i += p)
                nonPrimes.set(i);
            primes.add(p);
        }
        return primes;
    }
}
```

Version using a TreeSet:

```mw
import java.util.Set;
import java.util.TreeSet;

public class Sieve{
    public static Set<Integer> findPrimeNumbers(int limit) {
    int last = 2;
    TreeSet<Integer> nums = new TreeSet<>();

    if(limit < last) return nums;

    for(int i = last; i <= limit; i++){
      nums.add(i);
    }

    return filterList(nums, last, limit);
  }

  private static TreeSet<Integer> filterList(TreeSet<Integer> list, int last, int limit) {
    int squared = last*last;
    if(squared < limit) {
      for(int i=squared; i <= limit; i += last) {
        list.remove(i);
      }
      return filterList(list, list.higher(last), limit);
    } 
    return list; 
  }
}
```

### Infinite iterator

An iterator that will generate primes indefinitely (perhaps until it runs out of memory), but very slowly.

Translation of

:

Python

Works with

:

Java

version 1.5+

```mw
import java.util.Iterator;
import java.util.PriorityQueue;
import java.math.BigInteger;

// generates all prime numbers
public class InfiniteSieve implements Iterator<BigInteger> {

    private static class NonPrimeSequence implements Comparable<NonPrimeSequence> {
   BigInteger currentMultiple;
   BigInteger prime;

   public NonPrimeSequence(BigInteger p) {
       prime = p;
       currentMultiple = p.multiply(p); // start at square of prime
   }
   @Override public int compareTo(NonPrimeSequence other) {
       // sorted by value of current multiple
       return currentMultiple.compareTo(other.currentMultiple);
   }
    }

    private BigInteger i = BigInteger.valueOf(2);
    // priority queue of the sequences of non-primes
    // the priority queue allows us to get the "next" non-prime quickly
    final PriorityQueue<NonPrimeSequence> nonprimes = new PriorityQueue<NonPrimeSequence>();

    @Override public boolean hasNext() { return true; }
    @Override public BigInteger next() {
   // skip non-prime numbers
   for ( ; !nonprimes.isEmpty() && i.equals(nonprimes.peek().currentMultiple); i = i.add(BigInteger.ONE)) {
            // for each sequence that generates this number,
            // have it go to the next number (simply add the prime)
            // and re-position it in the priority queue
       while (nonprimes.peek().currentMultiple.equals(i)) {
      NonPrimeSequence x = nonprimes.poll();
      x.currentMultiple = x.currentMultiple.add(x.prime);
      nonprimes.offer(x);
       }
   }
   // prime
        // insert a NonPrimeSequence object into the priority queue
   nonprimes.offer(new NonPrimeSequence(i));
   BigInteger result = i;
   i = i.add(BigInteger.ONE);
   return result;
    }

    public static void main(String[] args) {
   Iterator<BigInteger> sieve = new InfiniteSieve();
   for (int i = 0; i < 25; i++) {
       System.out.println(sieve.next());
   }
    }
}
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
```

### Infinite iterator with a faster algorithm (sieves odds-only)

The adding of each discovered prime's incremental step information to the mapping should be postponed until the candidate number reaches the primes square, as it is useless before that point. This drastically reduces the space complexity from O(n/log(n)) to O(sqrt(n/log(n))), in n primes produced, and also lowers the run time complexity due to the use of the hash table based HashMap, which is much more efficient for large ranges.

Translation of

:

Python

Works with

:

Java

version 1.5+

```mw
import java.util.Iterator;
import java.util.HashMap;
 
// generates all prime numbers up to about 10 ^ 19 if one can wait 1000's of years or so...
public class SoEInfHashMap implements Iterator<Long> {

  long candidate = 2;
  Iterator<Long> baseprimes = null;
  long basep = 3;
  long basepsqr = 9;
  // HashMap of the sequences of non-primes
  // the hash map allows us to get the "next" non-prime reasonably quickly
  // but further allows re-insertions to take amortized constant time
  final HashMap<Long,Long> nonprimes = new HashMap<>();

  @Override public boolean hasNext() { return true; }
  @Override public Long next() {
    // do the initial primes separately to initialize the base primes sequence
    if (this.candidate <= 5L) if (this.candidate++ == 2L) return 2L; else {
      this.candidate++; if (this.candidate == 5L) return 3L; else {
        this.baseprimes = new SoEInfHashMap();
        this.baseprimes.next(); this.baseprimes.next(); // throw away 2 and 3
        return 5L;
    } }
    // skip non-prime numbers including squares of next base prime
    for ( ; this.candidate >= this.basepsqr || //equals nextbase squared => not prime
              nonprimes.containsKey(this.candidate); candidate += 2) {
      // insert a square root prime sequence into hash map if to limit
      if (candidate >= basepsqr) { // if square of base prime, always equal
        long adv = this.basep << 1;
        nonprimes.put(this.basep * this.basep + adv, adv);
        this.basep = this.baseprimes.next();
        this.basepsqr = this.basep * this.basep;
      }
      // else for each sequence that generates this number,
      // have it go to the next number (simply add the advance)
      // and re-position it in the hash map at an emply slot
      else {
        long adv = nonprimes.remove(this.candidate);
        long nxt = this.candidate + adv;
        while (this.nonprimes.containsKey(nxt)) nxt += adv; //unique keys
        this.nonprimes.put(nxt, adv);
      }
    }
    // prime
    long tmp = candidate; this.candidate += 2; return tmp;
  }

  public static void main(String[] args) {    
    int n = 100000000;    
    long strt = System.currentTimeMillis();    
    SoEInfHashMap sieve = new SoEInfHashMap();
    int count = 0;
    while (sieve.next() <= n) count++;    
    long elpsd = System.currentTimeMillis() - strt;    
    System.out.println("Found " + count + " primes up to " + n + " in " + elpsd + " milliseconds.");
  }
  
}
```

**Output:**

```
Found 5761455 primes up to 100000000 in 4297 milliseconds.
```

### Infinite iterator with a very fast page segmentation algorithm (sieves odds-only)

Although somewhat faster than the previous infinite iterator version, the above code is still over 10 times slower than an infinite iterator based on array paged segmentation as in the following code, where the time to enumerate/iterate over the found primes (common to all the iterators) is now about half of the total execution time:

Translation of

:

JavaScript

Works with

:

Java

version 1.5+

```mw
import java.util.Iterator;
import java.util.ArrayList;

// generates all prime numbers up to about 10 ^ 19 if one can wait 100's of years or so...
// practical range is about 10^14 in a week or so...
public class SoEPagedOdds implements Iterator<Long> {
  private final int BFSZ = 1 << 16;
  private final int BFBTS = BFSZ * 32;
  private final int BFRNG = BFBTS * 2;
  private long bi = -1;
  private long lowi = 0;
  private final ArrayList<Integer> bpa = new ArrayList<>();
  private Iterator<Long> bps;
  private final int[] buf = new int[BFSZ];
  
  @Override public boolean hasNext() { return true; }
  @Override public Long next() {
    if (this.bi < 1) {
      if (this.bi < 0) {
        this.bi = 0;
        return 2L;
      }
      //this.bi muxt be 0
      long nxt = 3 + (this.lowi << 1) + BFRNG;
      if (this.lowi <= 0) { // special culling for first page as no base primes yet:
          for (int i = 0, p = 3, sqr = 9; sqr < nxt; i++, p += 2, sqr = p * p)
              if ((this.buf[i >>> 5] & (1 << (i & 31))) == 0)
                  for (int j = (sqr - 3) >> 1; j < BFBTS; j += p)
                      this.buf[j >>> 5] |= 1 << (j & 31);
      }
      else { // after the first page:
        for (int i = 0; i < this.buf.length; i++)
          this.buf[i] = 0; // clear the sieve buffer
        if (this.bpa.isEmpty()) { // if this is the first page after the zero one:
            this.bps = new SoEPagedOdds(); // initialize separate base primes stream:
            this.bps.next(); // advance past the only even prime of two
            this.bpa.add(this.bps.next().intValue()); // get the next prime (3 in this case)
        }
        // get enough base primes for the page range...
        for (long p = this.bpa.get(this.bpa.size() - 1), sqr = p * p; sqr < nxt;
                p = this.bps.next(), this.bpa.add((int)p), sqr = p * p) ;
        for (int i = 0; i < this.bpa.size() - 1; i++) {
          long p = this.bpa.get(i);
          long s = (p * p - 3) >>> 1;
          if (s >= this.lowi) // adjust start index based on page lower limit...
            s -= this.lowi;
          else {
            long r = (this.lowi - s) % p;
            s = (r != 0) ? p - r : 0;
          }
          for (int j = (int)s; j < BFBTS; j += p)
            this.buf[j >>> 5] |= 1 << (j & 31);
        }
      }
    }
    while ((this.bi < BFBTS) &&
           ((this.buf[(int)this.bi >>> 5] & (1 << ((int)this.bi & 31))) != 0))
        this.bi++; // find next marker still with prime status
    if (this.bi < BFBTS) // within buffer: output computed prime
        return 3 + ((this.lowi + this.bi++) << 1);
    else { // beyond buffer range: advance buffer
        this.bi = 0;
        this.lowi += BFBTS;
        return this.next(); // and recursively loop
    }
  }

  public static void main(String[] args) {    
    long n = 1000000000;
    long strt = System.currentTimeMillis();
    Iterator<Long> gen = new SoEPagedOdds();
    int count = 0;
    while (gen.next() <= n) count++;
    long elpsd = System.currentTimeMillis() - strt;
    System.out.println("Found " + count + " primes up to " + n + " in " + elpsd + " milliseconds.");
  }
  
}
```

**Output:**

```
Found 50847534 primes up to 1000000000 in 3201 milliseconds.
```


## JavaScript

```mw
function eratosthenes(limit) {
    var primes = [];
    if (limit >= 2) {
        var sqrtlmt = Math.sqrt(limit) - 2;
        var nums = new Array(); // start with an empty Array...
        for (var i = 2; i <= limit; i++) // and
            nums.push(i); // only initialize the Array once...
        for (var i = 0; i <= sqrtlmt; i++) {
            var p = nums[i]
            if (p)
                for (var j = p * p - 2; j < nums.length; j += p)
                    nums[j] = 0;
        }
        for (var i = 0; i < nums.length; i++) {
            var p = nums[i];
            if (p)
                primes.push(p);
        }
    }
    return primes;
}

var primes = eratosthenes(100);

if (typeof print == "undefined")
    print = (typeof WScript != "undefined") ? WScript.Echo : alert;
print(primes);
```

outputs:

```
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
```

Substituting the following code for the function for **an odds-only algorithm using bit packing** for the array produces code that is many times faster than the above:

```mw
function eratosthenes(limit) {
    var prms = [];
    if (limit >= 2) prms = [2];
    if (limit >= 3) {
        var sqrtlmt = (Math.sqrt(limit) - 3) >> 1;
        var lmt = (limit - 3) >> 1;
        var bfsz = (lmt >> 5) + 1
        var buf = [];
        for (var i = 0; i < bfsz; i++)
            buf.push(0);
        for (var i = 0; i <= sqrtlmt; i++)
            if ((buf[i >> 5] & (1 << (i & 31))) == 0) {
                var p = i + i + 3;
                for (var j = (p * p - 3) >> 1; j <= lmt; j += p)
                    buf[j >> 5] |= 1 << (j & 31);
            }
        for (var i = 0; i <= lmt; i++)
            if ((buf[i >> 5] & (1 << (i & 31))) == 0)
                prms.push(i + i + 3);
    }
    return prms;
}
```

While the above code is quite fast especially using an efficient JavaScript engine such as Google Chrome's V8, it isn't as elegant as it could be using the features of the new EcmaScript6 specification when it comes out about the end of 2014 and when JavaScript engines including those of browsers implement that standard in that we might choose to implement an incremental algorithm iterators or generators similar to as implemented in Python or F# (yield). Meanwhile, we can emulate some of those features by using a simulation of an iterator class (which is easier than using a call-back function) for an **"infinite" generator based on an Object dictionary** as in the following odds-only code written as a JavaScript class:

```mw
var SoEIncClass = (function () {
    function SoEIncClass() {
        this.n = 0;
    }
    SoEIncClass.prototype.next = function () {
        this.n += 2;
        if (this.n < 7) { // initialization of sequence to avoid runaway:
            if (this.n < 3) { // only even of two:
                this.n = 1; // odds from here...
                return 2;
            }
            if (this.n < 5)
                return 3;
            this.dict = {}; // n must be 5...
            this.bps = new SoEIncClass(); // new source of base primes
            this.bps.next(); // advance past the even prime of two...
            this.p = this.bps.next(); // first odd prime (3 in this case)
            this.q = this.p * this.p; // set guard
            return 5;
        } else { // past initialization:
            var s = this.dict[this.n]; // may or may not be defined...
            if (!s) { // not defined:
                if (this.n < this.q) // haven't reached the guard:
                    return this.n; // found a prime
                else { // n === q => not prime but at guard, so:
                    var p2 = this.p << 1; // the span odds-only is twice prime
                    this.dict[this.n + p2] = p2; // add next composite of prime to dict
                    this.p = this.bps.next();
                    this.q = this.p * this.p; // get next base prime guard
                    return this.next(); // not prime so advance...
                }
            } else { // is a found composite of previous base prime => not prime
                delete this.dict[this.n]; // advance to next composite of this prime:
                var nxt = this.n + s;
                while (this.dict[nxt]) nxt += s; // find unique empty slot in dict
                this.dict[nxt] = s; // to put the next composite for this base prime
                return this.next(); // not prime so advance...
            }
        }
    };
    return SoEIncClass;
})();
```

The above code can be used to find the nth prime (which would require estimating the required range limit using the previous fixed range code) by using the following code:

```mw
var gen = new SoEIncClass(); 
for (var i = 1; i < 1000000; i++, gen.next());
var prime = gen.next();
 
if (typeof print == "undefined")
    print = (typeof WScript != "undefined") ? WScript.Echo : alert;
print(prime);
```

to produce the following output (about five seconds using Google Chrome's V8 JavaScript engine):

```
15485863
```

The above code is considerably slower than the fixed range code due to the multiple method calls and the use of an object as a dictionary, which (using a hash table as its basis for most implementations) will have about a constant O(1) amortized time per operation but has quite a high constant overhead to convert the numeric indices to strings which are then hashed to be used as table keys for the look-up operations as compared to doing this more directly in implementations such as the Python dict with Python's built-in hashing functions for every supported type.

This can be implemented as **an "infinite" odds-only generator using page segmentation** for a considerable speed-up with the alternate JavaScript class code as follows:

```mw
var SoEPgClass = (function () {
    function SoEPgClass() {
        this.bi = -1; // constructor resets the enumeration to start...
    }
    SoEPgClass.prototype.next = function () {
        if (this.bi < 1) {
            if (this.bi < 0) {
                this.bi++;
                this.lowi = 0; // other initialization done here...
                this.bpa = [];
                return 2;
            } else { // bi must be zero:
                var nxt = 3 + (this.lowi << 1) + 262144;
                this.buf = new Array();
                for (var i = 0; i < 4096; i++) // faster initialization:
                    this.buf.push(0);
                if (this.lowi <= 0) { // special culling for first page as no base primes yet:
                    for (var i = 0, p = 3, sqr = 9; sqr < nxt; i++, p += 2, sqr = p * p)
                        if ((this.buf[i >> 5] & (1 << (i & 31))) === 0)
                            for (var j = (sqr - 3) >> 1; j < 131072; j += p)
                                this.buf[j >> 5] |= 1 << (j & 31);
                } else { // after the first page:
                    if (!this.bpa.length) { // if this is the first page after the zero one:
                        this.bps = new SoEPgClass(); // initialize separate base primes stream:
                        this.bps.next(); // advance past the only even prime of two
                        this.bpa.push(this.bps.next()); // get the next prime (3 in this case)
                    }
                    // get enough base primes for the page range...
                    for (var p = this.bpa[this.bpa.length - 1], sqr = p * p; sqr < nxt;
                            p = this.bps.next(), this.bpa.push(p), sqr = p * p) ;
                    for (var i = 0; i < this.bpa.length; i++) {
                        var p = this.bpa[i];
                        var s = (p * p - 3) >> 1;
                        if (s >= this.lowi) // adjust start index based on page lower limit...
                            s -= this.lowi;
                        else {
                            var r = (this.lowi - s) % p;
                            s = (r != 0) ? p - r : 0;
                        }
                        for (var j = s; j < 131072; j += p)
                            this.buf[j >> 5] |= 1 << (j & 31);
                    }
                }
            }
        }
        while (this.bi < 131072 && this.buf[this.bi >> 5] & (1 << (this.bi & 31)))
            this.bi++; // find next marker still with prime status
        if (this.bi < 131072) // within buffer: output computed prime
            return 3 + ((this.lowi + this.bi++) << 1);
        else { // beyond buffer range: advance buffer
            this.bi = 0;
            this.lowi += 131072;
            return this.next(); // and recursively loop
        }
    };
    return SoEPgClass;
})();
```

The above code is about fifty times faster (about five seconds to calculate 50 million primes to about a billion on the Google Chrome V8 JavaScript engine) than the above dictionary based code.

The speed for both of these "infinite" solutions will also respond to further wheel factorization techniques, especially for the dictionary based version where any added overhead to deal with the factorization wheel will be negligible compared to the dictionary overhead. The dictionary version would likely speed up about a factor of three or a little more with maximum wheel factorization applied; the page segmented version probably won't gain more than a factor of two and perhaps less due to the overheads of array look-up operations.

function is copy-pasted from above to produce a webpage version for beginners:

```mw
<script>
function eratosthenes(limit) {
    var primes = [];
    if (limit >= 2) {
        var sqrtlmt = Math.sqrt(limit) - 2;
        var nums = new Array(); // start with an empty Array...
        for (var i = 2; i <= limit; i++) // and
            nums.push(i); // only initialize the Array once...
        for (var i = 0; i <= sqrtlmt; i++) {
            var p = nums[i]
            if (p)
                for (var j = p * p - 2; j < nums.length; j += p)
                    nums[j] = 0;
        }
        for (var i = 0; i < nums.length; i++) {
            var p = nums[i];
            if (p)
                primes.push(p);
        }
    }
    return primes;
}
var primes = eratosthenes(100);
   output='';
        for (var i = 0; i < primes.length; i++) {
      output+=primes[i];   
      if (i < primes.length-1) output+=',';
        }
document.write(output);
</script>
```


## JOVIAL

```mw
START
FILE MYOUTPUT ... $ ''Insufficient information to complete this declaration''
PROC SIEVEE $
    '' define the sieve data structure ''
    ARRAY CANDIDATES 1000 B $
    FOR I =0,1,999 $
    BEGIN
        '' everything is potentially prime until proven otherwise ''
        CANDIDATES($I$) = 1$
    END
    '' Neither 1 nor 0 is prime, so flag them off ''
    CANDIDATES($0$) = 0$
    CANDIDATES($1$) = 0$
    '' start the sieve with the integer 0 ''
    FOR I = 0$
    BEGIN
        IF I GE 1000$
        GOTO DONE$
        '' advance to the next un-crossed out number. ''
        '' this number must be a prime ''
NEXTI.  IF I LS 1000 AND Candidates($I$) EQ 0 $
        BEGIN
            I = I + 1 $
            GOTO NEXTI $
        END
        '' insure against running off the end of the data structure ''
        IF I LT 1000 $
        BEGIN
            '' cross out all multiples of the prime, starting with 2*p. ''
            FOR J=2 $
            FOR K=0 $
            BEGIN
                K = J * I $
                IF K GT 999 $
                GOTO ADV $
                CANDIDATES($K$) = 0 $
                J = J + 1 $
            END
            '' advance to the next candidate ''
ADV.        I = I + 1 $
        END
    END
    '' all uncrossed-out numbers are prime (and only those numbers) ''
    '' print all primes ''
DONE. OPEN OUTPUT MYOUTPUT $
    FOR I=0,1,999$
    BEGIN
        IF CANDIDATES($I$) NQ 0$
        BEGIN
            OUTPUT MYOUTPUT I $
        END
    END
TERM$
```


## jq

Works with

:

jq

version 1.4

### Bare Bones

Short and sweet ...

```mw
# Denoting the input by $n, which is assumed to be a positive integer,
# eratosthenes/0 produces an array of primes less than or equal to $n:
def eratosthenes:

  def erase(i):
    if .[i] then
      reduce (range(2*i; length; i)) as $j (.; .[$j] = false) 
    else .
    end;

  (. + 1) as $n
  | (($n|sqrt) / 2) as $s
  | [null, null, range(2; $n)]
  | reduce (2, 1 + (2 * range(1; $s))) as $i (.; erase($i))
  | map(select(.));
```

**Examples**:

```mw
100 | eratosthenes
```

**Output:**

[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

```mw
1e7 | eratosthenes | length
```

**Output:**

664579

### Enhanced Sieve

Here is a more economical variant that:

- produces a stream of primes less than or equal to a given integer;
- only records the status of odd integers greater than 3 during the sieving process;
- optimizes the inner loop as described in the task description.

```mw
def primes:
  # The array we use for the sieve only stores information for the odd integers greater than 1:
  #  index   integer
  #      0         3
  #      k   2*k + 3
  # So if we wish to mark m = 2*k + 3, the relevant index is: m - 3 / 2
  def ix:
    if . % 2 == 0 then null
    else ((. - 3) / 2)
    end;
    
  # erase(i) sets .[i*j] to false for odd integral j > i, and assumes i is odd
  def erase(i):
    ((i - 3) / 2) as $k
    # Consider relevant multiples:
    then (((length * 2 + 3) / i)) as $upper
    # ... only consider odd multiples from i onwards
    | reduce range(i; $upper; 2) as $j (.;
         (((i * $j) - 3) / 2) as $m
         | if .[$m] then .[$m] = false else . end);

  if . < 2 then []
  else (. + 1) as $n
  | (($n|sqrt) / 2) as $s
  | [range(3; $n; 2)|true]
  | reduce (1 + (2 * range(1; $s)) ) as $i (.; erase($i))
  | . as $sieve
  | 2, (range(3; $n; 2) | select($sieve[ix]))
  end ;

def count(s): reduce s as $_ (0; .+1);

count(1e6 | primes)
```

**Output:**

```
78498
```
