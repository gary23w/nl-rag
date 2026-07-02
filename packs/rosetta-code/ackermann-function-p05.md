---
title: "Ackermann function (part 5/6)"
source: https://rosettacode.org/wiki/Ackermann_function
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/6
---

## Pure Data

```mw
#N canvas 741 265 450 436 10;
#X obj 83 111 t b l;
#X obj 115 163 route 0;
#X obj 115 185 + 1;
#X obj 83 380 f;
#X obj 161 186 swap;
#X obj 161 228 route 0;
#X obj 161 250 - 1;
#X obj 161 208 pack;
#X obj 115 314 t f f;
#X msg 161 272 \$1 1;
#X obj 115 142 t l;
#X obj 207 250 swap;
#X obj 273 271 - 1;
#X obj 207 272 t f f;
#X obj 207 298 - 1;
#X obj 207 360 pack;
#X obj 239 299 pack;
#X obj 83 77 inlet;
#X obj 83 402 outlet;
#X connect 0 0 3 0;
#X connect 0 1 10 0;
#X connect 1 0 2 0;
#X connect 1 1 4 0;
#X connect 2 0 8 0;
#X connect 3 0 18 0;
#X connect 4 0 7 0;
#X connect 4 1 7 1;
#X connect 5 0 6 0;
#X connect 5 1 11 0;
#X connect 6 0 9 0;
#X connect 7 0 5 0;
#X connect 8 0 3 1;
#X connect 8 1 15 1;
#X connect 9 0 10 0;
#X connect 10 0 1 0;
#X connect 11 0 13 0;
#X connect 11 1 12 0;
#X connect 12 0 16 1;
#X connect 13 0 14 0;
#X connect 13 1 16 0;
#X connect 14 0 15 0;
#X connect 15 0 10 0;
#X connect 16 0 10 0;
#X connect 17 0 0 0;
```


## PureBasic

```mw
Procedure.q Ackermann(m, n)
  If m = 0
    ProcedureReturn n + 1
  ElseIf  n = 0
    ProcedureReturn Ackermann(m - 1, 1)
  Else
    ProcedureReturn Ackermann(m - 1, Ackermann(m, n - 1))
  EndIf
EndProcedure

Debug Ackermann(3,4)
```


## Purity

```mw
data Iter = f => FoldNat <const $f One, $f> 
data Ackermann = FoldNat <const Succ, Iter>
```


## Python

### Python: Explicitly recursive

Works with

:

Python

version 2.5

```mw
def ack1(M, N):
   return (N + 1) if M == 0 else (
      ack1(M-1, 1) if N == 0 else ack1(M-1, ack1(M, N-1)))
```

Another version:

```mw
from functools import cache

@cache
def ack2(M, N):
    if M == 0:
        return N + 1
    elif N == 0:
        return ack2(M - 1, 1)
    else:
        return ack2(M - 1, ack2(M, N - 1))
```

**Example of use:**

```mw
>>> import sys
>>> sys.setrecursionlimit(3000)
>>> ack1(0,0)
1
>>> ack1(3,4)
125
>>> ack2(0,0)
1
>>> ack2(3,4)
125
```

From the Mathematica ack3 example:

```mw
def ack2(M, N):
   return (N + 1)   if M == 0 else (
          (N + 2)   if M == 1 else (
          (2*N + 3) if M == 2 else (
          (8*(2**N - 1) + 5) if M == 3 else (
          ack2(M-1, 1) if N == 0 else ack2(M-1, ack2(M, N-1))))))
```

Results confirm those of Mathematica for ack(4,1) and ack(4,2)

### Python: Without recursive function calls

The heading is more correct than saying the following is iterative as an explicit stack is used to replace explicit recursive function calls. I don't think this is what Comp. Sci. professors mean by iterative.

```mw
from collections import deque

def ack_ix(m, n):
    "Paddy3118's iterative with optimisations on m"

    stack = deque([])
    stack.extend([m, n])

    while  len(stack) > 1:
        n, m = stack.pop(), stack.pop()

        if   m == 0:
            stack.append(n + 1)
        elif m == 1:
            stack.append(n + 2)
        elif m == 2:
            stack.append(2*n + 3)
        elif m == 3:
            stack.append(2**(n + 3) - 3)
        elif n == 0:
            stack.extend([m-1, 1])
        else:
            stack.extend([m-1, m, n-1])

    return stack[0]
```

**Output:**

(From an ipython shell)

```
In [26]: %time a_4_2 = ack_ix(4, 2)
Wall time: 0 ns

In [27]: # How big is the answer?

In [28]: float(a_4_2)
Traceback (most recent call last):

  File "<ipython-input-28-af4ad951eff8>", line 1, in <module>
    float(a_4_2)

OverflowError: int too large to convert to float

In [29]: # How many decimal digits in the answer?

In [30]: len(str(a_4_2))
Out[30]: 19729
```


## Quackery

```mw
                           forward is ackermann ( m n --> r )
  [ over 0 = iff
      [ nip 1 + ] done
    dup 0 = iff
      [ drop 1 - 1
        ackermann ] done
     over 1 - unrot 1 -
     ackermann ackermann ]   resolves ackermann ( m n --> r )

  3 10 ackermann echo
```

**Output:**

```
8189
```


## Quirl

```mw
ackermann( 0  Int):ord(0 $b)           = add($b 1);
ackermann(Int  0 ):ord(1 $a)           = ackermann(add($a -1) 1);
ackermann(Int Int):ord(1 $a):ord(1 $b) = ackermann(add($a -1) ackermann($a add($b -1)))
```


## R

```mw
ackermann <- function(m, n) {
  if ( m == 0 ) {
    n+1
  } else if ( n == 0 ) {
    ackermann(m-1, 1)
  } else {
    ackermann(m-1, ackermann(m, n-1))
  }
}
```

```mw
for ( i in 0:3 ) {
  print(ackermann(i, 4))
}
```


## Racket

```mw
#lang racket
(define (ackermann m n)
  (cond [(zero? m) (add1 n)]
        [(zero? n) (ackermann (sub1 m) 1)]
        [else (ackermann (sub1 m) (ackermann m (sub1 n)))]))
```


## Raku

(formerly Perl 6)

Works with

:

Rakudo

version 2018.03

```mw
sub A(Int $m, Int $n) {
    if    $m == 0 { $n + 1 } 
    elsif $n == 0 { A($m - 1, 1) }
    else          { A($m - 1, A($m, $n - 1)) }
}
```

An implementation using multiple dispatch:

```mw
multi sub A(0,      Int $n) { $n + 1                   }
multi sub A(Int $m, 0     ) { A($m - 1, 1)             }
multi sub A(Int $m, Int $n) { A($m - 1, A($m, $n - 1)) }
```

Note that in either case, Int is defined to be arbitrary precision in Raku.

Here's a caching version of that, written in the sigilless style, with liberal use of Unicode, and the extra optimizing terms to make A(4,2) possible:

```mw
proto A(Int \𝑚, Int \𝑛) { (state @)[𝑚][𝑛] //= {*} }

multi A(0,      Int \𝑛) { 𝑛 + 1 }
multi A(1,      Int \𝑛) { 𝑛 + 2 }
multi A(2,      Int \𝑛) { 3 + 2 * 𝑛 }
multi A(3,      Int \𝑛) { 5 + 8 * (2 ** 𝑛 - 1) }

multi A(Int \𝑚, 0     ) { A(𝑚 - 1, 1) }
multi A(Int \𝑚, Int \𝑛) { A(𝑚 - 1, A(𝑚, 𝑛 - 1)) }

# Testing:
say A(4,1);
say .chars, " digits starting with ", .substr(0,50), "..." given A(4,2);
```

**Output:**

```
65533
19729 digits starting with 20035299304068464649790723515602557504478254755697...
```


## Rebol

```mw
ackermann: func [m n] [
    case [
        m = 0 [n + 1]
        n = 0 [ackermann m - 1 1]
        true [ackermann m - 1 ackermann m n - 1]
    ]
]
```

Optimized Ackermann with small-m shortcuts

```mw
ackermann: func [
    m [integer!]
    n [integer!]
] [
    ;; Small-m closed forms
    case [
        m = 0 [n + 1]
        m = 1 [n + 2]
        m = 2 [(2 * n) + 3]
        m = 3 [
            ;; 2^(n+3) - 3
            (to integer! power 2 (n + 3)) - 3
        ]
        ;; m >= 4 causes stack overflow
    ]
]
```

**Output:**

```
ackermann 0 0
;== 1
ackermann 3 4
;== 125
```


## Refal

```mw
$ENTRY Go {
    = <Prout 'A(3,9) = ' <A 3 9>>;
};

A {
    0   s.N   = <+ s.N 1>;
    s.M 0     = <A <- s.M 1> 1>;
    s.M s.N   = <A <- s.M 1> <A s.M <- s.N 1>>>;
};
```

**Output:**

```
A(3,9) = 4093
```


## ReScript

```mw
let _m = Sys.argv[2]
let _n = Sys.argv[3]

let m = int_of_string(_m)
let n = int_of_string(_n)

let rec a = (m, n) =>
  switch (m, n) {
  | (0, n) => (n+1)
  | (m, 0) => a(m-1, 1)
  | (m, n) => a(m-1, a(m, n-1))
  }

Js.log("ackermann(" ++ _m ++ ", " ++ _n ++ ") = "
    ++ string_of_int(a(m, n)))
```

**Output:**

```
$ bsc acker.res > acker.bs.js
$ node acker.bs.js 2 3
ackermann(2, 3) = 9
$ node acker.bs.js 3 4
ackermann(3, 4) = 125
```


## REXX

**Include** How to use **Include** Source code Procedures Ackermann1/Acker1 are true to the spirit of the task: pure recursion, no optimizations. Worked up to Ackermann(3,10) in a reasonable time. Ackermann(4,1) and higher were out of reach. Procedures Ackermann2/Acker2 apply the formulas given in the WP article, up to Ackermann(4,2), calculating in full precision. No recursion! The maximum number of digits and also the value of an exponent in Rexx is 1 billion. Ackermann(4,3) by far exceeds this and cannot be expressed, not even as floating point value with less precision.

```mw
-- 27 Oct 2025
include Setting
numeric digits 310000

say 'ACKERMANN FUNCTION'
say version
say
call Ackermann1
call Ackermann2
exit

Ackermann1:
procedure expose glob.
say 'Using recursion...'
do i=0 to 3
   do j=0 to 10
      say 'Ackermann('i','j')' '=' Acker1(i,j) Elaps('r')'s'
   end
end
say
return

Acker1:
procedure
arg xx,yy
select
   when xx = 0 then
      return yy+1
   when yy = 0 then
      return Acker1(xx-1,1)
   otherwise
      return Acker1(xx-1,Acker1(xx,yy-1))
end

Ackermann2:
procedure expose glob.
say 'Using closed formulas...'
do i=0 to 3
   do j=0 to 10
      say 'Ackermann('i','j')' '=' Acker2(i,j) Elaps('r')'s'
   end
end
say 'Ackermann(3,100) =' Acker2(3,100) Elaps('r')'s'
say 'Ackermann(3,1000) has' Length(Acker2(3,1000)) 'digits' Elaps('r')'s'
say 'Ackermann(3,10000) has' Length(Acker2(3,10000)) 'digits' Elaps('r')'s'
say 'Ackermann(3,100000) has' Length(Acker2(3,100000)) 'digits' Elaps('r')'s'
say 'Ackermann(3,1000000) has' Length(Acker2(3,1000000)) 'digits' Elaps('r')'s'
say 'Ackermann(4,0) =' Acker2(4,0) Elaps('r')'s'
say 'Ackermann(4,1) =' Acker2(4,1) Elaps('r')'s'
say 'Ackermann(4,2) has' Length(Acker2(4,2)) 'digits' Elaps('r')'s'
return

Acker2:
procedure
arg xx,yy
select
   when xx=0 then
      rr=yy+1
   when xx=1 then
      rr=yy+2
   when xx=2 then
      rr=yy+yy+3
   when xx=3 then
      rr=2**(yy+3)-3
   when xx=4 then
      select
         when yy=0 then
            rr=2**(2**2)-3
         when yy=1 then
            rr=2**(2**(2**2))-3
         when yy=2 then
            rr=2**(2**(2**(2**2)))-3
         otherwise
            rr=0
      end
   otherwise
      rr=0
end
return rr

include Abend
-- Elaps
include Timer
```

**Output:**

```
ACKERMANN FUNCTION
REXX-Regina_3.9.7(MT) 5.00 18 Mar 2025

Using recursion...
Ackermann(0,0) = 1 0.001s
Ackermann(0,1) = 2 0s
Ackermann(0,2) = 3 0s
Ackermann(0,3) = 4 0s
Ackermann(0,4) = 5 0s
Ackermann(0,5) = 6 0s
Ackermann(0,6) = 7 0s
Ackermann(0,7) = 8 0s
Ackermann(0,8) = 9 0s
Ackermann(0,9) = 10 0s
Ackermann(0,10) = 11 0s
Ackermann(1,0) = 2 0s
Ackermann(1,1) = 3 0s
Ackermann(1,2) = 4 0s
Ackermann(1,3) = 5 0s
Ackermann(1,4) = 6 0s
Ackermann(1,5) = 7 0s
Ackermann(1,6) = 8 0s
Ackermann(1,7) = 9 0s
Ackermann(1,8) = 10 0s
Ackermann(1,9) = 11 0s
Ackermann(1,10) = 12 0s
Ackermann(2,0) = 3 0s
Ackermann(2,1) = 5 0s
Ackermann(2,2) = 7 0s
Ackermann(2,3) = 9 0s
Ackermann(2,4) = 11 0s
Ackermann(2,5) = 13 0s
Ackermann(2,6) = 15 0s
Ackermann(2,7) = 17 0s
Ackermann(2,8) = 19 0.001s
Ackermann(2,9) = 21 0s
Ackermann(2,10) = 23 0s
Ackermann(3,0) = 5 0s
Ackermann(3,1) = 13 0s
Ackermann(3,2) = 29 0s
Ackermann(3,3) = 61 0.002s
Ackermann(3,4) = 125 0.008s
Ackermann(3,5) = 253 0.031s
Ackermann(3,6) = 509 0.135s
Ackermann(3,7) = 1021 0.523s
Ackermann(3,8) = 2045 2.132s
Ackermann(3,9) = 4093 9.203s
Ackermann(3,10) = 8189 42.991s

Using closed formulas...
Ackermann(0,0) = 1 0s
Ackermann(0,1) = 2 0s
Ackermann(0,2) = 3 0s
Ackermann(0,3) = 4 0s
Ackermann(0,4) = 5 0.001s
Ackermann(0,5) = 6 0s
Ackermann(0,6) = 7 0s
Ackermann(0,7) = 8 0s
Ackermann(0,8) = 9 0s
Ackermann(0,9) = 10 0s
Ackermann(0,10) = 11 0s
Ackermann(1,0) = 2 0s
Ackermann(1,1) = 3 0s
Ackermann(1,2) = 4 0s
Ackermann(1,3) = 5 0s
Ackermann(1,4) = 6 0s
Ackermann(1,5) = 7 0s
Ackermann(1,6) = 8 0s
Ackermann(1,7) = 9 0s
Ackermann(1,8) = 10 0s
Ackermann(1,9) = 11 0s
Ackermann(1,10) = 12 0s
Ackermann(2,0) = 3 0s
Ackermann(2,1) = 5 0s
Ackermann(2,2) = 7 0s
Ackermann(2,3) = 9 0s
Ackermann(2,4) = 11 0s
Ackermann(2,5) = 13 0s
Ackermann(2,6) = 15 0s
Ackermann(2,7) = 17 0s
Ackermann(2,8) = 19 0s
Ackermann(2,9) = 21 0s
Ackermann(2,10) = 23 0s
Ackermann(3,0) = 5 0s
Ackermann(3,1) = 13 0s
Ackermann(3,2) = 29 0s
Ackermann(3,3) = 61 0s
Ackermann(3,4) = 125 0s
Ackermann(3,5) = 253 0s
Ackermann(3,6) = 509 0.001s
Ackermann(3,7) = 1021 0s
Ackermann(3,8) = 2045 0s
Ackermann(3,9) = 4093 0s
Ackermann(3,10) = 8189 0s
Ackermann(3,100) = 10141204801825835211973625643005 0s
Ackermann(3,1000) has 302 digits 0.001s
Ackermann(3,10000) has 3012 digits 0.019s
Ackermann(3,100000) has 30104 digits 1.786s
Ackermann(3,1000000) has 301031 digits 165.731s
Ackermann(4,0) = 13 0s
Ackermann(4,1) = 65533 0s
Ackermann(4,2) has 19729 digits 0.718s
```


## Ring

Translation of

:

C#

```mw
for m = 0 to 3
        for n = 0 to 4
                see "Ackermann(" + m + ", " + n + ") = " + Ackermann(m, n) + nl
         next
next

func Ackermann m, n
        if m > 0
           if n > 0
                return Ackermann(m - 1, Ackermann(m, n - 1))
            but n = 0
                return Ackermann(m - 1, 1)
            ok 
        but m = 0
            if n >= 0 
                return n + 1
            ok
        ok
Raise("Incorrect Numerical input !!!")
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


## RISC-V Assembly

the basic recursive function, because memorization and other improvements would blow the clarity.

```mw
ackermann: 	#x: a1, y: a2, return: a0
beqz a1, npe #case m = 0
beqz a2, mme #case m > 0 & n = 0
addi sp, sp, -8 #case m > 0 & n > 0
sw ra, 4(sp)
sw a1, 0(sp)
addi a2, a2, -1
jal ackermann
lw a1, 0(sp)
addi a1, a1, -1
mv a2, a0
jal ackermann
lw t0, 4(sp)
addi sp, sp, 8
jr t0, 0
npe:
addi a0, a2, 1
jr ra, 0
mme:
addi sp, sp, -4
sw ra, 0(sp)
addi a1, a1, -1
li a2, 1
jal ackermann
lw t0, 0(sp)
addi sp, sp, 4
jr t0, 0
```


## Rocq

### Standard

```mw
Fixpoint ack (m : nat) : nat -> nat :=
  fix ack_m (n : nat) : nat :=
    match m with
      | 0 => S n
      | S pm =>
        match n with
          | 0 => ack pm 1
          | S pn => ack pm (ack_m pn)
        end
    end.

(*
  Example:
    A(3, 2) = 29
*)

Eval compute in ack 3 2.
```

**Output:**

```
     = 29
     : nat
```

### Using fold

```mw
Require Import Utf8.

Section FOLD.
  Context {A : Type} (f : A → A) (a : A).
  Fixpoint fold (n : nat) : A :=
    match n with
      | O => a
      | S k => f (fold k)
    end.
End FOLD.

Definition ackermann : nat → nat → nat :=
  fold (λ g, fold g (g (S O))) S.
```


## RPL

Works with

:

RPL

version HP49-C

```
« CASE 
     OVER NOT THEN NIP 1 + END 
     DUP NOT  THEN DROP 1 - 1 ACKER END 
     OVER 1 - ROT ROT 1 - ACKER ACKER
  END
» 'ACKER' STO
```

```
3 4 ACKER
```

**Output:**

```
1: 125
```

Runs in 7 min 13 secs on a HP-50g. Speed could be increased by replacing every `1` by `1.`, which would force calculations to be made with floating-point numbers, but we would then lose the arbitrary precision.


## Ruby

Translation of

:

Ada

```mw
def ack(m, n)
  if m == 0
    n + 1
  elsif n == 0
    ack(m-1, 1)
  else
    ack(m-1, ack(m, n-1))
  end
end
```

Example:

```mw
(0..3).each do |m|
  puts (0..6).map { |n| ack(m, n) }.join(' ')
end
```

**Output:**

```
 1 2 3 4 5 6 7 
 2 3 4 5 6 7 8 
 3 5 7 9 11 13 15 
 5 13 29 61 125 253 509
```


## Run BASIC

```mw
print ackermann(1, 2)
 
function ackermann(m, n)
   if (m = 0)             then ackermann = (n + 1)
   if (m > 0) and (n = 0) then ackermann = ackermann((m - 1), 1)
   if (m > 0) and (n > 0) then ackermann = ackermann((m - 1), ackermann(m, (n - 1)))
end function
```


## Rust

```mw
fn ack(m: isize, n: isize) -> isize {
    if m == 0 {
        n + 1
    } else if n == 0 {
        ack(m - 1, 1)
    } else {
        ack(m - 1, ack(m, n - 1))
    }
}

fn main() {
    let a = ack(3, 4);
    println!("{}", a); // 125
}
```

Or:

```mw
fn ack(m: u64, n: u64) -> u64 {
	match (m, n) {
		(0, n) => n + 1,
		(m, 0) => ack(m - 1, 1),
		(m, n) => ack(m - 1, ack(m, n - 1)),
	}
}
```


## Sather

```mw
class MAIN is

  ackermann(m, n:INT):INT
    pre m >= 0 and n >= 0
  is
    if m = 0 then return n + 1; end;
    if n = 0 then return ackermann(m-1, 1); end;
    return ackermann(m-1, ackermann(m, n-1));
  end;

  main is
    n, m :INT;
    loop n := 0.upto!(6);
      loop m := 0.upto!(3);
        #OUT + "A(" + m + ", " + n + ") = " + ackermann(m, n) + "\n";
      end;
    end; 
  end;
end;
```

Instead of `INT`, the class `INTI` could be used, even though we need to use a workaround since in the GNU Sather v1.2.3 compiler the INTI literals are not implemented yet.

```mw
class MAIN is

  ackermann(m, n:INTI):INTI is
    zero ::= 0.inti; -- to avoid type conversion each time
    one  ::= 1.inti;
    if m = zero then return n + one; end;
    if n = zero then return ackermann(m-one, one); end;
    return ackermann(m-one, ackermann(m, n-one));
  end;

  main is
    n, m :INT;
    loop n := 0.upto!(6);
      loop m := 0.upto!(3);
        #OUT + "A(" + m + ", " + n + ") = " + ackermann(m.inti, n.inti) + "\n";
      end;
    end; 
  end;
end;
```


## Scala

```mw
def ack(m: BigInt, n: BigInt): BigInt = {
  if (m==0) n+1
  else if (n==0) ack(m-1, 1)
  else ack(m-1, ack(m, n-1))
}
```

**Example:**

```
scala> for ( m <- 0 to 3; n <- 0 to 6 ) yield ack(m,n)
res0: Seq.Projection[BigInt] = RangeG(1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 8, 3, 5, 7, 9, 11, 13, 15, 5, 13, 29, 61, 125, 253, 509)
```

Memoized version using a mutable hash map:

```mw
val ackMap = new mutable.HashMap[(BigInt,BigInt),BigInt]
def ackMemo(m: BigInt, n: BigInt): BigInt = {
  ackMap.getOrElseUpdate((m,n), ack(m,n))
}
```


## Scheme

```mw
(define (A m n)
    (cond
        ((= m 0) (+ n 1))
        ((= n 0) (A (- m 1) 1))
        (else (A (- m 1) (A m (- n 1))))))
```

An improved solution that uses a lazy data structure, streams, and defines Knuth up-arrows to calculate iterative exponentiation:

```mw
(define (A m n)
  (letrec ((A-stream
    (cons-stream
      (ints-from 1) ;; m = 0
      (cons-stream
        (ints-from 2) ;; m = 1
        (cons-stream
          ;; m = 2
          (stream-map (lambda (n)
                        (1+ (* 2 (1+ n))))
                      (ints-from 0))
          (cons-stream
            ;; m = 3
            (stream-map (lambda (n)
                          (- (knuth-up-arrow 2 (- m 2) (+ n 3)) 3))
                        (ints-from 0))
             ;; m = 4...
            (stream-tail A-stream 3)))))))
    (stream-ref (stream-ref A-stream m) n)))

(define (ints-from n)
  (letrec ((ints-rec (cons-stream n (stream-map 1+ ints-rec))))
    ints-rec))

(define (knuth-up-arrow a n b)
  (let loop ((n n) (b b))
    (cond ((= b 0) 1)
          ((= n 1) (expt a b))
          (else    (loop (-1+ n) (loop n (-1+ b)))))))
```


## Scilab

```mw
clear
function acker=ackermann(m,n)
    global calls
    calls=calls+1
    if m==0 then     acker=n+1
    else
        if n==0 then acker=ackermann(m-1,1)
                else acker=ackermann(m-1,ackermann(m,n-1))
        end
    end
endfunction
function printacker(m,n)
    global calls
    calls=0
    printf('ackermann(%d,%d)=',m,n)
    printf('%d  calls=%d\n',ackermann(m,n),calls)
endfunction
maxi=3; maxj=6
for i=0:maxi
   for j=0:maxj
       printacker(i,j)
   end
end
```

**Output:**

```
ackermann(0,0)=1  calls=1
ackermann(0,1)=2  calls=1
ackermann(0,2)=3  calls=1
ackermann(0,3)=4  calls=1
ackermann(0,4)=5  calls=1
ackermann(0,5)=6  calls=1
ackermann(0,6)=7  calls=1
ackermann(1,0)=2  calls=2
ackermann(1,1)=3  calls=4
ackermann(1,2)=4  calls=6
ackermann(1,3)=5  calls=8
ackermann(1,4)=6  calls=10
ackermann(1,5)=7  calls=12
ackermann(1,6)=8  calls=14
ackermann(2,0)=3  calls=5
ackermann(2,1)=5  calls=14
ackermann(2,2)=7  calls=27
ackermann(2,3)=9  calls=44
ackermann(2,4)=11  calls=65
ackermann(2,5)=13  calls=90
ackermann(2,6)=15  calls=119
ackermann(3,0)=5  calls=15
ackermann(3,1)=13  calls=106
ackermann(3,2)=29  calls=541
ackermann(3,3)=61  calls=2432
ackermann(3,4)=125  calls=10307
ackermann(3,5)=253  calls=42438
ackermann(3,6)=509  calls=172233
```


## Seed7

### Basic version

```mw
const func integer: ackermann (in integer: m, in integer: n) is func
  result
    var integer: result is 0;
  begin
    if m = 0 then
      result := succ(n);
    elsif n = 0 then
      result := ackermann(pred(m), 1);
    else
      result := ackermann(pred(m), ackermann(m, pred(n)));
    end if;
  end func;
```

Original source: [2]

### Improved version

```mw
$ include "seed7_05.s7i";
  include "bigint.s7i";
  
const func bigInteger: ackermann (in bigInteger: m, in bigInteger: n) is func
  result
    var bigInteger: ackermann is 0_;
  begin
    case m of
      when {0_}: ackermann := succ(n);
      when {1_}: ackermann := n + 2_;
      when {2_}: ackermann := 3_ + 2_ * n;
      when {3_}: ackermann := 5_ + 8_ * pred(2_ ** ord(n));
      otherwise:
        if n = 0_ then
          ackermann := ackermann(pred(m), 1_);
        else
          ackermann := ackermann(pred(m), ackermann(m, pred(n)));
        end if;
    end case;
  end func;
    
const proc: main is func
  local
    var bigInteger: m is 0_;
    var bigInteger: n is 0_;
    var string: stri is "";
  begin
    for m range 0_ to 3_ do
      for n range 0_ to 9_ do
        writeln("A(" <& m <& ", " <& n <& ") = " <& ackermann(m, n));
      end for;
    end for;
    writeln("A(4, 0) = " <& ackermann(4_, 0_));
    writeln("A(4, 1) = " <& ackermann(4_, 1_));
    stri := str(ackermann(4_, 2_));
    writeln("A(4, 2) = (" <& length(stri) <& " digits)");
    writeln(stri[1 len 80]);
    writeln("...");
    writeln(stri[length(stri) - 79 ..]);
  end func;
```

Original source: [3]

**Output:**

```
A(0, 0) = 1
A(0, 1) = 2
A(0, 2) = 3
A(0, 3) = 4
A(0, 4) = 5
A(0, 5) = 6
A(0, 6) = 7
A(0, 7) = 8
A(0, 8) = 9
A(0, 9) = 10
A(1, 0) = 2
A(1, 1) = 3
A(1, 2) = 4
A(1, 3) = 5
A(1, 4) = 6
A(1, 5) = 7
A(1, 6) = 8
A(1, 7) = 9
A(1, 8) = 10
A(1, 9) = 11
A(2, 0) = 3
A(2, 1) = 5
A(2, 2) = 7
A(2, 3) = 9
A(2, 4) = 11
A(2, 5) = 13
A(2, 6) = 15
A(2, 7) = 17
A(2, 8) = 19
A(2, 9) = 21
A(3, 0) = 5
A(3, 1) = 13
A(3, 2) = 29
A(3, 3) = 61
A(3, 4) = 125
A(3, 5) = 253
A(3, 6) = 509
A(3, 7) = 1021
A(3, 8) = 2045
A(3, 9) = 4093
A(4, 0) = 13
A(4, 1) = 65533
A(4, 2) = (19729 digits)
20035299304068464649790723515602557504478254755697514192650169737108940595563114
...
84717124577965048175856395072895337539755822087777506072339445587895905719156733
```


## SETL

```mw
program ackermann;

(for m in [0..3])
  print(+/ [rpad('' + ack(m, n), 4): n in [0..6]]);
end;

proc ack(m, n);
  return {[0,n+1]}(m) ? ack(m-1, {[0,1]}(n) ? ack(m, n-1));
end proc;

end program;
```


## Shen

```mw
(define ack
  0 N -> (+ N 1)
  M 0 -> (ack (- M 1) 1)
  M N -> (ack (- M 1)
              (ack M (- N 1))))
```


## Sidef

```mw
func A(m, n) {
    m == 0 ? (n + 1)
           : (n == 0 ? (A(m - 1, 1))
                     : (A(m - 1, A(m, n - 1))));
}
```

Alternatively, using multiple dispatch:

```mw
func A((0), n) { n + 1 }
func A(m, (0)) { A(m - 1, 1) }
func A(m,  n)  { A(m-1, A(m, n-1)) }
```

Calling the function:

```mw
say A(3, 2);     # prints: 29
```


## Simula

as modified by R. Péter and R. Robinson:

```mw
 BEGIN
    INTEGER procedure
    Ackermann(g, p); SHORT INTEGER g, p;
        Ackermann:= IF g = 0 THEN p+1
            ELSE Ackermann(g-1, IF p = 0 THEN 1
                         ELSE Ackermann(g, p-1));

    INTEGER g, p;
    FOR p := 0 STEP 3 UNTIL 13 DO BEGIN
    	g := 4 - p/3;
        outtext("Ackermann("); outint(g, 0);
        outchar(','); outint(p, 2); outtext(") = ");
        outint(Ackermann(g, p), 0); outimage
    END
END
```

**Output:**

```
Ackermann(4, 0) = 13
Ackermann(3, 3) = 61
Ackermann(2, 6) = 15
Ackermann(1, 9) = 11
Ackermann(0,12) = 13
```


## Slate

```mw
m@(Integer traits) ackermann: n@(Integer traits)
[
  m isZero
    ifTrue: [n + 1]
    ifFalse:
      [n isZero
	 ifTrue: [m - 1 ackermann: n]
	 ifFalse: [m - 1 ackermann: (m ackermann: n - 1)]]
].
```


## Smalltalk

```mw
|ackermann|
ackermann := [ :n :m |
  (n = 0) ifTrue: [ (m + 1) ]
          ifFalse: [
           (m = 0) ifTrue: [ ackermann value: (n-1) value: 1 ]
                   ifFalse: [
                        ackermann value: (n-1)
                                  value: ( ackermann value: n
                                                     value: (m-1) )
                   ]
          ]
].

(ackermann value: 0 value: 0) displayNl.
(ackermann value: 3 value: 4) displayNl.
```


## SmileBASIC

```mw
DEF ACK(M,N)
 IF M==0 THEN
  RETURN N+1
 ELSEIF M>0 AND N==0 THEN
  RETURN ACK(M-1,1)
 ELSE
  RETURN ACK(M-1,ACK(M,N-1))
 ENDIF
END
```


## SNOBOL4

Works with

:

Macro Spitbol

Both Snobol4+ and CSnobol stack overflow, at ack(3,3) and ack(3,4), respectively.

```mw
define('ack(m,n)') :(ack_end)
ack     ack = eq(m,0) n + 1 :s(return)
        ack = eq(n,0) ack(m - 1,1) :s(return)
        ack = ack(m - 1,ack(m,n - 1)) :(return)
ack_end

*       # Test and display ack(0,0) .. ack(3,6)
L1      str = str ack(m,n) ' '
        n = lt(n,6) n + 1 :s(L1)
        output = str; str = ''
        n = 0; m = lt(m,3) m + 1 :s(L1)
end
```

**Output:**

```
1 2 3 4 5 6 7
2 3 4 5 6 7 8
3 5 7 9 11 13 15
5 13 29 61 125 253 509
```


## SNUSP

```mw
   /==!/==atoi=@@@-@-----#
   |   |                          Ackermann function
   |   |       /=========\!==\!====\  recursion:
$,@/>,@/==ack=!\?\<+#    |   |     |   A(0,j) -> j+1
 j   i           \<?\+>-@/#  |     |   A(i,0) -> A(i-1,1)
                    \@\>@\->@/@\<-@/#  A(i,j) -> A(i-1,A(i,j-1))
                      |  |     |
            #      #  |  |     |             /+<<<-\  
            /-<<+>>\!=/  \=====|==!/========?\>>>=?/<<#
            ?      ?           |   \<<<+>+>>-/
            \>>+<<-/!==========/
            #      #
```

One could employ tail recursion elimination by replacing "@/#" with "/" in two places above.


## SPAD

Works with

:

FriCAS, OpenAxiom, Axiom

```mw
NNI ==> NonNegativeInteger

A:(NNI,NNI) -> NNI

A(m,n) ==
  m=0 => n+1
  m>0 and n=0 => A(m-1,1)
  m>0 and n>0 => A(m-1,A(m,n-1))
  
-- Example  
matrix [[A(i,j) for i in 0..3] for j in 0..3]
```

**Output:**

```
        +1  2  3  5 +
        |           |
        |2  3  5  13|
   (1)  |           |
        |3  4  7  29|
        |           |
        +4  5  9  61+
                                             Type: Matrix(NonNegativeInteger)
```


## SQL PL

Works with

:

Db2 LUW

version 9.7 or higher.

With SQL PL:

```mw
--#SET TERMINATOR @

SET SERVEROUTPUT ON@

CREATE OR REPLACE FUNCTION ACKERMANN(
  IN M SMALLINT,
  IN N BIGINT
 ) RETURNS BIGINT
 BEGIN
  DECLARE RET BIGINT;
  DECLARE STMT STATEMENT;

  IF (M = 0) THEN
   SET RET = N + 1;
  ELSEIF (N = 0) THEN
   PREPARE STMT FROM 'SET ? = ACKERMANN(? - 1, 1)';
   EXECUTE STMT INTO RET USING M;
  ELSE
   PREPARE STMT FROM 'SET ? = ACKERMANN(? - 1, ACKERMANN(?, ? - 1))';
   EXECUTE STMT INTO RET USING M, M, N;
  END IF;
  RETURN RET;
 END @
 
BEGIN
 DECLARE M SMALLINT DEFAULT 0;
 DECLARE N SMALLINT DEFAULT 0;
 DECLARE MAX_LEVELS CONDITION FOR SQLSTATE '54038';
 DECLARE CONTINUE HANDLER FOR MAX_LEVELS BEGIN END;

 WHILE (N <= 6) DO
  WHILE (M <= 3) DO
   CALL DBMS_OUTPUT.PUT_LINE('ACKERMANN(' || M || ', ' || N || ') = ' || ACKERMANN(M, N));
   SET M = M + 1;
  END WHILE;
  SET M = 0;
  SET N = N + 1;
 END WHILE;
END @
```

Output:

```
db2 -td@
db2 => CREATE OR REPLACE FUNCTION ACKERMANN(
...
db2 (cont.) => END @
DB20000I  The SQL command completed successfully.
db2 => BEGIN
db2 (cont.) => END
...
DB20000I  The SQL command completed successfully.

ACKERMANN(0, 0) = 1
ACKERMANN(1, 0) = 2
ACKERMANN(2, 0) = 3
ACKERMANN(3, 0) = 5
ACKERMANN(0, 1) = 2
ACKERMANN(1, 1) = 3
ACKERMANN(2, 1) = 5
ACKERMANN(3, 1) = 13
ACKERMANN(0, 2) = 3
ACKERMANN(1, 2) = 4
ACKERMANN(2, 2) = 7
ACKERMANN(3, 2) = 29
ACKERMANN(0, 3) = 4
ACKERMANN(1, 3) = 5
ACKERMANN(2, 3) = 9
ACKERMANN(3, 3) = 61
ACKERMANN(0, 4) = 5
ACKERMANN(1, 4) = 6
ACKERMANN(2, 4) = 11
ACKERMANN(0, 5) = 6
ACKERMANN(1, 5) = 7
ACKERMANN(2, 5) = 13
ACKERMANN(0, 6) = 7
ACKERMANN(1, 6) = 8
ACKERMANN(2, 6) = 15
```

The maximum levels of cascade calls in Db2 are 16, and in some cases when executing the Ackermann function, it arrives to this limit (SQL0724N). Thus, the code catches the exception and continues with the next try.


## Standard ML

```mw
fun a (0, n) = n+1
  | a (m, 0) = a (m-1, 1)
  | a (m, n) = a (m-1, a (m, n-1))
```


## Stata

```mw
mata
function ackermann(m,n) {
	if (m==0) {
		return(n+1)
	} else if (n==0) {
		return(ackermann(m-1,1))
	} else {
		return(ackermann(m-1,ackermann(m,n-1)))
	}
}

for (i=0; i<=3; i++) printf("%f\n",ackermann(i,4))
5
6
11
125
end
```


## Stax

```
{n!{sd^}{c!{dv1y!}{vscvsay!y!}?}?}Y
```

```
0 0y!P
0 4y!P
1 0y!P
1 1y!P
2 1y!P
2 2y!P
3 1y!P
3 3y!P
3 1y!P
```

**Output:**

```
1
5
2
3
5
7
13
61
13
```


## Swift

```mw
func ackerman(m:Int, n:Int) -> Int {
    if m == 0 {
        return n+1
    } else if n == 0 {
        return ackerman(m-1, 1)
    } else {
        return ackerman(m-1, ackerman(m, n-1))
    }
}
```


## TAV

```mw
ackermann (n) (m) :
  ? n = 0
    :> m+1
  ? m = 0
    :> ackermann (n-1) 1
  :> ackermann (n-1) ackermann n (m-1) \ = ackermann (n-1) (ackermann n (m-1))
\ test it
main(params):+
  p1 =: string params[1] as integer else 3
  p2 =: string params[2] as integer else 5
  print "ackermann(" _ p1 _ "," _ p2 _ ") = " _ ackermann p1 p2
```


## Tcl

### Simple

Translation of

:

Ruby

```mw
proc ack {m n} {
    if {$m == 0} {
        expr {$n + 1}
    } elseif {$n == 0} {
        ack [expr {$m - 1}] 1
    } else {
        ack [expr {$m - 1}] [ack $m [expr {$n - 1}]]
    }
}
```

### With Tail Recursion

With Tcl 8.6, this version is preferred (though the language supports tailcall optimization, it does not apply it automatically in order to preserve stack frame semantics):

```mw
proc ack {m n} {
    if {$m == 0} {
        expr {$n + 1}
    } elseif {$n == 0} {
        tailcall ack [expr {$m - 1}] 1
    } else {
        tailcall ack [expr {$m - 1}] [ack $m [expr {$n - 1}]]
    }
}
```

### To Infinity… and Beyond!

If we want to explore the higher reaches of the world of Ackermann's function, we need techniques to really cut the amount of computation being done.

Works with

:

Tcl

version 8.6

```mw
package require Tcl 8.6

# A memoization engine, from http://wiki.tcl.tk/18152
oo::class create cache {
    filter Memoize
    variable ValueCache
    method Memoize args {
        # Do not filter the core method implementations
        if {[lindex [self target] 0] eq "::oo::object"} {
            return [next {*}$args]
        }

        # Check if the value is already in the cache
        set key [self target],$args
        if {[info exist ValueCache($key)]} {
            return $ValueCache($key)
        }

        # Compute value, insert into cache, and return it
        return [set ValueCache($key) [next {*}$args]]
    }
    method flushCache {} {
        unset ValueCache
        # Skip the cacheing
        return -level 2 ""
    }
}

# Make an object, attach the cache engine to it, and define ack as a method
oo::object create cached
oo::objdefine cached {
    mixin cache
    method ack {m n} {
        if {$m==0} {
            expr {$n+1}
        } elseif {$m==1} {
            # From the Mathematica version
            expr {$m+2}
        } elseif {$m==2} {
            # From the Mathematica version
            expr {2*$n+3}
        } elseif {$m==3} {
            # From the Mathematica version
            expr {8*(2**$n-1)+5}
        } elseif {$n==0} {
            tailcall my ack [expr {$m-1}] 1
        } else {
            tailcall my ack [expr {$m-1}] [my ack $m [expr {$n-1}]]
        }
    }
}

# Some small tweaks...
interp recursionlimit {} 100000
interp alias {} ack {} cacheable ack
```

But even with all this, you still run into problems calculating ${\displaystyle {\mathit {ack}}(4,3)}$ as that's kind-of large…


## TI-83 BASIC

This program assumes the variables N and M are the arguments of the function, and that the list L1 is empty. It stores the result in the system variable ANS. (Program names can be no longer than 8 characters, so I had to truncate the function's name.)

```mw
PROGRAM:ACKERMAN
:If not(M
:Then
:N+1→N
:Return
:Else
:If not(N
:Then
:1→N
:M-1→M
:prgmACKERMAN
:Else
:N-1→N
:M→L1(1+dim(L1
:prgmACKERMAN
:Ans→N
:L1(dim(L1))-1→M
:dim(L1)-1→dim(L1
:prgmACKERMAN
:End
:End
```

Here is a handler function that makes the previous function easier to use. (You can name it whatever you want.)

```mw
PROGRAM:AHANDLER
:0→dim(L1
:Prompt M
:Prompt N
:prgmACKERMAN
:Disp Ans
```


## TI-89 BASIC

```mw
Define A(m,n) = when(m=0, n+1, when(n=0, A(m-1,1), A(m-1, A(m, n-1))))
```


## TorqueScript

```mw
function ackermann(%m,%n)
{
   if(%m==0)
      return %n+1;
   if(%m>0&&%n==0)
      return ackermann(%m-1,1);
   if(%m>0&&%n>0)
      return ackermann(%m-1,ackermann(%m,%n-1));
}
```


## Transd

```mw
#lang transd

MainModule: {
    Ack: Lambda<Int Int Int>(λ m Int() n Int() 
        (if (not m) (ret (+ n 1)))
        (if (not n) (ret (exec Ack (- m 1) 1)))
        (ret (exec Ack (- m 1) (exec Ack m (- n 1))))
    ),
    _start: (λ (textout (exec Ack 3 1) "\n" 
                        (exec Ack 3 2) "\n"
                        (exec Ack 3 3)))
}
```

**Output:**

```
13
29
61
```


## TSE SAL

```mw
// library: math: get: ackermann: recursive <description></description> <version>1.0.0.0.5</version> <version control></version control> (filenamemacro=getmaare.s) [kn, ri, tu, 27-12-2011 14:46:59]
INTEGER PROC FNMathGetAckermannRecursiveI( INTEGER mI, INTEGER nI )
 IF ( mI == 0 )
  RETURN( nI + 1 )
 ENDIF
 IF ( nI == 0 )
  RETURN( FNMathGetAckermannRecursiveI( mI - 1, 1 ) )
 ENDIF
 RETURN( FNMathGetAckermannRecursiveI( mI - 1, FNMathGetAckermannRecursiveI( mI, nI - 1 ) ) )
END

PROC Main()
STRING s1[255] = "2"
STRING s2[255] = "3"
IF ( NOT ( Ask( "math: get: ackermann: recursive: m = ", s1, _EDIT_HISTORY_ ) ) AND ( Length( s1 ) > 0 ) ) RETURN() ENDIF
IF ( NOT ( Ask( "math: get: ackermann: recursive: n = ", s2, _EDIT_HISTORY_ ) ) AND ( Length( s2 ) > 0 ) ) RETURN() ENDIF
 Message( FNMathGetAckermannRecursiveI( Val( s1 ), Val( s2 ) ) ) // gives e.g. 9
END
```


## TXR

Translation of

:

Scheme

with memoization.

```mw
(defmacro defmemofun (name (. args) . body)
  (let ((hash (gensym "hash-"))
        (argl (gensym "args-"))
        (hent (gensym "hent-"))
        (uniq (copy-str "uniq")))
    ^(let ((,hash (hash :equal-based)))
       (defun ,name (,*args)
         (let* ((,argl (list ,*args))
                (,hent (inhash ,hash ,argl ,uniq)))
           (if (eq (cdr ,hent) ,uniq)
             (set (cdr ,hent) (block ,name (progn ,*body)))
             (cdr ,hent)))))))

(defmemofun ack (m n)
  (cond
    ((= m 0) (+ n 1))
    ((= n 0) (ack (- m 1) 1))
    (t (ack (- m 1) (ack m (- n 1))))))

(each ((i (range 0 3)))
  (each ((j (range 0 4)))
    (format t "ack(~a, ~a) = ~a\n" i j (ack i j))))
```

**Output:**

```
ack(0, 0) = 1
ack(0, 1) = 2
ack(0, 2) = 3
ack(0, 3) = 4
ack(0, 4) = 5
ack(1, 0) = 2
ack(1, 1) = 3
ack(1, 2) = 4
ack(1, 3) = 5
ack(1, 4) = 6
ack(2, 0) = 3
ack(2, 1) = 5
ack(2, 2) = 7
ack(2, 3) = 9
ack(2, 4) = 11
ack(3, 0) = 5
ack(3, 1) = 13
ack(3, 2) = 29
ack(3, 3) = 61
ack(3, 4) = 125
```


## Uiua

```mw
A ←|2.1 (
  ◡(×+1>0:>0)
  sw(+1pop|A-1:1pop:
    |A-1:off(A:-1:))
)

A 1 1
```

**Output:**

```
3
```


## UNIX Shell

Works with

:

Bash

```mw
ack() {
  local m=$1
  local n=$2
  if [ $m -eq 0 ]; then
    echo -n $((n+1))
  elif [ $n -eq 0 ]; then
    ack $((m-1)) 1
  else
    ack $((m-1)) $(ack $m $((n-1)))
  fi
}
```

Example:

```mw
for ((m=0;m<=3;m++)); do
  for ((n=0;n<=6;n++)); do
    ack $m $n
    echo -n " "
  done
  echo
done
```

**Output:**

```
1 2 3 4 5 6 7
2 3 4 5 6 7 8
3 5 7 9 11 13 15
5 13 29 61 125 253 509
```


## Ursalang

```mw
let A = fn(m, n) {
    if m == 0 {n + 1}
    else if m > 0 and n == 0 {A(m - 1, 1)}
    else {A(m - 1, A(m, n - 1))}
}
 
print(A(0, 0))
print(A(3, 4))
print(A(3, 1))
```


## Ursala

Anonymous recursion is the usual way of doing things like this.

```mw
#import std
#import nat

ackermann = 

~&al^?\successor@ar ~&ar?(
   ^R/~&f ^/predecessor@al ^|R/~& ^|/~& predecessor,
   ^|R/~& ~&\1+ predecessor@l)
```

test program for the first 4 by 7 numbers:

```mw
#cast %nLL

test = block7 ackermann*K0 iota~~/4 7
```

**Output:**

```
<
   <1,2,3,4,5,6,7>,
   <2,3,4,5,6,7,8>,
   <3,5,7,9,11,13,15>,
   <5,13,29,61,125,253,509>>
```


## V

Translation of

:

Joy

```mw
[ack
       [ [pop zero?] [popd succ]
         [zero?]     [pop pred 1 ack]
         [true]      [[dup pred swap] dip pred ack ack ]
       ] when].
```

using destructuring view

```mw
[ack
       [ [pop zero?] [ [m n : [n succ]] view i]
         [zero?]     [ [m n : [m pred 1 ack]] view i]
         [true]      [ [m n : [m pred m n pred ack ack]] view i]
       ] when].
```


## Vala

```mw
uint64 ackermann(uint64 m, uint64 n) {
  if (m == 0) return n + 1;
  if (n == 0) return ackermann(m - 1, 1);
  return ackermann(m - 1, ackermann(m, n - 1));
}

void main () {
  for (uint64 m = 0; m < 4; ++m) {
    for (uint64 n = 0; n < 10; ++n) {
      print(@"A($m,$n) = $(ackermann(m,n))\n");
    }
  }
}
```

**Output:**

```
A(0,0) = 1
A(0,1) = 2
A(0,2) = 3
A(0,3) = 4
A(0,4) = 5
A(0,5) = 6
A(0,6) = 7
A(0,7) = 8
A(0,8) = 9
A(0,9) = 10
A(1,0) = 2
A(1,1) = 3
A(1,2) = 4
A(1,3) = 5
A(1,4) = 6
A(1,5) = 7
A(1,6) = 8
A(1,7) = 9
A(1,8) = 10
A(1,9) = 11
A(2,0) = 3
A(2,1) = 5
A(2,2) = 7
A(2,3) = 9
A(2,4) = 11
A(2,5) = 13
A(2,6) = 15
A(2,7) = 17
A(2,8) = 19
A(2,9) = 21
A(3,0) = 5
A(3,1) = 13
A(3,2) = 29
A(3,3) = 61
A(3,4) = 125
A(3,5) = 253
A(3,6) = 509
A(3,7) = 1021
A(3,8) = 2045
A(3,9) = 4093
```


## VBA

```mw
Private Function Ackermann_function(m As Variant, n As Variant) As Variant
    Dim result As Variant
    Debug.Assert m >= 0
    Debug.Assert n >= 0
    If m = 0 Then
        result = CDec(n + 1)
    Else
        If n = 0 Then
            result = Ackermann_function(m - 1, 1)
        Else
            result = Ackermann_function(m - 1, Ackermann_function(m, n - 1))
        End If
    End If
    Ackermann_function = CDec(result)
End Function
Public Sub main()
    Debug.Print "           n=",
    For j = 0 To 7
        Debug.Print j,
    Next j
    Debug.Print
    For i = 0 To 3
        Debug.Print "m=" & i,
        For j = 0 To 7
            Debug.Print Ackermann_function(i, j),
        Next j
        Debug.Print
    Next i
End Sub
```

**Output:**

```
           n=  0             1             2             3             4             5             6             7            
m=0            1             2             3             4             5             6             7             8            
m=1            2             3             4             5             6             7             8             9            
m=2            3             5             7             9             11            13            15            17           
m=3            5             13            29            61            125           253           509           1021   
```


## VBScript

Based on BASIC version. Uncomment all the lines referring to `depth` and see just how deep the recursion goes.

**Implementation**

```mw
option explicit
'~ dim depth
function ack(m, n)
	'~ wscript.stdout.write depth & " "
	if m = 0 then 
		'~ depth = depth + 1
		ack = n + 1
		'~ depth = depth - 1
	elseif m > 0 and n = 0 then
		'~ depth = depth + 1
		ack = ack(m - 1, 1)
		'~ depth = depth - 1
	'~ elseif m > 0 and n > 0 then
	else
		'~ depth = depth + 1
		ack = ack(m - 1, ack(m, n - 1))
		'~ depth = depth - 1
	end if
	
end function
```

**Invocation**

```mw
wscript.echo ack( 1, 10 )
'~ depth = 0
wscript.echo ack( 2, 1 )
'~ depth = 0
wscript.echo ack( 4, 4 )
```

**Output:**

```
12
5
C:\foo\ackermann.vbs(16, 3) Microsoft VBScript runtime error: Out of stack space: 'ack'
```


## Visual Basic

Translation of

:

Rexx

Works with

:

Visual Basic

version VB6 Standard

```mw
Option Explicit
Dim calls As Long
Sub main()
    Const maxi = 4
    Const maxj = 9
    Dim i As Long, j As Long
    For i = 0 To maxi
        For j = 0 To maxj
            Call print_acker(i, j)
        Next j
    Next i
End Sub 'main
Sub print_acker(m As Long, n As Long)
    calls = 0
    Debug.Print "ackermann("; m; ","; n; ")=";
    Debug.Print ackermann(m, n), "calls="; calls
End Sub 'print_acker
Function ackermann(m As Long, n As Long) As Long
    calls = calls + 1
    If m = 0 Then
        ackermann = n + 1
    Else
        If n = 0 Then
            ackermann = ackermann(m - 1, 1)
        Else
            ackermann = ackermann(m - 1, ackermann(m, n - 1))
        End If
    End If
End Function 'ackermann
```

**Output:**

```
ackermann( 0 , 0 )= 1       calls= 1 
ackermann( 0 , 1 )= 2       calls= 1 
ackermann( 0 , 2 )= 3       calls= 1 
ackermann( 0 , 3 )= 4       calls= 1 
ackermann( 0 , 4 )= 5       calls= 1 
ackermann( 0 , 5 )= 6       calls= 1 
ackermann( 0 , 6 )= 7       calls= 1 
ackermann( 0 , 7 )= 8       calls= 1 
ackermann( 0 , 8 )= 9       calls= 1 
ackermann( 0 , 9 )= 10      calls= 1 
ackermann( 1 , 0 )= 2       calls= 2 
ackermann( 1 , 1 )= 3       calls= 4 
ackermann( 1 , 2 )= 4       calls= 6 
ackermann( 1 , 3 )= 5       calls= 8 
ackermann( 1 , 4 )= 6       calls= 10 
ackermann( 1 , 5 )= 7       calls= 12 
ackermann( 1 , 6 )= 8       calls= 14 
ackermann( 1 , 7 )= 9       calls= 16 
ackermann( 1 , 8 )= 10      calls= 18 
ackermann( 1 , 9 )= 11      calls= 20 
ackermann( 2 , 0 )= 3       calls= 5 
ackermann( 2 , 1 )= 5       calls= 14 
ackermann( 2 , 2 )= 7       calls= 27 
ackermann( 2 , 3 )= 9       calls= 44 
ackermann( 2 , 4 )= 11      calls= 65 
ackermann( 2 , 5 )= 13      calls= 90 
ackermann( 2 , 6 )= 15      calls= 119 
ackermann( 2 , 7 )= 17      calls= 152 
ackermann( 2 , 8 )= 19      calls= 189 
ackermann( 2 , 9 )= 21      calls= 230 
ackermann( 3 , 0 )= 5       calls= 15 
ackermann( 3 , 1 )= 13      calls= 106 
ackermann( 3 , 2 )= 29      calls= 541 
ackermann( 3 , 3 )= 61      calls= 2432 
ackermann( 3 , 4 )= 125     calls= 10307 
ackermann( 3 , 5 )= 253     calls= 42438 
ackermann( 3 , 6 )= 509     calls= 172233 
ackermann( 3 , 7 )= 1021    calls= 693964 
ackermann( 3 , 8 )= 2045    calls= 2785999 
ackermann( 3 , 9 )= 4093    calls= 11164370 
ackermann( 4 , 0 )= 13      calls= 107 
ackermann( 4 , 1 )= out of stack space
```


## V (Vlang)

```mw
fn ackermann(m int, n int ) int {
    if m == 0 {
        return n + 1
    }
    else if n == 0 {
        return ackermann(m - 1, 1)
    }
    return ackermann(m - 1, ackermann(m, n - 1) )
}

fn main() {
    for m := 0; m <= 4; m++ {
        for n := 0; n < ( 6 - m ); n++ {
            println('Ackermann($m, $n) = ${ackermann(m, n)}')
        }
    }
}
```

**Output:**

```
Ackermann(0, 0) = 1
Ackermann(0, 1) = 2
Ackermann(0, 2) = 3
Ackermann(0, 3) = 4
Ackermann(0, 4) = 5
Ackermann(0, 5) = 6
Ackermann(1, 0) = 2
Ackermann(1, 1) = 3
Ackermann(1, 2) = 4
Ackermann(1, 3) = 5
Ackermann(1, 4) = 6
Ackermann(2, 0) = 3
Ackermann(2, 1) = 5
Ackermann(2, 2) = 7
Ackermann(2, 3) = 9
Ackermann(3, 0) = 5
Ackermann(3, 1) = 13
Ackermann(3, 2) = 29
Ackermann(4, 0) = 13
Ackermann(4, 1) = 65533
```


## Wart

```mw
def (ackermann m n)
  (if m=0
        n+1
      n=0
        (ackermann m-1 1)
      :else
        (ackermann m-1 (ackermann m n-1)))
```


## WDTE

```mw
let memo a m n => true {
	== m 0 => + n 1;
	== n 0 => a (- m 1) 1;
	true => a (- m 1) (a m (- n 1));
};
```


## Wren

```mw
// To use recursion definition and declaration must be on separate lines
var Ackermann 
Ackermann = Fn.new {|m, n|
    if (m == 0) return n + 1
    if (n == 0) return Ackermann.call(m - 1, 1)
    return Ackermann.call(m - 1, Ackermann.call(m, n - 1))
}

var pairs = [ [1, 3], [2, 3], [3, 3], [1, 5], [2, 5], [3, 5] ]
for (pair in pairs) {
    var p1 = pair[0]
    var p2 = pair[1]
    System.print("A[%(p1), %(p2)] = %(Ackermann.call(p1, p2))")
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


## X86 Assembly

Works with

:

nasm

Works with

:

windows

```mw
section .text

global _main
_main:
    mov eax, 3 ;m
    mov ebx, 4 ;n
    call ack ;returns number in ebx
    ret
    
ack:
    cmp eax, 0
    je M0 ;if M == 0
    cmp ebx, 0
    je N0 ;if N == 0
    dec ebx ;else N-1
    push eax ;save M
    call ack1 ;ack(m,n) -> returned in ebx so no further instructions needed
    pop eax ;restore M
    dec eax ;M - 1
    call ack1 ;return ack(m-1,ack(m,n-1))
    ret
    M0:
        inc ebx ;return n + 1
        ret
    N0:
        dec eax
        inc ebx ;ebx always 0: inc -> ebx = 1
        call ack1 ;return ack(M-1,1)
        ret
```


## XLISP

```mw
(defun ackermann (m n)
    (cond
        ((= m 0) (+ n 1))
        ((= n 0) (ackermann (- m 1) 1))
        (t (ackermann (- m 1) (ackermann m (- n 1))))))
```

Test it:

```mw
(print (ackermann 3 9))
```

Output (after a very perceptible pause):

```
4093
```

That worked well. Test it again:

```mw
(print (ackermann 4 1))
```

Output (after another pause):

```
Abort: control stack overflow
happened in: #<Code ACKERMANN>
```


## XPL0

```mw
include c:\cxpl\codes;

func Ackermann(M, N);
int M, N;
[if M=0 then return N+1;
 if N=0 then return Ackermann(M-1, 1);
return Ackermann(M-1, Ackermann(M, N-1));
]; \Ackermann

int M, N;
[for M:= 0 to 3 do
    [for N:= 0 to 7 do
        [IntOut(0, Ackermann(M, N));  ChOut(0,9\tab\)];
    CrLf(0);
    ];
]
```

Recursion overflows the stack if either M or N is extended by a single count.

**Output:**

```
1       2       3       4       5       6       7       8       
2       3       4       5       6       7       8       9       
3       5       7       9       11      13      15      17      
5       13      29      61      125     253     509     1021    
```
