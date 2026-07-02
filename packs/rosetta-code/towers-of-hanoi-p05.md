---
title: "Towers of Hanoi (part 5/5)"
source: https://rosettacode.org/wiki/Towers_of_Hanoi
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/5
---

## SETL

```mw
program hanoi;
    loop for [src, dest] in move(4, 1, 2, 3) do
        print("Move disk from pole " + src + " to pole " + dest);
    end loop;

    proc move(n, src, via, dest);
        if n=0 then return []; end if;
        return move(n-1, src, dest, via)
             + [[src, dest]]
             + move(n-1, via, src, dest);
    end proc;
end program;
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


## SheerPower 4GL

```mw
declare integer discs%

discs% = 4
print 'Tower of Hanoi — '; discs%; ' discs'
print 'Minimum moves: '; 2 ^ discs% - 1
print

call hanoi(discs%, 'A', 'C', 'B')

! =============================================================================
! Routine: hanoi(n%, from$, to$, via$)
!
! Move n% discs from peg from$ to peg to$, using peg via$ as auxiliary.
! Prints each move as "Move disc N from X to Y".
! =============================================================================
routine hanoi(n%, from$, to$, via$)
  if n% > 0 then
    call hanoi(n% - 1, from$, via$, to$)
    print 'Move disc '; n%; ' from '; from$; ' to '; to$
    call hanoi(n% - 1, via$, to$, from$)
  end if
end routine
```


## Sidef

Translation of

:

Perl

```mw
func hanoi(n, from=1, to=2, via=3) {
    if (n == 1) {
        say "Move disk from pole #{from} to pole #{to}.";
    } else {
        hanoi(n-1, from, via,   to);
        hanoi(  1, from,  to,  via);
        hanoi(n-1,  via,  to, from);
    }
}

hanoi(4);
```


## SNOBOL4

```mw
*       # Note: count is global

        define('hanoi(n,src,trg,tmp)') :(hanoi_end)
hanoi   hanoi = eq(n,0) 1 :s(return)
        hanoi(n - 1, src, tmp, trg)
        count  = count + 1
        output = count ': Move disc from ' src ' to ' trg
        hanoi(n - 1, tmp, trg, src) :(return)
hanoi_end

*       # Test with 4 discs
        hanoi(4,'A','C','B')
end
```

**Output:**

```
1: Move disc from A to B
2: Move disc from A to C
3: Move disc from B to C
4: Move disc from A to B
5: Move disc from C to A
6: Move disc from C to B
7: Move disc from A to B
8: Move disc from A to C
9: Move disc from B to C
10: Move disc from B to A
11: Move disc from C to A
12: Move disc from B to C
13: Move disc from A to B
14: Move disc from A to C
15: Move disc from B to C
```


## SparForte

As a structured script.

```mw
#!/usr/local/bin/spar
pragma annotate( summary, "hanoi" )
       @( description, "Solve the Towers of Hanoi problem with recursion." )
       @( see_also, "https://rosettacode.org/wiki/Towers_of_Hanoi" )
       @( author, "Ken O. Burtch" );
pragma license( unrestricted );

pragma restriction( no_external_commands );

procedure hanoi is
  type pegs is (left, center, right);

  -- Determine the moves

  procedure solve( num_disks : natural; start_peg : pegs;  end_peg : pegs; via_peg : pegs ) is
  begin
    if num_disks > 0 then
       solve( num_disks - 1, start_peg, via_peg, end_peg );
       put( "Move disk" )@( num_disks )@( " from " )@( start_peg )@( " to " )@( end_peg );
       new_line;
       solve( num_disks - 1, via_peg, end_peg, start_peg );
    end if;
  end solve;

begin
  -- solve with 4 disks at the left
  --solve( 4, left, right, center );
  solve( 4, left, right, center );
  put_line( "Towers of Hanoi puzzle completed" );
end hanoi;
```


## Standard ML

```
   fun hanoi(0, a, b, c) = [] |
       hanoi(n, a, b, c) = hanoi(n-1, a, c, b) @ [(a,b)] @ hanoi(n-1, c, b, a);
```


## Stata

```mw
function hanoi(n, a, b, c) {
	if (n>0) {
		hanoi(n-1, a, c, b)
		printf("Move from %f to %f\n", a, b)
		hanoi(n-1, c, b, a)
	}
}

hanoi(3, 1, 2, 3)

Move from 1 to 2
Move from 1 to 3
Move from 2 to 3
Move from 1 to 2
Move from 3 to 1
Move from 3 to 2
Move from 1 to 2
```


## Swift

Translation of

:

JavaScript

```mw
func hanoi(n:Int, a:String, b:String, c:String) {
    if (n > 0) {
        hanoi(n - 1, a, c, b)
        println("Move disk from \(a) to \(c)")
        hanoi(n - 1, b, a, c)
    }
}

hanoi(4, "A", "B", "C")
```

**Swift 2.1**

```mw
func hanoi(n:Int, a:String, b:String, c:String) {
  if (n > 0) {
    hanoi(n - 1, a: a, b: c, c: b)
    print("Move disk from \(a) to \(c)")
    hanoi(n - 1, a: b, b: a, c: c)
  }
}
 
hanoi(4, a:"A", b:"B", c:"C")
```


## Tcl

The use of `interp alias` shown is a sort of closure: keep track of the number of moves required

```mw
interp alias {} hanoi {} do_hanoi 0

proc do_hanoi {count n {from A} {to C} {via B}} {
    if {$n == 1} {
        interp alias {} hanoi {} do_hanoi [incr count]
        puts "$count: move from $from to $to"
    } else {
        incr n -1
        hanoi $n $from $via $to
        hanoi 1  $from $to $via
        hanoi $n $via $to $from
    }
}

hanoi 4
```

**Output:**

```
1: move from A to B
2: move from A to C
3: move from B to C
4: move from A to B
5: move from C to A
6: move from C to B
7: move from A to B
8: move from A to C
9: move from B to C
10: move from B to A
11: move from C to A
12: move from B to C
13: move from A to B
14: move from A to C
15: move from B to C
```


## TI-83 BASIC

TI-83 BASIC lacks recursion, so technically this task is impossible, however here is a version that uses an iterative method.

```mw
PROGRAM:TOHSOLVE
0→A
1→B
0→C
0→D
0→M
1→R
While A<1 or A>7
Input "No. of rings=?",A
End
randM(A+1,3)→[C]
[[1,2][1,3][2,3]]→[E]

Fill(0,[C])
For(I,1,A,1)
I?[C](I,1)
End
ClrHome
While [C](1,3)≠1 and [C](1,2)≠1

For(J,1,3)
For(I,1,A)
If [C](I,J)≠0:Then
Output(I+1,3J,[C](I,J))
End
End
End
While C=0
Output(1,3B," ")
1→I
[E](R,2)→J
While [C](I,J)=0 and I≤A
I+1→I
End
[C](I,J)→D
1→I
[E](R,1)→J
While [C](I,J)=0 and I≤A
I+1→I
End
If (D<[C](I,J) and D≠0) or [C](I,J)=0:Then
[E](R,2)→B
Else
[E](R,1)→B
End

1→I
While [C](I,B)=0 and I≤A
I+1→I
End
If I≤A:Then
[C](I,B)→C
0→[C](I,B)
Output(I+1,3B," ")
End
Output(1,3B,"V")
End

While C≠0
Output(1,3B," ")
If B=[E](R,2):Then
[E](R,1)→B
Else
[E](R,2)→B
End

1→I
While [C](I,B)=0 and I≤A
I+1→I
End
If [C](I,B)=0 or [C](I,B)>C:Then
C→[C](I-1,B)
0→C
M+1→M
End
End
Output(1,3B,"V")
R+1→R
If R=4:Then:1→R:End

End
```


## Tiny BASIC

Tiny BASIC does not have recursion, so only an iterative solution is possible... and it has no arrays, so actually keeping track of individual discs is not feasible.

But as if by magic, it turns out that the source and destination pegs on iteration number n are given by (n&n-1) mod 3 and ((n|n-1) + 1) mod 3 respectively, where & and | are the bitwise and and or operators. Line 40 onward is dedicated to implementing those bitwise operations, since Tiny BASIC hasn't got them natively.

```mw
 5  PRINT "How many disks?"
    INPUT D
    IF D < 1 THEN GOTO 5
    IF D > 10 THEN GOTO 5
    LET N = 1
10  IF D = 0 THEN GOTO 20
    LET D = D - 1
    LET N = 2*N
    GOTO 10
20  LET X = 0
30  LET X = X + 1
    IF X = N THEN END
    GOSUB 40
    LET S = S - 3*(S/3)
    GOSUB 50
    LET T = T + 1
    LET T = T - 3*(T/3)
    PRINT "Move disc on peg ",S+1," to peg ",T+1
    GOTO 30
40  LET B = X - 1
    LET A = X
    LET S = 0
    LET Z = 2048
45  LET C = 0
    IF B >= Z THEN LET C = 1
    IF A >= Z THEN LET C = C + 1
    IF C = 2 THEN LET S = S + Z
    IF A >= Z THEN LET A = A - Z
    IF B >= Z THEN LET B = B - Z
    LET Z = Z / 2
    IF Z = 0 THEN RETURN
    GOTO 45
50  LET B = X - 1
    LET A = X
    LET T = 0
    LET Z = 2048
55  LET C = 0
    IF B >= Z THEN LET C = 1
    IF A >= Z THEN LET C = C + 1
    IF C > 0 THEN LET T = T + Z
    IF A >= Z THEN LET A = A - Z
    IF B >= Z THEN LET B = B - Z
    LET Z = Z / 2
    IF Z = 0 THEN RETURN
    GOTO 55
```

**Output:**

```
How many discs?
4
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


## Toka

```mw
value| sa sb sc n |
[ to sc to sb to sa to n ] is vars!
[ ( num from to via -- )
  vars!
  n 0 <>
  [
    n sa sb sc 
    n 1- sa sc sb recurse
    vars!
    ." Move a ring from " sa . ." to " sb . cr
    n 1- sc sb sa recurse
  ] ifTrue
] is hanoi
```


## True BASIC

Translation of

:

FreeBASIC

```mw
DECLARE SUB hanoi

SUB hanoi(n, desde , hasta, via)
    IF n > 0 THEN
       CALL hanoi(n - 1, desde, via, hasta)
       PRINT "Mover disco"; n; "desde posición"; desde; "hasta posición"; hasta
       CALL hanoi(n - 1, via, hasta, desde)
    END IF
END SUB

PRINT "Tres discos"
PRINT
CALL hanoi(3, 1, 2, 3)
PRINT
PRINT "Cuatro discos"
PRINT
CALL hanoi(4, 1, 2, 3)
PRINT
PRINT "Pulsa un tecla para salir"
END
```


## TSE SAL

```mw
// library: program: run: towersofhanoi: recursive: sub <description></description> <version>1.0.0.0.0</version> <version control></version control> (filenamemacro=runprrsu.s) [kn, ri, tu, 07-02-2012 19:54:23]
PROC PROCProgramRunTowersofhanoiRecursiveSub( INTEGER totalDiskI, STRING fromS, STRING toS, STRING viaS, INTEGER bufferI )
 IF ( totalDiskI == 0 )
  RETURN()
 ENDIF
 PROCProgramRunTowersofhanoiRecursiveSub( totalDiskI - 1, fromS, viaS, toS, bufferI )
 AddLine( Format( "Move disk", " ", totalDiskI, " ", "from peg", " ", "'", fromS, "'", " ", "to peg", " ", "'", toS, "'" ), bufferI )
 PROCProgramRunTowersofhanoiRecursiveSub( totalDiskI - 1, viaS, toS, fromS, bufferI )
END

// library: program: run: towersofhanoi: recursive <description></description> <version>1.0.0.0.6</version> <version control></version control> (filenamemacro=runprtre.s) [kn, ri, tu, 07-02-2012 19:40:45]
PROC PROCProgramRunTowersofhanoiRecursive( INTEGER totalDiskI, STRING fromS, STRING toS, STRING viaS )
 INTEGER bufferI = 0
 PushPosition()
 bufferI = CreateTempBuffer()
 PopPosition()
 PROCProgramRunTowersofhanoiRecursiveSub( totalDiskI, fromS, toS, viaS, bufferI )
 GotoBufferId( bufferI )
END

PROC Main()
STRING s1[255] = "4"
IF ( NOT ( Ask( "program: run: towersofhanoi: recursive: totalDiskI = ", s1, _EDIT_HISTORY_ ) ) AND ( Length( s1 ) > 0 ) ) RETURN() ENDIF
 PROCProgramRunTowersofhanoiRecursive( Val( s1 ), "source", "target", "via" )
END
```


## uBasic/4tH

Translation of

:

C

```mw
Proc  _Move(4, 1,2,3)                  ' 4 disks, 3 poles
End

_Move Param(4)
  If (a@ > 0) Then
    Proc _Move (a@ - 1, b@, d@, c@)
    Print "Move disk from pole ";b@;" to pole ";c@
    Proc _Move (a@ - 1, d@, c@, b@)
  EndIf
Return
```


## Uiua

Works with

:

Uiua

version 0.18.0

```mw
F ← |1.0 (
  ⨬(&p $"Move disc from _ to _" °⊟ ⊏1_2
  | F⍜⊢-₁⍜(⊏2_3)⇌.
    F⍜⊢⋅1.
    F⍜⊢-₁⍜(⊏1_3)⇌
  )≠1⊢.
)
F 4_1_2_3
```

**Output:**

```
Move disc from 1 to 3
Move disc from 1 to 2
Move disc from 3 to 2
Move disc from 1 to 3
Move disc from 2 to 1
Move disc from 2 to 3
Move disc from 1 to 3
Move disc from 1 to 2
Move disc from 3 to 2
Move disc from 3 to 1
Move disc from 2 to 1
Move disc from 3 to 2
Move disc from 1 to 3
Move disc from 1 to 2
Move disc from 3 to 2
```


## UNIX Shell

Works with

:

Bourne Again SHell

Works with

:

Korn Shell

Works with

:

Z Shell

```mw
function move {
  typeset -i n=$1
  typeset from=$2
  typeset to=$3
  typeset via=$4

  if (( n )); then
    move $(( n - 1 )) "$from" "$via" "$to"
    echo "Move disk from pole $from to pole $to"
    move $(( n - 1 )) "$via" "$to" "$from"
  fi
}
  
move "$@"
```

A strict POSIX (or just really old) shell has no subprogram capability, but scripts are naturally reentrant, so:

Works with

:

Bourne Shell

Works with

:

Almquist Shell

```mw
#!/bin/sh
if [ "$1" -gt 0 ]; then
  "$0" "`expr $1 - 1`" "$2" "$4" "$3"
  echo "Move disk from pole $2 to pole $3"
  "$0" "`expr $1 - 1`" "$4" "$3" "$2"
fi
```

Output from any of the above:

**Output:**

```
$ hanoi 4 1 3 2
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


## Ursala

```mw
#import nat

move = ~&al^& ^rlPlrrPCT/~&arhthPX ^|W/~& ^|G/predecessor ^/~&htxPC ~&zyxPC

#show+

main = ^|T(~&,' -> '--)* move/4 <'start','end','middle'>
```

**Output:**

```
start -> middle
start -> end
middle -> end
start -> middle
end -> start
end -> middle
start -> middle
start -> end
middle -> end
middle -> start
end -> start
middle -> end
start -> middle
start -> end
middle -> end
```


## Uxntal

```mw
%newline { [ LIT2 0a -Console/write ] DEO }

|18 @Console/write

|0100

#0102 #0304 hanoi
POP2 POP2 

BRK

@hanoi ( from spare to count -- from spare to count )
    ( moving 0 disks is no-op )
    DUP ?{ JMP2r }

    ( move disks 1..count-1 to the spare peg )
    #01 SUB ROT SWP hanoi
    ( from to spare count-1 )

    ( print the current move )
    ;dict/move print/str
    INCk #30 ORA .Console/write DEO
    STH2
    ;dict/from print/str
    OVR #30 ORA .Console/write DEO
    ;dict/to print/str
    DUP #30 ORA .Console/write DEO
	newline
    STH2r

    ( move disks 1..count-1 from the spare peg to the goal peg )
    STH ROT ROT STHr hanoi

    ( restore original parameters for convenient recursion )
    STH2 SWP STH2r INC

    JMP2r

@print/str ( str* -- )
    LDAk .Console/write DEO
    INC2 LDAk ?/str
    POP2 JMP2r

@dict
    &move "Move 20 "disk 2000
    &from 20 "from 20 "pole 2000
    &to 20 "to 20 "pole 2000
```

**Output:**

```
Move disk 1 from pole 1 to pole 2
Move disk 2 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 3
Move disk 3 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 1
Move disk 2 from pole 3 to pole 2
Move disk 1 from pole 1 to pole 2
Move disk 4 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 3
Move disk 2 from pole 2 to pole 1
Move disk 1 from pole 3 to pole 1
Move disk 3 from pole 2 to pole 3
Move disk 1 from pole 1 to pole 2
Move disk 2 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 3
```


## VBScript

Derived from the BASIC256 version.

```mw
Sub Move(n,fromPeg,toPeg,viaPeg)
	If n > 0 Then
		Move n-1, fromPeg, viaPeg, toPeg
		WScript.StdOut.Write "Move disk from " & fromPeg & " to " & toPeg
		WScript.StdOut.WriteBlankLines(1)
		Move n-1, viaPeg, toPeg, fromPeg
	End If
End Sub

Move 4,1,2,3
WScript.StdOut.Write("Towers of Hanoi puzzle completed!")
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


## Vedit macro language

This implementation outputs the results in current edit buffer.

```mw
#1=1; #2=2; #3=3; #4=4          // move 4 disks from 1 to 2
Call("MOVE_DISKS")
Return

// Move disks
// #1 = from, #2 = to, #3 = via, #4 = number of disks
//
:MOVE_DISKS:
if (#4 > 0) {
    Num_Push(1,4)
        #9=#2; #2=#3; #3=#9; #4--       // #1 to #3 via #2
        Call("MOVE_DISKS")
    Num_Pop(1,4)

    Ins_Text("Move a disk from ")       // move one disk
    Num_Ins(#1, LEFT+NOCR)
    Ins_Text(" to ")
    Num_Ins(#2, LEFT)

    Num_Push(1,4)
        #9=#1; #1=#3; #3 = #9; #4--     // #3 to #2 via #1
        Call("MOVE_DISKS")
    Num_Pop(1,4)
}
Return
```


## Vim Script

```mw
function TowersOfHanoi(n, from, to, via)
  if (a:n > 1)
    call TowersOfHanoi(a:n-1, a:from, a:via, a:to)
  endif
  echom("Move a disc from " . a:from . " to " . a:to)
  if (a:n > 1)
    call TowersOfHanoi(a:n-1, a:via, a:to, a:from)
  endif
endfunction

call TowersOfHanoi(4, 1, 3, 2)
```

**Output:**

```
Move a disc from 1 to 2
Move a disc from 1 to 3
Move a disc from 2 to 3
Move a disc from 1 to 2
Move a disc from 3 to 1
Move a disc from 3 to 2
Move a disc from 1 to 2
Move a disc from 1 to 3
Move a disc from 2 to 3
Move a disc from 2 to 1
Move a disc from 3 to 1
Move a disc from 2 to 3
Move a disc from 1 to 2
Move a disc from 1 to 3
Move a disc from 2 to 3
```


## Visual Basic .NET

```mw
Module TowersOfHanoi
    Sub MoveTowerDisks(ByVal disks As Integer, ByVal fromTower As Integer, ByVal toTower As Integer, ByVal viaTower As Integer)
        If disks > 0 Then
            MoveTowerDisks(disks - 1, fromTower, viaTower, toTower)
            System.Console.WriteLine("Move disk {0} from {1} to {2}", disks, fromTower, toTower)
            MoveTowerDisks(disks - 1, viaTower, toTower, fromTower)
        End If
    End Sub

    Sub Main()
        MoveTowerDisks(4, 1, 2, 3)
    End Sub
End Module
```


## V (Vlang)

```mw
fn main() {
	hanoi(4, "A", "B", "C")
}

fn hanoi(n u64, a string, b string, c string) {
    if n > 0 {
        hanoi(n - 1, a, c, b)
        println("Move disk from ${a} to ${c}")
        hanoi(n - 1, b, a, c)
    }
}
```

**Output:**

```
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from A to B
Move disk from C to A
Move disk from C to B
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from B to A
Move disk from C to A
Move disk from B to C
Move disk from A to B
Move disk from A to C
Move disk from B to C
```


## VTL-2

VTL-2 doesn't have procedure parameters, so this stacks and unstacks the return line number and parameters as reuired. The "move" routune starts at line 2000, the routine at 4000 stacks the return line number and parameters for "move" and the routine at 5000 unstacks the return line number and parameters.

```mw
1000 N=4
1010 F=1
1020 T=2
1030 V=3
1040 S=0
1050 #=2000
1060 #=9999
2000 R=!
2010 #=N<1*2210
2020 #=4000
2030 N=N-1
2040 A=T
2050 T=V
2060 V=A
2070 #=2000
2080 #=5000
2090 ?="Move disk from peg: ";
2100 ?=F
2110 ?=" to peg: ";
2120 ?=T
2130 ?=""
2140 #=4000
2150 N=N-1
2160 A=F
2170 F=V
2180 V=A
2190 #=2000
2200 #=5000
2210 #=R
4000 S=S+1
4010 :S)=R
4020 S=S+1
4030 :S)=N
4040 S=S+1
4050 :S)=F
4060 S=S+1
4070 :S)=V
4080 S=S+1
4090 :S)=T
4100 #=!
5000 T=:S)
5010 S=S-1
5020 V=:S)
5030 S=S-1
5040 F=:S)
5050 S=S-1
5060 N=:S)
5070 S=S-1
5080 R=:S)
5090 S=S-1
5100 #=!
```

**Output:**

```
Move disk from peg: 1 to peg: 3
Move disk from peg: 1 to peg: 2
Move disk from peg: 3 to peg: 2
Move disk from peg: 1 to peg: 3
Move disk from peg: 2 to peg: 1
Move disk from peg: 2 to peg: 3
Move disk from peg: 1 to peg: 3
Move disk from peg: 1 to peg: 2
Move disk from peg: 3 to peg: 2
Move disk from peg: 3 to peg: 1
Move disk from peg: 2 to peg: 1
Move disk from peg: 3 to peg: 2
Move disk from peg: 1 to peg: 3
Move disk from peg: 1 to peg: 2
Move disk from peg: 3 to peg: 2
```


## Wren

Translation of

:

Kotlin

```mw
class Hanoi {
    construct new(disks) {
        _moves = 0
        System.print("Towers of Hanoi with %(disks) disks:\n")
        move(disks, "L", "C", "R")
        System.print("\nCompleted in %(_moves) moves\n")
    }

    move(n, from, to, via) {
        if (n > 0) {
            move(n - 1, from, via, to)
            _moves = _moves + 1
            System.print("Move disk %(n) from %(from) to %(to)")
            move(n - 1, via, to, from)
        }
    }
}

Hanoi.new(3)
Hanoi.new(4)
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


## XBasic

Works with

:

Windows XBasic

```mw
PROGRAM	"Hanoi"
VERSION	"0.0000"

DECLARE FUNCTION Entry ()
DECLARE FUNCTION Hanoi(n, desde , hasta, via)

FUNCTION  Entry ()
	PRINT "Three disks\n"
	Hanoi (3, 1, 2, 3)
	PRINT "\nFour discks\n"
	Hanoi (4, 1, 2, 3)
	PRINT "\nTowers of Hanoi puzzle completed!"
END FUNCTION

FUNCTION Hanoi (n, desde , hasta, via)
    IF n > 0 THEN
       Hanoi (n - 1, desde, via, hasta)
       PRINT "Move disk"; n; " from pole"; desde; " to pole"; hasta
       Hanoi (n - 1, via, hasta, desde)
    END IF
END FUNCTION
END PROGRAM
```

**Output:**

```
Same as FreeBASIC entry.
```


## XPL0

```mw
code Text=12;

proc MoveTower(Discs, From, To, Using);
int  Discs, From, To, Using;
[if Discs > 0 then
    [MoveTower(Discs-1, From, Using, To);
    Text(0, "Move from ");  Text(0, From);
    Text(0, " peg to ");  Text(0, To);  Text(0, " peg.^M^J");
    MoveTower(Discs-1, Using, To, From);
    ];
];

MoveTower(3, "left", "right", "center")
```

**Output:**

```
Move from left peg to right peg.
Move from left peg to center peg.
Move from right peg to center peg.
Move from left peg to right peg.
Move from center peg to left peg.
Move from center peg to right peg.
Move from left peg to right peg.
```


## XQuery

```mw
declare function local:hanoi($disk as xs:integer, $from as xs:integer,
    $to as xs:integer, $via as xs:integer) as element()* 
{
  if($disk > 0)
  then (
    local:hanoi($disk - 1, $from, $via, $to),
    <move disk='{$disk}'><from>{$from}</from><to>{$to}</to></move>,
    local:hanoi($disk - 1, $via, $to, $from)
  ) 
  else ()
};

<hanoi>
{
  local:hanoi(4, 1, 2, 3)
}
</hanoi>
```

**Output:**

```mw
<?xml version="1.0" encoding="UTF-8"?>
<hanoi>
   <move disk="1">
      <from>1</from>
      <to>3</to>
   </move>
   <move disk="2">
      <from>1</from>
      <to>2</to>
   </move>
   <move disk="1">
      <from>3</from>
      <to>2</to>
   </move>
   <move disk="3">
      <from>1</from>
      <to>3</to>
   </move>
   <move disk="1">
      <from>2</from>
      <to>1</to>
   </move>
   <move disk="2">
      <from>2</from>
      <to>3</to>
   </move>
   <move disk="1">
      <from>1</from>
      <to>3</to>
   </move>
   <move disk="4">
      <from>1</from>
      <to>2</to>
   </move>
   <move disk="1">
      <from>3</from>
      <to>2</to>
   </move>
   <move disk="2">
      <from>3</from>
      <to>1</to>
   </move>
   <move disk="1">
      <from>2</from>
      <to>1</to>
   </move>
   <move disk="3">
      <from>3</from>
      <to>2</to>
   </move>
   <move disk="1">
      <from>1</from>
      <to>3</to>
   </move>
   <move disk="2">
      <from>1</from>
      <to>2</to>
   </move>
   <move disk="1">
      <from>3</from>
      <to>2</to>
   </move>
</hanoi>
```


## XSLT

```mw
<xsl:template name="hanoi">
<xsl:param name="n"/>
<xsl:param name="from">left</xsl:param>
<xsl:param name="to">middle</xsl:param>
<xsl:param name="via">right</xsl:param>
  <xsl:if test="$n &gt; 0">
    <xsl:call-template name="hanoi">
      <xsl:with-param name="n"    select="$n - 1"/>
      <xsl:with-param name="from" select="$from"/>
      <xsl:with-param name="to"   select="$via"/>
      <xsl:with-param name="via"  select="$to"/>
    </xsl:call-template>
    <fo:block>
      <xsl:text>Move disk from </xsl:text>
      <xsl:value-of select="$from"/>
      <xsl:text> to </xsl:text>
      <xsl:value-of select="$to"/>
    </fo:block>
    <xsl:call-template name="hanoi">
      <xsl:with-param name="n"    select="$n - 1"/>
      <xsl:with-param name="from" select="$via"/>
      <xsl:with-param name="to"   select="$to"/>
      <xsl:with-param name="via"  select="$from"/>
    </xsl:call-template>
  </xsl:if>
</xsl:template>
```

```
<xsl:call-template name="hanoi"><xsl:with-param name="n" select="4"/></xsl:call-template>
```


## Yabasic

```mw
sub hanoi(ndisks, startPeg, endPeg)
    if ndisks then
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        //print "Move disk ", ndisks, " from ", startPeg, " to ", endPeg
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
    end if
end sub

print "Be patient, please.\n\n"
print "Hanoi 1 ellapsed ... ";

t1 = peek("millisrunning")
hanoi(22, 1, 3)
t2 = peek("millisrunning")
print t2-t1, " ms"

sub hanoi2(n, from, to_, via)
    if n = 1 then
	//print "Move from ", from, " to ", to_
    else
	hanoi2(n - 1, from, via , to_ )
    	hanoi2(1    , from, to_ , via )
    	hanoi2(n - 1, via , to_ , from)
    end if
end sub

print "Hanoi 2 ellapsed ... ";
hanoi2(22, 1, 3, 2)
print peek("millisrunning") - t2, " ms"
```


## YAMLScript

```mw
!ys-0

defn main(n=3):
  hanoi: n 'A' 'C' 'B'

defn hanoi(n from to via):
  when n > 0:
    hanoi: n.-- from via to
    say: "Move disk $n from $from to $to"
    hanoi: n.-- via to from
```

**Output:**

```
$ ys towers-of-hanoi.ys
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```


## Z80 Assembly

Works with

:

CP/M 3.1

version YAZE-AG-2.51.2 Z80 emulator

Works with

:

ZSM4 macro assembler

version YAZE-AG-2.51.2 Z80 emulator

Use the /S8 switch on the ZSM4 assembler for 8 significant characters for labels and names

```mw
	;
	; Towers of Hanoi using Z80 assembly language
	;
	; Runs under CP/M 3.1 on YAZE-AG-2.51.2 Z80 emulator
	; Assembled with zsm4 on same emulator/OS, uses macro capabilities of said assembler
	; Created with vim under Windows
	;
	; 2023-05-29 Xorph
	;

	;
	; Useful definitions
	;

	bdos	equ 05h		; Call to CP/M BDOS function
	strdel	equ 6eh		; Set string delimiter
	wrtstr	equ 09h		; Write string to console

	nul	equ 00h		; ASCII control characters
	cr	equ 0dh
	lf	equ 0ah

	cnull	equ '0'		; ASCII character constants
	ca	equ 'A'
	cb	equ 'B'
	cc	equ 'C'

	disks	equ 4		; Number of disks to move

	;
	; Macros for BDOS calls
	;

setdel 	macro	char		; Set string delimiter to char
	ld	c,strdel
	ld	e,char
	call	bdos
	endm

print 	macro	msg		; Output string to console
	ld	c,wrtstr
	ld	de,msg
	call	bdos
	endm

pushall	macro			; Save required registers to stack
	push	af
	push	bc
	push	de
	endm

popall	macro			; Recall required registers from stack
	pop	de
	pop	bc
	pop	af
	endm

	;
	; =====================
	; Start of main program
	; =====================
	;

	cseg

	setdel	nul		; Set string delimiter to 00h

	ld	a,disks		; Initialization:
	ld	b,ca		; Tower A is source
	ld	c,cb		; Tower B is target
	ld	d,cc		; Tower C is intermediate

hanoi:
	;
	; Parameters in registers:
	; Move a disks from b (source) to c (target) via d (intermediate)
	;

	or	a		; If 0 disks to move, return
	ret	z

	dec	a		; Move all but lowest disk from source to intermediate via target
	pushall			; Save registers
	ld	e,c		; Exchange c and d (target and intermediate)
	ld	c,d
	ld	d,e
	call	hanoi		; First recursion
	popall			; Restore registers

	ld	hl,source	; Print move of lowest disk from source to target, save registers during BDOS call
	ld	(hl),b		; Source is still in b
	ld	hl,target
	ld	(hl),c		; Target is back in c due to popall

	pushall
	print	movement
	popall

	ld	e,b		; Now move stack from intermediate to target via source
	ld	b,d		; Source is still in b, target in c and intermediate in d
	ld	d,e
	jr	hanoi		; Optimize tail recursion

	;
	; ================
	; Data definitions
	; ================
	;

	dseg

movement:
	defb	'Move disk from tower '
source:
	defs	1
	defb	' to tower '
target:
	defs	1
crlf:
	defb	cr,lf,nul
```

**Output:**

```
E>hanoi
Move disk from tower A to tower C
Move disk from tower A to tower B
Move disk from tower C to tower B
Move disk from tower A to tower C
Move disk from tower B to tower A
Move disk from tower B to tower C
Move disk from tower A to tower C
Move disk from tower A to tower B
Move disk from tower C to tower B
Move disk from tower C to tower A
Move disk from tower B to tower A
Move disk from tower C to tower B
Move disk from tower A to tower C
Move disk from tower A to tower B
Move disk from tower C to tower B

E>
```


## Zen C

```mw
fn hanoi(disk: int, from: string, to: string, via: string, pmoves: int*) {
    if disk > 0 {
        hanoi(disk - 1, from, via, to, pmoves);
        *pmoves += 1;
        println "Move disk {disk} from {from} to {to}";
        hanoi(disk - 1, via, to, from, pmoves);
    }
}

fn main() {
    let disks = [3, 4];
    for disk in disks {
        println "Towers of Hanoi with {disk} disks:\n";
        let moves = 0;
        hanoi(disk, "L", "C", "R", &moves);
        println "\nCompleted in {moves} moves.\n";
    }
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

Completed in 7 moves.

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

Completed in 15 moves.
```


## Zig

Translation of

:

C

```mw
const std = @import("std");

pub fn print(from: u32, to: u32) void {
    std.log.info("Moving disk from rod {} to rod {}", .{ from, to });
}

pub fn move(n: u32, from: u32, via: u32, to: u32) void {
    if (n > 1) {
        move(n - 1, from, to, via);
        print(from, to);
        move(n - 1, via, from, to);
    } else {
        print(from, to);
    }
}

pub fn main() !void {
    move(4, 1, 2, 3);
}
```


## zkl

Translation of

:

C

```mw
fcn move(n, from,to,via){
   if (n>0){
      move(n-1, from,via,to);
      println("Move disk from pole %d to pole %d".fmt(from, to));
      move(n-1, via,to,from);
   }
}
move(3, 1,2,3);
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
```

Retrieved from "

https://rosettacode.org/wiki/Towers_of_Hanoi?oldid=402720

"
