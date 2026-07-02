---
title: "Sieve of Eratosthenes (part 1/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/21
---

# Sieve of Eratosthenes

This task has been clarified. Its programming examples are in need of review to ensure that they still fit the requirements of the task.

The Sieve of Eratosthenes is a simple algorithm that finds the prime numbers up to a given integer.

**Task**

Implement the   Sieve of Eratosthenes   algorithm, with the only allowed optimization that the outer loop can stop at the square root of the limit, and the inner loop may start at the square of the prime just found.

That means especially that you shouldn't optimize by using pre-computed *wheels*, i.e. don't assume you need only to cross out odd numbers (wheel based on 2), numbers equal to 1 or 5 modulo 6 (wheel based on 2 and 3), or similar wheels based on low primes.

If there's an easy way to add such a wheel based optimization, implement it as an alternative version.

**Note**

- It is important that the sieve algorithm be the actual algorithm used to find prime numbers for the task.

**Related tasks**

- Emirp primes
- count in factors
- prime decomposition
- factors of an integer
- extensible prime generator
- primality by trial division
- factors of a Mersenne number
- trial factoring of a Mersenne number
- partition an integer X into N primes
- sequence of primes by Trial Division


## 11l

Translation of

:

Python

```mw
F primes_upto(limit)
   V is_prime = [0B]*2 [+] [1B]*(limit - 1)
   L(n) 0 .< Int(limit ^ 0.5 + 1.5)
      I is_prime[n]
         L(i) (n*n..limit).step(n)
            is_prime[i] = 0B
   R enumerate(is_prime).filter((i, prime) -> prime).map((i, prime) -> i)

print(primes_upto(100))
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## 360 Assembly

For maximum compatibility, this program uses only the basic instruction set.

```mw
*        Sieve of Eratosthenes 
ERATOST  CSECT  
         USING  ERATOST,R12
SAVEAREA B      STM-SAVEAREA(R15)
         DC     17F'0'
         DC     CL8'ERATOST'
STM      STM    R14,R12,12(R13) save calling context
         ST     R13,4(R15)      
         ST     R15,8(R13)
         LR     R12,R15         set addessability
*        ----   CODE
         LA     R4,1            I=1  
         LA     R6,1            increment
         L      R7,N            limit
LOOPI    BXH    R4,R6,ENDLOOPI  do I=2 to N
         LR     R1,R4           R1=I
         BCTR   R1,0             
         LA     R14,CRIBLE(R1)
         CLI    0(R14),X'01'
         BNE    ENDIF           if not CRIBLE(I)
         LR     R5,R4           J=I
         LR     R8,R4
         LR     R9,R7
LOOPJ    BXH    R5,R8,ENDLOOPJ  do J=I*2 to N by I
         LR     R1,R5           R1=J
         BCTR   R1,0
         LA     R14,CRIBLE(R1)
         MVI    0(R14),X'00'    CRIBLE(J)='0'B
         B      LOOPJ
ENDLOOPJ EQU    *
ENDIF    EQU    *
         B      LOOPI
ENDLOOPI EQU    *
         LA     R4,1            I=1  
         LA     R6,1
         L      R7,N
LOOP     BXH    R4,R6,ENDLOOP   do I=1 to N
         LR     R1,R4           R1=I
         BCTR   R1,0
         LA     R14,CRIBLE(R1)
         CLI    0(R14),X'01'
         BNE    NOTPRIME        if not CRIBLE(I) 
         CVD    R4,P            P=I
         UNPK   Z,P             Z=P
         MVC    C,Z             C=Z
         OI     C+L'C-1,X'F0'   zap sign
         MVC    WTOBUF(8),C+8
         WTO    MF=(E,WTOMSG)      
NOTPRIME EQU    *
         B      LOOP
ENDLOOP  EQU    *
RETURN   EQU    *
         LM     R14,R12,12(R13) restore context
         XR     R15,R15         set return code to 0
         BR     R14             return to caller
*        ----   DATA
I        DS     F
J        DS     F
         DS     0F
P        DS     PL8             packed
Z        DS     ZL16            zoned
C        DS     CL16            character 
WTOMSG   DS     0F
         DC     H'80'           length of WTO buffer
         DC     H'0'            must be binary zeroes
WTOBUF   DC     80C' '
         LTORG  
N        DC     F'100000'
CRIBLE   DC     100000X'01'
         YREGS  
         END    ERATOST
```

**Output:**

```
00000002
00000003
00000005
00000007
00000011
00000013
00000017
00000019
00000023
00000029
00000031
00000037
00000041
00000043
00000047
00000053
00000059
00000061
00000067
...
00099767
00099787
00099793
00099809
00099817
00099823
00099829
00099833
00099839
00099859
00099871
00099877
00099881
00099901
00099907
00099923
00099929
00099961
00099971
00099989
00099991
```


## 6502 Assembly

If this subroutine is called with the value of *n* in the accumulator, it will store an array of the primes less than *n* beginning at address 1000 hex and return the number of primes it has found in the accumulator.

```mw
ERATOS: STA  $D0      ; value of n
        LDA  #$00
        LDX  #$00
SETUP:  STA  $1000,X  ; populate array
        ADC  #$01
        INX
        CPX  $D0
        BPL  SET
        JMP  SETUP
SET:    LDX  #$02
SIEVE:  LDA  $1000,X  ; find non-zero
        INX
        CPX  $D0
        BPL  SIEVED
        CMP  #$00
        BEQ  SIEVE
        STA  $D1      ; current prime
MARK:   CLC
        ADC  $D1
        TAY
        LDA  #$00
        STA  $1000,Y
        TYA
        CMP  $D0
        BPL  SIEVE
        JMP  MARK
SIEVED: LDX  #$01
        LDY  #$00
COPY:   INX
        CPX  $D0
        BPL  COPIED
        LDA  $1000,X
        CMP  #$00
        BEQ  COPY
        STA  $2000,Y
        INY
        JMP  COPY
COPIED: TYA           ; how many found
        RTS
```


## 68000 Assembly

**Algorithm somewhat optimized:** array omits 1, 2, all higher odd numbers. Optimized for storage: uses bit array for prime/composite flags.

Works with

: [

EASy68K v5.13.00

]

Some of the macro code is derived from the examples included with EASy68K. See 68000 "100 Doors" listing for additional information.

```mw
*-----------------------------------------------------------
* Title      : BitSieve
* Written by : G. A. Tippery
* Date       : 2014-Feb-24, 2013-Dec-22
* Description: Prime number sieve
*-----------------------------------------------------------
      ORG    $1000

** ---- Generic macros ----   **
PUSH  MACRO
   MOVE.L   \1,-(SP)
   ENDM

POP   MACRO
   MOVE.L   (SP)+,\1
   ENDM

DROP  MACRO
   ADDQ  #4,SP
   ENDM
   
PUTS  MACRO
   ** Print a null-terminated string w/o CRLF **
   ** Usage: PUTS stringaddress
   ** Returns with D0, A1 modified
   MOVEQ #14,D0   ; task number 14 (display null string)
   LEA   \1,A1 ; address of string
   TRAP  #15   ; display it
   ENDM
   
GETN  MACRO
   MOVEQ #4,D0 ; Read a number from the keyboard into D1.L. 
   TRAP  #15
   ENDM

** ---- Application-specific macros ----  **

val   MACRO    ; Used by bit sieve. Converts bit address to the number it represents.
   ADD.L \1,\1 ; double it because odd numbers are omitted
   ADDQ  #3,\1 ; add offset because initial primes (1, 2) are omitted
   ENDM

* ** ================================================================================ **
* ** Integer square root routine, bisection method **
* ** IN: D0, should be 0<D0<$10000 (65536) -- higher values MAY work, no guarantee
* ** OUT: D1
*
SquareRoot:
*
   MOVEM.L  D2-D4,-(SP) ; save registers needed for local variables
*  DO == n
*  D1 == a
*  D2 == b
*  D3 == guess
*  D4 == temp
*
*     a = 1;
*     b = n;
   MOVEQ #1,D1
   MOVE.L   D0,D2
*     do {
   REPEAT
*     guess = (a+b)/2;
   MOVE.L   D1,D3
   ADD.L D2,D3
   LSR.L #1,D3
*     if (guess*guess > n) {  // inverse function of sqrt is square
   MOVE.L   D3,D4
   MULU  D4,D4    ; guess^2
   CMP.L D0,D4
   BLS   .else
*     b = guess;
   MOVE.L   D3,D2
   BRA   .endif
*     } else {
.else:
*     a = guess;
   MOVE.L   D3,D1
*     } //if
.endif:
*     } while ((b-a) > 1); ; Same as until (b-a)<=1 or until (a-b)>=1
   MOVE.L   D2,D4
   SUB.L D1,D4 ; b-a
   UNTIL.L    D4 <LE> #1 DO.S
*     return (a)  ; Result is in D1
*     } //LongSqrt()
   MOVEM.L  (SP)+,D2-D4 ; restore saved registers
   RTS
*
* ** ================================================================================ **

** ======================================================================= **
*
**  Prime-number Sieve of Eratosthenes routine using a big bit field for flags  **
*  Enter with D0 = size of sieve (bit array)
*  Prints found primes 10 per line
*  Returns # prime found in D6
*
*   Register usage:
*
*  D0 == n
*  D1 == prime
*  D2 == sqroot
*  D3 == PIndex
*  D4 == CIndex
*  D5 == MaxIndex
*  D6 == PCount
*
*  A0 == PMtx[0]
*
*   On return, all registers above except D0 are modified. Could add MOVEMs to save and restore D2-D6/A0.
*

** ------------------------   **

GetBit:     ** sub-part of Sieve subroutine **
      ** Entry: bit # is on TOS
      ** Exit: A6 holds the byte number, D7 holds the bit number within the byte
      ** Note: Input param is still on TOS after return. Could have passed via a register, but
                **  wanted to practice with stack. :)
*     
   MOVE.L   (4,SP),D7   ; get value from (pre-call) TOS
   ASR.L #3,D7 ; /8
   MOVEA D7,A6 ; byte #
   MOVE.L   (4,SP),D7   ; get value from (pre-call) TOS
   AND.L #$7,D7   ; bit #
   RTS

** ------------------------   **

Sieve:
   MOVE  D0,D5
   SUBQ  #1,D5
   JSR   SquareRoot  ; sqrt D0 => D1
   MOVE.L   D1,D2
   LEA   PArray,A0
   CLR.L D3
*
PrimeLoop:
   MOVE.L   D3,D1
   val   D1
   MOVE.L   D3,D4
   ADD.L D1,D4
*
CxLoop:     ; Goes through array marking multiples of d1 as composite numbers
   CMP.L D5,D4
   BHI   ExitCx
   PUSH  D4 ; set D7 as bit # and A6 as byte pointer for D4'th bit of array
   JSR GetBit
   DROP
   BSET  D7,0(A0,A6.L)  ; set bit to mark as composite number
   ADD.L D1,D4 ; next number to mark
   BRA   CxLoop
ExitCx:
   CLR.L D1 ; Clear new-prime-found flag
   ADDQ  #1,D3 ; Start just past last prime found 
PxLoop:     ; Searches for next unmarked (not composite) number
   CMP.L D2,D3 ; no point searching past where first unmarked multiple would be past end of array
   BHI   ExitPx   ; if past end of array
   TST.L D1
   BNE   ExitPx   ; if flag set, new prime found
   PUSH D3     ; check D3'th bit flag
   JSR   GetBit   ; sets D7 as bit # and A6 as byte pointer
   DROP     ; drop TOS
   BTST  D7,0(A0,A6.L)  ; read bit flag
   BNE   IsSet ; If already tagged as composite
   MOVEQ #-1,D1   ; Set flag that we've found a new prime
IsSet:
   ADDQ  #1,D3 ; next PIndex
   BRA   PxLoop
ExitPx:
   SUBQ  #1,D3 ; back up PIndex
   TST.L D1 ; Did we find a new prime #?
   BNE   PrimeLoop   ; If another prime # found, go process it
*
      ; fall through to print routine

** ------------------------   **

* Print primes found
*
*  D4 == Column count
*
*  Print header and assumed primes (#1, #2) 
      PUTS  Header   ; Print string @ Header, no CR/LF
   MOVEQ #2,D6 ; Start counter at 2 because #1 and #2 are assumed primes
   MOVEQ #2,D4
*
   MOVEQ #0,D3
PrintLoop:
   CMP.L D5,D3
   BHS   ExitPL
   PUSH  D3
   JSR   GetBit   ; sets D7 as bit # and A6 as byte pointer
   DROP     ; drop TOS
   BTST  D7,0(A0,A6.L)
   BNE      NotPrime
*     printf(" %6d", val(PIndex)
   MOVE.L   D3,D1
   val   D1
   AND.L #$0000FFFF,D1
   MOVEQ #6,D2
   MOVEQ #20,D0   ; display signed RJ
   TRAP  #15
   ADDQ  #1,D4
   ADDQ  #1,D6
*  *** Display formatting ***
*     if((PCount % 10) == 0) printf("\n");
   CMP   #10,D4
   BLO   NoLF
   PUTS  CRLF
   MOVEQ #0,D4
NoLF:
NotPrime:
   ADDQ  #1,D3
   BRA   PrintLoop
ExitPL:
   RTS

** ======================================================================= **

N  EQU   5000  ; *** Size of boolean (bit) array ***
SizeInBytes EQU   (N+7)/8
*
START:                     ; first instruction of program
   MOVE.L   #N,D0 ; # to test
   JSR   Sieve
*     printf("\n %d prime numbers found.\n", D6); ***
   PUTS  Summary1,A1
   MOVE  #3,D0 ; Display signed number in D1.L in decimal in smallest field.
   MOVE.W   D6,D1
   TRAP  #15
   PUTS  Summary2,A1

   SIMHALT              ; halt simulator

** ======================================================================= **

* Variables and constants here

   ORG   $2000
CR EQU   13
LF EQU   10
CRLF  DC.B  CR,LF,$00

PArray:  DCB.B SizeInBytes,0

Header:  DC.B  CR,LF,LF,' Primes',CR,LF,' ======',CR,LF
      DC.B  '     1     2',$00

Summary1:   DC.B  CR,LF,' ',$00
Summary2:   DC.B  ' prime numbers found.',CR,LF,$00

    END    START           ; last line of source
```


## 8080 Assembly

This does not attempt either of the allowed optimizations. I/O and program entry/exit assume the CP/M operating system.

```mw
bdos	equ	5h	        ; location of jump to BDOS entry point
wboot   equ     0       ; BDOS warm boot function
conout  equ     2       ; write character to console
prtstr  equ     9       ; write $-terminated string to console
cr      equ     13      ; carriage return
lf      equ     10      ; line feed
limit	equ	    100
	;------------------------------------------------------
	; main code
	;------------------------------------------------------
	org	100h	; program load point under CP/M
	lxi	sp,stack ; set our own stack
	;
	; initialize flag array 
	;
	lxi	b,limit	
	lxi	h,table+1
init:	mov	a,b	; have we reached the last element?
	ora	c	; (i.e., does BC = 0?)
	jz	sieve
	mvi	m,1	; 1 signifies prime
	inx	h	; point to next element
	dcx	b	; decrease count
	jmp	init
	;
	; sieve by striking out multiples of each prime
	; encountered
	;
sieve:	lxi     d,2	; 2 is the first prime
oloop:  mov     h,d	; HL = DE
        mov     l,e
iloop: 	dad     d	; HL = HL + DE
        push    h	; remember inner loop index
        lxi     b,table
        dad     b
	    mvi	    m,0
        pop     h
        push    h
        lxi     b,-limit
        dad     b	; CY if HL >= limit
        pop     h
        jnc     iloop
oloop2:	inx     d	; find next number not yet struck
	    push	h
	    lxi	    h,table
	    dad	    d
	    cpi	    m,0
	    pop	    h
	    jz	    oloop2  ; already struck out
        mov     h,d	; ready for another go if DE < limit
        mov     l,e	; 
        dad     b
        jnc     oloop	; or fall through when finished
	;
	; show primes and total found
	;
show:	lxi	b,limit
	lxi	d,2
	lxi	h,table+2  ; first prime is 2
show2:	mov	a,b	; have we reached the end?
	ora	c	; if so (BC=0), we're done
	jz	show4
	mov	a,m	; fetch byte pointed to by HL
	cpi	1	; is it prime?
	jnz	show3	; no, continue
	push	h	; otherwise, save position
	lhld	count	; increment count
	inx	h
	shld	count
	pop	h
	xchg
	call	putdec
	xchg
	mvi	a,' '	; separate with a space
	call	putchr
show3:	dcx	b
	inx	d
	inx	h
	jmp	show2
show4:	call	crlf	; show how many were found
	lhld	count
	call	putdec
	lxi	d,result
	call	message
	;
	; all finished. clean up and exit.
	;
	jmp	wboot
	;-------------------------------------------------------
	; console output of $-terminated string pointed to by DE
	;-------------------------------------------------------
message:
	push	h
	push	d
	push	b
	mvi	    c,prtstr
	call	bdos
	pop	b
	pop	d
	pop	h
	ret
	;------------------------------------------------------
	; output CRLF to console
	;------------------------------------------------------
crlf:	push 	h
	push 	d
	push	b
	mvi	e,cr
	mvi	c,conout
	call	bdos
	mvi	e,lf
	mvi	c,conout
	call	bdos
	pop	b
	pop	d
	pop	h
	ret
	;------------------------------------------------------
	; console output of char in A register
	;------------------------------------------------------
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
	;------------------------------------------------------
	; Output unsigned decimal number in HL to console
	;------------------------------------------------------
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
	cnz	putdec	; recursive call
	mov	a,e
	adi	'0'
	call	putchr
	pop	h
	pop	d
	pop	b
	ret
	;------------------------------------------------------
	;  message and data area
	;------------------------------------------------------
result:	db	' primes were found.',cr,lf,'$'
count:	dw	0
table:	ds	limit+1
stack	equ	$+256	; 128-level stack
	;
	end
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
25 primes were found
```


## 8086 Assembly

```mw
MAXPRM: equ   5000     ; Change this value for more primes
   cpu   8086
   bits  16
   org   100h
section  .text
erato:   mov   cx,MAXPRM   ; Initialize array (set all items to prime)
   mov   bp,cx    ; Keep a copy in BP
   mov   di,sieve
   mov   al,1
   rep   stosb
   ;;;   Sieve
   mov   bx,sieve ; Set base register to array
   inc   cx    ; CX=1 (CH=0, CL=1); CX was 0 before
   mov   si,cx    ; Start at number 2 (1+1)
.next:   inc   si    ; Next number 
   cmp   cl,[bx+si]  ; Is this number marked as prime?
   jne   .next    ; If not, try next number
   mov   ax,si    ; Otherwise, calculate square,
   mul   si
   mov   di,ax    ; and put it in DI
   cmp   di,bp    ; Check array bounds
   ja output      ; We're done when SI*SI>MAXPRM
.mark:   mov   [bx+di],ch  ; Mark byte as composite
   add   di,si    ; Next composite
   cmp   di,bp    ; While maximum not reached
   jbe   .mark
   jmp   .next
   ;;;   Output
output:  mov   si,2     ; Start at 2
.test:   dec   byte [bx+si]   ; Prime?
   jnz   .next    ; If not, try next number
   mov   ax,si    ; Otherwise, print number
   call  prax
.next:   inc   si
   cmp   si,MAXPRM
   jbe   .test
   ret
   ;;;   Write number in AX to standard output (using MS-DOS)
prax: push  bx    ; Save BX
   mov   bx,numbuf
   mov   bp,10    ; Divisor
.loop:   xor   dx,dx    ; Divide AX by 10, modulus in DX
   div   bp
   add   dl,'0'      ; ASCII digit
   dec   bx
   mov   [bx],dl     ; Store ASCII digit
   test  ax,ax    ; More digits?
   jnz   .loop
   mov   dx,bx    ; Print number
   mov   ah,9     ; 9 = MS-DOS syscall to print string
   int   21h
   pop   bx    ; Restore BX
   ret
section  .data
   db '*****'     ; Room for number
numbuf:  db 13,10,'$'
section  .bss 
sieve:   resb  MAXPRM
```

**Output:**

```
2
3
5
7
11
...
4969
4973
4987
4993
4999
```


## 8th

```mw
with: n

\ create a new buffer which will function as a bit vector
: bit-vec SED: n -- b
    dup 3 shr swap 7 band if 1+ then b:new b:clear ;

\ given a buffer, sieving prime, and limit, cross off multiples
\ of the sieving prime.
: +composites SED: b n n -- b
    >r dup sqr rot \ want: -- n index b
    repeat
        over 1- true b:bit!
        >r over + r>
    over r@ > until!
    rdrop nip nip ;

\ SoE algorithm proper
: make-sieve SED: n -- b
    dup>r bit-vec 2
    repeat
        tuck 1- b:bit@ not
        if
            over r@ +composites
        then swap 1+
    dup sqr r@ < while!
    rdrop drop ;

\ traverse the final buffer, creating an array of primes
: sieve>a SED: b n -- a
    >r a:new swap
    ( 1- b:bit@ not if >r I a:push r> then ) 2 r> loop drop ;

;with

: sieve SED: n -- a
    dup make-sieve swap sieve>a ;
```

**Output:**

```
ok> 100 sieve .
 [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
ok> 1_000_000 sieve a:len . \ count primes up to 1,000,000
78498
ok> -1 a:@ . \ largest prime < 1,000,000
999983
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program cribleEras64.s   */

/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeConstantesARM64.inc"

.equ MAXI,      100

/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:        .asciz "Prime  : @ \n"
szCarriageReturn:   .asciz "\n"

/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
sZoneConv:                  .skip 24
TablePrime:                 .skip   8 * MAXI 
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                               // entry of program 
    ldr x4,qAdrTablePrime           // address prime table
    mov x0,#2                       // prime 2
    bl displayPrime
    mov x1,#2
    mov x2,#1
1:                                  // loop for multiple of 2
    str x2,[x4,x1,lsl #3]           // mark  multiple of 2
    add x1,x1,#2
    cmp x1,#MAXI                    // end ?
    ble 1b                          // no loop
    mov x1,#3                       // begin indice
    mov x3,#1
2:
    ldr x2,[x4,x1,lsl #3]           // load table élément
    cmp x2,#1                       // is prime ?
    beq 4f
    mov x0,x1                       // yes -> display
    bl displayPrime
    mov x2,x1
3:                                  // and loop to mark multiples of this prime
    str x3,[x4,x2,lsl #3]
    add x2,x2,x1                    // add the prime
    cmp x2,#MAXI                    // end ?
    ble 3b                          // no -> loop
4:
    add x1,x1,2                     // other prime in table
    cmp x1,MAXI                     // end table ?
    ble 2b                          // no -> loop

100:                                // standard end of the program 
    mov x0,0                        // return code
    mov x8,EXIT                     // request to exit program
    svc 0                           // perform the system call
qAdrszCarriageReturn:    .quad szCarriageReturn
qAdrsMessResult:         .quad sMessResult
qAdrTablePrime:          .quad TablePrime

/******************************************************************/
/*      Display prime table elements                                */ 
/******************************************************************/
/* x0 contains the prime */
displayPrime:
    stp x1,lr,[sp,-16]!             // save  registers
    ldr x1,qAdrsZoneConv
    bl conversion10                 // call décimal conversion
    ldr x0,qAdrsMessResult
    ldr x1,qAdrsZoneConv            // insert conversion in message
    bl strInsertAtCharInc
    bl affichageMess                // display message
100:
    ldp x1,lr,[sp],16               // restaur  2 registers
    ret                             // return to address lr x30
qAdrsZoneConv:                   .quad sZoneConv  

/********************************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```

```
Prime  : 2
Prime  : 3
Prime  : 5
Prime  : 7
Prime  : 11
Prime  : 13
Prime  : 17
Prime  : 19
Prime  : 23
Prime  : 29
Prime  : 31
Prime  : 37
Prime  : 41
Prime  : 43
Prime  : 47
Prime  : 53
Prime  : 59
Prime  : 61
Prime  : 67
Prime  : 71
Prime  : 73
Prime  : 79
Prime  : 83
Prime  : 89
Prime  : 97
```


## ABAP

```mw
PARAMETERS: p_limit TYPE i OBLIGATORY DEFAULT 100.

AT SELECTION-SCREEN ON p_limit.
  IF p_limit LE 1.
    MESSAGE 'Limit must be higher then 1.' TYPE 'E'.
  ENDIF.

START-OF-SELECTION.
  FIELD-SYMBOLS: <fs_prime> TYPE flag.
  DATA: gt_prime TYPE TABLE OF flag,
        gv_prime TYPE flag,
        gv_i     TYPE i,
        gv_j     TYPE i.

  DO p_limit TIMES.
    IF sy-index > 1.
      gv_prime = abap_true.
    ELSE.
      gv_prime = abap_false.
    ENDIF.

    APPEND gv_prime TO gt_prime.
  ENDDO.

  gv_i = 2.
  WHILE ( gv_i <= trunc( sqrt( p_limit ) ) ).
    IF ( gt_prime[ gv_i ] EQ abap_true ).
      gv_j =  gv_i ** 2.
      WHILE ( gv_j <= p_limit ).
        gt_prime[ gv_j ] = abap_false.
        gv_j = ( gv_i ** 2 ) + ( sy-index * gv_i ).
      ENDWHILE.
    ENDIF.
    gv_i = gv_i + 1.
  ENDWHILE.

  LOOP AT gt_prime INTO gv_prime.
    IF gv_prime = abap_true.
      WRITE: / sy-tabix.
    ENDIF.
  ENDLOOP.
```


## ABC

```mw
HOW TO SIEVE UP TO n:
    SHARE sieve
    PUT {} IN sieve
    FOR cand IN {2..n}: PUT 1 IN sieve[cand]
    FOR cand IN {2..floor root n}:
        IF sieve[cand] = 1:
            PUT cand*cand IN comp
            WHILE comp <= n:
                PUT 0 IN sieve[comp]
                PUT comp+cand IN comp

HOW TO REPORT prime n:
    SHARE sieve
    IF n<2: FAIL
    REPORT sieve[n] = 1

SIEVE UP TO 100
FOR n IN {1..100}:
    IF prime n: WRITE n
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## ACL2

```mw
(defun nats-to-from (n i)
   (declare (xargs :measure (nfix (- n i))))
   (if (zp (- n i))
       nil
       (cons i (nats-to-from n (+ i 1)))))

(defun remove-multiples-up-to-r (factor limit xs i)
   (declare (xargs :measure (nfix (- limit i))))
   (if (or (> i limit)
           (zp (- limit i))
           (zp factor))
       xs
       (remove-multiples-up-to-r
        factor
        limit
        (remove i xs)
        (+ i factor))))

(defun remove-multiples-up-to (factor limit xs)
   (remove-multiples-up-to-r factor limit xs (* factor 2)))

(defun sieve-r (factor limit)
   (declare (xargs :measure (nfix (- limit factor))))
   (if (zp (- limit factor))
       (nats-to-from limit 2)
       (remove-multiples-up-to factor (+ limit 1)
                               (sieve-r (1+ factor) limit))))

(defun sieve (limit)
   (sieve-r 2 limit))
```


## Action!

```mw
DEFINE MAX="1000"

PROC Main()
  BYTE ARRAY t(MAX+1)
  INT i,j,k,first

  FOR i=0 TO MAX
  DO
    t(i)=1
  OD

  t(0)=0
  t(1)=0

  i=2 first=1
  WHILE i<=MAX
  DO
    IF t(i)=1 THEN
      IF first=0 THEN
        Print(", ")
      FI
      PrintI(i)
      FOR j=2*i TO MAX STEP i
      DO
        t(j)=0
      OD
      first=0
    FI
    i==+1
  OD
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
```


## ActionScript

Works with ActionScript 3.0 (this is utilizing the actions panel, not a separated class file)

```mw
function eratosthenes(limit:int):Array
{
   var primes:Array = new Array();
   if (limit >= 2) {
      var sqrtlmt:int = int(Math.sqrt(limit) - 2);
      var nums:Array = new Array(); // start with an empty Array...
      for (var i:int = 2; i <= limit; i++) // and
         nums.push(i); // only initialize the Array once...
      for (var j:int = 0; j <= sqrtlmt; j++) {
         var p:int = nums[j]
         if (p)
            for (var t:int = p * p - 2; t < nums.length; t += p)
               nums[t] = 0;
      }
      for (var m:int = 0; m < nums.length; m++) {
         var r:int = nums[m];
         if (r)
            primes.push(r);
      }
   }
   return primes;
}
var e:Array = eratosthenes(1000);
trace(e);
```

Output:

**Output:**

```
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997
```


## Ada

```mw
with Ada.Text_IO, Ada.Command_Line;

procedure Eratos is
 
   Last: Positive := Positive'Value(Ada.Command_Line.Argument(1));
   Prime: array(1 .. Last) of Boolean := (1 => False, others => True);
   Base: Positive := 2;
   Cnt: Positive;
begin
   while Base * Base <= Last loop
      if Prime(Base) then
         Cnt := Base + Base;
         while Cnt <= Last loop
            Prime(Cnt) := False;
            Cnt := Cnt + Base;
         end loop;
      end if;
      Base := Base + 1;
   end loop;
   Ada.Text_IO.Put("Primes less or equal" & Positive'Image(Last) &" are:");
   for Number in Prime'Range loop
      if Prime(Number) then
         Ada.Text_IO.Put(Positive'Image(Number));
      end if;
   end loop;
end Eratos;
```

**Output:**

```
> ./eratos 31
Primes less or equal 31 are : 2 3 5 7 11 13 17 19 23 29 31
```


## Agda

```mw
-- imports
open import Data.Nat as ℕ     using (ℕ; suc; zero; _+_; _∸_)
open import Data.Vec as Vec   using (Vec; _∷_; []; tabulate; foldr)
open import Data.Fin as Fin   using (Fin; suc; zero)
open import Function          using (_∘_; const; id)
open import Data.List as List using (List; _∷_; [])
open import Data.Maybe        using (Maybe; just; nothing)

-- Without square cutoff optimization
module Simple where
  primes : ∀ n → List (Fin n)
  primes zero = []
  primes (suc zero) = []
  primes (suc (suc zero)) = []
  primes (suc (suc (suc m))) = sieve (tabulate (just ∘ suc))
    where
    sieve : ∀ {n} → Vec (Maybe (Fin (2 + m))) n → List (Fin (3 + m))
    sieve [] = []
    sieve (nothing ∷ xs) =         sieve xs
    sieve (just x  ∷ xs) = suc x ∷ sieve (foldr B remove (const []) xs x)
      where
      B = λ n → ∀ {i} → Fin i → Vec (Maybe (Fin (2 + m))) n

      remove : ∀ {n} → Maybe (Fin (2 + m)) → B n → B (suc n)
      remove _ ys zero    = nothing ∷ ys x
      remove y ys (suc z) = y       ∷ ys z

-- With square cutoff optimization
module SquareOpt where
  primes : ∀ n → List (Fin n)
  primes zero = []
  primes (suc zero) = []
  primes (suc (suc zero)) = []
  primes (suc (suc (suc m))) = sieve 1 m (Vec.tabulate (just ∘ Fin.suc ∘ Fin.suc))
    where
    sieve : ∀ {n} → ℕ → ℕ → Vec (Maybe (Fin (3 + m))) n → List (Fin (3 + m))
    sieve _ zero = List.mapMaybe id ∘ Vec.toList
    sieve _ (suc _) [] = []
    sieve i (suc l) (nothing ∷ xs) =     sieve (suc i) (l ∸ i ∸ i) xs
    sieve i (suc l) (just x  ∷ xs) = x ∷ sieve (suc i) (l ∸ i ∸ i) (Vec.foldr B remove (const []) xs i)
      where
      B = λ n → ℕ → Vec (Maybe (Fin (3 + m))) n

      remove : ∀ {i} → Maybe (Fin (3 + m)) → B i → B (suc i)
      remove _ ys zero    = nothing ∷ ys i
      remove y ys (suc j) = y       ∷ ys j
```


## Agena

Tested with Agena 2.9.5 Win32

```mw
# Sieve of Eratosthenes

# generate and return a sequence containing the primes up to sieveSize
sieve := proc( sieveSize :: number ) :: sequence is
    local sieve, result;

    result := seq(); # sequence of primes - initially empty
    create register sieve( sieveSize ); # "vector" to be sieved

    sieve[ 1 ] := false;
    for sPos from 2 to sieveSize do sieve[ sPos ] := true od;

    # sieve the primes
    for sPos from 2 to entier( sqrt( sieveSize ) ) do
        if sieve[ sPos ] then
            for p from sPos * sPos to sieveSize by sPos do
                sieve[ p ] := false
            od
        fi
    od;

    # construct the sequence of primes
    for sPos from 1 to sieveSize do
        if sieve[ sPos ] then insert sPos into result fi
    od

return result
end; # sieve

# test the sieve proc
for i in sieve( 100 ) do write( " ", i ) od; print();
```

**Output:**

```
 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## ALGOL 60

**Based on the 1962 Revised Repport**:

```
comment Sieve of Eratosthenes;
begin
   integer array t[0:1000];
   integer i,j,k;
   for i:=0 step 1 until 1000 do t[i]:=1;
   t[0]:=0; t[1]:=0; i:=0;
   for i:=i while i<1000 do
   begin
       for i:=i while i<1000 and t[i]=0 do i:=i+1;
       if i<1000 then
       begin
           j:=2;
           k:=j*i;
           for k:=k while k<1000 do
           begin
               t[k]:=0;
               j:=j+1;
               k:=j*i
           end;
           i:=i+1
       end
   end;
   for i:=0 step 1 until 999 do
   if t[i]≠0 then print(i,ꞌ is primeꞌ)
end
```

**An 1964 Implementation**:

**Works with:** ALGOL 60 for OS/360

```mw
'BEGIN'
    'INTEGER' 'ARRAY' CANDIDATES(/0..1000/);
    'INTEGER' I,J,K;
    'COMMENT' SET LINE-LENGTH=120,SET LINES-PER-PAGE=62,OPEN;
    SYSACT(1,6,120); SYSACT(1,8,62); SYSACT(1,12,1);
    'FOR' I := 0 'STEP' 1 'UNTIL' 1000 'DO'
    'BEGIN'
        CANDIDATES(/I/) := 1;
    'END';
    CANDIDATES(/0/) := 0;
    CANDIDATES(/1/) := 0;
    I := 0;
    'FOR' I := I 'WHILE' I 'LESS' 1000 'DO'
    'BEGIN'
        'FOR' I := I 'WHILE' I 'LESS' 1000
          'AND' CANDIDATES(/I/) 'EQUAL' 0 'DO'
            I := I+1;
        'IF' I 'LESS' 1000 'THEN'
        'BEGIN'
            J := 2;
            K := J*I;
            'FOR' K := K 'WHILE' K 'LESS' 1000 'DO'
            'BEGIN'
                CANDIDATES(/K/) := 0;
                J := J + 1;
                K := J*I;
            'END';
            I := I+1;
        'END';
        'FOR' I := 0 'STEP' 1 'UNTIL' 999 'DO'
        'IF' CANDIDATES(/I/) 'NOTEQUAL' 0  'THEN'
        'BEGIN'
            OUTINTEGER(1,I);
            OUTSTRING(1,'(' IS PRIME')');
            'COMMENT' NEW LINE;
            SYSACT(1,14,1)
        'END'
    'END'
'END'
```


## ALGOL 68

```mw
BOOL prime = TRUE, non prime = FALSE;
PROC eratosthenes = (INT n)[]BOOL:
(
  [n]BOOL sieve;
  FOR i TO UPB sieve DO sieve[i] := prime OD;
  INT m = ENTIER sqrt(n);
  sieve[1] := non prime;
  FOR i FROM 2 TO m DO
    IF sieve[i] = prime THEN
      FOR j FROM i*i BY i TO n DO
        sieve[j] := non prime
      OD
    FI
  OD;
  sieve
);
 
 print((eratosthenes(80),new line))
```

**Output:**

```
FTTFTFTFFFTFTFFFTFTFFFTFFFFFTFTFFFFFTFFFTFTFFFTFFFFFTFFFFFTFTFFFFFTFFFTFTFFFFFTF
```


## ALGOL W

### Standard, non-optimised sieve

```mw
begin

    % implements the sieve of Eratosthenes                                   %
    %     s(i) is set to true if i is prime, false otherwise                 %
    %     algol W doesn't have a upb operator, so we pass the size of the    %
    %     array in n                                                         %
    procedure sieve( logical array s ( * ); integer value n ) ;
    begin

        % start with everything flagged as prime                             % 
        for i := 1 until n do s( i ) := true;

        % sieve out the non-primes                                           %
        s( 1 ) := false;
        for i := 2 until truncate( sqrt( n ) )
        do begin
            if s( i )
            then begin
                for p := i * i step i until n do s( p ) := false
            end if_s_i
        end for_i ;

    end sieve ;

    % test the sieve procedure                                               %

    integer sieveMax;

    sieveMax := 100;
    begin

        logical array s ( 1 :: sieveMax );

        i_w := 2; % set output field width                                   %
        s_w := 1; % and output separator width                               %

        % find and display the primes                                        %
        sieve( s, sieveMax );
        for i := 1 until sieveMax do if s( i ) then writeon( i );

    end

end.
```

**Output:**

```
 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
```

### Odd numbers only version

Alternative version that only stores odd numbers greater than 1 in the sieve.

```mw
begin
    % implements the sieve of Eratosthenes                                   %
    % only odd numbers appear in the sieve, which starts at 3                %
    % s( i ) is set to true if ( i * 2 ) + 1 is prime                        %
    procedure sieve2( logical array s ( * ); integer value n ) ;
    begin
        % start with everything flagged as prime                             % 
        for i := 1 until n do s( i ) := true;
        % sieve out the non-primes                                           %
        % the subscripts of s are  1  2  3  4  5  6  7  8  9 10 11 12 13...  %
        %      which correspond to 3  5  7  9 11 13 15 17 19 21 23 25 27...  %
        for i := 1 until truncate( sqrt( n ) ) do begin
            if s( i ) then begin
                integer ip;
                ip := ( i * 2 ) + 1;
                for p := i + ip step ip until n do s( p ) := false
            end if_s_i
        end for_i ;
    end sieve2 ;
    % test the sieve2 procedure                                              %
    integer primeMax, arrayMax;
    primeMax := 100;
    arrayMax := ( primeMax div 2 ) - 1;
    begin
        logical array s ( 1 :: arrayMax);
        i_w := 2; % set output field width                                   %
        s_w := 1; % and output separator width                               %
        % find and display the primes                                        %
        sieve2( s, arrayMax );
        write( 2 );
        for i := 1 until arrayMax do if s( i ) then writeon( ( i * 2 ) + 1 );
    end
end.
```

**Output:**

Same as the standard version.


## ALGOL-M

```mw
BEGIN

COMMENT
  FIND PRIMES UP TO THE SPECIFIED LIMIT (HERE 1,000) USING 
  CLASSIC SIEVE OF ERATOSTHENES;

% CALCULATE INTEGER SQUARE ROOT %
INTEGER FUNCTION ISQRT(N);
INTEGER N;
BEGIN
    INTEGER R1, R2;
    R1 := N;
    R2 := 1;
    WHILE R1 > R2 DO
        BEGIN
            R1 := (R1+R2) / 2;
            R2 := N / R1;
        END;
    ISQRT := R1;
END;

INTEGER LIMIT, I, J, FALSE, TRUE, COL, COUNT;
INTEGER ARRAY FLAGS[1:1000];

LIMIT := 1000;
FALSE := 0;
TRUE := 1;

WRITE("FINDING PRIMES FROM 2 TO",LIMIT);

% INITIALIZE TABLE %
WRITE("INITIALIZING ... ");
FOR I := 1 STEP 1 UNTIL LIMIT DO
  FLAGS[I] := TRUE;

% SIEVE FOR PRIMES %
WRITEON("SIEVING ... ");
FOR I := 2 STEP 1 UNTIL ISQRT(LIMIT) DO
  BEGIN
    IF FLAGS[I] = TRUE THEN
        FOR J := (I * I) STEP I UNTIL LIMIT DO
          FLAGS[J] := FALSE;
  END;

% WRITE OUT THE PRIMES TEN PER LINE %
WRITEON("PRINTING");
COUNT := 0;
COL := 1;
WRITE("");  
FOR I := 2 STEP 1 UNTIL LIMIT DO
  BEGIN
    IF FLAGS[I] = TRUE THEN 
      BEGIN
         WRITEON(I);
         COUNT := COUNT + 1;
         COL := COL + 1;
         IF COL > 10 THEN
           BEGIN
             WRITE("");
             COL := 1;
           END;
      END;
  END;

WRITE("");
WRITE(COUNT, " PRIMES WERE FOUND.");

END
```

**Output:**

```
FINDING PRIMES FROM 2 TO  1000
INTIALIZING ... SIEVING ... PRINTING
    2     3     5     7    11    13    17    19    23    29
   31    37    41    43    47    53    59    61    67    71
                      . . .
  877   881   883   887   907   911   919   929   937   941
  947   953   967   971   977   983   991   997

  168 PRIMES WERE FOUND.
```


## APL

All these versions requires ⎕io←0 (index origin 0).

It would have been better to require a result of the boolean mask rather than the actual list of primes. The list of primes obtains readily from the mask by application of a simple function (here {⍵/⍳⍴⍵}). Other related computations (such as the number of primes < n) obtain readily from the mask, easier than producing the list of primes.

### Non-Optimized Version

```mw
sieve2←{                          
  b←⍵⍴1             
  b[⍳2⌊⍵]←0         
  2≥⍵:b             
  p←{⍵/⍳⍴⍵}∇⌈⍵*0.5  
  m←1+⌊(⍵-1+p×p)÷p  
  b ⊣ p {b[⍺×⍺+⍳⍵]←0}¨ m
}

primes2←{⍵/⍳⍴⍵}∘sieve2
```

The required list of prime divisors obtains by recursion ({⍵/⍳⍴⍵}∇⌈⍵*0.5).

=== Optimized Version ===|

```mw
sieve←{                           
  b←⍵⍴{∧⌿↑(×/⍵)⍴¨~⍵↑¨1}2 3 5
  b[⍳6⌊⍵]←(6⌊⍵)⍴0 0 1 1 0 1 
  49≥⍵:b                    
  p←3↓{⍵/⍳⍴⍵}∇⌈⍵*0.5        
  m←1+⌊(⍵-1+p×p)÷2×p        
  b ⊣ p {b[⍺×⍺+2×⍳⍵]←0}¨ m      
}

primes←{⍵/⍳⍴⍵}∘sieve
```

The optimizations are as follows:

- Multiples of 2 3 5 are marked by initializing b with ⍵⍴{∧⌿↑(×/⍵)⍴¨~⍵↑¨1}2 3 5 rather than with ⍵⍴1.
- Subsequently, only odd multiples of primes > 5 are marked.
- Multiples of a prime to be marked start at its square.

### Examples

```mw
   primes 100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

   primes¨ ⍳14
┌┬┬┬─┬───┬───┬─────┬─────┬───────┬───────┬───────┬───────┬──────────┬──────────┐
││││2│2 3│2 3│2 3 5│2 3 5│2 3 5 7│2 3 5 7│2 3 5 7│2 3 5 7│2 3 5 7 11│2 3 5 7 11│
└┴┴┴─┴───┴───┴─────┴─────┴───────┴───────┴───────┴───────┴──────────┴──────────┘

   sieve 13
0 0 1 1 0 1 0 1 0 0 0 1 0

   +/∘sieve¨ 10*⍳10
0 4 25 168 1229 9592 78498 664579 5761455 50847534
```

The last expression computes the number of primes < 1e0 1e1 ... 1e9. The last number 50847534 can perhaps be called the anti-Bertelsen's number (http://mathworld.wolfram.com/BertelsensNumber.html).


## AppleScript

```mw
on sieveOfEratosthenes(limit)
    script o
        property numberList : {missing value}
    end script
    
    repeat with n from 2 to limit
        set end of o's numberList to n
    end repeat
    repeat with n from 2 to (limit ^ 0.5 div 1)
        if (item n of o's numberList is n) then
            repeat with multiple from (n * n) to limit by n
                set item multiple of o's numberList to missing value
            end repeat
        end if
    end repeat
    
    return o's numberList's numbers
end sieveOfEratosthenes

sieveOfEratosthenes(1000)
```

**Output:**

```mw
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997}
```


## ARM Assembly

Works with

:

as

version Raspberry Pi

```mw
/* ARM assembly Raspberry PI  */
/*  program cribleEras.s   */

 /* REMARK 1 : this program use routines in a include file 
   see task Include a file language arm assembly 
   for the routine affichageMess conversion10 
   see at end of this program the instruction include */
/* for constantes see task include a file in arm assembly */
/************************************/
/* Constantes                       */
/************************************/
.include "../constantes.inc"

.equ MAXI,      101

/*********************************/
/* Initialized data              */
/*********************************/
.data
sMessResult:        .asciz "Prime  : @ \n"
szCarriageReturn:   .asciz "\n"

/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
sZoneConv:                  .skip 24
TablePrime:                 .skip   4 * MAXI 
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                               @ entry of program 
    ldr r4,iAdrTablePrime           @ address prime table
    mov r0,#2                       @ prime 2
    bl displayPrime
    mov r1,#2
    mov r2,#1
1:                                  @ loop for multiple of 2
    str r2,[r4,r1,lsl #2]           @ mark  multiple of 2
    add r1,#2
    cmp r1,#MAXI                    @ end ?
    ble 1b                          @ no loop
    mov r1,#3                       @ begin indice
    mov r3,#1
2:
    ldr r2,[r4,r1,lsl #2]           @ load table élément
    cmp r2,#1                       @ is prime ?
    beq 4f
    mov r0,r1                       @ yes -> display
    bl displayPrime
    mov r2,r1
3:                                  @ and loop to mark multiples of this prime
    str r3,[r4,r2,lsl #2]
    add r2,r1                       @ add the prime
    cmp r2,#MAXI              @ end ?
    ble 3b                          @ no -> loop
4:
    add r1,#2                       @ other prime in table
    cmp r1,#MAXI              @ end table ?
    ble 2b                          @ no -> loop

100:                                @ standard end of the program 
    mov r0, #0                      @ return code
    mov r7, #EXIT                   @ request to exit program
    svc #0                          @ perform the system call
iAdrszCarriageReturn:    .int szCarriageReturn
iAdrsMessResult:         .int sMessResult
iAdrTablePrime:          .int TablePrime

/******************************************************************/
/*      Display prime table elements                                */ 
/******************************************************************/
/* r0 contains the prime */
displayPrime:
    push {r1,lr}                    @ save registers
    ldr r1,iAdrsZoneConv
    bl conversion10                 @ call décimal conversion
    ldr r0,iAdrsMessResult
    ldr r1,iAdrsZoneConv            @ insert conversion in message
    bl strInsertAtCharInc
    bl affichageMess                @ display message
100:
    pop {r1,lr}
    bx lr
iAdrsZoneConv:                   .int sZoneConv  
/***************************************************/
/*      ROUTINES INCLUDE                           */
/***************************************************/
.include "../affichage.inc"
```

```
Prime  : 2
Prime  : 3
Prime  : 5
Prime  : 7
Prime  : 11
Prime  : 13
Prime  : 17
Prime  : 19
Prime  : 23
Prime  : 29
Prime  : 31
Prime  : 37
Prime  : 41
Prime  : 43
Prime  : 47
Prime  : 53
Prime  : 59
Prime  : 61
Prime  : 67
Prime  : 71
Prime  : 73
Prime  : 79
Prime  : 83
Prime  : 89
Prime  : 97
Prime  : 101
```


## Arturo

```mw
sieve: function [upto][
    composites: array.of: inc upto false
    loop 2..to :integer sqrt upto 'x [
        if not? composites\[x][
            loop range.step: x x^2 upto 'c [
                composites\[c]: true
            ]
        ]
    ]
    result: []
    loop.with:'i composites 'c [
        unless c -> 'result ++ i
    ]
    return result -- [0,1]
]

print sieve 100
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```
