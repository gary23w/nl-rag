---
title: "Fibonacci sequence (part 8/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 8/10
---

## Picat

### Function

tabling for speed.

```mw
go =>
  println([fib_fun(I) : I in 1..10]),
  F1=fib_fun(2**10),
  println(f1=F1),
  nl.

table
fib_fun(0) = 0.
fib_fun(1) = 1.
fib_fun(N) = fib_fun(N-1) + fib_fun(N-2).
```

**Output:**

```
[1,1,2,3,5,8,13,21,34,55]
f1 = 4506699633677819813104383235728886049367860596218604830803023149600030645708721396248792609141030396244873266580345011219530209367425581019871067646094200262285202346655868899711089246778413354004103631553925405243
```

### Array

```mw
fib_array(0,[0]).
fib_array(1,[0,1]).
fib_array(N,A) :-
   N > 1,
   A = new_array(N),
   A[1] = 1,
   A[2] = 1,
   foreach(I in 3..N)
     A[I] = A[I-1] + A[I-2]
   end.
```

### Loop

```mw
fib_loop(N) = Curr =>
  Curr = 0,
  Prev = 1,
  foreach(_I in 1..N)
    Tmp = Curr,
    Curr := Curr + Prev,
    Prev := Tmp
  end.
```

### Formula

Translation of

:

Tcl

Works for n <= 70.

```mw
fib_formula(N) = round((0.5 + 0.5*sqrt(5))**N / sqrt(5)).
```

### "Lazy lists"

Translation of

:

Prolog

```mw
go =>fib_lazy(X),
  A = new_list(15),
  append(A,_,X),
  println(A),

fib_lazy([0,1|X]) :-
    ffib(0,1,X).
ffib(A,B,X) :-
    freeze(X, (C is A+B, X=[C|Y], ffib(B,C,Y)) ).
```

**Output:**

```
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377]
```

### Generators idiom

Translation of

:

Prolog

```mw
go =>
  take(15, $fib_gen(0,1), $T-[], _G),
  println(T).

take( 0, Next, Z-Z, Next).
take( N, Next, [A|B]-Z, NZ):- N>0, !, next( Next, A, Next1),
  N1 is N-1,
  take( N1, Next1, $B-Z, NZ).
 
next( fib_gen(A,B), A, fib_gen(B,C)):- C is A+B.
```

**Output:**

```
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377]
```

### Reversible

This is a reversible variant using constraint modelling.

`fib_rev(N,F)` has these two usages:

- find F given a value N (this is the normal usage)
- find N given a value F (backward usage)

Note: In general, Picat supports arbitrary precision for integers. However, the constraint solvers only supports integer domains of -2**56..2**56 so the largest Fibonacci number that can be found by this predicate is N = 81.

```mw
import cp.

go =>
  N1 = 30,
  fib_rev(30,F1),
  println([n1=N1,fib1=F1]),
  
  F2 #= 20365011074,
  fib_rev(N2,F2),
  println([n2=N2,f2=F2]),
  
  F3 = 61305790721611591,
  fib_rev(N3,F3),
  println([n3=N3,F3]),
  nl.

table
fib_rev(0,1).
fib_rev(1,1).
fib_rev(N,F) :-
  N #> 0,
  F #> 0,
  N1 #= N-1, 
  N2 #= N-2,
  fib_rev(N1,F1), 
  fib_rev(N2,F2),  
  F #= F1+F2.
```

**Output:**

```
[n1 = 30,fib1 = 1346269]
[n2 = 50,f2 = 20365011074]
[n3 = 81,61305790721611591]
```


## PicoLisp

### Recursive

```mw
(de fibo (N)
   (if (>= 2 N)
      1
      (+ (fibo (dec N)) (fibo (- N 2))) ) )
```

### Recursive with Cache

Using a recursive version doesn't need to be slow, as the following shows:

```mw
(de fibo (N)
   (cache '(NIL) N  # Use a cache to accelerate
      (if (>= 2 N)
         N
         (+ (fibo (dec N)) (fibo (- N 2))) ) ) )

(bench (fibo 1000))
```

Output:

```mw
0.012 sec
-> 43466557686937456435688527675040625802564660517371780402481729089536555417949
05189040387984007925516929592259308032263477520968962323987332247116164299644090
6533187938298969649928516003704476137795166849228875
```

### Iterative

```mw
(de fib (N)
   (let (A 0  B 1)
      (do N
         (prog1 B (setq B (+ A B) A @)) ) ) )
```

### Coroutines

```mw
(co 'fibo
   (let (A 0  B 1)
      (yield 'ready)
      (while
         (yield
            (swap 'B (+ (swap 'A B) B)) ) ) ) )

(do 15
   (printsp (yield 'next 'fibo)) )
(prinl)
(yield NIL 'fibo)
```

**Output:**

```
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
```


## Pike

### Iterative

```mw
int     
fibIter(int n) {
    int fibPrev, fib, i;
    if (n < 2) {
        return 1;
    }
    fibPrev = 0;
    fib = 1;
    for (i = 1; i < n; i++) {
        int oldFib = fib;
        fib += fibPrev;
        fibPrev = oldFib;
    }
    return fib;
}
```

### Recursive

```mw
int 
fibRec(int n) {
    if (n < 2) {
        return(1);
    }
    return( fib(n-2) + fib(n-1) );
}
```


## PILOT

Works with

:

psPILOT

Translation of

:

11l

```
C: #count = 20
 : #a = 1
 : #b = 1
T: First #count fibonacci numbers:
*Loop
T: #a
C: #t = #b
 : #b = #a + #b
 : #a = #t
 : #count = #count - 1
J (#count > 0): *Loop
E:
```

**Output:**

```
First 20 fibonacci numbers:
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
610
987
2584
4181
6765
```


## PIR

Recursive:

Works with

:

Parrot

version tested with 2.4.0

```mw
.sub fib
  .param int n
  .local int nt
  .local int ft
  if n < 2 goto RETURNN
  nt = n - 1
  ft = fib( nt )
  dec nt
  nt = fib(nt)
  ft = ft + nt
  .return( ft )
RETURNN:
  .return( n )
  end
.end

.sub main :main
  .local int counter
  .local int f
  counter=0
LOOP: 
  if counter > 20 goto DONE
  f = fib(counter)
  print f
  print "\n"
  inc counter
  goto LOOP
DONE:
  end
.end
```

Iterative (stack-based):

Works with

:

Parrot

version tested with 2.4.0

```mw
.sub fib
  .param int n
  .local int counter
  .local int f
  .local pmc fibs
  .local int nmo
  .local int nmt

  fibs = new 'ResizableIntegerArray'
  if n == 0 goto RETURN0
  if n == 1 goto RETURN1
  push fibs, 0
  push fibs, 1
  counter = 2
FIBLOOP:
  if counter > n goto DONE
  nmo = pop fibs
  nmt = pop fibs
  f = nmo + nmt
  push fibs, nmt
  push fibs, nmo
  push fibs, f
  inc counter
  goto FIBLOOP
RETURN0:
  .return( 0 )
  end
RETURN1:
  .return( 1 )
  end
DONE:
  f = pop fibs
  .return( f )
  end
.end

.sub main :main
  .local int counter
  .local int f
  counter=0
LOOP: 
  if counter > 20 goto DONE
  f = fib(counter)
  print f
  print "\n"
  inc counter
  goto LOOP
DONE:
  end
.end
```


## PL/0

The program waits for *n*. Then it displays *n*th Fibonacci number.

```mw
var n, a, b, i, tmp;
begin
  ? n;
  a := 0; b := 1;
  i := 2;
  while i <= n do
  begin
    tmp := b; b := a + b; a := tmp;
    i := i + 1
  end;
  ! b
end.
```

4 runs.

**Input:**

```
5
```

**Output:**

```
       5
```

**Input:**

```
9
```

**Output:**

```
      34
```

**Input:**

```
13
```

**Output:**

```
     233
```

**Input:**

```
20
```

**Output:**

```
    6765
```


## PL/I

```mw
/* Form the n-th Fibonacci number, n > 1.    12 March 2022 */
Fib: procedure (n) returns (fixed binary (31));
   declare (i, n, f1, f2, f3) fixed binary (31);

   f1 = 0; f2 = 1;
   do i = 1 to n-2;
      f3 = f1 + f2;
      f1 = f2;
      f2 = f3;
   end;
   return (f3);

end Fib;
```


## PL/M

```mw
100H:
BDOS: PROCEDURE (FN, ARG); DECLARE FN BYTE, ARG ADDRESS; GO TO 5; END BDOS;
EXIT: PROCEDURE; CALL BDOS(0,0); END EXIT;
PRINT: PROCEDURE (S); DECLARE S ADDRESS; CALL BDOS(9,S); END PRINT;

PRINT$NUMBER: PROCEDURE (N);
    DECLARE S (6) BYTE INITIAL ('.....$');
    DECLARE (N, P) ADDRESS, C BASED P BYTE;
    P = .S(5);
DIGIT:
    P = P - 1;
    C = N MOD 10 + '0';
    N = N / 10;
    IF N > 0 THEN GO TO DIGIT;
    CALL PRINT(P);
END PRINT$NUMBER;

FIBONACCI: PROCEDURE (N) ADDRESS;
    DECLARE (N, A, B, C, I) ADDRESS;
    IF N<=1 THEN RETURN N;
    A = 0;
    B = 1;
    DO I=2 TO N;
        C = A;
        A = B;
        B = A + C;
    END;
    RETURN B;
END FIBONACCI;

DECLARE I ADDRESS;
DO I=0 TO 20;
    CALL PRINT$NUMBER(FIBONACCI(I));
    CALL PRINT(.' $');
END;
CALL EXIT;
EOF
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```


## PL/pgSQL

### Recursive

```mw
CREATE OR REPLACE FUNCTION fib(n INTEGER) RETURNS INTEGER AS $$
BEGIN
  IF (n < 2) THEN
    RETURN n;
  END IF;
  RETURN fib(n - 1) + fib(n - 2);
END;
$$ LANGUAGE plpgsql;
```

### Calculated

```mw
CREATE OR REPLACE FUNCTION fibFormula(n INTEGER) RETURNS INTEGER AS $$
BEGIN
  RETURN round(pow((pow(5, .5) + 1) / 2, n) / pow(5, .5));
END;
$$ LANGUAGE plpgsql;
```

### Linear

```mw
CREATE OR REPLACE FUNCTION fibLinear(n INTEGER) RETURNS INTEGER AS $$
DECLARE
  prevFib INTEGER := 0;
  fib INTEGER := 1;
BEGIN
  IF (n < 2) THEN
    RETURN n;
  END IF;

  WHILE n > 1 LOOP
    SELECT fib, prevFib + fib INTO prevFib, fib;
    n := n - 1;
  END LOOP;

  RETURN fib;
END;
$$ LANGUAGE plpgsql;
```

### Tail recursive

```mw
CREATE OR REPLACE FUNCTION fibTailRecursive(n INTEGER, prevFib INTEGER DEFAULT 0, fib INTEGER DEFAULT 1)
RETURNS INTEGER AS $$
BEGIN
  IF (n = 0) THEN
    RETURN prevFib;
  END IF;
  RETURN fibTailRecursive(n - 1, fib, prevFib + fib);
END;
$$ LANGUAGE plpgsql;
```


## PL/SQL

```mw
create or replace function fnu_fibonacci(p_num integer) return integer is
  f integer;
  p integer;
  q integer;
begin
  case when p_num < 0 or p_num != trunc(p_num) 
                            then raise_application_error(-20001, 'Invalid input: ' || p_num, true);
       when p_num in (0, 1) then f := p_num;
       else
            p := 0;
            q := 1;
            for i in 2 .. p_num loop
              f := p + q;
              p := q;
              q := f;
            end loop;
  end case;
  return(f);
end fnu_fibonacci;
/
```


## Plain English

```mw
To find a fibonacci number given a count:
Put 0 into a number.
Put 1 into another number.
Loop.
If a counter is past the count, put the number into the fibonacci number; exit.
Add the number to the other number.
Swap the number with the other number.
Repeat.
```


## Pluto

```mw
function fib(n)
  local a, b = 0, 1
  for _ = 1,n do
    a,b = b,a+b
  end
  return a
end

for i = 0,10 do
  print(fib(i))
end
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


## Pop11

```mw
define fib(x);
lvars a , b;
    1 -> a;
    1 -> b;
    repeat x - 1 times
         (a + b, b) -> (b, a);
    endrepeat;
    a;
enddefine;
```


## PostScript

Enter the desired number for "n" and run through your favorite postscript previewer or send to your postscript printer:

### Recursive

```mw
%!PS

% We want the 'n'th fibonacci number
/n 13 def

% Prepare output canvas:
/Helvetica findfont 20 scalefont setfont
100 100 moveto

%define the function recursively:
/fib { 
  dup 2 lt
  { }
  { 
    dup 1 sub fib 
    exch 2 sub fib
    add 
  } ifelse
} def
    
(Fib\() show n (....) cvs show (\) = ) show n fib (.....) cvs show

showpage
```

**Output**

```
Fib(13) = 233
```

### Iterative

```mw
%!PS

/Courier 16 selectfont

/fibonacci {
  dup 2 lt
  { }
  {
    0 exch
    1 exch
    2 exch 1 exch {
      pop
      exch
      1 index
      add
    } for
    exch
    pop
  } ifelse
} def

/str 4 string def

/n 10 def

72 720 moveto

0 1 n {
  fibonacci str cvs
  str show
  pop
} for

showpage
```

**Output**

```
0  1  1  2  3  5  8  13  21  34  55
```


## Potion

### Recursive

Starts with int and upgrades on-the-fly to doubles.

```mw
recursive = (n):
  if (n <= 1): 1. else: recursive (n - 1) + recursive (n - 2)..

n = 40
("fib(", n, ")= ", recursive (n), "\n") join print
```

```
recursive(40)= 165580141
real  0m2.851s
```

### Iterative

```mw
iterative = (n) :
   curr = 0
   prev = 1
   tmp = 0
   n times:
      tmp = curr
      curr = curr + prev
      prev = tmp
   .
   curr
.
```

### Matrix based

```mw
sqr = (x): x * x.

# Based on the fact that
# F2n = Fn(2Fn+1 - Fn)
# F2n+1 = Fn ^2 + Fn+1 ^2
matrix = (n) :
   algorithm = (n) :
      "computes (Fn, Fn+1)"
      if (n < 2): return ((0, 1), (1, 1)) at(n).
      
      # n = e + {0, 1}
      q = algorithm(n / 2)  # q = (Fe/2, Fe/2+1)
      q = (q(0) * (2 * q(1) - q(0)), sqr(q(0)) + sqr(q(1)))  # q => (Fe, Fe+1)
      if (n % 2 == 1) :  # q => (Fe+{0, 1}, Fe+1+{0,1}) = (Fn, Fn+1)
         q = (q(1), q(1) + q(0))
      .
      q
   .
   algorithm(n)(0)
.
```

### Handling negative values

```mw
fibonacci = (n) :
   myFavorite = matrix
   if (n >= 0) :
      myFavorite(n)
   .  else :
      n = n * -1
      if (n % 2 == 1) :
         myFavorite(n)
      . else :
         myFavorite(n) * -1
      .
   .
.
```


## PowerShell

### Iterative

```mw
function FibonacciNumber ( $count )
{
    $answer = @(0,1)
    while ($answer.Length -le $count)
    {
        $answer += $answer[-1] + $answer[-2]
    }
    return $answer
}
```

An even shorter version that eschews function calls altogether:

```mw
$count = 8
$answer = @(0,1)
0..($count - $answer.Length) | Foreach { $answer += $answer[-1] + $answer[-2] }
$answer
```

### Recursive

```mw
function fib($n) {
    switch ($n) {
        0            { return 0 }
        1            { return 1 }
        { $_ -lt 0 } { return [Math]::Pow(-1, -$n + 1) * (fib (-$n)) }
        default      { return (fib ($n - 1)) + (fib ($n - 2)) }
    }
}
```


## Processing

Translation of

:

Java

```mw
void setup() {
  size(400, 400);
  fill(255, 64);
  frameRate(2);
}
void draw() {
  int num = fibonacciNum(frameCount);
  println(frameCount, num);
  rect(0,0,num, num);
  if(frameCount==14) frameCount = -1; // restart
}
int fibonacciNum(int n) {
  return (n < 2) ? n : fibonacciNum(n - 1) + fibonacciNum(n - 2);
}
```

On the nth frame, the nth Fibonacci number is printed to the console and a square of that size is drawn on the sketch surface. The sketch restarts to keep drawing within the window size.

**Output:**

```
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
```


## Prolog

Works with

:

SWI Prolog

Works with

:

GNU Prolog

Works with

:

YAP

```mw
fib(1, 1) :- !.
fib(0, 0) :- !.
fib(N, Value) :-
  A is N - 1, fib(A, A1),
  B is N - 2, fib(B, B1),
  Value is A1 + B1.
```

This naive implementation works, but is very slow for larger values of N. Here are some simple measurements (in SWI-Prolog):

```mw
?- time(fib(0,F)).
% 2 inferences, 0.000 CPU in 0.000 seconds (88% CPU, 161943 Lips)
F = 0.

?- time(fib(10,F)).
% 265 inferences, 0.000 CPU in 0.000 seconds (98% CPU, 1458135 Lips)
F = 55.

?- time(fib(20,F)).
% 32,836 inferences, 0.016 CPU in 0.016 seconds (99% CPU, 2086352 Lips)
F = 6765.

?- time(fib(30,F)).
% 4,038,805 inferences, 1.122 CPU in 1.139 seconds (98% CPU, 3599899 Lips)
F = 832040.

?- time(fib(40,F)).
% 496,740,421 inferences, 138.705 CPU in 140.206 seconds (99% CPU, 3581264 Lips)
F = 102334155.
```

As you can see, the calculation time goes up exponentially as N goes higher.

### Poor man's memoization

Works with

:

SWI Prolog

Works with

:

YAP

Works with

:

GNU Prolog

The performance problem can be readily fixed by the addition of two lines of code (the first and last in this version):

```mw
%:- dynamic fib/2.  % This is ISO, but GNU doesn't like it.
:- dynamic(fib/2).  % Not ISO, but works in SWI, YAP and GNU unlike the ISO declaration.
fib(1, 1) :- !.
fib(0, 0) :- !.
fib(N, Value) :-
  A is N - 1, fib(A, A1),
  B is N - 2, fib(B, B1),
  Value is A1 + B1,
  asserta((fib(N, Value) :- !)).
```

Let's take a look at the execution costs now:

```mw
?- time(fib(0,F)).
% 2 inferences, 0.000 CPU in 0.000 seconds (90% CPU, 160591 Lips)
F = 0.

?- time(fib(10,F)).
% 37 inferences, 0.000 CPU in 0.000 seconds (96% CPU, 552610 Lips)
F = 55.

?- time(fib(20,F)).
% 41 inferences, 0.000 CPU in 0.000 seconds (96% CPU, 541233 Lips)
F = 6765.

?- time(fib(30,F)).
% 41 inferences, 0.000 CPU in 0.000 seconds (95% CPU, 722722 Lips)
F = 832040.

?- time(fib(40,F)).
% 41 inferences, 0.000 CPU in 0.000 seconds (96% CPU, 543572 Lips)
F = 102334155.
```

In this case by asserting the new N,Value pairing as a rule in the database we're making the classic time/space tradeoff. Since the space costs are (roughly) linear by N and the time costs are exponential by N, the trade-off is desirable. You can see the poor man's memoizing easily:

```mw
?- listing(fib).
:- dynamic fib/2.

fib(40, 102334155) :- !.
fib(39, 63245986) :- !.
fib(38, 39088169) :- !.
fib(37, 24157817) :- !.
fib(36, 14930352) :- !.
fib(35, 9227465) :- !.
fib(34, 5702887) :- !.
fib(33, 3524578) :- !.
fib(32, 2178309) :- !.
fib(31, 1346269) :- !.
fib(30, 832040) :- !.
fib(29, 514229) :- !.
fib(28, 317811) :- !.
fib(27, 196418) :- !.
fib(26, 121393) :- !.
fib(25, 75025) :- !.
fib(24, 46368) :- !.
fib(23, 28657) :- !.
fib(22, 17711) :- !.
fib(21, 10946) :- !.
fib(20, 6765) :- !.
fib(19, 4181) :- !.
fib(18, 2584) :- !.
fib(17, 1597) :- !.
fib(16, 987) :- !.
fib(15, 610) :- !.
fib(14, 377) :- !.
fib(13, 233) :- !.
fib(12, 144) :- !.
fib(11, 89) :- !.
fib(10, 55) :- !.
fib(9, 34) :- !.
fib(8, 21) :- !.
fib(7, 13) :- !.
fib(6, 8) :- !.
fib(5, 5) :- !.
fib(4, 3) :- !.
fib(3, 2) :- !.
fib(2, 1) :- !.
fib(1, 1) :- !.
fib(0, 0) :- !.
fib(A, D) :-
   B is A+ -1,
   fib(B, E),
   C is A+ -2,
   fib(C, F),
   D is E+F,
   asserta((fib(A, D):-!)).
```

All of the interim N/Value pairs have been asserted as facts for quicker future use, speeding up the generation of the higher Fibonacci numbers.

### Continuation passing style

Works with **SWI-Prolog** and module lambda, written by **Ulrich Neumerkel** found there http://www.complang.tuwien.ac.at/ulrich/Prolog-inedit/lambda.pl

```mw
:- use_module(lambda).
fib(N, FN) :-
   cont_fib(N, _, FN, \_^Y^_^U^(U = Y)).

cont_fib(N, FN1, FN, Pred) :-
   (   N < 2 ->
       call(Pred, 0, 1, FN1, FN)
   ;
       N1 is N - 1,
       P = \X^Y^Y^U^(U is X + Y),
       cont_fib(N1, FNA, FNB, P),
       call(Pred, FNA, FNB, FN1, FN)
   ).
```

### With lazy lists

Works with **SWI-Prolog** and others that support `freeze/2`.

```mw
fib([0,1|X]) :-
    ffib(0,1,X).
ffib(A,B,X) :-
    freeze(X, (C is A+B, X=[C|Y], ffib(B,C,Y)) ).
```

The predicate `fib(Xs)` unifies `Xs` with an infinite list whose values are the Fibonacci sequence. The list can be used like this:

```mw
?- fib(X), length(A,15), append(A,_,X), writeln(A).
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

### Generators idiom

```mw
take( 0, Next, Z-Z, Next).
take( N, Next, [A|B]-Z, NZ):- N>0, !, next( Next, A, Next1),
  N1 is N-1,
  take( N1, Next1, B-Z, NZ).

next( fib(A,B), A, fib(B,C)):- C is A+B.

%% usage: ?- take(15, fib(0,1), _X-[], G), writeln(_X).
%% [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
%% G = fib(610, 987)
```

### Yet another implementation

One of my favorites; loosely similar to the first example, but without the performance penalty, and needs nothing special to implement. Not even a dynamic database predicate. Attributed to M.E. for the moment, but simply because I didn't bother to search for the many people who probably did it like this long before I did. If someone knows who came up with it first, please let us know.

```mw
% Fibonacci sequence generator
fib(C, [P,S], C, N)  :- N is P + S.
fib(C, [P,S], Cv, V) :- succ(C, Cn), N is P + S, !, fib(Cn, [S,N], Cv, V).

fib(0, 0).
fib(1, 1).
fib(C, N) :- fib(2, [0,1], C, N). % Generate from 3rd sequence on
```

Looking at performance:

```
 ?- time(fib(30,X)).
% 86 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 832040 
 ?- time(fib(40,X)).
% 116 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 102334155
 ?- time(fib(100,X)).
% 296 inferences, 0.000 CPU in 0.001 seconds (0% CPU, Infinite Lips)
X = 354224848179261915075 
```

What I really like about this one, is it is also a generator- i.e. capable of generating all the numbers in sequence needing no bound input variables or special Prolog predicate support (such as freeze/3 in the previous example):

```
?- time(fib(X,Fib)).
% 0 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = Fib, Fib = 0 ;
% 1 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = Fib, Fib = 1 ;
% 3 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 2,
Fib = 1 ;
% 5 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 3,
Fib = 2 ;
% 5 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 4,
Fib = 3 ;
% 5 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = Fib, Fib = 5 ;
% 5 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 6,
Fib = 8
...etc.
```

It stays at 5 inferences per iteration after X=3. Also, quite useful:

```
 ?- time(fib(100,354224848179261915075)).
% 296 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
true .

?- time(fib(X,354224848179261915075)).
% 394 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 100 .
```

### Efficient implementation

```mw
% John Devou: 26-Nov-2021
% Efficient program to calculate n-th Fibonacci number.
% Works fast for n ≤ 1 000 000 000.

b(0,Bs,Bs).
b(N,Bs,Res):- N > 0, B is mod(N,2), M is div(N,2), b(M,[B|Bs],Res).

f([],A,_,_,A).
f([X|Xs],A,B,C,Res):- AA is A^2, BB is B^2, A_ is 2*BB-3*AA-C, B_ is AA+BB,
    (X =:= 1 -> T is A_+B_, f(Xs,B_,T,-2,Res); f(Xs,A_,B_,2,Res)).

fib(N,F):- b(N,[],Bs), f(Bs,0,1,2,F), !.
```

**Output:**

```
?- time(fib(30,X)).
% 59 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 832040.

?- time(fib(100,X)).
% 80 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 354224848179261915075.

?- time(fib(500,X)). 
% 102 inferences, 0.000 CPU in 0.000 seconds (?% CPU, Infinite Lips)
X = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125.

?- time(fib(1000000000,_)). 
% 334 inferences, 7.078 CPU in 7.526 seconds (94% CPU, 47 Lips)
true.
```


## Pure

### Tail Recursive

```mw
fib n = loop 0 1 n with
  loop a b n = if n==0 then a else loop b (a+b) (n-1);
end;
```


## Purity

The following takes a natural number and generates an initial segment of the Fibonacci sequence of that length:

```mw
data Fib1 = FoldNat 
            <
              const (Cons One (Cons One Empty)),
              (uncurry Cons) . ((uncurry Add) . (Head, Head . Tail), id)
            >
```

This following calculates the Fibonacci sequence as an infinite stream of natural numbers:

```mw
type (Stream A?,,,Unfold) = gfix X. A? . X?
data Fib2 = Unfold ((outl, (uncurry Add, outl))) ((curry id) One One)
```

As a histomorphism:

```mw
import Histo

data Fib3 = Histo . Memoize 
            <
              const One, 
              (p1 => 
              <
                const One, 
                (p2 => Add (outl $p1) (outl $p2)). UnmakeCofree
              > (outr $p1)) . UnmakeCofree
            >
```


## Python

### Analytic

Binet's formula:

```mw
from math import *

def analytic_fibonacci(n):
  assert isinstance(n,int), "n must be an integer."
  assert n<=71 , "n must be <=71 due to floating point precision limitations."
  sqrt_5 = sqrt(5);
  p = (1 + sqrt_5) / 2;
  q = 1/p;
  return int( (p**n + q**n) / sqrt_5 + 0.5 )

for i in range(1,31):
  print analytic_fibonacci(i),
```

Output:

```
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
```

#### Analytic with wider domain

Binet's formula for Fibonacci numbers up to 91, by using longdoubles:

```mw
def analytic_fibonacci91(m): 
   """
   Binet's algebraic formula for the nth Fibonacci number. 
   Good for up to n=91 
   Uses numpy longdoubles: 

   See: https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
   """

    import numpy as np
    assert isinstance(m,int), "parameter must be an integer."
    assert 0<=m<=91 , "n must be in the range 0 .. 91 due to double precision floating point precision limitations."
    if m < 2: return m
    # Make sure that nothing causes conversion to single
    n=np.longdouble(m)
    C1=np.longdouble(1)
    C2=np.longdouble(2)
    C5=np.longdouble(5)
    Chalf=C1/C2
    Cfifth=C1/C5
    root5=C5**Chalf
    t1=(C1+root5)/C2   
    t2=(C1-root5)/C2  
    f=(t1**n-t2**n)/root5    
    return int(f+0.1)

# Usage
print(f:=[[i,analytic_fibonacci91(i)] for i in range(92)])
```

```
Output
[[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5], [6, 8], [7, 13], [8, 21], [9, 34], [10, 55], [11, 89], [12, 144], [13, 233], [14, 377], [15, 610], [16, 987], [17, 1597], [18, 2584], [19, 4181], [20, 6765], [21, 10946], [22, 17711], [23, 28657], [24, 46368], [25, 75025], [26, 121393], [27, 196418], [28, 317811], [29, 514229], [30, 832040], [31, 1346269], [32, 2178309], [33, 3524578], [34, 5702887], [35, 9227465], [36, 14930352], [37, 24157817], [38, 39088169], [39, 63245986], [40, 102334155], [41, 165580141], [42, 267914296], [43, 433494437], [44, 701408733], [45, 1134903170], [46, 1836311903], [47, 2971215073], [48, 4807526976], [49, 7778742049], [50, 12586269025], [51, 20365011074], [52, 32951280099], [53, 53316291173], [54, 86267571272], [55, 139583862445], [56, 225851433717], [57, 365435296162], [58, 591286729879], [59, 956722026041], [60, 1548008755920], [61, 2504730781961], [62, 4052739537881], [63, 6557470319842], [64, 10610209857723], [65, 17167680177565], [66, 27777890035288], [67, 44945570212853], [68, 72723460248141], [69, 117669030460994], [70, 190392490709135], [71, 308061521170129], [72, 498454011879264], [73, 806515533049393], [74, 1304969544928657], [75, 2111485077978050], [76, 3416454622906707], [77, 5527939700884757], [78, 8944394323791464], [79, 14472334024676221], [80, 23416728348467685], [81, 37889062373143906], [82, 61305790721611591], [83, 99194853094755497], [84, 160500643816367088], [85, 259695496911122585], [86, 420196140727489673], [87, 679891637638612258], [88, 1100087778366101931], [89, 1779979416004714189], [90, 2880067194370816120], [91, 4660046610375530309]]
```

#### Binomial

Binet's algebraic formula as an all integer binomial expansion.

NOTE: This implementation is **NOT** faster than simply progressing up to Fib(n) by addition, starting from Fib(1).

```mw
def fib4k(n): # FIBonacci's numbers, Binet's Formula, Barron's Binomial expansion, Kra's code. 
    # (c) 2025 David A. Kra GNUFDL1.3 and Copyleft Creative Commons CC BY-SA Attribution-ShareAlike
    # 
    # ALL INTEGER. Tested up to Fib(4000).
    # NOTE: This implementation is NOT faster than simply progressing up to Fib(n) by addition, starting from Fib(1).
    # Thanks, Acknowledgement, and Appreciation to Barron https://stackexchange.com/users/9594318/barron 
    # No floats were exploited in the production of this function.
    # References:
    #   https://math.stackexchange.com/questions/674570/prove-that-binets-formula-gives-an-integer-using-the-binomial-theorem
    #   https://math.stackexchange.com/questions/2002702/fibonacci-identity-with-binomial-coefficients
    #   https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
    #       https://latex.artofproblemsolving.com/8/6/d/86d486c560727727342090b432e23ba85ac098b1.png 
    #   https://www.geeksforgeeks.org/find-nth-fibonacci-number-using-binets-formula/
    #   https://discuss.geeksforgeeks.org/comment/540dc728-8cfc-41e3-853e-e920e0a85101/gfg 
    #    # Fn=(1/(2**(n-1))) * SUM(j=0,n//2,((5**j)*comb(n,2*j+1))
    # 
    #   qc == Quick Combination. Instead of using comb, with its loop on each call, 
    #           derive the next (  comb(n,2*j+1)  ) by building up from what had already been calculated, 
    #           Given comb(n,2*j+1), then 
    #                 comb(n,2*(j+1)+1) = comb(n,2*j+1) *  (n-(2*j+1))*(n-2*j+1)-1) // ( (2*j+1)+1)*(2*j+1)+2) )
    #   qp == Quick Power. Instead of using 5**j, derive the next fttj as fttj*=5 
    #
    f=0
    fttj=1
    qc=n # = comb(n,1)
    for j in range(0,int(n/2+1)):
        f+=fttj*qc  # (5**k)*qc #  qc == comb(n,2*k+1)
        j2p1=j*2+1  
        # calculate the 5**k and the combinations for the next iteration,
        #   but for now, k and k2p1 have this iteration's values.
        fttj*=5
        qc=qc* (n-j2p1)*(n-j2p1-1) // ( (j2p1+1)*(j2p1+2) )   # for the next iteration

    f=f//(2 ** (n-1) )
    return f

</syntaxhighlight lang="python">
<pre>
Test

print([[i,fib4k(i)] for i in [4,40,400,4000]])

output

[[4, 3], [40, 102334155], [400, 176023680645013966468226945392411250770384383304492191886725992896575345044216019675], [4000, 39909473435004422792081248094960912600792570982820257852628876326523051818641373433549136769424132442293969306537520118273879628025443235370362250955435654171592897966790864814458223141914272590897468472180370639695334449662650312874735560926298246249404168309064214351044459077749425236777660809226095151852052781352975449482565838369809183771787439660825140502824343131911711296392457138867486593923544177893735428602238212249156564631452507658603400012003685322984838488962351492632577755354452904049241294565662519417235020049873873878602731379207893212335423484873469083054556329894167262818692599815209582517277965059068235543139459375028276851221435815957374273143824422909416395375178739268544368126894240979135322176080374780998010657710775625856041594078495411724236560242597759185543824798332467919613598667003025993715274875]]

</pre>

===Iterative===
<syntaxhighlight lang="python">def fib_iter(n):
    if n < 2:
        return n
    fib_prev = 1
    fib = 1
    for _ in range(2, n):
        fib_prev, fib = fib, fib + fib_prev
    return fib
```

#### Iterative positive and negative

```mw
def fib(n,x=[0,1]):
   for i in range(abs(n)-1): x=[x[1],sum(x)]
   return x[1]*pow(-1,abs(n)-1) if n<0 else x[1] if n else 0

for i in range(-30,31): print fib(i),
```

Output:

```
-832040 514229 -317811 196418 -121393 75025 -46368 28657 -17711 10946 -6765 4181 -2584 1597 -987 
610 -377 233 -144 89 -55 34 -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
```

### Recursive

```mw
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)
```

### Recursive with Memoization

```mw
def fib_memo():
    pad = {0:0, 1:1}
    def sub_func(n):
        if not n in pad:
            pad[n] = sub_func(n-1) + sub_func(n-2)
        return pad[n]
    return sub_func

fm = fib_memo()
for i in range(1,31):
    print(fm(i))
```

Output:

```
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
```

### Better Recursive doesn't need Memoization

The recursive code as written two sections above is incredibly slow and inefficient due to the nested recursion calls. Although the memoization above makes the code run faster, it is at the cost of extra memory use. The below code is syntactically recursive but actually encodes the efficient iterative process, and thus doesn't require memoization:

```mw
def fib_fast_rec(n):
    def inner_fib(prvprv, prv, c):
        if c < 1: 
            return prvprv
        return inner_fib(prv, prvprv + prv, c - 1) 
    return inner_fib(0, 1, n)
```

However, although much faster and not requiring memory, the above code can only work to a limited 'n' due to the limit on stack recursion depth by Python; it is better to use the iterative code above or the generative one below.

### Generative

```mw
def fib_gen(n):
    a, b = 0, 1
    while n>0:
        yield a
        a, b, n = b, a+b, n-1
```

#### Example use

```mw
>>> [i for i in fib_gen(11)]

[0,1,1,2,3,5,8,13,21,34,55]
```

### Matrix-Based

Translation of the matrix-based approach used in F#.

```mw
def prev_pow_two(n):
    """Gets the power of two that is less than or equal to the given input
    """
    if ((n & -n) == n):
        return n
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n//2

def crazy_fib(n):
    """Crazy fast fibonacci number calculation
    """
    pow_two = prev_pow_two(n)
    
    q = r = i = 1
    s = 0
    
    while i < pow_two:
        i *= 2
        q, r, s = q*q + r*r, r * (q + s), (r*r + s*s)
        
    while i < n:
        i += 1
        q, r, s = q+r, q, r
        
    return q
```

### Large step recurrence

This is much faster for a single, large value of n:

```mw
def fib(n, c={0:1, 1:1}):
    if n not in c:
        x = n // 2
        c[n] = fib(x-1) * fib(n-x-1) + fib(x) * fib(n - x)
    return c[n]

fib(10000000)  # calculating it takes a few seconds, printing it takes eons
```

### Same as above but slightly faster

Putting the dictionary outside the function makes this about 2 seconds faster, could just make a wrapper:

```mw
F = {0: 0, 1: 1, 2: 1}
def fib(n):
    if n in F:
        return F[n]
    f1 = fib(n // 2 + 1)
    f2 = fib((n - 1) // 2)
    F[n] = (f1 * f1 + f2 * f2 if n & 1 else f1 * f1 - f2 * f2)
    return F[n]
```

### Generative with Recursion

This can get very slow and uses a lot of memory. Can be sped up by caching the generator results.

```mw
def fib():
    """Yield fib[n+1] + fib[n]"""
    yield 1
    lhs, rhs = fib(), fib()
    # move lhs one iteration ahead
    yield next(lhs)
    while True:
        yield next(lhs)+next(rhs)

f=fib()
print [next(f) for _ in range(9)]
```

Output:

```
[1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Another version of recursive generators solution, starting from 0**

```mw
from itertools import islice

def fib():
    yield 0
    yield 1
    a, b = fib(), fib()
    next(b)
    while True:
        yield next(a)+next(b)
 
print(tuple(islice(fib(), 10)))
```

### As a scan or a fold

#### itertools.accumulate

The Fibonacci series can be defined quite simply and efficiently as a scan or accumulation, in which the accumulator is a pair of the two last numbers.

Works with

:

Python

version 3.7

```mw
def fibs(n):
    """Fibonacci accumulation

    An accumulation of the first n integers in the Fibonacci series. The accumulator is a
    pair of the two preceding numbers.
    """
    # Local import is more efficient.
    from itertools import accumulate

    # Note: Numbers generated in range(1, n) [or range(n-1)] call will not be used.
    return [a for a, b in accumulate(
        range(1, n),
        lambda acc, _: (acc[1],  sum(acc)),
        initial = (0, 1)
        )
    ]

# MAIN ---
if __name__ == '__main__':
    print(f'First twenty: {fibs(20)}')
```

**Output:**

```
First twenty: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
```

#### functools.reduce

A fold can be understood as an amnesic scan, and functools.reduce can provide a useful and efficient re-write of the scanning version above, if we only need the Nth term in the series:

Works with

:

Python

version 3.7

```mw
def nth_fib(n):
    """Nth Fibonacci term (by folding)
    
    Nth integer in the Fibonacci series.
    """
    from functools import reduce
    return reduce(
        lambda acc, _: (acc[1], sum(acc)),
        range(1, n),
        (0, 1)
    )[0]

# MAIN ---
if __name__ == '__main__':
    n = 1000
    print(f'{n}th term: {nth_fib(n)}')
```

**Output:**

```
1000th term: 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
```

Works with

:

Python

version 3.9

```mw
def fib(n):
    from functools import reduce
    return reduce(lambda x, y: (x[1], x[0] + x[1]), range(n), (0, 1))[0]
```

### Array and Range

```mw
fibseq = [1,1,]
fiblength = 21
for x in range(1,fiblength-1):
   xcount = fibseq[x-1] + fibseq[x]
   fibseq.append(xcount)
print(xcount)
```

**Output:**

```
10946
```


## Qi

### Recursive

```mw
(define fib
  0 -> 0
  1 -> 1
  N -> (+ (fib-r (- N 1))
          (fib-r (- N 2))))
```

### Iterative

```mw
(define fib-0
  V2 V1 0 -> V2
  V2 V1 N -> (fib-0 V1 (+ V2 V1) (1- N)))

(define fib
  N -> (fib-0 0 1 N))
```


## Quackery

```mw
  [ 0 1 rot times [ tuck + ] drop ] is fibo ( n --> n )

  100 fibo echo
```

**Output:**

```
354224848179261915075
```


## Quirl

### Using Binet's formula

Also works for negative indices.

```mw
fib(Int) = div(sub(pow(1/2+1/2\5 $a) pow(1/2-1/2\5 $a)) \5)
```

### Recursive

This definition uses only Quirl's core functions. Automatic memoization makes it quick, but it is limited by the recursion stack size. Also works for negative indices.

```mw
fib(0)              = 0;
fib(1)              = 1;
fib(Int):ord(2  $a) = add(fib@add($a -2)     fib@add($a -1));
fib(Int):ord($a -1) = add(fib@add($a  2) neg@fib@add($a  1))
```


## R

### Iterative positive and negative

```mw
fib=function(n,x=c(0,1)) {
   if (abs(n)>1) for (i in seq(abs(n)-1)) x=c(x[2],sum(x))
   if (n<0) return(x[2]*(-1)^(abs(n)-1)) else if (n) return(x[2]) else return(0)
}  

sapply(seq(-31,31),fib)
```

Output:

```
 [1] 1346269 -832040  514229 -317811  196418 -121393   75025  -46368   28657
[10]  -17711   10946   -6765    4181   -2584    1597    -987     610    -377
[19]     233    -144      89     -55      34     -21      13      -8       5
[28]      -3       2      -1       1       0       1       1       2       3
[37]       5       8      13      21      34      55      89     144     233
[46]     377     610     987    1597    2584    4181    6765   10946   17711
[55]   28657   46368   75025  121393  196418  317811  514229  832040 1346269
```

### Other methods

```mw
# recursive
recfibo <- function(n) {
  if ( n < 2 ) n
  else Recall(n-1) + Recall(n-2)
}

# print the first 21 elements
print.table(lapply(0:20, recfibo))

# iterative
iterfibo <- function(n) {
  if ( n < 2 )
    n
  else {
    f <- c(0, 1)
    for (i in 2:n) {
      t <- f[2]
      f[2] <- sum(f)
      f[1] <- t
    }
    f[2]
  }
}

print.table(lapply(0:20, iterfibo))

# iterative but looping replaced by map-reduce'ing
funcfibo <- function(n) {
  if (n < 2) 
    n
  else {
    generator <- function(f, ...) {
      c(f[2], sum(f))
    }
    Reduce(generator, 2:n, c(0,1))[2]
  }
}

print.table(lapply(0:20, funcfibo))
```

Note that an idiomatic way to implement such low level, basic arithmethic operations in R is to implement them C and then call the compiled code.

**Output:**

All three solutions print

```
 [1] 0    1    1    2    3    5    8    13   21   34   55   89   144  233  377 
[16] 610  987  1597 2584 4181 6765
```


## Ra

```mw
class FibonacciSequence
   **Prints the nth fibonacci number**
   
   on start
      
      args := program arguments
      
      if args empty
         print .fibonacci(8)
      
      else
         
         try
            print .fibonacci(integer.parse(args[0]))
         
         catch FormatException
            print to Console.error made !, "Input must be an integer"
            exit program with error code
         
         catch OverflowException
            print to Console.error made !, "Number too large"
            exit program with error code
   
   define fibonacci(n as integer) as integer is shared
      **Returns the nth fibonacci number**
      
      test
         assert fibonacci(0) = 0
         assert fibonacci(1) = 1
         assert fibonacci(2) = 1
         assert fibonacci(3) = 2
         assert fibonacci(4) = 3
         assert fibonacci(5) = 5
         assert fibonacci(6) = 8
         assert fibonacci(7) = 13
         assert fibonacci(8) = 21

      
      body
         a, b := 0, 1
      
         for n
            a, b := b, a + b
      
         return a
```


## Racket

### Tail Recursive

```mw
(define (fib n)
  (let loop ((cnt 0) (a 0) (b 1))
    (if (= n cnt)
        a
        (loop (+ cnt 1) b (+ a b)))))
```

```mw
(define (fib n (a 0) (b 1))
  (if (< n 2)
      1
      (+ a (fib (- n 1) b (+ a b)))))
```

### Matrix Form

```mw
#lang racket

(require math/matrix)

(define (fibmat n) (matrix-ref 
                    (matrix-expt (matrix ([1 1]
                                          [1 0])) 
                                 n) 
                    1 0))

(fibmat 1000)
```

### Foldl Form

```mw
(define (fib n)
  (car (foldl (lambda (y x)
                (let ((a (car x)) (b (cdr x)))
                  (cons b (+ a b)))) (cons 0 1) (range n))))
```


## Raku

(formerly Perl 6)

### List Generator

This constructs the fibonacci sequence as a lazy infinite list.

```mw
constant @fib = 0, 1, *+* ... *;
```

If you really need a function for it:

```mw
sub fib ($n) { @fib[$n] }
```

To support negative indices:

```mw
constant @neg-fib = 0, 1, *-* ... *;
sub fib ($n) { $n >= 0 ?? @fib[$n] !! @neg-fib[-$n] }
```

### Iterative

```mw
sub fib (Int $n --> Int) {
    $n > 1 or return $n;
    my ($prev, $this) = 0, 1;
    ($prev, $this) = $this, $this + $prev for 1 ..^ $n;
    return $this;
}
```

### Recursive

```mw
proto fib (Int $n --> Int) {*}
multi fib (0)  { 0 }
multi fib (1)  { 1 }
multi fib ($n) { fib($n - 1) + fib($n - 2) }
```


## Rapira

### Iterative

```mw
fun fibonacci(n)
    if n = 0 then
        return 0
    fi
    if n = 1 then
        return 1
    fi
    return fibonacci(n - 1) + fibonacci(n - 2)
end
```


## RASEL

```mw
1&-:?v2\:2\01\--2\
     >$.@
```


## RATFOR

```mw
program Fibonacci
#
integer*4 count, loop
integer*4 num1, num2, fib 

1 format(A)
2 format(I4)
3 format(I6,' ')
4 format(' ')
write(6,1,advance='no')'How Many: '
read(5,2)count

num1 = 0
num2 = 1
write(6,3,advance='no')num1
write(6,3,advance='no')num2

for (loop = 3; loop<=count; loop=loop+1)
      {
          fib = num1 + num2
          write(6,3,advance='no')fib
          num1 = num2
          num2 = fib
       }
write(6,4)
end
```


## Rebol

Translation of

:

Red

```mw
Rebol [
    title: "Rosetta code: Fibonacci sequence"
    file:  %Fibonacci_sequence.r3
    url:   https://rosettacode.org/wiki/Fibonacci_sequence
]

fibonacci: function/with [
    {Return the Nth Fibonacci number using iterative state advancement.
    Uses a shared block to swap fn and fn-1 in a single expression.}
    number [integer!]  "which Fibonacci number to compute (0-indexed)"
][
    fn-1: 0                                    ;; F(0)
    fn:   1                                    ;; F(1)
    loop number advance-fibonacci
][
    fn: fn-1: 0
    advance-fibonacci: [ fn: fn-1 + fn-1: fn ] ;; simultaneously: new fn = old fn + old fn-1
]

probe collect [repeat i 18 [keep fibonacci i]]
```

**Output:**

```
[1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181]
```


## Red

(unnecessarily, but pleasantly palindromic)

```mw
Red []

palindrome: [fn: fn-1 + fn-1: fn]
fibonacci: func [n][
   fn-1: 0
   fn: 1
   loop n palindrome
]
```


## Refal

```mw
$ENTRY Go {
    = <Prout <Repeat 18 Fibonacci 1 1>>
} ;

Repeat {
    0   s.F e.X = e.X;
    s.N s.F e.X = <Repeat <- s.N 1> s.F <Mu s.F e.X>>;
};

Fibonacci {
    e.X s.A s.B = e.X s.A s.B <+ s.A s.B>;
};
```

**Output:**

```
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```


## Relation

```mw
function fibonacci (n)
if n < 2 
set result = n
else
set f0 = 0
set f1 = 1
set k = 2
while k <= n
set result = f0 + f1
set f0 = f1
set f1 = result
set k = k + 1
end while
end if
end function
```


## Retro

### Recursive

```mw
: fib ( n-m ) dup [ 0 = ] [ 1 = ] bi or if; [ 1- fib ] sip [ 2 - fib ] do + ;
```

### Iterative

```mw
: fib ( n-N )
  [ 0 1 ] dip [ over + swap ] times drop ;
```


## REXX

**Include** How to use **Include** Source code Without special measures, the closed formula requires floating point calculations (exponentiation and root) in high precision if you want to calculate F1000 and on. For a given number, below program shows both running the whole sequence up to that number and using the formula.

```mw
-- 19 Sep 2025
include Setting

say 'FIBONACCI SEQUENCE'
say version
say
say 'Fibonacci numbers up to F100 are...'
call Fibonacci1 100
say
call Timer 'r'
say 'Selected Fibonacci numbers using recurrence...'
call Fibonacci2 1e2
call Fibonacci2 1e3
call Fibonacci2 1e4
call Fibonacci2 1e5
call Fibonacci2 1e6
say
call Timer 'r'
say 'Selected Fibonacci numbers using closed formula...'
call Fibonacci3 1e2
call Fibonacci3 1e3
call Fibonacci3 1e4
call Fibonacci3 1e5
say
call Timer 'r'
exit

Fibonacci1:
-- Show sequence
arg xx
numeric digits 25
call CharOut ,Right(0,22) Right(1,21)
a=0; b=1
do i=2 to xx
   c=b+a; a=b; b=c
   call CharOut ,Right(c,22)
   if i//5=4 | i//5=9 then
      say
end
say
return

Fibonacci2:
-- Get specific number sequence
arg xx
numeric digits xx/4
a=0; b=1
do i=2 to xx
   f=b+a; a=b; b=f
end
say 'F'xx '=' Left(f,10)'...'Right(f,10) '('Xpon(f) 'digits)' elaps('r')'s'
return

Fibonacci3:
-- Get specific number formula
arg xx
numeric digits xx/4
f=Round(((0.5*(1+SqRt(5)))**xx-(0.5*(1-SqRt(5)))**xx)/SqRt(5))/1
say 'F'xx '=' Left(f,10)'...'Right(f,10) '('Xpon(f) 'digits)' elaps('r')'s'
return

include Math
```

**Output:**

```
FIBONACCI SEQUENCE
REXX-ooRexx_5.1.0(MT)_64-bit 6.05 2 May 2025

Fibonacci numbers up to F100 are...
                     0                     1                     1                     2                     3
                     5                     8                    13                    21                    34
                    55                    89                   144                   233                   377
                   610                   987                  1597                  2584                  4181
                  6765                 10946                 17711                 28657                 46368
                 75025                121393                196418                317811                514229
                832040               1346269               2178309               3524578               5702887
               9227465              14930352              24157817              39088169              63245986
             102334155             165580141             267914296             433494437             701408733
            1134903170            1836311903            2971215073            4807526976            7778742049
           12586269025           20365011074           32951280099           53316291173           86267571272
          139583862445          225851433717          365435296162          591286729879          956722026041
         1548008755920         2504730781961         4052739537881         6557470319842        10610209857723
        17167680177565        27777890035288        44945570212853        72723460248141       117669030460994
       190392490709135       308061521170129       498454011879264       806515533049393      1304969544928657
      2111485077978050      3416454622906707      5527939700884757      8944394323791464     14472334024676221
     23416728348467685     37889062373143906     61305790721611591     99194853094755497    160500643816367088
    259695496911122585    420196140727489673    679891637638612258   1100087778366101931   1779979416004714189
   2880067194370816120   4660046610375530309   7540113804746346429  12200160415121876738  19740274219868223167
  31940434634990099905  51680708854858323072  83621143489848422977 135301852344706746049 218922995834555169026
 354224848179261915075

0.001 seconds

Selected Fibonacci numbers using recurrence...
F1E2 = 3542248481...9261915075 (20 digits) 0.001s
F1E3 = 4346655768...6849228875 (208 digits) 0.001s
F1E4 = 3364476487...9947366875 (2089 digits) 0.026s
F1E5 = 2597406934...3428746875 (20898 digits) 2.818s
F1E6 = 1953282128...8242546875 (208987 digits) 279.338s

282.183 seconds

Selected Fibonacci numbers using closed formula...
F1E2 = 3542248481...9261915075 (20 digits) 0s
F1E3 = 4346655768...6849228875 (208 digits) 0.004s
F1E4 = 3364476487...9947366875 (2089 digits) 0.511s
F1E5 = 2597406934...3428746875 (20898 digits) 60.319s

60.834 seconds
```

Maybe a surprise, but in REXX running the whole sequence for getting 1 number is faster.


## Rhombus

### Recursive

```mw
#lang rhombus/static

fun fib:
| fib(0): 1
| fib(1): 1
| fib(n): fib(n-2) + fib(n-1)
```

### Recursive with Memoization

```mw
#lang rhombus/static

def cache = MutableMap()

fun fib:
| fib(0): 1
| fib(1): 1
| fib(n):
    guard n !in cache | cache[n]
    let result = fib(n-2) + fib(n-1)
    cache[n] := result
    result

fib(100) // 573147844013817084101
```
