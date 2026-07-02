---
title: "Ackermann function (part 1/6)"
source: https://rosettacode.org/wiki/Ackermann_function
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/6
---

# Ackermann function

The **Ackermann function** is a classic example of a recursive function, notable especially because it is not a primitive recursive function. It grows very quickly in value, as does the size of its call tree.

The Ackermann function is usually defined as follows:

${\displaystyle A(m,n)={\begin{cases}n+1&{\mbox{if }}m=0\\A(m-1,1)&{\mbox{if }}m>0{\mbox{ and }}n=0\\A(m-1,A(m,n-1))&{\mbox{if }}m>0{\mbox{ and }}n>0.\end{cases}}}$

Its arguments are never negative and it always terminates.

**Task**

Write a function which returns the value of ${\displaystyle A(m,n)}$ . Arbitrary precision is preferred (since the function grows so quickly), but not required.

**See also**

- Conway chained arrow notation for the Ackermann function.


## 11l

Translation of

:

Python

```mw
F ack2(m, n) -> Int
   R I m == 0 {(n + 1)
 } E I m == 1 {(n + 2)
 } E I m == 2 {(2 * n + 3)
 } E I m == 3 {(8 * (2 ^ n - 1) + 5)
 } E I n == 0 {ack2(m - 1, 1)
 } E ack2(m - 1, ack2(m, n - 1))

print(ack2(0, 0))
print(ack2(3, 4))
print(ack2(4, 1))
```

**Output:**

```
1
125
65533
```


## 360 Assembly

Translation of

:

AWK

The OS/360 linkage is a bit tricky with the S/360 basic instruction set. To simplify, the program is recursive not reentrant.

```mw
*        Ackermann function        07/09/2015
&LAB     XDECO &REG,&TARGET
.*-----------------------------------------------------------------*
.*       THIS MACRO DISPLAYS THE REGISTER CONTENTS AS A TRUE       *
.*       DECIMAL VALUE. XDECO IS NOT PART OF STANDARD S360 MACROS! *
*------------------------------------------------------------------*
         AIF   (T'&REG EQ 'O').NOREG
         AIF   (T'&TARGET EQ 'O').NODEST
&LAB     B     I&SYSNDX               BRANCH AROUND WORK AREA
W&SYSNDX DS    XL8                    CONVERSION WORK AREA
I&SYSNDX CVD   &REG,W&SYSNDX          CONVERT TO DECIMAL
         MVC   &TARGET,=XL12'402120202020202020202020'
         ED    &TARGET,W&SYSNDX+2     MAKE FIELD PRINTABLE
         BC    2,*+12                 BYPASS NEGATIVE
         MVI   &TARGET+12,C'-'        INSERT NEGATIVE SIGN
         B     *+8                    BYPASS POSITIVE
         MVI   &TARGET+12,C'+'        INSERT POSITIVE SIGN
         MEXIT
.NOREG   MNOTE 8,'INPUT REGISTER OMITTED'
         MEXIT
.NODEST  MNOTE 8,'TARGET FIELD OMITTED'
         MEXIT
         MEND
ACKERMAN CSECT
         USING  ACKERMAN,R12       r12 : base register
         LR     R12,R15            establish base register
         ST     R14,SAVER14A       save r14
         LA     R4,0               m=0
LOOPM    CH     R4,=H'3'           do m=0 to 3
         BH     ELOOPM
         LA     R5,0               n=0
LOOPN    CH     R5,=H'8'           do n=0 to 8         
         BH     ELOOPN
         LR     R1,R4              m
         LR     R2,R5              n
         BAL    R14,ACKER          r1=acker(m,n)
         XDECO  R1,PG+19
         XDECO  R4,XD
         MVC    PG+10(2),XD+10
         XDECO  R5,XD
         MVC    PG+13(2),XD+10
         XPRNT  PG,44              print buffer
         LA     R5,1(R5)           n=n+1
         B      LOOPN
ELOOPN   LA     R4,1(R4)           m=m+1
         B      LOOPM
ELOOPM   L      R14,SAVER14A       restore r14
         BR     R14                return to caller
SAVER14A DS     F                  static save r14
PG       DC     CL44'Ackermann(xx,xx) = xxxxxxxxxxxx'
XD       DS     CL12
ACKER    CNOP   0,4                function r1=acker(r1,r2)
         LR     R3,R1              save argument r1 in r3
         LR     R9,R10             save stackptr (r10) in r9 temp
         LA     R1,STACKLEN        amount of storage required
         GETMAIN RU,LV=(R1)        allocate storage for stack
         USING  STACK,R10          make storage addressable
         LR     R10,R1             establish stack addressability
         ST     R14,SAVER14B       save previous r14
         ST     R9,SAVER10B        save previous r10
         LR     R1,R3              restore saved argument r1
START    ST     R1,M               stack m
         ST     R2,N               stack n
IF1      C      R1,=F'0'           if m<>0
         BNE    IF2                then goto if2
         LR     R11,R2             n
         LA     R11,1(R11)         return n+1
         B      EXIT
IF2      C      R2,=F'0'           else if m<>0
         BNE    IF3                then goto if3
         BCTR   R1,0               m=m-1
         LA     R2,1               n=1
         BAL    R14,ACKER          r1=acker(m)
         LR     R11,R1             return acker(m-1,1)
         B      EXIT
IF3      BCTR   R2,0               n=n-1
         BAL    R14,ACKER          r1=acker(m,n-1)
         LR     R2,R1              acker(m,n-1)
         L      R1,M               m
         BCTR   R1,0               m=m-1         
         BAL    R14,ACKER          r1=acker(m-1,acker(m,n-1))
         LR     R11,R1             return acker(m-1,1)
EXIT     L      R14,SAVER14B       restore r14
         L      R9,SAVER10B        restore r10 temp
         LA     R0,STACKLEN        amount of storage to free
         FREEMAIN A=(R10),LV=(R0)  free allocated storage
         LR     R1,R11             value returned
         LR     R10,R9             restore r10
         BR     R14                return to caller
         LTORG
         DROP   R12                base no longer needed
STACK    DSECT                     dynamic area
SAVER14B DS     F                  saved r14
SAVER10B DS     F                  saved r10
M        DS     F                  m
N        DS     F                  n
STACKLEN EQU    *-STACK
         YREGS  
         END    ACKERMAN
```

**Output:**

```
Ackermann( 0, 0) =            1
Ackermann( 0, 1) =            2
Ackermann( 0, 2) =            3
Ackermann( 0, 3) =            4
Ackermann( 0, 4) =            5
Ackermann( 0, 5) =            6
Ackermann( 0, 6) =            7
Ackermann( 0, 7) =            8
Ackermann( 0, 8) =            9
Ackermann( 1, 0) =            2
Ackermann( 1, 1) =            3
Ackermann( 1, 2) =            4
Ackermann( 1, 3) =            5
Ackermann( 1, 4) =            6
Ackermann( 1, 5) =            7
Ackermann( 1, 6) =            8
Ackermann( 1, 7) =            9
Ackermann( 1, 8) =           10
Ackermann( 2, 0) =            3
Ackermann( 2, 1) =            5
Ackermann( 2, 2) =            7
Ackermann( 2, 3) =            9
Ackermann( 2, 4) =           11
Ackermann( 2, 5) =           13
Ackermann( 2, 6) =           15
Ackermann( 2, 7) =           17
Ackermann( 2, 8) =           19
Ackermann( 3, 0) =            5
Ackermann( 3, 1) =           13
Ackermann( 3, 2) =           29
Ackermann( 3, 3) =           61
Ackermann( 3, 4) =          125
Ackermann( 3, 5) =          253
Ackermann( 3, 6) =          509
Ackermann( 3, 7) =         1021
Ackermann( 3, 8) =         2045
```


## 68000 Assembly

This implementation is based on the code shown in the computerphile episode in the youtube link at the top of this page (time index 5:00).

```mw
;
; Ackermann function for Motorola 68000 under AmigaOs 2+ by Thorham
;
; Set stack space to 60000 for m = 3, n = 5.
;
; The program will print the ackermann values for the range m = 0..3, n = 0..5
;
_LVOOpenLibrary equ -552
_LVOCloseLibrary equ -414
_LVOVPrintf equ -954

m equ 3 ; Nr of iterations for the main loop.
n equ 5 ; Do NOT set them higher, or it will take hours to complete on
        ; 68k, not to mention that the stack usage will become astronomical.
        ; Perhaps n can be a little higher... If you do increase the ranges
        ; then don't forget to increase the stack size.

execBase=4

start
    move.l  execBase,a6

    lea     dosName,a1
    moveq   #36,d0
    jsr     _LVOOpenLibrary(a6)
    move.l  d0,dosBase
    beq     exit

    move.l  dosBase,a6
    lea     printfArgs,a2

    clr.l   d3 ; m
.loopn
    clr.l   d4 ; n
.loopm
    bsr     ackermann

    move.l  d3,0(a2)
    move.l  d4,4(a2)
    move.l  d5,8(a2)
    move.l  #outString,d1
    move.l  a2,d2
    jsr     _LVOVPrintf(a6)

    addq.l  #1,d4
    cmp.l   #n,d4
    ble     .loopm

    addq.l  #1,d3
    cmp.l   #m,d3
    ble     .loopn

exit
    move.l  execBase,a6
    move.l  dosBase,a1
    jsr     _LVOCloseLibrary(a6)
    rts
;
; ackermann function
;
; in:
;
; d3 = m
; d4 = n
;
; out:
;
; d5 = ans
;
ackermann
    move.l  d3,-(sp)
    move.l  d4,-(sp)

    tst.l   d3
    bne     .l1
    move.l  d4,d5
    addq.l  #1,d5
    bra     .return
.l1
    tst.l   d4
    bne     .l2
    subq.l  #1,d3
    moveq   #1,d4
    bsr     ackermann
    bra     .return
.l2
    subq.l  #1,d4
    bsr     ackermann
    move.l  d5,d4
    subq.l  #1,d3
    bsr     ackermann

.return
    move.l  (sp)+,d4
    move.l  (sp)+,d3
    rts
;
; variables
;
dosBase
    dc.l    0

printfArgs
    dcb.l   3
;
; strings
;
dosName
    dc.b    "dos.library",0

outString
    dc.b    "ackermann (%ld,%ld) is: %ld",10,0
```


## 8080 Assembly

This function does 16-bit math. The test code prints a table of `ack(m,n)` for `m ∊ [0,4)` and `n ∊ [0,9)`, on a real 8080 this takes a little over two minutes.

```mw
	org	100h
	jmp	demo
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;	ACK(M,N); DE=M, HL=N, return value in HL.
ack:	mov	a,d	; M=0?
	ora	e
	jnz	ackm
	inx	h	; If so, N+1.
	ret
ackm:	mov	a,h	; N=0?
	ora	l
	jnz	ackmn
	lxi	h,1	; If so, N=1,
	dcx	d	; N-=1,
	jmp	ack	; A(M,N) - tail recursion
ackmn:	push	d	; M>0 and N>0: store M on the stack
	dcx	h	; N-=1
	call	ack	; N = ACK(M,N-1)
	pop	d	; Restore previous M
	dcx	d	; M-=1
	jmp	ack	; A(M,N) - tail recursion
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;	Print table of ack(m,n)
MMAX:	equ	4	; Size of table to print. Note that math is done in
NMAX:	equ	9	; 16 bits. 
demo:	lhld	6	; Put stack pointer at top of available memory
	sphl
	lxi	b,0	; let B,C hold 8-bit M and N.
acknum:	xra	a	; Set high bit of M and N to zero
	mov	d,a	; DE = B (M)
	mov	e,b
	mov	h,a	; HL = C (N)
	mov	l,c
	call	ack	; HL = ack(DE,HL)
	call	prhl	; Print the number
	inr	c	; N += 1
	mvi	a,NMAX	; Time for next line?
	cmp	c
	jnz	acknum	; If not, print next number
	push	b	; Otherwise, save BC
	mvi	c,9	; Print newline
	lxi	d,nl
	call	5
	pop	b	; Restore BC
	mvi	c,0	; Set N to 0
	inr	b	; M += 1
	mvi	a,MMAX	; Time to stop?
	cmp	b
	jnz	acknum	; If not, print next number
	rst	0
	;;;	Print HL as ASCII number.
prhl:	push	h	; Save all registers
	push	d
	push	b
	lxi	b,pnum	; Store pointer to num string on stack
	push	b
	lxi	b,-10	; Divisor
prdgt:	lxi	d,-1
prdgtl:	inx	d	; Divide by 10 through trial subtraction
	dad	b
	jc	prdgtl
	mvi	a,'0'+10
	add	l	; L = remainder - 10
	pop	h	; Get pointer from stack
	dcx	h	; Store digit
	mov	m,a
	push	h	; Put pointer back on stack
	xchg		; Put quotient in HL
	mov	a,h	; Check if zero 
	ora	l
	jnz	prdgt	; If not, next digit
	pop	d	; Get pointer and put in DE
	mvi	c,9	; CP/M print string
	call	5
	pop	b	; Restore registers 
	pop	d
	pop	h
	ret
	db	'*****'	; Placeholder for number
pnum:	db	9,'$'
nl:	db	13,10,'$'
```

**Output:**

```
1       2       3       4       5       6       7       8       9
2       3       4       5       6       7       8       9       10
3       5       7       9       11      13      15      17      19
5       13      29      61      125     253     509     1021    2045
```


## 8086 Assembly

This code does 16-bit math just like the 8080 version.

```mw
	cpu	8086
	bits	16
	org	100h
section	.text
	jmp	demo
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;	ACK(M,N); DX=M, AX=N, return value in AX.
ack:	and	dx,dx	; N=0?
	jnz	.m
	inc	ax	; If so, return N+1
	ret
.m:	and	ax,ax	; M=0?
	jnz	.mn
	mov	ax,1	; If so, N=1,
	dec	dx	; M -= 1
	jmp	ack	; ACK(M-1,1) - tail recursion
.mn:	push	dx	; Keep M on the stack
	dec	ax	; N-=1
	call	ack	; N = ACK(M,N-1)
	pop	dx	; Restore M
	dec	dx	; M -= 1
	jmp	ack	; ACK(M-1,ACK(M,N-1)) - tail recursion
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;	Print table of ack(m,n)
MMAX:	equ	4	; Size of table to print. Noe that math is done
NMAX:	equ	9	; in 16 bits.
demo:	xor	si,si	; Let SI hold M,
	xor	di,di	; and DI hold N.
acknum:	mov	dx,si	; Calculate ack(M,N)
	mov	ax,di
	call	ack
	call	prax	; Print number
	inc	di	; N += 1
	cmp	di,NMAX	; Row done?
	jb	acknum	; If not, print next number on row
	xor	di,di	; Otherwise, N=0,
	inc	si	; M += 1
	mov	dx,nl	; Print newline
	call	prstr
	cmp	si,MMAX	; Done?
	jb	acknum	; If not, start next row
	ret		; Otherwise, stop.
	;;;	Print AX as ASCII number.
prax:	mov	bx,pnum	; Pointer to number string
	mov	cx,10	; Divisor
.dgt:	xor	dx,dx	; Divide AX by ten
	div	cx
	add	dl,'0'	; DX holds remainder - add ASCII 0
	dec	bx	; Move pointer backwards
	mov	[bx],dl	; Save digit in string
	and	ax,ax	; Are we done yet?
	jnz	.dgt	; If not, next digit
	mov	dx,bx	; Tell DOS to print the string
prstr:	mov	ah,9
	int	21h
	ret
section	.data
	db	'*****'	; Placeholder for ASCII number
pnum:	db	9,'$'
nl:	db	13,10,'$'
```

**Output:**

```
1       2       3       4       5       6       7       8       9
2       3       4       5       6       7       8       9       10
3       5       7       9       11      13      15      17      19
5       13      29      61      125     253     509     1021    2045
```


## 8th

```mw
\ Ackermann function, illustrating use of "memoization".

\ Memoization is a technique whereby intermediate computed values are stored
\ away against later need.  It is particularly valuable when calculating those
\ values is time or resource intensive, as with the Ackermann function.

\ make the stack much bigger so this can complete!
100000 stack-size

\ This is where memoized values are stored:
{} var, dict

\ Simple accessor words
: dict! \ "key" val --
  dict @ -rot m:! drop ;

: dict@ \ "key" -- val
  dict @ swap m:@ nip ;

defer: ack1

\ We just jam the string representation of the two numbers together for a key:
: makeKey  \ m n -- m n key
	2dup >s swap >s s:+ ;

: ack2 \ m n -- A
	makeKey dup
	dict@ null?
	if \ can't find key in dict
		\ m n key null
		drop \ m n key
		-rot \ key m n
		ack1 \ key A
		tuck \ A key A
		dict! \ A
	else \ found value
		\ m n key value
		>r drop 2drop r>
	then ;

: ack \ m n -- A
	over not 
	if
		nip n:1+
	else
		dup not
		if
			drop n:1- 1 ack2
		else
			over swap n:1- ack2
			swap n:1- swap ack2
		then
	then ;

' ack is ack1

: ackOf \ m n --
        2dup
        "Ack(" . swap . ", " . . ") = " . ack . cr ;

0 0 ackOf
0 4 ackOf
1 0 ackOf
1 1 ackOf
2 1 ackOf
2 2 ackOf
3 1 ackOf
3 3 ackOf
4 0 ackOf

\ this last requires a very large data stack.  So start 8th with a parameter '-k 100000'
4 1 ackOf

bye
```

**The output:**

```
Ack(0, 0) = 1
Ack(0, 4) = 5
Ack(1, 0) = 2
Ack(1, 1) = 3
Ack(2, 1) = 5
Ack(2, 2) = 7
Ack(3, 1) = 13
Ack(3, 3) = 61
Ack(4, 0) = 13
Ack(4, 1) = 65533
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

or android 64 bits with application Termux

```mw
/* ARM assembly AARCH64 Raspberry PI 3B or android 64 bits */
/*  program ackermann64.s   */ 

/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"
.equ MMAXI,   4
.equ NMAXI,   10

/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:        .asciz "Result for @  @  : @ \n"
szMessError:        .asciz "Overflow !!.\n"
szCarriageReturn:   .asciz "\n"
 
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
main:                           // entry of program 
    mov x3,#0
    mov x4,#0
1:
    mov x0,x3
    mov x1,x4
    bl ackermann
    mov x5,x0
    mov x0,x3
    ldr x1,qAdrsZoneConv        // else display odd message
    bl conversion10             // call decimal conversion
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv        // insert value conversion in message
    bl strInsertAtCharInc
    mov x6,x0
    mov x0,x4
    ldr x1,qAdrsZoneConv        // else display odd message
    bl conversion10             // call decimal conversion
    mov x0,x6
    ldr x1,qAdrsZoneConv        // insert value conversion in message
    bl strInsertAtCharInc
    mov x6,x0
    mov x0,x5
    ldr x1,qAdrsZoneConv        // else display odd message
    bl conversion10             // call decimal conversion
    mov x0,x6
    ldr x1,qAdrsZoneConv        // insert value conversion in message
    bl strInsertAtCharInc
    bl affichageMess
    add x4,x4,#1
    cmp x4,#NMAXI
    blt 1b
    mov x4,#0
    add x3,x3,#1
    cmp x3,#MMAXI
    blt 1b
100:                            // standard end of the program 
    mov x0, #0                  // return code
    mov x8, #EXIT               // request to exit program
    svc #0                      // perform the system call
 
qAdrszCarriageReturn:     .quad szCarriageReturn
qAdrsMessResult:          .quad sMessResult
qAdrsZoneConv:            .quad sZoneConv
/***************************************************/
/*     fonction ackermann              */
/***************************************************/
// x0 contains a number m
// x1 contains a number n
// x0 return résult
ackermann:
    stp x1,lr,[sp,-16]!         // save  registres
    stp x2,x3,[sp,-16]!         // save  registres
    cmp x0,0
    beq 5f
    mov x3,-1
    csel x0,x3,x0,lt               // error
    blt 100f
    cmp x1,#0
    csel x0,x3,x0,lt               // error
    blt 100f
    bgt 1f
    sub x0,x0,#1
    mov x1,#1
    bl ackermann
    b 100f
1:
    mov x2,x0
    sub x1,x1,#1
    bl ackermann
    mov x1,x0
    sub x0,x2,#1
    bl ackermann
    b 100f
5:
    adds x0,x1,#1
    bcc 100f
    ldr x0,qAdrszMessError
    bl affichageMess
    mov x0,-1
100:

    ldp x2,x3,[sp],16         // restaur des  2 registres
    ldp x1,lr,[sp],16         // restaur des  2 registres
    ret
qAdrszMessError:        .quad szMessError

/********************************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```

**Output:**

```
Result for 0  0  : 1
Result for 0  1  : 2
Result for 0  2  : 3
Result for 0  3  : 4
Result for 0  4  : 5
Result for 0  5  : 6
Result for 0  6  : 7
Result for 0  7  : 8
Result for 0  8  : 9
Result for 0  9  : 10
Result for 1  0  : 2
Result for 1  1  : 3
Result for 1  2  : 4
Result for 1  3  : 5
Result for 1  4  : 6
Result for 1  5  : 7
Result for 1  6  : 8
Result for 1  7  : 9
Result for 1  8  : 10
Result for 1  9  : 11
Result for 2  0  : 3
Result for 2  1  : 5
Result for 2  2  : 7
Result for 2  3  : 9
Result for 2  4  : 11
Result for 2  5  : 13
Result for 2  6  : 15
Result for 2  7  : 17
Result for 2  8  : 19
Result for 2  9  : 21
Result for 3  0  : 5
Result for 3  1  : 13
Result for 3  2  : 29
Result for 3  3  : 61
Result for 3  4  : 125
Result for 3  5  : 253
Result for 3  6  : 509
Result for 3  7  : 1021
Result for 3  8  : 2045
Result for 3  9  : 4093
```


## ABAP

```mw
REPORT  zhuberv_ackermann.

CLASS zcl_ackermann DEFINITION.
  PUBLIC SECTION.
    CLASS-METHODS ackermann IMPORTING m TYPE i
                                      n TYPE i
                            RETURNING value(v) TYPE i.
ENDCLASS.            "zcl_ackermann DEFINITION

CLASS zcl_ackermann IMPLEMENTATION.

  METHOD: ackermann.

    DATA: lv_new_m TYPE i,
          lv_new_n TYPE i.

    IF m = 0.
      v = n + 1.
    ELSEIF m > 0 AND n = 0.
      lv_new_m = m - 1.
      lv_new_n = 1.
      v = ackermann( m = lv_new_m n = lv_new_n ).
    ELSEIF m > 0 AND n > 0.
      lv_new_m = m - 1.

      lv_new_n = n - 1.
      lv_new_n = ackermann( m = m n = lv_new_n ).

      v = ackermann( m = lv_new_m n = lv_new_n ).
    ENDIF.

  ENDMETHOD.                    "ackermann

ENDCLASS.                    "zcl_ackermann IMPLEMENTATION

PARAMETERS: pa_m TYPE i,
            pa_n TYPE i.

DATA: lv_result TYPE i.

START-OF-SELECTION.
  lv_result = zcl_ackermann=>ackermann( m = pa_m n = pa_n ).
  WRITE: / lv_result.
```


## ABC

```mw
HOW TO RETURN m ack n:
    SELECT:
        m=0: RETURN n+1
        m>0 AND n=0: RETURN (m-1) ack 1
        m>0 AND n>0: RETURN (m-1) ack (m ack (n-1))

FOR m IN {0..3}:
    FOR n IN {0..8}:
        WRITE (m ack n)>>6
    WRITE /
```

**Output:**

```
     1     2     3     4     5     6     7     8     9
     2     3     4     5     6     7     8     9    10
     3     5     7     9    11    13    15    17    19
     5    13    29    61   125   253   509  1021  2045
```


## Acornsoft Lisp

Translation of

:

Common Lisp

```mw
(defun ack (m n)
  (cond ((zerop m) (add1 n))
        ((zerop n) (ack (sub1 m) 1))
        (t         (ack (sub1 m) (ack m (sub1 n))))))
```

**Output:**

```
Evaluate : (ack 3 5)

Value is : 253
```


## Action!

Action! language does not support recursion. Therefore an iterative approach with a stack has been proposed.

```mw
DEFINE MAXSIZE="1000"
CARD ARRAY stack(MAXSIZE)
CARD stacksize=[0]

BYTE FUNC IsEmpty()
  IF stacksize=0 THEN
    RETURN (1)
  FI
RETURN (0)

PROC Push(BYTE v)
  IF stacksize=maxsize THEN
    PrintE("Error: stack is full!")
    Break()
  FI
  stack(stacksize)=v
  stacksize==+1
RETURN

BYTE FUNC Pop()
  IF IsEmpty() THEN
    PrintE("Error: stack is empty!")
    Break()
  FI
  stacksize==-1
RETURN (stack(stacksize))

CARD FUNC Ackermann(CARD m,n)
  Push(m)
  WHILE IsEmpty()=0
  DO
    m=Pop()
    IF m=0 THEN
      n==+1
    ELSEIF n=0 THEN
      n=1
      Push(m-1)
    ELSE
      n==-1
      Push(m-1)
      Push(m)
    FI
  OD
RETURN (n)

PROC Main()
  CARD m,n,res

  FOR m=0 TO 3
  DO
    FOR n=0 TO 4
    DO
      res=Ackermann(m,n)
      PrintF("Ack(%U,%U)=%U%E",m,n,res)
    OD
  OD
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
Ack(0,0)=1
Ack(0,1)=2
Ack(0,2)=3
Ack(0,3)=4
Ack(0,4)=5
Ack(1,0)=2
Ack(1,1)=3
Ack(1,2)=4
Ack(1,3)=5
Ack(1,4)=6
Ack(2,0)=3
Ack(2,1)=5
Ack(2,2)=7
Ack(2,3)=9
Ack(2,4)=11
Ack(3,0)=5
Ack(3,1)=13
Ack(3,2)=29
Ack(3,3)=61
Ack(3,4)=125
```


## ActionScript

```mw
public function ackermann(m:uint, n:uint):uint
{
    if (m == 0)
    {
        return n + 1;
    }
    if (n == 0)
    {
        return ackermann(m - 1, 1);
    }		

    return ackermann(m - 1, ackermann(m, n - 1));
}
```


## Ada

```mw
with Ada.Text_IO;  use Ada.Text_IO;

procedure Test_Ackermann is
   function Ackermann (M, N : Natural) return Natural is
   begin
      if M = 0 then
         return N + 1;
      elsif N = 0 then
         return Ackermann (M - 1, 1);
      else
         return Ackermann (M - 1, Ackermann (M, N - 1));
      end if;
   end Ackermann;
begin
   for M in 0..3 loop
      for N in 0..6 loop
         Put (Natural'Image (Ackermann (M, N)));
      end loop;
      New_Line;
   end loop;
end Test_Ackermann;
```

The implementation does not care about arbitrary precision numbers because the Ackermann function does not only grow, but also slow quickly, when computed recursively.

**Output:**

the first 4x7 Ackermann's numbers

```
 1 2 3 4 5 6 7
 2 3 4 5 6 7 8
 3 5 7 9 11 13 15
 5 13 29 61 125 253 509
```


## Agda

Works with

:

Agda

version 2.6.3

Library:

agda-stdlib v1.7

```mw
module Ackermann where

open import Data.Nat using (ℕ ; zero ; suc ; _+_)

ack : ℕ → ℕ → ℕ
ack zero n = n + 1
ack (suc m) zero = ack m 1
ack (suc m) (suc n) = ack m (ack (suc m) n)
      

open import Agda.Builtin.IO using (IO)
open import Agda.Builtin.Unit using (⊤)
open import Agda.Builtin.String using (String)
open import Data.Nat.Show using (show)

postulate putStrLn : String → IO ⊤
{-# FOREIGN GHC import qualified Data.Text as T #-}
{-# COMPILE GHC putStrLn = putStrLn . T.unpack #-}

main : IO ⊤
main = putStrLn (show (ack 3 9))

-- Output:
-- 4093
```

The Unicode characters can be entered in Emacs Agda as follows:

- ℕ : \bN
- → : \to
- ⊤ : \top

Running in Bash:

```mw
agda --compile Ackermann.agda
./Ackermann
```

**Output:**

```
4093
```


## Agena

This attempts to reduce the depth of recursion by using Agena'a "remember tables" to memoise the function and also expands n = 1, 2 and 3, as in the Maple, Mathematica, etc. samples. Also uses the variable column width idea from the Phix sample to keep the output table width relatively smallish.

```mw
scope # Ackermann function

    proc ackermann( m :: number, n :: number ) :: number
        feature reminisce; # create a remember table for this procedure
                           # it seems the procedure must be global for this statement
        return if   m = 0 then n + 1
               elif m = 1 then n + 2                   # expand some cases to avoid more
               elif m = 2 then 3 + 2 * n               # recursion - as in the Maple
               elif m = 3 then 5 + 8 * ( 2 ^ n - 1 )   # Mathematica, etc. samples
               elif n = 0 then ackermann( m - 1, 1 )
               else ackermann( m - 1, ackermann( m, n - 1 ) )
               fi
    end;

    local constant fmt := seq( " %1.0f", " %2.0f", " %2.0f", " %2.0f"
                             , " %3.0f", " %3.0f", " %3.0f", " %4.0f"
                             , " %4.0f", " %4.0f", " %4.0f", " %5.0f"
                             , " %5.0f", " %5.0f", " %6.0f", " %6.0f"
                             , " %6.0f", " %7.0f", " %7.0f", " %7.0f"
                             , " %7.0f", " %7.0f", " %7.0f", " %7.0f"
                            );
    local constant maxN := 20;

    printf( "  n" );
    for n from 0 to maxN do printf( fmt[ n + 1 ], n ) od;
    print();
    printf( " m+" );
    for n from 0 to 18 do printf( "------", n ) od;
    print();

    for m from 0 to 3 do
        printf( "%2d|", m );
        for n from 0 to maxN do
            printf( fmt[ n + 1 ], ackermann( m, n ) )
        od;
        print()
    od

end
```

**Output:**

```
  n 0  1  2  3   4   5   6    7    8    9   10    11    12    13     14     15     16      17      18      19      20
 m+------------------------------------------------------------------------------------------------------------------
 0| 1  2  3  4   5   6   7    8    9   10   11    12    13    14     15     16     17      18      19      20      21
 1| 2  3  4  5   6   7   8    9   10   11   12    13    14    15     16     17     18      19      20      21      22
 2| 3  5  7  9  11  13  15   17   19   21   23    25    27    29     31     33     35      37      39      41      43
 3| 5 13 29 61 125 253 509 1021 2045 4093 8189 16381 32765 65533 131069 262141 524285 1048573 2097149 4194301 8388605
```


## ALGOL 60

Works with

:

A60

```mw
begin 
   integer procedure ackermann(m,n);value m,n;integer m,n;
   ackermann:=if m=0 then n+1
         else if n=0 then ackermann(m-1,1)
                     else ackermann(m-1,ackermann(m,n-1));
   integer m,n;
   for m:=0 step 1 until 3 do begin
      for n:=0 step 1 until 6 do
         outinteger(1,ackermann(m,n));
      outstring(1,"\n")
   end
end
```

**Output:**

```
 1  2  3  4  5  6  7
 2  3  4  5  6  7  8
 3  5  7  9  11  13  15
 5  13  29  61  125  253  509
```


## ALGOL 68

Translation of

:

Ada

Works with

:

ALGOL 68

version Standard - no extensions to language used

Works with

:

ALGOL 68G

version Any - tested with release mk15-0.8b.fc9.i386

Works with

:

ELLA ALGOL 68

version Any (with appropriate job cards) - tested with release 1.8.8d.fc9.i386

```mw
PROC test ackermann = VOID: 
BEGIN
   PROC ackermann = (INT m, n)INT:
   BEGIN
      IF m = 0 THEN
         n + 1
      ELIF n = 0 THEN
         ackermann (m - 1, 1)
      ELSE
         ackermann (m - 1, ackermann (m, n - 1))
      FI
   END # ackermann #;

   FOR m FROM 0 TO 3 DO
      FOR n FROM 0 TO 6 DO
         print(ackermann (m, n))
      OD;
      new line(stand out)
   OD
END # test ackermann #;
test ackermann
```

**Output:**

```
         +1         +2         +3         +4         +5         +6         +7
         +2         +3         +4         +5         +6         +7         +8
         +3         +5         +7         +9        +11        +13        +15
         +5        +13        +29        +61       +125       +253       +509
```


## ALGOL W

Translation of

:

ALGOL 60

```mw
begin 
   integer procedure ackermann( integer value m,n ) ;
       if m=0 then n+1
       else if n=0 then ackermann(m-1,1)
                   else ackermann(m-1,ackermann(m,n-1));
   for m := 0 until 3 do begin
      write( ackermann( m, 0 ) );
      for n := 1 until 6 do writeon( ackermann( m, n ) );
   end for_m
end.
```

**Output:**

```
             1               2               3               4               5               6               7
             2               3               4               5               6               7               8
             3               5               7               9              11              13              15
             5              13              29              61             125             253             509
```


## APL

Works with

:

Dyalog APL

```mw
ack←{0=⍺:1+⍵ ⋄ 0=⍵:(⍺-1)∇1 ⋄ (⍺-1)∇⍺∇⍵-1}
```

A version that takes the arguments together in a single array:

Works with

:

Dyalog APL

```mw
ackermann←{
     0=1⊃⍵:1+2⊃⍵
     0=2⊃⍵:∇(¯1+1⊃⍵)1
     ∇(¯1+1⊃⍵),∇(1⊃⍵),¯1+2⊃⍵
 }
```


## AppleScript

```mw
on ackermann(m, n)
    if m is equal to 0 then return n + 1
    if n is equal to 0 then return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))
end ackermann
```


## Argile

Works with

:

Argile

version 1.0.0

```mw
use std

for each (val nat n) from 0 to 6
  for each (val nat m) from 0 to 3
    print "A("m","n") = "(A m n)

.:A <nat m, nat n>:. -> nat
  return (n+1)				if m == 0
  return (A (m - 1) 1)			if n == 0
  A (m - 1) (A m (n - 1))
```


## ArkScript

Works with

:

ArkScript

version 3.x

```mw
(let ackermann (fun (m n) {
  (if (> m 0)
    (if (= 0 n)
      (ackermann (- m 1) 1)
      (ackermann (- m 1) (ackermann m (- n 1))))
    (+ 1 n)) }))

(assert (= 509 (ackermann 3 6)) "(ackermann 3 6) == 509")
```


## ARM Assembly

Works with

:

as

version Raspberry Pi

or android 32 bits with application Termux

```mw
/* ARM assembly Raspberry PI  or android 32 bits */
/*  program ackermann.s   */ 

/* REMARK 1 : this program use routines in a include file 
   see task Include a file language arm assembly 
   for the routine affichageMess conversion10 
   see at end of this program the instruction include */
/* for constantes see task include a file in arm assembly */
/************************************/
/* Constantes                       */
/************************************/
.include "../constantes.inc"
.equ MMAXI,   4
.equ NMAXI,   10

/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:        .asciz "Result for @  @  : @ \n"
szMessError:        .asciz "Overflow !!.\n"
szCarriageReturn:   .asciz "\n"
 
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
main:                           @ entry of program 
    mov r3,#0
    mov r4,#0
1:
    mov r0,r3
    mov r1,r4
    bl ackermann
    mov r5,r0
    mov r0,r3
    ldr r1,iAdrsZoneConv        @ else display odd message
    bl conversion10             @ call decimal conversion
    ldr r0,iAdrsMessResult
    ldr r1,iAdrsZoneConv        @ insert value conversion in message
    bl strInsertAtCharInc
    mov r6,r0
    mov r0,r4
    ldr r1,iAdrsZoneConv        @ else display odd message
    bl conversion10             @ call decimal conversion
    mov r0,r6
    ldr r1,iAdrsZoneConv        @ insert value conversion in message
    bl strInsertAtCharInc
    mov r6,r0
    mov r0,r5
    ldr r1,iAdrsZoneConv        @ else display odd message
    bl conversion10             @ call decimal conversion
    mov r0,r6
    ldr r1,iAdrsZoneConv        @ insert value conversion in message
    bl strInsertAtCharInc
    bl affichageMess
    add r4,#1
    cmp r4,#NMAXI
    blt 1b
    mov r4,#0
    add r3,#1
    cmp r3,#MMAXI
    blt 1b
100:                            @ standard end of the program 
    mov r0, #0                  @ return code
    mov r7, #EXIT               @ request to exit program
    svc #0                      @ perform the system call
 
iAdrszCarriageReturn:     .int szCarriageReturn
iAdrsMessResult:          .int sMessResult
iAdrsZoneConv:            .int sZoneConv
/***************************************************/
/*     fonction ackermann              */
/***************************************************/
// r0 contains a number m
// r1 contains a number n
// r0 return résult
ackermann:
    push {r1-r2,lr}             @ save  registers 
    cmp r0,#0
    beq 5f
    movlt r0,#-1               @ error
    blt 100f
    cmp r1,#0
    movlt r0,#-1               @ error
    blt 100f
    bgt 1f
    sub r0,r0,#1
    mov r1,#1
    bl ackermann
    b 100f
1:
    mov r2,r0
    sub r1,r1,#1
    bl ackermann
    mov r1,r0
    sub r0,r2,#1
    bl ackermann
    b 100f
5:
    adds r0,r1,#1
    bcc 100f
    ldr r0,iAdrszMessError
    bl affichageMess
    bkpt
100:
    pop {r1-r2,lr}             @ restaur registers
    bx lr                      @ return
iAdrszMessError:        .int szMessError
/***************************************************/
/*      ROUTINES INCLUDE                           */
/***************************************************/
.include "../affichage.inc"
```

**Output:**

```
Result for 0            0            : 1
Result for 0            1            : 2
Result for 0            2            : 3
Result for 0            3            : 4
Result for 0            4            : 5
Result for 0            5            : 6
Result for 0            6            : 7
Result for 0            7            : 8
Result for 0            8            : 9
Result for 0            9            : 10
Result for 1            0            : 2
Result for 1            1            : 3
Result for 1            2            : 4
Result for 1            3            : 5
Result for 1            4            : 6
Result for 1            5            : 7
Result for 1            6            : 8
Result for 1            7            : 9
Result for 1            8            : 10
Result for 1            9            : 11
Result for 2            0            : 3
Result for 2            1            : 5
Result for 2            2            : 7
Result for 2            3            : 9
Result for 2            4            : 11
Result for 2            5            : 13
Result for 2            6            : 15
Result for 2            7            : 17
Result for 2            8            : 19
Result for 2            9            : 21
Result for 3            0            : 5
Result for 3            1            : 13
Result for 3            2            : 29
Result for 3            3            : 61
Result for 3            4            : 125
Result for 3            5            : 253
Result for 3            6            : 509
Result for 3            7            : 1021
Result for 3            8            : 2045
Result for 3            9            : 4093
```


## Arturo

```mw
ackermann: function [m,n][
    (m=0)? -> n+1 [
        (n=0)? -> ackermann m-1 1
               -> ackermann m-1 ackermann m n-1
    ]
]

loop 0..3 'a [
    loop 0..4 'b [
        print ["ackermann" a b "=>" ackermann a b]
    ]
]
```

**Output:**

```
ackermann 0 0 => 1 
ackermann 0 1 => 2 
ackermann 0 2 => 3 
ackermann 0 3 => 4 
ackermann 0 4 => 5 
ackermann 1 0 => 2 
ackermann 1 1 => 3 
ackermann 1 2 => 4 
ackermann 1 3 => 5 
ackermann 1 4 => 6 
ackermann 2 0 => 3 
ackermann 2 1 => 5 
ackermann 2 2 => 7 
ackermann 2 3 => 9 
ackermann 2 4 => 11 
ackermann 3 0 => 5 
ackermann 3 1 => 13 
ackermann 3 2 => 29 
ackermann 3 3 => 61 
ackermann 3 4 => 125
```


## ATS

```mw
fun ackermann
  {m,n:nat} .<m,n>.
  (m: int m, n: int n): Nat =
  case+ (m, n) of
  | (0, _) => n+1
  | (_, 0) =>> ackermann (m-1, 1)
  | (_, _) =>> ackermann (m-1, ackermann (m, n-1))
// end of [ackermann]
```


## AutoHotkey

```mw
A(m, n) {
  If (m > 0) && (n = 0)
    Return A(m-1,1)
  Else If (m > 0) && (n > 0)
    Return A(m-1,A(m, n-1))
  Else If (m=0)
    Return n+1
}

; Example:
MsgBox, % "A(1,2) = " A(1,2)
```


## AutoIt

### Classical version

```mw
Func Ackermann($m, $n)
    If ($m = 0) Then
        Return $n+1
    Else
        If ($n = 0) Then
            Return Ackermann($m-1, 1)
        Else
            return Ackermann($m-1, Ackermann($m, $n-1))
        EndIf
    EndIf
EndFunc
```

### Classical + cache implementation

This version works way faster than the classical one: Ackermann(3, 5) runs in 12,7 ms, while the classical version takes 402,2 ms.

```mw
Global $ackermann[2047][2047] ; Set the size to whatever you want
Func Ackermann($m, $n)
	If ($ackermann[$m][$n] <> 0) Then
		Return $ackermann[$m][$n]
	Else
		If ($m = 0) Then
			$return = $n + 1
		Else
			If ($n = 0) Then
				$return = Ackermann($m - 1, 1)
			Else
				$return = Ackermann($m - 1, Ackermann($m, $n - 1))
			EndIf
		EndIf
		$ackermann[$m][$n] = $return
		Return $return
	EndIf
EndFunc   ;==>Ackermann
```


## AWK

```mw
function ackermann(m, n) 
{
  if ( m == 0 ) { 
    return n+1
  }
  if ( n == 0 ) { 
    return ackermann(m-1, 1)
  }
  return ackermann(m-1, ackermann(m, n-1))
}

BEGIN {
  for(n=0; n < 7; n++) {
    for(m=0; m < 4; m++) {
      print "A(" m "," n ") = " ackermann(m,n)
    }
  }
}
```


## Babel

```mw
main: 
        {((0 0) (0 1) (0 2)
        (0 3) (0 4) (1 0)
        (1 1) (1 2) (1 3)
        (1 4) (2 0) (2 1)
        (2 2) (2 3) (3 0)
        (3 1) (3 2) (4 0)) 
    
        { dup
        "A(" << { %d " " . << } ... ") = " <<
    reverse give 
    ack 
    %d cr << } ... }

ack!: 
    { dup zero?
        { <-> dup zero?
            { <-> 
                cp
                1 -
                <- <- 1 - ->
                ack -> 
                ack }
            { <->
                1 - 
                <- 1 -> 
                ack }
        if }
        { zap 1 + }
    if }

zero?!: { 0 = }
```

**Output:**

```
A(0 0 ) = 1
A(0 1 ) = 2
A(0 2 ) = 3
A(0 3 ) = 4
A(0 4 ) = 5
A(1 0 ) = 2
A(1 1 ) = 3
A(1 2 ) = 4
A(1 3 ) = 5
A(1 4 ) = 6
A(2 0 ) = 3
A(2 1 ) = 5
A(2 2 ) = 7
A(2 3 ) = 9
A(3 0 ) = 5
A(3 1 ) = 13
A(3 2 ) = 29
A(4 0 ) = 13
```


## Ballerina

```mw
import ballerina/io;

function ackermann(int m, int n) returns int {
    if m == 0 { return n + 1; }
    if n == 0 { return ackermann(m - 1, 1); }
    return ackermann(m - 1, ackermann(m, n - 1));
}

public function main() {
    int[][] pairs = [ [1, 3], [2, 3], [3, 3], [1, 5], [2, 5], [3, 5] ];
    foreach var p in pairs {
        io:println(`A[${p[0]}, ${p[1]}] = ${ackermann(p[0], p[1])}`);
    }
}
```

**Output:**

```
A[1, 3] = 5
A[2, 3] = 9
A[3, 3] = 61
A[1, 5] = 7
A[2, 5] = 13
A[3, 5] = 253
```


## BASIC

### Applesoft BASIC

Works with

:

Chipmunk Basic

```mw
100 DIM R%(2900),M(2900),N(2900)
110 FOR M = 0 TO 3
120     FOR N = 0 TO 4
130         GOSUB 200"ACKERMANN
140         PRINT "ACK("M","N") = "ACK
150 NEXT N, M
160 END 

200 M(SP) = M
210 N(SP) = N

REM A(M - 1, A(M, N - 1))
220 IF M > 0 AND N > 0 THEN N = N - 1 : R%(SP) = 0 : SP = SP + 1 : GOTO 200

REM A(M - 1, 1)
230 IF M > 0 THEN M = M - 1 : N = 1 : R%(SP) = 1 : SP = SP + 1 : GOTO 200

REM N + 1
240 ACK = N + 1

REM RETURN
250 M = M(SP) : N = N(SP) : IF SP = 0 THEN RETURN
260 FOR SP = SP - 1 TO 0 STEP -1 : IF R%(SP) THEN M = M(SP) : N = N(SP) : NEXT SP : SP = 0 : RETURN
270 M = M - 1 : N = ACK : R%(SP) = 1 : SP = SP + 1 : GOTO 200
```

### BASIC256

```mw
dim stack(5000, 3)	# BASIC-256 lacks functions (as of ver. 0.9.6.66)
stack[0,0] = 3		# M
stack[0,1] = 7		# N
lev = 0 

gosub ackermann
print "A("+stack[0,0]+","+stack[0,1]+") = "+stack[0,2]
end

ackermann:
	if stack[lev,0]=0 then
		stack[lev,2] = stack[lev,1]+1
		return
	end if
	if stack[lev,1]=0 then 
		lev = lev+1
		stack[lev,0] = stack[lev-1,0]-1
		stack[lev,1] = 1
		gosub ackermann
		stack[lev-1,2] = stack[lev,2]
		lev = lev-1
		return
	end if
	lev = lev+1
	stack[lev,0] = stack[lev-1,0]
	stack[lev,1] = stack[lev-1,1]-1
	gosub ackermann
	stack[lev,0] = stack[lev-1,0]-1
	stack[lev,1] = stack[lev,2]
	gosub ackermann
	stack[lev-1,2] = stack[lev,2]
	lev = lev-1
	return
```

**Output:**

```
 A(3,7) = 1021
```

```mw
# BASIC256 since 0.9.9.1 supports functions
for m = 0 to 3
   for n = 0 to 4
      print m + " " + n + " " + ackermann(m,n)
   next n
next m
end

function ackermann(m,n)
   if m = 0 then
      ackermann = n+1
   else
      if n = 0 then
         ackermann = ackermann(m-1,1)
      else
         ackermann = ackermann(m-1,ackermann(m,n-1))
      endif
   end if
end function
```

**Output:**

```
0 0 1
0 1 2
0 2 3
0 3 4
0 4 5
1 0 2
1 1 3
1 2 4
1 3 5
1 4 6
2 0 3
2 1 5
2 2 7
2 3 9
2 4 11
3 0 5
3 1 13
3 2 29
3 3 61
3 4 125
```

### BBC BASIC

```mw
      PRINT FNackermann(3, 7)
      END
      
      DEF FNackermann(M%, N%)
      IF M% = 0 THEN = N% + 1
      IF N% = 0 THEN = FNackermann(M% - 1, 1)
      = FNackermann(M% - 1, FNackermann(M%, N%-1))
```

### Chipmunk Basic

Works with

:

Chipmunk Basic

version 3.6.4

```mw
100 for m = 0 to 4
110   print using "###";m;
120   for n = 0 to 6
130     if m = 4 and n = 1 then goto 160
140     print using "######";ack(m,n);
150   next n
160   print
170 next m
180 end
190 sub ack(m,n)
200   if m = 0 then ack = n+1
210   if m > 0 and n = 0 then ack = ack(m-1,1)
220   if m > 0 and n > 0 then ack = ack(m-1,ack(m,n-1))
230 end sub
```

### True BASIC

```mw
FUNCTION ack(m, n)
    IF m = 0 THEN LET ack = n+1
    IF m > 0 AND n = 0 THEN LET ack = ack(m-1, 1)
    IF m > 0 AND n > 0 THEN LET ack = ack(m-1, ack(m, n-1))
END FUNCTION

FOR m = 0 TO 4
    PRINT USING "###": m;
    FOR n = 0 TO 8
        ! A(4, 1) OR higher will RUN OUT of stack memory (default 1M)
        ! change n = 1 TO n = 2 TO calculate A(4, 2), increase stack!
        IF m = 4 AND n = 1 THEN EXIT FOR
        PRINT USING "######": ack(m, n);
    NEXT n
    PRINT
NEXT m

END
```

### QuickBasic

Works with

:

QuickBasic

version 4.5

BASIC runs out of stack space very quickly. The call ack(3, 4) gives a stack error.

```mw
DECLARE FUNCTION ack! (m!, n!)

FUNCTION ack (m!, n!)
       IF m = 0 THEN ack = n + 1

       IF m > 0 AND n = 0 THEN
               ack = ack(m - 1, 1)
       END IF
       IF m > 0 AND n > 0 THEN
               ack = ack(m - 1, ack(m, n - 1))
       END IF
END FUNCTION
```


## Batch File

Had trouble with this, so called in the gurus at StackOverflow. Thanks to Patrick Cuff for pointing out where I was going wrong.

```mw
::Ackermann.cmd
@echo off
set depth=0
:ack
if %1==0 goto m0
if %2==0 goto n0

:else
set /a n=%2-1
set /a depth+=1
call :ack %1 %n%
set t=%errorlevel%
set /a depth-=1
set /a m=%1-1
set /a depth+=1
call :ack %m% %t%
set t=%errorlevel%
set /a depth-=1
if %depth%==0 ( exit %t% ) else ( exit /b %t% )

:m0
set/a n=%2+1
if %depth%==0 ( exit %n% ) else ( exit /b %n% )

:n0
set /a m=%1-1
set /a depth+=1
call :ack %m% 1
set t=%errorlevel%
set /a depth-=1
if %depth%==0 ( exit %t% ) else ( exit /b %t% )
```

Because of the `exit` statements, running this bare closes one's shell, so this test routine handles the calling of Ackermann.cmd

```mw
::Ack.cmd
@echo off
cmd/c ackermann.cmd %1 %2
echo Ackermann(%1, %2)=%errorlevel%
```

A few test runs:

```
D:\Documents and Settings\Bruce>ack 0 4
Ackermann(0, 4)=5

D:\Documents and Settings\Bruce>ack 1 4
Ackermann(1, 4)=6

D:\Documents and Settings\Bruce>ack 2 4
Ackermann(2, 4)=11

D:\Documents and Settings\Bruce>ack 3 4
Ackermann(3, 4)=125
```


## bc

Requires a bc that supports long names and the print statement.

Works with

:

OpenBSD bc

Works with

:

GNU bc

```mw
define ack(m, n) {
   if ( m == 0 ) return (n+1);
   if ( n == 0 ) return (ack(m-1, 1));
   return (ack(m-1, ack(m, n-1)));
}

for (n=0; n<7; n++) {
  for (m=0; m<4; m++) {
     print "A(", m, ",", n, ") = ", ack(m,n), "\n"; 
  }
}
quit
```


## BCPL

```mw
GET "libhdr"

LET ack(m, n) = m=0 -> n+1,
                n=0 -> ack(m-1, 1),
                ack(m-1, ack(m, n-1))

LET start() = VALOF
{ FOR i = 0 TO 6 FOR m = 0 TO 3 DO
    writef("ack(%n, %n) = %n*n", m, n, ack(m,n))
  RESULTIS 0
}
```


## beeswax

Iterative slow version:

```mw
                         >M?f@h@gMf@h3yzp            if m>0 and n>0 => replace m,n with m-1,m,n-1
                    >@h@g'b?1f@h@gM?f@hzp            if m>0 and n=0 => replace m,n with m-1,1
_ii>Ag~1?~Lpz1~2h@g'd?g?Pfzp                         if m=0         => replace m,n with n+1
           >I;
     b                     <            <
```

A functional and recursive realization of the version above. Functions are realized by direct calls of functions via jumps (instruction `J`) to the entry points of two distinct functions:

1st function `_ii` (input function) with entry point at (row,col) = (4,1)

2nd function `Ag~1....` (Ackermann function) with entry point at (row,col) = (1,1)

Each block of `1FJ` or `1fFJ` in the code is a call of the Ackermann function itself.

```mw
Ag~1?Lp1~2@g'p?g?Pf1FJ                               Ackermann function.  if m=0 => run Ackermann function (m, n+1)
      xI;    x@g'p??@Mf1fFJ                                               if m>0 and n=0 => run Ackermann (m-1,1)
                 xM@~gM??f~f@f1FJ                                         if m>0 and n>0 => run Ackermann(m,Ackermann(m-1,n-1))
_ii1FJ                                               input function. Input m,n, then execute Ackermann(m,n)
```

Highly optimized and fast version, returns A(4,1)/A(5,0) almost instantaneously:

```mw
                             >Mf@Ph?@g@2h@Mf@Php     if m>4 and n>0 => replace m,n with m-1,m,n-1  
                 >~4~L#1~2hg'd?1f@hgM?f2h      p     if m>4 and n=0 => replace m,n with m-1,1
                #            q      <                                                   /n+3 times  \
                #X~4K#?2Fg?PPP>@B@M"pb               if m=4         => replace m,n with 2^(2^(....)))-3
                 # >~3K#?g?PPP~2BMMp>@MMMp           if m=3         => replace m,n with 2^(n+3)-3
_ii>Ag~1?~Lpz1~2h@gX'#?g?P      p  M                 if m=0         => replace m,n with n+1
    z      I       ~>~1K#?g?PP  p                    if m=1         => replace m,n with n+2
     f     ;       >2K#?g?~2.PPPp                    if m=2         => replace m,n with 2n+3
   z  b                         <  <     <
   d                                           <
```

Higher values than A(4,1)/(5,0) lead to UInt64 wraparound, support for numbers bigger than 2^64-1 is not implemented in these solutions.


## Befunge

### Befunge-93

Translation of

:

ERRE

Since Befunge-93 doesn't have recursive capabilities we need to use an iterative algorithm.

```mw
&>&>vvg0>#0\#-:#1_1v
@v:\<vp0    0:-1<\+<
^>00p>:#^_$1+\:#^_$.
```

### Befunge-98

Works with

:

CCBI

version 2.1

```mw
r[1&&{0
>v
 j
u>.@ 
1>  \:v
^  v:\_$1+
\^v_$1\1-
u^>1-0fp:1-\0fg101-
```

The program reads two integers (first m, then n) from command line, idles around funge space, then outputs the result of the Ackerman function. Since the latter is calculated truly recursively, the execution time becomes unwieldy for most m>3.


## Binary Lambda Calculus

The Ackermann function on Church numerals (arbitrary precision), as shown in https://github.com/tromp/AIT/blob/master/fast_growing_and_conjectures/ackermann.lam is the 63 bit BLC program

```
010000010110000001010111110101100010110000000011100101111011010
```
