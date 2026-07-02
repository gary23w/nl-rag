---
title: "Sorting algorithms/Quicksort (part 6/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/8
---

## Modula-3

This code is taken from libm3, which is basically Modula-3's "standard library". Note that this code uses Insertion sort when the array is less than 9 elements long.

```mw
GENERIC INTERFACE ArraySort(Elem);

PROCEDURE Sort(VAR a: ARRAY OF Elem.T; cmp := Elem.Compare);

END ArraySort.
```

```mw
GENERIC MODULE ArraySort (Elem);

PROCEDURE Sort (VAR a: ARRAY OF Elem.T;  cmp := Elem.Compare) =
  BEGIN
    QuickSort (a, 0, NUMBER (a), cmp);
    InsertionSort (a, 0, NUMBER (a), cmp);
  END Sort;

PROCEDURE QuickSort (VAR a: ARRAY OF Elem.T;  lo, hi: INTEGER;
                     cmp := Elem.Compare) =
  CONST CutOff = 9;
  VAR i, j: INTEGER;  key, tmp: Elem.T;
  BEGIN
    WHILE (hi - lo > CutOff) DO (* sort a[lo..hi) *)

      (* use median-of-3 to select a key *)
      i := (hi + lo) DIV 2;
      IF cmp (a[lo], a[i]) < 0 THEN
        IF cmp (a[i], a[hi-1]) < 0 THEN
          key := a[i];
        ELSIF cmp (a[lo], a[hi-1]) < 0 THEN
          key := a[hi-1];  a[hi-1] := a[i];  a[i] := key;
        ELSE
          key := a[lo];  a[lo] := a[hi-1];  a[hi-1] := a[i];  a[i] := key;
        END;
      ELSE (* a[lo] >= a[i] *)
        IF cmp (a[hi-1], a[i]) < 0 THEN
          key := a[i];  tmp := a[hi-1];  a[hi-1] := a[lo];  a[lo] := tmp;
        ELSIF cmp (a[lo], a[hi-1]) < 0 THEN
          key := a[lo];  a[lo] := a[i];  a[i] := key;
        ELSE
          key := a[hi-1];  a[hi-1] := a[lo];  a[lo] := a[i];  a[i] := key;
        END;
      END;

      (* partition the array *)
      i := lo+1;  j := hi-2;

      (* find the first hole *)
      WHILE cmp (a[j], key) > 0 DO DEC (j) END;
      tmp := a[j];
      DEC (j);

      LOOP
        IF (i > j) THEN EXIT END;

        WHILE i < hi AND cmp (a[i], key) < 0 DO INC (i) END;
        IF (i > j) THEN EXIT END;
        a[j+1] := a[i];
        INC (i);

        WHILE j > lo AND cmp (a[j], key) > 0 DO DEC (j) END;
        IF (i > j) THEN  IF (j = i-1) THEN  DEC (j)  END;  EXIT  END;
        a[i-1] := a[j];
        DEC (j);
      END;

      (* fill in the last hole *)
      a[j+1] := tmp;
      i := j+2;

      (* then, recursively sort the smaller subfile *)
      IF (i - lo < hi - i)
        THEN  QuickSort (a, lo, i-1, cmp);   lo := i;
        ELSE  QuickSort (a, i, hi, cmp);     hi := i-1;
      END;

    END; (* WHILE (hi-lo > CutOff) *)
  END QuickSort;

PROCEDURE InsertionSort (VAR a: ARRAY OF Elem.T;  lo, hi: INTEGER;
                         cmp := Elem.Compare) =
  VAR j: INTEGER;  key: Elem.T;
  BEGIN
    FOR i := lo+1 TO hi-1 DO
      key := a[i];
      j := i-1;
      WHILE (j >= lo) AND cmp (key, a[j]) < 0 DO
        a[j+1] := a[j];
        DEC (j);
      END;
      a[j+1] := key;
    END;
  END InsertionSort;

BEGIN
END ArraySort.
```

To use this generic code to sort an array of text, we create two files called TextSort.i3 and TextSort.m3, respectively.

```mw
INTERFACE TextSort = ArraySort(Text) END TextSort.
```

```mw
MODULE TextSort = ArraySort(Text) END TextSort.
```

Then, as an example:

```mw
MODULE Main;

IMPORT IO, TextSort;

VAR arr := ARRAY [1..10] OF TEXT {"Foo", "bar", "!ooF", "Modula-3", "hickup", 
                                 "baz", "quuz", "Zeepf", "woo", "Rosetta Code"};

BEGIN
  TextSort.Sort(arr);
  FOR i := FIRST(arr) TO LAST(arr) DO
    IO.Put(arr[i] & "\n");
  END;
END Main.
```


## Mond

Implements the simple quicksort algorithm.

```mw
fun quicksort( arr, cmp )
{
    if( arr.length() < 2 )
        return arr;
    
    if( !cmp )
        cmp = ( a, b ) -> a - b;
    
    var a = [ ], b = [ ];
    var pivot = arr[0];
    var len = arr.length();
    
    for( var i = 1; i < len; ++i )
    {
        var item = arr[i];
        
        if( cmp( item, pivot ) < cmp( pivot, item ) )
            a.add( item );
        else
            b.add( item );
    }
    
    a = quicksort( a, cmp );
    b = quicksort( b, cmp );
    
    a.add( pivot );
    
    foreach( var item in b )
        a.add( item );
    
    return a;
}
```

**Usage**

```mw
var array = [ 532, 16, 153, 3, 63.60, 925, 0.214 ];
var sorted = quicksort( array );

printLn( sorted );
```

**Output:**

```
[
  0.214,
  3,
  16,
  63.6,
  153,
  532,
  925
]
```


## MUMPS

Shows quicksort on a 16-element array.

```mw
main 
 new collection,size
 set size=16
 set collection=size for i=0:1:size-1 set collection(i)=$random(size)
 write "Collection to sort:",!!
 zwrite collection ; This will only work on Intersystem's flavor of MUMPS
 do quicksort(.collection,0,collection-1)
 write:$$isSorted(.collection) !,"Collection is sorted:",!!
 zwrite collection  ; This will only work on Intersystem's flavor of MUMPS
 q
quicksort(array,low,high)
 if low<high do  
 . set pivot=$$partition(.array,low,high)
 . do quicksort(.array,low,pivot-1)
 . do quicksort(.array,pivot+1,high)
 q
partition(A,p,r)
 set pivot=A(r)
 set i=p-1
 for j=p:1:r-1 do  
 . i A(j)<=pivot do  
 . . set i=i+1
 . . set helper=A(j)
 . . set A(j)=A(i)
 . . set A(i)=helper
 set helper=A(r)
 set A(r)=A(i+1)
 set A(i+1)=helper
 quit i+1
isSorted(array)
 set sorted=1
 for i=0:1:array-2 do  quit:sorted=0
 . for j=i+1:1:array-1 do  quit:sorted=0
 . . set:array(i)>array(j) sorted=0
 quit sorted
```

**Usage**

```mw
 do main()
```

**Output:**

```
Collection to sort:

collection=16
collection(0)=4
collection(1)=0
collection(2)=6
collection(3)=14
collection(4)=4
collection(5)=0
collection(6)=10
collection(7)=5
collection(8)=11
collection(9)=4
collection(10)=12
collection(11)=9
collection(12)=13
collection(13)=4
collection(14)=14
collection(15)=0

Collection is sorted:

collection=16
collection(0)=0
collection(1)=0
collection(2)=0
collection(3)=4
collection(4)=4
collection(5)=4
collection(6)=4
collection(7)=5
collection(8)=6
collection(9)=9
collection(10)=10
collection(11)=11
collection(12)=12
collection(13)=13
collection(14)=14
collection(15)=14
```


## Nanoquery

Translation of

:

Python

```mw
def quickSort(arr)
   less = {}
   pivotList = {}
   more = {}
   if len(arr) <= 1
      return arr
   else
      pivot = arr[0]
      for i in arr
         if i < pivot
            less.append(i)
         else if i > pivot
            more.append(i)
         else
            pivotList.append(i)
         end
      end
      
      less = quickSort(less)
      more = quickSort(more)
      
      return less + pivotList + more
   end
end
```


## Nemerle

Translation of

:

Haskell

A little less clean and concise than Haskell, but essentially the same.

```mw
using System;
using System.Console;
using Nemerle.Collections.NList;

module Quicksort
{
    Qsort[T] (x : list[T]) : list[T]
      where T : IComparable
    {
        |[]    => []
        |x::xs => Qsort($[y|y in xs, (y.CompareTo(x) < 0)]) + [x] + Qsort($[y|y in xs, (y.CompareTo(x) > 0)])
    }
    
    Main() : void
    {
        def empty = [];
        def single = [2];
        def several = [2, 6, 1, 7, 3, 9, 4];
        WriteLine(Qsort(empty));
        WriteLine(Qsort(single));
        WriteLine(Qsort(several));
    }
}
```


## NetRexx

This sample implements both the **simple** and **in place** algorithms as described in the task's description:

```mw
/* NetRexx */
options replace format comments java crossref savelog symbols binary

import java.util.List

placesList = [String -
    "UK  London",     "US  New York",   "US  Boston",     "US  Washington" -
  , "UK  Washington", "US  Birmingham", "UK  Birmingham", "UK  Boston"     -
]
lists = [ -
    placesList -
  , quickSortSimple(String[] Arrays.copyOf(placesList, placesList.length)) -
  , quickSortInplace(String[] Arrays.copyOf(placesList, placesList.length)) -
]

loop ln = 0 to lists.length - 1
  cl = lists[ln]
  loop ct = 0 to cl.length - 1
    say cl[ct]
    end ct
    say
  end ln

return

method quickSortSimple(array = String[]) public constant binary returns String[]

  rl = String[array.length]
  al = List quickSortSimple(Arrays.asList(array))
  al.toArray(rl)

  return rl

method quickSortSimple(array = List) public constant binary returns ArrayList

  if array.size > 1 then do
    less    = ArrayList()
    equal   = ArrayList()
    greater = ArrayList()

    pivot = array.get(Random().nextInt(array.size - 1))
    loop x_ = 0 to array.size - 1
      if (Comparable array.get(x_)).compareTo(Comparable pivot) < 0 then less.add(array.get(x_))
      if (Comparable array.get(x_)).compareTo(Comparable pivot) = 0 then equal.add(array.get(x_))
      if (Comparable array.get(x_)).compareTo(Comparable pivot) > 0 then greater.add(array.get(x_))
      end x_
    less    = quickSortSimple(less)
    greater = quickSortSimple(greater)
    out = ArrayList(array.size)
    out.addAll(less)
    out.addAll(equal)
    out.addAll(greater)

    array = out
    end

  return ArrayList array

method quickSortInplace(array = String[]) public constant binary returns String[]

  rl = String[array.length]
  al = List quickSortInplace(Arrays.asList(array))
  al.toArray(rl)

  return rl

method quickSortInplace(array = List, ixL = int 0, ixR = int array.size - 1) public constant binary returns ArrayList

  if ixL < ixR then do
    ixP = int ixL + (ixR - ixL) % 2
    ixP = quickSortInplacePartition(array, ixL, ixR, ixP)
    quickSortInplace(array, ixL, ixP - 1)
    quickSortInplace(array, ixP + 1, ixR)
    end

  array = ArrayList(array)
  return ArrayList array

method quickSortInplacePartition(array = List, ixL = int, ixR = int, ixP = int) public constant binary returns int

  pivotValue = array.get(ixP)
  rValue     = array.get(ixR)
  array.set(ixP, rValue)
  array.set(ixR, pivotValue)
  ixStore = ixL
  loop i_ = ixL to ixR - 1
    iValue = array.get(i_)
    if (Comparable iValue).compareTo(Comparable pivotValue) < 0 then do
      storeValue = array.get(ixStore)
      array.set(i_, storeValue)
      array.set(ixStore, iValue)
      ixStore = ixStore + 1
      end
    end i_
  storeValue = array.get(ixStore)
  rValue     = array.get(ixR)
  array.set(ixStore, rValue)
  array.set(ixR, storeValue)

  return ixStore
```

**Output:**

```
UK  London
US  New York
US  Boston
US  Washington
UK  Washington
US  Birmingham
UK  Birmingham
UK  Boston

UK  Birmingham
UK  Boston
UK  London
UK  Washington
US  Birmingham
US  Boston
US  New York
US  Washington

UK  Birmingham
UK  Boston
UK  London
UK  Washington
US  Birmingham
US  Boston
US  New York
US  Washington
```


## Nial

```mw
quicksort is fork [ >= [1 first,tally],
  pass,
  link [
      quicksort sublist [ < [pass, first], pass ],
      sublist [ match [pass,first],pass ],
      quicksort sublist [ > [pass,first], pass ]
  ]
]
```

Using it.

```mw
|quicksort [5, 8, 7, 4, 3]
=3 4 5 7 8
```


## Nim

### Procedural (in place) algorithm

```mw
proc quickSortImpl[T](a: var openarray[T], start, stop: int) =
  if stop - start > 0:
    let pivot = a[start]
    var left = start
    var right = stop
    while left <= right:
      while cmp(a[left], pivot) < 0:
        inc(left)
      while cmp(a[right], pivot) > 0:
        dec(right)
      if left <= right:
        swap(a[left], a[right])
        inc(left)
        dec(right)
    quickSortImpl(a, start, right)
    quickSortImpl(a, left, stop)

proc quickSort[T](a: var openarray[T]) =
  quickSortImpl(a, 0, a.len - 1)

var a = @[4, 65, 2, -31, 0, 99, 2, 83, 782]
a.quickSort()
echo a
```

### Functional (inmmutability) algorithm

```mw
import sequtils,sugar

func sorted[T](xs:seq[T]): seq[T] =
  if xs.len==0: @[] else: concat(
    xs[1..^1].filter(x=>x<xs[0]).sorted,
    @[xs[0]],
    xs[1..^1].filter(x=>x>=xs[0]).sorted
  )

@[4, 65, 2, -31, 0, 99, 2, 83, 782].sorted.echo
```

**Output:**

```
@[-31, 0, 2, 2, 4, 65, 83, 99, 782]
```


## Nix

```mw
let
  qs = l:
    if l == [] then []
    else
      with builtins;
      let x  = head l;
          xs = tail l;
          low  = filter (a: a < x)  xs;
          high = filter (a: a >= x) xs;
      in qs low ++ [x] ++ qs high;
in
  qs [4 65 2 (-31) 0 99 83 782]
```

**Output:**

```
[ -31 0 2 4 65 83 99 782 ]
```


## Oberon-2

Translation of

:

Pascal

```mw
MODULE QS;

IMPORT Out;
    
TYPE
  TItem = INTEGER;
  
CONST
  N = 10;
  
VAR
  I:LONGINT;
  A:ARRAY N OF INTEGER;
  
PROCEDURE Init(VAR A:ARRAY OF TItem);
BEGIN
  A[0] := 4; A[1] := 65; A[2] := 2; A[3] := -31; A[4] := 0;
  A[5] := 99; A[6] := 2; A[7] := 83; A[8] := 782; A[9] := 1;
END Init;

PROCEDURE QuickSort(VAR A:ARRAY OF TItem; Left,Right:LONGINT);
VAR
  I,J:LONGINT;
  Pivot,Temp:TItem;
BEGIN
  I := Left;
  J := Right;
  Pivot := A[(Left + Right) DIV 2];
  REPEAT
    WHILE Pivot > A[I] DO INC(I) END;
    WHILE Pivot < A[J] DO DEC(J) END;
    IF I <= J THEN
      Temp := A[I];
      A[I] := A[J];
      A[J] := Temp;
      INC(I);
      DEC(J);
    END;
  UNTIL I > J;
  IF Left < J THEN QuickSort(A, Left, J) END;
  IF I < Right THEN QuickSort(A, I, Right) END;
END QuickSort;
  
BEGIN
  Init(A);
  FOR I := 0 TO LEN(A)-1 DO
    Out.Int(A[I], 0); Out.Char(' ');
  END;
  Out.Ln;
  QuickSort(A, 0, LEN(A)-1);
  FOR I := 0 TO LEN(A)-1 DO
    Out.Int(A[I], 0); Out.Char(' ');
  END;
  Out.Ln;
END QS.
```


## Objeck

```mw
class QuickSort {
  function : Main(args : String[]) ~ Nil {
    array := [1, 3, 5, 7, 9, 8, 6, 4, 2];
    Sort(array);
    each(i : array) {
      array[i]->PrintLine();
    };
  }

  function : Sort(array : Int[]) ~ Nil {
    size := array->Size();
    if(size <= 1) {
      return;
    };
    Sort(array, 0, size - 1);
  }

  function : native : Sort(array : Int[], low : Int, high : Int) ~ Nil {
    i := low; j := high;
    pivot := array[low + (high-low)/2];

    while(i <= j) {
      while(array[i] < pivot) {
        i+=1;
      };

      while(array[j] > pivot) {
        j-=1;
      };

      if (i <= j) {
        temp := array[i];
        array[i] := array[j];
        array[j] := temp;
        i+=1; j-=1;
      };
    };

    if(low < j) {
      Sort(array, low, j);
    };

    if(i < high) {
      Sort(array, i, high);
    };
  }
}
```


## Objective-C

The latest XCode compiler is assumed with ARC enabled.

```mw
void quicksortInPlace(NSMutableArray *array, NSInteger first, NSInteger last, NSComparator comparator) {
    if (first >= last) return;
    id pivot = array[(first + last) / 2];
    NSInteger left = first;
    NSInteger right = last;
    while (left <= right) {
        while (comparator(array[left], pivot) == NSOrderedAscending)
            left++;
        while (comparator(array[right], pivot) == NSOrderedDescending)
            right--;
        if (left <= right)
            [array exchangeObjectAtIndex:left++ withObjectAtIndex:right--];
    }
    quicksortInPlace(array, first, right, comparator);
    quicksortInPlace(array, left, last, comparator);
}

NSArray* quicksort(NSArray *unsorted, NSComparator comparator) {
    NSMutableArray *a = [NSMutableArray arrayWithArray:unsorted];
    quicksortInPlace(a, 0, a.count - 1, comparator);
    return a;
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSArray *a = @[ @1, @3, @5, @7, @9, @8, @6, @4, @2 ];
        NSLog(@"Unsorted: %@", a);
        NSLog(@"Sorted: %@", quicksort(a, ^(id x, id y) { return [x compare:y]; }));
        NSArray *b = @[ @"Emil", @"Peg", @"Helen", @"Juergen", @"David", @"Rick", @"Barb", @"Mike", @"Tom" ];
        NSLog(@"Unsorted: %@", b);
        NSLog(@"Sorted: %@", quicksort(b, ^(id x, id y) { return [x compare:y]; }));
    }
    return 0;
}
```

**Output:**

```
Unsorted: (
    1,
    3,
    5,
    7,
    9,
    8,
    6,
    4,
    2
)
Sorted: (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
)
Unsorted: (
    Emil,
    Peg,
    Helen,
    Juergen,
    David,
    Rick,
    Barb,
    Mike,
    Tom
)
Sorted: (
    Barb,
    David,
    Emil,
    Helen,
    Juergen,
    Mike,
    Peg,
    Rick,
    Tom
)
```


## OCaml

### Declarative and purely functional

```mw
let rec quicksort gt = function
  | [] -> []
  | x::xs ->
      let ys, zs = List.partition (gt x) xs in
      (quicksort gt ys) @ (x :: (quicksort gt zs))
 
let _ =
  quicksort (>) [4; 65; 2; -31; 0; 99; 83; 782; 1]
```

The list based implementation is elegant and perspicuous, but inefficient in time (because `partition` and `@` are linear) and in space (since it creates numerous new lists along the way).

### Imperative and in place

Using aliased array slices from the Containers library.

```mw
  module Slice = CCArray_slice

  let quicksort : int Array.t -> unit = fun arr ->
    let rec quicksort' : int Slice.t -> unit = fun slice ->
      let len = Slice.length slice in

      if len > 1 then begin
        let pivot = Slice.get slice (len / 2)
        and i = ref 0
        and j = ref (len - 1)
        in
        while !i < !j do
          while Slice.get slice !i < pivot do incr i done;
          while Slice.get slice !j > pivot do decr j done;

          if !i < !j then begin
            let i_val = Slice.get slice !i in
            Slice.set slice !i (Slice.get slice !j);
            Slice.set slice !j i_val;

            incr i;
            decr j;
          end
        done;

        quicksort' (Slice.sub slice 0 !i);
        quicksort' (Slice.sub slice !i (len - !i));
      end
    in
    (* Take the array into an aliased array slice *)
    Slice.full arr |> quicksort'
```


## Octave

Translation of

:

MATLAB

(The MATLAB version works as is in Octave, provided that the code is put in a file named quicksort.m, and everything below the return must be typed in the prompt of course)

```mw
function f=quicksort(v)                       % v must be a column vector
  f = v; n=length(v);
  if(n > 1)
     vl = min(f); vh = max(f);                  % min, max
     p  = (vl+vh)*0.5;                          % pivot
     ia = find(f < p); ib = find(f == p); ic=find(f > p);
     f  = [quicksort(f(ia)); f(ib); quicksort(f(ic))];
  end
endfunction
 
N=30; v=rand(N,1); tic,u=quicksort(v); toc
u
```


## Oforth

Oforth built-in sort uses quick sort algorithm (see lang/collect/ListBuffer.of for implementation) :

```mw
[ 5, 8, 2, 3, 4, 1 ] sort
```


## Ol

```mw
(define (quicksort l ??)
  (if (null? l)
      '()
      (append (quicksort (filter (lambda (x) (?? (car l) x)) (cdr l)) ??)
              (list (car l))
              (quicksort (filter (lambda (x) (not (?? (car l) x))) (cdr l)) ??))))
 
(print 
   (quicksort (list 1 3 5 9 8 6 4 3 2) >))
(print 
   (quicksort (iota 100) >))
(print 
   (quicksort (iota 100) <))
```

**Output:**

```
(1 2 3 3 4 5 6 8 9)
(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99)
(99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0)
```


## ooRexx

Translation of

:

Python

```mw
    a = .array~Of(4, 65, 2, -31, 0, 99, 83, 782, 1)
    say 'before:' a~toString( ,', ')
    a = quickSort(a)
    say ' after:' a~toString( ,', ')
    exit

::routine quickSort
    use arg arr -- the array to be sorted
    less = .array~new
    pivotList = .array~new
    more = .array~new
    if arr~items <= 1 then
        return arr
    else do
        pivot = arr[1]
        do i over arr
            if i < pivot then
                less~append(i)
            else if i > pivot then
                more~append(i)
            else
                pivotList~append(i)
        end
        less = quickSort(less)
        more = quickSort(more)
        return less~~appendAll(pivotList)~~appendAll(more)
    end
```

**Output:**

```
before: 4, 65, 2, -31, 0, 99, 83, 782, 1
 after: -31, 0, 1, 2, 4, 65, 83, 99, 782 
```


## Oz

```mw
declare
  fun {QuickSort Xs}
     case Xs of nil then nil
     [] Pivot|Xr then
   fun {IsSmaller X} X < Pivot end
        Smaller Larger
     in
   {List.partition Xr IsSmaller ?Smaller ?Larger}
        {Append {QuickSort Smaller} Pivot|{QuickSort Larger}}
     end
  end
in
  {Show {QuickSort [3 1 4 1 5 9 2 6 5]}}
```


## PARI/GP

```mw
quickSort(v)={
  if(#v<2, return(v));
  my(less=List(),more=List(),same=List(),pivot);
  pivot=median([v[random(#v)+1],v[random(#v)+1],v[random(#v)+1]]); \\ Middle-of-three
  for(i=1,#v,
    if(v[i]<pivot,
      listput(less, v[i]),
      if(v[i]==pivot, listput(same, v[i]), listput(more, v[i]))
    )
  );
  concat(quickSort(Vec(less)), concat(Vec(same), quickSort(Vec(more))))
};
median(v)={
  vecsort(v)[#v>>1]
};
```


## Pascal

Works with

:

FPC

```mw
program QSortDemo;

{$mode objfpc}{$h+}{$b-}

procedure QuickSort(var A: array of Integer);
  procedure QSort(L, R: Integer);
  var
    I, J, Tmp, Pivot: Integer;
  begin
    if R - L < 1 then exit;
    I := L; J := R;
    {$push}{$q-}{$r-}Pivot := A[(L + R) shr 1];{$pop}
    repeat
      while A[I] < Pivot do Inc(I);
      while A[J] > Pivot do Dec(J);
      if I <= J then begin
        Tmp := A[I];
        A[I] := A[J];
        A[J] := Tmp;
        Inc(I); Dec(J);
      end;
    until I > J;
    QSort(L, J);
    QSort(I, R);
  end;
begin
  QSort(0, High(A));
end;

procedure PrintArray(const A: array of Integer);
var
  I: Integer;
begin
  Write('[');
  for I := 0 to High(A) - 1 do
    Write(A[I], ', ');
  WriteLn(A[High(A)], ']');
end;

var
  a: array[-7..6] of Integer = (-34, -20, 30, 13, 36, -10, 5, -25, 9, 19, 35, -50, 29, 11);
begin
  QuickSort(a);
  PrintArray(a);
end.
```

**Output:**

```
[-50, -34, -25, -20, -10, 5, 9, 11, 13, 19, 29, 30, 35, 36]
```


## PascalABC.NET

```mw
function Partition(a: array of integer; l,r: integer): integer;
begin
  var i := l - 1;
  var j := r + 1;
  var x := a[l];
  while True do
  begin
    repeat
      i += 1;
    until a[i]>=x;
    repeat
      j -= 1;
    until a[j]<=x;
    if i<j then 
      Swap(a[i],a[j])
    else 
    begin
      Result := j;
      exit;
    end;
  end;
end;
  
procedure QuickSort(a: array of integer; l,r: integer);
begin
  if l>=r then exit;
  var j := Partition(a,l,r);
  QuickSort(a,l,j);
  QuickSort(a,j+1,r);
end;

const n = 20;

begin
  var a := ArrRandom(n);
  Println('Before: ');
  Println(a);
  QuickSort(a,0,a.Length-1);
  Println('After sorting: ');
  Println(a);
end.
```

**Output:**

```
Before: 
[67,95,79,96,14,56,25,9,4,56,70,62,33,52,13,12,73,19,8,72]
After sorting: 
[4,8,9,12,13,14,19,25,33,52,56,56,62,67,70,72,73,79,95,96]
```


## Perl

```mw
sub quick_sort {
    return @_ if @_ < 2;
    my $p = splice @_, int rand @_, 1;
    quick_sort(grep $_ < $p, @_), $p, quick_sort(grep $_ >= $p, @_);
}

my @a = (4, 65, 2, -31, 0, 99, 83, 782, 1);
@a = quick_sort @a;
print "@a\n";
```


## Phix

```
with javascript_semantics

function quick_sort(sequence x)
--
-- put x into ascending order using recursive quick sort
--
    integer n = length(x)
    if n<2 then
        return x    -- already sorted (trivial case)
    end if
 
    integer mid = floor((n+1)/2),
            last = 1
    object midval = x[mid]
    x[mid] = x[1]
    for i=2 to n do
        object xi = x[i]
        if xi<midval then
            last += 1
            x[i] = x[last]
            x[last] = xi
        end if
    end for
 
    return quick_sort(x[2..last]) & {midval} & quick_sort(x[last+1..n])
end function
 
?quick_sort({5,"oranges","and",3,"apples"})
```

**Output:**

```
{3,5,"and","apples","oranges"}
```


## PHP

```mw
function quicksort($arr){
   $lte = $gt = array();
   if(count($arr) < 2){
      return $arr;
   }
   $pivot_key = key($arr);
   $pivot = array_shift($arr);
   foreach($arr as $val){
      if($val <= $pivot){
         $lte[] = $val;
      } else {
         $gt[] = $val;
      }
   }
   return array_merge(quicksort($lte),array($pivot_key=>$pivot),quicksort($gt));
}

$arr = array(1, 3, 5, 7, 9, 8, 6, 4, 2);
$arr = quicksort($arr);
echo implode(',',$arr);
```

```
1,2,3,4,5,6,7,8,9
```

```mw
function quickSort(array $array) {
    // base case
    if (empty($array)) {
        return $array;
    }
    $head = array_shift($array);
    $tail = $array;
    $lesser = array_filter($tail, function ($item) use ($head) {
        return $item <= $head;
    });
    $bigger = array_filter($tail, function ($item) use ($head) {
        return $item > $head;
    });
    return array_merge(quickSort($lesser), [$head], quickSort($bigger));
}
$testCase = [1, 4, 8, 2, 8, 0, 2, 8];
$result = quickSort($testCase);
echo sprintf("[%s] ==> [%s]\n", implode(', ', $testCase), implode(', ', $result));
```

```
[1, 4, 8, 2, 8, 0, 2, 8] ==> [0, 1, 2, 2, 4, 8, 8, 8]
```


## Picat

### Function

```mw
qsort([])    = [].
qsort([H|T]) = qsort([E : E in T, E =< H]) 
               ++ [H] ++
               qsort([E : E in T, E > H]).
```

### Recursion

Translation of

:

Prolog

```mw
qsort( [], [] ).
qsort( [H|U], S ) :-
  splitBy(H, U, L, R),
  qsort(L, SL),
  qsort(R, SR),
  append(SL, [H|SR], S).
 
% splitBy( H, U, LS, RS )
% True if LS = { L in U | L <= H }; RS = { R in U | R > H }
splitBy( _, [], [], []).
splitBy( H, [U|T], [U|LS], RS ) :- U =< H, splitBy(H, T, LS, RS).
splitBy( H, [U|T], LS, [U|RS] ) :- U  > H, splitBy(H, T, LS, RS).
```


## PicoLisp

```mw
(de quicksort (L)
   (if (cdr L)
      (let Pivot (car L)
          (append (quicksort (filter '((A) (< A Pivot)) (cdr L)))
                             (filter '((A) (= A Pivot))      L )
                  (quicksort (filter '((A) (> A Pivot)) (cdr L)))) )
      L) )
```


## PL/I

```mw
DCL (T(20)) FIXED BIN(31);   /* scratch space of length N */

QUICKSORT: PROCEDURE (A,AMIN,AMAX,N) RECURSIVE ;
   DECLARE (A(*))              FIXED BIN(31);
   DECLARE (N,AMIN,AMAX)       FIXED BIN(31) NONASGN;
   DECLARE (I,J,IA,IB,IC,PIV)  FIXED BIN(31);
   DECLARE (P,Q)               POINTER;
   DECLARE (AP(1))             FIXED BIN(31) BASED(P);
   
   IF(N <= 1)THEN RETURN;
   IA=0; IB=0; IC=N+1;
   PIV=(AMIN+AMAX)/2;
   DO I=1 TO N;
      IF(A(I) < PIV)THEN DO;
         IA+=1; A(IA)=A(I);
      END; ELSE IF(A(I) > PIV) THEN DO;
         IC-=1; T(IC)=A(I);
      END; ELSE DO;
         IB+=1; T(IB)=A(I);
      END;
   END;
   DO I=1  TO IB; A(I+IA)=T(I);   END;
   DO I=IC TO N;  A(I)=T(N+IC-I); END;
   P=ADDR(A(IC));
   IC=N+1-IC;
   IF(IA > 1) THEN CALL QUICKSORT(A, AMIN, PIV-1,IA);
   IF(IC > 1) THEN CALL QUICKSORT(AP,PIV+1,AMAX, IC);
   RETURN;
END QUICKSORT;
 MINMAX: PROC(A,AMIN,AMAX,N);
   DCL (AMIN,AMAX) FIXED BIN(31),
       (N,A(*))    FIXED BIN(31) NONASGN ;
   DCL (I,X,Y) FIXED BIN(31);
   
   AMIN=A(N); AMAX=AMIN;
   DO I=1 TO N-1;
      X=A(I); Y=A(I+1);
      IF (X < Y)THEN DO;
         IF (X < AMIN) THEN AMIN=X;
         IF (Y > AMAX) THEN AMAX=Y;
       END; ELSE DO;
          IF (X > AMAX) THEN AMAX=X;
          IF (Y < AMIN) THEN AMIN=Y;
       END;
   END;
   RETURN;
END MINMAX;
CALL MINMAX(A,AMIN,AMAX,N);
CALL QUICKSORT(A,AMIN,AMAX,N);
```


## Pluto

Translation of

:

Wren

The standard library function, table.sort, which Pluto inherits from Lua, uses the quicksort algorithm internally.

```mw
local array = {
    {4, 65, 2, -31, 0, 99, 2, 83, 782, 1},
    {7, 5, 2, 6, 1, 4, 2, 6, 3},
    {"echo", "lima", "charlie", "whiskey", "golf", "papa", "alfa", "india", "foxtrot", "kilo"}
}

for array as a do
    print($"Before: \{{a:concat(", ")}}")
    a:sort()
    print($"After : \{{a:concat(", ")}}")
    print()
end
```

**Output:**

```
Before: {4, 65, 2, -31, 0, 99, 2, 83, 782, 1}
After : {-31, 0, 1, 2, 2, 4, 65, 83, 99, 782}

Before: {7, 5, 2, 6, 1, 4, 2, 6, 3}
After : {1, 2, 2, 3, 4, 5, 6, 6, 7}

Before: {echo, lima, charlie, whiskey, golf, papa, alfa, india, foxtrot, kilo}
After : {alfa, charlie, echo, foxtrot, golf, india, kilo, lima, papa, whiskey}
```


## PowerShell

### First solution

```mw
Function SortThree( [Array] $data )
{
   if( $data[ 0 ] -gt $data[ 1 ] )
   {
      if( $data[ 0 ] -lt $data[ 2 ] )
      {
         $data = $data[ 1, 0, 2 ]
      } elseif ( $data[ 1 ] -lt $data[ 2 ] ){
         $data = $data[ 1, 2, 0 ]
      } else {
         $data = $data[ 2, 1, 0 ]
      }
   } else {
      if( $data[ 0 ] -gt $data[ 2 ] )
      {
         $data = $data[ 2, 0, 1 ]
      } elseif( $data[ 1 ] -gt $data[ 2 ] ) {
         $data = $data[ 0, 2, 1 ]
      }
   }
   $data
}

Function QuickSort( [Array] $data, $rand = ( New-Object Random ) )
{
   $datal = $data.length
   if( $datal -gt 3 )
   {
      [void] $datal--
      $median = ( SortThree $data[ 0, ( $rand.Next( 1, $datal - 1 ) ), -1 ] )[ 1 ]
      $lt = @()
      $eq = @()
      $gt = @()
      $data | ForEach-Object { if( $_ -lt $median ) { $lt += $_ } elseif( $_ -eq $median ) { $eq += $_ } else { $gt += $_ } }
      $lt = ( QuickSort $lt $rand )
      $gt = ( QuickSort $gt $rand )
      $data = @($lt) + $eq + $gt
   } elseif( $datal -eq 3 ) {
      $data = SortThree( $data )
   } elseif( $datal -eq 2 ) {
      if( $data[ 0 ] -gt $data[ 1 ] )
      {
         $data = $data[ 1, 0 ]
      }
   }
   $data
}

QuickSort 5,3,1,2,4 
QuickSort 'e','c','a','b','d' 
QuickSort 0.5,0.3,0.1,0.2,0.4 
$l = 100; QuickSort ( 1..$l | ForEach-Object { $Rand = New-Object Random }{ $Rand.Next( 0, $l - 1 ) } )
```

### Another solution

```mw
function quicksort($array) {
    $less, $equal, $greater = @(), @(), @()
    if( $array.Count -gt 1 ) { 
        $pivot = $array[0]
        foreach( $x in $array) {
            if($x -lt $pivot) { $less += @($x) }
            elseif ($x -eq $pivot) { $equal += @($x)}
            else { $greater += @($x) }
        }    
        $array = (@(quicksort $less) + @($equal) + @(quicksort $greater))
    }
    $array
}
$array = @(60, 21, 19, 36, 63, 8, 100, 80, 3, 87, 11)
"$(quicksort $array)"
```

```
The output is: 3 8 11 19 21 36 60 63 80 87 100
```

### Yet another solution

```mw
function quicksort($in) {
    $n = $in.count
    switch ($n) {
        0 {}
        1 { $in[0] }
        2 { if ($in[0] -lt $in[1]) {$in[0], $in[1]} else {$in[1], $in[0]} }
        default {
            $pivot = $in | get-random
            $lt = $in | ? {$_ -lt $pivot}
            $eq = $in | ? {$_ -eq $pivot}
            $gt = $in | ? {$_ -gt $pivot}
            @(quicksort $lt) + @($eq) + @(quicksort $gt)
        }
    }
}
```


## Prolog

```mw
qsort( [], [] ).
qsort( [H|U], S ) :- splitBy(H, U, L, R), qsort(L, SL), qsort(R, SR), append(SL, [H|SR], S).

% splitBy( H, U, LS, RS )
% True if LS = { L in U | L <= H }; RS = { R in U | R > H }
splitBy( _, [], [], []).
splitBy( H, [U|T], [U|LS], RS ) :- U =< H, splitBy(H, T, LS, RS).
splitBy( H, [U|T], LS, [U|RS] ) :- U  > H, splitBy(H, T, LS, RS).
```


## Python

```mw
def quick_sort(sequence):
    lesser = []
    equal = []
    greater = []
    if len(sequence) <= 1:
        return sequence
    pivot = sequence[0]
    for element in sequence:
        if element < pivot:
            lesser.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    lesser = quick_sort(lesser)
    greater = quick_sort(greater)
    return lesser + equal + greater

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = quick_sort(a)
```

In a Haskell fashion --

```mw
def qsort(L):
    return (qsort([y for y in L[1:] if y <  L[0]]) + 
            [L[0]] + 
            qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L
```

More readable, but still using list comprehensions:

```mw
def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list[1:]   if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)
```

More correctly in some tests:

```mw
from random import *

def qSort(a):
    if len(a) <= 1:
        return a
    else:
        q = choice(a)
        return qSort([elem for elem in a if elem < q]) + [q] * a.count(q) + qSort([elem for elem in a if elem > q])
```

```mw
def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        less = []
        more = []
        pivot = choice(a)
        for i in a:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + [pivot] * a.count(pivot) + more
```

Returning a new list:

```mw
def qsort(array):
    if len(array) < 2:
        return array
    head, *tail = array
    less = qsort([i for i in tail if i < head])
    more = qsort([i for i in tail if i >= head])
    return less + [head] + more
```

Sorting a list in place:

```mw
def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)
```

Functional Style (no for or while loops, constants only):

```mw
def quicksort(unsorted_list):
   if len(unsorted_list) == 0:
       return []
   pivot = unsorted_list[0]
   less = list(filter(lambda x: x <  pivot, unsorted_list))
   same = list(filter(lambda x: x == pivot, unsorted_list))
   more = list(filter(lambda x: x >  pivot, unsorted_list))

   return quicksort(less) + same + quicksort(more)
```


## Qi

```mw
(define keep
  _    []       -> []
  Pred [A|Rest] -> [A | (keep Pred Rest)] where (Pred A)
  Pred [_|Rest] -> (keep Pred Rest))

(define quicksort
  []    -> []
  [A|R] -> (append (quicksort (keep (>= A) R))
                   [A]
                   (quicksort (keep (< A) R))))

(quicksort [6 8 5 9 3 2 2 1 4 7])
```


## Quackery

Sort a nest of numbers.

```mw
[ stack ]                      is less      (     --> s )

[ stack ]                      is same      (     --> s )

[ stack ]                      is more      (     --> s )

[ - -1 1 clamp 1+ ]            is <=>       ( n n --> n )

[ dup size 2 < if done
  [] less put
  [] same put
  [] more put
  behead swap witheach
    [ 2dup swap <=>
      [ table less same more ]
      gather ]
  same gather
  less take recurse
  same take join
  more take recurse join ]     is quicksort (   [ --> [ )

[] 10 times [ i^ join ] 3 of
dup       echo cr
quicksort echo cr
```

**Output:**

```
[ 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 ]
[ 0 0 0 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 8 8 8 9 9 9 ]
```


## R

Translation of

:

Octave

```mw
qsort <- function(v) {
  if ( length(v) > 1 ) 
  {
    pivot <- (min(v) + max(v))/2.0                            # Could also use pivot <- median(v)
    c(qsort(v[v < pivot]), v[v == pivot], qsort(v[v > pivot])) 
  } else v
}

N <- 100
vs <- runif(N)
system.time(u <- qsort(vs))
print(u)
```


## Racket

```mw
#lang racket
(define (quicksort < l)
  (match l
    ['() '()]
    [(cons x xs) 
     (let-values ([(xs-gte xs-lt) (partition (curry < x) xs)])
       (append (quicksort < xs-lt) 
               (list x) 
               (quicksort < xs-gte)))]))
```

Examples

```mw
(quicksort < '(8 7 3 6 4 5 2))
;returns '(2 3 4 5 6 7 8)
(quicksort string<? '("Mergesort" "Quicksort" "Bubblesort"))
;returns '("Bubblesort" "Mergesort" "Quicksort")
```


## Raku

```mw
#| Recursive, single-thread, random pivot, single-pass, quicksort implementation
multi quicksort(\a where a.elems < 2) { a }
multi quicksort(\a, \pivot = a.pick) {
   my %prt{Order} is default([]) = a.classify: * cmp pivot;
   |samewith(%prt{Less}), |%prt{Same}, |samewith(%prt{More})
}
```

### concurrent implementation

The partitions can be sorted in parallel.

```mw
#| Recursive, parallel, random pivot, single-pass, quicksort implementation
multi quicksort-parallel-naive(\a where a.elems < 2) { a }
multi quicksort-parallel-naive(\a, \pivot = a.pick) {
   my %prt{Order} is default([]) = a.classify: * cmp pivot;
   my Promise $less = start { samewith(%prt{Less}) }
   my $more = samewith(%prt{More});
   await $less andthen |$less.result, |%prt{Same}, |$more;
}
```

Let's tune the parallel execution by applying a minimum batch size in order to spawn a new thread.

```mw
#| Recursive, parallel, batch tuned, single-pass, quicksort implementation
sub quicksort-parallel(@a, $batch = 2**9) {
   return @a if @a.elems < 2;

   # separate unsorted input into Order Less, Same and More compared to a random $pivot
   my $pivot = @a.pick;
   my %prt{Order} is default([]) = @a.classify( * cmp $pivot );

   # decide if we sort the Less partition on a new thread
   my $less = %prt{Less}.elems >= $batch
                 ?? start { samewith(%prt{Less}, $batch) }
                 !!         samewith(%prt{Less}, $batch);

   # meanwhile use current thread for sorting the More partition
   my $more = samewith(%prt{More}, $batch);

   # if we went parallel, we need to await the result
   await $less andthen $less = $less.result if $less ~~ Promise;

   # concat all sorted partitions into a list and return
   |$less, |%prt{Same}, |$more;
}
```

### testing

Let's run some tests.

```mw
say "x" x 10 ~ " Testing " ~ "x" x 10;
use Test;
my @functions-under-test = &quicksort, &quicksort-parallel-naive, &quicksort-parallel;
my @testcases =
      () => (),
      <a>.List => <a>.List,
      <a a> => <a a>,
      ("b", "a", 3) => (3, "a", "b"),
      <h b a c d f e g> => <a b c d e f g h>,
      <a 🎮 3 z 4 🐧> => <a 🎮 3 z 4 🐧>.sort
      ;

plan @testcases.elems * @functions-under-test.elems;
for @functions-under-test -> &fun {
   say &fun.name;
   is-deeply &fun(.key), .value, .key ~ "  =>  " ~ .value for @testcases;
}
done-testing;
```

```
xxxxxxxxxx Testing xxxxxxxxxx
1..18
quicksort
ok 1 -   =>
ok 2 - a  =>  a
ok 3 - a a  =>  a a
ok 4 - b a 3  =>  3 a b
ok 5 - h b a c d f e g  =>  a b c d e f g h
ok 6 - a 🎮 3 z 4 🐧  =>  3 4 a z 🎮 🐧
quicksort-parallel-naive
ok 7 -   =>
ok 8 - a  =>  a
ok 9 - a a  =>  a a
ok 10 - b a 3  =>  3 a b
ok 11 - h b a c d f e g  =>  a b c d e f g h
ok 12 - a 🎮 3 z 4 🐧  =>  3 4 a z 🎮 🐧
quicksort-parallel
ok 13 -   =>
ok 14 - a  =>  a
ok 15 - a a  =>  a a
ok 16 - b a 3  =>  3 a b
ok 17 - h b a c d f e g  =>  a b c d e f g h
ok 18 - a 🎮 3 z 4 🐧  =>  3 4 a z 🎮 🐧
```

### benchmarking

and some benchmarking

```mw
# run in a terminal: "zef install Benchmark" to install from https://raku.land
use Benchmark;

say "x" x 11 ~ " Benchmarking " ~ "x" x 11;
my $runs = 5;
my $elems = 10 * Kernel.cpu-cores * 2**10;
my @unsorted of Str = ('a'..'z').roll(8).join xx $elems;
my UInt $l-batch = 2**13;
my UInt $m-batch = 2**11;
my UInt $s-batch = 2**9;
my UInt $t-batch = 2**7;

say "elements: $elems, runs: $runs, cpu-cores: {Kernel.cpu-cores}, large/medium/small/tiny-batch: $l-batch/$m-batch/$s-batch/$t-batch";

my %results = timethese $runs, {
   single-thread         => { quicksort(@unsorted) },
   parallel-naive        => { quicksort-parallel-naive(@unsorted) },
   parallel-tiny-batch   => { quicksort-parallel(@unsorted, $t-batch) },
   parallel-small-batch  => { quicksort-parallel(@unsorted, $s-batch) },
   parallel-medium-batch => { quicksort-parallel(@unsorted, $m-batch) },
   parallel-large-batch  => { quicksort-parallel(@unsorted, $l-batch) },
}, :statistics;

my @metrics = <mean median sd>;
my $msg-row = "%.4f\t" x @metrics.elems ~ '%s';

for %results.sort( *.value<median> ) {
    once say @metrics.join("\t"); # header
        say sprintf($msg-row, .value{@metrics}, .key)
}
```

```
xxxxxxxxxxx Benchmarking xxxxxxxxxxx
elements: 40960, runs: 5, cpu-cores: 4, large/medium/small/tiny-batch: 8192/2048/512/128
mean    median  sd
1.2036  1.1476  0.0872  parallel-medium-batch
1.3223  1.3359  0.1451  parallel-tiny-batch
1.4504  1.4161  0.1231  parallel-small-batch
2.4201  2.3860  0.2590  parallel-large-batch
2.7142  2.6699  0.2803  parallel-naive
5.6303  5.5250  0.2329  single-thread
```


## Rebol

Translation of

:

Python

```mw
Rebol [
    title: "Rosetta code: Sorting algorithms/Quicksort"
    file:  %Sorting_algorithms-Quicksort.r3
    url:   https://rosettacode.org/wiki/Sorting_algorithms-Quicksort
]

quick-sort: function/with [
    "Sort a series in ascending order using quicksort."
    items [series!] "Series of values to sort"
][
    qsort items 1 length? items
    items
][
    qsort: function [
        ;; Sort a subrange of a block in-place using Hoare partition scheme.
        a     [series!]  ;; Series to sort in-place
        start [integer!] ;; Start index of subrange (inclusive)
        stop  [integer!] ;; Stop index of subrange (inclusive)
    ][
        if stop - start <= 0 [exit]

        ;; median-of-three: sort start/mid/stop and use median as pivot
        mid: (start + stop) >> 1
        if a/:start > a/:mid  [swap at a start at a mid ]
        if a/:start > a/:stop [swap at a start at a stop]
        if a/:mid   > a/:stop [swap at a mid   at a stop] 

        ;; initialise pivot and left/right cursors
        pivot: a/:start
        left:  start
        right: stop

        while [left <= right][
            while [a/:left  < pivot] [++ left]
            while [a/:right > pivot] [-- right]
            if left <= right [
                swap at a left  at a right
                ++ left
                -- right
            ]
        ]
        ;; recursively sort the two partitions
        qsort a start right
        qsort a left  stop
    ]
]

probe quick-sort [1 2 3 4 5 6 7 8 9]
probe quick-sort [3 1 2 8 5 7 9 4 6]
probe quick-sort "Hello Rosetta"
```

**Output:**

```
[1 2 3 4 5 6 7 8 9]
[1 2 3 4 5 6 7 8 9]
" HRaeelloostt"
```


## Red

```mw
Red []

;;-------------------------------
;; we have to use function not func here, otherwise we'd have to define all "vars" as local...
qsort: function [list][
;;-------------------------------
  if 1 >= length? list [  return list ]
  left: copy [] 
  right: copy []
  eq:   copy []  ;; "equal"
  pivot: list/2 ;; simply choose second element as pivot element
  foreach ele list [
      case [
       ele < pivot [ append left ele ]
       ele > pivot [ append right ele ]
       true        [ append eq ele ]
      ]
  ]
  ;; this is the last expression of the function, so coding "return" here is not necessary
  ;reduce [qsort left eq qsort right] ; NOTE: This internally produced a nested list like this:
  ; [[] [1 1 1] [[[2] [3 3 3] [4]] [7] [8]]]
  ; Although printing it displayed as normal, internally it's not, so I (hinjolicious) corrected it to this:
  append append qsort left eq qsort right ; corrected!
  ; Note though that this will still caused stack overflow on sorted / reversed data!
]

;; lets test the function with an array of 100k integers, range 1..1000  
list: []
loop 100000 [append list random 1000]
t0: now/time/precise  ;; start timestamp
qsort list ;; the return value (block) contains the sorted list, original list has not changed
print ["time1: "  now/time/precise   - t0]  ;; about 1.1 sec on my machine
t0: now/time/precise  
sort list  ;; just for fun time the builtin function also ( also implementation of quicksort ) 
print ["time2: " now/time/precise   - t0]
```

Another alternative with inplace array manipulation based on Python's example:

Note: Updated using median-of-three method to handle sorted / reversed data better. This is important to avoid recursion stack overflow because of Red's limited recursion stacks.

```mw
Red [
   title: "Quick Sort"
   author: "hinjolicious"
   resources: "Red Sensei, Python's example"
]

quick: function [a][ _quick a 1 length? a ]

_quick: function [a start stop][
   if stop - start <= 0 [return a]

   ; Handles sorted / reversed data better (no recursion stack overflow)
   mid: (start + stop) >> 1
   
   ;-- Sort start, mid, stop positions (put median at start)
   if a/(start) > a/(mid) [swap at a start at a mid]
   if a/(start) > a/(stop) [swap at a start at a stop]
   if a/(mid) > a/(stop) [swap at a mid at a stop] 
   
   ;-- Now a/(mid) is the median; move it to start position as pivot
   swap at a start at a mid   
   
   piv: a/(start)
   l: start
   r: stop
   while [l <= r][
      while [a/(l) < piv] [l: l + 1]
      while [a/(r) > piv] [r: r - 1]
      if l <= r [
         swap  at a l  at a r
         l: l + 1
         r: r - 1
      ]
   ]
   _quick a start r
   _quick a l stop
]

random/seed 1
max: 10000
dat: collect [loop max [keep random max]]

t: now/time/precise  
quick dat 
print ["quick: " now/time/precise - t]  
print ["sorted: " dat]
```

**Output:**

```
quick:  0:00:00.122122
sorted:  2 2 5 5 6 7 7 8 8 8 10 10 13 14 14 15 17 18 21 22 25 26 26 27 28 28 29 30 31 31 32 32 33 33 
34 34 37 37 38 38 39 40 41 42 42 43 43 43 44 46 47 47 49 50 52 53 53 56 59 60 60 61 62 64 65 67 67 69
 72 72 75 75 76 76 79 79 80 80 81 82 82 83 84 85 88 88 88 89 89 90 91 91 93 93 93 94 94 95 96 97 97 9
 ...
  9951 9951 9952 9952 9954 9955 9958 9959 9960 9960 9961 9961 9962 9963 9963 9964 9964 9965 9966 9966 
9967 9967 9967 9967 9967 9969 9970 9971 9974 9975 9976 9977 9977 9977 9981 9981 9982 9983 9987 9987 9
987 9987 9988 9988 9988 9988 9991 9992 9993 9994 9995 9996 9996 9999 9999 10000
>> 
```
