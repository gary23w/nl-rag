---
title: "Sorting algorithms/Quicksort (part 8/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 8/8
---

## Ursala

The distributing bipartition operator, *|, is useful for this algorithm. The pivot is chosen as the greater of the first two items, this being the least sophisticated method sufficient to ensure termination. The quicksort function is a higher order function parameterized by the relational predicate p, which can be chosen appropriately for the type of items in the list being sorted. This example demonstrates sorting a list of natural numbers.

```mw
#import nat

quicksort "p" = ~&itB^?a\~&a ^|WrlT/~& "p"*|^\~& "p"?hthPX/~&th ~&h

#cast %nL

example = quicksort(nleq) <694,1377,367,506,3712,381,1704,1580,475,1872>
```

**Output:**

```
<367,381,475,506,694,1377,1580,1704,1872,3712>
```


## V

```mw
[qsort
  [joinparts [p [*l1] [*l2] : [*l1 p *l2]] view].
  [split_on_first uncons [>] split].
  [small?]
    []
    [split_on_first [l1 l2 : [l1 qsort l2 qsort joinparts]] view i]
  ifte].
```

The way of joy (using binrec)

```mw
[qsort
   [small?] []
     [uncons [>] split]
     [[p [*l] [*g] : [*l p *g]] view]
    binrec].
```


## V (Vlang)

```mw
fn partition(mut arr []int, low int, high int) int {
   pivot := arr[high]
   mut i := (low - 1)
   for j in low .. high {
      if arr[j] < pivot {
         i++
         temp := arr[i]
         arr[i] = arr[j]
         arr[j] = temp
      }
   }
   temp := arr[i + 1]
   arr[i + 1] = arr[high]
   arr[high] = temp
   return i + 1
}

fn quick_sort(mut arr []int, low int, high int) {
   if low < high {
      pi := partition(mut arr, low, high)
      quick_sort(mut arr, low, pi - 1)
      quick_sort(mut arr, pi + 1, high)
   }
}

fn main() {
   mut arr := [4, 65, 2, -31, 0, 99, 2, 83, 782, 1]
   n := arr.len - 1
   println('Input: ' + arr.str())
   quick_sort(mut arr, 0, n)
   println('Output: ' + arr.str())
}
```

**Output:**

```
Input: [4, 65, 2, -31, 0, 99, 2, 83, 782, 1]
Output: [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782]
```


## Wart

```mw
def (qsort (pivot ... ns))
  (+ (qsort+keep (fn(_) (_ < pivot)) ns)
     list.pivot
     (qsort+keep (fn(_) (_ > pivot)) ns))

def (qsort x) :case x=nil
  nil
```


## Wren

Library:

Wren-sort

```mw
import "./sort" for Sort

var array = [
    [4, 65, 2, -31, 0, 99, 2, 83, 782, 1],
    [7, 5, 2, 6, 1, 4, 2, 6, 3],
    ["echo", "lima", "charlie", "whiskey", "golf", "papa", "alfa", "india", "foxtrot", "kilo"]
]
for (a in array) {
    System.print("Before: %(a)")
    Sort.quick(a)
    System.print("After : %(a)")
    System.print()
}
```

**Output:**

```
Before: [4, 65, 2, -31, 0, 99, 2, 83, 782, 1]
After : [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782]

Before: [7, 5, 2, 6, 1, 4, 2, 6, 3]
After : [1, 2, 2, 3, 4, 5, 6, 6, 7]

Before: [echo, lima, charlie, whiskey, golf, papa, alfa, india, foxtrot, kilo]
After : [alfa, charlie, echo, foxtrot, golf, india, kilo, lima, papa, whiskey]
```


## XPL0

```mw
include c:\cxpl\codes;          \intrinsic 'code' declarations
string 0;                       \use zero-terminated strings

proc    QSort(Array, Num);      \Quicksort Array into ascending order
char    Array;                  \address of array to sort
int     Num;                    \number of elements in the array
int     I, J, Mid, Temp;
[I:= 0;
J:= Num-1;
Mid:= Array(J>>1);
while I <= J do
       [while Array(I) < Mid do I:= I+1;
        while Array(J) > Mid do J:= J-1;
        if I <= J then
                [Temp:= Array(I);  Array(I):= Array(J);  Array(J):= Temp;
                I:= I+1;
                J:= J-1;
                ];
        ];
if I < Num-1 then QSort(@Array(I), Num-I);
if J > 0 then QSort(Array, J+1);
];      \QSort

func    StrLen(Str);            \Return number of characters in an ASCIIZ string
char    Str;
int     I;
for I:= 0 to -1>>1-1 do
        if Str(I) = 0 then return I;

char    Str;
[Str:= "Pack my box with five dozen liquor jugs.";
QSort(Str, StrLen(Str), 1);
Text(0, Str);  CrLf(0);
]
```

**Output:**

```
       .Pabcdeefghiiijklmnoooqrstuuvwxyz
```


## YAMLScript

```mw
!ys-0

defn main(nums='3 1 4 1 5 9 2 6 5 3 5'):
  nums .=: words().map(N)
  say: nums:quicksort

defn quicksort(xs):
  if xs:empty?:
    then: xs
    else:
      p =: xs:first
      rest =: xs:rest
      less =: rest.filter(lt(p))
      more =: rest.filter(ge(p))
      concat:
        quicksort(less)
        [p]
        quicksort(more)
```

**Output:**

```
$ ys sorting-algorithms-quicksort.ys
(1 1 2 3 3 4 5 5 5 6 9)
```


## Z80 Assembly

sjasmplus syntax

```mw
;--------------------------------------------------------------------------------------------------------------------
; Quicksort, inputs (__sdcccall(1) calling convention):
; HL = uint16_t* A (pointer to beginning of array)
; DE = uint16_t len (number of word elements in array)
; modifies: AF, A'F', BC, DE, HL
; WARNING: array can't be aligned to start/end of 64ki address space, like HL == 0x0000, or having last value at 0xFFFE
; WARNING: stack space required is on average about 6*log(len) (depending on the data, in extreme case it may be more)
quicksort_a:
    ; convert arguments to HL=A.begin(), DE=A.end() and continue with quicksort_a_impl
    ex      de,hl
    add     hl,hl
    add     hl,de
    ex      de,hl
    ;  |
    ; fallthrough into implementation
    ;  |
    ;  v
;--------------------------------------------------------------------------------------------------------------------
; Quicksort implementation, inputs:
; HL = uint16_t* A.begin() (pointer to beginning of array)
; DE = uint16_t* A.end() (pointer beyond array)
; modifies: AF, A'F', BC, HL (DE is preserved)
quicksort_a_impl:
    ; array must be located within 0x0002..0xFFFD
    ld      c,l
    ld      b,h         ; BC = A.begin()
    ; if (len < 2) return; -> if (end <= begin+2) return;
    inc     hl
    inc     hl
    or      a
    sbc     hl,de       ; HL = -(2*len-2), len = (2-HL)/2
    ret     nc          ; case: begin+2 >= end <=> (len < 2)

    push    de          ; preserve A.end() for recursion
    push    bc          ; preserve A.begin() for recursion

    ; uint16_t pivot = A[len / 2];
    rr      h
    rr      l
    dec     hl
    res     0,l
    add     hl,de
    ld      a,(hl)
    inc     hl
    ld      l,(hl)
    ld      h,b
    ld      b,l
    ld      l,c
    ld      c,a         ; HL = A.begin(), DE = A.end(), BC = pivot

    ; flip HL/DE meaning, it makes simpler the recursive tail and (A[j] > pivot) test
    ex      de,hl       ; DE = A.begin(), HL = A.end(), BC = pivot
    dec     de          ; but keep "from" address (related to A[i]) at -1 as "default" state

    ; for (i = 0, j = len - 1; ; i++, j--) { ; DE = (A+i-1).hi, HL = A+j+1
.find_next_swap:

    ; while (A[j] > pivot) j--;
.find_j:
    dec     hl
    ld      a,b
    sub     (hl)
    dec     hl          ; HL = A+j (finally)
    jr      c,.find_j   ; if cf=1, A[j].hi > pivot.hi
    jr      nz,.j_found ; if zf=0, A[j].hi < pivot.hi
    ld      a,c         ; if (A[j].hi == pivot.hi) then A[j].lo vs pivot.lo is checked
    sub     (hl)
    jr      c,.find_j
.j_found:

    ; while (A[i] < pivot) i++;
.find_i:
    inc     de
    ld      a,(de)
    inc     de          ; DE = (A+i).hi (ahead +0.5 for swap)
    sub     c
    ld      a,(de)
    sbc     a,b
    jr      c,.find_i   ; cf=1 -> A[i] < pivot

    ; if (i >= j) break; // DE = (A+i).hi, HL = A+j, BC=pivot
    sbc     hl,de       ; cf=0 since `jr c,.find_i`
    jr      c,.swaps_done
    add     hl,de       ; DE = (A+i).hi, HL = A+j

    ; swap(A[i], A[j]);
    inc     hl
    ld      a,(de)
    ldd
    ex      af,af
    ld      a,(de)
    ldi
    ex      af,af
    ld      (hl),a      ; Swap(A[i].hi, A[j].hi) done
    dec     hl
    ex      af,af
    ld      (hl),a      ; Swap(A[i].lo, A[j].lo) done

    inc     bc
    inc     bc          ; pivot value restored (was -=2 by ldd+ldi)
    ; --j; HL = A+j is A+j+1 for next loop (ready)
    ; ++i; DE = (A+i).hi is (A+i-1).hi for next loop (ready)
    jp      .find_next_swap

.swaps_done:
    ; i >= j, all elements were already swapped WRT pivot, call recursively for the two sub-parts
    dec     de          ; DE = A+i

    ; quicksort_c(A, i);
    pop     hl          ; HL = A
    call    quicksort_a_impl

    ; quicksort_c(A + i, len - i);
    ex      de,hl       ; HL = A+i
    pop     de          ; DE = end() (and return it preserved)
    jp      quicksort_a_impl
```

Full example with test/debug data for ZX Spectrum is at [github].


## Zig

Translation of

:

Rust

**Works with:** 0.10.x, 0.11.x, 0.12.0-dev.1390+94cee4fb2

```mw
const std = @import("std");

pub fn quickSort(comptime T: type, arr: []T, comptime compareFn: fn (T, T) bool) void {
    if (arr.len < 2) return;

    const pivot_index = partition(T, arr, compareFn);
    quickSort(T, arr[0..pivot_index], compareFn);
    quickSort(T, arr[pivot_index + 1 .. arr.len], compareFn);
}

fn partition(comptime T: type, arr: []T, comptime compareFn: fn (T, T) bool) usize {
    const pivot_index = arr.len / 2;
    const last_index = arr.len - 1;

    std.mem.swap(T, &arr[pivot_index], &arr[last_index]);

    var store_index: usize = 0;
    for (arr[0 .. arr.len - 1]) |*elem_ptr| {
        if (compareFn(elem_ptr.*, arr[last_index])) {
            std.mem.swap(T, elem_ptr, &arr[store_index]);
            store_index += 1;
        }
    }

    std.mem.swap(T, &arr[store_index], &arr[last_index]);
    return store_index;
}
```

```mw
const std = @import("std");

pub fn main() void {
    const print = std.debug.print;

    var arr = [_]i16{ 4, 65, 2, -31, 0, 99, 2, 83, 782, 1 };
    print("Before: {any}\n\n", .{arr});

    print("Sort numbers in ascending order.\n", .{});
    quickSort(i16, &arr, struct {
        fn sortFn(left: i16, right: i16) bool {
            return left < right;
        }
    }.sortFn);
    print("After: {any}\n\n", .{arr});

    print("Sort numbers in descending order.\n", .{});
    quickSort(i16, &arr, struct {
        fn sortFn(left: i16, right: i16) bool {
            return left > right;
        }
    }.sortFn);
    print("After: {any}\n\n", .{arr});
}
```

**Output:**

```
Before: { 4, 65, 2, -31, 0, 99, 2, 83, 782, 1 }

Sort numbers in ascending order.
After: { -31, 0, 1, 2, 2, 4, 65, 83, 99, 782 }

Sort numbers in descending order.
After: { 782, 99, 83, 65, 4, 2, 2, 1, 0, -31 }
```


## zkl

These are the Wikipedia algorithms.

Quick sort immutable sequence using crappy pivot choice:

```mw
fcn qtSort(list,cmp=Op("<")){   // sort immutable lists
   fcn(list,cmp,N){  // spendy to keep recreating cmp
      reg pivot=list[0], rest=list[1,*];
      left,right:=rest.filter22(cmp,pivot);
      N+=1;
      T.extend(self.fcn(left,cmp,N),T(pivot),self.fcn(right,cmp,N));
   }(list,cmp,0);
}
```

In place quick sort:

```mw
fcn qiSort(list,cmp='<){     // in place quick sort
   fcn(list,left,right,cmp){
      if (left<right){
    // partition list
    pivotIndex:=(left+right)/2; // or median of first,middle,last
    pivot:=list[pivotIndex];
    list.swap(pivotIndex,right); // move pivot to end
    pivotIndex:=left;
    i:=left; do(right-left){  // foreach i in ([left..right-1])
       if(cmp(list[i],pivot)){   // not cheap
          list.swap(i,pivotIndex);
          pivotIndex+=1;
       }
       i+=1;
    }
    list.swap(pivotIndex,right); // move pivot to final place

    // sort the partitions
         self.fcn(list,left,pivotIndex-1,cmp);
    return(self.fcn(list,pivotIndex+1,right,cmp));
      }
   }(list,0,list.len()-1,cmp);
   list;
}
```

Retrieved from "

https://rosettacode.org/wiki/Sorting_algorithms/Quicksort?oldid=404708

"
