---
title: "Ackermann function (part 2/6)"
source: https://rosettacode.org/wiki/Ackermann_function
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/6
---

## BQN

```mw
A ← {
  A 0‿n: n+1;
  A m‿0: A (m-1)‿1;
  A m‿n: A (m-1)‿(A m‿(n-1))
}
```

Example usage:

```mw
    A 0‿3
4
    A 1‿4
6
    A 2‿4
11
    A 3‿4
125
```


## Bracmat

Three solutions are presented here. The first one is a purely recursive version, only using the formulas at the top of the page. The value of A(4,1) cannot be computed due to stack overflow. It can compute A(3,9) (4093), but probably not A(3,10)

```mw
( Ack
=   m n
  .   !arg:(?m,?n)
    & ( !m:0&!n+1
      | !n:0&Ack$(!m+-1,1)
      | Ack$(!m+-1,Ack$(!m,!n+-1))
      )
);
```

The second version is a purely non-recursive solution that easily can compute A(4,1). The program uses a stack for Ackermann function calls that are to be evaluated, but that cannot be computed given the currently known function values - the "known unknowns". The currently known values are stored in a hash table. The Hash table also contains incomplete Ackermann function calls, namely those for which the second argument is not known yet - "the unknown unknowns". These function calls are associated with "known unknowns" that are going to provide the value of the second argument. As soon as such an associated known unknown becomes known, the unknown unknown becomes a known unknown and is pushed onto the stack.

Although all known values are stored in the hash table, the converse is not true: an element in the hash table is either a "known known" or an "unknown unknown" associated with an "known unknown".

```mw
  ( A
  =     m n value key eq chain
      , find insert future stack va val
    .   ( chain
        =   key future skey
          .   !arg:(?key.?future)
            & str$!key:?skey
            & (cache..insert)$(!skey..!future)
            & 
        )
      & (find=.(cache..find)$(str$!arg))
      & ( insert
        =   key value future v futureeq futurem skey
          .   !arg:(?key.?value)
            & str$!key:?skey
            & (   (cache..find)$!skey:(?key.?v.?future)
                & (cache..remove)$!skey
                & (cache..insert)$(!skey.!value.)
                & (   !future:(?futurem.?futureeq)
                    & (!futurem,!value.!futureeq)
                  | 
                  )
              | (cache..insert)$(!skey.!value.)&
              )
        )
      & !arg:(?m,?n)
      & !n+1:?value
      & :?eq:?stack
      &   whl
        ' ( (!m,!n):?key
          &     (   find$!key:(?.#%?value.?future)
                  & insert$(!eq.!value) !future
                |   !m:0
                  & !n+1:?value
                  & ( !eq:&insert$(!key.!value)
                    |   insert$(!key.!value) !stack:?stack
                      & insert$(!eq.!value)
                    )
                |   !n:0
                  &   (!m+-1,1.!key)
                      (!eq:|(!key.!eq))
                |   find$(!m,!n+-1):(?.?val.?)
                  & (   !val:#%
                      & (   find$(!m+-1,!val):(?.?va.?)
                          & !va:#%
                          & insert$(!key.!va)
                        |   (!m+-1,!val.!eq)
                            (!m,!n.!eq)
                        )
                    | 
                    )
                |   chain$(!m,!n+-1.!m+-1.!key)
                  &   (!m,!n+-1.)
                      (!eq:|(!key.!eq))
                )
                !stack
            : (?m,?n.?eq) ?stack
          )
      & !value
  )
& new$hash:?cache
```

**Some results:**

```
A$(0,0):1
A$(3,13):65533
A$(3,14):131069
A$(4,1):65533
```

The last solution is a recursive solution that employs some extra formulas, inspired by the Common Lisp solution further down.

```mw
( AckFormula
=   m n
  .   !arg:(?m,?n)
    & ( !m:0&!n+1
      | !m:1&!n+2
      | !m:2&2*!n+3
      | !m:3&2^(!n+3)+-3
      | !n:0&AckFormula$(!m+-1,1)
      | AckFormula$(!m+-1,AckFormula$(!m,!n+-1))
      )
)
```

**Some results:**

```
AckFormula$(4,1):65533
AckFormula$(4,2):2003529930406846464979072351560255750447825475569751419265016973.....22087777506072339445587895905719156733
```

The last computation costs about 0,03 seconds.


## Brat

```mw
ackermann = { m, n |
	when { m == 0 } { n + 1 }
		{ m > 0 && n == 0 } { ackermann(m - 1, 1) }
		{ m > 0 && n > 0 } { ackermann(m - 1, ackermann(m, n - 1)) }
}

p ackermann 3, 4  #Prints 125
```


## Bruijn

```mw
:import std/Combinator .
:import std/Number/Unary U
:import std/Math .

# unary ackermann
ackermann-unary [0 [[U.inc 0 1 (+1u)]] U.inc]

:test (ackermann-unary (+0u) (+0u)) ((+1u))
:test (ackermann-unary (+3u) (+4u)) ((+125u))

# ternary ackermann (lower space complexity)
ackermann-ternary y [[[=?1 ++0 (=?0 (2 --1 (+1)) (2 --1 (2 1 --0)))]]]

:test ((ackermann-ternary (+0) (+0)) =? (+1)) ([[1]])
:test ((ackermann-ternary (+3) (+4)) =? (+125)) ([[1]])
```


## C

Straightforward implementation per Ackermann definition:

```mw
#include <stdio.h>

int ackermann(int m, int n)
{
        if (!m) return n + 1;
        if (!n) return ackermann(m - 1, 1);
        return ackermann(m - 1, ackermann(m, n - 1));
}

int main()
{
        int m, n;
        for (m = 0; m <= 4; m++)
                for (n = 0; n < 6 - m; n++)
                        printf("A(%d, %d) = %d\n", m, n, ackermann(m, n));

        return 0;
}
```

**Output:**

```
A(0, 0) = 1
A(0, 1) = 2
A(0, 2) = 3
A(0, 3) = 4
A(0, 4) = 5
A(0, 5) = 6
A(1, 0) = 2
A(1, 1) = 3
A(1, 2) = 4
A(1, 3) = 5
A(1, 4) = 6
A(2, 0) = 3
A(2, 1) = 5
A(2, 2) = 7
A(2, 3) = 9
A(3, 0) = 5
A(3, 1) = 13
A(3, 2) = 29
A(4, 0) = 13
A(4, 1) = 65533
```

Ackermann function makes *a lot* of recursive calls, so the above program is a bit naive. We need to be slightly less naive, by doing some simple caching:

```mw
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int m_bits, n_bits;
int *cache;

int ackermann(int m, int n)
{
        int idx, res;
        if (!m) return n + 1;

        if (n >= 1<<n_bits) {
                printf("%d, %d\n", m, n);
                idx = 0;
        } else {
                idx = (m << n_bits) + n;
                if (cache[idx]) return cache[idx];
        }

        if (!n) res = ackermann(m - 1, 1);
        else    res = ackermann(m - 1, ackermann(m, n - 1));

        if (idx) cache[idx] = res;
        return res;
}
int main()
{
        int m, n;

        m_bits = 3;
        n_bits = 20;  /* can save n values up to 2**20 - 1, that's 1 meg */
        cache = malloc(sizeof(int) * (1 << (m_bits + n_bits)));
        memset(cache, 0, sizeof(int) * (1 << (m_bits + n_bits)));

        for (m = 0; m <= 4; m++)
                for (n = 0; n < 6 - m; n++)
                        printf("A(%d, %d) = %d\n", m, n, ackermann(m, n));

        return 0;
}
```

**Output:**

```
A(0, 0) = 1
A(0, 1) = 2
A(0, 2) = 3
A(0, 3) = 4
A(0, 4) = 5
A(0, 5) = 6
A(1, 0) = 2
A(1, 1) = 3
A(1, 2) = 4
A(1, 3) = 5
A(1, 4) = 6
A(2, 0) = 3
A(2, 1) = 5
A(2, 2) = 7
A(2, 3) = 9
A(3, 0) = 5
A(3, 1) = 13
A(3, 2) = 29
A(4, 0) = 13
A(4, 1) = 65533
```

Whee. Well, with some extra work, we calculated *one more* n value, big deal, right? But see, `A(4, 2) = A(3, A(4, 1)) = A(3, 65533) = A(2, A(3, 65532)) = ...` you can see how fast it blows up. In fact, no amount of caching will help you calculate large m values; on the machine I use A(4, 2) segfaults because the recursions run out of stack space--not a whole lot I can do about it. At least it runs out of stack space *quickly*, unlike the first solution...

A couple of alternative approaches...

```mw
/* Thejaka Maldeniya */

#include <conio.h>

unsigned long long HR(unsigned int n, unsigned long long a, unsigned long long b) {
	// (Internal) Recursive Hyperfunction: Perform a Hyperoperation...

	unsigned long long r = 1;

	while(b--)
		r = n - 3 ? HR(n - 1, a, r) : /* Exponentiation */ r * a;

	return r;
}

unsigned long long H(unsigned int n, unsigned long long a, unsigned long long b) {
	// Hyperfunction (Recursive-Iterative-O(1) Hybrid): Perform a Hyperoperation...

	switch(n) {
		case 0:
			// Increment
			return ++b;
		case 1:
			// Addition
			return a + b;
		case 2:
			// Multiplication
			return a * b;
	}

	return HR(n, a, b);
}

unsigned long long APH(unsigned int m, unsigned int n) {
	// Ackermann-Péter Function (Recursive-Iterative-O(1) Hybrid)
	return H(m, 2, n + 3) - 3;
}

unsigned long long * p = 0;

unsigned long long APRR(unsigned int m, unsigned int n) {
	if (!m) return ++n;

	unsigned long long r = p ? p[m] : APRR(m - 1, 1);

	--m;
	while(n--)
		r = APRR(m, r);

	return r;
}

unsigned long long APRA(unsigned int m, unsigned int n) {
	return
		m ?
			n ?
				APRR(m, n)
				: p ? p[m] : APRA(--m, 1)
			: ++n
		;
}

unsigned long long APR(unsigned int m, unsigned int n) {
	unsigned long long r = 0;

	// Allocate
	p = (unsigned long long *) malloc(sizeof(unsigned long long) * (m + 1));

	// Initialize
	for(; r <= m; ++r)
		p[r] = r ? APRA(r - 1, 1) : APRA(r, 0);

	// Calculate
	r = APRA(m, n);

	// Free
	free(p);

	return r;
}

unsigned long long AP(unsigned int m, unsigned int n) {
	return APH(m, n);
	return APR(m, n);
}

int main(int n, char ** a) {
	unsigned int M, N;

	if (n != 3) {
		printf("Usage: %s <m> <n>\n", *a);
		return 1;
	}

	printf("AckermannPeter(%u, %u) = %llu\n", M = atoi(a[1]), N = atoi(a[2]), AP(M, N));

	//printf("\nPress any key...");
	//getch();
	return 0;
}
```

A couple of more iterative techniques...

```mw
/* Thejaka Maldeniya */

#include <conio.h>

unsigned long long HI(unsigned int n, unsigned long long a, unsigned long long b) {
	// Hyperfunction (Iterative): Perform a Hyperoperation...

	unsigned long long *I, r = 1;
	unsigned int N = n - 3;

	if (!N)
		// Exponentiation
		while(b--)
			r *= a;
	else if(b) {
		n -= 2;

		// Allocate
		I = (unsigned long long *) malloc(sizeof(unsigned long long) * n--);

		// Initialize
		I[n] = b;

		// Calculate
		for(;;) {
			if(I[n]) {
				--I[n];
				if (n)
					I[--n] = r, r = 1;
				else
					r *= a;
			} else
				for(;;)
					if (n == N)
						goto a;
					else if(I[++n])
						break;
		}
a:

		// Free
		free(I);
	}

	return r;
}

unsigned long long H(unsigned int n, unsigned long long a, unsigned long long b) {
	// Hyperfunction (Iterative-O(1) Hybrid): Perform a Hyperoperation...

	switch(n) {
		case 0:
			// Increment
			return ++b;
		case 1:
			// Addition
			return a + b;
		case 2:
			// Multiplication
			return a * b;
	}

	return HI(n, a, b);
}

unsigned long long APH(unsigned int m, unsigned int n) {
	// Ackermann-Péter Function (Recursive-Iterative-O(1) Hybrid)
	return H(m, 2, n + 3) - 3;
}

unsigned long long * p = 0;

unsigned long long APIA(unsigned int m, unsigned int n) {
	if (!m) return ++n;

	// Initialize
	unsigned long long *I, r = p ? p[m] : APIA(m - 1, 1);
	unsigned int M = m;

	if (n) {
		// Allocate
		I = (unsigned long long *) malloc(sizeof(unsigned long long) * (m + 1));

		// Initialize
		I[m] = n;

		// Calculate
		for(;;) {
			if(I[m]) {
				if (m)
					--I[m], I[--m] = r, r = p ? p[m] : APIA(m - 1, 1);
				else
					r += I[m], I[m] = 0;
			} else
				for(;;)
					if (m == M)
						goto a;
					else if(I[++m])
						break;
		}
a:

		// Free
		free(I);
	}

	return r;
}

unsigned long long API(unsigned int m, unsigned int n) {
	unsigned long long r = 0;

	// Allocate
	p = (unsigned long long *) malloc(sizeof(unsigned long long) * (m + 1));

	// Initialize
	for(; r <= m; ++r)
		p[r] = r ? APIA(r - 1, 1) : APIA(r, 0);

	// Calculate
	r = APIA(m, n);

	// Free
	free(p);

	return r;
}

unsigned long long AP(unsigned int m, unsigned int n) {
	return APH(m, n);
	return API(m, n);
}

int main(int n, char ** a) {
	unsigned int M, N;

	if (n != 3) {
		printf("Usage: %s <m> <n>\n", *a);
		return 1;
	}

	printf("AckermannPeter(%u, %u) = %llu\n", M = atoi(a[1]), N = atoi(a[2]), AP(M, N));

	//printf("\nPress any key...");
	//getch();
	return 0;
}
```

A few further tweaks/optimizations may be possible.


## C

### Basic Version

```mw
using System;
class Program
{
    public static long Ackermann(long m, long n)
    {
        if(m > 0)
        {
            if (n > 0)
                return Ackermann(m - 1, Ackermann(m, n - 1));
            else if (n == 0)
                return Ackermann(m - 1, 1);
        }
        else if(m == 0)
        {
            if(n >= 0) 
                return n + 1;
        }

        throw new System.ArgumentOutOfRangeException();
    }
    
    static void Main()
    {
        for (long m = 0; m <= 3; ++m)
        {
            for (long n = 0; n <= 4; ++n)
            {
                Console.WriteLine("Ackermann({0}, {1}) = {2}", m, n, Ackermann(m, n));
            }
        }
    }
}
```

**Output:**

```
Ackermann(0, 0) = 1
Ackermann(0, 1) = 2
Ackermann(0, 2) = 3
Ackermann(0, 3) = 4
Ackermann(0, 4) = 5
Ackermann(1, 0) = 2
Ackermann(1, 1) = 3
Ackermann(1, 2) = 4
Ackermann(1, 3) = 5
Ackermann(1, 4) = 6
Ackermann(2, 0) = 3
Ackermann(2, 1) = 5
Ackermann(2, 2) = 7
Ackermann(2, 3) = 9
Ackermann(2, 4) = 11
Ackermann(3, 0) = 5
Ackermann(3, 1) = 13
Ackermann(3, 2) = 29
Ackermann(3, 3) = 61
Ackermann(3, 4) = 125
```

### Efficient Version

```mw
using System;
using System.Numerics;
using System.IO;
using System.Diagnostics;

namespace Ackermann_Function
{
    class Program
    {
        static void Main(string[] args)
        {
            int _m = 0;
            int _n = 0;
            Console.Write("m = ");
            try
            {
                _m = Convert.ToInt32(Console.ReadLine());
            }
            catch (Exception)
            {
                Console.WriteLine("Please enter a number.");
            }
            Console.Write("n = ");
            try
            {
                _n = Convert.ToInt32(Console.ReadLine());
            }
            catch (Exception)
            {
                Console.WriteLine("Please enter a number.");
            }
            //for (long m = 0; m <= 10; ++m)
            //{
            //    for (long n = 0; n <= 10; ++n)
            //    {
            //        DateTime now = DateTime.Now;
            //        Console.WriteLine("Ackermann({0}, {1}) = {2}", m, n, Ackermann(m, n));
            //        Console.WriteLine("Time taken:{0}", DateTime.Now - now);
            //    }
            //}

            DateTime now = DateTime.Now;
            Console.WriteLine("Ackermann({0}, {1}) = {2}", _m, _n, Ackermann(_m, _n));
            Console.WriteLine("Time taken:{0}", DateTime.Now - now);
            File.WriteAllText("number.txt", Ackermann(_m, _n).ToString());
            Process.Start("number.txt");
            Console.ReadKey();
        }
        public class OverflowlessStack<T>
        {
            internal sealed class SinglyLinkedNode
            {
                private const int ArraySize = 2048;
                T[] _array;
                int _size;
                public SinglyLinkedNode Next;
                public SinglyLinkedNode()
                {
                    _array = new T[ArraySize];
                }
                public bool IsEmpty { get { return _size == 0; } }
                public SinglyLinkedNode Push(T item)
                {
                    if (_size == ArraySize - 1)
                    {
                        SinglyLinkedNode n = new SinglyLinkedNode();
                        n.Next = this;
                        n.Push(item);
                        return n;
                    }
                    _array[_size++] = item;
                    return this;
                }
                public T Pop()
                {
                    return _array[--_size];
                }
            }
            private SinglyLinkedNode _head = new SinglyLinkedNode();

            public T Pop()
            {
                T ret = _head.Pop();
                if (_head.IsEmpty && _head.Next != null)
                    _head = _head.Next;
                return ret;
            }
            public void Push(T item)
            {
                _head = _head.Push(item);
            }
            public bool IsEmpty
            {
                get { return _head.Next == null && _head.IsEmpty; }
            }
        }
        public static BigInteger Ackermann(BigInteger m, BigInteger n)
        {
            var stack = new OverflowlessStack<BigInteger>();
            stack.Push(m);
            while (!stack.IsEmpty)
            {
                m = stack.Pop();
            skipStack:
                if (m == 0)
                    n = n + 1;
                else if (m == 1)
                    n = n + 2;
                else if (m == 2)
                    n = n * 2 + 3;
                else if (n == 0)
                {
                    --m;
                    n = 1;
                    goto skipStack;
                }
                else
                {
                    stack.Push(m - 1);
                    --n;
                    goto skipStack;
                }
            }
            return n;
        }
    }
}
```

Possibly the most efficient implementation of Ackermann in C#. It successfully runs Ack(4,2) when executed in Visual Studio. Don't forget to add a reference to System.Numerics.


## C++

### Basic version

```mw
#include <iostream>

unsigned int ackermann(unsigned int m, unsigned int n) {
  if (m == 0) {
    return n + 1;
  }
  if (n == 0) {
    return ackermann(m - 1, 1);
  }
  return ackermann(m - 1, ackermann(m, n - 1));
}

int main() {
  for (unsigned int m = 0; m < 4; ++m) {
    for (unsigned int n = 0; n < 10; ++n) {
      std::cout << "A(" << m << ", " << n << ") = " << ackermann(m, n) << "\n";
    }
  }
}
```

### Efficient version

Translation of

:

D

C++11 with boost's big integer type. Compile with:

```
g++ -std=c++11 -I /path/to/boost ackermann.cpp.
```

```mw
#include <iostream>
#include <sstream>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>

using big_int = boost::multiprecision::cpp_int;

big_int ipow(big_int base, big_int exp) {
  big_int result(1);
  while (exp) {
    if (exp & 1) {
      result *= base;
    }
    exp >>= 1;
    base *= base;
  }
  return result;
}

big_int ackermann(unsigned m, unsigned n) {
  static big_int (*ack)(unsigned, big_int) =
      [](unsigned m, big_int n)->big_int {
    switch (m) {
    case 0:
      return n + 1;
    case 1:
      return n + 2;
    case 2:
      return 3 + 2 * n;
    case 3:
      return 5 + 8 * (ipow(big_int(2), n) - 1);
    default:
      return n == 0 ? ack(m - 1, big_int(1)) : ack(m - 1, ack(m, n - 1));
    }
  };
  return ack(m, big_int(n));
}

int main() {
  for (unsigned m = 0; m < 4; ++m) {
    for (unsigned n = 0; n < 10; ++n) {
      std::cout << "A(" << m << ", " << n << ") = " << ackermann(m, n) << "\n";
    }
  }

  std::cout << "A(4, 1) = " << ackermann(4, 1) << "\n";

  std::stringstream ss;
  ss << ackermann(4, 2);
  auto text = ss.str();
  std::cout << "A(4, 2) = (" << text.length() << " digits)\n"
            << text.substr(0, 80) << "\n...\n"
            << text.substr(text.length() - 80) << "\n";
}
```

```
<pre>
A(0, 0) = 1
A(0, 1) = 2
A(0, 2) = 3
A(0, 3) = 4
A(0, 4) = 5
A(0, 5) = 6
A(0, 6) = 7
A(0, 7) = 8
A(0, 8) = 9
A(0, 9) = 10
A(1, 0) = 2
A(1, 1) = 3
A(1, 2) = 4
A(1, 3) = 5
A(1, 4) = 6
A(1, 5) = 7
A(1, 6) = 8
A(1, 7) = 9
A(1, 8) = 10
A(1, 9) = 11
A(2, 0) = 3
A(2, 1) = 5
A(2, 2) = 7
A(2, 3) = 9
A(2, 4) = 11
A(2, 5) = 13
A(2, 6) = 15
A(2, 7) = 17
A(2, 8) = 19
A(2, 9) = 21
A(3, 0) = 5
A(3, 1) = 13
A(3, 2) = 29
A(3, 3) = 61
A(3, 4) = 125
A(3, 5) = 253
A(3, 6) = 509
A(3, 7) = 1021
A(3, 8) = 2045
A(3, 9) = 4093
A(4, 1) = 65533
A(4, 2) = (19729 digits)
2003529930406846464979072351560255750447825475569751419265016973710894059556311
...
4717124577965048175856395072895337539755822087777506072339445587895905719156733
```


## Chapel

```mw
proc A(m:int, n:int):int {
        if m == 0 then
                return n + 1;
        else if n == 0 then
                return A(m - 1, 1);
        else
                return A(m - 1, A(m, n - 1));
}
```


## Clay

```mw
ackermann(m, n) {
    if(m == 0)
      return n + 1;
    if(n == 0)
      return ackermann(m - 1, 1);

    return ackermann(m - 1, ackermann(m, n - 1));
}
```


## CLIPS

**Functional solution**

```mw
(deffunction ackerman
  (?m ?n)
  (if (= 0 ?m)
    then (+ ?n 1)
    else (if (= 0 ?n)
      then (ackerman (- ?m 1) 1)
      else (ackerman (- ?m 1) (ackerman ?m (- ?n 1)))
    )
  )
)
```

**Example usage:**

```
CLIPS> (ackerman 0 4)
5
CLIPS> (ackerman 1 4)
6
CLIPS> (ackerman 2 4)
11
CLIPS> (ackerman 3 4)
125
```

**Fact-based solution**

```mw
(deffacts solve-items
  (solve 0 4)
  (solve 1 4)
  (solve 2 4)
  (solve 3 4)
)

(defrule acker-m-0
  ?compute <- (compute 0 ?n)
  =>
  (retract ?compute)
  (assert (ackerman 0 ?n (+ ?n 1)))
)

(defrule acker-n-0-pre
  (compute ?m&:(> ?m 0) 0)
  (not (ackerman =(- ?m 1) 1 ?))
  =>
  (assert (compute (- ?m 1) 1))
)

(defrule acker-n-0
  ?compute <- (compute ?m&:(> ?m 0) 0)
  (ackerman =(- ?m 1) 1 ?val)
  =>
  (retract ?compute)
  (assert (ackerman ?m 0 ?val))
)

(defrule acker-m-n-pre-1
  (compute ?m&:(> ?m 0) ?n&:(> ?n 0))
  (not (ackerman ?m =(- ?n 1) ?))
  =>
  (assert (compute ?m (- ?n 1)))
)

(defrule acker-m-n-pre-2
  (compute ?m&:(> ?m 0) ?n&:(> ?n 0))
  (ackerman ?m =(- ?n 1) ?newn)
  (not (ackerman =(- ?m 1) ?newn ?))
  =>
  (assert (compute (- ?m 1) ?newn))
)

(defrule acker-m-n
  ?compute <- (compute ?m&:(> ?m 0) ?n&:(> ?n 0))
  (ackerman ?m =(- ?n 1) ?newn)
  (ackerman =(- ?m 1) ?newn ?val)
  =>
  (retract ?compute)
  (assert (ackerman ?m ?n ?val))
)

(defrule acker-solve
  (solve ?m ?n)
  (not (compute ?m ?n))
  (not (ackerman ?m ?n ?))
  =>
  (assert (compute ?m ?n))
)

(defrule acker-solved
  ?solve <- (solve ?m ?n)
  (ackerman ?m ?n ?result)
  =>
  (retract ?solve)
  (printout t "A(" ?m "," ?n ") = " ?result crlf)
)
```

When invoked, each required A(m,n) needed to solve the requested (solve ?m ?n) facts gets generated as its own fact. Below shows the invocation of the above, as well as an excerpt of the final facts list. Regardless of how many input (solve ?m ?n) requests are made, each possible A(m,n) is only solved once.

```
CLIPS> (reset)
CLIPS> (facts)
f-0     (initial-fact)
f-1     (solve 0 4)
f-2     (solve 1 4)
f-3     (solve 2 4)
f-4     (solve 3 4)
For a total of 5 facts.
CLIPS> (run)
A(3,4) = 125
A(2,4) = 11
A(1,4) = 6
A(0,4) = 5
CLIPS> (facts)
f-0     (initial-fact)
f-15    (ackerman 0 1 2)
f-16    (ackerman 1 0 2)
f-18    (ackerman 0 2 3)
...
f-632   (ackerman 1 123 125)
f-633   (ackerman 2 61 125)
f-634   (ackerman 3 4 125)
For a total of 316 facts.
CLIPS>
```


## Clojure

```mw
(defn ackermann [m n] 
  (cond (zero? m) (inc n)
        (zero? n) (ackermann (dec m) 1)
        :else (ackermann (dec m) (ackermann m (dec n)))))
```


## CLU

```mw
% Ackermann function
ack = proc (m, n: int) returns (int)
    if     m=0 then return(n+1)
    elseif n=0 then return(ack(m-1, 1))
    else            return(ack(m-1, ack(m, n-1)))
    end
end ack

% Print a table of ack( 0..3, 0..8 )
start_up = proc ()
    po: stream := stream$primary_output()
    
    for m: int in int$from_to(0, 3) do
        for n: int in int$from_to(0, 8) do
            stream$putright(po, int$unparse(ack(m,n)), 8)
        end
        stream$putl(po, "")
    end
end start_up
```

**Output:**

```
       1       2       3       4       5       6       7       8       9
       2       3       4       5       6       7       8       9      10
       3       5       7       9      11      13      15      17      19
       5      13      29      61     125     253     509    1021    2045
```


## COBOL

```mw
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Ackermann.

       DATA DIVISION.
       LINKAGE SECTION.
       01  M          USAGE UNSIGNED-LONG.
       01  N          USAGE UNSIGNED-LONG.

       01  Return-Val USAGE UNSIGNED-LONG.

       PROCEDURE DIVISION USING M N Return-Val.
           EVALUATE M ALSO N
               WHEN 0 ALSO ANY
                   ADD 1 TO N GIVING Return-Val

               WHEN NOT 0 ALSO 0
                   SUBTRACT 1 FROM M
                   CALL "Ackermann" USING BY CONTENT M BY CONTENT 1
                       BY REFERENCE Return-Val

               WHEN NOT 0 ALSO NOT 0
                   SUBTRACT 1 FROM N
                   CALL "Ackermann" USING BY CONTENT M BY CONTENT N
                       BY REFERENCE Return-Val
                       
                   SUBTRACT 1 FROM M
                   CALL "Ackermann" USING BY CONTENT M
                       BY CONTENT Return-Val BY REFERENCE Return-Val
           END-EVALUATE

           GOBACK
           .
```


## CoffeeScript

```mw
ackermann = (m, n) ->
  if m is 0 then n + 1
  else if m > 0 and n is 0 then ackermann m - 1, 1
  else ackermann m - 1, ackermann m, n - 1
```


## Comal

```mw
0010 //
0020 // Ackermann function
0030 //
0040 FUNC a#(m#,n#)
0050   IF m#=0 THEN RETURN n#+1
0060   IF n#=0 THEN RETURN a#(m#-1,1)
0070   RETURN a#(m#-1,a#(m#,n#-1))
0080 ENDFUNC a#
0090 //
0100 // Print table of Ackermann values
0110 //
0120 ZONE 5
0130 FOR m#:=0 TO 3 DO
0140   FOR n#:=0 TO 4 DO PRINT a#(m#,n#),
0150   PRINT
0160 ENDFOR m#
0170 END
```

**Output:**

```
1    2    3    4    5
2    3    4    5    6
3    5    7    9    11
5    13   29   61   125
```


## Common Lisp

```mw
(defun ackermann (m n)
  (cond ((zerop m) (1+ n))
        ((zerop n) (ackermann (1- m) 1))
        (t         (ackermann (1- m) (ackermann m (1- n))))))
```

More elaborately:

```mw
(defun ackermann (m n)
  (case m ((0) (1+ n))
    ((1) (+ 2 n))
    ((2) (+ n n 3))
    ((3) (- (expt 2 (+ 3 n)) 3))
    (otherwise (ackermann (1- m) (if (zerop n) 1 (ackermann m (1- n)))))))

(loop for m from 0 to 4 do
      (loop for n from (- 5 m) to (- 6 m) do
	    (format t "A(~d, ~d) = ~d~%" m n (ackermann m n))))
```

**Output:**

```
A(0, 5) = 6
A(0, 6) = 7
A(1, 4) = 6
A(1, 5) = 7
A(2, 3) = 9
A(2, 4) = 11
A(3, 2) = 29
A(3, 3) = 61
A(4, 1) = 65533

A(4, 2) = 2003529930 <... skipping a few digits ...> 56733
```


## Component Pascal

BlackBox Component Builder

```mw
MODULE NpctAckerman;
 
IMPORT  StdLog;
 
VAR     
	m,n: INTEGER;
 
PROCEDURE Ackerman (x,y: INTEGER):INTEGER;
 
BEGIN
  IF    x = 0  THEN  RETURN  y + 1
  ELSIF y = 0  THEN  RETURN  Ackerman (x - 1 , 1)
  ELSE
    RETURN  Ackerman (x - 1 , Ackerman (x , y - 1))
  END
END Ackerman;
 
PROCEDURE Do*;
BEGIN
  FOR  m := 0  TO  3  DO
    FOR  n := 0  TO  6  DO
      StdLog.Int (Ackerman (m, n));StdLog.Char (' ')
    END;
    StdLog.Ln
  END;
  StdLog.Ln
END Do;

END NpctAckerman.
```

Execute: ^Q NpctAckerman.Do

```
<pre>
 1  2  3  4  5  6  7 
 2  3  4  5  6  7  8 
 3  5  7  9  11  13  15 
 5  13  29  61  125  253  509 
```


## Crystal

Translation of

:

Ruby

```mw
def ack(m, n)
  if m == 0
    n + 1
  elsif n == 0
    ack(m-1, 1)
  else
    ack(m-1, ack(m, n-1))
  end
end

#Example:
(0..3).each do |m|
  puts (0..6).map { |n| ack(m, n) }.join(' ')
end
```

**Output:**

```
1 2 3 4 5 6 7
2 3 4 5 6 7 8
3 5 7 9 11 13 15
5 13 29 61 125 253 509
```


## D

### Basic version

```mw
ulong ackermann(in ulong m, in ulong n) pure nothrow @nogc {
    if (m == 0)
        return n + 1;
    if (n == 0)
        return ackermann(m - 1, 1);
    return ackermann(m - 1, ackermann(m, n - 1));
}

void main() {
    assert(ackermann(2, 4) == 11);
}
```

### More Efficient Version

Translation of

:

Mathematica

```mw
import std.stdio, std.bigint, std.conv;

BigInt ipow(BigInt base, BigInt exp) pure nothrow {
    auto result = 1.BigInt;
    while (exp) {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

BigInt ackermann(in uint m, in uint n) pure nothrow
out(result) {
    assert(result >= 0);
} body {
    static BigInt ack(in uint m, in BigInt n) pure nothrow {
        switch (m) {
            case 0: return n + 1;
            case 1: return n + 2;
            case 2: return 3 + 2 * n;
            //case 3: return 5 + 8 * (2 ^^ n - 1);
            case 3: return 5 + 8 * (ipow(2.BigInt, n) - 1);
            default: return (n == 0) ?
                        ack(m - 1, 1.BigInt) :
                        ack(m - 1, ack(m, n - 1));
        }
    }

    return ack(m, n.BigInt);
}

void main() {
    foreach (immutable m; 1 .. 4)
        foreach (immutable n; 1 .. 9)
            writefln("ackermann(%d, %d): %s", m, n, ackermann(m, n));
    writefln("ackermann(4, 1): %s", ackermann(4, 1));

    immutable a = ackermann(4, 2).text;
    writefln("ackermann(4, 2)) (%d digits):\n%s...\n%s",
             a.length, a[0 .. 94], a[$ - 96 .. $]);
}
```

**Output:**

```
ackermann(1, 1): 3
ackermann(1, 2): 4
ackermann(1, 3): 5
ackermann(1, 4): 6
ackermann(1, 5): 7
ackermann(1, 6): 8
ackermann(1, 7): 9
ackermann(1, 8): 10
ackermann(2, 1): 5
ackermann(2, 2): 7
ackermann(2, 3): 9
ackermann(2, 4): 11
ackermann(2, 5): 13
ackermann(2, 6): 15
ackermann(2, 7): 17
ackermann(2, 8): 19
ackermann(3, 1): 13
ackermann(3, 2): 29
ackermann(3, 3): 61
ackermann(3, 4): 125
ackermann(3, 5): 253
ackermann(3, 6): 509
ackermann(3, 7): 1021
ackermann(3, 8): 2045
ackermann(4, 1): 65533
ackermann(4, 2)) (19729 digits):
2003529930406846464979072351560255750447825475569751419265016973710894059556311453089506130880...
699146577530041384717124577965048175856395072895337539755822087777506072339445587895905719156733
```


## Dart

no caching, the implementation takes ages even for A(4,1)

```mw
int A(int m, int n) => m==0 ? n+1 : n==0 ? A(m-1,1) : A(m-1,A(m,n-1));

main() {
  print(A(0,0));
  print(A(1,0));
  print(A(0,1));
  print(A(2,2));
  print(A(2,3));
  print(A(3,3));
  print(A(3,4));
  print(A(3,5));
  print(A(4,0));
}
```


## Dc

This needs a modern Dc with `r` (swap) and `#` (comment). It easily can be adapted to an older Dc, but it will impact readability a lot.

```mw
[               # todo: n 0 -- n+1 and break 2 levels
  + 1 +         # n+1
  q
] s1

[               # todo: m 0 -- A(m-1,1) and break 2 levels
  + 1 -         # m-1
  1             # m-1 1
  lA x          # A(m-1,1)
  q
] s2

[               # todo: m n -- A(m,n)
  r d 0=1       # n m(!=0)
  r d 0=2       # m(!=0) n(!=0)
  Sn            # m(!=0)
  d 1 - r       # m-1 m
  Ln 1 -        # m-1 m n-1
  lA x          # m-1 A(m,n-1)
  lA x          # A(m-1,A(m,n-1))
] sA

3 9 lA x f
```

**Output:**

```
4093
```


## Delphi

```mw
function Ackermann(m,n:Int64):Int64;
begin
    if m = 0 then
        Result := n + 1
    else if n = 0 then
        Result := Ackermann(m-1, 1)
    else
        Result := Ackermann(m-1, Ackermann(m, n - 1));
end;
```


## Draco

```mw
/* Ackermann function */
proc ack(word m, n) word:
    if   m=0 then n+1
    elif n=0 then ack(m-1, 1)
    else          ack(m-1, ack(m, n-1))
    fi
corp;

/* Write a table of Ackermann values */
proc nonrec main() void:
    byte m, n;
    for m from 0 upto 3 do
        for n from 0 upto 8 do
            write(ack(m,n) : 5)
        od;
        writeln()
    od
corp
```

**Output:**

```
    1    2    3    4    5    6    7    8    9
    2    3    4    5    6    7    8    9   10
    3    5    7    9   11   13   15   17   19
    5   13   29   61  125  253  509 1021 2045
```


## DWScript

```mw
function Ackermann(m, n : Integer) : Integer;
begin
    if m = 0 then
        Result := n+1
    else if n = 0 then
        Result := Ackermann(m-1, 1)
    else Result := Ackermann(m-1, Ackermann(m, n-1));
end;
```


## Dylan

```mw
define method ack(m == 0, n :: <integer>)
   n + 1
end;
define method ack(m :: <integer>, n :: <integer>)
   ack(m - 1, if (n == 0) 1 else ack(m, n - 1) end)
end;
```


## E

```mw
def A(m, n) {
    return if (m <=> 0)          { n+1              } \
      else if (m > 0 && n <=> 0) { A(m-1, 1)        } \
      else                       { A(m-1, A(m,n-1)) }
}
```


## EasyLang

```mw
func ackerm m n .
   if m = 0 : return n + 1
   if n = 0 : return ackerm (m - 1) 1
   return ackerm (m - 1) ackerm m (n - 1)
.
print ackerm 3 6
```

**Output:**

```
509
```


## Egel

```mw
def ackermann =
    [ 0 N -> N + 1
    | M 0 -> ackermann (M - 1) 1
    | M N -> ackermann (M - 1) (ackermann M (N - 1)) ]
```


## Eiffel

Example code

Test of Example code

```mw
class
	ACKERMAN_EXAMPLE

feature -- Basic Operations

	ackerman (m, n: NATURAL): NATURAL
			-- Recursively compute the n-th term of a series.
		require
			non_negative_m: m >= 0
			non_negative_n: n >= 0
		do
			if m = 0 then
				Result := n + 1
			elseif m > 0 and n = 0 then
				Result := ackerman (m - 1, 1)
			elseif m > 0 and n > 0 then
				Result := ackerman (m - 1, ackerman (m, n - 1))
			else
				check invalid_arg_state: False end
			end
		end

end
```


## Ela

```mw
ack 0 n = n+1
ack m 0 = ack (m - 1) 1
ack m n = ack (m - 1) <| ack m <| n - 1
```


## Elena

ELENA 6.x :

```mw
import extensions;

// --- Ackermann function ---

Ackermann(m,n)
{
   if(n < 0 || m < 0)
   {
      InvalidArgumentException.raise()
   };
    
   m =>
      0 : { ^n + 1 }
      ! : {
         n => 
            0 : { ^Ackermann(m - 1,1) }
            ! : { ^Ackermann(m - 1,Ackermann(m,n-1)) }
         }
}

public Program()
{
   for(int i:=0; i <= 3; i += 1)
   {
      for(int j := 0; j <= 5; j += 1)
      {
         Console.printLine("A(",i,",",j,")=",Ackermann(i,j))
      }
   };

   Console.readChar()
}
```

**Output:**

```
A(0,0)=1
A(0,1)=2
A(0,2)=3
A(0,3)=4
A(0,4)=5
A(0,5)=6
A(1,0)=2
A(1,1)=3
A(1,2)=4
A(1,3)=5
A(1,4)=6
A(1,5)=7
A(2,0)=3
A(2,1)=5
A(2,2)=7
A(2,3)=9
A(2,4)=11
A(2,5)=13
A(3,0)=5
A(3,1)=13
A(3,2)=29
A(3,3)=61
A(3,4)=125
A(3,5)=253
```


## Elixir

```mw
defmodule Ackermann do
  def ack(0, n), do: n + 1 
  def ack(m, 0), do: ack(m - 1, 1)
  def ack(m, n), do: ack(m - 1, ack(m, n - 1))
end

Enum.each(0..3, fn m ->
  IO.puts Enum.map_join(0..6, " ", fn n -> Ackermann.ack(m, n) end)
end)
```

**Output:**

```
1 2 3 4 5 6 7
2 3 4 5 6 7 8
3 5 7 9 11 13 15
5 13 29 61 125 253 509
```


## Emacs Lisp

```mw
(defun ackermann (m n)
  (cond ((zerop m) (1+ n))
	((zerop n) (ackermann (1- m) 1))
	(t         (ackermann (1- m)
			      (ackermann m (1- n))))))
```


## EMal

```mw
fun ackermann ← <int m, int n|when(m æ 0,
  n + 1,
  when(n æ 0,
  ackermann(m - 1, 1),
  ackermann(m - 1, ackermann(m, n - 1))))
for int m ← 0; m ≤ 3; ++m
  for int n ← 0; n ≤ 6; ++n
    writeLine("Ackermann(" + m + ", " + n + ") = ", ackermann(m, n))
  end
end
```

**Output:**

```
Ackermann(0, 0) = 1
Ackermann(0, 1) = 2
Ackermann(0, 2) = 3
Ackermann(0, 3) = 4
Ackermann(0, 4) = 5
Ackermann(0, 5) = 6
Ackermann(0, 6) = 7
Ackermann(1, 0) = 2
Ackermann(1, 1) = 3
Ackermann(1, 2) = 4
Ackermann(1, 3) = 5
Ackermann(1, 4) = 6
Ackermann(1, 5) = 7
Ackermann(1, 6) = 8
Ackermann(2, 0) = 3
Ackermann(2, 1) = 5
Ackermann(2, 2) = 7
Ackermann(2, 3) = 9
Ackermann(2, 4) = 11
Ackermann(2, 5) = 13
Ackermann(2, 6) = 15
Ackermann(3, 0) = 5
Ackermann(3, 1) = 13
Ackermann(3, 2) = 29
Ackermann(3, 3) = 61
Ackermann(3, 4) = 125
Ackermann(3, 5) = 253
Ackermann(3, 6) = 509
```


## Erlang

```mw
-module(ackermann).
-export([ackermann/2]).

ackermann(0, N) -> 
  N+1;
ackermann(M, 0) -> 
  ackermann(M-1, 1);
ackermann(M, N) when M > 0 andalso N > 0 ->
  ackermann(M-1, ackermann(M, N-1)).
```


## ERRE

Iterative version, using a stack. First version used various GOTOs statement, now removed and substituted with the new ERRE control statements.

```mw
PROGRAM ACKERMAN

!
! computes Ackermann function
! (second version for rosettacode.org)
!

!$INTEGER

DIM STACK[10000]

!$INCLUDE="PC.LIB"

PROCEDURE ACK(M,N->N)
  LOOP
    CURSOR_SAVE(->CURX%,CURY%) 
    LOCATE(8,1)
    PRINT("Livello Stack:";S;"  ")
    LOCATE(CURY%,CURX%)
    IF M<>0 THEN
       IF N<>0 THEN
           STACK[S]=M
           S+=1
           N-=1
        ELSE
           M-=1
           N+=1
        END IF
        CONTINUE LOOP
     ELSE
        N+=1
        S-=1
    END IF
    IF S<>0 THEN
        M=STACK[S]
        M-=1
        CONTINUE LOOP
      ELSE
        EXIT PROCEDURE
    END IF
  END LOOP
END PROCEDURE

BEGIN
   PRINT(CHR$(12);)
   FOR X=0 TO 3 DO
     FOR Y=0 TO 9 DO
        S=1
        ACK(X,Y->ANS)
        PRINT(ANS;)
     END FOR
     PRINT
   END FOR
END PROGRAM
```

Prints a list of Ackermann function values: from A(0,0) to A(3,9). Uses a stack to avoid overflow. Formating options to make this pretty are available, but for this example only basic output is used.

```
 1  2  3  4  5  6  7  8  9  10
 2  3  4  5  6  7  8  9  10  11
 3  5  7  9  11  13  15  17  19  21
 5  13  29  61  125  253  509  1021  2045  4093

Stack Level: 1
```


## Euler Math Toolbox

```mw
>M=zeros(1000,1000);
>function map A(m,n) ...
$  global M;
$  if m==0 then return n+1; endif;
$  if n==0 then return A(m-1,1); endif;
$  if m<=cols(M) and n<=cols(M) then
$    M[m,n]=A(m-1,A(m,n-1));
$    return M[m,n];
$  else return A(m-1,A(m,n-1));
$  endif;
$endfunction
>shortestformat; A((0:3)',0:5)
         1         2         3         4         5         6 
         2         3         4         5         6         7 
         3         5         7         9        11        13 
         5        13        29        61       125       253
```


## Euphoria

This is based on the VBScript example.

```mw
function ack(atom m, atom n)
    if m = 0 then 
        return n + 1
    elsif m > 0 and n = 0 then
        return ack(m - 1, 1)
    else
        return ack(m - 1, ack(m, n - 1))
    end if
end function

for i = 0 to 3 do
    for j = 0 to 6 do
        printf( 1, "%5d", ack( i, j ) )
    end for
    puts( 1, "\n" )
end for
```

### "Alternative"

Translation of

:

Python

```mw
function ackermann(integer m, integer n)
  if m=0 then return n+1
  elsif m>0 and n=0 then return ackermann(m-1, 1)
  elsif m>0 and n>0 then return ackermann(m-1, ackermann(m,n-1))
  else return 0
  end if
  return 0
end function

? ackermann(0, 0)
? ackermann(3, 4)
? ackermann(3, 10)
```

**Output:**

```
1
125
8189
```


## Ezhil

```mw
நிரல்பாகம் அகெர்மன்(முதலெண், இரண்டாமெண்)

  @((முதலெண் < 0) || (இரண்டாமெண் < 0)) ஆனால்

    பின்கொடு -1

  முடி

  @(முதலெண் == 0) ஆனால்

    பின்கொடு இரண்டாமெண்+1

  முடி

  @((முதலெண் > 0) && (இரண்டாமெண் == 00)) ஆனால்

    பின்கொடு அகெர்மன்(முதலெண் - 1, 1)

  முடி

  பின்கொடு அகெர்மன்(முதலெண் - 1, அகெர்மன்(முதலெண், இரண்டாமெண் - 1))

முடி

அ = int(உள்ளீடு("ஓர் எண்ணைத் தாருங்கள், அது பூஜ்ஜியமாகவோ, அதைவிடப் பெரியதாக இருக்கலாம்: "))
ஆ = int(உள்ளீடு("அதேபோல் இன்னோர் எண்ணைத் தாருங்கள், இதுவும் பூஜ்ஜியமாகவோ, அதைவிடப் பெரியதாகவோ இருக்கலாம்: "))

விடை = அகெர்மன்(அ, ஆ)

@(விடை < 0) ஆனால்

  பதிப்பி "தவறான எண்களைத் தந்துள்ளீர்கள்!"

இல்லை

  பதிப்பி "நீங்கள் தந்த எண்களுக்கான அகர்மென் மதிப்பு: ", விடை

முடி
```


## F

The following program implements the Ackermann function in F# but is not tail-recursive and so runs out of stack space quite fast.

```mw
let rec ackermann m n = 
    match m, n with
    | 0, n -> n + 1
    | m, 0 -> ackermann (m - 1) 1
    | m, n -> ackermann (m - 1) ackermann m (n - 1)

do
    printfn "%A" (ackermann (int fsi.CommandLineArgs.[1]) (int fsi.CommandLineArgs.[2]))
```

Transforming this into continuation passing style avoids limited stack space by permitting tail-recursion.

```mw
let ackermann M N =
    let rec acker (m, n, k) =
        match m,n with
            | 0, n -> k(n + 1)
            | m, 0 -> acker ((m - 1), 1, k)
            | m, n -> acker (m, (n - 1), (fun x -> acker ((m - 1), x, k)))
    acker (M, N, (fun x -> x))
```


## Factor

```mw
USING: kernel math locals combinators ;
IN: ackermann

:: ackermann ( m n -- u ) 
    { 
        { [ m 0 = ] [ n 1 + ] } 
        { [ n 0 = ] [ m 1 - 1 ackermann ] } 
        [ m 1 - m n 1 - ackermann ackermann ] 
    } cond ;
```


## Falcon

```mw
function ackermann( m, n )
 if m == 0:  return( n + 1 )
 if n == 0:  return( ackermann( m - 1, 1 ) )
 return( ackermann( m - 1, ackermann( m, n - 1 ) ) )
end

for M in [ 0:4 ]
 for N in [ 0:7 ]
   >> ackermann( M, N ), " "
 end
 >
end
```

The above will output the below. Formating options to make this pretty are available, but for this example only basic output is used.

```
1 2 3 4 5 6 7 
2 3 4 5 6 7 8 
3 5 7 9 11 13 15 
5 13 29 61 125 253 509 
```


## FALSE

```mw
[$$[%
  \$$[%
     1-\$@@a;!  { i j -> A(i-1, A(i, j-1)) }
  1]?0=[
     %1         { i 0 -> A(i-1, 1) }
   ]?
  \1-a;!
1]?0=[
  %1+           { 0 j -> j+1 }
 ]?]a: { j i }

3 3 a;! .  { 61 }
```


## Fantom

```mw
class Main
{
  // assuming m,n are positive
  static Int ackermann (Int m, Int n)
  {
    if (m == 0)
      return n + 1
    else if (n == 0)
      return ackermann (m - 1, 1)
    else
      return ackermann (m - 1, ackermann (m, n - 1))
  }

  public static Void main ()
  {
    (0..3).each |m|
    {
      (0..6).each |n|
      {
        echo ("Ackerman($m, $n) = ${ackermann(m, n)}")
      }
    }
  }
}
```

**Output:**

```
Ackerman(0, 0) = 1
Ackerman(0, 1) = 2
Ackerman(0, 2) = 3
Ackerman(0, 3) = 4
Ackerman(0, 4) = 5
Ackerman(0, 5) = 6
Ackerman(0, 6) = 7
Ackerman(1, 0) = 2
Ackerman(1, 1) = 3
Ackerman(1, 2) = 4
Ackerman(1, 3) = 5
Ackerman(1, 4) = 6
Ackerman(1, 5) = 7
Ackerman(1, 6) = 8
Ackerman(2, 0) = 3
Ackerman(2, 1) = 5
Ackerman(2, 2) = 7
Ackerman(2, 3) = 9
Ackerman(2, 4) = 11
Ackerman(2, 5) = 13
Ackerman(2, 6) = 15
Ackerman(3, 0) = 5
Ackerman(3, 1) = 13
Ackerman(3, 2) = 29
Ackerman(3, 3) = 61
Ackerman(3, 4) = 125
Ackerman(3, 5) = 253
Ackerman(3, 6) = 509
```


## FBSL

Mixed-language solution using pure FBSL, Dynamic Assembler, and Dynamic C layers of FBSL v3.5 concurrently. **The following is a single script**; the breaks are caused by switching between RC's different syntax highlighting schemes:

```mw
#APPTYPE CONSOLE

TestAckermann()

PAUSE

SUB TestAckermann()
	FOR DIM m = 0 TO 3
		FOR DIM n = 0 TO 10
			PRINT AckermannF(m, n), " ";
		NEXT
		PRINT
	NEXT
END SUB

FUNCTION AckermannF(m AS INTEGER, n AS INTEGER) AS INTEGER
	IF NOT m THEN RETURN n + 1
	IF NOT n THEN RETURN AckermannA(m - 1, 1)
	RETURN AckermannC(m - 1, AckermannF(m, n - 1))
END FUNCTION

DYNC AckermannC(m AS INTEGER, n AS INTEGER) AS INTEGER
```

```mw
	int Ackermann(int m, int n)
	{
		if (!m) return n + 1;
		if (!n) return Ackermann(m - 1, 1);
		return Ackermann(m - 1, Ackermann(m, n - 1));
	}
	
	int main(int m, int n)
	{
		return Ackermann(m, n);
	}
```

```mw
END DYNC

DYNASM AckermannA(m AS INTEGER, n AS INTEGER) AS INTEGER
```

```mw
	ENTER 0, 0
	INVOKE Ackermann, m, n
	LEAVE
	RET
	
	@Ackermann
	ENTER 0, 0

	.IF DWORD PTR [m] .THEN
		JMP @F
	.ENDIF
	MOV EAX, n
	INC EAX
	JMP xit

	@@
	.IF DWORD PTR [n] .THEN
		JMP @F
	.ENDIF
	MOV EAX, m
	DEC EAX
	INVOKE Ackermann, EAX, 1
	JMP xit

	@@
	MOV EAX, n
	DEC EAX
	INVOKE Ackermann, m, EAX
	MOV ECX, m
	DEC ECX
	INVOKE Ackermann, ECX, EAX
	
	@xit
	LEAVE
	RET 8
```

```mw
END DYNASM
```

**Output:**

```
1 2 3 4 5 6 7 8 9 10 11
2 3 4 5 6 7 8 9 10 11 12
3 5 7 9 11 13 15 17 19 21 23
5 13 29 61 125 253 509 1021 2045 4093 8189

Press any key to continue...
```


## Fermat

```mw
Func A(m,n) = if m = 0 then n+1 else if n = 0 then A(m-1,1) else A(m-1,A(m,n-1)) fi fi.;
A(3,8)
```

**Output:**

```
     2045
```


## Forth

```mw
: acker ( m n -- u )
	over 0= IF  nip 1+ EXIT  THEN
	swap 1- swap ( m-1 n -- )
	dup  0= IF  1+  recurse EXIT  THEN
	1- over 1+ swap recurse recurse ;
```

**Example of use:**

```
FORTH> 0 0 acker . 1  ok
FORTH> 3 4 acker . 125  ok
```

An optimized version:

```mw
: ackermann                            ( m n -- u ) 
  over                                 ( case statement) 
  0 over = if drop nip 1+     else
  1 over = if drop nip 2 +    else
  2 over = if drop nip 2* 3 + else
  3 over = if drop swap 5 + swap lshift 3 - else
    drop swap 1- swap dup
    if
      1- over 1+ swap recurse recurse exit
    else
      1+ recurse exit                  \ allow tail recursion
    then
  then then then then
;
```


## Fortran

Works with

:

Fortran

version 90 and later

```mw
PROGRAM EXAMPLE  
  IMPLICIT NONE
 
  INTEGER :: i, j
 
  DO i = 0, 3
    DO j = 0, 6
       WRITE(*, "(I10)", ADVANCE="NO") Ackermann(i, j)
    END DO
    WRITE(*,*)
  END DO
 
CONTAINS
 
  RECURSIVE FUNCTION Ackermann(m, n) RESULT(ack)
    INTEGER :: ack, m, n

    IF (m == 0) THEN
      ack = n + 1
    ELSE IF (n == 0) THEN
      ack = Ackermann(m - 1, 1)
    ELSE
      ack = Ackermann(m - 1, Ackermann(m, n - 1))
    END IF
  END FUNCTION Ackermann

END PROGRAM EXAMPLE
```


## Free Pascal

See #Delphi or #Pascal.


## FreeBASIC

```mw
' version 28-10-2016
' compile with: fbc -s console
' to do A(4, 2) the stack size needs to be increased
' compile with: fbc -s console -t 2000

Function ackerman (m As Long, n As Long) As Long

    If m = 0 Then ackerman = n +1

    If m > 0 Then
        If n = 0 Then
            ackerman = ackerman(m -1, 1)
        Else
            If n > 0 Then
                ackerman = ackerman(m -1, ackerman(m, n -1))
            End If
        End If
    End If
End Function

' ------=< MAIN >=------

Dim As Long m, n
Print

For m = 0 To 4
    Print Using "###"; m;
    For n = 0 To 10
        ' A(4, 1) or higher will run out of stack memory (default 1M)
        ' change n = 1 to n = 2 to calculate A(4, 2), increase stack!
        If m = 4 And n = 1 Then Exit For 
        Print Using "######"; ackerman(m, n);
    Next
    Print
Next

' empty keyboard buffer
While InKey <> "" : Wend
Print : Print "hit any key to end program"
Sleep
End
```

**Output:**

```
  0     1     2     3     4     5     6     7     8     9    10    11
  1     2     3     4     5     6     7     8     9    10    11    12
  2     3     5     7     9    11    13    15    17    19    21    23
  3     5    13    29    61   125   253   509  1021  2045  4093  8189
  4    13
```


## FunL

```mw
def
  ackermann( 0, n ) = n + 1
  ackermann( m, 0 ) = ackermann( m - 1, 1 )
  ackermann( m, n ) = ackermann( m - 1, ackermann(m, n - 1) )

for m <- 0..3, n <- 0..4
  printf( 'Ackermann( %d, %d ) = %d\n', m, n, ackermann(m, n) )
```

**Output:**

```
Ackermann( 0, 0 ) = 1
Ackermann( 0, 1 ) = 2
Ackermann( 0, 2 ) = 3
Ackermann( 0, 3 ) = 4
Ackermann( 0, 4 ) = 5
Ackermann( 1, 0 ) = 2
Ackermann( 1, 1 ) = 3
Ackermann( 1, 2 ) = 4
Ackermann( 1, 3 ) = 5
Ackermann( 1, 4 ) = 6
Ackermann( 2, 0 ) = 3
Ackermann( 2, 1 ) = 5
Ackermann( 2, 2 ) = 7
Ackermann( 2, 3 ) = 9
Ackermann( 2, 4 ) = 11
Ackermann( 3, 0 ) = 5
Ackermann( 3, 1 ) = 13
Ackermann( 3, 2 ) = 29
Ackermann( 3, 3 ) = 61
Ackermann( 3, 4 ) = 125
```


## Futhark

```mw
fun ackermann(m: int, n: int): int =
  if m == 0 then n + 1
  else if n == 0 then ackermann(m-1, 1)
  else ackermann(m - 1, ackermann(m, n-1))
```
