---
title: "Towers of Hanoi (part 1/5)"
source: https://rosettacode.org/wiki/Towers_of_Hanoi
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/5
---

# Towers of Hanoi

**Task**

Solve the   Towers of Hanoi   problem with recursion.


## 11l

Translation of

:

Python

```mw
F hanoi(ndisks, startPeg = 1, endPeg = 3) -> Void
   I ndisks
      hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
      print(‘Move disk #. from peg #. to peg #.’.format(ndisks, startPeg, endPeg))
      hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)

hanoi(ndisks' 3)
```

**Output:**

```
Move disk 1 from peg 1 to peg 3
Move disk 2 from peg 1 to peg 2
Move disk 1 from peg 3 to peg 2
Move disk 3 from peg 1 to peg 3
Move disk 1 from peg 2 to peg 1
Move disk 2 from peg 2 to peg 3
Move disk 1 from peg 1 to peg 3
```


## 360 Assembly

Translation of

:

PL/I

```mw
*        Towers of Hanoi           08/09/2015
HANOITOW CSECT
         USING  HANOITOW,R12       r12 : base register
         LR     R12,R15            establish base register
         ST     R14,SAVE14         save r14
BEGIN    LH     R2,=H'4'           n <===
         L      R3,=C'123 '        stating position
         BAL    R14,MOVE           r1=move(m,n)
RETURN   L      R14,SAVE14         restore r14
         BR     R14                return to caller
SAVE14   DS     F                  static save r14
PG       DC     CL44'xxxxxxxxxxxx Move disc from pole X to pole Y' 
NN       DC     F'0'
POLEX    DS     F                  current poles
POLEN    DS     F                  new poles
*        ....   recursive          subroutine move(n, poles)  [r2,r3]
MOVE     LR     R10,R11            save stackptr (r11) in r10 temp
         LA     R1,STACKLEN        amount of storage required
         GETMAIN RU,LV=(R1)        allocate storage for stack
         USING  STACKDS,R11        make storage addressable
         LR     R11,R1             establish stack addressability
         ST     R14,SAVE14M        save previous r14
         ST     R10,SAVE11M        save previous r11
         LR     R1,R5              restore saved argument r5
BEGINM   STM    R2,R3,STACK        push arguments to stack
         ST     R3,POLEX
         CH     R2,=H'1'           if n<>1
         BNE    RECURSE            then goto recurse
         L      R1,NN
         LA     R1,1(R1)           nn=nn+1
         ST     R1,NN
         XDECO  R1,PG              nn
         MVC    PG+33(1),POLEX+0   from
         MVC    PG+43(1),POLEX+1   to
         XPRNT  PG,44              print "move disk from to"
         B      RETURNM
RECURSE  L      R2,N               n
         BCTR   R2,0               n=n-1
         MVC    POLEN+0(1),POLES+0 from
         MVC    POLEN+1(1),POLES+2 via
         MVC    POLEN+2(1),POLES+1 to
         L      R3,POLEN           new poles
         BAL    R14,MOVE           call move(n-1,from,via,to)
         LA     R2,1               n=1
         MVC    POLEN,POLES 
         L      R3,POLEN           new poles
         BAL    R14,MOVE           call move(1,from,to,via)
         L      R2,N               n
         BCTR   R2,0               n=n-1
         MVC    POLEN+0(1),POLES+2 via
         MVC    POLEN+1(1),POLES+1 to
         MVC    POLEN+2(1),POLES+0 from
         L      R3,POLEN           new poles
         BAL    R14,MOVE           call move(n-1,via,to,from)
RETURNM  LM     R2,R3,STACK        pull arguments from stack
         LR     R1,R11             current stack
         L      R14,SAVE14M        restore r14
         L      R11,SAVE11M        restore r11
         LA     R0,STACKLEN        amount of storage to free
         FREEMAIN A=(R1),LV=(R0)   free allocated storage
         BR     R14                return to caller
         LTORG
         DROP   R12                base no longer needed
STACKDS  DSECT                     dynamic area
SAVE14M  DS     F                  saved r14
SAVE11M  DS     F                  saved r11
STACK    DS     0F                 stack
N        DS     F                  r2 n
POLES    DS     F                  r3 poles
STACKLEN EQU    *-STACKDS
         YREGS  
         END    HANOITOW
```

**Output:**

```
           1 Move disc from pole 1 to pole 3
           2 Move disc from pole 1 to pole 2
           3 Move disc from pole 3 to pole 2
           4 Move disc from pole 1 to pole 3
           5 Move disc from pole 2 to pole 1
           6 Move disc from pole 2 to pole 3
           7 Move disc from pole 1 to pole 3
           8 Move disc from pole 1 to pole 2
           9 Move disc from pole 3 to pole 2
          10 Move disc from pole 3 to pole 1
          11 Move disc from pole 2 to pole 1
          12 Move disc from pole 3 to pole 2
          13 Move disc from pole 1 to pole 3
          14 Move disc from pole 1 to pole 2
          15 Move disc from pole 3 to pole 2
```


## 6502 Assembly

Works with

:

Commodore

This should work on any Commodore 8-bit computer; just set `temp` to an appropriate zero-page location.

```mw
temp   = $FB   ; this works on a VIC-20 or C-64; adjust for other machines. Need two bytes zero-page space unused by the OS.

; kernal print-char routine
chrout  = $FFD2

; Main Towers of Hanoi routine. To call, load the accumulator with the number of disks to move,
; the X register with the source peg (1-3), and the Y register with the target peg.

hanoi:   cmp #$00       ; do nothing if the number of disks to move is zero
         bne nonzero
         rts

nonzero: pha            ; save registers on stack
         txa
         pha
         tya
         pha
         pha            ; and make room for the spare peg number

         ; Parameters are now on the stack at these offsets:
         count  = $0104
         source = $0103
         target = $0102
         spare  = $0101

         ; compute spare rod number (6 - source - dest)
         tsx
         lda #6
         sec
         sbc source, x
         sec
         sbc target, x
         sta spare, x

         ; prepare for first recursive call
         tay                ; target is the spare peg

         tsx
         lda source, x      ; source is the same
         sta temp           ; we're using X to access the stack, so save its value here for now

         lda count, x       ; move count - 1 disks
         sec
         sbc #1
         ldx temp           ; now load X for call 

         ; and recurse
         jsr hanoi

         ; restore X and Y for print call
         tsx
         ldy target, x
         lda source, x
         tax

         ; print instructions to move the last disk
         jsr print_move

         ; prepare for final recursive call
         tsx
         lda spare, x    ; source is now spare
         sta temp
         lda target, x   ; going to the original target
         tay            
         lda count, x    ; and again moving count-1 disks
         sec         
         sbc #1
         ldx temp
         jsr hanoi

         ; pop our stack frame, restore registers, and return
         pla
         pla
         tay
         pla
         tax
         pla
         rts

; constants for printing
prelude:   .asciiz "MOVE DISK FROM "
interlude: .asciiz " TO "
postlude:  .byte 13,0

; print instructions: move disk from (X) to (Y)
print_move:
         pha
         txa
         pha
         tya
         pha

         ; Parameters are now on the stack at these offsets:
         from   = $0102
           to   = $0101

         lda #<prelude
         ldx #>prelude
         jsr print_string
         tsx
         lda from,x
         clc
         adc #$30
         jsr chrout
         lda #<interlude
         ldx #>interlude
         jsr print_string
         tsx
         lda to,x
         clc
         adc #$30
         jsr chrout
         lda #<postlude
         ldx #>postlude
         jsr print_string
         pla
         tay
         pla
         tax
         pla
         rts

; utility routine: print null-terminated string at address AX
print_string:
         sta temp
         stx temp+1
         ldy #0
loop:    lda (temp),y
         beq done_print
         jsr chrout
         iny
         bne loop
done_print:
         rts
```

**Output:**

```
MOVE DISK FROM 1 TO 2
MOVE DISK FROM 1 TO 3
MOVE DISK FROM 2 TO 3
MOVE DISK FROM 1 TO 2
MOVE DISK FROM 3 TO 1
MOVE DISK FROM 3 TO 2
MOVE DISK FROM 1 TO 2
MOVE DISK FROM 1 TO 3
MOVE DISK FROM 2 TO 3
MOVE DISK FROM 2 TO 1
MOVE DISK FROM 3 TO 1
MOVE DISK FROM 2 TO 3
MOVE DISK FROM 1 TO 2
MOVE DISK FROM 1 TO 3
MOVE DISK FROM 2 TO 3
```


## 8080 Assembly

```mw
	org	100h
	lhld	6	; Top of CP/M usable memory
	sphl		; Put the stack there
	lxi	b,0401h	; Set up first arguments to move()
	lxi	d,0203h
	call	move	; move(4, 1, 2, 3)
	rst	0	; quit program
	;;;	Move B disks from C via D to E. 
move:	dcr	b	; One fewer disk in next iteration
	jz	mvout	; If this was the last disk, print move and stop
	push	b	; Otherwise, save registers,
	push	d 
	mov	a,d	; First recursive call
	mov	d,e
	mov	e,a
	call	move	; move(B-1, C, E, D)
	pop	d	; Restore registers
	pop	b
	call	mvout	; Print current move
	mov	a,c	; Second recursive call
	mov	c,d
	mov	d,a
	jmp	move	; move(B-1, D, C, E) - tail call optimization
	;;;	Print move, saving registers.
mvout:	push	b	; Save registers on stack
	push	d
	mov	a,c	; Store 'from' as ASCII digit in 'from' space
	adi	'0'
	sta	out1
	mov	a,e	; Store 'to' as ASCII digit in 'to' space
	adi	'0'
	sta	out2
	lxi	d,outstr
	mvi	c,9	; CP/M call to print the string
	call	5
	pop	d	; Restore register contents
	pop	b
	ret
	;;;	Move output with placeholder for pole numbers
outstr:	db	'Move disk from pole '
out1:	db	'* to pole '
out2:	db	'*',13,10,'$'
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## 8086 Assembly

```mw
	cpu	8086
	bits	16
	org	100h
section	.text
	mov	bx,0402h	; Set up first arguments to move()
	mov	cx,0103h	; Registers chosen s.t. CX contains output
	;;;	Move BH disks from CH via BL to CL
move:	dec	bh		; One fewer disk in next iteration
	jz	.out		; If this was last disk, just print move
	push	bx		; Save the registers for a recursive call
	push	cx
	xchg	bl,cl		; Swap the 'to' and 'via' registers
	call	move		; move(BH, CH, CL, BL)
	pop	cx		; Restore the registers from the stack
	pop	bx
	call	.out		; Print the move
	xchg	ch,bl		; Swap the 'from' and 'via' registers
	jmp	move		; move(BH, BL, CH, CL)
	;;;	Print the move
.out:	mov	ax,'00'		; Add ASCII 0 to both 'from' and 'to'
	add	ax,cx		; in one 16-bit operation
	mov	[out1],ah	; Store 'from' field in output
	mov	[out2],al	; Store 'to' field in output
	mov	dx,outstr	; MS-DOS system call to print string
	mov	ah,9
	int	21h
	ret
section	.data
outstr:	db	'Move disk from pole '
out1:	db	'* to pole '
out2:	db	'*',13,10,'$'
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## 8th

```mw
5 var, disks
var sa
var sb
var sc

: save sc ! sb ! sa ! disks ! ;
: get sa @ sb @ sc @ ;
: get2 get swap ;
: hanoi
	save disks @ not if ;; then
	disks @ get
	disks @ n:1- get2 hanoi save
	cr 
	" move a ring from " .  sa @ . " to " . sb @ .
	disks @ n:1- get2 rot hanoi
;

" Tower of Hanoi, with " . disks @ . " rings: " . 
disks @ 1 2 3 hanoi cr bye
```


## ABC

```mw
HOW TO MOVE n DISKS FROM src VIA via TO dest:
    IF n>0:
        MOVE n-1 DISKS FROM src VIA dest TO via
        WRITE "Move disk from pole", src, "to pole", dest/
        MOVE n-1 DISKS FROM via VIA dest TO src

MOVE 4 DISKS FROM 1 VIA 2 TO 3
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 3
```


## Action!

Translation of

:

Tiny BASIC

...via PL/M

```mw
;;; Iterative Towers of Hanoi; translated from Tiny BASIC via PL/M
;;;

DEFINE NUMBER_OF_DISCS = "4"

PROC Main()

  INT d, n, x

  n = 1
  FOR d = 1 TO NUMBER_OF_DISCS DO
    n = n + n
  OD
  FOR x = 1 TO n - 1 DO
    ; as with Algol W, PL/M, Action! has bit and MOD operators
    Print( "Move disc on peg " )
    Put( '1 + (   ( x AND ( x - 1 ) )       MOD 3 ) )
    Print( " to peg " )
    Put( '1 + ( ( ( x OR  ( x - 1 ) ) + 1 ) MOD 3 ) )
    PutE()
  OD
RETURN
```

**Output:**

```
Move disc on peg 1 to peg 3
Move disc on peg 1 to peg 2
Move disc on peg 3 to peg 2
Move disc on peg 1 to peg 3
Move disc on peg 2 to peg 1
Move disc on peg 2 to peg 3
Move disc on peg 1 to peg 3
Move disc on peg 1 to peg 2
Move disc on peg 3 to peg 2
Move disc on peg 3 to peg 1
Move disc on peg 2 to peg 1
Move disc on peg 3 to peg 2
Move disc on peg 1 to peg 3
Move disc on peg 1 to peg 2
Move disc on peg 3 to peg 2
```


## ActionScript

```mw
public function move(n:int, from:int, to:int, via:int):void
{
    if (n > 0)
    {
        move(n - 1, from, via, to);
        trace("Move disk from pole " + from + " to pole " + to);
        move(n - 1, via, to, from);
    }
}
```


## Ada

```mw
with Ada.Text_Io; use Ada.Text_Io;

procedure Towers is
   type Pegs is (Left, Center, Right);
   procedure Hanoi (Ndisks : Natural; Start_Peg : Pegs := Left; End_Peg : Pegs := Right; Via_Peg : Pegs := Center) is
   begin
      if Ndisks > 0 then
         Hanoi(Ndisks - 1, Start_Peg, Via_Peg, End_Peg);
         Put_Line("Move disk" & Natural'Image(Ndisks) & " from " & Pegs'Image(Start_Peg) & " to " & Pegs'Image(End_Peg));
         Hanoi(Ndisks - 1, Via_Peg, End_Peg, Start_Peg);
      end if;
   end Hanoi;
begin
   Hanoi(4);
end Towers;
```


## Agena

```mw
move := proc(n::number, src::number, dst::number, via::number) is
   if n > 0 then
      move(n - 1, src, via, dst)
      print(src & ' to ' & dst)
      move(n - 1, via, dst, src)
   fi
end

move(4, 1, 2, 3)
```


## ALGOL 60

```mw
begin
  procedure movedisk(n, f, t);
  integer n, f, t;
  begin
    outstring (1, "Move disk from");
    outinteger(1, f);
    outstring (1, "to");
    outinteger(1, t);
    outstring (1, "\n");
  end;

  procedure dohanoi(n, f, t, u);
  integer n, f, t, u;
  begin
    if n < 2 then
      movedisk(1, f, t)
    else
      begin
        dohanoi(n - 1, f, u, t);
        movedisk(1, f, t);
        dohanoi(n - 1, u, t, f);
      end;
  end;

  dohanoi(4, 1, 2, 3);
  outstring(1,"Towers of Hanoi puzzle completed!")
end
```

**Output:**

```
Move disk from 1 to 3 
Move disk from 1 to 2 
Move disk from 3 to 2 
Move disk from 1 to 3 
Move disk from 2 to 1 
Move disk from 2 to 3 
Move disk from 1 to 3 
Move disk from 1 to 2 
Move disk from 3 to 2 
Move disk from 3 to 1 
Move disk from 2 to 1 
Move disk from 3 to 2 
Move disk from 1 to 3 
Move disk from 1 to 2 
Move disk from 3 to 2 
Towers of Hanoi puzzle completed!
```


## ALGOL 68

```mw
PROC move = (INT n, from, to, via) VOID:
  IF n > 0 THEN
    move(n - 1, from, via, to);
    printf(($"Move disk from pole "g" to pole "gl$, from, to));
    move(n - 1, via, to, from)
  FI
;

main: (
  move(4, 1,2,3)
)
```

COMMENT Disk number is also printed in this code (works with a68g): COMMENT

```mw
PROC move = (INT n, from, to, via) VOID:
  IF n > 0 THEN
    move(n - 1, from, via, to);
    printf(($"Move disk "g"     from pole "g"     to pole "gl$, n,  from, to));
    move(n - 1, via, to, from)
  FI ;
main: (
  move(4, 1,2,3)
)
```


## ALGOL-M

```mw
begin
procedure move(n, src, via, dest);
integer n;
string(1) src, via, dest;
begin
    if n > 0 then
    begin
        move(n-1, src, dest, via);
        write("Move disk from pole ");
        writeon(src);
        writeon(" to pole ");
        writeon(dest);
        move(n-1, via, src, dest);
    end;
end;

move(4, "1", "2", "3");
end
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## ALGOL W

### Recursive

Following Agena, Algol 68, AmigaE...

```mw
begin
    procedure move ( integer value n, from, to, via ) ;
        if n > 0 then begin
            move( n - 1, from, via, to );
            write( i_w := 1, s_w := 0, "Move disk from peg: ", from, " to peg: ", to );
            move( n - 1, via, to, from )
        end move ;
 
    move( 4, 1, 2, 3 )
end.
```

### Iterative

Translation of

:

Tiny BASIC

```mw
begin % iterative towers of hanoi - translated from Tiny Basic %
    integer d, n;
    while begin writeon( "How many disks? " );
                read( d );
                d < 1 or d > 10
          end
    do begin end;
    n := 1;
    while d not = 0 do begin
        d := d - 1;
        n := 2 * n
    end;
    for x := 1 until n - 1 do begin
        integer s, t;
        % Algol W has the necessary bit and modulo operators so these are used here %
        %         instead of implementing them via subroutines                      %
        s :=   number( bitstring( x ) and bitstring( x - 1 ) )       rem 3;
        t := ( number( bitstring( x ) or  bitstring( x - 1 ) ) + 1 ) rem 3;
        write( i_w := 1, s_w := 0, "Move disc on peg ", s + 1, " to peg ", t + 1 )
    end
end.
```


## AmigaE

```mw
PROC move(n, from, to, via)
  IF n > 0
    move(n-1, from, via, to)
    WriteF('Move disk from pole \d to pole \d\n', from, to)
    move(n-1, via, to, from)
  ENDIF
ENDPROC

PROC main()
  move(4, 1,2,3)
ENDPROC
```


## Amazing Hopper

```mw
#include <hopper.h>
#proto hanoi(_X_,_Y_,_Z_,_W_)
main:
   get arg number (2,discos)
   {discos}!neg? do{fail=0,mov(fail),{"I need a positive (or zero) number here, not: ",fail}println,exit(0)}
   pos? do{
      _hanoi( discos, "A", "B", "C" )
   }
exit(0)
.locals
hanoi(discos,inicio,aux,fin)
   iif( {discos}eqto(1), {inicio, "->", fin, "\n"};print,  _hanoi({discos}minus(1), inicio,fin,aux);\
                                                           {inicio, "->", fin, "\n"};print;\
                                                           _hanoi({discos}minus(1), aux, inicio, fin))
back
```

**Output:**

```
For 4 discs:
A->B
A->C
B->C
A->B
C->A
C->B
A->B
A->C
B->C
B->A
C->A
B->C
A->B
A->C
B->C
```


## APL

Works with

:

Dyalog APL

```mw
hanoi←{
    move←{
        n from to via←⍵
        n≤0:⍬
        l←∇(n-1) from via to
        r←∇(n-1) via to from
        l,(⊂from to),r
    }
    '⊂Move disk from pole ⊃,I1,⊂ to pole ⊃,I1'⎕FMT↑move ⍵
}
```

**Output:**

```
      hanoi 4 1 2 3
Move disk from pole 1 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 2
```


## AppleScript

```mw
--------------------- TOWERS OF HANOI --------------------

-- hanoi :: Int -> (String, String, String) -> [(String, String)]
on hanoi(n, abc)
    script go
        on |λ|(n, {x, y, z})
            if n > 0 then
                set m to n - 1
                
                |λ|(m, {x, z, y}) & ¬
                    {{x, y}} & |λ|(m, {z, y, x})
            else
                {}
            end if
        end |λ|
    end script
    
    go's |λ|(n, abc)
end hanoi

--------------------------- TEST -------------------------
on run
    unlines(map(intercalate(" -> "), ¬
        hanoi(3, {"left", "right", "mid"})))
end run

-------------------- GENERIC FUNCTIONS -------------------

-- intercalate :: String -> [String] -> String
on intercalate(delim)
    script
        on |λ|(xs)
            set {dlm, my text item delimiters} to ¬
                {my text item delimiters, delim}
            set s to xs as text
            set my text item delimiters to dlm
            s
        end |λ|
    end script
end intercalate

-- Lift 2nd class handler function into 1st class script wrapper 
-- mReturn :: First-class m => (a -> b) -> m (a -> b)
on mReturn(f)
    if class of f is script then
        f
    else
        script
            property |λ| : f
        end script
    end if
end mReturn

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

-- unlines :: [String] -> String
on unlines(xs)
    set {dlm, my text item delimiters} to ¬
        {my text item delimiters, linefeed}
    set str to xs as text
    set my text item delimiters to dlm
    str
end unlines
```

**Output:**

```
left -> right
left -> mid
right -> mid
left -> right
mid -> left
mid -> right
left -> right
```

More illustratively:

*(I've now eliminated the recursive*|move|()*handler's tail calls. So it's now only called 2 ^ (n - 1) times as opposed to 2 ^ (n + 1) - 1 with full recursion. The maximum call depth of n is only reached once, whereas with full recursion, the maximum depth was n + 1 and this was reached 2 ^ n times.)*

```mw
on hanoi(n, source, target)
    set t1 to tab & "tower 1: " & tab
    set t2 to tab & "tower 2: " & tab
    set t3 to tab & "tower 3: " & tab
    
    script o
        property m : 0
        property tower1 : {}
        property tower2 : {}
        property tower3 : {}
        property towerRefs : {a reference to tower1, a reference to tower2, a reference to tower3}
        property process : missing value
        
        on |move|(n, source, target)
            set aux to 6 - source - target
            repeat with n from n to 2 by -1 -- Tail call elimination repeat.
                |move|(n - 1, source, aux)
                set end of item target of my towerRefs to n
                tell item source of my towerRefs to set its contents to reverse of rest of its reverse
                set m to m + 1
                set end of my process to ¬
                    {(m as text) & ". move disc " & n & (" from tower " & source) & (" to tower " & target & ":"), ¬
                        t1 & tower1, ¬
                        t2 & tower2, ¬
                        t3 & tower3}
                tell source
                    set source to aux
                    set aux to it
                end tell
            end repeat
            -- Specific code for n = 1:
            set end of item target of my towerRefs to 1
            tell item source of my towerRefs to set its contents to reverse of rest of its reverse
            set m to m + 1
            set end of my process to ¬
                {(m as text) & ". move disc 1 from tower " & source & (" to tower " & target & ":"), ¬
                    t1 & tower1, ¬
                    t2 & tower2, ¬
                    t3 & tower3}
        end |move|
    end script
    
    repeat with i from n to 1 by -1
        set end of item source of o's towerRefs to i
    end repeat
    
    set astid to AppleScript's text item delimiters
    set AppleScript's text item delimiters to ", "
    set o's process to {"Starting with " & n & (" discs on tower " & (source & ":")), ¬
        t1 & o's tower1, t2 & o's tower2, t3 & o's tower3}
    if (n > 0) then tell o to |move|(n, source, target)
    set end of o's process to "That's it!"
    set AppleScript's text item delimiters to linefeed
    set process to o's process as text
    set AppleScript's text item delimiters to astid
    
    return process
end hanoi

-- Test:
set numberOfDiscs to 3
set sourceTower to 1
set destinationTower to 2
hanoi(numberOfDiscs, sourceTower, destinationTower)
```

**Output:**

```
"Starting with 3 discs on tower 1:
    tower 1:     3, 2, 1
    tower 2:     
    tower 3:     
1. move disc 1 from tower 1 to tower 2:
    tower 1:     3, 2
    tower 2:     1
    tower 3:     
2. move disc 2 from tower 1 to tower 3:
    tower 1:     3
    tower 2:     1
    tower 3:     2
3. move disc 1 from tower 2 to tower 3:
    tower 1:     3
    tower 2:     
    tower 3:     2, 1
4. move disc 3 from tower 1 to tower 2:
    tower 1:     
    tower 2:     3
    tower 3:     2, 1
5. move disc 1 from tower 3 to tower 1:
    tower 1:     1
    tower 2:     3
    tower 3:     2
6. move disc 2 from tower 3 to tower 2:
    tower 1:     1
    tower 2:     3, 2
    tower 3:     
7. move disc 1 from tower 1 to tower 2:
    tower 1:     
    tower 2:     3, 2, 1
    tower 3:     
That's it!"
```


## ARM Assembly

```mw
.text
.global	_start
_start:	mov	r0,#4		@ 4 disks,
	mov	r1,#1		@ from pole 1,
	mov	r2,#2		@ via pole 2,
	mov	r3,#3		@ to pole 3.
	bl	move
	mov	r0,#0		@ Exit to Linux afterwards
	mov	r7,#1
	swi	#0
	@@@	Move r0 disks from r1 via r2 to r3
move:	subs	r0,r0,#1	@ One fewer disk in next iteration
	beq	show		@ If last disk, just print move
	push	{r0-r3,lr}	@ Save all the registers incl. link register
	eor	r2,r2,r3	@ Swap the 'to' and 'via' registers
	eor	r3,r2,r3
	eor	r2,r2,r3
	bl	move		@ Recursive call
	pop	{r0-r3}		@ Restore all the registers except LR
	bl	show		@ Show current move
	eor	r1,r1,r3	@ Swap the 'to' and 'via' registers
	eor	r3,r1,r3
	eor	r1,r1,r3
	pop	{lr}		@ Restore link register
	b	move		@ Tail call
	@@@	Show move
show:	push	{r0-r3,lr}	@ Save all the registers
	add	r1,r1,#'0	@ Write the source pole
	ldr	lr,=spole
	strb	r1,[lr] 
	add	r3,r3,#'0	@ Write the destination pole
	ldr	lr,=dpole
	strb	r3,[lr]
	mov	r0,#1		@ 1 = stdout
	ldr	r1,=moves	@ Pointer to string
	ldr	r2,=mlen	@ Length of string
	mov	r7,#4		@ 4 = Linux write syscall
	swi	#0 		@ Print the move
	pop	{r0-r3,pc}	@ Restore all the registers and return
.data
moves:	.ascii	"Move disk from pole "
spole:	.ascii	"* to pole "
dpole:	.ascii	"*\n"
mlen	=	. - moves
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 3 to pole 1
Move disk from pole 1 to pole 2
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 2 to pole 3
Move disk from pole 3 to pole 1
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 3 to pole 1
```


## Arturo

Translation of

:

D

```mw
hanoi: function [n f dir via][
	if n>0 [
		hanoi n-1 f via dir
		print ["Move disk" n "from" f "to" dir]
		hanoi n-1 via dir f
	]
]
 
hanoi 3 'L 'M 'R
```

**Output:**

```
Move disk 1 from L to M 
Move disk 2 from L to R 
Move disk 1 from M to R 
Move disk 3 from L to M 
Move disk 1 from R to L 
Move disk 2 from R to M 
Move disk 1 from L to M
```


## Asymptote

```mw
void hanoi(int n, string origen, string auxiliar, string destino) {
  if (n == 1) {
    write("Move disk 1 from " + origen + " to " + destino);
  } else {
    hanoi(n - 1, origen, destino, auxiliar);
    write("Move disk " + string(n) + " from " + origen + " to " + destino);
    hanoi(n - 1, auxiliar, origen, destino);
  }
}

hanoi(3, "pole 1", "pole 2", "pole 3");
write("Towers of Hanoi puzzle completed!");
```

**Output:**

```
Move disk 1 from pole 1 to pole 3
Move disk 2 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 2
Move disk 3 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 1
Move disk 2 from pole 2 to pole 3
Move disk 1 from pole 1 to pole 3
Towers of Hanoi puzzle completed!
```


## AutoHotkey

```mw
move(n, from, to, via)  ;n = # of disks, from = start pole, to = end pole, via = remaining pole 
{
  if (n = 1)
  {
    msgbox , Move disk from pole %from% to pole %to% 
  }
  else
  {
    move(n-1, from, via, to)
    move(1, from, to, via)
    move(n-1, via, to, from)
  }
}
move(64, 1, 3, 2)
```


## AutoIt

```mw
Func move($n, $from, $to, $via)
	If ($n = 1) Then
		ConsoleWrite(StringFormat("Move disk from pole "&$from&" To pole "&$to&"\n"))
	Else
		move($n - 1, $from, $via, $to)
		move(1, $from, $to, $via)
		move($n - 1, $via, $to, $from)
	EndIf
EndFunc

move(4, 1,2,3)
```


## AWK

Translation of

:

Logo

```mw
$ awk 'func hanoi(n,f,t,v){if(n>0){hanoi(n-1,f,v,t);print(f,"->",t);hanoi(n-1,v,t,f)}}
BEGIN{hanoi(4,"left","middle","right")}'
```

**Output:**

```
left -> right
left -> middle
right -> middle
left -> right
middle -> left
middle -> right
left -> right
left -> middle
right -> middle
right -> left
middle -> left
right -> middle
left -> right
left -> middle
right -> middle
```


## Ballerina

Translation of

:

Wren

```mw
import ballerina/io;

class Hanoi {
    private int moves;

    function init(int disks) {
        self.moves = 0;
        io:println("Towers of Hanoi with ", disks, " disks:\n");
        self.move(disks, "L", "C", "R");
        io:println("\nCompleted in ", self.moves, " moves\n");
    }

    private function move(int n, string frm, string to, string via) {
        if n > 0 {
            self.move(n - 1, frm, via, to);
            self.moves += 1;
            io:println("Move disk ", n, " from ", frm, " to ", to);
            self.move(n - 1, via, to, frm);
        }
    }
}

public function main() {
    _ = new Hanoi(3);
    _ = new Hanoi(4);
}
```

**Output:**

```
Towers of Hanoi with 3 disks:

Move disk 1 from L to C
Move disk 2 from L to R
Move disk 1 from C to R
Move disk 3 from L to C
Move disk 1 from R to L
Move disk 2 from R to C
Move disk 1 from L to C

Completed in 7 moves

Towers of Hanoi with 4 disks:

Move disk 1 from L to R
Move disk 2 from L to C
Move disk 1 from R to C
Move disk 3 from L to R
Move disk 1 from C to L
Move disk 2 from C to R
Move disk 1 from L to R
Move disk 4 from L to C
Move disk 1 from R to C
Move disk 2 from R to L
Move disk 1 from C to L
Move disk 3 from R to C
Move disk 1 from L to R
Move disk 2 from L to C
Move disk 1 from R to C

Completed in 15 moves
```


## BASIC

### Using a Subroutine

Works with

:

FreeBASIC

Works with

:

RapidQ

```mw
SUB move (n AS Integer, fromPeg AS Integer, toPeg AS Integer, viaPeg AS Integer)
    IF n>0 THEN
        move n-1, fromPeg, viaPeg, toPeg
        PRINT "Move disk from "; fromPeg; " to "; toPeg
        move n-1, viaPeg, toPeg, fromPeg
    END IF
END SUB

move 4,1,2,3
```

### Using `GOSUB`s

Here's an example of implementing recursion in an old BASIC that only has global variables:

Works with

:

Chipmunk Basic

Works with

:

Commodore BASIC

Works with

:

GW-BASIC

Works with

:

Locomotive Basic

Works with

:

MSX_BASIC

```mw
10 DEPTH=4: REM SHOULD EQUAL NUMBER OF DISKS
20 DIM N(DEPTH), F(DEPTH), T(DEPTH), V(DEPTH): REM STACK PER PARAMETER
30 SP = 0:    REM STACK POINTER
40 N(SP) = 4: REM START WITH 4 DISCS
50 F(SP) = 1: REM ON PEG 1
60 T(SP) = 2: REM MOVE TO PEG 2
70 V(SP) = 3: REM VIA PEG 3
80 GOSUB 100
90 END
99 REM MOVE SUBROUTINE 
100 IF N(SP) = 0 THEN RETURN
110 OS = SP:           REM STORE STACK POINTER
120 SP = SP + 1:       REM INCREMENT STACK POINTER
130 N(SP) = N(OS) - 1: REM MOVE N-1 DISCS
140 F(SP) = F(OS)    : REM FROM START PEG
150 T(SP) = V(OS)    : REM TO VIA PEG
160 V(SP) = T(OS)    : REM VIA TO PEG
170 GOSUB 100
180 OS = SP - 1: REM OS WILL HAVE CHANGED
190 PRINT "MOVE DISC FROM"; F(OS); "TO"; T(OS)
200 N(SP) = N(OS) - 1: REM MOVE N-1 DISCS
210 F(SP) = V(OS)    : REM FROM VIA PEG
220 T(SP) = T(OS)    : REM TO DEST PEG
230 V(SP) = F(OS)    : REM VIA FROM PEG
240 GOSUB 100
250 SP = SP - 1      : REM RESTORE STACK POINTER FOR CALLER
260 RETURN
```

### Using binary method

Works with

:

Chipmunk Basic

Works with

:

Commodore BASIC

Very fast version in BASIC V2 on Commodore C-64

Works with

:

Locomotive Basic

Works with

:

MSX_BASIC

```mw
   10 DEF FNM3(X)=X-INT(X/3)*3:REM MODULO 3
   20 N=4:GOSUB 100
   30 END
   99 REM HANOI
  100 :FOR M=1 TO 2^N-1
  110 ::PRINT MID$(STR$(M),2);":",FNM3(M AND M-1)+1;"TO";FNM3((M OR M-1)+1)+1
  130 :NEXT M
  140 RETURN
```

**Output:**

```
1:     1 TO 3 
2:     1 TO 2 
3:     3 TO 2 
4:     1 TO 3 
5:     2 TO 1 
6:     2 TO 3 
7:     1 TO 3 
8:     1 TO 2 
9:     3 TO 2 
10:    3 TO 1 
11:    2 TO 1 
12:    3 TO 2 
13:    1 TO 3 
14:    1 TO 2 
15:    3 TO 2 
```

### Applesoft BASIC

This is a binary solution. A subroutine handles bit-wise AND or OR as these Applesoft keywords work logically not bit-wise.

```mw
 100  DATA4,":  "," TO "
 110  DEF  FN M(X) = X -  INT (X / 3) * 3 + 1
 120  READ N,T$(0),T$(1)
 130  LET M$(1) =  CHR$ (13)
 140  FOR M = 1 TO 2 ^ N - 1
 150      FOR O = 0 TO 1
 160          GOSUB 200"ANDOR
 170          PRINT  MID$ ( STR$ (M),1,( NOT O) * 255)T$(O) FN M(R + O)M$(O);
 180  NEXT O,M
 190  END

 REM BITWISE M WITH M-1, RESULT IN R
 REM    AND WHEN O = 0
 REM     OR WHEN NOT O
 200  LET R = 0
 210  LET B1 = M
 220  LET B2 = M - 1
 230  FOR I = 0 TO 1E9
 240      LET M1 = B1 -  INT (B1 / 2) * 2
 250      LET M2 = B2 -  INT (B2 / 2) * 2
 260      LET MR = M1 AND M2
 270      IF O THEN MR = M1 OR M2
 280      LET R = R + MR * (2 ^ I)
 290      LET B1 =  INT (B1 / 2)
 300      LET B2 =  INT (B2 / 2)
 310      IF B1 OR B2 THEN  NEXT I
 320  RETURN
```

**Output:**

```
1:  1 TO 3
2:  1 TO 2
3:  3 TO 2
4:  1 TO 3
5:  2 TO 1
6:  2 TO 3
7:  1 TO 3
8:  1 TO 2
9:  3 TO 2
10:  3 TO 1
11:  2 TO 1
12:  3 TO 2
13:  1 TO 3
14:  1 TO 2
15:  3 TO 2
```

### BASIC256

```mw
call move(4,1,2,3)
print "Towers of Hanoi puzzle completed!"
end

subroutine move (n, fromPeg, toPeg, viaPeg)
    if n>0 then
        call move(n-1, fromPeg, viaPeg, toPeg)
        print "Move disk from "+fromPeg+" to "+toPeg
        call move(n-1, viaPeg, toPeg, fromPeg)
    end if
end subroutine
```

**Output:**

```
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 2 to 1
Move disk from 2 to 3
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 3 to 1
Move disk from 2 to 1
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Towers of Hanoi puzzle completed!
```

### BazzBasic

```mw
' ============================================
' https://rosettacode.org/wiki/Towers_of_Hanoi
' BazzBasic: https://github.com/EkBass/BazzBasic
' ============================================

' Recursive solution: move n disks from peg 'from' to peg 'to'
' using peg 'via' as auxiliary.
' Return value is unused — all output is produced as a side effect.

DEF FN Hanoi$(n$, from$, to$, via$)
    LET r$
    IF n$ = 1 THEN
        PRINT "Move disk 1 from peg " + from$ + " to peg " + to$
        RETURN ""
    END IF
    r$ = FN Hanoi$(n$ - 1, from$, via$, to$)
    PRINT "Move disk " + STR(INT(n$)) + " from peg " + from$ + " to peg " + to$
    r$ = FN Hanoi$(n$ - 1, via$, to$, from$)
    RETURN ""
END DEF

[inits]
    LET DISKS# = 4
    LET result$

[main]
    result$ = FN Hanoi$(DISKS#, "A", "C", "B")
END

' Output (4 disks, 15 moves):
' Move disk 1 from peg A to peg C
' Move disk 2 from peg A to peg B
' Move disk 1 from peg C to peg B
' Move disk 3 from peg A to peg C
' Move disk 1 from peg B to peg A
' Move disk 2 from peg B to peg C
' Move disk 1 from peg A to peg C
' Move disk 4 from peg A to peg B
' Move disk 1 from peg C to peg B
' Move disk 2 from peg C to peg A
' Move disk 1 from peg B to peg A
' Move disk 3 from peg C to peg B
' Move disk 1 from peg A to peg C
' Move disk 2 from peg A to peg B
' Move disk 1 from peg C to peg B
```

### IS-BASIC

```mw
100 PROGRAM "Hanoi.bas"
110 CALL HANOI(4,1,3,2)
120 DEF HANOI(DISK,FRO,TO,WITH)
130   IF DISK>0 THEN
140     CALL HANOI(DISK-1,FRO,WITH,TO)
150     PRINT "Move disk";DISK;"from";FRO;"to";TO
160     CALL HANOI(DISK-1,WITH,TO,FRO)
170   END IF
180 END DEF
```

### Quite BASIC

Translation of

:

BASIC

```mw
100 CLS
120 LET D = 4   : REM SHOULD EQUAL NUMBER OF DISKS
130 ARRAY N: ARRAY F: ARRAY T: ARRAY V: REM STACK PER PARAMETER
140 LET S = 0   : REM STACK POINTER
150 LET N(S) = 4: REM START WITH 4 DISCS
160 LET F(S) = 1: REM ON PEG 1
170 LET T(S) = 2: REM MOVE TO PEG 2
180 LET V(S) = 3: REM VIA PEG 3
190 GOSUB 220
200 END
210 REM MOVE SUBROUTINE 
220 IF N(S) = 0 THEN RETURN
230 LET O = S          : REM STORE STACK POINTER
240 LET S = S + 1      : REM INCREMENT STACK POINTER
250 LET N(S) = N(O) - 1: REM MOVE N-1 DISCS
260 LET F(S) = F(O)    : REM FROM START PEG
270 LET T(S) = V(O)    : REM TO VIA PEG
280 LET V(S) = T(O)    : REM VIA TO PEG
290 GOSUB 220
300 LET O = S - 1      : REM O WILL HAVE CHANGED
310 PRINT "MOVE DISC FROM "; F(O); " TO "; T(O)
320 LET N(S) = N(O) - 1: REM MOVE N-1 DISCS
330 LET F(S) = V(O)    : REM FROM VIA PEG
340 LET T(S) = T(O)    : REM TO DEST PEG
350 LET V(S) = F(O)    : REM VIA FROM PEG
360 GOSUB 220
370 LET S = S - 1      : REM RESTORE STACK POINTER FOR CALLER
380 RETURN
390 END
```

**Output:**

```
MOVE DISC FROM 1 TO 3
MOVE DISC FROM 1 TO 2
MOVE DISC FROM 3 TO 2
MOVE DISC FROM 1 TO 3
MOVE DISC FROM 2 TO 1
MOVE DISC FROM 2 TO 3
MOVE DISC FROM 1 TO 3
MOVE DISC FROM 1 TO 2
MOVE DISC FROM 3 TO 2
MOVE DISC FROM 3 TO 1
MOVE DISC FROM 2 TO 1
MOVE DISC FROM 3 TO 2
MOVE DISC FROM 1 TO 3
MOVE DISC FROM 1 TO 2
MOVE DISC FROM 3 TO 2
```


## Batch File

```mw
@echo off
setlocal enabledelayedexpansion

	%==The main thing==%
	%==First param - Number of disks==%
	%==Second param - Start pole==%
	%==Third param - End pole==%
	%==Fourth param - Helper pole==%
call :move 4 START END HELPER
echo.
pause
exit /b 0

	%==The "function"==%
:move
	setlocal
	set n=%1
	set from=%2
	set to=%3
	set via=%4

	if %n% gtr 0 (
		set /a x=!n!-1
		call :move !x! %from% %via% %to%
		echo Move top disk from pole %from% to pole %to%.
		call :move !x! %via% %to% %from%
	) 
	exit /b 0
```

**Output:**

```
Move top disk from pole START to pole HELPER.
Move top disk from pole START to pole END.
Move top disk from pole HELPER to pole END.
Move top disk from pole START to pole HELPER.
Move top disk from pole END to pole START.
Move top disk from pole END to pole HELPER.
Move top disk from pole START to pole HELPER.
Move top disk from pole START to pole END.
Move top disk from pole HELPER to pole END.
Move top disk from pole HELPER to pole START.
Move top disk from pole END to pole START.
Move top disk from pole HELPER to pole END.
Move top disk from pole START to pole HELPER.
Move top disk from pole START to pole END.
Move top disk from pole HELPER to pole END.

Press any key to continue . . .
```


## BBC BASIC

Works with

:

BBC BASIC for Windows

```mw
      DIM Disc$(13),Size%(3)
      FOR disc% = 1 TO 13
        Disc$(disc%) = STRING$(disc%," ")+STR$disc%+STRING$(disc%," ")
        IF disc%>=10 Disc$(disc%) = MID$(Disc$(disc%),2)
        Disc$(disc%) = CHR$17+CHR$(128+disc%-(disc%>7))+Disc$(disc%)+CHR$17+CHR$128
      NEXT disc%
      
      MODE 3
      OFF
      ndiscs% = 13
      FOR n% = ndiscs% TO 1 STEP -1
        PROCput(n%,1)
      NEXT
      INPUT TAB(0,0) "Press Enter to start" dummy$
      PRINT TAB(0,0) SPC(20);
      PROChanoi(ndiscs%,1,2,3)
      VDU 30
      END
      
      DEF PROChanoi(a%,b%,c%,d%)
      IF a%=0 ENDPROC
      PROChanoi(a%-1,b%,d%,c%)
      PROCtake(a%,b%)
      PROCput(a%,c%)
      PROChanoi(a%-1,d%,c%,b%)
      ENDPROC
      
      DEF PROCput(disc%,peg%)
      PRINTTAB(13+26*(peg%-1)-disc%,20-Size%(peg%))Disc$(disc%);
      Size%(peg%) = Size%(peg%)+1
      ENDPROC
      
      DEF PROCtake(disc%,peg%)
      Size%(peg%) = Size%(peg%)-1
      PRINTTAB(13+26*(peg%-1)-disc%,20-Size%(peg%))STRING$(2*disc%+1," ");
      ENDPROC
```


## BCPL

```mw
get "libhdr"

let start() be move(4, 1, 2, 3)
and move(n, src, via, dest) be if n > 0 do 
$(  move(n-1, src, dest, via)
    writef("Move disk from pole %N to pole %N*N", src, dest);
    move(n-1, via, src, dest)
$)
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## Befunge

This is loosely based on the Python sample. The number of disks is specified by the first integer on the stack (the initial character 4 in the example below). If you want the program to prompt the user for that value, you can replace the 4 with a & (the read integer command).

```mw
48*2+1>#v_:!#@_0" ksid evoM">:#,_$:8/:.v
>8v8:<$#<+9-+*2%3\*3/3:,+55.+1%3:$_,#!>#:<
: >/!#^_:0\:8/1-8vv,_$8%:3/1+.>0" gep ot"^
^++3-%3\*2/3:%8\*<>:^:"from peg "0\*8-1<
```

**Output:**

```
Move disk 1 from peg 1 to peg 2
Move disk 2 from peg 1 to peg 3
Move disk 1 from peg 2 to peg 3
Move disk 3 from peg 1 to peg 2
Move disk 1 from peg 3 to peg 1
Move disk 2 from peg 3 to peg 2
Move disk 1 from peg 1 to peg 2
Move disk 4 from peg 1 to peg 3
Move disk 1 from peg 2 to peg 3
Move disk 2 from peg 2 to peg 1
Move disk 1 from peg 3 to peg 1
Move disk 3 from peg 2 to peg 3
Move disk 1 from peg 1 to peg 2
Move disk 2 from peg 1 to peg 3
Move disk 1 from peg 2 to peg 3
```


## BQN

**Based on:** APL

```mw
Move ← {
    𝕩⊑⊸≤0 ? ⟨⟩;
    𝕊 n‿from‿to‿via:
    l ← 𝕊 ⟨n-1, from, via, to⟩
    r ← 𝕊 ⟨n-1, via, to, from⟩
    l∾(<from‿to)∾r
}
{"Move disk from pole "∾(•Fmt 𝕨)∾" to pole "∾•Fmt 𝕩}´˘>Move 4‿1‿2‿3
```

```mw
┌─                                 
╵"Move disk from pole 1 to pole 3  
  Move disk from pole 1 to pole 2  
  Move disk from pole 3 to pole 2  
  Move disk from pole 1 to pole 3  
  Move disk from pole 2 to pole 1  
  Move disk from pole 2 to pole 3  
  Move disk from pole 1 to pole 3  
  Move disk from pole 1 to pole 2  
  Move disk from pole 3 to pole 2  
  Move disk from pole 3 to pole 1  
  Move disk from pole 2 to pole 1  
  Move disk from pole 3 to pole 2  
  Move disk from pole 1 to pole 3  
  Move disk from pole 1 to pole 2  
  Move disk from pole 3 to pole 2" 
                                  ┘
```


## Bracmat

```mw
( ( move
  =   n from to via
    .   !arg:(?n,?from,?to,?via)
      & (   !n:>0
          & move$(!n+-1,!from,!via,!to)
          & out$("Move disk from pole " !from " to pole " !to)
          & move$(!n+-1,!via,!to,!from)
        | 
        )
  )
& move$(4,1,2,3)
);
```

**Output:**

```
Move disk from pole  1  to pole  3
Move disk from pole  1  to pole  2
Move disk from pole  3  to pole  2
Move disk from pole  1  to pole  3
Move disk from pole  2  to pole  1
Move disk from pole  2  to pole  3
Move disk from pole  1  to pole  3
Move disk from pole  1  to pole  2
Move disk from pole  3  to pole  2
Move disk from pole  3  to pole  1
Move disk from pole  2  to pole  1
Move disk from pole  3  to pole  2
Move disk from pole  1  to pole  3
Move disk from pole  1  to pole  2
Move disk from pole  3  to pole  2
```


## Brainf***

```mw
[
This implementation is recursive and uses
a stack, consisting of frames that are 8
bytes long. The layout is as follows:

Byte   Description
   0   recursion flag
       (the program stops if the flag is
        zero)
   1   the step which is currently
       executed
       4 means a call to
               move(a, c, b, n - 1)
       3 means a call to
               move(a, b, c, 1)
       2 means a call to
               move(b, a, c, n - 1)
       1 prints the source and dest pile
   2   flag to check whether the current
       step has already been done or if
       it still must be executed
   3   the step which will be executed
       in the next loop
   4   the source pile
   5   the helper pile
   6   the destination pile
   7   the number of disks to move

The first stack frame (0 0 0 0 0 0 0 0)
is used to abort the recursion.
]

>>>>>>>>

These are the parameters for the program
(1 4 1 0 'a 'b 'c 5)
+>++++>+>>
>>>>++++++++[<++++++++++++>-]<
[<<<+>+>+>-]<<<+>++>+++>+++++>
<<<<<<<<

[> while (recurse)
  [- if (step gt 0)
    >[-]+< todo = 1
    [- if (step gt 1)
      [- if (step gt 2)
        [- if (step gt 3)
          >>+++<< next = 3
          >-< todo = 0
          >>>>>>[>+>+<<-]>[<+>-]> n dup
          -
          [[-] if (sub(n 1) gt 0)
            <+>>>++++> push (1 0 0 4)

            copy and push a
            <<<<<<<<[>>>>>>>>+>+
            <<<<<<<<<-]>>>>>>>>
            >[<<<<<<<<<+>>>>>>>>>-]< >

            copy and push c
            <<<<<<<[>>>>>>>+>+
            <<<<<<<<-]>>>>>>>
            >[<<<<<<<<+>>>>>>>>-]< >

            copy and push b
            <<<<<<<<<[>>>>>>>>>+>+
            <<<<<<<<<<-]>>>>>>>>>
            >[<<<<<<<<<<+>>>>>>>>>>-]< >

            copy n and push sub(n 1)
            <<<<<<<<[>>>>>>>>+>+
            <<<<<<<<<-]>>>>>>>>
            >[<<<<<<<<<+>>>>>>>>>-]< -
            >>
          ]
          <<<<<<<<
        ]
        >[-< if ((step gt 2) and todo)
          >>++<< next = 2
          >>>>>>>
          +>>>+> push 1 0 0 1 a b c 1
          <<<<<<<<[>>>>>>>>+>+
          <<<<<<<<<-]>>>>>>>>
          >[<<<<<<<<<+>>>>>>>>>-]< > a
          <<<<<<<<[>>>>>>>>+>+
          <<<<<<<<<-]>>>>>>>>
          >[<<<<<<<<<+>>>>>>>>>-]< > b
          <<<<<<<<[>>>>>>>>+>+
          <<<<<<<<<-]>>>>>>>>
          >[<<<<<<<<<+>>>>>>>>>-]< > c
          + >>
        >]<
      ]
      >[-< if ((step gt 1) and todo)
        >>>>>>[>+>+<<-]>[<+>-]> n dup
        -
        [[-] if (n sub 1 gt 0)
          <+>>>++++> push (1 0 0 4)

          copy and push b
          <<<<<<<[>>>>>>>+
          <<<<<<<-]>>>>>>>
          >[<<<<<<<<+>>>>>>>>-]< >

          copy and push a
          <<<<<<<<<[>>>>>>>>>+
          <<<<<<<<<-]>>>>>>>>>
          >[<<<<<<<<<<+>>>>>>>>>>-]< >

          copy and push c
          <<<<<<<<[>>>>>>>>+
          <<<<<<<<-]>>>>>>>>
          >[<<<<<<<<<+>>>>>>>>>-]< >

          copy n and push sub(n 1)
          <<<<<<<<[>>>>>>>>+>+
          <<<<<<<<<-]>>>>>>>>
          >[<<<<<<<<<+>>>>>>>>>-]< -
          >>
        ]
        <<<<<<<<
      >]<
    ]
    >[-< if ((step gt 0) and todo)
      >>>>>>>
      >++++[<++++++++>-]<
      >>++++++++[<+++++++++>-]<++++
      >>++++++++[<++++++++++++>-]<+++++
      >>+++++++++[<++++++++++++>-]<+++
      <<<
      >.+++++++>.++.--.<<.
      >>-.+++++.----.<<.
      >>>.<---.+++.>+++.+.+.<.<<.
      >.>--.+++++.---.++++.
        -------.+++.<<.
      >>>++.-------.-.<<<.
      >+.>>+++++++.---.-----.<<<.
      <<<<.>>>>.
      >>----.>++++++++.<+++++.<<.
      >.>>.---.-----.<<<.
      <<.>>++++++++++++++.
      >>>[-]<[-]<[-]<[-]
      +++++++++++++.---.[-]
      <<<<<<<
    >]<
    >>[<<+>>-]<< step = next
  ]
  return with clear stack frame
  <[-]>[-]>[-]>[-]>[-]>[-]>[-]>[-]<<<<<<
  <<<<<<<<
  >>[<<+>>-]<< step = next
  <
]
```
