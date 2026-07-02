---
title: "Fibonacci sequence (part 4/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/10
---

## Delphi

### Iterative

```mw
function FibonacciI(N: Word): UInt64;
var
  Last, New: UInt64;
  I: Word;
begin
  if N < 2 then
    Result := N
  else begin
    Last := 0;
    Result := 1;
    for I := 2 to N do
    begin
      New := Last + Result;
      Last := Result;
      Result := New;
    end;
  end;
end;
```

### Recursive

```mw
function Fibonacci(N: Word): UInt64;
begin
  if N < 2 then
    Result := N
  else
   Result := Fibonacci(N - 1) + Fibonacci(N - 2);
end;
```

### Matrix

Algorithm is based on

${\displaystyle {\begin{pmatrix}1&1\\1&0\end{pmatrix}}^{n}={\begin{pmatrix}F(n+1)&F(n)\\F(n)&F(n-1)\end{pmatrix}}}$

.

```mw
function fib(n: Int64): Int64;

  type TFibMat = array[0..1] of array[0..1] of Int64;
   
  function FibMatMul(a,b: TFibMat): TFibMat;
  var i,j,k: integer;
      tmp: TFibMat;
  begin
    for i := 0 to 1 do
      for j := 0 to 1 do
      begin
   tmp[i,j] := 0;
   for k := 0 to 1 do tmp[i,j] := tmp[i,j] + a[i,k] * b[k,j];
      end;
    FibMatMul := tmp;
  end;
   
  function FibMatExp(a: TFibMat; n: Int64): TFibmat;
  begin
    if n <= 1 then fibmatexp := a
    else if (n mod 2 = 0) then FibMatExp := FibMatExp(FibMatMul(a,a), n div 2)
    else if (n mod 2 = 1) then FibMatExp := FibMatMul(a, FibMatExp(FibMatMul(a,a), n div 2));
  end;

var 
  matrix: TFibMat;
   
begin
  matrix[0,0] := 1;
  matrix[0,1] := 1;
  matrix[1,0] := 1;
  matrix[1,1] := 0;
  if n > 1 then
    matrix := fibmatexp(matrix,n-1);
  fib := matrix[0,0];
end;
```


## DIBOL-11

```mw
    ;     Redone to include the first two values that
    ;     are noot computed.

      START    ;First 15 Fibonacci NUmbers

      RECORD
              FIB1,    D10,   0
              FIB2,    D10,   1
              FIBNEW,  D10
              LOOPCNT, D2,    3

       RECORD HEADER
,            A32, "First 15 Fibonacci Numbers."

       RECORD OUTPUT
             LOOPOUT, A2
,         A3, " : "
              FIBOUT, A10

      PROC

      OPEN(8,O,'TT:')

      WRITES(8,HEADER)

;   The First Two are given.

        FIBOUT = 0
        LOOPOUT = 1
      WRITES(8,OUTPUT)
        FIBOUT = 1
        LOOPOUT = 2
      WRITES(8,OUTPUT)

;   The Rest are Computed.
      
     LOOP,
             FIBNEW = FIB1 + FIB2
             LOOPOUT = LOOPCNT, 'ZX'
             FIBOUT = FIBNEW, 'ZZZZZZZZZX'

             WRITES(8,OUTPUT)

             FIB1 = FIB2
             FIB2 = FIBNEW
             
             LOOPCNT = LOOPCNT + 1
             IF LOOPCNT .LE. 15 GOTO LOOP

             CLOSE 8
             END
```


## DuckDB

Works with

:

DuckDB

version V1.1

Works with

:

DuckDB

version V1.0

DuckDB cannot process any of the programs presented in the #SQL entry on this page without alterations, but only small changes are typically required. For this entry, three of the snippets have been adapted for DuckDB; in each case, a brief explanation of the required changes is also provided.

### Part 1: Recursive CTE

The following is almost identical to the code shown in the **Recursive** section within the #SQL entry. The function signature had to be altered, and the keyword RECURSIVE added; the `order by` was added to ensure the results have the expected order.

```mw
create or replace function fib_to(n) as table (
  with recursive fib(e,f) as (
  select 1, 1 
    union all
    select e+f,e from fib
    where e <= n)
  select f from fib
  order by f
);

from fib_to(55);
```

**Output:**

```
┌───────┐
│   f   │
│ int32 │
├───────┤
│     1 │
│     1 │
│     2 │
│     3 │
│     5 │
│     8 │
│    13 │
│    21 │
│    34 │
│    55 │
└───────┘
```

### Part 2: Analytic formula

The first line of the SELECT statement given in the "As a power" subsection of the "Analytic" section of the #SQL entry requires no alteration for the following adaptation, but the FROM and CONNECT lines must be altered as DuckDB has no DUAL table.

```mw
select round ( power( ( 1 + sqrt( 5 ) ) / 2, level ) / sqrt( 5 ) ) fib
from range(1,11) t(level);
```

**Output:**

```
┌────────┐
│  fib   │
│ double │
├────────┤
│    1.0 │
│    1.0 │
│    2.0 │
│    3.0 │
│    5.0 │
│    8.0 │
│   13.0 │
│   21.0 │
│   34.0 │
│   55.0 │
└────────┘
```

### Part 3: Recursive CTE for PostgreSQL

Only three lines of the program for PostgreSQL as shown in the #SQL entry had to be changed for DuckDB:

- the signature of the function (the two lines with $$ signs);
- the initialization line: `SELECT 0., 1.`

However, although the resulting program produces the correct result for fib(100), it would be better not to assume the insertion order is preserved during construction of the recursive table.

At any rate, here is the modified program, minus the comments. The initalization line has been changed simply to:

```mw
SELECT 0::UHUGEINT, 1::UHUGEINT
```

but there are other possibilities, e.g. specifying the type as DOUBLE would allow greater range.

```mw
# Warning: the following program has been naively adapted from the PostgresQL but 
# should be further modified to ensure correctness, e.g. by adding a counter
CREATE or replace FUNCTION fib(n) AS (
    WITH RECURSIVE fibonacci(current, previous) AS (

    SELECT 0::UHUGEINT, 1::UHUGEINT
    -- another possibility: SELECT 0::FLOAT, 1::FLOAT
    UNION ALL
        SELECT previous + current, current FROM fibonacci
    )
    SELECT current FROM fibonacci
    LIMIT 1 OFFSET n
);

# Example
select fib(100);
```

**Output:**

```
┌───────────────────────┐
│       fib(100)        │
│        uint128        │
├───────────────────────┤
│ 354224848179261915075 │
└───────────────────────┘
```


## DWScript

```mw
function fib(N : Integer) : Integer;
begin
  if N < 2 then Result := 1
  else Result := fib(N-2) + fib(N-1);
End;
```


## Dyalect

```mw
func fib(n) {
    if n < 2 {
        return n
    } else {
        return fib(n - 1) + fib(n - 2)
    }
}

print(fib(30))
```


## E

```mw
def fib(n) {
    var s := [0, 1]
    for _ in 0..!n { 
        def [a, b] := s
        s := [b, a+b]
    }
    return s[0]
}
```

(This version defines fib(0) = 0 because OEIS A000045 does.)


## EasyLang

```mw
func fib n .
   if n < 2 : return n
   val = 1
   for i = 2 to n
      h = prev + val
      prev = val
      val = h
   .
   return val
.
print fib 36
```

Recursive (inefficient):

```mw
func fib n .
   if n < 2 : return n
   return fib (n - 2) + fib (n - 1)
.
print fib 36
```


## EchoLisp

Use **memoization** with the recursive version.

```mw
(define (fib n) 
    (if (< n 2) n 
    (+ (fib (- n 2)) (fib (1- n)))))

(remember 'fib #(0 1))

(for ((i 12)) (write (fib i)))
0 1 1 2 3 5 8 13 21 34 55 89
```


## ECL

### Analytic

```mw
//Calculates Fibonacci sequence up to n steps using Binet's closed form solution

FibFunction(UNSIGNED2 n) := FUNCTION
   REAL Sqrt5 := Sqrt(5); 
   REAL Phi := (1+Sqrt(5))/2;
   REAL Phi_Inv := 1/Phi; 
   UNSIGNED FibValue := ROUND( ( POWER(Phi,n)-POWER(Phi_Inv,n) ) /Sqrt5); 
   RETURN FibValue; 
   END;  

 FibSeries(UNSIGNED2 n) := FUNCTION
 
 Fib_Layout := RECORD
 UNSIGNED5 FibNum;
 UNSIGNED5 FibValue; 
 END; 
 
 FibSeq := DATASET(n+1,
  TRANSFORM 
 ( Fib_Layout 
 , SELF.FibNum := COUNTER-1
 , SELF.FibValue := IF(SELF.FibNum<2,SELF.FibNum, FibFunction(SELF.FibNum) )
 ) 
 ); 
 
 RETURN FibSeq; 
 
 END; }
```


## EDSAC order code

This program calculates the *n*th—by default the tenth—number in the Fibonacci sequence and displays it (in binary) in the first word of storage tank 3.

```mw
[ Fibonacci sequence
  ==================
  
  A program for the EDSAC
  
  Calculates the nth Fibonacci
  number and displays it at the
  top of storage tank 3
  
  The default value of n is 10
  
  To calculate other Fibonacci
  numbers, set the starting value
  of the count to n-2
  
  Works with Initial Orders 2 ]

        T56K  [ set load point  ]
        GK    [ set theta       ]
        
[ Orders ]

[  0 ]  T20@  [ a = 0           ]
        A17@  [ a += y          ]
        U18@  [ temp = a        ]
        A16@  [ a += x          ]
        T17@  [ y = a; a = 0    ]
        A18@  [ a += temp       ]
        T16@  [ x = a; a = 0    ]
        
        A19@  [ a = count       ]
        S15@  [ a -= 1          ]
        U19@  [ count = a       ]
        E@    [ if a>=0 go to θ ]
        
        T20@  [ a = 0           ]
        A17@  [ a += y          ]
        T96F  [ C(96) = a; a = 0]
        
        ZF    [ halt ]
        
[ Data ]
        
[ 15 ]  P0D   [ const: 1        ]
[ 16 ]  P0F   [ var: x = 0      ]
[ 17 ]  P0D   [ var: y = 1      ]
[ 18 ]  P0F   [ var: temp = 0   ]
[ 19 ]  P4F   [ var: count = 8  ]
[ 20 ]  P0F   [ used to clear a ]

        EZPF  [ begin execution ]
```

**Output:**

```
00000000000110111
```


## Eiffel

```mw
class
   APPLICATION

create
   make

feature

   fibonacci (n: INTEGER): INTEGER
      require
         non_negative: n >= 0
      local
         i, n2, n1, tmp: INTEGER
      do
         n2 := 0
         n1 := 1
         from
            i := 1
         until
            i >= n
         loop
            tmp := n1
            n1 := n2 + n1
            n2 := tmp
            i := i + 1
         end
         Result := n1
         if n = 0 then
            Result := 0
         end
      end

feature {NONE} -- Initialization

   make
         -- Run application.
      do
         print (fibonacci (0))
         print (" ")
         print (fibonacci (1))
         print (" ")
         print (fibonacci (2))
         print (" ")
         print (fibonacci (3))
         print (" ")
         print (fibonacci (4))
         print ("%N")
      end

end
```


## Ela

Tail-recursive function:

```mw
fib = fib' 0 1           
      where fib' a b 0 = a                 
            fib' a b n = fib' b (a + b) (n - 1)
```

Infinite (lazy) list:

```mw
fib = fib' 1 1
      where fib' x y = & x :: fib' y (x + y)
```


## Elena

Translation of

:

Smalltalk

ELENA 6.x :

```mw
import extensions;
 
fibu(n)
{
    int[] ac := new int[]{ 0,1 };
    if (n < 2) 
    {
        ^ ac[n] 
    }
    else
    {
        for(int i := 2; i <= n; i+=1)
        {
            int t := ac[1];
            ac[1] := ac[0] + ac[1];
            ac[0] := t
        };
 
        ^ ac[1]
    }
}
 
public Program()
{
    for(int i := 0; i <= 10; i+=1)
    {
        Console.printLine(fibu(i))
    }
}
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

### Alternative version using yieldable method

```mw
import extensions;

singleton FibonacciEnumerable : Enumerable
{
   Enumerator enumerator()
      = FibonacciEnumerable.infinitEnumerator();

   yield Enumerator infinitEnumerator()
   {
        long n_2 := 1l; 
        long n_1 := 1l;

        :yield n_2;             
        :yield n_1;

        while(true)
        {
            long n := n_2 + n_1;

            :yield n;

            n_2 := n_1;
            n_1 := n
        }
   }
}

public Program()
{
    auto e := FibonacciEnumerable.enumerator();
    
    if(!e.next())
       InvalidOperationException.raise();
    
    for(int i := 0; i < 10 && e.next(); i += 1) {
        Console.printLine(*e)
    };
    
    Console.readChar()
}
```


## Elixir

```mw
defmodule Fibonacci do
    def fib(0), do: 0
    def fib(1), do: 1
    def fib(n), do: fib(0, 1, n-2)
    
    def fib(_, prv, -1), do: prv
    def fib(prvprv, prv, n) do
        next = prv + prvprv
        fib(prv, next, n-1)
    end
end

IO.inspect Enum.map(0..10, fn i-> Fibonacci.fib(i) end)
```

Using Stream:

```mw
Stream.unfold({0,1}, fn {a,b} -> {a,{b,a+b}} end) |> Enum.take(10)
```

**Output:**

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```


## Elm

Naïve recursive implementation.

```mw
fibonacci : Int -> Int
fibonacci n = if n < 2 then
        n
    else
        fibonacci(n - 2) + fibonacci(n - 1)
```

**version 2**

```mw
fib : Int -> number
fib n =
   case n of
      0 -> 0
      1 -> 1
      _ -> fib (n-1) + fib (n-2)
```

**Output:**

```
elm repl
> fib 40
102334155 : number

> List.map (\elem -> fib elem) (List.range 1 40)
[1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,
4181,6765,10946,17711,28657,46368,75025,121393,196418,
317811,514229,832040,1346269,2178309,3524578,5702887,
9227465,14930352,24157817,39088169,63245986,102334155]
    : List number
```


## Emacs Lisp

### version 1

```mw
(defun fib (n a b c)
  (cond
   ((< c n) (fib n b (+ a b) (+ 1 c)))
   ((= c n) b)
   (t a)))

(defun fibonacci (n)
  (if (< n 2)
      n
    (fib n 0 1 1)))
```

### version 2

```mw
(defun fibonacci (n)
  (let (vec i j k)
    (if (< n 2)
        n
      (setq vec (make-vector (+ n 1) 0)
            i 0
            j 1
            k 2)
      (setf (aref vec 1) 1)
      (while (<= k n)
        (setf (aref vec k) (+ (elt vec i) (elt vec j)))
        (setq i (1+ i)
              j (1+ j)
              k (1+ k)))
      (elt vec n))))
```

**Eval:**

```mw
(insert
 (mapconcat (lambda (n) (format "%d" (fibonacci n)))
            (number-sequence 0 15) " "))
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
```


## Erlang

### Recursive

```mw
-module(fib).
-export([fib/1]).

fib(0) -> 0;
fib(1) -> 1;
fib(N) -> fib(N-1) + fib(N-2).
```

### Iterative

```mw
-module(fiblin).
-export([fib/1])

fib(0) -> 0;
fib(1) -> 1;
fib(2) -> 1;
fib(3) -> 2;
fib(4) -> 3;
fib(5) -> 5;

fib(N) when is_integer(N) -> fib(N - 6, 5, 8).
fib(N, A, B) -> if N < 1 -> B; true -> fib(N-1, B, A+B) end.
```

**Evaluate:**

```mw
io:write([fiblin:fib(X) || X <- lists:seq(1,10) ]).
```

**Output:**

```
   
[1,1,2,3,5,8,13,21,34,55]ok
```

### Iterative 2

```mw
fib(N) -> fib(N, 0, 1).

fib(0, Result, _Next) -> Result;
fib(Iter, Result, Next) -> fib(Iter-1, Next, Result+Next).
```


## ERRE

```mw
!-------------------------------------------
! derived from my book "PROGRAMMARE IN ERRE"
! iterative solution
!-------------------------------------------

PROGRAM FIBONACCI

!$DOUBLE

!VAR F1#,F2#,TEMP#,COUNT%,N%

BEGIN    !main
   INPUT("Number",N%)
   F1=0
   F2=1
   REPEAT
      TEMP=F2
      F2=F1+F2
      F1=TEMP
      COUNT%=COUNT%+1
   UNTIL COUNT%=N%
   PRINT("FIB(";N%;")=";F2)

   ! Obviously a FOR loop or a WHILE loop can
   ! be used to solve this problem

END PROGRAM
```

**Output:**

```
Number? 20
FIB( 20 )= 6765
```


## Euphoria

### 'Recursive' version

Works with

:

Euphoria

version any version

```mw
function fibor(integer n)
  if n<2 then return n end if
  return fibor(n-1)+fibor(n-2)
end function
```

### 'Iterative' version

Works with

:

Euphoria

version any version

```mw
function fiboi(integer n)
integer f0=0, f1=1, f  
  if n<2 then return n end if
  for i=2 to n do
    f=f0+f1
    f0=f1
    f1=f   
  end for
  return f
end function
```

### 'Tail recursive' version

Works with

:

Euphoria

version 4.0.0

```mw
function fibot(integer n, integer u = 1, integer s = 0)
  if n < 1 then
    return s
  else
    return fibot(n-1,u+s,u)
  end if
end function

-- example:
? fibot(10) -- says 55
```

### 'Paper tape' version

Works with

:

Euphoria

version 4.0.0

```mw
include std/mathcons.e -- for PINF constant

enum ADD, MOVE, GOTO, OUT, TEST, TRUETO

global sequence tape = { 0, 
          1, 
             { ADD, 2, 1 }, 
             { TEST, 1, PINF }, 
             { TRUETO, 0 }, 
             { OUT, 1, "%.0f\n" }, 
             { MOVE, 2, 1 }, 
             { MOVE, 0, 2 }, 
             { GOTO, 3  } }

global integer ip
global integer test
global atom accum

procedure eval( sequence cmd )
   atom i = 1
   while i <= length( cmd ) do
      switch cmd[ i ] do
         case ADD then
            accum = tape[ cmd[ i + 1 ] ] + tape[ cmd[ i + 2 ] ]
            i += 2

         case OUT then
            printf( 1, cmd[ i + 2], tape[ cmd[ i + 1 ] ] ) 
            i += 2

         case MOVE then
            if cmd[ i + 1 ] = 0 then
               tape[ cmd[ i + 2 ] ] = accum
            else
               tape[ cmd[ i + 2 ] ] = tape[ cmd[ i + 1 ] ]
            end if
            i += 2

         case GOTO then
            ip = cmd[ i + 1 ] - 1 -- due to ip += 1 in main loop
            i += 1

         case TEST then
            if tape[ cmd[ i + 1 ] ] = cmd[ i + 2 ] then
               test = 1
            else
               test = 0
            end if
            i += 2

         case TRUETO then
            if test then
               if cmd[ i + 1 ] = 0 then
                  abort(0)
               else
                  ip = cmd[ i + 1 ] - 1
               end if
            end if

      end switch
      i += 1
   end while
end procedure

test = 0
accum = 0
ip = 1

while 1 do

   -- embedded sequences (assumed to be code) are evaluated
   -- atoms (assumed to be data) are ignored

   if sequence( tape[ ip ] ) then
      eval( tape[ ip ] ) 
   end if
   ip += 1
end while
```


## Excel

### LAMBDA

Binding the name FIBONACCI to the following lambda in the Excel worksheet Name Manager:

(See The LAMBDA worksheet function)

Works with

:

Office 365 Betas 2021

```mw
FIBONACCI
=LAMBDA(n,
    APPLYN(n - 2)(
        LAMBDA(xs,
            APPENDROWS(xs)(
                SUM(
                    LASTNROWS(2)(xs)
                )
            )
        )
    )({1;1})
)
```

And assuming that the following names are also bound to reusable generic lambdas in the Name manager:

```mw
APPENDROWS
=LAMBDA(xs,
    LAMBDA(ys,
        LET(
            nx, ROWS(xs),
            rowIndexes, SEQUENCE(nx + ROWS(ys)),
            colIndexes, SEQUENCE(
                1,
                MAX(COLUMNS(xs), COLUMNS(ys))
            ),

            IFERROR(
                IF(rowIndexes <= nx,
                    INDEX(xs, rowIndexes, colIndexes),
                    INDEX(ys, rowIndexes - nx, colIndexes)
                ),
                NA()
            )
        )
    )
)

APPLYN
=LAMBDA(n,
    LAMBDA(f,
        LAMBDA(x,
            IF(0 < n,
                APPLYN(n - 1)(f)(
                    f(x)
                ),
                x
            )
        )
    )
)

LASTNROWS
=LAMBDA(n,
    LAMBDA(xs,
        LET(
            nRows, COUNTA(xs),
            x, MIN(nRows, n),

            IF(0 < n,
                INDEX(
                    xs,
                    SEQUENCE(
                        x, 1,
                        1 + nRows - x,  1
                    )
                ),
                NA()
            )
        )
    )
)
```

**Output:**

The FIBONACCI(n) lambda defines a column of integers.

Here we obtain a row, by composing FIBONACCI with the built-in TRANSPOSE function:

fx

=TRANSPOSE(FIBONACCI(15))

A

B

C

D

E

F

G

H

I

J

K

L

M

N

O

P

1

2

15 Fibonacci terms:

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

Or as a fold, obtaining just the Nth term of the Fibonacci series:

```mw
FIBONACCI2
=LAMBDA(n,
    INDEX(
        FOLDL(
            LAMBDA(ab,
                LAMBDA(_,
                    APPEND(INDEX(ab, 2))(SUM(ab))
                )
            )
        )({0;1})(
            ENUMFROMTO(1)(n)
        ),
        1
    )
)
```

Assuming the following generic bindings in the Excel worksheet Name manager:

```mw
APPEND
=LAMBDA(xs,
    LAMBDA(ys,
        LET(
            nx, ROWS(xs),
            rowIndexes, SEQUENCE(nx + ROWS(ys)),
            colIndexes, SEQUENCE(
                1,
                MAX(COLUMNS(xs), COLUMNS(ys))
            ),
            IF(rowIndexes <= nx,
                INDEX(xs, rowIndexes, colIndexes),
                INDEX(ys, rowIndexes - nx, colIndexes)
            )
        )
    )
)

ENUMFROMTO
=LAMBDA(a,
    LAMBDA(z,
        SEQUENCE(1 + z - a, 1, a, 1)
    )
)

FOLDL
=LAMBDA(op,
    LAMBDA(a,
        LAMBDA(xs,
            IF(
                2 > ROWS(xs),
                op(a)(xs),
                FOLDL(op)(
                    op(a)(
                        HEAD(xs)
                    )
                )(
                    TAIL(xs)
                )
            )
        )
    )
)

HEAD
=LAMBDA(xs,
    INDEX(xs, 1, SEQUENCE(1, COLUMNS(xs)))
)

TAIL
=LAMBDA(xs,
    INDEX(
        xs,
        SEQUENCE(ROWS(xs) - 1, 1, 2, 1),
        SEQUENCE(1, COLUMNS(xs))
    )
)
```

**Output:**

|   | fx | =FIBONACCI2(A2) |
|---|---|---|
|   | A | B |
| 1 | N | Fibonacci |
| 2 | 32 | 2178309 |
| 3 | 64 | 10610209857723 |


## F

This is a fast [tail-recursive] approach using the F# big integer support:

```mw
let fibonacci n : bigint =
  let rec f a b n =
    match n with
    | 0 -> a
    | 1 -> b
    | n -> (f b (a + b) (n - 1))
  f (bigint 0) (bigint 1) n
> fibonacci 100;;
val it : bigint = 354224848179261915075I
```

Lazy evaluated using sequence workflow:

```mw
let rec fib = seq { yield! [0;1];
                    for (a,b) in Seq.zip fib (Seq.skip 1 fib) -> a+b}
```

The above is extremely slow due to the nested recursions on sequences, which aren't very efficient at the best of times. The above takes seconds just to compute the 30th Fibonacci number!

Lazy evaluation using the sequence unfold anamorphism is much much better as to efficiency:

```mw
let fibonacci = Seq.unfold (fun (x, y) -> Some(x, (y, x + y))) (0I,1I)
fibonacci |> Seq.nth 10000
```

Approach similar to the Matrix algorithm in C#, with some shortcuts involved. Since it uses exponentiation by squaring, calculations of fib(n) where n is a power of 2 are particularly quick. Eg. fib(2^20) was calculated in a little over 4 seconds on this poster's laptop.

```mw
open System
open System.Diagnostics
open System.Numerics

/// Finds the highest power of two which is less than or equal to a given input.
let inline prevPowTwo (x : int) =
    let mutable n = x
    n <- n - 1
    n <- n ||| (n >>> 1)
    n <- n ||| (n >>> 2)
    n <- n ||| (n >>> 4)
    n <- n ||| (n >>> 8)
    n <- n ||| (n >>> 16)
    n <- n + 1
    match x with
    | x when x = n -> x
    | _ -> n/2

/// Evaluates the nth Fibonacci number using matrix arithmetic and
/// exponentiation by squaring.
let crazyFib (n : int) =
    let powTwo = prevPowTwo n

    /// Applies 2n rule repeatedly until another application of the rule would
    /// go over the target value (or the target value has been reached).
    let rec iter1 i q r s =
        match i with
        | i when i < powTwo ->
            iter1 (i*2) (q*q + r*r) (r * (q+s)) (r*r + s*s)
        | _ -> i, q, r, s

    /// Applies n+1 rule until the target value is reached.
    let rec iter2 (i, q, r, s) =
        match i with
        | i when i < n -> 
            iter2 ((i+1), (q+r), q, r)
        | _ -> q

    match n with
    | 0 -> 1I
    | _ ->
        iter1 1 1I 1I 0I
        |> iter2
```


## Factor

### Combinatory

```mw
! produce the nth fib
: fib ( n -- fib )     1 0 rot [ tuck + ]      times     drop ; inline

! produce a list of the first n fibs
: fibseq ( n -- fibs ) 1 0 rot [ [ + ] 2keep ] replicate 2nip ; inline
```

### Iterative

```mw
: fib ( n -- m )
    dup 2 < [
        [ 0 1 ] dip [ swap [ + ] keep ] times
        drop
    ] unless ;
```

### Recursive

```mw
: fib ( n -- m )
    dup 2 < [
        [ 1 - fib ] [ 2 - fib ] bi +
    ] unless ;
```

### Tail-Recursive

```mw
: fib2 ( x y n -- a )
  dup 1 <
    [ 2drop ]
    [ [ swap [ + ] keep ] dip 1 - fib2 ]
  if ;
: fib ( n -- m ) [ 0 1 ] dip fib2 ;
```

### Matrix

Translation of

:

Ruby

```mw
USE: math.matrices

: fib ( n -- m )
    dup 2 < [
        [ { { 0 1 } { 1 1 } } ] dip 1 - m^n
        second second
    ] unless ;
```


## Falcon

### Iterative

```mw
function fib_i(n)

    if n < 2: return n

    fibPrev = 1
    fib = 1
    for i in [2:n]
        tmp = fib
        fib += fibPrev
        fibPrev = tmp
    end
    return fib
end
```

### Recursive

```mw
function fib_r(n)
    if n < 2 :  return n
    return fib_r(n-1) + fib_r(n-2)
end
```

### Tail Recursive

```mw
function fib_tr(n)
    return fib_aux(n,0,1)       
end
function fib_aux(n,a,b)
   switch n
      case 0 : return a
      default: return fib_aux(n-1,a+b,a)
   end
end
```


## FALSE

```mw
[[$0=~][1-@@\$@@+\$44,.@]#]f:
20n: {First 20 numbers}
0 1 n;f;!%%44,. {Output: "0,1,1,2,3,5..."}
```


## Fancy

```mw
class Fixnum {
  def fib {
    match self -> {
      case 0 -> 0
      case 1 -> 1
      case _ -> self - 1 fib + (self - 2 fib)
    }
  }
}

15 times: |x| {
  x fib println
}
```


## Fantom

Ints have a limit of 64-bits, so overflow errors occur after computing Fib(92) = 7540113804746346429.

```mw
class Main
{
  static Int fib (Int n) 
  {
    if (n < 2) return n
    fibNums := [1, 0]
    while (fibNums.size <= n)
    {
      fibNums.insert (0, fibNums[0] + fibNums[1])
    }
    return fibNums.first
  }

  public static Void main ()
  {
    20.times |n| 
    {
      echo ("Fib($n) is ${fib(n)}")
    }
  }
}
```


## Fe

Recursive:

```mw
(= fib (fn (n)
  (if (< n 2) n
    (+ (fib (- n 1)) (fib (- n 2))))))
```

Iterative:

```mw
(= fib (fn (n)
  (let p0 0)
  (let p1 1)
  (while (< 0 n)
    (= n (- n 1))
    (let tmp (+ p0 p1)) 
    (= p0 p1)
    (= p1 tmp))
  p0))
```


## Fermat

```mw
Func Fibonacci(n) = if n<0 then -(-1)^n*Fibonacci(-n) else if n<2 then n else 
    Array fib[n+1];
    fib[1] := 0;
    fib[2] := 1;
    for i = 2, n do 
    fib[i+1]:=fib[i]+fib[i-1]
    od;
    Return(fib[n+1]);
    fi;
    fi;
    .
```


## Fexl

```mw
# (fib n) = the nth Fibonacci number
\fib=
    (
    \loop==
        (\x\y\n
        le n 0 x;
        \z=(+ x y)
        \n=(- n 1)
        loop y z n
        )
    loop 0 1
    )

# Now test it:
for 0 20 (\n say (fib n))
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
89
144
233
377
610
987
1597
2584
4181
6765
```


## Fish

Outputs Fibonacci numbers until stopped.

```mw
10::n' 'o&+&$10.
```


## FOCAL

```mw
01.10 TYPE "FIBONACCI NUMBERS" !
01.20 ASK "N =", N
01.30 SET A=0
01.40 SET B=1
01.50 FOR I=2,N; DO 2.0
01.60 TYPE "F(N) ", %8, B, !
01.70 QUIT

02.10 SET T=B
02.20 SET B=A+B
02.30 SET A=T
```

**Output:**

```
FIBONACCI NUMBERS
N =:20
F(N) =    6765
```


## Forth

```mw
: fib ( n -- fib )
    0 1 rot 0 do
        over + swap
    loop drop ;
```

Or, for negative-index support:

```mw
: fib ( n -- Fn ) 0 1 begin
  rot dup 0 = if drop drop exit then
  dup 0 > if   1 - rot rot dup rot +
          else 1 + rot rot over - swap then 
again ;
```

Since there are only a fixed and small amount of Fibonacci numbers that fit in a machine word, this FORTH version creates a table of Fibonacci numbers at compile time. It stops compiling numbers when there is arithmetic overflow (the number turns negative, indicating overflow.)

```mw
: F-start,  here 1 0 dup , ;
: F-next,   over + swap
            dup 0> IF  dup , true  ELSE  false  THEN ;

: computed-table  ( compile: 'start 'next / run: i -- x )
   create
      >r execute
      BEGIN  r@ execute not  UNTIL  rdrop
   does> 
       swap cells + @ ;

' F-start, ' F-next,  computed-table fibonacci 2drop
here swap - cell/ Constant #F/64   \ # of fibonacci numbers generated

16 fibonacci . 987  ok
#F/64 . 93  ok
92 fibonacci . 7540113804746346429  ok   \ largest number generated.
```


## Fortran

### FORTRAN IV

```mw
C     FIBONACCI SEQUENCE - FORTRAN IV
      NN=46
      DO 1 I=0,NN
    1 WRITE(*,300) I,IFIBO(I)
  300 FORMAT(1X,I2,1X,I10)
      END
C
      FUNCTION IFIBO(N)
      IF(N) 9,1,2
    1 IFN=0
      GOTO 9
    2 IF(N-1) 9,3,4
    3 IFN=1
      GOTO 9
    4 IFNM1=0
      IFN=1
      DO 5 I=2,N
      IFNM2=IFNM1
      IFNM1=IFN
    5 IFN=IFNM1+IFNM2
    9 IFIBO=IFN
      END
```

**Output:**

```
  0          0
  1          1
  2          1
  3          2
  4          3
  5          5
  6          8
  7         13
  8         21
  9         34
 10         55
...
 45 1134903170
 46 1836311903
```

### FORTRAN 90

```mw
function fibfc(n) result(f) ! integer forward count using 128 bit integers.
    !   DOMAIN:  up to 184
    !   uses 16 byte integers
    integer(16), intent (in) :: n ! input
    integer(16)              :: f ! output
    integer(16)              :: i, fm2, fm1

    if (n>184) then
        PRINT *, "ERROR: 'a' must be in the domain 0 <= n <= 184 !"
        STOP
    end if
    f=0
    fm2=0
    fm1=1
    IF ( n > 0 ) f = 1
    IF ( n < 3 ) return
    do i = 2, n
       f=fm2+fm1
       fm2=fm1
       fm1=f
    enddo
end function

</syntaxhighlight lang="fortran">

===FORTRAN 77===
<syntaxhighlight lang="fortran">
      FUNCTION IFIB(N)
      IF (N.EQ.0) THEN
        ITEMP0=0
      ELSE IF (N.EQ.1) THEN
        ITEMP0=1
      ELSE IF (N.GT.1) THEN
        ITEMP1=0
        ITEMP0=1
        DO 1 I=2,N
          ITEMP2=ITEMP1
          ITEMP1=ITEMP0
          ITEMP0=ITEMP1+ITEMP2
    1   CONTINUE
      ELSE
        ITEMP1=1
        ITEMP0=0
        DO 2 I=-1,N,-1
          ITEMP2=ITEMP1
          ITEMP1=ITEMP0
          ITEMP0=ITEMP2-ITEMP1
    2   CONTINUE
      END IF
      IFIB=ITEMP0
      END
```

Test program

```mw
      EXTERNAL IFIB
      CHARACTER*10 LINE
      PARAMETER ( LINE = '----------' )
      WRITE(*,900) 'N', 'F[N]', 'F[-N]'
      WRITE(*,900) LINE, LINE, LINE
      DO 1 N = 0, 10
        WRITE(*,901) N, IFIB(N), IFIB(-N)
    1 CONTINUE
  900 FORMAT(3(X,A10))
  901 FORMAT(3(X,I10))
      END
```

**Output:**

```
          N       F[N]      F[-N]
 ---------- ---------- ----------
          0          0          0
          1          1          1
          2          1         -1
          3          2          2
          4          3         -3
          5          5          5
          6          8         -8
          7         13         13
          8         21        -21
          9         34         34
         10         55        -55
```

### Recursive

In ISO Fortran 90 or later, use a RECURSIVE function:

```mw
module fibonacci
contains
    recursive function fibR(n) result(fib)
        integer, intent(in) :: n
        integer             :: fib
        
        select case (n)
            case (:0);      fib = 0
            case (1);       fib = 1
            case default;   fib = fibR(n-1) + fibR(n-2)
        end select
    end function fibR
```

### Iterative

In ISO Fortran 90 or later:

```mw
    function fibI(n)
        integer, intent(in) :: n
        integer, parameter :: fib0 = 0, fib1 = 1
        integer            :: fibI, back1, back2, i
 
        select case (n)
            case (:0);      fibI = fib0
            case (1);       fibI = fib1
     
            case default
                fibI = fib1
                back1 = fib0
                do i = 2, n
                    back2 = back1
                    back1 = fibI
                    fibI   = back1 + back2
                end do
         end select
    end function fibI
end module fibonacci
```

Test program

```mw
program fibTest
    use fibonacci
    
    do i = 0, 10
        print *, fibr(i), fibi(i)
    end do 
end program fibTest
```

**Output:**

```
0 0
1 1
1 1
2 2
3 3
5 5
8 8
13 13
21 21
34 34
55 55
```


## Free Pascal

*See also: Pascal*

```mw
type
   /// domain for Fibonacci function
   /// where result is within nativeUInt
   // You can not name it fibonacciDomain,
   // since the Fibonacci function itself
   // is defined for all whole numbers
   // but the result beyond F(n) exceeds high(nativeUInt).
   fibonacciLeftInverseRange =
      {$ifdef CPU64} 0..93 {$else} 0..47 {$endif};

{**
   implements Fibonacci sequence iteratively
   
   \param n the index of the Fibonacci number to calculate
   \returns the Fibonacci value at n
}
function fibonacci(const n: fibonacciLeftInverseRange): nativeUInt;
type
   /// more meaningful identifiers than simple integers
   relativePosition = (previous, current, next);
var
   /// temporary iterator variable
   i: longword;
   /// holds preceding fibonacci values
   f: array[relativePosition] of nativeUInt;
begin
   f[previous] := 0;
   f[current] := 1;
   
   // note, in Pascal for-loop-limits are inclusive
   for i := 1 to n do
   begin
      f[next] := f[previous] + f[current];
      f[previous] := f[current];
      f[current] := f[next];
   end;
   
   // assign to previous, bc f[current] = f[next] for next iteration
   fibonacci := f[previous];
end;
```


## Frink

All of Frink's integers can be arbitrarily large.

```mw
fibonacciN[n] :=
{
   a = 0
   b = 1
   count = 0
   while count < n
   {
      [a,b] = [b, a + b]
      count = count + 1
   }
   return a
}
```


## FRISC Assembly

To find the nth Fibonacci number, call this subroutine with n in register R0: the answer will be returned in R0 too. Contents of other registers are preserved.

```mw
FIBONACCI   PUSH   R1
            PUSH   R2
            PUSH   R3

            MOVE   0,  R1
            MOVE   1,  R2

FIB_LOOP    SUB    R0,  1, R0
            JP_Z   FIB_DONE

            MOVE   R2, R3
            ADD    R1, R2, R2
            MOVE   R3, R1

            JP     FIB_LOOP

FIB_DONE    MOVE   R2, R0

            POP    R3
            POP    R2
            POP    R1

            RET
```


## FunL

### Recursive

```mw
def
  fib( 0 ) = 0
  fib( 1 ) = 1
  fib( n ) = fib( n - 1 ) + fib( n - 2 )
```

### Tail Recursive

```mw
def fib( n ) =
  def
    _fib( 0, prev, _ )    = prev
    _fib( 1, _,    next ) = next
    _fib( n, prev, next ) = _fib( n - 1, next, next + prev )

  _fib( n, 0, 1 )
```

### Lazy List

```mw
val fib =
  def _fib( a, b ) = a # _fib( b, a + b )

  _fib( 0, 1 )

println( fib(10000) )
```

**Output:**

```
33644764876431783266621612005107543310302148460680063906564769974680081442166662368155595513633734025582065332680836159373734790483865268263040892463056431887354544369559827491606602099884183933864652731300088830269235673613135117579297437854413752130520504347701602264758318906527890855154366159582987279682987510631200575428783453215515103870818298969791613127856265033195487140214287532698187962046936097879900350962302291026368131493195275630227837628441540360584402572114334961180023091208287046088923962328835461505776583271252546093591128203925285393434620904245248929403901706233888991085841065183173360437470737908552631764325733993712871937587746897479926305837065742830161637408969178426378624212835258112820516370298089332099905707920064367426202389783111470054074998459250360633560933883831923386783056136435351892133279732908133732642652633989763922723407882928177953580570993691049175470808931841056146322338217465637321248226383092103297701648054726243842374862411453093812206564914032751086643394517512161526545361333111314042436854805106765843493523836959653428071768775328348234345557366719731392746273629108210679280784718035329131176778924659089938635459327894523777674406192240337638674004021330343297496902028328145933418826817683893072003634795623117103101291953169794607632737589253530772552375943788434504067715555779056450443016640119462580972216729758615026968443146952034614932291105970676243268515992834709891284706740862008587135016260312071903172086094081298321581077282076353186624611278245537208532365305775956430072517744315051539600905168603220349163222640885248852433158051534849622434848299380905070483482449327453732624567755879089187190803662058009594743150052402532709746995318770724376825907419939632265984147498193609285223945039707165443156421328157688908058783183404917434556270520223564846495196112460268313970975069382648706613264507665074611512677522748621598642530711298441182622661057163515069260029861704945425047491378115154139941550671256271197133252763631939606902895650288268608362241082050562430701794976171121233066073310059947366875
```

### Iterative

```mw
def fib( n ) =
  a, b = 0, 1

  for i <- 1..n
    a, b = b, a+b

  a
```

### Binet's Formula

```mw
import math.sqrt

def fib( n ) =
  phi = (1 + sqrt( 5 ))/2
  int( (phi^n - (-phi)^-n)/sqrt(5) + .5 )
```

### Matrix Exponentiation

```mw
def mul( a, b ) =
  res = array( a.length(), b(0).length() )

  for i <- 0:a.length(), j <- 0:b(0).length()
    res( i, j ) = sum( a(i, k)*b(k, j) | k <- 0:b.length() )

  vector( res )

def
  pow( _, 0 ) = ((1, 0), (0, 1))
  pow( x, 1 ) = x
  pow( x, n )
    | 2|n = pow( mul(x, x), n\2 )
    | otherwise = mul(x, pow( mul(x, x), (n - 1)\2 ) )

def fib( n ) = pow( ((0, 1), (1, 1)), n )(0, 1)

for i <- 0..10
  println( fib(i) )
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


## Futhark

### Iterative

```mw
fun main(n: int): int =
  loop((a,b) = (0,1)) = for _i < n do
    (b, a + b)
  in a
```


## FutureBasic

### Iterative

```mw
window 1, @"Fibonacci Sequence", (0,0,480,620)

local fn Fibonacci( n as long ) as long
  static long s1
  static long s2
  long        temp
  
  if ( n < 2 )
    s1 = n
    exit fn
  else
    temp = s1 + s2
    s2 = s1
    s1 = temp
    exit fn
  end if
end fn = s1

long i
CFTimeInterval t

t = fn CACurrentMediaTime

for i = 0 to 40
  print i;@".\t";fn Fibonacci(i)
next i

print : printf @"Compute time: %.3f ms",(fn CACurrentMediaTime-t)*1000

HandleEvents
```

Output:

```
0. 0
1. 1
2. 1
3. 2
4. 3
5. 5
6. 8
7. 13
8. 21
9. 34
10.   55
11.   89
12.   144
13.   233
14.   377
15.   610
16.   987
17.   1597
18.   2584
19.   4181
20.   6765
21.   10946
22.   17711
23.   28657
24.   46368
25.   75025
26.   121393
27.   196418
28.   317811
29.   514229
30.   832040
31.   1346269
32.   2178309
33.   3524578
34.   5702887
35.   9227465
36.   14930352
37.   24157817
38.   39088169
39.   63245986
40.   102334155

Compute time: 2.143 ms
```

### Recursive

Cost is a time penalty

```mw
local fn Fibonacci( n as NSInteger ) as NSInteger
NSInteger result
if n < 2 then result = n : exit fn
result = fn Fibonacci( n-1 ) + fn Fibonacci( n-2 )
end fn = result

window 1

NSInteger i
CFTimeInterval t

t = fn CACurrentMediaTime
for i = 0 to 40
print i;@".\t";fn Fibonacci(i)
next
print : printf @"Compute time: %.3f ms",(fn CACurrentMediaTime-t)*1000

HandleEvents
```

**Output:**

```
0. 0
1. 1
2. 1
3. 2
4. 3
5. 5
6. 8
7. 13
8. 21
9. 34
10.   55
11.   89
12.   144
13.   233
14.   377
15.   610
16.   987
17.   1597
18.   2584
19.   4181
20.   6765
21.   10946
22.   17711
23.   28657
24.   46368
25.   75025
26.   121393
27.   196418
28.   317811
29.   514229
30.   832040
31.   1346269
32.   2178309
33.   3524578
34.   5702887
35.   9227465
36.   14930352
37.   24157817
38.   39088169
39.   63245986
40.   102334155

Compute time: 2844.217 ms
```


## Fōrmulæ

Fōrmulæ programs are not textual, visualization/edition of programs is done showing/manipulating structures but not text. Moreover, there can be multiple visual representations of the same program. Even though it is possible to have textual representation —i.e. XML, JSON— they are intended for storage and transfer purposes more than visualization and edition.

Programs in Fōrmulæ are created/edited online in its website.

In **this page** you can see and run the program(s) related to this task and their results. You can also change either the programs or the parameters they are called with, for experimentation, but remember that these programs were created with the main purpose of showing a clear solution of the task, and they generally lack any kind of validation.

### Recursive

Recursive version is slow, it is O(2n), or of exponential order.

It is because it makes a lot of recursive calls.

To illustrate this, the following is a functions that makes a tree or the recursive calls:

### Iterative (3 variables)

It is O(n), or of linear order.

### Iterative (2 variables)

It is O(n), or of linear order.

### Iterative, using a list

It is O(n), or of linear order.

### Using matrix multiplication

### Divide and conquer

It is an optimized version of the matrix multiplication algorithm, with an order of O(lg(n))

### Closed-form

It has an order of O(lg(n))


## GAP

```mw
fib := function(n)
  local a;
  a := [[0, 1], [1, 1]]^n;
  return a[1][2];
end;
```

GAP has also a buit-in function for that.

```mw
Fibonacci(n);
```


## Gecho

```mw
0 1 dup wover + dup wover + dup wover + dup wover +
```

Prints the first several fibonacci numbers...


## Gleam

### Recursive

```mw
pub fn fib(n: Int) -> Int {
  case n {
    0 -> 0
    1 -> 1
    n -> fib(n - 1) + fib(n - 2)
  }
}
```

### Iterative

```mw
pub fn fib(n: Int) -> Int {
  fib_helper(n, 0, 1)
}

fn fib_helper(n: Int, res: Int, next: Int) -> Int {
  case n, res, next {
    0, res, _ -> res
    iter, res, next -> fib_helper(iter - 1, next, res + next)
  }
}
```


## GML

```mw
///fibonacci(n)
//Returns the nth fibonacci number

var n, numb;
n = argument0;

if (n == 0)
    {
    numb = 0;
    }
else
    {
    var fm2, fm1;
    fm2 = 0;
    fm1 = 1;
    numb = 1;
    repeat(n-1)
        {
        numb = fm2+fm1;
        fm2 = fm1;
        fm1 = numb;
        }
    }

return numb;
```


## Go

### Recursive

```mw
func fib(a int) int {
  if a < 2 {
    return a
  }
  return fib(a - 1) + fib(a - 2)
}
```

### Iterative

```mw
import (
   "math/big"
)

func fib(n uint64) *big.Int {
   if n < 2 {
      return big.NewInt(int64(n))
   }
   a, b := big.NewInt(0), big.NewInt(1)
   for n--; n > 0; n-- {
      a.Add(a, b)
      a, b = b, a
   }
   return b
}
```

### Iterative using a closure

```mw
func fibNumber() func() int {
   fib1, fib2 := 0, 1
   return func() int {
      fib1, fib2 = fib2, fib1 + fib2
      return fib1
   }
}

func fibSequence(n int) int {
   f := fibNumber()
   fib := 0
   for i := 0; i < n; i++ {
      fib = f()
   }
   return fib
}
```

### Using a goroutine and channel

```mw
func fib(c chan int) {
   a, b := 0, 1
   for {
      c <- a
      a, b = b, a+b
   }
}

func main() {
   c := make(chan int)
   go fib(c)
   for i := 0; i < 10; i++ {
      fmt.Println(<-c)
   }
}
```


## Golfscript

```
{1 0@{.@+}*\;}:f;
20, {f p}/
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
89
144
233
377
610
987
1597
2584
4181
```


## Grain

### Recursive

```mw
import String from "string"
import File from "sys/file"
let rec fib = n => if (n < 2) {
  n
} else {
  fib(n - 1) + fib(n - 2)
}
for (let mut i = 0; i <= 20; i += 1) {
  File.fdWrite(File.stdout, Pervasives.toString(fib(i)))
  ignore(File.fdWrite(File.stdout, " "))
}
```

### Iterative

```mw
import File from "sys/file"
let fib = j => {
  let mut fnow = 0, fnext = 1
  for (let mut n = 0; n <= j; n += 1) {
    if (n == 0 || n == 1) {
      let output1 = " " ++ toString(n)
      ignore(File.fdWrite(File.stdout, output1))
    } else {
      let tempf = fnow + fnext
      fnow = fnext
      fnext = tempf
      let output2 = " " ++ toString(fnext)
      ignore(File.fdWrite(File.stdout, output2))
    }
  }
}
fib(20)
```

**Output:**

### Iterative with Buffer

```mw
import Buffer from "buffer"
import String from "string"
let fib = j => {
  // set-up minimal, growable buffer
  let buf = Buffer.make(j * 2)
  let mut fnow = 0, fnext = 1
  for (let mut n = 0; n <= j; n += 1) {
    if (n == 0 || n == 1) {
      Buffer.addChar(' ', buf)
      Buffer.addString(toString(n), buf)
    } else {
      let tempf = fnow + fnext
      fnow = fnext
      fnext = tempf
      Buffer.addChar(' ', buf)
      Buffer.addString(toString(fnext), buf)
    }
  }
  // stringify buffer and return
  Buffer.toString(buf)
}
let output = fib(20)
print(output)
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 
```


## Groovy

Full "extra credit" solutions.

### Recursive

A recursive closure must be *pre-declared*.

```mw
def rFib
rFib = { 
    it == 0   ? 0 
    : it == 1 ? 1 
    : it > 1  ? rFib(it-1) + rFib(it-2)
    /*it < 0*/: rFib(it+2) - rFib(it+1)
    
}
```

### Iterative

```mw
def iFib = { 
    it == 0   ? 0 
    : it == 1 ? 1 
    : it > 1  ? (2..it).inject([0,1]){i, j -> [i[1], i[0]+i[1]]}[1]
    /*it < 0*/: (-1..it).inject([0,1]){i, j -> [i[1]-i[0], i[0]]}[0]
}
```

### Analytic

```mw
final φ = (1 + 5**(1/2))/2
def aFib = { (φ**it - (-φ)**(-it))/(5**(1/2)) as BigInteger }
```

Test program:

```mw
def time = { Closure c ->
    def start = System.currentTimeMillis()
    def result = c()
    def elapsedMS = (System.currentTimeMillis() - start)/1000
    printf '(%6.4fs elapsed)', elapsedMS
    result
}

print "  F(n)      elapsed time   "; (-10..10).each { printf ' %3d', it }; println()
print "--------- -----------------"; (-10..10).each { print ' ---' }; println()
[recursive:rFib, iterative:iFib, analytic:aFib].each { name, fib ->
    printf "%9s ", name
    def fibList = time { (-10..10).collect {fib(it)} }
    fibList.each { printf ' %3d', it }
    println()
}
```

**Output:**

```
  F(n)      elapsed time    -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10
--------- ----------------- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
recursive (0.0080s elapsed) -55  34 -21  13  -8   5  -3   2  -1   1   0   1   1   2   3   5   8  13  21  34  55
iterative (0.0040s elapsed) -55  34 -21  13  -8   5  -3   2  -1   1   0   1   1   2   3   5   8  13  21  34  55
 analytic (0.0030s elapsed) -55  34 -21  13  -8   5  -3   2  -1   1   0   1   1   2   3   5   8  13  21  34  55
```


## Harbour

### Recursive

```mw
#include "harbour.ch"
Function fibb(a,b,n)
return(if(--n>0,fibb(b,a+b,n),a))
```

### Iterative

```mw
#include "harbour.ch"
Function fibb(n) 
   local fnow:=0, fnext:=1, tempf
   while (--n>0)
      tempf:=fnow+fnext
      fnow:=fnext
      fnext:=tempf
   end while
return(fnext)
```
