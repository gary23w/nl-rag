---
title: "Sorting algorithms/Quicksort (part 5/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/8
---

## Java

### Imperative

Works with

:

Java

version 1.5+

Translation of

:

Python

```mw
public static <E extends Comparable<? super E>> List<E> quickSort(List<E> arr) {
    if (arr.isEmpty())
        return arr;
    else {
        E pivot = arr.get(0);

        List<E> less = new LinkedList<E>();
        List<E> pivotList = new LinkedList<E>();
        List<E> more = new LinkedList<E>();

        // Partition
        for (E i: arr) {
            if (i.compareTo(pivot) < 0)
                less.add(i);
            else if (i.compareTo(pivot) > 0)
                more.add(i);
            else
                pivotList.add(i);
        }

        // Recursively sort sublists
        less = quickSort(less);
        more = quickSort(more);

        // Concatenate results
        less.addAll(pivotList);
        less.addAll(more);
        return less;
    }
}
```

### Functional

Works with

:

Java

version 1.8

```mw
public static <E extends Comparable<E>> List<E> sort(List<E> col) {
    if (col == null || col.isEmpty())
        return Collections.emptyList();
    else {
        E pivot = col.get(0);
        Map<Integer, List<E>> grouped = col.stream()
                .collect(Collectors.groupingBy(pivot::compareTo));
        return Stream.of(sort(grouped.get(1)), grouped.get(0), sort(grouped.get(-1)))
                .flatMap(Collection::stream).collect(Collectors.toList());
    }
}
```


## JavaScript

### Imperative

```mw
function sort(array, less) {

  function swap(i, j) {
    var t = array[i];
    array[i] = array[j];
    array[j] = t;
  }

  function quicksort(left, right) {

    if (left < right) {
      var pivot = array[left + Math.floor((right - left) / 2)],
          left_new = left,
          right_new = right;

      do {
        while (less(array[left_new], pivot)) {
          left_new += 1;
        }
        while (less(pivot, array[right_new])) {
          right_new -= 1;
        }
        if (left_new <= right_new) {
          swap(left_new, right_new);
          left_new += 1;
          right_new -= 1;
        }
      } while (left_new <= right_new);

      quicksort(left, right_new);
      quicksort(left_new, right);

    }
  }

  quicksort(0, array.length - 1);

  return array;
}
```

Example:

```mw
var test_array = [10, 3, 11, 15, 19, 1];
var sorted_array = sort(test_array, function(a,b) { return a<b; });
```

**Output:**

```mw
[ 1, 3, 10, 11, 15, 19 ]
```

### Functional

#### ES6

Using **destructuring** and **satisfying immutability** we can propose a single expresion solution (from https://github.com/ddcovery/expressive_sort)

```mw
const qsort = ([pivot, ...others]) => 
  pivot === void 0 ? [] : [
    ...qsort(others.filter(n => n < pivot)),
    pivot,
    ...qsort(others.filter(n => n >= pivot))
  ];

qsort( [ 11.8, 14.1, 21.3, 8.5, 16.7, 5.7 ] )
```

**Output:**

```
[ 5.7, 8.5, 11.8, 14.1, 16.7, 21.3 ]
```

#### ES5

Unlike what happens with ES6, there are no destructuring nor lambdas, but we can **ensure immutability** and propose a **single expression** solution with standard anonymous functions

```mw
function qsort( xs ){
  return xs.length === 0 ? [] : [].concat(
    qsort( xs.slice(1).filter(function(x){ return x< xs[0] })),
    xs[0],
    qsort( xs.slice(1).filter(function(x){ return x>= xs[0] }))
  )
}
qsort( [ 11.8, 14.1, 21.3, 8.5, 16.7, 5.7 ] )
```

**Output:**

```
[5.7, 8.5, 11.8, 14.1, 16.7, 21.3]
```


## Joy

```mw
DEFINE qsort ==
  [small]            # termination condition: 0 or 1 element
  []                 # do nothing
  [uncons [>] split] # pivot and two lists
  [enconcat]         # insert the pivot after the recursion
  binrec.            # recursion on the two lists
```


## jq

jq's built-in sort currently (version 1.4) uses the standard C qsort, a quicksort. sort can be used on any valid JSON array.

Example:

```mw
[1, 1.1, [1,2], true, false, null, {"a":1}, null] | sort
```

**Output:**

```mw
[null,null,false,true,1,1.1,[1,2],{"a":1}]
```

Here is an implementation in jq of the pseudo-code (and comments :-) given at the head of this article:

```mw
def quicksort:
  if length < 2 then .                            # it is already sorted
  else .[0] as $pivot
       | reduce .[] as $x
         # state: [less, equal, greater]
           ( [ [], [], [] ];                      # three empty arrays:
             if   $x  < $pivot then .[0] += [$x]  # add x to less
             elif $x == $pivot then .[1] += [$x]  # add x to equal
             else                   .[2] += [$x]  # add x to greater
             end
         )
       | (.[0] | quicksort ) + .[1] + (.[2] | quicksort )
  end ;
```

Fortunately, the example input used above produces the same output,

and so both are omitted here.


## Julia

Built-in function for in-place sorting via quicksort (the code from the standard library is quite readable):

```mw
sort!(A, alg=QuickSort)
```

A simple polymorphic implementation of an in-place recursive quicksort (based on the pseudocode above):

```mw
function quicksort!(A,i=1,j=length(A))
    if j > i
        pivot = A[rand(i:j)] # random element of A
        left, right = i, j
        while left <= right
            while A[left] < pivot
                left += 1
            end
            while A[right] > pivot
                right -= 1
            end
            if left <= right
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            end
        end
        quicksort!(A,i,right)
        quicksort!(A,left,j)
    end
    return A
end
```

A one-line (but rather inefficient) implementation based on the Haskell version, which operates out-of-place and allocates temporary arrays:

```mw
qsort(L) = isempty(L) ? L : vcat(qsort(filter(x -> x < L[1], L[2:end])), L[1:1], qsort(filter(x -> x >= L[1], L[2:end])))
```

**Output:**

```
julia> A = [84,77,20,60,47,20,18,97,41,49,31,39,73,68,65,52,1,92,15,9]

julia> qsort(A)
[1,9,15,18,20,20,31,39,41,47,49,52,60,65,68,73,77,84,92,97]

julia> quicksort!(copy(A))
[1,9,15,18,20,20,31,39,41,47,49,52,60,65,68,73,77,84,92,97]

julia> qsort(A) == quicksort!(copy(A)) == sort(A) == sort(A, alg=QuickSort)
true
```


## K


## Bi-partition

Works with

:

ngn/k

```mw
qsort:{$[2>#?x;x;,/o'x@&'~:\x<*1?x]}
```

This version partitions the array into [elements greater than or equal to the pivot], and [those less than the pivot], stopping recursion when the subarray contains only one unique element.

The `$[...]` works as `$[if;then;else]`.

`x<*1?x` selects a random pivot and gives a logical mask (vector of 0’s and 1’s) where a 1 at index n indicates that the element at n is less than the pivot.

`f\` successively applies f until the result converges (i.e., yields a result from a prior iteration), and collects the intermediate results (including the initial argument). Since f is negation here, this happens after one iteration. Each mask is coupled with its negation, e.g., `~:\0 1 1` produces `(0 1 1;1 0 0)`.

`x@&'` converts each logical mask into corresponding indices, and uses them to index into array x, yielding the two partitions.

Finally, `,/o'` recurses on each partition and joins the results.


## Tri-partition

A 3-partition version (faster if many elements are equal):

```mw
quicksort:{p:*x[1?#x];:[0=#x;x;,/(_f x[&x<p];x[&x=p];_f x[&x>p])]}
```

Example:

```mw
    quicksort 1 3 5 7 9 8 6 4 2
```

**Output:**

```
1 2 3 4 5 6 7 8 9
```

Explanation:

```mw
  _f
```

is the current function called recursively.

```mw
   :[....]
```

generally means :[condition1;then1;condition2;then2;....;else]. Here it is used as :[if;then;else].

This construct

```mw
   p:*x[1?#x]
```

assigns a random element in x (the argument) to p, as the pivot value.

And here is the full if/then/else clause:

```mw
    :[
        0=#x;           / if length of x is zero 
        x;              / then return x
                        / else
        ,/(             / join the results of: 
          _f x[&x<p]         / sort (recursively) elements less than pivot p
          x[&x=p]            / elements equal to p 
          _f x[&x>p])        / sort (recursively) elements greater than p 
     ]
```

Note that - as with APL and J - for larger arrays it's much faster to sort using "<" (grade up) which gives the indices of the list sorted ascending, i.e.

```mw
   t@<t:1 3 5 7 9 8 6 4 2
1 2 3 4 5 6 7 8 9
```


## Koka

Haskell-like solution

```mw
fun qsort( xs : list<int> ) : div list<int> {
  match(xs) {
    Cons(x,xx) -> {
      val ys = xx.filter fn(el) { el < x }
      val zs = xx.filter fn(el) { el >= x }
      qsort(ys) ++ [x] ++ qsort(zs)
    }
    Nil -> Nil
  }
}
```

or using standard `partition` function

```mw
fun qsort( xs : list<int> ) : div list<int> {
  match(xs) {
    Cons(x,xx) -> {
      val (ys, zs) = xx.partition fn(el) { el < x }
      qsort(ys) ++ [x] ++ qsort(zs)
    }
    Nil -> Nil
  }
}
```

Example:

```mw
fun main() {
  val arr = [24,63,77,26,84,64,56,80,85,17]
  println(arr.qsort.show)
}
```

**Output:**

```
[17,24,26,56,63,64,77,80,84,85]
```


## Kotlin

A version that reflects the algorithm directly:

```mw
fun <E : Comparable<E>> List<E>.qsort(): List<E> =
        if (size < 2) this
        else filter { it < first() }.qsort() +
                filter { it == first() } +
                filter { it > first() }.qsort()
```

A more efficient version that does only one comparison per element:

```mw
fun <E : Comparable<E>> List<E>.qsort(): List<E> =
        if (size < 2) this
        else {
            val (less, high) = subList(1, size).partition { it < first() }
            less.qsort() + first() + high.qsort()
        }
```


## Lambdatalk

```mw
We create a binary tree from a random array, then we walk the canopy.

1) three functions for readability:         
 
{def BT.data  {lambda {:t} {A.get 0 :t}}} -> BT.data
{def BT.left  {lambda {:t} {A.get 1 :t}}} -> BT.left
{def BT.right {lambda {:t} {A.get 2 :t}}} -> BT.right

2) adding a leaf to the tree: 

{def BT.add {lambda {:x :t}
 {if {A.empty? :t}
  then {A.new :x {A.new} {A.new}}
  else {if   {= :x {BT.data :t}}
        then :t
        else {if {< :x {BT.data :t}}
              then {A.new {BT.data :t} 
                          {BT.add :x {BT.left :t}}
                          {BT.right :t}}
              else {A.new {BT.data :t} 
                          {BT.left :t}
                          {BT.add :x {BT.right :t}} }}}}}}
-> BT.add

3) creating the tree from an array of numbers:

{def BT.create           
 {def BT.create.rec
  {lambda {:l :t}
   {if {A.empty? :l}
    then :t
    else {BT.create.rec {A.rest :l}
                        {BT.add {A.first :l} :t}} }}}
 {lambda {:l}
  {BT.create.rec :l {A.new}} }}
-> BT.create

4) walking the canopy -> sorting in increasing order:

{def BT.sort
 {lambda {:t}
  {if {A.empty? :t}
   then else {BT.sort {BT.left :t}}
             {BT.data :t}
             {BT.sort {BT.right :t}} }}}   
-> BT.sort

Testing

1) generating random numbers:

{def L {A.new 
 {S.map {lambda {:n} {floor {* {random} 100000}}} {S.serie 1 100}}}} 
-> L =  [1850,7963,50540,92667,72892,47361,19018,40640,10126,80235,48407,51623,63597,71675,27814,63478,18985,88032,46585,85209,
74053,95005,27592,9575,22162,35904,70467,38527,89715,36594,54309,39950,89345,72224,7772,65756,68766,43942,52422,85144,
66010,38961,21647,53194,72166,33545,49037,23218,27969,83566,19382,53120,55291,77374,27502,66648,99637,37322,9815,432,90565,
37831,26503,99232,87024,65625,75155,55382,30120,58117,70031,13011,81375,10490,39786,1926,71311,4213,55183,2583,22075,90411,
92928,61120,94259,433,93332,88423,64119,40850,94318,27816,84818,90632,5094,36696,94705,50602,45818,61365]

2) creating the tree is the main work:

{def T {BT.create {L}}} 
-> T = [1850,[432,],[433,],]]],[7963,[7772,[1926,],[4213,[2583,],]],[5094,],]]]],]],[50540,[47361,[19018,[10126,[9575,],
[9815,],]]],[18985,[13011,[10490,],]],]],]]],[40640,[27814,[27592,[22162,[21647,[19382,],]],[22075,],]]],[23218,],
[27502,[26503,],]],]]]],]],[35904,[33545,[27969,[27816,],]],[30120,],]]],]],[38527,[36594,],[37322,[36696,],]],[37831,],]]]],
[39950,[38961,],[39786,],]]],]]]]],[46585,[43942,[40850,],]],[45818,],]]],]]]],[48407,],[49037,],]]]],[92667,[72892,
[51623,[50602,],]],[63597,[63478,[54309,[52422,],[53194,[53120,],]],]]],[55291,[55183,],]],[55382,],[58117,],[61120,],[61365,],]]]]]]],]],[71675,[70467,[65756,[65625,[64119,],]],]],[68766,[66010,],[66648,],]]],[70031,],]]]],[71311,],]]],
[72224,[72166,],]],]]]]],[80235,[74053,],[77374,[75155,],]],]]],[88032,[85209,[85144,[83566,[81375,],]],[84818,],]]],]],
[87024,],]]],[89715,[89345,[88423,],]],]],[90565,[90411,],]],[90632,],]]]]]]],[95005,[92928,],[94259,[93332,],]],[94318,],
[94705,],]]]]],[99637,[99232,],]],]]]]]]]

3) walking the canopy is fast:   

{BT.sort {T}}
->  432 433 1850 1926 2583 4213 5094 7772 7963 9575 9815 10126 10490 13011 18985 19018 19382 21647 22075 22162 23218 26503
 27502 27592 27814 27816 27969 30120 33545 35904 36594 36696 37322 37831 38527 38961 39786 39950 40640 40850 43942 45818
 46585 47361 48407 49037 50540 50602 51623 52422 53120 53194 54309 55183 55291 55382 58117 61120 61365 63478 63597 64119
 65625 65756 66010 66648 68766 70031 70467 71311 71675 72166 72224 72892 74053 75155 77374 80235 81375 83566 84818 85144
 85209 87024 88032 88423 89345 89715 90411 90565 90632 92667 92928 93332 94259 94318 94705 95005 99232 99637     

4) walking with new leaves is fast:

{BT.sort {BT.add -1 {T}}}
->  -1 432 433 1850 1926 2583 4213 5094 7772 7963 9575 9815 10126 10490 13011 18985 19018 19382 21647 22075 22162 23218 26503
 27502 27592 27814 27816 27969 30120 33545 35904 36594 36696 37322 37831 38527 38961 39786 39950 40640 40850 43942 45818 46585
 47361 48407 49037 50540 50602 51623 52422 53120 53194 54309 55183 55291 55382 58117 61120 61365 63478 63597 64119 65625 65756
 66010 66648 68766 70031 70467 71311 71675 72166 72224 72892 74053 75155 77374 80235 81375 83566 84818 85144 85209 87024 88032
 88423 89345 89715 90411 90565 90632 92667 92928 93332 94259 94318 94705 95005 99232 99637

{BT.sort {BT.add 50000 {T}}}
->  432 433 1850 1926 2583 4213 5094 7772 7963 9575 9815 10126 10490 13011 18985 19018 19382 21647 22075 22162 23218 26503
 27502 27592 27814 27816 27969 30120 33545 35904 36594 36696 37322 37831 38527 38961 39786 39950 40640 40850 43942 45818 46585
 47361 48407 49037 50000 50540 50602 51623 52422 53120 53194 54309 55183 55291 55382 58117 61120 61365 63478 63597 64119 65625
 65756 66010 66648 68766 70031 70467 71311 71675 72166 72224 72892 74053 75155 77374 80235 81375 83566 84818 85144 85209 87024
 88032 88423 89345 89715 90411 90565 90632 92667 92928 93332 94259 94318 94705 95005 99232 99637

{BT.sort {BT.add 100000 {T}}}
->  432 433 1850 1926 2583 4213 5094 7772 7963 9575 9815 10126 10490 13011 18985 19018 19382 21647 22075 22162 23218 26503
 27502 27592 27814 27816 27969 30120 33545 35904 36594 36696 37322 37831 38527 38961 39786 39950 40640 40850 43942 45818 46585
 47361 48407 49037 50540 50602 51623 52422 53120 53194 54309 55183 55291 55382 58117 61120 61365 63478 63597 64119 65625 65756
 66010 66648 68766 70031 70467 71311 71675 72166 72224 72892 74053 75155 77374 80235 81375 83566 84818 85144 85209 87024 88032
 88423 89345 89715 90411 90565 90632 92667 92928 93332 94259 94318 94705 95005 99232 99637 100000
```


## Lobster

```mw
include "std.lobster"

def quicksort(xs, lt):
    if xs.length <= 1:
        xs
    else:
        pivot := xs[0]
        tail := xs.slice(1, -1)
        f1 := filter tail:  lt(_, pivot)
        f2 := filter tail: !lt(_, pivot)
        append(append(quicksort(f1, lt), [ pivot ]),
                      quicksort(f2, lt))

sorted := [ 3, 9, 5, 4, 1, 3, 9, 5, 4, 1 ].quicksort(): _a < _b
print sorted
```


## Logo

```mw
; quicksort (lists, functional)

to small? :list
  output or [empty? :list] [empty? butfirst :list]
end
to quicksort :list
  if small? :list [output :list]
  localmake "pivot first :list
  output (sentence
    quicksort filter [? < :pivot] butfirst :list
              filter [? = :pivot]          :list
    quicksort filter [? > :pivot] butfirst :list
  )
end

show quicksort [1 3 5 7 9 8 6 4 2]
```

```mw
; quicksort (arrays, in-place)

to incr :name
  make :name (thing :name) + 1
end
to decr :name
  make :name (thing :name) - 1
end
to swap :i :j :a
  localmake "t item :i :a
  setitem :i :a item :j :a
  setitem :j :a :t
end

to quick :a :low :high
  if :high <= :low [stop]
  localmake "l :low
  localmake "h :high
  localmake "pivot item ashift (:l + :h) -1  :a
  do.while [
    while [(item :l :a) < :pivot] [incr "l]
    while [(item :h :a) > :pivot] [decr "h]
    if :l <= :h [swap :l :h :a  incr "l  decr "h]
  ] [:l <= :h]
  quick :a :low :h
  quick :a :l :high
end
to sort :a
  quick :a first :a count :a
end

make "test {1 3 5 7 9 8 6 4 2}
sort :test
show :test
```


## Logtalk

```mw
quicksort(List, Sorted) :-
    quicksort(List, [], Sorted).

quicksort([], Sorted, Sorted).
quicksort([Pivot| Rest], Acc, Sorted) :- 
    partition(Rest, Pivot, Smaller0, Bigger0),
    quicksort(Smaller0, [Pivot| Bigger], Sorted),
    quicksort(Bigger0, Acc, Bigger).

partition([], _, [], []).
partition([X| Xs], Pivot, Smalls, Bigs) :-
    (   X @< Pivot ->
        Smalls = [X| Rest],
        partition(Xs, Pivot, Rest, Bigs)
    ;   Bigs = [X| Rest],
        partition(Xs, Pivot, Smalls, Rest)
    ).
```


## Lua

NOTE: If you want to use quicksort in a Lua script, you don't need to implement it yourself. Just do:

```
table.sort(tableName)
```

### in-place

```mw
--in-place quicksort
function quicksort(t, start, endi)
  start, endi = start or 1, endi or #t
  --partition w.r.t. first element
  if(endi - start < 1) then return t end
  local pivot = start
  for i = start + 1, endi do
    if t[i] <= t[pivot] then
      if i == pivot + 1 then
        t[pivot],t[pivot+1] = t[pivot+1],t[pivot]
      else
        t[pivot],t[pivot+1],t[i] = t[i],t[pivot],t[pivot+1]
      end
      pivot = pivot + 1
    end
  end
  t = quicksort(t, start, pivot - 1)
  return quicksort(t, pivot + 1, endi)
end

--example
print(unpack(quicksort{5, 2, 7, 3, 4, 7, 1}))
```

### non in-place

```mw
function quicksort(t)
  if #t<2 then return t end
  local pivot=t[1]
  local a,b,c={},{},{}
  for _,v in ipairs(t) do
    if     v<pivot then a[#a+1]=v
    elseif v>pivot then c[#c+1]=v
    else                b[#b+1]=v
    end
  end
  a=quicksort(a)
  c=quicksort(c)
  for _,v in ipairs(b) do a[#a+1]=v end
  for _,v in ipairs(c) do a[#a+1]=v end
  return a
end
```


## Lucid

[1]

```mw
qsort(a) = if eof(first a) then a else follow(qsort(b0),qsort(b1)) fi
 where
    p = first a < a;
    b0 = a whenever p;
    b1 = a whenever not p;
    follow(x,y) = if xdone then y upon xdone else x fi
                    where
                       xdone = iseod x fby xdone or iseod x; 
                    end;
 end
```


## M2000 Interpreter

### Recursive calling Functions

```mw
Module Checkit1 {
      Group Quick {
      Private:
            Function partition {
                     Read &A(), p, r
                     x = A(r)
                     i = p-1
                     For j=p to r-1 {
                         If .LE(A(j), x) Then {
                                i++
                                Swap A(i),A(j)
                             }
                      }
                      Swap A(i+1),A(r)
                     = i+1
                  }
      Public:
            LE=Lambda->Number<=Number
            Function quicksort {
                 Read &A(), p, r
                 If p < r Then {
                   q = .partition(&A(), p, r)
                   Call .quicksort(&A(), p, q - 1)
                   Call .quicksort(&A(), q + 1, r)
                }
            }
      }
      Dim A(10)<<Random(50, 100)
      Print A()
      Call Quick.quicksort(&A(), 0, Len(A())-1)
      Print A()
}
Checkit1
```

### Recursive calling Subs

Variables p, r, q removed from quicksort function. we use stack for values. Also Partition push to stack now. Works for string arrays too.

```mw
Module Checkit2 {
      Class Quick {
      Private:
            partition=lambda-> {
                  Read &A(), p, r : i = p-1 : x=A(r)
                  For j=p to r-1 {If .LE(A(j), x) Then i++:Swap A(i),A(j)
                  } : Swap A(i+1), A(r) :  Push i+1
            }
      Public:
            LE=Lambda->Number<=Number
            Module ForStrings {
                  .partition<=lambda-> {
                        Read &A$(), p, r : i = p-1 : x$=A$(r)
                        For j=p to r-1 {If A$(j)<= x$ Then i++:Swap A$(i),A$(j)
                        } : Swap A$(i+1), A$(r) : Push i+1
                  }
            }
            Function quicksort (ref$) {
                  myQuick()
                  sub myQuick()
                        If Stackitem() >= stackitem(2) Then drop 2 : Exit Sub
                        Over 2, 2 : Call .partition(ref$) : Over : Shiftback  3, 2
                        myQuick(number,  number - 1)
                        myQuick( number + 1, number)
                  End Sub
             } 
      }
      Quick=Quick()
      Dim A(10)
      A(0):=57, 83, 74, 98, 51, 73, 85, 76, 65, 92
      Print A()
      Call Quick.quicksort(&A(), 0, Len(A())-1)
      Print A()
      Quick=Quick()
      Quick.ForStrings
      Dim A$()
      A$()=("one","two", "three","four", "five")
      Print A$()
      Call Quick.quicksort(&A$(), 0, Len(A$())-1)
      Print A$()
}
Checkit2
```

### Non Recursive

Partition function return two values (where we want q, and use it as q-1 an q+1 now Partition() return final q-1 and q+1_ Example include numeric array, array of arrays (we provide a lambda for comparison) and string array.

```mw
Module Checkit3 {
      Class Quick {
      Private:
            partition=lambda-> {
                  Read &A(), p, r : i = p-1 : x=A(r)
                  For j=p to r-1 {If .LE(A(j), x) Then i++:Swap A(i),A(j)
                  } : Swap A(i+1), A(r) :  Push  i+2, i 
            }
      Public:
            LE=Lambda->Number<=Number
            Module ForStrings {
                  .partition<=lambda-> {
                        Read &A$(), p, r : i = p-1 : x$=A$(r)
                        For j=p to r-1 {If A$(j)<= x$ Then i++:Swap A$(i),A$(j)
                        } : Swap A$(i+1), A$(r) : Push i+2, i
                  }
            }
            Function quicksort {
                 Read ref$
                 {
                         loop : If Stackitem() >= Stackitem(2) Then Drop 2 : if  empty then {Break} else continue
                         over 2,2 : call .partition(ref$) :shift 3 
                 }
            }
      }
      Quick=Quick()
      Dim A(10)<<Random(50, 100)
      Print A()
      Call Quick.quicksort(&A(), 0, Len(A())-1)
      Print A()
      Quick=Quick()
      Function join$(a$()) {
            n=each(a$(), 1, -2)
            k$=""
            while n {
                  overwrite k$, ".", n^:=array$(n)
            }
            =k$
      }
      Stack New {
                  Data "1.3.6.1.4.1.11.2.17.19.3.4.0.4" , "1.3.6.1.4.1.11.2.17.19.3.4.0.1", "1.3.6.1.4.1.11150.3.4.0.1"
                  Data "1.3.6.1.4.1.11.2.17.19.3.4.0.10", "1.3.6.1.4.1.11.2.17.5.2.0.79", "1.3.6.1.4.1.11150.3.4.0"
                  Dim Base 0, arr(Stack.Size)
                  Link arr() to arr$()
                  i=0 : While not Empty {arr$(i)=piece$(letter$+".", ".") : i++ }
      }
      \\ change comparison function
      Quick.LE=lambda (a, b)->{
            Link a, b to a$(), b$()
             def i=-1
             do {
                   i++
             } until a$(i)="" or b$(i)="" or a$(i)<>b$(i)
             if b$(i)="" then =a$(i)="":exit
             if a$(i)="" then =true:exit
             =val(a$(i))<=val(b$(i))
      }
      Call Quick.quicksort(&arr(), 0, Len(arr())-1)
      For i=0 to len(arr())-1 {
            Print join$(arr(i))
      }
      \\ Fresh load
      Quick=Quick()
      Quick.ForStrings
      Dim A$()
      A$()=("one","two", "three","four", "five")
      Print A$()
      Call Quick.quicksort(&A$(), 0, Len(A$())-1)
      Print A$()
}
Checkit3
```


## M4

```mw
dnl  return the first element of a list when called in the funny way seen below
define(`arg1', `$1')dnl
dnl
dnl  append lists 1 and 2
define(`append',
   `ifelse(`$1',`()',
      `$2',
      `ifelse(`$2',`()',
         `$1',
         `substr($1,0,decr(len($1))),substr($2,1)')')')dnl
dnl
dnl  separate list 2 based on pivot 1, appending to left 3 and right 4,
dnl  until 2 is empty, and then combine the sort of left with pivot with
dnl  sort of right
define(`sep',
   `ifelse(`$2', `()',
      `append(append(quicksort($3),($1)),quicksort($4))',
      `ifelse(eval(arg1$2<=$1),1,
         `sep($1,(shift$2),append($3,(arg1$2)),$4)',
         `sep($1,(shift$2),$3,append($4,(arg1$2)))')')')dnl
dnl
dnl  pick first element of list 1 as pivot and separate based on that
define(`quicksort',
   `ifelse(`$1', `()',
      `()',
      `sep(arg1$1,(shift$1),`()',`()')')')dnl
dnl
quicksort((3,1,4,1,5,9))
```

**Output:**

```
(1,1,3,4,5,9)
```


## Maclisp

```mw
;; While not strictly required, it simplifies the
;; implementation considerably to use filter. MACLisp
;; Doesn't have one out of the box, so we bring our own
(DEFUN FILTER (F LIST)
        (COND
         ((EQ LIST NIL) NIL)
         ((FUNCALL F (CAR LIST))
          (CONS (CAR LIST) (FILTER F (CDR LIST))))
         (T
          (FILTER F (CDR LIST)))))

;; And then, quicksort.
(DEFUN QUICKSORT (LIST)
    (COND
     ((OR (EQ LIST ())
          (EQ (CDR LIST) ()))
      LIST)
     (T
      (LET
        ((PIVOT (CAR LIST))
         (REST (CDR LIST)))
        (APPEND
            (QUICKSORT (FILTER #'(LAMBDA (X) (<= X PIVOT)) REST))
            (LIST PIVOT)
            (QUICKSORT (FILTER #'(LAMBDA (X) (> X PIVOT)) REST)))))))
```


## Maple

```mw
swap := proc(arr, a, b)
   local temp := arr[a]:
   arr[a] := arr[b]:
   arr[b] := temp:
end proc:
quicksort := proc(arr, low, high)
   local pi:
   if (low < high) then
      pi := qpart(arr,low,high):
      quicksort(arr, low, pi-1):
      quicksort(arr, pi+1, high):
   end if:
end proc:
qpart := proc(arr, low, high)
   local i,j,pivot;
   pivot := arr[high]:
   i := low-1:
   for j from low to high-1 by 1 do
      if (arr[j] <= pivot) then
         i++:
         swap(arr, i, j):
      end if;
   end do;
   swap(arr, i+1, high):
   return (i+1):
end proc:
a:=Array([12,4,2,1,0]);
quicksort(a,1,5);
a;
```

**Output:**

```
[0, 1, 2, 4, 12]
```


## Mathematica /Wolfram Language

```mw
QuickSort[x_List] := Module[{pivot},
  If[Length@x <= 1, Return[x]];
  pivot = RandomChoice@x;
  Flatten@{QuickSort[Cases[x, j_ /; j < pivot]], Cases[x, j_ /; j == pivot], QuickSort[Cases[x, j_ /; j > pivot]]}
  ]
```

```mw
qsort[{}] = {};
qsort[{x_, xs___}] := Join[qsort@Select[{xs}, # <= x &], {x}, qsort@Select[{xs}, # > x &]];
```

```mw
QuickSort[{}] := {}
QuickSort[list: {__}] := With[{pivot=RandomChoice[list]},
   Join[ <|1->{}, -1->{}|>, GroupBy[list,Order[#,pivot]&] ] // Catenate[ {QuickSort@#[1], #[0], QuickSort@#[-1]} ]&
]
```


## MATLAB

This implements the pseudo-code in the specification. The input can be either a row or column vector, but the returned vector will always be a row vector. This can be modified to operate on any built-in primitive or user defined class by replacing the "<=" and ">" comparisons with "le" and "gt" functions respectively. This is because operators can not be overloaded, but the functions that are equivalent to the operators can be overloaded in class definitions.

This should be placed in a file named *quickSort.m*.

```mw
function sortedArray = quickSort(array)

    if numel(array) <= 1 %If the array has 1 element then it can't be sorted       
        sortedArray = array;
        return
    end
    
    pivot = array(end);
    array(end) = [];
        
    %Create two new arrays which contain the elements that are less than or
    %equal to the pivot called "less" and greater than the pivot called
    %"greater"
    less = array( array <= pivot );
    greater = array( array > pivot );
    
    %The sorted array is the concatenation of the sorted "less" array, the
    %pivot and the sorted "greater" array in that order
    sortedArray = [quickSort(less) pivot quickSort(greater)];
    
end
```

A slightly more vectorized version of the above code that removes the need for the *less* and *greater* arrays:

```mw
function sortedArray = quickSort(array)

    if numel(array) <= 1 %If the array has 1 element then it can't be sorted       
        sortedArray = array;
        return
    end
    
    pivot = array(end);
    array(end) = [];
    
    sortedArray = [quickSort( array(array <= pivot) ) pivot quickSort( array(array > pivot) )];
    
end
```

Sample usage:

```mw
quickSort([4,3,7,-2,9,1])

ans =

    -2     1     3     4     7     9
```


## MAXScript

```mw
fn quickSort arr =
(
    less = #()
    pivotList = #()
    more = #()
    if arr.count <= 1 then
    (
        arr
    )
    else
    (
        pivot = arr[arr.count/2]
        for i in arr do
        (
            case of
            (
                (i < pivot):  (append less i)
                (i == pivot): (append pivotList i)
                (i > pivot):  (append more i)
            )
        )
        less = quickSort less
        more = quickSort more
        less + pivotList + more
    )
)
a = #(4, 89, -3, 42, 5, 0, 2, 889)
a = quickSort a
```


## Mercury

### A quicksort that works on linked lists

Works with

:

Mercury

version 22.01.1

```mw
%%%-------------------------------------------------------------------

:- module quicksort_task_for_lists.

:- interface.
:- import_module io.
:- pred main(io, io).
:- mode main(di, uo) is det.

:- implementation.
:- import_module int.
:- import_module list.

%%%-------------------------------------------------------------------
%%%
%%% Partitioning a list into three:
%%%
%%%    Left         elements less than the pivot
%%%    Middle       elements equal to the pivot
%%%    Right        elements greater than the pivot
%%%
%%% The implementation is tail-recursive.
%%%

:- pred partition(comparison_func(T), T, list(T),
                  list(T), list(T), list(T)).
:- mode partition(in, in, in, out, out, out) is det.
partition(Compare, Pivot, Lst, Left, Middle, Right) :-
  partition(Compare, Pivot, Lst, [], Left, [], Middle, [], Right).

:- pred partition(comparison_func(T), T, list(T),
                  list(T), list(T),
                  list(T), list(T),
                  list(T), list(T)).
:- mode partition(in, in, in,
                  in, out,
                  in, out,
                  in, out) is det.
partition(_, _, [], Left0, Left, Middle0, Middle, Right0, Right) :-
  Left = Left0,
  Middle = Middle0,
  Right = Right0.
partition(Compare, Pivot, [Head | Tail], Left0, Left,
          Middle0, Middle, Right0, Right) :-
  Compare(Head, Pivot) = Cmp,
  (if (Cmp = (<))
   then partition(Compare, Pivot, Tail,
                  [Head | Left0], Left,
                  Middle0, Middle,
                  Right0, Right)
   else if (Cmp = (=))
   then partition(Compare, Pivot, Tail,
                  Left0, Left,
                  [Head | Middle0], Middle,
                  Right0, Right)
   else partition(Compare, Pivot, Tail,
                  Left0, Left,
                  Middle0, Middle,
                  [Head | Right0], Right)).

%%%-------------------------------------------------------------------
%%%
%%% Quicksort using the first element as pivot.
%%%
%%% This is not the world's best choice of pivot, but it is the
%%% easiest one to get from a linked list.
%%%
%%% This implementation is *not* tail-recursive--as most quicksort
%%% implementations also are not. (However, do an online search on
%%% "quicksort fortran 77" and you will find some "tail-recursive"
%%% implementations, with the tail recursions expressed as gotos.)
%%%

:- func quicksort(comparison_func(T), list(T)) = list(T).
quicksort(_, []) = [].
quicksort(Compare, [Pivot | Tail]) = Sorted_Lst :-
  partition(Compare, Pivot, Tail, Left, Middle, Right),
  quicksort(Compare, Left) = Sorted_Left,
  quicksort(Compare, Right) = Sorted_Right,
  Sorted_Left ++ [Pivot | Middle] ++ Sorted_Right = Sorted_Lst.

%%%-------------------------------------------------------------------

:- func example_numbers = list(int).
example_numbers = [1, 3, 9, 5, 8, 6, 5, 1, 7, 9, 8, 6, 4, 2].

:- func int_compare(int, int) = comparison_result.
int_compare(I, J) = Cmp :-
  if (I < J) then (Cmp = (<))
  else if (I = J) then (Cmp = (=))
  else (Cmp = (>)).

main(!IO) :-
  quicksort(int_compare, example_numbers) = Sorted_Numbers,
  print("unsorted: ", !IO),
  print_line(example_numbers, !IO),
  print("sorted:   ", !IO),
  print_line(Sorted_Numbers, !IO).

%%%-------------------------------------------------------------------
%%% local variables:
%%% mode: mercury
%%% prolog-indent-width: 2
%%% end:
```

**Output:**

```
$ mmc quicksort_task_for_lists.m && ./quicksort_task_for_lists
unsorted: [1, 3, 9, 5, 8, 6, 5, 1, 7, 9, 8, 6, 4, 2]
sorted:   [1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
```

### A quicksort that works on arrays

Works with

:

Mercury

version 22.01.1

The in-place partitioning algorithm here is similar to but not quite the same as that of the task pseudocode. I wrote it by referring to some Fortran code I wrote several months ago for a quickselect. (That quickselect had a random pivot, however.)

```mw
%%%-------------------------------------------------------------------

:- module quicksort_task_for_arrays.

:- interface.
:- import_module io.
:- pred main(io, io).
:- mode main(di, uo) is det.

:- implementation.
:- import_module array.
:- import_module int.
:- import_module list.

%%%-------------------------------------------------------------------
%%%
%%% Partitioning a subarray into two halves: one with elements less
%%% than or equal to a pivot, the other with elements greater than or
%%% equal to a pivot.
%%%
%%% The implementation is tail-recursive.
%%%

:- pred partition(pred(T, T), T, int, int, array(T), array(T), int).
:- mode partition(pred(in, in) is semidet, in, in, in,
                  array_di, array_uo, out).
partition(Less_than, Pivot, I_first, I_last, Arr0, Arr, I_pivot) :-
  I = I_first - 1,
  J = I_last + 1,
  partition_loop(Less_than, Pivot, I, J, Arr0, Arr, I_pivot).

:- pred partition_loop(pred(T, T), T, int, int,
                       array(T), array(T), int).
:- mode partition_loop(pred(in, in) is semidet, in, in, in,
                       array_di, array_uo, out).
partition_loop(Less_than, Pivot, I, J, Arr0, Arr, Pivot_index) :-
  if (I = J) then (Arr = Arr0,
                   Pivot_index = I)
  else (I1 = I + 1,
        I2 = search_right(Less_than, Pivot, I1, J, Arr0),
        (if (I2 = J) then (Arr = Arr0,
                           Pivot_index = J)
         else (J1 = J - 1,
               J2 = search_left(Less_than, Pivot, I2, J1, Arr0),
               swap(I2, J2, Arr0, Arr1),
               partition_loop(Less_than, Pivot, I2, J2, Arr1, Arr,
                              Pivot_index)))).

:- func search_right(pred(T, T), T, int, int, array(T)) = int.
:- mode search_right(pred(in, in) is semidet,
                     in, in, in, in) = out is det.
search_right(Less_than, Pivot, I, J, Arr0) = K :-
  if (I = J) then (I = K)
  else if Less_than(Pivot, Arr0^elem(I)) then (I = K)
  else (search_right(Less_than, Pivot, I + 1, J, Arr0) = K).

:- func search_left(pred(T, T), T, int, int, array(T)) = int.
:- mode search_left(pred(in, in) is semidet,
                    in, in, in, in) = out is det.
search_left(Less_than, Pivot, I, J, Arr0) = K :-
  if (I = J) then (J = K)
  else if Less_than(Arr0^elem(J), Pivot) then (J = K)
  else (search_left(Less_than, Pivot, I, J - 1, Arr0) = K).

%%%-------------------------------------------------------------------
%%%
%%% Quicksort with median of three as pivot.
%%%
%%% Like most quicksort implementations, this one is *not*
%%% tail-recursive.
%%%

%% quicksort/3 sorts an entire array.
:- pred quicksort(pred(T, T), array(T), array(T)).
:- mode quicksort(pred(in, in) is semidet, array_di, array_uo) is det.
quicksort(Less_than, Arr0, Arr) :-
  bounds(Arr0, I_first, I_last),
  quicksort(Less_than, I_first, I_last, Arr0, Arr).

%% quicksort/5 sorts a subarray.
:- pred quicksort(pred(T, T), int, int, array(T), array(T)).
:- mode quicksort(pred(in, in) is semidet, in, in,
                  array_di, array_uo) is det.
quicksort(Less_than, I_first, I_last, Arr0, Arr) :-
  if (I_last - I_first >= 2)
  then (median_of_three(Less_than, I_first, I_last,
                        Arr0, Arr1, Pivot),

        %% Partition only from I_first to I_last - 1.
        partition(Less_than, Pivot, I_first, I_last - 1,
                  Arr1, Arr2, K),

        %% Now everything that is less than the pivot is to the
        %% left of K.

        %% Put the pivot at K, moving the element that had been there
        %% to the end. If K = I_last, then this element is actually
        %% garbage and will be overwritten with the pivot, which turns
        %% out to be the greatest element. Otherwise, the moved
        %% element is not less than the pivot and so the partitioning
        %% is preserved.
        Arr2^elem(K) = Elem_to_move,
        (Arr2^elem(I_last) := Elem_to_move) = Arr3,
        (Arr3^elem(K) := Pivot) = Arr4,

        %% Sort the subarray on either side of the pivot.
        quicksort(Less_than, I_first, K - 1, Arr4, Arr5),
        quicksort(Less_than, K + 1, I_last, Arr5, Arr))

  else if (I_last - I_first = 1) % Two elements.
  then (Elem_first = Arr0^elem(I_first),
        Elem_last = Arr0^elem(I_last),
        (if Less_than(Elem_first, Elem_last)
         then (Arr = Arr0)
         else ((Arr0^elem(I_first) := Elem_last) = Arr1,
               (Arr1^elem(I_last) := Elem_first) = Arr)))

  else (Arr = Arr0).            % Zero or one element.

%% median_of_three/6 both chooses a pivot and rearranges the array
%% elements so one may partition them from I_first to I_last - 1,
%% leaving the pivot element out of the array.
:- pred median_of_three(pred(T, T), int, int, array(T), array(T), T).
:- mode median_of_three(pred(in, in) is semidet, in, in,
                        array_di, array_uo, out) is det.
median_of_three(Less_than, I_first, I_last, Arr0, Arr, Pivot) :-
  I_middle = I_first + ((I_last - I_first) // 2),
  Elem_first = Arr0^elem(I_first),
  Elem_middle = Arr0^elem(I_middle),
  Elem_last = Arr0^elem(I_last),
  (if pred_xor(Less_than, Less_than,
               Elem_middle, Elem_first,
               Elem_last, Elem_first)
   then (Pivot = Elem_first,
         (if Less_than(Elem_middle, Elem_last)
          then (Arr1 = (Arr0^elem(I_first) := Elem_middle),
                Arr = (Arr1^elem(I_middle) := Elem_last))
          else (Arr = (Arr0^elem(I_first) := Elem_last))))
   else if pred_xor(Less_than, Less_than,
                    Elem_middle, Elem_first,
                    Elem_middle, Elem_last)
   then (Pivot = Elem_middle,
         (if Less_than(Elem_first, Elem_last)
          then (Arr = (Arr0^elem(I_middle) := Elem_last))
          else (Arr1 = (Arr0^elem(I_first) := Elem_last),
                Arr = (Arr1^elem(I_middle) := Elem_first))))
   else (Pivot = Elem_last,
         (if Less_than(Elem_first, Elem_middle)
          then (Arr = Arr0)
          else (Arr1 = (Arr0^elem(I_first) := Elem_middle),
                Arr = (Arr1^elem(I_middle) := Elem_first))))).

:- pred pred_xor(pred(T, T), pred(T, T), T, T, T, T).
:- mode pred_xor(pred(in, in) is semidet,
                 pred(in, in) is semidet,
                 in, in, in, in) is semidet.
pred_xor(P, Q, W, X, Y, Z) :-
  if P(W, X) then (not Q(Y, Z)) else Q(Y, Z).

%%%-------------------------------------------------------------------

:- func example_numbers = list(int).
example_numbers = [1, 3, 9, 5, 8, 6, 5, 0, 1, 7, 9, 8, 6, 4, 2, -28,
                   30, 31, 1, 3, 9, 5, 8, 6, 5, 1, 6, 4, 2, -28, 30,
                   -50, 500, -1234, 1234, 12].

main(!IO) :-
  (array.from_list(example_numbers, Arr0)),
  print_line("", !IO),
  print_line(Arr0, !IO),
  print_line("", !IO),
  print_line("                                               |", !IO),
  print_line("                                               V", !IO),
  print_line("", !IO),
  quicksort(<, Arr0, Arr1),
  print_line(Arr1, !IO),
  print_line("", !IO).

%%%-------------------------------------------------------------------
%%% local variables:
%%% mode: mercury
%%% prolog-indent-width: 2
%%% end:
```

**Output:**

```
$ mmc quicksort_task_for_arrays.m && ./quicksort_task_for_arrays

array([1, 3, 9, 5, 8, 6, 5, 0, 1, 7, 9, 8, 6, 4, 2, -28, 30, 31, 1, 3, 9, 5, 8, 6, 5, 1, 6, 4, 2, -28, 30, -50, 500, -1234, 1234, 12])

                                               |
                                               V

array([-1234, -50, -28, -28, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9, 12, 30, 30, 31, 500, 1234])
```


## MiniScript

Quick implementation for Miniscript, simply goes through the list reference and swaps the positions

```mw
Partition = function(a, low, high)
    pivot = a[low]
    leftwall = low

    for i in range(low + 1, high)
        if a[i] < pivot then
            leftwall = leftwall + 1
            temp = a[leftwall]
            a[leftwall] = a[i]
            a[i] = temp
        end if
    end for

    temp = a[leftwall]
    a[leftwall] = pivot
    a[low] = temp

    return leftwall
end function

QuickSort = function(a, low=null, high=null)
   if not low then low = 0
   if not high then high = a.len - 1
    if low < high then
        pivot_location = Partition(a, low, high)
        QuickSort a, low, pivot_location - 1
        QuickSort a, pivot_location + 1, high
    end if

    return a
end function

print QuickSort([3, 5, 2, 4, 1])
```

**Output:**

```
[1, 2, 3, 4, 5]
```


## Miranda

```mw
main :: [sys_message]
main = [Stdout ("Before: " ++ show testlist ++ "\n"),
        Stdout ("After:  " ++ show (quicksort testlist) ++ "\n")]
       where testlist = [4,65,2,-31,0,99,2,83,782,1]

quicksort []  = []
quicksort [x] = [x]
quicksort xs  = (quicksort less) ++ equal ++ (quicksort more)
                where pivot = hd xs
                      less  = [x | x<-xs; x<pivot]
                      equal = [x | x<-xs; x=pivot]
                      more  = [x | x<-xs; x>pivot]
```

**Output:**

```
Before: [4,65,2,-31,0,99,2,83,782,1]
After:  [-31,0,1,2,2,4,65,83,99,782]
```


## Modula-2

The definition module exposes the interface. This one uses the procedure variable feature to pass a caller defined compare callback function so that it can sort various simple and structured record types.

This Quicksort assumes that you are working with an an array of pointers to an arbitrary type and are not moving the record data itself but only the pointers. The M2 type "ADDRESS" is considered compatible with any pointer type.

The use of type ADDRESS here to achieve genericity is something of a chink the the normal strongly typed flavor of Modula-2. Unlike the other language types, "system" types such as ADDRESS or WORD must be imported explicity from the SYSTEM MODULE. The ISO standard for the "Generic Modula-2" language extension provides genericity without the chink, but most compilers have not implemented this extension.

```mw
(*#####################*)
 DEFINITION MODULE QSORT; 
(*#####################*)      

FROM SYSTEM IMPORT ADDRESS;

TYPE CmpFuncPtrs = PROCEDURE(ADDRESS, ADDRESS):INTEGER;

 PROCEDURE QuickSortPtrs(VAR Array:ARRAY OF ADDRESS; N:CARDINAL;
                         Compare:CmpFuncPtrs);
END QSORT.
```

The implementation module is not visible to clients, so it may be changed without worry so long as it still implements the definition.

Sedgewick suggests that faster sorting will be achieved if you drop back to an insertion sort once the partitions get small.

```mw
(*##########################*)
 IMPLEMENTATION MODULE QSORT; 
(*##########################*)

FROM SYSTEM    IMPORT ADDRESS;

CONST SmallPartition  = 9;

(*
NOTE
        1.Reference on QuickSort: "Implementing Quicksort Programs", Robert
          Sedgewick, Communications of the ACM, Oct 78, v21 #10.
*)

(*==============================================================*)
 PROCEDURE QuickSortPtrs(VAR Array:ARRAY OF ADDRESS; N:CARDINAL;
                         Compare:CmpFuncPtrs);
(*==============================================================*)

         (*-----------------------------*)
          PROCEDURE Swap(VAR A,B:ADDRESS);
         (*-----------------------------*)

         VAR  temp :ADDRESS;

         BEGIN

         temp := A; A := B; B := temp;

         END Swap;

         (*-------------------------------*)
          PROCEDURE TstSwap(VAR A,B:ADDRESS);
         (*-------------------------------*)

         VAR  temp   :ADDRESS;

         BEGIN

         IF Compare(A,B) > 0 THEN
            temp := A; A := B; B := temp;
         END;

         END TstSwap;

         (*--------------*)
          PROCEDURE Isort;
         (*--------------*)
         (*
                 Insertion sort.
         *)

         VAR  i,j    :CARDINAL;
              temp   :ADDRESS;

         BEGIN

         IF N < 2 THEN RETURN END;

         FOR i := N-2 TO 0 BY -1 DO
            IF Compare(Array[i],Array[i+1]) > 0 THEN
               temp := Array[i];
               j := i+1;
               REPEAT
                  Array[j-1] := Array[j];
                  INC(j);
               UNTIL (j = N) OR (Compare(Array[j],temp) >= 0);
               Array[j-1] := temp;
            END;
         END;

         END Isort;

         (*----------------------------------*)
          PROCEDURE Quick(left,right:CARDINAL);
         (*----------------------------------*)

         VAR
              i,j,
              second     :CARDINAL;
              Partition  :ADDRESS;

         BEGIN

         IF right > left THEN
            i := left; j := right;

            Swap(Array[left],Array[(left+right) DIV 2]);

            second := left+1;                          (* insure 2nd element is in   *)
            TstSwap(Array[second], Array[right]);      (* the lower part, last elem  *)
            TstSwap(Array[left], Array[right]);        (* in the upper part          *)
            TstSwap(Array[second], Array[left]);       (* THUS, only one test is     *)
                                                       (* needed in repeat loops     *)
            Partition := Array[left];

            LOOP
               REPEAT INC(i) UNTIL Compare(Array[i],Partition) >= 0;
               REPEAT DEC(j) UNTIL Compare(Array[j],Partition) <= 0;
               IF j < i THEN
                  EXIT
               END;
               Swap(Array[i],Array[j]);
            END; (*loop*)
            Swap(Array[left],Array[j]);

            IF (j > 0) AND (j-1-left >= SmallPartition) THEN
               Quick(left,j-1);
            END;
            IF right-i >= SmallPartition THEN
               Quick(i,right);
            END;
         END;

         END Quick;

 BEGIN (* QuickSortPtrs --------------------------------------------------*)

IF N > SmallPartition THEN              (* won't work for 2 elements *)
   Quick(0,N-1);
END;

Isort;

END QuickSortPtrs;

END QSORT.
```
