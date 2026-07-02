---
title: "Binary search (part 4/6)"
source: https://rosettacode.org/wiki/Binary_search
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/6
---

## Groovy

Both solutions use *sublists* and a tracking offset in preference to "high" and "low".

#### Recursive Solution

```mw
def binSearchR
//define binSearchR closure.
binSearchR = { a, key, offset=0 ->
    def m = n.intdiv(2)
    def n = a.size()
    a.empty \
        ? ["The insertion point is": offset] \
        : a[m] > key \
            ? binSearchR(a[0..<m],key, offset) \
            : a[m] < target \
                ? binSearchR(a[(m + 1)..<n],key, offset + m + 1) \
                : [index: offset + m]
}
```

#### Iterative Solution

```mw
def binSearchI = { aList, target ->
    def a = aList
    def offset = 0
    while (!a.empty) {
        def n = a.size()
        def m = n.intdiv(2)
        if(a[m] > target) {
            a = a[0..<m]
        } else if (a[m] < target) {
            a = a[(m + 1)..<n]
            offset += m + 1
        } else {
            return [index: offset + m]
        }
    }
    return ["insertion point": offset]
}
```

Test:

```mw
def a = [] as Set
def random = new Random()
while (a.size() < 20) { a << random.nextInt(30) }
def source = a.sort()
source[0..-2].eachWithIndex { si, i -> assert si < source[i+1] }

println "${source}"
1.upto(5) {
    target = random.nextInt(10) + (it - 2) * 10
    print "Trial #${it}. Looking for: ${target}"
    def answers = [binSearchR, binSearchI].collect { search ->
        search(source, target)
    }
    assert answers[0] == answers[1]
    println """
    Answer: ${answers[0]}, : ${source[answers[0].values().iterator().next()]}"""
}
```

Output:

```
[1, 2, 5, 8, 9, 10, 11, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29]
Trial #1. Looking for: -9
    Answer: [insertion point:0], : 1
Trial #2. Looking for: 7
    Answer: [insertion point:3], : 8
Trial #3. Looking for: 18
    Answer: [index:9], : 18
Trial #4. Looking for: 29
    Answer: [index:19], : 29
Trial #5. Looking for: 32
    Answer: [insertion point:20], : null
```


## Haskell

### Recursive algorithm

The algorithm itself, parametrized by an "interrogation" predicate *p* in the spirit of the explanation above:

```mw
import Data.Array (Array, Ix, (!), listArray, bounds)

-- BINARY SEARCH --------------------------------------------------------------
bSearch
  :: Integral a
  => (a -> Ordering) -> (a, a) -> Maybe a
bSearch p (low, high)
  | high < low = Nothing
  | otherwise =
    let mid = (low + high) `div` 2
    in case p mid of
         LT -> bSearch p (low, mid - 1)
         GT -> bSearch p (mid + 1, high)
         EQ -> Just mid

-- Application to an array:
bSearchArray
  :: (Ix i, Integral i, Ord e)
  => Array i e -> e -> Maybe i
bSearchArray a x = bSearch (compare x . (a !)) (bounds a)

-- TEST -----------------------------------------------------------------------
axs
  :: (Num i, Ix i)
  => Array i String
axs =
  listArray
    (0, 11)
    [ "alpha"
    , "beta"
    , "delta"
    , "epsilon"
    , "eta"
    , "gamma"
    , "iota"
    , "kappa"
    , "lambda"
    , "mu"
    , "theta"
    , "zeta"
    ]

main :: IO ()
main =
  let e = "mu"
      found = bSearchArray axs e
  in putStrLn $
     '\'' :
     e ++
     case found of
       Nothing -> "' Not found"
       Just x -> "' found at index " ++ show x
```

**Output:**

```
'mu' found at index 9
```

The algorithm uses tail recursion, so the iterative and the recursive approach are identical in Haskell (the compiler will convert recursive calls into jumps).

A common optimisation of recursion is to delegate the main computation to a helper function with simpler type signature. For the option type of the return value, we could also use an Either as an alternative to a Maybe.

```mw
import Data.Array (Array, Ix, (!), listArray, bounds)

-- BINARY SEARCH USING A HELPER FUNCTION WITH A SIMPLER TYPE SIGNATURE
findIndexBinary
  :: Ord a
  => (a -> Ordering) -> Array Int a -> Either String Int
findIndexBinary p axs =
  let go (lo, hi)
        | hi < lo = Left "not found"
        | otherwise =
          let mid = (lo + hi) `div` 2
          in case p (axs ! mid) of
               LT -> go (lo, pred mid)
               GT -> go (succ mid, hi)
               EQ -> Right mid
  in go (bounds axs)

-- TEST ---------------------------------------------------
haystack :: Array Int String
haystack =
  listArray
    (0, 11)
    [ "alpha"
    , "beta"
    , "delta"
    , "epsilon"
    , "eta"
    , "gamma"
    , "iota"
    , "kappa"
    , "lambda"
    , "mu"
    , "theta"
    , "zeta"
    ]

main :: IO ()
main =
  let needle = "lambda"
  in putStrLn $
     '\'' :
     needle ++
     either
       ("' " ++)
       (("' found at index " ++) . show)
       (findIndexBinary (compare needle) haystack)
```

**Output:**

```
'lambda' found at index 8
```

### Iterative algorithm

The iterative algorithm could be written in terms of the **until** function, which takes a predicate **p**, a function **f**, and a seed value **x**.

It returns the result of applying **f** until **p** holds.

```mw
import Data.Array (Array, Ix, (!), listArray, bounds)

-- BINARY SEARCH USING THE ITERATIVE ALGORITHM
findIndexBinary_
  :: Ord a
  => (a -> Ordering) -> Array Int a -> Either String Int
findIndexBinary_ p axs =
  let (lo, hi) =
        until
          (\(lo, hi) -> lo > hi || 0 == hi)
          (\(lo, hi) ->
              let m = quot (lo + hi) 2
              in case p (axs ! m) of
                   LT -> (lo, pred m)
                   GT -> (succ m, hi)
                   EQ -> (m, 0))
          (bounds axs) :: (Int, Int)
  in if 0 /= hi
       then Left "not found"
       else Right lo

-- TEST ---------------------------------------------------
haystack :: Array Int String
haystack =
  listArray
    (0, 11)
    [ "alpha"
    , "beta"
    , "delta"
    , "epsilon"
    , "eta"
    , "gamma"
    , "iota"
    , "kappa"
    , "lambda"
    , "mu"
    , "theta"
    , "zeta"
    ]

main :: IO ()
main =
  let needle = "kappa"
  in putStrLn $
     '\'' :
     needle ++
     either
       ("' " ++)
       (("' found at index " ++) . show)
       (findIndexBinary_ (compare needle) haystack)
```

**Output:**

```
'kappa' found at index 7
```


## Hobbes

```mw
binSearchHelper x = match x with
  | (xs, target, lo, hi) -> if (lo > hi) then -1L else let mid = (lo + hi) / 2 in if (xs[mid] == target) then mid else if (xs[mid] < target) then binSearchHelper((xs, target, mid + 1, hi)) else binSearchHelper((xs, target, lo, mid - 1))

binSearch x = match x with
  | (xs, target) -> binSearchHelper((xs, target, 0L, length(xs) - 1))
```

**Output:**

```
> [binSearch(([1, 3, 5, 7, 9, 11, 13], t)) | t <- [1, 5, 13, 4, 14]]
[0, 2, 6, -1, -1]
```


## HicEst

```mw
REAL :: n=10,  array(n)

   array = NINT( RAN(n) )
   SORT(Vector=array, Sorted=array)
   x = NINT( RAN(n) )

   idx = binarySearch( array, x )
   WRITE(ClipBoard) x, "has position ", idx, "in ", array
 END

FUNCTION binarySearch(A, value)
   REAL :: A(1), value

   low = 1
   high = LEN(A)
   DO i = 1, high
     IF( low > high) THEN
       binarySearch = 0
       RETURN
     ELSE
       mid = INT( (low + high) / 2 )
       IF( A(mid) > value) THEN
         high = mid - 1
       ELSEIF( A(mid) < value ) THEN
         low = mid + 1
       ELSE
         binarySearch = mid
         RETURN
       ENDIF
     ENDIF
   ENDDO
 END
```

```mw
7 has position 9 in 0 0 1 2 3 3 4 6 7 8
5 has position 0 in 0 0 1 2 3 3 4 6 7 8
```


## Hoon

```mw
|=  [arr=(list @ud) x=@ud]
=/  lo=@ud  0
=/  hi=@ud  (dec (lent arr))
|-
?>  (lte lo hi)
=/  mid  (div (add lo hi) 2)
=/  val  (snag mid arr)
?:  (lth x val)  $(hi (dec mid))
?:  (gth x val)  $(lo +(mid))
mid
```


## Icon and Unicon

Only a recursive solution is shown here.

```mw
procedure binsearch(A, target)
    if *A = 0 then fail
    mid := *A/2 + 1
    if target > A[mid] then {
        return mid + binsearch(A[(mid+1):0], target)
        }
    else if target < A[mid] then {
        return binsearch(A[1+:(mid-1)], target)
        }
    return mid
end
```

A program to test this is:

```mw
procedure main(args)
    target := integer(!args) | 3
    every put(A := [], 1 to 18 by 2)

    outList("Searching", A)
    write(target," is ",("at "||binsearch(A, target)) | "not found")
end

procedure outList(prefix, A)
    writes(prefix,": ")
    every writes(!A," ")
    write()
end
```

with some sample runs:

```
->bins 0
Searching: 1 3 5 7 9 11 13 15 17 
0 is not found
->bins 1
Searching: 1 3 5 7 9 11 13 15 17 
1 is at 1
->bins 2
Searching: 1 3 5 7 9 11 13 15 17 
2 is not found
->bins 3
Searching: 1 3 5 7 9 11 13 15 17 
3 is at 2
->bins 16
Searching: 1 3 5 7 9 11 13 15 17 
16 is not found
->bins 17
Searching: 1 3 5 7 9 11 13 15 17 
17 is at 9
->bins 7
Searching: 1 3 5 7 9 11 13 15 17 
7 is at 4
->bins 9
Searching: 1 3 5 7 9 11 13 15 17 
9 is at 5
->bins 10
Searching: 1 3 5 7 9 11 13 15 17 
10 is not found
->
```


## J

J already includes a binary search primitive (`I.`). The following code offers an interface compatible with the requirement of this task, and returns either the index of the element if it has been found or 'Not Found' otherwise:

```mw
bs=. i. 'Not Found'"_^:(-.@-:) I.
```

**Examples:**

```mw
   2 3 5 6 8 10 11 15 19 20 bs 11
6
   2 3 5 6 8 10 11 15 19 20 bs 12
Not Found
```

Direct tacit iterative and recursive versions to compare to other implementations follow:

**Iterative**

```mw
'`X Y L H M'=. ,{{y&{::`''}}&>i.5      NB. Setting mnemonics for boxes (e.g. X=.0&{::)
'l h m'     =. 2 3 4                   NB. more box mnemonics (used for e.g. m})

boxes   =. ;,a:$~3:                    NB. Appending 3 (empty) boxes to the inputs
LowHigh =. (0;#@X) (l,h)} ]            NB. Setting the low and high bounds   
midpoint=. <@(<.@(2%~L+H)) m} ]        NB. Updating the midpoint
case    =. >:@:*@(Y-M{X)               NB. Less=0, equal=1, or greater=2

squeeze =. (<@(_1+M) h} ])`(<@_ l} ])`(<@(1+M) l} ])@.case
return  =. [: M (<@'Not Found' m} ])^:(_~:L)
bs      =. return@(squeeze@midpoint^:(L<:H)^:_)@LowHigh@boxes
```

**Recursive**

```mw
'`X Y L H M'=. ,{{y&{::`''}}&>i.5      NB. Setting mnemonics for boxes (e.g. X=.0&{::)
'l h m'     =. 2 3 4                   NB. more box mnemonics (used for e.g. m})

boxes   =. a:,~;                       NB. Appending 3 (empty) boxes to the inputs
LowHigh =. (0;#@X) (l,h)} ]            NB. Setting the low and high bounds   
midpoint=. <@(<.@(2%~L+H)) m} ]        NB. Updating the midpoint
case    =. >:@:*@(Y-M{X)               NB. Less=0, equal=1, or greater=2

recur   =. (X bs Y;L;(_1+M))`M`(X bs Y;(1+M);H)@.case
bs      =. recur@midpoint`('Not Found'"_)@.(H<L)@boxes :: ([ bs ]; 0; <:@#@[)
```


## Java

**Iterative**

```mw
public class BinarySearchIterative {

    public static int binarySearch(int[] nums, int check) {
        int hi = nums.length - 1;
        int lo = 0;
        while (hi >= lo) {
            int guess = (lo + hi) >>> 1;  // from OpenJDK
            if (nums[guess] > check) {
                hi = guess - 1;
            } else if (nums[guess] < check) {
                lo = guess + 1;
            } else {
                return guess;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] haystack = {1, 5, 6, 7, 8, 11};
        int needle = 5;
        int index = binarySearch(haystack, needle);
        if (index == -1) {
            System.out.println(needle + " is not in the array");
        } else {
            System.out.println(needle + " is at index " + index);
        }
    }
}
```

**Recursive**

```mw
public class BinarySearchRecursive {

    public static int binarySearch(int[] haystack, int needle, int lo, int hi) {
        if (hi < lo) {
            return -1;
        }
        int guess = (hi + lo) / 2;
        if (haystack[guess] > needle) {
            return binarySearch(haystack, needle, lo, guess - 1);
        } else if (haystack[guess] < needle) {
            return binarySearch(haystack, needle, guess + 1, hi);
        }
        return guess;
    }

    public static void main(String[] args) {
        int[] haystack = {1, 5, 6, 7, 8, 11};
        int needle = 5;

        int index = binarySearch(haystack, needle, 0, haystack.length);

        if (index == -1) {
            System.out.println(needle + " is not in the array");
        } else {
            System.out.println(needle + " is at index " + index);
        }
    }
}
```

**Library** When the key is not found, the following functions return `~insertionPoint` (the bitwise complement of the index where the key would be inserted, which is guaranteed to be a negative number).

For arrays:

```mw
import java.util.Arrays;

int index = Arrays.binarySearch(array, thing);
int index = Arrays.binarySearch(array, startIndex, endIndex, thing);

// for objects, also optionally accepts an additional comparator argument:
int index = Arrays.binarySearch(array, thing, comparator);
int index = Arrays.binarySearch(array, startIndex, endIndex, thing, comparator);
```

For Lists:

```mw
import java.util.Collections;

int index = Collections.binarySearch(list, thing);
int index = Collections.binarySearch(list, thing, comparator);
```


## JavaScript

### ES5

Recursive binary search implementation

```mw
function binary_search_recursive(a, value, lo, hi) {
  if (hi < lo) { return null; }

  var mid = Math.floor((lo + hi) / 2);

  if (a[mid] > value) {
    return binary_search_recursive(a, value, lo, mid - 1);
  }
  if (a[mid] < value) {
    return binary_search_recursive(a, value, mid + 1, hi);
  }
  return mid;
}
```

Iterative binary search implementation

```mw
function binary_search_iterative(a, value) {
  var mid, lo = 0,
      hi = a.length - 1;

  while (lo <= hi) {
    mid = Math.floor((lo + hi) / 2);

    if (a[mid] > value) {
      hi = mid - 1;
    } else if (a[mid] < value) {
      lo = mid + 1;
    } else {
      return mid;
    }
  }
  return null;
}
```

### ES6

Recursive and iterative, by composition of pure functions, with tests and output:

```mw
(() => {
    'use strict';

    const main = () => {

        // findRecursive :: a -> [a] -> Either String Int
        const findRecursive = (x, xs) => {
            const go = (lo, hi) => {
                if (hi < lo) {
                    return Left('not found');
                } else {
                    const
                        mid = div(lo + hi, 2),
                        v = xs[mid];
                    return v > x ? (
                        go(lo, mid - 1)
                    ) : v < x ? (
                        go(mid + 1, hi)
                    ) : Right(mid);
                }
            };
            return go(0, xs.length);
        };

        // findRecursive :: a -> [a] -> Either String Int
        const findIter = (x, xs) => {
            const [m, l, h] = until(
                ([mid, lo, hi]) => lo > hi || lo === mid,
                ([mid, lo, hi]) => {
                    const
                        m = div(lo + hi, 2),
                        v = xs[m];
                    return v > x ? [
                        m, lo, m - 1
                    ] : v < x ? [
                        m, m + 1, hi
                    ] : [m, m, hi];
                },
                [div(xs.length / 2), 0, xs.length - 1]
            );
            return l > h ? (
                Left('not found')
            ) : Right(m);
        };

        // TESTS ------------------------------------------

        const
            // (pre-sorted AZ)
            xs = ["alpha", "beta", "delta", "epsilon", "eta", "gamma",
                "iota", "kappa", "lambda", "mu", "nu", "theta", "zeta"
            ];
        return JSON.stringify([
            'Recursive',
            map(x => either(
                    l => "'" + x + "' " + l,
                    r => "'" + x + "' found at index " + r,
                    findRecursive(x, xs)
                ),
                knuthShuffle(['cape'].concat(xs).concat('cairo'))
            ),
            '',
            'Iterative:',
            map(x => either(
                    l => "'" + x + "' " + l,
                    r => "'" + x + "' found at index " + r,
                    findIter(x, xs)
                ),
                knuthShuffle(['cape'].concat(xs).concat('cairo'))
            )
        ], null, 2);
    };

    // GENERIC FUNCTIONS ----------------------------------

    // Left :: a -> Either a b
    const Left = x => ({
        type: 'Either',
        Left: x
    });

    // Right :: b -> Either a b
    const Right = x => ({
        type: 'Either',
        Right: x
    });

    // div :: Int -> Int -> Int
    const div = (x, y) => Math.floor(x / y);

    // either :: (a -> c) -> (b -> c) -> Either a b -> c
    const either = (fl, fr, e) =>
        'Either' === e.type ? (
            undefined !== e.Left ? (
                fl(e.Left)
            ) : fr(e.Right)
        ) : undefined;

    // Abbreviation for quick testing

    // enumFromTo :: (Int, Int) -> [Int]
    const enumFromTo = (m, n) =>
        Array.from({
            length: 1 + n - m
        }, (_, i) => m + i);

    // FOR TESTS

    // knuthShuffle :: [a] -> [a]
    const knuthShuffle = xs => {
        const swapped = (iFrom, iTo, xs) =>
            xs.map(
                (x, i) => iFrom !== i ? (
                    iTo !== i ? x : xs[iFrom]
                ) : xs[iTo]
            );
        return enumFromTo(0, xs.length - 1)
            .reduceRight((a, i) => {
                const iRand = randomRInt(0, i)();
                return i !== iRand ? (
                    swapped(i, iRand, a)
                ) : a;
            }, xs);
    };

    // map :: (a -> b) -> [a] -> [b]
    const map = (f, xs) =>
        (Array.isArray(xs) ? (
            xs
        ) : xs.split('')).map(f);

    // FOR TESTS

    // randomRInt :: Int -> Int -> IO () -> Int
    const randomRInt = (low, high) => () =>
        low + Math.floor(
            (Math.random() * ((high - low) + 1))
        );

    // reverse :: [a] -> [a]
    const reverse = xs =>
        'string' !== typeof xs ? (
            xs.slice(0).reverse()
        ) : xs.split('').reverse().join('');

    // until :: (a -> Bool) -> (a -> a) -> a -> a
    const until = (p, f, x) => {
        let v = x;
        while (!p(v)) v = f(v);
        return v;
    };

    // MAIN ---
    return main();
})();
```

**Output:**

```
[
  "Recursive",
  [
    "'delta' found at index 2",
    "'cairo' not found",
    "'cape' not found",
    "'gamma' found at index 5",
    "'eta' found at index 4",
    "'kappa' found at index 7",
    "'alpha' found at index 0",
    "'mu' found at index 9",
    "'beta' found at index 1",
    "'epsilon' found at index 3",
    "'nu' found at index 10",
    "'iota' found at index 6",
    "'theta' found at index 11",
    "'lambda' found at index 8",
    "'zeta' found at index 12"
  ],
  "",
  "Iterative:",
  [
    "'theta' found at index 11",
    "'kappa' found at index 7",
    "'zeta' found at index 12",
    "'cairo' not found",
    "'epsilon' found at index 3",
    "'beta' found at index 1",
    "'nu' found at index 10",
    "'eta' found at index 4",
    "'alpha' found at index 0",
    "'lambda' found at index 8",
    "'iota' found at index 6",
    "'mu' found at index 9",
    "'gamma' found at index 5",
    "'delta' found at index 2",
    "'cape' not found"
  ]
]
```


## jq

Works with

:

jq

**Also works with gojq, the Go implementation of jq**

jq and gojq both have a binary-search builtin named `bsearch`.

In the following, a parameterized filter for performing a binary search of a sorted JSON array is defined. Specifically, binarySearch(value) will return an index (i.e. offset) of `value` in the array if the array contains the value, and otherwise (-1 - ix), where ix is the insertion point, if the value cannot be found.

binarySearch will always terminate. The inner function is recursive.

```mw
def binarySearch(value):
  # To avoid copying the array, simply pass in the current low and high offsets
  def binarySearch(low; high):
      if (high < low) then (-1 - low)
      else ( (low + high) / 2 | floor) as $mid
           | if (.[$mid] > value) then binarySearch(low; $mid-1)
             elif (.[$mid] < value) then binarySearch($mid+1; high)
             else $mid
             end
      end;
   binarySearch(0; length-1);
```

Example:

```mw
[-1,-1.1,1,1,null,[null]] | binarySearch(1)
```

**Output:**

2


## Jsish

```mw
/**
   Binary search, in Jsish, based on Javascript entry
   Tectonics: jsish -u -time true -verbose true binarySearch.jsi
*/
function binarySearchIterative(haystack, needle) {
    var mid, low = 0, high = haystack.length - 1;

    while (low <= high) {
        mid = Math.floor((low + high) / 2);
        if (haystack[mid] > needle) {
            high = mid - 1;
        } else if (haystack[mid] < needle) {
            low = mid + 1;
        } else {
            return mid;
        }
    }
    return null;
}

/* recursive */
function binarySearchRecursive(haystack, needle, low, high) {
    if (high < low) { return null; }

    var mid = Math.floor((low + high) / 2);

    if (haystack[mid] > needle) {
        return binarySearchRecursive(haystack, needle, low, mid - 1);
    }
    if (haystack[mid] < needle) {
        return binarySearchRecursive(haystack, needle, mid + 1, high);
    }
    return mid;
}

/* Testing and timing */
if (Interp.conf('unitTest') > 0) {
    var arr = [];
    for (var i = -5000; i <= 5000; i++) { arr.push(i); }

    assert(arr.length == 10001);
    assert(binarySearchIterative(arr, 0) == 5000);
    assert(binarySearchRecursive(arr, 0, 0, arr.length - 1) == 5000);

    assert(binarySearchIterative(arr, 5000) == 10000);
    assert(binarySearchRecursive(arr, -5000, 0, arr.length - 1) == 0);

    assert(binarySearchIterative(arr, -5001) == null);

    puts('--Time 100 passes--');
    puts('Iterative:', Util.times(function() { binarySearchIterative(arr, 42); }, 100), 'µs');
    puts('Recursive:', Util.times(function() { binarySearchRecursive(arr, 42, 0, arr.length - 1); }, 100), 'µs');
}
```

**Output:**

```
prompt$ jsish -u -time true -verbose true binarySearch.jsi
Test binarySearch.jsi
CMD: /usr/local/bin/jsish -Iasserts true -IunitTest 1 binarySearch.jsi
OUTPUT: <--Time 100 passes--
Iterative: 25969 µs
Recursive: 40863 µs
>
[PASS] binarySearch.jsi          (165 ms)
```


## Julia

Works with

:

Julia

version 0.6

**Iterative**:

```mw
function binarysearch(lst::Vector{T}, val::T) where T
    low = 1
    high = length(lst)
    while low ≤ high
        mid = (low + high) ÷ 2
        if lst[mid] > val
            high = mid - 1
        elseif lst[mid] < val
            low = mid + 1
        else
            return mid
        end
    end
    return 0
end
```

**Recursive**:

```mw
function binarysearch(lst::Vector{T}, value::T, low=1, high=length(lst)) where T
    if isempty(lst) return 0 end
    if low ≥ high
        if low > high || lst[low] != value
            return 0
        else
            return low
        end
    end
    mid = (low + high) ÷ 2
    if lst[mid] > value
        return binarysearch(lst, value, low, mid-1)
    elseif lst[mid] < value
        return binarysearch(lst, value, mid+1, high)
    else
        return mid
    end
end
```


## K

Recursive:

```mw
bs:{[a;t] 
    if[0=#a; :_n];
    m:_(#a)%2;
    if[t>a@m
        tmp:_f[(m+1) _ a;t]
        :[_n~tmp; :_n; :1+m+tmp]]
    if[t<a@m
        :_f[m#a;t]]
    :m
}

  v:8 30 35 45 49 77 79 82 87 97
  {bs[v;x]}' v
0 1 2 3 4 5 6 7 8 9
```


## Kotlin

```mw
fun <T : Comparable<T>> Array<T>.iterativeBinarySearch(target: T): Int {
    var hi = size - 1
    var lo = 0
    while (hi >= lo) {
        val guess = lo + (hi - lo) / 2
        if (this[guess] > target) hi = guess - 1
        else if (this[guess] < target) lo = guess + 1
        else return guess
    }
    return -1
}

fun <T : Comparable<T>> Array<T>.recursiveBinarySearch(target: T, lo: Int, hi: Int): Int {
    if (hi < lo) return -1

    val guess = (hi + lo) / 2

    return if (this[guess] > target) recursiveBinarySearch(target, lo, guess - 1)
    else if (this[guess] < target) recursiveBinarySearch(target, guess + 1, hi)
    else guess
}

fun main(args: Array<String>) {
    val a = arrayOf(1, 3, 4, 5, 6, 7, 8, 9, 10)
    var target = 6
    var r = a.iterativeBinarySearch(target)
    println(if (r < 0) "$target not found" else "$target found at index $r")
    target = 250
    r = a.iterativeBinarySearch(target)
    println(if (r < 0) "$target not found" else "$target found at index $r")

    target = 6
    r = a.recursiveBinarySearch(target, 0, a.size)
    println(if (r < 0) "$target not found" else "$target found at index $r")
    target = 250
    r = a.recursiveBinarySearch(target, 0, a.size)
    println(if (r < 0) "$target not found" else "$target found at index $r")
}
```

**Output:**

```
6 found at index 4
250 not found
6 found at index 4
250 not found
```


## Lambdatalk

Can be tested in (http://lambdaway.free.fr)[1]

```mw
{def BS 
 {def BS.r {lambda {:a :v :i0 :i1}
  {let { {:a :a} {:v :v} {:i0 :i0} {:i1 :i1}
         {:m {floor {* {+ :i0 :i1} 0.5}}} } 
  {if {<  :i1 :i0}
   then :v is not found
   else {if {> {array.item :a :m} :v}
   then {BS.r :a :v :i0 {- :m 1} }
   else {if {<  {array.item :a :m} :v}
   then {BS.r :a :v {+ :m 1} :i1 }
   else :v is at array[:m] }}}}} }
 {lambda {:a :v}
  {BS.r :a :v 0 {- {array.length :a} 1}} }} 
-> BS

{def A {array 12 14 16 18 20 22 25 27 30}}
-> A = [12,14,16,18,20,22,25,27,30]

{BS {A} -1}  -> -1 is not found
{BS {A} 24}  -> 24 is not found
{BS {A} 25}  -> 25 is at array[6]
{BS {A} 123} -> 123 is not found

{def B {array {serie 1 100000 2}}} 
-> B = [1,3,5,... 99997,99999]

{BS {B} 100}   -> 100 is not found
{BS {B} 12345} -> 12345 is at array[6172]
```


## Logo

```mw
to bsearch :value :a :lower :upper
  if :upper < :lower [output []]
  localmake "mid int (:lower + :upper) / 2
  if item :mid :a > :value [output bsearch :value :a :lower :mid-1]
  if item :mid :a < :value [output bsearch :value :a :mid+1 :upper]
  output :mid
end
```


## LOLCODE

**Iterative**

```mw
HAI 1.2
  CAN HAS STDIO?
  
  VISIBLE "HAI WORLD!!!1!"
  VISIBLE "IMA GONNA SHOW U BINA POUNCE NAO"
 
  I HAS A list ITZ A BUKKIT
  list HAS A index0 ITZ 2
  list HAS A index1 ITZ 3
  list HAS A index2 ITZ 5
  list HAS A index3 ITZ 7
  list HAS A index4 ITZ 8
  list HAS A index5 ITZ 9
  list HAS A index6 ITZ 12
  list HAS A index7 ITZ 20
  
  BTW Method to access list by index number aka: list[index4]
  HOW IZ list access YR indexNameNumber
	FOUND YR list'Z SRS indexNameNumber
  IF U SAY SO
  
  BTW Method to print the array on the same line
  HOW IZ list printList 
  I HAS A allList ITZ ""
	I HAS A indexNameNumber ITZ "index0"
	I HAS A index ITZ 0
	IM IN YR walkingLoop UPPIN YR index TIL BOTH SAEM index AN 8
		indexNameNumber R SMOOSH "index" index MKAY
		allList R SMOOSH allList " " list IZ access YR indexNameNumber MKAY MKAY
	IM OUTTA YR walkingLoop
	FOUND YR allList
  IF U SAY SO
  
  VISIBLE "WE START WIF BUKKIT LIEK DIS: " list IZ printList MKAY
 
  I HAS A target ITZ 12
  VISIBLE "AN TARGET LIEK DIS: " target
  
  VISIBLE "AN NAO 4 MAGI"
  
  HOW IZ I binaPounce YR list AN YR listLength AN YR target 
	I HAS A left ITZ 0
	I HAS A right ITZ DIFF OF listLength AN 1
	IM IN YR whileLoop
		BTW exit while loop when left > right
		DIFFRINT left AN SMALLR OF left AN right
		O RLY?
			YA RLY
				GTFO 
		OIC
		
		I HAS A mid ITZ QUOSHUNT OF SUM OF left AN right AN 2
		I HAS A midIndexname ITZ SMOOSH "index" mid MKAY
		
		BTW if target == list[mid] return mid
		BOTH SAEM target AN list IZ access YR midIndexname MKAY
		O RLY?
			YA RLY
				FOUND YR mid
		OIC
		
		BTW if target < list[mid] right = mid - 1
		DIFFRINT target AN BIGGR OF target AN list IZ access YR midIndexname MKAY
		O RLY?
			YA RLY
				right R DIFF OF mid AN 1
		OIC
		
		BTW if target > list[mid] left = mid + 1
		DIFFRINT target AN SMALLR OF target AN list IZ access YR midIndexname MKAY
		O RLY?
			YA RLY
				left R SUM OF mid AN 1
		OIC
	IM OUTTA YR whileLoop
	
	FOUND YR -1
  IF U SAY SO
  
  BTW call binary search on target here and print the index
  I HAS A targetIndex ITZ I IZ binaPounce YR list AN YR 8 AN YR target MKAY
  VISIBLE "TARGET " target " IZ IN BUKKIT " targetIndex
  
  VISIBLE "WE HAS TEH TARGET!!1!!"
  VISIBLE "I CAN HAS UR CHEEZBURGER NAO?"
  
KTHXBYE
end
```

Output

```
HAI WORLD!!!1!
IMA GONNA SHOW U BINA POUNCE NAO
WE START WIF BUKKIT LIEK DIS:  2 3 5 7 8 9 12 20
AN TARGET LIEK DIS: 12
AN NAO 4 MAGI
TARGET 12 IZ IN BUKKIT 6
WE HAS TEH TARGET!!1!!
I CAN HAS UR CHEEZBURGER NAO?
```


## Lua

**Iterative**

```mw
function binarySearch (list,value)
    local low = 1
    local high = #list
    while low <= high do
        local mid = math.floor((low+high)/2)
        if list[mid] > value then high = mid - 1
        elseif list[mid] < value then low = mid + 1
        else return mid
        end
    end
    return false
end
```

**Recursive**

```mw
function binarySearch (list, value)
    local function search(low, high)
        if low > high then return false end
        local mid = math.floor((low+high)/2)
        if list[mid] > value then return search(low,mid-1) end
        if list[mid] < value then return search(mid+1,high) end
        return mid
    end
    return search(1,#list)
end
```


## M4

```mw
define(`notfound',`-1')dnl
define(`midsearch',`ifelse(defn($1[$4]),$2,$4,
`ifelse(eval(defn($1[$4])>$2),1,`binarysearch($1,$2,$3,decr($4))',`binarysearch($1,$2,incr($4),$5)')')')dnl
define(`binarysearch',`ifelse(eval($4<$3),1,notfound,`midsearch($1,$2,$3,eval(($3+$4)/2),$4)')')dnl
dnl
define(`setrange',`ifelse(`$3',`',$2,`define($1[$2],$3)`'setrange($1,incr($2),shift(shift(shift($@))))')')dnl
define(`asize',decr(setrange(`a',1,1,3,5,7,11,13,17,19,23,29)))dnl
dnl
binarysearch(`a',5,1,asize)
binarysearch(`a',8,1,asize)
```

Output:

```
3
-1
```


## M2000 Interpreter

```mw
\\ binary search
const N=10
Dim A(0 to N-1)
A(0):=1,2,3,4,5,6,8,9,10,11
Print Len(A())=10
Function BinarySearch(&A(), aValue) {
	def long mid, lo, hi
	def boolean ok=False
	let lo=0, hi=Len(A())-1
	While lo<=hi
		mid=(lo+hi)/2
		if A(mid)>aValue Then
			hi=mid-1
		Else.if A(mid)<aValue Then
			lo=mid+1
		Else
			=mid
			ok=True
			exit
		End if
	End While
	if not ok then =-lo-1
}
For i=0 to 12
Rem	Print "Search for value:";i
	where= BinarySearch(&A(), i)
	if where>=0 then
		Print "found i at index: ";where
	else
		where=-where-1
		if where<len(A()) then
			Print "Not found, we can insert it at index: ";where
			Dim A(len(A())+1)   ' redim
			stock A(where)	 keep len(A())-where-1, A(where+1)  'move items up
			A(where)=i  ' insert value
		Else
			Print "Not found, we can append to array at index: ";where
			Dim A(len(A())+1)   ' redim
			A(where)=i  ' insert value
		End If
	end if
next i
Print Len(A())=13
Print A()
```


## MACRO-11

This deals with the overflow problem when calculating `mid` by using a `ROR` (rotate right) instruction to divide by two, which rotates the carry flag back into the result. `ADD` produces a 17-bit result, with the 17th bit in the carry flag.

```mw
        .TITLE  BINRTA
        .MCALL  .TTYOUT,.PRINT,.EXIT
        ; TEST CODE
BINRTA::CLR     R5
1$:     MOV     R5,R0
        ADD     #'0,R0
        .TTYOUT
        MOV     R5,R0
        MOV     #DATA,R1
        MOV     #DATEND,R2
        JSR     PC,BINSRC
        BEQ     2$
        .PRINT  #4$
        BR      3$
2$:     .PRINT  #5$
3$:     INC     R5
        CMP     R5,#^D10
        BLT     1$
        .EXIT
4$:     .ASCII  / NOT/
5$:     .ASCIZ  / FOUND/
        .EVEN

        ; TEST DATA
DATA:   .WORD   1, 2, 3, 5, 7
DATEND  =       . + 2

        ; BINARY SEARCH
        ; INPUT: R0 = VALUE, R1 = LOW PTR, R2 = HIGH PTR
        ; OUTPUT: ZF SET IF VALUE FOUND; R1 = INSERTION POINT
BINSRC: BR      3$
1$:     MOV     R1,R3
        ADD     R2,R3
        ROR     R3
        CMP     (R3),R0
        BGE     2$
        ADD     #2,R3
        MOV     R3,R1
        BR      3$
2$:     SUB     #2,R3
        MOV     R3,R2
3$:     CMP     R2,R1
        BGE     1$
        CMP     (R1),R0
        RTS     PC
        .END    BINRTA
```

**Output:**

```
0 NOT FOUND
1 FOUND
2 FOUND
3 FOUND
4 NOT FOUND
5 FOUND
6 NOT FOUND
7 FOUND
8 NOT FOUND
9 NOT FOUND
```


## Maple

The calculation of "mid" cannot overflow, since Maple uses arbitrary precision integer arithmetic, and the largest list or array is far, far smaller than the effective range of integers.

**Recursive**

```mw
BinarySearch := proc( A, value, low, high )
        description "recursive binary search";
        if high < low then
                FAIL
        else
                local mid := iquo( high + low, 2 );
                if A[ mid ] > value then
                        thisproc( A, value, low, mid - 1 )
                elif A[ mid ] < value then
                        thisproc( A, value, mid + 1, high )
                else
                        mid
                end if
        end if
end proc:
```

**Iterative**

```mw
BinarySearch := proc( A, value )
        description "iterative binary search";
        local low, high;

        low, high := ( lowerbound, upperbound )( A );
        while low <= high do
                local mid := iquo( low + high, 2 );
                if A[ mid ] > value then
                        high := mid - 1
                elif A[ mid ] < value then
                        low := mid + 1
                else
                        return mid
                end if
        end do;
        FAIL
end proc:
```

We can use either lists or Arrays (or Vectors) for the first argument for these.

```mw
> N := 10:
> P := [seq]( ithprime( i ), i = 1 .. N ):
> BinarySearch( P, 12, 1, N ); # recursive version
                                  FAIL

> BinarySearch( P, 13, 1, N ); # recursive version
                                   6

> BinarySearch( Array( P ), 13, 1, N ); # make P into an array
                                   6

> PP := Array( -2 .. 7, P ): # check it works if the array is not 1-based.
> BinarySearch( PP, 13 ); # iterative version
                                   3

> PP[ 3 ];
                                   13
```


## Mathematica / Wolfram Language

**Recursive**

```mw
BinarySearchRecursive[x_List, val_, lo_, hi_] := 
 Module[{mid = lo + Round@((hi - lo)/2)},
  If[hi < lo, Return[-1]];
  Return[ 
   Which[x[[mid]] > val, BinarySearchRecursive[x, val, lo, mid - 1],
    x[[mid]] < val, BinarySearchRecursive[x, val, mid + 1, hi],
    True, mid]
   ];
  ]
```

**Iterative**

```mw
BinarySearch[x_List, val_] := Module[{lo = 1, hi = Length@x, mid},
  While[lo <= hi,
   mid = lo + Round@((hi - lo)/2);
   Which[x[[mid]] > val, hi = mid - 1,
    x[[mid]] < val, lo = mid + 1,
    True, Return[mid]
    ];
   ];
  Return[-1];
  ]
```


## MATLAB

**Recursive**

```mw
function mid = binarySearchRec(list,value,low,high)

    if( high < low )
        mid = [];
        return
    end
    
    mid = floor((low + high)/2);
    
    if( list(mid) > value )
        mid = binarySearchRec(list,value,low,mid-1);
        return
    elseif( list(mid) < value )
        mid = binarySearchRec(list,value,mid+1,high);
        return
    else
        return
    end
        
end
```

Sample Usage:

```mw
>> binarySearchRec([1 2 3 4 5 6 6.5 7 8 9 11 18],6.5,1,numel([1 2 3 4 5 6 6.5 7 8 9 11 18]))

ans =

     7
```

**Iterative**

```mw
function mid = binarySearchIter(list,value)

    low = 1;
    high = numel(list) - 1;
    
    while( low <= high )
        mid = floor((low + high)/2);
    
        if( list(mid) > value )
            high = mid - 1;
        elseif( list(mid) < value )
        	low = mid + 1;
        else
            return
        end
    end
    
    mid = [];
            
end
```

Sample Usage:

```mw
>> binarySearchIter([1 2 3 4 5 6 6.5 7 8 9 11 18],6.5)

ans =

     7
```


## Maxima

```mw
find(L, n) := block([i: 1, j: length(L), k, p],
    if n < L[i] or n > L[j] then 0 else (
        while j - i > 0 do (
            k: quotient(i + j, 2),
            p: L[k],
            if n < p then j: k - 1 elseif n > p then i: k + 1 else i: j: k
        ),
        if n = L[i] then i else 0
    )
)$

".."(a, b) := if a < b then makelist(i, i, a, b) else makelist(i, i, a, b, -1)$
infix("..")$

a: sublist(1 .. 1000, primep)$

find(a, 27);
0
find(a, 421);
82
```


## MAXScript

**Iterative**

```mw
fn binarySearchIterative arr value =
(
    lower = 1
    upper = arr.count
    while lower <= upper do
    (
        mid = (lower + upper) / 2
        if arr[mid] > value then
        (
            upper = mid - 1
        )
        else if arr[mid] < value then
        (
            lower = mid + 1
        )
        else
        (
            return mid
        )
    )
    -1
)

arr = #(1, 3, 4, 5, 6, 7, 8, 9, 10)
result = binarySearchIterative arr 6
```

**Recursive**

```mw
fn binarySearchRecursive arr value lower upper =
(
    if lower == upper then
    (
        if arr[lower] == value then
        (
            return lower
        )
        else
        (
            return -1
        )
    )
    mid = (lower + upper) / 2
    if arr[mid] > value then
    (
        return binarySearchRecursive arr value lower (mid-1)
    )
    else if arr[mid] < value then
    (
        return binarySearchRecursive arr value (mid+1) upper
    )
    else
    (
        return mid
    )
)

arr = #(1, 3, 4, 5, 6, 7, 8, 9, 10)
result = binarySearchRecursive arr 6 1 arr.count
```


## Modula-2

Translation of

:

C

Works with

:

ADW Modula-2

version any (Compile with the linker option

Console Application

).

```mw
MODULE BinarySearch;

FROM STextIO IMPORT 
  WriteLn, WriteString;
FROM SWholeIO IMPORT 
  WriteInt;

TYPE
  TArray = ARRAY [0 .. 9] OF INTEGER;

CONST 
  A = TArray{-31, 0, 1, 2, 2, 4, 65, 83, 99, 782}; (* Sorted data *)

VAR  
  X: INTEGER;

PROCEDURE DoBinarySearch(A: ARRAY OF INTEGER; X: INTEGER): INTEGER;
VAR
  L, H, M: INTEGER;
BEGIN
  L := 0; H := HIGH(A);
  WHILE L <= H DO
    M := L + (H - L) / 2;
    IF A[M] < X THEN 
      L := M + 1
    ELSIF A[M] > X THEN 
      H := M - 1
    ELSE 
      RETURN M
    END
  END;
  RETURN -1
END DoBinarySearch;
     
PROCEDURE DoBinarySearchRec(A: ARRAY OF INTEGER; X, L, H: INTEGER): INTEGER;
VAR
  M: INTEGER;
BEGIN
  IF H < L THEN
    RETURN -1
  END;
  M := L + (H - L) / 2;
  IF A[M] > X THEN 
    RETURN DoBinarySearchRec(A, X, L, M - 1)
  ELSIF A[M] < X THEN 
    RETURN DoBinarySearchRec(A, X, M + 1, H)
  ELSE 
    RETURN M
  END
END DoBinarySearchRec;

PROCEDURE WriteResult(X, IndX: INTEGER);
BEGIN
  WriteInt(X, 1);
  IF IndX >= 0 THEN     
    WriteString(" is at index ");
    WriteInt(IndX, 1);
    WriteString(".")   
  ELSE
    WriteString(" is not found.")
  END;  
  WriteLn
END WriteResult;

BEGIN
  X := 2;
  WriteResult(X, DoBinarySearch(A, X));
  X := 5;
  WriteResult(X, DoBinarySearchRec(A, X, 0, HIGH(A)));
END BinarySearch.
```

**Output:**

```
2 is at index 4.
5 is not found.
```


## MiniScript

**Recursive:**

```mw
binarySearch = function(A, value, low, high)
    if high < low then return null
    mid = floor((low + high) / 2)
    if A[mid] > value then return binarySearch(A, value, low, mid-1)
    if A[mid] < value then return binarySearch(A, value, mid+1, high)
    return mid
end function
```

**Iterative:**

```mw
binarySearch = function(A, value)
    low = 0
    high = A.len - 1
    while true
        if high < low then return null
        mid = floor((low + high) / 2)
        if A[mid] > value then
            high = mid - 1
        else if A[mid] < value then
            low = mid + 1
        else
            return mid
        end if
    end while
end function
```


## N/t/roff

Works with

:

GNU TROFF

version 1.22.2

```mw
.de end
..
.de array
.	nr \\$1.c 0 1
.	de \\$1.push end
.		nr \\$1..\\\\n+[\\$1.c] \\\\$1
.	end
.	de \\$1.pushln end
.		if \\\\n(.$>0 .\\$1.push \\\\$1
.		if \\\\n(.$>1 \{ \
.			shift
.			\\$1.pushln \\\\$@
\}
.	end
..
.
.de binarysearch
.	nr min 1
.	nr max \\n[\\$1.c]
.	nr guess \\n[min]+\\n[max]/2
.	while !\\n[\\$1..\\n[guess]]=\\$2 \{ \
.		ie \\n[\\$1..\\n[guess]]<\\$2 .nr min \\n[guess]+1
.		el .nr max \\n[guess]-1
.
.		if \\n[min]>\\n[max] \{
.			nr guess 0
.			break
.		\}
.		nr guess \\n[min]+\\n[max]/2
.	\}
\\n[guess]
..
.array a
.a.pushln 1 4 9 16 25 36 49 64 81 100 121 144
.binarysearch a 100
.br
.ie \n[guess]=0 The item \fBdoesn't exist\fP.
.el The item \fBdoes exist\fP.
```


## Nim

**Library**

```mw
import algorithm

let s = @[2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,25,27,30]
echo binarySearch(s, 10)
```

**Iterative** (from the standard library)

```mw
proc binarySearch[T](a: openArray[T], key: T): int =
  var b = len(a)
  while result < b:
    var mid = (result + b) div 2
    if a[mid] < key: result = mid + 1
    else: b = mid
  if result >= len(a) or a[result] != key: result = -1
```


## Niue

**Library**

```mw
1 2 3 4 5
3 bsearch . ( => 2 )
5 bsearch . ( => 0 )
'sam 'tom 'kenny ( must be sorted before calling bsearch ) 
sort
.s ( => kenny sam tom )
'sam bsearch . ( => 1 )
'tom bsearch . ( => 0 )
'kenny bsearch . ( => 2 )
'tony bsearch . ( => -1)
```


## Oberon-2

Translation of

:

Pascal

```mw
MODULE BS;

  IMPORT Out;
    
  VAR
    List:ARRAY 10 OF REAL;
    
  PROCEDURE Init(VAR List:ARRAY OF REAL);
  BEGIN
    List[0] := -31; List[1] := 0; List[2] := 1; List[3] := 2;
    List[4] := 2; List[5] := 4; List[6] := 65; List[7] := 83;
    List[8] := 99; List[9] := 782;
  END Init;
  
  PROCEDURE BinarySearch(List:ARRAY OF REAL;Element:REAL):LONGINT;
    VAR
      L,M,H:LONGINT;
  BEGIN
    L := 0;
    H := LEN(List)-1;
    WHILE L <= H DO
      M := (L + H) DIV 2;
      IF List[M] > Element THEN
	H := M - 1;
      ELSIF List[M] < Element THEN
	L := M + 1;
      ELSE
	RETURN M;
      END;
    END;
    RETURN -1;
  END BinarySearch;

  PROCEDURE RBinarySearch(VAR List:ARRAY OF REAL;Element:REAL;L,R:LONGINT):LONGINT;
    VAR
      M:LONGINT;
  BEGIN
    IF R < L THEN RETURN -1 END;
    M := (L + R) DIV 2;
    IF Element = List[M] THEN
      RETURN M
    ELSIF Element < List[M] THEN
      RETURN RBinarySearch(List, Element, L, R-1)
    ELSE
      RETURN RBinarySearch(List, Element, M-1, R)
    END;
  END RBinarySearch;

BEGIN
  Init(List);
  Out.Int(BinarySearch(List, 2), 0); Out.Ln;
  Out.Int(RBinarySearch(List, 65, 0, LEN(List)-1),0); Out.Ln;
END BS.
```


## Objeck

**Iterative**

```mw
use Structure;

bundle Default {
  class BinarySearch {
    function : Main(args : String[]) ~ Nil {
      values := [-1, 3, 8, 13, 22];
      DoBinarySearch(values, 13)->PrintLine();
      DoBinarySearch(values, 7)->PrintLine();
    }
    
    function : native : DoBinarySearch(values : Int[], value : Int) ~ Int {
      low := 0;
      high := values->Size() - 1;

      while(low <= high) {
        mid := (low + high) / 2;
        
        if(values[mid] > value) {
          high := mid - 1;
        }
        else if(values[mid] < value) {
          low := mid + 1;
        }
        else {
          return mid;
        };
      };

      return -1;
    }
  }
}
```


## Objective-C

**Iterative**

```mw
#import <Foundation/Foundation.h>

@interface NSArray (BinarySearch)
// Requires all elements of this array to implement a -compare: method which
// returns a NSComparisonResult for comparison.
// Returns NSNotFound when not found
- (NSInteger) binarySearch:(id)key;
@end

@implementation NSArray (BinarySearch)
- (NSInteger) binarySearch:(id)key {
  NSInteger lo = 0;
  NSInteger hi = [self count] - 1;
  while (lo <= hi) {
    NSInteger mid = lo + (hi - lo) / 2;
    id midVal = self[mid];
    switch ([midVal compare:key]) {
    case NSOrderedAscending:
      lo = mid + 1;
      break;
    case NSOrderedDescending:
      hi = mid - 1;
      break;
    case NSOrderedSame:
      return mid;
    }
  }
  return NSNotFound;
}
@end

int main()
{
  @autoreleasepool {

    NSArray *a = @[@1, @3, @4, @5, @6, @7, @8, @9, @10];
    NSLog(@"6 is at position %d", [a binarySearch:@6]); // prints 4

  }
  return 0;
}
```

**Recursive**

```mw
#import <Foundation/Foundation.h>

@interface NSArray (BinarySearchRecursive)
// Requires all elements of this array to implement a -compare: method which
// returns a NSComparisonResult for comparison.
// Returns NSNotFound when not found
- (NSInteger) binarySearch:(id)key inRange:(NSRange)range;
@end

@implementation NSArray (BinarySearchRecursive)
- (NSInteger) binarySearch:(id)key inRange:(NSRange)range {
  if (range.length == 0)
    return NSNotFound;
  NSInteger mid = range.location + range.length / 2;
  id midVal = self[mid];
  switch ([midVal compare:key]) {
  case NSOrderedAscending:
    return [self binarySearch:key
                      inRange:NSMakeRange(mid + 1, NSMaxRange(range) - (mid + 1))];
  case NSOrderedDescending:
    return [self binarySearch:key
                      inRange:NSMakeRange(range.location, mid - range.location)];
  default:
    return mid;
  }
}
@end

int main()
{
  @autoreleasepool {

    NSArray *a = @[@1, @3, @4, @5, @6, @7, @8, @9, @10];
    NSLog(@"6 is at position %d", [a binarySearch:@6]); // prints 4

  }
  return 0;
}
```

**Library**

Works with

:

Mac OS X

version 10.6+

```mw
#import <Foundation/Foundation.h>

int main()
{
  @autoreleasepool {

    NSArray *a = @[@1, @3, @4, @5, @6, @7, @8, @9, @10];
    NSLog(@"6 is at position %lu", [a indexOfObject:@6
                                      inSortedRange:NSMakeRange(0, [a count])
                                            options:0
                                    usingComparator:^(id x, id y){ return [x compare: y]; }]); // prints 4

  }
  return 0;
}
```

Using Core Foundation (part of Cocoa, all versions):

```mw
#import <Foundation/Foundation.h>

CFComparisonResult myComparator(const void *x, const void *y, void *context) {
  return [(__bridge id)x compare:(__bridge id)y];
}

int main(int argc, const char *argv[]) {
  @autoreleasepool {

    NSArray *a = @[@1, @3, @4, @5, @6, @7, @8, @9, @10];
    NSLog(@"6 is at position %ld", CFArrayBSearchValues((__bridge CFArrayRef)a,
                                                        CFRangeMake(0, [a count]),
                                                        (__bridge const void *)@6,
                                                        myComparator,
                                                        NULL)); // prints 4

  }
  return 0;
}
```


## OCaml

**Recursive**

```mw
let rec binary_search a value low high =
  if high = low then
    if a.(low) = value then
      low
    else
      raise Not_found
  else let mid = (low + high) / 2 in
    if a.(mid) > value then
      binary_search a value low (mid - 1)
    else if a.(mid) < value then
      binary_search a value (mid + 1) high
    else
      mid
```

Output:

```
# let arr = [|1; 3; 4; 5; 6; 7; 8; 9; 10|];;
val arr : int array = [|1; 3; 4; 5; 6; 7; 8; 9; 10|]
# binary_search arr 6 0 (Array.length arr - 1);;
- : int = 4
# binary_search arr 2 0 (Array.length arr - 1);;
Exception: Not_found.
```

OCaml supports proper tail-recursion; so this is effectively the same as iteration.


## Octave

**Recursive**

```mw
function i = binsearch_r(array, val, low, high)
  if ( high < low )
    i = 0;
  else
    mid = floor((low + high) / 2);
    if ( array(mid) > val )
      i = binsearch_r(array, val, low, mid-1);
    elseif ( array(mid) < val ) 
      i = binsearch_r(array, val, mid+1, high);
    else
      i = mid;
    endif
  endif
endfunction
```

**Iterative**

```mw
function i = binsearch(array, value)
  low = 1;
  high = numel(array);
  i = 0;
  while ( low <= high )
    mid = floor((low + high)/2);
    if (array(mid) > value) 
      high = mid - 1;
    elseif (array(mid) < value)
      low = mid + 1;
    else
      i = mid;
      return;
    endif
  endwhile
endfunction
```

**Example of using**

```mw
r = sort(discrete_rnd(10, [1:10], ones(10,1)/10));
disp(r);
binsearch_r(r, 5, 1, numel(r))
binsearch(r, 5)
```
