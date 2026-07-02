---
title: "Sieve of Eratosthenes (part 3/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/21
---

## C++

### Standard Library

This implementation follows the standard library pattern of std::iota. The start and end iterators are provided for the container. The destination container is used for marking primes and then filled with the primes which are less than the container size. This method requires no memory allocation inside the function.

```mw
#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>

// Fills the range [start, end) with 1 if the integer corresponding to the index is composite and 0 otherwise.
// requires: I is RandomAccessIterator
template<typename I>
void mark_composites(I start, I end)
{
    std::fill(start, end, 0);

    for (auto it = start + 1; it != end; ++it)
    {
        if (*it == 0)
        {
            auto prime = std::distance(start, it) + 1;
            // mark all multiples of this prime number as composite.
            auto multiple_it = it;
            while (std::distance(multiple_it, end) > prime)
            {
                std::advance(multiple_it, prime);
                *multiple_it = 1;
            }
        }
    }
}

// Fills "out" with the prime numbers in the range 2...N where N = distance(start, end).
// requires: I is a RandomAccessIterator
//           O is an OutputIterator
template <typename I, typename O>
O sieve_primes(I start, I end, O out)
{
    mark_composites(start, end);
    for (auto it = start + 1; it != end; ++it)
    {
        if (*it == 0)
        {
            *out = std::distance(start, it) + 1;
            ++out;
        }
    }
    return out;
}

int main()
{
    std::vector<uint8_t> is_composite(1000);
    sieve_primes(is_composite.begin(), is_composite.end(), std::ostream_iterator<int>(std::cout, " "));

    // Alternative to store in a vector: 
    // std::vector<int> primes;
    // sieve_primes(is_composite.begin(), is_composite.end(), std::back_inserter(primes));
}
```

### Boost

```mw
// yield all prime numbers less than limit. 
template<class UnaryFunction>
void primesupto(int limit, UnaryFunction yield)
{
  std::vector<bool> is_prime(limit, true);
  
  const int sqrt_limit = static_cast<int>(std::sqrt(limit));
  for (int n = 2; n <= sqrt_limit; ++n)
    if (is_prime[n]) {
   yield(n);

   for (unsigned k = n*n, ulim = static_cast<unsigned>(limit); k < ulim; k += n) 
      //NOTE: "unsigned" is used to avoid an overflow in `k+=n` for `limit` near INT_MAX
     is_prime[k] = false;
    }

  for (int n = sqrt_limit + 1; n < limit; ++n)
    if (is_prime[n])
   yield(n);
}
```

Full program:

Works with

:

Boost

```mw
/**
   $ g++ -I/path/to/boost sieve.cpp -o sieve && sieve 10000000
 */
#include <inttypes.h> // uintmax_t
#include <limits>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>

#include <boost/lambda/lambda.hpp>

int main(int argc, char *argv[])
{
  using namespace std;
  using namespace boost::lambda;

  int limit = 10000;
  if (argc == 2) {
    stringstream ss(argv[--argc]);
    ss >> limit;

    if (limit < 1 or ss.fail()) {
      cerr << "USAGE:\n  sieve LIMIT\n\nwhere LIMIT in the range [1, " 
      << numeric_limits<int>::max() << ")" << endl;
      return 2;
    }
  }

  // print primes less then 100
  primesupto(100, cout << _1 << " ");
  cout << endl;  

  // find number of primes less then limit and their sum
  int count = 0;
  uintmax_t sum = 0;
  primesupto(limit, (var(sum) += _1, var(count) += 1));

  cout << "limit sum pi(n)\n" 
       << limit << " " << sum << " " << count << endl;
}
```


## Chapel

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** Doesn't compile since at least Chapel version 1.20 to 1.24.1. |
|---|

This solution uses nested iterators to create new wheels at run time:

```mw
// yield prime and remove all multiples of it from children sieves
iter sieve(prime):int {

        yield prime;

        var last = prime;
        label candidates for candidate in sieve(prime+1) do {
                for composite in last..candidate by prime do {

                        // candidate is a multiple of this prime
                        if composite == candidate {
                                // remember size of last composite
                                last = composite;
                                // and try the next candidate
                                continue candidates;
                        }
                }

                // candidate cannot need to be removed by this sieve
                // yield to parent sieve for checking
                yield candidate;
        }
}
```

The topmost sieve needs to be started with 2 (the smallest prime):

```mw
config const N = 30;
for p in sieve(2) {
        if p > N {
                writeln();
                break;
        }
        write(" ", p);
}
```

### Alternate Conventional Bit-Packed Implementation

The following code implements the conventional monolithic (one large array) Sieve of Eratosthenes where the representations of the numbers use only one bit per number, using an iteration for output so as to not require further memory allocation:

compile with the `--fast` option

```mw
use Time;
use BitOps;

type Prime = uint(32);

config const limit: Prime = 1000000000; // sieve limit

proc main() {
  write("The first 25 primes are:  ");
  for p in primes(100) do write(p, " "); writeln();
  
  var count = 0; for p in primes(1000000) do count += 1;
  writeln("Count of primes to a million is:  ", count, ".");
  
  var timer: Timer;
  timer.start();

  count = 0;
  for p in primes(limit) do count += 1;

  timer.stop();
  write("Found ", count, " primes up to ", limit);
  writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
}

iter primes(n: Prime): Prime {
  const szlmt = n / 8;
  var cmpsts: [0 .. szlmt] uint(8); // even number of byte array rounded up

  for bp in 2 .. n {
    if cmpsts[bp >> 3] & (1: uint(8) << (bp & 7)) == 0 {
      const s0 = bp * bp;
      if s0 > n then break;
      for c in s0 .. n by bp { cmpsts[c >> 3] |= 1: uint(8) << (c & 7); }
    }
  }

  for p in 2 .. n do if cmpsts[p >> 3] & (1: uint(8) << (p & 7)) == 0 then yield p;

}
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Count of primes to a million is:  78498.
Found 50847534 primes up to 1000000000 in 7964.05 milliseconds.
```

Time as run using Chapel version 24.1 on an Intel Skylake i5-6500 at 3.6 GHz (turbo, single threaded).

### Alternate Odds-Only Bit-Packed Implementation

```mw
use Time;
use BitOps;

type Prime = int(32);

config const limit: Prime = 1000000000; // sieve limit

proc main() {
  write("The first 25 primes are:  ");
  for p in primes(100) do write(p, " "); writeln();
  
  var count = 0; for p in primes(1000000) do count += 1;
  writeln("Count of primes to a million is:  ", count, ".");
  
  var timer: Timer;
  timer.start();

  count = 0;
  for p in primes(limit) do count += 1;

  timer.stop();
  write("Found ", count, " primes up to ", limit);
  writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
}

iter primes(n: Prime): Prime {
  const ndxlmt = (n - 3) / 2;
  const szlmt = ndxlmt / 8;
  var cmpsts: [0 .. szlmt] uint(8); // even number of byte array rounded up

  for i in 0 .. ndxlmt { // never gets to the end!
    if cmpsts[i >> 3] & (1: uint(8) << (i & 7)) == 0 {
      const bp = i + i + 3;
      const s0 = (bp * bp - 3) / 2;
      if s0 > ndxlmt then break;
      for s in s0 .. ndxlmt by bp do cmpsts[s >> 3] |= 1: uint(8) << (s & 7);
    }
  }

  yield 2;
  for i in 0 .. ndxlmt do
    if cmpsts[i >> 3] & (1: uint(8) << (i & 7)) == 0 then yield i + i + 3;

}
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Count of primes to a million is:  78498.
Found 50847534 primes up to 1000000000 in 4008.16 milliseconds.
```

Time as run using Chapel version 24.1 on an Intel Skylake i5-6500 at 3.6 GHz (turbo, single threaded).

As you can see, sieving odds-only is about twice as fast due to the reduced number of operations; it also uses only half the amount of memory. However, this is still not all that fast at about 14.4 CPU clock cycles per sieve culling operation due to the size of the array exceeding the CPU cache size(s).

### Hash Table Based Odds-Only Version

Translation of

:

Python

code link

Works with

:

Chapel

version 1.25.1

```mw
use Time;

config const limit = 100000000;

type Prime = uint(32);

class Primes { // needed so we can use next to get successive values
  var n: Prime; var obp: Prime; var q: Prime;
  var bps: owned Primes?;
  var keys: domain(Prime); var dict: [keys] Prime;
  proc next(): Prime { // odd primes!
    if this.n < 5 { this.n = 5; return 3; }
    if this.bps == nil {
      this.bps = new Primes(); // secondary odd base primes feed
      this.obp = this.bps!.next(); this.q = this.obp * this.obp;
    }
    while true {
      if this.n >= this.q { // advance secondary stream of base primes...
        const adv = this.obp * 2; const key = this.q + adv;
        this.obp = this.bps!.next(); this.q = this.obp * this.obp;       
        this.keys += key; this.dict[key] = adv;
      }
      else if this.keys.contains(this.n) { // found a composite; advance...
        const adv = this.dict[this.n]; this.keys.remove(this.n);
        var nkey = this.n + adv;
        while this.keys.contains(nkey) do nkey += adv;
        this.keys += nkey; this.dict[nkey] = adv;
      }
      else { const p = this.n; this.n += 2; return p; }
      this.n += 2;
    }
    return 0; // to keep compiler happy in returning a value!
  }
  iter these(): Prime { yield 2; while true do yield this.next(); }
}

proc main() {
  var count = 0;
  write("The first 25 primes are:  ");
  for p in new Primes() { if count >= 25 then break; write(p, " "); count += 1; }
  writeln();
  
  var timer: Timer;
  timer.start();

  count = 0;
  for p in new Primes() { if p > limit then break; count += 1; }

  timer.stop();
  write("Found ", count, " primes up to ", limit);
  writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
}
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Found 5761455 primes up to 100000000 in 5195.41 milliseconds.
```

Time as run using Chapel version 24.1 on an Intel Skylake i5-6500 at 3.6 GHz (turbo, single threaded).

As you can see, this is much slower than the array based versions but much faster than previous Chapel version code as the hashing has been greatly improved.

As an alternate to the use of a built-in library, the following code implements a specialized BasePrimesTable that works similarly to the way the Python associative arrays work as to hashing algorithm used (no hashing, as the hash values for integers are just themselves) and something similar to the Python method of handling hash table collisions is used:

Works with

:

Chapel

version 1.25.1

Compile with the `--fast` compiler command line option

```mw
use Time;
 
config const limit = 100000000;
 
type Prime = uint(32);

record BasePrimesTable { // specialized for the use here...
  record BasePrimeEntry { var fullkey: Prime; var val: Prime; }
  var cpcty: int = 8; var sz: int = 0;
  var dom = { 0 .. cpcty - 1 }; var bpa: [dom] BasePrimeEntry;
  proc grow() {   
    const ndom = dom; var cbpa: [ndom] BasePrimeEntry = bpa[ndom];
    bpa = new BasePrimeEntry(); cpcty *= 2; dom = { 0 .. cpcty - 1 };
    for kv in cbpa do if kv.fullkey != 0 then add(kv.fullkey, kv.val);   
  }
  proc find(k: Prime): int { // internal get location of value or -1
    const msk = cpcty - 1; var skey = k: int & msk;
    var perturb = k: int; var loop = 8;
    do {
      if bpa[skey].fullkey == k then return skey;
      perturb >>= 5; skey = (5 * skey + 1 + perturb) & msk;
      loop -= 1; if perturb > 0 then loop = 8;
    } while loop > 0;
    return -1; // not found!
  }
  proc contains(k: Prime): bool { return find(k) >= 0; }
  proc add(k, v: Prime) { // if exists then replaces else new entry
    const fndi = find(k);
    if fndi >= 0 then bpa[fndi] = new BasePrimeEntry(k, v);
    else {
      sz += 1; if 2 * sz > cpcty then grow();
      const msk = cpcty - 1; var skey = k: int & msk;
      var perturb = k: int; var loop = 8;
      do {
        if bpa[skey].fullkey == 0 {
          bpa[skey] = new BasePrimeEntry(k, v); return; }
        perturb >>= 5; skey = (5 * skey + 1 + perturb) & msk;
        loop -= 1; if perturb > 0 then loop = 8;
      } while loop > 0;
    }
  }
  proc remove(k: Prime) { // if doesn't exist does nothing
    const fndi = find(k);
    if fndi >= 0 { bpa[fndi].fullkey = 0; sz -= 1; }
  }
  proc this(k: Prime): Prime { // returns value or 0 if not found
    const fndi = find(k);
    if fndi < 0 then return 0; else return bpa[fndi].val;
  }
}

class Primes { // needed so we can use next to get successive values
  var n: Prime; var obp: Prime; var q: Prime;
  var bps: shared Primes?; var dict = new BasePrimesTable();
  proc next(): Prime { // odd primes!
    if this.n < 5 { this.n = 5; return 3; }
    if this.bps == nil {
      this.bps = new Primes(); // secondary odd base primes feed
      this.obp = this.bps!.next(); this.q = this.obp * this.obp;
    }
    while true {
      if this.n >= this.q { // advance secondary stream of base primes...
        const adv = this.obp * 2; const key = this.q + adv;
        this.obp = this.bps!.next(); this.q = this.obp * this.obp;
        this.dict.add(key, adv);
      }
      else if this.dict.contains(this.n) { // found a composite; advance...
        const adv = this.dict[this.n]; this.dict.remove(this.n);
        var nkey = this.n + adv;
        while this.dict.contains(nkey) do nkey += adv;
        this.dict.add(nkey, adv);
      }
      else { const p = this.n; this.n += 2; return p; }
      this.n += 2;
    }
    return 0; // to keep compiler happy in returning a value!
  }
  iter these(): Prime { yield 2; while true do yield this.next(); }
}

proc main() {
  var count = 0;
  write("The first 25 primes are:  ");
  for p in new Primes() { if count >= 25 then break; write(p, " "); count += 1; }
  writeln();
 
  var timer: Timer;
  timer.start();
 
  count = 0;
  for p in new Primes() { if p > limit then break; count += 1; }
 
  timer.stop();
  write("Found ", count, " primes up to ", limit);
  writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
}
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Found 5761455 primes up to 100000000 in 2351.79 milliseconds.
```

This last code is quite usable up to a hundred million (as here) or even a billion in a little over ten times the time, but is still slower than the very simple odds-only monolithic array version and is also more complex, although it uses less memory (only for the hash table for the base primes of about eight Kilobytes for sieving to a billion compared to over 60 Megabytes for the monolithic odds-only simple version).

Chapel version 1.25.1 provides yet another option as to the form of the code although the algorithm is the same in that one can now override the hashing function for Chapel records so that they can be used as the Key Type for Hash Map's as follows:

Works with

:

Chapel

version 1.25.1

Compile with the `--fast` compiler command line option

```mw
use Time;

use Map;
 
config const limit = 100000000;
 
type Prime = uint(32);
 
class Primes { // needed so we can use next to get successive values
  record PrimeR { var prime: Prime; proc hash() { return prime; } }
  var n: PrimeR = new PrimeR(0); var obp: Prime; var q: Prime;
  var bps: owned Primes?;
  var dict = new map(PrimeR, Prime);
  proc next(): Prime { // odd primes!
    if this.n.prime < 5 { this.n.prime = 5; return 3; }
    if this.bps == nil {
      this.bps = new Primes(); // secondary odd base primes feed
      this.obp = this.bps!.next(); this.q = this.obp * this.obp;
    }
    while true {
      if this.n.prime >= this.q { // advance secondary stream of base primes...
        const adv = this.obp * 2; const key = new PrimeR(this.q + adv);
        this.obp = this.bps!.next(); this.q = this.obp * this.obp;       
        this.dict.add(key, adv);
      }
      else if this.dict.contains(this.n) { // found a composite; advance...
        const adv = this.dict.getValue(this.n); this.dict.remove(this.n);
        var nkey = new PrimeR(this.n.prime + adv);
        while this.dict.contains(nkey) do nkey.prime += adv;
        this.dict.add(nkey, adv);
      }
      else { const p = this.n.prime;
             this.n.prime += 2; return p; }
      this.n.prime += 2;
    }
    return 0; // to keep compiler happy in returning a value!
  }
  iter these(): Prime { yield 2; while true do yield this.next(); }
}
 
proc main() {
  var count = 0;
  write("The first 25 primes are:  ");
  for p in new Primes() { if count >= 25 then break; write(p, " "); count += 1; }
  writeln();
 
  var timer: Timer;
  timer.start();
 
  count = 0;
  for p in new Primes() { if p > limit then break; count += 1; }
 
  timer.stop();
  write("Found ", count, " primes up to ", limit);
  writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
}
```

This works in about exactly the same time as the last previous code, but doesn't require special custom adaptations of the associative array so that the standard library Map can be used.

### Functional Tree Folding Odds-Only Version

Chapel isn't really a very functional language even though it has some functional forms of code in the Higher Order Functions (HOF's) of zippered, scanned, and reduced, iterations and has first class functions (FCF's) and lambdas (anonymous functions), these last can't be closures (capture variable bindings from external scope(s)), nor can the work around of using classes to emulate closures handle recursive (Y-combinator type) variable bindings using reference fields (at least currently with version 1.22). However, the Tree Folding add-on to the Richard Bird lazy list sieve doesn't require any of the things that can't be emulated using classes, so a version is given as follows:

Translation of

:

Nim

code link

Works with

:

1.22

version - compile with the --fast compiler command line flag for full optimization

```mw
use Time;

type Prime = uint(32);

config const limit = 1000000: Prime;

// Chapel doesn't have closures, so we need to emulate them with classes...
class PrimeCIS { // base prime stream...
  var head: Prime;
  proc next(): shared PrimeCIS { return new shared PrimeCIS(); }
}

class PrimeMultiples: PrimeCIS {
  var adv: Prime;
  override proc next(): shared PrimeCIS {
    return new shared PrimeMultiples(
      this.head + this.adv, this.adv): shared PrimeCIS; }
}

class PrimeCISCIS { // base stream of prime streams; never used directly...
  var head: shared PrimeCIS;
  proc init() { this.head = new shared PrimeCIS(); }
  proc next(): shared PrimeCISCIS {
    return new shared PrimeCISCIS(); }
}

class AllMultiples: PrimeCISCIS {
  var bps: shared PrimeCIS;
  proc init(bsprms: shared PrimeCIS) {
    const bp = bsprms.head; const sqr = bp * bp; const adv = bp + bp;
    this.head = new shared PrimeMultiples(sqr, adv): PrimeCIS;
    this.bps = bsprms;
  }
  override proc next(): shared PrimeCISCIS {
    return new shared AllMultiples(this.bps.next()): PrimeCISCIS; }
}

class Union: PrimeCIS {
  var feeda, feedb: shared PrimeCIS;
  proc init(fda: shared PrimeCIS, fdb: shared PrimeCIS) {
    const ahd = fda.head; const bhd = fdb.head;
    this.head = if ahd < bhd then ahd else bhd;
    this.feeda = fda; this.feedb = fdb;
  }
  override proc next(): shared PrimeCIS {    
    const ahd = this.feeda.head; const bhd = this.feedb.head;
    if ahd < bhd then
      return new shared Union(this.feeda.next(), this.feedb): shared PrimeCIS;
    if ahd > bhd then
      return new shared Union(this.feeda, this.feedb.next()): shared PrimeCIS;
    return new shared Union(this.feeda.next(),
                            this.feedb.next()): shared PrimeCIS;
  }
}

class Pairs: PrimeCISCIS {
  var feed: shared PrimeCISCIS;
  proc init(fd: shared PrimeCISCIS) {
    const fs = fd.head; const sss = fd.next(); const ss = sss.head;
    this.head = new shared Union(fs, ss): shared PrimeCIS; this.feed = sss;
  }
  override proc next(): shared PrimeCISCIS {
    return new shared Pairs(this.feed.next()): shared PrimeCISCIS; }
}

class Composites: PrimeCIS {
  var feed: shared PrimeCISCIS;
  proc init(fd: shared PrimeCISCIS) {
    this.head = fd.head.head; this.feed = fd;
  }
  override proc next(): shared PrimeCIS {
    const fs = this.feed.head.next();
    const prs = new shared Pairs(this.feed.next()): shared PrimeCISCIS;
    const ncs = new shared Composites(prs): shared PrimeCIS;
    return new shared Union(fs, ncs): shared PrimeCIS;
  }
}

class OddPrimesFrom: PrimeCIS {
  var cmpsts: shared PrimeCIS;
  override proc next(): shared PrimeCIS {
    var n = head + 2; var cs = this.cmpsts;
    while true {
      if n < cs.head then
        return new shared OddPrimesFrom(n, cs): shared PrimeCIS;
      n += 2; cs = cs.next();
    }
    return this.cmpsts; // never used; keeps compiler happy!
  }
}

class OddPrimes: PrimeCIS {
  proc init() { this.head = 3; }
  override proc next(): shared PrimeCIS {
    const bps = new shared OddPrimes(): shared PrimeCIS;
    const mlts = new shared AllMultiples(bps): shared PrimeCISCIS;
    const cmpsts = new shared Composites(mlts): shared PrimeCIS;
    return new shared OddPrimesFrom(5, cmpsts): shared PrimeCIS;
  }
}

iter primes(): Prime {
  yield 2; var cur = new shared OddPrimes(): shared PrimeCIS;
  while true { yield cur.head; cur = cur.next(); }
}

// test it...
write("The first 25 primes are: "); var cnt = 0;
for p in primes() { if cnt >= 25 then break; cnt += 1; write(" ", p); }

Time as run using Chapel version 24.1 on an Intel Skylake i5-6500 at 3.6 GHz (turbo, single threaded).

var timer: Timer; timer.start(); cnt = 0;
for p in primes() { if p > limit then break; cnt += 1; }
timer.stop(); write("\nFound ", cnt, " primes up to ", limit);
writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
Found 78498 primes up to 1000000 in 344.859 milliseconds.
```

Time as run using Chapel version 24.1 on an Intel Skylake i5-6500 at 3.6 GHz (turbo, single threaded).

The above code is really just a toy example to show that Chapel can handle some tasks functionally (within the above stated limits) although doing so is slower than the Hash Table version above and also takes more memory as the nested lazy list structure consumes more memory in lazy list links and "plumbing" than does the simple implementation of a Hash Table. It also has a worst asymptotic performance with an extra `log(n)` factor where `n` is the sieving range; this can be shown by running the above program with `--limit=10000000` run time command line option to sieve to ten million which takes about 4.5 seconds to count the primes up to ten million (a factor of ten higher range, but much higher than the expected increased factor of about 10 per cent extra as per the Hash Table version with about 20 per cent more operations times the factor of ten for this version). Other than for the extra operations, this version is generally slower due to the time to do the many small allocations/de-allocations of the functional object instances, and this will be highly dependent on the platform on which it is run: cygwin on Windows may be particularly slow due to the extra level of indirection, and some on-line IDE's may also be slow due to their level of virtualization.

### A Multi-Threaded Page-Segmented Odds-Only Bit-Packed Version

To take advantage of the features that make Chapel shine, we need to use it to do some parallel computations, and to efficiently do that for the Sieve of Eratosthenes, we need to divide the work into page segments where we can assign each largish segment to a separate thread/task; this also improves the speed due to better cache associativity with most memory accesses to values that are already in the cache(s). Once we have divided the work, Chapel offers lots of means to implement the parallelism but to be a true Sieve of Eratosthenes, we need to have the ability to output the results in order; with many of the convenience mechanisms not doing that, the best/simplest option is likely task parallelism with the output results assigned to an rotary indexed array containing the `sync` results. It turns out that, although the Chapel compiler can sometimes optimize the code so the overhead of creating tasks is not onerous, for this case where the actual tasks are somewhat complex, the compiler can't recognize that an automatically generated thread pool(s) are required so we need to generate the thread pool(s) manually. The code that implements the multi-threading of page segments using thread pools is as follows:

Works with

:

1.24.1

version - compile with the --fast compiler command line flag for full optimization

```mw
use Time; use BitOps; use CPtr;

type Prime = uint(64);
type PrimeNdx = int(64);
type BasePrime = uint(32);

config const LIMIT = 1000000000: Prime;

config const L1 = 16; // CPU L1 cache size in Kilobytes (1024);
assert (L1 == 16 || L1 == 32 || L1 == 64,
        "L1 cache size must be 16, 32, or 64 Kilobytes!");
config const L2 = 128; // CPU L2 cache size in Kilobytes (1024);
assert (L2 == 128 || L2 == 256 || L2 == 512,
        "L2 cache size must be 128, 256, or 512 Kilobytes!");
const CPUL1CACHE: int = L1 * 1024 * 8; // size in bits!
const CPUL2CACHE: int = L2 * 1024 * 8; // size in bits!
config const NUMTHRDS = here.maxTaskPar;
assert(NUMTHRDS >= 1, "NUMTHRDS must be at least one!");

const WHLPRMS = [ 2: Prime, 3: Prime, 5: Prime, 7: Prime,
                            11: Prime, 13: Prime, 17: Prime];
const FRSTSVPRM = 19: Prime; // past the pre-cull primes!
// 2 eliminated as even; 255255 in bytes...
const WHLPTRNSPN = 3 * 5 * 7 * 11 * 13 * 17;
// rounded up to next 64-bit boundary plus a 16 Kilobyte buffer for overflow...
const WHLPTRNBTSZ = ((WHLPTRNSPN * 8 + 63) & (-64)) + 131072;

// number of base primes within small span!
const SZBPSTRTS = 6542 - WHLPRMS.size + 1; // extra one for marker!
// number of base primes for CPU L1 cache buffer!
const SZMNSTRTS = (if L1 == 16 then 12251 else
                     if L1 == 32 then 23000 else 43390)
                       - WHLPRMS.size + 1; // extra one for marker!

// using this Look Up Table faster than bit twiddling...
const bitmsk = for i in 0 .. 7 do 1:uint(8) << i;

var WHLPTRN: SieveBuffer = new SieveBuffer(WHLPTRNBTSZ); fillWHLPTRN(WHLPTRN);
proc fillWHLPTRN(ref wp: SieveBuffer) {
  const hi = WHLPRMS.size - 1;
  const rng = 0 .. hi; var whlhd = new shared BasePrimeArr({rng});
  // contains wheel pattern primes skipping the small wheel prime (2)!...
  // never advances past the first base prime arr as it ends with a huge!...
  for i in rng do whlhd.bparr[i] = (if i != hi then WHLPRMS[i + 1] // skip 2!
                                    else 0x7FFFFFFF): BasePrime; // last huge!
  var whlbpas = new shared BasePrimeArrs(whlhd);
  var whlstrts = new StrtsArr({rng});
  wp.cull(0, WHLPTRNBTSZ, whlbpas, whlstrts);
  // eliminate wheel primes from the WHLPTRN buffer!...
  wp.cmpsts[0] = 0xFF: uint(8);
}

// the following two must be classes for compability with sync...
class PrimeArr { var dom = { 0 .. -1 }; var prmarr: [dom] Prime; }
class BasePrimeArr { var dom = { 0 .. -1 }; var bparr: [dom] BasePrime; }
record StrtsArr { var dom = { 0 .. -1 }; var strtsarr: [dom] int(32); }
record SieveBuffer {
  var dom = { 0 .. -1 }; var cmpsts: [dom] uint(8) = 0;
  proc init() {}
  proc init(btsz: int) { dom = { 0 .. btsz / 8 - 1 }; }
  proc deinit() { dom = { 0 .. -1 }; }

  proc fill(lwi: PrimeNdx) { // fill from the WHLPTRN stamp...
    const sz = cmpsts.size; const mvsz = min(sz, 16384);
    var mdlo = ((lwi / 8) % (WHLPTRNSPN: PrimeNdx)): int;
    for i in 0 .. sz - 1 by 16384 {
      c_memcpy(c_ptrTo(cmpsts[i]): c_void_ptr,
               c_ptrTo(WHLPTRN.cmpsts[mdlo]): c_void_ptr, mvsz);    
      mdlo += 16384; if mdlo >= WHLPTRNSPN then mdlo -= WHLPTRNSPN;
    }
  }

  proc count(btlmt: int) { // count by 64 bits using CPU popcount...
    const lstwrd = btlmt / 64; const lstmsk = (-2):uint(64) << (btlmt & 63);
    const cmpstsp = c_ptrTo(cmpsts: [dom] uint(8)): c_ptr(uint(64));
    var i = 0; var cnt = (lstwrd * 64 + 64): int;
    while i < lstwrd { cnt -= popcount(cmpstsp[i]): int; i += 1; }
    return cnt - popcount(cmpstsp[lstwrd] | lstmsk): int;    
  }

  // most of the time is spent doing culling operations as follows!...
  proc cull(lwi: PrimeNdx, bsbtsz: int, bpas: BasePrimeArrs,
                                        ref strts: StrtsArr) {
    const btlmt = cmpsts.size * 8 - 1; const bplmt = bsbtsz / 32;
    const ndxlmt = lwi: Prime + btlmt: Prime; // can't overflow!
    const strtssz = strts.strtsarr.size;
    // C pointer for speed magic!...
    const cmpstsp = c_ptrTo(cmpsts[0]);
    const strtsp = c_ptrTo(strts.strtsarr);

    // first fill the strts array with pre-calculated start addresses...
    var i = 0; for bp in bpas {
      // calculate page start address for the given base prime...
      const bpi = bp: int; const bbp = bp: Prime; const ndx0 = (bbp - 3) / 2;
      const s0 = (ndx0 + ndx0) * (ndx0 + 3) + 3; // can't overflow!
      if s0 > ndxlmt then {
        if i < strtssz then strtsp[i] = -1: int(32); break; }
      var s = 0: int;
      if s0 >= lwi: Prime then s = (s0 - lwi: Prime): int;
      else { const r = (lwi: Prime - s0) % bbp;
            if r == 0 then s = 0: int; else s = (bbp - r): int; };
      if i < strtssz - 1 { strtsp[i] = s: int(32); i += 1; continue; }
      if i < strtssz { strtsp[i] = -1; i = strtssz; }
      // cull the full buffer for this given base prime as usual...
      // only works up to limit of int(32)**2!!!!!!!!
      while s <= btlmt { cmpstsp[s >> 3] |= bitmsk[s & 7]; s += bpi; }
    }

    // cull the smaller sub buffers according to the strts array...
    for sbtlmt in bsbtsz - 1 .. btlmt by bsbtsz {
      i = 0; for bp in bpas { // bp never bigger than uint(32)!
        // cull the sub buffer for this given base prime...
        var s = strtsp[i]: int; if s < 0 then break;
        var bpi = bp: int; var nxt = 0x7FFFFFFFFFFFFFFF;
        if bpi <= bplmt { // use loop "unpeeling" for a small improvement...
          const slmt = s + bpi * 8 - 1;
          while s <= slmt {
            const bmi = s & 7; const msk = bitmsk[bmi];
            var c = s >> 3; const clmt = sbtlmt >> 3;
            while c <= clmt { cmpstsp[c] |= msk; c += bpi; }
            nxt = min(nxt, (c << 3): int(64) | bmi: int(64)); s += bpi;
          }
          strtsp[i] = nxt: int(32); i += 1;
        }
        else { while s <= sbtlmt { // standard cull loop...
                 cmpstsp[s >> 3] |= bitmsk[s & 7]; s += bpi; }
               strtsp[i] = s: int(32); i += 1; }
      }
    }
  }
}

// a generic record that contains a page result generating function;
// allows manual iteration through the use of the next() method;
// multi-threaded through the use of a thread pool...
class PagedResults {
  const cnvrtrclsr; // output converter closure emulator, (lwi, sba) => output
  var lwi: PrimeNdx; var bsbtsz: int;
  var bpas: shared BasePrimeArrs? = nil: shared BasePrimeArrs?;
  var sbs: [ 0 .. NUMTHRDS - 1 ] SieveBuffer = new SieveBuffer();
  var strts: [ 0 .. NUMTHRDS - 1 ] StrtsArr = new StrtsArr();
  var qi: int = 0;
  var wrkq$: [ 0 .. NUMTHRDS - 1 ] sync PrimeNdx;
  var rsltsq$: [ 0 .. NUMTHRDS - 1 ] sync cnvrtrclsr(lwi, sbs(0)).type;

  proc init(cvclsr, li: PrimeNdx, bsz: int) {
    cnvrtrclsr = cvclsr; lwi = li; bsbtsz = bsz; }

  proc deinit() { // kill the thread pool when out of scope...
    if bpas == nil then return; // no thread pool!
    for i in wrkq$.domain {
      wrkq$[i].writeEF(-1); while true { const r = rsltsq$[i].readFE();
        if r == nil then break; }
    }
  }
 
  proc next(): cnvrtrclsr(lwi, sbs(0)).type {   
    proc dowrk(ri: int) { // used internally!...
      while true {
        const li = wrkq$[ri].readFE(); // following to kill thread!
        if li < 0 { rsltsq$[ri].writeEF(nil: cnvrtrclsr(li, sbs(ri)).type); break; }
        sbs[ri].fill(li);
        sbs[ri].cull(li, bsbtsz, bpas!, strts[ri]);
        rsltsq$[ri].writeEF(cnvrtrclsr(li, sbs[ri]));
      }
    }
    if this.bpas == nil { // init on first use; avoids data race!
      this.bpas = new BasePrimeArrs();
      if this.bsbtsz < CPUL1CACHE {
        this.sbs = new SieveBuffer(bsbtsz);
        this.strts = new StrtsArr({0 .. SZBPSTRTS - 1});
      }
      else {
        this.sbs = new SieveBuffer(CPUL2CACHE);
        this.strts = new StrtsArr({0 .. SZMNSTRTS - 1});
      }
      // start threadpool and give it inital work...
      for i in rsltsq$.domain {
        begin with (const in i) dowrk(i);
        this.wrkq$[i].writeEF(this.lwi); this.lwi += this.sbs[i].cmpsts.size * 8;
      }
    }
    const rslt = this.rsltsq$[qi].readFE();
    this.wrkq$[qi].writeEF(this.lwi);
    this.lwi += this.sbs[qi].cmpsts.size * 8;
    this.qi = if qi >= NUMTHRDS - 1 then 0 else qi + 1;
    return rslt;
  }
 
  iter these() { while lwi >= 0 do yield next(); }
}

// the sieve buffer to base prime array converter closure...
record SB2BPArr {  
  proc this(lwi: PrimeNdx, sb: SieveBuffer): shared BasePrimeArr? {
    const bsprm = (lwi + lwi + 3): BasePrime;
    const szlmt = sb.cmpsts.size * 8 - 1; var i, j = 0;
    var arr = new shared BasePrimeArr({ 0 .. sb.count(szlmt) - 1 });
    while i <= szlmt { if sb.cmpsts[i >> 3] & bitmsk[i & 7] == 0 {
                        arr.bparr[j] = bsprm + (i + i): BasePrime; j += 1; }
                      i += 1; }
    return arr;
  }
}

// a memoizing lazy list of BasePrimeArr's...
class BasePrimeArrs {
  var head: shared BasePrimeArr;
  var tail: shared BasePrimeArrs? = nil: shared BasePrimeArrs?;
  var lock$: sync bool = true;
  var feed: shared PagedResults(SB2BPArr) =
    new shared PagedResults(new SB2BPArr(), 65536, 65536);

  proc init() { // make our own first array to break data race!
    var sb = new SieveBuffer(256); sb.fill(0);
    const sb2 = new SB2BPArr();
    head = sb2(0, sb): shared BasePrimeArr;
    this.complete(); // fake base primes!
    sb = new SieveBuffer(65536); sb.fill(0);
    // use (completed) self as source of base primes!
    var strts = new StrtsArr({ 0 .. 256 });
    sb.cull(0, 65536, this, strts);
    // replace head with new larger version culled using fake base primes!...
    head = sb2(0, sb): shared BasePrimeArr;
  }

  // for initializing for use by the fillWHLPTRN proc...
  proc init(hd: shared BasePrimeArr) {
    head = hd; feed = new shared PagedResults(new SB2BPArr(), 0, 0);
  }

  // for initializing lazily extended list as required...
  proc init(hd: shared BasePrimeArr, fd: PagedResults) { head = hd; feed = fd; }

  proc next(): shared BasePrimeArrs {
    if this.tail == nil { // in case other thread slipped through!     
      if this.lock$.readFE() && this.tail == nil { // empty sync -> block others!
        const nhd = this.feed.next(): shared BasePrimeArr;
        this.tail = new shared BasePrimeArrs(nhd , this.feed);
      }
      this.lock$.writeEF(false); // fill the sync so other threads can do nothing!
    }
    return this.tail: shared BasePrimeArrs; // necessary cast!
  }
 
  iter these(): BasePrime {
    for bp in head.bparr do yield bp; var cur = next();
    while true {
      for bp in cur.head.bparr do yield bp; cur = cur.next(); }
  }
}

record SB2PrmArr {
  proc this(lwi: PrimeNdx, sb: SieveBuffer): shared PrimeArr? {
    const bsprm = (lwi + lwi + 3): Prime;
    const szlmt = sb.cmpsts.size * 8 - 1; var i, j = 0;
    var arr = new shared PrimeArr({0 .. sb.count(szlmt) - 1});
    while i <= szlmt { if sb.cmpsts[i >> 3] & bitmsk[i & 7] == 0 then {
                        arr.prmarr[j] = bsprm + (i + i): Prime; j += 1; }
                      i += 1; }
    return arr;
  }
}

iter primes(): Prime {
  for p in WHLPRMS do yield p: Prime;
  for pa in new shared PagedResults(new SB2PrmArr(), 0, CPUL1CACHE) do
    for p in pa!.prmarr do yield p;
}

// use a class so that it can be used as a generic sync value!...
class CntNxt { const cnt: int; const nxt: PrimeNdx; }

// a class that emulates a closure and a return value...
record SB2Cnt {
  const nxtlmt: PrimeNdx;
  proc this(lwi: PrimeNdx, sb: SieveBuffer): shared CntNxt? {
    const btszlmt = sb.cmpsts.size * 8 - 1; const lstndx = lwi + btszlmt: PrimeNdx;
    const btlmt = if lstndx > nxtlmt then max(0, (nxtlmt - lwi): int) else btszlmt;
    return new shared CntNxt(sb.count(btlmt), lstndx);
  }
}

// couut primes to limit, just like it says...
proc countPrimesTo(lmt: Prime): int(64) {
  const nxtlmt = ((lmt - 3) / 2): PrimeNdx; var count = 0: int(64);
  for p in WHLPRMS { if p > lmt then break; count += 1; }
  if lmt < FRSTSVPRM then return count;
  for cn in new shared PagedResults(new SB2Cnt(nxtlmt), 0, CPUL1CACHE) {
    count += cn!.cnt: int(64); if cn!.nxt >= nxtlmt then break;
  }
  return count;
}

// test it...
write("The first 25 primes are: "); var cnt = 0;
for p in primes() { if cnt >= 25 then break; cnt += 1; write(" ", p); }

cnt = 0; for p in primes() { if p > 1000000 then break; cnt += 1; }
writeln("\nThere are ", cnt, " primes up to a million.");

write("Sieving to ", LIMIT, " with ");
write("CPU L1/L2 cache sizes of ", L1, "/", L2, " KiloBytes ");
writeln("using ", NUMTHRDS, " threads.");

var timer: Timer; timer.start();
// the slow way!:
// var count = 0; for p in primes() { if p > LIMIT then break; count += 1; }
const count = countPrimesTo(LIMIT); // the fast way!
timer.stop();

write("Found ", count, " primes up to ", LIMIT);
writeln(" in ", timer.elapsed(TimeUnits.milliseconds), " milliseconds.");
```

**Output:**

```
The first 25 primes are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
There are 78498 primes up to a million.
Sieving to 1000000000 with CPU L1/L2 cache sizes of 16/128 KiloBytes using 4 threads.
Found 50847534 primes up to 1000000000 in 128.279 milliseconds.
```

Time as run using Chapel version 1.24.1 on an Intel Skylake i5-6500 at 3.2 GHz (base, multi-threaded).

Note that the above code does implement some functional concepts as in a memoized lazy list of base prime arrays, but as this is used at the page level, the slowish performance doesn't impact the overall execution time much and the code is much more elegant in using this concept such that we compute new pages of base primes as they are required for increasing range.

Some of the most tricky bits due to having thread pools is stopping and de-initializing when they go out of scope; this is done by the `deinit` method of the `PagedResults` generic class, and was necessary to prevent a segmentation fault when the thread pool goes out of scope.

The tight inner loops for culling composite number representations have been optimized to some extent in using "loop unpeeling" for smaller base primes to simplify the loops down to simple masking by a constant with eight separate loops for the repeating pattern over bytes and culling by sub buffer CPU L1 cache sizes over the outer sieve buffer size of the CPU L2 cache size in order to make the task work-sized chunks larger for less task context switching overheads and for reduced time lost to culling start address calculations per base prime (which needs to use some integer division that is always slower than other integer operations). This last optimization allows for reasonably efficient culling up to the square of the CPU L2 cache size in bits or 1e12 for the one Megabit CPU L2 cache size many mid-range Intel CPU's have currently when used for multi-threading (half of the actual size for Hyper-Threaded - HT - threads as they share both the L1 and the L2 caches over the pairs of Hyper-Threaded (HT) threads per core).

Although this code can be used for much higher sieving ranges, it is not recommended due to not yet being tuned for better efficiency above 1e12; there are no checks limiting the user to this range, but, as well as decreasing efficiency for sieving limits much higher than this, at some point there will be errors due to integer overflows but these will be for huge sieving ranges taking days -> weeks -> months -> years to execute on common desktop CPU's.

A further optimization used is to create a pre-culled `WHLPTRN` `SieveBuffer` where the odd primes (since we cull odds-only) of 3, 5, 7, 11, 13, and 17 have already been culled and using that to pre-fill the page segment buffers so that no culling by these base prime values is required, this reduces the number of operations by about 45% compared to if it wasn't done but the ratio of better performance is only about 34.5% better as this changes the ratio of (fast) smaller base primes to larger (slower) ones.

All of the improvements to this point allow the shown performance as per the displayed output for the above program; using a command line argument of `--L1=32 --L2=256 --LIMIT=100000000000` (a hundred billion - 1e11 - on this computer, which has cache sizes of that amount and no Hyper-Threading - HT), it can count the primes to 1e11 in about 17.5 seconds using the above mentioned CPU. It will be over two times faster than this using a more modern desktop CPU such as the Intel Core i7-9700K which has twice as many effective cores, a higher CPU clock rate, is about 10% to 15% faster due the a more modern CPU architecture which is three generations newer. Of course using a top end AMD Threadripper CPU with its 64/128 cores/threads will be almost eight times faster again except that it will lose about 20% due to its slower clock speed when all cores/threads are used; note that high core CPU's will only give these speed gains for large sieving ranges such as 1e11 and above since otherwise there aren't enough work chunks to go around for all the threads available!

Incredibly, even run single threaded (argument of `--NUMTHRDS=1`) this implementation is only about 20% slower than the reference Sieve of Atkin "primegen/primespeed" implementation in counting the number of primes to a billion and is about 20% faster in counting the primes to a hundred billion (arguments of `--LIMIT=100000000000 --NUMTHRDS=1`) with both using the same size of CPU L1 cache buffer of 16 Kilobytes; This implementation does not yet have the level of wheel optimization of the Sieve of Atkin as it has only the limited wheel optimization of Odds-Only plus the use of the pre-cull fill. Maximum wheel factorization will reduce the number of operations for this code to less than about half the current number, making it faster than the Sieve of Atkin for all ranges, and approach the speed of Kim Walisch's "primesieve". However, not having primitive element pointers and pointer operations, there are some optimizations used that Kim Walisch's "primesieve" uses of extreme loop unrolling that mean that it can never quite reach the speed of "primeseive" by about 20% to 30%.

The above code is a fairly formidable benchmark, which I have also written in Fortran as in likely the major computer language that is comparable. I see that Chapel has the following advantages over Fortran:

1) It is somewhat cleaner to read and write code with more modern forms of expression, especially as to declaring variables/constants which can often be inferred as to type.

2) The Object Oriented Programming paradigm has been designed in from the beginning and isn't just an add-on that needs to be careful not to break legacy code; Fortran's method of expression this paradigm using modules seems awkward by comparison.

3) It has some more modern forms of automatic memory management as to type safety and sharing of allocated memory structures.

4) It has several modern forms of managing concurrency built in from the beginning rather than being add-on's or just being the ability to call through to OpenMP/MPI.

That said, it also as the following disadvantages, at least as I see it:

1) One of the worst things about Chapel is the slow compilation speed, which is about ten times slower than GNU gfortran.

2) It's just my personal opinion, but so much about forms of expression have been modernized and improved, it seems very dated to go back to using curly braces to delineate code blocks and semi-colons as line terminators; Most modern languages at least dispense with the latter.

3) Some programming features offered are still being defined, although most evolutionary changes now no longer are breaking code changes.

Speed isn't really an issue with either one, with some types of tasks better suited to one or the other but mostly about the same; for this particular task they are about the same if one were to implement the same algorithmic optimizations other than that one can do some of the extreme loop unrolling optimization with Fortran that can't be done with Chapel as Fortran has some limited form of pointers, although not the full set of pointer operators that C/C++ like languages have. I think that if both were optimized as much as each is capable, Fortran may run about 20% faster, perhaps due to the maturity of its compile and due to the availablity of (limited) pointer operations.

The primary additional optimization available to Chapel code is the addition of Maximum Wheel-Factorization as per my StackOverflow JavaScript Tutorial answer, with the other major improvement to add "bucket sieving" for sieving limits above about 1e12 so as to get reasonable efficiency up to 1e16 and above.
