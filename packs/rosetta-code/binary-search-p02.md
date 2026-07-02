---
title: "Binary search (part 2/6)"
source: https://rosettacode.org/wiki/Binary_search
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/6
---

## ARM Assembly

Works with

:

as

version Raspberry Pi

```mw
/* ARM assembly Raspberry PI  */
/*  program binsearch.s   */

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
sMessResult:        .ascii "Value find at index : "
sMessValeur:        .fill 11, 1, ' '            @ size => 11
szCarriageReturn:   .asciz "\n"
sMessRecursif:      .asciz "Recursive search : \n"
sMessNotFound:      .asciz "Value not found. \n"

.equ NBELEMENTS,      9
TableNumber:	     .int   4,6,7,10,11,15,22,30,35

/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                                           @ entry of program 
    mov r0,#4                                   @ search first value
    ldr r1,iAdrTableNumber                      @ address number table
    mov r2,#NBELEMENTS                          @ number of élements 
    bl bSearch
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message

    mov r0,#11                                  @ search median value
    ldr r1,iAdrTableNumber
    mov r2,#NBELEMENTS
    bl bSearch
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message

    mov r0,#12                                  @value not found
    ldr r1,iAdrTableNumber
    mov r2,#NBELEMENTS
    bl bSearch
    cmp r0,#-1
    bne 2f
    ldr r0,iAdrsMessNotFound
    bl affichageMess 
    b 3f
2:
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message
3:
    mov r0,#35                                  @ search last value
    ldr r1,iAdrTableNumber
    mov r2,#NBELEMENTS
    bl bSearch
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message
/****************************************/
/*       recursive                      */
/****************************************/
    ldr r0,iAdrsMessRecursif
    bl affichageMess                            @ display message

    mov r0,#4                                   @ search first value
    ldr r1,iAdrTableNumber
    mov r2,#0                                   @ low index of elements
    mov r3,#NBELEMENTS - 1                      @ high index of elements
    bl bSearchR
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message
   
    mov r0,#11
    ldr r1,iAdrTableNumber
    mov r2,#0
    mov r3,#NBELEMENTS - 1
    bl bSearchR
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message
    
    mov r0,#12
    ldr r1,iAdrTableNumber
    mov r2,#0
    mov r3,#NBELEMENTS - 1
    bl bSearchR
    cmp r0,#-1
    bne 2f
    ldr r0,iAdrsMessNotFound
    bl affichageMess 
    b 3f
2:
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message
3:
    mov r0,#35
    ldr r1,iAdrTableNumber
    mov r2,#0
    mov r3,#NBELEMENTS - 1
    bl bSearchR
    ldr r1,iAdrsMessValeur                      @ display value
    bl conversion10                             @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                            @ display message

100:                                            @ standard end of the program 
    mov r0, #0                                  @ return code
    mov r7, #EXIT                               @ request to exit program
    svc #0                                      @ perform the system call

iAdrsMessValeur:          .int sMessValeur
iAdrszCarriageReturn:     .int szCarriageReturn
iAdrsMessResult:          .int sMessResult
iAdrsMessRecursif:        .int sMessRecursif
iAdrsMessNotFound:        .int sMessNotFound
iAdrTableNumber:          .int TableNumber

/******************************************************************/
/*     binary search   iterative                                  */ 
/******************************************************************/
/* r0 contains the value to search */
/* r1 contains the adress of table */
/* r2 contains the number of elements */
/* r0 return index or -1 if not find */
bSearch:
    push {r2-r5,lr}                                 @ save registers
    mov r3,#0                                       @ low index
    sub r4,r2,#1                                    @ high index = number of elements - 1
1:
    cmp r3,r4
    movgt r0,#-1                                    @not found
    bgt 100f
    add r2,r3,r4                                    @ compute (low + high) /2
    lsr r2,#1
    ldr r5,[r1,r2,lsl #2]                           @ load value of table at index r2
    cmp r5,r0
    moveq r0,r2                                     @ find !!!
    beq 100f
    addlt r3,r2,#1                                  @ lower -> index low = index + 1
    subgt r4,r2,#1                                  @ bigger -> index high = index - 1
    b 1b                                            @ and loop
100:
    pop {r2-r5,lr}
    bx lr                       @ return 
/******************************************************************/
/*     binary search   recursif                                  */ 
/******************************************************************/
/* r0 contains the value to search */
/* r1 contains the adress of table */
/* r2 contains the low index of elements */
/* r3 contains the high index of elements */
/* r0 return index or -1 if not find */
bSearchR:
    push {r2-r5,lr}                                  @ save registers
    cmp r3,r2                                        @ index high < low ?
    movlt r0,#-1                                     @ yes -> not found
    blt 100f

    add r4,r2,r3                                     @ compute (low + high) /2
    lsr r4,#1
    ldr r5,[r1,r4,lsl #2]                            @ load value of table at index r4
    cmp r5,r0
    moveq r0,r4                                      @ find !!!
    beq 100f 

    bgt 1f                                           @ bigger ?
    add r2,r4,#1                                     @ no new search with low = index + 1
    bl bSearchR
    b 100f
1:                                                   @ bigger
    sub r3,r4,#1                                     @ new search with high = index - 1
    bl bSearchR
100:
    pop {r2-r5,lr}
    bx lr                                            @ return 
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
    pop {r0,r1,r2,r7,lr}                           @ restaur des  2 registres
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

1:	                                            @ start loop
    bl divisionpar10U                               @unsigned  r0 <- dividende. quotient ->r0 reste -> r1
    add r1,#48                                      @ digit
    strb r1,[r3,r2]                                 @ store digit on area
    cmp r0,#0                                       @ stop if quotient = 0 
    subne r2,#1                                     @ else previous position
    bne 1b	                                    @ and loop
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
    mov r0,r4                                        @ result length 
    mov r1,#' '                                      @ space
3:
    strb r1,[r3,r4]                                  @ store space in area
    add r4,#1                                        @ next position
    cmp r4,#LGZONECAL
    ble 3b                                           @ loop if r4 <= area size

100:
    pop {r1-r4,lr}                                   @ restaur registres 
    bx lr                                            @return

/***************************************************/
/*   division par 10   unsigned                    */
/***************************************************/
/* r0 dividende   */
/* r0 quotient */	
/* r1 remainder  */
divisionpar10U:
    push {r2,r3,r4, lr}
    mov r4,r0                                        @ save value
    //mov r3,#0xCCCD                                 @ r3 <- magic_number lower  raspberry 3
    //movt r3,#0xCCCC                                @ r3 <- magic_number higter raspberry 3
    ldr r3,iMagicNumber                              @ r3 <- magic_number    raspberry 1 2
    umull r1, r2, r3, r0                             @ r1<- Lower32Bits(r1*r0) r2<- Upper32Bits(r1*r0) 
    mov r0, r2, LSR #3                               @ r2 <- r2 >> shift 3
    add r2,r0,r0, lsl #2                             @ r2 <- r0 * 5 
    sub r1,r4,r2, lsl #1                             @ r1 <- r4 - (r2 * 2)  = r4 - (r0 * 10)
    pop {r2,r3,r4,lr}
    bx lr                                            @ leave function 
iMagicNumber:  	.int 0xCCCCCCCD
```


## Arturo

```mw
binarySearch: function [arr,val,low,high][
    if high < low -> return ø
    mid: shr low+high 1
    when.has: val [
        [< arr\[mid]]   -> return binarySearch arr val low mid-1
        [> arr\[mid]]   -> return binarySearch arr val mid+1 high
        true            -> return mid
    ]
]

ary: [
    0 1 4 5 6 7 8 9 12 26 45 67 
    78 90 98 123 211 234 456 769 
    865 2345 3215 14345 24324
]

loop [0 42 45 24324 99999] 'v [
    i: binarySearch ary v 0 (size ary)-1
    switch not? null? i    -> print ["found" v "at index:" i]
                           -> print [v "not found"]
]
```

**Output:**

```
found 0 at index: 0 
42 not found 
found 45 at index: 10 
found 24324 at index: 24 
99999 not found
```


## AutoHotkey

```mw
array := "1,2,4,6,8,9"
StringSplit, A, array, `,   ; creates associative array
MsgBox % x := BinarySearch(A, 4, 1, A0) ; Recursive
MsgBox % A%x%
MsgBox % x := BinarySearchI(A, A0, 4)  ; Iterative
MsgBox % A%x%

BinarySearch(A, value, low, high) { ; A0 contains length of array
  If (high < low)               ; A1, A2, A3...An are array elements
    Return not_found
  mid := Floor((low + high) / 2)
  If (A%mid% > value) ; A%mid% is automatically global since no such locals are present
    Return BinarySearch(A, value, low, mid - 1)
  Else If (A%mid% < value)
    Return BinarySearch(A, value, mid + 1, high)
  Else
    Return mid
}

BinarySearchI(A, lengthA, value) {
  low := 0
  high := lengthA - 1
  While (low <= high) {
    mid := Floor((low + high) / 2) ; round to lower integer
    If (A%mid% > value)   
      high := mid - 1
    Else If (A%mid% < value)
      low := mid + 1
    Else
      Return mid
  }
  Return not_found
}
```


## AWK

Works with

:

Gawk

Works with

:

Mawk

Works with

:

Nawk

**Recursive**

```mw
function binary_search(array, value, left, right,       middle) {
    if (right < left) return 0
    middle = int((right + left) / 2)
    if (value == array[middle]) return 1
    if (value <  array[middle])
        return binary_search(array, value, left, middle - 1)
    return binary_search(array, value, middle + 1, right)
}
```

**Iterative**

```mw
function binary_search(array, value, left, right,       middle) {
    while (left <= right) {
        middle = int((right + left) / 2)
        if (value == array[middle]) return 1
        if (value <  array[middle]) right = middle - 1
        else                        left  = middle + 1
    }
    return 0
}
```


## Axe

**Iterative**

BSEARCH takes 3 arguments: a pointer to the start of the data, the data to find, and the length of the array in bytes.

```mw
Lbl BSEARCH
0→L
r₃-1→H
While L≤H
 (L+H)/2→M
 If {L+M}>r₂
  M-1→H
 ElseIf {L+M}<r₂
  M+1→L
 Else
  M
  Return
 End
End
-1
Return
```


## BASIC

**Recursive**

Works with

:

FreeBASIC

Works with

:

RapidQ

```mw
FUNCTION binary_search ( array() AS Integer, value AS Integer, lo AS Integer, hi AS Integer) AS Integer
  DIM middle AS Integer
  
  IF hi < lo THEN
    binary_search = 0
  ELSE
    middle = (hi + lo) / 2
    SELECT CASE value
      CASE IS < array(middle)
	binary_search = binary_search(array(), value, lo, middle-1)
      CASE IS > array(middle)
	binary_search = binary_search(array(), value, middle+1, hi)
      CASE ELSE
	binary_search = middle
    END SELECT
  END IF
END FUNCTION
```

**Iterative**

Works with

:

FreeBASIC

Works with

:

RapidQ

```mw
FUNCTION binary_search ( array() AS Integer, value AS Integer, lo AS Integer, hi AS Integer) AS Integer
  DIM middle AS Integer
  
  WHILE lo <= hi
    middle = (hi + lo) / 2
    SELECT CASE value
      CASE IS < array(middle)
	hi = middle - 1
      CASE IS > array(middle)
	lo = middle + 1
      CASE ELSE
	binary_search = middle
	EXIT FUNCTION
    END SELECT
  WEND
  binary_search = 0
END FUNCTION
```

**Testing the function**

The following program can be used to test both recursive and iterative version.

```mw
SUB search (array() AS Integer, value AS Integer)
  DIM idx AS Integer

  idx = binary_search(array(), value, LBOUND(array), UBOUND(array))
  PRINT "Value "; value;
  IF idx < 1 THEN
    PRINT " not found"
  ELSE
    PRINT " found at index "; idx
  END IF
END SUB

DIM test(1 TO 10) AS Integer
DIM i AS Integer

DATA 2, 3, 5, 6, 8, 10, 11, 15, 19, 20
FOR i = 1 TO 10		' Fill the test array
  READ test(i)
NEXT i

search test(), 4
search test(), 8
search test(), 20
```

Output:

```
Value 4 not found
Value 8 found at index 5
Value 20 found at index 10
```

### Applesoft BASIC

Works with

:

QBasic

Works with

:

Chipmunk Basic

Works with

:

GW-BASIC

Works with

:

MSX BASIC

Works with

:

Quite BASIC

```mw
100 REM Binary search
110 HOME : REM  110 CLS for Chipmunk Basic, MSX Basic, QBAsic and Quite BASIC
111 REM REMOVE line 110 for Minimal BASIC
120 DIM a(10)
130 LET n = 10
140 FOR j = 1 TO n
150 READ a(j)
160 NEXT j
170 REM Sorted data
180 DATA -31,0,1,2,2,4,65,83,99,782
190 LET x = 2
200 GOSUB 440
210 GOSUB 310
220 LET x = 5
230 GOSUB 440
240 GOSUB 310
250 GOTO 720
300 REM Print result
310 PRINT x;
320 IF i < 0 THEN 350
330 PRINT " is at index "; i; "."
340 RETURN
350 PRINT " is not found."
360 RETURN
400 REM Binary search algorithm
410 REM N - number of elements
420 REM X - searched element
430 REM Result: I - index of X
440 LET l = 0
450 LET h = n - 1
460 LET f = 0
470 LET m = l
480 IF l > h THEN 590
490 IF f <> 0 THEN 590
500 LET m = l + INT((h - l) / 2)
510 IF a(m) >= x THEN 540
520 LET l = m + 1
530 GOTO 480
540 IF a(m) <= x THEN 570
550 LET h = m - 1
560 GOTO 480
570 LET f = 1
580 GOTO 480
590 IF f = 0 THEN 700
600 LET i = m
610 RETURN
700 LET i = -1
710 RETURN
720 END
```

### ASIC

```mw
REM Binary search
DIM A(10)
REM Sorted data
DATA -31, 0, 1, 2, 2, 4, 65, 83, 99, 782
FOR I = 0 TO 9
  READ A(I)
NEXT I
N = 10
X = 2
GOSUB DoBinarySearch:
GOSUB PrintResult:
X = 5
GOSUB DoBinarySearch:
GOSUB PrintResult:
END

PrintResult:
PRINT X;
IF IndX >= 0 THEN
  PRINT " is at index ";
  PRINT IndX;
  PRINT "."
ELSE
  PRINT " is not found."
ENDIF
RETURN

DoBinarySearch:
REM Binary search algorithm
REM N - number of elements
REM X - searched element
REM Result: IndX - index of X
L = 0
H = N - 1
Found = 0
Loop:
  IF L > H THEN AfterLoop:
  IF Found <> 0 THEN AfterLoop:  
  REM (L <= H) and (Found = 0)
  M = H - L
  M = M / 2
  M = L + M
  REM So, M = L + (H - L) / 2
  IF A(M) < X THEN
    L = M + 1
  ELSE
    IF A(M) > X THEN
      H = M - 1
    ELSE
      Found = 1
    ENDIF
  ENDIF
  GOTO Loop:
AfterLoop:
IF Found = 0 THEN
  IndX = -1
ELSE
  IndX = M
ENDIF
RETURN
```

**Output:**

```
     2 is at index      4.
     5 is not found.
```

### BASIC256

#### Recursive Solution

```mw
function binarySearchR(array, valor, lb, ub)
    if ub < lb then
        return false
    else
        mitad = floor((lb + ub) / 2)
        if valor < array[mitad] then return binarySearchR(array, valor, lb, mitad-1)
        if valor > array[mitad] then return binarySearchR(array, valor, mitad+1, ub)
        if valor = array[mitad] then return mitad
    end if
end function
```

#### Iterative Solution

```mw
function binarySearchI(array, valor)
    lb = array[?,]
    ub = array[?]

    while lb <= ub
        mitad = floor((lb + ub) / 2)
        begin case
            case array[mitad] > valor
                ub = mitad - 1
            case array[mitad] < valor
                lb = mitad + 1
            else
                return mitad
        end case
    end while
    return false
end function
```

**Test:**

```mw
items = 10e5
dim array(items)
for n = 0 to items-1 : array[n] = n : next n

t0 = msec
print binarySearchI(array, 3)
print msec - t0; " millisec"
t1 = msec
print binarySearchR(array, 3, array[?,], array[?])
print msec - t1; " millisec"
end
```

**Output:**

```
3
839 millisec
3
50 millisec
```

### BBC BASIC

```mw
      DIM array%(9)
      array%() = 7, 14, 21, 28, 35, 42, 49, 56, 63, 70
      
      secret% = 42
      index% = FNwhere(array%(), secret%, 0, DIM(array%(),1))
      IF index% >= 0 THEN
        PRINT "The value "; secret% " was found at index "; index%
      ELSE
        PRINT "The value "; secret% " was not found"
      ENDIF
      END
      
      REM Search ordered array A%() for the value S% from index B% to T%
      DEF FNwhere(A%(), S%, B%, T%)
      LOCAL H%
      H% = 2
      WHILE H%<(T%-B%) H% *= 2:ENDWHILE
      H% /= 2
      REPEAT
        IF (B%+H%)<=T% IF S%>=A%(B%+H%) B% += H%
        H% /= 2
      UNTIL H%=0
      IF S%=A%(B%) THEN = B% ELSE = -1
```

### Chipmunk Basic

Works with

:

Chipmunk Basic

version 3.6.4

Works with

:

QBasic

Works with

:

GW-BASIC

```mw
100 rem Binary search
110 cls
120 dim a(10)
130 n% = 10
140 for i% = 0 to 9 : read a(i%) : next i%
150 rem Sorted data
160 data -31,0,1,2,2,4,65,83,99,782
170 x = 2 : gosub 280
180 gosub 230
190 x = 5 : gosub 280
200 gosub 230
210 end
220 rem Print result
230 print x;
240 if indx% >= 0 then print "is at index ";str$(indx%);"." else print "is not found."
250 return
260 rem Binary search algorithm
270 rem N% - number of elements; X - searched element; Result: INDX% - index of X
280 l% = 0 : h% = n%-1 : found% = 0
290 while (l% <= h%) and  not found%
300  m% = l%+int((h%-l%)/2)
310  if a(m%) < x then l% = m%+1 else if a(m%) > x then h% = m%-1 else found% = -1
320 wend
330 if found% = 0 then indx% = -1 else indx% = m%
340 return
```

### Craft Basic

```mw
'iterative binary search example

define size = 0, search = 0, flag = 0, value = 0
define middle = 0, low = 0, high = 0

dim list[2, 3, 5, 6, 8, 10, 11, 15, 19, 20]

arraysize size, list

let value = 4
gosub binarysearch

let value = 8
gosub binarysearch

let value = 20
gosub binarysearch

end

sub binarysearch

	let search = 1
	let middle = 0
	let low = 0
	let high = size

	do

		if low <= high then

    			let middle = int((high + low ) / 2)
			let flag = 1

     			 if value < list[middle] then

				let high = middle - 1
				let flag = 0

			endif

      			if value > list[middle] then

				let low = middle + 1
				let flag = 0

      			endif

			if flag = 1 then

				let search = 0

    			endif

		endif

	loop low <= high and search = 1

	if search = 1 then

		let middle = 0

	endif

	if middle < 1 then

		print "not found"

	endif

	if middle >= 1 then

		print "found at index ", middle

	endif

return
```

**Output:**

```
not found
found at index 4

found at index 9
```

### FreeBASIC

```mw
function binsearch( array() as integer, target as integer ) as integer
    'returns the index of the target number, or -1 if it is not in the array
    dim as uinteger lo = lbound(array), hi = ubound(array), md = (lo + hi)\2
    if array(lo) = target then return lo
    if array(hi) = target then return hi
    while lo + 1 < hi
        if array(md) = target then return md
        if array(md)<target then lo = md else hi = md
        md = (lo + hi)\2
    wend
    return -1
end function
```

### GW-BASIC

Translation of

:

ASIC

Works with

:

BASICA

```mw
10 REM Binary search
20 DIM A(10)
30 N% = 10
40 FOR I% = 0 TO 9: READ A(I%): NEXT I%
50 REM Sorted data
60 DATA -31, 0, 1, 2, 2, 4, 65, 83, 99, 782
70 X = 2: GOSUB 500
80 GOSUB 200
90 X = 5: GOSUB 500
100 GOSUB 200
110 END
190 REM Print result
200 PRINT X;
210 IF INDX% >= 0 THEN PRINT "is at index"; STR$(INDX%);"." ELSE PRINT "is not found."
220 RETURN
480 REM Binary search algorithm
490 REM N% - number of elements; X - searched element; Result: INDX% - index of X
500 L% = 0: H% = N% - 1: FOUND% = 0
510 WHILE (L% <= H%) AND NOT FOUND%
520  M% = L% + (H% - L%) \ 2
530  IF A(M%) < X THEN L% = M% + 1 ELSE IF A(M%) > X THEN H% = M% - 1 ELSE FOUND% = -1
540 WEND
550 IF FOUND% = 0 THEN INDX% = -1 ELSE INDX% = M%
560 RETURN
```

**Output:**

```
2 is at index 4.
5 is not found.
```

### IS-BASIC

```mw
100 PROGRAM "Search.bas"
110 RANDOMIZE
120 NUMERIC ARR(1 TO 20)
130 CALL FILL(ARR)
140 PRINT:INPUT PROMPT "Value: ":N
150 LET IDX=SEARCH(ARR,N)
160 IF IDX THEN
170   PRINT "The value";N;"was found the index";IDX
180 ELSE
190   PRINT "The value";N;"was not found."
200 END IF
210 DEF FILL(REF T)
220   LET T(LBOUND(T))=RND(3):PRINT T(1);
230   FOR I=LBOUND(T)+1 TO UBOUND(T)
240     LET T(I)=T(I-1)+RND(3)+1
250     PRINT T(I);
260   NEXT
270 END DEF
280 DEF SEARCH(REF T,N)
290   LET SEARCH=0:LET BO=LBOUND(T):LET UP=UBOUND(T)
300   DO
310     LET K=INT((BO+UP)/2)
320     IF T(K)<N THEN LET BO=K+1
330     IF T(K)>N THEN LET UP=K-1
340   LOOP WHILE BO<=UP AND T(K)<>N
350   IF BO<=UP THEN LET SEARCH=K
360 END DEF
```

### Liberty BASIC

```mw
dim theArray(100)
for i = 1 to 100
  theArray(i) = i
next i

print binarySearch(80,30,90)

wait

FUNCTION binarySearch(val, lo, hi)
  IF hi < lo THEN
    binarySearch = 0
  ELSE
    middle = int((hi + lo) / 2):print middle
    if val < theArray(middle) then binarySearch = binarySearch(val, lo, middle-1)
    if val > theArray(middle) then binarySearch = binarySearch(val, middle+1, hi)
    if val = theArray(middle) then binarySearch = middle
  END IF
END FUNCTION
```

### Minimal BASIC

Translation of

:

ASIC

Works with

:

Bywater BASIC

version 3.00

Works with

:

Commodore BASIC

version 3.5

Works with

:

MSX Basic

version any

Works with

:

Nascom ROM BASIC

version 4.7

```mw
10 REM Binary search
20 LET N = 10
30 FOR I = 1 TO N
40 READ A(I)
50 NEXT I
60 REM Sorted data
70 DATA -31, 0, 1, 2, 2, 4, 65, 83, 99, 782
80 LET X = 2
90 GOSUB 500
100 GOSUB 200
110 LET X = 5
120 GOSUB 500
130 GOSUB 200
140 END

190 REM Print result
200 PRINT X;
210 IF I1 < 0 THEN 240
220 PRINT "is at index"; I1; "."
230 RETURN
240 PRINT "is not found."
250 RETURN

460 REM Binary search algorithm
470 REM N - number of elements
480 REM X - searched element
490 REM Result: I1 - index of X
500 LET L = 0
510 LET H = N-1
520 LET F = 0
530 LET M = L
540 IF L > H THEN 650
550 IF F <> 0 THEN 650
560 LET M = L+INT((H-L)/2)
570 IF A(M) >= X THEN 600
580 LET L = M+1
590 GOTO 540
600 IF A(M) <= X THEN 630
610 LET H = M-1
620 GOTO 540
630 LET F = 1
640 GOTO 540
650 IF F = 0 THEN 680
660 LET I1 = M
670 RETURN
680 LET I1 = -1
690 RETURN
```

### MSX Basic

The Minimal BASIC solution works without any changes.

### Palo Alto Tiny BASIC

Translation of

:

ASIC

```mw
    10 REM BINARY SEARCH
    20 LET N=10
    30 REM SORTED DATA
    40 LET @(1)=-31,@(2)=0,@(3)=1,@(4)=2,@(5)=2
    50 LET @(6)=4,@(7)=65,@(8)=83,@(9)=99,@(10)=782
    60 LET X=2;GOSUB 500
    70 GOSUB 200
    80 LET X=5;GOSUB 500
    90 GOSUB 200
   100 STOP
   190 REM PRINT RESULT
   200 IF J<0 PRINT #1,X," IS NOT FOUND.";RETURN
   210 PRINT #1,X," IS AT INDEX ",J,".";RETURN
   460 REM BINARY SEARCH ALGORITHM
   470 REM N - NUMBER OF ELEMENTS
   480 REM X - SEARCHED ELEMENT
   490 REM RESULT: J - INDEX OF X
   500 LET L=0,H=N-1,F=0,M=L
   510 IF L>H GOTO 570
   520 IF F#0 GOTO 570
   530 LET M=L+(H-L)/2
   540 IF @(M)<X LET L=M+1;GOTO 510
   550 IF @(M)>X LET H=M-1;GOTO 510
   560 LET F=1;GOTO 510
   570 IF F=0 LET J=-1;RETURN
   580 LET J=M;RETURN
```

**Output:**

```
 2 IS AT INDEX  4.
 5 IS NOT FOUND.
```

### PureBasic

Both recursive and iterative procedures are included and called in the code below.

```mw
#Recursive = 0 ;recursive binary search method
#Iterative = 1 ;iterative binary search method
#NotFound = -1 ;search result if item not found

;Recursive
Procedure  R_BinarySearch(Array a(1), value, low, high)
  Protected mid
  If high < low
    ProcedureReturn #NotFound
  EndIf 
  
  mid = (low + high) / 2
  If a(mid) > value
    ProcedureReturn R_BinarySearch(a(), value, low, mid - 1)
  ElseIf a(mid) < value
    ProcedureReturn R_BinarySearch(a(), value, mid + 1, high)
  Else
    ProcedureReturn mid
  EndIf 
EndProcedure

;Iterative
Procedure I_BinarySearch(Array a(1), value, low, high)
  Protected mid
  While low <= high
    mid = (low + high) / 2
    If a(mid) > value            
      high = mid - 1
    ElseIf a(mid) < value
      low = mid + 1
    Else
      ProcedureReturn mid
    EndIf
  Wend

  ProcedureReturn #NotFound
EndProcedure

Procedure search (Array a(1), value, method)
  Protected idx
  
  Select method
    Case #Iterative
      idx = I_BinarySearch(a(), value, 0, ArraySize(a()))
    Default
      idx = R_BinarySearch(a(), value, 0, ArraySize(a()))
  EndSelect
  
  Print("  Value " + Str(Value))
  If idx < 0
    PrintN(" not found")
  Else
    PrintN(" found at index " + Str(idx))
  EndIf
EndProcedure

#NumElements = 9 ;zero based count
Dim test(#NumElements)

DataSection
  Data.i 2, 3, 5, 6, 8, 10, 11, 15, 19, 20
EndDataSection

;fill the test array
For i = 0 To #NumElements		
  Read test(i)
Next

If OpenConsole()

  PrintN("Recursive search:")
  search(test(), 4, #Recursive)
  search(test(), 8, #Recursive)
  search(test(), 20, #Recursive)

  PrintN("")
  PrintN("Iterative search:")
  search(test(), 4, #Iterative)
  search(test(), 8, #Iterative)
  search(test(), 20, #Iterative)

  Print(#CRLF$ + #CRLF$ + "Press ENTER to exit")
  Input()
  CloseConsole()
EndIf
```

Sample output:

```
Recursive search:
  Value 4 not found
  Value 8 found at index 4
  Value 20 found at index 9

Iterative search:
  Value 4 not found
  Value 8 found at index 4
  Value 20 found at index 9
```

### Quite BASIC

Works with

:

QBasic

Works with

:

Applesoft BASIC

Works with

:

Chipmunk Basic

Works with

:

GW-BASIC

Works with

:

Minimal BASIC

Works with

:

MSX BASIC

```mw
100 REM Binary search
110 CLS : REM  110 HOME for Applesoft BASIC : REM REMOVE for Minimal BASIC
120 DIM a(10)
130 LET n = 10
140 FOR j = 1 TO n
150 READ a(j)
160 NEXT j
170 REM Sorted data
180 DATA -31,0,1,2,2,4,65,83,99,782
190 LET x = 2
200 GOSUB 440
210 GOSUB 310
220 LET x = 5
230 GOSUB 440
240 GOSUB 310
250 GOTO 720
300 REM Print result
310 PRINT x;
320 IF i < 0 THEN 350
330 PRINT " is at index "; i; "."
340 RETURN
350 PRINT " is not found."
360 RETURN
400 REM Binary search algorithm
410 REM N - number of elements
420 REM X - searched element
430 REM Result: I - index of X
440 LET l = 0
450 LET h = n - 1
460 LET f = 0
470 LET m = l
480 IF l > h THEN 590
490 IF f <> 0 THEN 590
500 LET m = l + INT((h - l) / 2)
510 IF a(m) >= x THEN 540
520 LET l = m + 1
530 GOTO 480
540 IF a(m) <= x THEN 570
550 LET h = m - 1
560 GOTO 480
570 LET f = 1
580 GOTO 480
590 IF f = 0 THEN 700
600 LET i = m
610 RETURN
700 LET i = -1
710 RETURN
720 END
```

### Run BASIC

**Recursive**

```mw
dim theArray(100)
global theArray
for i = 1 to 100
  theArray(i) = i
next i

print binarySearch(80,30,90)

FUNCTION binarySearch(val, lo, hi)
  IF hi < lo THEN
    binarySearch = 0
  ELSE
    middle = (hi + lo) / 2
    if val < theArray(middle) then binarySearch = binarySearch(val, lo, middle-1)
    if val > theArray(middle) then binarySearch = binarySearch(val, middle+1, hi)
    if val = theArray(middle) then binarySearch = middle
  END IF
END FUNCTION
```

### TI-83 BASIC

```mw
PROGRAM:BINSEARC
:Disp "INPUT A LIST:"
:Input L1
:SortA(L1)
:Disp "INPUT A NUMBER:"
:Input A
:1→L
:dim(L1)→H
:int(L+(H-L)/2)→M
:While L<H and L1(M)≠A
:If A>M
:Then
:M+1→L
:Else
:M-1→H
:End
:int(L+(H-L)/2)→M
:End
:If L1(M)=A
:Then
:Disp A
:Disp "IS AT POSITION"
:Disp M
:Else
:Disp A
:Disp "IS NOT IN"
:Disp L1
```

### uBasic/4tH

Translation of

:

Run BASIC

The overflow is fixed - which is a bit of overkill, since uBasic/4tH has only one array of 256 elements.

```mw
For i = 1 To 100                       ' Fill array with some values
  @(i-1) = i
Next

Print FUNC(_binarySearch(50,0,99))     ' Now find value '50'
End                                    ' and prints its index

_binarySearch Param(3)                 ' value, start index, end index
  Local(1)                             ' The middle of the array

If c@ < b@ Then                        ' Ok, signal we didn't find it
  Return (-1)
Else
  d@ = SHL(b@ + c@, -1)                ' Prevent overflow (LOL!)
  If a@ < @(d@) Then Return (FUNC(_binarySearch (a@, b@, d@-1)))
  If a@ > @(d@) Then Return (FUNC(_binarySearch (a@, d@+1, c@)))
  If a@ = @(d@) Then Return (d@)       ' We found it, return index!
EndIf
```

### VBA

**Recursive version**:

```mw
Public Function BinarySearch(a, value, low, high)
'search for "value" in ordered array a(low..high)
'return index point if found, -1 if not found

  If high < low Then
    BinarySearch = -1 'not found
    Exit Function
  End If
  midd = low + Int((high - low) / 2) ' "midd" because "Mid" is reserved in VBA
  If a(midd) > value Then
    BinarySearch = BinarySearch(a, value, low, midd - 1)
  ElseIf a(midd) < value Then
    BinarySearch = BinarySearch(a, value, midd + 1, high)
  Else
    BinarySearch = midd
  End If
End Function
```

Here are some test functions:

```mw
Public Sub testBinarySearch(n)
Dim a(1 To 100)
'create an array with values = multiples of 10
For i = 1 To 100: a(i) = i * 10: Next
Debug.Print BinarySearch(a, n, LBound(a), UBound(a))
End Sub

Public Sub stringtestBinarySearch(w)
'uses BinarySearch with a string array
Dim a
a = Array("AA", "Maestro", "Mario", "Master", "Mattress", "Mister", "Mistress", "ZZ")
Debug.Print BinarySearch(a, w, LBound(a), UBound(a))
End Sub
```

and sample output:

```
stringtestBinarySearch "Master"
 3 
testBinarySearch "Master"
-1 
testBinarySearch 170
 17 
stringtestBinarySearch 170
-1 
stringtestBinarySearch "Moo"
-1 
stringtestBinarySearch "ZZ"
 7 
```

**Iterative version:**

```mw
Public Function BinarySearch2(a, value)
'search for "value" in array a
'return index point if found, -1 if not found

  low = LBound(a)
  high = UBound(a)
  Do While low <= high
    midd = low + Int((high - low) / 2)
    If a(midd) = value Then
      BinarySearch2 = midd
      Exit Function
    ElseIf a(midd) > value Then
      high = midd - 1
    Else
      low = midd + 1
    End If
 Loop
 BinarySearch2 = -1 'not found
End Function
```

### VBScript

Translation of

:

BASIC

**Recursive**

```mw
Function binary_search(arr,value,lo,hi)
		If hi < lo Then
			binary_search = 0
		Else
			middle=Int((hi+lo)/2)
			If value < arr(middle) Then
				binary_search = binary_search(arr,value,lo,middle-1)
			ElseIf value > arr(middle) Then
				binary_search = binary_search(arr,value,middle+1,hi)
			Else
				binary_search = middle
				Exit Function
			End If
		End If
End Function

'Tesing the function.
num_range = Array(2,3,5,6,8,10,11,15,19,20)
n = CInt(WScript.Arguments(0))
idx = binary_search(num_range,n,LBound(num_range),UBound(num_range))
If idx > 0 Then
	WScript.StdOut.Write n & " found at index " & idx
	WScript.StdOut.WriteLine
Else
	WScript.StdOut.Write n & " not found"
	WScript.StdOut.WriteLine
End If
```

**Output:**

**Note: Array index starts at 0.**

```
C:\>cscript /nologo binary_search.vbs 4
4 not found

C:\>cscript /nologo binary_search.vbs 8
8 found at index 4

C:\>cscript /nologo binary_search.vbs 20
20 found at index 9
```

### Visual Basic .NET

**Iterative**

```mw
Function BinarySearch(ByVal A() As Integer, ByVal value As Integer) As Integer
    Dim low As Integer = 0
    Dim high As Integer = A.Length - 1
    Dim middle As Integer = 0

    While low <= high
        middle = (low + high) / 2
        If A(middle) > value Then
            high = middle - 1
        ElseIf A(middle) < value Then
            low = middle + 1
        Else
            Return middle
        End If
    End While

    Return Nothing
End Function
```

**Recursive**

```mw
Function BinarySearch(ByVal A() As Integer, ByVal value As Integer, ByVal low As Integer, ByVal high As Integer) As Integer
    Dim middle As Integer = 0

    If high < low Then
        Return Nothing
    End If

    middle = (low + high) / 2

    If A(middle) > value Then
        Return BinarySearch(A, value, low, middle - 1)
    ElseIf A(middle) < value Then
        Return BinarySearch(A, value, middle + 1, high)
    Else
        Return middle
    End If
End Function
```

### Yabasic

Translation of

:

Lua

```mw
sub floor(n)
    return int(n + .5)
end sub

sub binarySearch(list(), value)
    local low, high, mid
    
    low = 1 : high = arraysize(list(), 1)

    while(low <= high)
        mid = floor((low + high) / 2)
        if list(mid) > value then
            high = mid - 1
        elsif list(mid) < value then
            low = mid + 1
        else
            return mid
        end if
    wend
    return false
end sub

ITEMS = 10e6

dim list(ITEMS)

for n = 1 to ITEMS
    list(n) = n
next n

print binarySearch(list(), 3)
print peek("millisrunning")
```

### ZX Spectrum Basic

Translation of

:

FreeBASIC

Iterative method:

```mw
10 DATA 2,3,5,6,8,10,11,15,19,20
20 DIM t(10)
30 FOR i=1 TO 10
40 READ t(i)
50 NEXT i
60 LET value=4: GO SUB 100
70 LET value=8: GO SUB 100
80 LET value=20: GO SUB 100
90 STOP 
100 REM Binary search
110 LET lo=1: LET hi=10
120 IF lo>hi THEN LET idx=0: GO TO 170
130 LET middle=INT ((hi+lo)/2)
140 IF value<t(middle) THEN LET hi=middle-1: GO TO 120
150 IF value>t(middle) THEN LET lo=middle+1: GO TO 120
160 LET idx=middle
170 PRINT "Value ";value;
180 IF idx=0 THEN PRINT " not found": RETURN 
190 PRINT " found at index ";idx: RETURN
```


## Batch File

```mw
@echo off & setlocal enabledelayedexpansion

:: Binary Chop Algorithm - Michael Sanders 2017
::
:: example output...
::
:: binary chop algorithm vs. standard for loop
::
:: number to find 941
:: for loop required 941 iterations
:: binchop required 10 iterations

:setup

   set x=1
   set y=999
   set /a z=(%random% * (%y% - 1) / 32768 + 1)

:pseudoarray

   for /l %%q in (%x%,1,%y%) do set /a array[%%q]=%%q

:std4loop

   for /l %%q in (%x%,1,%y%) do (
      if !array[%%q]!==%z% (set f=%%q& goto :binchop)
   )

:binchop

   if !x! leq !y! (
      set /a i+=1
      set /a "p=(!x!+!y!)/2"
      call set /a t=%%array[!p!]%%
      if !t! equ !z! (set b=!i!& goto :done)
      if !t! lss !z! (set /a x=!p!+1) else (set /a y=!p!-1)
      goto :binchop
   )

:done

   cls
   echo binary chop algorithm vs. standard for loop...
   echo.
   echo . number to find !z!
   echo . for loop required !f! iterations
   echo . binchop required !b! iterations
   endlocal & exit /b 0
```


## BQN

BQN has two builtin functions for binary search: `⍋`(Bins Up) and `⍒`(Bins Down). This is a recursive method.

```mw
BSearch ← {
  BS ⟨a, value⟩:
  BS ⟨a, value, 0, ¯1+≠a⟩;
  BS ⟨a, value, low, high⟩:
  mid ← ⌊2÷˜low+high
  {
    high<low ? ¯1;
    (mid⊑a)>value ? BS ⟨a, value, low, mid-1⟩;
    (mid⊑a)<value ? BS ⟨a, value, mid+1, high⟩;
    mid
  }
}

•Show BSearch ⟨8‿30‿35‿45‿49‿77‿79‿82‿87‿97, 97⟩
```

```mw
9
```


## Brat

```mw
binary_search = { search_array, value, low, high |
  true? high < low
    { null }
    {
      mid = ((low + high) / 2).to_i
      
      true? search_array[mid] > value
        { binary_search search_array, value, low, mid - 1 }
	{ true? search_array[mid] < value
	  { binary_search search_array, value, mid + 1, high }
	  { mid }
      }
   }
}

#Populate array
numbers = 1000.of { random 1000 }

#Sort the array
numbers.sort!

#Find a number
x = random 1000

p "Looking for #{x}"

index = binary_search numbers, x, 0, numbers.length - 1

null? index
	{ p "Not found" }
	{ p "Found at index: #{index}" }
```


## Bruijn

```mw
:import std/Combinator .
:import std/Math .
:import std/List .
:import std/Option .

binary-search [y [[[[[2 <? 3 none go]]]]] (+0) --(∀0) 0]
	go [compare-case eq lt gt (2 !! 0) 1] /²(3 + 2)
		eq some 0
		lt 5 4 --0 2 1
		gt 5 ++0 3 2 1

# example using sorted list of x^3, x=[-50,50]
find [[map-or "not found" [0 : (1 !! 0)] (binary-search 0 1)] lst]
	lst take (+100) ((\pow (+3)) <$> (iterate ++‣ (-50)))

:test (find (+100)) ("not found")
:test ((head (find (+125))) =? (+55)) ([[1]])
:test ((head (find (+117649))) =? (+99)) ([[1]])
```


## C

```mw
#include <stdio.h>

int bsearch (int *a, int n, int x) {
    int i = 0, j = n - 1;
    while (i <= j) {
        int k = i + ((j - i) / 2);
        if (a[k] == x) {
            return k;
        }
        else if (a[k] < x) {
            i = k + 1;
        }
        else {
            j = k - 1;
        }
    }
    return -1;
}

int bsearch_r (int *a, int x, int i, int j) {
    if (j < i) {
        return -1;
    }
    int k = i + ((j - i) / 2);
    if (a[k] == x) {
        return k;
    }
    else if (a[k] < x) {
        return bsearch_r(a, x, k + 1, j);
    }
    else {
        return bsearch_r(a, x, i, k - 1);
    }
}

int main () {
    int a[] = {-31, 0, 1, 2, 2, 4, 65, 83, 99, 782};
    int n = sizeof a / sizeof a[0];
    int x = 2;
    int i = bsearch(a, n, x);
    if (i >= 0)  
      printf("%d is at index %d.\n", x, i);
    else
      printf("%d is not found.\n", x);
    x = 5;
    i = bsearch_r(a, x, 0, n - 1);
    if (i >= 0)  
      printf("%d is at index %d.\n", x, i);
    else
      printf("%d is not found.\n", x);
    return 0;
}
```

**Output:**

```
2 is at index 4.
5 is not found.
```
