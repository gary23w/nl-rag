---
title: "Towers of Hanoi (part 4/5)"
source: https://rosettacode.org/wiki/Towers_of_Hanoi
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/5
---

## Picat

```mw
main => 
    hanoi(3, left, center, right).

hanoi(0, _From, _To, _Via) => true.
hanoi(N, From, To, Via) =>
    hanoi(N - 1, From, Via, To),
    printf("Move disk %w from pole %w to pole %w\n", N, From, To),
    hanoi(N - 1, Via, To, From).
```

**Output:**

```
Move disk 1 from pole left to pole center
Move disk 2 from pole left to pole right
Move disk 1 from pole center to pole right
Move disk 3 from pole left to pole center
Move disk 1 from pole right to pole left
Move disk 2 from pole right to pole center
Move disk 1 from pole left to pole center
count=7, theoretical=7
```

### Fast counting

```mw
main => 
   hanoi(64).

hanoi(N) => 
   printf("N=%d\n", N),
   Count = move(N, left, center, right) ,
   printf("count=%w, theoretical=%w\n", Count, 2**N-1).
 
table
move(0, _From, _To, _Via) = 0.
move(N, From, To, Via) = Count => 
    Count1 = move(N - 1, From, Via, To),
    Count2 = move(N - 1, Via, To, From),
    Count = Count1+Count2+1.
```

**Output:**

```
N=64
count=18446744073709551615, theoretical=18446744073709551615
```


## PicoLisp

```mw
(de move (N A B C)  # Use: (move 3 'left 'center 'right)
   (unless (=0 N)
      (move (dec N) A C B)
      (println 'Move 'disk 'from A 'to B)
      (move (dec N) C B A) ) )
```


## PL/I

Translation of

:

Fortran

```mw
tower: proc options (main);

   call Move (4,1,2,3);

Move: procedure (ndiscs, from, to, via) recursive;
   declare (ndiscs, from, to, via) fixed binary;

   if ndiscs = 1 then
      put skip edit ('Move disc from pole ', trim(from), ' to pole ',
         trim(to) ) (a);
   else
      do;
         call Move (ndiscs-1, from, via, to);
         call Move (1, from, to, via);
         call Move (ndiscs-1, via, to, from);
      end;
end Move;

end tower;
```


## PL/M

Translation of

:

Tiny BASIC

Iterative solution as PL/M doesn't do recursion.

Works with

:

8080 PL/M Compiler

... under CP/M (or an emulator)

```mw
100H: /* ITERATIVE TOWERS OF HANOI; TRANSLATED FROM TINY BASIC (VIA ALGOL W) */

   /* CP/M BDOS SYSTEM CALL                                                  */
   BDOS: PROCEDURE( FN, ARG ); DECLARE FN BYTE, ARG ADDRESS; GOTO 5; END;
   /* I/O ROUTINES                                                           */
   PR$CHAR:   PROCEDURE( C ); DECLARE C BYTE;    CALL BDOS( 2, C );  END;
   PR$STRING: PROCEDURE( S ); DECLARE S ADDRESS; CALL BDOS( 9, S );  END;

   DECLARE ( D, N, X, S, T ) ADDRESS;
   /* FIXED NUMBER OF DISCS: 4 */
   N = 1;
   DO D = 1 TO 4;
       N = N + N;
   END;
   DO X = 1 TO N - 1;
       /* AS IN ALGOL W, WE CAN USE PL/M'S BIT ABD MOD OPERATORS             */
       S =   ( X AND ( X - 1 ) )       MOD 3;
       T = ( ( X OR  ( X - 1 ) ) + 1 ) MOD 3;
       CALL PR$STRING( .'MOVE DISC ON PEG $' );
       CALL PR$CHAR( '1' + S );
       CALL PR$STRING( .' TO PEG $' );
       CALL PR$CHAR( '1' + T );
       CALL PR$STRING( .( 0DH, 0AH, '$' ) );
   END;
EOF
```

**Output:**

```
MOVE DISC ON PEG 1 TO PEG 3
MOVE DISC ON PEG 1 TO PEG 2
MOVE DISC ON PEG 3 TO PEG 2
MOVE DISC ON PEG 1 TO PEG 3
MOVE DISC ON PEG 2 TO PEG 1
MOVE DISC ON PEG 2 TO PEG 3
MOVE DISC ON PEG 1 TO PEG 3
MOVE DISC ON PEG 1 TO PEG 2
MOVE DISC ON PEG 3 TO PEG 2
MOVE DISC ON PEG 3 TO PEG 1
MOVE DISC ON PEG 2 TO PEG 1
MOVE DISC ON PEG 3 TO PEG 2
MOVE DISC ON PEG 1 TO PEG 3
MOVE DISC ON PEG 1 TO PEG 2
MOVE DISC ON PEG 3 TO PEG 2
```


## Plain TeX

```mw
\newcount\hanoidepth
\def\hanoi#1{%
  \hanoidepth = #1
  \move abc
}%
\def\move#1#2#3{%
  \advance \hanoidepth by -1
  \ifnum \hanoidepth > 0
    \move #1#3#2
  \fi
  Move the upper disk from pole #1 to pole #3.\par
  \ifnum \hanoidepth > 0
    \move#2#1#3
  \fi
  \advance \hanoidepth by 1
}

\hanoi{5}
\end
```


## Pluto

Translation of

:

Wren

```mw
class Hanoi
    function __construct(disks)
        self.moves = 0
        print($"Towers of Hanoi with {disks} disks:\n")       
        self:move(disks, "L", "C", "R")
        print($"\nCompleted in {self.moves} moves\n")
    end

    function move(n, from, to, via)
        if n > 0 then
            self:move(n - 1, from, via, to)
            ++self.moves
            print($"Move disk {n} from {from} to {to}")
            self:move(n - 1, via, to, from)
        end
    end
end

new Hanoi(3)
new Hanoi(4)
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


## Pop11

```mw
define hanoi(n, src, dst, via);
if n > 0 then
    hanoi(n - 1, src, via, dst);
    'Move disk ' >< n >< ' from ' >< src >< ' to ' >< dst >< '.' =>
    hanoi(n - 1, via, dst, src);
endif;
enddefine;

hanoi(4, "left", "middle", "right");
```


## PostScript

A million-page document, each page showing one move.

```mw
%!PS-Adobe-3.0
%%BoundingBox: 0 0 300 300

/plate {
        exch 100 mul 50 add exch th mul 10 add moveto
        dup s mul neg 2 div 0 rmoveto
        dup s mul 0 rlineto
        0 th rlineto
        s neg mul 0 rlineto
        closepath gsave .5 setgray fill grestore 0 setgray stroke
} def

/drawtower {
        0 1 2 { /x exch def /y 0 def
                tower x get {
                        dup 0 gt { x y plate /y y 1 add def } {pop} ifelse
                } forall
        } for showpage
} def

/apop { [ exch aload pop /last exch def ] last } def
/apush{ [ 3 1 roll aload pop counttomark -1 roll ] } def

/hanoi {
        0 dict begin /from /mid /to /h 5 -1 2 { -1 roll def } for
        h 1 eq {        
                tower from get apop tower to get apush
                tower to 3 -1 roll put
                tower from 3 -1 roll put
                drawtower
        } {     
                /h h 1 sub def
                from to mid h hanoi
                from mid to 1 hanoi
                mid from to h hanoi
        } ifelse
        end
} def

/n 12 def
/s 90 n div def
/th 180 n div def
/tower [ [n 1 add -1 2 { } for ] [] [] ] def

drawtower 0 1 2 n hanoi

%%EOF
```


## PowerShell

Works with

:

PowerShell

version 4.0

```mw
function hanoi($n, $a,  $b, $c) {
    if($n -eq 1) {
        "$a -> $c"
    } else{    
         hanoi ($n - 1) $a $c $b
         hanoi 1 $a $b $c
         hanoi ($n - 1) $b $a $c
    }
}
hanoi 3 "A" "B" "C"
```

**Output:**

```
A -> C
A -> B
C -> B
A -> C
B -> A
B -> C
A -> C
```


## Prolog

From Programming in Prolog by W.F. Clocksin & C.S. Mellish

```mw
hanoi(N) :- move(N,left,center,right).

move(0,_,_,_) :- !.
move(N,A,B,C) :-
    M is N-1,
    move(M,A,C,B),
    inform(A,B),
    move(M,C,B,A).

inform(X,Y) :- write([move,a,disk,from,the,X,pole,to,Y,pole]), nl.
```

Using DCGs and separating core logic from IO

```mw
hanoi(N, Src, Aux, Dest, Moves-NMoves) :-
  NMoves is 2^N - 1,
  length(Moves, NMoves),
  phrase(move(N, Src, Aux, Dest), Moves).

move(1, Src, _, Dest) --> !,
  [Src->Dest].

move(2, Src, Aux, Dest) --> !,
  [Src->Aux,Src->Dest,Aux->Dest].

move(N, Src, Aux, Dest) -->
  { succ(N0, N) },
  move(N0, Src, Dest, Aux),
  move(1, Src, Aux, Dest),
  move(N0, Aux, Src, Dest).
```


## PureBasic

Algorithm according to http://en.wikipedia.org/wiki/Towers_of_Hanoi

```mw
Procedure Hanoi(n, A.s, C.s, B.s)
  If n
    Hanoi(n-1, A, B, C)
    PrintN("Move the plate from "+A+" to "+C)
    Hanoi(n-1, B, C, A)
  EndIf
EndProcedure
```

Full program

```mw
Procedure Hanoi(n, A.s, C.s, B.s)
  If n
    Hanoi(n-1, A, B, C)
    PrintN("Move the plate from "+A+" to "+C)
    Hanoi(n-1, B, C, A)
  EndIf
EndProcedure

If OpenConsole()
  Define n=3
  PrintN("Moving "+Str(n)+" pegs."+#CRLF$)
  Hanoi(n,"Left Peg","Middle Peg","Right Peg")
  PrintN(#CRLF$+"Press ENTER to exit."): Input()
EndIf
```

**Output:**

```
Moving 3 pegs.

Move the plate from Left Peg to Middle Peg
Move the plate from Left Peg to Right Peg
Move the plate from Middle Peg to Right Peg
Move the plate from Left Peg to Middle Peg
Move the plate from Right Peg to Left Peg
Move the plate from Right Peg to Middle Peg
Move the plate from Left Peg to Middle Peg

Press ENTER to exit.
```


## Python

### Recursive

```mw
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print(f"Move disk {ndisks} from peg {startPeg} to peg {endPeg}")
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
 
hanoi(4)
```

**Output:**

for ndisks=2

```
Move disk 1 from peg 1 to peg 2
Move disk 2 from peg 1 to peg 3
Move disk 1 from peg 2 to peg 3
```

Or, separating the definition of the data from its display:

Works with

:

Python

version 3.7

```mw
'''Towers of Hanoi'''

# hanoi :: Int -> String -> String -> String -> [(String, String)]
def hanoi(n):
    '''A list of (from, to) label pairs,
       where a, b and c are labels for each of the
       three Hanoi tower positions.'''
    def go(n, a, b, c):
        p = n - 1
        return (
            go(p, a, c, b) + [(a, b)] + go(p, c, b, a)
        ) if 0 < n else []
    return lambda a: lambda b: lambda c: go(n, a, b, c)

# TEST ----------------------------------------------------
if __name__ == '__main__':

    # fromTo :: (String, String) -> String
    def fromTo(xy):
        '''x -> y'''
        x, y = xy
        return x.rjust(5, ' ') + ' -> ' + y

    print(__doc__ + ':\n\n' + '\n'.join(
        map(fromTo, hanoi(4)('left')('right')('mid'))
    ))
```

**Output:**

```
Towers of Hanoi:

 left -> mid
 left -> right
  mid -> right
 left -> mid
right -> left
right -> mid
 left -> mid
 left -> right
  mid -> right
  mid -> left
right -> left
  mid -> right
 left -> mid
 left -> right
  mid -> right
```

### Graphic

Refactoring the version above to recursively generate a simple visualisation:

Works with

:

Python

version 3.7

```mw
'''Towers of Hanoi'''

from itertools import accumulate, chain, repeat
from inspect import signature
import operator

# hanoi :: Int -> [(Int, Int)]
def hanoi(n):
    '''A list of index pairs, representing disk moves
       between indexed Hanoi positions.
    '''
    def go(n, a, b, c):
        p = n - 1
        return (
            go(p, a, c, b) + [(a, b)] + go(p, c, b, a)
        ) if 0 < n else []
    return go(n, 0, 2, 1)

# hanoiState :: ([Int],[Int],[Int], String) -> (Int, Int) ->
#               ([Int],[Int],[Int], String)
def hanoiState(tpl, ab):
    '''A new Hanoi tower state'''
    a, b = ab
    xs, ys = tpl[a], tpl[b]

    w = 3 * (2 + (2 * max(map(max, filter(len, tpl[:-1])))))

    def delta(i):
        return tpl[i] if i not in ab else xs[1:] if (
            i == a
        ) else [xs[0]] + ys

    tkns = moveName(('left', 'mid', 'right'))(ab)
    caption = ' '.join(tkns)
    return tuple(map(delta, [0, 1, 2])) + (
        (caption if tkns[0] != 'mid' else caption.rjust(w, ' ')),
    )

# showHanoi :: ([Int],[Int],[Int], String) -> String
def showHanoi(tpl):
    '''Captioned string representation of an updated Hanoi tower state.'''

    def fullHeight(n):
        return lambda xs: list(repeat('', n - len(xs))) + xs

    mul = curry(operator.mul)
    lt = curry(operator.lt)
    rods = fmap(fmap(mul('__')))(
        list(tpl[0:3])
    )
    h = max(map(len, rods))
    w = 2 + max(
        map(
            compose(max)(fmap(len)),
            filter(compose(lt(0))(len), rods)
        )
    )
    xs = fmap(concat)(
        transpose(fmap(
            compose(fmap(center(w)(' ')))(
                fullHeight(h)
            )
        )(rods))
    )
    return tpl[3] + '\n\n' + unlines(xs) + '\n' + ('___' * w)

# moveName :: (String, String, String) -> (Int, Int) -> [String]
def moveName(labels):
    '''(from, to) index pair represented as an a -> b string.'''
    def go(ab):
        a, b = ab
        return [labels[a], ' to ', labels[b]] if a < b else [
            labels[b], ' from ', labels[a]
        ]
    return lambda ab: go(ab)

# TEST ----------------------------------------------------
def main():
    '''Visualisation of a Hanoi tower sequence for N discs.
    '''
    n = 3
    print('Hanoi sequence for ' + str(n) + ' disks:\n')
    print(unlines(
        fmap(showHanoi)(
            scanl(hanoiState)(
                (enumFromTo(1)(n), [], [], '')
            )(hanoi(n))
        )
    ))

# GENERIC -------------------------------------------------

# center :: Int -> Char -> String -> String
def center(n):
    '''String s padded with c to approximate centre,
       fitting in but not truncated to width n.'''
    return lambda c: lambda s: s.center(n, c)

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))

# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xs):
    '''The concatenation of all the elements
       in a list or iterable.'''

    def f(ys):
        zs = list(chain(*ys))
        return ''.join(zs) if isinstance(ys[0], str) else zs

    return (
        f(xs) if isinstance(xs, list) else (
            chain.from_iterable(xs)
        )
    ) if xs else []

# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    if 1 < len(signature(f).parameters):
        return lambda x: lambda y: f(x, y)
    else:
        return f

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))

# fmap :: (a -> b) -> [a] -> [b]
def fmap(f):
    '''fmap over a list.
       f lifted to a function over a list.
    '''
    return lambda xs: list(map(f, xs))

# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.
    '''
    return lambda a: lambda xs: (
        accumulate(chain([a], xs), f)
    )

# showLog :: a -> IO String
def showLog(*s):
    '''Arguments printed with
       intercalated arrows.'''
    print(
        ' -> '.join(map(str, s))
    )

# transpose :: Matrix a -> Matrix a
def transpose(m):
    '''The rows and columns of the argument transposed.
       (The matrix containers and rows can be lists or tuples).
    '''
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m

# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)

# TEST ----------------------------------------------------
if __name__ == '__main__':
    main()
```

```
Hanoi sequence for 3 disks:

   __                   
  ____                  
 ______                 
________________________
left  to  right

  ____                  
 ______            __   
________________________
left  to  mid

 ______   ____     __   
________________________
        mid  from  right

           __           
 ______   ____          
________________________
left  to  right

           __           
          ____   ______ 
________________________
left  from  mid

   __     ____   ______ 
________________________
          mid  to  right

                  ____  
   __            ______ 
________________________
left  to  right

                   __   
                  ____  
                 ______ 
________________________
```

### **Library:** VPython

There is a 3D hanoi-game in the examples that come with VPython, and at github.


## Quackery

```mw
  [ stack ]                     is rings    (     --> [ )

  [ rings share
    depth share -
    8 * times sp
    emit sp emit sp
    say 'move' cr ]             is echomove ( c c -->   )

  [ dup rings put
    depth put
    char a char b char c
    [ swap decurse
      rot 2dup echomove
      decurse
      swap rot ]
    3 times drop
    depth release
    rings release ]             is hanoi    (   n --> n )

  say 'How to solve a three ring Towers of Hanoi puzzle:' cr cr
  3 hanoi cr
```

**Output:**

```
How to solve a three ring Towers of Hanoi puzzle:

                        a c move
                a b move
                        c b move
        a c move
                        b a move
                b c move
                        a c move
a b move
                        c b move
                c a move
                        b a move
        c b move
                        a c move
                a b move
                        c b move
```


## Quite BASIC

```
'This is implemented on the Quite BASIC website
'http://www.quitebasic.com/prj/puzzle/towers-of-hanoi/
```

```mw
1000 REM Towers of Hanoi
1010 REM Quite BASIC Puzzle Project
1020 CLS
1030 PRINT "Towers of Hanoi"
1040 PRINT
1050 PRINT "This is a recursive solution for seven discs."
1060 PRINT
1070 PRINT "See the REM statements in the program if you didn't think that recursion was possible in classic BASIC!"
1080 REM Yep, recursive GOSUB calls works in Quite BASIC!  
1090 REM However, to actually write useful recursive algorithms, it helps to have variable scoping and parameters to subroutines -- something classic BASIC is lacking.  In this case we have only one "parameter" -- the variable N.  And subroutines are always called with N-1.  This is lucky for us because we can keep track of the value by decrementing it when we enter subroutines and incrementing it back when we exit.
1100 REM If we had subroutine parameters we could have written a single subroutine for moving discs from peg P to peg Q where P and Q were subroutine parameters, but no such luck.  Instead we have to write six different subroutines for moving from peg to peg.  See Subroutines 4000, 5000, 6000, 7000, 8000, and 9000.
1110 REM ===============================
2000 REM A, B, and C are arrays holding the discs
2010 REM We refer to the corresponding pegs as peg A, B, and C
2020 ARRAY A
2030 ARRAY B
2040 ARRAY C
2050 REM Fill peg A with seven discs
2060 FOR I = 0 TO 6
2070 LET A[I] = 7 - I
2080 NEXT I
2090 REM X, Y, Z hold the number of discs on pegs A, B, and C
2100 LET X = 7
2110 LET Y = 0
2120 LET Z = 0
2130 REM Disc colors
2140 ARRAY P
2150 LET P[1] = "cyan"
2160 LET P[2] = "blue"
2170 LET P[3] = "green"
2180 LET P[4] = "yellow"
2190 LET P[5] = "magenta"
2200 LET P[6] = "orange"
2210 LET P[7] = "red"
2220 REM Draw initial position -- all discs on the A peg
2230 FOR I = 0 TO 6
2240 FOR J = 8 - A[I] TO 8 + A[I]
2250 PLOT J, I, P[A[I]]
2260 NEXT J
2270 NEXT I 
2280 REM N is the number of discs to move
2290 LET N = 7
2320 REM Move all discs from peg A to peg B
2310 GOSUB 6000
2320 END
3000 REM The subroutines 3400, 3500, 3600, 3700, 3800, 3900 
3010 REM handle the drawing of the discs on the canvas as we
3020 REM move discs from one peg to another.
3030 REM These subroutines also update the variables X, Y, and Z
3040 REM which hold the number of discs on each peg.
3050 REM ============================== 
3400 REM Subroutine -- Remove disc from peg A
3410 LET X = X - 1
3420 FOR I = 8 - A[X] TO 8 + A[X]
3430 PLOT I, X, "gray"
3440 NEXT I
3450 RETURN
3500 REM Subroutine -- Add disc to peg A
3510 FOR I = 8 - A[X] TO 8 + A[X]
3520 PLOT I, X, P[A[X]]
3530 NEXT I
3540 LET X = X + 1
3550 PAUSE 400 * (5 - LEVEL) + 10 
3560 RETURN
3600 REM Subroutine -- Remove disc from peg B
3610 LET Y = Y - 1
3620 FOR I = 24 - B[Y] TO 24 + B[Y]
3630 PLOT I, Y, "gray"
3640 NEXT I
3650 RETURN
3700 REM Subroutine -- Add disc to peg B
3710 FOR I = 24 - B[Y] TO 24 + B[Y]
3720 PLOT I, Y, P[B[Y]]
3730 NEXT I
3740 LET Y = Y + 1
3750 PAUSE 400 * (5 - LEVEL) + 10 
3760 RETURN
3800 REM Subroutine -- Remove disc from peg C
3810 LET Z = Z - 1
3820 FOR I = 40 - C[Z] TO 40 + C[Z]
3830 PLOT I, Z, "gray"
3840 NEXT I
3850 RETURN
3900 REM Subroutine -- Add disc to peg C
3910 FOR I = 40 - C[Z] TO 40 + C[Z]
3920 PLOT I, Z, P[C[Z]]
3930 NEXT I
3940 LET Z = Z + 1
3950 PAUSE 400 * (5 - LEVEL) + 10 
3960 RETURN
4000 REM ======================================
4010 REM Recursive Subroutine -- move N discs from peg B to peg A
4020 REM First move N-1 discs from peg B to peg C
4030 LET N = N - 1
4040 IF N <> 0 THEN GOSUB 9000
4050 REM Then move one disc from peg B to peg A 
4060 GOSUB 3600
4070 LET A[X] = B[Y]
4080 GOSUB 3500
4090 REM And finally move N-1 discs from peg C to peg A
4100 IF N <> 0 THEN GOSUB 5000
4110 REM Restore N before returning
4120 LET N = N + 1
4130 RETURN
5000 REM ======================================
5010 REM Recursive Subroutine -- Move N discs from peg C to peg A
5020 REM First move N-1 discs from peg C to peg B
5030 LET N = N - 1
5040 IF N <> 0 THEN GOSUB 8000
5050 REM Then move one disc from peg C to peg A
5060 GOSUB 3800
5070 LET A[X] = C[Z]
5080 GOSUB 3500
5090 REM And finally move N-1 discs from peg B to peg A
5100 IF N <> 0 THEN GOSUB 4000
5120 REM Restore N before returning
5130 LET N = N + 1
5140 RETURN
6000 REM ======================================
6000 REM Recursive Subroutine -- Move N discs from peg A to peg B
6010 REM First move N-1 discs from peg A to peg C
6020 LET N = N - 1
6030 IF N <> 0 THEN GOSUB 7000
6040 REM Then move one disc from peg A to peg B
6050 GOSUB 3400
6060 LET B[Y] = A[X]
6070 GOSUB 3700
6090 REM And finally move N-1 discs from peg C to peg B
6100 IF N <> 0 THEN GOSUB 8000
6110 REM Restore N before returning
6120 LET N = N + 1
6130 RETURN
7000 REM ======================================
7010 REM Recursive Subroutine -- Move N discs from peg A to peg C
7020 REM First move N-1 discs from peg A to peg B
7030 LET N = N - 1
7040 IF N <> 0 THEN GOSUB 6000
7050 REM Then move one disc from peg A to peg C
7060 GOSUB 3400
7070 LET C[Z] = A[X]
7080 GOSUB 3900
7090 REM And finally move N-1 discs from peg B to peg C
7100 IF N <> 0 THEN GOSUB 9000
7110 REM Restore N before returning
7120 LET N = N + 1
7130 RETURN
8000 REM ======================================
8010 REM Recursive Subroutine -- Move N discs from peg C to peg B
8020 REM First move N-1 discs from peg C to peg A
8030 LET N = N - 1
8040 IF N <> 0 THEN GOSUB 5000
8050 REM Then move one disc from peg C to peg B
8060 GOSUB 3800
8070 LET B[Y] = C[Z]
8080 GOSUB 3700
8090 REM And finally move N-1 discs from peg A to peg B
8100 IF N <> 0 THEN GOSUB 6000
8110 REM Restore N before returning
8120 LET N = N + 1
8130 RETURN
9000 REM ======================================
9010 REM Recursive Subroutine -- Move N discs from peg B to peg C
9020 REM First move N-1 discs from peg B to peg A
9030 LET N = N - 1
9040 IF N <> 0 THEN GOSUB 4000
9050 REM Then move one disc from peg B to peg C
9060 GOSUB 3600
9070 LET C[Z] = B[Y]
9080 GOSUB 3900
9090 REM And finally move N-1 discs from peg A to peg C
9100 IF N <> 0 THEN GOSUB 7000
9110 REM Restore N before returning
9120 LET N = N + 1
9130 RETURN
```


## R

Translation of

:

Octave

```mw
hanoimove <- function(ndisks, from, to, via) {
  if (ndisks == 1) {
    cat("move disk from", from, "to", to, "\n")
  } else {
    hanoimove(ndisks - 1, from, via, to)
    hanoimove(1, from, to, via)
    hanoimove(ndisks - 1, via, to, from)
  }
}

hanoimove(4, 1, 2, 3)
```


## Racket

```mw
#lang racket
(define (hanoi n a b c)
  (when (> n 0)
    (hanoi (- n 1) a c b)
    (printf "Move ~a to ~a\n" a b)
    (hanoi (- n 1) c b a)))
(hanoi 4 'left 'middle 'right)
```


## Raku

(formerly Perl 6)

```mw
subset Peg of Int where 1|2|3;

multi hanoi (0,      Peg $a,     Peg $b,     Peg $c)     { }
multi hanoi (Int $n, Peg $a = 1, Peg $b = 2, Peg $c = 3) {
    hanoi $n - 1, $a, $c, $b;
    say "Move $a to $b.";
    hanoi $n - 1, $c, $b, $a;
}
```


## Rascal

Translation of

:

Python

```mw
public void hanoi(ndisks, startPeg, endPeg){
	if(ndisks>0){
		hanoi(ndisks-1, startPeg, 6 - startPeg - endPeg);
		println("Move disk <ndisks> from peg <startPeg> to peg <endPeg>");
		hanoi(ndisks-1, 6 - startPeg - endPeg, endPeg);
	}
}
```

**Output:**

```mw
rascal>hanoi(4,1,3)
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
ok
```


## Raven

Translation of

:

Python

```mw
define hanoi use ndisks, startpeg, endpeg
   ndisks 0 > if
      6 startpeg - endpeg - startpeg ndisks 1 - hanoi
      endpeg startpeg ndisks "Move disk %d from peg %d to peg %d\n" print 
      endpeg 6 startpeg - endpeg - ndisks 1 - hanoi

define dohanoi use ndisks
   # startpeg=1, endpeg=3
   3 1 ndisks hanoi

# 4 disks
4 dohanoi
```

**Output:**

```
raven hanoi.rv 
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


## Rebol

```mw
Rebol [
	Title: "Towers of Hanoi"
	URL: http://rosettacode.org/wiki/Towers_of_Hanoi
]

hanoi: func [
    {Begin moving the golden disks from one pole to the next.
     Note: when last disk moved, the world will end.}
    disks [integer!] "Number of discs on starting pole."
    /poles "Name poles."
    from to via
][
    if disks = 0 [return ()]
    if not poles [from: 'left  to: 'middle  via: 'right]

    hanoi/poles disks - 1 from via to
    print [from "->" to]
    hanoi/poles disks - 1 via to from
]

hanoi 4
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


## Red

```mw
Red [ "Towers of Hanoi - Hinjo, 20 July 2025" ]
hanoi: function [n src tgt aux] [
    if n > 0 [
        hanoi n - 1 src aux tgt
        print ["Move from " src " to " tgt]
        hanoi n - 1 aux tgt src
    ]
]
hanoi 5 "A" "C" "B"
```

**Output:**

```
Move from  A  to  C
Move from  A  to  B
Move from  C  to  B
Move from  A  to  C
Move from  B  to  A
Move from  B  to  C
Move from  A  to  C
Move from  A  to  B
Move from  C  to  B
Move from  C  to  A
Move from  B  to  A
Move from  C  to  B
Move from  A  to  C
Move from  A  to  B
Move from  C  to  B
Move from  A  to  C
Move from  B  to  A
Move from  B  to  C
Move from  A  to  C
Move from  B  to  A
Move from  C  to  B
Move from  C  to  A
Move from  B  to  A
Move from  B  to  C
Move from  A  to  C
Move from  A  to  B
Move from  C  to  B
Move from  A  to  C
Move from  B  to  A
Move from  B  to  C
Move from  A  to  C
>> 
```


## Refal

```mw
$ENTRY Go {
    = <Move 4 1 2 3>;
};

Move {
    0 e.X = ;
    s.N s.Src s.Via s.Dest, <- s.N 1>: s.Next =
        <Move s.Next s.Src s.Dest s.Via>
        <Prout "Move disk from pole" s.Src "to pole" s.Dest>
        <Move s.Next s.Via s.Src s.Dest>;
};
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


## Retro

```mw
[[User:Wodan58|Wodan58]] ([[User talk:Wodan58|talk]])
{ 'Num 'From 'To 'Via } [ var ] a:for-each 
 
:set     !Via !To !From !Num ; 
:display @To @From 'Move_a_ring_from_%n_to_%n\n s:format s:put ; 
 
:hanoi (num,from,to,via-) 
  set @Num n:-zero? 
  [ @Num @From @To @Via 
    @Num n:dec @From @Via @To hanoi set display 
    @Num n:dec @Via @To @From hanoi ] if ; 
 
#3 #1 #3 #2 hanoi nl 
[[User:Wodan58|Wodan58]] ([[User talk:Wodan58|talk]])
```


## REXX

### simple text moves

```mw
/*REXX program  displays  the  moves  to solve  the  Tower of Hanoi  (with  N  disks).  */
parse arg N .                                    /*get optional number of disks from CL.*/
if N=='' | N==","  then N=3                      /*Not specified?  Then use the default.*/
#= 0                                             /*#:  the number of disk moves (so far)*/
z= 2**N  -  1                                    /*Z:   "     "    " minimum # of moves.*/
call mov  1, 3, N                                /*move the top disk,  then recurse ··· */
say                                              /* [↓]  Display the minimum # of moves.*/
say 'The minimum number of moves to solve a '      N"─disk  Tower of Hanoi is "     z
exit                                             /*stick a fork in it,  we're all done. */
/*──────────────────────────────────────────────────────────────────────────────────────*/
mov: procedure expose # z; parse arg  @1,@2,@3;          L= length(z)
     if @3==1  then do;  #= # + 1                /*bump the (disk) move counter by one. */
                         say 'step'   right(#, L)":  move disk on tower"   @1  '───►'   @2
                    end
               else do;  call mov @1,               6 -@1 -@2,         @3 -1
                         call mov @1,               @2,                  1
                         call mov 6 - @1 - @2,      @2,                @3 -1
                    end
     return                                      /* [↑]  this subroutine uses recursion.*/
```

**output   when using the default input:**

```
step 1:  move disk on tower 1 ───► 3
step 2:  move disk on tower 1 ───► 2
step 3:  move disk on tower 3 ───► 2
step 4:  move disk on tower 1 ───► 3
step 5:  move disk on tower 2 ───► 1
step 6:  move disk on tower 2 ───► 3
step 7:  move disk on tower 1 ───► 3

The minimum number of moves to solve a  3-disk  Tower of Hanoi is  7
```

**output**   when the following was entered (to solve with four disks):   4

```
step  1:  move disk on tower 1 ───► 2
step  2:  move disk on tower 1 ───► 3
step  3:  move disk on tower 2 ───► 3
step  4:  move disk on tower 1 ───► 2
step  5:  move disk on tower 3 ───► 1
step  6:  move disk on tower 3 ───► 2
step  7:  move disk on tower 1 ───► 2
step  8:  move disk on tower 1 ───► 3
step  9:  move disk on tower 2 ───► 3
step 10:  move disk on tower 2 ───► 1
step 11:  move disk on tower 3 ───► 1
step 12:  move disk on tower 2 ───► 3
step 13:  move disk on tower 1 ───► 2
step 14:  move disk on tower 1 ───► 3
step 15:  move disk on tower 2 ───► 3

The minimum number of moves to solve a  4-disk  Tower of Hanoi is  15
```

### pictorial moves

This REXX version pictorially shows   (via ASCII art)   the moves for solving the Town of Hanoi.

Quite a bit of code has been dedicated to showing a "picture" of the towers with the disks, and the movement of the disk (for each move).   "Coloring" of the disks is attempted with dithering.

In addition, it shows each move in a countdown manner (the last move is marked as #1).

It may not be obvious from the pictorial display of the moves, but whenever a disk is moved from one tower to another, it is always the top disk that is moved   (to the target tower).

Also, since the pictorial showing of the moves may be voluminous (especially for a larger number of disks), the move counter is started with the maximum and is the count shown is decremented so the viewer can see how many moves are left to display.

```mw
/*REXX program  displays  the  moves  to solve  the  Tower of Hanoi  (with  N  disks).  */
parse arg N .                                    /*get optional number of disks from CL.*/
if N=='' | N==","  then N=3                      /*Not specified?  Then use the default.*/
sw= 80;    wp= sw%3 - 1;   blanks= left('', wp)  /*define some default REXX variables.  */
c.1= sw % 3 % 2                                  /* [↑]  SW: assume default Screen Width*/
c.2= sw % 2 - 1                                  /* ◄───  C.1 C.2 C.2  are the positions*/
c.3= sw - 2 - c.1                                /*                    of the 3 columns.*/
#= 0;        z= 2**N - 1;           moveK= z     /*#moves; min# of moves; where to move.*/
@abc= 'abcdefghijklmnopqrstuvwxyN'               /*dithering chars when many disks used.*/
ebcdic= ('f2'x==2)                               /*determine if EBCDIC or ASCII machine.*/

if ebcdic then do;   bar= 'bf'x;    ar= "df"x;    dither= 'db9f9caf'x;         down= "9a"x
                      tr= 'bc'x;    bl= "ab"x;    br= 'bb'x;   vert= "fa"x;      tl= 'ac'x
               end
          else do;   bar= 'c4'x;    ar= "10"x;    dither= 'b0b1b2db'x;         down= "19"x
                      tr= 'bf'x;    bl= "c0"x;    br= 'd9'x;   vert= "b3"x;      tl= 'da'x
               end

verts= vert || vert;           Tcorners= tl || tr;              box     = left(dither, 1)
downs= down || down;           Bcorners= bl || br;              boxChars= dither || @abc
$.= 0;         $.1= N;         k= N;                            kk= k + k

  do j=1  for N;   @.3.j= blanks;    @.2.j= blanks;    @.1.j= center( copies(box, kk), wp)
  if N<=length(boxChars)  then @.1.j= translate( @.1.j, , substr( boxChars, kk%2, 1), box)
  kk= kk - 2
  end   /*j*/                                    /*populate the tower of Hanoi spindles.*/

call showTowers;   call mov 1,3,N;   say
say 'The minimum number of moves to solve a '        N"-disk  Tower of Hanoi is "      z
exit                                             /*stick a fork in it,  we're all done. */
/*──────────────────────────────────────────────────────────────────────────────────────*/
dsk: parse arg from dest;   #= # + 1;       pp=
     if from==1  then do;  pp= overlay(bl,  pp, c.1)
                           pp= overlay(bar, pp, c.1+1, c.dest-c.1-1, bar) || tr
                      end
     if from==2  then do
                      if dest==1  then do;  pp= overlay(tl,  pp, c.1)
                                            pp= overlay(bar, pp, c.1+1, c.2-c.1-1,bar)||br
                                       end
                      if dest==3  then do;  pp= overlay(bl,  pp, c.2)
                                            pp= overlay(bar, pp, c.2+1, c.3-c.2-1,bar)||tr
                                       end
                      end
     if from==3  then do;  pp= overlay(br,  pp, c.3)
                           pp= overlay(bar, pp, c.dest+1, c.3-c.dest-1, bar)
                           pp= overlay(tl,  pp, c.dest)
                      end
     say translate(pp, downs, Bcorners || Tcorners || bar);     say overlay(moveK, pp, 1)
     say translate(pp, verts, Tcorners || Bcorners || bar)
     say translate(pp, downs, Tcorners || Bcorners || bar);     moveK= moveK - 1
     $.from= $.from - 1;      $.dest= $.dest + 1;     _f= $.from + 1;           _t= $.dest
     @.dest._t= @.from._f;    @.from._f= blanks;      call showTowers
     return
/*──────────────────────────────────────────────────────────────────────────────────────*/
mov: if arg(3)==1  then      call dsk arg(1) arg(2)
                   else do;  call mov arg(1),              6 -arg(1) -arg(2),    arg(3) -1
                             call mov arg(1),              arg(2),               1
                             call mov 6 -arg(1) -arg(2),   arg(2),               arg(3) -1
                        end                 /* [↑]  The  MOV  subroutine is recursive,  */
     return                                 /*it uses no variables, is uses BIFs instead*/
/*──────────────────────────────────────────────────────────────────────────────────────*/
showTowers: do j=N  by -1  for N; _=@.1.j @.2.j @.3.j;  if _\=''  then say _; end;  return
```

**output   when using the default input:**

```
           ░░
          ▒▒▒▒
         ▓▓▓▓▓▓
            ↓
7           └───────────────────────────────────────────────────┐
                                                                │
                                                                ↓
          ▒▒▒▒
         ▓▓▓▓▓▓                                                ░░
            ↓
6           └─────────────────────────┐
                                      │
                                      ↓
         ▓▓▓▓▓▓                     ▒▒▒▒                       ░░
                                                                ↓
5                                     ┌─────────────────────────┘
                                      │
                                      ↓
                                     ░░
         ▓▓▓▓▓▓                     ▒▒▒▒
            ↓
4           └───────────────────────────────────────────────────┐
                                                                │
                                                                ↓
                                     ░░
                                    ▒▒▒▒                     ▓▓▓▓▓▓
                                      ↓
3           ┌─────────────────────────┘
            │
            ↓
           ░░                       ▒▒▒▒                     ▓▓▓▓▓▓
                                      ↓
2                                     └─────────────────────────┐
                                                                │
                                                                ↓
                                                              ▒▒▒▒
           ░░                                                ▓▓▓▓▓▓
            ↓
1           └───────────────────────────────────────────────────┐
                                                                │
                                                                ↓
                                                               ░░
                                                              ▒▒▒▒
                                                             ▓▓▓▓▓▓

The minimum number of moves to solve a  3-disk  Tower of Hanoi is  7
```


## Ring

```mw
move(4, 1, 2, 3)

func move n, src, dst, via
     if n > 0 move(n - 1, src, via, dst)
        see "" + src + " to " + dst + nl
        move(n - 1, via, dst, src) ok
```


## RPL

Translation of

:

Python

Works with

:

Halcyon Calc

version 4.2.7

```
≪ → ndisks start end
  ≪ IF ndisks THEN
        ndisks 1 - start 6 start - end - HANOI
        start →STR " → " + end →STR +
        ndisks 1 - 6 start - end - end HANOI
        END
≫ ≫ 'HANOI' STO
```

```
3 1 3 HANOI
```

**Output:**

```
7: "1 → 3"
6: "1 → 2"
5: "3 → 2"
4: "1 → 3"
3: "2 → 1"
2: "2 → 3"
1: "1 → 3"
```


## Ruby

### version 1

```mw
def move(num_disks, start=0, target=1, using=2)
  if num_disks == 1
   @towers[target] << @towers[start].pop
    puts "Move disk from #{start} to #{target} : #{@towers}"
  else
    move(num_disks-1, start, using, target)
    move(1,           start, target, using)
    move(num_disks-1, using, target, start)
  end 
end

n = 5
@towers = [[*1..n].reverse, [], []]
move(n)
```

**Output:**

```
Move disk from 0 to 1 : [[5, 4, 3, 2], [1], []]
Move disk from 0 to 2 : [[5, 4, 3], [1], [2]]
Move disk from 1 to 2 : [[5, 4, 3], [], [2, 1]]
Move disk from 0 to 1 : [[5, 4], [3], [2, 1]]
Move disk from 2 to 0 : [[5, 4, 1], [3], [2]]
Move disk from 2 to 1 : [[5, 4, 1], [3, 2], []]
Move disk from 0 to 1 : [[5, 4], [3, 2, 1], []]
Move disk from 0 to 2 : [[5], [3, 2, 1], [4]]
Move disk from 1 to 2 : [[5], [3, 2], [4, 1]]
Move disk from 1 to 0 : [[5, 2], [3], [4, 1]]
Move disk from 2 to 0 : [[5, 2, 1], [3], [4]]
Move disk from 1 to 2 : [[5, 2, 1], [], [4, 3]]
Move disk from 0 to 1 : [[5, 2], [1], [4, 3]]
Move disk from 0 to 2 : [[5], [1], [4, 3, 2]]
Move disk from 1 to 2 : [[5], [], [4, 3, 2, 1]]
Move disk from 0 to 1 : [[], [5], [4, 3, 2, 1]]
Move disk from 2 to 0 : [[1], [5], [4, 3, 2]]
Move disk from 2 to 1 : [[1], [5, 2], [4, 3]]
Move disk from 0 to 1 : [[], [5, 2, 1], [4, 3]]
Move disk from 2 to 0 : [[3], [5, 2, 1], [4]]
Move disk from 1 to 2 : [[3], [5, 2], [4, 1]]
Move disk from 1 to 0 : [[3, 2], [5], [4, 1]]
Move disk from 2 to 0 : [[3, 2, 1], [5], [4]]
Move disk from 2 to 1 : [[3, 2, 1], [5, 4], []]
Move disk from 0 to 1 : [[3, 2], [5, 4, 1], []]
Move disk from 0 to 2 : [[3], [5, 4, 1], [2]]
Move disk from 1 to 2 : [[3], [5, 4], [2, 1]]
Move disk from 0 to 1 : [[], [5, 4, 3], [2, 1]]
Move disk from 2 to 0 : [[1], [5, 4, 3], [2]]
Move disk from 2 to 1 : [[1], [5, 4, 3, 2], []]
Move disk from 0 to 1 : [[], [5, 4, 3, 2, 1], []]
```

### version 2

```mw
# solve(source, via, target)
# Example:
# solve([5, 4, 3, 2, 1], [], [])
# Note this will also solve randomly placed disks,
# "place all disk in target with legal moves only".
def solve(*towers)
  # total number of disks
  disks = towers.inject(0){|sum, tower| sum+tower.length}
  x=0 # sequence number
  p towers # initial trace
  # have we solved the puzzle yet?
  while towers.last.length < disks do
    x+=1 # assume the next step
    from = (x&x-1)%3
    to = ((x|(x-1))+1)%3
    # can we actually take from tower?
    if top = towers[from].last
      bottom = towers[to].last
      # is the move legal?
      if !bottom || bottom > top
        # ok, do it!
        towers[to].push(towers[from].pop)
        p towers # trace
      end
    end
  end
end

solve([5, 4, 3, 2, 1], [], [])
```

**Output:**

```
[[5, 4, 3, 2, 1], [], []]
[[5, 4, 3, 2], [], [1]]
[[5, 4, 3], [2], [1]]
[[5, 4, 3], [2, 1], []]
[[5, 4], [2, 1], [3]]
[[5, 4, 1], [2], [3]]
[[5, 4, 1], [], [3, 2]]
[[5, 4], [], [3, 2, 1]]
[[5], [4], [3, 2, 1]]
[[5], [4, 1], [3, 2]]
[[5, 2], [4, 1], [3]]
[[5, 2, 1], [4], [3]]
[[5, 2, 1], [4, 3], []]
[[5, 2], [4, 3], [1]]
[[5], [4, 3, 2], [1]]
[[5], [4, 3, 2, 1], []]
[[], [4, 3, 2, 1], [5]]
[[1], [4, 3, 2], [5]]
[[1], [4, 3], [5, 2]]
[[], [4, 3], [5, 2, 1]]
[[3], [4], [5, 2, 1]]
[[3], [4, 1], [5, 2]]
[[3, 2], [4, 1], [5]]
[[3, 2, 1], [4], [5]]
[[3, 2, 1], [], [5, 4]]
[[3, 2], [], [5, 4, 1]]
[[3], [2], [5, 4, 1]]
[[3], [2, 1], [5, 4]]
[[], [2, 1], [5, 4, 3]]
[[1], [2], [5, 4, 3]]
[[1], [], [5, 4, 3, 2]]
[[], [], [5, 4, 3, 2, 1]]
```


## Run BASIC

```mw
a = move(4, "1", "2", "3")
function move(n, a$, b$, c$) 
if n > 0 then
	a = move(n-1, a$, c$, b$)
	print "Move disk from " ; a$ ; " to " ; c$
	a = move(n-1, b$, a$, c$)
end if
end function
```

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
```


## Rust

Translation of

:

C

```mw
fn move_(n: i32, from: i32, to: i32, via: i32) {
    if n > 0 {
        move_(n - 1, from, via, to);
        println!("Move disk from pole {} to pole {}", from, to);
        move_(n - 1, via, to, from);
    }
}

fn main() {
    move_(4, 1,2,3);
}
```


## SASL

Copied from SAL manual, Appendix II, answer (3)

```mw
hanoi 8 ‘abc"
WHERE
hanoi 0 (a,b,c,) = ()
hanoi n ( a,b,c) = hanoi (n-1) (a,c,b) ,
                   ‘move a disc from " , a , ‘ to " , b , NL ,
                   hanoi (n-1) (c,b,a)
?
```


## Sather

Translation of

:

Fortran

```mw
class MAIN is
  
  move(ndisks, from, to, via:INT) is
    if ndisks = 1 then
      #OUT + "Move disk from pole " + from + " to pole " + to + "\n";
    else
      move(ndisks-1, from, via, to);
      move(1, from, to, via);
      move(ndisks-1, via, to, from);
    end;
  end;

  main is
    move(4, 1, 2, 3);
  end;
end;
```


## Scala

```mw
def move(n: Int, from: Int, to: Int, via: Int) : Unit = {
    if (n == 1) {
      Console.println("Move disk from pole " + from + " to pole " + to)
    } else {
      move(n - 1, from, via, to)
      move(1, from, to, via)
      move(n - 1, via, to, from)
    }
  }
```

This next example is from http://gist.github.com/66925 it is a translation to Scala of a Prolog solution and solves the problem at compile time

```mw
object TowersOfHanoi {
  import scala.reflect.Manifest
  
  def simpleName(m:Manifest[_]):String = {
    val name = m.toString
    name.substring(name.lastIndexOf('$')+1)
  }
  
  trait Nat
  final class _0 extends Nat
  final class Succ[Pre<:Nat] extends Nat
 
  type _1 = Succ[_0]
  type _2 = Succ[_1]
  type _3 = Succ[_2]
  type _4 = Succ[_3]
 
  case class Move[N<:Nat,A,B,C]()
 
  implicit def move0[A,B,C](implicit a:Manifest[A],b:Manifest[B]):Move[_0,A,B,C] = {
        System.out.println("Move from "+simpleName(a)+" to "+simpleName(b));null
  }
 
  implicit def moveN[P<:Nat,A,B,C](implicit m1:Move[P,A,C,B],m2:Move[_0,A,B,C],m3:Move[P,C,B,A])
   :Move[Succ[P],A,B,C] = null
  
  def run[N<:Nat,A,B,C](implicit m:Move[N,A,B,C]) = null
  
  case class Left()
  case class Center()
  case class Right()
  
  def main(args:Array[String]){
    run[_2,Left,Right,Center]
  }
}
```


## Scheme

Recursive Process

```mw
(define (towers-of-hanoi n from to spare)
  (define (print-move from to)
    (display "Move[")
    (display from)
    (display ", ")
    (display to)
    (display "]")
    (newline))
  (cond ((= n 0) "done")
        (else
         (towers-of-hanoi (- n 1) from spare to)
         (print-move from to)
         (towers-of-hanoi (- n 1) spare to from))))

(towers-of-hanoi 3 "A" "B" "C")
```

**Output:**

```
Move[A, B]
Move[A, C]
Move[B, C]
Move[A, B]
Move[C, A]
Move[C, B]
Move[A, B]
"done"
```


## Seed7

```mw
const proc: hanoi (in integer: disk, in string: source, in string: dest, in string: via) is func
  begin
    if disk > 0 then
      hanoi(pred(disk), source, via, dest);
      writeln("Move disk " <& disk <& " from " <& source <& " to " <& dest);
      hanoi(pred(disk), via, dest, source);
    end if;
  end func;
```
