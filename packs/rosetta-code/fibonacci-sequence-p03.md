---
title: "Fibonacci sequence (part 3/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/10
---

## Brainf***

Works with

:

Brainf***

version implementations with unbounded cell size

The first cell contains *n* (10), the second cell will contain *fib(n)* (55), and the third cell will contain *fib(n-1)* (34).

```mw
++++++++++
>>+<<[->[->+>+<<]>[-<+>]>[-<+>]<<<]

Print the number
>>[-]<[->+<]>

>+
[[-]<
  [->+<
    [->+<[->+<[->+<[->+<[->+<[->+<[->+<[->+<
      [->[-]>>+>+<<<]
    ]]]]]]]]<
  ]>>[>]++++++[-<++++++++>]>>
]<<<[.[-]<<<]

<+++++++++++++.---.
```

**Output:**

```
55
```

The following generates n fibonacci numbers and prints them, though not in ascii. It does have a limit due to the cells usually being 1 byte in size.

```mw
+++++ +++++ #0 set to n
>> +     Init #2 to 1
<<
[
   -  #Decrement counter in #0
   >>.   Notice: This doesn't print it in ascii
      To look at results you can pipe into a file and look with a hex editor
   
      Copying sequence to save #2 in #4 using #5 as restore space
   >>[-] Move to #4 and clear
   >[-]  Clear #5
   <<<   #2
   [  Move loop
      - >> + > + <<< Subtract #2 and add #4 and #5
   ]
   >>>
   [  Restore loop
      - <<< + >>> Subtract from #5 and add to #2
   ]

   <<<<  Back to #1
      Non destructive add sequence using #3 as restore value
   [  Loop to add
      - > + > + <<   Subtract #1 and add to value #2 and restore space #3
   ]
   >>
   [  Loop to restore #1 from #3
      - << + >>   Subtract from restore space #3 and add in #1
   ]
   
   << [-]   Clear #1
   >>>
   [  Loop to move #4 to #1
      - <<< + >>> Subtract from #4 and add to #1
   ]
   <<<<  Back to #0
]
```


## Brat

### Recursive

```mw
fibonacci = { x |
        true? x < 2, x, { fibonacci(x - 1) + fibonacci(x - 2) }
}
```

### Tail Recursive

```mw
fib_aux = { x, next, result |
        true? x == 0,
                result,
                { fib_aux x - 1, next + result, next }
}

fibonacci = { x |
  fib_aux x, 1, 0
}
```

### Memoization

```mw
cache = hash.new

fibonacci = { x |
  true? cache.key?(x)
    { cache[x] }
    {true? x < 2, x, { cache[x] = fibonacci(x - 1) + fibonacci(x - 2) }}
}
```


## Bruijn

```mw
:import std/Combinator .
:import std/Math .
:import std/List .

# unary/Church fibonacci (moderately fast but very high space complexity)
fib-unary [0 [[[2 0 [2 (1 0)]]]] k i]

:test (fib-unary (+6u)) ((+8u))

# ternary fibonacci using infinite list iteration (very fast)
fib-list \index fibs
   fibs head <$> (iterate &[[0 : (1 + 0)]] ((+0) : (+1)))

:test (fib-list (+6)) ((+8))

# recursive fib (very slow)
fib-rec y [[0 <? (+1) (+0) (0 <? (+2) (+1) rec)]]
   rec (1 --0) + (1 --(--0))

:test (fib-rec (+6)) ((+8))
```

Performance using `HigherOrder` reduction without optimizations:

```mw
> :time fib-list (+1000)
0.9 seconds
> :time fib-unary (+50u)
1.7 seconds
> :time fib-rec (+25)
5.1 seconds
> :time fib-list (+50)
0.0006 seconds
```


## Burlesque

```mw
{0 1}{^^++[+[-^^-]\/}30.*\[e!vv
```

```mw
0 1{{.+}c!}{1000.<}w!
```


## C

### Recursive

```mw
long long fibb(long long a, long long b, int n) {
    return (--n>0)?(fibb(b, a+b, n)):(a);
}
```

### Iterative

```mw
long long int fibb(int n) {
   int fnow = 0, fnext = 1, tempf;
   while(--n>0){
      tempf = fnow + fnext;
      fnow = fnext;
      fnext = tempf;
      }
      return fnext;  
}
```

### Analytic

```mw
#include <tgmath.h>
#define PHI ((1 + sqrt(5))/2)

long long unsigned fib(unsigned n) {
    return floor( (pow(PHI, n) - pow(1 - PHI, n))/sqrt(5) );
}
```

### Generative

Translation of

:

Python

Works with

:

gcc

version version 4.1.2 20080704 (Red Hat 4.1.2-44)

```mw
#include <stdio.h>
typedef enum{false=0, true=!0} bool;
typedef void iterator;

#include <setjmp.h>
/* declare label otherwise it is not visible in sub-scope */
#define LABEL(label) jmp_buf label; if(setjmp(label))goto label;
#define GOTO(label) longjmp(label, true)

/* the following line is the only time I have ever required "auto" */
#define FOR(i, iterator) { auto bool lambda(i); yield_init = (void *)&lambda; iterator; bool lambda(i)
#define DO {
#define     YIELD(x) if(!yield(x))return
#define     BREAK    return false
#define     CONTINUE return true
#define OD CONTINUE; } }

static volatile void *yield_init; /* not thread safe */
#define YIELDS(type) bool (*yield)(type) = yield_init

iterator fibonacci(int stop){
    YIELDS(int);
    int f[] = {0, 1};
    int i;
    for(i=0; i<stop; i++){
        YIELD(f[i%2]);
        f[i%2]=f[0]+f[1];
    }
}

main(){
  printf("fibonacci: ");
  FOR(int i, fibonacci(16)) DO
    printf("%d, ",i);
  OD;
  printf("...\n");
}
```

**Output:**

```
fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
```

### Fast method for a single large value

```mw
#include <stdlib.h>
#include <stdio.h>
#include <gmp.h>

typedef struct node node;
struct node {
   int n;
   mpz_t v;
   node *next;
};

#define CSIZE 37
node *cache[CSIZE];

// very primitive linked hash table
node * find_cache(int n)
{
   int idx = n % CSIZE;
   node *p;

   for (p = cache[idx]; p && p->n != n; p = p->next);
   if (p) return p;

   p = malloc(sizeof(node));
   p->next = cache[idx];
   cache[idx] = p;

   if (n < 2) {
      p->n = n;
      mpz_init_set_ui(p->v, 1);
   } else {
      p->n = -1; // -1: value not computed yet
      mpz_init(p->v);
   }
   return p;
}

mpz_t tmp1, tmp2;
mpz_t *fib(int n)
{
   int x;
   node *p = find_cache(n);

   if (p->n < 0) {
      p->n = n;
      x = n / 2;

      mpz_mul(tmp1, *fib(x-1), *fib(n - x - 1));
      mpz_mul(tmp2, *fib(x), *fib(n - x));
      mpz_add(p->v, tmp1, tmp2);
   }
   return &p->v;
}

int main(int argc, char **argv)
{
   int i, n;
   if (argc < 2) return 1;

   mpz_init(tmp1);
   mpz_init(tmp2);

   for (i = 1; i < argc; i++) {
      n = atoi(argv[i]);
      if (n < 0) {
         printf("bad input: %s\n", argv[i]);
         continue;
      }

      // about 75% of time is spent in printing
      gmp_printf("%Zd\n", *fib(n));
   }
   return 0;
}
```

**Output:**

```
% ./a.out 0 1 2 3 4 5
1
1
2
3
5
8
% ./a.out 10000000 | wc -c    # count length of output, including the newline
1919488
```


## C

### Recursive

```mw
public static ulong Fib(uint n) {
    return (n < 2)? n : Fib(n - 1) + Fib(n - 2);
}
```

### Tail-Recursive

```mw
public static ulong Fib(uint n) {
    return Fib(0, 1, n);
}

private static ulong Fib(ulong a, ulong b, uint n) {
    return (n < 1)? a :(n == 1)?  b : Fib(b, a + b, n - 1);
}
```

### Iterative

```mw
public static ulong Fib(uint x) {
    if (x == 0) return 0;

    ulong prev = 0;
    ulong next = 1;
    for (int i = 1; i < x; i++)
    {
        ulong sum = prev + next;
        prev = next;
        next = sum;
    }
    return next;
}
```

### Iterative

```mw
using System; using System.Text; // FIBRUS.cs Russia
namespace Fibrus { class Program { static void Main() 
{ long fi1=1; long fi2=1; long fi3=1; int da; int i; int d; 
for (da=1; da<=78; da++) // rextester.com/MNGUV70257
    { d = 20-Convert.ToInt32((Convert.ToString(fi3)).Length);
    for (i=1; i<d; i++) Console.Write(".");
Console.Write(fi3); Console.Write(" "); Console.WriteLine(da);
    fi3 = fi2 + fi1;
    fi1 = fi2;
    fi2 = fi3;
}}}}
```

**Output:**

```
..................1 1
..................2 2
..................3 3
...
...5527939700884757 76
...8944394323791464 77
..14472334024676221 78
```

### Eager-Generative

```mw
public static IEnumerable<long> Fibs(uint x) {
    IList<ulong> fibs = new List<ulong>();

    ulong prev = -1;
    ulong next = 1;
    for (int i = 0; i < x; i++)
    {
     long sum = prev + next;
        prev = next;
        next = sum;
        fibs.Add(sum); 
    }
    return fibs;
}
```

### Lazy-Generative

```mw
public static IEnumerable<ulong> Fibs(uint x) {
    ulong prev = -1;
    ulong next = 1;
    for (uint i = 0; i < x; i++) {
        ulong sum = prev + next;
        prev = next;
        next = sum;
        yield return sum;
    }
}
```

### Analytic

This returns digits up to the 93rd Fibonacci number, but the digits become inaccurate past the 71st. There is custom rounding applied to the result that allows the function to be accurate at the 71st number instead of topping out at the 70th.

```mw
static double r5 = Math.Sqrt(5.0), Phi = (r5 + 1.0) / 2.0;

static ulong fib(uint n) {
    if (n > 71) throw new ArgumentOutOfRangeException("n", n, "Needs to be smaller than 72."); 
    double r = Math.Pow(Phi, n) / r5; 
    return (ulong)(n < 64 ? Math.Round(r) : Math.Floor(r)); }
```

To get to the 93rd Fibonacci number, one must use the decimal type, rather than the double type, like this:

```mw
static decimal Sqrt_dec(decimal x, decimal g) { decimal t, lg;
    do { t = x / g; lg = g; g = (t + g) / 2M; } while (lg != g);
    return g; }

static decimal Pow_dec (decimal bas, uint exp) {
    if (exp == 0) return 1M;
    decimal tmp = Pow_dec(bas, exp >> 1); tmp *= tmp;
    if ((exp & 1) == 1) tmp *= bas; return tmp; }

static decimal r5 = Sqrt_dec(5.0M, (decimal)Math.Sqrt(5.0)),
               Phi = (r5 + 1.0M) / 2.0M;

static ulong fib(uint n) {
    if (n > 93) throw new ArgumentOutOfRangeException("n", n, "Needs to be smaller than 94."); 
    decimal r = Pow_dec(Phi, n) / r5; 
    return (ulong)(n < 64 ? Math.Round(r) : Math.Floor(r)); }
```

Note that the Math.Pow() function and the Math.Sqrt() function must be replaced with ones returning the decimal type. If one allows the fib() function to return the decimal type, one can reach the 138th Fibonacci number. However, the accuracy is lost after the 128th.

```mw
static decimal Sqrt_dec(decimal x, decimal g) { decimal t, lg;
    do { t = x / g; lg = g; g = (t + g) / 2M; } while (lg != g);
    return g; }

static decimal Pow_dec (decimal bas, uint exp) {
    if (exp == 0) return 1M;
    decimal tmp = Pow_dec(bas, exp >> 1); tmp *= tmp;
    if ((exp & 1) == 1) tmp *= bas; return tmp; }

static decimal r5 = Sqrt_dec(5.0M, (decimal)Math.Sqrt(5.0)),
               Phi = (r5 + 1.0M) / 2.0M;

static decimal fib(uint n) {
    if (n > 128) throw new ArgumentOutOfRangeException("n", n, "Needs to be smaller than 129."); 
    decimal r = Pow_dec(Phi, n) / r5; 
    return n < 64 ? Math.Round(r) : Math.Floor(r); }
```

### Matrix

Algorithm is based on

${\displaystyle {\begin{pmatrix}1&1\\1&0\end{pmatrix}}^{n}={\begin{pmatrix}F(n+1)&F(n)\\F(n)&F(n-1)\end{pmatrix}}}$

.

Needs `System.Windows.Media.Matrix` or similar Matrix class. Calculates in ${\displaystyle O(n)}$ .

```mw
public static ulong Fib(uint n) {
    var M = new Matrix(1,0,0,1);
    var N = new Matrix(1,1,1,0);
    for (uint i = 1; i < n; i++) M *= N;
    return (ulong)M[0][0];
}
```

Needs `System.Windows.Media.Matrix` or similar Matrix class. Calculates in ${\displaystyle O(\log {n})}$ .

```mw
private static Matrix M;
private static readonly Matrix N = new Matrix(1,1,1,0);

public static ulong Fib(uint n) {
    M = new Matrix(1,0,0,1);
    MatrixPow(n-1);
    return (ulong)M[0][0];
}

private static void MatrixPow(double n){
    if (n > 1) {
        MatrixPow(n/2);
        M *= M;
    }
    if (n % 2 == 0) M *= N;
}
```

### Array (Table) Lookup

```mw
private static int[] fibs = new int[]{ -1836311903, 1134903170, 
  -701408733, 433494437, -267914296, 165580141, -102334155, 
  63245986, -39088169, 24157817, -14930352, 9227465, -5702887, 
  3524578, -2178309, 1346269, -832040, 514229, -317811, 196418, 
  -121393, 75025, -46368, 28657, -17711, 10946, -6765, 4181, 
  -2584, 1597, -987, 610, -377, 233, -144, 89, -55, 34, -21, 13, 
  -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
  144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
  28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
  1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
  39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
  701408733, 1134903170, 1836311903};

public static int Fib(int n) {
    if(n < -46 || n > 46) throw new ArgumentOutOfRangeException("n", n, "Has to be between -46 and 47.")
    return fibs[n+46];
}
```

### Arbitrary Precision

Library:

System.Numerics

This large step recurrence routine can calculate the two millionth Fibonacci number in under 1 / 5 second at tio.run. This routine can generate the fifty millionth Fibonacci number in under 30 seconds at tio.run. The unused conventional iterative method times out at two million on tio.run, you can only go to around 1,290,000 or so to keep the calculation time (plus string conversion time) under the 60 second timeout limit there. When using this large step recurrence method, it takes around 5 seconds to convert the two millionth Fibonacci number (417975 digits) into a string (so that one may count those digits).

```mw
using System;
using System.Collections.Generic;
using BI = System.Numerics.BigInteger;
 
class Program
{
    // A sparse array of values calculated along the way
    static SortedList<int, BI> sl = new SortedList<int, BI>();
 
    // This routine is semi-recursive, but doesn't need to evaluate every number up to n.
    // Algorithm from here: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section3
    static BI Fsl(int n)
    {
        if (n < 2) return n;
        int n2 = n >> 1, pm = n2 + ((n & 1) << 1) - 1; IfNec(n2); IfNec(pm);
        return n2 > pm ? (2 * sl[pm] + sl[n2]) * sl[n2] : sqr(sl[n2]) + sqr(sl[pm]);
        // Helper routine for Fsl(). It adds an entry to the sorted list when necessary
        void IfNec(int x) { if (!sl.ContainsKey(x)) sl.Add(x, Fsl(x)); }
        // Helper function to square a BigInteger
        BI sqr(BI x) { return x * x; }
    }
 
    // Conventional iteration method (not used here)
    public static BI Fm(BI n)
    {
        if (n < 2) return n; BI cur = 0, pre = 1;
        for (int i = 0; i <= n - 1; i++) { BI sum = cur + pre; pre = cur; cur = sum; }
        return cur;
    }
 
    public static void Main()
    {
        int num = 2_000_000, digs = 35, vlen;
        var sw = System.Diagnostics.Stopwatch.StartNew(); var v = Fsl(num); sw.Stop();
        Console.Write("{0:n3} ms to calculate the {1:n0}th Fibonacci number, ",
          sw.Elapsed.TotalMilliseconds, num);
        Console.WriteLine("number of digits is {0}", vlen = (int)Math.Ceiling(BI.Log10(v)));
        if (vlen < 10000) {
            sw.Restart(); Console.WriteLine(v); sw.Stop();
            Console.WriteLine("{0:n3} ms to write it to the console.", sw.Elapsed.TotalMilliseconds);
        } else
            Console.Write("partial: {0}...{1}", v / BI.Pow(10, vlen - digs), v % BI.Pow(10, digs));
    }
}
```

**Output:**

```
137.209 ms to calculate the 2,000,000th Fibonacci number, number of digits is 417975
partial: 85312949175076415430516606545038251...91799493108960825129188777803453125
```

### Shift PowerMod

Library:

System.Numerics

Illustrated here is an algorithm to compute a Fibonacci number directly, without needing to calculate any of the Fibonacci numbers less than the desired result. It uses shifting and the power mod function (`BigInteger.ModPow()` in C#). It calculates more quickly than the large step recurrence routine (illustrated above) for smaller Fibonacci numbers (less than 2800 digits or so, around Fibonacci(13000)), but gets slower for larger ones, as the intermediate BigIntegers created are very large, much larger than the Fibonacci result.

Also included is a routine that returns an array of Fibonacci numbers (`fibTab()`). It reuses the intermediate large shifted BigIntegers on suceeding iterations, therfore it is a little more efficient than calling the oneshot (`oneFib()`) routine repeatedly from a loop.

```mw
using System;
using BI = System.Numerics.BigInteger;

class Program {
  
  // returns the nth Fibonacci number without calculating 0..n-1
  static BI oneFib(int n) {
    BI z = (BI)1 << ++n;
    return BI.ModPow(z, n, (z << n) - z - 1) % z;
  }

  // returns an array of Fibonacci numbers from the 0th to the nth
  static BI[] fibTab(int n) {
    var res = new BI[++n];
    BI z = (BI)1 << 1, zz = z << 1;
    for (int i = 0; i < n; ) {
      res[i] = BI.ModPow(z, ++i, zz - z - 1) % z;
      z <<= 1; zz <<= 2;
    }
    return res;
  }
  
  static void Main(string[] args) {
    int n = 20;
    Console.WriteLine("Fibonacci numbers 0..{0}: {1}", n, string.Join(" ",fibTab(n)));
    n = 1000;
    Console.WriteLine("Fibonacci({0}): {1}", n, oneFib(n));
  }
}
```

**Output:**

```
Fibonacci numbers 0..20: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
Fibonacci(1000): 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
```


## C++

Using unsigned int, this version only works up to 48 before fib overflows.

```mw
#include <iostream>

int main()
{
        unsigned int a = 1, b = 1;
        unsigned int target = 48;
        for(unsigned int n = 3; n <= target; ++n)
        {
                unsigned int fib = a + b;
                std::cout << "F("<< n << ") = " << fib << std::endl;
                a = b;
                b = fib;
        }

        return 0;
}
```

Library:

GMP

This version does not have an upper bound.

```mw
#include <iostream>
#include <gmpxx.h>

int main()
{
        mpz_class a = mpz_class(1), b = mpz_class(1);
        mpz_class target = mpz_class(100);
        for(mpz_class n = mpz_class(3); n <= target; ++n)
        {
                mpz_class fib = b + a;
                if ( fib < b )
                {
                        std::cout << "Overflow at " << n << std::endl;
                        break;
                }
                std::cout << "F("<< n << ") = " << fib << std::endl;
                a = b;
                b = fib;
        }
        return 0;
}
```

Version using transform:

```mw
#include <algorithm>
#include <vector>
#include <functional>
#include <iostream>
 
unsigned int fibonacci(unsigned int n) {
  if (n == 0) return 0;
  std::vector<int> v(n+1);
  v[1] = 1;
  transform(v.begin(), v.end()-2, v.begin()+1, v.begin()+2, std::plus<int>());
  // "v" now contains the Fibonacci sequence from 0 up
  return v[n];
}
```

Far-fetched version using adjacent_difference:

```mw
#include <numeric>
#include <vector>
#include <functional>
#include <iostream>

unsigned int fibonacci(unsigned int n) {
  if (n == 0) return 0;
  std::vector<int> v(n, 1);
  adjacent_difference(v.begin(), v.end()-1, v.begin()+1, std::plus<int>());
  // "array" now contains the Fibonacci sequence from 1 up
  return v[n-1];
}
```

Version which computes at compile time with metaprogramming:

```mw
#include <iostream>

template <int n> struct fibo
{
    enum {value=fibo<n-1>::value+fibo<n-2>::value};
};
 
template <> struct fibo<0>
{
    enum {value=0};
};

template <> struct fibo<1>
{
    enum {value=1};
};

int main(int argc, char const *argv[])
{
    std::cout<<fibo<12>::value<<std::endl;
    std::cout<<fibo<46>::value<<std::endl;
    return 0;
}
```

The following version is based on fast exponentiation:

```mw
#include <iostream>

inline void fibmul(int* f, int* g)
{
  int tmp = f[0]*g[0] + f[1]*g[1];
  f[1] = f[0]*g[1] + f[1]*(g[0] + g[1]);
  f[0] = tmp;
}

int fibonacci(int n)
{
  int f[] = { 1, 0 };
  int g[] = { 0, 1 };
  while (n > 0)
  {
    if (n & 1) // n odd
    {
      fibmul(f, g);
      --n;
    }
    else
    {
      fibmul(g, g);
      n >>= 1;
    }
  }
  return f[1];
}

int main()
{
  for (int i = 0; i < 20; ++i)
    std::cout << fibonacci(i) << " ";
  std::cout << std::endl;
}
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
```

### Using Zeckendorf Numbers

The nth fibonacci is represented as Zeckendorf 1 followed by n-1 zeroes. Here I define a class N which defines the operations increment ++() and comparison <=(other N) for Zeckendorf Numbers.

```mw
// Use Zeckendorf numbers to display Fibonacci sequence.
// Nigel Galloway October 23rd., 2012
int main(void) {
  char NG[22] = {'1',0};
  int x = -1;
  N G;
  for (int fibs = 1; fibs <= 20; fibs++) {
   for (;G <= N(NG); ++G) x++;
   NG[fibs] = '0';
   NG[fibs+1] = 0;
   std::cout << x << " ";
  }
  std::cout << std::endl;
  return 0;
}
```

**Output:**

```
1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946
```

### Using Standard Template Library

Possibly less "Far-fetched version".

```mw
// Use Standard Template Library to display Fibonacci sequence.
// Nigel Galloway March 30th., 2013
#include <algorithm>
#include <iostream>
#include <iterator>
int main()
{
   int x = 1, y = 1;
   generate_n(std::ostream_iterator<int>(std::cout, " "), 21, [&]{int n=x; x=y; y+=n; return n;});
   return 0;
}
```

**Output:**

1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946


## Calcscript

```
(def fib (i)
  (eq (any= i 0) 0
      (any= i 1) 1
      (+ (fib (-1 i)) (fib (- i 2)))))

(def loop (r)
  (eq (list? (cdr r))
    (d (p (fib (car r)))
       (loop (cdr r))))
    (Same))

(loop (range 1 12))
```

**Output:**

```
1
1
2
3
5
8
13
21
34
55
89
```


## Cat

```mw
define fib {
  dup 1 <=
    []
    [dup 1 - fib swap 2 - fib +]
  if
}
```


## Chapel

```mw
iter fib() {
        var a = 0, b = 1;

        while true {
                yield a;
                (a, b) = (b, b + a);
        }
}
```


## Chef

```mw
Stir-Fried Fibonacci Sequence.

An unobfuscated iterative implementation.
It prints the first N + 1 Fibonacci numbers,
where N is taken from standard input.

Ingredients.
0 g last
1 g this
0 g new
0 g input

Method.
Take input from refrigerator.
Put this into 4th mixing bowl.
Loop the input.
Clean the 3rd mixing bowl.
Put last into 3rd mixing bowl.
Add this into 3rd mixing bowl.
Fold new into 3rd mixing bowl.
Clean the 1st mixing bowl.
Put this into 1st mixing bowl.
Fold last into 1st mixing bowl.
Clean the 2nd mixing bowl.
Put new into 2nd mixing bowl.
Fold this into 2nd mixing bowl.
Put new into 4th mixing bowl.
Endloop input until looped.
Pour contents of the 4th mixing bowl into baking dish.

Serves 1.
```


## Chez Scheme

```mw
(define fib (lambda (n) (cond ((> n 1) (+ (fib (- n 1)) (fib (- n 2)))) 
                              ((= n 1) 1) 
                              ((= n 0) 0))))
```


## Clio

Clio is pure and functions are lazy and memoized by default

```mw
fn fib n:
  if n < 2: n
  else: (n - 1 -> fib) + (n - 2 -> fib)

[0:100] -> * fib -> * print
```


## Clojure

### Lazy Sequence

This is implemented idiomatically as an infinitely long, lazy sequence of all Fibonacci numbers:

```mw
(defn fibs []
  (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1])))
```

Thus to get the nth one:

```mw
(nth (fibs) 5)
```

So long as one does not hold onto the head of the sequence, this is unconstrained by length.

The one-line implementation may look confusing at first, but on pulling it apart it actually solves the problem more "directly" than a more explicit looping construct.

```mw
(defn fibs []
  (map first ;; throw away the "metadata" (see below) to view just the fib numbers
       (iterate ;; create an infinite sequence of [prev, curr] pairs
         (fn [[a b]] ;; to produce the next pair, call this function on the current pair
           [b (+ a b)]) ;; new prev is old curr, new curr is sum of both previous numbers
         [0 1]))) ;; recursive base case: prev 0, curr 1
```

A more elegant solution is inspired by the Haskell implementation of an infinite list of Fibonacci numbers:

```mw
(def fib (lazy-cat [0 1] (map + fib (rest fib))))
```

Then, to see the first ten,

```mw
user> (take 10 fib)
(0 1 1 2 3 5 8 13 21 34)
```

### Iterative

Here's a simple interative process (using a recursive function) that carries state along with it (as args) until it reaches a solution:

```mw
;; max is which fib number you'd like computed (0th, 1st, 2nd, etc.)
;; n is which fib number you're on for this call (0th, 1st, 2nd, etc.)
;; j is the nth fib number (ex. when n = 5, j = 5)
;; i is the nth - 1 fib number
(defn- fib-iter
  [max n i j]
  (if (= n max)
    j
    (recur max
           (inc n)
           j
           (+ i j))))

(defn fib
  [max]
  (if (< max 2)
    max
    (fib-iter max 1 0N 1N)))
```

"defn-" means that the function is private (for use only inside this library). The "N" suffixes on integers tell Clojure to use arbitrary precision ints for those.

### Doubling Algorithm (Fast)

Based upon the doubling algorithm which computes in O(log (n)) time as described here https://www.nayuki.io/page/fast-fibonacci-algorithms Implementation credit: https://stackoverflow.com/questions/27466311/how-to-implement-this-fast-doubling-fibonacci-algorithm-in-clojure/27466408#27466408

```mw
(defn fib [n]
  (letfn [(fib* [n]
            (if (zero? n)
              [0 1]
              (let [[a b] (fib* (quot n 2))
                    c (*' a (-' (*' 2 b) a))
                    d (+' (*' b b) (*' a a))]
                (if (even? n)
                  [c d]
                  [d (+' c d)]))))]
    (first (fib* n))))
```

### Recursive

A naive slow recursive solution:

```mw
(defn fib [n]
  (case n
    0 0
    1 1
    (+ (fib (- n 1))
       (fib (- n 2)))))
```

This can be improved to an O(n) solution, like the iterative solution, by memoizing the function so that numbers that have been computed are cached. Like a lazy sequence, this also has the advantage that subsequent calls to the function use previously cached results rather than recalculating.

```mw
(def fib
  (memoize
    (fn [n]
      (case n
        0 0
        1 1
        (+ (fib (- n 1))
           (fib (- n 2)))))))
```

### Using core.async

```mw
(ns fib.core)
(require '[clojure.core.async
           :refer [<! >! >!! <!! timeout chan alt! go]])

(defn fib [c]
  (loop [a 0 b 1]
    (>!! c a)
    (recur b (+ a b))))

(defn -main []
  (let [c (chan)]
    (go (fib c))
    (dorun
      (for [i (range 10)]
        (println (<!! c))))))
```


## CLU

```mw
% Generate Fibonacci numbers
fib = iter () yields (int)
    a: int := 0
    b: int := 1
    
    while true do
        yield (a)
        a, b := b, a+b
    end
end fib

% Grab the n'th value from an iterator 
nth = proc [T: type] (g: itertype () yields (T), n: int) returns (T)
    for v: T in g() do
        if n<=0 then return (v) end
        n := n-1
    end
end nth

% Print a few values
start_up = proc ()
    po: stream := stream$primary_output()
    
    % print values coming out of the fibonacci iterator
    % (which are generated one after the other without delay)
    count: int := 0
    for f: int in fib() do 
        stream$putl(po, "F(" || int$unparse(count) || ") = " || int$unparse(f))
        count := count + 1
        if count = 15 then break end
    end
    
    % print a few random fibonacci numbers
    % (to do this it has to restart at the beginning for each 
    % number, making it O(N))
    fibs: sequence[int] := sequence[int]$[20,30,50]
    for n: int in sequence[int]$elements(fibs) do
        stream$putl(po, "F(" || int$unparse(n) || ") = "
                             || int$unparse(nth[int](fib, n)))
    end
end start_up
```

**Output:**

```
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144
F(13) = 233
F(14) = 377
F(20) = 6765
F(30) = 832040
F(50) = 12586269025
```


## CMake

Iteration uses a while() loop. Memoization uses global properties.

```mw
set_property(GLOBAL PROPERTY fibonacci_0 0)
set_property(GLOBAL PROPERTY fibonacci_1 1)
set_property(GLOBAL PROPERTY fibonacci_next 2)

# var = nth number in Fibonacci sequence.
function(fibonacci var n)
  # If the sequence is too short, compute more Fibonacci numbers.
  get_property(next GLOBAL PROPERTY fibonacci_next)
  if(NOT next GREATER ${n})
    # a, b = last 2 Fibonacci numbers
    math(EXPR i "${next} - 2")
    get_property(a GLOBAL PROPERTY fibonacci_${i})
    math(EXPR i "${next} - 1")
    get_property(b GLOBAL PROPERTY fibonacci_${i})

    while(NOT next GREATER ${n})
      math(EXPR i "${a} + ${b}")  # i = next Fibonacci number
      set_property(GLOBAL PROPERTY fibonacci_${next} ${i})
      set(a ${b})
      set(b ${i})
      math(EXPR next "${next} + 1")
    endwhile()
    set_property(GLOBAL PROPERTY fibonacci_next ${next})
  endif()

  get_property(answer GLOBAL PROPERTY fibonacci_${n})
  set(${var} ${answer} PARENT_SCOPE)
endfunction(fibonacci)
```

```mw
# Test program: print 0th to 9th and 25th to 30th Fibonacci numbers.
set(s "")
foreach(i RANGE 0 9)
  fibonacci(f ${i})
  set(s "${s} ${f}")
endforeach(i)
set(s "${s} ... ")
foreach(i RANGE 25 30)
  fibonacci(f ${i})
  set(s "${s} ${f}")
endforeach(i)
message(${s})
```

```
 0 1 1 2 3 5 8 13 21 34 ... 75025 121393 196418 317811 514229 832040
```


## COBOL

### Iterative

```mw
Program-ID. Fibonacci-Sequence.
Data Division.
Working-Storage Section.
  01  FIBONACCI-PROCESSING.
    05  FIBONACCI-NUMBER  PIC 9(36)   VALUE 0.
    05  FIB-ONE           PIC 9(36)   VALUE 0.
    05  FIB-TWO           PIC 9(36)   VALUE 1.
  01  DESIRED-COUNT       PIC 9(4).
  01  FORMATTING.
    05  INTERM-RESULT     PIC Z(35)9.
    05  FORMATTED-RESULT  PIC X(36).
    05  FORMATTED-SPACE   PIC x(35).
Procedure Division.
  000-START-PROGRAM.
    Display "What place of the Fibonacci Sequence would you like (<173)? " with no advancing.
    Accept DESIRED-COUNT.
    If DESIRED-COUNT is less than 1
      Stop run.
    If DESIRED-COUNT is less than 2
      Move FIBONACCI-NUMBER to INTERM-RESULT
      Move INTERM-RESULT to FORMATTED-RESULT
      Unstring FORMATTED-RESULT delimited by all spaces into FORMATTED-SPACE,FORMATTED-RESULT
      Display FORMATTED-RESULT
      Stop run.
    Subtract 1 from DESIRED-COUNT.
    Move FIBONACCI-NUMBER to INTERM-RESULT.
    Move INTERM-RESULT to FORMATTED-RESULT.
    Unstring FORMATTED-RESULT delimited by all spaces into FORMATTED-SPACE,FORMATTED-RESULT.
    Display FORMATTED-RESULT.
    Perform 100-COMPUTE-FIBONACCI until DESIRED-COUNT = zero.
    Stop run.
  100-COMPUTE-FIBONACCI.
    Compute FIBONACCI-NUMBER = FIB-ONE + FIB-TWO.
    Move FIB-TWO to FIB-ONE.
    Move FIBONACCI-NUMBER to FIB-TWO.
    Subtract 1 from DESIRED-COUNT.
    Move FIBONACCI-NUMBER to INTERM-RESULT.
    Move INTERM-RESULT to FORMATTED-RESULT.
    Unstring FORMATTED-RESULT delimited by all spaces into FORMATTED-SPACE,FORMATTED-RESULT.
    Display FORMATTED-RESULT.
```

### Recursive

Works with

:

GNU Cobol

version 2.0

```mw
       >>SOURCE FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. fibonacci-main.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  num                                 PIC 9(6) COMP.
01  fib-num                             PIC 9(6) COMP.

PROCEDURE DIVISION.
    ACCEPT num
    CALL "fibonacci" USING CONTENT num RETURNING fib-num
    DISPLAY fib-num
    .
END PROGRAM fibonacci-main.

IDENTIFICATION DIVISION.
PROGRAM-ID. fibonacci RECURSIVE.

DATA DIVISION.
LOCAL-STORAGE SECTION.
01  1-before                            PIC 9(6) COMP.
01  2-before                            PIC 9(6) COMP.

LINKAGE SECTION.
01  num                                 PIC 9(6) COMP.

01  fib-num                             PIC 9(6) COMP BASED.

PROCEDURE DIVISION USING num RETURNING fib-num.
    ALLOCATE fib-num
    EVALUATE num
        WHEN 0
            MOVE 0 TO fib-num
        WHEN 1
            MOVE 1 TO fib-num
        WHEN OTHER
            SUBTRACT 1 FROM num
            CALL "fibonacci" USING CONTENT num RETURNING 1-before
            SUBTRACT 1 FROM num
            CALL "fibonacci" USING CONTENT num RETURNING 2-before
            ADD 1-before TO 2-before GIVING fib-num
    END-EVALUATE
    .
END PROGRAM fibonacci.
```


## CoffeeScript

### Analytic

```mw
fib_ana = (n) ->
    sqrt = Math.sqrt
    phi = ((1 + sqrt(5))/2)
    Math.round((Math.pow(phi, n)/sqrt(5)))
```

### Iterative

```mw
fib_iter = (n) ->
    return n if n < 2
    [prev, curr] = [0, 1]
    [prev, curr] = [curr, curr + prev] for i in [1..n]
    curr
```

### Recursive

```mw
fib_rec = (n) ->
  if n < 2 then n else fib_rec(n-1) + fib_rec(n-2)
```


## Comefrom0x10

Recursion is not possible in Comefrom0x10.

### Iterative

```mw
stop = 6
a = 1
i = 1  # start
a      # print result

fib
  comefrom if i is 1  # start
  b = 1
  comefrom fib        # start of loop
  i = i + 1
  next_b = a + b
  a = b
  b = next_b

  comefrom fib if i > stop
```


## Common Lisp

Note that Common Lisp uses bignums, so this will never overflow.

### Iterative

```mw
(defun fibonacci-iterative (n &aux (f0 0) (f1 1))
  (case n
    (0 f0)
    (1 f1)
    (t (loop for n from 2 to n
             for a = f0 then b and b = f1 then result
             for result = (+ a b)
             finally (return result)))))
```

Simpler one:

```mw
(defun fibonacci (n)
  (let ((a 0) (b 1) (c n))
    (loop for i from 2 to n do
    (setq c (+ a b)
          a b
          b c))
    c))
```

Not a function, just printing out the entire (for some definition of "entire") sequence with a `for var =` loop:

```mw
(loop for x = 0 then y and y = 1 then (+ x y) do (print x))
```

### Recursive

```mw
(defun fibonacci-recursive (n)
  (if (< n 2)
      n
     (+ (fibonacci-recursive (- n 2)) (fibonacci-recursive (- n 1)))))
```

```mw
(defun fibonacci-tail-recursive ( n &optional (a 0) (b 1))
  (if (= n 0) 
      a 
      (fibonacci-tail-recursive (- n 1) b (+ a b))))
```

Tail recursive and squaring:

```mw
(defun fib (n &optional (a 1) (b 0) (p 0) (q 1))
    (if (= n 1) (+ (* b p) (* a q))
     (fib (ash n -1) 
          (if (evenp n) a (+ (* b q) (* a (+ p q))))
          (if (evenp n) b (+ (* b p) (* a q)))
          (+ (* p p) (* q q))
          (+ (* q q) (* 2 p q))))) ;p is Fib(2^n-1), q is Fib(2^n).

(print (fib 100000))
```

### Alternate solution

I use Allegro CL 10.1

```mw
;; Project : Fibonacci sequence

(defun fibonacci (nr)
           (cond ((= nr 0) 1)
           ((= nr 1) 1)
           (t (+ (fibonacci (- nr 1))
           (fibonacci (- nr 2))))))
(format t "~a" "First 10 Fibonacci numbers") 
(dotimes (n 10) 
(if (< n 1) (terpri))
(if (< n 9) (format t "~a" " "))
(write(+ n 1)) (format t "~a" ": ")
(write (fibonacci n)) (terpri))
```

Output:

```
First 10 Fibonacci numbers
 1: 1
 2: 1
 3: 2
 4: 3
 5: 5
 6: 8
 7: 13
 8: 21
 9: 34
10: 55
```

### Solution with methods and eql specializers

```mw
(defmethod fib (n)
  (declare ((integer 0 *) n))
  (+ (fib (- n 1))
     (fib (- n 2))))

(defmethod fib ((n (eql 0))) 0)

(defmethod fib ((n (eql 1))) 1)
```

### List-based iterative

This solution uses a list to keep track of the Fibonacci sequence for 0 or a positive integer.

```mw
(defun fibo (n)
  (cond ((< n 0) nil)
        ((< n 2) n)
        (t (let ((leo '(1 0)))
             (loop for i from 2 upto n do
               (setf leo (cons (+ (first leo) 
                                  (second leo))
                               leo))
               finally (return (first leo)))))))
```

**Output:**

```
> (fibo 0)
0
> (fibo 1)
1
> (fibo 10)
55
> (fibo 100)
354224848179261915075
> (fibo 1000)
43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
> (fibo -10)
NIL
```

### List-based recursive

This solution computes Fibonacci numbers as either:

1. a list starting from the first element;
2. a single number;
3. an interval from *i*-th to *j*-th element.

Options #2 and #3 can take negative parameters, but *i* (lowest index in range) must be greater than *j* (highest index in range).

Values are represented internally by a reversed list that grows from the head (and that's why we reverse it back when we return it).

```mw
(defparameter *fibo-start* '(1 1)) ; elements 1 and 2

;;; Helper functions
(defun grow-fibo (fibo)
    (cons (+ (first fibo) (second fibo)) fibo))

(defun generate-fibo (fibo n) ; n must be > 1
    (if (equal (list-length fibo) n)
        fibo
        (generate-fibo (grow-fibo fibo)  n)))

;;; User functions
(defun fibo (n)
    (cond ((= n 0) 0)
          ((= (abs n) 1) 1)
          (t (let ((result (first (generate-fibo *fibo-start* (abs n)))))
               (if (and (< n -1) (evenp n))
                 (- result)
                 result)))))

(defun fibo-list (n)
    (cond ((< n 1) nil)
          ((= n 1) '(1))
          (t (reverse (generate-fibo *fibo-start* n)))))

(defun fibo-range (lower upper)
   (if (<= upper lower)
     nil
     (reverse (generate-fibo
                 (list
                    (fibo (1+ lower))
                    (fibo  lower))
                 (1+ (- upper lower))))))
```

**Output:**

```
> (fibo 100)
354224848179261915075
> (fibo -150)
-9969216677189303386214405760200
> (fibo-list 20)
(1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765)
> (fibo-range -10 15)
(-55 34 -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610)
> (fibo-range 0 20)
(0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765)
```


## Computer/zero Assembly

To find the ${\displaystyle n}$ th Fibonacci number, set the initial value of count equal to ${\displaystyle n}$ –2 and run the program. The machine will halt with the answer stored in the accumulator. Since Computer/zero's word length is only eight bits, the program will not work with values of ${\displaystyle n}$ greater than 13.

```mw
loop:   LDA  y      ; higher No.
        STA  temp
        ADD  x      ; lower No.
        STA  y
        LDA  temp
        STA  x

        LDA  count
        SUB  one
        BRZ  done

        STA  count
        JMP  loop

done:   LDA  y
        STP

one:         1
count:       8      ; n = 10
x:           1
y:           1
temp:        0
```


## Corescript

```mw
print Fibonacci Sequence:
var previous = 1
var number = 0
var temp = (blank)

:fib
if number > 50000000000:kill
print (number)
set temp = (add number previous)
set previous = (number)
set number = (temp)
goto fib

:kill
stop
```


## Cowgol

```mw
include "cowgol.coh";

sub fibonacci(n: uint32): (a: uint32) is
    a := 0;
    var b: uint32 := 1;
    while n > 0 loop
        var c := a + b;
        a := b;
        b := c;
        n := n - 1;
    end loop;
end sub;

# test
var i: uint32 := 0;
while i < 20 loop
    print_i32(fibonacci(i));
    print_char(' ');
    i := i + 1;
end loop;
print_nl();
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
```


## Crystal

### Recursive

```mw
def fib(n)
  n < 2 ? n : fib(n - 1) + fib(n - 2)
end
```

### Iterative

```mw
def fibIterative(n, prevFib = 0, fib = 1)
  return n if n < 2

  n.times do
    prevFib, fib = fib, prevFib + fib
  end

  prevFib
end
```

### Tail Recursive

```mw
def fibTailRecursive(n, prevFib = 0, fib = 1)
  n == 0 ? prevFib : fibTailRecursive(n - 1, fib, prevFib + fib)
end
```

### Analytic

```mw
def fibBinet(n)
  (((5 ** 0.5 + 1) / 2) ** n / 5 ** 0.5).round.to_i
end
```


## D

Here are four versions of Fibonacci Number calculating functions. *FibD* has an argument limit of magnitude 84 due to floating point precision, the others have a limit of 92 due to overflow (long).The traditional recursive version is inefficient. It is optimized by supplying a static storage to store intermediate results. A Fibonacci Number generating function is added. All functions have support for negative arguments.

```mw
import std.stdio, std.conv, std.algorithm, std.math;

long sgn(alias unsignedFib)(int n) { // break sign manipulation apart
    immutable uint m = (n >= 0) ? n : -n;
    if (n < 0 && (n % 2 == 0))
        return -unsignedFib(m);
    else
        return unsignedFib(m);
}

long fibD(uint m) { // Direct Calculation, correct for abs(m) <= 84
    enum sqrt5r =  1.0L / sqrt(5.0L);         //  1 / sqrt(5)
    enum golden = (1.0L + sqrt(5.0L)) / 2.0L; // (1 + sqrt(5)) / 2
    return roundTo!long(pow(golden, m) * sqrt5r);
}

long fibI(in uint m) pure nothrow { // Iterative
    long thisFib = 0;
    long nextFib = 1;
    foreach (i; 0 .. m) {
        long tmp = nextFib;
        nextFib += thisFib;
        thisFib  = tmp;
    }
    return thisFib;
}

long fibR(uint m) { // Recursive
    return (m < 2) ? m : fibR(m - 1) + fibR(m - 2);
}

long fibM(uint m) { // memoized Recursive
    static long[] fib = [0, 1];
    while (m >= fib.length )
        fib ~= fibM(m - 2) + fibM(m - 1);
    return fib[m];
}

alias sgn!fibD sfibD;
alias sgn!fibI sfibI;
alias sgn!fibR sfibR;
alias sgn!fibM sfibM;

auto fibG(in int m) { // generator(?)
    immutable int sign = (m < 0) ? -1 : 1;
    long yield;
    
    return new class {
        final int opApply(int delegate(ref int, ref long) dg) {
            int idx = -sign; // prepare for pre-increment
            foreach (f; this)
                if (dg(idx += sign, f))
                    break;
            return 0;
        }
        
        final int opApply(int delegate(ref long) dg) {
            long f0, f1 = 1;
            foreach (p; 0 .. m * sign + 1) {
                if (sign == -1 && (p % 2 == 0))
                    yield = -f0;
                else
                    yield = f0;
                if (dg(yield)) break;
                auto temp = f1;
                f1 = f0 + f1;
                f0 = temp;
            }
            return 0;
        }
    };
}

void main(in string[] args) {
    int k = args.length > 1 ? to!int(args[1]) : 10;
    writefln("Fib(%3d) = ", k);
    writefln("D : %20d <- %20d + %20d",
             sfibD(k), sfibD(k - 1), sfibD(k - 2));
    writefln("I : %20d <- %20d + %20d",
             sfibI(k), sfibI(k - 1), sfibI(k - 2));
    if (abs(k) < 36 || args.length > 2)
        // set a limit for recursive version
        writefln("R : %20d <- %20d + %20d",
                 sfibR(k), sfibM(k - 1), sfibM(k - 2));
    writefln("O : %20d <- %20d + %20d",
             sfibM(k), sfibM(k - 1), sfibM(k - 2));
    foreach (i, f; fibG(-9))
        writef("%d:%d | ", i, f);
}
```

**Output:**

for n = 85

```
Fib( 85) = 
D :   259695496911122586 <-   160500643816367088 +    99194853094755497
I :   259695496911122585 <-   160500643816367088 +    99194853094755497
O :   259695496911122585 <-   160500643816367088 +    99194853094755497
0:0 | -1:1 | -2:-1 | -3:2 | -4:-3 | -5:5 | -6:-8 | -7:13 | -8:-21 | -9:34 | 
```

### Matrix Exponentiation Version

```mw
import std.bigint;

T fibonacciMatrix(T=BigInt)(size_t n) {
    int[size_t.sizeof * 8] binDigits;
    size_t nBinDigits;
    while (n > 0) {
        binDigits[nBinDigits] = n % 2;
        n /= 2;
        nBinDigits++;
    }

    T x=1, y, z=1;
    foreach_reverse (b; binDigits[0 .. nBinDigits]) {
        if (b) {
            x = (x + z) * y;
            y = y ^^ 2 + z ^^ 2;
        } else {
            auto x_old = x;
            x = x ^^ 2 + y ^^ 2;
            y = (x_old + z) * y;
        }
        z = x + y;
    }

    return y;
}

void main() {
    10_000_000.fibonacciMatrix;
}
```

### Faster Version

For N = 10_000_000 this is about twice faster (run-time about 2.20 seconds) than the matrix exponentiation version.

```mw
import std.bigint, std.math;

// Algorithm from: Takahashi, Daisuke,
// "A fast algorithm for computing large Fibonacci numbers".
// Information Processing Letters 75.6 (30 November 2000): 243-246.
// Implementation from:
// pythonista.wordpress.com/2008/07/03/pure-python-fibonacci-numbers
BigInt fibonacci(in ulong n)
in {
    assert(n > 0, "fibonacci(n): n must be > 0.");
} body {
    if (n <= 2)
        return 1.BigInt;
    BigInt F = 1;
    BigInt L = 1;
    int sign = -1;
    immutable uint n2 = cast(uint)(cast(double)n).log2.floor;
    auto mask = 2.BigInt ^^ (n2 - 1);
    foreach (immutable i; 1 .. n2) {
        auto temp = F ^^ 2;
        F = (F + L) / 2;
        F = 2 * F ^^ 2 - 3 * temp - 2 * sign;
        L = 5 * temp + 2 * sign;
        sign = 1;
        if (n & mask) {
            temp = F;
            F = (F + L) / 2;
            L = F + 2 * temp;
            sign = -1;
        }
        mask /= 2;
    }
    if ((n & mask) == 0) {
        F *= L;
    } else {
        F = (F + L) / 2;
        F = F * L - sign;
    }
    return F;
}

void main() {
    10_000_000.fibonacci;
}
```


## Dart

### Basic

```mw
int fib(int n) {
  if (n==0 || n==1) {
    return n;
  }
  var prev=1;
  var current=1;
  for (var i=2; i<n; i++) {
    var next = prev + current;
    prev = current;
    current = next;    
  }
  return current;
}

int fibRec(int n) => n==0 || n==1 ? n : fibRec(n-1) + fibRec(n-2);

main() {
  print(fib(11));
  print(fibRec(11));
}
```

### Iterative Approach

```mw
Iterable<int> fibonacci(int n) sync* {
  int a = 1, b = 1;

  for (int i = 0; i < n; i++) {
    yield a;

    int temp = a;
    a = b;
    b = temp + b;
  }
}

void main() => print(fibonacci(20));
```

**Output:**

```
(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ..., 4181, 6765)
```

### Recursive Function

```mw
Iterable<int> fibonacci([int n = 1, int m = 1]) sync* {
  yield n;
  yield* fibonacci(m, n + m);
}

void main() => print(fibonacci().take(20));
```

**Output:**

```
(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ..., 4181, 6765)
```

### Generator Function

```mw
Iterable<int> fibonacci() sync* {
  int a = 1, b = 1;

  while (true) {
    yield a;

    int temp = a;
    a = b;
    b = temp + b;
  }
}

void main() => print(fibonacci().take(20));
```

**Output:**

```
(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ..., 4181, 6765)
```


## Datalog

Simple recurive implementation for Souffle.

```mw
.decl Fib(i:number, x:number)
Fib(0, 0). 
Fib(1, 1). 
Fib(i+2,x+y) :- Fib(i+1, x), Fib(i, y), i+2<=40, i+2>=2.
Fib(i-2,y-x) :- Fib(i-1, x), Fib(i, y), i-2>=-40, i-2<0.
```


## DBL

```mw
;
;       Fibonacci sequence for DBL version 4 by Dario B.
;
        RECORD

FIB1,  D10
FIB2,  D10
FIBN,  D10

J,     D5
A2,    A2
A5,    A5
                                PROC
;----------------------------------------------------------------
        XCALL FLAGS (0007000000,1)         ;Suppress STOP message

        OPEN (1,O,'TT:')
        DISPLAY (1,'First 10 Fibonacci Numbers:',10)
 
        FIB2=1

        FOR J=1 UNTIL 10
        DO BEGIN
                FIBN=FIB1+FIB2

                A2=J,'ZX'
                A5=FIBN,'ZZZZX'
                DISPLAY (1,A2,' : ',A5,10)

                FIB1=FIB2
                FIB2=FIBN
            END
 
        CLOSE 1
END
```


## Dc

This needs a modern Dc with `r` (swap) and `#` (comment). It easily can be adapted to an older Dc, but it will impact readability a lot.

```mw
[               # todo: n(<2) -- 1 and break 2 levels
  d -           # 0
  1 +           # 1
  q
] s1

[               # todo: n(>-1) -- F(n)
  d 0=1         # n(!=0)
  d 1=1         # n(!in {0,1})
  2 - d 1 +     # (n-2) (n-1)
  lF x          # (n-2) F(n-1)
  r             # F(n-1) (n-2)
  lF x          # F(n-1)+F(n-2)
  +
] sF

33 lF x f
```

**Output:**

```
5702887
```
