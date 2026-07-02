---
title: "100 doors (part 2/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/10
---

## ARM Assembly

Works with

:

as

version Raspberry Pi

**unoptimized**

```mw
/* ARM assembly Raspberry PI  */
/*  program 100doors.s   */

/************************************/
/* Constantes                       */
/************************************/
.equ STDOUT, 1                                 @ Linux output console
.equ EXIT,   1                                 @ Linux syscall
.equ WRITE,  4                                 @ Linux syscall
.equ NBDOORS,   100
/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:       .ascii "The door "
sMessValeur:       .fill 11, 1, ' '            @ size => 11
                      .asciz "is open.\n"

/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
stTableDoors:	.skip   4 * NBDOORS
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                                         @ entry of program 
    push {fp,lr}                              @ saves 2 registers 
    @ display first line
    ldr r3,iAdrstTableDoors                   @ table address
    mov r5,#1            
1:
    mov r4,r5
2:                                            @ begin loop
    ldr r2,[r3,r4,lsl #2]                     @ read doors index r4
    cmp r2,#0
    moveq r2,#1                               @ if r2 = 0   1 -> r2
    movne r2,#0                               @ if r2 = 1   0 -> r2
    str r2,[r3,r4,lsl #2]                     @ store value of doors
    add r4,r5                                 @ increment r4 with  r5 value
    cmp r4,#NBDOORS                           @ number of doors ?
    ble 2b                                    @ no -> loop
    add r5,#1                                 @ increment the increment !!
    cmp r5,#NBDOORS                           @ number of doors ?
    ble 1b                                    @ no -> loop

                                              @ loop display state doors
    mov r4,#0              
3:
    ldr r2,[r3,r4,lsl #2]                     @ read state doors r4 index
    cmp r2,#0
    beq 4f
    mov r0,r4                                 @ open -> display message
    ldr r1,iAdrsMessValeur                    @ display value index
    bl conversion10                           @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                          @ display message
4:
    add r4,#1
    cmp r4,#NBDOORS
    ble 3b                                    @ loop
 

100:                                          @ standard end of the program 
    mov r0, #0                                @ return code
    pop {fp,lr}                               @restaur 2 registers
    mov r7, #EXIT                             @ request to exit program
    svc #0                                    @ perform the system call

iAdrsMessValeur:                .int sMessValeur
iAdrstTableDoors:		.int stTableDoors
iAdrsMessResult:		.int sMessResult

/******************************************************************/
/*     display text with size calculation                         */ 
/******************************************************************/
/* r0 contains the address of the message */
affichageMess:
    push {r0,r1,r2,r7,lr}                     @ save  registres
    mov r2,#0                                 @ counter length 
1:                                            @ loop length calculation 
    ldrb r1,[r0,r2]                           @ read octet start position + index 
    cmp r1,#0                                 @ if 0 its over 
    addne r2,r2,#1                            @ else add 1 in the length 
    bne 1b                                    @ and loop 
                                              @ so here r2 contains the length of the message 
    mov r1,r0        			      @ address message in r1 
    mov r0,#STDOUT      		      @ code to write to the standard output Linux 
    mov r7, #WRITE                            @ code call system "write" 
    svc #0                                    @ call systeme 
    pop {r0,r1,r2,r7,lr}                      @ restaur des  2 registres */ 
    bx lr                                     @ return  
/******************************************************************/
/*     Converting a register to a decimal unsigned                */ 
/******************************************************************/
/* r0 contains value and r1 address area   */
/* r0 return size of result (no zero final in area) */
/* area size => 11 bytes          */
.equ LGZONECAL,   10
conversion10:
    push {r1-r4,lr}                            @ save registers 
    mov r3,r1
    mov r2,#LGZONECAL

1:	                                       @ start loop
    bl divisionpar10U                          @unsigned  r0 <- dividende. quotient ->r0 reste -> r1
    add r1,#48                                 @ digit	
    strb r1,[r3,r2]                            @ store digit on area
    cmp r0,#0                                  @ stop if quotient = 0 
    subne r2,#1                                @ else previous position
    bne 1b	                               @ and loop
    // and move digit from left of area
    mov r4,#0
2:
    ldrb r1,[r3,r2]
    strb r1,[r3,r4]
    add r2,#1
    add r4,#1
    cmp r2,#LGZONECAL
    ble 2b
    // and move spaces in end on area
    mov r0,r4                                 @ result length 
    mov r1,#' '                               @ space	
3:
    strb r1,[r3,r4]                           @ store space in area
    add r4,#1                                 @ next position
    cmp r4,#LGZONECAL
    ble 3b                                    @ loop if r4 <= area size

100:
    pop {r1-r4,lr}                            @ restaur registres 
    bx lr                                     @return

/***************************************************/
/*   division par 10   unsigned                    */
/***************************************************/
/* r0 dividende   */
/* r0 quotient */	
/* r1 remainder  */
divisionpar10U:
    push {r2,r3,r4, lr}
    mov r4,r0                                        @ save value
    //mov r3,#0xCCCD                                 @ r3 <- magic_number  lower   @ for Raspberry pi 3
    //movt r3,#0xCCCC                                @ r3 <- magic_number  upper   @ for Raspberry pi 3
    ldr r3,iMagicNumber                              @ for Raspberry pi 1 2
    umull r1, r2, r3, r0                             @ r1<- Lower32Bits(r1*r0) r2<- Upper32Bits(r1*r0) 
    mov r0, r2, LSR #3                               @ r2 <- r2 >> shift 3
    add r2,r0,r0, lsl #2                             @ r2 <- r0 * 5 
    sub r1,r4,r2, lsl #1                             @ r1 <- r4 - (r2 * 2)  = r4 - (r0 * 10)
    pop {r2,r3,r4,lr}
    bx lr                                            @ leave function 
iMagicNumber:            .int 0xCCCCCCCD
```

**optimized**

```mw
/*********************************************/
/* optimized version                         */
/*********************************************/
/* ARM assembly Raspberry PI  */
/*  program 100doors.s   */

/************************************/
/* Constantes                       */
/************************************/
.equ STDOUT, 1     @ Linux output console
.equ EXIT,   1     @ Linux syscall
.equ WRITE,  4     @ Linux syscall
.equ NBDOORS,   100
/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:       .ascii "The door "
sMessValeur:       .fill 11, 1, ' '                 @ size => 11
                   .asciz "is open.\n"

/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                                               @ entry of program 
    push {fp,lr}                                    @ saves 2 registers 
                                                    @ display first line
    mov r5,#3                                       @ start value of increment
    mov r4,#1                                       @ start doors
                                                    @ loop display state doors
1:
    mov r0,r4                                       @ open -> display message
    ldr r1,iAdrsMessValeur                          @ display value index
    bl conversion10                                 @ call function
    ldr r0,iAdrsMessResult
    bl affichageMess                                @ display message
    add r4,r5                                       @ add increment
    add r5,#2                                       @ new increment
    cmp r4,#NBDOORS
    ble 1b                                          @ loop
 

100:   @ standard end of the program 
    mov r0, #0                                      @ return code
    pop {fp,lr}                                     @ restaur 2 registers
    mov r7, #EXIT                                   @ request to exit program
    svc #0                                          @ perform the system call

iAdrsMessValeur:                .int sMessValeur
iAdrsMessResult:		.int sMessResult

/******************************************************************/
/*     display text with size calculation                         */ 
/******************************************************************/
/* r0 contains the address of the message */
affichageMess:
    push {r0,r1,r2,r7,lr}                           @ save  registres
    mov r2,#0                                       @ counter length 
1:                                                  @ loop length calculation 
    ldrb r1,[r0,r2]                                 @ read octet start position + index 
    cmp r1,#0                                       @ if 0 its over 
    addne r2,r2,#1                                  @ else add 1 in the length 
    bne 1b                                          @ and loop 
                                                    @ so here r2 contains the length of the message 
    mov r1,r0        			            @ address message in r1 
    mov r0,#STDOUT      		            @ code to write to the standard output Linux 
    mov r7, #WRITE                                  @ code call system "write" 
    svc #0                                          @ call systeme 
    pop {r0,r1,r2,r7,lr}                            @ restaur des  2 registres */ 
    bx lr                                           @ return  
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
    bl divisionpar10U                               @ unsigned  r0 <- dividende. quotient ->r0 reste -> r1
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
    mov r0,r4                                       @ result length 
    mov r1,#' '                                     @ space	
3:
    strb r1,[r3,r4]                                 @ store space in area
    add r4,#1                                       @ next position
    cmp r4,#LGZONECAL
    ble 3b                                          @ loop if r4 <= area size

100:
    pop {r1-r4,lr}                                  @ restaur registres 
    bx lr                                           @return

/***************************************************/
/*   division par 10   unsigned                    */
/***************************************************/
/* r0 dividende   */
/* r0 quotient */	
/* r1 remainder  */
divisionpar10U:
    push {r2,r3,r4, lr}
    mov r4,r0                                       @ save value
    //mov r3,#0xCCCD                                @ r3 <- magic_number  lower   @ for raspberry 3
    //movt r3,#0xCCCC                               @ r3 <- magic_number  upper   @ for raspberry 3
    ldr r3,iMagicNumber                             @ for raspberry 1 2
    umull r1, r2, r3, r0                            @ r1<- Lower32Bits(r1*r0) r2<- Upper32Bits(r1*r0) 
    mov r0, r2, LSR #3                              @ r2 <- r2 >> shift 3
    add r2,r0,r0, lsl #2                            @ r2 <- r0 * 5 
    sub r1,r4,r2, lsl #1                            @ r1 <- r4 - (r2 * 2)  = r4 - (r0 * 10)
    pop {r2,r3,r4,lr}
    bx lr                                           @ leave function 
iMagicNumber:            .int 0xCCCCCCCD
```


## Arturo

```mw
isOpen: map 1..101 => false
 
loop 1..100 'pass ->
	loop (range.step:pass pass 100) 'door [
		isOpen\[door]: not? isOpen\[door]
	]

loop 1..100 'x ->
	if isOpen\[x] [
		print ["Door" x "is open."]
	]
```

**Output:**

```
Door 1 is open. 
Door 4 is open. 
Door 9 is open. 
Door 16 is open. 
Door 25 is open. 
Door 36 is open. 
Door 49 is open. 
Door 64 is open. 
Door 81 is open. 
Door 100 is open.
```


## Astro

```mw
var doors = falses(100)

for a in 1..100: for b in a..a..100:
    doors[b] = not doors[b]

for a in 1..100:
    print "Door $a is ${(doors[a]) ? 'open.': 'closed.'}"
```


## Asymptote

```mw
for(int i = 1; i < 100; ++i) {
    if (i % i^2 < 11)  {
      write("Door ", i^2, suffix=none);
      write(" is open");
    }
  }
```


## ATS

```mw
#include "share/atspre_staload.hats"

implement
main0((*void*)) = let
//
var A = @[bool][100](false)
val A = $UNSAFE.cast{arrayref(bool,100)}(addr@A)
//
fnx
loop
(
  pass: intGte(0)
) : void =
  if pass < 100
    then loop2 (pass, pass)
  // end of [if]
and
loop2
(
  pass: natLt(100), door: intGte(0)
) : void =
  if door < 100
    then (A[door] := ~A[door]; loop2(pass, door+pass+1))
    else loop(pass+1)
  // end of [if]
//
fun
loop3
(
  door: intGte(0)
) : void =
  if door < 100
    then (
      println!("door #", door+1, " is ", (if A[door] then "open" else "closed"): string, ".");
      loop3(door+1)
    ) (* end of [then] *)
  // end of [if]
//
in
  loop(0); loop3 (0)
end // end of [main0]
```


## AutoHotkey

### Standard Approach

```mw
Loop, 100
  Door%A_Index% := "closed"

Loop, 100 {
  x := A_Index, y := A_Index
  While (x <= 100)
  {
    CurrentDoor := Door%x%
    If CurrentDoor contains closed
    {
      Door%x% := "open"
      x += y
    }
    else if CurrentDoor contains open
    {
      Door%x% := "closed"
      x += y
    }
  }
}

Loop, 100 {
   CurrentDoor := Door%A_Index%
   If CurrentDoor contains open
      Res .= "Door " A_Index " is open`n"
}
MsgBox % Res
```

### Alternative Approach

Making use of the identity:

${\displaystyle \sum _{i=1}^{n}(2i-1)=n^{2}}$

```mw
increment := 3, square := 1 
Loop, 100 
    If (A_Index = square) 
        outstring .= "`nDoor " A_Index " is open" 
        ,square += increment, increment += 2 
MsgBox,, Succesfull, % SubStr(outstring, 2)
```

### Optimized

```mw
While (Door := A_Index ** 2) <= 100
   Result .= "Door " Door " is open`n"
MsgBox, %Result%
```


## AutoIt

```mw
#include <array.au3>
$doors = 100

;door array, 0 = closed, 1 = open
Local $door[$doors +1]

For $ii = 1 To $doors
	For $i = $ii To $doors Step $ii
		$door[$i] = Not $door[$i]
	next
Next

;display to screen
For $i = 1 To $doors
	ConsoleWrite (Number($door[$i])& " ")
	If Mod($i,10) = 0 Then ConsoleWrite(@CRLF)
Next
```


## AutoLISP

```mw
(defun CreateDoors (n / doors)
  (repeat n
    (setq doors (cons nil doors))
  )
)

(defun Doors (doors / cnt)
  (setq cnt 0)
  (mapcar
   '(lambda (d)
      (zerop (rem (sqrt (setq cnt (1+ cnt))) 1))
    )
    doors
  )
)

> (Doors (CreateDoors 100))
(T nil nil T nil nil nil nil T nil nil nil nil nil nil T nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil nil T nil nil nil nil)
```


## AWK

**unoptimized**

```
BEGIN {
  for(i=1; i <= 100; i++)
  {
    doors[i] = 0 # close the doors
  }
  for(i=1; i <= 100; i++)
  {
    for(j=i; j <= 100; j += i)
    {
      doors[j] = (doors[j]+1) % 2
    }
  }
  for(i=1; i <= 100; i++)
  {
    print i, doors[i] ? "open" : "close"
  }
}
```

**optimized**

```
BEGIN {
  for(i=1; i <= 100; i++) {
    doors[i] = 0 # close the doors
  }
  for(i=1; i <= 100; i++) {
    if ( int(sqrt(i)) == sqrt(i) ) {
      doors[i] = 1
    }
  }
  for(i=1; i <= 100; i++)
  {
    print i, doors[i] ? "open" : "close"
  }
}
```


## Axiom

Unoptimized:

```mw
(open,closed,change,open?) := (true,false,not,test);
doors := bits(100,closed);
for i in 1..#doors repeat
  for j in i..#doors by i repeat
    doors.j := change doors.j
[i for i in 1..#doors | open? doors.i]
```

Optimized:

```mw
[i for i in 1..100 | perfectSquare? i] -- or
[i^2 for i in 1..sqrt(100)::Integer]
```


## B

Works with

:

The Amsterdam Compiler Kit - B

version V6.1pre1

```mw
main()
{
  auto doors[100]; /* != 0 means open */
  auto pass, door;

  door = 0;
  while( door<100 ) doors[door++] = 0;

  pass = 0;
  while( pass<100 )
  {
    door = pass;
    while( door<100 )
    {
      doors[door] = !doors[door];
      door =+ pass+1;
    }
    ++pass;
  }

  door = 0;
  while( door<100 )
  {
    printf("door #%d is %s.*n", door+1, doors[door] ? "open" : "closed");
    ++door;
  }

  return(0);
}
```


## BabyCobol

```mw
      * NB: the implementation is rather vanilla
      * besides using the idiomatic buffer overrun.
      * LOOP is what PERFORM in COBOL is, with defaults.
      * MOVE in this language acts like OVE CORRESPONDING,
      * which is actually good here.
       IDENTIFICATION DIVISION.
           PROGRAM-ID. ONE HUNDRED DOORS.
       DATA DIVISION.
       01 I PICTURE IS 9(3).
       01 J LIKE I.
       01 DOOR PICTURE IS 9 OCCURS 100 TIMES.
       01 STOP LIKE DOOR.
       PROCEDURE DIVISION.
      * Initialise the data
           MOVE HIGH-VALUES TO STOP
           MOVE SPACES TO DOOR.
      * Do the main algorithm
           LOOP VARYING I UNTIL DOOR(I) = 9
               LOOP VARYING J FROM I TO 100 BY I
                   SUBTRACT DOOR (J) FROM 1 GIVING DOOR (J)
               END
           END.
      * Print the results
           LOOP VARYING I UNTIL DOOR(I) = 9
               DISPLAY "Door" I "is" WITH NO ADVANCING
               IF DOOR (I) = 1
               THEN DISPLAY "open"
               ELSE DISPLAY "closed".
           END.
```


## BaCon

```mw
OPTION BASE 1

DECLARE doors[100]

FOR size = 1 TO 100
    FOR pass = 0 TO 100 STEP size
	doors[pass] = NOT(doors[pass])
    NEXT
NEXT

FOR which = 1 TO 100
    IF doors[which] THEN PRINT which
NEXT
```

**Output:**

```
1
4
9
16
25
36
49
64
81
100
```


## Bait

```mw
const NUM_DOORS := 100

fun main() {
	// All doors are closed by default (`false`)
	mut is_open := []bool{length = NUM_DOORS}

	// Make 100 passes by the doors
	for pass := 0; pass < 100; pass += 1 {
		// Only visit every `pass + 1`th door
		for door := pass; door < NUM_DOORS; door += pass + 1 {
			is_open[door] = not is_open[door]
		}
	}

	// Print the doors that are open
	for i, open in is_open {
		if open {
			println("Door #${i + 1} is open.")
		}
	}

}
```

**Output:**

```
Door #1 is open.
Door #4 is open.
Door #9 is open.
Door #16 is open.
Door #25 is open.
Door #36 is open.
Door #49 is open.
Door #64 is open.
Door #81 is open.
Door #100 is open.
```


## Ballerina

```mw
// https://rosettacode.org/wiki/100_doors
import ballerina/io;

public function main() {
    boolean[100] doors = [];
    foreach int i in int:range(0,100,1) {
        foreach int j in int:range(i, 100, i+1) {
            doors[j] = ! doors[j];
        }
    }
    foreach int i in int:range(0,doors.length(),1) {
        if doors[i] {
            io:println("Door #",i+1," is ","open");
        }
    }
}
```

**Output:**

```
Door #1 is open
Door #4 is open
Door #9 is open
Door #16 is open
Door #25 is open
Door #36 is open
Door #49 is open
Door #64 is open
Door #81 is open
Door #100 is open
```


## BASIC

### ANSI BASIC

Translation of

:

ALGOL 68

Works with

:

Decimal BASIC

```mw
100 REM 100 doors
110 REM The unoptimised door flipping method
120 REM which simulates the process
130 DIM IsDoorOpen(1 TO 100)
140 LET DoorMax = UBOUND(IsDoorOpen)
150 REM Set all doors to closed
160 FOR I = 1 TO DoorMax
170    LET IsDoorOpen(I) = 0
180 NEXT I
190 REM Repeatedly flip the doors
200 FOR I = 1 TO DoorMax
210    FOR J = I TO DoorMax STEP I 
220       LET IsDoorOpen(J) = 1 - IsDoorOpen(J)
230    NEXT J
240 NEXT I
250 REM Display the results
260 FOR I = 1 TO DoorMax   
270    IF IsDoorOpen(I) <> 0 THEN PRINT I;
280 NEXT I
290 PRINT
300 END
```

**Output:**

```
 1  4  9  16  25  36  49  64  81  100 
```

### Applesoft BASIC

Based on the Sinclair ZX81 BASIC implementation.

```mw
 100 :
 110  REM  100 DOORS PROBLEM
 120 :
 130  DIM D(100)
 140  FOR P = 1 TO 100
 150  FOR T = P TO 100 STEP P
 160  D(T) =  NOT D(T): NEXT T
 170  NEXT P
 180  FOR I = 1 TO 100
 190  IF D(I) THEN  PRINT I;" ";
 200  NEXT I
```

**Output:**

```
                                        
]RUN
1 4 9 16 25 36 49 64 81 100
```

### BASIC256

```mw
# 100 doors problem
dim d(100)

# simple solution
print "simple solution"
gosub initialize
for t = 1 to 100
   for j = t to 100 step t
      d[j-1] = not d[j-1]
   next j
next t
gosub showopen

# more optimized solution
print "more optimized solution"
gosub initialize
for t = 1 to 10
      d[t^2-1] = true
next t
gosub showopen
end

initialize:
for t = 1 to d[?]
   d[t-1] = false	 # closed
next t
return

showopen:
for t = 1 to d[?]
   print d[t-1]+ " ";
   if t%10 = 0 then print
next t
return
```

**ultra optimizado**: portado desde la versión Julia

```mw
for i = 1 to 10 : if i % i^2 < 11 then print "La puerta "; int(i^2); " esta abierta" : end if : next i : end
```

### BazzBasic

```mw
' ============================================
' 100 DOORS - BazzBasic Edition
' https://rosettacode.org/wiki/100_doors
' BazzBasic: https://github.com/EkBass/BazzBasic
' ============================================
' 100 doors, all closed. 100 passes:
' Pass N toggles every Nth door.
' Which doors are open after all passes?
' ============================================

[inits]
	LET DOORS# = 100
	DIM door$

	' Initialize all doors to 0 (closed)
	FOR d$ = 1 TO DOORS#
		door$(d$) = 0
	NEXT

[simulate]
	FOR pass$ = 1 TO DOORS#
		FOR d$ = pass$ TO DOORS# STEP pass$
			door$(d$) = 1 - door$(d$)
		NEXT
	NEXT

[report]
	CLS
	PRINT "100 Doors — rosettacode.org/wiki/100_doors"
	PRINT REPEAT("=", 44)
	PRINT ""
	PRINT "Open doors after all 100 passes:"
	PRINT ""

	LET count$ = 0
	FOR d$ = 1 TO DOORS#
		IF door$(d$) = 1 THEN
			PRINT "  Door "; d$
			count$ = count$ + 1
		END IF
	NEXT

	PRINT ""
	PRINT REPEAT("-", 44)
	PRINT count$; " doors open  (the perfect squares 1..100)"
	PRINT ""
	PRINT "Press any key...";
	WAITKEY()
END
```

### CBASIC

Works with

:

CBASIC 2

Works with

:

CB80

```mw
dim doors%(100)

print "Finding solution to the 100 Doors Problem"

rem - all doors are initially closed
for i% = 1 to 100
  doors%(i%) = 0
next i%

rem - pass through at increasing intervals
for i% = 1 to 100
  for j% = i% to 100 step i%
    rem - flip each door encountered
    doors%(j%) = 1 - doors%(j%)
  next j%
next i%

rem - show which doors are open
print "The open doors are: ";
for i% = 1 to 100
  if doors%(i%) = 1 then print i%;
next i%

print
print "Thanks for consulting the puzzle guru!"

end
```

**Output:**

```
Finding solution to the 100 Doors Problem
The open doors are: 1 4 9 15 25 36 47 64 81 100
Thanks for consulting the puzzle guru!
```

### Chipmunk Basic

Works with

:

Chipmunk Basic

version 3.6.4

Works with

:

Applesoft BASIC

Works with

:

QBasic

Works with

:

GW-BASIC

Based on the Sinclair ZX81 BASIC implementation.

```mw
100 CLS : REM  10 HOME for Applesoft BASIC
110 DIM D(100)
120 FOR P = 1 TO 100
130   FOR T = P TO 100 STEP P
140     D(T) = NOT D(T)
150   NEXT T
160 NEXT P
170 ' Print "opened" doors
180 FOR I = 1 TO 100
190   IF D(I) THEN PRINT I;" ";
200 NEXT I
210 END
```

**Output:**

```
>RUN
1  4  9  16  25  36  49  64  81  100  >
```

### Commodore BASIC

Based on the Sinclair ZX81 BASIC implementation.

```mw
10 DIM D(100)
20 FOR I=1 TO 100
30 FOR J=I TO 100 STEP I
40 D(J) = NOT D(J)
50 NEXT J
60 NEXT I
70 FOR I=1 TO 100
80 IF D(I) THEN PRINT I,
90 NEXT I
```

### GW-BASIC

Works with

:

Applesoft BASIC

Works with

:

Chipmunk Basic

Works with

:

QBasic

Based on the Sinclair ZX81 BASIC implementation.

```mw
100 CLS : REM  10 HOME for Applesoft BASIC
110 DIM D(100)
120 FOR P = 1 TO 100
130   FOR T = P TO 100 STEP P
140     D(T) = NOT D(T)
150   NEXT T
160 NEXT P
170 ' Print "opened" doors
180 FOR I = 1 TO 100
190   IF D(I) THEN PRINT I;" ";
200 NEXT I
210 END
```

**Output:**

```
  1  4  9  16  25  36  49  64  81  100
```

### IS-BASIC

```mw
100 PROGRAM "100doors.bas"
110 NUMERIC D(1 TO 100)
120 FOR I=1 TO 100
130   LET D(I)=0
140 NEXT
150 FOR I=1 TO 100
160   FOR J=I TO 100 STEP I
170     LET D(J)=NOT D(J)
180   NEXT 
190 NEXT
200 FOR I=1 TO 100
210   IF D(I) THEN PRINT I
220 NEXT
```

Optimized:

```mw
100 PROGRAM "100doors.bas"
110 LET NR=1:LET D=3
120 DO
130   PRINT NR
140   LET NR=NR+D:LET D=D+2
150 LOOP WHILE NR<=100
```

### Minimal BASIC

Works with

:

IS-BASIC

```mw
10 PRINT "FOLLOWING DOORS ARE OPEN:"
20 LET I = 0
30 REM LOOP
40 LET I = I + 1
50 PRINT I * I; " ";
60 IF I * I < 100 THEN 30
70 END
```

### MoonRock

Translation of

:

ALGOL W

Works with

:

MoonRock

version 0.50

```mw
' 100 doors

BEGIN DEF
%DoorMax = 100
%LastI = %DoorMax - 1
DIM DoorOpen%[%DoorMax]

BEGIN CODE
' The unoptimised door flipping method
' which simulates the process
' Set all doors to closed
FOR I% = 0 TO %LastI
  DoorOpen%[I%] = FALSE
NEXT
' Repeatedly flip the doors
FOR I% = 1 TO %DoorMax
  J% = I% - 1 
  WHILE J% < %DoorMax
    IF DoorOpen%[J%] = TRUE THEN
      DoorOpen%[J%] = FALSE
    ELSE
      DoorOpen%[J%] = TRUE
    ENDIF
    J% = J% + I%   
  WEND
NEXT
' Display the results
FOR I% = 0 TO %LastI 
  IF DoorOpen%[I%] = TRUE THEN 
    IPl1% = I% + 1
    PRINT " " + IPl1% 
  ENDIF
NEXT
PRINT "\n"
END
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100
```

### MSX Basic

Based on the Sinclair ZX81 BASIC implementation.

```mw
10 DIM D(100)
20 FOR I=1 TO 100
30 FOR J=i TO 100 STEP I
40 D(J)=NOT D(J)
50 NEXT J
60 NEXT I
70 FOR I=1 TO 100
80 IF D(I) THEN PRINT I;
90 NEXT I
100 END
```

**Output:**

```
                                        
]RUN
1 4 9 16 25 36 49 64 81 100
```

### QBasic

Works with

:

QBASIC, QB64

**unoptimized**

```mw
REM "100 Doors" program for QB64 BASIC (http://www.qb64.net/), a QuickBASIC-like compiler.
REM Author: G. A. Tippery
REM Date: 12-Feb-2014
REM
REM   Unoptimized (naive) version, per specifications at http://rosettacode.org/wiki/100_doors

DEFINT A-Z
CONST N = 100
DIM door(N)

FOR stride = 1 TO N
    FOR index = stride TO N STEP stride
        LET door(index) = NOT (door(index))
    NEXT index
NEXT stride

PRINT "Open doors:"
FOR index = 1 TO N
    IF door(index) THEN PRINT index
NEXT index

END
```

Works with

:

QuickBasic

version 4.5

**unoptimized**

```mw
DIM doors(0 TO 99)
FOR pass = 0 TO 99
	FOR door = pass TO 99 STEP pass + 1
		PRINT doors(door)
		PRINT NOT doors(door)
		doors(door) = NOT doors(door)
	NEXT door
NEXT pass
FOR i = 0 TO 99
	PRINT "Door #"; i + 1; " is ";
	IF NOT doors(i) THEN
		PRINT "closed"
	ELSE
		PRINT "open"
	END IF
NEXT i
```

**optimized**

```mw
DIM doors(0 TO 99)
FOR door = 0 TO 99
	IF INT(SQR(door)) = SQR(door) THEN doors(door) = -1
NEXT door
FOR i = 0 TO 99
	PRINT "Door #"; i + 1; " is ";
	IF NOT doors(i) THEN
		PRINT "closed"
	ELSE
		PRINT "open"
	END IF
NEXT i
```

### Quite BASIC

```mw
100 ARRAY D
110 FOR P = 1 TO 100
120  FOR T = P TO 100 STEP P
130   LET D[T] =  (D[T] <> 1)
140  NEXT T
150 NEXT P
160 FOR I = 1 TO 100
170  IF D[I] THEN PRINT I;" ";
180 NEXT I
190 END
```

### Tiny BASIC

```mw
    PRINT "Open doors are:"

    LET I = 1
10  IF I = 100 THEN END 
    rem funcion SQR
    LET B = I*I
    rem funcion MODULO
    LET A = I - (I / B) * B
    IF A < 11 THEN PRINT B
    LET I = I + 1
    GOTO 10
```

### Sinclair ZX81 BASIC

Works with only 1k of RAM, although it doesn't leave too much to play with.

```mw
10 DIM D(100)
20 FOR I=1 TO 100
30 FOR J=I TO 100 STEP I
40 LET D(J)=NOT D(J)
50 NEXT J
60 NEXT I
70 FOR I=1 TO 100
80 IF D(I) THEN PRINT I,
90 NEXT I
```


## Batch File

**unoptimized**

```mw
@echo off
setlocal enableDelayedExpansion
:: 0 = closed
:: 1 = open
:: SET /A treats undefined variable as 0
:: Negation operator ! must be escaped because delayed expansion is enabled
for /l %%p in (1 1 100) do for /l %%d in (%%p %%p 100) do set /a "door%%d=^!door%%d"
for /l %%d in (1 1 100) do if !door%%d!==1 (
  echo door %%d is open
) else echo door %%d is closed
```

**optimized**

```mw
@echo off
setlocal enableDelayedExpansion
set /a square=1, incr=3
for /l %%d in (1 1 100) do (
  if %%d neq !square! (echo door %%d is closed) else (
    echo door %%d is open
    set /a square+=incr, incr+=2
  )
)
```


## BBC BASIC

```mw
DIM doors%(100)
FOR pass% = 1 TO 100
    FOR door% = pass% TO 100 STEP pass%
        doors%(door%) = NOT doors%(door%)
    NEXT door%
NEXT pass%      
FOR door% = 1 TO 100
    IF doors%(door%) PRINT "Door " ; door% " is open"
NEXT door%
```


## bc

```mw
/* 0 means door is closed, 1 means door is open */
for (i = 0; i < 100; i++) {
    for (j = i; j < 100; j += (i + 1)) {
        d[j] = 1 - d[j]     /* Toggle door */
    }
}

"Open doors:
"
for (i = 0; i < 100; i++) {
    if (d[i] == 1) (i + 1)
}
```


## BCPL

```mw
get "libhdr"

let start() be 
$(  let doors = vec 100

    // close all doors
    for n = 1 to 100 do doors!n := 0

    // make 100 passes
    for pass = 1 to 100 do
    $(  let n = pass
        while n <= 100 do
        $(  doors!n := ~doors!n
            n := n + pass
        $)
    $)
    
    // report which doors are open
    for n = 1 to 100 do
        if doors!n then
            writef("Door %N is open.*N", n)
$)
```

**Output:**

```
Door 1 is open.
Door 4 is open.
Door 9 is open.
Door 16 is open.
Door 25 is open.
Door 36 is open.
Door 49 is open.
Door 64 is open.
Door 81 is open.
Door 100 is open.
```


## Befunge

### Befunge-93

#### Unoptimized

Requires an interpreter with working read-write memory support. Padding the code page with extra blank lines can sometimes help.

```mw
>"d">:00p1-:>:::9%\9/9+g2%!\:9v
$.v_^#!$::$_^#`"c":+g00p+9/9\%<
::<_@#`$:\*:+55:+1p27g1g+9/9\%9
```

#### Optimized

Just calculates the first 10 perfect squares.

```mw
1+:::*.9`#@_
```

### Befunge-98

Works with

:

CCBI

version 2.1

```mw
108p0>:18p;;>:9g!18g9p08g]
*`!0\|+relet|-1`*aap81::+]
;::+1<r]!g9;>$08g1+:08paa[
*`#@_^._aa
```


## Binary Lambda Calculus

This computes the characteristic sequence of squares by flipping every i'th door in round i, for infinitely many rounds i. But since it's computed lazily and the prefix stabilizes, we can still take the first 100 bits and print them! See corresponding source code at https://github.com/tromp/AIT/blob/master/characteristic_sequences/squares.lam

```
0001000100010101000110100000010110000011001110110010100011010000000000101111111000000101111101011001011001000110100001111100110100101111101111000000001011111111110110011001111111011100000000101111110000001011111010110011011100101011000000101111011001011110011110011110110100000000001011011100111011110000000001000000111001110100000000101101110110
```

Output

```
1001000010000001000000001000000000010000000000001000000000000001000000000000000010000000000000000001
```


## Blade

### Unoptimized version

```mw
var doors = [false] * 100
for i in 0..100 {
  iter var j = i; j < 100; j += i + 1 {
    doors[j] = !doors[j]
  }
  var state = doors[i] ? 'open' : 'closed'
  echo 'Door ${i + 1} is ${state}'
}
```

### Optimized version

```mw
for i in 1..101 {
  echo 'Door ${i} is ${i ** 0.5 % 1 > 0 ? "closed" : "open"}'
}
```

### Ultra-optimized version

```mw
for i in 1..11 echo 'Door ${i**2} is open'
```


## BlitzMax

Works with

:

BlitzMax

version 1.37

**optimized**

```mw
Graphics 640,480
i=1
While ((i*i)<=100)
	a$=i*i
	DrawText a$,10,20*i
	Print i*i
	i=i+1 
Wend
Flip 
WaitKey
```


## BlooP

The currently available BlooP interpreters don't really allow iterating over cells with any level of ease, so instead I loop over each door in turn, running it through all 100 cycles and toggling it when it is a multiple of the step number.

```mw
DEFINE PROCEDURE ''DIVIDE'' [A,B]:
BLOCK 0: BEGIN
  IF A < B, THEN:
    QUIT BLOCK 0;
  CELL(0) <= 1;
  OUTPUT <= 1;
  LOOP AT MOST A TIMES:
  BLOCK 2: BEGIN
    IF OUTPUT * B = A, THEN:
    QUIT BLOCK 0;
    OUTPUT <= OUTPUT + 1;
    IF OUTPUT * B > A, THEN:
    BLOCK 3: BEGIN
      OUTPUT <= CELL(0);
      QUIT BLOCK 0;
    BLOCK 3: END;
    CELL(0) <= OUTPUT;
  BLOCK 2: END;
BLOCK 0: END.

DEFINE PROCEDURE ''MINUS'' [A,B]:
BLOCK 0: BEGIN
  IF A < B, THEN:
    QUIT BLOCK 0;
  LOOP AT MOST A TIMES:
  BLOCK 1: BEGIN
    IF OUTPUT + B = A, THEN:
      QUIT BLOCK 0;
    OUTPUT <= OUTPUT + 1;
  BLOCK 1: END;
BLOCK 0: END.

DEFINE PROCEDURE ''MODULUS'' [A,B]:
BLOCK 0: BEGIN
  CELL(0) <= DIVIDE[A,B];
  OUTPUT <= MINUS[A,CELL(0) * B];
BLOCK 0: END.

DEFINE PROCEDURE ''TOGGLE'' [DOOR]:
BLOCK 0: BEGIN
  IF DOOR = 1, THEN:
    QUIT BLOCK 0;
  OUTPUT <= 1;
BLOCK 0: END.

DEFINE PROCEDURE ''NUMBERS'' [DOOR, COUNT]:
BLOCK 0: BEGIN
  CELL(0) <= 1; /*each number*/
  OUTPUT <= 0; /*current door state*/
  
  LOOP COUNT TIMES:
  BLOCK 1: BEGIN

    IF MODULUS[DOOR, CELL(0)] = 0, THEN:
      OUTPUT <= TOGGLE[OUTPUT];
    
    CELL(0) <= CELL(0) + 1;

  BLOCK 1: END;

BLOCK 0: END.

DEFINE PROCEDURE ''DOORS'' [COUNT]:
BLOCK 0: BEGIN

  CELL(0) <= 1; /*each door*/
  LOOP COUNT TIMES:
  BLOCK 1: BEGIN

    CELL(1) <= NUMBERS[CELL(0), COUNT];  /*iterate over the states of this door to get its final state*/
    IF CELL(1) = 1, THEN: /*door state = open*/
      PRINT[CELL(0), '   '];
    
    CELL(0) <= CELL(0) + 1;

  BLOCK 1: END;
BLOCK 0: END.

DOORS[100];
```

**Output:**

```
 > 1   
 > 4   
 > 9   
 > 16   
 > 25   
 > 36   
 > 49   
 > 64   
 > 81   
 > 100   
```


## Bracmat

Bracmat is not really at home in tasks that involve addressing things by index number. Here are four solutions that each do the task, but none should win a price for cleanliness.

Solution 1. Use an indexable array. Local variables are stored in stacks. Each stack corresponds to one variable name and vice versa. Stacks can also be used as arrays, but because of how local variables are implemented, arrays cannot be declared as local variables.

```mw
( 100doors-tbl
=   door step
  .   tbl$(doors.101) { Create an array. Indexing is 0-based. Add one extra for addressing element nr. 100 }
    & 0:?step
    &   whl
      ' ( 1+!step:~>100:?step   { ~> means 'not greater than', i.e. 'less than or equal' }
        & 0:?door
        &   whl
          ' ( !step+!door:~>100:?door
            & 1+-1*!(!door$doors):?doors  { <number>$<variable> sets the current index, which stays the same until explicitly changed. }
            )
        )
    & 0:?door
    &   whl
      ' ( 1+!door:~>100:?door
        &   out
          $ ( door
              !door
              is
              ( !(!door$doors):1&open
              | closed
              )
            )
        )
    & tbl$(doors.0)  { clean up the array }
)
```

Solution 2. Use one variable for each door. In Bracmat, a variable name can be any non-empty string, even a number, so we use the numbers 1 .. 100 as variable names, but also as door numbers. When used as variable an extra level of indirection is needed. See the occurrences of `?!` and `!!` in the following code.

```mw
( 100doors-var
=   step door
  .   0:?door
    &   whl
      ' ( 1+!door:~>100:?door
        & closed:?!door { this creates a variable and assigns a value 'closed' to it }
        )
    & 0:?step
    &   whl
      ' ( 1+!step:~>100:?step
        & 0:?door
        &   whl
          ' ( !step+!door:~>100:?door
            &   ( !!door:closed&open
                | closed
                )
              : ?!door   
            )
        )
    & 0:?door
    &   whl
      ' ( 1+!door:~>100:?door
        & out$(door !door is !!door)
        )
    & 0:?door
    &   whl
      ' ( 1+!door:~>100:?door
        & tbl$(!door.0)         { cleanup the variable }
        )
)
```

Solution 3. Use a list and a dedicated positioning pattern to address the right door in the list. Create a new list by concatenating the skipped elements with the toggled elements. This solution is computationally unfavourable because of the many concatenations.

```mw
( 100doors-list
=   doors door doorIndex step
  .   :?doors
    & 0:?door
    &   whl
      ' ( 1+!door:~>100:?door
        & closed !doors:?doors
        )
    & 0:?skip
    &   whl
      ' ( :?ndoors
        &   whl
          ' ( !doors:?skipped [!skip %?door ?doors  { the [<number> pattern only succeeds when the scanning cursor is at position <number> }
            &     !ndoors
                  !skipped
                  ( !door:open&closed
                  | open
                  )
              : ?ndoors
            )
        & !ndoors !doors:?doors
        & 1+!skip:<100:?skip
        )
    & out$!doors
)
```

Solution 4. Use a list of objects. Each object can be changed without the need to re-create the whole list.

```mw
( 100doors-obj
=   doors door doorIndex step
  .   :?doors
    & 0:?door
    &   whl
      ' ( 1+!door:~>100:?door
        & new$(=closed) !doors:?doors
        )
    & 0:?skip
    &   whl
      ' ( !doors:?tododoors
        &   whl
          ' ( !tododoors:? [!skip %?door ?tododoors
            &   ( !(door.):open&closed
                | open
                )
              : ?(door.)
            )
        & 1+!skip:<100:?skip
        )
    & out$!doors
)
```

These four functions are called in the following way:

```mw
100doors-tbl$
& 100doors-var$
& 100doors-list$
& 100doors-obj$;
```


## Burlesque

Version using square numbers:

```mw
blsq ) 10ro2?^
{1 4 9 16 25 36 49 64 81 100}
```


## BQN

### First Solution

```mw
swch ← ≠´{100⥊1«𝕩⥊0}¨1+↕100
¯1↓∾{𝕩∾@+10}¨•Fmt¨⟨swch,/swch⟩
```

```mw
"⟨ 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 ⟩
⟨ 0 3 8 15 24 35 48 63 80 99 ⟩"
```

```mw
swch
```

uses an idea similar to the GNU APL solution to generate a boolean array of the correct switches.

The second line then formats the boolean array and the truthy indices into a string for display.

Try it here!

### Second Solution

this idea taken from Uiua solution and it's almost identical

```mw
F ← {1+ / 2| +˝ 0= |⌜˜ 1+↕𝕩}
F 100
# ⟨ 1 4 9 16 25 36 49 64 81 100 ⟩
```

### Optimized

```mw
F ← {×˜1+↕⌊√𝕩}
F 100
# ⟨ 1 4 9 16 25 36 49 64 81 100 ⟩
```


## C

### unoptimized

Uses:

C Runtime

(

Components:

{{#foreach: component$n$|{{{component$n$}}}

Property "Uses Library" (as page type) with input value "Library/C Runtime/{{{component$n$}}}" contains invalid characters or is incomplete and therefore can cause unexpected results during a query or annotation process.

, }})

```mw
#include <stdio.h>

int main()
{
  char is_open[100] = { 0 };
  int pass, door;

  /* do the 100 passes */
  for (pass = 0; pass < 100; ++pass)
    for (door = pass; door < 100; door += pass+1)
      is_open[door] = !is_open[door];

  /* output the result */
  for (door = 0; door < 100; ++door)
    printf("door #%d is %s.\n", door+1, (is_open[door]? "open" : "closed"));

  return 0;
}
```

Using defensive programming, pointers, sentinel values and some other standard programming practices,

Uses:

C Runtime

(

Components:

{{#foreach: component$n$|{{{component$n$}}}

Property "Uses Library" (as page type) with input value "Library/C Runtime/{{{component$n$}}}" contains invalid characters or is incomplete and therefore can cause unexpected results during a query or annotation process.

, }})

```mw
#include <stdio.h>

#define NUM_DOORS 100

int main(int argc, char *argv[])
{
  int is_open[NUM_DOORS] = { 0 } ;
  int * doorptr, * doorlimit = is_open + NUM_DOORS ;
  int pass ;

  /* do the N passes, go backwards because the order is not important */
  for ( pass= NUM_DOORS ; ( pass ) ; -- pass ) {
    for ( doorptr= is_open + ( pass-1 ); ( doorptr < doorlimit ) ; doorptr += pass ) {
      ( * doorptr ) ^= 1 ;
    }
  }

  /* output results */
  for ( doorptr= is_open ; ( doorptr != doorlimit ) ; ++ doorptr ) {
    printf("door #%lld is %s\n", ( doorptr - is_open ) + 1, ( * doorptr ) ? "open" : "closed" ) ;
  }
}
```

### memory optimization

This uses bits to represent doors.

```mw
#include <stdio.h>
#include <stdint.h>

int main() {
  uint32_t doorBytes[4] = {0};

  for (uint32_t i = 1; i <= 100; ++i)
    for (uint32_t j = i - 1; j <= 99; j += i)
      doorBytes[j % 4] ^= (uint32_t)1 << j / 4;

  for (uint32_t i = 0; i <= 99; doorBytes[i++ % 4] >>= 1)
    if (doorBytes[i % 4] & 1)
      printf("door %d is open\n", i + 1);
}
```

### optimized

This optimized version makes use of the fact that finally only the doors with square index are open, as well as the fact that ${\displaystyle n^{2}=1+3+5+\ldots +(2n-1)}$ .

Uses:

C Runtime

(

Components:

{{#foreach: component$n$|{{{component$n$}}}

Property "Uses Library" (as page type) with input value "Library/C Runtime/{{{component$n$}}}" contains invalid characters or is incomplete and therefore can cause unexpected results during a query or annotation process.

, }})

```mw
#include <stdio.h>

int main()
{
  int square = 1, increment = 3, door;
  for (door = 1; door <= 100; ++door)
  {
    printf("door #%d", door);
    if (door == square)
    {
      printf(" is open.\n");
      square += increment;
      increment += 2;
    }
    else
      printf(" is closed.\n");
  }
  return 0;
}
```

The following ultra-short optimized version demonstrates the flexibility of C loops, but isn't really considered good C style:

```mw
#include <stdio.h>

int main()
{
  int door, square, increment;
  for (door = 1, square = 1, increment = 1; door <= 100; door++ == square && (square += increment += 2))
    printf("door #%d is %s.\n", door, (door == square? "open" : "closed"));
  return 0;
}
```

Or really optimize it -- square of an integer is, well, computable:

```mw
#include <stdio.h>

int main()
{
	int i;
	for (i = 1; i * i <= 100; i++)
		printf("door %d open\n", i * i);

	return 0;
}
```
