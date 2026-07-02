---
title: "Sorting algorithms/Quicksort (part 4/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/8
---

## Common Lisp

The functional programming way

```mw
(defun quicksort (list &aux (pivot (car list)) )
  (if (cdr list)
      (nconc (quicksort (remove-if-not #'(lambda (x) (< x pivot)) list))
             (remove-if-not #'(lambda (x) (= x pivot)) list)
             (quicksort (remove-if-not #'(lambda (x) (> x pivot)) list)))
      list))
```

With flet

```mw
(defun qs (list)
  (if (cdr list)
      (flet ((pivot (test)
               (remove (car list) list :test-not test)))
        (nconc (qs (pivot #'>)) (pivot #'=) (qs (pivot #'<))))
      list))
```

In-place non-functional

```mw
(defun quicksort (sequence)
  (labels ((swap (a b) (rotatef (elt sequence a) (elt sequence b)))
           (sub-sort (left right)
             (when (< left right)
               (let ((pivot (elt sequence right))
                     (index left))
                 (loop for i from left below right
                       when (<= (elt sequence i) pivot)
                         do (swap i (prog1 index (incf index))))
                 (swap right index)
                 (sub-sort left (1- index))
                 (sub-sort (1+ index) right)))))
    (sub-sort 0 (1- (length sequence)))
    sequence))
```

Functional with destructuring

```mw
(defun quicksort (list)
  (when list
    (destructuring-bind (x . xs) list
      (nconc (quicksort (remove-if (lambda (a) (> a x)) xs))
        `(,x)
        (quicksort (remove-if (lambda (a) (<= a x)) xs))))))
```


## Cowgol

```mw
include "cowgol.coh";

# Comparator interface, on the model of C, i.e:
# foo < bar => -1, foo == bar => 0, foo > bar => 1
typedef CompRslt is int(-1, 1);
interface Comparator(foo: intptr, bar: intptr): (rslt: CompRslt);

# Quicksort an array of pointer-sized integers given a comparator function
# (This is the closest you can get to polymorphism in Cowgol).
# Because Cowgol does not support recursion, a pointer to free memory
# for a stack must also be given.
sub qsort(A: [intptr], len: intptr, comp: Comparator, stack: [intptr]) is 
    # The partition function can be taken almost verbatim from Wikipedia
    sub partition(lo: intptr, hi: intptr): (p: intptr) is
        # This is not quite as bad as it looks: /2 compiles into a single shift
        # and "@bytesof intptr" is always power of 2 so compiles into shift(s).
        var pivot := [A + (hi/2 + lo/2) * @bytesof intptr];
        var i := lo - 1;
        var j := hi + 1;
        loop
            loop    
                i := i + 1;
                if comp([A + i*@bytesof intptr], pivot) != -1 then
                    break;
                end if;
            end loop;
            loop
                j := j - 1;
                if comp([A + j*@bytesof intptr], pivot) != 1 then
                    break;
                end if;
            end loop;
            if i >= j then
                p := j;
                return;
            end if;
            var ii := i * @bytesof intptr;
            var jj := j * @bytesof intptr;
            var t := [A+ii];
            [A+ii] := [A+jj];
            [A+jj] := t;
        end loop;
    end sub;
    
    # Cowgol lacks recursion, so we'll have to solve it by implementing
    # the stack ourselves.
    var sp: intptr := 0; # stack index
    sub push(n: intptr) is
        sp := sp + 1;
        [stack] := n;
        stack := @next stack;
    end sub;
    sub pop(): (n: intptr) is
        sp := sp - 1;
        stack := @prev stack;
        n := [stack];
    end sub;
    
    # start by sorting [0..length-1]
    push(len-1); 
    push(0);
    while sp != 0 loop
        var lo := pop();
        var hi := pop();
        if lo < hi then
            var p := partition(lo, hi);
            push(hi);   # note the order - we need to push the high pair
            push(p+1);  # first for it to be done last
            push(p);
            push(lo);
        end if;
    end loop;
end sub;

# Test: sort a list of numbers
sub NumComp implements Comparator is
    # Compare the inputs as numbers
    if foo < bar then rslt := -1;
    elseif foo > bar then rslt := 1;
    else rslt := 0;
    end if;
end sub;

# Numbers
var numbers: intptr[] := {
    65,13,4,84,29,5,96,73,5,11,17,76,38,26,44,20,36,12,44,51,79,8,99,7,19,95,26
};

# Room for the stack
var stackbuf: intptr[256];

# Sort the numbers in place
qsort(&numbers as [intptr], @sizeof numbers, NumComp, &stackbuf as [intptr]);

# Print the numbers (hopefully in order)
var i: @indexof numbers := 0;
while i < @sizeof numbers loop
    print_i32(numbers[i] as uint32);
    print_char(' ');
    i := i + 1;
end loop;
print_nl();
```

**Output:**

```
4 5 5 7 8 11 12 13 17 19 20 26 26 29 36 38 44 44 51 65 73 76 79 84 95 96 99
```


## Crystal

Translation of

:

Ruby

```mw
def quick_sort(a : Array(Int32)) : Array(Int32)
  return a if a.size <= 1
  p = a[0]
  lt, rt = a[1 .. -1].partition { |x| x < p }
  return quick_sort(lt) + [p] + quick_sort(rt)
end

a = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
puts quick_sort(a) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


## Curry

Copied from Curry: Example Programs.

```mw
-- quicksort using higher-order functions:

qsort :: [Int] -> [Int] 
qsort []     = []
qsort (x:l)  = qsort (filter (<x) l) ++ x : qsort (filter (>=x) l)

goal = qsort [2,3,1,0]
```


## D

A Functional version

```mw
import std.stdio : writefln, writeln;
import std.algorithm: filter;
import std.array;

T[] quickSort(T)(T[] xs) => 
  xs.length == 0 ? [] :  
    xs[1 .. $].filter!(x => x< xs[0]).array.quickSort ~  
    xs[0 .. 1] ~  
    xs[1 .. $].filter!(x => x>=xs[0]).array.quickSort; 

void main() =>
  [4, 65, 2, -31, 0, 99, 2, 83, 782, 1].quickSort.writeln;
```

**Output:**

```
[-31, 0, 1, 2, 2, 4, 65, 83, 99, 782]
```

A simple high-level version (same output):

```mw
import std.stdio, std.array;

T[] quickSort(T)(T[] items) pure nothrow {
    if (items.empty)
        return items;
    T[] less, notLess;
    foreach (x; items[1 .. $])
        (x < items[0] ? less : notLess) ~= x;
    return less.quickSort ~ items[0] ~ notLess.quickSort;
}

void main() {
    [4, 65, 2, -31, 0, 99, 2, 83, 782, 1].quickSort.writeln;
}
```

Often short functional sieves are not a true implementations of the Sieve of Eratosthenes: http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

Similarly, one could argue that a true QuickSort is in-place, as this more efficient version (same output):

```mw
import std.stdio, std.algorithm;

void quickSort(T)(T[] items) pure nothrow @safe @nogc {
    if (items.length >= 2) {
        auto parts = partition3(items, items[$ / 2]);
        parts[0].quickSort;
        parts[2].quickSort;
    }
}

void main() {
    auto items = [4, 65, 2, -31, 0, 99, 2, 83, 782, 1];
    items.quickSort;
    items.writeln;
}
```


## Delphi

Works with

:

Delphi

version 6.0

Library:

SysUtils,StdCtrls

This quick sort routine is infinitely versatile. It sorts an array of pointers. The advantage of this is that pointers can contain anything, ranging from integers, to strings, to floating point numbers to objects. The way each pointer is interpreted is through the compare routine, which is customized for the particular situation. The compare routine can interpret each pointer as a string, an integer, a float or an object and it can treat those items in different ways. For example, the order in which it compares strings controls whether the sort is alphabetical or reverse alphabetical. In this case, I show an integer sort, an alphabetic string sort, a reverse alphabetical string sort and a string sort by length.

```mw
{Dynamic array of pointers}

type TPointerArray = array of Pointer;

procedure QuickSort(SortList: TPointerArray; L, R: Integer; SCompare: TListSortCompare);
{Do quick sort on items held in TPointerArray}
{SCompare controls how the pointers are interpreted}
var I, J: Integer;
var P,T: Pointer;
begin
repeat
   begin
   I := L;
   J := R;
   P := SortList[(L + R) shr 1];
   repeat
      begin
      while SCompare(SortList[I], P) < 0 do Inc(I);
      while SCompare(SortList[J], P) > 0 do Dec(J);
      if I <= J then
         begin
         {Exchange itesm}
         T:=SortList[I];
         SortList[I]:=SortList[J];
         SortList[J]:=T;
         if P = SortList[I] then P := SortList[J]
         else if P = SortList[J] then P := SortList[I];
         Inc(I);
         Dec(J);
         end;
      end
   until I > J;
   if L < J then QuickSort(SortList, L, J, SCompare);
   L := I;
   end
until I >= R;
end;

procedure DisplayStrings(Memo: TMemo; PA: TPointerArray);
{Display pointers as strings}
var I: integer;
var S: string;
begin
S:='[';
for I:=0 to High(PA) do
   begin
   if I>0 then S:=S+' ';
   S:=S+string(PA[I]^);
   end;
S:=S+']';
Memo.Lines.Add(S);
end;

procedure DisplayIntegers(Memo: TMemo; PA: TPointerArray);
{Display pointer array as integers}
var I: integer;
var S: string;
begin
S:='[';
for I:=0 to High(PA) do
   begin
   if I>0 then S:=S+' ';
   S:=S+IntToStr(Integer(PA[I]));
   end;
S:=S+']';
Memo.Lines.Add(S);
end;

function IntCompare(Item1, Item2: Pointer): Integer;
{Compare for integer sort}
begin
Result:=Integer(Item1)-Integer(Item2);
end;

function StringCompare(Item1, Item2: Pointer): Integer;
{Compare for alphabetical string sort}
begin
Result:=AnsiCompareText(string(Item1^),string(Item2^));
end;

function StringRevCompare(Item1, Item2: Pointer): Integer;
{Compare for reverse alphabetical order}
begin
Result:=AnsiCompareText(string(Item2^),string(Item1^));
end;

function StringLenCompare(Item1, Item2: Pointer): Integer;
{Compare for string length sort}
begin
Result:=Length(string(Item1^))-Length(string(Item2^));
end;

{Arrays of strings and integers}

var IA: array [0..9] of integer = (23, 14, 62, 28, 56, 91, 33, 30, 75, 5);
var SA: array [0..15] of string = ('Now','is','the','time','for','all','good','men','to','come','to','the','aid','of','the','party.');

procedure ShowQuickSort(Memo: TMemo);
var L: TStringList;
var PA: TPointerArray;
var I: integer;
begin
Memo.Lines.Add('Integer Sort');
SetLength(PA,Length(IA));
for I:=0 to High(IA) do PA[I]:=Pointer(IA[I]);
Memo.Lines.Add('Before Sorting');
DisplayIntegers(Memo,PA);
QuickSort(PA,0,High(PA),IntCompare);
Memo.Lines.Add('After Sorting');
DisplayIntegers(Memo,PA);

Memo.Lines.Add('');
Memo.Lines.Add('String Sort - Alphabetical');
SetLength(PA,Length(SA));
for I:=0 to High(SA) do PA[I]:=Pointer(@SA[I]);
Memo.Lines.Add('Before Sorting');
DisplayStrings(Memo,PA);
QuickSort(PA,0,High(PA),StringCompare);
Memo.Lines.Add('After Sorting');
DisplayStrings(Memo,PA);

Memo.Lines.Add('');
Memo.Lines.Add('String Sort - Reverse Alphabetical');
QuickSort(PA,0,High(PA),StringRevCompare);
Memo.Lines.Add('After Sorting');
DisplayStrings(Memo,PA);

Memo.Lines.Add('');
Memo.Lines.Add('String Sort - By Length');
QuickSort(PA,0,High(PA),StringLenCompare);
Memo.Lines.Add('After Sorting');
DisplayStrings(Memo,PA);
end;
```

**Output:**

```
Integer Sort
Before Sorting
[23 14 62 28 56 91 33 30 75 5]
After Sorting
[5 14 23 28 30 33 56 62 75 91]

String Sort - Alphabetical
Before Sorting
[Now is the time for all good men to come to the aid of the party.]
After Sorting
[aid all come for good is men Now party. of the the the time to to]

String Sort - Reverse Alphabetical
After Sorting
[to to time the the the party. of Now men is good for come all aid]

String Sort - By Length
After Sorting
[of is to to men aid all for Now the the the time come good party.]
Elapsed Time: 16.478 ms.
```


## Dart

```mw
quickSort(List a) {
  if (a.length <= 1) {
    return a;
  }
  
  var pivot = a[0];
  var less = [];
  var more = [];
  var pivotList = [];
  
  // Partition
  a.forEach((var i){    
    if (i.compareTo(pivot) < 0) {
      less.add(i);
    } else if (i.compareTo(pivot) > 0) {
      more.add(i);
    } else {
      pivotList.add(i);
    }
  });
  
  // Recursively sort sublists
  less = quickSort(less);
  more = quickSort(more);
  
  // Concatenate results
  less.addAll(pivotList);
  less.addAll(more);
  return less;
}

void main() {
  var arr=[1,5,2,7,3,9,4,6,8];
  print("Before sort");
  arr.forEach((var i)=>print("$i"));
  arr = quickSort(arr);
  print("After sort");
  arr.forEach((var i)=>print("$i"));
}
```


## E

```mw
def quicksort := {

    def swap(container, ixA, ixB) {
        def temp := container[ixA]
        container[ixA] := container[ixB]
        container[ixB] := temp
    }

    def partition(array, var first :int, var last :int) {
        if (last <= first) { return }
  
        # Choose a pivot
        def pivot := array[def pivotIndex := (first + last) // 2]
  
        # Move pivot to end temporarily
        swap(array, pivotIndex, last)
  
        var swapWith := first
  
        # Scan array except for pivot, and...
        for i in first..!last {
            if (array[i] <= pivot) {   # items ≤ the pivot
                swap(array, i, swapWith) # are moved to consecutive positions on the left
                swapWith += 1
            }
        }
  
        # Swap pivot into between-partition position.
        # Because of the swapping we know that everything before swapWith is less
        # than or equal to the pivot, and the item at swapWith (since it was not
        # swapped) is greater than the pivot, so inserting the pivot at swapWith
        # will preserve the partition.
        swap(array, swapWith, last)
        return swapWith
    }

    def quicksortR(array, first :int, last :int) {
        if (last <= first) { return }
        def pivot := partition(array, first, last)
        quicksortR(array, first, pivot - 1)
        quicksortR(array, pivot + 1, last)
    }

    def quicksort(array) { # returned from block
        quicksortR(array, 0, array.size() - 1)
    }
}
```


## EasyLang

```mw
proc qsort left right &d[] .
   if left < right
      piv = d[left]
      mid = left
      for i = left + 1 to right
         if d[i] < piv
            mid += 1
            swap d[i] d[mid]
         .
      .
      swap d[left] d[mid]
      qsort left mid - 1 d[]
      qsort mid + 1 right d[]
   .
.
proc sort &d[] .
   qsort 1 len d[] d[]
.
d[] = [ 29 4 72 44 55 26 27 77 92 5 ]
sort d[]
print d[]
```

**Output:**

```
[ 4 5 26 27 29 44 55 72 77 92 ]
```


## EchoLisp

```mw
(lib 'list) ;; list-partition

(define compare 0) ;; counter

(define (quicksort L compare-predicate: proc aux:  (part null))
(if  (<= (length L) 1) L
     (begin
     ;; counting the number of comparisons
     (set! compare (+ compare (length (rest L))))
      ;; pivot = first element of list
     (set! part (list-partition (rest L) proc (first L)))
     (append (quicksort (first part) proc )
            (list (first L)) 
            (quicksort (second part) proc)))))
```

**Output:**

```mw
(shuffle (iota 15))
    → (10 0 14 11 13 9 2 5 4 8 1 7 12 3 6)
(quicksort (shuffle (iota 15)) <)
    → (0 1 2 3 4 5 6 7 8 9 10 11 12 13 14)

;; random list of numbers in [0 .. n[
;; count number of comparisons
(define (qtest (n 10000))
   (set! compare 0)
   (quicksort (shuffle (iota n)) >)
   (writeln 'n n 'compare# compare ))
   
(qtest 1000)
  n     1000       compare#     12764    
(qtest 10000)
  n     10000      compare#     277868    
(qtest 100000)
  n     100000     compare#     6198601
```


## Eero

Translated from Objective-C example on this page.

```mw
#import <Foundation/Foundation.h>

void quicksortInPlace(MutableArray array, const long first, const long last)
  if first >= last
    return
  Value pivot = array[(first + last) / 2]
  left := first
  right := last
  while left <= right
    while array[left] < pivot
      left++
    while array[right] > pivot
      right--
    if left <= right
      array.exchangeObjectAtIndex: left++, withObjectAtIndex: right--

  quicksortInPlace(array, first, right)
  quicksortInPlace(array, left, last)

Array quicksort(Array unsorted)
  a := []
  a.addObjectsFromArray: unsorted
  quicksortInPlace(a, 0, a.count - 1)
  return a

int main(int argc, const char * argv[])
  autoreleasepool
    a := [1, 3, 5, 7, 9, 8, 6, 4, 2]
    Log( 'Unsorted: %@', a)
    Log( 'Sorted: %@', quicksort(a) )
    b := ['Emil', 'Peg', 'Helen', 'Juergen', 'David', 'Rick', 'Barb', 'Mike', 'Tom']
    Log( 'Unsorted: %@', b)
    Log( 'Sorted: %@', quicksort(b) )

  return 0
```

Alternative implementation (not necessarily as efficient, but very readable)

```mw
#import <Foundation/Foundation.h>

implementation Array (Quicksort)

  plus: Array array, return Array = 
    self.arrayByAddingObjectsFromArray: array

  filter: BOOL (^)(id) predicate, return Array
    array := []
    for id item in self
      if predicate(item)
        array.addObject: item
    return array.copy

  quicksort, return Array = self
    if self.count > 1      
      id x = self[self.count / 2]
      lesser := self.filter: (id y | return y < x)
      greater := self.filter: (id y | return y > x)
      return lesser.quicksort + [x] + greater.quicksort

end

int main()
  autoreleasepool
    a := [1, 3, 5, 7, 9, 8, 6, 4, 2]
    Log( 'Unsorted: %@', a)
    Log( 'Sorted: %@', a.quicksort )
    b := ['Emil', 'Peg', 'Helen', 'Juergen', 'David', 'Rick', 'Barb', 'Mike', 'Tom']
    Log( 'Unsorted: %@', b)
    Log( 'Sorted: %@', b.quicksort )

  return 0
```

**Output:**

```
2013-09-04 16:54:31.780 a.out[2201:507] Unsorted: (
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
2013-09-04 16:54:31.781 a.out[2201:507] Sorted: (
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
2013-09-04 16:54:31.781 a.out[2201:507] Unsorted: (
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
2013-09-04 16:54:31.782 a.out[2201:507] Sorted: (
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


## Eiffel

The

```mw
QUICKSORT
```

class:

```mw
class
   QUICKSORT [G -> COMPARABLE]

create
   make

feature {NONE} --Implementation

   is_sorted (list: ARRAY [G]): BOOLEAN
      require
         not_void: list /= Void
      local
         i: INTEGER
      do
         Result := True
         from
            i := list.lower + 1
         invariant
            i >= list.lower + 1 and i <= list.upper + 1
         until
            i > list.upper
         loop
            Result := Result and list [i - 1] <= list [i]
            i := i + 1
         variant
            list.upper + 1 - i
         end
      end

   concatenate_array (a: ARRAY [G] b: ARRAY [G]): ARRAY [G]
      require
         not_void: a /= Void and b /= Void
      do
         create Result.make_from_array (a)
         across
            b as t
         loop
            Result.force (t.item, Result.upper + 1)
         end
      ensure
         same_size: a.count + b.count = Result.count
      end

   quicksort_array (list: ARRAY [G]): ARRAY [G]
      require
         not_void: list /= Void
      local
         less_a: ARRAY [G]
         equal_a: ARRAY [G]
         more_a: ARRAY [G]
         pivot: G
      do
         create less_a.make_empty
         create more_a.make_empty
         create equal_a.make_empty
         create Result.make_empty
         if list.count <= 1 then
            Result := list
         else
            pivot := list [list.lower]
            across
               list as li
            invariant
               less_a.count + equal_a.count + more_a.count <= list.count
            loop
               if li.item < pivot then
                  less_a.force (li.item, less_a.upper + 1)
               elseif li.item = pivot then
                  equal_a.force (li.item, equal_a.upper + 1)
               elseif li.item > pivot then
                  more_a.force (li.item, more_a.upper + 1)
               end
            end
            Result := concatenate_array (Result, quicksort_array (less_a))
            Result := concatenate_array (Result, equal_a)
            Result := concatenate_array (Result, quicksort_array (more_a))
         end
      ensure
         same_size: list.count = Result.count
         sorted: is_sorted (Result)
      end

feature -- Initialization

   make
      do
      end

   quicksort (a: ARRAY [G]): ARRAY [G]
      do
         Result := quicksort_array (a)
      end

end
```

A test application:

```mw
class
   APPLICATION

create
   make

feature {NONE} -- Initialization

   make
         -- Run application.
      local
         test: ARRAY [INTEGER]
         sorted: ARRAY [INTEGER]
         sorter: QUICKSORT [INTEGER]
      do
         create sorter.make
         test := <<1, 3, 2, 4, 5, 5, 7, -1>>
         sorted := sorter.quicksort (test)
         across
            sorted as s
         loop
            print (s.item)
            print (" ")
         end
         print ("%N")
      end

end
```


## Elena

ELENA 6.x :

```mw
import extensions;
import system'routines;
import system'collections;
 
extension op
{
    quickSort()
    {
        if (self.isEmpty()) { ^ self };
 
        var pivot := self[0];
 
        auto less := new ArrayList();
        auto pivotList := new ArrayList();
        auto more := new ArrayList();
 
        self.forEach::(item)
        {
            if (item < pivot)
            {
                less.append(item)
            }
            else if (item > pivot) 
            {
                more.append(item)
            }
            else
            {
                pivotList.append(item)
            }
        };
 
        less := less.quickSort();
        more := more.quickSort();
 
        less.appendRange(pivotList);
        less.appendRange(more);
 
        ^ less
    }
}
 
public Program()
{
    var list := new int[]{3, 14, 1, 5, 9, 2, 6, 3};
 
    Console.printLine("before:", list.asEnumerable());
    Console.printLine("after :", list.quickSort().asEnumerable());
}
```

**Output:**

```
before:3,14,1,5,9,2,6,3
after :1,2,3,3,5,6,9,14
```


## Elixir

```mw
defmodule Sort do
  def qsort([]), do: []
  def qsort([h | t]) do
    {lesser, greater} = Enum.split_with(t, &(&1 < h))
    qsort(lesser) ++ [h] ++ qsort(greater)
  end
end
```


## Erlang

like haskell. Used by Measure_relative_performance_of_sorting_algorithms_implementations. If changed keep the interface or change Measure_relative_performance_of_sorting_algorithms_implementations

```mw
-module( quicksort ).

-export( [qsort/1] ).

qsort([]) -> [];
qsort([X|Xs]) ->
   qsort([ Y || Y <- Xs, Y < X]) ++ [X] ++ qsort([ Y || Y <- Xs, Y >= X]).
```

multi-process implementation (number processes = number of processor cores):

```mw
quick_sort(L) -> qs(L, trunc(math:log2(erlang:system_info(schedulers)))).

qs([],_) -> [];
qs([H|T], N) when N > 0  -> 
    {Parent, Ref} = {self(), make_ref()},
    spawn(fun()-> Parent ! {l1, Ref, qs([E||E<-T, E<H], N-1)} end), 
    spawn(fun()-> Parent ! {l2, Ref, qs([E||E<-T, H =< E], N-1)} end), 
    {L1, L2} = receive_results(Ref, undefined, undefined), 
    L1 ++ [H] ++ L2;
qs([H|T],_) ->
    qs([E||E<-T, E<H],0) ++ [H] ++ qs([E||E<-T, H =< E],0).

receive_results(Ref, L1, L2) ->
    receive
        {l1, Ref, L1R} when L2 == undefined -> receive_results(Ref, L1R, L2);
        {l2, Ref, L2R} when L1 == undefined -> receive_results(Ref, L1, L2R);
        {l1, Ref, L1R} -> {L1R, L2};
        {l2, Ref, L2R} -> {L1, L2R}
    after 5000 -> receive_results(Ref, L1, L2)
    end.
```


## Emacs Lisp

**Unoptimized**

Library:

seq.el

```mw
(require 'seq)

(defun quicksort (xs)
  (if (null xs)
      ()
    (let* ((head (car xs))
           (tail (cdr xs))
           (lower-part (quicksort (seq-filter (lambda (x) (<= x head)) tail)))
           (higher-part (quicksort (seq-filter (lambda (x) (> x head)) tail))))
      (append lower-part (list head) higher-part))))
```


## ERRE

```mw
PROGRAM QUICKSORT_DEMO

DIM ARRAY[21]

!$DYNAMIC
DIM QSTACK[0]

!$INCLUDE="PC.LIB"

PROCEDURE QSORT(ARRAY[],START,NUM)
  FIRST=START               ! initialize work variables
  LAST=START+NUM-1
  LOOP
    REPEAT
      TEMP=ARRAY[(LAST+FIRST) DIV 2]  ! seek midpoint
      I=FIRST
      J=LAST
      REPEAT     ! reverse both < and > below to sort descending
      WHILE ARRAY[I]<TEMP DO
        I=I+1
        END WHILE
        WHILE ARRAY[J]>TEMP DO
          J=J-1
        END WHILE
        EXIT IF I>J
        IF I<J THEN SWAP(ARRAY[I],ARRAY[J]) END IF
        I=I+1
        J=J-1
      UNTIL NOT(I<=J)
      IF I<LAST THEN             ! Done
         QSTACK[SP]=I            ! Push I
         QSTACK[SP+1]=LAST       ! Push Last
         SP=SP+2
      END IF
      LAST=J
    UNTIL NOT(FIRST<LAST)

    EXIT IF SP=0
    SP=SP-2
    FIRST=QSTACK[SP]            ! Pop First
    LAST=QSTACK[SP+1]           ! Pop Last
  END LOOP
END PROCEDURE

BEGIN
   RANDOMIZE(TIMER)              ! generate a new series each run

                                 ! create an array
   FOR X=1 TO 21 DO              ! fill with random numbers
       ARRAY[X]=RND(1)*500       ! between 0 and 500
   END FOR
   PRIMO=6                       ! sort starting here
   NUM=10                        ! sort this many elements
   CLS
   PRINT("Before Sorting:";TAB(31);"After sorting:")
   PRINT("===============";TAB(31);"==============")
   FOR X=1 TO 21 DO              ! show them before sorting
      IF X>=PRIMO AND X<=PRIMO+NUM-1 THEN
         PRINT("==>";)
      END IF
      PRINT(TAB(5);)
      WRITE("###.##";ARRAY[X])
   END FOR

! create a stack
!$DIM QSTACK[INT(NUM/5)+10]
   QSORT(ARRAY[],PRIMO,NUM)
!$ERASE QSTACK

   LOCATE(2,1)
   FOR X=1 TO 21 DO                ! print them after sorting
      LOCATE(2+X,30)
      IF X>=PRIMO AND X<=PRIMO+NUM-1 THEN
         PRINT("==>";)             ! point to sorted items
      END IF
      LOCATE(2+X,35)
      WRITE("###.##";ARRAY[X])
   END FOR
END PROGRAM
```


## F

```mw
let rec qsort = function
    hd :: tl ->
        let less, greater = List.partition ((>=) hd) tl
        List.concat [qsort less; [hd]; qsort greater]
    | _ -> []
```


## Factor

```mw
: qsort ( seq -- seq )
    dup empty? [ 
      unclip [ [ < ] curry partition [ qsort ] bi@ ] keep
      prefix append
    ] unless ;
```


## Fe

```mw
; utility for list joining
(= join (fn (a b)
  (if (is a nil) b (is b nil) a (do
    (let res a)
    (while (cdr a) (= a (cdr a)))
    (setcdr a b)
    res))))

(= quicksort (fn (lst)
  (if (not (cdr lst)) lst (do
    (let pivot (car lst))
    (let less nil)
    (let equal nil)
    (let greater nil)
    ; filter list for less than pivot, equal to pivot and greater than pivot
    (while lst
      (let x (car lst))
      (if (< x pivot) (= less (cons x less))
          (< pivot x) (= greater (cons x greater))
          (= equal (cons x equal)))
      (= lst (cdr lst)))
    ; sort 'less' and 'greater' partitions ('equal' partition is always sorted)
    (= less (quicksort less))
    (= greater (quicksort greater))
    ; join partitions to one
    (join less (join equal greater))))))

(print '(4 65 0 2 -31 99 2 0 83 782 1))
(print (quicksort '(4 65 0 2 -31 99 2 0 83 782 1)))
```

Outputs:

```mw
(4 65 0 2 -31 99 2 0 83 782 1)
(-31 0 0 1 2 2 4 65 83 99 782)
```


## Fexl

```mw
# (sort xs) is the ordered list of all elements in list xs.
# This version preserves duplicates.
\sort== 
    (\xs
    xs [] \x\xs
    append (sort; filter (gt x) xs);   # all the items less than x
    cons x; append (filter (eq x) xs); # all the items equal to x
    sort; filter (lt x) xs             # all the items greater than x
    )

# (unique xs) is the ordered list of unique elements in list xs.
\unique==
    (\xs
    xs [] \x\xs
    append (unique; filter (gt x) xs); # all the items less than x
    cons x;                            # x itself
    unique; filter (lt x) xs           # all the items greater than x
    )
```


## Forth

```mw
: mid ( l r -- mid ) over - 2/ -cell and + ;

: exch ( addr1 addr2 -- ) dup @ >r over @ swap ! r> swap ! ;

: partition ( l r -- l r r2 l2 )
  2dup mid @ >r ( r: pivot )
  2dup begin
    swap begin dup @  r@ < while cell+ repeat
    swap begin r@ over @ < while cell- repeat
    2dup <= if 2dup exch >r cell+ r> cell- then
  2dup > until  r> drop ;

: qsort ( l r -- )
  partition  swap rot
  \ 2over 2over - + < if 2swap then
  2dup < if recurse else 2drop then
  2dup < if recurse else 2drop then ;

: sort ( array len -- )
  dup 2 < if 2drop exit then
  1- cells over + qsort ;
```


## Fortran

Works with

:

Fortran

version 90 and later

```mw
       recursive subroutine fsort(a)
      use inserts, only:insertion_sort !Not included in this posting
      implicit none
!
! PARAMETER definitions
!
      integer, parameter  ::  changesize = 64
!
! Dummy arguments
!
      real, dimension(:) ,contiguous ::  a
      intent (inout) a
!
! Local variables
!
      integer  ::  first = 1
      integer  ::  i
      integer  ::  j
      integer  ::  last
      logical  ::  stay
      real  ::  t
      real  ::  x
!
!*Code                                                                  
!
      last = size(a, 1)
      if( (last - first)<changesize )then
          call insertion_sort(a(first:last)) 
          return
      end if
      j = shiftr((first + last), 1) + 1
                                     !
      x = a(j)
      i = first
      j = last
      stay = .true.
      do while ( stay )
          do while ( a(i)<x )
              i = i + 1
          end do
          do while ( x<a(j) )
              j = j - 1
          end do
          if( j<i )then
              stay = .false.
          else
              t = a(i)      ! Swap the values
              a(i) = a(j)
              a(j) = t
              i = i + 1     ! Adjust the pointers (PIVOT POINTS)
              j = j - 1
          end if
      end do
      if( first<i - 1 )call fsort(a(first:i - 1))   ! We still have some left to do on the lower
      if( j + 1<last )call fsort(a(j + 1:last))     ! We still have some left to do on the upper
      return
      end subroutine fsort
```


## FunL

```mw
def
  qsort( [] )    =  []
  qsort( p:xs )  =  qsort( xs.filter((< p)) ) + [p] + qsort( xs.filter((>= p)) )
```

Here is a more efficient version using the `partition` function.

```mw
def
  qsort( [] )    =  []
  qsort( x:xs )  =
    val (ys, zs) = xs.partition( (< x) )
    qsort( ys ) + (x : qsort( zs ))

println( qsort([4, 2, 1, 3, 0, 2]) )
println( qsort(["Juan", "Daniel", "Miguel", "William", "Liam", "Ethan", "Jacob"]) )
```

**Output:**

```
[0, 1, 2, 2, 3, 4]
[Daniel, Ethan, Jacob, Juan, Liam, Miguel, William]
```


## Gleam

Translation of

:

Standard ML

```mw
import gleam/int
import gleam/list
import gleam/order.{type Order, Lt}

pub fn quick_sort(xs: List(a), compare: fn(a, a) -> Order) -> List(a) {
  case xs {
    [] -> []
    [x, ..xs] -> {
      let #(left, right) = list.partition(xs, fn(y) { compare(y, x) == Lt })
      let ql = quick_sort(left, compare)
      let qr = quick_sort(right, compare)
      list.append(list.append(ql, [x]), qr)
    }
  }
}

pub fn main() {
  [31, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8] |> quick_sort(int.compare) |> echo
}
```


## Go

Note that Go's `sort.Sort` function is a Quicksort so in practice it would be just be used. It's actually a combination of quick sort, heap sort, and insertion sort. It starts with a quick sort, after a depth of 2*ceil(lg(n+1)) it switches to heap sort, or once a partition becomes small (less than eight items) it switches to insertion sort.

Old school, following Hoare's 1962 paper.

As a nod to the task request to work for all types with weak strict ordering, code below uses the < operator when comparing key values. The three points are noted in the code below.

Actually supporting arbitrary types would then require at a minimum a user supplied less-than function, and values referenced from an array of interface{} types. More efficient and flexible though is the sort interface of the Go sort package. Replicating that here seemed beyond the scope of the task so code was left written to sort an array of ints.

Go has no language support for indexing with discrete types other than integer types, so this was not coded.

Finally, the choice of a recursive closure over passing slices to a recursive function is really just a very small optimization. Slices are cheap because they do not copy the underlying array, but there's still a tiny bit of overhead in constructing the slice object. Passing just the two numbers is in the interest of avoiding that overhead.

```mw
package main

import "fmt"

func main() {
    list := []int{31, 41, 59, 26, 53, 58, 97, 93, 23, 84}
    fmt.Println("unsorted:", list)

    quicksort(list)
    fmt.Println("sorted!  ", list)
}

func quicksort(a []int) {
    var pex func(int, int)
    pex = func(lower, upper int) {
        for {
            switch upper - lower {
            case -1, 0: // 0 or 1 item in segment.  nothing to do here!
                return
            case 1: // 2 items in segment
                // < operator respects strict weak order
                if a[upper] < a[lower] {
                    // a quick exchange and we're done.
                    a[upper], a[lower] = a[lower], a[upper]
                }
                return
            // Hoare suggests optimized sort-3 or sort-4 algorithms here,
            // but does not provide an algorithm.
            }

            // Hoare stresses picking a bound in a way to avoid worst case
            // behavior, but offers no suggestions other than picking a
            // random element.  A function call to get a random number is
            // relatively expensive, so the method used here is to simply
            // choose the middle element.  This at least avoids worst case
            // behavior for the obvious common case of an already sorted list.
            bx := (upper + lower) / 2
            b := a[bx]  // b = Hoare's "bound" (aka "pivot")
            lp := lower // lp = Hoare's "lower pointer"
            up := upper // up = Hoare's "upper pointer"
        outer:
            for {
                // use < operator to respect strict weak order
                for lp < upper && !(b < a[lp]) {
                    lp++
                }
                for {
                    if lp > up {
                        // "pointers crossed!"
                        break outer
                    }
                    // < operator for strict weak order
                    if a[up] < b {
                        break // inner
                    }
                    up--
                }
                // exchange
                a[lp], a[up] = a[up], a[lp]
                lp++
                up--
            }
            // segment boundary is between up and lp, but lp-up might be
            // 1 or 2, so just call segment boundary between lp-1 and lp.
            if bx < lp {
                // bound was in lower segment
                if bx < lp-1 {
                    // exchange bx with lp-1
                    a[bx], a[lp-1] = a[lp-1], b
                }
                up = lp - 2
            } else {
                // bound was in upper segment
                if bx > lp {
                    // exchange
                    a[bx], a[lp] = a[lp], b
                }
                up = lp - 1
                lp++
            }
            // "postpone the larger of the two segments" = recurse on
            // the smaller segment, then iterate on the remaining one.
            if up-lower < upper-lp {
                pex(lower, up)
                lower = lp
            } else {
                pex(lp, upper)
                upper = up
            }
        }
    }
    pex(0, len(a)-1)
}
```

**Output:**

```
unsorted: [31 41 59 26 53 58 97 93 23 84]
sorted!   [23 26 31 41 53 58 59 84 93 97]
```

More traditional version of quicksort. It work generically with any container that conforms to `sort.Interface`.

```mw
package main

import (
    "fmt"
    "sort"
    "math/rand"
)

func partition(a sort.Interface, first int, last int, pivotIndex int) int {
    a.Swap(first, pivotIndex) // move it to beginning
    left := first+1
    right := last
    for left <= right {
        for left <= last && a.Less(left, first) {
            left++
        }
        for right >= first && a.Less(first, right) {
            right--
        }
        if left <= right {
            a.Swap(left, right)
            left++
            right--
        }
    }
    a.Swap(first, right) // swap into right place
    return right    
}

func quicksortHelper(a sort.Interface, first int, last int) {
    if first >= last {
        return
    }
    pivotIndex := partition(a, first, last, rand.Intn(last - first + 1) + first)
    quicksortHelper(a, first, pivotIndex-1)
    quicksortHelper(a, pivotIndex+1, last)
}

func quicksort(a sort.Interface) {
    quicksortHelper(a, 0, a.Len()-1)
}

func main() {
    a := []int{1, 3, 5, 7, 9, 8, 6, 4, 2}
    fmt.Printf("Unsorted: %v\n", a)
    quicksort(sort.IntSlice(a))
    fmt.Printf("Sorted: %v\n", a)
    b := []string{"Emil", "Peg", "Helen", "Juergen", "David", "Rick", "Barb", "Mike", "Tom"}
    fmt.Printf("Unsorted: %v\n", b)
    quicksort(sort.StringSlice(b))
    fmt.Printf("Sorted: %v\n", b)
}
```

**Output:**

```
Unsorted: [1 3 5 7 9 8 6 4 2]
Sorted: [1 2 3 4 5 6 7 8 9]
Unsorted: [Emil Peg Helen Juergen David Rick Barb Mike Tom]
Sorted: [Barb David Emil Helen Juergen Mike Peg Rick Tom]
```


## Golfscript

```
{.,0>{(\.{2$<!},qs\{2$<},qs@+\+}*}:qs;

[4 65 0 2 -31 99 2 0 83 782 1] $ p
[4 65 0 2 -31 99 2 0 83 782 1] qs p
```

**Output:**

```
[-31 0 0 1 2 2 4 65 83 99 782]
[-31 0 0 1 2 2 4 65 83 99 782]
```


## Haskell

The famous two-liner, reflecting the underlying algorithm directly:

```mw
qsort [] = []
qsort (x:xs) = qsort [y | y <- xs, y < x] ++ [x] ++ qsort [y | y <- xs, y >= x]
```

A more efficient version, doing only one comparison per element:

```mw
import Data.List (partition)

qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (x:xs) = qsort ys ++ [x] ++ qsort zs where
    (ys, zs) = partition (< x) xs
```


## Hobbes

```mw
qsort :: [int] -> [int]
qsort xs = if (length(xs) <= 1) then xs else let pivot = xs[0] in qsort([x | x <- [xs[i] | i <- [1L..length(xs)-1]], x < pivot]) ++ [x | x <- xs, x == pivot] ++ qsort([x | x <- [xs[i] | i <- [1L..length(xs)-1]], x > pivot])
```

**Output:**

```
> qsort([4, 65, 2, -31, 0, 99, 83, 782, 1])
[-31, 0, 1, 2, 4, 65, 83, 99, 782]
```


## Hobbes

```mw
quicksort :: [int] -> [int]
quicksort xs = if (length(xs) <= 1) then xs
               else concat((quicksort(smaller), equal, quicksort(larger)))
               where
                 pivot = xs[length(xs) / 2]
                 smaller = [x | x <- xs, x < pivot]
                 equal = [x | x <- xs, x == pivot]
                 larger = [x | x <- xs, x > pivot]

concat :: ([[int]]) -> [int]
concat xss = concatHelper((xss, 0, []))

concatHelper :: ([[int]] * int * [int]) -> [int]
concatHelper x = match x with
  | (xss, i, acc) -> if (i >= length(xss)) then acc
                     else concatHelper((xss, i + 1, acc ++ xss[i]))
```

**Output:**

```
> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]
```


## Icon and Unicon

```mw
procedure main()                     #: demonstrate various ways to sort a list and string 
   demosort(quicksort,[3, 14, 1, 5, 9, 2, 6, 3],"qwerty")
end

procedure quicksort(X,op,lower,upper)                      #: return sorted list
local pivot,x 

   if /lower := 1 then {                                   # top level call setup
      upper := *X   
      op := sortop(op,X)                                   # select how and what we sort
      }

   if upper - lower > 0 then {
      every x := quickpartition(X,op,lower,upper) do       # find a pivot and sort ...
          /pivot | X := x                                  # ... how to return 2 values w/o a structure
      X := quicksort(X,op,lower,pivot-1)                   # ... left            
      X := quicksort(X,op,pivot,upper)                     # ... right
      }

   return X                                             
end

procedure quickpartition(X,op,lower,upper)                 #: quicksort partitioner helper
local   pivot
static  pivotL
initial pivotL := list(3)

   pivotL[1] := X[lower]                                   # endpoints
   pivotL[2] := X[upper]                                   # ... and
   pivotL[3] := X[lower+?(upper-lower)]                    # ... random midpoint
   if op(pivotL[2],pivotL[1]) then pivotL[2] :=: pivotL[1] # mini-
   if op(pivotL[3],pivotL[2]) then pivotL[3] :=: pivotL[2] # ... sort
   pivot := pivotL[2]                                      # median is pivot

   lower -:= 1
   upper +:= 1
   while lower < upper do {                                # find values on wrong side of pivot ...
      while op(pivot,X[upper -:= 1])                       # ... rightmost 
      while op(X[lower +:=1],pivot)                        # ... leftmost
      if lower < upper then                                # not crossed yet
         X[lower] :=: X[upper]                             # ... swap 
      }

   suspend lower                                           # 1st return pivot point
   suspend X                                               # 2nd return modified X (in case immutable)
end
```

Implementation notes:

- Since this transparently sorts both string and list arguments the result must 'return' to bypass call by value (strings)
- The partition procedure must "return" two values - 'suspend' is used to accomplish this

Algorithm notes:

- The use of a type specific sorting operator meant that a general pivot choice need to be made. The median of the ends and random middle seemed reasonable. It turns out to have been suggested by Sedgewick.
- Sedgewick's suggestions for tail calling to recurse into the larger side and using insertion sort below a certain size were not implemented. (Q: does Icon/Unicon has tail calling optimizations?)

Note: This example relies on the supporting procedures 'sortop', and 'demosort' in Bubble Sort. The full demosort exercises the named sort of a list with op = "numeric", "string", ">>" (lexically gt, descending),">" (numerically gt, descending), a custom comparator, and also a string.

**Output:**

Abbreviated

```
Sorting Demo using procedure quicksort
  on list : [ 3 14 1 5 9 2 6 3 ]
    with op = &null:         [ 1 2 3 3 5 6 9 14 ]   (0 ms)
  ...
  on string : "qwerty"
    with op = &null:         "eqrtwy"   (0 ms)
```


## IDL

IDL has a powerful optimized sort() built-in. The following is thus merely for demonstration.

```mw
function qs, arr
  if (count = n_elements(arr)) lt 2 then return,arr
  pivot = total(arr) / count ; use the average for want of a better choice
  return,[qs(arr[where(arr le pivot)]),qs(arr[where(arr gt pivot)])]
 end
```

Example:

```
IDL> print,qs([3,17,-5,12,99])
     -5       3      12      17      99
```


## Idris

```mw
quicksort : Ord elem => List elem -> List elem
quicksort [] = []
quicksort (x :: xs) =
  let lesser = filter (< x) xs
      greater = filter(>= x) xs in
        (quicksort lesser) ++ [x] ++ (quicksort greater)
```

Example:

```
*quicksort> quicksort [1, 3, 7, 2, 5, 4, 9, 6, 8, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] : List Integer
```


## Io

```mw
List do(
    quickSort := method(
        if(size > 1) then(
            pivot := at(size / 2 floor)
            return select(x, x < pivot) quickSort appendSeq(
                select(x, x == pivot) appendSeq(select(x, x > pivot) quickSort)
            )
        ) else(return self)
    )

    quickSortInPlace := method(
        copy(quickSort)
    )
)

lst := list(5, -1, -4, 2, 9)
lst quickSort println # ==> list(-4, -1, 2, 5, 9)
lst quickSortInPlace println # ==> list(-4, -1, 2, 5, 9)
```

Another more low-level Quicksort implementation can be found in Io's [github ] repository.


## Isabelle

```mw
theory Quicksort
imports Main
begin

fun quicksort :: "('a :: linorder) list ⇒ 'a list" where
  "quicksort [] = []"
| "quicksort (x#xs) = (quicksort [y←xs. y<x]) @ [x] @ (quicksort [y←xs. y>x])"

lemma "quicksort [4::int, 2, 7, 1] = [1, 2, 4, 7]"
  by(code_simp)

lemma set_first_second_partition:
  fixes x :: "'a :: linorder"
  shows "{y ∈ ys. y < x} ∪ {x} ∪ {y ∈ ys. x < y} =
         insert x ys"
  by fastforce

lemma set_quicksort: "set (quicksort xs) = set xs"
  by(induction xs rule: quicksort.induct)
    (simp add: set_first_second_partition[simplified])+

theorem "sorted (quicksort xs)" 
proof(induction xs rule: quicksort.induct)
  case 1
  show "sorted (quicksort [])" by simp
next
  case (2 x xs)
  assume IH_less:    "sorted (quicksort [y←xs. y<x])"
  assume IH_greater: "sorted (quicksort [y←xs. y>x])"
  have pivot_geq_first_partition:
    "∀z∈set (quicksort [y←xs. y<x]). z ≤ x"
    by (simp add: set_quicksort less_imp_le)
  have pivot_leq_second_partition:
    "∀z ∈ (set (quicksort [y←xs. y>x])). (x ≤ z)"
    by (simp add: set_quicksort less_imp_le)
  have first_partition_leq_second_partition:
    "∀p∈set (quicksort [y←xs. y<x]).
        ∀z ∈ (set (quicksort [y←xs. y>x])). (p ≤ z)"
    by (auto simp add: set_quicksort)
    
  from IH_less IH_greater
       pivot_geq_first_partition pivot_leq_second_partition
       first_partition_leq_second_partition
  show "sorted (quicksort (x # xs))"  by(simp add: sorted_append)
qed

text‹
The specification on rosettacode says
 ▪ All elements less than the pivot must be in the first partition.
 ▪ All elements greater than the pivot must be in the second partition.
Since this specification neither says "less than or equal" nor
"greater or equal", this quicksort implementation removes duplicate elements.
›
lemma "quicksort [1::int, 1, 1, 2, 2, 3] = [1, 2, 3]"
  by(code_simp)

text‹If we try the following, we automatically get a counterexample›
lemma "length (quicksort xs) = length xs"
(*
  Auto Quickcheck found a counterexample:
    xs = [a⇩1, a⇩1]
  Evaluated terms:
    length (quicksort xs) = 1
    length xs = 2
*)
  oops
end
```


## J

Generally, this task should be accomplished in J using

/:~

. Here we take an approach that's more comparable with the other examples on this page.

Translation of

:

K

A two-partition tacit version with random pivot:

```mw
qsort=: (((<:#[) ,&$: (>#[)) (?@#{]))^:(1<#@~.)
```

Use:

```mw
   qsort 7 4 1 5 9 8 2 4 6
```

**Output:**

```
1 2 4 4 5 6 7 8 9
```

A three-partition explicit version broken into smaller steps:

```mw
sel=: 1 : 'u # ]'

quicksort=: 3 : 0
 if.
  1 >: #y
 do.
  y
 else.
  p=. y{~?#y 
  (quicksort y <sel p),(y =sel p),quicksort y >sel p
 end.
)
```

See the Quicksort essay in the J Wiki for additional explanations and examples.


## Jactl

```mw
def qsort(x) {
  switch(x) {
    [],[_] -> x
    [h,*t] -> qsort(t.filter{it <= h}) + [h] + qsort(t.filter{it > h})
  }
}

def list = 10.map{ random(20) }
println qsort(list)
```

**Output:**

```
[1, 6, 6, 7, 9, 9, 11, 15, 16, 18]
```
