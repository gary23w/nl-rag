---
title: "Sorting algorithms/Quicksort (part 2/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/8
---

## ARM Assembly

Works with

:

as

version Raspberry Pi

```mw
/* ARM assembly Raspberry PI  */
/*  program quickSort.s   */
/* look pseudo code in wikipedia  quicksort */

/************************************/
/* Constantes                       */
/************************************/
.equ STDOUT, 1     @ Linux output console
.equ EXIT,   1     @ Linux syscall
.equ WRITE,  4     @ Linux syscall
/*********************************/
/* Initialized data              */
/*********************************/
.data
szMessSortOk:       .asciz "Table sorted.\n"
szMessSortNok:      .asciz "Table not sorted !!!!!.\n"
sMessResult:        .ascii "Value  : "
sMessValeur:        .fill 11, 1, ' '            @ size => 11
szCarriageReturn:   .asciz "\n"
 
.align 4
iGraine:  .int 123456
.equ NBELEMENTS,      10
#TableNumber:       .int   9,5,6,1,2,3,10,8,4,7
#TableNumber:       .int   1,3,5,2,4,6,10,8,4,7
#TableNumber:       .int   1,3,5,2,4,6,10,8,4,7
#TableNumber:       .int   1,2,3,4,5,6,10,8,4,7
TableNumber:        .int   10,9,8,7,6,5,4,3,2,1
#TableNumber:       .int   13,12,11,10,9,8,7,6,5,4,3,2,1
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                                              @ entry of program 
 
1:
    ldr r0,iAdrTableNumber                         @ address number table

    mov r1,#0                                      @ indice first item
    mov r2,#NBELEMENTS                             @ number of élements 
    bl triRapide                                   @ call quicksort
    ldr r0,iAdrTableNumber                         @ address number table
    bl displayTable
 
    ldr r0,iAdrTableNumber                         @ address number table
    mov r1,#NBELEMENTS                             @ number of élements 
    bl isSorted                                    @ control sort
    cmp r0,#1                                      @ sorted ?
    beq 2f                                    
    ldr r0,iAdrszMessSortNok                       @ no !! error sort
    bl affichageMess
    b 100f
2:                                                 @ yes
    ldr r0,iAdrszMessSortOk
    bl affichageMess
100:                                               @ standard end of the program 
    mov r0, #0                                     @ return code
    mov r7, #EXIT                                  @ request to exit program
    svc #0                                         @ perform the system call
 
iAdrsMessValeur:          .int sMessValeur
iAdrszCarriageReturn:    .int szCarriageReturn
iAdrsMessResult:          .int sMessResult
iAdrTableNumber:          .int TableNumber
iAdrszMessSortOk:         .int szMessSortOk
iAdrszMessSortNok:        .int szMessSortNok
/******************************************************************/
/*     control sorted table                                   */ 
/******************************************************************/
/* r0 contains the address of table */
/* r1 contains the number of elements  > 0  */
/* r0 return 0  if not sorted   1  if sorted */
isSorted:
    push {r2-r4,lr}                                    @ save registers
    mov r2,#0
    ldr r4,[r0,r2,lsl #2]
1:
    add r2,#1
    cmp r2,r1
    movge r0,#1
    bge 100f
    ldr r3,[r0,r2, lsl #2]
    cmp r3,r4
    movlt r0,#0
    blt 100f
    mov r4,r3
    b 1b
100:
    pop {r2-r4,lr}
    bx lr                                              @ return 

/***************************************************/
/*   Appel récursif Tri Rapide quicksort           */
/***************************************************/
/* r0 contains the address of table */
/* r1 contains index of first item  */
/* r2 contains the number of elements  > 0  */
triRapide:
    push {r2-r5,lr}                                   @ save registers
    sub r2,#1                                         @ last item index
    cmp r1,r2                                         @ first > last ? 
    bge 100f                                          @ yes -> end
    mov r4,r0                                         @ save r0
    mov r5,r2                                         @ save r2
    bl partition1                                     @ cutting into 2 parts
    mov r2,r0                                         @ index partition
    mov r0,r4                                         @ table address
    bl triRapide                                      @ sort lower part
    add r1,r2,#1                                      @ index begin = index partition + 1
    add r2,r5,#1                                      @ number of elements
    bl triRapide                                      @ sort higter part
   
 100:                                                 @ end function
    pop {r2-r5,lr}                                    @ restaur  registers 
    bx lr                                             @ return

/******************************************************************/
/*      Partition table elements                                */ 
/******************************************************************/
/* r0 contains the address of table */
/* r1 contains index of first item  */
/* r2 contains index of last item   */

partition1:
    push {r1-r7,lr}                                    @ save registers
    ldr r3,[r0,r2,lsl #2]                              @ load value last index
    mov r4,r1                                          @ init with first index
    mov r5,r1                                          @ init with first index
1:                                                     @ begin loop
    ldr r6,[r0,r5,lsl #2]                              @ load value
    cmp r6,r3                                          @ compare value
    ldrlt r7,[r0,r4,lsl #2]                            @ if < swap value table
    strlt r6,[r0,r4,lsl #2]
    strlt r7,[r0,r5,lsl #2]
    addlt r4,#1                                        @ and increment index 1
    add    r5,#1                                       @ increment index 2
    cmp r5,r2                                          @ end ?
    blt 1b                                             @ no loop
    ldr r7,[r0,r4,lsl #2]                              @ swap value
    str r3,[r0,r4,lsl #2]
    str r7,[r0,r2,lsl #2]
    mov r0,r4                                          @ return index partition
100:
    pop {r1-r7,lr}
    bx lr

/******************************************************************/
/*      Display table elements                                */ 
/******************************************************************/
/* r0 contains the address of table */
displayTable:
    push {r0-r3,lr}                                    @ save registers
    mov r2,r0                                          @ table address
    mov r3,#0
1:                                                     @ loop display table
    ldr r0,[r2,r3,lsl #2]
    ldr r1,iAdrsMessValeur                             @ display value
    bl conversion10                                    @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                                   @ display message
    add r3,#1
    cmp r3,#NBELEMENTS - 1
    ble 1b
    ldr r0,iAdrszCarriageReturn
    bl affichageMess
100:
    pop {r0-r3,lr}
    bx lr
/******************************************************************/
/*     display text with size calculation                         */ 
/******************************************************************/
/* r0 contains the address of the message */
affichageMess:
    push {r0,r1,r2,r7,lr}                          @ save  registres
    mov r2,#0                                      @ counter length 
1:                                                 @ loop length calculation 
    ldrb r1,[r0,r2]                                @ read octet start position + index 
    cmp r1,#0                                      @ if 0 its over 
    addne r2,r2,#1                                 @ else add 1 in the length 
    bne 1b                                         @ and loop 
                                                   @ so here r2 contains the length of the message 
    mov r1,r0                                      @ address message in r1 
    mov r0,#STDOUT                                 @ code to write to the standard output Linux 
    mov r7, #WRITE                                 @ code call system "write" 
    svc #0                                         @ call systeme 
    pop {r0,r1,r2,r7,lr}                           @ restaur des  2 registres */ 
    bx lr                                          @ return  
/******************************************************************/
/*     Converting a register to a decimal unsigned                */ 
/******************************************************************/
/* r0 contains value and r1 address area   */
/* r0 return size of result (no zero final in area) */
/* area size => 11 bytes          */
.equ LGZONECAL,   10
conversion10:
    push {r1-r4,lr}                                 @ save registers 
    mov r3,r1
    mov r2,#LGZONECAL
 
1:                                             @ start loop
    bl divisionpar10U                               @ unsigned  r0 <- dividende. quotient ->r0 reste -> r1
    add r1,#48                                      @ digit
    strb r1,[r3,r2]                                 @ store digit on area
    cmp r0,#0                                       @ stop if quotient = 0 
    subne r2,#1                                     @ else previous position
    bne 1b                                      @ and loop
                                                    @ and move digit from left of area
    mov r4,#0
2:
    ldrb r1,[r3,r2]
    strb r1,[r3,r4]
    add r2,#1
    add r4,#1
    cmp r2,#LGZONECAL
    ble 2b
                                                      @ and move spaces in end on area
    mov r0,r4                                         @ result length 
    mov r1,#' '                                       @ space
3:
    strb r1,[r3,r4]                                   @ store space in area
    add r4,#1                                         @ next position
    cmp r4,#LGZONECAL
    ble 3b                                            @ loop if r4 <= area size
 
100:
    pop {r1-r4,lr}                                    @ restaur registres 
    bx lr                                             @return
 
/***************************************************/
/*   division par 10   unsigned                    */
/***************************************************/
/* r0 dividende   */
/* r0 quotient */ 
/* r1 remainder  */
divisionpar10U:
    push {r2,r3,r4, lr}
    mov r4,r0                                          @ save value
    //mov r3,#0xCCCD                                   @ r3 <- magic_number lower  raspberry 3
    //movt r3,#0xCCCC                                  @ r3 <- magic_number higter raspberry 3
    ldr r3,iMagicNumber                                @ r3 <- magic_number    raspberry 1 2
    umull r1, r2, r3, r0                               @ r1<- Lower32Bits(r1*r0) r2<- Upper32Bits(r1*r0) 
    mov r0, r2, LSR #3                                 @ r2 <- r2 >> shift 3
    add r2,r0,r0, lsl #2                               @ r2 <- r0 * 5 
    sub r1,r4,r2, lsl #1                               @ r1 <- r4 - (r2 * 2)  = r4 - (r0 * 10)
    pop {r2,r3,r4,lr}
    bx lr                                              @ leave function 
iMagicNumber:     .int 0xCCCCCCCD
```


## Arturo

```mw
quickSort: function [items][
   if 2 > size items -> return items
   
   pivot: first items
   left:  select slice items 1 (size items)-1 'x -> x < pivot
   right: select slice items 1 (size items)-1 'x -> x >= pivot

   ((quickSort left) ++ pivot) ++ quickSort right
]

print quickSort [3 1 2 8 5 7 9 4 6]
```

**Output:**

```
1 2 3 4 5 6 7 8 9
```


## ATS

### A quicksort working on non-linear linked lists

```mw
(*------------------------------------------------------------------*)
(* Quicksort in ATS2, for non-linear lists.                         *)
(*------------------------------------------------------------------*)

#include "share/atspre_staload.hats"

#define NIL list_nil ()
#define ::  list_cons

(*------------------------------------------------------------------*)

(* A simple quicksort working on "garbage-collected" linked lists,
   with first element as pivot. This is meant as a demonstration, not
   as a superior sort algorithm.

   It is based on the "not-in-place" task pseudocode. *)

datatype comparison_result =
| first_is_less_than_second of ()
| first_is_equal_to_second of ()
| first_is_greater_than_second of ()

extern fun {a : t@ype}
list_quicksort$comparison (x : a, y : a) :<> comparison_result

extern fun {a : t@ype}
list_quicksort {n   : int}
               (lst : list (a, n)) :<> list (a, n)

(* -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - *)

implement {a}
list_quicksort {n} (lst) =
  let
    fun
    partition {n     : nat}
              .<n>.             (* Proof of termination. *)
              (lst   : list (a, n),
               pivot : a)
        :<> [n1, n2, n3 : int | n1 + n2 + n3 == n]
            @(list (a, n1), list (a, n2), list (a, n3)) =
      (* This implementation is *not* tail recursive. I may get a
         scolding for using ATS to risk stack overflow! However, I
         need more practice writing non-tail routines. :) Also, a lot
         of programmers in other languages would do it this
         way--especially if the lists are evaluated lazily. *)
      case+ lst of
      | NIL => @(NIL, NIL, NIL)
      | head :: tail =>
        let
          val @(lt, eq, gt) = partition (tail, pivot)
          prval () = lemma_list_param lt
          prval () = lemma_list_param eq
          prval () = lemma_list_param gt
        in
          case+ list_quicksort$comparison<a> (head, pivot) of
          | first_is_less_than_second ()    => @(head :: lt, eq, gt)
          | first_is_equal_to_second ()     => @(lt, head :: eq, gt)
          | first_is_greater_than_second () => @(lt, eq, head :: gt)
        end

    fun
    quicksort {n   : nat}
              .<n>.             (* Proof of termination. *)
              (lst : list (a, n))
        :<> list (a, n) =
      case+ lst of
      | NIL => lst
      | _ :: NIL => lst
      | head :: tail =>
        let
          (* We are careful here to run "partition" on "tail" rather
             than "lst", so the termination metric will be provably
             decreasing. (Really the compiler *forces* us to take such
             care, or else to change :<> to :<!ntm>) *)
          val pivot = head
          prval () = lemma_list_param tail
          val @(lt, eq, gt) = partition {n - 1} (tail, pivot)
          prval () = lemma_list_param lt
          prval () = lemma_list_param eq
          prval () = lemma_list_param gt
          val eq = pivot :: eq
          and lt = quicksort lt
          and gt = quicksort gt
        in
          lt + (eq + gt)
        end

    prval () = lemma_list_param lst
  in
    quicksort {n} lst
  end

(*------------------------------------------------------------------*)

val example_strings =
  $list ("choose", "any", "element", "of", "the", "array",
         "to", "be", "the", "pivot",
         "divide", "all", "other", "elements", "except",
         "the", "pivot", "into", "two", "partitions",
         "all", "elements", "less", "than", "the", "pivot",
         "must", "be", "in", "the", "first", "partition",
         "all", "elements", "greater", "than", "the", "pivot",
         "must", "be", "in", "the", "second", "partition",
         "use", "recursion", "to", "sort", "both", "partitions",
         "join", "the", "first", "sorted", "partition", "the",
         "pivot", "and", "the", "second", "sorted", "partition")

implement
list_quicksort$comparison<string> (x, y) =
  let
    val i = strcmp (x, y)
  in
    if i < 0 then
      first_is_less_than_second
    else if i = 0 then
      first_is_equal_to_second
    else
      first_is_greater_than_second
  end

implement
main0 () =
  let
    val sorted_strings = list_quicksort<string> example_strings

    fun
    print_strings {n       : nat} .<n>.
                  (strings : list (string, n),
                   i       : int) : void =
      case+ strings of
      | NIL => if i <> 1 then println! () else ()
      | head :: tail =>
        begin
          print! head;
          if i = 8 then
            begin
              println! ();
              print_strings (tail, 1)
            end
          else
            begin
              print! " ";
              print_strings (tail, succ i)
            end
        end
  in
    println! (length example_strings);
    println! (length sorted_strings);
    print_strings (sorted_strings, 1)
  end

(*------------------------------------------------------------------*)
```

**Output:**

```
$ patscc -O3 -DATS_MEMALLOC_GCBDW quicksort_task_for_lists.dats -lgc && ./a.out
62
62
all all all and any array be be
be both choose divide element elements elements elements
except first first greater in in into join
less must must of other partition partition partition
partition partitions partitions pivot pivot pivot pivot pivot
recursion second second sort sorted sorted than than
the the the the the the the the
the the to to two use
```

### A quicksort working on linear linked lists

This program was derived from the quicksort for non-linear linked lists.

```mw
(*------------------------------------------------------------------*)
(* Quicksort in ATS2, for linear lists.                             *)
(*------------------------------------------------------------------*)

#include "share/atspre_staload.hats"

#define NIL list_vt_nil ()
#define ::  list_vt_cons

(*------------------------------------------------------------------*)

(* A simple quicksort working on linear linked lists, with first
   element as pivot. This is meant as a demonstration, not as a
   superior sort algorithm.

   It is based on the "not-in-place" task pseudocode. *)

#define FIRST_IS_LESS_THAN_SECOND     1
#define FIRST_IS_EQUAL_TO_SECOND      2
#define FIRST_IS_GREATER_THAN_SECOND  3

typedef comparison_result =
  [i : int | (i == FIRST_IS_LESS_THAN_SECOND    ||
              i == FIRST_IS_EQUAL_TO_SECOND     ||
              i == FIRST_IS_GREATER_THAN_SECOND)]
  int i

extern fun {a : vt@ype}
list_vt_quicksort$comparison (x : !a, y : !a) :<> comparison_result

extern fun {a : vt@ype}
list_vt_quicksort {n   : int}
                  (lst : list_vt (a, n)) :<!wrt> list_vt (a, n)

(* -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - *)

implement {a}
list_vt_quicksort {n} (lst) =
  let
    fun
    partition {n     : nat}
              .<n>.             (* Proof of termination. *)
              (lst   : list_vt (a, n),
               pivot : !a)
        :<> [n1, n2, n3 : int | n1 + n2 + n3 == n]
            @(list_vt (a, n1), list_vt (a, n2), list_vt (a, n3)) =
      (* This implementation is *not* tail recursive. I may get a
         scolding for using ATS to risk stack overflow! However, I
         need more practice writing non-tail routines. :) Also, a lot
         of programmers in other languages would do it this
         way--especially if the lists are evaluated lazily. *)
      case+ lst of
      | ~ NIL => @(NIL, NIL, NIL)
      | ~ head :: tail =>
        let
          val @(lt, eq, gt) = partition (tail, pivot)
          prval () = lemma_list_vt_param lt
          prval () = lemma_list_vt_param eq
          prval () = lemma_list_vt_param gt
        in
          case+ list_vt_quicksort$comparison<a> (head, pivot) of
          | FIRST_IS_LESS_THAN_SECOND    => @(head :: lt, eq, gt)
          | FIRST_IS_EQUAL_TO_SECOND     => @(lt, head :: eq, gt)
          | FIRST_IS_GREATER_THAN_SECOND => @(lt, eq, head :: gt)
        end

    fun
    quicksort {n   : nat}
              .<n>.             (* Proof of termination. *)
              (lst : list_vt (a, n))
        :<!wrt> list_vt (a, n) =
      case+ lst of
      | NIL => lst
      | _ :: NIL => lst
      | ~ head :: tail =>
        let
          (* We are careful here to run "partition" on "tail" rather
             than "lst", so the termination metric will be provably
             decreasing. (Really the compiler *forces* us to take such
             care, or else to add !ntm to the effects.) *)
          val pivot = head
          prval () = lemma_list_vt_param tail
          val @(lt, eq, gt) = partition {n - 1} (tail, pivot)
          prval () = lemma_list_vt_param lt
          prval () = lemma_list_vt_param eq
          prval () = lemma_list_vt_param gt
          val eq = pivot :: eq
          and lt = quicksort lt
          and gt = quicksort gt
        in
          list_vt_append (lt, list_vt_append (eq, gt))
        end

    prval () = lemma_list_vt_param lst
  in
    quicksort {n} lst
  end

(*------------------------------------------------------------------*)

implement
list_vt_quicksort$comparison<Strptr1> (x, y) =
  let
    val i = compare (x, y)
  in
    if i < 0 then
      FIRST_IS_LESS_THAN_SECOND
    else if i = 0 then
      FIRST_IS_EQUAL_TO_SECOND
    else
      FIRST_IS_GREATER_THAN_SECOND
  end

implement
list_vt_map$fopr<string><Strptr1> (s) = string0_copy s

implement
list_vt_freelin$clear<Strptr1> (x) = strptr_free x

implement
main0 () =
  let
    val example_strings =
      $list_vt
        ("choose", "any", "element", "of", "the", "array",
         "to", "be", "the", "pivot",
         "divide", "all", "other", "elements", "except",
         "the", "pivot", "into", "two", "partitions",
         "all", "elements", "less", "than", "the", "pivot",
         "must", "be", "in", "the", "first", "partition",
         "all", "elements", "greater", "than", "the", "pivot",
         "must", "be", "in", "the", "second", "partition",
         "use", "recursion", "to", "sort", "both", "partitions",
         "join", "the", "first", "sorted", "partition", "the",
         "pivot", "and", "the", "second", "sorted", "partition")

    val example_strptrs =
      list_vt_map<string><Strptr1> (example_strings)
    val sorted_strptrs = list_vt_quicksort<Strptr1> example_strptrs

    fun
    print_strptrs {n       : nat} .<n>.
                  (strptrs : !list_vt (Strptr1, n),
                   i       : int) : void =
      case+ strptrs of
      | NIL => if i <> 1 then println! () else ()
      | @ head :: tail =>
        begin
          print! head;
          if i = 8 then
            begin
              println! ();
              print_strptrs (tail, 1)
            end
          else
            begin
              print! " ";
              print_strptrs (tail, succ i)
            end;
          fold@ strptrs
        end
  in
    println! (length example_strings);
    println! (length sorted_strptrs);
    print_strptrs (sorted_strptrs, 1);
    list_vt_freelin<Strptr1> sorted_strptrs;
    list_vt_free<string> example_strings
  end

(*------------------------------------------------------------------*)
```

**Output:**

```
$ patscc -O3 -DATS_MEMALLOC_LIBC quicksort_task_for_list_vt.dats && ./a.out
62
62
all all all and any array be be
be both choose divide element elements elements elements
except first first greater in in into join
less must must of other partition partition partition
partition partitions partitions pivot pivot pivot pivot pivot
recursion second second sort sorted sorted than than
the the the the the the the the
the the to to two use
```

### A quicksort working on arrays of non-linear elements

```mw
(*------------------------------------------------------------------*)
(* Quicksort in ATS2, for arrays of non-linear values.              *)
(*------------------------------------------------------------------*)

#include "share/atspre_staload.hats"

#define NIL list_nil ()
#define ::  list_cons

(*------------------------------------------------------------------*)

(* A simple quicksort working on arrays of non-linear values, using
   a programmer-selectible pivot.

   It is based on the "in-place" task pseudocode. *)

extern fun {a : t@ype}          (* A "less-than" predicate. *)
array_quicksort$lt (x : a, y : a) : bool

extern fun {a : t@ype}
array_quicksort$select_pivot {n     : int}
                             {i, j  : nat | i < j; j < n}
                             (arr   : &array (a, n) >> _,
                              first : size_t i,
                              last  : size_t j) : a

extern fun {a : t@ype}
array_quicksort {n   : int}
                (arr : &array (a, n) >> _,
                 n   : size_t n) : void

(* -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - *)

fn {a : t@ype}
swap {n    : int}
     {i, j : nat | i < n; j < n}
     (arr  : &array(a, n) >> _,
      i    : size_t i,
      j    : size_t j) : void =
  {
    val x = arr[i] and y = arr[j]
    val () = (arr[i] := y) and () = (arr[j] := x)
  }

implement {a}
array_quicksort {n} (arr, n) =
  let
    sortdef index = {i : nat | i < n}
    typedef index (i : int) = [0 <= i; i < n] size_t i
    typedef index = [i : index] index i

    macdef lt = array_quicksort$lt<a>

    fun
    quicksort {i, j  : index}
              (arr   : &array(a, n) >> _,
               first : index i,
               last  : index j) : void =
      if first < last then
        {
          val pivot : a =
            array_quicksort$select_pivot<a> (arr, first, last)

          fun
          search_rightwards (arr  : &array (a, n),
                             left : index) : index =
            if arr[left] \lt pivot then
              let
                val () = assertloc (succ left <> n)
              in
                search_rightwards (arr, succ left)
              end
            else
              left

          fun
          search_leftwards (arr   : &array (a, n),
                            left  : index,
                            right : index) : index =
            if right < left then
              right
            else if pivot \lt arr[right] then
              let
                val () = assertloc (right <> i2sz 0)
              in
                search_leftwards (arr, left, pred right)
              end
            else
              right

          fun
          partition (arr    : &array (a, n) >> _,
                     left0  : index,
                     right0 : index) : @(index, index) =
            let
              val left = search_rightwards (arr, left0)
              val right = search_leftwards (arr, left, right0)
            in
              if left <= right then
                let
                  val () = assertloc (succ left <> n)
                  and () = assertloc (right <> i2sz 0)
                in
                  swap (arr, left, right);
                  partition (arr, succ left, pred right)
                end
              else
                @(left, right)
            end

          val @(left, right) = partition (arr, first, last)

          val () = quicksort (arr, first, right)
          and () = quicksort (arr, left, last)
        }
  in
    if i2sz 2 <= n then
      quicksort {0, n - 1} (arr, i2sz 0, pred n)
  end

(*------------------------------------------------------------------*)

val example_strings =
  $list ("choose", "any", "element", "of", "the", "array",
         "to", "be", "the", "pivot",
         "divide", "all", "other", "elements", "except",
         "the", "pivot", "into", "two", "partitions",
         "all", "elements", "less", "than", "the", "pivot",
         "must", "be", "in", "the", "first", "partition",
         "all", "elements", "greater", "than", "the", "pivot",
         "must", "be", "in", "the", "second", "partition",
         "use", "recursion", "to", "sort", "both", "partitions",
         "join", "the", "first", "sorted", "partition", "the",
         "pivot", "and", "the", "second", "sorted", "partition")

implement
array_quicksort$lt<string> (x, y) =
  strcmp (x, y) < 0

implement
array_quicksort$select_pivot<string> {n} (arr, first, last) =
  (* Median of three, with swapping around of elements during pivot
     selection. See https://archive.ph/oYENx *)
  let
    macdef lt = array_quicksort$lt<string>

    val middle = first + ((last - first) / i2sz 2)

    val xfirst = arr[first]
    and xmiddle = arr[middle]
    and xlast = arr[last]
  in
    if (xmiddle \lt xfirst) xor (xlast \lt xfirst) then
      begin
        swap (arr, first, middle);
        if xlast \lt xmiddle then
          swap (arr, first, last);
        xfirst
      end
    else if (xmiddle \lt xfirst) xor (xmiddle \lt xlast) then
      begin
        if xlast \lt xfirst then
          swap (arr, first, last);
        xmiddle
      end
    else
      begin
        swap (arr, middle, last);
        if xmiddle \lt xfirst then
          swap (arr, first, last);
        xlast
      end
  end

implement
main0 () =
  let
    prval () = lemma_list_param example_strings
    val n = length example_strings

    val @(pf, pfgc | p) = array_ptr_alloc<string> (i2sz n)
    macdef arr = !p

    val () = array_initize_list (arr, n, example_strings)
    val () = array_quicksort<string> (arr, i2sz n)
    val sorted_strings = list_vt2t (array2list (arr, i2sz n))

    val () = array_ptr_free (pf, pfgc | p)

    fun
    print_strings {n       : nat} .<n>.
                  (strings : list (string, n),
                   i       : int) : void =
      case+ strings of
      | NIL => if i <> 1 then println! () else ()
      | head :: tail =>
        begin
          print! head;
          if i = 8 then
            begin
              println! ();
              print_strings (tail, 1)
            end
          else
            begin
              print! " ";
              print_strings (tail, succ i)
            end
        end
  in
    println! (length example_strings);
    println! (length sorted_strings);
    print_strings (sorted_strings, 1)
  end

(*------------------------------------------------------------------*)
```

**Output:**

```
$ patscc -O3 -DATS_MEMALLOC_GCBDW quicksort_task_for_arrays.dats -lgc && ./a.out
62
62
all all all and any array be be
be both choose divide element elements elements elements
except first first greater in in into join
less must must of other partition partition partition
partition partitions partitions pivot pivot pivot pivot pivot
recursion second second sort sorted sorted than than
the the the the the the the the
the the to to two use
```

### A quicksort working on arrays of linear elements

The quicksort for arrays of non-linear elements *makes a copy* of the pivot value, and compares this copy with array elements *by value*. Here, however, the array elements are *linear* values. They cannot be copied, unless a special "copy" procedure is provided. We do not want to require such a procedure. So we must do something else.

What we do is move the pivot to the last element of the array, by safely swapping it with the original last element. We partition the array to the left of the last element, comparing array elements with the pivot (that is, the last element) *by reference*.

```mw
(*------------------------------------------------------------------*)
(* Quicksort in ATS2, for arrays of (possibly) linear values.       *)
(*------------------------------------------------------------------*)

#include "share/atspre_staload.hats"

#define NIL list_vt_nil ()
#define ::  list_vt_cons

(*------------------------------------------------------------------*)

(* A simple quicksort working on arrays of non-linear values, using
   a programmer-selectible pivot.

   It is based on the "in-place" task pseudocode. *)

extern fun {a : vt@ype}          (* A "less-than" predicate. *)
array_quicksort$lt {px, py : addr}
                   (pfx    : !(a @ px),
                    pfy    : !(a @ py) |
                    px     : ptr px,
                    py     : ptr py) : bool

extern fun {a : vt@ype}
array_quicksort$select_pivot_index {n     : int}
                                   {i, j  : nat | i < j; j < n}
                                   (arr   : &array (a, n),
                                    first : size_t i,
                                    last  : size_t j)
    : [k : int | i <= k; k <= j] size_t k

extern fun {a : vt@ype}
array_quicksort {n   : int}
                (arr : &array (a, n) >> _,
                 n   : size_t n) : void

(* -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - *)

prfn                   (* Subdivide an array view into three views. *)
array_v_subdivide3 {a : vt@ype} {p : addr} {n1, n2, n3 : nat}
                   (pf : @[a][n1 + n2 + n3] @ p)
    :<prf> @(@[a][n1] @ p,
           @[a][n2] @ (p + n1 * sizeof a),
           @[a][n3] @ (p + (n1 + n2) * sizeof a)) =
  let
    prval (pf1, pf23) =
      array_v_split {a} {p} {n1 + n2 + n3} {n1} pf
    prval (pf2, pf3) =
      array_v_split {a} {p + n1 * sizeof a} {n2 + n3} {n2} pf23
  in
    @(pf1, pf2, pf3)
  end

prfn            (* Join three contiguous array views into one view. *)
array_v_join3 {a : vt@ype} {p : addr} {n1, n2, n3 : nat}
              (pf1 : @[a][n1] @ p,
               pf2 : @[a][n2] @ (p + n1 * sizeof a),
               pf3 : @[a][n3] @ (p + (n1 + n2) * sizeof a))
    :<prf> @[a][n1 + n2 + n3] @ p =
  let
    prval pf23 =
      array_v_unsplit {a} {p + n1 * sizeof a} {n2, n3} (pf2, pf3)
    prval pf = array_v_unsplit {a} {p} {n1, n2 + n3} (pf1, pf23)
  in
    pf
  end

fn {a : vt@ype}            (* Safely swap two elements of an array. *)
swap_elems_1 {n     : int}
             {i, j  : nat | i <= j; j < n}
             {p     : addr}
             (pfarr : !array_v(a, p, n) >> _ |
              p     : ptr p,
              i     : size_t i,
              j     : size_t j) : void =

  let
    fn {a : vt@ype}
    swap {n     : int}
         {i, j  : nat | i < j; j < n}
         {p     : addr}
         (pfarr : !array_v(a, p, n) >> _ |
          p     : ptr p,
          i     : size_t i,
          j     : size_t j) : void =
      {

        (* Safely swapping linear elements requires that views of
           those elements be split off from the rest of the
           array. Why? Because those elements will temporarily be in
           an uninitialized state. (Actually they will be "?!", but
           the difference is unimportant here.)

           Remember, a linear value is consumed by using it.

           The view for the whole array can be reassembled only after
           new values have been stored, making the entire array once
           again initialized. *)

        prval @(pf1, pf2, pf3) =
          array_v_subdivide3 {a} {p} {i, j - i, n - j} pfarr
        prval @(pfi, pf2_) = array_v_uncons pf2
        prval @(pfj, pf3_) = array_v_uncons pf3

        val pi = ptr_add<a> (p, i)
        and pj = ptr_add<a> (p, j)

        val xi = ptr_get<a> (pfi | pi)
        and xj = ptr_get<a> (pfj | pj)

        val () = ptr_set<a> (pfi | pi, xj)
        and () = ptr_set<a> (pfj | pj, xi)

        prval pf2 = array_v_cons (pfi, pf2_)
        prval pf3 = array_v_cons (pfj, pf3_)
        prval () = pfarr := array_v_join3 (pf1, pf2, pf3)
      }
  in
    if i < j then
      swap {n} {i, j} {p} (pfarr | p, i, j)
    else
      ()   (* i = j must be handled specially, due to linear typing.*)
  end

fn {a : vt@ype}            (* Safely swap two elements of an array. *)
swap_elems_2 {n    : int}
             {i, j : nat | i <= j; j < n}
             (arr  : &array(a, n) >> _,
              i     : size_t i,
              j     : size_t j) : void =
  swap_elems_1 (view@ arr | addr@ arr, i, j)

overload swap_elems with swap_elems_1
overload swap_elems with swap_elems_2
overload swap with swap_elems

fn {a : vt@ype}         (* Safely compare two elements of an array. *)
lt_elems_1 {n     : int}
           {i, j  : nat | i < n; j < n}
           {p     : addr}
           (pfarr : !array_v(a, p, n) |
            p     : ptr p,
            i     : size_t i,
            j     : size_t j) : bool =
  let
    fn
    compare {n     : int}
            {i, j  : nat | i < j; j < n}
            {p     : addr}
            (pfarr : !array_v(a, p, n) |
             p     : ptr p,
             i     : size_t i,
             j     : size_t j,
             gt    : bool) : bool =
      let
        prval @(pf1, pf2, pf3) =
          array_v_subdivide3 {a} {p} {i, j - i, n - j} pfarr
        prval @(pfi, pf2_) = array_v_uncons pf2
        prval @(pfj, pf3_) = array_v_uncons pf3

        val pi = ptr_add<a> (p, i)
        and pj = ptr_add<a> (p, j)

        val retval =
          if gt then
            array_quicksort$lt<a> (pfj, pfi | pj, pi)
          else
            array_quicksort$lt<a> (pfi, pfj | pi, pj)

        prval pf2 = array_v_cons (pfi, pf2_)
        prval pf3 = array_v_cons (pfj, pf3_)
        prval () = pfarr := array_v_join3 (pf1, pf2, pf3)
      in
        retval
      end
  in
    if i < j then
      compare {n} {i, j} {p} (pfarr | p, i, j, false)
    else if j < i then
      compare {n} {j, i} {p} (pfarr | p, j, i, true)
    else
      false
  end

fn {a : vt@ype}         (* Safely compare two elements of an array. *)
lt_elems_2 {n    : int}
           {i, j : nat | i < n; j < n}
           (arr  : &array (a, n),
            i    : size_t i,
            j    : size_t j) : bool =
  lt_elems_1 (view@ arr | addr@ arr, i, j)

overload lt_elems with lt_elems_1
overload lt_elems with lt_elems_2

implement {a}
array_quicksort {n} (arr, n) =
  let
    sortdef index = {i : nat | i < n}
    typedef index (i : int) = [0 <= i; i < n] size_t i
    typedef index = [i : index] index i

    macdef lt = array_quicksort$lt<a>

    fun
    quicksort {i, j  : index}
              (arr   : &array(a, n) >> _,
               first : index i,
               last  : index j) : void =
      if first < last then
        {
          val pivot =
            array_quicksort$select_pivot_index<a> (arr, first, last)

          (* Swap the pivot with the last element. *)
          val () = swap (arr, pivot, last)
          val pivot = last

          fun
          search_rightwards (arr  : &array (a, n),
                             left : index) : index =
            if lt_elems<a> (arr, left, pivot) then
              let
                val () = assertloc (succ left <> n)
              in
                search_rightwards (arr, succ left)
              end
            else
              left

          fun
          search_leftwards (arr   : &array (a, n),
                            left  : index,
                            right : index) : index =
            if right < left then
              right
            else if lt_elems<a> (arr, pivot, right) then
              let
                val () = assertloc (right <> i2sz 0)
              in
                search_leftwards (arr, left, pred right)
              end
            else
              right

          fun
          partition (arr    : &array (a, n) >> _,
                     left0  : index,
                     right0 : index) : @(index, index) =
            let
              val left = search_rightwards (arr, left0)
              val right = search_leftwards (arr, left, right0)
            in
              if left <= right then
                let
                  val () = assertloc (succ left <> n)
                  and () = assertloc (right <> i2sz 0)
                in
                  swap (arr, left, right);
                  partition (arr, succ left, pred right)
                end
              else
                @(left, right)
            end

          val @(left, right) = partition (arr, first, pred last)

          val () = quicksort (arr, first, right)
          and () = quicksort (arr, left, last)
        }
  in
    if i2sz 2 <= n then
      quicksort {0, n - 1} (arr, i2sz 0, pred n)
  end

(*------------------------------------------------------------------*)

implement
array_quicksort$lt<Strptr1> (pfx, pfy | px, py) =
  compare (!px, !py) < 0

implement
array_quicksort$select_pivot_index<Strptr1> {n} (arr, first, last) =
  (* Median of three. *)
  let
    val middle = first + ((last - first) / i2sz 2)
  in
    if lt_elems<Strptr1> (arr, middle, first)
          xor lt_elems<Strptr1> (arr, last, first) then
      first
    else if lt_elems<Strptr1> (arr, middle, first)
              xor lt_elems<Strptr1> (arr, middle, last) then
      middle
    else
      last
  end

implement
list_vt_map$fopr<string><Strptr1> (s) = string0_copy s

implement
list_vt_freelin$clear<Strptr1> (x) = strptr_free x

implement
main0 () =
  let
    val example_strings =
      $list_vt
        ("choose", "any", "element", "of", "the", "array",
         "to", "be", "the", "pivot",
         "divide", "all", "other", "elements", "except",
         "the", "pivot", "into", "two", "partitions",
         "all", "elements", "less", "than", "the", "pivot",
         "must", "be", "in", "the", "first", "partition",
         "all", "elements", "greater", "than", "the", "pivot",
         "must", "be", "in", "the", "second", "partition",
         "use", "recursion", "to", "sort", "both", "partitions",
         "join", "the", "first", "sorted", "partition", "the",
         "pivot", "and", "the", "second", "sorted", "partition")

    val example_strptrs =
      list_vt_map<string><Strptr1> (example_strings)

    prval () = lemma_list_vt_param example_strptrs
    val n = length example_strptrs

    val @(pf, pfgc | p) = array_ptr_alloc<Strptr1> (i2sz n)
    macdef arr = !p

    val () = array_initize_list_vt<Strptr1> (arr, n, example_strptrs)
    val () = array_quicksort<Strptr1> (arr, i2sz n)
    val sorted_strptrs = array2list (arr, i2sz n)

    fun
    print_strptrs {n       : nat} .<n>.
                  (strptrs : !list_vt (Strptr1, n),
                   i       : int) : void =
      case+ strptrs of
      | NIL => if i <> 1 then println! () else ()
      | @ head :: tail =>
        begin
          print! head;
          if i = 8 then
            begin
              println! ();
              print_strptrs (tail, 1)
            end
          else
            begin
              print! " ";
              print_strptrs (tail, succ i)
            end;
          fold@ strptrs
        end
  in
    println! (length example_strings);
    println! (length sorted_strptrs);
    print_strptrs (sorted_strptrs, 1);
    list_vt_freelin<Strptr1> sorted_strptrs;
    array_ptr_free (pf, pfgc | p);
    list_vt_free<string> example_strings
  end

(*------------------------------------------------------------------*)
```

**Output:**

```
$ patscc -O3 -DATS_MEMALLOC_LIBC quicksort_task_for_arrays_2.dats
62
62
all all all and any array be be
be both choose divide element elements elements elements
except first first greater in in into join
less must must of other partition partition partition
partition partitions partitions pivot pivot pivot pivot pivot
recursion second second sort sorted sorted than than
the the the the the the the the
the the to to two use
```

### A *stable* quicksort working on linear lists

See the code at the quickselect task.

**Output:**

```
$ patscc -O3 -DATS_MEMALLOC_LIBC quickselect_task_for_list_vt.dats && ./a.out quicksort
stable sort by first character:
duck, deer, dolphin, elephant, earwig, giraffe, pronghorn, wildebeest, woodlouse, whip-poor-will
```


## AutoHotkey

Translated from the python example:

```mw
a := [4, 65, 2, -31, 0, 99, 83, 782, 7]
for k, v in QuickSort(a)
   Out .= "," v
MsgBox, % SubStr(Out, 2)
return

QuickSort(a)
{
   if (a.MaxIndex() <= 1)
      return a
   Less := [], Same := [], More := []
   Pivot := a[1]
   for k, v in a
   {
      if (v < Pivot)
         less.Insert(v)
      else if (v > Pivot)
         more.Insert(v)
      else
         same.Insert(v)
   }
   Less := QuickSort(Less)
   Out := QuickSort(More)
   if (Same.MaxIndex())
      Out.Insert(1, Same*) ; insert all values of same at index 1
   if (Less.MaxIndex())
      Out.Insert(1, Less*) ; insert all values of less at index 1
   return Out
}
```

Old implementation for AutoHotkey 1.0:

```mw
MsgBox % quicksort("8,4,9,2,1")

quicksort(list)
{
  StringSplit, list, list, `,
  If (list0 <= 1)
    Return list
  pivot := list1
  Loop, Parse, list, `,
  {
    If (A_LoopField < pivot)
      less = %less%,%A_LoopField%
    Else If (A_LoopField > pivot)
      more = %more%,%A_LoopField%
    Else
      pivotlist = %pivotlist%,%A_LoopField%
  }
  StringTrimLeft, less, less, 1
  StringTrimLeft, more, more, 1
  StringTrimLeft, pivotList, pivotList, 1
  less := quicksort(less)
  more := quicksort(more)
  Return less . pivotList . more
}
```
