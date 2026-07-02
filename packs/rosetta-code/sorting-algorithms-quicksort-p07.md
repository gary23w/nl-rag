---
title: "Sorting algorithms/Quicksort (part 7/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 7/8
---

## REXX

### version 1 quickSort

Translation of

:

Python

The Python code translates very well to ooRexx but here is a way to implement it in classic REXX as well.

This REXX version doesn't handle numbers with leading/trailing/embedded blanks, or textual values that have blanks (or whitespace) in them.

```mw
 
/*REXX*/
    a = '4 65 2 -31 0 99 83 782 1'
    do i = 1 to words(a)
        queue word(a, i)
    end
    call quickSort
    parse pull item
    do queued()
        call charout ,item', '
        parse pull item
    end
    say item
    exit

quickSort: procedure
/* In classic Rexx, arguments are passed by value, not by reference so stems
    cannot be passed as arguments nor used as return values.  Putting their
    contents on the external data queue is a way to bypass this issue. */

    /* construct the input stem */
    arr.0 = queued()
    do i = 1 to arr.0
        parse pull arr.i
    end
    less.0 = 0
    pivotList.0 = 0
    more.0 = 0
    if arr.0 <= 1 then do
        if arr.0 = 1 then
            queue arr.1
        return
    end
    else do
        pivot = arr.1
        do i = 1 to arr.0
            item = arr.i
            select
                when item < pivot then do
                    j = less.0 + 1
                    less.j = item
                    less.0 = j
                end
                when item > pivot then do
                    j = more.0 + 1
                    more.j = item
                    more.0 = j
                end
                otherwise
                    j = pivotList.0 + 1
                    pivotList.j = item
                    pivotList.0 = j
            end
        end
    end
    /* recursive call to sort the less. stem */
    do i = 1 to less.0
        queue less.i
    end
    if queued() > 0 then do
        call quickSort
        less.0 = queued()
        do i = 1 to less.0
            parse pull less.i
        end
    end
    /* recursive call to sort the more. stem */
    do i = 1 to more.0
        queue more.i
    end
    if queued() > 0 then do
        call quickSort
        more.0 = queued()
        do i = 1 to more.0
            parse pull more.i
        end
    end
    /* put the contents of all 3 stems on the queue in order */
    do i = 1 to less.0
        queue less.i
    end
    do i = 1 to pivotList.0
        queue pivotList.i
    end
    do i = 1 to more.0
        queue more.i
    end
    return
```

### Version 2 Elegant

A basic quicksort using the stack, but only for the pending partitions. Short and elegant.

```mw
Elegant:
procedure expose stem.
push 1 stem.0
do while queued() > 0
   pull l r
   if l < r then do
      m = (l+r)%2; p = stem.m; i = l-1; j = r+1
      do forever
         do until stem.j <= p
            j = j-1
         end
         do until stem.i >= p
            i = i+1
         end
         if i < j then do
            t = stem.i; stem.i = stem.j; stem.j = t
         end
         else
            leave
      end
      push l j; push j+1 r
   end
end
return
```

### Version 3 Recursive

Also a basic quicksort, but now using recursion as stated in the task. No stack usage.

```mw
Recursive:
procedure expose stem.
arg l r
m = (l+r)%2; p = stem.m
i = l; j = r
do while i <= j
   do i = i while stem.i < p
   end
   do j = j by -1 while stem.j > p
   end
   if i <= j then do
      t = stem.i; stem.i = stem.j; stem.j = t
      i = i+1; j = j-1
   end
end
if l < j then
   call Recursive l j
if i < r then
   call Recursive i r
return
```

### Version 6 Optimized

The fastest. As in Version 1, no recursion and no stack usage. The pending partitions are kept in small stems. For partitions < 11 items, a selection sort is employed. Pivot choice is optimized to prevent 'worst case' scenarios.

```mw
Optimized:
procedure expose stem.
n = stem.0; s = 1; sl.1 = 1; sr.1 = n
do until s = 0
   l = sl.s; r = sr.s; s = s-1
   do until l >= r
      if r-l < 11 then do
         do i = l+1 to r
            a = stem.i
            do j=i-1 by -1 to l while stem.j > a
               k = j+1; stem.k = stem.j
            end
            k = j+1; stem.k = a
         end
         if s = 0 then
            leave
         l = sl.s; r = sr.s; s = s-1
      end
      else do
         m = (l+r)%2
         if stem.l > stem.m then do
            t = stem.l; stem.l = stem.m; stem.m = t
         end
         if stem.l > stem.r then do
            t = stem.l; stem.l = stem.r; stem.r = t
         end
         if stem.m > stem.r then do
            t = stem.m; stem.m = stem.r; stem.r = t
         end
         i = l; j = r; p = stem.m
         do until i > j
            do i = i while stem.i < p
            end
            do j = j by -1 while stem.j > p
            end
            if i <= j then do
               t = stem.i; stem.i = stem.j; stem.j = t
               i = i+1; j = j-1
            end
         end
         if j-l < r-i then do
            if i < r then do
               s = s+1; sl.s = i; sr.s = r
            end
            r = j
         end
         else do
            if l < j then do
               s = s+1; sl.s = l; sr.s = j
            end
            l = i
         end
      end
   end
end
return
```

### Timing all versions

Using following program, with all versions copied in.

```mw
-- 24 Aug 2025
include Setting

say 'QUICKSORT'
say version
say
numeric digits 9
arg n v
if n = '' then n = 10
if v = '' then v = 1
show = (n > 0); n = Abs(n)
say 'Timing Version' v 'for' n 'random numbers'
call Generate
if show then call ShowSave
if v = 0 | v = 1 then do
   call Time 'r'; call Save2Stack; say 'Save2Stack' format(time('e'),3,3) 'seconds'
   call Time 'r'; call Quicksort; say 'Quicksort ' format(time('e'),3,3) 'seconds'
   call Time 'r'; call Stack2Stem; say 'Stack2Stem' format(time('e'),3,3) 'seconds'
   if show then call ShowStem
end
if v = 0 | v = 2 then do
   call Save2Stem
   call Time 'r'; call Elegant; say 'Elegant' format(time('e'),3,3) 'seconds'
   if show then call ShowStem
end
if v = 0 | v = 3 then do
   call Save2Stem
   call Time 'r'; call Recursive 1 n; say 'Recursive' format(time('e'),3,3) 'seconds'
   if show then call ShowStem
end
if v = 0 | v = 4 then do
   call Save2Stem
   call Time 'r'; call Optimized; say 'Optimized' format(time('e'),3,3) 'seconds'
   if show then call ShowStem
end
say
exit

Generate:
do x = 1 to n
   save.x = 10000*Random(0,9999)+Random(0,9999)
end
save.0 = n
return

ShowSave:
do x = 1 to 5
   say x save.x
end
do x = n-4 to n
   say x save.x
end
say
return

ShowStem:
do x = 1 to 5
   say x stem.x
end
do x = n-4 to n
   say x stem.x
end
say
return

Save2Stem:
do x = 0 to n
   stem.x = save.x
end
return

Save2Stack:
do x = 1 to n
   queue save.x
end
return

Quicksort: procedure
arr.0 = queued()
do i = 1 to arr.0
    parse pull arr.i
end
less.0 = 0
pivotList.0 = 0
more.0 = 0
if arr.0 <= 1 then do
    if arr.0 = 1 then
        queue arr.1
    return
end
else do
    pivot = arr.1
    do i = 1 to arr.0
        item = arr.i
        select
            when item < pivot then do
                j = less.0 + 1
                less.j = item
                less.0 = j
            end
            when item > pivot then do
                j = more.0 + 1
                more.j = item
                more.0 = j
            end
            otherwise
                j = pivotList.0 + 1
                pivotList.j = item
                pivotList.0 = j
        end
    end
end
do i = 1 to less.0
    queue less.i
end
if queued() > 0 then do
    call quickSort
    less.0 = queued()
    do i = 1 to less.0
        parse pull less.i
    end
end
do i = 1 to more.0
    queue more.i
end
if queued() > 0 then do
    call quickSort
    more.0 = queued()
    do i = 1 to more.0
        parse pull more.i
    end
end
do i = 1 to less.0
    queue less.i
end
do i = 1 to pivotList.0
    queue pivotList.i
end
do i = 1 to more.0
    queue more.i
end
return

Stack2Stem:
do x = 1 to n
   parse pull stem.x
end
return

Elegant:
procedure expose stem.
push 1 stem.0
do while queued() > 0
   pull l r
   if l < r then do
      m = (l+r)%2; p = stem.m; i = l-1; j = r+1
      do forever
         do until stem.j <= p
            j = j-1
         end
         do until stem.i >= p
            i = i+1
         end
         if i < j then do
            t = stem.i; stem.i = stem.j; stem.j = t
         end
         else
            leave
      end
      push l j; push j+1 r
   end
end
return

Recursive:
procedure expose stem.
arg l r
m = (l+r)%2; p = stem.m
i = l; j = r
do while i <= j
   do i = i while stem.i < p
   end
   do j = j by -1 while stem.j > p
   end
   if i <= j then do
      t = stem.i; stem.i = stem.j; stem.j = t
      i = i+1; j = j-1
   end
end
if l < j then
   call Recursive l j
if i < r then
   call Recursive i r
return

Optimized:
procedure expose stem.
n = stem.0; s = 1; sl.1 = 1; sr.1 = n
do until s = 0
   l = sl.s; r = sr.s; s = s-1
   do until l >= r
      if r-l < 20 then do
         do i = l+1 to r
            a = stem.i
            do j=i-1 by -1 to l while stem.j > a
               k = j+1; stem.k = stem.j
            end
            k = j+1; stem.k = a
         end
         if s = 0 then
            leave
         l = sl.s; r = sr.s; s = s-1
      end
      else do
         m = (l+r)%2
         if stem.l > stem.m then do
            t = stem.l; stem.l = stem.m; stem.m = t
         end
         if stem.l > stem.r then do
            t = stem.l; stem.l = stem.r; stem.r = t
         end
         if stem.m > stem.r then do
            t = stem.m; stem.m = stem.r; stem.r = t
         end
         i = l; j = r; p = stem.m
         do until i > j
            do i = i while stem.i < p
            end
            do j = j by -1 while stem.j > p
            end
            if i <= j then do
               t = stem.i; stem.i = stem.j; stem.j = t
               i = i+1; j = j-1
            end
         end
         if j-l < r-i then do
            if i < r then do
               s = s+1; sl.s = i; sr.s = r
            end
            r = j
         end
         else do
            if l < j then do
               s = s+1; sl.s = l; sr.s = j
            end
            l = i
         end
      end
   end
end
return

include Abend
```

Running under Regina with some values for n and v.

**Output:**

```
QUICKSORT - 4 Mar 2025
REXX-Regina_3.9.6(MT) 5.00 29 Apr 2024

Timing Version 0 for 1000 random numbers
1 1301504
2 38896302
3 64465028
4 45809725
5 15575175
996 63419779
997 64807001
998 37579553
999 48391176
1000 10331477

Save2Stack   0.001 seconds
Quicksort    0.014 seconds
Stack2Stem   0.000 seconds
1 61491
2 269651
3 273193
4 412881
5 502890
996 99166237
997 99503994
998 99694640
999 99764115
1000 99892071

Elegant   0.005 seconds
1 61491
2 269651
3 273193
4 412881
5 502890
996 99166237
997 99503994
998 99694640
999 99764115
1000 99892071

Recursive   0.005 seconds
1 61491
2 269651
3 273193
4 412881
5 502890
996 99166237
997 99503994
998 99694640
999 99764115
1000 99892071

Optimized   0.004 seconds
1 61491
2 269651
3 273193
4 412881
5 502890
996 99166237
997 99503994
998 99694640
999 99764115
1000 99892071

QUICKSORT - 4 Mar 2025
REXX-Regina_3.9.6(MT) 5.00 29 Apr 2024

Timing Version 0 for 10000 random numbers
1 45804118
2 58006939
3 99056246
4 19385685
5 20501425
9996 353332
9997 55031534
9998 59163614
9999 53889037
10000 50007918

Save2Stack   0.002 seconds
Quicksort    0.182 seconds
Stack2Stem   0.001 seconds
1 11640
2 11650
3 33340
4 38842
5 49723
9996 99969708
9997 99978183
9998 99982926
9999 99990755
10000 99994460

Elegant   0.060 seconds
1 11640
2 11650
3 33340
4 38842
5 49723
9996 99969708
9997 99978183
9998 99982926
9999 99990755
10000 99994460

Recursive   0.064 seconds
1 11640
2 11650
3 33340
4 38842
5 49723
9996 99969708
9997 99978183
9998 99982926
9999 99990755
10000 99994460

Optimized   0.048 seconds
1 11640
2 11650
3 33340
4 38842
5 49723
9996 99969708
9997 99978183
9998 99982926
9999 99990755
10000 99994460

QUICKSORT - 4 Mar 2025
REXX-Regina_3.9.6(MT) 5.00 29 Apr 2024

Timing Version 0 for 100000 random numbers
1 79656070
2 53147678
3 33198079
4 73711621
5 25030588
99996 95991033
99997 91754003
99998 96554128
99999 17561510
100000 90831043

Save2Stack   0.012 seconds
Quicksort    2.604 seconds
Stack2Stem   0.018 seconds
1 1655
2 2312
3 2996
4 5234
5 5910
99996 99996845
99997 99997333
99998 99998029
99999 99998520
100000 99998624

Elegant   0.831 seconds
1 1655
2 2312
3 2996
4 5234
5 5910
99996 99996845
99997 99997333
99998 99998029
99999 99998520
100000 99998624

Recursive   0.820 seconds
1 1655
2 2312
3 2996
4 5234
5 5910
99996 99996845
99997 99997333
99998 99998029
99999 99998520
100000 99998624

Optimized   0.624 seconds
1 1655
2 2312
3 2996
4 5234
5 5910
99996 99996845
99997 99997333
99998 99998029
99999 99998520
100000 99998624
```

And the same for ooRexx.

**Output:**

```
QUICKSORT - 4 Mar 2025
REXX-ooRexx_5.0.0(MT)_64-bit 6.05 23 Dec 2022

Timing Version 0  for 1000 random numbers
1 12348318
2 21439648
3 53366128
4 74109613
5 66433021
996 15294386
997 41393496
998 98896596
999 76044992
1000 36705449

Save2Stack   0.016 seconds
Quicksort    0.874 seconds
Stack2Stem   0.032 seconds
1 86063
2 244756
3 543315
4 573109
5 1007248
996 99303638
997 99361501
998 99490621
999 99607308
1000 99915213

Elegant   0.097 seconds
1 86063
2 244756
3 543315
4 573109
5 1007248
996 99303638
997 99361501
998 99490621
999 99607308
1000 99915213

Recursive   0.016 seconds
1 86063
2 244756
3 543315
4 573109
5 1007248
996 99303638
997 99361501
998 99490621
999 99607308
1000 99915213

Optimized   0.000 seconds
1 86063
2 244756
3 543315
4 573109
5 1007248
996 99303638
997 99361501
998 99490621
999 99607308
1000 99915213

QUICKSORT - 4 Mar 2025
REXX-ooRexx_5.0.0(MT)_64-bit 6.05 23 Dec 2022

Timing Version 0  for 10000 random numbers
1 18751559
2 9664983
3 6520871
4 81853537
5 89290461
9996 15858744
9997 68183578
9998 35786265
9999 56447804
10000 79587338

Save2Stack   0.203 seconds
Quicksort   12.867 seconds
Stack2Stem   0.219 seconds
1 24406
2 29380
3 33215
4 41202
5 49899
9996 99934267
9997 99965563
9998 99969701
9999 99975853
10000 99981523

Elegant   1.218 seconds
1 24406
2 29380
3 33215
4 41202
5 49899
9996 99934267
9997 99965563
9998 99969701
9999 99975853
10000 99981523

Recursive   0.063 seconds
1 24406
2 29380
3 33215
4 41202
5 49899
9996 99934267
9997 99965563
9998 99969701
9999 99975853
10000 99981523

Optimized   0.047 seconds
1 24406
2 29380
3 33215
4 41202
5 49899
9996 99934267
9997 99965563
9998 99969701
9999 99975853
10000 99981523

QUICKSORT - 4 Mar 2025
REXX-ooRexx_5.0.0(MT)_64-bit 6.05 23 Dec 2022

Timing Version 0  for 100000 random numbers
1 14248584
2 45991690
3 89316579
4 84248840
5 12197638
99996 37141859
99997 969474
99998 38567819
99999 51328048
100000 15192855

Save2Stack   1.890 seconds
Quicksort  234.253 seconds
Stack2Stem   1.906 seconds
1 204
2 2240
3 3097
4 3636
5 7776
99996 99996524
99997 99996951
99998 99998955
99999 99999284
100000 99999411

Elegant  12.473 seconds
1 204
2 2240
3 3097
4 3636
5 7776
99996 99996524
99997 99996951
99998 99998955
99999 99999284
100000 99999411

Recursive   1.047 seconds
1 204
2 2240
3 3097
4 3636
5 7776
99996 99996524
99997 99996951
99998 99998955
99999 99999284
100000 99999411

Optimized   0.843 seconds
1 204
2 2240
3 3097
4 3636
5 7776
99996 99996524
99997 99996951
99998 99998955
99999 99999284
100000 99999411
```

- Overall Regina is about 2 times faster with big stems
- Both interpreters aren't really fond of stack operations
- But ooRexx underperforms in this area
- Straithforward coding (no stack, no recursion) showed to be fastest
- However, the fast versions require 'expose stem.' and thus are not generic anymore


## Refal

```mw
$ENTRY Go {
    , 7 6 5 9 8 4 3 1 2 0: e.Arr
    = <Prout e.Arr>
      <Prout <Sort e.Arr>>;
};

Sort {
    = ;
    s.N = s.N;
    s.Pivot e.X =
        <Sort <Filter s.Pivot '-' e.X>>
        <Filter s.Pivot '=' e.X>
        s.Pivot
        <Sort <Filter s.Pivot '+' e.X>>;
};

Filter {
    s.N s.Comp = ;
    s.N s.Comp s.I e.List, <Compare s.I s.N>: {
        s.Comp = s.I <Filter s.N s.Comp e.List>;
        s.X = <Filter s.N s.Comp e.List>;
    };
};
```

**Output:**

```
7 6 5 9 8 4 3 1 2 0
0 1 2 3 4 5 6 7 8 9
```


## Ring

```mw
# Project : Sorting algorithms/Quicksort

test = [4, 65, 2, -31, 0, 99, 2, 83, 782, 1]
see "before sort:" + nl
showarray(test)
quicksort(test, 1, 10)
see "after sort:" + nl
showarray(test)
 
func quicksort(a, s, n)
       if n < 2 
          return
       ok
       t = s + n - 1
       l = s
       r = t
       p = a[floor((l + r) / 2)]
       while l <= r
               while a[l] < p 
                       l = l + 1
               end
               while a[r] > p
                       r = r - 1
               end
               if l <= r
                  temp = a[l]
                  a[l] = a[r]
                  a[r] = temp
                  l = l + 1
                  r = r - 1
              ok
       end
       if s < r 
          quicksort(a, s, r - s + 1)
       ok
       if l < t 
         quicksort(a, l, t - l + 1 )
       ok

func showarray(vect)
        svect = ""
        for n = 1 to len(vect)
              svect = svect + vect[n] + " "
        next
        svect = left(svect, len(svect) - 1)
        see svect + nl
```

Output:

```
before sort:
4 65 2 -31 0 99 2 83 782 1
after sort:
-31 0 1 2 2 4 65 83 99 782
```


## RISC-V Assembly

for Raspberry pi pico 2 see instructions to page risc v

```mw
# riscv assembly raspberry pico2 rp2350
# program quicksort.s
# connexion putty com3
/*********************************************/
/*           CONSTANTES                      */
/********************************************/
/* for this file see risc-v task include a file */
.include "../../../constantesRiscv.inc"

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

szMessSortOk:       .asciz "Area sorted.\n"
szMessSortNok:      .asciz "Area not sorted !!!!!.\n"
szLibSort:          .asciz "\nAfter sort\n"
szSpace:            .asciz " " 

.align 2
tabNumber:        .int 5,7,8,3,2,9,1,4,6     
#tabNumber:        .int 9,8,7,6,5,4,3,2,1      
.equ NBTABNUMBER1, . - tabNumber
.equ NBTABNUMBER, NBTABNUMBER1 / 4 # compute items number

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

    la s0,tabNumber            # number array address
   li s1,0
   li s2,NBTABNUMBER
2:                             # item loop
    sh2add t3,s1,s0            # compute item address
   lw a0,(t3)
   call displayResultD
   add s1,s1,1
   blt s1,s2,2b   
    la a0,szCariageReturn
    call writeString
   mv a0,s0                   # number array address
   li a1,0                    # first item
   addi a2,s2,-1              # last item
   call quickSort            # sort
   mv a0,s0                   # number array address
   li a1,0                    # first item
   addi a2,s2,-1              # last item 
   call isSorted
   
   la a0,szLibSort
   call writeString

   li s1,0
3:                             # item loop
    sh2add t3,s1,s0            # compute item address
   lw a0,(t3)
   call displayResultD
   add s1,s1,1
   blt s1,s2,3b
    la a0,szCariageReturn
    call writeString
   la a0,szMessEnd
   call writeString
    call getchar
100:                           # final loop
    j 100b
/**********************************************/
/*   display Result  décimal                     */
/**********************************************/
/* a0    value */
.equ LGZONECONV,   20
displayResultD:
    addi    sp, sp, -4         # reserve stack
    sw      ra, 0(sp)
    la a1,sConvArea            # conversion result address
    call conversion10          # binary conversion 
    la a0,sConvArea            # message address
    call writeString           # display message
    la a0,szSpace
    call writeString
100:
    lw      ra, 0(sp)
    addi    sp, sp, 4
    ret 
   
/**********************************************/
/*                        */
/**********************************************/
/* a0 area address */
/* a1 first element */
/* a2 last element */
.equ LGZONECONV,   20
isSorted:
    addi    sp, sp, -4         # reserve stack
    sw      ra, 0(sp)
   mv t0,a1
   sh2add t1,t0,a0
   lw t2,(t1)                 # load first element
1:
    addi t0,t0,1
    ble t0,a2,2f               # end indice ?
   la a0,szMessSortOk
   call writeString
    li a0,1                    # yes -> area is sorted
    j 100f  
2:
   sh2add t1,t0,a0
   lw t3,(t1)                 # load next element  
   bge t3,t2,3f               # >=  ?
   la a0,szMessSortNok
   call writeString
    li a0,0                    # no -> area is not sorted
    j 100f  
3:
    mv t2,t3
   j 1b
100:
    lw      ra, 0(sp)
    addi    sp, sp, 4
    ret 

/******************************************************************/
/*         quick sort                                         */ 
/******************************************************************/
/* a0 contains array address */
/* a1 contains the first element    */
/* a2 contains the last element  */
quickSort:
    addi    sp, sp, -16        # reserve stack
    sw      ra, 0(sp)          # save registers
   sw      s0, 4(sp)
   sw      s1, 8(sp)
   sw      s2, 12(sp)
   bge a1,a2,100f             # first > last ? -> end
   mv s0,a0                   # save address area
   mv s1,a1                   # save first indice
   mv s2,a2                   # save last indice
    call partition             # partitioning
   addi  a2,a0,-1             # index partition - 1
   mv a1,s1                   # move first index
   mv s1,a0                   # save partition index
   mv a0,s0                   # array address
   call quickSort             # sort lower part
   addi a1,s1,1               # partition index + 1
   mv a2,s2                   # last index
   mv a0,s0
   call quickSort            # sort higter part
   
100:
    lw      ra, 0(sp)
    lw      s0, 4(sp)
   lw      s1, 8(sp)
   lw      s2, 12(sp)
    addi    sp, sp, 16
    ret
/******************************************************************/
/*         shell sort                                         */ 
/******************************************************************/
/* a0 contains the address of table */
/* a1 contains index of first item  */
/* a2 contains index of last item   */
partition:                     # INFO: partition
    addi    sp, sp, -4         # reserve stack
    sw      ra, 0(sp)          # save registers 
   mv t0,a1                   # init with first index
   mv t1,a1                   # init with first index
   sh2add t2,a2,a0   
   lw t3,(t2)                 # load value last index
1:                             # begin loop
    sh2add t2,t1,a0  
   lw t4,(t2)                 # load value
   bge t4,t3,2f               # compare value 2
   sh2add t2,t0,a0            # if value2 < value 1 -> swap values
   lw t5,(t2)
   sh2add t2,t0,a0
   sw t4,(t2)
   sh2add t2,t1,a0
   sw t5,(t2)
   addi t0,t0,1               # increment index
2:
   addi t1,t1,1               # increment index 2
    blt t1,a2,1b               # < maxi -> loop
   sh2add t2,t0,a0            # else swap value
   lw t5,(t2)
   sh2add t2,t0,a0
   sw t3,(t2)
   sh2add t2,a2,a0 
   sw t5,(t2)
   mv a0,t0                   # return index partition   
   
100:
    lw      ra, 0(sp)
    addi    sp, sp, 4
    ret  
/************************************/
/*     file include  Fonctions   */
/***********************************/
/* for this file see risc-v task include a file */
.include "../../../includeFunctions.s"
```

```
Program riscv start.
5 7 8 3 2 9 1 4 6
Area sorted.

After sort
1 2 3 4 5 6 7 8 9

Program end OK.
```


## RPL

Works with

:

HP

version 48

```
≪ DUP SIZE → size 
   ≪ IF size 1 > THEN
         DUP size 2 / CEIL GET { } DUP DUP → pivot less equal greater
         ≪ 1 size FOR j
              DUP j GET pivot 
              CASE
                 DUP2 <  THEN DROP 'less'  STO+ END
                 DUP2 == THEN DROP 'equal' STO+ END
                 DROP 'greater' STO+ END
            NEXT DROP
            less QSORT
            greater QSORT
            equal SWAP + +
         ≫ 
      END
≫ ≫ 'QSORT' STO 
```


## Ruby

```mw
class Array
  def quick_sort
    return self if length <= 1
    pivot = self[0]
    less, greatereq = self[1..-1].partition { |x| x < pivot }
    less.quick_sort + [pivot] + greatereq.quick_sort
  end
end
```

or

```mw
class Array
  def quick_sort
    return self if length <= 1
    pivot = sample
    group = group_by{ |x| x <=> pivot }
    group.default = []
    group[-1].quick_sort + group[0] + group[1].quick_sort
  end
end
```

or functionally

```mw
class Array
  def quick_sort
    h, *t = self
    h ? t.partition { |e| e < h }.inject { |l, r| l.quick_sort + [h] + r.quick_sort } : []
  end
end
```


## Rust

```mw
fn main() {
    println!("Sort numbers in descending order");
    let mut numbers = [4, 65, 2, -31, 0, 99, 2, 83, 782, 1];
    println!("Before: {:?}", numbers);

    quick_sort(&mut numbers, &|x,y| x > y);
    println!("After:  {:?}\n", numbers);

    println!("Sort strings alphabetically");
    let mut strings = ["beach", "hotel", "airplane", "car", "house", "art"];
    println!("Before: {:?}", strings);

    quick_sort(&mut strings, &|x,y| x < y);
    println!("After:  {:?}\n", strings);
    
    println!("Sort strings by length");
    println!("Before: {:?}", strings);

    quick_sort(&mut strings, &|x,y| x.len() < y.len());
    println!("After:  {:?}", strings);    
}

fn quick_sort<T,F>(v: &mut [T], f: &F) 
    where F: Fn(&T,&T) -> bool
{
    let len = v.len();
    if len >= 2 {
        let pivot_index = partition(v, f);
        quick_sort(&mut v[0..pivot_index], f);
        quick_sort(&mut v[pivot_index + 1..len], f);
    }
}

fn partition<T,F>(v: &mut [T], f: &F) -> usize 
    where F: Fn(&T,&T) -> bool
{
    let len = v.len();
    let pivot_index = len / 2;
    let last_index = len - 1;

    v.swap(pivot_index, last_index);

    let mut store_index = 0;
    for i in 0..last_index {
        if f(&v[i], &v[last_index]) {
            v.swap(i, store_index);
            store_index += 1;
        }
    }

    v.swap(store_index, len - 1);
    store_index
}
```

**Output:**

```
Sort numbers in descending order
Before: [4, 65, 2, -31, 0, 99, 2, 83, 782, 1]
After:  [782, 99, 83, 65, 4, 2, 2, 1, 0, -31]

Sort strings alphabetically
Before: ["beach", "hotel", "airplane", "car", "house", "art"]
After:  ["airplane", "art", "beach", "car", "hotel", "house"]

Sort strings by length
Before: ["airplane", "art", "beach", "car", "hotel", "house"]
After:  ["car", "art", "house", "hotel", "beach", "airplane"]
```

Or, using functional style (slower than the imperative style but faster than functional style in other languages):

```mw
fn main() {
    let numbers = [4, 65, 2, -31, 0, 99, 2, 83, 782, 1];
    println!("{:?}\n", quick_sort(numbers.iter()));
}

fn quick_sort<T, E>(mut v: T) -> Vec<E>
where
    T: Iterator<Item = E>,
    E: PartialOrd,
{
    match v.next() {
        None => Vec::new(),

        Some(pivot) => {
            let (lower, higher): (Vec<_>, Vec<_>) = v.partition(|it| it < &pivot);
            let lower = quick_sort(lower.into_iter());
            let higher = quick_sort(higher.into_iter());
            lower.into_iter()
                .chain(core::iter::once(pivot))
                .chain(higher.into_iter())
                .collect()
        }
    }
}
```

By the way this implementation needs only O(n) memory because the partition(...) call already "consumes" v. This means that the memory of v will be freed here, before the recursive calls to quick_sort(...). If we tried to use v later, we would get a compilation error.


## SASL

Copied from SASL manual, Appendix II, solution (2)(b)

```mw
DEF || this rather nice solution is due to Silvio Meira
sort () = ()
sort (a : x) = sort {b <- x; b <= a } ++ a : sort { b <- x; b>a}
?
```


## Sather

```mw
class SORT{T < $IS_LT{T}} is

  private afilter(a:ARRAY{T}, cmp:ROUT{T,T}:BOOL, p:T):ARRAY{T} is
    filtered ::= #ARRAY{T};
    loop v ::= a.elt!;
      if cmp.call(v, p) then
        filtered := filtered.append(|v|);
      end;
    end;
    return filtered;
  end;

  private mlt(a, b:T):BOOL is return a < b; end;
  private mgt(a, b:T):BOOL is return a > b; end;
  quick_sort(inout a:ARRAY{T}) is
    if a.size < 2 then return; end;
    pivot ::= a.median;
    left:ARRAY{T} := afilter(a, bind(mlt(_,_)), pivot);
    right:ARRAY{T} := afilter(a, bind(mgt(_,_)), pivot);
    quick_sort(inout left);
    quick_sort(inout right);
    res ::= #ARRAY{T};
    res := res.append(left, |pivot|,  right);
    a := res;
  end;
end;
```

```mw
class MAIN is
  main is
    a:ARRAY{INT} := |10, 9, 8, 7, 6, -10, 5, 4, 656, -11|;
    b ::= a.copy;
    SORT{INT}::quick_sort(inout a);
    #OUT + a + "\n" + b.sort + "\n";
  end;
end;
```

The ARRAY class has a builtin sorting method, which is quicksort (but under certain condition an insertion sort is used instead), exactly `quicksort_range`; this implementation is original.


## Scala

What follows is a progression on genericity here.

First, a quick sort of a list of integers:

```mw
  def sort(xs: List[Int]): List[Int] = xs match {
    case Nil => Nil
    case head :: tail =>
      val (less, notLess) = tail.partition(_ < head) // Arbitrarily partition list in two
      sort(less) ++ (head :: sort(notLess))          // Sort each half
  }
```

Next, a quick sort of a list of some type T, given a lessThan function:

```mw
  def sort[T](xs: List[T], lessThan: (T, T) => Boolean): List[T] = xs match {
    case Nil => Nil
    case x :: xx =>
      val (lo, hi) = xx.partition(lessThan(_, x))
      sort(lo, lessThan) ++ (x :: sort(hi, lessThan))
  }
```

To take advantage of known orderings, a quick sort of a list of some type T, for which exists an implicit (or explicit) Ordering[T]:

```mw
  def sort[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = xs match {
    case Nil => Nil
    case x :: xx =>
      val (lo, hi) = xx.partition(ord.lt(_, x))
      sort[T](lo) ++ (x :: sort[T](hi))
  }
```

That last one could have worked with Ordering, but Ordering is Java, and doesn't have the less than operator. Ordered is Scala-specific, and provides it.

```mw
  def sort[T <: Ordered[T]](xs: List[T]): List[T] = xs match {
    case Nil => Nil
    case x :: xx =>
      val (lo, hi) = xx.partition(_ < x)
      sort(lo) ++ (x :: sort(hi))
  }
```

What hasn't changed in all these examples is ordering a list. It is possible to write a generic quicksort in Scala, which will order any kind of collection. To do so, however, requires that the type of the collection, itself, be made a parameter to the function. Let's see it below, and then remark upon it:

```mw
  def sort[T, C[T] <: scala.collection.TraversableLike[T, C[T]]]
    (xs: C[T])
    (implicit ord: scala.math.Ordering[T],
      cbf: scala.collection.generic.CanBuildFrom[C[T], T, C[T]]): C[T] = {
    // Some collection types can't pattern match
    if (xs.isEmpty) {
      xs
    } else {
      val (lo, hi) = xs.tail.partition(ord.lt(_, xs.head))
      val b = cbf()
      b.sizeHint(xs.size)
      b ++= sort(lo)
      b += xs.head
      b ++= sort(hi)
      b.result()
    }
  }
```

The type of our collection is "C[T]", and, by providing C[T] as a type parameter to TraversableLike, we ensure C[T] is capable of returning instances of type C[T]. Traversable is the base type of all collections, and TraversableLike is a trait which contains the implementation of most Traversable methods.

We need another parameter, though, which is a factory capable of building a C[T] collection. That is being passed implicitly, so callers to this method do not need to provide them, as the collection they are using should already provide one as such implicitly. Because we need that implicitly, then we need to ask for the "T => Ordering[T]" as well, as the "T <: Ordered[T]" which provides it cannot be used in conjunction with implicit parameters.

The body of the function is from the list variant, since many of the Traversable collection types don't support pattern matching, "+:" or "::".


## Scheme

### List quicksort

```mw
(define (split-by l p k)
  (let loop ((low '())
             (high '())
             (l l))
    (cond ((null? l)
           (k low high))
          ((p (car l))
           (loop low (cons (car l) high) (cdr l)))
          (else
           (loop (cons (car l) low) high (cdr l))))))
 
(define (quicksort l gt?)
  (if (null? l)
      '()
      (split-by (cdr l) 
                (lambda (x) (gt? x (car l)))
                (lambda (low high)
                  (append (quicksort low gt?)
                          (list (car l))
                          (quicksort high gt?))))))

(quicksort '(1 3 5 7 9 8 6 4 2) >)
```

With srfi-1:

```mw
(define (quicksort l gt?)
  (if (null? l)
      '()
      (append (quicksort (filter (lambda (x) (gt? (car l) x)) (cdr l)) gt?)
              (list (car l))
              (quicksort (filter (lambda (x) (not (gt? (car l) x))) (cdr l)) gt?))))

(quicksort '(1 3 5 7 9 8 6 4 2) >)
```

### Vector quicksort (in place)

Works with

:

Chibi Scheme

Works with

:

Gauche Scheme

Works with

:

CHICKEN Scheme

version 5.3.0

For CHICKEN:

Library:

r7rs

```mw
;;;-------------------------------------------------------------------
;;;
;;; Quicksort in R7RS Scheme, working in-place on vectors (that is,
;;; arrays). I closely follow the "better quicksort algorithm"
;;; pseudocode, and thus the code is more "procedural" than
;;; "functional".
;;;
;;; I use a random pivot. If you can generate a random number quickly,
;;; this is a good method, but for this demonstration I have taken a
;;; fast linear congruential generator and made it brutally slow. It's
;;; just a demonstration. :)
;;;

(import (scheme base))
(import (scheme case-lambda))
(import (scheme write))

;;;-------------------------------------------------------------------
;;;
;;; Add "while" loops to the language.
;;;

(define-syntax while
  (syntax-rules ()
    ((_ pred? body ...)
     (let loop ()
       (when pred?
         (begin body ...)
         (loop))))))

;;;-------------------------------------------------------------------
;;;
;;; In-place quicksort.
;;;

(define vector-quicksort!
  (case-lambda

    ;; Use a default pivot selector.
    ((<? vec)
     ;; Random pivot.
     (vector-quicksort! (lambda (vec i-first i-last)
                          (vector-ref vec (randint i-first i-last)))
                        <? vec))

    ;; Specify a pivot selector.
    ((pivot-select <? vec)
     ;;
     ;; The recursion:
     ;;
     (let quicksort! ((i-first 0)
                      (i-last (- (vector-length vec) 1)))
       (let ((n (- i-last i-first -1)))
         (when (> n 1)
           (let* ((pivot (pivot-select vec i-first i-last)))
             (let ((left i-first)
                   (right i-last))
               (while (<= left right)
                 (while (< (vector-ref vec left) pivot)
                   (set! left (+ left 1)))
                 (while (> (vector-ref vec right) pivot)
                   (set! right (- right 1)))
                 (when (<= left right)
                   (let ((lft (vector-ref vec left))
                         (rgt (vector-ref vec right)))
                     (vector-set! vec left rgt)
                     (vector-set! vec right lft)
                     (set! left (+ left 1))
                     (set! right (- right 1)))))
               (quicksort! i-first right)
               (quicksort! left i-last)))))))))

;;;-------------------------------------------------------------------
;;;
;;; A simple linear congruential generator, attributed by
;;; https://en.wikipedia.org/w/index.php?title=Linear_congruential_generator&oldid=1083800601
;;; to glibc and GCC. No attempt has been made to optimize this code.
;;;

(define seed 1)
(define two**31 (expt 2 31))
(define (random-integer)
  (let* ((s0 seed)
         (s1 (truncate-remainder (+ (* 1103515245 s0) 12345)
                                 two**31)))
    (set! seed s1)
    s0))
(define randint
  (case-lambda
    ((n) (truncate-remainder (random-integer) n))
    ((i-first i-last) (+ i-first (randint (- i-last i-first -1))))))

;;;-------------------------------------------------------------------
;;;
;;; A demonstration of in-place vector quicksort.
;;;

(define vec1 (vector-copy #(60 53 100 72 19 67 14
                               31 4 1 5 9 2 6 5 3 5 8
                               28 9 95 22 67 55 20 41
                               42 29 20 74 39)))
(vector-quicksort! < vec1)
(write vec1)
(newline)

;;;-------------------------------------------------------------------
```

**Output:**

```
$ gosh vector-quicksort.scm
#(1 2 3 4 5 5 5 6 8 9 9 14 19 20 20 22 28 29 31 39 41 42 53 55 60 67 67 72 74 95 100)
```


## Seed7

```mw
const proc: quickSort (inout array elemType: arr, in integer: left, in integer: right) is func
  local
    var elemType: compare_elem is elemType.value;
    var integer: less_idx is 0;
    var integer: greater_idx is 0;
    var elemType: help is elemType.value;
  begin
    if right > left then
      compare_elem := arr[right];
      less_idx := pred(left);
      greater_idx := right;
      repeat
        repeat
          incr(less_idx);
        until arr[less_idx] >= compare_elem;
        repeat
          decr(greater_idx);
        until arr[greater_idx] <= compare_elem or greater_idx = left;
        if less_idx < greater_idx then
          help := arr[less_idx];
          arr[less_idx] := arr[greater_idx];
          arr[greater_idx] := help;
        end if;
      until less_idx >= greater_idx;
      arr[right] := arr[less_idx];
      arr[less_idx] := compare_elem;
      quickSort(arr, left, pred(less_idx));
      quickSort(arr, succ(less_idx), right);
    end if;
  end func;

const proc: quickSort (inout array elemType: arr) is func
  begin
    quickSort(arr, 1, length(arr));
  end func;
```

Original source: [2]


## SETL

In-place sort (looks much the same as the C version)

```mw
a := [2,5,8,7,0,9,1,3,6,4];
qsort(a);
print(a);

proc qsort(rw a);
  if #a > 1 then
    pivot := a(#a div 2 + 1);
    l := 1;
    r := #a;
    (while l < r)
      (while a(l) < pivot) l +:= 1; end;
      (while a(r) > pivot) r -:= 1; end;
      swap(a(l), a(r));
    end;
    qsort(a(1..l-1));
    qsort(a(r+1..#a));
  end if;
end proc;

proc swap(rw x, rw y);
  [y,x] := [x,y];
end proc;
```

Copying sort using comprehensions:

```mw
a := [2,5,8,7,0,9,1,3,6,4];
print(qsort(a));

proc qsort(a);
  if #a > 1 then
    pivot := a(#a div 2 + 1);
    a := qsort([x in a | x < pivot]) +
         [x in a | x = pivot] +
         qsort([x in a | x > pivot]);
  end if;
  return a;
end proc;
```


## Sidef

```mw
func quicksort (a) {
    a.len < 2 && return(a);
    var p = a.pop_rand;          # to avoid the worst cases
    __FUNC__(a.grep{ .< p}) + [p] + __FUNC__(a.grep{ .>= p});
}
```


## Simula

```mw
PROCEDURE QUICKSORT(A); REAL ARRAY A;
BEGIN

    PROCEDURE QS(A, FIRST, LAST); REAL ARRAY A; INTEGER FIRST, LAST;
    BEGIN
        INTEGER LEFT, RIGHT;
        LEFT := FIRST; RIGHT := LAST;
        IF RIGHT - LEFT + 1 > 1 THEN
        BEGIN
            REAL PIVOT;
            PIVOT := A((LEFT + RIGHT) // 2); 
            WHILE LEFT <= RIGHT DO
            BEGIN
                WHILE A(LEFT) < PIVOT DO LEFT := LEFT + 1;
                WHILE A(RIGHT) > PIVOT DO RIGHT := RIGHT - 1;
                IF LEFT <= RIGHT THEN
                BEGIN
                    REAL SWAP;
                    SWAP := A(LEFT); A(LEFT) := A(RIGHT); A(RIGHT) := SWAP;
                    LEFT := LEFT + 1; RIGHT := RIGHT - 1;
                END;
            END;
            QS(A, FIRST, RIGHT);
            QS(A, LEFT, LAST);
        END;
    END QS;

    QS(A, LOWERBOUND(A, 1), UPPERBOUND(A, 1));

END QUICKSORT;
```


## Standard ML

```mw
fun quicksort [] = []
  | quicksort (x::xs) =
    let 
        val (left, right) = List.partition (fn y => y<x) xs
    in
        quicksort left @ [x] @ quicksort right
    end
```

Solution 2:

Without using List.partition

```mw
fun par_helper([], x, l, r) = (l, r) 
  | par_helper(h::t, x, l, r) = 
      if h <= x then 
         par_helper(t, x, l @ [h], r)
      else
         par_helper(t, x, l, r @ [h]);

fun par(l, x) = par_helper(l, x, [], []);

fun quicksort [] = []
  | quicksort (h::t) =
    let 
        val (left, right) = par(t, h)
    in
        quicksort left @ [h] @ quicksort right
    end;
```


## Swift

```mw
func quicksort<T where T : Comparable>(inout elements: [T], range: Range<Int>) {
  if (range.endIndex - range.startIndex > 1) {
    let pivotIndex = partition(&elements, range)
    quicksort(&elements, range.startIndex ..< pivotIndex)
    quicksort(&elements, pivotIndex+1 ..< range.endIndex)
  }
}

func quicksort<T where T : Comparable>(inout elements: [T]) {
  quicksort(&elements, indices(elements))
}
```


## Symsyn

```mw
x : 23 : 15 : 99 : 146 : 3 : 66 : 71 : 5 : 23 : 73 : 19

quicksort param l r

   l i
   r j
   ((l+r) shr 1) k
   x.k pivot

repeat
   if pivot > x.i
      + cmp 
      + i
      goif
   endif

   if pivot < x.j
      + cmp
      - j
      goif
   endif

   if i <= j
      swap x.i x.j
      - j
      + i
   endif

   if i <= j
      go repeat
   endif

   if l < j 
      save l r i j
      call quicksort l j
      restore l r i j
   endif
 
   if i < r 
      save l r i j
      call quicksort i r
      restore l r i j
   endif

   return

start

 ' original values : ' $r

 call showvalues

 call quicksort 0 10

 ' sorted values : ' $r

 call showvalues

 stop

showvalues
 $s
 i
 if i <= 10
    "$s ' ' x.i ' '" $s
    + i
    goif
 endif
 " $r $s " []

 return
```


## Tailspin

Simple recursive quicksort:

```mw
templates quicksort
  @: [];
  $ -> #
  when <[](2..)> do
    def pivot: $(1);
    [ [ $(2..last)... -> \(
      when <..$pivot> do
        $ !
      otherwise
        ..|@quicksort: $;
     \)] -> quicksort..., $pivot, $@ -> quicksort... ] !
   otherwise
     $ !
end quicksort

[4,5,3,8,1,2,6,7,9,8,5] -> quicksort -> !OUT::write
```

In v0.5 recursion must be done internally on the matchers, so we need a separate partition function

```mw
quicksort templates
  partition templates
    @ set [];
    pivot is $(1);
    [$(2..)... -> #]!
    $pivot !
    $@ !
    when <|..$pivot> do
      $ !
    otherwise
      ..|@ set $;
  end partition
  [$ -> #] !
  when <|[](1..)> do
    $ -> partition -> # !
  when <~|[]> do
    $ !
end quicksort

[4,5,3,8,1,2,6,7,9,8,5] -> quicksort !
```

In place:

```mw
templates quicksort
  templates partial
    def first: $(1);
    def last: $(2);
    def pivot: $@quicksort($first);
    @: $(1) + 1;
    $(2) -> #

    when <..~$@> do
      def limit: $;
      @quicksort($first): $@quicksort($limit);
      @quicksort($limit): $pivot;
      [ $first, $limit - 1 ] !
      [ $limit + 1, $last ] !

    when <?($@quicksort($) <$pivot~..>)> do
      $ - 1 -> #

    when <?($@quicksort($@) <..$pivot>)> do
      @: $@ + 1; $ -> #

    otherwise
      def temp: $@quicksort($@);
      @quicksort($@): $@quicksort($);
      @quicksort($): $temp;
      @: $@ + 1; $ - 1 -> #
  end partial
  @: $;
  [1, $@::length] -> #
  $@ !

  when <?($(1) <..~$(2)>)> do
    $ -> partial -> #
end quicksort

[4,5,3,8,1,2,6,7,9,8,5] -> quicksort -> !OUT::write
```

v0.5

```mw
quicksort templates
  partial templates
    first is $(1);
    last is $(2);
    pivot is $@quicksort($first);
    @ set $first + 1;
    $last -> # !

    when <|..~$@> do
      limit is $;
      @quicksort($first) set $@quicksort($limit);
      @quicksort($limit) set $pivot;
      [ $first, $limit - 1 ] !
      [ $limit + 1, $last ] !

    when <|?($@quicksort($) matches <|$pivot~..>)> do
      $ - 1 -> # !

    when <|?($@quicksort($@) matches <|..$pivot>)> do
      @ set $@ + 1; $ -> # !

    otherwise
      temp is $@quicksort($@);
      @quicksort($@) set $@quicksort($);
      @quicksort($) set $temp;
      @ set $@ + 1; $ - 1 -> # !
  end partial

  @ set $;
  [1, $@::length] -> !#
  $@ !

  when <|?($(1) matches <|..~$(2)>)> do
    $ -> partial -> !#
end quicksort

[4,5,3,8,1,2,6,7,9,8,5] -> quicksort !
```


## Tcl

```mw
package require Tcl 8.5

proc quicksort {m} {
    if {[llength $m] <= 1} {
        return $m
    }
    set pivot [lindex $m 0]
    set less [set equal [set greater [list]]]
    foreach x $m {
        lappend [expr {$x < $pivot ? "less" : $x > $pivot ? "greater" : "equal"}] $x
    }
    return [concat [quicksort $less] $equal [quicksort $greater]]
}

puts [quicksort {8 6 4 2 1 3 5 7 9}] ;# => 1 2 3 4 5 6 7 8 9
```


## TypeScript

```mw
/**
  Generic quicksort function using typescript generics.
  Follows quicksort as done in CLRS.
*/
export type Comparator<T> = (o1: T, o2: T) => number;

export function quickSort<T>(array: T[], compare: Comparator<T>) {
  if (array.length <= 1 || array == null) {
    return;
  }
  sort(array, compare, 0, array.length - 1);
}

function sort<T>(
    array: T[], compare: Comparator<T>, low: number, high: number) {
  if (low < high) {
    const partIndex = partition(array, compare, low, high);
    sort(array, compare, low, partIndex - 1);
    sort(array, compare, partIndex + 1, high);
  }
}

function partition<T>(
    array: T[], compare: Comparator<T>, low: number, high: number): number {
  const pivot: T = array[high];
  let i: number = low - 1;
  for (let j = low; j <= high - 1; j++) {
    if (compare(array[j], pivot) == -1) {
      i = i + 1;
      swap(array, i, j)
    }
  }
  if (compare(array[high], array[i + 1]) == -1) {
    swap(array, i + 1, high);
  }
  return i + 1;
}

function swap<T>(array: T[], i: number, j: number) {
  const newJ: T = array[i];
  array[i] = array[j];
  array[j] = newJ;
}

export function testQuickSort(): void {
  function numberComparator(o1: number, o2: number): number {
    if (o1 < o2) {
      return -1;
    } else if (o1 == o2) {
      return 0;
    }
    return 1;
  }
  let tests: number[][] = [
    [], [1], [2, 1], [-1, 2, -3], [3, 16, 8, -5, 6, 4], [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5]
  ];

  for (let testArray of tests) {
    quickSort(testArray, numberComparator);
    console.log(testArray);
  }
}
```


## UnixPipes

Works with

:

Zsh

```mw
split() {
  (while read n ; do
      test $1 -gt $n && echo $n > $2 || echo $n > $3
  done)
}

qsort() {
 (read p; test -n "$p" && (
     lc="1.$1" ; gc="2.$1"
     split $p >(qsort $lc >$lc) >(qsort $gc >$gc);
     cat $lc <(echo $p) $gc
     rm -f $lc $gc;
 ))
}

cat to.sort | qsort
```
