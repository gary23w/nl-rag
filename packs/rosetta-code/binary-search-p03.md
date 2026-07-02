---
title: "Binary search (part 3/6)"
source: https://rosettacode.org/wiki/Binary_search
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/6
---

## C

**Recursive**

```mw
namespace Search {
  using System;

  public static partial class Extensions {
    /// <summary>Use Binary Search to find index of GLB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of GLB for value</returns>
    public static int RecursiveBinarySearchForGLB<T>(this T[] entries, T value)
      where T : IComparable {
      return entries.RecursiveBinarySearchForGLB(value, 0, entries.Length - 1);
    }

    /// <summary>Use Binary Search to find index of GLB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <param name="left">leftmost index to search</param>
    /// <param name="right">rightmost index to search</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of GLB for value</returns>
    public static int RecursiveBinarySearchForGLB<T>(this T[] entries, T value, int left, int right)
      where T : IComparable {
      if (left <= right) {
        var middle = left + (right - left) / 2;
        return entries[middle].CompareTo(value) < 0 ?
          entries.RecursiveBinarySearchForGLB(value, middle + 1, right) :
          entries.RecursiveBinarySearchForGLB(value, left, middle - 1);
      }

      //[Assert]left == right + 1
      // GLB: entries[right] < value && value <= entries[right + 1]
      return right;
    }

    /// <summary>Use Binary Search to find index of LUB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of LUB for value</returns>
    public static int RecursiveBinarySearchForLUB<T>(this T[] entries, T value)
      where T : IComparable {
      return entries.RecursiveBinarySearchForLUB(value, 0, entries.Length - 1);
    }

    /// <summary>Use Binary Search to find index of LUB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <param name="left">leftmost index to search</param>
    /// <param name="right">rightmost index to search</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of LUB for value</returns>
    public static int RecursiveBinarySearchForLUB<T>(this T[] entries, T value, int left, int right)
      where T : IComparable {
      if (left <= right) {
        var middle = left + (right - left) / 2;
        return entries[middle].CompareTo(value) <= 0 ?
          entries.RecursiveBinarySearchForLUB(value, middle + 1, right) :
          entries.RecursiveBinarySearchForLUB(value, left, middle - 1);
      }

      //[Assert]left == right + 1
      // LUB: entries[left] > value && value >= entries[left - 1]
      return left;
    }
  }
}
```

**Iterative**

```mw
namespace Search {
  using System;

  public static partial class Extensions {
    /// <summary>Use Binary Search to find index of GLB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of GLB for value</returns>
    public static int BinarySearchForGLB<T>(this T[] entries, T value)
      where T : IComparable {
      return entries.BinarySearchForGLB(value, 0, entries.Length - 1);
    }

    /// <summary>Use Binary Search to find index of GLB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <param name="left">leftmost index to search</param>
    /// <param name="right">rightmost index to search</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of GLB for value</returns>
    public static int BinarySearchForGLB<T>(this T[] entries, T value, int left, int right)
      where T : IComparable {
      while (left <= right) {
        var middle = left + (right - left) / 2;
        if (entries[middle].CompareTo(value) < 0)
          left = middle + 1;
        else
          right = middle - 1;
      }

      //[Assert]left == right + 1
      // GLB: entries[right] < value && value <= entries[right + 1]
      return right;
    }

    /// <summary>Use Binary Search to find index of LUB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of LUB for value</returns>
    public static int BinarySearchForLUB<T>(this T[] entries, T value)
      where T : IComparable {
      return entries.BinarySearchForLUB(value, 0, entries.Length - 1);
    }

    /// <summary>Use Binary Search to find index of LUB for value</summary>
    /// <typeparam name="T">type of entries and value</typeparam>
    /// <param name="entries">array of entries</param>
    /// <param name="value">search value</param>
    /// <param name="left">leftmost index to search</param>
    /// <param name="right">rightmost index to search</param>
    /// <remarks>entries must be in ascending order</remarks>
    /// <returns>index into entries of LUB for value</returns>
    public static int BinarySearchForLUB<T>(this T[] entries, T value, int left, int right)
      where T : IComparable {
      while (left <= right) {
        var middle = left + (right - left) / 2;
        if (entries[middle].CompareTo(value) <= 0)
          left = middle + 1;
        else
          right = middle - 1;
      }

      //[Assert]left == right + 1
      // LUB: entries[left] > value && value >= entries[left - 1]
      return left;
    }
  }
}
```

**Example**

```mw
//#define UseRecursiveSearch

using System;
using Search;

class Program {
  static readonly int[][] tests = {
    new int[] { },
    new int[] { 2 },
    new int[] { 2, 2 },
    new int[] { 2, 2, 2, 2 },
    new int[] { 3, 3, 4, 4 },
    new int[] { 0, 1, 3, 3, 4, 4 },
    new int[] { 0, 1, 2, 2, 2, 3, 3, 4, 4},
    new int[] { 0, 1, 1, 2, 2, 2, 3, 3, 4, 4 },
    new int[] { 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4 },
    new int[] { 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4 },
    new int[] { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4 },
  };

  static void Main(string[] args) {
    var index = 0;
    foreach (var test in tests) {
      var join = String.Join(" ", test);
      Console.WriteLine($"test[{index}]: {join}");
#if UseRecursiveSearch
      var glb = test.RecursiveBinarySearchForGLB(2);
      var lub = test.RecursiveBinarySearchForLUB(2);
#else
      var glb = test.BinarySearchForGLB(2);
      var lub = test.BinarySearchForLUB(2);
#endif
      Console.WriteLine($"glb = {glb}");
      Console.WriteLine($"lub = {lub}");

      index++;
    }
#if DEBUG
    Console.Write("Press Enter");
    Console.ReadLine();
#endif
  }
}
```

**Output**

```
test[0]:
glb = -1
lub = 0
test[1]: 2
glb = -1
lub = 1
test[2]: 2 2
glb = -1
lub = 2
test[3]: 2 2 2 2
glb = -1
lub = 4
test[4]: 3 3 4 4
glb = -1
lub = 0
test[5]: 0 1 3 3 4 4
glb = 1
lub = 2
test[6]: 0 1 2 2 2 3 3 4 4
glb = 1
lub = 5
test[7]: 0 1 1 2 2 2 3 3 4 4
glb = 2
lub = 6
test[8]: 0 1 1 1 1 2 2 3 3 4 4
glb = 4
lub = 7
test[9]: 0 1 1 1 1 2 2 2 2 2 2 2 3 3 4 4
glb = 4
lub = 12
test[10]: 0 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 3 3 4 4
glb = 13
lub = 21
```


## C++

**Recursive**

```mw
template <class T> int binsearch(const T array[], int low, int high, T value) {
    if (high < low) {
        return -1;
    }
    auto mid = (low + high) / 2;
    if (value < array[mid]) {
        return binsearch(array, low, mid - 1, value);
    } else if (value > array[mid]) {
        return binsearch(array, mid + 1, high, value);
    }
    return mid;
}

#include <iostream>
int main()
{
  int array[] = {2, 3, 5, 6, 8};
  int result1 = binsearch(array, 0, sizeof(array)/sizeof(int), 4),
      result2 = binsearch(array, 0, sizeof(array)/sizeof(int), 8);
  if (result1 == -1) std::cout << "4 not found!" << std::endl;
  else std::cout << "4 found at " << result1 << std::endl;
  if (result2 == -1) std::cout << "8 not found!" << std::endl;
  else std::cout << "8 found at " << result2 << std::endl;

  return 0;
}
```

**Iterative**

```mw
template <class T>
int binSearch(const T arr[], int len, T what) {
  int low = 0;
  int high = len - 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    if (arr[mid] > what)
      high = mid - 1;
    else if (arr[mid] < what)
      low = mid + 1;
    else
      return mid;
  }
  return -1; // indicate not found 
}
```

**Library**

C++'s Standard Template Library has four functions for binary search, depending on what information you want to get. They all need

```mw
#include <algorithm>
```

The `lower_bound()` function returns an iterator to the first position where a value could be inserted without violating the order; i.e. the first element equal to the element you want, or the place where it would be inserted.

```mw
int *ptr = std::lower_bound(array, array+len, what); // a custom comparator can be given as fourth arg
```

The `upper_bound()` function returns an iterator to the last position where a value could be inserted without violating the order; i.e. one past the last element equal to the element you want, or the place where it would be inserted.

```mw
int *ptr = std::upper_bound(array, array+len, what); // a custom comparator can be given as fourth arg
```

The `equal_range()` function returns a pair of the results of `lower_bound()` and `upper_bound()`.

```mw
std::pair<int *, int *> bounds = std::equal_range(array, array+len, what); // a custom comparator can be given as fourth arg
```

Note that the difference between the bounds is the number of elements equal to the element you want.

The `binary_search()` function returns true or false for whether an element equal to the one you want exists in the array. It does not give you any information as to where it is.

```mw
bool found = std::binary_search(array, array+len, what); // a custom comparator can be given as fourth arg
```


## Chapel

**iterative** -- almost a direct translation of the pseudocode

```mw
proc binsearch(A : [], value) 
{
        var low = A.domain.dim(0).low;
        var high = A.domain.dim(0).high;
        while (low <= high) 
        {
                var mid = (low + high) / 2;

                if A(mid) > value then
                        high = mid - 1;
                else if A(mid) < value then
                        low = mid + 1;
                else
                        return mid;
        }
        return 0;
}

writeln(binsearch([3, 4, 6, 9, 11], 9));
```

**Output:**

```
4
```


## Clojure

**Recursive**

```mw
(defn bsearch
  ([coll t]
    (bsearch coll 0 (dec (count coll)) t))
  ([coll l u t]
    (if (> l u) -1
      (let [m (quot (+ l u) 2) mth (nth coll m)]
        (cond
          ; the middle element is greater than t
          ; so search the lower half
          (> mth t) (recur coll l (dec m) t)
          ; the middle element is less than t
          ; so search the upper half
          (< mth t) (recur coll (inc m) u t)
          ; we've found our target
          ; so return its index
          (= mth t) m)))))
```


## CLU

```mw
% Binary search in an array
% If the item is found, returns `true' and the index;
% if the item is not found, returns `false' and the leftmost insertion point
% The datatype must support the < and > operators.
binary_search = proc [T: type] (a: array[T], val: T) returns (bool, int)
                where T has lt: proctype (T,T) returns (bool),
                      T has gt: proctype (T,T) returns (bool)
    low: int := array[T]$low(a)
    high: int := array[T]$high(a)
    
    while low <= high do
        mid: int := low + (high - low) / 2
        if a[mid] > val then 
            high := mid - 1
        elseif a[mid] < val then 
            low := mid + 1
        else
            return (true, mid)
        end
    end
    return (false, low)
end binary_search

% Test the binary search on an array 
start_up = proc ()
    po: stream := stream$primary_output()
    
    % primes up to 20 (note that arrays are 1-indexed by default)
    primes: array[int] := array[int]$[2,3,5,7,11,13,17,19]
    
    % binary search for each number from 1 to 20
    for n: int in int$from_to(1,20) do
        i: int
        found: bool
        found, i := binary_search[int](primes, n)
        
        if found then
            stream$putl(po, int$unparse(n) 
                            || " found at location " 
                            || int$unparse(i));
        else
            stream$putl(po, int$unparse(n) 
                            || " not found, would be inserted at location "
                            || int$unparse(i));
        end
    end
end start_up
```

**Output:**

```
1 not found, would be inserted at location 1
2 found at location 1
3 found at location 2
4 not found, would be inserted at location 3
5 found at location 3
6 not found, would be inserted at location 4
7 found at location 4
8 not found, would be inserted at location 5
9 not found, would be inserted at location 5
10 not found, would be inserted at location 5
11 found at location 5
12 not found, would be inserted at location 6
13 found at location 6
14 not found, would be inserted at location 7
15 not found, would be inserted at location 7
16 not found, would be inserted at location 7
17 found at location 7
18 not found, would be inserted at location 8
19 found at location 8
20 not found, would be inserted at location 9
```


## COBOL

COBOL's `SEARCH ALL` statement is implemented as a binary search on most implementations.

```mw
        >>SOURCE FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. binary-search.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  nums-area                           VALUE "01040612184356".
    03  nums                            PIC 9(2)
                                        OCCURS 7 TIMES
                                        ASCENDING KEY nums
                                        INDEXED BY nums-idx.
PROCEDURE DIVISION.
    SEARCH ALL nums
        WHEN nums (nums-idx) = 4
            DISPLAY "Found 4 at index " nums-idx
    END-SEARCH
    .
END PROGRAM binary-search.
```


## CoffeeScript

**Recursive**

```mw
binarySearch = (xs, x) ->
  do recurse = (low = 0, high = xs.length - 1) ->
    mid = Math.floor (low + high) / 2
    switch
      when high < low then NaN
      when xs[mid] > x then recurse low, mid - 1
      when xs[mid] < x then recurse mid + 1, high
      else mid
```

**Iterative**

```mw
binarySearch = (xs, x) ->
  [low, high] = [0, xs.length - 1]
  while low <= high
    mid = Math.floor (low + high) / 2
    switch
      when xs[mid] > x then high = mid - 1
      when xs[mid] < x then low = mid + 1
      else return mid
  NaN
```

**Test**

```mw
do (n = 12) ->
  odds = (it for it in [1..n] by 2)
  result = (it for it in \
    (binarySearch odds, it for it in [0..n]) \
    when not isNaN it)
  console.assert "#{result}" is "#{[0...odds.length]}"
  console.log "#{odds} are odd natural numbers"
  console.log "#{it} is ordinal of #{odds[it]}" for it in result
```

Output:

```
1,3,5,7,9,11 are odd natural numbers"
0 is ordinal of 1
1 is ordinal of 3
2 is ordinal of 5
3 is ordinal of 7
4 is ordinal of 9
5 is ordinal of 11
```


## Common Lisp

**Iterative**

```mw
(defun binary-search (value array)
  (let ((low 0)
        (high (1- (length array))))
    
    (do () ((< high low) nil)
      (let ((middle (floor (+ low high) 2)))
        
        (cond ((> (aref array middle) value)
               (setf high (1- middle)))
              
              ((< (aref array middle) value)
               (setf low (1+ middle)))
              
              (t (return middle)))))))
```

**Recursive**

```mw
(defun binary-search (value array &optional (low 0) (high (1- (length array))))
  (if (< high low)
      nil
      (let ((middle (floor (+ low high) 2)))
        
        (cond ((> (aref array middle) value)
               (binary-search value array low (1- middle)))
              
              ((< (aref array middle) value)
               (binary-search value array (1+ middle) high))
              
              (t middle)))))
```


## Crystal

**Recursive**

```mw
class Array
  def binary_search(val, low = 0, high = (size - 1))
    return nil if high < low
    #mid = (low + high) >> 1
    mid = low + ((high - low) >> 1)
    case val <=> self[mid]
      when -1
        binary_search(val, low, mid - 1)
      when 1
        binary_search(val, mid + 1, high)
      else mid
    end
  end
end

ary = [0,1,4,5,6,7,8,9,12,26,45,67,78,90,98,123,211,234,456,769,865,2345,3215,14345,24324]

[0, 42, 45, 24324, 99999].each do |val|
  i = ary.binary_search(val)
  if i
    puts "found #{val} at index #{i}: #{ary[i]}"
  else
    puts "#{val} not found in array"
  end
end
```

**Iterative**

```mw
class Array
  def binary_search_iterative(val)
    low, high = 0, size - 1
    while low <= high
      #mid = (low + high) >> 1
      mid = low + ((high - low) >> 1)
      case val <=> self[mid]
        when 1
          low = mid + 1
        when -1
          high = mid - 1
        else
          return mid
      end
    end
    nil
  end
end

ary = [0,1,4,5,6,7,8,9,12,26,45,67,78,90,98,123,211,234,456,769,865,2345,3215,14345,24324]

[0, 42, 45, 24324, 99999].each do |val|
  i = ary.binary_search_iterative(val)
  if i
    puts "found #{val} at index #{i}: #{ary[i]}"
  else
    puts "#{val} not found in array"
  end
end
```

**Output:**

```
found 0 at index 0: 0
42 not found in array
found 45 at index 10: 45
found 24324 at index 24: 24324
99999 not found in array
```


## D

```mw
import std.stdio, std.array, std.range, std.traits;

/// Recursive.
bool binarySearch(R, T)(/*in*/ R data, in T x) pure nothrow @nogc
if (isRandomAccessRange!R && is(Unqual!T == Unqual!(ElementType!R))) {
    if (data.empty)
        return false;
    immutable i = data.length / 2;
    immutable mid = data[i];
    if (mid > x)
        return data[0 .. i].binarySearch(x);
    if (mid < x)
        return data[i + 1 .. $].binarySearch(x);
    return true;
}

/// Iterative.
bool binarySearchIt(R, T)(/*in*/ R data, in T x) pure nothrow @nogc
if (isRandomAccessRange!R && is(Unqual!T == Unqual!(ElementType!R))) {
    while (!data.empty) {
        immutable i = data.length / 2;
        immutable mid = data[i];
        if (mid > x)
            data = data[0 .. i];
        else if (mid < x)
            data = data[i + 1 .. $];
        else
            return true;
    }
    return false;
}

void main() {
    /*const*/ auto items = [2, 4, 6, 8, 9].assumeSorted;
    foreach (const x; [1, 8, 10, 9, 5, 2])
        writefln("%2d %5s %5s %5s", x,
                 items.binarySearch(x),
                 items.binarySearchIt(x),
                 // Standard Binary Search:
                 !items.equalRange(x).empty);
}
```

**Output:**

```
 1 false false false
 8  true  true  true
10 false false false
 9  true  true  true
 5 false false false
 2  true  true  true
```


## Delphi

See #Pascal.


## E

```mw
/** Returns null if the value is not found. */
def binarySearch(collection, value) {
    var low := 0
    var high := collection.size() - 1
    while (low <= high) {
        def mid := (low + high) // 2
        def comparison := value.op__cmp(collection[mid])
        if      (comparison.belowZero()) { high := mid - 1 } \
        else if (comparison.aboveZero()) { low := mid + 1 }  \
        else if (comparison.isZero())    { return mid }      \
        else                             { throw("You expect me to binary search with a partial order?") }
    }
    return null
}
```


## EasyLang

```mw
func binSearch &a[] val .
   low = 1
   high = len a[]
   while low <= high
      mid = (low + high) div 2
      if a[mid] > val
         high = mid - 1
      elif a[mid] < val
         low = mid + 1
      else
         return mid
      .
   .
   return 0
.
a[] = [ 2 4 6 8 9 ]
print binSearch a[] 8
```

**Output:**

```
4
```


## Eiffel

The following solution is based on the one described in: C. A. Furia, B. Meyer, and S. Velder. *Loop Invariants: Analysis, Classification, and Examples*. ACM Computing Surveys, 46(3), Article 34, January 2014. (Also available at http://arxiv.org/abs/1211.4470). It includes detailed loop invariants and pre- and postconditions, which make the running time linear (instead of logarithmic) when full contract checking is enabled.

```mw
class
	APPLICATION

create
	make

feature {NONE} -- Initialization

	make
		local
			a: ARRAY [INTEGER]
			keys: ARRAY [INTEGER]
		do
			a := <<0, 1, 4, 5, 6, 7, 8, 9,
			       12, 26, 45, 67, 78, 90,
			       98, 123, 211, 234, 456,
			       769, 865, 2345, 3215,
			       14345, 24324>>
			keys := <<0, 42, 45, 24324, 99999>>
			across keys as k loop
				if has_binary (a, k.item) then
					print ("The array has an element " + k.item.out)
				else
					print ("The array has NOT an element " + k.item.out)
				end
				print ("%N")
			end
		end

feature -- Search

	has_binary (a: ARRAY [INTEGER]; key: INTEGER): BOOLEAN
		-- Does `a[a.lower..a.upper]' include an element `key'?
		require
			is_sorted (a, a.lower, a.upper)
		local
			i: INTEGER
		do
			i := where_binary (a, key)
			if a.lower <= i and i <= a.upper then
				Result := True
			else
				Result := False
			end
		end

	where_binary (a: ARRAY [INTEGER]; key: INTEGER): INTEGER
		-- The index of an element `key' within `a[a.lower..a.upper]' if it exists.
		-- Otherwise an integer outside `[a.lower..a.upper]'
		require
			is_sorted (a, a.lower, a.upper)
		do
			Result := where_binary_range (a, key, a.lower, a.upper)
		end

	where_binary_range (a: ARRAY [INTEGER]; key: INTEGER; low, high: INTEGER): INTEGER
		-- The index of an element `key' within `a[low..high]' if it exists.
		-- Otherwise an integer outside `[low..high]'
		note
			source: "http://arxiv.org/abs/1211.4470"
		require
			is_sorted (a, low, high)
		local
			i, j, mid: INTEGER
		do
			if low > high then
				Result := low - 1
			else
				from
					i := low
					j := high
					mid := low
					Result := low - 1
				invariant
					low <= i and i <= mid + 1
					low <= mid and mid <= j and j <= high
					i <= j
					has (a, key, i, j) = has (a, key, low, high)
				until
					i >= j
				loop
					mid := i + (j - i) // 2
					if a [mid] < key then
						i := mid + 1
					else
						j := mid
					end
				variant
					j - i
				end
				if a [i] = key then
					Result := i
				end
			end
		ensure
			low <= Result and Result <= high implies a [Result] = key
			Result < low or Result > high implies not has (a, key, low, high)
		end

feature -- Implementation

	is_sorted (a: ARRAY [INTEGER]; low, high: INTEGER): BOOLEAN
		-- Is `a[low..high]' sorted in nondecreasing order?
		require
			a.lower <= low
			high <= a.upper
		do
			Result := across low |..| (high - 1) as i all a [i.item] <= a [i.item + 1] end
		end

	has (a: ARRAY [INTEGER]; key: INTEGER; low, high: INTEGER): BOOLEAN
		-- Is there an element `key' in `a[low..high]'?
		require
			a.lower <= low
			high <= a.upper
		do
			Result := across low |..| high as i some a [i.item] = key end
		end

end
```


## Elixir

```mw
defmodule Binary do
  def search(list, value), do: search(List.to_tuple(list), value, 0, length(list)-1)
  
  def search(_tuple, _value, low, high) when high < low, do: :not_found
  def search(tuple, value, low, high) do
    mid = div(low + high, 2)
    midval = elem(tuple, mid)
    cond do
      value <  midval -> search(tuple, value, low, mid-1)
      value >  midval -> search(tuple, value, mid+1, high)
      value == midval -> mid 
    end
  end
end

list = [0,1,4,5,6,7,8,9,12,26,45,67,78,90,98,123,211,234,456,769,865,2345,3215,14345,24324]
Enum.each([0,42,45,24324,99999], fn val ->
  case Binary.search(list, val) do
    :not_found -> IO.puts "#{val} not found in list"
    index      -> IO.puts "found #{val} at index #{index}"
  end
end)
```

**Output:**

```
found 0 at index 0
42 not found in list
found 45 at index 10
found 24324 at index 24
99999 not found in list
```


## Emacs Lisp

```mw
(defun binary-search (value array)
  (let ((low 0)
        (high (1- (length array))))
    (cl-do () ((< high low) nil)
      (let ((middle (floor (+ low high) 2)))
        (cond ((> (aref array middle) value)
               (setf high (1- middle)))
              ((< (aref array middle) value)
               (setf low (1+ middle)))
              (t (cl-return middle)))))))
```


## EMal

```mw
type BinarySearch:Recursive
fun binarySearch ← int by List values, int value
  fun recurse ← int by int low, int high
    if high < low do return -1 end
	int mid ← low + (high - low) / 2
    return when(values[mid] > value,
      recurse(low, mid - 1),
      when(values[mid] < value,
      recurse(mid + 1, high),
      mid))
  end
  return recurse(0, values.length - 1)
end
type BinarySearch:Iterative
fun binarySearch ← int by List values, int value
  int low ← 0
  int high ← values.length - 1
  while low ≤ high
	int mid ← low + (high - low) / 2
    if values[mid] > value do high ← mid - 1
    else if values[mid] < value do low ← mid + 1
    else do return mid
	end
  end
  return -1
end
List values ← int[0, 1, 4, 5, 6, 7, 8, 9, 12, 26, 45, 67, 78, 
  90, 98, 123, 211, 234, 456, 769, 865, 2345, 3215, 14345, 24324]
List matches ← int[24324, 32, 78, 287, 0, 42, 45, 99999]
writeLine("recursive | iterative")
matches.list(<int match|writeLine(
  (text!BinarySearch:Recursive.binarySearch(values, match)).padStart(9, " "), " | ",
  (text!BinarySearch:Iterative.binarySearch(values, match)).padStart(9, " ")))
```

**Output:**

```
recursive | iterative
       24 |        24
       -1 |        -1
       12 |        12
       -1 |        -1
        0 |         0
       -1 |        -1
       10 |        10
       -1 |        -1
```


## Erlang

```mw
%% Task: Binary Search algorithm
%% Author: Abhay Jain

-module(searching_algorithm).
-export([start/0]).

start() ->
    List = [1,2,3],
    binary_search(List, 5, 1, length(List)).
    
    
binary_search(List, Value, Low, High) ->
    if Low > High ->
        io:format("Number ~p not found~n", [Value]),
        not_found;
       true ->
        Mid = (Low + High) div 2,
        MidNum = lists:nth(Mid, List),
        if MidNum > Value ->
            binary_search(List, Value, Low, Mid-1);
           MidNum < Value ->
            binary_search(List, Value, Mid+1, High);
           true ->
            io:format("Number ~p found at index ~p", [Value, Mid]),
            Mid
        end
    end.
```


## Euphoria

### Recursive

```mw
function binary_search(sequence s, object val, integer low, integer high)
    integer mid, cmp
    if high < low then
        return 0 -- not found
    else
        mid = floor( (low + high) / 2 )
        cmp = compare(s[mid], val)
        if  cmp > 0 then
            return binary_search(s, val, low, mid-1)
        elsif cmp < 0 then
            return binary_search(s, val, mid+1, high)
        else
            return mid
        end if
    end if
end function
```

### Iterative

```mw
function binary_search(sequence s, object val)
    integer low, high, mid, cmp
    low = 1
    high = length(s)
    while low <= high do
        mid = floor( (low + high) / 2 )
        cmp = compare(s[mid], val)
        if cmp > 0 then
            high = mid - 1
        elsif cmp < 0 then
            low = mid + 1
        else
            return mid
        end if
    end while
    return 0 -- not found
end function
```


## F

Generic recursive version, using #light syntax:

```mw
let rec binarySearch (myArray:array<IComparable>, low:int, high:int, value:IComparable) =
    if (high < low) then
        null
    else
        let mid = (low + high) / 2

        if (myArray.[mid] > value) then
            binarySearch (myArray, low, mid-1, value)
        else if (myArray.[mid] < value) then
            binarySearch (myArray, mid+1, high, value)
        else
            myArray.[mid]
```


## Factor

Factor already includes a binary search in its standard library. The following code offers an interface compatible with the requirement of this task, and returns either the index of the element if it has been found or f otherwise.

```mw
USING: binary-search kernel math.order ;

: binary-search ( seq elt -- index/f )
    [ [ <=> ] curry search ] keep = [ drop f ] unless ;
```


## FBSL

FBSL has built-in QuickSort() and BSearch() functions:

```mw
#APPTYPE CONSOLE

DIM va[], sign = {1, -1}, toggle

PRINT "Loading ... ";
DIM gtc = GetTickCount()
FOR DIM i = 0 TO 1000000
	va[] = sign[toggle] * PI * i
	toggle = NOT toggle		' randomize the array
NEXT
PRINT "done in ", GetTickCount() - gtc, " milliseconds"

PRINT "Sorting ... ";
gtc = GetTickCount()
QUICKSORT(va)				' quick sort the array
PRINT "done in ", GetTickCount() - gtc, " milliseconds"

gtc = GetTickCount()
PRINT 1000000 * PI, " found at index ", BSEARCH(va, 1000000 * PI), _	' binary search through the array
	" in ", GetTickCount() - gtc, " milliseconds"

PAUSE
```

Output:

```
Loading ... done in 906 milliseconds
Sorting ... done in 547 milliseconds
3141592.65358979 found at index 1000000 in 0 milliseconds

Press any key to continue...
```

User-defined implementations of the same would be considerably slower. Nonetheless, here they are in order to comply with the task requirements.

**Iterative:**

```mw
#APPTYPE CONSOLE

DIM va[]

PRINT "Loading ... ";
DIM gtc = GetTickCount()
FOR DIM i = 0 TO 1000000: va[] = i * PI: NEXT
PRINT "done in ", GetTickCount() - gtc, " milliseconds"

gtc = GetTickCount()
PRINT 1000000 * PI, " found at index ", BSearchIter(va, 1000000 * PI), _
	" in ", GetTickCount() - gtc, " milliseconds"

PAUSE

FUNCTION BSearchIter(BYVAL array, BYVAL num)
	STATIC low = LBOUND(va), high = UBOUND(va)
	WHILE low <= high
		DIM midp = (high + low) \ 2
		IF array[midp] > num THEN
			high = midp - 1
		ELSEIF array[midp] < num THEN
			low = midp + 1
		ELSE
			RETURN midp
		END IF
	WEND
	RETURN -1
END FUNCTION
```

Output:

```
Loading ... done in 391 milliseconds
3141592.65358979 found at index 1000000 in 62 milliseconds

Press any key to continue...
```

**Recursive:**

```mw
#APPTYPE CONSOLE

DIM va[]

PRINT "Loading ... ";
DIM gtc = GetTickCount()
FOR DIM i = 0 TO 1000000: va[] = i * PI: NEXT
PRINT "done in ", GetTickCount() - gtc, " milliseconds"

gtc = GetTickCount()
PRINT 1000000 * PI, " found at index ", BSearchRec(va, 1000000 * PI, LBOUND(va), UBOUND(va)), _
	" in ", GetTickCount() - gtc, " milliseconds"

PAUSE

FUNCTION BSearchRec(BYVAL array, BYVAL num, BYVAL low, BYVAL high)
	IF high < low THEN RETURN -1
	DIM midp = (high + low) \ 2
	IF array[midp] > num THEN
		RETURN BSearchRec(array, num, low, midp - 1)
	ELSEIF array[midp] < num THEN
		RETURN BSearchRec(array, num, midp + 1, high)
	END IF
	RETURN midp
END FUNCTION
```

Output:

```
Loading ... done in 390 milliseconds
3141592.65358979 found at index 1000000 in 938 milliseconds

Press any key to continue...
```


## Forth

This version is designed for maintaining a sorted array. If the item is not found, then then location returned is the proper insertion point for the item. This could be used in an optimized Insertion sort, for example.

```mw
defer (compare)
' - is (compare) \ default to numbers

: cstr-compare ( cstr1 cstr2 -- <=> ) \ counted strings
  swap count rot count compare ;

: mid ( u l -- mid ) tuck - 2/ -cell and + ;

: bsearch ( item upper lower -- where found? )
  rot >r
  begin  2dup >
  while  2dup mid
         dup @ r@ (compare)
         dup
  while  0<
         if   nip cell+   ( upper mid+1 )
         else rot drop swap ( mid lower )
         then
  repeat drop nip nip             true
  else   max ( insertion-point ) false
  then
  r> drop ;

create test 2 , 4 , 6 , 9 , 11 ,   99 ,
: probe ( n -- ) test 5 cells bounds bsearch . @ . cr ;
1 probe \ 0 2
2 probe \ -1 2
3 probe \ 0 4
10 probe \ 0 11
11 probe \ -1 11
12 probe \ 0 99
```


## Fortran

**Recursive** In ISO Fortran 90 or later use a RECURSIVE function and ARRAY SECTION argument:

```mw
recursive function binarySearch_R (a, value) result (bsresult)
    real, intent(in) :: a(:), value
    integer          :: bsresult, mid
    
    mid = size(a)/2 + 1
    if (size(a) == 0) then
        bsresult = 0        ! not found
    else if (a(mid) > value) then
        bsresult= binarySearch_R(a(:mid-1), value)
    else if (a(mid) < value) then
        bsresult = binarySearch_R(a(mid+1:), value)
        if (bsresult /= 0) then
            bsresult = mid + bsresult
        end if
    else
        bsresult = mid      ! SUCCESS!!
    end if
end function binarySearch_R
```

**Iterative** In ISO Fortran 90 or later use an ARRAY SECTION POINTER:

```mw
function binarySearch_I (a, value)
    integer                  :: binarySearch_I
    real, intent(in), target :: a(:)
    real, intent(in)         :: value
    real, pointer            :: p(:)
    integer                  :: mid, offset
    
    p => a
    binarySearch_I = 0
    offset = 0
    do while (size(p) > 0)
        mid = size(p)/2 + 1
        if (p(mid) > value) then
            p => p(:mid-1)
        else if (p(mid) < value) then
            offset = offset + mid
            p => p(mid+1:)
        else
            binarySearch_I = offset + mid    ! SUCCESS!!
            return
        end if
    end do
end function binarySearch_I
```

### Iterative, exclusive bounds, three-way test.

This has the array indexed from 1 to N, and the "not found" return code is zero or negative. Changing the search to be for A(first:last) is trivial, but the "not-found" return protocol would require adjustment, as when starting the array indexing at zero. Aside from the "not found" report, The variables used in the search *must* be able to hold the values *first - 1* and *last + 1* so for example with sixteen-bit two's complement integers the maximum value for *last* is 3276**6**, **not** 3276**7**.

Depending on the version of Fortran the compiler supports, the specification of the array parameter may vary, as A(1) or A(*) or A(:), and in the latter case, parameter N could be omitted because the size of an array parameter may be ascertained via the SIZE function. For the more advanced fortrans, declaring the parameters to be INTENT(IN) may help, as despite passing arrays "by reference" being the norm, the newer compilers may generate copy-in, copy-out code, vitiating the whole point of using a fast binary search instead of a slow linear search. In this case, INTENT(IN) will at least prevent the copy-back. In such a situation however, preparing in-line code may be the better move: fortunately, there is not a lot of code involved. There is no point in using an explicitly recursive version (even though the same actions may result during execution) because of the overhead of parameter passing and procedure entry/exit.

Later compilers offer features allowing the development of "generic" functions so that the same function name may be used yet the actual routine invoked will be selected according to how the parameters are integers or floating-point, and of different precisions. There would still need to be a version of the function for each type combination, each with its own name. Unfortunately, there is no three-way comparison test for character data.

The use of "exclusive" bounds simplifies the adjustment of the bounds: the appropriate bound simply receives the value of P, there is *no* + 1 or - 1 adjustment *at every step*; similarly, the determination of an empty span is easy, and avoiding the risk of integer overflow via (L + R)/2 is achieved at the same time. The "inclusive" bounds version by contrast requires *two* manipulations of L and R *at every step* - once to see if the span is empty, and a second time to locate the index to test.

```mw
      INTEGER FUNCTION FINDI(X,A,N)	!Binary chopper. Find i such that X = A(i)
Careful: it is surprisingly difficult to make this neat, due to vexations when N = 0 or 1.
       REAL X,A(*)		!Where is X in array A(1:N)?
       INTEGER N		!The count.
       INTEGER L,R,P		!Fingers.
        L = 0			!Establish outer bounds, to search A(L+1:R-1).
        R = N + 1		!L = first - 1; R = last + 1.
    1   P = (R - L)/2		!Probe point. Beware INTEGER overflow with (L + R)/2.
        IF (P.LE.0) GO TO 5	!Aha! Nowhere!! The span is empty.
        P = P + L		!Convert an offset from L to an array index.
        IF (X - A(P)) 3,4,2	!Compare to the probe point.
    2   L = P			!A(P) < X. Shift the left bound up: X follows A(P).
        GO TO 1			!Another chop.
    3   R = P			!X < A(P). Shift the right bound down: X precedes A(P).
        GO TO 1			!Try again.
    4   FINDI = P		!A(P) = X. So, X is found, here!
       RETURN			!Done.
Curse it!
    5   FINDI = -L		!X is not found. Insert it at L + 1, i.e. at A(1 - FINDI).
      END FUNCTION FINDI	!A's values need not be all different, merely in order.
```

#### Statistics

Imagine a test array containing the even numbers: 2,4,6,8. A count could be kept of the number of probes required to find each of those four values, and likewise with a search for the odd numbers 1,3,5,7,9 that would probe all the places where a value might be not found. Plot the average number of probes for the two cases, plus the maximum number of probes for any case, and then repeat for another number of elements to search. With only one element in the array to be searched, all values are the same: one probe.

#### An alternative version

```mw
      INTEGER FUNCTION FINDI(X,A,N)	!Binary chopper. Find i such that X = A(i)
Careful: it is surprisingly difficult to make this neat, due to vexations when N = 0 or 1.
       REAL X,A(*)		!Where is X in array A(1:N)?
       INTEGER N		!The count.
       INTEGER L,R,P		!Fingers.
        L = 0			!Establish outer bounds, to search A(L+1:R-1).
        R = N + 1		!L = first - 1; R = last + 1.
        GO TO 1			!Hop to it.
    2   L = P			!A(P) < X. Shift the left bound up: X follows A(P).
    1   P = (R - L)/2		!Probe point. Beware INTEGER overflow with (L + R)/2.
        IF (P.LE.0) GO TO 5	!Aha! Nowhere!! The span is empty.
        P = P + L		!Convert an offset from L to an array index.
        IF (X - A(P)) 3,4,2	!Compare to the probe point.
    3   R = P			!X < A(P). Shift the right bound down: X precedes A(P).
        GO TO 1			!Try again.
    4   FINDI = P		!A(P) = X. So, X is found, here!
       RETURN			!Done.
Curse it!
    5   FINDI = -L		!X is not found. Insert it at L + 1, i.e. at A(1 - FINDI).
      END FUNCTION FINDI	!A's values need not be all different, merely in order.
```

The point of this is that the IF-test is going to initiate some jumps, so why not arrange that one of the bound adjustments needs no subsequent jump to the start of the next iteration - in the first version, both bound adjustments needed such a jump, the GO TO 1 statements. This was done by shifting the code for label 2 up to precede the code for label 1 - and removing its now pointless GO TO 1 (executed each time), but adding an initial GO TO 1, executed once only. This sort of change is routine when manipulating spaghetti code...

It is because the method involves such a small amount of effort per iteration that minor changes offer a significant benefit. A lot depends on the implementation of the three-way test: the hope is that after the comparison, the computer hardware has indicators set for various outcomes, so that the necessary conditional branches can be made through successive inspection of those indicators, rather than repeating the comparison. These branch tests may in turn be made in an order that notes which option (if any) involves "falling through" to the next statement, thus it may be better to swap the order of labels 3 and 4. Further, the compiler may itself choose to re-order the various code pieces. First Fortran (in 1958) had a FREQUENCY statement whereby the programmer could indicate which paths were the more likely - for the binary search, equality is the less likely discovery. An assembler version of this routine attended to all these details.

Some compilers do not produce machine code directly, but instead translate the source code into another language which is then compiled, and a common choice for that is C. This is all very well, but C is one of the many languages that do *not* have a three-way test option and so cannot represent Fortran's three-way IF statement directly. Before emitting asservations of faith that pseudocode such as

```
 if expression > 0 then optionP
  else if expression < 0 then optionN
   else optionZ;
```

will be recognised by the most excellent compiler producing only one comparison, note that the two expressions are *not* the same (one has <, the other >), and test what happens with pseudocode such as

```
 if X > 0 then print "Positive"
  else if X > 0 then print "Still positive";
```

That is, does the compiler make any remark, and does the resulting machine code contain a redundant test? However, despite all the above, the three-way IF statement has been declared deprecated in later versions of Fortran, with no alternative to repeated testing offered.

Incidentally, the exclusive-bounds version leads to a good version of the interpolation search (whereby the probe position is interpolated, not just in the middle of the span), unlike the version based on inclusive-bounds. Further, the unsourced offering in Wikipedia contains a bug - try searching an array of two equal elements for that value.


## Futhark

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** Futhark's syntax has changed, so this example will not compile |
|---|

Straightforward translation of imperative iterative algorithm.

```mw
fun main(as: [n]int, value: int): int =
  let low = 0
  let high = n-1
  loop ((low,high)) = while low <= high do
    -- invariants: value > as[i] for all i < low
    --             value < as[i] for all i > high
    let mid = (low+high) / 2
    in if as[mid] > value
       then (low, mid - 1)
       else if as[mid] < value
       then (mid + 1, high)
       else (mid, mid-1) -- Force termination.
  in low
```


## FutureBasic

Translation of

:

Objective-C

**Iterative**

```mw
include "NSLog.incl"

NSInteger local fn BinarySearch( array as CFArrayRef, key as CFTypeRef )
NSInteger lo = 0
NSInteger hi = len(array) - 1
while ( lo <= hi )
  NSInteger i = lo + (hi - lo) / 2
  CFTypeRef midVal = array[i]
  select ( fn NumberCompare( midVal, key ) )
    case NSOrderedAscending
      lo = i + 1
    case NSOrderedDescending
      hi = i - 1
    case NSOrderedSame:
      return i
  end select
wend
end fn = NSNotFound

void local fn DoIt
  CFArrayRef a = @[@1, @3, @4, @5, @6, @7, @8, @9, @10]
  NSLog(@"6 is at position %d", fn BinarySearch( a, @6 ) ) // prints 4
end fn

fn DoIt

HandleEvents
```

**Recursive**

```mw
include "NSLog.incl"

NSInteger local fn BinarySearch( array as CFArrayRef, key as CFTypeRef )
NSInteger lo = 0
include "NSLog.incl"

NSInteger local fn BinarySearch( array as CFArrayRef, key as CFTypeRef, range as CFRange )
if ( range.length == 0 ) then return NSNotFound

NSInteger i = range.location + range.length / 2
CFTypeRef midVal = array[i]

select ( fn NumberCompare( midVal, key ) )
  case NSOrderedAscending
    return fn BinarySearch( array, key, fn CFRangeMake( i + 1, range.length - i + 1 ) )
  case NSOrderedDescending
    return fn BinarySearch( array, key, fn CFRangeMake( range.location, i - range.location ) )
end select
end fn = i

void local fn DoIt
  CFArrayRef a = @[@1, @3, @4, @5, @6, @7, @8, @9, @10]
  NSLog(@"6 is at position %d", fn BinarySearch( a, @6, fn CFRangeMake(0,len(a)) )) // prints 4
end fn

fn DoIt

HandleEvents
```


## GAP

```mw
Find := function(v, x)
  local low, high, mid;
  low := 1;
  high := Length(v);
  while low <= high do
    mid := QuoInt(low + high, 2);
    if v[mid] > x then
      high := mid - 1;
    elif v[mid] < x then
      low := mid + 1;
    else
      return mid;
    fi;
  od;
  return fail;
end;

u := [1..10]*7;
# [ 7, 14, 21, 28, 35, 42, 49, 56, 63, 70 ]
Find(u, 34);
# fail
Find(u, 35);
# 5
```


## Go

**Recursive**:

```mw
func binarySearch(a []float64, value float64, low int, high int) int {
    if high < low {
        return -1
    }
    mid := (low + high) / 2
    if a[mid] > value {
        return binarySearch(a, value, low, mid-1)
    } else if a[mid] < value {
        return binarySearch(a, value, mid+1, high)
    }
    return mid
}
```

**Iterative**:

```mw
func binarySearch(a []float64, value float64) int {
    low := 0
    high := len(a) - 1
    for low <= high {
        mid := (low + high) / 2
        if a[mid] > value {
            high = mid - 1
        } else if a[mid] < value {
            low = mid + 1
        } else {
            return mid
        }
    }
    return -1
}
```

**Library**:

```mw
import "sort"

//...

sort.SearchInts([]int{0,1,4,5,6,7,8,9}, 6) // evaluates to 4
```

Exploration of library source code shows that it uses the mid = low + (high - low) / 2 technique to avoid overflow.

There are also functions `sort.SearchFloat64s()`, `sort.SearchStrings()`, and a very general `sort.Search()` function that allows you to binary search a range of numbers based on any condition (not necessarily just search for an index of an element in an array).


## Golfscript

```
{:Val;:A;
0:Low;A,(:High;
1:f;
{Low High>!f&}{
  Low High+2/:Mid;
  A Mid= Val> {
    Mid(:High;
  } {
    A Mid= Val< {
      Mid):Low;
    } {
      Mid
      0:f;
    } if
  } if
}while
f{-1}*
}:bs;

[0 1 2 5 6 8 9] 8 bs p
[0 1 2 5 6 8 9] 11 bs p
```

**Output:**

```
5
-1
```
