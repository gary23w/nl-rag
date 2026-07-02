---
title: "Binary search (part 1/6)"
source: https://rosettacode.org/wiki/Binary_search
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/6
---

# Binary search

A binary search divides a range of values into halves, and continues to narrow down the field of search until the unknown value is found. It is the classic example of a "divide and conquer" algorithm.

As an analogy, consider the children's game "guess a number." The scorer has a secret number, and will only tell the player if their guessed number is higher than, lower than, or equal to the secret number. The player then uses this information to guess a new number.

As the player, an optimal strategy for the general case is to start by choosing the range's midpoint as the guess, and then asking whether the guess was higher, lower, or equal to the secret number. If the guess was too high, one would select the point exactly between the range midpoint and the beginning of the range. If the original guess was too low, one would ask about the point exactly between the range midpoint and the end of the range. This process repeats until one has reached the secret number.

**Task**

Given the starting point of a range, the ending point of a range, and the "secret value", implement a binary search through a sorted integer array for a certain number. Implementations can be recursive or iterative (both if you can). Print out whether or not the number was in the array afterwards. If it was, print the index also.

There are several binary search algorithms commonly seen. They differ by how they treat multiple values equal to the given value, and whether they indicate whether the element was found or not. For completeness we will present pseudocode for all of them.

All of the following code examples use an "inclusive" upper bound (i.e. `high = N-1` initially). Any of the examples can be converted into an equivalent example using "exclusive" upper bound (i.e. `high = N` initially) by making the following simple changes (which simply increase `high` by 1):

- change `high = N-1` to `high = N`
- change `high = mid-1` to `high = mid`
- (for recursive algorithm) change `if (high < low)` to `if (high <= low)`
- (for iterative algorithm) change `while (low <= high)` to `while (low < high)`

**Traditional algorithm**

The algorithms are as follows (from Wikipedia). The algorithms return the index of some element that equals the given value (if there are multiple such elements, it returns some arbitrary one). It is also possible, when the element is not found, to return the "insertion point" for it (the index that the value would have if it were inserted into the array).

**Recursive Pseudocode**:

```
  // initially called with low = 0, high = N-1
  BinarySearch(A[0..N-1], value, low, high) {
      // invariants: value > A[i] for all i < low
                     value < A[i] for all i > high
      if (high < low)
          return not_found // value would be inserted at index "low"
      mid = (low + high) / 2
      if (A[mid] > value)
          return BinarySearch(A, value, low, mid-1)
      else if (A[mid] < value)
          return BinarySearch(A, value, mid+1, high)
      else
          return mid
  }
```

**Iterative Pseudocode**:

```
  BinarySearch(A[0..N-1], value) {
      low = 0
      high = N - 1
      while (low <= high) {
          // invariants: value > A[i] for all i < low
                         value < A[i] for all i > high
          mid = (low + high) / 2
          if (A[mid] > value)
              high = mid - 1
          else if (A[mid] < value)
              low = mid + 1
          else
              return mid
      }
      return not_found // value would be inserted at index "low"
  }
```

**Leftmost insertion point**

The following algorithms return the leftmost place where the given element can be correctly inserted (and still maintain the sorted order). This is the lower (inclusive) bound of the range of elements that are equal to the given value (if any). Equivalently, this is the lowest index where the element is greater than or equal to the given value (since if it were any lower, it would violate the ordering), or 1 past the last index if such an element does not exist. This algorithm does not determine if the element is actually found. This algorithm only requires one comparison per level.

**Recursive Pseudocode**:

```
  // initially called with low = 0, high = N - 1
  BinarySearch_Left(A[0..N-1], value, low, high) {
      // invariants: value > A[i] for all i < low
                     value <= A[i] for all i > high
      if (high < low)
          return low
      mid = (low + high) / 2
      if (A[mid] >= value)
          return BinarySearch_Left(A, value, low, mid-1)
      else
          return BinarySearch_Left(A, value, mid+1, high)
  }
```

**Iterative Pseudocode**:

```
  BinarySearch_Left(A[0..N-1], value) {
      low = 0
      high = N - 1
      while (low <= high) {
          // invariants: value > A[i] for all i < low
                         value <= A[i] for all i > high
          mid = (low + high) / 2
          if (A[mid] >= value)
              high = mid - 1
          else
              low = mid + 1
      }
      return low
  }
```

**Rightmost insertion point**

The following algorithms return the rightmost place where the given element can be correctly inserted (and still maintain the sorted order). This is the upper (exclusive) bound of the range of elements that are equal to the given value (if any). Equivalently, this is the lowest index where the element is greater than the given value, or 1 past the last index if such an element does not exist. This algorithm does not determine if the element is actually found. This algorithm only requires one comparison per level. Note that these algorithms are almost exactly the same as the leftmost-insertion-point algorithms, except for how the inequality treats equal values.

**Recursive Pseudocode**:

```
  // initially called with low = 0, high = N - 1
  BinarySearch_Right(A[0..N-1], value, low, high) {
      // invariants: value >= A[i] for all i < low
                     value < A[i] for all i > high
      if (high < low)
          return low
      mid = (low + high) / 2
      if (A[mid] > value)
          return BinarySearch_Right(A, value, low, mid-1)
      else
          return BinarySearch_Right(A, value, mid+1, high)
  }
```

**Iterative Pseudocode**:

```
  BinarySearch_Right(A[0..N-1], value) {
      low = 0
      high = N - 1
      while (low <= high) {
          // invariants: value >= A[i] for all i < low
                         value < A[i] for all i > high
          mid = (low + high) / 2
          if (A[mid] > value)
              high = mid - 1
          else
              low = mid + 1
      }
      return low
  }
```

**Extra credit**

Make sure it does not have overflow bugs.

The line in the pseudo-code above to calculate the mean of two integers:

```
mid = (low + high) / 2
```

could produce the wrong result in some programming languages when used with a bounded integer type, if the addition causes an overflow. (This can occur if the array size is greater than half the maximum integer value.) If signed integers are used, and `low + high` overflows, it becomes a negative number, and dividing by 2 will still result in a negative number. Indexing an array with a negative number could produce an out-of-bounds exception, or other undefined behavior. If unsigned integers are used, an overflow will result in losing the largest bit, which will produce the wrong result.

One way to fix it is to manually add half the range to the low number:

```
mid = low + (high - low) / 2
```

Even though this is mathematically equivalent to the above, it is not susceptible to overflow.

Another way for signed integers, possibly faster, is the following:

```
mid = (low + high) >>> 1
```

where `>>>` is the logical right shift operator. The reason why this works is that, for signed integers, even though it overflows, when viewed as an unsigned number, the value is still the correct sum. To divide an unsigned number by 2, simply do a logical right shift.

**Related task**

- Guess the number/With Feedback (Player)

**See also**

- wp:Binary search algorithm
- Extra, Extra - Read All About It: Nearly All Binary Searches and Mergesorts are Broken.


## 11l

```mw
F binary_search(l, value)
   V low = 0
   V high = l.len - 1
   L low <= high
      V mid = (low + high) I/ 2
      I l[mid] > value
         high = mid - 1
      E I l[mid] < value
         low = mid + 1
      E
         R mid
   R -1
```


## 360 Assembly

```mw
*        Binary search             05/03/2017
BINSEAR  CSECT
         USING  BINSEAR,R13        base register
         B      72(R15)            skip savearea
         DC     17F'0'             savearea
         STM    R14,R12,12(R13)    save previous context
         ST     R13,4(R15)         link backward
         ST     R15,8(R13)         link forward
         LR     R13,R15            set addressability
         MVC    LOW,=H'1'          low=1
         MVC    HIGH,=AL2((XVAL-T)/2)  high=hbound(t)
         SR     R6,R6              i=0
         MVI    F,X'00'            f=false
         LH     R4,LOW             low
       DO WHILE=(CH,R4,LE,HIGH)    do while low<=high
         LA     R6,1(R6)             i=i+1
         LH     R1,LOW               low
         AH     R1,HIGH              +high
         SRA    R1,1                 /2  {by right shift}
         STH    R1,MID               mid=(low+high)/2
         SLA    R1,1                 *2
         LH     R7,T-2(R1)           y=t(mid)
       IF CH,R7,EQ,XVAL THEN         if xval=y then
         MVI    F,X'01'                f=true
         B      EXITDO                 leave
       ENDIF    ,                    endif
       IF CH,R7,GT,XVAL THEN         if y>xval then
         LH     R2,MID                 mid
         BCTR   R2,0                   -1
         STH    R2,HIGH                high=mid-1
       ELSE     ,                    else
         LH     R2,MID                 mid
         LA     R2,1(R2)               +1
         STH    R2,LOW                low=mid+1
       ENDIF    ,                    endif
         LH     R4,LOW               low
       ENDDO    ,                  enddo
EXITDO   EQU    *                exitdo:
         XDECO  R6,XDEC            edit i
         MVC    PG(4),XDEC+8       output i
         MVC    PG+4(6),=C' loops'
         XPRNT  PG,L'PG            print buffer
         LH     R1,XVAL            xval
         XDECO  R1,XDEC            edit xval
         MVC    PG(4),XDEC+8       output xval
       IF CLI,F,EQ,X'01' THEN      if f then
         MVC    PG+4(10),=C' found at '
         LH     R1,MID               mid
         XDECO  R1,XDEC              edit mid
         MVC    PG+14(4),XDEC+8      output mid
       ELSE     ,                  else
         MVC    PG+4(20),=C' is not in the list.'
       ENDIF    ,                  endif
         XPRNT  PG,L'PG            print buffer
         L      R13,4(0,R13)       restore previous savearea pointer
         LM     R14,R12,12(R13)    restore previous context
         XR     R15,R15            rc=0
         BR     R14                exit
T        DC     H'3',H'7',H'13',H'19',H'23',H'31',H'43',H'47'
         DC     H'61',H'73',H'83',H'89',H'103',H'109',H'113',H'131'
         DC     H'139',H'151',H'167',H'181',H'193',H'199',H'229',H'233'
         DC     H'241',H'271',H'283',H'293',H'313',H'317',H'337',H'349'
XVAL     DC     H'229'             <= search value
LOW      DS     H
HIGH     DS     H
MID      DS     H
F        DS     X                  flag
PG       DC     CL80' '            buffer
XDEC     DS     CL12               temp
         YREGS
         END    BINSEAR
```

**Output:**

```
   5 loops
 229 found at   23
```


## 8080 Assembly

This is the iterative version of the 'leftmost insertion point' algorithm. (On a processor like the 8080, you would not want to use recursion if you can avoid it. A subroutine call alone takes two bytes of stack space, meaning the needed stack space would be bigger than the array that's being searched.) For simplicity, it operates on an array of unsigned 8-bit integers, as this is the 8080's native datatype, and this task is about binary search, not about implementing operations on other datatypes in terms of 8-bit integers.

On entry, the subroutine `binsrch` takes the lookup value in the `B` register, a pointer to the start of the array in the `HL` registers, and a pointer to the end of the array in the `DE` registers. On exit, `HL` will contain the location of the value in the array, if it was found, and the leftmost insertion point, if it was not.

Test code is included, which will loop through the values [0..255] and report for each number whether it was in the array or not.

```mw
		org	100h	; Entry for test code
		jmp	test

		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;; Binary search in array of unsigned 8-bit integers
		;; B = value to look for
		;; HL = begin of array (low)
		;; DE = end of array, inclusive (high)
		;; The entry point is 'binsrch'
		;; On return, HL = location of value (if contained
		;; in array), or insertion point (if not)

binsrch_lo:	inx	h	; low = mid + 1
		inx	sp	; throw away 'low'
		inx	sp

binsrch:	mov	a,d	; low > high? (are we there yet?)
		cmp	h	; test high byte
		rc
		mov	a,e	; test low byte
		cmp	l
		rc

		push	h	; store 'low'

		dad	d	; mid = (low+high)>>1
		mov	a,h	; rotate the carry flag back in
		rar		; to take care of any overflow
		mov	h,a
		mov	a,l
		rar
		mov	l,a
	
		mov	a,m	; A[mid] >= value?
		cmp	b
		jc	binsrch_lo

		xchg		; high = mid - 1
		dcx	d
		pop	h	; restore 'low'
		jmp	binsrch

		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;; Test data

primes:		db	2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
		db	41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83
		db	89, 97, 101, 103, 107, 109, 113, 127, 131
		db	137, 139, 149, 151, 157, 163, 167, 173, 179
		db	181, 191, 193, 197, 199, 211, 223, 227, 229
		db	233, 239, 241, 251
primes_last:	equ	$ - 1

		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;; Test code (CP/M compatible)

yep:		db	": yes", 13, 10, "$"
nope:		db	": no", 13, 10, "$"

num_out:	mov	a,b		;; Output number in B as decimal
		mvi	c,100
		call	dgt_out
		mvi	c,10
		call	dgt_out
		mvi	c,1
dgt_out:	mvi	e,'0' - 1	;; Output 100s, 10s or 1s
dgt_out_loop:	inr	e		;; (depending on C)
		sub	c		
		jnc	dgt_out_loop
		add	c
e_out:		push	psw		;; Output character in E
		push	b		;; preserving working registers
		mvi	c,2
		call	5
		pop	b
		pop	psw
		ret

		;; Main test code
test:		mvi	b,0		; Test value
		
test_loop:	call	num_out		; Output current number to test
		
		lxi	h,primes	; Set up input for binary search
		lxi	d,primes_last
		call	binsrch		; Search for B in array
		
		lxi	d,nope		; Location of "no" string
		mov	a,b		; Check if location binsrch returned
		cmp	m		; contains the value we were looking for
		jnz	str_out		; If not, print the "no" string
		lxi	d,yep		; But if so, use location of "yes" string
str_out:	push	b		; Preserve B across CP/M call
		mvi	c,9		; Print the string
		call	5
		pop	b		; Restore B				
		
		inr	b		; Test next value
		jnz	test_loop			

		rst	0
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program binSearch64.s   */

/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"

/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:        .asciz "Value find at index : @ \n"
szCarriageReturn:   .asciz "\n"
sMessRecursif:      .asciz "Recursive search : \n"
sMessNotFound:      .asciz "Value not found. \n"

TableNumber:        .quad   4,6,7,10,11,15,22,30,35
                    .equ NBELEMENTS,  (. - TableNumber) / 8
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss
sZoneConv:          .skip 24
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                                           // entry of program 
    mov x0,4                                    // search first value
    ldr x1,qAdrTableNumber                      // address number table
    mov x2,NBELEMENTS                           // number of élements 
    bl bSearch
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message
 
    mov x0,#11                                  // search median value
    ldr x1,qAdrTableNumber
    mov x2,#NBELEMENTS
    bl bSearch
    ldr x1,qAdrsZoneConv
    bl conversion10                             // decimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message
 
    mov x0,#12                                  //value not found
    ldr x1,qAdrTableNumber
    mov x2,#NBELEMENTS
    bl bSearch
    cmp x0,#-1
    bne 2f
    ldr x0,qAdrsMessNotFound
    bl affichageMess 
    b 3f
2:
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message
3:
    mov x0,#35                                  // search last value
    ldr x1,qAdrTableNumber
    mov x2,#NBELEMENTS
    bl bSearch
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message

/****************************************/
/*       recursive                      */
/****************************************/
    ldr x0,qAdrsMessRecursif
    bl affichageMess                            // display message
 
    mov x0,#4                                   // search first value
    ldr x1,qAdrTableNumber
    mov x2,#0                                   // low index of elements
    mov x3,#NBELEMENTS - 1                      // high index of elements
    bl bSearchR
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message
 
    mov x0,#11
    ldr x1,qAdrTableNumber
    mov x2,#0
    mov x3,#NBELEMENTS - 1
    bl bSearchR
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message
 
    mov x0,#12
    ldr x1,qAdrTableNumber
    mov x2,#0
    mov x3,#NBELEMENTS - 1
    bl bSearchR
    cmp x0,#-1
    bne 4f
    ldr x0,qAdrsMessNotFound
    bl affichageMess 
    b 5f
4:
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message

5:
    mov x0,#35
    ldr x1,qAdrTableNumber
    mov x2,#0
    mov x3,#NBELEMENTS - 1
    bl bSearchR
    ldr x1,qAdrsZoneConv
    bl conversion10                             // décimal conversion 
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc                       // insert result at @ character
    bl affichageMess                            // display message

 
100:                                            // standard end of the program 
    mov x0, #0                                  // return code
    mov x8, #EXIT                               // request to exit program
    svc #0                                      // perform the system call
 
//qAdrsMessValeur:          .quad sMessValeur
qAdrsZoneConv:            .quad sZoneConv
qAdrszCarriageReturn:     .quad szCarriageReturn
qAdrsMessResult:          .quad sMessResult
qAdrsMessRecursif:        .quad sMessRecursif
qAdrsMessNotFound:        .quad sMessNotFound
qAdrTableNumber:          .quad TableNumber
 
/******************************************************************/
/*     binary search   iterative                                  */ 
/******************************************************************/
/* x0 contains the value to search */
/* x1 contains the adress of table */
/* x2 contains the number of elements */
/* x0 return index or -1 if not find */
bSearch:
    stp x1,lr,[sp,-16]!              // save  registers
    stp x2,x3,[sp,-16]!              // save  registers
    stp x4,x5,[sp,-16]!              // save  registers
    mov x3,#0                        // low index
    sub x4,x2,#1                     // high index = number of elements - 1
1:
    cmp x3,x4
    bgt 99f
    add x2,x3,x4                     // compute (low + high) /2
    lsr x2,x2,#1
    ldr x5,[x1,x2,lsl #3]            // load value of table at index x2
    cmp x5,x0
    beq 98f
    bgt 2f
    add x3,x2,#1                     // lower -> index low = index + 1
    b 1b                             // and loop
2:
    sub x4,x2,#1                     // bigger -> index high = index - 1
    b 1b                             // and loop
98:
    mov x0,x2                        // find !!!
    b 100f
99:
    mov x0,#-1                       //not found
100:
    ldp x4,x5,[sp],16                // restaur  2 registers
    ldp x2,x3,[sp],16                // restaur  2 registers
    ldp x1,lr,[sp],16                // restaur  2 registers
    ret                              // return to address lr x30
/******************************************************************/
/*     binary search   recursif                                  */ 
/******************************************************************/
/* x0 contains the value to search */
/* x1 contains the adress of table */
/* x2 contains the low index of elements */
/* x3 contains the high index of elements */
/* x0 return index or -1 if not find */
bSearchR:
    stp x2,lr,[sp,-16]!              // save  registers
    stp x3,x4,[sp,-16]!              // save  registers
    stp x5,x6,[sp,-16]!              // save  registers
    cmp x3,x2                        // index high < low ?
    bge 1f
    mov x0,#-1                       // yes -> not found
    b 100f
1:
    add x4,x2,x3                                     // compute (low + high) /2
    lsr x4,x4,#1
    ldr x5,[x1,x4,lsl #3]                            // load value of table at index x4
    cmp x5,x0
    beq 99f 
    bgt 2f                                           // bigger ?
    add x2,x4,#1                                     // no new search with low = index + 1
    bl bSearchR
    b 100f
2:                                                   // bigger
    sub x3,x4,#1                                     // new search with high = index - 1
    bl bSearchR
    b 100f
99:
    mov x0,x4                                      // find !!!
    b 100f 
100:
    ldp x5,x6,[sp],16                // restaur  2 registers
    ldp x3,x4,[sp],16                // restaur  2 registers
    ldp x2,lr,[sp],16                // restaur  2 registers
    ret                              // return to address lr x30
/********************************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```

```
Value find at index : 0
Value find at index : 4
Value not found.
Value find at index : 8
Recursive search :
Value find at index : 0
Value find at index : 4
Value not found.
Value find at index : 8
```


## ACL2

```mw
(defun defarray (name size initial-element)
   (cons name
         (compress1 name
                    (cons (list :HEADER
                                :DIMENSIONS (list size)
                                :MAXIMUM-LENGTH (1+ size)
                                :DEFAULT initial-element
                                :NAME name)
                                nil))))

(defconst *dim* 100000)

(defun array-name (array)
   (first array))
       
(defun set-at (array i val)
   (cons (array-name array)
         (aset1 (array-name array)
                (cdr array)
                i
                val)))

(defun populate-array-ordered (array n)
   (if (zp n)
       array
       (populate-array-ordered (set-at array
                                       (- *dim* n)
                                       (- *dim* n))
                               (1- n))))
(include-book "arithmetic-3/top" :dir :system)

(defun binary-search-r (needle haystack low high)
   (declare (xargs :measure (nfix (1+ (- high low)))))
   (let* ((mid (floor (+ low high) 2))
          (current (aref1 (array-name haystack)
                          (cdr haystack)
                          mid)))
         (cond ((not (and (natp low) (natp high))) nil)
               ((= current needle)
                mid)
               ((zp (1+ (- high low))) nil)
               ((> current needle)
                (binary-search-r needle
                                 haystack
                                 low
                                 (1- mid)))
               (t (binary-search-r needle
                                   haystack
                                   (1+ mid)
                                   high)))))

(defun binary-search (needle haystack)
   (binary-search-r needle haystack 0
                    (maximum-length (array-name haystack)
                                    (cdr haystack))))

(defun test-bsearch (needle)
   (binary-search needle
                  (populate-array-ordered
                   (defarray 'haystack *dim* 0)
                   *dim*)))
```


## Action!

```mw
INT FUNC BinarySearch(INT ARRAY a INT len,value)
  INT low,high,mid

  low=0 high=len-1
  WHILE low<=high
  DO
    mid=low+(high-low) RSH 1
    IF a(mid)>value THEN
      high=mid-1
    ELSEIF a(mid)<value THEN
      low=mid+1
    ELSE
      RETURN (mid)
    FI
  OD
RETURN (-1)

PROC Test(INT ARRAY a INT len,value)
  INT i

  Put('[)
  FOR i=0 TO len-1
  DO
    PrintI(a(i))
    IF i<len-1 THEN Put(32) FI
  OD
  i=BinarySearch(a,len,value)
  Print("] ") PrintI(value)
  IF i<0 THEN
    PrintE(" not found")
  ELSE
    Print(" found at index ")
    PrintIE(i)
  FI
RETURN

PROC Main()
  INT ARRAY a=[65530 0 1 2 5 6 8 9]

  Test(a,8,6)
  Test(a,8,-6)
  Test(a,8,9)
  Test(a,8,-10)
  Test(a,8,10)
  Test(a,8,7)
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
[-6 0 1 2 5 6 8 9] 6 found at index 5
[-6 0 1 2 5 6 8 9] -6 found at index 0
[-6 0 1 2 5 6 8 9] 9 found at index 7
[-6 0 1 2 5 6 8 9] -10 not found
[-6 0 1 2 5 6 8 9] 10 not found
[-6 0 1 2 5 6 8 9] 7 not found
```


## Ada

Both solutions are generic. The element can be of any comparable type (such that the operation < is visible in the instantiation scope of the function Search). Note that the completion condition is different from one given in the pseudocode example above. The example assumes that the array index type does not overflow when mid is incremented or decremented beyond the corresponding array bound. This is a wrong assumption for Ada, where array bounds can start or end at the very first or last value of the index type. To deal with this, the exit condition is rather directly expressed as crossing the corresponding array bound by the coming interval middle.

**Recursive**

```mw
with Ada.Text_IO;  use Ada.Text_IO;

procedure Test_Recursive_Binary_Search is
   Not_Found : exception;
   
   generic
      type Index is range <>;
      type Element is private;
      type Array_Of_Elements is array (Index range <>) of Element;
      with function "<" (L, R : Element) return Boolean is <>;
   function Search (Container : Array_Of_Elements; Value : Element) return Index;

   function Search (Container : Array_Of_Elements; Value : Element) return Index is
      Mid : Index;
   begin
      if Container'Length > 0 then
         Mid := (Container'First + Container'Last) / 2;
         if Value < Container (Mid) then
            if Container'First /= Mid then
               return Search (Container (Container'First..Mid - 1), Value);
            end if;
         elsif Container (Mid) < Value then
            if Container'Last /= Mid then
               return Search (Container (Mid + 1..Container'Last), Value);
            end if;
         else
            return Mid;
         end if;
      end if;
      raise Not_Found;
   end Search;

   type Integer_Array is array (Positive range <>) of Integer;
   function Find is new Search (Positive, Integer, Integer_Array);
   
   procedure Test (X : Integer_Array; E : Integer) is
   begin
      New_Line;
      for I in X'Range loop
         Put (Integer'Image (X (I)));
      end loop;
      Put (" contains" & Integer'Image (E) & " at" & Integer'Image (Find (X, E)));
   exception
      when Not_Found =>
         Put (" does not contain" & Integer'Image (E));
   end Test;
begin
   Test ((2, 4, 6, 8, 9), 2);
   Test ((2, 4, 6, 8, 9), 1);
   Test ((2, 4, 6, 8, 9), 8);
   Test ((2, 4, 6, 8, 9), 10);
   Test ((2, 4, 6, 8, 9), 9);
   Test ((2, 4, 6, 8, 9), 5);
end Test_Recursive_Binary_Search;
```

**Iterative**

```mw
with Ada.Text_IO;  use Ada.Text_IO;

procedure Test_Binary_Search is
   Not_Found : exception;
   
   generic
      type Index is range <>;
      type Element is private;
      type Array_Of_Elements is array (Index range <>) of Element;
      with function "<" (L, R : Element) return Boolean is <>;
   function Search (Container : Array_Of_Elements; Value : Element) return Index;

   function Search (Container : Array_Of_Elements; Value : Element) return Index is
      Low  : Index := Container'First;
      High : Index := Container'Last;
      Mid  : Index;
   begin
      if Container'Length > 0 then
         loop
            Mid := (Low + High) / 2;
            if Value < Container (Mid) then
               exit when Low = Mid;
               High := Mid - 1;
            elsif Container (Mid) < Value then
               exit when High = Mid;
               Low := Mid + 1;
            else
               return Mid;
            end if;
         end loop;
      end if;
      raise Not_Found;
   end Search;

   type Integer_Array is array (Positive range <>) of Integer;
   function Find is new Search (Positive, Integer, Integer_Array);
   
   procedure Test (X : Integer_Array; E : Integer) is
   begin
      New_Line;
      for I in X'Range loop
         Put (Integer'Image (X (I)));
      end loop;
      Put (" contains" & Integer'Image (E) & " at" & Integer'Image (Find (X, E)));
   exception
      when Not_Found =>
         Put (" does not contain" & Integer'Image (E));
   end Test;
begin
   Test ((2, 4, 6, 8, 9), 2);
   Test ((2, 4, 6, 8, 9), 1);
   Test ((2, 4, 6, 8, 9), 8);
   Test ((2, 4, 6, 8, 9), 10);
   Test ((2, 4, 6, 8, 9), 9);
   Test ((2, 4, 6, 8, 9), 5);
end Test_Binary_Search;
```

Sample output:

```
 2 4 6 8 9 contains 2 at 1
 2 4 6 8 9 does not contain 1
 2 4 6 8 9 contains 8 at 4
 2 4 6 8 9 does not contain 10
 2 4 6 8 9 contains 9 at 5
 2 4 6 8 9 does not contain 5
```


## ALGOL 68

```mw
BEGIN
MODE ELEMENT = STRING;
 
# Iterative: #
PROC iterative binary search = ([]ELEMENT hay stack, ELEMENT needle)INT: (
    INT out,
        low := LWB hay stack,
        high := UPB hay stack;
    WHILE low < high DO
        INT mid := (low+high) OVER 2;
        IF hay stack[mid] > needle THEN high := mid-1
        ELIF hay stack[mid] < needle THEN low := mid+1
        ELSE out:= mid; stop iteration FI
    OD;
        low EXIT
    stop iteration:
        out
);
# Recursive: #
PROC recursive binary search = ([]ELEMENT hay stack, ELEMENT needle)INT: (
    IF LWB hay stack > UPB hay stack THEN
        LWB hay stack
    ELIF LWB hay stack = UPB hay stack THEN
        IF hay stack[LWB hay stack] = needle THEN LWB hay stack
        ELSE LWB hay stack FI
    ELSE
        INT mid := (LWB hay stack+UPB hay stack) OVER 2;
        IF hay stack[mid] > needle THEN recursive binary search(hay stack[:mid-1], needle)
        ELIF hay stack[mid] < needle THEN mid + recursive binary search(hay stack[mid+1:], needle)
        ELSE mid FI
   FI
);
PROC test search = (PROC([]ELEMENT, ELEMENT)INT search, []ELEMENT hay stack, []ELEMENT test cases)VOID:
     FOR case TO UPB test cases DO
        ELEMENT needle = test cases[case];
        INT index = search(hay stack, needle);
        BOOL found = ( index <= 0 | FALSE | hay stack[index]=needle);
        print(("""", needle, """ ", (found|"FOUND at"|"near"), " index ", whole(index, 0), newline))
     OD;
 
 BEGIN  # Test cases: #
  []ELEMENT hay stack = ("AA","Maestro","Mario","Master","Mattress","Mister","Mistress","ZZ")
          , test cases = ("A","Master","Monk","ZZZ")
          ;
  test search(iterative binary search, hay stack, test cases);
  test search(recursive binary search, hay stack, test cases)
 END
END
```

**Output:**

Shows iterative search output - recursive search output is the same.

```
"A" near index 1
"Master" FOUND at index 4
"Monk" near index 8
"ZZZ" near index 8
```


## ALGOL W

Ieterative and recursive binary search procedures, from the pseudo code. Finds the left most occurance/insertion point.

```mw
begin % binary search %
    % recursive binary search, left most insertion point %
    integer procedure binarySearchLR ( integer array A ( * )
                                     ; integer value find, Low, high
                                     ) ;
        if high < low then low
        else begin
            integer mid;
            mid := ( low + high ) div 2;
            if A( mid ) >= find then binarySearchLR( A, find, low,     mid - 1 )
            else                     binarySearchLR( A, find, mid + 1, high    )
        end binarySearchR ;
    % iteratve binary search leftmost insertion point %
    integer procedure binarySearchLI ( integer array A ( * )
                                     ; integer value find, lowInit, highInit
                                     ) ;
        begin
            integer low, high;
            low  := lowInit;
            high := highInit;
            while low <= high do begin
                integer mid;
                mid := ( low + high ) div 2;
                if A( mid ) >= find then high := mid - 1
                else                     low  := mid + 1
            end while_low_le_high ;
            low
        end binarySearchLI ;
    % tests %
    begin
        integer array t ( 1 :: 10 );
        integer tPos;
        tPos := 1;
        for tValue := 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 do begin
            t( tPos ) := tValue;
            tPos      := tPOs + 1
        end for_tValue ;
        for s := 0 step 8 until 24 do begin
            integer pos;
            pos := binarySearchLR( t, s, 1, 10 );
            if t( pos ) = s then write( I_W := 3, S_W := 0, "recursive search finds           ", s, " at ", pos )
            else                 write( I_W := 3, S_W := 0, "recursive search suggests insert ", s, " at ", pos )
            ;
            pos := binarySearchLI( t, s, 1, 10 );
            if t( pos ) = s then write( I_W := 3, S_W := 0, "iterative search finds           ", s, " at ", pos )
            else                 write( I_W := 3, S_W := 0, "iterative search suggests insert ", s, " at ", pos )
        end for_s
    end
end.
```

**Output:**

```
recursive search suggests insert   0 at   1
iterative search suggests insert   0 at   1
recursive search suggests insert   8 at   3
iterative search suggests insert   8 at   3
recursive search finds            16 at   4
iterative search finds            16 at   4
recursive search suggests insert  24 at   5
iterative search suggests insert  24 at   5
```


## APL

Works with

:

Dyalog APL

APL already includes a binary search primitive (`⍸`). The following code offers an interface compatible with the requirement of this task.

```mw
binsrch←{
   ⎕IO(⍺{                       ⍝ first lower bound is start of array
       ⍵<⍺:⍬                    ⍝ if high < low, we didn't find it
       mid←⌊(⍺+⍵)÷2             ⍝ calculate mid point
       ⍺⍺[mid]>⍵⍵:⍺∇mid-1       ⍝ if too high, search from ⍺ to mid-1
       ⍺⍺[mid]<⍵⍵:(mid+1)∇⍵     ⍝ if too low, search from mid+1 to ⍵
       mid                      ⍝ otherwise, we did find it
   }⍵)⎕IO+(≢⍺)-1                ⍝ first higher bound is top of array
}
```


## AppleScript

```mw
on binarySearch(n, theList, l, r)
    repeat until (l = r)
        set m to (l + r) div 2
        if (item m of theList < n) then
            set l to m + 1
        else
            set r to m
        end if
    end repeat
    
    if (item l of theList is n) then return l
    return missing value
end binarySearch

on test(n, theList, l, r)
    set |result| to binarySearch(n, theList, l, r)
    if (|result| is missing value) then
        return (n as text) & " is not in range " & l & " thru " & r & " of the list"
    else
        return "The first occurrence of " & n & " in range " & l & " thru " & r & " of the list is at index " & |result|
    end if
end test

set theList to {1, 2, 3, 3, 5, 7, 7, 8, 9, 10, 11, 12}
return test(7, theList, 4, 11) & linefeed & test(7, theList, 7, 12) & linefeed & test(7, theList, 1, 5)
```

**Output:**

(AppleScript indices are 1-based)

```
"The first occurrence of 7 in range 4 thru 11 of the list is at index 6
The first occurrence of 7 in range 7 thru 12 of the list is at index 7
7 is not in range 1 thru 5 of the list"
```
