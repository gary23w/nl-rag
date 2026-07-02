---
title: "FizzBuzz (part 6/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/7
---

## R

```mw
xx <- x <- 1:100
xx[x %% 3 == 0] <- "Fizz"
xx[x %% 5 == 0] <- "Buzz"
xx[x %% 15 == 0] <- "FizzBuzz"
xx
```

Or, without directly checking for divisibility by 15:

```mw
xx <- rep("", 100)
x <- 1:100
xx[x %% 3 == 0] <- paste0(xx[x %% 3 == 0], "Fizz")
xx[x %% 5 == 0] <- paste0(xx[x %% 5 == 0], "Buzz")
xx[xx == ""] <- x[xx == ""]
xx
```

Or, (ab)using the vector recycling rule:

```mw
x <- paste0(rep("", 100), c("", "", "Fizz"), c("", "", "", "", "Buzz"))
cat(ifelse(x == "", 1:100, x), sep = "\n")
```

Or, for an abuse of the recycling rules that could be generalised:

```mw
x <- paste0(rep("", 100), rep(c("", "Fizz"), times = c(2, 1)), rep(c("", "Buzz"), times = c(4, 1)))
cat(ifelse(x == "", 1:100, x), sep = "\n")
```

Or, with a more straightforward use of ifelse:

```mw
x <- 1:100
ifelse(x %% 15 == 0, 'FizzBuzz',
       ifelse(x %% 5 == 0, 'Buzz',
              ifelse(x %% 3 == 0, 'Fizz', x)))
```

Or, adapting from General FizzBuzz#Names solution:

```mw
namedNums <- c(Fizz = 3, Buzz = 5)
for(i in 1:100)
{
  isFactor <- i %% namedNums == 0
  print(if(any(isFactor)) paste0(names(namedNums)[isFactor], collapse = "") else i)
}
```


## Racket

```mw
#lang racket

(for ([n (in-range 1 101)]) 
  (displayln 
   (match (gcd n 15) 
     [15 "fizzbuzz"] 
     [3 "fizz"] 
     [5 "buzz"] 
     [_ n])))
```


## Raku

(formerly Perl 6)

Works with

:

Rakudo Star

version 2015-09-10

Most straightforwardly:

```mw
for 1 .. 100 {
    when $_ %% (3 & 5) { say 'FizzBuzz'; }
    when $_ %% 3       { say 'Fizz'; }
    when $_ %% 5       { say 'Buzz'; }
    default            { .say; }
}
```

Or abusing multi subs:

```mw
multi sub fizzbuzz(Int $ where * %% 15) { 'FizzBuzz' }
multi sub fizzbuzz(Int $ where * %%  5) { 'Buzz' }
multi sub fizzbuzz(Int $ where * %%  3) { 'Fizz' }
multi sub fizzbuzz(Int $number        ) { $number }
(1 .. 100)».&fizzbuzz.say;
```

Or abusing list metaoperators:

```mw
[1..100].map({[~] ($_%%3, $_%%5) »||» "" Z&& <fizz buzz> or $_ })».say
```

Concisely (readable):

```mw
say 'Fizz' x $_ %% 3 ~ 'Buzz' x $_ %% 5 || $_ for 1 .. 100;
```

Shortest FizzBuzz to date:

```mw
say "Fizz"x$_%%3~"Buzz"x$_%%5||$_ for 1..100
```

And here's an implementation that never checks for divisibility:

```mw
.say for
    (
      (flat ('' xx 2, 'Fizz') xx *)
      Z~
      (flat ('' xx 4, 'Buzz') xx *)
    )
    Z||
    1 .. 100;
```


## RapidQ

The BASIC solutions work with RapidQ, too. However, here is a bit more esoteric solution using the IIF() function.

```mw
FOR i=1 TO 100
    t$ = IIF(i MOD 3 = 0, "Fizz", "") + IIF(i MOD 5 = 0, "Buzz", "")
    PRINT IIF(LEN(t$), t$, i)
NEXT i
```


## Rascal

```mw
import IO;

public void fizzbuzz() {
   for(int n <- [1 .. 100]){
      fb = ((n % 3 == 0) ? "Fizz" : "") + ((n % 5 == 0) ? "Buzz" : "");
      println((fb == "") ?"<n>" : fb);
   }
}
```


## Raven

```mw
100 each 1 + as n
  ''
  n 3 mod 0 = if 'Fizz' cat
  n 5 mod 0 = if 'Buzz' cat
  dup empty if drop n
  say
```


## REALbasic

See FizzBuzz/Basic


## ReasonML

```mw
let fizzbuzz i =>
  switch (i mod 3, i mod 5) {
  | (0, 0) => "FizzBuzz"
  | (0, _) => "Fizz"
  | (_, 0) => "Buzz"
  | _ => string_of_int i
  };

for i in 1 to 100 {
  print_endline (fizzbuzz i)
};
```


## Rebol

An implementation that concatenates strings and includes a proper code header (title, date, etc.)

```mw
Rebol [
	Title: "FizzBuzz"
	URL: http://rosettacode.org/wiki/FizzBuzz
]

; Concatenative. Note use of 'case/all' construct to evaluate all
; conditions. I use 'copy' to allocate a new string each time through
; the loop -- otherwise 'x' would get very long...

repeat i 100 [
	x: copy ""
	case/all [
		0 = mod i 3 [append x "Fizz"]
		0 = mod i 5 [append x "Buzz"]
		"" = x      [x: mold i]
	]
	print x
]
```

Here is an example by Nick Antonaccio.

```mw
repeat i 100 [
    print switch/default 0 compose [
        (mod i 15) ["fizzbuzz"]
        (mod i 3)  ["fizz"]
        (mod i 5)  ["buzz"]
    ][i]
]
```

And a minimized version:

```mw
repeat i 100[j:""if i // 3 = 0[j:"fizz"]if i // 5 = 0[j: join j"buzz"]if""= j[j: i]print j]
```

The following is presented as a curiosity only, not as an example of good coding practice:

```mw
m: func [i d] [0 = mod i d]  
spick: func [t x y][either any [not t  "" = t][y][x]]
zz: func [i] [rejoin [spick m i 3 "Fizz" ""  spick m i 5 "Buzz" ""]]
repeat i 100 [print spick z: zz i z i]
```


## Red

```mw
Red [Title: "FizzBuzz"]

repeat i 100 [
    print case [
        i % 15 = 0 ["FizzBuzz"]
        i % 5 = 0 ["Buzz"]
        i % 3 = 0 ["Fizz"]
        true [i]
    ]
]
```


## Refal

```mw
$ENTRY Go {
    = <FizzBuzz 1>;
};

FizzBuzz {
    101 = ;
    s.N = <Prout <Item s.N>>
          <FizzBuzz <+ 1 s.N>>;
};

Item {
    s.N, <Mod s.N 15>: 0 = FizzBuzz;
    s.N, <Mod s.N 5>: 0  = Buzz;
    s.N, <Mod s.N 3>: 0  = Fizz;
    s.N = s.N;
};
```


## Retro

Replaced everything, since it didn't work anymore

```mw
( empty string result to display result )
~~~

'result var
' s:format !result

'number var
#1 !number

~~~
( checks for empty string if result empty print number )
( else append fizz for divisible by 3 and prepend buzz for divisible by 5)
( if; exists the word fizzbuzz immediately )
~~~

:fizzbuzz (-)
    @number #3  mod #0 eq? [ 'fizz @result s:append !result ] if
    @number #5  mod #0 eq? [ 'buzz @result s:prepend !result ] if
    ' @result s:eq? [ @number n:put nl ] if;
    ' @result s:eq? not [ @result s:put nl ] if;    
     ;

[ fizzbuzz 'result var
    ' s:format !result @number #1 + !number @number #100 lteq? ] while

~~~
```


## REXX

This version's program logic closely mirrors the problem statement:

### three IF-THEN

```mw
/*REXX program displays numbers  1 ──► 100  (some transformed) for the FizzBuzz problem.*/
                                                 /*╔═══════════════════════════════════╗*/
  do j=1  to 100;      z=  j                     /*║                                   ║*/
  if j//3    ==0  then z= 'Fizz'                 /*║  The divisors  (//)  of the  IFs  ║*/
  if j//5    ==0  then z= 'Buzz'                 /*║  must be in ascending order.      ║*/
  if j//(3*5)==0  then z= 'FizzBuzz'             /*║                                   ║*/
  say right(z, 8)                                /*╚═══════════════════════════════════╝*/
  end   /*j*/                                    /*stick a fork in it,  we're all done. */
```

**output**

```
       1
       2
    Fizz
       4
    Buzz
    Fizz
       7
       8
    Fizz
    Buzz
      11
    Fizz
      13
      14
FizzBuzz
      16
      17
    Fizz
      19
    Buzz
    Fizz
      22
      23
    Fizz
    Buzz
      26
    Fizz
      28
      29
FizzBuzz
      31
      32
    Fizz
      34
    Buzz
    Fizz
      37
      38
    Fizz
    Buzz
      41
    Fizz
      43
      44
FizzBuzz
      46
      47
    Fizz
      49
    Buzz
    Fizz
      52
      53
    Fizz
    Buzz
      56
    Fizz
      58
      59
FizzBuzz
      61
      62
    Fizz
      64
    Buzz
    Fizz
      67
      68
    Fizz
    Buzz
      71
    Fizz
      73
      74
FizzBuzz
      76
      77
    Fizz
      79
    Buzz
    Fizz
      82
      83
    Fizz
    Buzz
      86
    Fizz
      88
      89
FizzBuzz
      91
      92
    Fizz
      94
    Buzz
    Fizz
      97
      98
    Fizz
    Buzz
```

### SELECT-WHEN

This version is a different form, but essentially identical to the   **IF-THEN**   (above), but doesn't require the use of a temporary variable to hold/contain the output.

```mw
/*REXX program displays numbers  1 ──► 100  (some transformed) for the FizzBuzz problem.*/
                                                 /*╔═══════════════════════════════════╗*/
  do j=1  to 100                                 /*║                                   ║*/
      select                                     /*║                                   ║*/
      when j//15==0  then say 'FizzBuzz'         /*║ The divisors  (//)  of the  WHENs ║*/
      when j//5 ==0  then say '    Buzz'         /*║ must be in  descending  order.    ║*/
      when j//3 ==0  then say '    Fizz'         /*║                                   ║*/
      otherwise           say right(j, 8)        /*╚═══════════════════════════════════╝*/
      end   /*select*/
  end       /*j*/                                /*stick a fork in it,  we're all done. */
```

**output**   is identical to the 1st REXX version.

### two IF-THEN

This version lends itself to expansion   (such as using   **Jazz**   for multiples of   **7**).

```mw
/*REXX program displays numbers  1 ──► 100  (some transformed) for the FizzBuzz problem.*/

   do j=1  for 100;  _=
   if j//3 ==0  then _=_'Fizz'
   if j//5 ==0  then _=_'Buzz'
/* if j//7 ==0  then _=_'Jazz' */                /* ◄─── note that this is a comment.   */
   say right(word(_ j,1),8)
   end   /*j*/                                   /*stick a fork in it,  we're all done. */
```

**output**   is identical to the 1st REXX version.

### "geek" version

```mw
/*REXX program displays numbers  1 ──► 100  (some transformed) for the FizzBuzz problem.*/
                                                 /* [↓]  concise, but somewhat obtuse.  */
  do j=1  for 100
  say right(word(word('Fizz', 1+(j//3\==0))word('Buzz', 1+(j//5\==0)) j, 1), 8)
  end   /*j*/
                                                 /*stick a fork in it,  we're all done. */
```

**output**   is identical to the 1st REXX version.


## Rhombus

Adapted from the Racket version.

```mw
#lang rhombus/static

for (i in 1..=100):
  match math.gcd(i, 15)
  | 15: println("fizzbuzz")
  | 3:  println("fizz")
  | 5:  println("buzz")
  | _:  println(i)
```


## Rhovas

Standard FizzBuzz using a pattern matching approach:

- `range(1, 100, :incl)` creates an inclusion range
- `.for {` iterates through the range, with the current element being `val`
- Pattern matching on `[val.mod(3), val.mod(5)]` is used to check divisibility conditions
  - `[0, 0]`, for instance, matches when `val`is divisible by both `3` and `5`
  - `else` matches all other possibilities, in this case when `val` is not divisible by `3` or `5`

```mw
range(1, 100, :incl).for {
    match ([val.mod(3), val.mod(5)]) {
       [0, 0]: print("FizzBuzz");
       [0, _]: print("Fizz");
       [_, 0]: print("Buzz");
       else: print(val);
    }
};
```


## Ring

```mw
for n = 1 to 100
    if n % 15 = 0 see "" + n + " = " + "FizzBuzz" + nl loop
    but n % 3 = 0 see "" + n + " = " + "Fizz"+ nl
    but n % 5 = 0 see "" + n + " = " + "Buzz" + nl
    else see "" + n + " = " + n + nl ok
next
```

**Output:**

Limited to first 20.

```
1 = 1
2 = 2
3 = Fizz
4 = 4
5 = Buzz
6 = Fizz
7 = 7
8 = 8
9 = Fizz
10 = Buzz
11 = 11
12 = Fizz
13 = 13
14 = 14
15 = FizzBuzz
16 = 16
17 = 17
18 = Fizz
19 = 19
20 = Buzz
```


## RISC-V Assembly

for Raspberry pi pico 2 see instructions to page risc v

```mw
# riscv assembly raspberry pico2 rp2350
# program fizzbuzz.s
# connexion putty com3
/*********************************************/
/*           CONSTANTES                      */
/********************************************/
/* for this file see risc-v task include a file */
.include "../../../constantesRiscv.inc"
/****************************************************/
/* MACROS                   */
/****************************************************/
#.include "../ficmacrosriscv.inc"             # only for debugging
/*******************************************/
/* INITIALED DATAS                    */
/*******************************************/ 
.data
szMessStart:         .asciz "Program riscv start.\r\n"
szMessEndOk:         .asciz "Program riscv end OK.\r\n"
szCariageReturn:     .asciz "\r\n"
szMessFizz:          .asciz " Fizz\n"
szMessBuzz:          .asciz " Buzz\n"
szMessFizzBuzz:      .asciz " FizzBuzz\n"

.align 2
/*******************************************/ 
/*  UNINITIALED DATA                    */
/*******************************************/ 
.bss
sConvArea:         .skip 24

.align 2
/**********************************************/
/* SECTION CODE                              */
/**********************************************/
.text
.global main

main:
    call stdio_init_all        # général init
1:                             # start loop connexion 
    li a0,0                    # raz argument register
    call tud_cdc_n_connected   # waiting for USB connection
    beqz a0,1b                 # return code = zero ? yes -> loop
	
    la a0,szMessStart          # message address
    call writeString           # display message
	
    li s0,0                    # loop indice
	li s1,3                    # divisor 3
	li s2,5                    # divisor 5
	li s3,15                   # divisor 15
	li s4,100
1:	
    remu t0,s0,s3              # / by 15 
	bnez t0,2f
    la s5,szMessFizzBuzz
	j 4f
2:	
    remu t0,s0,s2              # / by 5 
	bnez t0,3f
    la s5,szMessBuzz
	j 4f	
3:	
    remu t0,s0,s1              # / by 3
	bnez t0,5f
    la s5,szMessFizz
	j 4f
	
4:	
	mv a0,s0
    la a1,sConvArea
    call conversion10           # conversion decimal

	la a0,sConvArea 
	call writeString
	#la a0,szCariageReturn
	#call writeString
	mv a0,s5
    call writeString           # display message
5:
	addi s0,s0,1
	ble s0,s4,1b
	

 	
    la a0,szMessEndOk          # message address
    call writeString           # display message
    call getchar
100:                           # final loop
    j 100b

/************************************/
/*     file include  Fonctions      */
/***********************************/
/* for this file see risc-v task include a file */
.include "../../../includeFunctions.s"
```

```
Program riscv start.
0 FizzBuzz
3 Fizz
5 Buzz
6 Fizz
9 Fizz
10 Buzz
12 Fizz
15 FizzBuzz
18 Fizz
20 Buzz
21 Fizz
24 Fizz
25 Buzz
27 Fizz
30 FizzBuzz
33 Fizz
35 Buzz
36 Fizz
39 Fizz
40 Buzz
42 Fizz
45 FizzBuzz
48 Fizz
50 Buzz
51 Fizz
54 Fizz
55 Buzz
57 Fizz
60 FizzBuzz
63 Fizz
65 Buzz
66 Fizz
69 Fizz
70 Buzz
72 Fizz
75 FizzBuzz
78 Fizz
80 Buzz
81 Fizz
84 Fizz
85 Buzz
87 Fizz
90 FizzBuzz
93 Fizz
95 Buzz
96 Fizz
99 Fizz
100 Buzz
Program riscv end OK.
```


## Robotic

```mw
set "local1" to 1
: "loop"
wait for 10
if "('local1' % 15)" = 0 then "fizzbuzz"
if "('local1' % 3)" = 0 then "fizz"
if "('local1' % 5)" = 0 then "buzz"
* "&local1&"
: "inc"
inc "local1" by 1
if "local1" <= 100 then "loop"
goto "done"

: "fizzbuzz"
* "FizzBuzz"
goto "inc"

: "fizz"
* "Fizz"
goto "inc"

: "buzz"
* "Buzz"
goto "inc"

: "done"
end
```

The **wait for 10** function is not really necessary, but it helps to slow down the output.


## Rockstar

```
Midnight takes your heart and your soul
While your heart is as high as your soul
Put your heart without your soul into your heart

Give back your heart

Desire is a lovestruck ladykiller
My world is nothing 
Fire is ice
Hate is water
Until my world is Desire,
Build my world up
If Midnight taking my world, Fire is nothing and Midnight taking my world, Hate is nothing
Shout "FizzBuzz!"
Take it to the top

If Midnight taking my world, Fire is nothing
Shout "Fizz!"
Take it to the top

If Midnight taking my world, Hate is nothing
Say "Buzz!"
Take it to the top
  
Whisper my world
```


## Rocq

```mw
Require Import Coq.Lists.List.
(* https://coq.inria.fr/library/Coq.Lists.List.html *)

Require Import Coq.Strings.String.
(* https://coq.inria.fr/library/Coq.Strings.String.html *)

Require Import Coq.Strings.Ascii.
(* https://coq.inria.fr/library/Coq.Strings.Ascii.html *)

Require Import Coq.Init.Nat.
(* https://coq.inria.fr/library/Coq.Init.Nat.html *)

(** Definition of [string_of_nat] to convert natural numbers to strings. *)

Definition ascii_of_digit (n : nat) : ascii :=
  ascii_of_nat (n + 48).

Definition is_digit (n : nat) : bool :=
  andb (0 <=? n) (n <=? 9).

Fixpoint rec_string_of_nat (counter : nat) (n : nat) (acc : string) : string :=
  match counter with
    | 0 => EmptyString
    | S c =>
      if (is_digit n)
      then String (ascii_of_digit n) acc
      else rec_string_of_nat c (n / 10) (String (ascii_of_digit (n mod 10)) acc)
  end.
(** The counter is only used to ensure termination. *)

Definition string_of_nat (n : nat) : string :=
  rec_string_of_nat n n EmptyString.

(** The FizzBuzz problem. *)

Definition fizz : string :=
  "Fizz".

Definition buzz : string :=
  "Buzz".

Definition new_line : string :=
  String (ascii_of_nat 10) EmptyString.

Definition is_divisible_by (n : nat) (k : nat) : bool :=
  (n mod k) =? 0.

Definition get_term (n : nat) : string :=
  if (is_divisible_by n 15) then fizz ++ buzz
  else if (is_divisible_by n 3) then fizz
  else if (is_divisible_by n 5) then buzz
  else (string_of_nat n).

Definition range (a : nat) (b : nat) : list nat :=
  seq a b.

Definition get_terms (n : nat) : list string :=
  map get_term (range 1 n).

Definition fizz_buzz : string :=
  concat new_line (get_terms 100).

(** This shows the string. *)
Eval compute in fizz_buzz.
```

Output

```
     = "1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz"%string
     : string
```


## RPG

```
 **free
 dcl-s ix Int(5);
 for ix = 1 to 100;
   select;
   when %rem(ix:15) = 0;
     dsply 'FizzBuzz';
   when %rem(ix:5) = 0;
     dsply 'Buzz';
   when %rem(ix:3) = 0;
     dsply 'Fizz';
   other;
     dsply (%char(ix));
   endsl;
 endfor;
```


## RPL

#### Structured programming

```
≪ { } 
   1 100 FOR j 
      IF j 3 MOD THEN "" ELSE "Fizz" END     @ alternate version: j MOD 3 "" "Fizz" IFTE
      IF j 5 MOD NOT THEN "Buzz" + END 
      IF DUP SIZE NOT THEN DROP j END 
      + 
   NEXT 
≫ 'FIZZB' STO
```

#### Arithmetic

```
≪ { } 1 100 FOR j 
     j 3 MOD NOT j 5 MOD NOT → a b 
     ≪ IF a b + THEN "FizzBuzz" 5 4 a * - a b 2 * MAX 4 * SUB ELSE j END 
     ≫ + NEXT 
≫ 'FIZZB' STO
```

#### Data-centric

```
≪ "FizzBuzz" { (1,4) (5,8) (1,8) } → fb idx 
   ≪ { } 1 100 FOR j 
      IF j 3 MOD NOT j 5 MOD NOT 2 * + THEN fb idx LAST GET C→R SUB ELSE j END 
      + NEXT 
≫ ≫ 'FIZZB' STO
```

#### Esoteric one-liner

```
≪ ≪ j ROT MOD "" ROT IFTE ≫ → f ≪ { } 1 100 FOR j 3 "Fizz" f EVAL 5 "Buzz" f EVAL + SIZE LAST j IFTE + NEXT ≫ ≫ EVAL
```

#### Using list handling capabilities

Works with

:

RPL

version HP48-R

```
« "Fizz" "Buzz" DUP2 + 3 →LIST REVLIST → fb
  « « n { 15 5 3 1 } MOD NOT fb n + IFT HEAD » n 1 100 1 SEQ
» » 'FIZZB' STO
```

which can be translated into a one-line command:

```
« n { 15 5 3 1 } MOD NOT { "Fizz" "Buzz" "FizzBuzz" } n + IFT HEAD » n 1 100 1 SEQ
```


## Ruby

```mw
1.upto(100) do |n|
  print "Fizz" if a = (n % 3).zero?
  print "Buzz" if b = (n % 5).zero?
  print n unless (a || b)
  puts
end
```

A bit more straightforward:

```mw
(1..100).each do |n|
  puts if (n % 15).zero?
    "FizzBuzz"
  elsif (n % 5).zero?
    "Buzz"
  elsif (n % 3).zero?
    "Fizz"
  else
    n
  end
end
```

Enumerable#Lazy and classes:

We can grab the first n fizz/buzz/fizzbuzz numbers in a list with a user defined function (filter_map), starting at the number we desire

i.e, grabbing the first 10 fizz numbers starting from 30, fizz = Fizz.new(30,10) #=> [30, 33, 36, 39, 42, 45, 48, 51, 54, 57]

```mw
class Enumerator::Lazy
  def filter_map
    Lazy.new(self) do |holder, *values|
      result = yield *values
      holder << result if result
    end
  end
end
 
class Fizz
  def initialize(head, tail)
    @list = (head..Float::INFINITY).lazy.filter_map{|i| i if i % 3 == 0}.first(tail)
  end
 
  def fizz?(num)
    search = @list
    search.include?(num)
  end
 
  def drop(num)
    list = @list
    list.delete(num)
  end
 
  def to_a
    @list.to_a
  end
end
 
class Buzz
  def initialize(head, tail)
    @list = (head..Float::INFINITY).lazy.filter_map{|i| i if i % 5 == 0}.first(tail)
  end
 
  def buzz?(num)
    search = @list
    search.include?(num)
  end
 
  def drop(num)
    list = @list
    list.delete(num)
  end
 
  def to_a
    @list.to_a
  end
end
 
class FizzBuzz
  def initialize(head, tail)
    @list = (head..Float::INFINITY).lazy.filter_map{|i| i if i % 15 == 0}.first(tail)
  end
 
  def fizzbuzz?(num)
    search = @list
    search.include?(num)
  end
 
  def to_a
    @list.to_a
  end
 
  def drop(num)
    list = @list
    list.delete(num)
  end
end
stopper = 100
@fizz = Fizz.new(1,100)
@buzz = Buzz.new(1,100)
@fizzbuzz = FizzBuzz.new(1,100)
def min(v, n)
  if v == 1
    puts "Fizz: #{n}"
    @fizz::drop(n)
  elsif v == 2
    puts "Buzz: #{n}"
    @buzz::drop(n)
  else
    puts "FizzBuzz: #{n}"
    @fizzbuzz::drop(n)
  end
end
(@fizz.to_a & @fizzbuzz.to_a).map{|d| @fizz::drop(d)}
(@buzz.to_a & @fizzbuzz.to_a).map{|d| @buzz::drop(d)}
while @fizz.to_a.min < stopper or @buzz.to_a.min < stopper or @fizzbuzz.to_a.min < stopper
  f, b, fb = @fizz.to_a.min, @buzz.to_a.min, @fizzbuzz.to_a.min
  min(1,f)  if f < fb and f < b
  min(2,b)  if b < f and b < fb
  min(0,fb) if fb < b and fb < f
end
```

An example using string interpolation:

```mw
(1..100).each do |n|
  v = "#{"Fizz" if n % 3 == 0}#{"Buzz" if n % 5 == 0}"
  puts v.empty? ? n : v
end
```

Interpolation inspired one-liner:

```mw
1.upto(100) { |n| puts "#{'Fizz' if n % 3 == 0}#{'Buzz' if n % 5 == 0}#{n if n % 3 != 0 && n % 5 != 0}" }
```

An example using append:

```mw
1.upto 100 do |n|
  r = ''
  r << 'Fizz' if n % 3 == 0
  r << 'Buzz' if n % 5 == 0
  r << n.to_s if r.empty?
  puts r
end
```

Yet another solution:

```mw
1.upto(100) { |i| puts "#{[:Fizz][i%3]}#{[:Buzz][i%5]}"[/.+/] || i }
```

Yet another solution:

```mw
1.upto(100){|i|puts'FizzBuzz '[n=i**4%-15,n+13]||i}
```

Used Enumerable#cycle:

```mw
f = [nil, nil, :Fizz].cycle
b = [nil, nil, nil, nil, :Buzz].cycle
(1..100).each do |i|
  puts "#{f.next}#{b.next}"[/.+/] || i
end
```

After beforehand preparing the Array which put the number from 1 to 100, it processes.

```mw
seq = *0..100
{Fizz:3, Buzz:5, FizzBuzz:15}.each{|k,n| n.step(100,n){|i|seq[i]=k}}
puts seq.drop(1)
```

Monkeypatch example:

```mw
class Integer
  def fizzbuzz
    v = "#{"Fizz" if self % 3 == 0}#{"Buzz" if self % 5 == 0}"
    v.empty? ? self : v
  end
end

puts *(1..100).map(&:fizzbuzz)
```

Without mutable variables or inline printing.

```mw
fizzbuzz = ->(i) do
  (i%15).zero? and next "FizzBuzz"
  (i%3).zero?  and next "Fizz"
  (i%5).zero?  and next "Buzz"
  i
end

puts (1..100).map(&fizzbuzz).join("\n")
```

Jump anywhere#Ruby has a worse example of FizzBuzz, using a continuation!

Using Ruby 3's Pattern Matching:

```mw
1.upto(100) do |n|
  puts case [(n % 3).zero?, (n % 5).zero?]
       in true, false
         "Fizz"
       in false, true
         "Buzz"
       in true, true
         "FizzBuzz"
       else
         n
       end
end
```


## Ruby with RSpec

This is a solution to FizzBuzz using Test-Driven Development (In this case, with Ruby and RSpec). You will need to set up the correct file structure first, with /lib and /spec directories in your root.

Your spec/fizzbuzz_spec.rb file should like this:

```mw
require 'fizzbuzz'

describe 'FizzBuzz' do
  context 'knows that a number is divisible by' do
    it '3' do
      expect(is_divisible_by_three?(3)).to be_true
    end
    it '5' do
      expect(is_divisible_by_five?(5)).to be_true
    end
    it '15' do
      expect(is_divisible_by_fifteen?(15)).to be_true
    end
  end
  context 'knows that a number is not divisible by' do
    it '3' do
      expect(is_divisible_by_three?(1)).not_to be_true
    end
    it '5' do
      expect(is_divisible_by_five?(1)).not_to be_true
    end
    it '15' do
      expect(is_divisible_by_fifteen?(1)).not_to be_true
    end
  end
  context 'while playing the game it returns' do
    it 'the number' do
      expect(fizzbuzz(1)).to eq 1
    end
    it 'Fizz' do
      expect(fizzbuzz(3)).to eq 'Fizz'
    end
    it 'Buzz' do
      expect(fizzbuzz(5)).to eq 'Buzz'
    end
    it 'FizzBuzz' do
      expect(fizzbuzz(15)).to eq 'FizzBuzz'
    end
  end
end
```

There are many ways to get these tests to pass. Here is an example solution of what your lib/fizzbuzz.rb file could look like:

```mw
def fizzbuzz(number)
  return 'FizzBuzz' if is_divisible_by_fifteen?(number)
  return 'Buzz' if is_divisible_by_five?(number)
  return 'Fizz' if is_divisible_by_three?(number)
  number
end

def is_divisible_by_three?(number)
  is_divisible_by(number, 3)
end

def is_divisible_by_five?(number)
  is_divisible_by(number, 5)
end

def is_divisible_by_fifteen?(number)
  is_divisible_by(number, 15)
end

def is_divisible_by(number, divisor)
  number % divisor == 0
end
```

When writing Test Driven code, it's important to remember that you should use the Red, Green, Refactor cycle. Simply writing each of these code snippets independently would go against everything TDD is about. Here is a good video that takes you through the process of writing this FizzBuzz implementation using Ruby & RSpec.


## Run BASIC

See FizzBuzz/Basic


## Rust

Basic example with a for loop and match:

```mw
fn main() {
    for i in 1..=100 {
        match (i % 3, i % 5) {
            (0, 0) => println!("fizzbuzz"),
            (0, _) => println!("fizz"),
            (_, 0) => println!("buzz"),
            (_, _) => println!("{}", i),
        }
    }
}
```

Using an iterator and immutable data:

```mw
use std::borrow::Cow;

fn main() {
    (1..=100)
        .map(|n| match (n % 3, n % 5) {
            (0, 0) => "FizzBuzz".into(),
            (0, _) => "Fizz".into(),
            (_, 0) => "Buzz".into(),
            _ => Cow::from(n.to_string()),
        })
        .for_each(|n| println!("{:?}", n));
}
```

A folding iterator version, buffered with a single string allocation, by making use of expressions the `write!` macro.

```mw
use std::fmt::Write;

fn fizzbuzz() -> String {
    (1..=100).fold(String::new(), |mut output, x| {
        let fizz = if x % 3 == 0 { "fizz" } else { "" };
        let buzz = if x % 5 == 0 { "buzz" } else { "" };
        if fizz.len() + buzz.len() != 0 {
            output + fizz + buzz + "\n"
        } else {
            write!(&mut output, "{}", x).unwrap();
            output + "\n"
        }
    })
}

fn main() {
    println!("{}", fizzbuzz());
}
```

Or the ultimate optimized version with hardcoded output, no standard library or main function, and direct assembly syscalls to write to stdout.

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** No longer compiles using v1.95.0. A version using ARM assembly would also be useful. |
|---|

```mw
#![no_std]
#![feature(asm, lang_items, libc, no_std, start)]
 
extern crate libc;
 
const LEN: usize = 413;
static OUT: [u8; LEN] = *b"\
    1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n\
    16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n\
    31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n\
    46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n\
    61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n\
    76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n\
    91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n";
 
#[start]
fn start(_argc: isize, _argv: *const *const u8) -> isize {
    unsafe {
        asm!(
            "
            mov $$1, %rax
            mov $$1, %rdi
            mov $0, %rsi
            mov $1, %rdx
            syscall
            "
            :
            : "r" (&OUT[0]) "r" (LEN)
            : "rax", "rdi", "rsi", "rdx"
            :
        );
    }
    0
}
 
#[lang = "eh_personality"] extern fn eh_personality() {}
#[lang = "panic_fmt"] extern fn panic_fmt() {}
```


## Salmon

```mw
iterate (x; [1...100])
  ((x % 15 == 0) ? "FizzBuzz" :
   ((x % 3 == 0) ? "Fizz" :
    ((x % 5 == 0) ? "Buzz" : x)))!;
```

or

```mw
iterate (x; [1...100])
  {
    if (x % 15 == 0)
        "FizzBuzz"!
    else if (x % 3 == 0)
        "Fizz"!
    else if (x % 5 == 0)
        "Buzz"!
    else
        x!;
  };
```


## SAS

```mw
data _null_;
  do i=1 to 100;
    if mod(i,15)=0 then put "FizzBuzz";
    else if mod(i,5)=0 then put "Buzz";
    else if mod(i,3)=0 then put "Fizz";
    else put i;
  end;
run;
```


## Sather

```mw
class MAIN is
  main is
    loop i ::= 1.upto!(100);
      s:STR := "";
      if i % 3 = 0 then s := "Fizz"; end;
      if i % 5 = 0 then s := s + "Buzz"; end;
      if s.length > 0 then
        #OUT + s + "\n";
      else
        #OUT + i + "\n";
      end;      
    end;
  end;
end;
```


## Scala

Library:

Scala

### Idiomatic scala code

```mw
object FizzBuzz extends App {
  1 to 100 foreach { n =>
    println((n % 3, n % 5) match {
      case (0, 0) => "FizzBuzz"
      case (0, _) => "Fizz"
      case (_, 0) => "Buzz"
      case _ => n
    })
  }
}
```

### Geeky over-generalized solution ☺

```mw
def replaceMultiples(x: Int, rs: (Int, String)*): Either[Int, String] =
  rs map { case (n, s) => Either cond(x % n == 0, s, x)} reduceLeft ((a, b) => 
    a fold(_ => b, s => b fold(_ => a, t => Right(s + t))))

def fizzbuzz = replaceMultiples(_: Int, 3 -> "Fizz", 5 -> "Buzz") fold(_.toString, identity)

1 to 100 map fizzbuzz foreach println
```

### By a two-liners geek

```mw
def f(n: Int, div: Int, met: String, notMet: String): String = if (n % div == 0) met else notMet
for (i <- 1 to 100) println(f(i, 15, "FizzBuzz", f(i, 3, "Fizz", f(i, 5, "Buzz", i.toString))))
```

### One-liner geek

```mw
for (i <- 1 to 100) println(Seq(15 -> "FizzBuzz", 3 -> "Fizz", 5 -> "Buzz").find(i % _._1 == 0).map(_._2).getOrElse(i))
```

### Functional Scala

```mw
def fizzBuzzTerm(n: Int): String =
  if (n % 15 == 0) "FizzBuzz"
  else if (n % 3 == 0) "Fizz"
  else if (n % 5 == 0) "Buzz"
  else n.toString

def fizzBuzz(): Unit = LazyList.from(1).take(100).map(fizzBuzzTerm).foreach(println)
```

### Scala 3 (Dotty)

Written so as to introduce changes, with comments.

```mw
def fizzBuzzTerm(n: Int): String | Int = // union types
  (n % 3, n % 5) match // optional semantic indentation; no braces
    case (0, 0) => "FizzBuzz"
    case (0, _) => "Fizz"
    case (_, 0) => "Buzz"
    case _      => n // no need for `.toString`, thanks to union type
  end match // optional `end` keyword, with what it's ending
end fizzBuzzTerm // `end` also usable for identifiers

val fizzBuzz = // no namespace object is required; all top level
  LazyList.from(1).map(fizzBuzzTerm)

@main def run(): Unit = // @main for main method; can take custom args
  fizzBuzz.take(100).foreach(println)
```


## Scheme

```mw
(do ((i 1 (+ i 1)))
    ((> i 100))
    (display
      (cond ((= 0 (modulo i 15)) "FizzBuzz")
            ((= 0 (modulo i 3))  "Fizz")
            ((= 0 (modulo i 5))  "Buzz")
            (else                i)))
    (newline))
```

Using a recursive procedure.

```mw
(define (fizzbuzz x y)
  (println
    (cond (( = (modulo x 15) 0 ) "FizzBuzz")
          (( = (modulo x 3) 0 ) "Fizz")
          (( = (modulo x 5) 0 ) "Buzz")
          (else x)))

    (if (< x y) (fizzbuzz (+ x 1) y)))

(fizzbuzz 1 100)
```

Approach with maps and filters, easier to change, less readable than the previous.

```mw
(define (fizzbuzz x)
  (let ([words '((3 . "Fizz")
                 (5 . "Buzz"))])
    (define (fbm x)
      (let ([w (map cdr (filter (lambda (wo) (= 0 (modulo x (car wo)))) words))])
        (if (null? w) x (apply string-append w))))
    (for-each (cut format #t "~a~%" <>) (map fbm (iota x 1 1)))))

(fizzbuzz 15)
```


## Sed

```mw
#n
# doesn't work if there's no input
# initialize counters (0 = empty) and value
s/.*/  0/
: loop
# increment counters, set carry
s/^\(a*\) \(b*\) \([0-9][0-9]*\)/\1a \2b \3@/
# propagate carry
: carry
s/ @/ 1/
s/9@/@0/
s/8@/9/
s/7@/8/
s/6@/7/
s/5@/6/
s/4@/5/
s/3@/4/
s/2@/3/
s/1@/2/
s/0@/1/
/@/b carry
# save state
h
# handle factors
s/aaa/Fizz/
s/bbbbb/Buzz/
# strip value if any factor
/z/s/[0-9]//g
# strip counters and spaces
s/[ab ]//g
# output
p
# restore state
g
# roll over counters
s/aaa//
s/bbbbb//
# loop until value = 100
/100/q
b loop
```

Using seq:

```mw
seq 100 | sed '/.*[05]$/s//Buzz/;n;s//Buzz/;n;s//Buzz/;s/^[0-9]*/Fizz/'
```

### GNU sed

GNU sed has *first~step* address expression that matches every *step*th line. This makes following one-liners possible.

Using seq:

```mw
seq 100 | sed '0~3 s/.*/Fizz/; 0~5 s/[0-9]*$/Buzz/'
```

Using yes:

```mw
yes | sed -n '0~3s/y/Fizz/;0~5s/y*$/Buzz/;tx;=;b;:x;p;100q'
```

Using the option *-z (--zero-data)* first introduced in GNU sed 4.2.2 (2012-12-22):

```mw
sed -nz '0~3s/^/Fizz/;0~5s/$/Buzz/;tx;=;b;:x;p;100q' /dev/zero | sed 'y/\c@/\n/'
```

Second invocation of *sed* translates null characters to newlines. The same could be achieved with tr \\0 \\n


## Seed7

```mw
$ include "seed7_05.s7i";

const proc: main is func
  local
    var integer: number is 0;
  begin
    for number range 1 to 100 do
      if number rem 15 = 0 then
        writeln("FizzBuzz");
      elsif number rem 5 = 0 then
        writeln("Buzz");
      elsif number rem 3 = 0 then
        writeln("Fizz");
      else
        writeln(number);
      end if;
    end for;
  end func;
```


## SenseTalk

```mw
repeat 100
	put "" into output
	if the counter is a multiple of 3 then
		put "Fizz" after output
	end if
	if the counter is a multiple of 5 then
		put "Buzz" after output
	end if
	if output is empty then
		put the counter into output
	end if
	put output
end repeat
```


## SETL

```mw
program fizzbuzz;
    loop for n in [1..100] do
        print(fizzbuzz(n));
    end loop;

    proc fizzbuzz(n);
        divs := [[3, "Fizz"], [5, "Buzz"]];
        return +/[w : [d,w] in divs | n mod d=0] ? str n;
    end proc;
end program;
```


## SequenceL

```mw
import <Utilities/Conversion.sl>;
import <Utilities/Sequence.sl>;

main(args(2)) := 
	let
		result[i] := 
				"FizzBuzz" when i mod 3 = 0 and i mod 5 = 0
			else
				"Fizz" when i mod 3 = 0
			else
				"Buzz" when i mod 5 = 0
			else
				intToString(i)
			foreach i within 1 ... 100;
	in
		delimit(result, '\n');
```


## Shale

```mw
#!/usr/local/bin/shale

string library

r var
i var
i 1 =
{ i 100 <= } {
  r "" =
  i 3 % 0 == { r r "fizz" concat string::() = } ifthen
  i 5 % 0 == { r r "buzz" concat string::() = } ifthen
  r "" equals string::() { i } { r } if i "%3d: %p\n" printf
  i++
} while
```


## SheerPower 4GL

```mw
declare integer i%

for i% = 1 to 100
  if i% mod 15 = 0 then
    print 'FizzBuzz'
  elseif i% mod 3 = 0 then
    print 'Fizz'
  elseif i% mod 5 = 0 then
    print 'Buzz'
  else
    print i%
  end if
next i%
```


## Shen

```mw
(define fizzbuzz
  101 -> (nl)
  N -> (let divisible-by? (/. A B (integer? (/ A B)))
         (cases (divisible-by? N 15) (do (output "Fizzbuzz!~%")
                                         (fizzbuzz (+ N 1)))
                (divisible-by? N 3) (do (output "Fizz!~%")
                                        (fizzbuzz (+ N 1)))
                (divisible-by? N 5) (do (output "Buzz!~%")
                                        (fizzbuzz (+ N 1)))
                true (do (output (str N)) 
                         (nl)
                         (fizzbuzz (+ N 1))))))

(fizzbuzz 1)
```

### Alternative showing off other features like prolog integration and guards

```mw
(defprolog fizz
  0 <-- (is _ (output "Fizz"));
  N <-- (when (> N 0)) (is N1 (- N 3)) (fizz N1);
)

(defprolog buzz
  0 <-- (is _ (output "Buzz"));
  N <-- (when (> N 0)) (is N1 (- N 5)) (buzz N1);
)

(define none
  [] -> true
  [true | _] -> false
  [_ | B] -> (none B)
)

(define fizzbuzz
  N M -> (nl) where (> N M)
  N M -> (do
    (if (none [(prolog? (receive N) (fizz N)) (prolog? (receive N) (buzz N))])
      (output (str N))
      (output "!")
    )
    (nl)
    (fizzbuzz (+ N 1) M)
  )
)

(fizzbuzz 1 100)
```


## Sidef

Structured:

```mw
{ |i|
    if (i %% 3) {
        print "Fizz"
        i %% 5 && print "Buzz"
        print "\n"
    }
    elsif (i %% 5) { say "Buzz" }
    else  { say i }
} << 1..100
```

Declarative:

```mw
func fizzbuzz({ _ %% 15 }) { "FizzBuzz" }
func fizzbuzz({ _ %%  5 }) {     "Buzz" }
func fizzbuzz({ _ %%  3 }) {     "Fizz" }
func fizzbuzz(        n  ) {          n }

for n in (1..100) { say fizzbuzz(n) }
```

One-liner:

```mw
{>"#{<Fizz>[.%3]}#{<Buzz>[.%5]}"||_}<<1..100
```


## Simula

```mw
begin
    integer i;
    for i := 1 step 1 until 100 do
    begin
        boolean fizzed;
        fizzed := 0 = mod(i, 3);
        if fizzed then
            outtext("Fizz");
        if mod(i, 5) = 0 then
            outtext("Buzz")
        else if not fizzed then
            outint(i, 3);
        outimage
    end;
end
```


## SkookumScript

Answer by printing out one of the 4 alternatives:

```mw
1.to 100
  [
  println(
    if idx.mod(15) = 0 ["FizzBuzz"]
      idx.mod(3) = 0 ["Fizz"]
      idx.mod(5) = 0 ["Buzz"]
      else [idx])
  ]
```

Answer by building up a string:

```mw
1.to 100
  [
  !str: ""
  if idx.mod(3) = 0 [str += "Fizz"]
  if idx.mod(5) = 0 [str += "Buzz"]
  println(if str.empty? [idx] else [str])
  ]
```

Or doing initial bind in one step:

```mw
1.to 100
  [
  !str: if idx.mod(3) = 0 ["Fizz"] else [""]
  if idx.mod(5) = 0 [str += "Buzz"]
  println(if str.empty? [idx] else [str])
  ]
```


## Slate

```mw
n@(Integer traits) fizzbuzz
[
  output ::= ((n \\ 3) isZero ifTrue: ['Fizz'] ifFalse: ['']) ; ((n \\ 5) isZero ifTrue: ['Buzz'] ifFalse: ['']).
  output isEmpty ifTrue: [n printString] ifFalse: [output]
].
1 to: 100 do: [| :i | inform: i fizzbuzz]
```


## Slope

```mw
(define fizz-buzz
  (lambda (x) 
      (define ret "") 
      (if (zero? (% x 3))(set! ret (append ret "fizz")))
      (if (zero? (% x 5))(set! ret (append ret "buzz")))
      (if (equal? ret "") (set! ret (append ret x)))
      ret))
(apply display-lines (list-join (map fizz-buzz (range 100 1))))
```


## Small

See FizzBuzz/EsoLang


## SmallBASIC

See FizzBuzz/Basic


## Smalltalk

Since only GNU Smalltalk supports file-based programming, we'll be using its syntax.

```mw
Integer extend [
    fizzbuzz [
        | fb |
        fb := '%<Fizz|>1%<Buzz|>2' % {
            self \\ 3 == 0.  self \\ 5 == 0 }.
        ^fb isEmpty ifTrue: [ self ] ifFalse: [ fb ]
    ]
]
1 to: 100 do: [ :i | i fizzbuzz displayNl ]
```

A Squeak/Pharo example using the Transcript window:

```mw
(1 to: 100) do:
	[:n | 
		((n \\ 3)*(n \\ 5)) isZero 
                        ifFalse: [Transcript show: n].
		(n \\ 3) isZero
			ifTrue: [Transcript show: 'Fizz'].
		(n \\ 5) isZero
			ifTrue: [Transcript show: 'Buzz'].
		Transcript cr.]
```

The Squeak/Pharo examples below present possibilities using the powerful classes available. In this example, the dictionary can have as keys pairs of booleans and in the interaction the several boolean patterns select the string to be printed or if the pattern is not found the number itself is printed.

```mw
fizzbuzz := Dictionary with: #(true true)->'FizzBuzz' 
                       with: #(true false)->'Fizz' 
                       with: #(false true)->'Buzz'.

1 to: 100 do: 
	[ :i | Transcript show: 
               (fizzbuzz at: {i isDivisibleBy: 3. i isDivisibleBy: 5} 
		         ifAbsent: [ i ]); cr]
```

Yet another approach with Squeak/Pharo Smalltalk:

```mw
0 to: 100 do: [ :i |
    (i \\ 3 = 0 and: [ i \\ 5 = 0 ])
        ifTrue: [ Transcript show: 'FizzBuzz'; cr. ]
        ifFalse: [
            (i \\ 3 = 0)
                ifTrue: [ Transcript show: 'Fizz'; cr. ].
            (i \\ 5 = 0)
                ifTrue: [ Transcript show: 'Buzz'; cr. ].
            ((i \\ 3 ~= 0) and: [ i \\ 5 ~= 0 ])
                ifTrue: [ Transcript show: i printString; cr. ].
        ].
].
```

Smalltalk does not have a case-select construct, but a similar effect can be attained using a collection and the #includes: method:

```mw
1 to: 100 do: [:n | |r| 
	r := n rem: 15.
	Transcript show: (r isZero 
	   ifTrue:['fizzbuzz'] 
	   ifFalse: [(#(3 6 9 12) includes: r) 
		ifTrue:['fizz'] 
		ifFalse:[((#(5 10) includes: r)) 
			ifTrue:['buzz'] 
			ifFalse:[n]]]); 
	cr].
```

If the construction of the whole collection is done beforehand, Smalltalk provides a straightforward way of doing because collections can be heterogeneous (may contain any object):

```mw
fbz := (1 to: 100) asOrderedCollection.
 3 to: 100 by:  3 do: [:i | fbz at: i put: 'Fizz'].
 5 to: 100 by:  5 do: [:i | fbz at: i put: 'Buzz'].
15 to: 100 by: 15 do: [:i | fbz at: i put: 'FizzBuzz'].
fbz do: [:i | Transcript show: i; cr].
```

The approach building a dynamic string can be done as well:

```mw
1 to: 100 do: [:i | |fb s| 
	fb := {i isDivisibleBy: 3. i isDivisibleBy: 5. nil}. 
	fb at: 3 put: (fb first | fb second) not. 
	s := '<1?Fizz:><2?Buzz:><3?{1}:>' format: {i printString}. 
	Transcript show: (s expandMacrosWithArguments: fb); cr].
```


## SNOBOL4

Merely posting a solution by Daniel Lyons

```mw
        I = 1
LOOP    FIZZBUZZ = ""
        EQ(REMDR(I, 3), 0)              :F(TRY_5)
        FIZZBUZZ = FIZZBUZZ "FIZZ"
TRY_5   EQ(REMDR(I, 5), 0)              :F(DO_NUM)
        FIZZBUZZ = FIZZBUZZ "BUZZ"      
DO_NUM  IDENT(FIZZBUZZ, "")             :F(SHOW)
        FIZZBUZZ = I
SHOW    OUTPUT = FIZZBUZZ
        I = I + 1
        LE(I, 100)                      :S(LOOP)
END
```


## SNUSP

See FizzBuzz/EsoLang


## SparForte

As a structured script.

```mw
#!/usr/local/bin/spar
pragma annotate( summary, "fizzbuzz" );
pragma annotate( description, "Write a program that prints the numbers from 1 to 100. But for multiples of" );
pragma annotate( description, "three print 'Fizz' instead of the number and for the multiples of five print" );
pragma annotate( description, "'Buzz'. For numbers which are multiples of both three and five print" );
pragma annotate( description, "'FizzBuzz'" );
pragma annotate( see_also, "http://rosettacode.org/wiki/FizzBuzz" );
pragma annotate( author, "Ken O. Burtch" );
pragma license( unrestricted );

pragma restriction( no_external_commands );

procedure fizzbuzz is
begin
   for i in 1..100 loop
      if i mod 15 = 0 then
         ? "FizzBuzz";
      elsif i mod 5 = 0 then
         ? "Buzz";
      elsif i mod 3 = 0 then
         ? "Fizz";
      else
         ? i;
      end if;
   end loop;
end fizzbuzz;
```


## SQL

Library:

SQL

### Oracle SQL

```mw
SELECT CASE
    WHEN MOD(level,15)=0 THEN 'FizzBuzz'
    WHEN MOD(level,3)=0 THEN 'Fizz'
    WHEN MOD(level,5)=0 THEN 'Buzz'
    ELSE TO_CHAR(level)
    END FizzBuzz
    FROM dual
    CONNECT BY LEVEL <= 100;
```

Or using Oracle's DECODE and NVL:

```mw
SELECT nvl(decode(MOD(level,3),0,'Fizz')||decode(MOD(level,5),0,'Buzz'),level)
FROM dual
CONNECT BY level<=100;
```

### PostgreSQL specific

```mw
SELECT i, fizzbuzz 
  FROM 
    (SELECT i, 
            CASE 
              WHEN i % 15 = 0 THEN 'FizzBuzz' 
              WHEN i %  5 = 0 THEN 'Buzz' 
              WHEN i %  3 = 0 THEN 'Fizz' 
              ELSE NULL 
            END AS fizzbuzz 
       FROM generate_series(1,100) AS i) AS fb 
 WHERE fizzbuzz IS NOT NULL;
```

Using Generate_Series and tables only:

```mw
SELECT COALESCE(FIZZ || BUZZ, FIZZ, BUZZ, OUTPUT) AS FIZZBUZZ FROM
(SELECT GENERATE_SERIES AS FULL_SERIES, TO_CHAR(GENERATE_SERIES,'99') AS OUTPUT 
FROM GENERATE_SERIES(1,100)) F LEFT JOIN 
(SELECT TEXT 'Fizz' AS FIZZ, GENERATE_SERIES AS FIZZ_SERIES FROM GENERATE_SERIES(0,100,3)) FIZZ ON
FIZZ.FIZZ_SERIES = F.FULL_SERIES LEFT JOIN
(SELECT TEXT 'Buzz' AS BUZZ, GENERATE_SERIES AS BUZZ_SERIES FROM GENERATE_SERIES(0,100,5)) BUZZ ON
BUZZ.BUZZ_SERIES = F.FULL_SERIES;
```

### Recursive Common Table Expressions (MSSQL 2005+)

```mw
WITH nums (n, fizzbuzz ) AS (
	SELECT 1, CONVERT(nvarchar, 1) UNION ALL
	SELECT
		(n + 1) as n1, 
		CASE
			WHEN (n + 1) % 15 = 0 THEN 'FizzBuzz'
			WHEN (n + 1) % 3  = 0 THEN 'Fizz'
			WHEN (n + 1) % 5  = 0 THEN 'Buzz'
			ELSE CONVERT(nvarchar, (n + 1))
		END
	FROM nums WHERE n < 100
)
SELECT n, fizzbuzz FROM nums
ORDER BY n ASC
OPTION ( MAXRECURSION 100 )
```

### SQL Anywhere specific - minimalist

```mw
SELECT 
        isnull(if row_num % 3 = 0 then 'Fizz' endif + if row_num % 5 = 0 then 'Buzz' endif, str(row_num)) 
FROM 
        sa_rowgenerator(1,100)
```

### Generic SQL using a join

This should work in most RDBMSs, but you may need to change MOD(i,divisor) to i % divisor.

```mw
-- Load some numbers
CREATE TABLE numbers(i INTEGER);
INSERT INTO numbers VALUES(1);
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
INSERT INTO numbers SELECT i + (SELECT MAX(i) FROM numbers) FROM numbers;
-- Define the fizzes and buzzes
CREATE TABLE fizzbuzz (message VARCHAR(8), divisor INTEGER);
INSERT INTO fizzbuzz VALUES('fizz',      3);
INSERT INTO fizzbuzz VALUES('buzz',      5);
INSERT INTO fizzbuzz VALUES('fizzbuzz', 15);
-- Play fizzbuzz
SELECT COALESCE(max(message),CAST(i AS VARCHAR(99))) as result
FROM numbers LEFT OUTER JOIN fizzbuzz ON MOD(i,divisor) = 0
GROUP BY i
HAVING i <= 100
ORDER BY i;
-- Tidy up
DROP TABLE fizzbuzz;
DROP TABLE numbers;
```


## Squirrel

```mw
function Fizzbuzz(n) {
    for (local i = 1; i <= n; i += 1) {
        if (i % 15 == 0)
            print ("FizzBuzz\n")
        else if (i % 5 == 0)
            print ("Buzz\n")
        else if (i % 3 == 0)
            print ("Fizz\n")
        else {
            print (i + "\n")
        }
    }
}
Fizzbuzz(100);
```


## Stata

```mw
program define fizzbuzz
	args n
	forvalues i = 1/`n' {
		if mod(`i',15) == 0 {
			display "FizzBuzz"
		}
		else if mod(`i',5) == 0 {
			display "Buzz"
		}
		else if mod(`i',3) == 0 {
			display "Fizz"
		}
		else {
			display `i'
		}
	}
end
```


## Stax

```
100R{3%!"Fizz"*_5%!"Buzz"*+c_?P}F
```

Golfed:

```
AJm3%!`M"(`*_5%!`-C`*+c_?
```


## Swahili

```mw
shughuli fizzBuzz() {
  kwa i = 1 mpaka 100 {
    kama (i % 15 == 0) {
      andika("FizzBuzz")
    } au (i % 5 == 0) {
      andika("Buzz")
    } au (i % 3 == 0) {
      andika("Fizz")
    } sivyo {
      andika(i)
    }
  }
}
```


## Swift

### using a switch statement

```mw
for i in 1...100 {
    switch (i % 3, i % 5) {
    case (0, 0):
        print("FizzBuzz")
    case (0, _):
        print("Fizz")
    case (_, 0):
        print("Buzz")
    default:
        print(i)
    }
}
```

### using two if statements and an Optional

```mw
for i in 1...100{
    var s:String?
    if i%3==0{s="Fizz"}
    if i%5==0{s=(s ?? "")+"Buzz"}
    print(s ?? i)
}
```

### using a precomputed cycle

```mw
import Foundation

let formats: [String] = [
  "%d",
  "%d",
  "fizz",
  "%d",
  "buzz",
  "fizz",
  "%d",
  "%d",
  "fizz",
  "buzz",
  "%d",
  "fizz",
  "%d",
  "%d",
  "fizzbuzz",
]

var count = 0
var index = 0
while count < 100 {
  count += 1
  print(String(format: formats[index], count))
  index += 1
  index %= 15
}
```


## Symsyn

```mw
| FizzBuzz

 1 I
 if I LE 100
    mod I 3 X
    mod I 5 Y
    if X EQ 0
       'FIZZ' $S
       if Y EQ 0
          + 'BUZZ' $S 
       endif
    else
       if Y EQ 0
          'BUZZ' $S
       else
          ~ I $S
       endif
    endif
    $S []
    + I
    goif
 endif
```
