---
title: "Sieve of Eratosthenes (part 9/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 9/21
---

## Go

### Basic sieve of array of booleans

```mw
package main
import "fmt"

func main() {
    const limit = 201 // means sieve numbers < 201

    // sieve
    c := make([]bool, limit) // c for composite.  false means prime candidate
    c[1] = true              // 1 not considered prime
    p := 2
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
    for n := 1; n < limit; n++ {
        if c[n] {
            fmt.Print("  .")
        } else {
            fmt.Printf("%3d", n)
        }
        if n%20 == 0 {
            fmt.Println("")
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

### Odds-only bit-packed array output-enumerating version

The above version's output is rather specialized; the following version uses a closure function to enumerate over the culled composite number array, which is bit packed. By using this scheme for output, no extra memory is required above that required for the culling array:

```mw
package main

import (
   "fmt"
   "math"
)

func primesOdds(top uint) func() uint {
   topndx := int((top - 3) / 2)
   topsqrtndx := (int(math.Sqrt(float64(top))) - 3) / 2
   cmpsts := make([]uint, (topndx/32)+1)
   for i := 0; i <= topsqrtndx; i++ {
      if cmpsts[i>>5]&(uint(1)<<(uint(i)&0x1F)) == 0 {
         p := (i << 1) + 3
         for j := (p*p - 3) >> 1; j <= topndx; j += p {
            cmpsts[j>>5] |= 1 << (uint(j) & 0x1F)
         }
      }
   }
   i := -1
   return func() uint {
      oi := i
      if i <= topndx {
         i++
      }
      for i <= topndx && cmpsts[i>>5]&(1<<(uint(i)&0x1F)) != 0 {
         i++
      }
      if oi < 0 {
         return 2
      } else {
         return (uint(oi) << 1) + 3
      }
   }
}

func main() {
   iter := primesOdds(100)
   for v := iter(); v <= 100; v = iter() {
      print(v, " ")
   }
   iter = primesOdds(1000000)
   count := 0
   for v := iter(); v <= 1000000; v = iter() {
      count++
   }
   fmt.Printf("\r\n%v\r\n", count)
}
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
78498
```

### Sieve Tree

A fairly odd sieve tree method:

```mw
package main
import "fmt"

type xint uint64
type xgen func()(xint)

func primes() func()(xint) {
   pp, psq := make([]xint, 0), xint(25)

   var sieve func(xint, xint)xgen
   sieve = func(p, n xint) xgen {
      m, next := xint(0), xgen(nil)
      return func()(r xint) {
         if next == nil {
            r = n
            if r <= psq {
               n += p
               return
            }

            next = sieve(pp[0] * 2, psq) // chain in
            pp = pp[1:]
            psq = pp[0] * pp[0]

            m = next()
         }
         switch {
         case n < m: r, n = n, n + p
         case n > m: r, m = m, next()
         default:    r, n, m = n, n + p, next()
         }
         return
      }
   }

   f := sieve(6, 9)
   n, p := f(), xint(0)

   return func()(xint) {
      switch {
      case p < 2: p = 2
      case p < 3: p = 3
      default:
         for p += 2; p == n; {
            p += 2
            if p > n {
               n = f()
            }
         }
         pp = append(pp, p)
      }
      return p
   }
}

func main() {
   for i, p := 0, primes(); i < 100000; i++ {
      fmt.Println(p())
   }
}
```

### Concurrent Daisy-chain sieve

A concurrent prime sieve adopted from the example in the "Go Playground" window at http://golang.org/

```mw
package main
import "fmt"
 
// Send the sequence 2, 3, 4, ... to channel 'out'
func Generate(out chan<- int) {
   for i := 2; ; i++ {
      out <- i                  // Send 'i' to channel 'out'
   }
}
 
// Copy the values from 'in' channel to 'out' channel,
//   removing the multiples of 'prime' by counting.
// 'in' is assumed to send increasing numbers
func Filter(in <-chan int, out chan<- int, prime int) {
        m := prime + prime                // first multiple of prime
   for {
      i := <- in                // Receive value from 'in'
      for i > m {
         m = m + prime     // next multiple of prime
         }
      if i < m {
         out <- i          // Send 'i' to 'out'
         }
   }
}
 
// The prime sieve: Daisy-chain Filter processes
func Sieve(out chan<- int) {
   gen := make(chan int)             // Create a new channel
   go Generate(gen)                  // Launch Generate goroutine
   for  {
      prime := <- gen
      out <- prime
      ft := make(chan int)
      go Filter(gen, ft, prime)
      gen = ft
   }
}

func main() {
   sv := make(chan int)              // Create a new channel
   go Sieve(sv)                      // Launch Sieve goroutine
   for i := 0; i < 1000; i++ {
      prime := <- sv
      if i >= 990 { 
          fmt.Printf("%4d ", prime) 
          if (i+1)%20==0 {
         fmt.Println("")
          }
      }
   }
}
```

The output:

```
7841 7853 7867 7873 7877 7879 7883 7901 7907 7919 
```

Runs at ~ n^2.1 empirically, producing up to n=3000 primes in under 5 seconds.

### Postponed Concurrent Daisy-chain sieve

Here we postpone the *creation* of filters until the prime's square is seen in the input, to radically reduce the amount of filter channels in the sieve chain.

```mw
package main
import "fmt"
 
// Send the sequence 2, 3, 4, ... to channel 'out'
func Generate(out chan<- int) {
   for i := 2; ; i++ {
      out <- i                  // Send 'i' to channel 'out'
   }
}
 
// Copy the values from 'in' channel to 'out' channel,
//   removing the multiples of 'prime' by counting.
// 'in' is assumed to send increasing numbers
func Filter(in <-chan int, out chan<- int, prime int) {
        m := prime * prime                // start from square of prime
   for {
      i := <- in                // Receive value from 'in'
      for i > m {
         m = m + prime     // next multiple of prime
         }
      if i < m {
         out <- i          // Send 'i' to 'out'
         }
   }
}
 
// The prime sieve: Postponed-creation Daisy-chain of Filters
func Sieve(out chan<- int) {
   gen := make(chan int)             // Create a new channel
   go Generate(gen)                  // Launch Generate goroutine
   p := <- gen
   out <- p
   p = <- gen          // make recursion shallower ---->
   out <- p            // (Go channels are _push_, not _pull_)
   
   base_primes := make(chan int)     // separate primes supply  
   go Sieve(base_primes)             
   bp := <- base_primes              // 2           <---- here
   bq := bp * bp                     // 4

   for  {
      p = <- gen
      if p == bq {                    // square of a base prime
         ft := make(chan int)
         go Filter(gen, ft, bp)  // filter multiples of bp in gen out
         gen = ft
         bp = <- base_primes     // 3
         bq = bp * bp            // 9
      } else {
         out <- p
      }
   }
}

func main() {
   sv := make(chan int)              // Create a new channel
   go Sieve(sv)                      // Launch Sieve goroutine
   lim := 25000              
   for i := 0; i < lim; i++ {
      prime := <- sv
      if i >= (lim-10) { 
          fmt.Printf("%4d ", prime) 
          if (i+1)%20==0 {
         fmt.Println("")
          }
      }
   }
}
```

The output:

```
286999 287003 287047 287057 287059 287087 287093 287099 287107 287117 
```

Runs at ~ n^1.2 empirically, producing up to n=25,000 primes on ideone in under 5 seconds.

### Incremental Odds-only Sieve

Uses Go's built-in hash tables to store odd composites, and defers adding new known composites until the square is seen.

```mw
package main

import "fmt"

func main() {
    primes := make(chan int)
    go PrimeSieve(primes)

    p := <-primes
    for p < 100 {
        fmt.Printf("%d ", p)
        p = <-primes
    }

    fmt.Println()
}

func PrimeSieve(out chan int) {
    out <- 2
    out <- 3

    primes := make(chan int)
    go PrimeSieve(primes)

    var p int
    <-primes
    p = <-primes

    sieve := make(map[int]int)
    q := p * p
    n := p

    for {
        n += 2
        step, isComposite := sieve[n]
        if isComposite {
            delete(sieve, n)
            m := n + step
            for sieve[m] != 0 {
                m += step
            }
            sieve[m] = step

        } else if n < q {
            out <- n

        } else {
            step = p + p
            m := n + step
            for sieve[m] != 0 {
                m += step
            }
            sieve[m] = step
            p = <-primes
            q = p * p
        }
    }
}
```

The output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Golfscript

```
{:j;.@.@<@@\)>j\++}:at;
{):q;:z{q<}{z+}/}:mt;

~:J.([0]*1[.]\+\2-1??),2>
{:I; .I=! {I.* J mt {1 at}/}*}/

0\ {
!{.p}*
1+
}/;
```

**Output  —  for input `100`:**

```
2
3
5
6
7
10
11
13
14
15
17
19
21
22
23
26
29
30
31
33
34
35
37
38
39
41
42
43
46
47
51
53
55
57
58
59
61
62
65
66
67
69
70
71
73
74
77
78
79
82
83
85
86
87
89
91
93
94
95
97
```


## Groovy

This solution uses a BitSet for compactness and speed, but in Groovy, BitSet has full List semantics. It also uses both the "square root of the boundary" shortcut and the "square of the prime" shortcut.

```mw
def sievePrimes = { bound -> 
    def isPrime  = new BitSet(bound)
    isPrime[0..1] = false
    isPrime[2..bound] = true
    (2..(Math.sqrt(bound))).each { pc ->
        if (isPrime[pc]) {
            ((pc**2)..bound).step(pc) { isPrime[it] = false }
        }
    }
    (0..bound).findAll { isPrime[it] }
}
```

Test:

```mw
println sievePrimes(100)
```

Output:

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## GW-BASIC

```mw
10  INPUT "ENTER NUMBER TO SEARCH TO: ";LIMIT
20  DIM FLAGS(LIMIT)
30  FOR N = 2 TO SQR (LIMIT)
40  IF FLAGS(N) < > 0 GOTO 80
50  FOR K = N * N TO LIMIT STEP N
60  FLAGS(K) = 1
70  NEXT K
80  NEXT N
90  REM  DISPLAY THE PRIMES
100  FOR N = 2 TO LIMIT
110  IF FLAGS(N) = 0 THEN PRINT N;", ";
120  NEXT N
```
