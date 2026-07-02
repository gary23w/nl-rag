---
title: "Fibonacci sequence (part 6/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/10
---

## Mathematica / Wolfram Language

The Wolfram Language already has a built-in function Fibonacci, but a simple recursive implementation would be

```mw
fib[0] = 0
fib[1] = 1
fib[n_Integer] := fib[n - 1] + fib[n - 2]
```

An optimization is to cache the values already calculated:

```mw
fib[0] = 0
fib[1] = 1
fib[n_Integer] := fib[n] = fib[n - 1] + fib[n - 2]
```

The above implementations may be too simplistic, as the first is incredibly slow for any reasonable range due to nested recursions and while the second is faster it uses an increasing amount of memory. The following uses recursion much more effectively while not using memory:

```mw
fibi[prvprv_Integer, prv_Integer, rm_Integer] :=
  If[rm < 1, prvprv, fibi[prv, prvprv + prv, rm - 1]]
fib[n_Integer] := fibi[0, 1, n]
```

However, the recursive approaches in Mathematica are limited by the limit set for recursion depth (default 1024 or 4096 for the above cases), limiting the range for 'n' to about 1000 or 2000. The following using an iterative approach has an extremely high limit (greater than a million):

```mw
fib[n_Integer] := Block[{tmp, prvprv = 0, prv = 1},
  For[i = 0, i < n, i++, tmp = prv; prv += prvprv; prvprv = tmp];
  Return[prvprv]]
```

If one wanted a list of Fibonacci numbers, the following is quite efficient:

```mw
fibi[{prvprv_Integer, prv_Integer}] := {prv, prvprv + prv}
fibList[n_Integer] := Map[Take[#, 1] &, NestList[fibi, {0, 1}, n]] // Flatten
```

Output from the last with "fibList[100]":

```mw
{0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, \
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, \
196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, \
9227465, 14930352, 24157817, 39088169, 63245986, 102334155, \
165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, \
2971215073, 4807526976, 7778742049, 12586269025, 20365011074, \
32951280099, 53316291173, 86267571272, 139583862445, 225851433717, \
365435296162, 591286729879, 956722026041, 1548008755920, \
2504730781961, 4052739537881, 6557470319842, 10610209857723, \
17167680177565, 27777890035288, 44945570212853, 72723460248141, \
117669030460994, 190392490709135, 308061521170129, 498454011879264, \
806515533049393, 1304969544928657, 2111485077978050, \
3416454622906707, 5527939700884757, 8944394323791464, \
14472334024676221, 23416728348467685, 37889062373143906, \
61305790721611591, 99194853094755497, 160500643816367088, \
259695496911122585, 420196140727489673, 679891637638612258, \
1100087778366101931, 1779979416004714189, 2880067194370816120, \
4660046610375530309, 7540113804746346429, 12200160415121876738, \
19740274219868223167, 31940434634990099905, 51680708854858323072, \
83621143489848422977, 135301852344706746049, 218922995834555169026, \
354224848179261915075}
```

The Wolfram Language can also solve recurrence equations using the built-in function RSolve

```mw
fib[n] /. RSolve[{fib[n] == fib[n - 1] + fib[n - 2], fib[0] == 0, 
    fib[1] == 1}, fib[n], n][[1]]
```

which evaluates to the built-in function Fibonacci[n]

This function can also be expressed as

```mw
Fibonacci[n] // FunctionExpand // FullSimplify
```

which evaluates to

```mw
(2^-n ((1 + Sqrt[5])^n - (-1 + Sqrt[5])^n Cos[n π]))/Sqrt[5]
```

and is defined for all real or complex values of n.


## MATLAB

### Matrix

Translation of

:

Julia

```mw
function f = fib(n)
   
   f = [1 1 ; 1 0]^(n-1);
   f = f(1,1);
   
end
```

### Iterative

```mw
function F = fibonacci(n)
    
    Fn = [1 0]; %Fn(1) is F_{n-2}, Fn(2) is F_{n-1} 
    F = 0; %F is F_{n}
    
    for i = (1:abs(n))
        Fn(2) = F;
        F = sum(Fn);
        Fn(1) = Fn(2);
    end
        
    if n < 0
        F = F*((-1)^(n+1));
    end   

end
```

### Dramadah Matrix Method

The MATLAB help file suggests an interesting method of generating the Fibonacci numbers. Apparently the determinate of the Dramadah Matrix of type 3 (MATLAB designation) and size n-by-n is the nth Fibonacci number. This method is implimented below.

```mw
function number = fibonacci2(n)
    
    if n == 1
        number = 1;
    elseif n == 0
        number = 0;
    elseif n < 0
        number = ((-1)^(n+1))*fibonacci2(-n);;
    else
        number = det(gallery('dramadah',n,3));
    end

end
```

### Tartaglia/Pascal Triangle Method

```mw
function number = fibonacci(n)
%construct the Tartaglia/Pascal Triangle
    pt=tril(ones(n));
    for r = 3 : n
    % Every element is the addition of the two elements
    % on top of it. That means the previous row.
        for c = 2 : r-1
            pt(r, c) = pt(r-1, c-1) + pt(r-1, c);
        end   
    end
    number=trace(rot90(pt));
end
```


## Maxima

```mw
/* fib(n) is built-in; here is an implementation */
fib2(n) := (matrix([0, 1], [1, 1])^^n)[1, 2]$

fib2(100)-fib(100);
0

fib2(-10);
-55
```


## MAXScript

### Iterative

```mw
fn fibIter n =
(
    if n < 2 then
    (
        n
    )
    else
    (
        fib = 1
        fibPrev = 1
        for num in 3 to n do
        (
            temp = fib
            fib += fibPrev
            fibPrev = temp
        )
        fib
    ) 
)
```

### Recursive

```mw
fn fibRec n =
(
    if n < 2 then
    (
        n
    )
    else
    (
        fibRec (n - 1) + fibRec (n - 2)
    )
)
```


## Mercury

Mercury is both a logic language and a functional language. As such there are two possible interfaces for calculating a Fibonacci number. This code shows both styles. Note that much of the code here is ceremony put in place to have this be something which can actually compile. The actual Fibonacci number generation is contained in the predicate `fib/2` and in the function `fib/1`. The predicate `main/2` illustrates first the unification semantics of the predicate form and the function call semantics of the function form.

The provided code uses a very naive form of generating a Fibonacci number. A more realistic implementation would use memoization to cache previous results, exchanging time for space. Also, in the case of supplying both a function implementation and a predicate implementation, one of the two would be implemented in terms of the other. Examples of this are given as comments below.

### fib.m

```mw
% The following code is derived from the Mercury Tutorial by Ralph Becket.
% http://www.mercury.csse.unimelb.edu.au/information/papers/book.pdf
:- module fib.
 
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
 
:- implementation.
:- import_module int.
 
:- pred fib(int::in, int::out) is det.
fib(N, X) :-
    ( if N =< 2
          then X = 1
          else fib(N - 1, A), fib(N - 2, B), X = A + B ).
 
:- func fib(int) = int is det.
fib(N) = X :- fib(N, X).
 
main(!IO) :-
    fib(40, X),
    write_string("fib(40, ", !IO),
    write_int(X, !IO),
    write_string(")\n", !IO),
 
    write_string("fib(40) = ", !IO),
    write_int(fib(40), !IO),
    write_string("\n", !IO).
```

### Iterative algorithm

The much faster iterative algorithm can be written as:

```mw
:- pred fib_acc(int::in, int::in, int::in, int::in, int::out) is det.

fib_acc(N, Limit, Prev2, Prev1, Res) :-
    ( N < Limit ->
        % limit not reached, continue computation.
        ( N =< 2 ->
            Res0 = 1
        ;
            Res0 = Prev2 + Prev1
        ),
        fib_acc(N+1, Limit, Prev1, Res0, Res)
    ;
        % Limit reached, return the sum of the two previous results.
        Res = Prev2 + Prev1
    ).
```

This predicate can be called as

```mw
fib_acc(1, 40, 1, 1, Result)
```

It has several inputs which form the loop, the first is the current number, the second is a limit, ie when to stop counting. And the next two are accumulators for the last and next-to-last results.

### Memoization

But what if you want the speed of the fib_acc with the recursive (more declarative) definition of fib? Then use memoization, because Mercury is a pure language fib(N, F) will always give the same F for the same N, guaranteed. Therefore memoization asks the compiler to use a table to remember the value for F for any N, and it's a one line change:

```mw
:- pragma memo(fib/2).
:- pred fib(int::in, int::out) is det.
fib(N, X) :-
    ( if N =< 2
          then X = 1
          else fib(N - 1, A), fib(N - 2, B), X = A + B ).
```

We've shown the definition of fib/2 again, but the only change here is the memoization pragma (see the reference manual). This is not part of the language specification and different Mercury implementations are allowed to ignore it, however there is only one implementation so in practice memoization is fully supported.

Memoization trades speed for space, a table of results is constructed and kept in memory. So this version of fib consumes more memory than than fib_acc. It is also slightly slower than fib_acc since it must manage its table of results but it is much much faster than without memoization. Memoization works very well for the Fibonacci sequence because in the naive version the same results are calculated over and over again.


## Metafont

```mw
vardef fibo(expr n) =
if n=0: 0
elseif n=1: 1
else:
  fibo(n-1) + fibo(n-2)
fi
enddef;

for i=0 upto 10: show fibo(i); endfor
end
```


## min

Works with

:

min

version 0.37.0

```mw
(
  (2 <)
  (pred (1 0 (over + swap)) dip times pop)
  unless
) ^fib
```


## MiniScript

An efficient solution (for n >= 0):

```mw
fibonacci = function(n)
    if n < 2 then return n
    n1 = 0
    n2 = 1
    for i in range(n-1, 1)
        ans = n1 + n2
        n1 = n2
        n2 = ans
    end for
    return ans
end function

print fibonacci(6)
```

And for comparison, a recursive solution (also for n >= 0):

```mw
rfib = function(n)
    if n < 1 then return 0
    if n == 1 then return 1
    return rfib(n-1) + rfib(n-2)
end function

print rfib(6)
```


## MiniZinc

```mw
function var int: fibonacci(int: n) =
  let {
    array[0..n] of var int: fibonacci;
    constraint forall(a in 0..n)(
      fibonacci[a] = if (a == 0 \/ a == 1) then
        a
      else
        fibonacci[a-1]+fibonacci[a-2]
      endif
    )
  } in fibonacci[n];
 
var int: fib = fibonacci(6);
solve satisfy;
output [show(fib),"\n"];
```


## MIPS Assembly

This is the iterative approach to the Fibonacci sequence.

```mw
   .text
main: li $v0, 5      # read integer from input. The read integer will be stroed in $v0
   syscall
   
   beq   $v0, 0, is1
   beq   $v0, 1,  is1   
   
   li $s4, 1      # the counter which has to equal to $v0   
      
   li $s0, 1
   li $s1, 1

loop: add   $s2, $s0, $s1
   addi  $s4, $s4, 1
   beq   $v0, $s4, iss2
   
   add   $s0, $s1, $s2
   addi  $s4, $s4, 1
   beq   $v0, $s4, iss0
   
   add   $s1, $s2, $s0
   addi  $s4, $s4, 1
   beq   $v0, $s4, iss1

   b  loop

iss0: move  $a0, $s0 
   b  print

iss1: move  $a0, $s1 
   b  print

iss2: move  $a0, $s2 
   b  print
   
   
is1:  li $a0, 1
   b  print
   
print:   li $v0, 1
   syscall
   li $v0, 10
   syscall
```


## Mirah

```mw
def fibonacci(n:int)
    return n if n < 2
    fibPrev = 1
    fib = 1
    3.upto(Math.abs(n)) do 
        oldFib = fib
        fib = fib + fibPrev
        fibPrev = oldFib
    end
    fib * (n<0 ? int(Math.pow(n+1, -1)) : 1)
end

puts fibonacci 1
puts fibonacci 2
puts fibonacci 3
puts fibonacci 4
puts fibonacci 5
puts fibonacci 6
puts fibonacci 7
```


## МК-61/52

```mw
П0  1  lg Вx <->   +  L0 03 С/П   БП
03
```

Instruction: *n* В/О С/П, where *n* is serial number of the number of Fibonacci sequence; С/П for the following numbers.


## ML

### Standard ML

#### Tail Recursion

This version is tail recursive.

```mw
fun fib n = 
    let
   fun fib' (0,a,b) = a
     | fib' (n,a,b) = fib' (n-1,a+b,a)
    in
   fib' (n,0,1)
    end
```

#### Recursion

```mw
fun fib n = if n < 2 then n else fib (n - 1) + fib (n - 2)
```

### MLite

#### Recursion

Tail recursive.

```mw
fun fib 
        (0, x1, x2) = x2
      | (n, x1, x2) = fib (n-1, x2, x1+x2)
      | n = fib (n, 0, 1)
```


## ML/I

```mw
MCSKIP "WITH" NL
"" Fibonacci - recursive
MCSKIP MT,<>
MCINS %.
MCDEF FIB WITHS ()
AS <MCSET T1=%A1.
MCGO L1 UNLESS 2 GR T1
%T1.<>MCGO L0
%L1.%FIB(%T1.-1)+FIB(%T1.-2).>
fib(0) is FIB(0)
fib(1) is FIB(1)
fib(2) is FIB(2)
fib(3) is FIB(3)
fib(4) is FIB(4)
fib(5) is FIB(5)
```


## Modula-2

```mw
MODULE Fibonacci;
FROM FormatString IMPORT FormatString;
FROM Terminal IMPORT WriteString,WriteLn,ReadChar;

PROCEDURE Fibonacci(n : LONGINT) : LONGINT;
VAR
    a,b,c : LONGINT;
BEGIN
    IF n<0 THEN RETURN 0 END;

    a:=1;
    b:=1;

    WHILE n>0 DO
        c := a + b;
        a := b;
        b := c;
        DEC(n)
    END;

    RETURN a
END Fibonacci;

VAR
    buf : ARRAY[0..63] OF CHAR;
    i : INTEGER;
    r : LONGINT;
BEGIN
    FOR i:=0 TO 10 DO
        r := Fibonacci(i);

        FormatString("%l\n", buf, r);
        WriteString(buf);
    END;

    ReadChar
END Fibonacci.
```


## Modula-3

### Recursive

```mw
PROCEDURE Fib(n: INTEGER): INTEGER =
  BEGIN
    IF n < 2 THEN
      RETURN n;
    ELSE
      RETURN Fib(n-1) + Fib(n-2);
    END;
  END Fib;
```

### Iterative (with negatives)

```mw
PROCEDURE IterFib(n: INTEGER): INTEGER =

VAR

  limit := ABS(n);
  prev := 0;
  curr, next: INTEGER;

BEGIN

  (* trivial case *)
  IF n = 0 THEN RETURN 0; END;

  IF n > 0 THEN (* positive case *)

    curr := 1;
    FOR i := 2 TO limit DO
      next := prev + curr;
      prev := curr;
      curr := next;
    END;

  ELSE (* negative case *)

    curr := -1;
    FOR i := 2 TO limit DO
      next := prev - curr;
      prev := curr;
      curr := next;
    END;

  END;

  RETURN curr;

END IterFib;
```


## Monicelli

Recursive version. It includes a main that reads a number N from standard input and prints the Nth Fibonacci number.

```mw
# Main
Lei ha clacsonato
voglio un nonnulla, Necchi mi porga un nonnulla
il nonnulla come se fosse brematurata la supercazzola bonaccia con il nonnulla o scherziamo?
un nonnulla a posterdati

# Fibonacci function 'bonaccia'
blinda la supercazzola Necchi bonaccia con antani Necchi o scherziamo? che cos'è l'antani? 
minore di 3: vaffanzum 1! o tarapia tapioco: voglio unchiamo, Necchi come se fosse brematurata 
la supercazzola bonaccia con antani meno 1 o scherziamo? voglio duechiamo, 
Necchi come se fosse brematurata la supercazzola bonaccia con antani meno 2 o scherziamo? vaffanzum 
unchiamo più duechiamo! e velocità di esecuzione
```


## MontiLang

Reads number from standard input and prints to that number in the fibonacci sequence

```mw
0 VAR a .
1 VAR b .
INPUT TOINT
FOR :
    a b + VAR c .
    a PRINT .
    b VAR a .
    c VAR b .
ENDFOR
```

Forth-style solution

```mw
def over
    swap dup rot swap
enddef

|Enter a number to obtain Fibonacci sequence: | input nip var count .
0 1
FOR count
    over out |, | out . + swap
ENDFOR
. print
input
clear
```

Simpler

```mw
|Enter a number to obtain Fibonacci sequence: | input nip 1 - var count .
0 1
FOR count
    out |, | out . dup rot +
ENDFOR
print
input   /# wait until press ENTER #/
clear   /# empties the stack #/
```


## Moonli

Recursive but memoized version that still takes O(n) time. In fact, repeated calls are faster than O(n).

```mw
let table = make-hash-table():
  defun fib(n):
    if gethash(n, table): gethash(n, table)
    elif (n < 2): n
    else: gethash(n, table) = fib(n - 1) + fib(n - 2)
    end
  end
end
```


## MUMPS

### Iterative

```mw
FIBOITER(N)
 ;Iterative version to get the Nth Fibonacci number
 ;N must be a positive integer
 ;F is the tree containing the values
 ;I is a loop variable.
 QUIT:(N\1'=N)!(N<0) "Error: "_N_" is not a positive integer."
 NEW F,I
 SET F(0)=0,F(1)=1
 QUIT:N<2 F(N)
 FOR I=2:1:N SET F(I)=F(I-1)+F(I-2)
 QUIT F(N)
```

```
USER>W $$FIBOITER^ROSETTA(30)
832040
```


## Nanoquery

### Iterative

```mw
def fibIter(n)
        if (n < 2)
                return n
        end if
 
        $fib = 1
        $fibPrev = 1
 
   for num in range(2, n - 1)
                fib += fibPrev
                fibPrev = fib - fibPrev
        end for
 
        return fib
end
```


## Nemerle

### Recursive

```mw
using System;
using System.Console;

module Fibonacci
{
    Fibonacci(x : long) : long
    {
        |x when x < 2 => x
        |_ => Fibonacci(x - 1) + Fibonacci(x - 2)
    }
    
    Main() : void
    {
        def num = Int64.Parse(ReadLine());
        foreach (n in $[0 .. num])
            WriteLine("{0}: {1}", n, Fibonacci(n));
    }
}
```

### Tail Recursive

```mw
Fibonacci(x : long, current : long, next : long) : long
{
    match(x)
    {
        |0 => current
        |_ => Fibonacci(x - 1, next, current + next)
    }
}
  
Fibonacci(x : long) : long
{
    Fibonacci(x, 0, 1)
}
```


## NESL

### Recursive

```mw
function fib(n) = if n < 2 then n else fib(n - 2) + fib(n - 1);
```


## NetRexx

Translation of

:

REXX

```mw
/* NetRexx */

options replace format comments java crossref savelog symbols

numeric digits 210000                  /*prepare for some big 'uns.     */
parse arg x y .                        /*allow a single number or range.*/
if x == '' then do                     /*no input? Then assume -30-->+30*/
  x = -30
  y = -x
  end

if y == '' then y = x             /*if only one number, show fib(n)*/
loop k = x to y                   /*process each Fibonacci request.*/
  q = fib(k)
  w = q.length                    /*if wider than 25 bytes, tell it*/
  say 'Fibonacci' k"="q
  if w > 25 then say 'Fibonacci' k "has a length of" w
  end k
exit

/*-------------------------------------FIB subroutine (non-recursive)---*/
method fib(arg) private static
  parse arg n
  na = n.abs

  if na < 2 then return na             /*handle special cases.          */
  a = 0
  b = 1

  loop j = 2 to na
    s = a + b
    a = b
    b = s
    end j

  if n > 0 | na // 2 == 1 then return  s /*if positive or odd negative... */
                          else return -s /*return a negative Fib number.  */
```


## NewLISP

### Iterative

```mw
(define (fibonacci n)
    (let (L '(0 1))
        (dotimes (i n)
            (setq L (list (L 1) (apply + L))))
        (L 1)) )
```

### Recursive

```mw
(define (fibonacci n)
(if (< n 2) 1
    (+ (fibonacci (- n 1))  
       (fibonacci (- n 2)))))
```

### Matrix multiplication

```mw
(define (fibonacci n)
  (letn (f '((0 1) (1 1)) fib f)
    (dotimes (i n)
        (set 'fib (multiply fib f)))
    (fib 0 1)) )

(print(fibonacci 10)) ;;89
```

### With a stack

```mw
;;;   Global variable (bigints); can be isolated in a namespace if need be
(setq stack '(0L 1L))
;
;;;   If the stack is too short, complete it; then read from it
;;;   Adding at the end of a list is optimized in NewLisp
(define (fib n)
   (while (<= (length stack) n)
      (push (+ (stack -1) (stack -2)) stack -1))
   (stack n))
;
;;; Test (~ 7+ s on my mediocre laptop)
;(println (time (fib 50000)))
;;;   or
(println (length (fib 50000)))
;;;   outputs 10450 (digits)
```


## NGS

### Iterative

Translation of

:

Python

```mw
F fib(n:Int) {
   n < 2 returns n
   local a = 1, b = 1
   # i is automatically local because of for()
   for(i=2; i<n; i=i+1) {
      local next = a + b
      a = b
      b = next
   }
   b
}
```


## Nial

### Iterative

On my machine, about 1.7s for 100,000 iterations, n=92. Maybe a few percent faster than iterative Python. Note that n>92 produces overflow; Python keeps going - single iteration with n=1,000,000 takes it about 15s.

```mw
fibi is op n {
  if n<2 then 
    n
  else 
    x1:=0; x2:=1; 
    for i with tell (n - 1) do 
      x:=x1+x2;
      x1:=x2;
      x2:=x;
    endfor;
    x2
  endif};
```

Iterative using fold. Slightly faster, <1.6s:

```mw
fibf is op n {1 pick ((n- 1) fold [1 pick, +] 0 1)};
```

Tacit verion of above. Slightly faster still, <1.4s:

```mw
fibf2 is 1 pick fold [1 pick, +] reverse (0 1 hitch) (-1+);
```

### Recursive

Really slow (over 8s for single iteration, n=33). (Similar to time for recursive python version with n=37.)

```mw
fibr is op n {fork [2>, +, + [fibr (-1 +), fibr (-2 +)]] n};
```

...or tacit version. More than twice as fast (?) but still slow:

```mw
fibr2 is fork [2>, +, + [fibr2 (-1 +), fibr2 (-2 +)]];
```

### Matrix

Matrix inner product (ip). This appears to be the fastest, about 1.0s for 100,000 iterations, n=92: Note that n>92 produces negative result.

```mw
fibm is op n {floor (0 1 pick (reduce ip (n reshape [2 2 reshape 1 1 1 0])))};
```

Could it look a little more like J? (Maybe 5% slower than above.)

```mw
$ is reshape;
~ is tr f op a b {b f a}; % Goes before verb, rather than after like in J;
_ is floor; % Not really J, but J-ish? (Cannot redefine "<.".);

fibm2 is _(0 1 pick reduce ip([2 2$1 1 1 0](~$)));
```

Alternate, not involving replicating matrix n times, but maybe 50% slower than the fastest matrix version above - similar speed to iterative:

```mw
fibm3 is op n {a:=2 2$1 1 1 0; _(0 1 pick ((n- 1) fold (a ip) a))};
```


## Nim

### Analytic

```mw
proc Fibonacci(n: int): int64 =
  var fn = float64(n)
  var p: float64 = (1.0 + sqrt(5.0)) / 2.0
  var q: float64 = 1.0 / p
  return int64((pow(p, fn) + pow(q, fn)) / sqrt(5.0))
```

### Iterative

```mw
proc Fibonacci(n: int): int =
  var
    first = 0
    second = 1

  for i in 0 .. <n:
    swap first, second
    second += first

  result = first
```

### Recursive

```mw
proc Fibonacci(n: int): int64 =
  if n <= 2:
    result = 1
  else:
    result = Fibonacci(n - 1) + Fibonacci(n - 2)
```

### Tail-recursive

```mw
proc Fibonacci(n: int, current: int64, next: int64): int64 =
  if n == 0:
    result = current
  else:
    result = Fibonacci(n - 1, next, current + next)
proc Fibonacci(n: int): int64 =
  result = Fibonacci(n, 0, 1)
```

### Continuations

```mw
iterator fib: int {.closure.} =
  var a = 0
  var b = 1
  while true:
    yield a
    swap a, b
    b = a + b

var f = fib
for i in 0.. <10:
  echo f()
```


## Nix

```mw
fibonacci = n:
    if n <= 1 then n else (fibonacci (n - 1) + fibonacci (n - 2));
```


## Nu

Works with

:

Nushell

version 0.97.1

```mw
def 'seq fibonacci' [] {
  generate { {out: $in.0, next: [$in.1 ($in | math sum)]} } [0 1]
}

seq fibonacci | get 7
```

**Output:**

```
13
```


## Oberon-2

Works with

:

oo2c

version 2

```mw
MODULE Fibonacci;
IMPORT
  Out := NPCT:Console;

PROCEDURE Fibs(VAR r: ARRAY OF LONGREAL);
VAR
  i: LONGINT;
BEGIN
  r[0] := 1.0; r[1] := 1.0;
  FOR i := 2 TO LEN(r) - 1 DO
    r[i] := r[i - 2] + r[i - 1];
  END
END Fibs;

PROCEDURE FibsR(n: LONGREAL): LONGREAL;
BEGIN
  IF n < 2. THEN
    RETURN n
  ELSE
    RETURN FibsR(n - 1) + FibsR(n - 2)
  END
END FibsR;

PROCEDURE Show(r: ARRAY OF LONGREAL);
VAR
  i: LONGINT;
BEGIN
  Out.String("First ");Out.Int(LEN(r),0);Out.String(" Fibonacci numbers");Out.Ln;
  FOR i := 0 TO LEN(r) - 1 DO
    Out.LongRealFix(r[i],8,0)
  END;
  Out.Ln
END Show;

PROCEDURE Gen(s: LONGINT);
VAR
  x: POINTER TO ARRAY OF LONGREAL;
BEGIN
  NEW(x,s);
  Fibs(x^);
  Show(x^)  
END Gen;

PROCEDURE GenR(s: LONGINT);
VAR
  i: LONGINT;
BEGIN
  Out.String("First ");Out.Int(s,0);Out.String(" Fibonacci numbers (Recursive)");Out.Ln;
  FOR i := 1 TO s DO  
    Out.LongRealFix(FibsR(i),8,0)
  END;
  Out.Ln  
END GenR;

BEGIN 
  Gen(10);
  Gen(20);
  GenR(10);
  GenR(20);
END Fibonacci.
```

**Output:**

```
First 10 Fibonacci numbers
      1.      1.      2.      3.      5.      8.     13.     21.     34.     55.
First 20 Fibonacci numbers
      1.      1.      2.      3.      5.      8.     13.     21.     34.     55.     89.    144.    233.    377.    610.    987.   1597.   2584.   4181.   6765.
First 10 Fibonacci numbers (Recursive)
      1.      1.      2.      3.      5.      8.     13.     21.     34.     55.
First 20 Fibonacci numbers (Recursive)
      1.      1.      2.      3.      5.      8.     13.     21.     34.     55.     89.    144.    233.    377.    610.    987.   1597.   2584.   4181.   6765.
```


## Objeck

### Recursive

```mw
bundle Default {
  class Fib {
    function : Main(args : String[]), Nil {
      for(i := 0; i <= 10; i += 1;) {
        Fib(i)->PrintLine();
      };
    }
    
    function : native : Fib(n : Int), Int {
      if(n < 2) {
        return n;
      };
      
      return Fib(n-1) + Fib(n-2);
    }
  }
}
```


## Objective-C

### Recursive

```mw
-(long)fibonacci:(int)position
{
    long result = 0;
    if (position < 2) {
        result = position;
    } else {
        result = [self fibonacci:(position -1)] + [self fibonacci:(position -2)];
    }
    return result;    
}
```

### Iterative

```mw
+(long)fibonacci:(int)index {
    long beforeLast = 0, last = 1;
    while (index > 0) {
        last += beforeLast;
        beforeLast = last - beforeLast;
        --index;
    }
    return last;
}
```


## OCaml

### Tail-Recursive (fast)

```mw
let fib n =
  let rec aux i a b =
    if i = 0 then a else aux (pred i) b (a + b)
  in
  aux n 0 1
```

### Iterative

```mw
let fib_iter n =
  if n < 2 then
    n
  else let fib_prev = ref 1
  and fib = ref 1 in
    for num = 2 to n - 1 do
      let temp = !fib in
        fib := !fib + !fib_prev;
        fib_prev := temp
    done;
    !fib
```

### Recursive

```mw
let rec fib_rec n =
  if n < 2 then
    n
  else
    fib_rec (n - 1) + fib_rec (n - 2)

let rec fib = function 
    0 -> 0
  | 1 -> 1
  | n -> if n > 0 then fib (n-1) + fib (n-2)
         else fib (n+2) - fib (n+1)
```

### Arbitrary Precision

Using OCaml's Num module.

```mw
open Num

let fib =
  let rec fib_aux f0 f1 = function
    | 0 -> f0
    | 1 -> f1
    | n -> fib_aux f1 (f1 +/ f0) (n - 1)
  in
  fib_aux (num_of_int 0) (num_of_int 1)

(* support for negatives *)
let fib n = 
      if n < 0 && n mod 2 = 0 then minus_num (fib (abs n))  
      else fib (abs n)
;;
(* It can be called from the command line with an argument *)
(* Result is send to standart output *)
let n = int_of_string Sys.argv.(1) in 
print_endline (string_of_num (fib n))
```

compile with:

```
ocamlopt nums.cmxa -o fib fib.ml
```

Output:

```
$ ./fib 0
0
$ ./fib 10
55
$ ./fib 399
108788617463475645289761992289049744844995705477812699099751202749393926359816304226
$ ./fib -6
-8
```

### O(log(n)) with arbitrary precision

This performs log2(N) matrix multiplies. Each multiplication is not constant-time but increases sub-linearly, about O(log(N)).

```mw
open Num

let mul (a,b,c) (d,e,f) = let bxe = b*/e in
  (a*/d +/ bxe, a*/e +/ b*/f, bxe +/ c*/f)

let id = (Int 1, Int 0, Int 1)
let rec pow a n =
  if n=0 then id else
    let b = pow a (n/2) in
    if (n mod 2) = 0 then mul b b else mul a (mul b b)

let fib n =
  let (_,y,_) = (pow (Int 1, Int 1, Int 0) n) in
  string_of_num y
;;
Printf.printf "fib %d = %s\n" 300 (fib 300)
```

Output:

```
fib 300 = 222232244629420445529739893461909967206666939096499764990979600
```

### Matrix Exponentiation

```mw
open List
;;
let rec bin n =
  if n < 2 then [n mod 2 = 1]
  else bin (n/2) @ [n mod 2 = 1]
;;
let cut = function
  | [] -> [] 
  | _ :: x -> x
;;
let multiply a b =
  let ((p, q), (r, s)) = a in
  let ((t, u), (v, w)) = b in
  ((p*t+q*v, p*u+q*w), (r*t+s*v, r*u+s*w))
;;
let fib n =
  let rec f p q r =
    if length r = 1 then
      if nth r 0 then (multiply p q, q)
      else (p, q)
    else
      let (pp, qq) = f p q (cut r) in
      let qqq = multiply qq qq in
      if nth r 0 then (multiply pp qqq, qqq)
      else (pp, qqq) in
  f ((1L, 0L), (0L, 1L)) ((1L, 1L), (1L, 0L)) (bin n) |> fst |> fst |> snd
;;
```


## Octave

### Recursive

```mw
% recursive
function fibo = recfibo(n)
  if ( n < 2 )
    fibo = n;
  else
    fibo = recfibo(n-1) + recfibo(n-2);
  endif
endfunction
```

**Testing**

```mw
% testing
for i = 0 : 20
  printf("%d %d\n", i, recfibo(i));
endfor
```

### Iterative

```mw
% iterative
function fibo = iterfibo(n)
  if ( n < 2 )
    fibo = n;
  else
    f = zeros(2,1);
    f(1) = 0; 
    f(2) = 1;
    for i = 2 : n
      t = f(2);
      f(2) = f(1) + f(2);
      f(1) = t;
    endfor
    fibo = f(2);
  endif
endfunction
```

**Testing**

```mw
% testing
for i = 0 : 20
  printf("%d %d\n", i, iterfibo(i));
endfor
```

### Analytic

```mw
function retval = fibanalytic(n)
  retval = round(((5 .^ 0.5 + 1) / 2) .^ n / 5 .^ 0.5);
endfunction
```

### Tail Recursive

```mw
function retval = fibtailrecursive(n, prevfib = 0, fib = 1)
  if (n == 0)
    retval = prevfib;
  else
    retval = fibtailrecursive(n - 1, fib, prevfib + fib);
  endif
endfunction
```


## Odin

Fibinacci Sequence - Iterative Solution Odin Build: dev-2023-07-nightly:3072479c

```mw
package fib
import "core:fmt"

main :: proc() {
   fmt.println("\nFibonacci Seq - starting n and n+1 from 0 and 1:")
   fmt.println("------------------------------------------------")
   for j: u128 = 0; j <= 20; j += 1 {
      fmt.println("n:", j, "\tFib:", fibi(j))
   }
}

fibi :: proc(n: u128) -> u128 {
    if n < 2 {
        return n
    }
    a, b: u128 = 0, 1
    for _ in 2..=n {
        a += b
        a, b = b, a
    }
    return b
}
```

**Output:**

```
First 20 Fibonacci Numbers
Starting n and n+1 from 0 and 1
-------------------------------
n: 0    Fib: 0
n: 1    Fib: 1
n: 2    Fib: 1
n: 3    Fib: 2
n: 4    Fib: 3
n: 5    Fib: 5
n: 6    Fib: 8
n: 7    Fib: 13
n: 8    Fib: 21
n: 9    Fib: 34
n: 10   Fib: 55
n: 11   Fib: 89
n: 12   Fib: 144
n: 13   Fib: 233
n: 14   Fib: 377
n: 15   Fib: 610
n: 16   Fib: 987
n: 17   Fib: 1597
n: 18   Fib: 2584
n: 19   Fib: 4181
n: 20   Fib: 6765
-------------------------------
```


## Oforth

```mw
: fib   0 1 rot #[ tuck + ] times drop ;
```


## Ol

Same as Scheme example(s).


## Onyx (wasm)

```mw
use core.iter
use core { printf }

// Procedural Simple For-Loop Style
fib_for_loop :: (n: i32) -> i32 {
    a: i32 = 0;
    b: i32 = 1;
    for 0 .. n {
        tmp := a;
        a = b;
        b = tmp + b;
    }
    return a;
}

FibState :: struct { a, b: u64 }

// Functional Folding Style
fib_by_fold :: (n: i32) => {
    end_state := 
        iter.counter()
        |> iter.take(n)
        |> iter.fold(
            FibState.{ a = 0, b = 1 },
            (_, state) => FibState.{
                a = state.b,
                b = state.a + state.b
            }
        );
    return end_state.a;
}

// Custom Iterator Style
fib_iterator :: (n: i32) => 
    iter.generator(
        &.{ a = cast(u64) 0, b = cast(u64) 1, counter = n },
        (state: & $Ctx) -> (u64, bool) {
            if state.counter <= 0 {
                return 0, false;
            }
            tmp := state.a;
            state.a = state.b;
            state.b = state.b + tmp;
            state.counter -= 1;
            return tmp, true;
        }
    );

main :: () {
    printf("\nBy For Loop:\n");
    for i in 0 .. 21 {
        printf("{} ", fib_for_loop(i));
    }

    printf("\n\nBy Iterator:\n");
    for i in 0 .. 21 {
        printf("{} ", fib_by_fold(i));
    }

    printf("\n\nBy Fold:\n");
    for value, index in fib_iterator(21) {
        printf("{} ", value);
    }
}
```

**Output:**

```
For-Loop:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

Functional Fold:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

Custom Iterator:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```


## OPL

```mw
FIBON:
REM Fibonacci sequence is generated to the Organiser II floating point variable limit.
REM CLEAR/ON key quits.
REM Mikesan - http://forum.psion2.org/
LOCAL A,B,C
A=1 :B=1 :C=1
PRINT A,
DO
  C=A+B
  A=B
  B=C
  PRINT A,
UNTIL GET=1
```


## Order

### Recursive

```mw
#include <order/interpreter.h>

#define ORDER_PP_DEF_8fib_rec                     \
ORDER_PP_FN(8fn(8N,                               \
                8if(8less(8N, 2),                 \
                    8N,                           \
                    8add(8fib_rec(8sub(8N, 1)),   \
                         8fib_rec(8sub(8N, 2))))))

ORDER_PP(8fib_rec(10))
```

Tail recursive version (example supplied with language):

```mw
#include <order/interpreter.h>
 
#define ORDER_PP_DEF_8fib                                         \
ORDER_PP_FN(8fn(8N,                                               \
                8fib_iter(8N, 0, 1)))
 
#define ORDER_PP_DEF_8fib_iter                                    \
ORDER_PP_FN(8fn(8N, 8I, 8J,                                       \
                8if(8is_0(8N),                                    \
                    8I,                                           \
                    8fib_iter(8dec(8N), 8J, 8add(8I, 8J)))))
 
ORDER_PP(8to_lit(8fib(8nat(5,0,0))))
```

### Memoization

```mw
#include <order/interpreter.h>

#define ORDER_PP_DEF_8fib_memo                                    \
ORDER_PP_FN(8fn(8N,                                               \
                8tuple_at(0, 8fib_memo_inner(8N, 8seq))))
                

#define ORDER_PP_DEF_8fib_memo_inner                                            \
ORDER_PP_FN(8fn(8N, 8M,                                                         \
                8cond((8less(8N, 8seq_size(8M)), 8pair(8seq_at(8N, 8M), 8M))    \
                      (8equal(8N, 0), 8pair(0, 8seq(0)))                        \
                      (8equal(8N, 1), 8pair(1, 8seq(0, 1)))                     \
                      (8else,                                                   \
                        8lets((8S, 8fib_memo_inner(8sub(8N, 2), 8M))            \
                              (8T, 8fib_memo_inner(8dec(8N), 8tuple_at(1, 8S))) \
                              (8U, 8add(8tuple_at(0, 8S), 8tuple_at(0, 8T))),   \
                              8pair(8U,                                         \
                                    8seq_append(8tuple_at(1, 8T), 8seq(8U))))))))
                    

ORDER_PP(
8for_each_in_range(8fn(8N,
                       8print(8to_lit(8fib_memo(8N)) (,) 8space)),
                   1, 21)
)
```


## Oz

### Iterative

Using mutable references (cells).

```mw
fun{FibI N}
  Temp = {NewCell 0}
  A = {NewCell 0}
  B = {NewCell 1}
in    
  for I in 1..N do
    Temp := @A + @B
    A := @B
    B := @Temp
  end
  @A
end
```

### Recursive

Inefficient (blows up the stack).

```mw
fun{FibR N}
  if N < 2 then N
  else {FibR N-1} + {FibR N-2}
  end
end
```

### Tail-recursive

Using accumulators.

```mw
fun{Fib N}
   fun{Loop N A B}
      if N == 0 then
    B
      else
    {Loop N-1 A+B A}
      end
   end
in    
   {Loop N 1 0}
end
```

### Lazy-recursive

```mw
declare
  fun lazy {FiboSeq}
     {LazyMap
      {Iterate fun {$ [A B]} [B A+B] end [0 1]}
      Head}
  end

  fun {Head A|_} A end

  fun lazy {Iterate F I}
     I|{Iterate F {F I}}
  end

  fun lazy {LazyMap Xs F}
     case Xs of X|Xr then {F X}|{LazyMap Xr F}
     [] nil then nil
     end
  end
in
  {Show {List.take {FiboSeq} 8}}
```


## PARI/GP

### Built-in

```mw
fibonacci(n)
```

### Matrix

```mw
fib(n)=([1,1;1,0]^n)[1,2]
```

### Analytic

This uses the Binet form.

```mw
fib(n)=my(phi=(1+sqrt(5))/2);round((phi^n-phi^-n)/sqrt(5))
```

The second term can be dropped since the error is always small enough to be subsumed by the rounding.

```mw
fib(n)=round(((1+sqrt(5))/2)^n/sqrt(5))
```

### Algebraic

This is an exact version of the above formula. `quadgen(5)` represents ${\displaystyle \phi }$ and the number is stored in the form ${\displaystyle a+b\phi }$ . `imag` takes the coefficient of ${\displaystyle \phi }$ . This uses the relation

${\displaystyle \phi ^{n}=F_{n-1}+F_{n}\phi }$

and hence `real(quadgen(5)^n)` would give the (n-1)-th Fibonacci number.

```mw
fib(n)=imag(quadgen(5)^n)
```

A more direct translation (note that ${\displaystyle {\sqrt {5}}=2\phi -1}$ ) would be

```mw
fib(n)=my(phi=quadgen(5));(phi^n-(-1/phi)^n)/(2*phi-1)
```

### Combinatorial

This uses the generating function. It can be trivially adapted to give the first n Fibonacci numbers.

```mw
fib(n)=polcoeff(x/(1-x-x^2)+O(x^(n+1)),n)
```

### Binary powering

This is an efficient method (similar to the one used internally by `fibonacci()`), although running it without compilation won't give competitive speed.

```mw
fib(n)={
  if(n<=0,
    if(n,(-1)^(n+1)*fib(n),0)
  ,
    my(v=lucas(n-1));
    (2*v[1]+v[2])/5
  )
};
lucas(n)={
  if (!n, return([2,1]));
  my(v=lucas(n >> 1), z=v[1], t=v[2], pr=v[1]*v[2]);
  n=n%4;
  if(n%2,
    if(n==3,[v[1]*v[2]+1,v[2]^2-2],[v[1]*v[2]-1,v[2]^2+2])
  ,
    if(n,[v[1]^2+2,v[1]*v[2]+1],[v[1]^2-2,v[1]*v[2]-1])
  )
};
```

### Recursive

```mw
fib(n)={
  if(n<2,
    n
  ,
    fib(n-1)+fib(n)
  )
};
```

### Anonymous recursion

Works with

:

PARI/GP

version 2.8.0+

This uses `self()` which gives a self-reference.

```mw
fib(n)={
  if(n<2,
    n
  ,
    my(s=self());
    s(n-2)+s(n-1)
  )
};
```

It can be used without being named:

```mw
apply(n->if(n<2,n,my(s=self());s(n-2)+s(n-1)), [1..10])
```

gives

**Output:**

```
%1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Memoization

```mw
F=[];
fib(n)={
  if(n>#F,
    F=concat(F, vector(n-#F));
    F[n]=fib(n-1)+fib(n-2)
  ,
    if(n<2,
      n
    ,
      if(F[n],F[n],F[n]=fib(n-1)+fib(n-2))
    )
  );
}
```

### Iterative

```mw
fib(n)={
  if(n<0,return((-1)^(n+1)*fib(n)));
  my(a=0,b=1,t);
  while(n,
    t=a+b;
    a=b;
    b=t;
    n--
  );
  a
};
```

### Trigonometric

This solution uses the complex hyperbolic sine.

```mw
fib(n)=real(2/sqrt(5)/I^n*sinh(n*log(I*(1+sqrt(5))/2)))\/1;
```

### Chebyshev

This solution uses Chebyshev polynomials of the second kind (Chyebyshev U-polynomials).

```mw
fib(n)=n--;polchebyshev(n,2,I/2)*I^n;
```

or

```mw
fib(n)=abs(polchebyshev(n-1,2,I/2));
```

### Anti-Hadamard matrix

All n×n (0,1) lower Hessenberg matrices have determinant at most F(n). The n×n anti-Hadamard matrix matches this upper bound, and hence can be used as an inefficient method for computing Fibonacci numbers of positive index. These matrices are the same as Matlab's type-3 "Dramadah" matrices, following a naming suggestion of C. L. Mallows according to Graham & Sloane.

```mw
matantihadamard(n)={
  matrix(n,n,i,j,
    my(t=j-i+1);
    if(t<1,t%2,t<3)
  );
}
fib(n)=matdet(matantihadamard(n))
```

### Testing adjacent bits

The Fibonacci numbers can be characterized (for n > 0) as the number of n-bit strings starting and ending with 1 without adjacent 0s. This inefficient, exponential-time algorithm demonstrates:

```mw
fib(n)=
{
  my(g=2^(n+1)-1);
  sum(i=2^(n-1),2^n-1,
    bitor(i,i<<1)==g
  );
}
```

### One-by-one

This code is purely for amusement and requires n > 1. It tests numbers in order to see if they are Fibonacci numbers, and waits until it has seen *n* of them.

```mw
fib(n)=my(k=0);while(n--,k++;while(!issquare(5*k^2+4)&&!issquare(5*k^2-4),k++));k
```


## ParaCL

```mw
fibbonachi = func(x) : fibb
{
  res = 1;
  if (x > 1)
    res = fibb(x - 1) + fibb(x - 2);
  res;
}
```
