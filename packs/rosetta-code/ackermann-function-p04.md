---
title: "Ackermann function (part 4/6)"
source: https://rosettacode.org/wiki/Ackermann_function
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/6
---

## MAD

While MAD supports function calls, it does not handle recursion automatically. There is support for a stack, but the programmer has to set it up himself (by defining an array to reserve memory, then making it the stack using the `SET LIST`) command. Values have to be pushed and popped from it by hand (using `SAVE` and `RESTORE`), and for a function to be reentrant, even the return address has to be kept.

On top of this, all variables are global throughout the program (there is no scope), and argument passing is done by reference, meaning that even once the stack is set up, arguments cannot be passed in the normal way. To define a function that takes arguments, one would have to declare a helper function that then passes the arguments to the recursive function via the stack or the global variables. The following program demonstrates this.

```mw
            NORMAL MODE IS INTEGER
            DIMENSION LIST(3000)
            SET LIST TO LIST
          
            INTERNAL FUNCTION(DUMMY)
            ENTRY TO ACKH.
LOOP        WHENEVER M.E.0
                FUNCTION RETURN N+1
            OR WHENEVER N.E.0
                M=M-1
                N=1
                TRANSFER TO LOOP
            OTHERWISE
                SAVE RETURN
                SAVE DATA M
                N=N-1
                N=ACKH.(0)
                RESTORE DATA M
                RESTORE RETURN
                M=M-1
                TRANSFER TO LOOP
            END OF CONDITIONAL
            ERROR RETURN
            END OF FUNCTION
            
            INTERNAL FUNCTION(MM,NN)
            ENTRY TO ACK.
            M=MM
            N=NN
            FUNCTION RETURN ACKH.(0)
            END OF FUNCTION
            
            THROUGH SHOW, FOR I=0, 1, I.G.3
            THROUGH SHOW, FOR J=0, 1, J.G.8
SHOW        PRINT FORMAT ACKF,I,J,ACK.(I,J)
            
            VECTOR VALUES ACKF = $4HACK(,I1,1H,,I1,4H) = ,I4*$
            END OF PROGRAM
```

**Output:**

```
ACK(0,0) =    1
ACK(0,1) =    2
ACK(0,2) =    3
ACK(0,3) =    4
ACK(0,4) =    5
ACK(0,5) =    6
ACK(0,6) =    7
ACK(0,7) =    8
ACK(0,8) =    9
ACK(1,0) =    2
ACK(1,1) =    3
ACK(1,2) =    4
ACK(1,3) =    5
ACK(1,4) =    6
ACK(1,5) =    7
ACK(1,6) =    8
ACK(1,7) =    9
ACK(1,8) =   10
ACK(2,0) =    3
ACK(2,1) =    5
ACK(2,2) =    7
ACK(2,3) =    9
ACK(2,4) =   11
ACK(2,5) =   13
ACK(2,6) =   15
ACK(2,7) =   17
ACK(2,8) =   19
ACK(3,0) =    5
ACK(3,1) =   13
ACK(3,2) =   29
ACK(3,3) =   61
ACK(3,4) =  125
ACK(3,5) =  253
ACK(3,6) =  509
ACK(3,7) = 1021
ACK(3,8) = 2045
```


## Maple

Strictly by the definition given above, we can code this as follows.

```mw
Ackermann := proc( m :: nonnegint, n :: nonnegint )
  option remember; # optional automatic memoization
  if m = 0 then
    n + 1
  elif n = 0 then
    thisproc( m - 1, 1 )
  else
    thisproc( m - 1, thisproc( m, n - 1 ) )
  end if
end proc:
```

In Maple, the keyword

```mw
thisproc
```

refers to the currently executing procedure (closure) and is used when writing recursive procedures. (You could also use the name of the procedure, Ackermann in this case, but then a concurrently executing task or thread could re-assign that name while the recursive procedure is executing, resulting in an incorrect result.)

To make this faster, you can use known expansions for small values of ${\displaystyle m}$ . (See Wikipedia:Ackermann function)

```mw
Ackermann := proc( m :: nonnegint, n :: nonnegint )
  option remember; # optional automatic memoization
  if m = 0 then
    n + 1
  elif m = 1 then
    n + 2
  elif m = 2 then
    2 * n + 3
  elif m = 3 then
    8 * 2^n - 3
  elif n = 0 then
    thisproc( m - 1, 1 )
  else
    thisproc( m - 1, thisproc( m, n - 1 ) )
  end if
end proc:
```

This makes it possible to compute `Ackermann( 4, 1 )` and `Ackermann( 4, 2 )` essentially instantly, though `Ackermann( 4, 3 )` is still out of reach.

To compute Ackermann( 1, i ) for i from 1 to 10 use

```mw
> map2( Ackermann, 1, [seq]( 1 .. 10 ) );
               [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

To get the first 10 values for m = 2 use

```mw
> map2( Ackermann, 2, [seq]( 1 .. 10 ) );
               [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
```

For Ackermann( 4, 2 ) we get a very long number with

```mw
> length( Ackermann( 4, 2 ) );
                      19729
```

digits.


## Mathcad

Mathcad is a non-text-based programming environment. The equation below is an approximation of the way that it is entered (and) displayed on a Mathcad worksheet. The worksheet is available at https://community.ptc.com/t5/PTC-Mathcad/Rosetta-Code-Ackermann-Function/m-p/750117#M197410

This particular version of Ackermann's function was created in Mathcad Prime Express 7.0, a free version of Mathcad Prime 7.0 with restrictions (such as no programming or symbolics). All Prime Express numbers are complex. There is a recursion depth limit of about 4,500.

```mw
A(m,n):=if(m=0,n+1,if(n=0,A(m-1,1),A(m-1,A(m,n-1))))
```

The worksheet also contains an explictly-calculated version of Ackermann's function that calls the tetration function na.

na(a,n):=if(n=0,1,ana(a,n-1))

aerror(m,n):=error(format("cannot compute a({0},{1})",m,n))

a(m,n):=if(m=0,n+1,if(m=1,n+2,if(m=2,2n+3,if(m=3,2^(n+3)-3,aerror(m,n)))))

a(m,n):=if(m=4,na(2,n+3)-3,a(m,n)


## Mathematica / Wolfram Language

Two possible implementations would be:

```mw
$RecursionLimit=Infinity
Ackermann1[m_,n_]:=
 If[m==0,n+1,
  If[ n==0,Ackermann1[m-1,1],
   Ackermann1[m-1,Ackermann1[m,n-1]]
  ]
 ]

 Ackermann2[0,n_]:=n+1;
 Ackermann2[m_,0]:=Ackermann1[m-1,1];
 Ackermann2[m_,n_]:=Ackermann1[m-1,Ackermann1[m,n-1]]
```

Note that the second implementation is quite a bit faster, as doing 'if' comparisons is slower than the built-in pattern matching algorithms. Examples:

```mw
Flatten[#,1]&@Table[{"Ackermann2["<>ToString[i]<>","<>ToString[j]<>"] =",Ackermann2[i,j]},{i,3},{j,8}]//Grid
```

gives back:

```mw
Ackermann2[1,1] =	3
Ackermann2[1,2] =	4
Ackermann2[1,3] =	5
Ackermann2[1,4] =	6
Ackermann2[1,5] =	7
Ackermann2[1,6] =	8
Ackermann2[1,7] =	9
Ackermann2[1,8] =	10
Ackermann2[2,1] =	5
Ackermann2[2,2] =	7
Ackermann2[2,3] =	9
Ackermann2[2,4] =	11
Ackermann2[2,5] =	13
Ackermann2[2,6] =	15
Ackermann2[2,7] =	17
Ackermann2[2,8] =	19
Ackermann2[3,1] =	13
Ackermann2[3,2] =	29
Ackermann2[3,3] =	61
Ackermann2[3,4] =	125
Ackermann2[3,5] =	253
Ackermann2[3,6] =	509
Ackermann2[3,7] =	1021
Ackermann2[3,8] =	2045
```

If we would like to calculate Ackermann[4,1] or Ackermann[4,2] we have to optimize a little bit:

```mw
Clear[Ackermann3]
$RecursionLimit=Infinity;
Ackermann3[0,n_]:=n+1;
Ackermann3[1,n_]:=n+2;
Ackermann3[2,n_]:=3+2n;
Ackermann3[3,n_]:=5+8 (2^n-1);
Ackermann3[m_,0]:=Ackermann3[m-1,1];
Ackermann3[m_,n_]:=Ackermann3[m-1,Ackermann3[m,n-1]]
```

Now computing Ackermann[4,1] and Ackermann[4,2] can be done quickly (<0.01 sec): Examples 2:

```mw
Ackermann3[4, 1]
Ackermann3[4, 2]
```

gives back:

```mw
65533
2003529930406846464979072351560255750447825475569751419265016973710894059556311453089506130880........699146577530041384717124577965048175856395072895337539755822087777506072339445587895905719156733
```

Ackermann[4,2] has 19729 digits, several thousands of digits omitted in the result above for obvious reasons. Ackermann[5,0] can be computed also quite fast, and is equal to 65533. Summarizing Ackermann[0,n_], Ackermann[1,n_], Ackermann[2,n_], and Ackermann[3,n_] can all be calculated for n>>1000. Ackermann[4,0], Ackermann[4,1], Ackermann[4,2] and Ackermann[5,0] are only possible now. Maybe in the future we can calculate higher Ackermann numbers efficiently and fast. Although showing the results will always be a problem.


## MATLAB

```mw
function A = ackermannFunction(m,n)
    if m == 0
        A = n+1;
    elseif (m > 0) && (n == 0)
        A = ackermannFunction(m-1,1);
    else
        A = ackermannFunction( m-1,ackermannFunction(m,n-1) );
    end
end
```


## Maxima

```mw
ackermann(m, n) := if integerp(m) and integerp(n) then ackermann[m, n] else 'ackermann(m, n)$

ackermann[m, n] := if m = 0 then n + 1
                   elseif m = 1 then 2 + (n + 3) - 3
                   elseif m = 2 then 2 * (n + 3) - 3
                   elseif m = 3 then 2^(n + 3) - 3
                   elseif n = 0 then ackermann[m - 1, 1]
                   else ackermann[m - 1, ackermann[m, n - 1]]$

tetration(a, n) := if integerp(n) then block([b: a], for i from 2 thru n do b: a^b, b) else 'tetration(a, n)$

/* this should evaluate to zero */
ackermann(4, n) - (tetration(2, n + 3) - 3);
subst(n = 2, %);
ev(%, nouns);
```


## MAXScript

Use with caution. Will cause a stack overflow for m > 3.

```mw
fn ackermann m n =
(
    if m == 0 then
    (
        return n + 1
    )
    else if n == 0 then
    (
        ackermann (m-1) 1
    )
    else
    (
        ackermann (m-1) (ackermann m (n-1))
    )
)
```


## Mercury

This is the Ackermann function with some (obvious) elements elided. The `ack/3` predicate is implemented in terms of the `ack/2` function. The `ack/2` function is implemented in terms of the `ack/3` predicate. This makes the code both more concise and easier to follow than would otherwise be the case. The `integer` type is used instead of `int` because the problem statement stipulates the use of bignum integers if possible.

```mw
:- func ack(integer, integer) = integer.
ack(M, N) = R :- ack(M, N, R).

:- pred ack(integer::in, integer::in, integer::out) is det.
ack(M, N, R) :-
	( ( M < integer(0)  
	  ; N < integer(0) ) -> throw(bounds_error)
	; M = integer(0)     -> R = N + integer(1)
	; N = integer(0)     -> ack(M - integer(1), integer(1), R)
	;                       ack(M - integer(1), ack(M, N - integer(1)), R) ).
```


## min

Works with

:

min

version 0.19.3

```mw
(
  :n :m
  (
    ((m 0 ==) (n 1 +))
    ((n 0 ==) (m 1 - 1 ackermann))
    ((true) (m 1 - m n 1 - ackermann ackermann))
  ) case
) :ackermann
```


## MiniScript

```mw
ackermann = function(m, n)
    if m == 0 then return n+1
    if n == 0 then return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))
end function
 
for m in range(0, 3)
    for n in range(0, 4)
        print "(" + m + ", " + n + "): " + ackermann(m, n)
    end for
end for
```


## МК-61/52

```mw
П1	<->	П0	ПП	06	С/П	ИП0	x=0	13	ИП1
1	+	В/О	ИП1	x=0	24	ИП0	1	П1	-
П0	ПП	06	В/О	ИП0	П2	ИП1	1	-	П1
ПП	06	П1	ИП2	1	-	П0	ПП	06	В/О
```


## ML/I

ML/I loves recursion, but runs out of its default amount of storage with larger numbers than those tested here!

### Program

```mw
MCSKIP "WITH" NL
"" Ackermann function
"" Will overflow when it reaches implementation-defined signed integer limit
MCSKIP MT,<>
MCINS %.
MCDEF ACK WITHS ( , )
AS <MCSET T1=%A1.
MCSET T2=%A2.
MCGO L1 UNLESS T1 EN 0
%%T2.+1.MCGO L0
%L1.MCGO L2 UNLESS T2 EN 0
ACK(%%T1.-1.,1)MCGO L0
%L2.ACK(%%T1.-1.,ACK(%T1.,%%T2.-1.))>
"" Macro ACK now defined, so try it out
a(0,0) => ACK(0,0)
a(0,1) => ACK(0,1)
a(0,2) => ACK(0,2)
a(0,3) => ACK(0,3)
a(0,4) => ACK(0,4)
a(0,5) => ACK(0,5)
a(1,0) => ACK(1,0)
a(1,1) => ACK(1,1)
a(1,2) => ACK(1,2)
a(1,3) => ACK(1,3)
a(1,4) => ACK(1,4)
a(2,0) => ACK(2,0)
a(2,1) => ACK(2,1)
a(2,2) => ACK(2,2)
a(2,3) => ACK(2,3)
a(3,0) => ACK(3,0)
a(3,1) => ACK(3,1)
a(3,2) => ACK(3,2)
a(4,0) => ACK(4,0)
```

**Output:**

```mw
a(0,0) => 1
a(0,1) => 2
a(0,2) => 3
a(0,3) => 4
a(0,4) => 5
a(0,5) => 6
a(1,0) => 2
a(1,1) => 3
a(1,2) => 4
a(1,3) => 5
a(1,4) => 6
a(2,0) => 3
a(2,1) => 5
a(2,2) => 7
a(2,3) => 9
a(3,0) => 5
a(3,1) => 13
a(3,2) => 29
a(4,0) => 13
```


## mLite

```mw
fun ackermann( 0, n ) = n + 1 
	| ( m, 0 ) = ackermann( m - 1, 1 )
	| ( m, n ) = ackermann( m - 1, ackermann(m, n - 1) )
```

Test code providing tuples from (0,0) to (3,8)

```mw
fun jota x = map (fn x = x-1) ` iota x

fun test_tuples (x, y) = append_map (fn a = map (fn b = (b, a)) ` jota x) ` jota y

map ackermann (test_tuples(4,9))
```

Result

```
[1, 2, 3, 5, 2, 3, 5, 13, 3, 4, 7, 29, 4, 5, 9, 61, 5, 6, 11, 125, 6, 7, 13, 253, 7, 8, 15, 509, 8, 9, 17, 1021, 9, 10, 19, 2045]
```


## Modula-2

```mw
MODULE ackerman;

IMPORT  ASCII, NumConv, InOut;

VAR     m, n            : LONGCARD;
        string          : ARRAY [0..19] OF CHAR;
        OK              : BOOLEAN;

PROCEDURE Ackerman (x, y   : LONGCARD) : LONGCARD;

BEGIN
  IF    x = 0  THEN  RETURN  y + 1
  ELSIF y = 0  THEN  RETURN  Ackerman (x - 1 , 1)
  ELSE
    RETURN  Ackerman (x - 1 , Ackerman (x , y - 1))
  END
END Ackerman;

BEGIN
  FOR  m := 0  TO  3  DO
    FOR  n := 0  TO  6  DO
      NumConv.Num2Str (Ackerman (m, n), 10, string, OK);
      IF  OK  THEN
        InOut.WriteString (string)
      ELSE
        InOut.WriteString ("* Error in number * ")
      END;
      InOut.Write (ASCII.HT)
    END;
    InOut.WriteLn
  END;
  InOut.WriteLn
END ackerman.
```

**Output:**

```
jan@Beryllium:~/modula/rosetta$ ackerman
1       2       3       4       5       6       7
2       3       4       5       6       7       8
3       5       7       9       11      13      15

5       13      29      61      125     253     509
```


## Modula-3

The type CARDINAL is defined in Modula-3 as [0..LAST(INTEGER)], in other words, it can hold all positive integers.

```mw
MODULE Ack EXPORTS Main;

FROM IO IMPORT Put;
FROM Fmt IMPORT Int;

PROCEDURE Ackermann(m, n: CARDINAL): CARDINAL =
  BEGIN
    IF m = 0 THEN 
      RETURN n + 1;
    ELSIF n = 0 THEN
      RETURN Ackermann(m - 1, 1);
    ELSE
      RETURN Ackermann(m - 1, Ackermann(m, n - 1));
    END;
  END Ackermann;

BEGIN
  FOR m := 0 TO 3 DO
    FOR n := 0 TO 6 DO
      Put(Int(Ackermann(m, n)) & " ");
    END;
    Put("\n");
  END;
END Ack.
```

**Output:**

```
1 2 3 4 5 6 7 
2 3 4 5 6 7 8 
3 5 7 9 11 13 15 
5 13 29 61 125 253 509 
```


## MUMPS

```mw
Ackermann(m,n)	;
	If m=0 Quit n+1
	If m>0,n=0 Quit $$Ackermann(m-1,1)
	If m>0,n>0 Quit $$Ackermann(m-1,$$Ackermann(m,n-1))
	Set $Ecode=",U13-Invalid parameter for Ackermann: m="_m_", n="_n_","

Write $$Ackermann(1,8) ; 10
Write $$Ackermann(2,8) ; 19
Write $$Ackermann(3,5) ; 253
```


## Neko

```mw
/**
 Ackermann recursion, in Neko
 Tectonics:
    nekoc ackermann.neko
    neko ackermann 4 0
*/
ack = function(x,y) {
   if (x == 0) return y+1;
   if (y == 0) return ack(x-1,1);
   return ack(x-1, ack(x,y-1));
};

var arg1 = $int($loader.args[0]);
var arg2 = $int($loader.args[1]);

/* If not given, or negative, default to Ackermann(3,4) */
if (arg1 == null || arg1 < 0) arg1 = 3;
if (arg2 == null || arg2 < 0) arg2 = 4;

try
   $print("Ackermann(", arg1, ",", arg2, "): ", ack(arg1,arg2), "\n")
catch problem
   $print("Ackermann(", arg1, ",", arg2, "): ", problem, "\n")
```

**Output:**

```
prompt$ nekoc ackermann.neko
prompt$ neko ackermann.n 3 4
Ackermann(3,4): 125

prompt$ time neko ackermann.n 4 1
Ackermann(4,1): Stack Overflow

real    0m31.475s
user    0m31.460s
sys     0m0.012s

prompt$ time neko ackermann 3 10
Ackermann(3,10): 8189

real    0m1.865s
user    0m1.862s
sys     0m0.004s
```


## Nemerle

In Nemerle, we can state the Ackermann function as a lambda. By using pattern-matching, our definition strongly resembles the mathematical notation.

```mw
using System;
using Nemerle.IO;

def ackermann(m, n) {
    def A = ackermann;
    match(m, n) {
        | (0, n) => n + 1
        | (m, 0) when m > 0 => A(m - 1, 1)
        | (m, n) when m > 0 && n > 0 => A(m - 1, A(m, n - 1))
        | _ => throw Exception("invalid inputs");
    }
}

for(mutable m = 0; m < 4; m++) {
    for(mutable n = 0; n < 5; n++) {
        print("ackermann($m, $n) = $(ackermann(m, n))\n");
    }
}
```

A terser version using implicit `match` (which doesn't use the alias `A` internally):

```mw
def ackermann(m, n) {
    | (0, n) => n + 1
    | (m, 0) when m > 0 => ackermann(m - 1, 1)
    | (m, n) when m > 0 && n > 0 => ackermann(m - 1, ackermann(m, n - 1))
    | _ => throw Exception("invalid inputs");
}
```

Or, if we were set on using the `A` notation, we could do this:

```mw
def ackermann = {
    def A(m, n) {
        | (0, n) => n + 1
        | (m, 0) when m > 0 => A(m - 1, 1)
        | (m, n) when m > 0 && n > 0 => A(m - 1, A(m, n - 1))
        | _ => throw Exception("invalid inputs");
    }
    A
}
```


## NetRexx

```mw
/* NetRexx */
options replace format comments java crossref symbols binary

numeric digits 66

parse arg j_ k_ .
if j_ = '' | j_ = '.' | \j_.datatype('w') then j_ = 3
if k_ = '' | k_ = '.' | \k_.datatype('w') then k_ = 5

loop m_ = 0 to j_
  say
  loop n_ = 0 to k_
    say 'ackermann('m_','n_') =' ackermann(m_, n_).right(5)
    end n_
  end m_
return

method ackermann(m, n) public static
  select
    when m = 0 then rval = n + 1
    when n = 0 then rval = ackermann(m - 1, 1)
    otherwise       rval = ackermann(m - 1, ackermann(m, n - 1))
    end
  return rval
```


## NewLISP

```mw
#! /usr/local/bin/newlisp

(define (ackermann m n)
  (cond ((zero? m) (inc n))
        ((zero? n) (ackermann (dec m) 1))
        (true (ackermann (- m 1) (ackermann m (dec n))))))
```

```
In case of stack overflow error, you have to start your program with a proper "-s <value>" flag
as "newlisp -s 100000 ./ackermann.lsp".
See http://www.newlisp.org/newlisp_manual.html#stack_size
```


## Nim

```mw
from strutils import parseInt

proc ackermann(m, n: int64): int64 =
  if m == 0:
    result = n + 1
  elif n == 0:
    result = ackermann(m - 1, 1)
  else:
    result = ackermann(m - 1, ackermann(m, n - 1))

proc getNumber(): int =
  try:
    result = stdin.readLine.parseInt
  except ValueError:
    echo "An integer, please!"
    result = getNumber()
  if result < 0:
    echo "Please Enter a non-negative Integer: "
    result = getNumber()

echo "First non-negative Integer please: "
let first = getNumber()
echo "Second non-negative Integer please: "
let second = getNumber()
echo "Result: ", $ackermann(first, second)
```


## Nit

Source: the official Nit’s repository.

```mw
# Task: Ackermann function
#
# A simple straightforward recursive implementation.
module ackermann_function

fun ack(m, n: Int): Int
do
	if m == 0 then return n + 1
	if n == 0 then return ack(m-1,1)
	return ack(m-1, ack(m, n-1))
end

for m in [0..3] do
	for n in [0..6] do
		print ack(m,n)
	end
	print ""
end
```

Output:

```
1
2
3
4
5
6
7

2
3
4
5
6
7
8

3
5
7
9
11
13
15

5
13
29
61
125
253
509
```


## Oberon-2

```mw
MODULE ackerman;

IMPORT  Out;

VAR     m, n    : INTEGER;

PROCEDURE Ackerman (x, y   : INTEGER) : INTEGER;

BEGIN
  IF    x = 0  THEN  RETURN  y + 1
  ELSIF y = 0  THEN  RETURN  Ackerman (x - 1 , 1)
  ELSE
    RETURN  Ackerman (x - 1 , Ackerman (x , y - 1))
  END
END Ackerman;

BEGIN
  FOR  m := 0  TO  3  DO
    FOR  n := 0  TO  6  DO
      Out.Int (Ackerman (m, n), 10);
      Out.Char (9X)
    END;
    Out.Ln
  END;
  Out.Ln
END ackerman.
```


## Objeck

Translation of

:

C#

– C sharp

```mw
class Ackermann {
  function : Main(args : String[]) ~ Nil {
    for(m := 0; m <= 3; ++m;) {
      for(n := 0; n <= 4; ++n;) {
        a := Ackermann(m, n);
        if(a > 0) {
          "Ackermann({$m}, {$n}) = {$a}"->PrintLine();
        };
      };
    };
  }
  
  function : Ackermann(m : Int, n : Int) ~ Int {
    if(m > 0) {
      if (n > 0) {
        return Ackermann(m - 1, Ackermann(m, n - 1));
      }
      else if (n = 0) {
        return Ackermann(m - 1, 1);
      };
    }
    else if(m = 0) {
      if(n >= 0) { 
        return n + 1;
      };
    };
    
    return -1;
  }
}
```

```
Ackermann(0, 0) = 1
Ackermann(0, 1) = 2
Ackermann(0, 2) = 3
Ackermann(0, 3) = 4
Ackermann(0, 4) = 5
Ackermann(1, 0) = 2
Ackermann(1, 1) = 3
Ackermann(1, 2) = 4
Ackermann(1, 3) = 5
Ackermann(1, 4) = 6
Ackermann(2, 0) = 3
Ackermann(2, 1) = 5
Ackermann(2, 2) = 7
Ackermann(2, 3) = 9
Ackermann(2, 4) = 11
Ackermann(3, 0) = 5
Ackermann(3, 1) = 13
Ackermann(3, 2) = 29
Ackermann(3, 3) = 61
Ackermann(3, 4) = 125
```


## OCaml

```mw
let rec a m n =
  if m=0 then (n+1) else
  if n=0 then (a (m-1) 1) else
  (a (m-1) (a m (n-1)))
```

or:

```mw
let rec a = function
  | 0, n -> (n+1)
  | m, 0 -> a(m-1, 1)
  | m, n -> a(m-1, a(m, n-1))
```

with memoization using an hash-table:

```mw
let h = Hashtbl.create 4001

let a m n =
  try Hashtbl.find h (m, n)
  with Not_found ->
    let res = a (m, n) in
    Hashtbl.add h (m, n) res;
    (res)
```

taking advantage of the memoization we start calling small values of **m** and **n** in order to reduce the recursion call stack:

```mw
let a m n =
  for _m = 0 to m do
    for _n = 0 to n do
      ignore(a _m _n);
    done;
  done;
  (a m n)
```

### Arbitrary precision

With arbitrary-precision integers (Big_int module):

```mw
open Big_int
let one  = unit_big_int
let zero = zero_big_int
let succ = succ_big_int
let pred = pred_big_int
let eq = eq_big_int

let rec a m n =
  if eq m zero then (succ n) else
  if eq n zero then (a (pred m) one) else
  (a (pred m) (a m (pred n)))
```

compile with:

```
ocamlopt -o acker nums.cmxa acker.ml
```

### Tail-Recursive

Here is a tail-recursive version:

```mw
let rec find_option h v =
  try Some(Hashtbl.find h v)
  with Not_found -> None

let rec a bounds caller todo m n =
  match m, n with
  | 0, n ->
      let r = (n+1) in
      ( match todo with
        | [] -> r
        | (m,n)::todo ->
            List.iter (fun k ->
              if not(Hashtbl.mem bounds k)
              then Hashtbl.add bounds k r) caller;
            a bounds [] todo m n )

  | m, 0 ->
      a bounds caller todo (m-1) 1

  | m, n ->
      match find_option bounds (m, n-1) with
      | Some a_rec ->
          let caller = (m,n)::caller in
          a bounds caller todo (m-1) a_rec
      | None ->
          let todo = (m,n)::todo
          and caller = [(m, n-1)] in
          a bounds caller todo m (n-1)

let a = a (Hashtbl.create 42 (* arbitrary *) ) [] [] ;;
```

This one uses the arbitrary precision, the tail-recursion, and the optimisation explain on the Wikipedia page about (m,n) = (3,_).

```mw
open Big_int
let one  = unit_big_int
let zero = zero_big_int
let succ = succ_big_int
let pred = pred_big_int
let add = add_big_int
let sub = sub_big_int
let eq = eq_big_int
let three = succ(succ one)
let power = power_int_positive_big_int

let eq2 (a1,a2) (b1,b2) =
  (eq a1 b1) && (eq a2 b2)

module H = Hashtbl.Make
  (struct
     type t = Big_int.big_int * Big_int.big_int
     let equal = eq2
     let hash (x,y) = Hashtbl.hash
       (Big_int.string_of_big_int x ^ "," ^
          Big_int.string_of_big_int y)
       (* probably not a very good hash function *)
   end)

let rec find_option h v =
  try Some (H.find h v)
  with Not_found -> None

let rec a bounds caller todo m n =
  let may_tail r =
    let k = (m,n) in
    match todo with
    | [] -> r
    | (m,n)::todo ->
        List.iter (fun k ->
                     if not (H.mem bounds k)
                     then H.add bounds k r) (k::caller);
        a bounds [] todo m n
  in
  match m, n with
  | m, n when eq m zero ->
      let r = (succ n) in
      may_tail r
 
  | m, n when eq n zero ->
      let caller = (m,n)::caller in
      a bounds caller todo (pred m) one
 
  | m, n when eq m three ->
      let r = sub (power 2 (add n three)) three in
      may_tail r

  | m, n ->
      match find_option bounds (m, pred n) with
      | Some a_rec ->
          let caller = (m,n)::caller in
          a bounds caller todo (pred m) a_rec
      | None ->
          let todo = (m,n)::todo in
          let caller = [(m, pred n)] in
          a bounds caller todo m (pred n)
 
let a = a (H.create 42 (* arbitrary *)) [] [] ;;

let () =
  let m, n =
    try
      big_int_of_string Sys.argv.(1),
      big_int_of_string Sys.argv.(2)
    with _ ->
      Printf.eprintf "usage: %s <int> <int>\n" Sys.argv.(0);
      exit 1
  in
  let r = a m n in
  Printf.printf "(a %s %s) = %s\n"
      (string_of_big_int m)
      (string_of_big_int n)
      (string_of_big_int r);
;;
```


## Octave

```mw
function r = ackerman(m, n)
  if ( m == 0 )
    r = n + 1;
  elseif ( n == 0 )
    r = ackerman(m-1, 1);
  else
    r = ackerman(m-1, ackerman(m, n-1));
  endif
endfunction

for i = 0:3
  disp(ackerman(i, 4));
endfor
```


## Oforth

```mw
: A( m n -- p )
   m ifZero: [ n 1+ return ]
   m 1- n ifZero: [ 1 ] else: [ A( m, n 1- ) ] A
;
```


## Ol

```mw
; simple version
(define (A m n)
    (cond
        ((= m 0) (+ n 1))
        ((= n 0) (A (- m 1) 1))
        (else (A (- m 1) (A m (- n 1))))))

(print "simple version (A 3 6): " (A 3 6))

; smart (lazy) version
(define (ints-from n)
   (cons* n (delay (ints-from (+ n 1)))))

(define (knuth-up-arrow a n b)
  (let loop ((n n) (b b))
    (cond ((= b 0) 1)
          ((= n 1) (expt a b))
          (else    (loop (- n 1) (loop n (- b 1)))))))

(define (A+ m n)
   (define (A-stream)
      (cons*
         (ints-from 1) ;; m = 0
         (ints-from 2) ;; m = 1
         ;; m = 2
         (lmap (lambda (n)
                  (+ (* 2 (+ n 1)) 1))
            (ints-from 0))
         ;; m = 3
         (lmap (lambda (n)
               (- (knuth-up-arrow 2 (- m 2) (+ n 3)) 3))
            (ints-from 0))
         ;; m = 4...
         (delay (ldrop (A-stream) 3))))
   (llref (llref (A-stream) m) n))

(print "extended version (A 3 6): " (A+ 3 6))
```

**Output:**

```
simple version (A 3 6): 509
extended version (A 3 6): 509
```


## OOC

```mw
ack: func (m: Int, n: Int) -> Int {
  if (m == 0) {
    n + 1 
  } else if (n == 0) {
    ack(m - 1, 1)
  } else {
    ack(m - 1, ack(m, n - 1)) 
  }
}

main: func {
  for (m in 0..4) {
    for (n in 0..10) {
      "ack(#{m}, #{n}) = #{ack(m, n)}" println()
    }   
  }
}
```


## ooRexx

```mw
loop m = 0 to 3
    loop n = 0 to 6
        say "Ackermann("m", "n") =" ackermann(m, n)
    end
end

::routine ackermann
  use strict arg m, n
  -- give us some precision room
  numeric digits 10000
  if m = 0 then return n + 1
  else if n = 0 then return ackermann(m - 1, 1)
  else return ackermann(m - 1, ackermann(m, n - 1))
```

**Output:**

```
Ackermann(0, 0) = 1
Ackermann(0, 1) = 2
Ackermann(0, 2) = 3
Ackermann(0, 3) = 4
Ackermann(0, 4) = 5
Ackermann(0, 5) = 6
Ackermann(0, 6) = 7
Ackermann(1, 0) = 2
Ackermann(1, 1) = 3
Ackermann(1, 2) = 4
Ackermann(1, 3) = 5
Ackermann(1, 4) = 6
Ackermann(1, 5) = 7
Ackermann(1, 6) = 8
Ackermann(2, 0) = 3
Ackermann(2, 1) = 5
Ackermann(2, 2) = 7
Ackermann(2, 3) = 9
Ackermann(2, 4) = 11
Ackermann(2, 5) = 13
Ackermann(2, 6) = 15
Ackermann(3, 0) = 5
Ackermann(3, 1) = 13
Ackermann(3, 2) = 29
Ackermann(3, 3) = 61
Ackermann(3, 4) = 125
Ackermann(3, 5) = 253
Ackermann(3, 6) = 509
```


## Order

```mw
#include <order/interpreter.h>

#define ORDER_PP_DEF_8ack ORDER_PP_FN(    \
8fn(8X, 8Y,                               \
    8cond((8is_0(8X), 8inc(8Y))           \
          (8is_0(8Y), 8ack(8dec(8X), 1))  \
          (8else, 8ack(8dec(8X), 8ack(8X, 8dec(8Y)))))))

ORDER_PP(8to_lit(8ack(3, 4)))      // 125
```


## Oz

Oz has arbitrary precision integers.

```mw
declare

  fun {Ack M N}
     if     M == 0 then N+1
     elseif N == 0 then {Ack M-1 1}
     else               {Ack M-1 {Ack M N-1}}
     end
  end

in

  {Show {Ack 3 7}}
```


## PARI/GP

Naive implementation.

```mw
A(m,n)={
  if(m,
    if(n,
      A(m-1, A(m,n-1))
    ,
      A(m-1,1)
    )
  ,
    n+1
  )
};
```


## Pascal

```mw
Program Ackerman;

function ackermann(m, n: Integer) : Integer;
begin
   if m = 0 then
      ackermann := n+1
   else if n = 0 then
      ackermann := ackermann(m-1, 1)
   else
      ackermann := ackermann(m-1, ackermann(m, n-1));
end;

var
   m, n	: Integer;

begin
   for n := 0 to 6 do
      for m := 0 to 3 do
	 WriteLn('A(', m, ',', n, ') = ', ackermann(m,n));
end.
```


## PascalABC.NET

```mw
function Ackermann(m,n: integer): integer;
begin
  if (m < 0) or (n < 0) then
    raise new System.ArgumentOutOfRangeException();
  if m = 0 then
    Result := n + 1
  else if n = 0 then
    Result := Ackermann(m - 1, 1)
  else Result := Ackermann(m - 1, Ackermann(m, n - 1))
end;

begin
  for var m := 0 to 3 do
  for var n := 0 to 4 do
    Println($'Ackermann({m}, {n}) = {Ackermann(m,n)}');
end.
```

**Output:**

```
Ackermann(0, 0) = 1
Ackermann(0, 1) = 2
Ackermann(0, 2) = 3
Ackermann(0, 3) = 4
Ackermann(0, 4) = 5
Ackermann(1, 0) = 2
Ackermann(1, 1) = 3
Ackermann(1, 2) = 4
Ackermann(1, 3) = 5
Ackermann(1, 4) = 6
Ackermann(2, 0) = 3
Ackermann(2, 1) = 5
Ackermann(2, 2) = 7
Ackermann(2, 3) = 9
Ackermann(2, 4) = 11
Ackermann(3, 0) = 5
Ackermann(3, 1) = 13
Ackermann(3, 2) = 29
Ackermann(3, 3) = 61
Ackermann(3, 4) = 125
```


## Perl

We memoize calls to *A* to make *A*(2, *n*) and *A*(3, *n*) feasible for larger values of *n*.

```mw
{
    my @memo;
    sub A {
        my( $m, $n ) = @_;
        $memo[ $m ][ $n ] and return $memo[ $m ][ $n ];
        $m or return $n + 1;
        return $memo[ $m ][ $n ] = (
            $n
               ? A( $m - 1, A( $m, $n - 1 ) )
               : A( $m - 1, 1 )
        );
    }
}
```

An implementation using the conditional statements 'if', 'elsif' and 'else':

```mw
sub A {
    my ($m, $n) = @_;
    if    ($m == 0) { $n + 1 }
    elsif ($n == 0) { A($m - 1, 1) }
    else            { A($m - 1, A($m, $n - 1)) }
}
```

An implementation using ternary chaining:

```mw
sub A {
  my ($m, $n) = @_;
  $m == 0 ? $n + 1 :
  $n == 0 ? A($m - 1, 1) :
            A($m - 1, A($m, $n - 1))
}
```

Adding memoization and extra terms:

```mw
use Memoize;  memoize('ack2');
use bigint try=>"GMP";

sub ack2 {
   my ($m, $n) = @_;
   $m == 0 ? $n + 1 :
   $m == 1 ? $n + 2 :
   $m == 2 ? 2*$n + 3 :
   $m == 3 ? 8 * (2**$n - 1) + 5 :
   $n == 0 ? ack2($m-1, 1)
           : ack2($m-1, ack2($m, $n-1));
}
print "ack2(3,4) is ", ack2(3,4), "\n";
print "ack2(4,1) is ", ack2(4,1), "\n";
print "ack2(4,2) has ", length(ack2(4,2)), " digits\n";
```

**Output:**

```
ack2(3,4) is 125
ack2(4,1) is 65533
ack2(4,2) has 19729 digits
```

An optimized version, which uses `@_` as a stack, instead of recursion. Very fast.

```mw
use strict;
use warnings;
use Math::BigInt;

use constant two => Math::BigInt->new(2);

sub ack {
	my $n = pop;
	while( @_ ) {
		my $m = pop;
		if( $m > 3 ) {
			push @_, (--$m) x $n;
			push @_, reverse 3 .. --$m;
			$n = 13;
		} elsif( $m == 3 ) {
			if( $n < 29 ) {
				$n = ( 1 << ( $n + 3 ) ) - 3;
			} else {
				$n = two ** ( $n + 3 ) - 3;
			}
		} elsif( $m == 2 ) {
			$n = 2 * $n + 3;
		} elsif( $m >= 0 ) {
			$n = $n + $m + 1;
		} else {
			die "negative m!";
		}
	}
	$n;
}
 
print "ack(3,4) is ", ack(3,4), "\n";
print "ack(4,1) is ", ack(4,1), "\n";
print "ack(4,2) has ", length(ack(4,2)), " digits\n";
```


## Phix

### native version

```
function ack(integer m, integer n)
    if m=0 then
        return n+1
    elsif m=1 then
        return n+2
    elsif m=2 then
        return 2*n+3
    elsif m=3 then
        return power(2,n+3)-3
    elsif m>0 and n=0 then
        return ack(m-1,1)
    else
        return ack(m-1,ack(m,n-1))
    end if
end function
 
constant limit = 23,
         fmtlens = {1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8}
 
atom t0 = time()
printf(1,"   0")
for j=1 to limit do
    string fmt = sprintf(" %%%dd",fmtlens[j+1])
    printf(1,fmt,j)
end for
printf(1,"\n")
for i=0 to 5 do
    printf(1,"%d:",i)
    for j=0 to iff(i>=4?5-i:limit) do
        string fmt = sprintf(" %%%dd",fmtlens[j+1])
        printf(1,fmt,{ack(i,j)})
    end for
    printf(1,"\n")
end for
```

**Output:**

```
   0  1  2  3   4   5   6    7    8    9   10    11    12    13     14     15     16      17      18      19      20       21       22       23
0: 1  2  3  4   5   6   7    8    9   10   11    12    13    14     15     16     17      18      19      20      21       22       23       24
1: 2  3  4  5   6   7   8    9   10   11   12    13    14    15     16     17     18      19      20      21      22       23       24       25
2: 3  5  7  9  11  13  15   17   19   21   23    25    27    29     31     33     35      37      39      41      43       45       47       49
3: 5 13 29 61 125 253 509 1021 2045 4093 8189 16381 32765 65533 131069 262141 524285 1048573 2097149 4194301 8388605 16777213 33554429 67108861
4: 13 65533
5: 65533
```

ack(4,2) and above fail with power function overflow. ack(3,100) will get you an answer, but only accurate to 16 or so digits.

### gmp version

Translation of

:

Go

Library:

Phix/mpfr

```
-- demo\rosetta\Ackermann.exw
include mpfr.e

procedure ack(integer m, mpz n)
    if m=0 then                 
        mpz_add_ui(n, n, 1)                     -- return n+1
    elsif m=1 then
        mpz_add_ui(n, n, 2)                     -- return n+2
    elsif m=2 then
        mpz_mul_si(n, n, 2)
        mpz_add_ui(n, n, 3)                     -- return 2*n+3
    elsif m=3 then
        if not mpz_fits_integer(n) then
            -- As per Go: 2^MAXINT would most certainly run out of memory.
            -- (think about it: a million digits is fine but pretty daft; 
            --  however a billion digits requires > addressable memory.)
            integer bn = mpz_sizeinbase(n, 2)
            throw(sprintf("A(m,n) had n of %d bits; too large",bn))
        end if
        integer ni = mpz_get_integer(n)
        mpz_set_si(n, 8)
        mpz_mul_2exp(n, n, ni) -- (n:=8*2^ni)
        mpz_sub_ui(n, n, 3)                     -- return power(2,n+3)-3
    elsif mpz_cmp_si(n,0)=0 then
        mpz_set_si(n, 1)
        ack(m-1,n)                              -- return ack(m-1,1)
    else
        mpz_sub_ui(n, n, 1)
        ack(m,n)
        ack(m-1,n)                              -- return ack(m-1,ack(m,n-1))
    end if
end procedure

constant limit = 23,
         fmtlens = {1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8},
         extras = {{3,100},{3,1e6},{4,2},{4,3}}

procedure ackermann_tests()
    atom t0 = time()
    atom n = mpz_init()
    printf(1,"   0")
    for j=1 to limit do
        string fmt = sprintf(" %%%dd",fmtlens[j+1])
        printf(1,fmt,j)
    end for
    printf(1,"\n")
    for i=0 to 5 do
        printf(1,"%d:",i)
        for j=0 to iff(i>=4?5-i:limit) do
            mpz_set_si(n, j)
            ack(i,n)
            string fmt = sprintf(" %%%ds",fmtlens[j+1])
            printf(1,fmt,{mpz_get_str(n)})
        end for
        printf(1,"\n")
    end for
    printf(1,"\n")
    for i=1 to length(extras) do
        integer {em, en} = extras[i]
        mpz_set_si(n, en)
        string res
        try
            ack(em,n)
            res = mpz_get_str(n)
            integer lr = length(res)
            if lr>50 then
                res[21..-21] = "..."
                res &= sprintf(" (%d digits)",lr)
            end if
        catch e
            -- ack(4,3), ack(5,1) and ack(6,0) all fail,
            --                   just as they should do
            res = "***ERROR***: "&e[E_USER]
        end try
        printf(1,"ack(%d,%d) %s\n",{em,en,res})
    end for     
    n = mpz_free(n)
    printf(1,"\n")
    printf(1,"ackermann_tests completed (%s)\n\n",{elapsed(time()-t0)})
end procedure

ackermann_tests()
```

**Output:**

```
   0  1  2  3   4   5   6    7    8    9   10    11    12    13     14     15     16      17      18      19      20       21       22       23
0: 1  2  3  4   5   6   7    8    9   10   11    12    13    14     15     16     17      18      19      20      21       22       23       24
1: 2  3  4  5   6   7   8    9   10   11   12    13    14    15     16     17     18      19      20      21      22       23       24       25
2: 3  5  7  9  11  13  15   17   19   21   23    25    27    29     31     33     35      37      39      41      43       45       47       49
3: 5 13 29 61 125 253 509 1021 2045 4093 8189 16381 32765 65533 131069 262141 524285 1048573 2097149 4194301 8388605 16777213 33554429 67108861
4: 13 65533
5: 65533

ack(3,100) 10141204801825835211973625643005
ack(3,1000000) 79205249834367186005...39107225301976875005 (301031 digits)
ack(4,2) 20035299304068464649...45587895905719156733 (19729 digits)
ack(4,3) ***ERROR***: A(m,n) had n of 65536 bits; too large

ackermann_tests completed (0.2s)
```


## Phixmonti

```mw
def ack
    var n var m
    
    m 0 == if
        n 1 +
    else
        n 0 == if
            m 1 - 1 ack
        else
            m 1 - m n 1 - ack ack
        endif
    endif
enddef

3 6 ack print nl
```


## PHP

```mw
function ackermann( $m , $n )
{
    if ( $m==0 )
    {
        return $n + 1;
    }
    elseif ( $n==0 )
    {
        return ackermann( $m-1 , 1 );
    }
    return ackermann( $m-1, ackermann( $m , $n-1 ) );
}

echo ackermann( 3, 4 );
// prints 125
```


## Picat

```mw
go =>
    foreach(M in 0..3)
        println([m=M,[a(M,N) : N in 0..16]])
    end,
    nl,
    printf("a2(4,1): %d\n", a2(4,1)),
    nl,
    time(check_larger(3,10000)),
    nl,
    time(check_larger(4,2)),
    nl.

% Using a2/2 and chop off large output
check_larger(M,N) => 
    printf("a2(%d,%d): ", M,N),
    A = a2(M,N).to_string,
    Len = A.len,
    if Len < 50 then
      println(A)
    else 
      println(A[1..20] ++ ".." ++ A[Len-20..Len])
    end,
    println(digits=Len).

% Plain tabled (memoized) version with guards
table
a(0, N) = N+1 => true.
a(M, 0) = a(M-1,1), M > 0 => true.
a(M, N) = a(M-1,a(M, N-1)), M > 0, N > 0 => true.

% Faster and pure function version (no guards). 
% (Based on Python example.)
table
a2(0,N) = N + 1.
a2(1,N) = N + 2.
a2(2,N) = 2*N + 3.
a2(3,N) = 8*(2**N - 1) + 5.
a2(M,N) = cond(N == 0,a2(M-1, 1), a2(M-1, a2(M, N-1))).
```

**Output:**

```
[m = 0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]]
[m = 1,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
[m = 2,[3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]
[m = 3,[5,13,29,61,125,253,509,1021,2045,4093,8189,16381,32765,65533,131069,262141,524285]]

a2(4,1): 65533

a2(3,10000): 15960504935046067079..454194438340773675005
digits = 3012
CPU time 0.02 seconds.

a2(4,2): 20035299304068464649..445587895905719156733
digits = 19729
CPU time 0.822 seconds.
```


## PicoLisp

```mw
(de ack (X Y)
   (cond
      ((=0 X) (inc Y))
      ((=0 Y) (ack (dec X) 1))
      (T (ack (dec X) (ack X (dec Y)))) ) )
```


## Piet

Rendered as wikitable:

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

ww

This is a naive implementation that does not use any optimization. Find the explanation at [[1]]. Computing the Ackermann function for (4,1) is possible, but takes quite a while because the stack grows very fast to large dimensions.

Example output:

```
   ? 3
   ? 5
   253
```


## Pike

```mw
int main(){
   write(ackermann(3,4) + "\n");
}
 
int ackermann(int m, int n){
   if(m == 0){
      return n + 1;
   } else if(n == 0){
      return ackermann(m-1, 1);
   } else {
      return ackermann(m-1, ackermann(m, n-1));
   }
}
```


## PL/I

```mw
Ackerman: procedure (m, n) returns (fixed (30)) recursive;
   declare (m, n) fixed (30);
   if m = 0 then return (n+1);
   else if m > 0 & n = 0 then return (Ackerman(m-1, 1));
   else if m > 0 & n > 0 then return (Ackerman(m-1, Ackerman(m, n-1)));
   return (0);
end Ackerman;
```


## PL/SQL

```mw
DECLARE

  FUNCTION ackermann(pi_m IN NUMBER,
                     pi_n IN NUMBER) RETURN NUMBER IS
  BEGIN
    IF pi_m = 0 THEN
      RETURN pi_n + 1;
    ELSIF pi_n = 0 THEN
      RETURN ackermann(pi_m - 1, 1);
    ELSE
      RETURN ackermann(pi_m - 1, ackermann(pi_m, pi_n - 1));
    END IF;
  END ackermann;

BEGIN
  FOR n IN 0 .. 6 LOOP
    FOR m IN 0 .. 3 LOOP
      dbms_output.put_line('A(' || m || ',' || n || ') = ' || ackermann(m, n));
    END LOOP;
  END LOOP;
END;
```

**Output:**

```
A(0,0) = 1
A(1,0) = 2
A(2,0) = 3
A(3,0) = 5
A(0,1) = 2
A(1,1) = 3
A(2,1) = 5
A(3,1) = 13
A(0,2) = 3
A(1,2) = 4
A(2,2) = 7
A(3,2) = 29
A(0,3) = 4
A(1,3) = 5
A(2,3) = 9
A(3,3) = 61
A(0,4) = 5
A(1,4) = 6
A(2,4) = 11
A(3,4) = 125
A(0,5) = 6
A(1,5) = 7
A(2,5) = 13
A(3,5) = 253
A(0,6) = 7
A(1,6) = 8
A(2,6) = 15
A(3,6) = 509
```


## Pluto

```mw
function ack(m,n)
  if m==0 then
    return n+1
  elseif n == 0 then
    return ack(m-1,1)
  else return ack(m-1,ack(m,n-1)) end
end

for i = 0,3 do
   for j = 0,8 do
      print($"A({i},{j})={ack(i,j)}")
   end
end
```

**Output:**

```
A(0,0)=1
A(0,1)=2
A(0,2)=3
A(0,3)=4
A(0,4)=5
A(0,5)=6
A(0,6)=7
A(0,7)=8
A(0,8)=9
A(1,0)=2
A(1,1)=3
A(1,2)=4
A(1,3)=5
A(1,4)=6
A(1,5)=7
A(1,6)=8
A(1,7)=9
A(1,8)=10
A(2,0)=3
A(2,1)=5
A(2,2)=7
A(2,3)=9
A(2,4)=11
A(2,5)=13
A(2,6)=15
A(2,7)=17
A(2,8)=19
A(3,0)=5
A(3,1)=13
A(3,2)=29
A(3,3)=61
A(3,4)=125
A(3,5)=253
A(3,6)=509
A(3,7)=1021
A(3,8)=2045
```


## PostScript

```mw
/ackermann{
/n exch def
/m exch def %PostScript takes arguments in the reverse order as specified in the function definition
m 0 eq{
n 1 add
}if
m 0 gt n 0 eq and
{
m 1 sub 1 ackermann
}if
m 0 gt n 0 gt and{
m 1 sub m n 1 sub ackermann ackermann
}if
}def
```

Library:

initlib

```mw
/A {
[/.m /.n] let
{
    {.m 0 eq} {.n succ} is?
    {.m 0 gt .n 0 eq and} {.m pred 1 A} is?
    {.m 0 gt .n 0 gt and} {.m pred .m .n pred A A} is?
} cond
end}.
```


## Potion

```mw
ack = (m, n):
  if (m == 0): n + 1
. elsif (n == 0): ack(m - 1, 1)
. else: ack(m - 1, ack(m, n - 1)).
.

4 times(m):
  7 times(n):
    ack(m, n) print
    " " print.
  "\n" print.
```


## PowerBASIC

```mw
FUNCTION PBMAIN () AS LONG
    DIM m AS QUAD, n AS QUAD

    m = ABS(VAL(INPUTBOX$("Enter a whole number.")))
    n = ABS(VAL(INPUTBOX$("Enter another whole number.")))

    MSGBOX STR$(Ackermann(m, n))
END FUNCTION

FUNCTION Ackermann (m AS QUAD, n AS QUAD) AS QUAD
    IF 0 = m THEN
        FUNCTION = n + 1
    ELSEIF 0 = n THEN
        FUNCTION = Ackermann(m - 1, 1)
    ELSE    ' m > 0; n > 0
        FUNCTION = Ackermann(m - 1, Ackermann(m, n - 1))
    END IF
END FUNCTION
```


## PowerShell

Translation of

:

PHP

```mw
function ackermann ([long] $m, [long] $n) {
    if ($m -eq 0) {
        return $n + 1
    }
    
    if ($n -eq 0) {
        return (ackermann ($m - 1) 1)
    }
    
    return (ackermann ($m - 1) (ackermann $m ($n - 1)))
}
```

Building an example table (takes a while to compute, though, especially for the last three numbers; also it fails with the last line in Powershell v1 since the maximum recursion depth is only 100 there):

```mw
foreach ($m in 0..3) {
    foreach ($n in 0..6) {
        Write-Host -NoNewline ("{0,5}" -f (ackermann $m $n))
    }
    Write-Host
}
```

**Output:**

```
    1    2    3    4    5    6    7
    2    3    4    5    6    7    8
    3    5    7    9   11   13   15
    5   13   29   61  125  253  509
```

### A More "PowerShelly" Way

```mw
function Get-Ackermann ([int64]$m, [int64]$n)
{
    if ($m -eq 0)
    {
        return $n + 1
    }
 
    if ($n -eq 0)
    {
        return Get-Ackermann ($m - 1) 1
    }
 
    return (Get-Ackermann ($m - 1) (Get-Ackermann $m ($n - 1)))
}
```

Save the result to an array (for possible future use?), then display it using the `Format-Wide` cmdlet:

```mw
$ackermann = 0..3 | ForEach-Object {$m = $_; 0..6 | ForEach-Object {Get-Ackermann $m  $_}}

$ackermann | Format-Wide {"{0,3}" -f $_} -Column 7 -Force
```

**Output:**

```
  1                   2                  3                  4                  5                  6                  7               
  2                   3                  4                  5                  6                  7                  8               
  3                   5                  7                  9                 11                 13                 15               
  5                  13                 29                 61                125                253                509               
```


## Processing

```mw
int ackermann(int m, int n) {
  if (m == 0)
    return n + 1;
  else if (m > 0 && n == 0)
    return ackermann(m - 1, 1);
  else
    return ackermann( m - 1, ackermann(m, n - 1) );
}

// Call function to produce output:
// the first 4x7 Ackermann numbers
void setup() {
  for (int m=0; m<4; m++) {
    for (int n=0; n<7; n++) {
      print(ackermann(m, n), " ");
    }
    println();
  }
}
```

**Output:**

```
1  2  3  4  5  6  7
2  3  4  5  6  7  8
3  5  7  9  11  13  15
5  13  29  61  125  253  509
```

### Processing Python mode

Python is not very adequate for deep recursion, so even setting sys.setrecursionlimit(1000000000) if m = 5 it throws 'maximum recursion depth exceeded'

```mw
from __future__ import print_function

def setup():
    for m in range(4):
        for n in range(7):
            print("{} ".format(ackermann(m, n)), end = "")
        print()
    # print('finished')

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
```

### Processing.R

Processing.R may exceed its stack depth at ~n==6 and returns null.

```mw
setup <- function() {
  for (m in 0:3) {
    for (n in 0:4) {
      stdout$print(paste(ackermann(m, n), " "))
    }
    stdout$println("")
  }
}

ackermann <- function(m, n) {
  if ( m == 0 ) {
    return(n+1)
  } else if ( n == 0 ) {
    ackermann(m-1, 1)
  } else {
    ackermann(m-1, ackermann(m, n-1))
  }
}
```

**Output:**

```
1  2  3  4  5  
2  3  4  5  6  
3  5  7  9  11  
5  13  29  61  125
```


## Prolog

Works with

:

SWI Prolog

```mw
:- table ack/3. % memoization reduces the execution time of ack(4,1,X) from several
                % minutes to about one second on a typical desktop computer.
ack(0, N, Ans) :- Ans is N+1.
ack(M, 0, Ans) :- M>0, X is M-1, ack(X, 1, Ans).
ack(M, N, Ans) :- M>0, N>0, X is M-1, Y is N-1, ack(M, Y, Ans2), ack(X, Ans2, Ans).
```

"Pure" Prolog Version (Uses Peano arithmetic instead of is/2):

```mw
ack(0,N,s(N)).
ack(s(M),0,P):- ack(M,s(0),P).
ack(s(M),s(N),P):- ack(s(M),N,S), ack(M,S,P).

% Peano's first axiom in Prolog is that s(0) AND s(s(N)):- s(N)
% Thanks to this we don't need explicit N > 0 checks.
% Nor explicit arithmetic operations like X is M-1.
% Recursion and unification naturally decrement s(N) to N.
% But: Prolog clauses are relations and cannot be replaced by their result, like functions.
% Because of this we do need an extra argument to hold the output of the function.
% And we also need an additional call to the function in the last clause.

% Example input/output:
% ?- ack(s(0),s(s(0)),P).
% P = s(s(s(s(0)))) ;
% false.
```


## Pure

```mw
A 0 n = n+1;
A m 0 = A (m-1) 1 if m > 0;
A m n = A (m-1) (A m (n-1)) if m > 0 && n > 0;
```
