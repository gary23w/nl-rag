---
title: "Fibonacci sequence (part 1/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/10
---

# Fibonacci sequence

The **Fibonacci sequence** is a sequence   Fn   of natural numbers defined recursively:

```
      F0 = 0 
      F1 = 1 
      Fn = Fn-1 + Fn-2 , if n > 1 
```

**Task**

Write a function to generate the   nth   Fibonacci number.

Solutions can be iterative, recursive (though recursive solutions are generally considered too slow and are mostly used as an exercise in recursion), or use Binet's algebraic formula.

The sequence is sometimes extended for negative numbers by using an alternating inverse of the positive values. Rewriting the definition as

```
      Fn = Fn+2 - Fn+1 , if n < 0 
```

leads to

```
      F-n = (-1)n+1 Fn .
```

Support for negative n in the solution is optional.

**Related tasks**

- Fibonacci n-step number sequences
- Leonardo numbers

**References**

- Wikipedia, Fibonacci number
- Wikipedia, Lucas number
- MathWorld, Fibonacci Number
- Some identities for r-Fibonacci numbers
- OEIS Fibonacci numbers
- OEIS Lucas numbers


## 0815

```mw
%<:0D:>~$<:01:~%>=<:a94fad42221f2702:>~>
}:_s:{x{={~$x+%{=>~>x~-x<:0D:~>~>~^:_s:?
```


## 11l

Translation of

:

Python

```mw
F fib_iter(n)
   I n < 2
      R n
   V fib_prev = 1
   V fib = 1
   L 2 .< n
      (fib_prev, fib) = (fib, fib + fib_prev)
   R fib

L(i) 1..20
   print(fib_iter(i), end' ‘ ’)
print()
```

**Output:**

```
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```


## 360 Assembly

For maximum compatibility, programs use only the basic instruction set.

### using fullword integers

```mw
*        Fibonacci sequence    05/11/2014
*        integer (31 bits) = 10 decimals -> max fibo(46)
FIBONACC CSECT
         USING FIBONACC,R12    base register
SAVEAREA B     STM-SAVEAREA(R15) skip savearea
         DC    17F'0'          savearea
         DC    CL8'FIBONACC'   eyecatcher
STM      STM   R14,R12,12(R13) save previous context
         ST    R13,4(R15)      link backward
         ST    R15,8(R13)      link forward
         LR    R12,R15         set addressability
*        ----
         LA    R1,0            f(n-2)=0
         LA    R2,1            f(n-1)=1
         LA    R4,2            n=2 
         LA    R6,1            step
         LH    R7,NN           limit
LOOP     EQU   *               for n=2 to nn
         LR    R3,R2             f(n)=f(n-1)
         AR    R3,R1             f(n)=f(n-1)+f(n-2)
         CVD   R4,PW             n  convert binary to packed (PL8)
         UNPK  ZW,PW             packed (PL8) to zoned (ZL16)
         MVC   CW,ZW             zoned (ZL16) to  char (CL16)
         OI    CW+L'CW-1,X'F0'   zap sign
         MVC   WTOBUF+5(2),CW+14 output
         CVD   R3,PW             f(n) binary to packed decimal (PL8)
         MVC   ZN,EM             load mask
         ED    ZN,PW             packed dec (PL8) to char (CL20)
         MVC   WTOBUF+9(14),ZN+6 output
         WTO   MF=(E,WTOMSG)     write buffer
         LR    R1,R2             f(n-2)=f(n-1)
         LR    R2,R3             f(n-1)=f(n)
         BXLE  R4,R6,LOOP      endfor n
*        ----
         LM    R14,R12,12(R13) restore previous savearea pointer
         XR    R15,R15         return code set to 0
         BR    R14             return to caller
*        ----  DATA
NN       DC    H'46'           nn max n
PW       DS    PL8             15num
ZW       DS    ZL16
CW       DS    CL16
ZN       DS    CL20
*                  ' b 0 0 0 , 0 0 0 , 0 0 0 , 0 0 0 , 0 0 0'  15num
EM       DC    XL20'402020206B2020206B2020206B2020206B202120'  mask
WTOMSG   DS    0F
         DC    H'80',XL2'0000'
*                   fibo(46)=1836311903         
WTOBUF   DC    CL80'fibo(12)=1234567890'
         REGEQU
         END   FIBONACC
```

**Output:**

```
...
fibo(41)=   165,580,141
fibo(42)=   267,914,296
fibo(43)=   433,494,437
fibo(44)=   701,408,733
fibo(45)= 1,134,903,170
fibo(46)= 1,836,311,903
```

### using packed decimals

```mw
*        Fibonacci sequence        31/07/2018
*        packed dec (PL8) = 15 decimals => max fibo(73)
FIBOWTOP CSECT
         USING  FIBOWTOP,R13       base register
         B      72(R15)            skip savearea
         DC     17F'0'             savearea
         SAVE   (14,12)            save previous context
         ST     R13,4(R15)         link backward
         ST     R15,8(R13)         link forward
         LR     R13,R15            set addressability
*        ----
         ZAP    FNM2,=P'0'         f(0)=0
         ZAP    FNM1,=P'1'         f(1)=1
         LA     R4,2               n=2 
         LA     R6,1               step
         LH     R7,NN              limit
LOOP     EQU    *                  for n=2 to nn
         ZAP    FN,FNM1              f(n)=f(n-2)
         AP     FN,FNM2              f(n)=f(n-1)+f(n-2)
         CVD    R4,PW                n 
         MVC    ZN,EM                load mask
         ED     ZN,PW                packed dec (PL8) to char (CL16)
         MVC    WTOBUF+5(2),ZN+L'ZN-2  output
         MVC    ZN,EM                load mask
         ED     ZN,FN                packed dec (PL8) to char (CL16)
         MVC    WTOBUF+9(L'ZN),ZN        output
         WTO    MF=(E,WTOMSG)        write buffer
         ZAP    FNM2,FNM1            f(n-2)=f(n-1)
         ZAP    FNM1,FN              f(n-1)=f(n)
         BXLE   R4,R6,LOOP         endfor n
*        ----
         L      R13,4(0,R13)       restore previous savearea pointer
         RETURN (14,12),RC=0       restore registers from calling sav
*        ----   DATA
NN       DC     H'73'              nn
FNM2     DS     PL8                f(n-2)
FNM1     DS     PL8                f(n-1)
FN       DS     PL8                f(n)
PW       DS     PL8                15num
ZN       DS     CL20
*                   ' b 0 0 0 , 0 0 0 , 0 0 0 , 0 0 0 , 0 0 0'  15num
EM       DC     XL20'402020206B2020206B2020206B2020206B202120'  mask
WTOMSG   DS     0F
         DC     H'80',XL2'0000'
*                    fibo(73)=806515533049393
WTOBUF   DC     CL80'fibo(12)=123456789012345 '
         REGEQU  
         END    FIBOWTOP
```

**Output:**

```
...
fibo(68)=  72,723,460,248,141
fibo(69)= 117,669,030,460,994
fibo(70)= 190,392,490,709,135
fibo(71)= 308,061,521,170,129
fibo(72)= 498,454,011,879,264
fibo(73)= 806,515,533,049,393
```


## 6502 Assembly

This subroutine stores the first *n*—by default the first ten—Fibonacci numbers in memory, beginning (because, why not?) at address 3867 decimal = F1B hex. Intermediate results are stored in three sequential addresses within the low 256 bytes of memory, which are the most economical to access.

The results are calculated and stored, but are not output to the screen or any other physical device: how to do that would depend on the hardware and the operating system.

```mw
       LDA  #0
       STA  $F0     ; LOWER NUMBER
       LDA  #1
       STA  $F1     ; HIGHER NUMBER
       LDX  #0
LOOP:  LDA  $F1
       STA  $0F1B,X
       STA  $F2     ; OLD HIGHER NUMBER
       ADC  $F0
       STA  $F1     ; NEW HIGHER NUMBER
       LDA  $F2
       STA  $F0     ; NEW LOWER NUMBER
       INX
       CPX  #$0A    ; STOP AT FIB(10)
       BMI  LOOP
       RTS          ; RETURN FROM SUBROUTINE
```


## 68000 Assembly

Translation of

:

ARM Assembly

Input is in D0, and the output is also in D0. There is no protection from 32-bit overflow, so use at your own risk. (I used this C compiler to create this in ARM Assembly and translated it manually into 68000 Assembly. It wasn't that difficult since both CPUs have similar architectures.)

```mw
fib:
   MOVEM.L D4-D5,-(SP)
      MOVE.L D0,D4
      MOVEQ #0,D5
      CMP.L #2,D0
      BCS .bar
      MOVEQ #0,D5
.foo:
      MOVE.L D4,D0
      SUBQ.L #1,D0
      JSR fib
      SUBQ.L #2,D4
      ADD.L D0,D5
      CMP.L #1,D4
      BHI .foo
.bar:
      MOVE.L D5,D0
      ADD.L D4,D0
   MOVEM.L (SP)+,D4-D5
   RTS
```


## 8080 Assembly

This subroutine expects to be called with the value of ${\displaystyle n}$ in register A, and returns ${\displaystyle f(n)}$ also in A. You may want to take steps to save the previous contents of B, C, and D. The routine only works with fairly small values of ${\displaystyle n}$ .

```mw
FIBNCI: MOV  C,  A  ; C will store the counter
        DCR  C      ; decrement, because we know f(1) already
        MVI  A,  1
        MVI  B,  0
LOOP:   MOV  D,  A
        ADD  B      ; A := A + B
        MOV  B,  D
        DCR  C
        JNZ  LOOP   ; jump if not zero
        RET         ; return from subroutine
```

The range may be easily be extended from the 13th (= 233) to the 24th (= 46368) Fibonacci number with 16-bit addition. The code here assumes the CP/M operating system.

```mw
       ;-------------------------------------------------------
       ; useful equates
       ;-------------------------------------------------------
bdos  equ   5  ; BDOS entry 
cr     equ  13 ; ASCII carriage return
lf     equ  10 ; ASCII line feed
space equ       32   ; ASCII space char
conout   equ   2  ; BDOS console output function
putstr   equ       9 ; BDOS print string function
nterms   equ      20 ; number of terms (max=24) to display
       ;-------------------------------------------------------
       ; main code begins here
       ;-------------------------------------------------------
       org      100h
       lxi      h,0         ; save CP/M's stack
       dad      sp
       shld    oldstk
       lxi      sp,stack   ; set our own stack
       lxi      d,signon   ; print signon message
       mvi      c,putstr
       call bdos
       mvi  a,0          ; start with Fib(0)
mloop:   push  a         ; save our count 
       call    fib
       call putdec
       mvi      a,space    ; separate the numbers
       call putchr
       pop      a        ; get our count back
       inr      a        ; increment it
       cpi      nterms+1   ; have we reached our limit?
       jnz      mloop      ; no, keep going
       lhld oldstk      ; all done; get CP/M's stack back
       sphl           ; restore it
       ret                ; back to command processor
       ;-------------------------------------------------------
       ;  calculate nth Fibonacci number (max n = 24)
       ;  entry: A = n 
       ;  exit:  HL = Fib(n)
       ;-------------------------------------------------------
fib:  mov   c,a           ; C holds n
       lxi  d,0           ; DE holds Fib(n-2)
       lxi  h,1           ; HL holds Fib(n-1)
       ana      a         ; Fib(0) is a special case
       jnz      fib2     ; n > 0 so calculate normally
       xchg            ; otherwise return with HL=0
       ret
fib2: dcr       c
       jz       fib3     ; we're done
       push    h          ; save Fib(n-1)
       dad  d          ; HL = Fib(n), soon to be Fib(n-1) 
       pop  d          ; DE = old F(n-1), now Fib(n-2)
       jmp  fib2      ; ready for next pass
fib3: ret
       ;-------------------------------------------------------
       ; console output of char in A register
       ;-------------------------------------------------------
putchr:  push  h
       push d
       push b
       mov      e,a
       mvi      c,conout
       call bdos
       pop      b
       pop      d
       pop      h
       ret
       ;---------------------------------------------------------
       ; Output decimal number to console
       ; HL holds 16-bit unsigned binary number to print
       ;---------------------------------------------------------
putdec: push   b
       push d
       push h
       lxi      b,-10
       lxi      d,-1
putdec2:
       dad      b
       inx      d
       jc       putdec2
       lxi      b,10
       dad      b
       xchg
       mov      a,h
       ora  l
       cnz      putdec     ; recursive call
       mov      a,e
       adi      '0'
       call putchr
       pop      h
       pop      d
       pop      b
       ret
       ;-------------------------------------------------------
       ; data area
       ;-------------------------------------------------------
signon: db      'Fibonacci number sequence:',cr,lf,'$'
oldstk:  dw     0
stack equ       $+128      ; 64-level stack
       ;
       end
```

**Output:**

```
Fibonacci number sequence:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```


## 8086 Assembly

### Calculating the values at runtime

Is it cheating to write it in C for 64-bit x86 then port it to 16-bit x86?

The max input is 24 before you start having 16-bit overflow.

```mw
fib:
;  WRITTEN IN C WITH X86-64 CLANG 3.3 AND DOWNGRADED TO 16-BIT X86
;  INPUT: DI = THE NUMBER YOU WISH TO CALC THE FIBONACCI NUMBER FOR.
;  OUTPUTS TO AX
                                 
        push    BP
        push    BX
        push    AX
        mov     BX, DI        ;COPY INPUT TO BX
        xor     AX, AX        ;MOV AX,0
        test    BX, BX        ;SET FLAGS ACCORDING TO BX
        je      LBB0_4        ;IF BX == 0 RETURN 0
        cmp     BX, 1         ;IF BX == 1 RETURN 1
        jne     LBB0_3
        mov     AX, 1         ;ELSE, SET AX = 1 AND RETURN
        jmp     LBB0_4
LBB0_3:
        lea     DI, WORD PTR [BX - 1]   ;DI = BX - 1
        call    fib        ;RETURN FIB(BX-1)
        mov     BP, AX        ;STORE THIS IN BP
        add     BX, -2
        mov     DI, BX  
        call    fib        ;GET FIB(DI - 2)
        add     AX, BP             ;RETURN FIB(DI - 1) + FIB(DI - 2)
LBB0_4:

   add sp,2
        pop     BX
        pop     BP
        ret
```

### Using A Lookup Table

With old computers it was common to use lookup tables to fetch pre-calculated values that would otherwise take some time to compute. The elements of the table are ordered by index, so you can simply create a function that takes an offset as the parameter and returns the element of the array at that offset.

Although lookup tables are very fast, there are some drawbacks to using them. For one, you end up taking up a lot of space. We're wasting a lot of bytes to store very low numbers at the beginning (each takes up 4 bytes regardless of how many digits you see). Unfortunately, when using lookup tables you have very little choice, since trying to conditionally change the scaling of the index would more than likely take more code than encoding all data as the maximum size regardless of the contents, as was done here. This keeps it simple for the CPU, which isn't aware of the intended size of each entry of the table.

For the purpose of this example, assume that both this code and the table are in the `.CODE` segment.

```mw
getfib:
;input: BX = the desired fibonacci number (in other words, the "n" in "F(n)")
;       DS must point to the segment where the fibonacci table is stored
;outputs to DX:AX (DX = high word, AX = low word)
  push ds
    cmp bx,41  ;bounds check
    ja IndexOutOfBounds
    shl bx,1
    shl bx,1 ;multiply by 4, since this is a table of dwords
    mov ax,@code
    mov ds,ax
    mov si,offset fib
    mov ax,[ds:si]    ;fetch the low word into AX
    mov dx,2[ds:si]   ;fetch the high word into DX
  pop ds
  ret

IndexOutOfBounds:
     stc             ;set carry to indicate an error
     mov ax,0FFFFh   ;return FFFF as the error code
   pop ds
   ret

;table of the first 41 fibonacci numbers
fib dword 0, 1, 1, 2, 3, 5, 8, 13 
    dword 21, 34, 55, 89, 144, 233, 377, 610
    dword 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657
    dword 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269
    dword 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986
    dword 102334155
```


## 8th

An iterative solution:

```mw
: fibon \ n -- fib(n)
  >r 0 1 
  ( tuck n:+ ) \ fib(n-2) fib(n-1) -- fib(n-1) fib(n)
  r> n:1- times ;

: fib \ n -- fib(n)
  dup 1 n:= if 1 ;; then
  fibon nip ;
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

or android 64 bits with application Termux

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program numfibo64.s   */

/*******************************************/
/* Constantes                              */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"

/*********************************/
/* Initialized data              */
/*********************************/
.data
szMessDebutPgm:    .asciz "Program 64 bits start. \n"
szCarriageReturn:  .asciz "\n"
szMessFinOK:       .asciz "Program normal end. \n"
szMessErreur:      .asciz "Error  !!!\n"
szMessFibo:        .asciz "\nFibonaci numbers :\n"

.align 4
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss  
sZoneConv:               .skip 24 
.align 4

/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:
    ldr x0,qAdrszMessDebutPgm
    bl affichageMess            // start message 
    
    ldr x0,qAdrszMessFibo
    bl affichageMess
    mov x0,#0                   // rank
    mov x1,#0                   // L(0)  or L(n-2)
    mov x2,#1                   // L(1)  or L(n-1)        
    mov x3,#20                  // maxi
    bl genererFibo
    
    ldr x0,qAdrszMessFinOK
    bl affichageMess       
    b 100f
99:
    ldr x0,qAdrszMessErreur        // error
    bl affichageMess
    mov x0, #1                     // return code error
    b 100f
100: 
    mov x8,EXIT 
    svc #0                         // system call
qAdrszMessDebutPgm:          .quad szMessDebutPgm
qAdrszMessFinOK:             .quad szMessFinOK
qAdrszMessErreur:            .quad szMessErreur 
qAdrsZoneConv:               .quad sZoneConv
qAdrszMessFibo:              .quad szMessFibo
/***************************************************/
/*   Generation Fibonacci number                 */
/***************************************************/
/* x0 contains n     */
/* x1 contains L(0)  */
/* x2 contains L(1)  */
/* x3 contains limit number */
genererFibo:
    stp x4,lr,[sp,-16]!
    stp x5,x6,[sp,-16]! 
    mov x4,x0
    cmp x3,#0                    // end compute ?
    ble 100f
    cmp x0,#0                    // L(0) ?
    bne 1f
    mov x0,x1
    bl displayNumber
    add x0,x4,#1                // increment rank
    sub x3,x3,#1                // decrement counter
    bl genererFibo
    b 100f
1:
    cmp x0,#1                   // L(1) ?
    bne 2f
    mov x0,x2
    bl displayNumber
    add x0,x4,#1
    sub x3,x3,#1
    bl genererFibo
    b 100f
2:
    add x5,x2,x1                // add L(n-2) L(n-1)  
    mov x0,x5
    bl displayNumber
    add x0,x4,#1
    sub x3,x3,#1
    mov x1,x2                   // L(n-1) -> L(n-2)
    mov x2,x5                   // number -> L(n-1)
    bl genererFibo
    b 100f
    
100:
    ldp x5,x6,[sp],16 
    ldp x4,lr,[sp],16         // TODO: a completer 
    ret
/***************************************************/
/*   display number                  */
/***************************************************/
/* x0 contains number  */
displayNumber:
    stp x1,lr,[sp,-16]!       // TODO: a completer 
    ldr x1,qAdrsZoneConv
    bl conversion10
    ldr x0,qAdrsZoneConv
    bl affichageMess
    ldr x0,qAdrszCarriageReturn
    bl affichageMess
100:
    ldp x1,lr,[sp],16         // TODO: a completer 
    ret
qAdrszCarriageReturn:         .quad szCarriageReturn

/***************************************************/
/*      ROUTINES INCLUDE                 */
/***************************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeARM64.inc"
```

**Output:**

```
Program 64 bits start.

Fibonaci numbers :
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
Program normal end.
```


## ABAP

### Iterative

```mw
FORM fibonacci_iter USING index TYPE i
                    CHANGING number_fib TYPE i.
  DATA: lv_old type i,
        lv_cur type i.
  Do index times.
    If sy-index = 1 or sy-index = 2.
      lv_cur = 1.
      lv_old = 0.
    endif.
    number_fib = lv_cur + lv_old.
    lv_old = lv_cur.
    lv_cur = number_fib.
  enddo.
ENDFORM.
```

### Impure Functional

Works with

:

ABAP

version 7.4 SP08 Or above only

```mw
cl_demo_output=>display( REDUCE #( INIT fibnm = VALUE stringtab( ( |0| ) ( |1| ) )
                                        n TYPE string
                                        x = `0`
                                        y = `1`
                                      FOR i = 1 WHILE i <= 100
                                     NEXT n = ( x + y )
                                          fibnm = VALUE #( BASE fibnm ( n ) )
                                          x = y
                                          y = n ) ).
```


## ACL2

Fast, tail recursive solution:

```mw
(defun fast-fib-r (n a b)
   (if (or (zp n) (zp (1- n)))
       b
       (fast-fib-r (1- n) b (+ a b))))

(defun fast-fib (n)
   (fast-fib-r n 1 1))

(defun first-fibs-r (n i)
   (declare (xargs :measure (nfix (- n i))))
   (if (zp (- n i))
       nil
       (cons (fast-fib i)
             (first-fibs-r n (1+ i)))))

(defun first-fibs (n)
   (first-fibs-r n 0))
```

**Output:**

```
>(first-fibs 20)
(1 1 2 3 5 8 13 21 34 55 89
   144 233 377 610 987 1597 2584 4181 6765)
```


## Action!

Action! language does not support recursion. Therefore an iterative approach has been proposed.

```mw
INT FUNC Fibonacci(INT n)
  INT curr,prev,tmp

  IF n>=-1 AND n<=1 THEN
    RETURN (n)
  FI

  prev=0
  IF n>0 THEN
    curr=1
    DO
      tmp=prev
      prev=curr
      curr==+tmp
      n==-1
    UNTIL n=1
    OD
  ELSE
    curr=-1
    DO
      tmp=prev
      prev=curr
      curr==+tmp
      n==+1
    UNTIL n=-1
    OD
  FI
RETURN (curr)

PROC Main()
  BYTE n
  INT f

  Put(125) ;clear screen

  FOR n=0 TO 22
  DO
    f=Fibonacci(n)
    Position(2,n+1)
    PrintF("Fib(%I)=%I",n,f)

    IF n>0 THEN
      f=Fibonacci(-n)
      Position(21,n+1)
      PrintF("Fib(%I)=%I",-n,f)
    FI
  OD
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
Fib(0)=0
Fib(1)=1           Fib(-1)=-1
Fib(2)=1           Fib(-2)=-1
Fib(3)=2           Fib(-3)=-2
Fib(4)=3           Fib(-4)=-3
Fib(5)=5           Fib(-5)=-5
Fib(6)=8           Fib(-6)=-8
Fib(7)=13          Fib(-7)=-13
Fib(8)=21          Fib(-8)=-21
Fib(9)=34          Fib(-9)=-34
Fib(10)=55         Fib(-10)=-55
Fib(11)=89         Fib(-11)=-89
Fib(12)=144        Fib(-12)=-144
Fib(13)=233        Fib(-13)=-233
Fib(14)=377        Fib(-14)=-377
Fib(15)=610        Fib(-15)=-610
Fib(16)=987        Fib(-16)=-987
Fib(17)=1597       Fib(-17)=-1597
Fib(18)=2584       Fib(-18)=-2584
Fib(19)=4181       Fib(-19)=-4181
Fib(20)=6765       Fib(-20)=-6765
Fib(21)=10946      Fib(-21)=-10946
Fib(22)=17711      Fib(-22)=-17711
```


## ActionScript

```mw
public function fib(n:uint):uint
{
    if (n < 2)
        return n;
    
    return fib(n - 1) + fib(n - 2);
}
```


## Ada

### Recursive

```mw
with Ada.Text_IO, Ada.Command_Line;

procedure Fib is

   X: Positive := Positive'Value(Ada.Command_Line.Argument(1));

   function Fib(P: Positive) return Positive is
   begin
      if P <= 2 then
         return 1;
      else
         return Fib(P-1) + Fib(P-2);
      end if;
   end Fib;

begin
   Ada.Text_IO.Put("Fibonacci(" & Integer'Image(X) & " ) = ");
   Ada.Text_IO.Put_Line(Integer'Image(Fib(X)));
end Fib;
```

### Iterative, build-in integers

```mw
with Ada.Text_IO;  use Ada.Text_IO;

procedure Test_Fibonacci is
   function Fibonacci (N : Natural) return Natural is
      This : Natural := 0;
      That : Natural := 1;
      Sum  : Natural;
   begin
      for I in 1..N loop
         Sum  := This + That;
         That := This;
         This := Sum;
      end loop;
      return This;
   end Fibonacci;
begin
   for N in 0..10 loop
      Put_Line (Positive'Image (Fibonacci (N)));
   end loop;
end Test_Fibonacci;
```

**Output:**

```
 0
 1
 1
 2
 3
 5
 8
 13
 21
 34
 55
```

### Iterative, long integers

Using the big integer implementation from a cryptographic library [1].

```mw
with Ada.Text_IO, Ada.Command_Line, Crypto.Types.Big_Numbers;

procedure Fibonacci is

   X: Positive := Positive'Value(Ada.Command_Line.Argument(1));

   Bit_Length: Positive := 1 + (696 * X) / 1000;
   -- that number of bits is sufficient to store the full result.

   package LN is new Crypto.Types.Big_Numbers
     (Bit_Length + (32 - Bit_Length mod 32));
     -- the actual number of bits has to be a multiple of 32
   use LN;

   function Fib(P: Positive) return Big_Unsigned is
      Previous: Big_Unsigned := Big_Unsigned_Zero;
      Result:   Big_Unsigned := Big_Unsigned_One;
      Tmp:      Big_Unsigned;
   begin
      -- Result = 1 = Fibonacci(1)
      for I in 1 .. P-1 loop
         Tmp := Result;
         Result := Previous + Result;
         Previous := Tmp;
         -- Result = Fibonacci(I+1))
      end loop;
      return Result;
   end Fib;

begin
   Ada.Text_IO.Put("Fibonacci(" & Integer'Image(X) & " ) = ");
   Ada.Text_IO.Put_Line(LN.Utils.To_String(Fib(X)));
end Fibonacci;
```

**Output:**

```
> ./fibonacci 777
Fibonacci( 777 ) = 1081213530912648191985419587942084110095342850438593857649766278346130479286685742885693301250359913460718567974798268702550329302771992851392180275594318434818082
```

### Fast method using fast matrix exponentiation

```mw
with ada.text_io;
use  ada.text_io;

procedure fast_fibo is 
   -- We work with biggest natural integers in a 64 bits machine 
   type Big_Int is mod 2**64;

   -- We provide an index type for accessing the fibonacci sequence terms 
   type Index is new Big_Int;

   -- fibo is a generic function that needs a modulus type since it will return
   -- the n'th term of the fibonacci sequence modulus this type (use Big_Int to get the   
   -- expected behaviour in this particular task)
   generic
      type ring_element is mod <>;
      with function "*" (a, b : ring_element) return ring_element is <>;
      function fibo (n : Index) return ring_element;
   function fibo (n : Index) return ring_element is

      type matrix is array (1 .. 2, 1 .. 2) of ring_element;

      -- f is the matrix you apply to a column containing (F_n, F_{n+1}) to get 
      -- the next one containing (F_{n+1},F_{n+2})
      -- could be a more general matrix (given as a generic parameter) to deal with 
      -- other linear sequences of order 2
      f : constant matrix := (1 => (0, 1), 2 => (1, 1));

      function "*" (a, b : matrix) return matrix is
      (1 => (a(1,1)*b(1,1)+a(1,2)*b(2,1), a(1,1)*b(1,2)+a(1,2)*b(2,2)),
       2 => (a(2,1)*b(1,1)+a(2,2)*b(2,1), a(2,1)*b(1,2)+a(2,2)*b(2,2)));

      function square (m : matrix) return matrix is (m * m);

      -- Fast_Pow could be non recursive but it doesn't really matter since
      -- the number of calls is bounded up by the size (in bits) of Big_Int (e.g 64)
      function fast_pow (m : matrix; n : Index) return matrix is
      (if n = 0 then (1 => (1, 0), 2 => (0, 1)) -- = identity matrix
       elsif n mod 2 = 0 then square (fast_pow (m, n / 2)) 
       else m * square (fast_pow (m, n / 2)));

   begin
      return fast_pow (f, n)(2, 1);
   end fibo;

   function Big_Int_Fibo is new fibo (Big_Int);
begin
   -- calculate instantly F_n with n=10^15 (modulus 2^64 )
   put_line (Big_Int_Fibo (10**15)'img);
end fast_fibo;
```


## AdvPL

### Recursive

```mw
#include "totvs.ch"
User Function fibb(a,b,n)
return(if(--n>0,fibb(b,a+b,n),a))
```

### Iterative

```mw
#include "totvs.ch"
User Function fibb(n) 
   local fnow:=0, fnext:=1, tempf
   while (--n>0)
      tempf:=fnow+fnext
      fnow:=fnext
      fnext:=tempf
   end while
return(fnext)
```


## Agda

```mw
module FibonacciSequence where

open import Data.Nat using (ℕ ; zero ; suc ; _+_)

rec_fib : (m : ℕ) -> (a : ℕ) -> (b : ℕ) -> ℕ
rec_fib zero a b = a
rec_fib (suc k) a b = rec_fib k b (a + b)

fib : (n : ℕ) -> ℕ
fib n = rec_fib n zero (suc zero)
```


## Aime

```mw
integer
fibs(integer n)
{
    integer w;

    if (n == 0) {
        w = 0;
    } elif (n == 1) {
        w = 1;
    } else {
        integer a, b, i;

        i = 1;
        a = 0;
        b = 1;
        while (i < n) {
            w = a + b;
            a = b;
            b = w;
            i += 1;
        }
    }

    return w;
}
```


## ALGOL 60

Works with

:

A60

```mw
begin
    comment Fibonacci sequence;
    integer procedure fibonacci(n); value n; integer n;
    begin
        integer i, fn, fn1, fn2;
        fn2 := 1;
        fn1 := 0;
        fn  := 0;
        for i := 1 step 1 until n do begin
            fn  := fn1 + fn2;
            fn2 := fn1;
            fn1 := fn
        end;
        fibonacci := fn
    end fibonacci;
 
    integer i;
    for i := 0 step 1 until 20 do outinteger(1,fibonacci(i))
end
```

**Output:**

```
 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584  4181  6765
```


## ALGOL 68

### Analytic

Works with

:

ALGOL 68

version Revision 1 - no extensions to language used

Works with

:

ALGOL 68G

version Any - tested with release

1.18.0-9h.tiny

Works with

:

ELLA ALGOL 68

version Any (with appropriate job cards) - tested with release

1.8-8d

```mw
PROC analytic fibonacci = (LONG INT n)LONG INT:(
  LONG REAL sqrt 5 = long sqrt(5);
  LONG REAL p = (1 + sqrt 5) / 2;
  LONG REAL q = 1/p;
  ROUND( (p**n + q**n) / sqrt 5 )
);

FOR i FROM 1 TO 30 WHILE
  print(whole(analytic fibonacci(i),0));
# WHILE # i /= 30 DO
  print(", ")
OD;
print(new line)
```

**Output:**

```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040
```

### Iterative

Works with

:

ALGOL 68

version Revision 1 - no extensions to language used

Works with

:

ALGOL 68G

version Any - tested with release

1.18.0-9h.tiny

Works with

:

ELLA ALGOL 68

version Any (with appropriate job cards) - tested with release

1.8-8d

```mw
PROC iterative fibonacci = (INT n)INT: 
  CASE n+1 IN
    0, 1, 1, 2, 3, 5
  OUT
    INT even:=3, odd:=5;
    FOR i FROM odd+1 TO n DO
      (ODD i|odd|even) := odd + even
    OD;
    (ODD n|odd|even)
  ESAC;

FOR i FROM 0 TO 30 WHILE
  print(whole(iterative fibonacci(i),0));
# WHILE # i /= 30 DO
  print(", ")
OD;
print(new line)
```

**Output:**

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040
```

### Recursive

Works with

:

ALGOL 68

version Revision 1 - no extensions to language used

Works with

:

ALGOL 68G

version Any - tested with release

1.18.0-9h.tiny

Works with

:

ELLA ALGOL 68

version Any (with appropriate job cards) - tested with release

1.8-8d

```mw
PROC recursive fibonacci = (INT n)INT:
  ( n < 2 | n | fib(n-1) + fib(n-2));
```

### Generative

Translation of

:

Python

– Note: This specimen retains the original

Python

coding style.

Works with

:

ALGOL 68

version Revision 1 - no extensions to language used

Works with

:

ALGOL 68G

version Any - tested with release

1.18.0-9h.tiny

Works with

:

ELLA ALGOL 68

version Any (with appropriate job cards) - tested with release

1.8-8d

```mw
MODE YIELDINT = PROC(INT)VOID;

PROC gen fibonacci = (INT n, YIELDINT yield)VOID: (
  INT even:=0, odd:=1;
  yield(even);
  yield(odd);
  FOR i FROM odd+1 TO n DO
    yield( (ODD i|odd|even) := odd + even )
  OD
);

main:(
  # FOR INT n IN # gen fibonacci(30, # ) DO ( #
  ##   (INT n)VOID:(
        print((" ",whole(n,0)))
  # OD # ));
    print(new line)
)
```

**Output:**

```
1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
```

### Array (Table) Lookup

Works with

:

ALGOL 68

version Revision 1 - no extensions to language used

Works with

:

ALGOL 68G

version Any - tested with release

1.18.0-9h.tiny

Works with

:

ELLA ALGOL 68

version Any (with appropriate job cards) - tested with release

1.8-8d

This uses a pre-generated list, requiring much less run-time processor usage, but assumes that INT is only 31 bits wide.

```mw
[]INT const fibonacci = []INT( -1836311903, 1134903170,
  -701408733, 433494437, -267914296, 165580141, -102334155,
  63245986, -39088169, 24157817, -14930352, 9227465, -5702887,
  3524578, -2178309, 1346269, -832040, 514229, -317811, 196418,
  -121393, 75025, -46368, 28657, -17711, 10946, -6765, 4181,
  -2584, 1597, -987, 610, -377, 233, -144, 89, -55, 34, -21, 13,
  -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
  144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
  28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
  1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
  39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
  701408733, 1134903170, 1836311903
)[@-46];

PROC VOID value error := stop;

PROC lookup fibonacci = (INT i)INT: (
  IF LWB const fibonacci <= i AND i<= UPB const fibonacci THEN
    const fibonacci[i]
  ELSE
    value error; SKIP
  FI
);

FOR i FROM 0 TO 30 WHILE
  print(whole(lookup fibonacci(i),0));
# WHILE # i /= 30 DO
  print(", ")
OD;
print(new line)
```

**Output:**

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040
```


## ALGOL W

```mw
begin
    % return the nth Fibonacci number %
    integer procedure Fibonacci( integer value n ) ;
        begin
            integer fn, fn1, fn2;
            fn2 := 1;
            fn1 := 0;
            fn  := 0;
            for i := 1 until n do begin
                fn  := fn1 + fn2;
                fn2 := fn1;
                fn1 := fn
            end ;
            fn
        end Fibonacci ;

    for i := 0 until 10 do writeon( i_w := 3, s_w := 0, Fibonacci( i ) )

end.
```

**Output:**

```
  0  1  1  2  3  5  8 13 21 34 55
```


## ALGOL-M

Note that the 21st Fibonacci number (= 10946) is the largest that can be calculated without overflowing ALGOL-M's integer data type.

#### Iterative

```mw
INTEGER FUNCTION FIBONACCI( X ); INTEGER X;
BEGIN
    INTEGER M, N, A, I;
    M := 0;
    N := 1;
    FOR I := 2 STEP 1 UNTIL X DO
    BEGIN
        A := N;
        N := M + N;
        M := A;
    END;
    FIBONACCI := N;
END;
```

#### Naively recursive

```mw
INTEGER FUNCTION FIBONACCI( X ); INTEGER X;
BEGIN
    IF X < 3 THEN
        FIBONACCI := 1
    ELSE
        FIBONACCI := FIBONACCI( X - 2 ) + FIBONACCI( X - 1 );
END;
```


## Alore

```mw
def fib(n as Int) as Int
   if n < 2
      return 1
   end
   return fib(n-1) + fib(n-2)
end
```


## Amazing Hopper

Analitic, Recursive and Iterative mode.

```mw
#include <hbasic.h>

#define TERM1    1.61803398874989
#define TERM2    -0.61803398874989

#context get Fibonacci number with analitic mode
  GetArgs(n) 
  get Inv of (M_SQRT5), Mul by( Pow (TERM 1, n), Minus( Pow(TERM 2, n) )  );
  then Return\\

#proto fibonacci_recursive(__X__)
#synon _fibonacci_recursive    getFibonaccinumberwithrecursivemodeof

#proto fibonacci_iterative(__X__)
#synon _fibonacci_iterative    getFibonaccinumberwithiterativemodeof

Begin
  Option Stack 1024

  get Arg Number(2, n), and Take( n );
  then, get Fibonacci number with analitic mode, and Print It with a Newl.
  secondly, get Fibonacci number with recursive mode of(n), and Print It with a Newl.
  finally, get Fibonacci number with iterative mode of (n), and Print It with a Newl.
End

Subrutines

fibonacci_recursive(n)
   Iif ( var(n) Is Le? (2), 1 , \
         get Fibonacci number with recursive mode of( var(n) Minus (1));\
         get Fibonacci number with recursive mode of( var(n) Minus (2)); and Add It )
Return

fibonacci_iterative(n)
  A=0
  B=1
  For Up( I:=2, n, 1 )
    C=B
    Let ( B: = var(A) Plus (B) )
    A=C
  Next
Return(B)
```

**Output:**

```
$ hopper src/fibo1.bas 25
75025
75025
75025
```


## AntLang

```mw
/Sequence
fib:{<0;1> {x,<x[-1]+x[-2]>}/ range[x]}
/nth
fibn:{fib[x][x]}
```


## Apex

```mw
/*
 author: snugsfbay
 date: March 3, 2016
 description: Create a list of x numbers in the Fibonacci sequence.
     - user may specify the length of the list 
     - enforces a minimum of 2 numbers in the sequence because any fewer is not a sequence
     - enforces a maximum of 47 because further values are too large for integer data type 
     - Fibonacci sequence always starts with 0 and 1 by definition
*/
public class FibNumbers{

final static Integer MIN = 2; //minimum length of sequence
final static Integer MAX = 47; //maximum length of sequence

/* 
  description: method to create a list of numbers in the Fibonacci sequence 
  param: user specified integer representing length of sequence should be 2-47, inclusive.
      - Sequence starts with 0 and 1 by definition so the minimum length could be as low as 2.
      - For 48th number in sequence or greater, code would require a Long data type rather than an Integer.
  return: list of integers in sequence.
*/
public static List<Integer> makeSeq(Integer len){

  List<Integer> fib = new List<Integer>{0,1}; // initialize list with first two values
  Integer i;
  
  if(len<MIN || len==null || len>MAX) {
      if (len>MAX){
          len=MAX; //set length to maximum if user entered too high a value
      }else{
          len=MIN; //set length to minimum if user entered too low a value or none
      }
  } //This could be refactored using teneray operator, but we want code coverage to be reflected for each condition
  
  //start with initial list size to find previous two values in the sequence, continue incrementing until list reaches user defined length
  for(i=fib.size(); i<len; i++){ 
    fib.add(fib[i-1]+fib[i-2]); //create new number based on previous numbers and add that to the list
  }

  return fib; 
  }
  
}
```


## APL

#### Naive Recursive

Works with

:

Dyalog APL

The idomatic array way:

```mw
fib←{⍵≤1:⍵ ⋄ (+/∇¨⍵-1 2}
```

or the scalar way:

```mw
fib←{⍵≤1:⍵ ⋄ (∇⍵-1)+∇⍵-2}
```

This naive solution requires Dyalog APL or April because GNU APL does not support this syntax for conditional guards.

#### Array

Works with

:

Dyalog APL

Works with

:

GNU APL

Since APL is an array language we'll use the following identity:

${\displaystyle {\begin{pmatrix}1&1\\1&0\end{pmatrix}}^{n}={\begin{pmatrix}F_{n+1}&F_{n}\\F_{n}&F_{n-1}\end{pmatrix}}.}$

In APL:

```mw
↑+.×/N/⊂2 2⍴1 1 1 0
```

Plugging in 4 for N gives the following result:

${\displaystyle {\begin{pmatrix}5&3\\3&2\end{pmatrix}}}$

Here's what happens: We replicate the 2-by-2 matrix N times and then apply inner product-replication. The *First* removes the shell from the *Enclose*. At this point we're basically done, but we need to pick out only ${\displaystyle F_{n}}$ in order to complete the task. Here's one way:

```mw
↑0 1↓↑+.×/N/⊂2 2⍴1 1 1 0
```

#### Analytic

Works with

:

Dyalog APL

Works with

:

GNU APL

An alternative approach, using Binet's formula (which was apparently known long before Binet):

```mw
⌊.5+(((1+PHI)÷2)*⍳N)÷PHI←5*.5
```


## AppleScript

### Imperative

```mw
set fibs to {}
set x to (text returned of (display dialog "What fibbonaci number do you want?" default answer "3"))
set x to x as integer
repeat with y from 1 to x
   if (y = 1 or y = 2) then
      copy 1 to the end of fibs
   else
      copy ((item (y - 1) of fibs) + (item (y - 2) of fibs)) to the end of fibs
   end if
end repeat
return item x of fibs
```

### Functional

The simple recursive version is famously slow:

```mw
on fib(n)
    if n < 1 then
        0
    else if n < 3 then
        1
    else
        fib(n - 2) + fib(n - 1)
    end if
end fib
```

but we can combine **enumFromTo(m, n)** with the accumulator of a higher-order **fold/reduce** function to memoize the series:

Translation of

:

JavaScript

(ES6 memoized fold example)

Translation of

:

Haskell

(Memoized fold example)

```mw
-------------------- FIBONACCI SEQUENCE --------------------

-- fib :: Int -> Int
on fib(n)
    
    -- lastTwo : (Int, Int) -> (Int, Int)
    script lastTwo
        on |λ|([a, b])
            [b, a + b]
        end |λ|
    end script
    
    item 1 of foldl(lastTwo, {0, 1}, enumFromTo(1, n))
end fib

--------------------------- TEST ---------------------------
on run
    
    fib(32)
    
    --> 2178309
end run

-------------------- GENERIC FUNCTIONS ---------------------

-- enumFromTo :: Int -> Int -> [Int]
on enumFromTo(m, n)
    if m ≤ n then
        set lst to {}
        repeat with i from m to n
            set end of lst to i
        end repeat
        lst
    else
        {}
    end if
end enumFromTo

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

```
2178309
```


## Arendelle

```
( fibonacci , 1; 1 )

[ 98 , // 100 numbers of fibonacci

   ( fibonacci[ @fibonacci? ] ,

      @fibonacci[ @fibonacci - 1 ] + @fibonacci[ @fibonacci - 2 ]

   )

   "Index: | @fibonacci? | => | @fibonacci[ @fibonacci? - 1 ] |"
]
```


## ArkScript

Works with

:

ArkScript

version 3.x

Recursive solution:

```mw
(let fibo (fun (n)
  (if (< n 2)
    n
    (+ (fibo (- n 1)) (fibo (- n 2))))))

(assert (= 6765 (fibo 20)) "(fibo 20) == 6765")
```

Iterative solution:

```mw
(let fibo (fun (n) {
  (mut i 0)
  (mut a 0)
  (mut b 1)
  (while (< i n) {
    (let c (+ a b))
    (set a b)
    (set b c)
    (set i (+ 1 i)) })
  a }))

(assert (= 6765 (fibo 20)) "(fibo 20) == 6765")
```


## ARM Assembly

Expects to be called with ${\displaystyle n}$ in R0, and will return ${\displaystyle f(n)}$ in the same register.

```mw
fibonacci:
        push  {r1-r3}
        mov   r1,  #0
        mov   r2,  #1
        
fibloop:
        mov   r3,  r2
        add   r2,  r1,  r2
        mov   r1,  r3
        sub   r0,  r0,  #1
        cmp   r0,  #1
        bne   fibloop
        
        mov   r0,  r2
        pop   {r1-r3}
        mov   pc,  lr
```


## ArnoldC

```mw
IT'S SHOWTIME

HEY CHRISTMAS TREE f1
YOU SET US UP @I LIED
TALK TO THE HAND f1

HEY CHRISTMAS TREE f2
YOU SET US UP @NO PROBLEMO

HEY CHRISTMAS TREE f3
YOU SET US UP @I LIED

STICK AROUND @NO PROBLEMO

GET TO THE CHOPPER f3
HERE IS MY INVITATION f1
GET UP f2
ENOUGH TALK
TALK TO THE HAND f3

GET TO THE CHOPPER f1
HERE IS MY INVITATION f2
ENOUGH TALK

GET TO THE CHOPPER f2
HERE IS MY INVITATION f3
ENOUGH TALK

CHILL

YOU HAVE BEEN TERMINATED
```


## Arturo

### Recursive

```mw
fib: $[x][
   switch x<2 -> 1
            -> (fib x-1) + (fib x-2)
]

loop 1..25 [x][
   print ["Fibonacci of" x "=" fib x]
]
```

### Iterative

```mw
fib: function [n][
    if n < 2 -> return 1
    
    a: 1
    b: 1
    
    loop 2..n 'x [
        tmp: a + b
        a: b
        b: tmp
    ]
    
    return b
]

loop 1..25 'x [
    print ["Fibonacci of" x "=" fib x]
]
```

**Output:**

```
Fibonacci of 1 = 1 
Fibonacci of 2 = 2 
Fibonacci of 3 = 3 
Fibonacci of 4 = 5 
Fibonacci of 5 = 8 
Fibonacci of 6 = 13 
Fibonacci of 7 = 21 
Fibonacci of 8 = 34 
Fibonacci of 9 = 55 
Fibonacci of 10 = 89 
Fibonacci of 11 = 144 
Fibonacci of 12 = 233 
Fibonacci of 13 = 377 
Fibonacci of 14 = 610 
Fibonacci of 15 = 987 
Fibonacci of 16 = 1597 
Fibonacci of 17 = 2584 
Fibonacci of 18 = 4181 
Fibonacci of 19 = 6765 
Fibonacci of 20 = 10946 
Fibonacci of 21 = 17711 
Fibonacci of 22 = 28657 
Fibonacci of 23 = 46368 
Fibonacci of 24 = 75025 
Fibonacci of 25 = 121393
```


## AsciiDots

```mw
/--#$--\
|      |
>-*>{+}/
| \+-/
1  |
#  1
|  #
|  |
.  .
```


## ATS

### Recursive

```mw
fun fib_rec(n: int): int =
  if n >= 2 then fib_rec(n-1) + fib_rec(n-2) else n
```

### Iterative

```mw
(*
** This one is also referred to as being tail-recursive 
*)
fun
fib_trec(n: int): int =
if
n > 0
then (fix loop (i:int, r0:int, r1:int): int => if i > 1 then loop (i-1, r1, r0+r1) else r1)(n, 0, 1)
else 0
```

### Iterative and Verified

```mw
(*
** This implementation is verified!
*)

dataprop FIB (int, int) =
  | FIB0 (0, 0) | FIB1 (1, 1)
  | {n:nat} {r0,r1:int} FIB2 (n+2, r0+r1) of (FIB (n, r0), FIB (n+1, r1))
// end of [FIB] // end of [dataprop]

fun
fibats{n:nat}
  (n: int (n))
: [r:int] (FIB (n, r) | int r) = let
  fun loop
    {i:nat | i <= n}{r0,r1:int}
  (
    pf0: FIB (i, r0), pf1: FIB (i+1, r1)
  | ni: int (n-i), r0: int r0, r1: int r1
  ) : [r:int] (FIB (n, r) | int r) =
    if (ni > 0)
      then loop{i+1}(pf1, FIB2 (pf0, pf1) | ni - 1, r1, r0 + r1)
      else (pf0 | r0)
    // end of [if]
  // end of [loop]
in
  loop {0} (FIB0 (), FIB1 () | n, 0, 1)
end // end of [fibats]
```

### Matrix-based

```mw
(* ****** ****** *)
//
// How to compile:
// patscc -o fib fib.dats
//
(* ****** ****** *)
//
#include
"share/atspre_staload.hats"
//
(* ****** ****** *)
//
abst@ype
int3_t0ype =
  (int, int, int)
//
typedef int3 = int3_t0ype
//
(* ****** ****** *)

extern
fun int3 : (int, int, int) -<> int3
extern
fun int3_1 : int3 -<> int
extern
fun mul_int3_int3: (int3, int3) -<> int3

(* ****** ****** *)

local

assume
int3_t0ype = (int, int, int)

in (* in-of-local *)
//
implement
int3 (x, y, z) = @(x, y, z)
//
implement int3_1 (xyz) = xyz.1
//
implement
mul_int3_int3
(
  @(a,b,c), @(d,e,f)
) =
  (a*d + b*e, a*e + b*f, b*e + c*f)
//
end // end of [local]

(* ****** ****** *)
//
implement
gnumber_int<int3> (n) = int3(n, 0, n)
//
implement gmul_val<int3> = mul_int3_int3
//
(* ****** ****** *)
//
fun
fib (n: intGte(0)): int =
  int3_1(gpow_int_val<int3> (n, int3(1, 1, 0)))
//
(* ****** ****** *)

implement
main0 () =
{
//
val N = 10
val () = println! ("fib(", N, ") = ", fib(N))
val N = 20
val () = println! ("fib(", N, ") = ", fib(N))
val N = 30
val () = println! ("fib(", N, ") = ", fib(N))
val N = 40
val () = println! ("fib(", N, ") = ", fib(N))
//
} (* end of [main0] *)
```


## AutoHotkey

*Search autohotkey.com*: sequence

### Iterative

Translation of

:

C

```mw
Loop, 5
  MsgBox % fib(A_Index)
Return

fib(n)
{
  If (n < 2) 
    Return n
  i := last := this := 1
  While (i <= n)
  {
    new := last + this
    last := this
    this := new
    i++
  }
  Return this
}
```

### Recursive and iterative

Source: AutoHotkey forum by Laszlo

```mw
/*
Important note: the recursive version would be very slow
without a global or static array. The iterative version
handles also negative arguments properly.
*/

FibR(n) {       ; n-th Fibonacci number (n>=0, recursive with static array Fibo) 
   Static 
   Return n<2 ? n : Fibo%n% ? Fibo%n% : Fibo%n% := FibR(n-1)+FibR(n-2) 
} 

Fib(n) {        ; n-th Fibonacci number (n < 0 OK, iterative) 
   a := 0, b := 1 
   Loop % abs(n)-1 
      c := b, b += a, a := c 
   Return n=0 ? 0 : n>0 || n&1 ? b : -b 
}
```


## AutoIt

### Iterative

```mw
#AutoIt Version: 3.2.10.0
$n0 = 0
$n1 = 1
$n = 10
MsgBox (0,"Iterative Fibonacci ", it_febo($n0,$n1,$n))

Func it_febo($n_0,$n_1,$N)
   $first = $n_0
   $second = $n_1
   $next = $first + $second
   $febo = 0
   For $i = 1 To $N-3
      $first = $second
      $second = $next
      $next = $first + $second
   Next
   if $n==0 Then
      $febo = 0
   ElseIf $n==1 Then
      $febo = $n_0
   ElseIf $n==2 Then
      $febo = $n_1
   Else
      $febo = $next
   EndIf
   Return $febo
EndFunc
```

### Recursive

```mw
#AutoIt Version: 3.2.10.0
$n0 = 0
$n1 = 1
$n = 10
MsgBox (0,"Recursive Fibonacci ", rec_febo($n0,$n1,$n))
Func rec_febo($r_0,$r_1,$R)
   if  $R<3 Then
      if $R==2 Then
    Return $r_1
      ElseIf $R==1 Then
    Return $r_0
      ElseIf $R==0 Then
    Return 0
      EndIf
      Return $R
   Else
      Return rec_febo($r_0,$r_1,$R-1) + rec_febo($r_0,$r_1,$R-2)
   EndIf
EndFunc
```
