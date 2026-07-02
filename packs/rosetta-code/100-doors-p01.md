---
title: "100 doors (part 1/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/10
---

# 100 doors

There are 100 doors in a row that are all initially closed.

You make 100 passes by the doors.

The first time through, visit every door and *toggle* the door (if the door is closed, open it; if it is open, close it).

The second time, only visit every 2nd door (door #2, #4, #6, ...), and toggle it.

The third time, visit every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

**Task**

Answer the question: what state are the doors in after the last pass? Which are open, which are closed?

**Alternate:** As noted in this page's discussion page, the only doors that remain open are those whose numbers are perfect squares.

Opening only those doors is an optimization that may also be expressed; however, as should be obvious, this defeats the intent of comparing implementations across programming languages.

**Why doesn't syntax highlighting work on this page ?**

Currently, there is a limit on how many <syntaxhighlight> tags can appear on a page, so only the first few languages get highlighting, the rest are shown in monochrome. You could try "manual highlighting", possibly using one of the highlighters on Syntax highlighting using Mediawiki formatting or something similar.


## 11l

Translation of

:

Python

```mw
V doors = [0B] * 100
L(i) 0.<100
   L(j) (i .< 100).step(i + 1)
      doors[j] = !doors[j]
   print(‘Door ’(i + 1)‘: ’(I doors[i] {‘open’} E ‘close’))
```


## 360 Assembly

```mw
*        100 doors                 13/08/2015
HUNDOOR  CSECT
         USING  HUNDOOR,R12
         LR     R12,R15
         LA     R6,0
         LA     R8,1               step 1
         LA     R9,100
LOOPI    BXH    R6,R8,ELOOPI       do ipass=1 to 100 (R6)
         LR     R7,R6
         SR     R7,R6
         LR     R10,R6             step ipass
         LA     R11,100
LOOPJ    BXH    R7,R10,ELOOPJ      do idoor=ipass to 100 by ipass (R7)
         LA     R5,DOORS-1
         AR     R5,R7
         XI     0(R5),X'01'        doors(idoor)=not(doors(idoor))
NEXTJ    B      LOOPJ
ELOOPJ   B      LOOPI
ELOOPI   LA     R10,BUFFER         R10 address of the buffer
         LA     R5,DOORS           R5 address of doors item
         LA     R6,1               idoor=1 (R6)
         LA     R9,100             loop counter
LOOPN    CLI    0(R5),X'01'        if doors(idoor)=1
         BNE    NEXTN
         XDECO  R6,XDEC            idoor to decimal
         MVC    0(4,R10),XDEC+8    move decimal to buffer
         LA     R10,4(R10)
NEXTN	 LA     R6,1(R6)           idoor=idoor+1
         LA     R5,1(R5)
         BCT    R9,LOOPN           loop
ELOOPN   XPRNT  BUFFER,80
RETURN   XR     R15,R15
         BR     R14
DOORS    DC     100X'00'
BUFFER   DC     CL80' '
XDEC     DS     CL12
         YREGS
         END    HUNDOOR
```

**Output:**

```
   1   4   9  16  25  36  49  64  81 100
```


## 4DOS Batch

```mw
@echo off
set doors=%@repeat[C,100]
do step = 1 to 100
  do door = %step to 100 by %step
    set doors=%@left[%@eval[%door-1],%doors]%@if[%@instr[%@eval[%door-1],1,%doors]==C,O,C]%@right[%@eval[100-%door],%doors]
  enddo
enddo
```

The SET line consists of three functions:

```mw
%@left[n,string]                      ^: Return n leftmost chars in string
%@right[n,string]                     ^: Return n rightmost chars in string
%@if[condition,true-val,false-val]    ^: Evaluate condition; return true-val if true, false-val if false
```

Here @IF is used to toggle between C and O.


## 6502 Assembly

Works with

: [

www.6502asm.com

] version beta

**unoptimized** Based on BASIC QB64 unoptimized version

```mw
; 100 DOORS in  6502 assembly language for: http://www.6502asm.com/beta/index.html
; Written for the original MOS Technology, Inc. NMOS version of the 6502, but should work with any version.
; Based on BASIC QB64 unoptimized version: http://rosettacode.org/wiki/100_doors#BASIC
;
; Notes:
;    Doors array[1..100] is at $0201..$0264. On the specified emulator, this is in video memory, so tbe results will 
; be directly shown as pixels in the display.
;    $0200 (door 0) is cleared for display purposes but is not involved in the open/close loops.
;    Y register holds Stride
;    X register holds Index
;    Zero Page address $01 used to add Stride to Index (via A) because there's no add-to-X or add-Y-to-A instruction.

  ; First, zero door array
    LDA #00
    LDX #100
Z_LOOP:
    STA 200,X
    DEX
    BNE Z_LOOP
    STA 200,X

  ; Now do doors repeated open/close
    LDY #01        ; Initial value of Stride
S_LOOP:
    CPY #101
    BCS S_DONE
    TYA            ; Initial value of Index
I_LOOP:
    CMP #101
    BCS I_DONE
    TAX            ; Use as Door array index
    INC $200,X     ; Toggle bit 0 to reverse state of door
    STY 01         ; Add stride (Y) to index (X, via A)
    ADC 01
    BCC I_LOOP
I_DONE:
    INY
    BNE S_LOOP
S_DONE:

  ; Finally, format array values for output: 0 for closed, 1 for open
    LDX #100
C_LOOP:
    LDA $200,X
    AND #$01
    STA $200,X
    DEX
    BNE C_LOOP
```

48. bytes of code; the specified emulator does not report cycles.

Works with

: [

6502asm.com

] version 1.2

**optimized** Largely inspired by the optimized C implementation - makes use of the fact that finally only the doors whose numbers are squares of integers are open, as well as the fact that

```
  
    
      
        
          
            
              n
              
                2
              
            
            =
            1
            +
            3
            +
            5
            +
            …
            +
            (
            2
            n
            −
            1
            )
          
        
      
    
    {\displaystyle {\displaystyle n^{2}=1+3+5+\ldots +(2n-1)}}
  
.
```

```mw
  ;assumes memory at $02xx is initially set to 0 and stack pointer is initialized
  ;the 1 to 100 door byte array will be at $0200-$0263 (decimal 512 to 611)
  ;Zero-page location $01 will hold delta
  ;At end, closed doors = $00, open doors = $01

start:    ldx #0        ;initialize index - first door will be at $200 + $0
          stx $1
          inc $1        ;start out with a delta of 1 (0+1=1)
openloop: inc $200,X    ;open X'th door
          inc $1        ;add 2 to delta
          inc $1
          txa           ;add delta to X by transferring X to A, adding delta to A, then transferring back to X
          clc           ;  clear carry before adding (6502 has no add-without-carry instruction)
          adc $1
          tax
          cpx #$64      ;check to see if we're at or past the 100th door (at $200 + $63)
          bmi openloop  ;jump back to openloop if less than 100
```

22. bytes of code; the specified emulator does not report cycles.


## 68000 Assembly

Works with

: [

EASy68K v5.13.00

]

Some of the macro code is derived from the examples included with EASy68K.

```mw
*-----------------------------------------------------------
* Title      : 100Doors.X68
* Written by : G. A. Tippery
* Date       : 2014-01-17
* Description: Solves "100 Doors" problem, see: http://rosettacode.org/wiki/100_doors
* Notes      : Translated from C "Unoptimized" version, http://rosettacode.org/wiki/100_doors#unoptimized
*            : No optimizations done relative to C version; "for("-equivalent loops could be optimized.
*-----------------------------------------------------------

*
*   System-specific general console I/O macros (Sim68K, in this case)
*
PUTS    MACRO
    ** Print a null-terminated string w/o CRLF **
    ** Usage: PUTS stringaddress
    ** Returns with D0, A1 modified
        MOVEQ   #14,D0      ; task number 14 (display null string)
        LEA     \1,A1       ; address of string
        TRAP    #15         ; display it
        ENDM
*
PRINTN  MACRO
    ** Print decimal integer from number in register
    ** Usage: PRINTN register
    ** Returns with D0,D1 modified
        IFNC '\1','D1'      ;if some register other than D1
          MOVE.L \1,D1      ;put number to display in D1
        ENDC
        MOVE.B  #3,D0
        TRAP    #15         ;display number in D1
*
*   Generic constants
*
CR      EQU     13      ;ASCII Carriage Return
LF      EQU     10      ;ASCII Line Feed

*
*   Definitions specific to this program
*
*   Register usage:
*   D3 == pass (index)
*   D4 == door (index)
*   A2 == Doors array pointer
*
SIZE    EQU     100             ;Define a symbolic constant for # of doors

        ORG     $1000           ;Specify load address for program -- actual address system-specific
START:                          ; Execution starts here
        LEA     Doors,A2        ; make A2 point to Doors byte array
        MOVEQ   #0,D3
PassLoop:
        CMP     #SIZE,D3
        BCC     ExitPassLoop    ; Branch on Carry Clear - being used as Branch on Higher or Equal
        MOVE    D3,D4
DoorLoop:
        CMP     #SIZE,D4
        BCC     ExitDoorLoop
        NOT.B   0(A2,D4)
        ADD     D3,D4
        ADDQ    #1,D4
        BRA     DoorLoop
ExitDoorLoop:
        ADDQ    #1,D3
        BRA     PassLoop
ExitPassLoop:

* $28 = 40. bytes of code to this point. 32626 cycles so far.
*   At this point, the result exists as the 100 bytes starting at address Doors.
* To get output, we must use methods specific to the particular hardware, OS, or
* emulator system that the code is running on.  I use macros to "hide" some of the
* system-specific details; equivalent macros would be written for another system.

        MOVEQ   #0,D4
PrintLoop:
        CMP     #SIZE,D4
        BCC     ExitPrintLoop
        PUTS    DoorMsg1
        MOVE    D4,D1
        ADDQ    #1,D1           ; Convert index to 1-based instead of 0-based
        PRINTN  D1
        PUTS    DoorMsg2
        TST.B   0(A2,D4)        ; Is this door open (!= 0)?
        BNE     ItsOpen
        PUTS    DoorMsgC
        BRA     Next
ItsOpen:
        PUTS    DoorMsgO
Next:
        ADDQ    #1,D4
        BRA     PrintLoop
ExitPrintLoop:

*  What to do at end of program is also system-specific
        SIMHALT             ;Halt simulator
*
* $78 = 120. bytes of code to this point, but this will depend on how the I/O macros are actually written.
* Cycle count is nearly meaningless, as the I/O hardware and routines will dominate the timing.

*
*   Data memory usage
*
        ORG     $2000
Doors   DCB.B   SIZE,0      ;Reserve 100 bytes, prefilled with zeros

DoorMsg1 DC.B   'Door ',0
DoorMsg2 DC.B   ' is ',0
DoorMsgC DC.B   'closed',CR,LF,0
DoorMsgO DC.B   'open',CR,LF,0

        END     START       ;last line of source
```


## 8080 Assembly

```mw
page:	equ	2	; Store doors in page 2
doors:	equ	100	; 100 doors
puts:	equ	9	; CP/M string output
	org	100h
	xra	a	; Set all doors to zero
	lxi	h,256*page
	mvi	c,doors
zero:	mov	m,a
	inx	h
	dcr	c
	jnz	zero
	mvi	m,'$'	; CP/M string terminator (for easier output later)
	mov	d,a	; D=0 so that DE=E=pass counter
	mov	e,a	; E=0, first pass
	mvi	a,doors-1	; Last pass and door
pass:	mov	l,e	; L=door counter, start at first door in pass
door:	inr	m	; Incrementing always toggles the low bit
	dad	d	; Go to next door in pass
	inr	l
	cmp	l	; Was this the last door?
	jnc	door	; If not, do the next door
	inr	e	; Next pass
	cmp	e	; Was this the last pass?
	jnc	pass	; If not, do the next pass
	lxi	h,256*page
	mvi	c,doors	; Door counter
	lxi	d,130h	; D=1 (low bit), E=30h (ascii 0)
char:	mov	a,m	; Get door	
	ana	d	; Low bit gives door status
	ora	e	; ASCII 0 or 1
	mov	m,a	; Write character back
	inx	h	; Next door
	dcr	c	; Any doors left?
	jnz	char	; If so, next door
	lxi	d,256*page
	mvi	c,puts	; CP/M system call to print the string
	jmp	5
```

**Output:**

```
1001000010000001000000001000000000010000000000001000000000000001000000000000000010000000000000000001
```

**Optimized** Of course, calling it a solution is stretching a point, since the various optimized solutions presented for the task do not actually solve the puzzle; they merely print out the answer the programmer has already deduced. Still, generating a sequence of squares is an interesting exercise in its own right, and the elegant C example works particularly well here, since the 8080 lacks a built-in multiply instruction. 16-bit arithmetic is overkill for the stated task, but could be useful in other contexts. I/O and program entry/exit assume the CP/M operating system.

```mw
wboot	equ	0	; jump to BIOS warm boot routine
bdos	equ 	5	; BDOS entry  
conout	equ 	2	; BDOS console output function
putstr	equ	9	; BDOS print string function
ndoors	equ	100	; number of doors
	;
	org	100h
	lxi	sp,stack  ; set our own stack
	lxi	d,intro	  ; print introductory message
	mvi	c,putstr
	call	bdos
	;
	; generate sequence of squares to specified limit
	; HL holds the current square
	; DE holds the increment 
	; BC holds the negative of the limit
	;
gensqr:	lxi	h,1	; starting value of square
	lxi	d,3	; starting value of increment
	lxi	b,-ndoors
sqrs2:	call	putdec	; otherwise print current square
	mvi	a,' '	; separate with a space
	call	putchr
	push	h	; have we reached the limit?
	dad	b
	pop	h
	jc	done	; CY if HL > limit
	dad	d	; square += incrememnt
	inx	d	; increment += 2
	inx	d
	jmp	sqrs2	; repeat until finished
	;
done:	jmp	wboot	; exit with warm boot
	;---------------------------------------------------
	; console output of char in A register
	;---------------------------------------------------
putchr:	push	h
	push	d
	push	b
	mov	e,a
	mvi	c,conout
	call	bdos
	pop	b
	pop	d
	pop	h
	ret
	;---------------------------------------------------
	; Output decimal number to console
	; HL holds 16-bit unsigned binary number to print
	;---------------------------------------------------
putdec: push	b
	push	d
	push	h
	lxi	b,-10
	lxi	d,-1
putdec2:
	dad	b
	inx	d
	jc	putdec2
	lxi	b,10
	dad	b
	xchg
	mov	a,h
	ora	l
	cnz	putdec		; recursive call
	mov	a,e
	adi	'0'
	call	putchr
	pop	h
	pop	d
	pop	b
	ret
	;---------------------------------------------------
	; data area and stack
	;---------------------------------------------------
intro: db	'The open doors are: $'
stack	equ	$+128		; 64-level stack
	;
	end
```

**Output:**

```
The open doors are: 1 4 9 16 25 36 49 64 81 100
```


## 8086 Assembly

See 100 doors/8086 Assembly


## 8th

```mw
\ Array of doors; init to empty; accessing a non-extant member will return
\ 'null', which is treated as 'false', so we don't need to initialize it:
[] var, doors    

\ given a door number, get the value and toggle it:
: toggle-door \ n --
	doors @ over a:@
	not rot swap a:! drop ;

\ print which doors are open:
: .doors
	( 
		doors @ over a:@ nip
		if . space else drop then
	) 1 100 loop ;

\ iterate over the doors, skipping 'n':
: main-pass \ n --
	0
	true
	repeat
		drop
		dup toggle-door
		over n:+
		dup 101 <
	while 2drop drop ;

\ calculate the first 100 doors:
' main-pass 1 100 loop
\ print the results:
.doors cr bye
```

**Output:**

1 4 9 16 25 36 49 64 81 100


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

**unoptimized**

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program 100doors64.s   */
 
/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"

.equ NBDOORS,   100
/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:       .asciz "The door @ is open.\n"
 
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
stTableDoors:    .skip   8 * NBDOORS
sZoneConv:       .skip 24
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                             // entry of program 
    // display first line
    ldr x3,qAdrstTableDoors       // table address
    mov x5,1             
1:
    mov x4,x5
2:                               // begin loop
    ldr x2,[x3,x4,lsl #3]        // read doors index x4
    cmp x2,#0
    cset x2,eq
    //moveq x2,#1                // if x2 = 0   1 -> x2
    //movne x2,#0                // if x2 = 1   0 -> x2
    str x2,[x3,x4,lsl #3]        // store value of doors
    add x4,x4,x5                 // increment x4 with  x5 value
    cmp x4,NBDOORS               // number of doors ?
    ble 2b                       // no -> loop
    add x5,x5,#1                 // increment the increment !!
    cmp x5,NBDOORS               // number of doors ?
    ble 1b                       // no -> loop
 
                                 // loop display state doors
    mov x4,#0              
3:
    ldr x2,[x3,x4,lsl #3]        // read state doors x4 index
    cmp x2,#0
    beq 4f
    mov x0,x4                    // open -> display message
    ldr x1,qAdrsZoneConv          // display value index
    bl conversion10              // call function
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv 
    bl strInsertAtCharInc        // insert result at first @ character
    bl affichageMess             // display message
4:
    add x4,x4,1
    cmp x4,NBDOORS
    ble 3b                       // loop
 
 
100:                             // standard end of the program 
    mov x0,0                     // return code
    mov x8,EXIT                  // request to exit program
    svc 0                        // perform the system call
 
qAdrstTableDoors:        .quad stTableDoors
qAdrsMessResult:         .quad sMessResult
qAdrsZoneConv:           .quad sZoneConv
/***********************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```

**optimized**

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program 100doors64_1.s   */
 
/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"

.equ NBDOORS,   100
/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:       .asciz "The door @ is open.\n"
 
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
sZoneConv:        .skip 24
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                             // entry of program 
 
    mov x5,3
    mov x4,1
1:
    mov x0,x4
    ldr x1,qAdrsZoneConv          // display value index
    bl conversion10              // call function
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv 
    bl strInsertAtCharInc        // insert result at first @ character
    bl affichageMess             // display message
    add x4,x4,x5
    add x5,x5,2
    cmp x4,NBDOORS
    ble 1b                       // loop
 
 
100:                             // standard end of the program 
    mov x0,0                     // return code
    mov x8,EXIT                  // request to exit program
    svc 0                        // perform the system call
 
qAdrsMessResult:         .quad sMessResult
qAdrsZoneConv:           .quad sZoneConv
/***********************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```


## ABAP

**unoptimized**

```mw
form open_doors_unopt.
  data: lv_door  type i,
        lv_count type i value 1.
  data: lt_doors type standard table of c initial size 100.
  field-symbols: <wa_door> type c.
  do 100 times.
    append initial line to lt_doors assigning <wa_door>.
    <wa_door> = 'X'.
  enddo.

  while lv_count < 100.
    lv_count = lv_count + 1.
    lv_door = lv_count.
    while lv_door < 100.
      read table lt_doors index lv_door assigning <wa_door>.
      if <wa_door> = ' '.
        <wa_door> = 'X'.
      else.
        <wa_door> = ' '.
      endif.
      add lv_count to lv_door.
    endwhile.
  endwhile.

  loop at lt_doors assigning <wa_door>.
    if <wa_door> = 'X'.
      write : / 'Door', (4) sy-tabix right-justified, 'is open' no-gap.
    endif.
  endloop.
endform.
```

**unoptimized / functional**

```mw
cl_demo_output=>display( REDUCE stringtab( INIT list TYPE stringtab
                                              aux TYPE i
                                          FOR door = 1 WHILE door <= 100
                                          FOR pass = 1 WHILE pass <= 100
                                         NEXT aux   = COND #( WHEN pass = 1 THEN 1
                                                              WHEN door MOD pass = 0 THEN aux + 1 ELSE aux  )
                                              list  = COND #( WHEN pass = 100
                                                                THEN COND #( WHEN aux MOD 2 <> 0 THEN VALUE #( BASE list ( CONV #( door ) ) )
                                                                              ELSE list ) ELSE list ) ) ).
```

**optimized**

Using ${\displaystyle \sum _{i=1}^{n}(2i-1)=n^{2}}$

```mw
form open_doors_opt.
  data: lv_square type i value 1,
        lv_inc    type i value 3.
  data: lt_doors  type standard table of c initial size 100.
  field-symbols: <wa_door> type c.
  do 100 times.
    append initial line to lt_doors assigning <wa_door>.
    if sy-index = lv_square.
      <wa_door> = 'X'.
      add: lv_inc to lv_square, 2 to lv_inc.
      write : / 'Door', (4) sy-index right-justified, 'is open' no-gap.
    endif.
  enddo.
endform.
```

**ultra-optimized / imperative**

```mw
DO 10 TIMES.
  DATA(val) = sy-index * sy-index.
  WRITE: / val.
ENDDO.
```

**ultra-optimized / functional**

```mw
cl_demo_output=>display( REDUCE stringtab( INIT list TYPE stringtab
                                          FOR i = 1 WHILE i <= 10
                                         NEXT list = VALUE #( BASE list ( i * i ) ) ) ).
```


## ABC

```mw
HOW TO INITIALIZE:
    SHARE doors
    PUT {} IN doors
    FOR door IN {1..100}:
        PUT 0 IN doors[door]

HOW TO TOGGLE door:
    SHARE doors
    PUT 1-doors[door] IN doors[door]

HOW TO WALK step:
    SHARE doors
    PUT step IN door
    WHILE door <= 100:
        TOGGLE door
        PUT door+step IN door

HOW TO DISPLAY OPEN DOORS:
    SHARE doors
    FOR door IN {1..100}:
        IF doors[door] = 1:
            WRITE "Door", door, "is open"/

INITIALIZE
FOR pass IN {1..100}: WALK pass
DISPLAY OPEN DOORS
```

**Output:**

```
Door 1 is open
Door 4 is open
Door 9 is open
Door 16 is open
Door 25 is open
Door 36 is open
Door 49 is open
Door 64 is open
Door 81 is open
Door 100 is open
```


## ACL2

```mw
(defun rep (n x)
   (if (zp n)
       nil
       (cons x
             (rep (- n 1) x))))

(defun toggle-every-r (n i bs)
   (if (endp bs)
       nil
       (cons (if (zp i)
                 (not (first bs))
                 (first bs))
             (toggle-every-r n (mod (1- i) n) (rest bs)))))

(defun toggle-every (n bs)
   (toggle-every-r n (1- n) bs))

(defun 100-doors (i doors)
   (if (zp i)
       doors
       (100-doors (1- i) (toggle-every i doors))))
```


## Action!

```mw
DEFINE COUNT="100"

PROC Main()
  BYTE ARRAY doors(COUNT+1)
  BYTE door,pass

  FOR door=1 TO COUNT
  DO
    doors(door)=0
  OD
  
  PrintE("Following doors are open:")
  FOR pass=1 TO COUNT
  DO
    FOR door=pass TO COUNT STEP pass
    DO
      doors(door)==!$FF
    OD
    IF doors(pass)=$FF THEN
      PrintB(pass) Put(32)
    FI
  OD
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
Following doors are open:
1 4 9 16 25 36 49 64 81 100
```


## ActionScript

Works with

:

ActionScript

version 3.0

**unoptimized**

```mw
package {                                                                                
    import flash.display.Sprite;                                              

    public class Doors extends Sprite {
        public function Doors() {

            // Initialize the array
            var doors:Array = new Array(100);
            for (var i:Number = 0; i < 100; i++) {
                doors[i] = false;

            // Do the work
            for (var pass:Number = 0; pass < 100; pass++) {
                for (var j:Number = pass; j < 100; j += (pass+1)) {
                    doors[j] = !doors[j];
                }
            }
            trace(doors);
        }
    }
}
```


## Acurity Architect

```
Using #HASH-OFF, OPTION OICC ="^" , CICC ="^"
```

```mw
VAR sStatus: SHORT
VAR sArray: SHORT
VAR sCount: SHORT
VAR sDoor: SHORT
VAR sPass: SHORT
VAR zIndex: STRING
VAR zState: STRING
//
SET sStatus = GET_UNUSED_ARRAY_HANDLE(sArray)
SET sStatus = INIT_SORTED_ARRAY(sArray, 0, 0, 1)
//
DO sCount = 1 TO 100
  DO sPass = 1 TO 100
    SET sDoor = sCount * sPass
    IF sDoor <= 100
      SET zIndex = REPEAT("0", 3 - LENGTH(STR(sDoor))) + STR(sDoor)
      SET sStatus = READ_ARRAY_REC("=", sArray, zIndex)
      SET zState = "OPEN"
      IF GET_STRING_SAY(sArray, 1) = "OPEN"
        SET zState = "CLOSE"
      ENDIF
      //
      SET sStatus = ADD_ARRAY_REC(sArray, zIndex)
      SET sStatus = PUT_STRING_SAY(sArray, 1, zState)
    ELSE
      BREAK
    ENDIF
  ENDDO
ENDDO
//
SET zIndex = ""
SET sStatus = READ_ARRAY_REC(">=", sArray, zIndex)
DO WHILE sStatus = 0
  >>Door:  ^zIndex^  State: ^GET_STRING_SAY(sArray, 1)^
  SET sStatus = READ_ARRAY_REC("+", sArray, zIndex)
ENDDO
```

**Output:**

```
Door:  001  State: OPEN
Door:  002  State: CLOSE
Door:  003  State: CLOSE
Door:  004  State: OPEN
Door:  005  State: CLOSE
Door:  006  State: CLOSE
Door:  007  State: CLOSE
Door:  008  State: CLOSE
Door:  009  State: OPEN
Door:  010  State: CLOSE
Door:  011  State: CLOSE
Door:  012  State: CLOSE
Door:  013  State: CLOSE
Door:  014  State: CLOSE
Door:  015  State: CLOSE
Door:  016  State: OPEN
Door:  017  State: CLOSE
Door:  018  State: CLOSE
Door:  019  State: CLOSE
Door:  020  State: CLOSE
Door:  021  State: CLOSE
Door:  022  State: CLOSE
Door:  023  State: CLOSE
Door:  024  State: CLOSE
Door:  025  State: OPEN
Door:  026  State: CLOSE
Door:  027  State: CLOSE
Door:  028  State: CLOSE
Door:  029  State: CLOSE
Door:  030  State: CLOSE
Door:  031  State: CLOSE
Door:  032  State: CLOSE
Door:  033  State: CLOSE
Door:  034  State: CLOSE
Door:  035  State: CLOSE
Door:  036  State: OPEN
Door:  037  State: CLOSE
Door:  038  State: CLOSE
Door:  039  State: CLOSE
Door:  040  State: CLOSE
Door:  041  State: CLOSE
Door:  042  State: CLOSE
Door:  043  State: CLOSE
Door:  044  State: CLOSE
Door:  045  State: CLOSE
Door:  046  State: CLOSE
Door:  047  State: CLOSE
Door:  048  State: CLOSE
Door:  049  State: OPEN
Door:  050  State: CLOSE
Door:  051  State: CLOSE
Door:  052  State: CLOSE
Door:  053  State: CLOSE
Door:  054  State: CLOSE
Door:  055  State: CLOSE
Door:  056  State: CLOSE
Door:  057  State: CLOSE
Door:  058  State: CLOSE
Door:  059  State: CLOSE
Door:  060  State: CLOSE
Door:  061  State: CLOSE
Door:  062  State: CLOSE
Door:  063  State: CLOSE
Door:  064  State: OPEN
Door:  065  State: CLOSE
Door:  066  State: CLOSE
Door:  067  State: CLOSE
Door:  068  State: CLOSE
Door:  069  State: CLOSE
Door:  070  State: CLOSE
Door:  071  State: CLOSE
Door:  072  State: CLOSE
Door:  073  State: CLOSE
Door:  074  State: CLOSE
Door:  075  State: CLOSE
Door:  076  State: CLOSE
Door:  077  State: CLOSE
Door:  078  State: CLOSE
Door:  079  State: CLOSE
Door:  080  State: CLOSE
Door:  081  State: OPEN
Door:  082  State: CLOSE
Door:  083  State: CLOSE
Door:  084  State: CLOSE
Door:  085  State: CLOSE
Door:  086  State: CLOSE
Door:  087  State: CLOSE
Door:  088  State: CLOSE
Door:  089  State: CLOSE
Door:  090  State: CLOSE
Door:  091  State: CLOSE
Door:  092  State: CLOSE
Door:  093  State: CLOSE
Door:  094  State: CLOSE
Door:  095  State: CLOSE
Door:  096  State: CLOSE
Door:  097  State: CLOSE
Door:  098  State: CLOSE
Door:  099  State: CLOSE
Door:  100  State: OPEN
```


## Ada

**unoptimized**

```mw
with Ada.Text_Io; use Ada.Text_Io;
 
 procedure Doors is
    type Door_State is (Closed, Open);
    type Door_List is array(Positive range 1..100) of Door_State;
    The_Doors : Door_List := (others => Closed);
 begin
    for I in 1..100 loop
       for J in The_Doors'range loop
          if J mod I = 0 then
             if The_Doors(J) = Closed then
                 The_Doors(J) := Open;
             else
                The_Doors(J) := Closed;
             end if;
          end if;
       end loop;
    end loop;
    for I in The_Doors'range loop
       Put_Line(Integer'Image(I) & " is " & Door_State'Image(The_Doors(I)));
    end loop;
 end Doors;
```

**optimized**

```mw
with Ada.Text_Io; use Ada.Text_Io;
 with Ada.Numerics.Elementary_Functions; use Ada.Numerics.Elementary_Functions;
 
 procedure Doors_Optimized is
    Num : Float;
 begin
    for I in 1..100 loop
       Num := Sqrt(Float(I));
       Put(Integer'Image(I) & " is ");
       if Float'Floor(Num) = Num then
          Put_Line("Opened");
       else
          Put_Line("Closed");
       end if;
    end loop;
 end Doors_Optimized;
```


## Adina

```mw
двери = новый-массив 100 ложь

цикл
  шаг
    в-диапазоне 1 101
  цикл
    номер
      в-диапазоне (шаг - 1) 100 шаг
    двери[номер] := не двери[номер]

цикл
  номер 100
  вывести/перенос
    формат «Дверь ~a ~a»
      номер + 1
      двери[номер] ? «открыта» «закрыта»
```

or in english

```mw
english()
doors = make-vector 100 #f

for
  $ step
    in-range 1 101
  for
    $ number
      in-range (step - 1) 100 step
    doors[number] := not doors[number]

for
  $ number 100
  displayln
    format "Door ~a ~a"
      number + 1
      if doors[number] "open" "closed"
```


## Agena

Translation of Algol W. Tested with Agena 2.9.5 Win32

```
# find the first few squares via the unoptimised door flipping method
scope

    local doorMax := 100;
    local door;
    create register door( doorMax );

    # set all doors to closed
    for i to doorMax do door[ i ] := false od;

    # repeatedly flip the doors
    for i to doorMax do
        for j from i to doorMax by i do door[ j ] := not door[ j ] od
    od;

    # display the results
    for i to doorMax do if door[ i ] then write( " ", i ) fi od; print()

epocs
```


## Aikido

```mw
var doors = new int [100]

foreach pass 100 {
    for (var door = pass ; door < 100 ; door += pass+1) {
        doors[door] = !doors[door]
    }
}

var d = 1
foreach door doors {
    println ("door " + d++ + " is " + (door ? "open" : "closed"))

}
```


## ALGOL 60

Works with

:

A60

```
begin
 
comment - 100 doors problem in ALGOL-60;
 
boolean array doors[1:100];
integer i, j;
boolean open, closed;
 
open := true;
closed := not true;
 
outstring(1,"100 Doors Problem\n");
 
comment - all doors are initially closed;
for i := 1 step 1 until 100 do
  doors[i] := closed;
 
comment
  cycle through at increasing intervals
  and flip each door encountered;
for i := 1 step 1 until 100 do
  for j := i step i until 100 do
    doors[j] := not doors[j];
 
comment - show which doors are open;
outstring(1,"The open doors are:");
for i := 1 step 1 until 100 do
  if doors[i] then
     outinteger(1,i);
 
end
```

**Output:**

```
100 Doors Problem
The open doors are: 1  4  9  16  25  36  49  64  81  100
```


## ALGOL 68

**unoptimized**

```
PROC doors = (INT limit)VOID:
(
  MODE DOORSTATE = BOOL;
  BOOL closed = FALSE;
  BOOL open = NOT closed;
  MODE DOORLIST = [limit]DOORSTATE;

  DOORLIST the doors;
  FOR i FROM LWB the doors TO UPB the doors DO the doors[i]:=closed OD;

  FOR i FROM LWB the doors TO UPB the doors DO
    FOR j FROM LWB the doors BY i TO UPB the doors DO
      the doors[j] := NOT the doors[j]
    OD
  OD;
  FOR i FROM LWB the doors TO UPB the doors DO
    print((whole(i,-12)," is ",(the doors[i]|"opened"|"closed"),newline))
  OD
);
doors(100)
```

**optimized**

```
PROC doors optimised = ( INT limit )VOID:
  FOR i TO limit DO
    REAL num := sqrt(i);
    print((whole(i,0)," is ",(ENTIER num = num |"opened"|"closed"),newline))
  OD
;
doors optimised(100)
```


## ALGOL W

```
begin
    % find the first few squares via the unoptimised door flipping method   %
 
    integer doorMax;
    doorMax := 100;
 
    begin
        % need to start a new block so the array can have variable bounds   %
 
        % array of doors - door( i ) is true if open, false if closed       %
        logical array door( 1 :: doorMax );
 
        % set all doors to closed                                           %
        for i := 1 until doorMax do door( i ) := false;
 
        % repeatedly flip the doors                                         %
        for i := 1 until doorMax
        do begin
            for j := i step i until doorMax
            do begin
                door( j ) := not door( j )
            end
        end;
 
        % display the results                                               %
        i_w := 1; % set integer field width                                 %
        s_w := 1; % and separator width                                     %
        for i := 1 until doorMax do if door( i ) then writeon( i )
 
    end
 
end.
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100 
```


## ALGOL-M

```mw
BEGIN

INTEGER ARRAY DOORS[1:100];
INTEGER I, J, OPEN, CLOSED;

OPEN := 1;
CLOSED := 0;

% ALL DOORS ARE INITIALLY CLOSED %
FOR I := 1 STEP 1 UNTIL 100 DO
  BEGIN
    DOORS[I] := CLOSED;
  END;

% PASS THROUGH AT INCREASING INTERVALS AND FLIP %
FOR I := 1 STEP 1 UNTIL 100 DO
  BEGIN
     FOR J := I STEP I UNTIL 100 DO
       BEGIN
         DOORS[J] := 1 - DOORS[J];
       END;
  END;

% SHOW RESULTS %
WRITE("THE OPEN DOORS ARE:");
WRITE("");
FOR I := 1 STEP 1 UNTIL 100 DO
  BEGIN
    IF DOORS[I] = OPEN THEN
      WRITEON(I);
  END;

END
```

**Output:**

```
THE OPEN DOORS ARE:
     1     4     9    16    25    36    49    64    81   100
```


## AmigaE

```mw
PROC main()
  DEF t[100]: ARRAY,
      pass, door
  FOR door := 0 TO 99 DO t[door] := FALSE
  FOR pass := 0 TO 99
    door := pass
    WHILE door <= 99
      t[door] := Not(t[door])
      door := door + pass + 1
    ENDWHILE
  ENDFOR
  FOR door := 0 TO 99 DO WriteF('\d is \s\n', door+1,
                                IF t[door] THEN 'open' ELSE 'closed')
ENDPROC
```


## APL

Works with

:

GNU APL

```mw
doors←{100⍴((⍵-1)⍴0),1}
≠⌿⊃doors¨ ⍳100
```

**optimized** Note that ⎕IO = 1

```
2|+/[1]0=D∘.|D←⍳100
```

The idea is that the *n*:th door will be flipped the same number of times as there are divisors for *n*. So first we make D all ints 1..100 (D←⍳100). The next step is to find the remainders of every such int when divided by every other (D∘.|D). This results in a 100×100 matrix which we turn into a binary one by testing if the values are equal to zero i.e. divisors. Next: sum along axis 1, i.e. the columns. This tells us the number of divisors. Finally calculate the remainder of these when divided by 2, i.e. find which *n* have an odd number of divisors, i.e. will be flipped an odd number of times and thus end up open.

Works with

:

Dyalog APL

Works with

:

GNU APL

```mw
≠⌿0=(⍳100)∘.|⍳100
```

Each of the above solutions produces the same output:

**Output:**

```
1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 
      0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
```

However the result is obtained, applying the ⍸ function (which has been in Dyalog since 16.0 and was added to GNU APL in SVN r1368, 2020-12-03) will transform the Boolean array into a list of the indices of the true values (open doors):

```mw
⍸≠⌿0=(⍳100)∘.|⍳100
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100
```


## AppleScript

### Iteration

```mw
set is_open to {}
repeat 100 times
   set end of is_open to false
end
repeat with pass from 1 to 100
  repeat with door from pass to 100 by pass
    set item door of is_open to not item door of is_open
  end
end
set open_doors to {}
repeat with door from 1 to 100
   if item door of is_open then
     set end of open_doors to door
   end
end
set text item delimiters to ", "
display dialog "Open doors: " & open_doors
```

This is similar to the above, but makes use of the fact that the final status of the first door in each pass is known as it's about to be set and the door number can thus be logged at that point if needed. It makes a separate checking repeat at the end unnecessary, the toggled status boolean doesn't need to be put back into the list, and the door number can be stored in the redundant list slot instead of a separate results list having to be built. It would be satisfying if the first pass, opening all the doors, could be combined with the initial creation of the doors list, but the task description does say "all initially closed"!

```mw
on _100doors()
    script o
        property doors : {}
    end script
    repeat 100 times
        set end of o's doors to false -- false = "not open".
    end repeat
    repeat with pass from 1 to 100
        if (not item pass of o's doors) then set item pass of o's doors to pass
        repeat with d from (pass + pass) to 100 by pass
            set item d of o's doors to (not item d of o's doors)
        end repeat
    end repeat
    
    return o's doors's integers
end _100doors

on join(lst, delim)
    set astid to AppleScript's text item delimiters
    set AppleScript's text item delimiters to delim
    set txt to lst as text
    set AppleScript's text item delimiters to astid
    return txt
end join

return "Open doors:
" & join(_100doors(), ", ")
```

**Output:**

```mw
"Open doors:
1, 4, 9, 16, 25, 36, 49, 64, 81, 100"
```

### Functional composition

```mw
-- FINAL DOOR STATES ---------------------------------------------------------

-- finalDoors :: Int -> [(Int, Bool)]
on finalDoors(n)
    
    -- toggledCorridor :: [(Int, Bool)] -> (Int, Bool) -> Int -> [(Int, Bool)]
    script toggledCorridor
        on |λ|(a, _, k)
            
            -- perhapsToggled :: Bool -> Int -> Bool
            script perhapsToggled
                on |λ|(x, i)
                    if i mod k = 0 then
                        {i, not item 2 of x}
                    else
                        {i, item 2 of x}
                    end if
                end |λ|
            end script
            
            map(perhapsToggled, a)
        end |λ|
    end script
    
    set xs to enumFromTo(1, n)
    
    foldl(toggledCorridor, ¬
        zip(xs, replicate(n, {false})), xs)
end finalDoors

-- TEST ----------------------------------------------------------------------
on run
    -- isOpenAtEnd :: (Int, Bool) -> Bool
    script isOpenAtEnd
        on |λ|(door)
            (item 2 of door)
        end |λ|
    end script
    
    -- doorNumber :: (Int, Bool) -> Int
    script doorNumber
        on |λ|(door)
            (item 1 of door)
        end |λ|
    end script
    
    map(doorNumber, filter(isOpenAtEnd, finalDoors(100)))
    
    --> {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
end run

-- GENERIC FUNCTIONS ---------------------------------------------------------

-- enumFromTo :: Int -> Int -> [Int]
on enumFromTo(m, n)
    if n < m then
        set d to -1
    else
        set d to 1
    end if
    set lst to {}
    repeat with i from m to n by d
        set end of lst to i
    end repeat
    return lst
end enumFromTo

-- filter :: (a -> Bool) -> [a] -> [a]
on filter(f, xs)
    tell mReturn(f)
        set lst to {}
        set lng to length of xs
        repeat with i from 1 to lng
            set v to item i of xs
            if |λ|(v, i, xs) then set end of lst to v
        end repeat
        return lst
    end tell
end filter

-- foldl :: (a -> b -> a) -> a -> [b] -> a
on foldl(f, startValue, xs)
    tell mReturn(f)
        set v to startValue
        set lng to length of xs
        repeat with i from 1 to lng
            set v to |λ|(v, item i of xs, i, xs)
        end repeat
        return v
    end tell
end foldl

-- map :: (a -> b) -> [a] -> [b]
on map(f, xs)
    tell mReturn(f)
        set lng to length of xs
        set lst to {}
        repeat with i from 1 to lng
            set end of lst to |λ|(item i of xs, i, xs)
        end repeat
        return lst
    end tell
end map

-- min :: Ord a => a -> a -> a
on min(x, y)
    if y < x then
        y
    else
        x
    end if
end min

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

-- replicate :: Int -> a -> [a]
on replicate(n, a)
    set out to {}
    if n < 1 then return out
    set dbl to {a}
    
    repeat while (n > 1)
        if (n mod 2) > 0 then set out to out & dbl
        set n to (n div 2)
        set dbl to (dbl & dbl)
    end repeat
    return out & dbl
end replicate

-- zip :: [a] -> [b] -> [(a, b)]
on zip(xs, ys)
    set lng to min(length of xs, length of ys)
    set lst to {}
    repeat with i from 1 to lng
        set end of lst to {item i of xs, item i of ys}
    end repeat
    return lst
end zip
```

**Output:**

```mw
{1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
```

### Odd numbers of integer factors

The question of which doors are flipped an odd number of times reduces to the question of which numbers in the range have an odd number of integer factors (for an AppleScript implementation of integerFactors(n) see Factors of An Integer). Using **map** from the functional composition example above:

```mw
map(factorCountMod2, enumFromTo(1, 100))

on factorCountMod2(n)
    {n, (length of integerFactors(n)) mod 2 = 1}
end factorCountMod2
```

This, on inspection, and further reflection, then collapses to the even simpler question of which numbers are perfect squares, since all other numbers have an even number of integer factors (n factors below the square root, plus n paired cofactors above the square root). Using **map** and **enumFromTo** from the functional composition example above:

```mw
-- perfectSquaresUpTo :: Int -> [Int]
on perfectSquaresUpTo(n)
    script squared
        -- (Int -> Int)
        on |λ|(x)
            x * x
        end |λ|
    end script
    
    set realRoot to n ^ (1 / 2)
    set intRoot to realRoot as integer
    set blnNotPerfectSquare to not (intRoot = realRoot)
    
    map(squared, enumFromTo(1, intRoot - (blnNotPerfectSquare as integer)))
end perfectSquaresUpTo

on run
    
    perfectSquaresUpTo(100)
    
end run
```

**Output:**

```mw
{1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
```


## Arbre

```mw
openshut(n):
  for x in [1..n]
    x%n==0

pass(n):
  if n==100
    openshut(n)
  else
    openshut(n) xor pass(n+1)

100doors():
  pass(1) -> io
```


## Argile

```mw
use std, array

close all doors
for each pass from 1 to 100
  for (door = pass) (door <= 100) (door += pass)
    toggle door

let int pass, door.

.: close all doors :. {memset doors 0 size of doors}
.:toggle <int door>:. {    !!(doors[door - 1])     }

let doors be an array of 100 bool

for each door from 1 to 100
  printf "#%.3d %s\n" door (doors[door - 1]) ? "[ ]", "[X]"
```


## ArkScript

Works with

:

ArkScript

version 4.0.0

```mw
(import std.Range :range :forEach)
(import std.List)

(mut doors (list:fill 100 false))
(let r (range 0 100))

(forEach r
  (fun (i) {
    (mut j i)
    (while (< j 100) {
      (@= doors j (not (@ doors j)))
      (set j (+ j i 1)) })
    (print doors) }))

(print
  (list:map
    (list:filter
      (list:zipWithIndex doors)
      (fun (e)
        (@ e 1)))
    (fun (e) (@ e 0))))
```

**Output:**

```mw
[true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true true]
...
[true false false true false false false false true false false false false false false true false false false false false false false false true false false false false false false false false false false true false false false false false false false false false false false false true false false false false false false false false false false false false false false true false false false false false false false false false false false false false false false false true false false false false false false false false false false false false false false false false false false true]
[0 3 8 15 24 35 48 63 80 99]
```
