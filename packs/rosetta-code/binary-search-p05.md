---
title: "Binary search (part 5/6)"
source: https://rosettacode.org/wiki/Binary_search
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/6
---

## Ol

```mw
(define (binary-search value vector)
   (let helper ((low 0)
                (high (- (vector-length vector) 1)))
      (unless (< high low)
         (let ((middle (quotient (+ low high) 2)))
            (cond
               ((> (vector-ref vector middle) value)
                  (helper low (- middle 1)))
               ((< (vector-ref vector middle) value)
                  (helper (+ middle 1) high))
               (else middle))))))

(print
   (binary-search 12 [1 2 3 4 5 6 7 8 9 10 11 12 13]))
; ==> 12
```


## ooRexx

```mw
data = .array~of(1, 3, 5, 7, 9, 11)
-- search keys with a number of edge cases
searchkeys = .array~of(0, 1, 4, 7, 11, 12)
say "recursive binary search"
loop key over searchkeys
    pos = recursiveBinarySearch(data, key)
    if pos == 0 then say "Key" key "not found"
    else say "Key" key "found at postion" pos
end
say
say "iterative binary search"
loop key over searchkeys
    pos = iterativeBinarySearch(data, key)
    if pos == 0 then say "Key" key "not found"
    else say "Key" key "found at postion" pos
end

::routine recursiveBinarySearch
  -- NB:  Rexx arrays are 1-based
  use strict arg data, value, low = 1, high = (data~items)

  -- make sure we don't go beyond the bounds
  high = min(high, data~items)
  -- zero indicates not found
  if high < low then return 0

  mid = (low + high) % 2
  if data[mid] > value then
      return recursiveBinarySearch(data, value, low, mid - 1)
  else if data[mid] < value then
      return recursiveBinarySearch(data, value, mid + 1, high)
  -- got it!
  return mid

::routine iterativeBinarySearch
  -- NB:  Rexx arrays are 1-based
  use strict arg data, value, low = 1, high = (data~items)

  -- make sure we don't go beyond the bounds
  high = min(high, data~items)
  -- zero indicates not found
  if high < low then return 0
  loop while low <= high
      mid = (low + high) % 2
      if data[mid] > value then
          high = mid - 1
      else if data[mid] < value then
          low = mid + 1
      else
          return mid
  end
  return 0
```

Output:

```
recursive binary search
Key 0 not found
Key 1 found at postion 1
Key 4 not found
Key 7 found at postion 4
Key 11 found at postion 6
Key 12 not found

iterative binary search
Key 0 not found
Key 1 found at postion 1
Key 4 not found
Key 7 found at postion 4
Key 11 found at postion 6
Key 12 not found
```


## Oz

**Recursive**

```mw
declare
  fun {BinarySearch Arr Val}
     fun {Search Low High}
        if Low > High then nil
        else
           Mid = (Low+High) div 2
        in
           if Val < Arr.Mid then {Search Low Mid-1}
           elseif Val > Arr.Mid then {Search Mid+1 High}
           else [Mid]
           end
        end
     end
  in
     {Search {Array.low Arr} {Array.high Arr}}
  end

  A = {Tuple.toArray unit(2 3 5 6 8)}
in
  {System.printInfo "searching 4: "} {Show {BinarySearch A 4}}
  {System.printInfo "searching 8: "} {Show {BinarySearch A 8}}
```

**Iterative**

```mw
declare
  fun {BinarySearch Arr Val}
     Low = {NewCell {Array.low Arr}}
     High = {NewCell {Array.high Arr}}
  in
     for while:@Low =< @High  return:Return  default:nil do
        Mid = (@Low + @High) div 2
     in
        if Val < Arr.Mid then High := Mid-1
        elseif Val > Arr.Mid then Low := Mid+1
        else {Return [Mid]}
        end
     end
  end

  A = {Tuple.toArray unit(2 3 5 6 8)}
in
  {System.printInfo "searching 4: "} {Show {BinarySearch A 4}}
  {System.printInfo "searching 8: "} {Show {BinarySearch A 8}}
```


## PARI/GP

Note that, despite the name, `setsearch` works on sorted vectors as well as sets.

```mw
setsearch(s, n)
```

The following is another implementation that takes a more manual approach. Instead of using an intrinsic function, a general binary search algorithm is implemented using the language alone.

Translation of

:

N/t/roff

```mw
binarysearch(v, x) = {
    local(
        minm = 1,
        maxm = length(v),
        guess = floor(maxm/2+minm/2)
    );

    while(v[guess] != x,    
        if(v[guess] < x, minm = guess + 1, maxm = guess - 1);
        if(minm > maxm,
            guess = 0;
            break
        );
        guess = floor(maxm/2+minm/2)
    );

    return(guess);
}

idx = binarysearch([1,4,9,16,25,36,49,64,81,100,121,144], 121);
if(idx, \
    print("Item exists on index ", idx), \
    print("Item does not exist anywhere.") \
)
```


## Pascal

**Iterative**

```mw
function binary_search(element: real; list: array of real): integer;
var
    l, m, h: integer;
begin
    l := Low(list);
    h := High(list);
    binary_search := -1;
    while l <= h do
    begin
        m := (l + h) div 2;
        if list[m] > element then
        begin
            h := m - 1;
        end
        else if list[m] < element then
        begin
            l := m + 1;
        end
        else
        begin
            binary_search := m;
            break;
        end;
    end;
end;
```

Usage:

```mw
var
    list: array[0 .. 9] of real;
// ...
indexof := binary_search(123, list);
```


## PascalABC.NET

```mw
function BinarySearch(a: array of integer; x: integer): integer;
begin
  var (l,r) := (0, a.Length-1); 
  repeat
    var mid := (l + r) div 2;
    if x = a[mid] then 
    begin
      Result := mid;
      exit
    end;
    if x > a[mid] then
      l := mid + 1
    else r := mid - 1;
  until l > r;
  Result := -1;
end;

function BinarySearchRecursive(a: array of integer; x: integer): integer;
  function BinarySearchHelper(a: array of integer; x: integer; l,r: integer): integer;
  begin
    if l > r then
      Result := -1
    else begin
      var mid := (l + r) div 2;
      if x = a[mid] then
        Result := mid
      else if x < a[mid] then
        Result := BinarySearchHelper(a, x, l, mid - 1)
      else Result := BinarySearchHelper(a, x, mid + 1, r)
    end;  
  end;
begin
  Result := BinarySearchHelper(a,x,0,a.Length-1);
end;

begin
  var a := ArrRandomInteger(10,1,20);
  a.Sort;
  a.Println;
  var x := 10;
  var ind := BinarySearch(a,x);
  if ind >= 0 then
    Println($'{x} found at index {ind}')
  else Println($'{x} not found');

  ind := BinarySearchRecursive(a,x);
  if ind >= 0 then
    Println($'{x} found at index {ind}')
  else Println($'{x} not found');
  
  x := a.RandomElement;
  ind := BinarySearch(a,x);
  if ind >= 0 then
    Println($'{x} found at index {ind}')
  else Println($'{x} not found');

  ind := BinarySearchRecursive(a,x);
  if ind >= 0 then
    Println($'{x} found at index {ind}')
  else Println($'{x} not found');
end.
```

**Output:**

```
2 3 5 12 13 14 14 15 15 17
10 not found
10 not found
13 found at index 4
13 found at index 4
```

**Library**

```mw
##
var s := |2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,25,27,30|;
s.binarysearch(10).println;
```


## Perl

**Iterative**

```mw
sub binary_search {
    my ($array_ref, $value, $left, $right) = @_;
    while ($left <= $right) {
        my $middle = int(($right + $left) >> 1);
        if ($value == $array_ref->[$middle]) {
            return $middle;
        }
        elsif ($value < $array_ref->[$middle]) {
            $right = $middle - 1;
        }
        else {
            $left = $middle + 1;
        }
    }
    return -1;
}
```

**Recursive**

```mw
sub binary_search {
    my ($array_ref, $value, $left, $right) = @_;
    return -1 if ($right < $left);
    my $middle = int(($right + $left) >> 1);
    if ($value == $array_ref->[$middle]) {
        return $middle;
    }
    elsif ($value < $array_ref->[$middle]) {
        binary_search($array_ref, $value, $left, $middle - 1);
    }
    else {
        binary_search($array_ref, $value, $middle + 1, $right);
    }
}
```


## Phix

Standard autoinclude builtin/bsearch.e, reproduced here (for reference only, don't copy/paste unless you plan to modify and rename it)

```
global function binary_search(object needle, sequence haystack)
integer lo = 1,
        hi = length(haystack),
        mid = lo,
        c = 0
 
    while lo<=hi do
        mid = floor((lo+hi)/2)
        c = compare(needle, haystack[mid])
        if c<0 then
            hi = mid-1
        elsif c>0 then
            lo = mid+1
        else
            return mid  -- found!
        end if
    end while
    mid += c>0
    return -mid         -- where it would go, if inserted now
end function
```

The low + (high-low)/2 trick is not needed, since interim integer results are accurate to 53 bits (on 32 bit, 64 bits on 64 bit) on Phix.

Returns a positive index if found, otherwise the negative index where it would go if inserted now. Example use

```
with javascript_semantics
?binary_search(0,{1,3,5})   -- -1
?binary_search(1,{1,3,5})   --  1
?binary_search(2,{1,3,5})   -- -2
?binary_search(3,{1,3,5})   --  2
?binary_search(4,{1,3,5})   -- -3
?binary_search(5,{1,3,5})   --  3
?binary_search(6,{1,3,5})   -- -4
```


## PHP

**Iterative**

```mw
function binary_search( $array, $secret, $start, $end )
{
        do
        {
                $guess = (int)($start + ( ( $end - $start ) / 2 ));

                if ( $array[$guess] > $secret )
                        $end = $guess;

                if ( $array[$guess] < $secret )
                        $start = $guess;

                if ( $end < $start)
                        return -1;

        } while ( $array[$guess] != $secret );

        return $guess;
}
```

**Recursive**

```mw
function binary_search( $array, $secret, $start, $end )
{
        $guess = (int)($start + ( ( $end - $start ) / 2 ));

        if ( $end < $start)
                return -1;

        if ( $array[$guess] > $secret )
                return (binary_search( $array, $secret, $start, $guess ));

        if ( $array[$guess] < $secret )
                return (binary_search( $array, $secret, $guess, $end ) );

        return $guess;
}
```


## Picat

### Iterative

```mw
go =>
  A = [2, 4, 6, 8, 9],
  TestValues = [2,1,8,10,9,5],

  foreach(Value in TestValues)
    test(binary_search,A, Value)
  end,
  test(binary_search,[1,20,3,4], 5),
  nl.

% Test with binary search predicate Search
test(Search,A,Value) => 
  Ret = apply(Search,A,Value),
  printf("A: %w Value:%d Ret: %d: ", A, Value, Ret),
  if Ret == -1 then
    println("The array is not sorted.")
  elseif Ret == 0 then
    printf("The value %d is not in the array.\n", Value)
  else
    printf("The value %d is found at position %d.\n", Value, Ret)
  end.

binary_search(A, Value) = V =>
  V1 = 0,
  % we want a sorted array
  if not sort(A) == A then
    V1 := -1
  else 
    Low = 1,
    High = A.length,
    Mid = 1,
    Found = 0,
    while (Found == 0, Low <= High) 
       Mid := (Low + High) // 2,
       if A[Mid] > Value then
         High := Mid - 1
       elseif A[Mid] < Value then
         Low := Mid + 1
       else 
         V1 := Mid,
         Found := 1
      end
    end
  end,
  V = V1.
```

**Output:**

```
A: [2,4,6,8,9] Value:2 Ret: 1: The value 2 is found at position 1.
A: [2,4,6,8,9] Value:1 Ret: 0: The value 1 is not in the array.
A: [2,4,6,8,9] Value:8 Ret: 4: The value 8 is found at position 4.
A: [2,4,6,8,9] Value:10 Ret: 0: The value 10 is not in the array.
A: [2,4,6,8,9] Value:9 Ret: 5: The value 9 is found at position 5.
A: [2,4,6,8,9] Value:5 Ret: 0: The value 5 is not in the array.
A: [1,20,3,4] Value:5 Ret: -1: The array is not sorted.
```

### Recursive version

```mw
binary_search_rec(A, Value) = Ret =>
  Ret = binary_search_rec(A,Value, 1, A.length).

binary_search_rec(A, _Value, _Low, _High) = -1, sort(A) != A => true.
binary_search_rec(_A, _Value, Low, High)  =  0, High < Low   => true.
binary_search_rec(A, Value, Low, High)    = Mid => 
  Mid1 = (Low + High) // 2,
   if A[Mid1] > Value then
     Mid1 := binary_search_rec(A, Value, Low, Mid1-1)
   elseif A[Mid1] < Value then
     Mid1 := binary_search_rec(A, Value, Mid1+1, High)
   end,
   Mid = Mid1.
```


## PicoLisp

**Recursive**

```mw
(de recursiveSearch (Val Lst Len)
   (unless (=0 Len)
      (let (N (inc (/ Len 2))  L (nth Lst N))
         (cond
            ((= Val (car L)) Val)
            ((> Val (car L))
               (recursiveSearch Val (cdr L) (- Len N)) )
            (T (recursiveSearch Val Lst (dec N))) ) ) ) )
```

Output:

```
: (recursiveSearch 5 (2 3 5 8 "abc" "klm" "xyz" (7) (a b)) 9)
-> 5
: (recursiveSearch '(a b) (2 3 5 8 "abc" "klm" "xyz" (7) (a b)) 9)
-> (a b)
: (recursiveSearch (9) (2 3 5 8 "abc" "klm" "xyz" (7) (a b)) 9)
-> NIL
```

**Iterative**

```mw
(de iterativeSearch (Val Lst Len)
   (use (N L)
      (loop
         (T (=0 Len))
         (setq
            N (inc (/ Len 2))
            L (nth Lst N) )
         (T (= Val (car L)) Val)
         (if (> Val (car L))
            (setq Lst (cdr L)  Len (- Len N))
            (setq Len (dec N)) ) ) ) )
```

Output:

```
: (iterativeSearch 5 (2 3 5 8 "abc" "klm" "xyz" (7) (a b)) 9)
-> 5
: (iterativeSearch '(a b) (2 3 5 8 "abc" "klm" "xyz" (7) (a b)) 9)
-> (a b)
: (iterativeSearch (9) (2 3 5 8 "abc" "klm" "xyz" (7) (a b)) 9)
-> NIL
```


## PL/I

```mw
/* A binary search of list A for element M */
search: procedure (A, M) returns (fixed binary);
   declare (A(*), M) fixed binary;
   declare (l, r, mid) fixed binary;

   l = lbound(a,1)-1; r = hbound(A,1)+1;
   do while (l <= r);
      mid = (l+r)/2;
      if A(mid) = M then return (mid);
      if A(mid) < M then
         L = mid+1;
      else
         R = mid-1;
   end;
   return (lbound(A,1)-1);
end search;
```


## Pluto

Library:

Pluto-table2

Library:

Pluto-fmt

The first above module already contains a binary search function which uses an iterative algorithm. However, for good measure, we hand code a version using a recursive algorithm as well.

```mw
require "table2"
local fmt = require "fmt"

local function rec_bsearch(a, v, low = 1, high = #a)
    if high < low then return false, 0 end
    local mid = low + (high - low) // 2
    if a[mid] > v then return rec_bsearch(a, v, low, mid - 1) end
    if a[mid] < v then return rec_bsearch(a, v, mid + 1, high) end
    return true, mid
end

local a = {10, 22, 45, 67, 89, 97}
fmt.lprint(a, ", ", "{}", "array = ")
print()

local texts = {"Using the library function (iterative algorithm):",
               "Using the recursive algorithm:"}

local values = { {22, 70}, {67, 93} }

local fns = {table.bsearch, rec_bsearch}

for i = 1, 2 do
    print(texts[i])
    for values[i] as v do
        local found, index = fns[i](a, v)
        if found then
            print($"  {v} was found at index {index} of the array")
        else
            print($"  {v} was not found in the array")
        end
    end
    if i == 1 then print() end
end
```

**Output:**

```
array = {10, 22, 45, 67, 89, 97}

Using the library function (iterative algorithm):
  22 was found at index 2 of the array
  70 was not found in the array

Using the recursive algorithm:
  67 was found at index 4 of the array
  93 was not found in the array
```


## Pop11

**Iterative**

```mw
define BinarySearch(A, value);
    lvars low = 1, high = length(A), mid;
    while low <= high do
        (low + high) div 2 -> mid;
        if A(mid) > value then
            mid - 1 -> high;
        elseif A(mid) < value then
            mid + 1 -> low;
        else
            return(mid);
        endif;
    endwhile;
    return("not_found");
enddefine;

/* Tests */
lvars A = {2 3 5 6 8};

BinarySearch(A, 4) =>
BinarySearch(A, 5) =>
BinarySearch(A, 8) =>
```

**Recursive**

```mw
define BinarySearch(A, value);
    define do_it(low, high);
        if high < low then
            return("not_found");
        endif;
        (low + high) div 2 -> mid;
        if A(mid) > value then
            do_it(low, mid-1);
        elseif A(mid) < value then
            do_it(mid+1, high);
        else
            mid;
        endif;
    enddefine;
    do_it(1, length(A));
enddefine;
```


## PowerShell

```mw
function BinarySearch-Iterative ([int[]]$Array, [int]$Value)
{
    [int]$low = 0
    [int]$high = $Array.Count - 1

    while ($low -le $high)
    {
        [int]$mid = ($low + $high) / 2

        if ($Array[$mid] -gt $Value)
        {
            $high = $mid - 1
        }
        elseif ($Array[$mid] -lt $Value)
        {
            $low = $mid + 1
        }
        else
        {
            return $mid
        }
    }

    return -1
}

function BinarySearch-Recursive ([int[]]$Array, [int]$Value, [int]$Low = 0, [int]$High = $Array.Count)
{
    if ($High -lt $Low)
    {
        return -1
    }

    [int]$mid = ($Low + $High) / 2

    if ($Array[$mid] -gt $Value)
    {
        return BinarySearch $Array $Value $Low ($mid - 1)
    }
    elseif ($Array[$mid] -lt $Value)
    {
        return BinarySearch $Array $Value ($mid + 1) $High
    }
    else
    {
        return $mid
    }
}

function Show-SearchResult ([int[]]$Array, [int]$Search, [ValidateSet("Iterative", "Recursive")][string]$Function)
{
    switch ($Function)
    {
        "Iterative" {$index = BinarySearch-Iterative -Array $Array -Value $Search}
        "Recursive" {$index = BinarySearch-Recursive -Array $Array -Value $Search}
    }

    if ($index -ge 0)
    {
        Write-Host ("Using BinarySearch-{0}: {1} is at index {2}" -f $Function, $numbers[$index], $index)
    }
    else
    {
        Write-Host ("Using BinarySearch-{0}: {1} not found" -f $Function, $Search) -ForegroundColor Red
    }
}
```

```mw
Show-SearchResult -Array 10, 28, 41, 46, 58, 74, 76, 86, 89, 98 -Search 41 -Function Iterative
Show-SearchResult -Array 10, 28, 41, 46, 58, 74, 76, 86, 89, 98 -Search 99 -Function Iterative
Show-SearchResult -Array 10, 28, 41, 46, 58, 74, 76, 86, 89, 98 -Search 86 -Function Recursive
Show-SearchResult -Array 10, 28, 41, 46, 58, 74, 76, 86, 89, 98 -Search 11 -Function Recursive
```

**Output:**

```
Using BinarySearch-Iterative: 41 is at index 2
Using BinarySearch-Iterative: 99 not found
Using BinarySearch-Recursive: 86 is at index 7
Using BinarySearch-Recursive: 11 not found
```


## Prolog

Tested with Gnu-Prolog.

```mw
bin_search(Elt,List,Result):-
  length(List,N), bin_search_inner(Elt,List,1,N,Result).
  
bin_search_inner(Elt,List,J,J,J):-
  nth(J,List,Elt).
bin_search_inner(Elt,List,Begin,End,Mid):-
  Begin < End,
  Mid is (Begin+End) div 2,
  nth(Mid,List,Elt).
bin_search_inner(Elt,List,Begin,End,Result):-
  Begin < End,
  Mid is (Begin+End) div 2,
  nth(Mid,List,MidElt),
  MidElt < Elt,
  NewBegin is Mid+1,
  bin_search_inner(Elt,List,NewBegin,End,Result).
bin_search_inner(Elt,List,Begin,End,Result):-
  Begin < End,
  Mid is (Begin+End) div 2,
  nth(Mid,List,MidElt),
  MidElt > Elt,
  NewEnd is Mid-1,
  bin_search_inner(Elt,List,Begin,NewEnd,Result).
```

**Output examples:**

```
 ?- bin_search(4,[1,2,4,8,16,32,64,128],Result).
Result = 3.

?- bin_search(5,[1,2,4,8],Result).
Result = -1.
```


## Python

### Python: Iterative

```mw
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1
```

We can also generalize this kind of binary search from direct matches to searches using a custom comparator function. In addition to a search for a particular word in an AZ-sorted list, for example, we could also perform a binary search for a word of a given **length** (in a word-list sorted by rising length), or for a particular value of any other comparable property of items in a suitably sorted list:

```mw
# findIndexBinary :: (a -> Ordering) -> [a] -> Maybe Int
def findIndexBinary(p):
    def isFound(bounds):
        (lo, hi) = bounds
        return lo > hi or 0 == hi

    def half(xs):
        def choice(lh):
            (lo, hi) = lh
            mid = (lo + hi) // 2
            cmpr = p(xs[mid])
            return (lo, mid - 1) if cmpr < 0 else (
                (1 + mid, hi) if cmpr > 0 else (
                    mid, 0
                )
            )
        return lambda bounds: choice(bounds)

    def go(xs):
        (lo, hi) = until(isFound)(
            half(xs)
        )((0, len(xs) - 1)) if xs else None
        return None if 0 != hi else lo

    return lambda xs: go(xs)

# COMPARISON CONSTRUCTORS ---------------------------------

# compare :: a -> a -> Ordering
def compare(a):
    '''Simple comparison of x and y -> LT|EQ|GT'''
    return lambda b: -1 if a < b else (1 if a > b else 0)

# byKV :: (a -> b) -> a -> a -> Ordering
def byKV(f):
    '''Property accessor function -> target value -> x -> LT|EQ|GT'''
    def go(v, x):
        fx = f(x)
        return -1 if v < fx else 1 if v > fx else 0
    return lambda v: lambda x: go(v, x)

# TESTS ---------------------------------------------------
def main():

    # BINARY SEARCH FOR WORD IN AZ-SORTED LIST

    mb1 = findIndexBinary(compare('iota'))(
        # Sorted AZ
        ['alpha', 'beta', 'delta', 'epsilon', 'eta', 'gamma', 'iota',
         'kappa', 'lambda', 'mu', 'theta', 'zeta']
    )

    print (
        'Not found' if None is mb1 else (
            'Word found at index ' + str(mb1)
        )
    )

    # BINARY SEARCH FOR WORD OF GIVEN LENGTH (IN WORD-LENGTH SORTED LIST)

    mb2 = findIndexBinary(byKV(len)(7))(
        # Sorted by rising length
        ['mu', 'eta', 'beta', 'iota', 'zeta', 'alpha', 'delta', 'gamma',
         'kappa', 'theta', 'lambda', 'epsilon']
    )

    print (
        'Not found' if None is mb2 else (
            'Word of given length found at index ' + str(mb2)
        )
    )

# GENERIC -------------------------------------------------

# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)

if __name__ == '__main__':
    main()
```

**Output:**

```
Word found at index 6
Word of given length found at index 11
```

### Python: Recursive

```mw
def binary_search(l, value, low = 0, high = -1):
    if not l: return -1
    if(high == -1): high = len(l)-1
    if low >= high:
        if l[low] == value: return low
        else: return -1
    mid = (low+high)//2
    if l[mid] > value: return binary_search(l, value, low, mid-1)
    elif l[mid] < value: return binary_search(l, value, mid+1, high)
    else: return mid
```

Generalizing again with a custom comparator function (see preamble to second iterative version above).

This time using the recursive definition:

```mw
# findIndexBinary_ :: (a -> Ordering) -> [a] -> Maybe Int
def findIndexBinary_(p):
    def go(xs):
        def bin(lo, hi):
            if hi < lo:
                return None
            else:
                mid = (lo + hi) // 2
                cmpr = p(xs[mid])
                return bin(lo, mid - 1) if -1 == cmpr else (
                    bin(mid + 1, hi) if 1 == cmpr else (
                        mid
                    )
                )
        n = len(xs)
        return bin(0, n - 1) if 0 < n else None
    return lambda xs: go(xs)

# COMPARISON CONSTRUCTORS ---------------------------------

# compare :: a -> a -> Ordering
def compare(a):
    '''Simple comparison of x and y -> LT|EQ|GT'''
    return lambda b: -1 if a < b else (1 if a > b else 0)

# byKV :: (a -> b) -> a -> a -> Ordering
def byKV(f):
    '''Property accessor function -> target value -> x -> LT|EQ|GT'''
    def go(v, x):
        fx = f(x)
        return -1 if v < fx else 1 if v > fx else 0
    return lambda v: lambda x: go(v, x)

# TESTS ---------------------------------------------------

if __name__ == '__main__':

    # BINARY SEARCH FOR WORD IN AZ-SORTED LIST

    mb1 = findIndexBinary_(compare('mu'))(
        # Sorted AZ
        ['alpha', 'beta', 'delta', 'epsilon', 'eta', 'gamma', 'iota',
         'kappa', 'lambda', 'mu', 'theta', 'zeta']
    )

    print (
        'Not found' if None is mb1 else (
            'Word found at index ' + str(mb1)
        )
    )

    # BINARY SEARCH FOR WORD OF GIVEN LENGTH (IN WORD-LENGTH SORTED LIST)

    mb2 = findIndexBinary_(byKV(len)(6))(
        # Sorted by rising length
        ['mu', 'eta', 'beta', 'iota', 'zeta', 'alpha', 'delta', 'gamma',
         'kappa', 'theta', 'lambda', 'epsilon']
    )

    print (
        'Not found' if None is mb2 else (
            'Word of given length found at index ' + str(mb2)
        )
    )
```

**Output:**

```
Word found at index 9
Word of given length found at index 10
```

### Python: Library

Python's `bisect` module provides binary search functions

```mw
index = bisect.bisect_left(list, item) # leftmost insertion point
index = bisect.bisect_right(list, item) # rightmost insertion point
index = bisect.bisect(list, item) # same as bisect_right

# same as above but actually insert the item into the list at the given place:
bisect.insort_left(list, item)
bisect.insort_right(list, item)
bisect.insort(list, item)
```

#### Python: Alternate

Complete binary search function with python's `bisect` module:

```mw
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
```

Returns the nearest item of list l to value.

```mw
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low + 1 < high:
        mid = (low+high)//2
        if l[mid] > value:
            high = mid
        elif l[mid] < value:
            low = mid
        else:
            return mid
    return high if abs(l[high] - value) < abs(l[low] - value) else low
```


## Quackery

Written from pseudocode for rightmost insertion point, iterative.

```mw
  [ stack ]                   is value.bs    (         --> n   )
  [ stack ]                   is nest.bs     (         --> n   )
  [ stack ]                   is test.bs     (         --> n   )

  [ ]'[ test.bs put
    value.bs put
    nest.bs put
    1 - swap
    [ 2dup < if done
      2dup + 1 >>
      nest.bs share over peek
      value.bs share swap
      test.bs share do iff
        [ 1 - unrot nip ]
        again
      [ 1+ nip ] again ]  
    drop
    nest.bs take over peek
    value.bs take 2dup swap
    test.bs share do
    dip [ test.bs take do ]
    or not
    dup dip [ not + ] ]       is bsearchwith ( n n [ x --> n b )

  [ dup echo
    over size 0 swap 2swap 
    bsearchwith < iff
      [ say " was identified as item " ]
    else
      [ say " could go into position " ]
    echo 
    say "." cr ]              is task        (     [ n --> n   )
```

**Output:**

Testing in the shell.

```
/O>   ' [ 10 20 30 40 50 60 70 80 90 ] 30 task
...   ' [ 10 20 30 40 50 60 70 80 90 ] 66 task
... 
30 was identified as item 2.
66 could go into position 6.

Stack empty.
```


## R

**Recursive**

```mw
BinSearch <- function(A, value, low, high) {
  if ( high < low ) {
    return(NULL)
  } else {
    mid <- floor((low + high) / 2)
    if ( A[mid] > value )
      BinSearch(A, value, low, mid-1)
    else if ( A[mid] < value )
      BinSearch(A, value, mid+1, high)
    else
      mid
  }
}
```

**Iterative**

```mw
IterBinSearch <- function(A, value) {
  low = 1
  high = length(A)
  i = 0
  while ( low <= high ) {
    mid <- floor((low + high)/2)
    if ( A[mid] > value )
      high <- mid - 1
    else if ( A[mid] < value )
      low <- mid + 1
    else
      return(mid)
  }
  NULL
}
```

**Example**

```mw
a <- 1:100
IterBinSearch(a, 50)
BinSearch(a, 50, 1, length(a)) # output 50
IterBinSearch(a, 101) # outputs NULL
```


## Racket

```mw
#lang racket
(define (binary-search x v)
  ; loop : index index -> index or #f
  ;   return i s.t. l<=i<h and v[i]=x
  (define (loop l h)
    (cond [(>= l h) #f]
          [else (define m (quotient (+ l h) 2))
                (define y (vector-ref v m))
                (cond 
                  [(> y x) (loop l (- m 1))]
                  [(< y x) (loop (+ m 1) h)]
                  [else m])]))
  (loop 0 (vector-length v)))
```

Examples:

```
(binary-search 6 #(1 3 4 5 6 7 8 9 10))  ; gives 4
(binary-search 6 #(1 3 4 5 7 8 9 10))    ; gives #f 
```


## Raku

(formerly Perl 6) With either of the below implementations of `binary_search`, one could write a function to search any object that does `Positional` this way:

```mw
sub search (@a, $x --> Int) {
    binary_search { $x cmp @a[$^i] }, 0, @a.end
}
```

**Iterative**

Works with

:

Rakudo

version 2015.12

```mw
sub binary_search (&p, Int $lo is copy, Int $hi is copy --> Int) {
    until $lo > $hi {
        my Int $mid = ($lo + $hi) div 2;
        given p $mid {
            when -1 { $hi = $mid - 1; } 
            when  1 { $lo = $mid + 1; }
            default { return $mid;    }
        }
    }
    fail;
}
```

**Recursive**

Translation of

:

Haskell

Works with

:

Rakudo

version 2015.12

```mw
sub binary_search (&p, Int $lo, Int $hi --> Int) {
    $lo <= $hi or fail;
    my Int $mid = ($lo + $hi) div 2;
    given p $mid {
        when -1 { binary_search &p, $lo,      $mid - 1 } 
        when  1 { binary_search &p, $mid + 1, $hi      }
        default { $mid                                 }
    }
}
```


## REXX

### recursive version

Incidentally, REXX doesn't care if the values in the list are integers (or even numbers), as long as they're in order. (includes the extra credit)

/*REXX program finds a value in a list of integers using an iterative binary search.*/ list=3 7 13 19 23 31 43 47 61 73 83 89 103 109 113 131 139 151 167 181 193 199,

```
 229 233 241 271 283 293 313 317 337 349 353 359 383 389 401 409 421 433 443,
 449 463 467 491 503 509 523 547 571 577 601 619 643 647 661 677 683 691 709,
 743 761 773 797 811 823 829 839 859 863 883 887 911 919 941 953 971 983 1013
```

/* [needle] a list of some low weak primes.*/ Parse Arg needle . /* get a # that's specified on t*/ If needle==*Then*

```
 Call exit '***error***  no argument specified.'
```

low=1 high=words(list) loc=binarysearch(low,high) If loc==-1 Then

```
 Call exit needle "wasn't found in the list."
```

Say needle "is in the list, its index is:" loc'.' Exit /*---------------------------------------------------------------------*/ binarysearch: Procedure Expose list needle

```
 Parse Arg i_low,i_high
 If i_high<i_low Then        /* the item wasn't found in the list     */
   Return-1
 i_mid=(i_low+i_high)%2      /* calculate the midpoint in the list    */
 y=word(list,i_mid)          /* obtain the midpoint value in the list */
 Select
   When y=needle Then
     Return i_mid
   When y>needle Then
     Return binarysearch(i_low,i_mid-1)
   Otherwise
     Return binarysearch(i_mid+1,i_high)
   End
```

exit: Say arg(1)

**output   when using the input of:     499.1**

```
499.1 wasn't found in the list.
```

**output   when using the input of:     619**

```
619 is in the list, its index is: 53.
```

### iterative version

(includes the extra credit)

```mw
/* REXX program finds a value in a list of integers                    */
/*  using an iterative binary search.                                  */
  list=3 7 13 19 23 31 43 47 61 73 83 89 103 109 113 131 139 151 167 181 193 199,
  229 233 241 271 283 293 313 317 337 349 353 359 383 389 401 409 421 433 443,
  449 463 467 491 503 509 523 547 571 577 601 619 643 647 661 677 683 691 709,
  743 761 773 797 811 823 829 839 859 863 883 887 911 919 941 953 971 983 1013
/* list: a list of some low weak primes.                               */
Parse Arg needle                      /* get a number to be looked for */
If needle=="" Then
  Call exit "***error***  no argument specified."
low=1
high=words(list)
Do While low<=high
  mid=(low+high)%2
  y=word(list,mid)
  Select
    When y=needle Then
      Call exit needle "is in the list, its index is:" mid'.'
    When y>needle Then         /* too high                             */
      high=mid-1               /* set upper nound                      */
    Otherwise                  /* too low                              */
      low=mid+1                /* set lower limit                      */
    End
  End
Call exit needle "wasn't found in the list."

exit: Say arg(1)
```

**output   when using the input of:     -314**

```
-314 wasn't found in the list.
```

**output   when using the input of:     619**

```
619 is in the list, its index is: 53.
```

### iterative version

(includes the extra credit)

```mw
/*REXX program finds a  value  in a  list of integers  using an iterative binary search.*/
@=  3   7  13  19  23  31  43  47  61  73  83  89 103 109 113 131 139 151 167 181,
  193 199 229 233 241 271 283 293 313 317 337 349 353 359 383 389 401 409 421 433,
  443 449 463 467 491 503 509 523 547 571 577 601 619 643 647 661 677 683 691 709,
  743 761 773 797 811 823 829 839 859 863 883 887 911 919 941 953 971 983 1013
                                                 /* [↑]  a list of some low weak primes.*/
parse arg ? .                                    /*get a  #  that's specified on the CL.*/
if ?==''  then do;    say;       say '***error***  no argument specified.';       say
                      exit 13
               end
 low= 1
high= words(@)
say  'arithmetic mean of the '   high    " values is: "   (word(@, 1) + word(@, high)) / 2
say
               do  while  low<=high;     mid= (low + high) % 2;            y= word(@, mid)

               if ?=y  then do;  say ?   ' is in the list, its index is: '    mid
                                 exit            /*stick a fork in it,  we're all done. */
                            end

               if y>?  then high= mid - 1        /*too high?                            */
                       else  low= mid + 1        /*too low?                             */
               end   /*while*/

say  ?   " wasn't found in the list."            /*stick a fork in it,  we're all done. */
```

**output   when using the input of:     -314**

```
arithmetic mean of the  79  values is:  508

-314  wasn't found in the list.
```

**output   when using the input of:     619**

```
arithmetic mean of the  79  values is:  508

619  is in the list, its index is:  53
```


## Ring

```mw
decimals(0)
array = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
 
find= 42
index = where(array,find,0,len(array))
if index >= 0 
   see "the value " + find+ " was found at index " + index
else
   see "the value " + find + " was not found"
ok

func where(a,s,b,t)
     h = 2
     while h<(t-b)
           h *= 2
     end
     h /= 2
     while h != 0
           if (b+h)<=t
              if s>=a[b+h]
                 b += h
              ok
           ok
           h /= 2
     end
     if s=a[b]
        return b-1
     else 
        return -1
     ok
```

Output:

```
the value 42 was found at index 6
```


## RISC-V Assembly

for Raspberry pi pico 2 see instructions to page risc v

```mw
# riscv assembly raspberry pico2 rp2350
# program binarysearch.s
# connexion putty com3
/*********************************************/
/*           CONSTANTES                      */
/********************************************/
/* for this file see risc-v task include a file */
.include "../../constantesRiscv.inc"

/****************************************************/
/* MACROS                   */
/****************************************************/
#.include "../ficmacrosriscv.inc"           # for debugging only

/*******************************************/
/* INITIALED DATAS                    */
/*******************************************/ 
.data
szMessStart:        .asciz "Program riscv start.\r\n"
szMessEnd:          .asciz "\nProgram end OK.\r\n"
szCariageReturn:    .asciz "\r\n"
szMessResult:       .asciz "Value found at index : "
szMessNotFound:     .asciz "Value not found. \r\n"

.align 2
TableNumber:        .int   -10,4,6,7,10,11,15,22,30,35
.equ NBELEMENTS1,   . - TableNumber
.equ NBELEMENTS,  NBELEMENTS1 / 4

.align 2
/*******************************************/ 
/*  UNINITIALED DATA                    */
/*******************************************/ 
.bss
.align 2
sConvArea:       .skip 24

/********************************...-..--*****/
/* SECTION CODE                              */
/**********************************************/
.text
.global main

main:
    call stdio_init_all        # général init
1:                             # start loop connexion 
    li a0,0                    # raz argument register
    call tud_cdc_n_connected   # waiting for USB connection
    beqz a0,1b                 # return code = zero ?
  
    la a0,szMessStart          # message address
    call writeString           # display message
    
    li a0,-10                  # find first value
    call testSearch
    li a0,35                    # find last value
    call testSearch
    li a0,10                    # find medium value
    call testSearch
    
    li a0,100                   # value not in array
    call testSearch
    li a0,-100                  # value not in array
    call testSearch

    la a0,szMessEnd
    call writeString
    call getchar
100:                           # final loop
    j 100b
/**********************************************/
/*   test   binary search                     */
/**********************************************/
/* a0    search value */
testSearch:                     # INFO: testSearch
    addi    sp, sp, -8         # reserve stack
    sw      ra, 0(sp)
    sw      s0,4(sp)
    mv s0,a0
    la a1,TableNumber
    li a2,NBELEMENTS
    call bsearch
    bltz a0,1f
    mv s0,a0
    la a0,szMessResult
    call writeString
    mv a0,s0
    la a1,sConvArea
    call conversion10
    la a0,sConvArea
    call writeString
   
    la a0,szCariageReturn
    call writeString
    j 100f
1:
    la a0,szMessNotFound
    call writeString
100:
    lw      ra, 0(sp)
    lw      s0, 4(sp)
    addi    sp, sp, 8
    ret  

/***************************************************/
/*   binary search */
/***************************************************/
/* a0 search  value           */
/* a1 array address */
/* a2 array size */
/* a0 return index or -1 if not find */
bsearch:                 # INFO: bsearch
    addi    sp, sp, -8   # save registres
    sw      ra, 0(sp)
    li t0,0              # low index
    addi t1,a2,-1        # high index N - 1
1:
    bgt t0,t1,99f        # not found
    add t2,t0,t1
    srli t2,t2,1         # compute (low+high)/ 2
    sh2add t3,t2,a1      # compute index address
    lw t4,(t3)           # load array value
    blt t4,a0,2f
    bgt t4,a0,3f
    mv a0,t2             # value found return index
    j 100f
2:                       # lower
    addi t0,t2,1         # low index = index + 1
    j 1b
3:                       # upper
    addi t1,t2,-1        # high index = index - 1
    j 1b
99:
    li a0,-1
100:    
    lw      ra, 0(sp)
    addi    sp, sp, 8
    ret 

/************************************/
/*     file include  Fonctions   */
/***********************************/
/* for this file see risc-v task include a file */
.include "../../includeFunctions.s"
```

```
Program riscv start.
Value found at index : 0
Value found at index : 9
Value found at index : 4
Value not found.
Value not found.

Program end OK.
```


## RPL

**Iterative**

If the searched value is not found, it returns the insertion point as a negative number.

Works with

:

RPL

version HP-48R

```
« → a value
  « 1 a SIZE 1 CF
    WHILE DUP2 ≤ 1 FC? AND REPEAT
       DUP2 + 2 / FLOOR
       CASE
          a OVER GET value > THEN SWAP DROP 1 - END
          a OVER GET value < THEN ROT DROP 1 + SWAP END
          1 SF 
       END 
    END
    IF 1 FS? THEN ROT ROT DROP2
             ELSE DROP NEG END
» » 'BINPOS' STO          @   ( { items } value → position )
```


## Ruby

**Recursive**

```mw
class Array
  def binary_search(val, low=0, high=(length - 1))
    return nil if high < low
    mid = (low + high) >> 1
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

[0,42,45,24324,99999].each do |val|
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
    low, high = 0, length - 1
    while low <= high
      mid = (low + high) >> 1
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

[0,42,45,24324,99999].each do |val|
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

**Built in** Since Ruby 2.0, arrays ship with a binary search method "bsearch":

```mw
haystack = [0,1,4,5,6,7,8,9,12,26,45,67,78,90,98,123,211,234,456,769,865,2345,3215,14345,24324]
needles = [0,42,45,24324,99999]

needles.select{|needle| haystack.bsearch{|hay| needle <=> hay} } # => [0, 45, 24324]
```

Which is 60% faster than "needles & haystack".


## Rust

**Iterative**

```mw
fn binary_search<T:PartialOrd>(searchvalue: T, v: &[T] ) -> Option<usize> {
    let mut lower = 0 as usize;
    let mut upper = v.len();
    while upper > lower {
        let mid = lower + (upper - lower) / 2;
        if v[mid] == searchvalue {
            return Some(mid);
        } else if searchvalue < v[mid] {
            upper = mid;
        } else {
            lower = mid + 1;
        }
    }
    None
}
```


## Scala

**Recursive**

```mw
def binarySearch[A <% Ordered[A]](a: IndexedSeq[A], v: A) = {
  def recurse(low: Int, high: Int): Option[Int] = (low + high) / 2 match {
    case _ if high < low => None
    case mid if a(mid) > v => recurse(low, mid - 1)
    case mid if a(mid) < v => recurse(mid + 1, high)
    case mid => Some(mid)
  }
  recurse(0, a.size - 1)
}
```

**Iterative**

```mw
def binarySearch[T](xs: Seq[T], x: T)(implicit ordering: Ordering[T]): Option[Int] = {
    var low: Int = 0
    var high: Int = xs.size - 1

    while (low <= high)
      low + high >>> 1 match {
        case guess if ordering.gt(xs(guess), x) => high = guess - 1 //too high
        case guess if ordering.lt(xs(guess), x) => low = guess + 1 // too low
        case guess => return Some(guess) //found it
      }
    None //not found
  }
```

**Test**

```mw
def testBinarySearch(n: Int) = {
  val odds = 1 to n by 2
  val result = (0 to n).flatMap(binarySearch(odds, _))
  assert(result == (0 until odds.size))
  println(s"$odds are odd natural numbers")
  for (it <- result)
    println(s"$it is ordinal of ${odds(it)}")
}

def main() = testBinarySearch(12)
```

Output:

```
Range(1, 3, 5, 7, 9, 11) are odd natural numbers
0 is ordinal of 1
1 is ordinal of 3
2 is ordinal of 5
3 is ordinal of 7
4 is ordinal of 9
5 is ordinal of 11
```


## Scheme

**Recursive**

```mw
(define (binary-search value vector)
  (let helper ((low 0)
               (high (- (vector-length vector) 1)))
    (if (< high low)
        #f
        (let ((middle (quotient (+ low high) 2)))
          (cond ((> (vector-ref vector middle) value)
                 (helper low (- middle 1)))
                ((< (vector-ref vector middle) value)
                 (helper (+ middle 1) high))
                (else middle))))))
```

Example:

```
> (binary-search 6 '#(1 3 4 5 6 7 8 9 10))
4
> (binary-search 2 '#(1 3 4 5 6 7 8 9 10))
#f
```

The calls to helper are in tail position, so since Scheme implementations support proper tail-recursion the computation proces is iterative.


## Seed7

**Iterative**

```mw
const func integer: binarySearchIterative (in array elemType: arr, in elemType: aKey) is func
  result
    var integer: result is 0;
  local
    var integer: low is 1;
    var integer: high is 0;
    var integer: middle is 0;
  begin
    high := length(arr);
    while result = 0 and low <= high do
      middle := low + (high - low) div 2;
      if aKey < arr[middle] then
        high := pred(middle);
      elsif aKey > arr[middle] then
        low := succ(middle);
      else
        result := middle;
      end if;
    end while;
  end func;
```

**Recursive**

```mw
const func integer: binarySearch (in array elemType: arr, in elemType: aKey, in integer: low, in integer: high) is func
  result
    var integer: result is 0;
  begin
    if low <= high then
      result := (low + high) div 2;
      if aKey < arr[result] then
        result := binarySearch(arr, aKey, low, pred(result)); # search left
      elsif aKey > arr[result] then
        result := binarySearch(arr, aKey, succ(result), high); # search right
      end if;
    end if;
  end func;

const func integer: binarySearchRecursive (in array elemType: arr, in elemType: aKey) is
  return binarySearch(arr, aKey, 1, length(arr));
```


## SequenceL

**Recursive**

```mw
binarySearch(A(1), value(0), low(0), high(0)) :=
	let
		mid := low + (high - low) / 2;
	in
			-1 when high < low //Not Found
		else
			binarySearch(A, value, low, mid - 1) when A[mid] > value
		else
			binarySearch(A, value, mid + 1, high) when A[mid] < value
		else
			mid;
```


## Sidef

Iterative:

```mw
func binary_search(a, i) {
 
    var l = 0
    var h = a.end
 
    while (l <= h) {
        var mid = (h+l / 2 -> int)
        a[mid] > i && (h = mid-1; next)
        a[mid] < i && (l = mid+1; next)
        return mid
    }
 
    return -1
}
```

Recursive:

```mw
func binary_search(arr, value, low=0, high=arr.end) {
    high < low && return -1
    var middle = ((high+low) // 2)

    given (arr[middle]) { |item|
        case (value < item) {
            binary_search(arr, value, low, middle-1)
        }
        case (value > item) {
            binary_search(arr, value, middle+1, high)
        }
        case (value == item) {
            middle
        }
    }
}
```

Usage:

```mw
say binary_search([34, 42, 55, 778], 55);       #=> 2
```
