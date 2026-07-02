---
title: "FizzBuzz (part 2/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/7
---

## C

```mw
class Program
{
    public void FizzBuzzGo()
    {
        Boolean Fizz = false;
        Boolean Buzz = false;
        for (int count = 1; count <= 100; count ++)
        {
            Fizz = count % 3 == 0;
            Buzz = count % 5 == 0;
            if (Fizz && Buzz)
            {
                Console.WriteLine("Fizz Buzz");
                listBox1.Items.Add("Fizz Buzz");
            }
            else if (Fizz)
            {
                Console.WriteLine("Fizz");
                listBox1.Items.Add("Fizz");
            }
            else if (Buzz)
            {
                Console.WriteLine("Buzz");
                listBox1.Items.Add("Buzz");
            }
            else
            {
                Console.WriteLine(count);
                listBox1.Items.Add(count);
            }
        }
    }
}
```

```mw
class Program
{
    static void Main()
    {
        for (uint i = 1; i <= 100; i++)
        {
            string s = null;
 
            if (i % 3 == 0)
                s = "Fizz";
 
            if (i % 5 == 0)
                s += "Buzz";
 
            System.Console.WriteLine(s ?? i.ToString());
        }
    }
}
```

```mw
using System;
using System.Linq;

namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            Enumerable.Range(1, 100)
                .Select(a => String.Format("{0}{1}", a % 3 == 0 ? "Fizz" : string.Empty, a % 5 == 0 ? "Buzz" : string.Empty))
                .Select((b, i) => String.IsNullOrEmpty(b) ? (i + 1).ToString() : b)
                .ToList()
                .ForEach(Console.WriteLine);
        }
    }
}
```

```mw
using System;
using System.Globalization;
using System.Linq;

namespace FizzBuzz
{
    class Program
    {
        static void Main()
        {
            Enumerable.Range(1, 100)
                .GroupBy(e => e % 15 == 0 ? "FizzBuzz" : e % 5 == 0 ? "Buzz" : e % 3 == 0 ? "Fizz" : string.Empty)
                .SelectMany(item => item.Select(x => new { 
                    Value = x, 
                    Display = String.IsNullOrEmpty(item.Key) ? x.ToString(CultureInfo.InvariantCulture) : item.Key 
                }))
                .OrderBy(x => x.Value)
                .Select(x => x.Display)
                .ToList()
                .ForEach(Console.WriteLine);
        }
    }
}
```

```mw
using System;
namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                if (i % 15 == 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine("Fizz");
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine("Buzz");
                }
                else
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
```

```mw
using System;
using System.Globalization;

namespace Rosettacode
{
    class Program
    {
        static void Main()
        {
            for (var number = 0; number < 100; number++)
            {
                if ((number % 3) == 0 & (number % 5) == 0)
                {
                    //For numbers which are multiples of both three and five print "FizzBuzz".
                    Console.WriteLine("FizzBuzz");
                    continue;
                }

                if ((number % 3) == 0) Console.WriteLine("Fizz");
                if ((number % 5) == 0) Console.WriteLine("Buzz");
                if ((number % 3) != 0 && (number % 5) != 0) Console.WriteLine(number.ToString(CultureInfo.InvariantCulture));

                if (number % 5 == 0)
                {
                    Console.WriteLine(Environment.NewLine);
                }
            }
        }
    }
}
```

```mw
using System;
using System.Linq;
 
namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            Enumerable.Range(1, 100).ToList().ForEach(i => Console.WriteLine(i % 5 == 0 ? string.Format(i % 3 == 0 ? "Fizz{0}" : "{0}", "Buzz") : string.Format(i%3 == 0 ? "Fizz" : i.ToString())));
        }
    }
}
```

### With C#8 switch expressions

```mw
class Program
{
    public static string FizzBuzzIt(int n) =>
        (n % 3, n % 5) switch
        {
            (0, 0) => "FizzBuzz",
            (0, _) => "Fizz",
            (_, 0) => "Buzz",
            (_, _) => $"{n}"
        };

    static void Main(string[] args)
    { 
        foreach (var n in Enumerable.Range(1, 100))
        {
            Console.WriteLine(FizzBuzzIt(n));
        }
    }
}
```

### TDD using delegates

```mw
using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace FizzBuzz
{
    [TestClass]
    public class FizzBuzzTest
    {
        private FizzBuzz fizzBuzzer;

        [TestInitialize]
        public void Initialize()
        {
            fizzBuzzer = new FizzBuzz();
        }

        [TestMethod]
        public void Give4WillReturn4()
        {
            Assert.AreEqual("4", fizzBuzzer.FizzBuzzer(4));
        }

        [TestMethod]
        public void Give9WillReturnFizz()
        {
            Assert.AreEqual("Fizz", fizzBuzzer.FizzBuzzer(9));
        }

        [TestMethod]
        public void Give25WillReturnBuzz()
        {
            Assert.AreEqual("Buzz", fizzBuzzer.FizzBuzzer(25));
        }

        [TestMethod]
        public void Give30WillReturnFizzBuzz()
        {
            Assert.AreEqual("FizzBuzz", fizzBuzzer.FizzBuzzer(30));
        }

        [TestMethod]
        public void First15()
        {
            ICollection expected = new ArrayList
                {"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"};

            var actual = Enumerable.Range(1, 15).Select(x => fizzBuzzer.FizzBuzzer(x)).ToList();

            CollectionAssert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void From1To100_ToShowHowToGet100()
        {
            const int expected = 100;
            var actual = Enumerable.Range(1, 100).Select(x => fizzBuzzer.FizzBuzzer(x)).ToList();

            Assert.AreEqual(expected, actual.Count);
        }
    }

    public class FizzBuzz
    {
        private delegate string Xzzer(int value);
        private readonly IList<Xzzer> _functions = new List<Xzzer>();

        public FizzBuzz()
        {
            _functions.Add(x => x % 3 == 0 ? "Fizz" : "");
            _functions.Add(x => x % 5 == 0 ? "Buzz" : "");
        }

        public string FizzBuzzer(int value)
        {
            var result = _functions.Aggregate(String.Empty, (current, function) => current + function.Invoke(value));
            return String.IsNullOrEmpty(result) ? value.ToString(CultureInfo.InvariantCulture) : result;
        }
    }
}
```

### Good old C ways

```mw
using System;
int max = 100;
for(int i=0;
    ++i<=max; 
    Console.WriteLine("{0}{1}{2}", i%3==0 ? "Fizz" : "", i%5==0 ? "Buzz" : "", i%3!=0 && i%5!=0  ? i.ToString() : "")
){}
```


## C++

### minimal conditions

```mw
#include <iostream>
#include <chrono>

int main()
{

	int fizz = 0, buzz = 0, fizzbuzz = 0;

	bool isFizz = false;

	auto startTime = std::chrono::high_resolution_clock::now();

	for (unsigned int i = 1; i <= 4000000000; i++) {
		isFizz = false;

		if (i % 3 == 0) {
			isFizz = true;
			fizz++;
		}

		if (i % 5 == 0) {
			if (isFizz) {
				fizz--;
				fizzbuzz++;
			}
			else {
				buzz++;
			}
		}

	}

	auto endTime = std::chrono::high_resolution_clock::now();
	auto totalTime = endTime - startTime;

	printf("\t fizz : %d, buzz: %d, fizzbuzz: %d, duration %lld milliseconds\n", fizz, buzz, fizzbuzz, (totalTime / std::chrono::milliseconds(1)));

	return 0;
}
```

### with modulo

```mw
#include <iostream>

using namespace std;
int main ()
{
       for (int i = 1; i <= 100; i++) 
       {
               if ((i % 15) == 0)
                       cout << "FizzBuzz\n";
               else if ((i % 3) == 0)
                       cout << "Fizz\n";
               else if ((i % 5) == 0)
                       cout << "Buzz\n";
               else
                       cout << i << "\n";
       }
       return 0;
}
```

### without modulo 15

```mw
#include <iostream>
using namespace std;

int main()
{
  for (int i = 0; i <= 100; ++i)
  {
    bool fizz = (i % 3) == 0;
    bool buzz = (i % 5) == 0;
    if (fizz)
      cout << "Fizz";
    if (buzz)
      cout << "Buzz";
    if (!fizz && !buzz)
      cout << i;
    cout << "\n";
  }
  return 0;
}
```

### without modulo

Modulo can be expensive on some architectures.

```mw
#include <iostream>

int main()
{
    int i, f = 2, b = 4; 

    for ( i = 1 ; i <= 100 ; ++i, --f, --b )
    {
        if ( f && b ) { std::cout << i;             }
        if ( !f )     { std::cout << "Fizz"; f = 3; }
        if ( !b )     { std::cout << "Buzz"; b = 5; }
        std::cout << std::endl;
    }

    return 0;
}
```

### using std::transform

Works with

:

C++11

```mw
#include <iostream>                                                                                                     
#include <algorithm>
#include <vector>

int main()
{
  std::vector<int> range(100);
  std::iota(range.begin(), range.end(), 1);

  std::vector<std::string> values;
  values.resize(range.size());

  auto fizzbuzz = [](int i) -> std::string {
    if ((i%15) == 0) return "FizzBuzz";
    if ((i%5) == 0)  return "Buzz";
    if ((i%3) == 0)  return "Fizz";
    return std::to_string(i);
  };

  std::transform(range.begin(), range.end(), values.begin(), fizzbuzz);

  for (auto& str: values) std::cout << str << std::endl;

  return 0;
}
```

### metaprogramming

Version computing FizzBuzz at compile time with metaprogramming:

```mw
#include <iostream>

template <int n, int m3, int m5> 
struct fizzbuzz : fizzbuzz<n-1, (n-1)%3, (n-1)%5>
{
  fizzbuzz() 
  { std::cout << n << std::endl; }
};

template <int n>
struct fizzbuzz<n, 0, 0> : fizzbuzz<n-1, (n-1)%3, (n-1)%5>
{
  fizzbuzz() 
  { std::cout << "FizzBuzz" << std::endl; }
};

template <int n, int p>
struct fizzbuzz<n, 0, p> : fizzbuzz<n-1, (n-1)%3, (n-1)%5>
{
  fizzbuzz() 
  { std::cout << "Fizz" << std::endl; }
};

template <int n, int p>
struct fizzbuzz<n, p, 0> : fizzbuzz<n-1, (n-1)%3, (n-1)%5>
{
  fizzbuzz() 
  { std::cout << "Buzz" << std::endl; }
};

template <>
struct fizzbuzz<0,0,0>
{
  fizzbuzz() 
  { std::cout << 0 << std::endl; }
};

template <int n>
struct fb_run
{
  fizzbuzz<n, n%3, n%5> fb;
};

int main()
{
  fb_run<100> fb;
  return 0;
}
```

### hardcore templates

Compile with -ftemplate-depth-9000 -std=c++0x:

```mw
#include <iostream>
#include <string>
#include <cstdlib>
#include <boost/mpl/string.hpp>
#include <boost/mpl/fold.hpp>
#include <boost/mpl/size_t.hpp>

using namespace std;
using namespace boost;

///////////////////////////////////////////////////////////////////////////////
// exponentiation calculations
template <int accum, int base, int exp> struct POWER_CORE : POWER_CORE<accum * base, base, exp - 1>{};

template <int accum, int base>
struct POWER_CORE<accum, base, 0>
{
    enum : int { val = accum };
};

template <int base, int exp> struct POWER : POWER_CORE<1, base, exp>{};

///////////////////////////////////////////////////////////////////////////////
// # of digit calculations
template <int depth, unsigned int i> struct NUM_DIGITS_CORE : NUM_DIGITS_CORE<depth + 1, i / 10>{};

template <int depth>
struct NUM_DIGITS_CORE<depth, 0>
{
    enum : int { val = depth};
};

template <int i> struct NUM_DIGITS : NUM_DIGITS_CORE<0, i>{};

template <>
struct NUM_DIGITS<0>
{
    enum : int { val = 1 };
};

///////////////////////////////////////////////////////////////////////////////
// Convert digit to character (1 -> '1')
template <int i>
struct DIGIT_TO_CHAR
{
    enum : char{ val = i + 48 };
};

///////////////////////////////////////////////////////////////////////////////
// Find the digit at a given offset into a number of the form 0000000017
template <unsigned int i, int place> // place -> [0 .. 10]
struct DIGIT_AT
{
    enum : char{ val = (i / POWER<10, place>::val) % 10 };
};

struct NULL_CHAR
{
    enum : char{ val = '\0' };
};

///////////////////////////////////////////////////////////////////////////////
// Convert the digit at a given offset into a number of the form '0000000017' to a character
template <unsigned int i, int place> // place -> [0 .. 9]
    struct ALT_CHAR : DIGIT_TO_CHAR< DIGIT_AT<i, place>::val >{};

///////////////////////////////////////////////////////////////////////////////
// Convert the digit at a given offset into a number of the form '17' to a character

// Template description, with specialization to generate null characters for out of range offsets
template <unsigned int i, int offset, int numDigits, bool inRange>  
    struct OFFSET_CHAR_CORE_CHECKED{};
template <unsigned int i, int offset, int numDigits>                
    struct OFFSET_CHAR_CORE_CHECKED<i, offset, numDigits, false> : NULL_CHAR{};
template <unsigned int i, int offset, int numDigits>                
    struct OFFSET_CHAR_CORE_CHECKED<i, offset, numDigits, true>  : ALT_CHAR<i, (numDigits - offset) - 1 >{};

// Perform the range check and pass it on
template <unsigned int i, int offset, int numDigits>
    struct OFFSET_CHAR_CORE : OFFSET_CHAR_CORE_CHECKED<i, offset, numDigits, offset < numDigits>{};

// Calc the number of digits and pass it on
template <unsigned int i, int offset>
    struct OFFSET_CHAR : OFFSET_CHAR_CORE<i, offset, NUM_DIGITS<i>::val>{};

///////////////////////////////////////////////////////////////////////////////
// Integer to char* template. Works on unsigned ints.
template <unsigned int i>
struct IntToStr
{
    const static char str[];
    typedef typename mpl::string<
    OFFSET_CHAR<i, 0>::val,
    OFFSET_CHAR<i, 1>::val,
    OFFSET_CHAR<i, 2>::val,
    OFFSET_CHAR<i, 3>::val,
    OFFSET_CHAR<i, 4>::val,
    OFFSET_CHAR<i, 5>::val,
    /*OFFSET_CHAR<i, 6>::val,
    OFFSET_CHAR<i, 7>::val,
    OFFSET_CHAR<i, 8>::val,
    OFFSET_CHAR<i, 9>::val,*/
    NULL_CHAR::val>::type type;
};

template <unsigned int i>
const char IntToStr<i>::str[] = 
{
    OFFSET_CHAR<i, 0>::val,
    OFFSET_CHAR<i, 1>::val,
    OFFSET_CHAR<i, 2>::val,
    OFFSET_CHAR<i, 3>::val,
    OFFSET_CHAR<i, 4>::val,
    OFFSET_CHAR<i, 5>::val,
    OFFSET_CHAR<i, 6>::val,
    OFFSET_CHAR<i, 7>::val,
    OFFSET_CHAR<i, 8>::val,
    OFFSET_CHAR<i, 9>::val,
    NULL_CHAR::val
};

template <bool condition, class Then, class Else>
struct IF
{
    typedef Then RET;
};

template <class Then, class Else>
struct IF<false, Then, Else>
{
    typedef Else RET;
};

template < typename Str1, typename Str2 >
struct concat : mpl::insert_range<Str1, typename mpl::end<Str1>::type, Str2> {};
template <typename Str1, typename Str2, typename Str3 >
struct concat3 : mpl::insert_range<Str1, typename mpl::end<Str1>::type, typename concat<Str2, Str3 >::type > {};

typedef typename mpl::string<'f','i','z','z'>::type fizz;
typedef typename mpl::string<'b','u','z','z'>::type buzz;
typedef typename mpl::string<'\r', '\n'>::type mpendl;
typedef typename concat<fizz, buzz>::type fizzbuzz;

// discovered boost mpl limitation on some length

template <int N>
struct FizzBuzz
{
    typedef typename concat3<typename FizzBuzz<N - 1>::type, typename IF<N % 15 == 0, typename fizzbuzz::type, typename IF<N % 3 == 0, typename fizz::type, typename IF<N % 5 == 0, typename buzz::type, typename IntToStr<N>::type >::RET >::RET >::RET, typename mpendl::type>::type type;
};

template <>
struct FizzBuzz<1>
{
    typedef mpl::string<'1','\r','\n'>::type type;
};

int main(int argc, char** argv)
{
    const int n = 7;
    std::cout << mpl::c_str<FizzBuzz<n>::type>::value << std::endl;
	return 0;
}
```

Note: it takes up lots of memory and takes several seconds to compile. To enable compilation for 7 < n <= 25, please, modify include/boost/mpl/limits/string.hpp BOOST_MPL_LIMIT_STRING_SIZE to 128 instead of 32).


## Calcscript

```
(fn fizz (i)
  (r
    (eq (valid? (/ i 15)) (puts FizzBuzz))
    (eq (valid? (/ i 5 )) (puts Buzz))
    (eq (valid? (/ i 3 )) (puts Fizz))
    (p i)
  )
)

(fn count (n i)
  (d
    (t (- n i))
    (fizz i)
    (count n (+ i 1))
  )
)

(count 101 1)
```

**Output:**

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
```


## Casio BASIC

See FizzBuzz/Basic


## Cduce

```mw
(* FizzBuzz in CDuce *)

let format (n : Int) : Latin1 =
    if (n mod 3 = 0) || (n mod 5 = 0) then "FizzBuzz"
    else if (n mod 5 = 0) then "Buzz"
    else if (n mod 3 = 0) then "Fizz"
    else string_of (n);;

let fizz (n : Int, size : Int) : _ = 
    print (format (n) @ "\n");
    if (n = size) then
        n = 0 (* do nothing *)
    else
        fizz(n + 1, size);;

let fizbuzz (size : Int) : _ = fizz (1, size);;

let _ = fizbuzz(100);;
```


## Ceylon

```mw
shared void run() => {for (i in 1..100) {for (j->k in [3->"Fizz", 5->"Buzz"]) if (j.divides(i)) k}.reduce(plus) else i}.each(print);
```


## Chapel

```mw
proc fizzbuzz(n) {
	for i in 1..n do
		if i % 15 == 0 then
			writeln("FizzBuzz");
		else if i % 5 == 0 then
			writeln("Buzz");
		else if i % 3 == 0 then
			writeln("Fizz");
		else
			writeln(i);
}

fizzbuzz(100);
```


## Chef

See FizzBuzz/EsoLang


## Cherrycake

```mw
# Route with custom number of iterations
cached get ~/:n {

    # Get the Number of Iterations from the URL Params
    int n = req.params.n || 100

    # Loop through each iteration
    for (i in range(n)) {

        if (i % 2 == 0 && i % 3 == 0) { res.write("FizzBuzz\n") continue }
        if (i % 2 == 0) { res.write("Fizz\n"); continue; }
        if (i % 3 == 0) { res.write("Buzz\n"); continue; }
        res.write(i + "\n");

    }

    # Close the connection
    res.end();

}
```


## CJam

source license

```
100{):I3%!"Fizz"*I5%!"Buzz"*+Ie|N}/
```


## Clay

```mw
main() {
    for(i in range(1,100)) {
        if(i % 3 == 0 and i % 5 == 0) println("fizzbuzz");
        else if(i % 3 == 0) println("fizz");
        else if(i % 5 == 0) println("buzz");
        else print(i);
    }
}
```


## Clipper

Also compiles with Harbour (Harbour 3.2.0dev (r1405201749))

```mw
PROCEDURE Main()

   LOCAL n
   LOCAL cFB 

   FOR n := 1 TO 100
      cFB := ""
      AEval( { { 3, "Fizz" }, { 5, "Buzz" } }, {|x| cFB += iif( ( n % x[ 1 ] ) == 0, x[ 2 ], "" ) } )
      ?? iif( cFB == "", LTrim( Str( n ) ), cFB ) + iif( n == 100, ".", ", " )
   NEXT

   RETURN
```

The advantage of this approach is that it is trivial to add another factor:

```
AEval( {{3,"Fizz"},{5,"Buzz"},{9,"Jazz"}}, {|x| cFB += Iif((n % x[1])==0, x[2], "")})
```


## CLIPS

```mw
(deffacts count
          (count-to 100))

(defrule print-numbers
         (count-to ?max)
         =>
         (loop-for-count (?num ?max) do
        (if (and (= (mod ?num 3) 0) (= (mod ?num 5) 0) ) then
                (printout t "FizzBuzz" crlf)
         else (if (= (mod ?num 3) 0) then
                      (printout t "Fizz" crlf)
               else (if (= (mod ?num 5) 0) then
                             (printout t "Buzz" crlf)
                     else
                             (printout t ?num crlf))))))
```


## Clojure

```mw
(doseq [x (range 1 101)] (println x (str (when (zero? (mod x 3)) "fizz") (when (zero? (mod x 5)) "buzz"))))
```

```mw
(defn fizzbuzz [start finish] 
  (map (fn [n]
	(cond
		(zero? (mod n 15)) "FizzBuzz"
		(zero? (mod n 3)) "Fizz"
		(zero? (mod n 5)) "Buzz"
		:else n))
	(range start finish)))
(fizzbuzz 1 100)
```

```mw
(map (fn [x] (cond (zero? (mod x 15)) "FizzBuzz" 
                   (zero? (mod x 5)) "Buzz"
                   (zero? (mod x 3)) "Fizz"
		     :else x))
     (range 1 101))
```

```mw
(map #(let [s (str (if (zero? (mod % 3)) "Fizz") (if (zero? (mod % 5)) "Buzz"))] (if (empty? s) % s)) (range 1 101))
```

```mw
(def fizzbuzz (map 
  #(cond (zero? (mod % 15)) "FizzBuzz"
         (zero? (mod % 5)) "Buzz"
         (zero? (mod % 3)) "Fizz"
               :else %)
  (iterate inc 1)))
```

```mw
(defn fizz-buzz 
  ([] (fizz-buzz (range 1 101)))
  ([lst]
     (letfn [(fizz? [n] (zero? (mod n 3)))
	     (buzz? [n] (zero? (mod n 5)))]
       (let [f     "Fizz" 
	     b     "Buzz" 
	     items (map (fn [n]
			  (cond (and (fizz? n) (buzz? n)) (str f b)
				(fizz? n) f
				(buzz? n) b
				:else n))
			lst)] items))))
```

```mw
(map (fn [n] 
       (if-let [fb (seq (concat (when (zero? (mod n 3)) "Fizz")
                                (when (zero? (mod n 5)) "Buzz")))]
           (apply str fb)
           n))
     (range 1 101))
```

```mw
(take 100 (map #(let [s (str %2 %3) ] (if (seq s) s (inc %)) )
            (range)
            (cycle [ "" "" "Fizz" ])
            (cycle [ "" "" "" "" "Buzz" ])))
```

```mw
(map #(nth (conj (cycle [% % "Fizz" % "Buzz" "Fizz" % % "Fizz" "Buzz" % "Fizz" % % "FizzBuzz"]) %) %) (range 1 101))
```

```mw
(let [n nil fizz (cycle [n n "fizz"]) buzz (cycle [n n n n "buzz"]) nums (iterate inc 1)]
  (take 20 (map #(if (or %1 %2) (str %1 %2) %3) fizz buzz nums)))
```

```mw
(take 100
      (map #(if (pos? (compare %1 %2)) %1 %2)
           (map str (drop 1 (range)))
           (map str (cycle ["" "" "Fizz"]) (cycle ["" "" "" "" "Buzz"]))))
```

```mw
;;Using clojure maps
(defn fizzbuzz
  [n]
  (let [rule {3 "Fizz"
              5 "Buzz"}
        divs (->> rule
                  (map first)
                  sort
                  (filter (comp (partial = 0)
                                (partial rem n))))]
    (if (empty? divs)
      (str n)
      (->> divs
           (map rule)
           (apply str)))))

(defn allfizzbuzz
  [max]
  (map fizzbuzz (range 1 (inc max))))
```

```mw
(take 100
   (map #(str %1 %2 (if-not (or %1 %2) %3))
        (cycle [nil nil "Fizz"])
        (cycle [nil nil nil nil "Buzz"])
        (rest (range))
   ))
```

```mw
(take 100
  (
    (fn [& fbspec]
      (let [
             fbseq #(->> (repeat nil) (cons %2) (take %1) reverse cycle)
             strfn #(apply str (if (every? nil? (rest %&)) (first %&)) (rest %&))
          ]
        (->>
          fbspec
          (partition 2)
          (map #(apply fbseq %))
          (apply map strfn (rest (range)))
          ) ;;endthread
      ) ;;endlet
    ) ;;endfn
    3 "Fizz" 5 "Buzz" 7 "Bazz"
  ) ;;endfn apply
) ;;endtake
```

```mw
(take 100
      (map-indexed
        #(case %2 14 "FizzBuzz" (2 5 8 11) "Fizz" (4 9) "Buzz" (inc %1))
        (cycle (range 15))
        )
)
```

```mw
(take 100
       (->>
          (map str (cycle [nil nil "Fizz"]) (cycle [nil nil nil nil "Buzz"]))
          (map-indexed #(if (empty? %2) (inc %1) %2))
       )
)
```

```mw
(take 100 
   (map-indexed
      #(if (number? %2) (+ %1 %2) %2)
      (cycle [1 1 "Fizz" 1 "Buzz" "Fizz" 1 1 "Fizz" "Buzz" 1 "Fizz" 1 1 "FizzBuzz"])
      )
)
```


## CLU

```mw
start_up = proc ()
    po: stream := stream$primary_output()
 
    for i: int in int$from_to(1, 100) do
        out: string := ""
        if i // 3 = 0 then out := out || "Fizz" end
        if i // 5 = 0 then out := out || "Buzz" end
        if string$empty(out) then out := int$unparse(i) end
        stream$putl(po, out)
    end
end start_up
```


## CMake

```mw
foreach(i RANGE 1 100)
  math(EXPR off3 "${i} % 3")
  math(EXPR off5 "${i} % 5")
  if(NOT off3 AND NOT off5)
    message(FizzBuzz)
  elseif(NOT off3)
    message(Fizz)
  elseif(NOT off5)
    message(Buzz)
  else()
    message(${i})
  endif()
endforeach(i)
```


## COBOL

### Canonical version

Works with

:

OpenCOBOL

```mw
      * FIZZBUZZ.COB
      * cobc -x -g FIZZBUZZ.COB
      *
       IDENTIFICATION        DIVISION.
       PROGRAM-ID.           fizzbuzz.
       DATA                  DIVISION.
       WORKING-STORAGE       SECTION.
       01 CNT      PIC 9(03) VALUE 1.
       01 REM      PIC 9(03) VALUE 0.
       01 QUOTIENT PIC 9(03) VALUE 0.
       PROCEDURE             DIVISION.
      *
       PERFORM UNTIL CNT > 100
         DIVIDE 15 INTO CNT GIVING QUOTIENT REMAINDER REM
         IF REM = 0
           THEN
             DISPLAY "FizzBuzz " WITH NO ADVANCING
           ELSE
             DIVIDE 3 INTO CNT GIVING QUOTIENT REMAINDER REM
             IF REM = 0
               THEN
                 DISPLAY "Fizz " WITH NO ADVANCING
               ELSE
                 DIVIDE 5 INTO CNT GIVING QUOTIENT REMAINDER REM
                 IF REM = 0
                   THEN
                     DISPLAY "Buzz " WITH NO ADVANCING
                   ELSE
                     DISPLAY CNT " " WITH NO ADVANCING
                 END-IF
             END-IF
         END-IF
         ADD 1 TO CNT
       END-PERFORM
       DISPLAY ""
       STOP RUN.
```

### Simpler version

I know this doesn't have the full-bodied, piquant flavor expected from COBOL, but it is a little shorter.

Works with

:

OpenCOBOL

```mw
Identification division.
Program-id. fizz-buzz.

Data division.
Working-storage section.

01 num pic 999.

Procedure division.
    Perform varying num from 1 by 1 until num > 100
        if function mod (num, 15) = 0 then display "fizzbuzz"
        else if function mod (num, 3) = 0 then display "fizz"
        else if function mod (num, 5) = 0 then display "buzz"
        else display num
    end-perform.
    Stop run.
```

### Evaluate Version

I think this shows clearly that it's resolving the problem and illuminating the rules specified

Works with

:

OpenCOBOL

```mw
       IDENTIFICATION DIVISION.
       PROGRAM-ID.  FIZZBUZZ.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  X PIC 999.
       01  Y PIC 999.
       01  REM3 PIC 999.
       01  REM5 PIC 999.
       PROCEDURE DIVISION.
           PERFORM VARYING X FROM 1 BY 1 UNTIL X > 100
               DIVIDE X BY 3 GIVING Y REMAINDER REM3
               DIVIDE X BY 5 GIVING Y REMAINDER REM5
            EVALUATE REM3 ALSO REM5
              WHEN ZERO ALSO ZERO
                DISPLAY "FizzBuzz"
              WHEN ZERO ALSO ANY
                DISPLAY "Fizz"
              WHEN ANY ALSO ZERO
                DISPLAY "Buzz"
              WHEN OTHER
                DISPLAY X
            END-EVALUATE
           END-PERFORM
           STOP RUN
           .
```

### Chase the Fizz

Works with

:

OpenCOBOL

A solution that simply evaluates and adds.

```mw
         >>SOURCE FORMAT FREE
identification division.
program-id. fizzbuzz.
data division.
working-storage section.
01  i pic 999.
01  fizz pic 999 value 3.
01  buzz pic 999 value 5.
procedure division.
start-fizzbuzz.
    perform varying i from 1 by 1 until i > 100 
        evaluate i also i
        when fizz also buzz
            display 'fizzbuzz'
            add 3 to fizz
            add 5 to buzz
        when fizz also any
            display 'fizz'
            add 3 to fizz
        when buzz also any
            display 'buzz'
            add 5 to buzz
        when other
            display i
        end-evaluate
    end-perform
    stop run
    .
end program fizzbuzz.
```


## Coco

```mw
for i from 1 to 100
    console.log do
       if      i % 15 == 0 then 'FizzBuzz'
       else if i % 3 == 0 then 'Fizz'
       else if i % 5 == 0 then 'Buzz'
       else i
```

```mw
for i from 1 to 100
    console.log(['Fizz' unless i % 3] + ['Buzz' unless i % 5] or String(i))
```


## Coconut

```mw
def fizzbuzz(n):
      case (n % 3, n % 5):
          match (0, 0): return "FizzBuzz"
          match (0, _): return "Fizz"
          match (_, 0): return "Buzz"
      else: return n |> str
range(1,101)|> map$(fizzbuzz)|> x -> '\n'.join(x)|> print
```


## CoffeeScript

```mw
for i in [1..100]
  if i % 15 is 0
    console.log "FizzBuzz"
  else if i % 3 is 0
    console.log "Fizz"
  else if i % 5 is 0
    console.log "Buzz"
  else
    console.log i
```

```mw
for i in [1..100]
  console.log \
    if i % 15 is 0
      "FizzBuzz"
    else if i % 3 is 0
      "Fizz"
    else if i % 5 is 0
      "Buzz"
    else
      i
```

```mw
for i in [1..100]
  console.log(['Fizz' if i % 3 is 0] + ['Buzz' if i % 5 is 0] or i)
```


## Cognate

This is the first example given on Cognate's website (available under the BSD-2-Clause license):

```mw
Def Fizzbuzz (
	Let N be Of (Integer?);
	Def Multiple as (Zero? Modulo Swap N);

	If Multiple of 15 then "fizzbuzz"
	If Multiple of 3  then "fizz"
	If Multiple of 5  then "buzz"
	                  else N
);

For each in Range 1 to 100 (Print Fizzbuzz);
```


## ColdFusion

```mw
<Cfloop from="1" to="100" index="i">
  <Cfif i mod 15 eq 0>FizzBuzz
  <Cfelseif i mod 5 eq 0>Fizz
  <Cfelseif i mod 3 eq 0>Buzz
  <Cfelse><Cfoutput>#i# </Cfoutput>
  </Cfif>      
</Cfloop>
```

cfscript version

```mw
<cfscript>
result = "";
  for(i=1;i<=100;i++){
    result=ListAppend(result, (i%15==0) ? "FizzBuzz": (i%5==0) ? "Buzz" : (i%3 eq 0)? "Fizz" : i );
  }
  WriteOutput(result);
</cfscript>
```


## Comal

```mw
0010 FOR i#:=1 TO 100 DO
0020   IF i# MOD 15=0 THEN
0030     PRINT "FizzBuzz"
0040   ELIF i# MOD 5=0 THEN
0050     PRINT "Buzz"
0060   ELIF i# MOD 3=0 THEN
0070     PRINT "Fizz"
0080   ELSE
0090     PRINT i#
0100   ENDIF
0110 ENDFOR i#
0120 END
```


## Comefrom0x10

```mw
fizzbuzz
  mod_three = 3
  mod_five = 5
  comefrom fizzbuzz
  n
  comefrom fizzbuzz if n is mod_three
  comefrom fizzbuzz if n is mod_five
  n = n + 1

  fizz
    comefrom fizzbuzz if n is mod_three
    'Fizz'...
    mod_three = mod_three + 3
    linebreak
      # would like to write "unless mod_three is mod_five"
      comefrom fizz if mod_three - mod_five - 3
      ''

  buzz
    comefrom fizzbuzz if n is mod_five
    'Buzz'
    mod_five = mod_five + 5

  comefrom fizzbuzz if n is 100
```


## Commodore BASIC

See FizzBuzz/Basic


## Common Lisp

Solution 1:

```mw
(defun fizzbuzz ()
  (loop for x from 1 to 100 do
    (princ (cond ((zerop (mod x 15)) "FizzBuzz")
                 ((zerop (mod x 3))  "Fizz")
                 ((zerop (mod x 5))  "Buzz")
                 (t                  x)))
    (terpri)))
```

Solution 2:

```mw
(defun fizzbuzz ()
  (loop for x from 1 to 100 do
    (format t "~&~{~A~}"
      (or (append (when (zerop (mod x 3)) '("Fizz"))
                  (when (zerop (mod x 5)) '("Buzz")))
          (list x)))))
```

Solution 3:

```mw
(defun fizzbuzz ()
  (loop for n from 1 to 100
     do (format t "~&~[~[FizzBuzz~:;Fizz~]~*~:;~[Buzz~*~:;~D~]~]~%"
                (mod n 3) (mod n 5) n)))
```

Solution 4:

```mw
(loop as n from 1 to 100
      as fizz = (zerop (mod n 3))
      as buzz = (zerop (mod n 5))
      as numb = (not (or fizz buzz))
      do
  (format t
   "~&~:[~;Fizz~]~:[~;Buzz~]~:[~;~D~]~%"
   fizz buzz numb n))
```

Solution 5:

```mw
(format t "~{~:[~&~;~:*~:(~a~)~]~}"
  (loop as n from 1 to 100
        as f = (zerop (mod n 3))
        as b = (zerop (mod n 5))
        collect nil
        if f collect 'fizz
        if b collect 'buzz
        if (not (or f b)) collect n))
```

Solution 6:

```mw
(format t "~{~{~:[~;Fizz~]~:[~;Buzz~]~:[~*~;~d~]~}~%~}"
  (loop as n from 1 to 100
        as f = (zerop (mod n 3))
        as b = (zerop (mod n 5))
        collect (list f b (not (or f b)) n)))
```

Solution 7:

```mw
(defun core (x)
  (mapcar 
    #'(lambda (a b) (if (equal 0 (mod x a)) b x)) 
    '(3 5) 
    '("fizz" "buzz")))

(defun filter-core (x)
  (if (equal 1 (length (remove-duplicates x)))
    (list (car x))
    (remove-if-not #'stringp x)))

(defun fizzbuzz (x)
  (loop for a from 1 to x do
    (print (format nil "~{~a~}" (filter-core (core a))))))

(fizzbuzz 100)
```

Solution 8:

```mw
(defun range (min max)
  (loop
    :for x :from min :to max
    :collect x))

(defun fizzbuzz ()
  (map 'nil #'(lambda (n)
                (princ
                  (cond
                    ((zerop (mod n 15)) "FizzBuzz!")
                    ((zerop (mod n 5)) "Buzz!")
                    ((zerop (mod n 3)) "Fizz!")
                    (t n))
                  (terpri)))
            (range 1 100)))
```

First 16 lines of output:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```

### Alternate solution

I use Allegro CL 10.1

```mw
;; Project : FizzBuzz

(defun fizzbuzz (&optional n)
          (let ((n (or n 1)))
          (if (> n 100)
              nil
              (progn
              (let ((mult-3 (is-mult-p n 3))
              (mult-5 (is-mult-p n 5)))
              (if mult-3
                  (princ "Fizz"))
              (if mult-5
                  (princ "Buzz"))
              (if (not (or mult-3 mult-5))
                  (princ n))
              (princ #\linefeed)
              (fizzbuzz (+ n 1)))))))
(defun is-mult-p (n multiple)
          (= (rem n multiple) 0))
(fizzbuzz 1)
```

Output:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```


## Cowgol

### Straightforward version

```mw
include "cowgol.coh";

var i: uint8 := 1;
while i <= 100 loop
    if i % 15 == 0 then 
        print("FizzBuzz");
    elseif i % 5 == 0 then
        print("Buzz");
    elseif i % 3 == 0 then
        print("Fizz");
    else
        print_i8(i);
    end if;
    print_nl();
    i := i + 1;
end loop;
```

### No division

When targeting small systems, it is generally a good idea not to use division if you don't have to. Most of the processors Cowgol targets do not have hardware division, requiring the use of slow and bulky software division routines. This is not helped by the fact that these processors are not fast to begin with, and memory is usually scarce.

Avoiding division requires not only that `%` be avoided, but also `print_i8` cannot be used, as printing integers in decimal format is also done by division. Instead, this code keeps separate 'fizz' and 'buzz' counters around, as well as keeping the number ready in ASCII format for printing. Nevertheless, the following code compiles to a 252-byte 8080 executable, whereas the naive version above compiles to a 755-byte executable. (Compare to the 8080 assembly program above, which assembles to a 98-byte executable.)

```mw
include "cowgol.coh";

var i: uint8 := 100;
var fizz: uint8 := 3;
var buzz: uint8 := 5;
var dh: uint8 := '0';
var dl: uint8 := '1';
var prnum: uint8;

while i != 0 loop
    fizz := fizz - 1;
    buzz := buzz - 1;
    prnum := 1;

    if fizz == 0 then   
        print("Fizz");
        fizz := 3;
        prnum := 0;
    end if;
    
    if buzz == 0 then
        print("Buzz");
        buzz := 5;
        prnum := 0;
    end if;
    
    if prnum != 0 then
        if dh != '0' then
            print_char(dh);
        end if;
        print_char(dl);
    end if;
    
    dl := dl + 1;
    if dl == ('9' + 1) then
        dl := '0';
        dh := dh + 1;
    end if;
    
    print_nl();
    i := i - 1;
end loop;
```


## Craft Basic

See FizzBuzz/Basic


## Crystal

```mw
1.upto(100) do |v|
  p fizz_buzz(v)
end

def fizz_buzz(value)
  word = ""
  word += "fizz" if value % 3 == 0
  word += "buzz" if value % 5 == 0
  word += value.to_s if word.empty?
  word
end
```

A more natural solution with the string building:

```mw
1.upto(100) do |n|
  case
  when n % 15 == 0
    puts "FizzBuzz" 
  when n % 5 == 0
    puts "Buzz"
  when n % 3 == 0
    puts "Fizz"
  else
    puts n
  end
end
```


## CSS

```
<!DOCTYPE html>
<html lang="en">
<head>
  <style>
    li { list-style-position: inside }

    li:nth-child(3n), li:nth-child(5n) { 
      list-style-type: none 
    }

    li:nth-child(3n)::before{ content:'Fizz' }
    li:nth-child(5n)::after { content:'Buzz' }
  </style>
</head>
<body>
  <ol>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ol>
</body>
</html>
```


## Cubescript

```mw
alias fizzbuzz [
	loop i 100 [
		push i (+ $i 1) [
			cond (! (mod $i 15)) [
				echo FizzBuzz
			] (! (mod $i 3)) [
				echo Fizz
			] (! (mod $i 5)) [
				echo Buzz
			] [
				echo $i
			]
		]
	]
]
```


## D

```mw
import std.stdio, std.algorithm, std.conv;

/// With if-else.
void fizzBuzz(in uint n) {
    foreach (immutable i; 1 .. n + 1)
        if (!(i % 15))
            "FizzBuzz".writeln;
        else if (!(i % 3))
            "Fizz".writeln;
        else if (!(i % 5))
            "Buzz".writeln;
        else
            i.writeln;
}

/// With switch case.
void fizzBuzzSwitch(in uint n) {
    foreach (immutable i; 1 .. n + 1)
        switch (i % 15) {
            case 0:
                "FizzBuzz".writeln;
                break;
            case 3, 6, 9, 12:
                "Fizz".writeln;
                break;
            case 5, 10:
                "Buzz".writeln;
                break;
            default:
                i.writeln;
        }
}

void fizzBuzzSwitch2(in uint n) {
    foreach (immutable i; 1 .. n + 1)
        (i % 15).predSwitch(
        0,       "FizzBuzz",
        3,       "Fizz",
        5,       "Buzz",
        6,       "Fizz",
        9,       "Fizz",
        10,      "Buzz",
        12,      "Fizz",
        /*else*/ i.text).writeln;
}

void main() {
    100.fizzBuzz;
    writeln;
    100.fizzBuzzSwitch;
    writeln;
    100.fizzBuzzSwitch2;
}
```

Alternate version calculating values at compile time:

```mw
import std;

void main()
{
    auto fizzbuzz(in uint i)
    {
        string r;
        if (i % 3 == 0) r ~= "fizz";
        if (i % 5 == 0) r ~= "buzz";
        if (r.length == 0) r ~= i.to!string;
        return r;
    }
    
    enum r = 1.iota(101).map!fizzbuzz;

    r.each!writeln;
}
```


## Dart

```mw
main() {
  for (int i = 1; i <= 100; i++) {
    List<String> out = [];
    if (i % 3 == 0)
      out.add("Fizz");
    if (i % 5 == 0)
      out.add("Buzz");
    print(out.length > 0 ? out.join("") : i);
  }
}
```


## dc

Translation of

:

bc

```mw
[[Fizz]P 1 sw]sF
[[Buzz]P 1 sw]sB
[li p sz]sN
[[
]P]sW
[
 0 sw         [w = 0]sz
 li 3 % 0 =F  [Fizz if 0 == i % 3]sz
 li 5 % 0 =B  [Buzz if 0 == i % 5]sz
 lw 0 =N      [print Number if 0 == w]sz
 lw 1 =W      [print neWline if 1 == w]sz
 li 1 + si    [i += 1]sz
 li 100 !<L   [continue Loop if 100 >= i]sz 
]sL
1 si          [i = 1]sz
0 0 =L        [enter Loop]sz
```

The bc translation written in dc style.

```mw
# dc is stack based, so we use the stack instead of a variable for our 
# current number.

1                       # Number = 1
[[Fizz]n 1 sw]sF        # Prints "Fizz" prevents Number from printing
[[Buzz]n 1 sw]sB        # Prints "Buzz" prevents Number from printing
[dn]sN                  # Prints Number
[
        dd              # Put two extra copies of Number on stack
        0 sw            # w = 0
        3% 0=F          # Fizz if 0 == Number % 3 (destroys 1st copy)
        5% 0=B          # Buzz if 0 == Number % 5 (destroys 2nd copy)
        lw 0=N          # Print Number if 0 == w
        [
]n                      # Print new line
        1+d             # Number += 1 and put extra copy on stack
        100!<L          # Continue Loop if 100 >= Number (destroys copy)
]dsLx                   # Enter Loop
```


## Delphi

```mw
program FizzBuzz;

{$APPTYPE CONSOLE}

uses SysUtils;

var
  i: Integer;
begin
  for i := 1 to 100 do
  begin
    if i mod 15 = 0 then
      Writeln('FizzBuzz')
    else if i mod 3 = 0 then
      Writeln('Fizz')
    else if i mod 5 = 0 then
      Writeln('Buzz')
    else
      Writeln(i);
  end;
end.
```


## DeviousYarn

```mw
each { x range(1 100)
    ?  { divisible(x 3)
        p:'Fizz' }
    ?  { divisible(x 5)
        p:'Buzz' }
    -? { !:divisible(x 3)
        p:x }
    o
}
```


## Draco

```mw
proc nonrec main() void:
    byte i;
    for i from 1 upto 100 do
        if i % 15 = 0 then writeln("FizzBuzz")
        elif i % 5 = 0 then writeln("Buzz")
        elif i % 3 = 0 then writeln("Fizz")
        else writeln(i)
        fi
    od
corp
```


## DUP

FizzBuzz, realized using two different methods for string/character output:

Output to STDOUT via single character output.

```mw
[$$3/%$[]['F,'i,'z,'z,]?\5/%$[]['B,'u,'z,'z,]?*[$.][]?10,]c:    {define function c: mod 3, mod 5 tests, print proper output}
0[$100<][1+c;!]#                                                {loop from 1 to 100}
```

Output to STDOUT, using stored strings and a separately defined string output operator:

```mw
[\[^^>][$;,1+]#%%]⇒P                                       {define operator P: print stored string}
[$$3/%$[][0$"Fizz"P]?\5/%$[][0$"Buzz"P]?*[$.][]?10,]c:     {define function c: mod 3, mod 5 tests, print according output}
0[$100<][1+c;!]#                                           {loop from 1 to 100}
```


## DWScript

```mw
var i : Integer;

for i := 1 to 100 do begin
   if i mod 15 = 0 then
      PrintLn('FizzBuzz')
   else if i mod 3 = 0 then
      PrintLn('Fizz')
   else if i mod 5 = 0 then
      PrintLn('Buzz')
   else PrintLn(i);
end;
```


## Dyalect

```mw
var n = 1

while n < 20 {
    if n % 15 == 0 {
        print("fizzbuzz")
    } else if n % 3 == 0 {
        print("fizz")
    } else if n % 5 == 0 {
        print("buzz")
    } else {
        print(n)
    }

    n = n + 1
}
```

**Output:**

```
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
```


## Déjà Vu

```mw
for i range 1 100:
	if = 0 % i 15:
		"FizzBuzz"
	elseif = 0 % i 3:
		"Fizz"
	elseif = 0 % i 5:
		"Buzz"
	else:
		i
	!print
```


## E

```mw
for i in 1..100 {
   println(switch ([i % 3, i % 5]) {
     match [==0, ==0] { "FizzBuzz" }
     match [==0, _  ] { "Fizz" }
     match [_,   ==0] { "Buzz" }
     match _          { i }
   })
 }
```


## EasyLang

```mw
for i = 1 to 100
   if i mod 15 = 0
      print "FizzBuzz"
   elif i mod 5 = 0
      print "Buzz"
   elif i mod 3 = 0
      print "Fizz"
   else
      print i
   .
.
```


## ECL

```mw
DataRec := RECORD
    STRING  s;
END;

DataRec MakeDataRec(UNSIGNED c) := TRANSFORM
    SELF.s := MAP
        (
            c % 15 = 0  =>  'FizzBuzz',
            c % 3 = 0   =>  'Fizz',
            c % 5 = 0   =>  'Buzz',
            (STRING)c
        );
END;

d := DATASET(100,MakeDataRec(COUNTER));

OUTPUT(d);
```


## Ecstasy

```mw
module FizzBuzz {
    void run() {
        @Inject Console console;
        for (Int x : 1..100) {
            console.print(switch (x % 3, x % 5) {
                case (0, 0): "FizzBuzz";
                case (0, _): "Fizz";
                case (_, 0): "Buzz";
                case (_, _): x.toString();
            });
        }
    }
}
```


## Ed

This script uses POSIX EREs, so should be run with -E flag (at least on GNU ed).

```mw
H
a
100
.
# iota.ed
g/[^0-9]{1,}/s///g
,p
# decimal -> unary
g/^0+([0-9])/s//\1/
g/^9([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiiii/
g/^8([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiii/
g/^7([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiii/
g/^6([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiii/
g/^5([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiii/
g/^4([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiii/
g/^3([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iii/
g/^2([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2ii/
g/^1([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2i/
g/^0([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2/
g/^9([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiiii/
g/^8([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiii/
g/^7([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiii/
g/^6([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiii/
g/^5([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiii/
g/^4([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiii/
g/^3([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iii/
g/^2([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2ii/
g/^1([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2i/
g/^0([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2/
g/^9([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiiii/
g/^8([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiii/
g/^7([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiii/
g/^6([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiii/
g/^5([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiii/
g/^4([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiii/
g/^3([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iii/
g/^2([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2ii/
g/^1([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2i/
g/^0([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2/
g/^9([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiiii/
g/^8([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiii/
g/^7([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiii/
g/^6([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiii/
g/^5([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiii/
g/^4([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiii/
g/^3([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iii/
g/^2([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2ii/
g/^1([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2i/
g/^0([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2/
g/^9([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiiii/
g/^8([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiiii/
g/^7([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiiii/
g/^6([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiiii/
g/^5([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiiii/
g/^4([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iiii/
g/^3([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2iii/
g/^2([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2ii/
g/^1([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2i/
g/^0([0-9]*)(i*)/s//\1\2\2\2\2\2\2\2\2\2\2/
# iota logic
s/\B/\
/g
a

.
y
d
g/i/x\
s/.*/&i/\
-1d\
y
# fizzbuzz
g/^(i{15})+$/s//FizzBuzz/
g/^(i{5})+$/s//Buzz/
g/^(i{3})+$/s//Fizz/
# unary -> decimal (for 0-10000 range)
g/i{9000}(i{0,999})/s//9\1/
g/i{8000}(i{0,999})/s//8\1/
g/i{7000}(i{0,999})/s//7\1/
g/i{6000}(i{0,999})/s//6\1/
g/i{5000}(i{0,999})/s//5\1/
g/i{4000}(i{0,999})/s//4\1/
g/i{3000}(i{0,999})/s//3\1/
g/i{2000}(i{0,999})/s//2\1/
g/i{1000}(i{0,999})/s//1\1/
v/^[0-9]i*$/s/.*/0&/
g/i{900}(i{0,99})/s//9\1/
g/i{800}(i{0,99})/s//8\1/
g/i{700}(i{0,99})/s//7\1/
g/i{600}(i{0,99})/s//6\1/
g/i{500}(i{0,99})/s//5\1/
g/i{400}(i{0,99})/s//4\1/
g/i{300}(i{0,99})/s//3\1/
g/i{200}(i{0,99})/s//2\1/
g/i{100}(i{0,99})/s//1\1/
v/^[0-9]{2}i*$/s/^([0-9])(i*)$/\10\2/
g/i{90}(i{0,9})/s//9\1/
g/i{80}(i{0,9})/s//8\1/
g/i{70}(i{0,9})/s//7\1/
g/i{60}(i{0,9})/s//6\1/
g/i{50}(i{0,9})/s//5\1/
g/i{40}(i{0,9})/s//4\1/
g/i{30}(i{0,9})/s//3\1/
g/i{20}(i{0,9})/s//2\1/
g/i{10}(i{0,9})/s//1\1/
v/^[0-9]{3}i*$/s/^([0-9]{2})(i*)$/\10\2/
g/i{9}/s//9/
g/i{8}/s//8/
g/i{7}/s//7/
g/i{6}/s//6/
g/i{5}/s//5/
g/i{4}/s//4/
g/i{3}/s//3/
g/i{2}/s//2/
g/i{1}/s//1/
v/^[0-9]{4}i*$/s/^([0-9]{3})(i*)$/\10\2/
g/^0+([0-9])/s//\1/
g/0F1zz/s//Fizz/
g/0Buzz/s//Buzz/
,p
Q
```
