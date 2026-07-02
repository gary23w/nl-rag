---
title: "Sorting algorithms/Quicksort (part 1/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/8
---

# Sorting algorithms/Quicksort

<

Sorting algorithms

| This page uses content from **Wikipedia**. The original article was at Quicksort. The list of authors can be seen in the **page history**. As with Rosetta Code, the text of Wikipedia is available under the GNU FDL. (See links for details on variance) |
|---|

**Task**

Sort an array (or list) elements using the   *quicksort*   algorithm.

The elements must have a   strict weak order   and the index of the array can be of any discrete type.

For languages where this is not possible, sort an array of integers.

Quicksort, also known as   *partition-exchange sort*,   uses these steps.

1. Choose any element of the array to be the pivot.
2. Divide all other elements (except the pivot) into two partitions.
  - All elements less than the pivot must be in the first partition.
  - All elements greater than the pivot must be in the second partition.
3. Use recursion to sort both partitions.
4. Join the first sorted partition, the pivot, and the second sorted partition.

The best pivot creates partitions of equal length (or lengths differing by   **1**).

The worst pivot creates an empty partition (for example, if the pivot is the first or last element of a sorted array).

The run-time of Quicksort ranges from   *O(n*log*n)*   with the best pivots, to   *O(n2)*   with the worst pivots, where   *n*   is the number of elements in the array.

This is a simple quicksort algorithm, adapted from Wikipedia.

```
function quicksort(array)
    less, equal, greater := three empty arrays
    if length(array) > 1  
        pivot := select any element of array
        for each x in array
            if x < pivot then add x to less
            if x = pivot then add x to equal
            if x > pivot then add x to greater
        quicksort(less)
        quicksort(greater)
        array := concatenate(less, equal, greater)
```

A better quicksort algorithm works in place, by swapping elements within the array, to avoid the memory allocation of more arrays.

```
function quicksort(array)
    if length(array) > 1
        pivot := select any element of array
        left := first index of array
        right := last index of array
        while left ≤ right
            while array[left] < pivot
                left := left + 1
            while array[right] > pivot
                right := right - 1
            if left ≤ right
                swap array[left] with array[right]
                left := left + 1
                right := right - 1
        quicksort(array from first index to right)
        quicksort(array from left to last index)
```

Quicksort has a reputation as the fastest sort. Optimized variants of quicksort are common features of many languages and libraries. One often contrasts quicksort with   merge sort,   because both sorts have an average time of   *O(n*log*n)*.

"On average, mergesort does fewer comparisons than quicksort, so it may be better when complicated comparison routines are used. Mergesort also takes advantage of pre-existing order, so it would be favored for using sort() to merge several sorted arrays. On the other hand, quicksort is often faster for small arrays, and on arrays of a few distinct values, repeated many times."

—

http://perldoc.perl.org/sort.html

Quicksort is at one end of the spectrum of divide-and-conquer algorithms, with merge sort at the opposite end.

- Quicksort is a conquer-then-divide algorithm, which does most of the work during the partitioning and the recursive calls. The subsequent reassembly of the sorted partitions involves trivial effort.
- Merge sort is a divide-then-conquer algorithm. The partioning happens in a trivial way, by splitting the input array in half. Most of the work happens during the recursive calls and the merge phase.

With quicksort, every element in the first partition is less than or equal to every element in the second partition. Therefore, the merge phase of quicksort is so trivial that it needs no mention!

This task has not specified whether to allocate new arrays, or sort in place. This task also has not specified how to choose the pivot element. (Common ways to are to choose the first element, the middle element, or the median of three elements.) Thus there is a variety among the following implementations.


## 11l

Translation of

:

Python

```mw
F _quicksort(&array, start, stop) -> Void
   I stop - start > 0
      V pivot = array[start]
      V left = start
      V right = stop
      L left <= right
         L array[left] < pivot
            left++
         L array[right] > pivot
            right--
         I left <= right
            swap(&array[left], &array[right])
            left++
            right--
      _quicksort(&array, start, right)
      _quicksort(&array, left, stop)

F quicksort(&array)
   _quicksort(&array, 0, array.len - 1)

V arr = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
quicksort(&arr)
print(arr)
```

**Output:**

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


## 360 Assembly

Translation of

:

REXX

Structured version with ASM & ASSIST macros.

```mw
*        Quicksort                 14/09/2015 & 23/06/2016
QUICKSOR CSECT
         USING  QUICKSOR,R13       base register
         B      72(R15)            skip savearea
         DC     17F'0'             savearea
         STM    R14,R12,12(R13)    prolog
         ST     R13,4(R15)         "
         ST     R15,8(R13)         " 
         LR     R13,R15            "
         MVC    A,=A(1)            a(1)=1
         MVC    B,=A(NN)           b(1)=hbound(t)
         L      R6,=F'1'           k=1
       DO WHILE=(LTR,R6,NZ,R6)   do while k<>0    ==================
         LR     R1,R6              k 
         SLA    R1,2               ~
         L      R10,A-4(R1)        l=a(k)
         LR     R1,R6              k
         SLA    R1,2               ~
         L      R11,B-4(R1)        m=b(k)
         BCTR   R6,0               k=k-1
         LR     R4,R11             m
         C      R4,=F'2'           if m<2 
         BL     ITERATE            then iterate
         LR     R2,R10             l
         AR     R2,R11             +m
         BCTR   R2,0               -1
         ST     R2,X               x=l+m-1
         LR     R2,R11             m
         SRA    R2,1               m/2
         AR     R2,R10             +l
         ST     R2,Y               y=l+m/2
         L      R1,X               x
         SLA    R1,2               ~
         L      R4,T-4(R1)         r4=t(x)
         L      R1,Y               y
         SLA    R1,2               ~
         L      R5,T-4(R1)         r5=t(y)
         LR     R1,R10             l
         SLA    R1,2               ~
         L      R3,T-4(R1)         r3=t(l)
         IF     CR,R4,LT,R3        if t(x)<t(l)       ---+
         IF     CR,R5,LT,R4          if t(y)<t(x)        |
         LR     R7,R4                  p=t(x)            |
         L      R1,X                   x                 |
         SLA    R1,2                   ~                 |
         ST     R3,T-4(R1)             t(x)=t(l)         |
         ELSEIF CR,R5,GT,R3          elseif t(y)>t(l)    |
         LR     R7,R3                  p=t(l)            |
         ELSE   ,                    else                |
         LR     R7,R5                  p=t(y)            |
         L      R1,Y                   y                 |
         SLA    R1,2                   ~                 |
         ST     R3,T-4(R1)            t(y)=t(l)          |
         ENDIF  ,                    end if              |
         ELSE   ,                  else                  |
         IF     CR,R5,LT,R3          if t(y)<t(l)        |
         LR     R7,R3                  p=t(l)            |
         ELSEIF CR,R5,GT,R4          elseif t(y)>t(x)    |
         LR     R7,R4                  p=t(x)            |
         L      R1,X                   x                 |
         SLA    R1,2                   ~                 |
         ST     R3,T-4(R1)             t(x)=t(l)         |
         ELSE   ,                    else                |
         LR     R7,R5                  p=t(y)            |
         L      R1,Y                   y                 |
         SLA    R1,2                   ~                 |
         ST     R3,T-4(R1)             t(y)=t(l)         |
         ENDIF  ,                    end if              |
         ENDIF  ,                  end if             ---+
         LA     R8,1(R10)          i=l+1
         L      R9,X               j=x
FOREVER  EQU    *                  do forever  --------------------+  
         LR     R1,R8                i                             |
         SLA    R1,2                 ~                             |
         LA     R2,T-4(R1)           @t(i)                         |
         L      R0,0(R2)             t(i)                          |
         DO WHILE=(CR,R8,LE,R9,AND,  while i<=j and   ---+         |   X
               CR,R0,LE,R7)                t(i)<=p       |         |
         AH     R8,=H'1'               i=i+1             |         |
         AH     R2,=H'4'               @t(i)             |         |
         L      R0,0(R2)               t(i)              |         |
         ENDDO  ,                    end while        ---+         |
         LR     R1,R9                j                             |
         SLA    R1,2                 ~                             |
         LA     R2,T-4(R1)           @t(j)                         |
         L      R0,0(R2)             t(j)                          |
         DO WHILE=(CR,R8,LT,R9,AND,  while i<j and    ---+         |   X
               CR,R0,GE,R7)                t(j)>=p       |         |
         SH     R9,=H'1'               j=j-1             |         |
         SH     R2,=H'4'               @t(j)             |         |
         L      R0,0(R2)               t(j)              |         |
         ENDDO  ,                    end while        ---+         |
         CR     R8,R9                if i>=j                       |
         BNL    LEAVE                then leave (segment finished) |
         LR     R1,R8                i                             |
         SLA    R1,2                 ~                             |
         LA     R2,T-4(R1)           @t(i)                         |
         LR     R1,R9                j                             |
         SLA    R1,2                 ~                             |
         LA     R3,T-4(R1)           @t(j)                         |
         L      R0,0(R2)             w=t(i)       +                |
         MVC    0(4,R2),0(R3)        t(i)=t(j)    |swap t(i),t(j)  |
         ST     R0,0(R3)             t(j)=w       +                |
         B      FOREVER            end do forever  ----------------+
LEAVE    EQU    *
         LR     R9,R8              j=i
         BCTR   R9,0               j=i-1
         LR     R1,R9              j
         SLA    R1,2               ~
         LA     R3,T-4(R1)         @t(j)
         L      R2,0(R3)           t(j)
         LR     R1,R10             l
         SLA    R1,2               ~
         ST     R2,T-4(R1)         t(l)=t(j)
         ST     R7,0(R3)           t(j)=p
         LA     R6,1(R6)           k=k+1
         LR     R1,R6              k
         SLA    R1,2               ~
         LA     R4,A-4(R1)         r4=@a(k)
         LA     R5,B-4(R1)         r5=@b(k)
         IF     C,R8,LE,Y          if i<=y           ----+
         ST     R8,0(R4)             a(k)=i              |
         L      R2,X                 x                   |
         SR     R2,R8                -i                  |
         LA     R2,1(R2)             +1                  |
         ST     R2,0(R5)             b(k)=x-i+1          |
         LA     R6,1(R6)             k=k+1               |
         ST     R10,4(R4)            a(k)=l              |
         LR     R2,R9                j                   |
         SR     R2,R10               -l                  |
         ST     R2,4(R5)             b(k)=j-l            |
         ELSE   ,                  else                  |
         ST     R10,4(R4)            a(k)=l              |
         LR     R2,R9                j                   |
         SR     R2,R10               -l                  |
         ST     R2,0(R5)             b(k)=j-l            |
         LA     R6,1(R6)             k=k+1               |
         ST     R8,4(R4)             a(k)=i              |
         L      R2,X                 x                   |
         SR     R2,R8                -i                  |
         LA     R2,1(R2)             +1                  |
         ST     R2,4(R5)             b(k)=x-i+1          |
         ENDIF  ,                  end if            ----+
ITERATE  EQU    *                  
       ENDDO    ,                  end while  =====================
*        ***    *********          print sorted table
         LA     R3,PG              ibuffer
         LA     R4,T               @t(i)
       DO WHILE=(C,R4,LE,=A(TEND)) do i=1 to hbound(t)
         L      R2,0(R4)             t(i)
         XDECO  R2,XD                edit t(i)
         MVC    0(4,R3),XD+8         put in buffer
         LA     R3,4(R3)             ibuffer=ibuffer+1
         LA     R4,4(R4)             i=i+1
       ENDDO    ,                  end do
         XPRNT  PG,80              print buffer
         L      R13,4(0,R13)       epilog 
         LM     R14,R12,12(R13)    "
         XR     R15,R15            "
         BR     R14                exit
T        DC     F'10',F'9',F'9',F'6',F'7',F'16',F'1',F'16',F'17',F'15'
         DC     F'1',F'9',F'18',F'16',F'8',F'20',F'18',F'2',F'19',F'8'
TEND     DS     0F
NN       EQU    (TEND-T)/4)
A        DS     (NN)F              same size as T
B        DS     (NN)F              same size as T
X        DS     F
Y        DS     F
PG       DS     CL80
XD       DS     CL12
         YREGS 
         END    QUICKSOR
```

**Output:**

```
   1   1   2   6   7   8   8   9   9   9  10  15  16  16  16  17  18  18  19  20
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program quickSort64.s  */
 
/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeConstantesARM64.inc"

/*********************************/
/* Initialized data              */
/*********************************/
.data
szMessSortOk:       .asciz "Table sorted.\n"
szMessSortNok:      .asciz "Table not sorted !!!!!.\n"
sMessResult:        .asciz "Value  : @ \n"
szCarriageReturn:   .asciz "\n"
 
.align 4
TableNumber:      .quad   1,3,6,2,5,9,10,8,4,7,11
#TableNumber:     .quad   10,9,8,7,6,-5,4,3,2,1
                 .equ NBELEMENTS, (. - TableNumber) / 8 
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss
sZoneConv:       .skip 24
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                                              // entry of program 
    ldr x0,qAdrTableNumber                         // address number table
    mov x1,0                                       // first element
    mov x2,NBELEMENTS                              // number of élements 
    bl quickSort
    ldr x0,qAdrTableNumber                         // address number table
    bl displayTable
 
    ldr x0,qAdrTableNumber                         // address number table
    mov x1,NBELEMENTS                              // number of élements 
    bl isSorted                                    // control sort
    cmp x0,1                                       // sorted ?
    beq 1f                                    
    ldr x0,qAdrszMessSortNok                       // no !! error sort
    bl affichageMess
    b 100f
1:                                                 // yes
    ldr x0,qAdrszMessSortOk
    bl affichageMess
100:                                               // standard end of the program 
    mov x0,0                                       // return code
    mov x8,EXIT                                    // request to exit program
    svc 0                                          // perform the system call
 
qAdrsZoneConv:            .quad sZoneConv
qAdrszCarriageReturn:     .quad szCarriageReturn
qAdrsMessResult:          .quad sMessResult
qAdrTableNumber:          .quad TableNumber
qAdrszMessSortOk:         .quad szMessSortOk
qAdrszMessSortNok:        .quad szMessSortNok
/******************************************************************/
/*     control sorted table                                   */ 
/******************************************************************/
/* x0 contains the address of table */
/* x1 contains the number of elements  > 0  */
/* x0 return 0  if not sorted   1  if sorted */
isSorted:
    stp x2,lr,[sp,-16]!             // save  registers
    stp x3,x4,[sp,-16]!             // save  registers
    mov x2,0
    ldr x4,[x0,x2,lsl 3]
1:
    add x2,x2,1
    cmp x2,x1
    bge 99f
    ldr x3,[x0,x2, lsl 3]
    cmp x3,x4
    blt 98f
    mov x4,x3
    b 1b
98:
    mov x0,0                       // not sorted
    b 100f
99:
    mov x0,1                       // sorted
100:
    ldp x3,x4,[sp],16              // restaur  2 registers
    ldp x2,lr,[sp],16              // restaur  2 registers
    ret                            // return to address lr x30
/***************************************************/
/*   Appel récursif Tri Rapide quicksort           */
/***************************************************/
/* x0 contains the address of table */
/* x1 contains index of first item  */
/* x2 contains the number of elements  > 0  */
quickSort:
    stp x2,lr,[sp,-16]!             // save  registers
    stp x3,x4,[sp,-16]!             // save  registers
    str x5,   [sp,-16]!             // save  registers
    sub x2,x2,1                     // last item index
    cmp x1,x2                       // first > last ? 
    bge 100f                        // yes -> end
    mov x4,x0                       // save x0
    mov x5,x2                       // save x2
    bl partition1                   // cutting into 2 parts
    mov x2,x0                       // index partition
    mov x0,x4                       // table address
    bl quickSort                    // sort lower part
    add x1,x2,1                     // index begin = index partition + 1
    add x2,x5,1                     // number of elements
    bl quickSort                    // sort higter part
 
 100:                               // end function
    ldr x5,   [sp],16               // restaur  1 register
    ldp x3,x4,[sp],16               // restaur  2 registers
    ldp x2,lr,[sp],16               // restaur  2 registers
    ret                             // return to address lr x30
 
/******************************************************************/
/*      Partition table elements                                */ 
/******************************************************************/
/* x0 contains the address of table */
/* x1 contains index of first item  */
/* x2 contains index of last item   */
partition1:
    stp x1,lr,[sp,-16]!             // save  registers
    stp x2,x3,[sp,-16]!             // save  registers
    stp x4,x5,[sp,-16]!             // save  registers
    stp x6,x7,[sp,-16]!             // save  registers
    ldr x3,[x0,x2,lsl 3]            // load value last index
    mov x4,x1                       // init with first index
    mov x5,x1                       // init with first index
1:                                  // begin loop
    ldr x6,[x0,x5,lsl 3]            // load value
    cmp x6,x3                       // compare value
    bge 2f
    ldr x7,[x0,x4,lsl 3]            // if < swap value table
    str x6,[x0,x4,lsl 3]
    str x7,[x0,x5,lsl 3]
    add x4,x4,1                     // and increment index 1
2:
    add x5,x5,1                     // increment index 2
    cmp x5,x2                       // end ?
    blt 1b                          // no loop
    ldr x7,[x0,x4,lsl 3]            // swap value
    str x3,[x0,x4,lsl 3]
    str x7,[x0,x2,lsl 3]
    mov x0,x4                       // return index partition
100:
    ldp x6,x7,[sp],16               // restaur  2 registers
    ldp x4,x5,[sp],16               // restaur  2 registers
    ldp x2,x3,[sp],16               // restaur  2 registers
    ldp x1,lr,[sp],16               // restaur  2 registers
    ret                             // return to address lr x30
 
/******************************************************************/
/*      Display table elements                                */ 
/******************************************************************/
/* x0 contains the address of table */
displayTable:
    stp x1,lr,[sp,-16]!              // save  registers
    stp x2,x3,[sp,-16]!              // save  registers
    mov x2,x0                        // table address
    mov x3,0
1:                                   // loop display table
    ldr x0,[x2,x3,lsl 3]
    ldr x1,qAdrsZoneConv
    bl conversion10S                  // décimal conversion
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc            // insert result at // character
    bl affichageMess                 // display message
    add x3,x3,1
    cmp x3,NBELEMENTS - 1
    ble 1b
    ldr x0,qAdrszCarriageReturn
    bl affichageMess
    mov x0,x2
100:
    ldp x2,x3,[sp],16               // restaur  2 registers
    ldp x1,lr,[sp],16               // restaur  2 registers
    ret                             // return to address lr x30
/********************************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```

```
Value  : +1
Value  : +2
Value  : +3
Value  : +4
Value  : +5
Value  : +6
Value  : +7
Value  : +8
Value  : +9
Value  : +10
Value  : +11

Table sorted.
```


## ABAP

This works for ABAP Version 7.40 and above

```mw
report z_quicksort.

data(numbers) = value int4_table( ( 4 ) ( 65 ) ( 2 ) ( -31 ) ( 0 ) ( 99 ) ( 2 ) ( 83 ) ( 782 ) ( 1 ) ).
perform quicksort changing numbers.

write `[`.
loop at numbers assigning field-symbol(<numbers>).
  write <numbers>.
endloop.
write `]`.

form quicksort changing numbers type int4_table.
  data(less) = value int4_table( ).
  data(equal) = value int4_table( ).
  data(greater) = value int4_table( ).

  if lines( numbers ) > 1.
    data(pivot) = numbers[ lines( numbers ) / 2 ].

    loop at numbers assigning field-symbol(<number>).
      if <number> < pivot.
        append <number> to less.
      elseif <number> = pivot.
        append <number> to equal.
      elseif <number> > pivot.
        append <number> to greater.
      endif.
    endloop.

    perform quicksort changing less.
    perform quicksort changing greater.

    clear numbers.
    append lines of less to numbers.
    append lines of equal to numbers.
    append lines of greater to numbers.
  endif.
endform.
```

**Output:**

```
[        31-         0          1          2          2          4         65         83         99        782  ]
```


## ACL2

```mw
(defun partition (p xs)
   (if (endp xs)
       (mv nil nil)
       (mv-let (less more)
               (partition p (rest xs))
          (if (< (first xs) p)
              (mv (cons (first xs) less) more)
              (mv less (cons (first xs) more))))))

(defun qsort (xs)
   (if (endp xs)
       nil
       (mv-let (less more)
               (partition (first xs) (rest xs))
          (append (qsort less)
                  (list (first xs))
                  (qsort more)))))
```

Usage:

```mw
> (qsort '(8 6 7 5 3 0 9))
(0 3 5 6 7 8 9)
```


## Action!

Action! language does not support recursion. Therefore an iterative approach with a stack has been proposed.

```mw
DEFINE MAX_COUNT="100"
INT ARRAY stack(MAX_COUNT)
INT stackSize

PROC PrintArray(INT ARRAY a INT size)
  INT i

  Put('[)
  FOR i=0 TO size-1
  DO
    IF i>0 THEN Put(' ) FI
    PrintI(a(i))
  OD
  Put(']) PutE()
RETURN

PROC InitStack()
  stackSize=0
RETURN

BYTE FUNC IsEmpty()
  IF stackSize=0 THEN
    RETURN (1)
  FI
RETURN (0)

PROC Push(INT low,high)
  stack(stackSize)=low  stackSize==+1
  stack(stackSize)=high stackSize==+1
RETURN

PROC Pop(INT POINTER low,high)
  stackSize==-1 high^=stack(stackSize)
  stackSize==-1 low^=stack(stackSize)
RETURN

INT FUNC Partition(INT ARRAY a INT low,high)
  INT part,v,i,tmp

  v=a(high)
  part=low-1

  FOR i=low TO high-1
  DO
    IF a(i)<=v THEN
      part==+1
      tmp=a(part) a(part)=a(i) a(i)=tmp
    FI
  OD

  part==+1
  tmp=a(part) a(part)=a(high) a(high)=tmp
RETURN (part)

PROC QuickSort(INT ARRAY a INT size)
  INT low,high,part

  InitStack()
  Push(0,size-1)
  WHILE IsEmpty()=0
  DO
    Pop(@low,@high)
    part=Partition(a,low,high)
    IF part-1>low THEN
      Push(low,part-1)      
    FI
    IF part+1<high THEN
      Push(part+1,high)
    FI
  OD
RETURN

PROC Test(INT ARRAY a INT size)
  PrintE("Array before sort:")
  PrintArray(a,size)
  QuickSort(a,size)
  PrintE("Array after sort:")
  PrintArray(a,size)
  PutE()
RETURN

PROC Main()
  INT ARRAY
    a(10)=[1 4 65535 0 3 7 4 8 20 65530],
    b(21)=[10 9 8 7 6 5 4 3 2 1 0
      65535 65534 65533 65532 65531
      65530 65529 65528 65527 65526],
    c(8)=[101 102 103 104 105 106 107 108],
    d(12)=[1 65535 1 65535 1 65535 1
      65535 1 65535 1 65535]
  
  Test(a,10)
  Test(b,21)
  Test(c,8)
  Test(d,12)
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
Array before sort:
[1 4 -1 0 3 7 4 8 20 -6]
Array after sort:
[-6 -1 0 1 3 4 4 7 8 20]

Array before sort:
[10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10]
Array after sort:
[-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10]

Array before sort:
[101 102 103 104 105 106 107 108]
Array after sort:
[101 102 103 104 105 106 107 108]

Array before sort:
[1 -1 1 -1 1 -1 1 -1 1 -1 1 -1]
Array after sort:
[-1 -1 -1 -1 -1 -1 1 1 1 1 1 1]
```


## ActionScript

Works with

:

ActionScript

version 3

The functional programming way

```mw
function quickSort (array:Array):Array
{
    if (array.length <= 1)
        return array;

    var pivot:Number = array[Math.round(array.length / 2)];

    return quickSort(array.filter(function (x:Number, index:int, array:Array):Boolean { return x <  pivot; })).concat(
            array.filter(function (x:Number, index:int, array:Array):Boolean { return x == pivot; })).concat(
        quickSort(array.filter(function (x:Number, index:int, array:Array):Boolean { return x > pivot; })));
}
```

The faster way

```mw
function quickSort (array:Array):Array
{
    if (array.length <= 1)
        return array;

    var pivot:Number = array[Math.round(array.length / 2)];

    var less:Array = [];
    var equal:Array = [];
    var greater:Array = [];

    for each (var x:Number in array) {
        if (x < pivot)
            less.push(x);
        if (x == pivot)
            equal.push(x);
        if (x > pivot)
            greater.push(x);
    }

    return quickSort(less).concat(
            equal).concat(
            quickSort(greater));
}
```


## Ada

This example is implemented as a generic procedure.

The procedure specification is:

```mw
-----------------------------------------------------------------------
-- Generic Quick_Sort procedure
-----------------------------------------------------------------------
generic
   type Element is private;
   type Index is (<>);
   type Element_Array is array(Index range <>) of Element;
   with function "<" (Left, Right : Element) return Boolean is <>;
procedure Quick_Sort(A : in out Element_Array);
```

The procedure body deals with any discrete index type, either an integer type or an enumerated type.

```mw
-----------------------------------------------------------------------
-- Generic Quick_Sort procedure
----------------------------------------------------------------------- 

procedure Quick_Sort (A : in out Element_Array) is
   
   procedure Swap(Left, Right : Index) is
      Temp : Element := A (Left);
   begin
      A (Left) := A (Right);
      A (Right) := Temp;
   end Swap;
  
begin
   if A'Length > 1 then
   declare
      Pivot_Value : Element := A (A'First);
      Right       : Index := A'Last;
      Left        : Index := A'First;
   begin
       loop
          while Left < Right and not (Pivot_Value < A (Left)) loop
             Left := Index'Succ (Left);
          end loop;
          while Pivot_Value < A (Right) loop
             Right := Index'Pred (Right);
          end loop;
          exit when Right <= Left;
          Swap (Left, Right);
          Left := Index'Succ (Left);
          Right := Index'Pred (Right);
       end loop;
       if Right = A'Last then
          Right := Index'Pred (Right);
          Swap (A'First, A'Last);
       end if;
       if Left = A'First then
          Left := Index'Succ (Left);
       end if;
       Quick_Sort (A (A'First .. Right));
       Quick_Sort (A (Left .. A'Last));
   end;
   end if;
end Quick_Sort;
```

An example of how this procedure may be used is:

```mw
with Ada.Text_Io;
with Ada.Float_Text_IO; use Ada.Float_Text_IO; 
with Quick_Sort;

procedure Sort_Test is
   type Days is (Mon, Tue, Wed, Thu, Fri, Sat, Sun);
   type Sales is array (Days range <>) of Float;
   procedure Sort_Days is new Quick_Sort(Float, Days, Sales);
   
   procedure Print (Item : Sales) is
   begin
      for I in Item'range loop
         Put(Item => Item(I), Fore => 5, Aft => 2, Exp => 0);
      end loop;
   end Print;
  
   Weekly_Sales : Sales := (Mon => 300.0, 
      Tue => 700.0, 
      Wed => 800.0, 
      Thu => 500.0, 
      Fri => 200.0, 
      Sat => 100.0, 
      Sun => 900.0);
  
begin
  
   Print(Weekly_Sales);
   Ada.Text_Io.New_Line(2);
   Sort_Days(Weekly_Sales);
   Print(Weekly_Sales);
  
end Sort_Test;
```


## ALGOL 68

```mw
#--- Swap function ---#
PROC swap = (REF []INT array, INT first, INT second) VOID:
(
    INT temp := array[first];
    array[first] := array[second];
    array[second]:= temp
);

#--- Quick sort 3 arg function ---#
PROC quick = (REF [] INT array, INT first, INT last) VOID:
(
    INT smaller := first + 1,  
        larger  := last,
        pivot   := array[first];
  
    WHILE smaller <= larger DO
        WHILE array[smaller] < pivot   AND   smaller < last DO   
            smaller +:= 1        
        OD;
        WHILE array[larger]  > pivot   AND   larger > first DO   
            larger  -:= 1       
        OD; 
        IF smaller < larger THEN 
            swap(array, smaller, larger); 
            smaller +:= 1;
            larger  -:= 1
        ELSE
            smaller +:= 1
        FI
    OD;
    
    swap(array, first, larger);    

    IF first < larger-1 THEN
        quick(array, first, larger-1)  
    FI;
    IF last > larger +1 THEN
        quick(array, larger+1, last)   
    FI
);

#--- Quick sort 1 arg function ---#
PROC quicksort = (REF []INT array) VOID:
(
  IF UPB array > 1 THEN
    quick(array, 1, UPB array) 
  FI
);

#***************************************************************#
main:
(
    [10]INT a; 
    FOR i FROM 1 TO UPB a DO 
        a[i] := ROUND(random*1000)
    OD;                             

    print(("Before:", a));
    quicksort(a);
    print((newline, newline));
    print(("After: ", a))
)
```

**Output:**

```
Before:        +73       +921       +179       +961        +50       +324        +82       +178       +243       +458
                                                                                                                     
After:         +50        +73        +82       +178       +179       +243       +324       +458       +921       +961
```


## ALGOL W

```mw
% Quicksorts in-place the array of integers v, from lb to ub %
procedure quicksort ( integer array v( * )
                    ; integer value lb, ub
                    ) ;
if ub > lb then begin
    % more than one element, so must sort %
    integer left, right, pivot;
    left   := lb;
    right  := ub;
    % choosing the middle element of the array as the pivot %
    pivot  := v( left + ( ( right + 1 ) - left ) div 2 );
    while begin
        while left  <= ub and v( left  ) < pivot do left  := left  + 1;
        while right >= lb and v( right ) > pivot do right := right - 1;
        left <= right
    end do begin
        integer swap;
        swap       := v( left  );
        v( left  ) := v( right );
        v( right ) := swap;
        left       := left  + 1;
        right      := right - 1
    end while_left_le_right ;
    quicksort( v, lb,   right );
    quicksort( v, left, ub    )
end quicksort ;
```


## APL

Works with

:

Dyalog APL

Translation of

:

J

```mw
      qsort ← {1≥≢∪⍵:⍵ ⋄ p←⍵[?≢⍵] ⋄ (∇(⍵≤p)/⍵) , ∇(⍵>p)/⍵}
      qsort 31 4 1 5 9 2 6 5 3 5 8
1 2 3 4 5 5 5 6 8 9 31
```

Of course, in real APL applications, one would use ⍋ (Grade Up) to sort (which will pick a sorting algorithm suited to the argument):

```mw
      sort ← {⍵[⍋⍵]}
      sort 31 4 1 5 9 2 6 5 3 5 8
1 2 3 4 5 5 5 6 8 9 31
```


## AppleScript

### Functional

Emphasising clarity and simplicity more than run-time performance. (Practical scripts will often delegate sorting to the OS X shell, or, since OS X Yosemite, to Foundation classes through the ObjC interface).

Translation of

:

JavaScript

(Functional ES5 version)

```mw
-- quickSort :: (Ord a) => [a] -> [a]
on quickSort(xs)
    if length of xs > 1 then
        set {h, t} to uncons(xs)
        
        -- lessOrEqual :: a -> Bool
        script lessOrEqual
            on |λ|(x)
                x ≤ h
            end |λ|
        end script
        
        set {less, more} to partition(lessOrEqual, t)
        
        quickSort(less) & h & quickSort(more)
    else
        xs
    end if
end quickSort

-- TEST -----------------------------------------------------------------------
on run
    
    quickSort([11.8, 14.1, 21.3, 8.5, 16.7, 5.7])
    
    --> {5.7, 8.5, 11.8, 14.1, 16.7, 21.3}
    
end run

-- GENERIC FUNCTIONS ----------------------------------------------------------

-- partition :: predicate -> List -> (Matches, nonMatches)
-- partition :: (a -> Bool) -> [a] -> ([a], [a])
on partition(f, xs)
    tell mReturn(f)
        set lst to {{}, {}}
        repeat with x in xs
            set v to contents of x
            set end of item ((|λ|(v) as integer) + 1) of lst to v
        end repeat
        return {item 2 of lst, item 1 of lst}
    end tell
end partition

-- uncons :: [a] -> Maybe (a, [a])
on uncons(xs)
    if length of xs > 0 then
        {item 1 of xs, rest of xs}
    else
        missing value
    end if
end uncons

-- Lift 2nd class handler function into 1st class script wrapper 
-- mReturn :: Handler -> Script
on mReturn(f)
    if class of f is script then
        f
    else
        script
            property |λ| : f
        end script
    end if
end mReturn
```

**Output:**

```mw
{5.7, 8.5, 11.8, 14.1, 16.7, 21.3}
```

### Straightforward

Emphasising clarity, quick sorting, *and* correct AppleScript:

```mw
-- In-place Quicksort (basic algorithm).
-- Algorithm: S.A.R. (Tony) Hoare, 1960.
on quicksort(theList, l, r) -- Sort items l thru r of theList.
    set listLength to (count theList)
    if (listLength < 2) then return
    -- Convert negative and/or transposed range indices.
    if (l < 0) then set l to listLength + l + 1
    if (r < 0) then set r to listLength + r + 1
    if (l > r) then set {l, r} to {r, l}
    
    -- Script object containing the list as a property (to allow faster references to its items)
    -- and the recursive subhandler.
    script o
        property lst : theList
        
        on qsrt(l, r)
            set pivot to my lst's item ((l + r) div 2)
            set i to l
            set j to r
            repeat until (i > j)
                set lv to my lst's item i
                repeat while (pivot > lv)
                    set i to i + 1
                    set lv to my lst's item i
                end repeat
                
                set rv to my lst's item j
                repeat while (rv > pivot)
                    set j to j - 1
                    set rv to my lst's item j
                end repeat
                
                if (j > i) then
                    set my lst's item i to rv
                    set my lst's item j to lv
                else if (i > j) then
                    exit repeat
                end if
                
                set i to i + 1
                set j to j - 1
            end repeat
            
            if (j > l) then qsrt(l, j)
            if (i < r) then qsrt(i, r)
        end qsrt
    end script
    
    tell o to qsrt(l, r)
    
    return -- nothing.
end quicksort
property sort : quicksort

-- Demo:
local aList
set aList to {28, 9, 95, 22, 67, 55, 20, 41, 60, 53, 100, 72, 19, 67, 14, 42, 29, 20, 74, 39}
sort(aList, 1, -1) -- Sort items 1 thru -1 of aList.
return aList
```

**Output:**

```mw
{9, 14, 19, 20, 20, 22, 28, 29, 39, 41, 42, 53, 55, 60, 67, 67, 72, 74, 95, 100}
```


## Arc

```mw
(def qs (seq)
  (if (empty seq) nil
      (let pivot (car seq)
   (join (qs (keep [< _ pivot] (cdr seq)))
         (list pivot)
         (qs (keep [>= _ pivot] (cdr seq)))))))
```


## ArkScript

Works with

:

ArkScript

version 4.0.0

```mw
(import std.List :filter)

(let quicksort (fun (array) {
  (if (empty? array)
    # if the given list is empty, return it
    []
    # otherwise, sort it
    {
      # the pivot will be the first element
      (let pivot (head array))

      # call quicksort on a smaller array containing all the elements less than the pivot
      (mut less (quicksort (filter (tail array) (fun (e) (< e pivot)))))

      # and after that, call quicksort on a smaller array containing all the elements greater or equal to the pivot
      (let more (quicksort (filter (tail array) (fun (e) (>= e pivot)))))

      (concat! less [pivot] more)
      # return a concatenation of arrays
      less }) }))

# an unsorted list to sort
(let a [3 6 1 5 1 65 324 765 1 6 3 0 6 9 6 5 3 2 5 6 7 64 645 7 345 432 432 4 324 23])

(assert (= (quicksort a) [0 1 1 1 2 3 3 3 4 5 5 5 6 6 6 6 6 7 7 9 23 64 65 324 324 345 432 432 645 765]) "(quicksort a) is sorted")
```
