---
title: "FizzBuzz (part 5/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/7
---

## NetRexx

```mw
loop j=1 for 100
  select
    when j//15==0 then say 'FizzBuzz'
    when j//5==0  then say 'Buzz'
    when j//3==0  then say 'Fizz'
    otherwise say j.right(4)
  end
end
```


## Never

```mw
func fizz_buzz() -> int
{
    var i = 1;

    for (i = 1; i <= 100; i = i + 1)
    {
        /* if (i % 15 == 0) */
        if (i % 3 == 0 && i % 5 == 0)
        {
            prints("Fizz Buzz\n")
        }
        else if (i % 3 == 0)
        {
            prints("Fizz\n")
        }
        else if (i % 5 == 0)
        {
            prints("Buzz\n")
        }
        else
        {
            prints(i + "\n")
        }
    };

    0
}

func main() -> int {
    fizz_buzz();

    0
}
```

**Output:**

```
prompt$ never -f fizzbuzz.nev 2>/dev/null
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
Fizz Buzz
16
...
89
Fizz Buzz
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


## NewLISP

```mw
(dotimes (i 100)
  (println
   (cond
    ((= 0 (% i 15)) "FizzBuzz")
    ((= 0 (% i 3)) "Fizz")
    ((= 0 (% i 5)) "Buzz")
    ('t i))))
```

Solution 2.

Many of the solutions have a command to print "fizzbuzz". Since the programs can print "fizz" and "buzz", why not print "fizz" followed immediately by "buzz"? This also removes the need to check for divisibility by 15.

It would be nice to have a very easy way to know whether a word was actually printed (because we otherwise have to print the number). I mean a way that doesn't involve checking for divisibility again or setting a flag.

We want a macro or function that is somewhat like "or" but that evaluates all of the expressions even if the first yields true. Like "or", it returns a true value (a number) if any of the expressions yielded true. In newLISP, it seems that a function suffices, but in some languages a macro may be necessary because the arguments to a function are not always evaluated from left to right.

I believe that this method makes it easier to modify the program when the list of words to be printed is extended.

```mw
(define (try-all) ;; The arguments are in (args) or $args.
  (let (cnt (length (filter true? $args)))
    (if (zero? cnt) nil cnt)))

(define (fizz)
  (define (say? n s) (if (= 0 (% i n)) (print s))) ;; Dynamic scoping.
  (for (i 1 21)
    (unless
      (try-all
        (say? 3 'fizz)
        (say? 5 'buzz)
        (say? 7 'boom)
        (say? 11 'crux))
      (print i))
    (println)))

(fizz)

1
2
fizz
4
buzz
fizz
boom
8
fizz
buzz
crux
fizz
13
boom
fizzbuzz
16
17
fizz
19
buzz
fizzboom
```

Solution 3.

Instead of explicitly including the numbers 3, 5, 7, etc., let's tell the computer to use the prime numbers starting with 3.

```mw
(define (m-prime-gen)
  (fn ( , n)  ;; Unused parameter n is our local variable.
    ;; Self-modifying code.
    (until (= 1 (length (factor (setf n (++ 2))))))
    n))

(define (try-all) ;; The arguments are in (args) or $args.
  (let (cnt (length (filter true? $args)))
    (if (zero? cnt) nil cnt)))

(define (fizz)
  (define (say? n s) (if (= 0 (% i n)) (print s))) ;; Dynamic scoping.
  (for (i 1 21)
    (let (p (m-prime-gen))
      (unless
        (try-all
          (say? (p) 'fizz)
          (say? (p) 'buzz)
          (say? (p) 'boom)
          (say? (p) 'crux)
          (say? (p) 'ZAP))
        (print i))
      (println))))

(fizz)

1
2
fizz
4
buzz
fizz
boom
8
fizz
buzz
crux
fizz
ZAP
boom
fizzbuzz
16
17
fizz
19
buzz
fizzboom
```


## NewtonScript

```mw
for i := 1 to 100 do
begin
	if i mod 15 = 0 then
		print("FizzBuzz")
	else if i mod 3 = 0 then
		print("Fizz")
	else if i mod 5 = 0 then
		print("Buzz")
	else
		print(i);
	print("\n")
end
```


## Nickle

```mw
/* Fizzbuzz in nickle */

void function fizzbuzz(size) {
    for (int i = 1; i < size; i++) {
        if (i % 15 == 0) { printf("Fizzbuzz\n"); }
        else if (i % 5 == 0) { printf("Buzz\n"); }
        else if (i % 3 == 0) { printf("Fizz\n"); }
        else { printf("%i\n", i); }
    }
}

fizzbuzz(1000);
```


## Nim

Translation of

:

Python

```mw
for i in 1..100:
  if i mod 15 == 0:
    echo("FizzBuzz")
  elif i mod 3 == 0:
    echo("Fizz")
  elif i mod 5 == 0:
    echo("Buzz")
  else:
    echo(i)
```

### Without Modulus

```mw
var messages = @["", "Fizz", "Buzz", "FizzBuzz"]
var acc = 810092048
for i in 1..100:
  var c = acc and 3
  echo(if c == 0: $i else: messages[c])
  acc = acc shr 2 or c shl 28
```

### Using macro

Computes everything at compile time.

```mw
import macros
macro FizzBuzz(N): untyped =
  var source = ""
  for i in 1..N.intVal:
    source &= "echo \""
    if i mod 15 == 0:
      source &= "FizzBuzz"
    elif i mod 3 == 0:
      source &= "Fizz"
    elif i mod 5 == 0:
      source &= "Buzz"
    else:
      source &= $i
    source &= "\"\n"
  result = parseStmt(source)

FizzBuzz(100)
```


## Nix

```mw
with (import <nixpkgs> { }).lib;
with builtins;
let
  fizzbuzz = { x ? 1 }:
    ''
      ${if (mod x 15 == 0) then
        "FizzBuzz"
      else if (mod x 3 == 0) then
        "Fizz"
      else if (mod x 5 == 0) then
        "Buzz"
      else
        (toString x)}
    '' + (if (x < 100) then
      fizzbuzz { x = x + 1; } else "");
in
fizzbuzz { }
```


## Nu

Determine and match:

```mw
1..100 | each {
  { x: $in, mod3: ($in mod 3), mod5: ($in mod 5), }
  | match $in {
    { mod3: 0, mod5: 0, } => 'FizzBuz',
    { mod3: 0, mod5: _, } => 'Fizz',
    { mod3: _, mod5: 0, } => 'Buzz',
                        _ => $in.x
  }
} | str join "\n"
```

if else if:

```mw
1..100 | each {
  if $in mod 15 == 0 {'FizzBuzz'} else if $in mod 3 == 0 {'Fizz'} else if $in mod 5 == 0 {'Buzz'} else {$in}
} | str join "\n"
```

```mw
1..100 | each {(
  if $in mod 15 == 0 {'FizzBuzz'}
  else if $in mod 3 == 0 {'Fizz'}
  else if $in mod 5 == 0 {'Buzz'}
  else {$in}
)} | str join "\n"
```

string construction and fixup:

```mw
(1..100
| each {|i| $"(if $i mod 3 == 0 {"Fizz"})(if $i mod 5 == 0 {"Buzz"})"
| if ($in == "") {$i} else {$in}}
| str join "\n")
```


## Oberon-2

```mw
MODULE FizzBuzz;

   IMPORT Out;

   VAR i: INTEGER;

BEGIN
   FOR i := 1 TO 100 DO 
      IF i MOD 15 = 0 THEN 
         Out.String("FizzBuzz")
      ELSIF i MOD 5 = 0 THEN
         Out.String("Buzz")
      ELSIF i MOD 3 = 0 THEN 
         Out.String("Fizz")
      ELSE 
         Out.Int(i,0)
      END;
      Out.Ln
   END
END FizzBuzz.
```


## Objeck

```mw
bundle Default {
  class Fizz {
    function : Main(args : String[]) ~ Nil {
      for(i := 0; i <= 100; i += 1;) {
        if(i % 15 = 0) {
          "FizzBuzz"->PrintLine();
        }
        else if(i % 3 = 0) {
          "Fizz"->PrintLine();
        }  
        else if(i % 5 = 0) {
          "Buzz"->PrintLine();
        }
        else {
          i->PrintLine();
        };
      };
    }
  }
}
```


## Objective-C

```mw
// FizzBuzz in Objective-C
#import <Foundation/Foundation.h>

int main(int argc, char* argv[]) {
	for (NSInteger i=1; I <= 101; i++) {
		if (i % 15 == 0) {
		    NSLog(@"FizzBuzz\n");
		} else if (i % 3 == 0) {
		    NSLog(@"Fizz\n");
		} else if (i % 5 == 0) {
		    NSLog(@"Buzz\n");
		} else {
		    NSLog(@"%li\n", i);
		}
	}
}
```


## OCaml

Idiomatic OCaml to solve the stated problem:

```mw
let fizzbuzz i =
  match i mod 3, i mod 5 with
    0, 0 -> "FizzBuzz"
  | 0, _ -> "Fizz"
  | _, 0 -> "Buzz"
  | _    -> string_of_int i
 
let _ =
  for i = 1 to 100 do print_endline (fizzbuzz i) done
```

With a view toward extensibility, there are many approaches: monadic, list of rules, ... here we'll use a piped sequence of rules to define a new "fizzbuzz" function:

```mw
(* Useful rule declaration: "cond => f", 'cond'itionally applies 'f' to 'a'ccumulated value *)
let (=>) cond f a = if cond then f a else a
let append s a = a^s

let fizzbuzz i =
  "" |> (i mod 3 = 0 => append "Fizz")
     |> (i mod 5 = 0 => append "Buzz")
     |> (function "" -> string_of_int i
                | s  -> s)
```


## Octave

```mw
for i = 1:100
  if ( mod(i,15) == 0 )
    disp("FizzBuzz");
  elseif ( mod(i, 3) == 0 )
    disp("Fizz")
  elseif ( mod(i, 5) == 0 )
    disp("Buzz")
  else
    disp(i)
  endif
endfor
```


## Oforth

```mw
: fizzbuzz
| i |
   100 loop: i [
      null 
      i 3 mod ifZero: [ "Fizz" + ]
      i 5 mod ifZero: [ "Buzz" + ]
      dup ifNull: [ drop i ] . 
      ] ;
```


## Ol

```mw
(for-each (lambda (x)
      (print (cond
         ((and (zero? (mod x 3)) (zero? (mod x 5)))
            "FizzBuzz")
         ((zero? (mod x 3))
            "Fizz")
         ((zero? (mod x 5))
            "Buzz")
         (else
            x))))
   (iota 100))
```


## Onyx (wasm)

```mw
use core { * }

fizzbuzz :: (len: u32) -> void {
    for i in 1..len+1 {
        msg : str;
        if (i%3 == 0 && i%5 == 0) { msg = "FizzBuzz !!!"; }
        elseif (i%3 == 0) { msg = "Fizz"; }
        elseif (i%5 == 0) { msg = "Buzz"; }
        else { msg = tprintf("{}", i); }
        printf("{}\n", msg);
    }
}

main :: () {
    fizzbuzz(100);
}
```


## OOC

```mw
fizz: func (n: Int) -> Bool {
  if(n % 3 == 0) {
    printf("Fizz")
    return true
  }
  return false
}

buzz: func (n: Int) -> Bool {
  if(n % 5 == 0) {
    printf("Buzz")
    return true
  }
  return false
}

main: func {
  for(n in 1..100) {
    fizz:= fizz(n)
    buzz:= buzz(n)
    fizz || buzz || printf("%d", n)
    println()
  }
}
```


## Order

```mw
#include <order/interpreter.h>

// Get FB for one number
#define ORDER_PP_DEF_8fizzbuzz ORDER_PP_FN(            \
8fn(8N,                                                \
    8let((8F, 8fn(8N, 8G,                              \
                  8is_0(8remainder(8N, 8G)))),         \
         8cond((8ap(8F, 8N, 15), 8quote(fizzbuzz))     \
               (8ap(8F, 8N, 3), 8quote(fizz))          \
               (8ap(8F, 8N, 5), 8quote(buzz))          \
               (8else, 8N)))) )

// Print E followed by a comma (composable, 8print is not a function)
#define ORDER_PP_DEF_8print_el ORDER_PP_FN( \
8fn(8E, 8print(8E 8comma)) )

ORDER_PP(  // foreach instead of map, to print but return nothing
  8seq_for_each(8compose(8print_el, 8fizzbuzz), 8seq_iota(1, 100))
)
```


## PureBasic

See FizzBuzz/Basic


## OxygenBasic

```mw
declare
  fun {FizzBuzz X}
     if     X mod 15 == 0 then 'FizzBuzz'
     elseif X mod  3 == 0 then 'Fizz'
     elseif X mod  5 == 0 then 'Buzz'
     else                      X
     end
  end
in
  for I in 1..100 do
     {Show {FizzBuzz I}}
  end
```


## Palo Alto Tiny BASIC

See FizzBuzz/Basic.


## PARI/GP

```mw
{for(n=1,100,
  print(if(n%3,
    if(n%5,
      n
    ,
      "Buzz"
    )
  ,
    if(n%5,
      "Fizz"
    ,
      "FizzBuzz"
    )
  ))
)}
```


## Pascal

### Pascal-P

Works with

:

Pascal-P

version P4

```mw
program fizzbuzz(output);
var
  i: integer;
begin
  for i := 1 to 100 do
    if i mod 15 = 0 then
      writeln('FizzBuzz')
    else if i mod 3 = 0 then
      writeln('Fizz')
    else if i mod 5 = 0 then
      writeln('Buzz')
    else
      writeln(i)
end.
```

### PascalABC.NET

```mw
begin
  for var i:=1 to 100 do
    if i mod 15 = 0 then
      Print('FizzBuzz')
    else if i mod 3 = 0 then
      Print('Fizz')   
    else if i mod 5 = 0 then
      Print('Buzz')   
    else Print(i)   
end.
```


## PDP-8 Assembly

Works with

:

PAL-D

Runs on SimH, or any PDP-8 with an EAE

```mw
/--------------------------------------------------------
/THIS PROGRAM PRINTS THE INTEGERS FROM 1 TO 100 (INCL).
/WITH THE FOLLOWING RESTRICTIONS:
/  FOR MULTIPLES OF THREE, PRINT 'FIZZ'
/  FOR MULTIPLES OF FIVE,  PRINT 'BUZZ'
/  FOR MULTIPLES OF BOTH THREE AND FIVE, PRINT 'FIZZBUZZ'
/--------------------------------------------------------

/--------------------------------------------------------
/DEFINES
/--------------------------------------------------------
SWBA=7447               /EAE MODE A INSTRUCTION
DVI=7407                /EAE DIVIDE INSTRUCTION
AIX0=0010               /AUTO INDEX REGISTER 0
CR=0215                 /CARRIAGE RETURN
LF=0212                 /LINEFEED
EOT=0000                /END OF TEXT NUL
FIZMOD=0003             /CONSTANT DECIMAL 3 (FIZZ)
BUZMOD=0005             /CONSTANT DECIMAL 5 (BUZZ)
K10=0012                /CONSTANT DECIMAL 10

LAST=0144               /FIZZBUZZ THE NUMBERS 1..LAST
                        /0144 OCTAL == 100 DECIMAL
                        /CAN BE ANY FROM [0001...7777]

/--------------------------------------------------------
/FIZZBUZZ START=0200
/--------------------------------------------------------
        *200            /START IN MEMORY AT 0200 OCTAL
FZZBZZ, CLA             /CLEAR AC
        TAD (-LAST-1    /LOAD CONSTANT -(LAST+1)
        DCA CNTR        /SET UP MAIN COUNTER
        TAD (-FIZMOD    /SET UP FIZZ COUNTER
        DCA FIZCTR      /TO -3
        TAD (-BUZMOD    /SET UP BUZZ COUNTER
        DCA BUZCTR      /TO -5
LOOP,   ISZ CNTR        /READY?
        SKP             /NO: CONTINUE
        JMP I [7600     /YES: RETURN TO OS/8, REPLACE BY
                        /'HLT' IF NOT ON OS/8
CHKFIZ, ISZ FIZCTR      /MULTIPLE OF 3?
        JMP CHKBUZ      /NO: CONTINUE
        TAD FIZSTR      /YES: LOAD ADDRESS OF 'FIZZ'
        JMS STROUT      /PRINT IT TO TTY
        TAD (-FIZMOD    /RELOAD THE
        DCA FIZCTR      /MOD 3 COUNTER
CHKBUZ, ISZ BUZCTR      /MULTIPLE OF 5?
        JMP CHKNUM      /NO: CONTINUE
        TAD BUZSTR      /YES: LOAD ADDRESS OF 'BUZZ'
        JMS STROUT      /PRINT IT TO TTY
        TAD (-BUZMOD    /RELOAD THE
        DCA BUZCTR      /MOD 5 COUNTER
        JMP NXTLIN      /PRINT NEWLINE AND CONTINUE
CHKNUM, TAD FIZCTR      /CHECK WHETHER MOD 3 COUNTER
        TAD (FIZMOD     /IS RELOADED
        SNA             /DID WE JUST PRINT 'FIZZ'?
        JMP NXTLIN      /YES: PRINT NEWLINE AND CONTINUE
        CLA             /ZERO THE AC
NUM,    TAD CNTR        /LOAD THE MAIN NUMBER COUNTER
        TAD (LAST+1     /OFFSET IT TO A POSITIVE VALUE
        JMS NUMOUT      /PRINT IT TO THE TTY
NXTLIN, TAD LINSTR      /LOAD THE ADDRESS OF THE NEWLINE
        JMS STROUT      /PRINT IT TO TTY
        JMP LOOP        /CONTINUE WITH THE NEXT NUMBER
CNTR,   0               /MAIN COUNTER
FIZCTR, 0               /FIZZ COUNTER
BUZCTR, 0               /BUZZ COUNTER

/--------------------------------------------------------
/WRITE ASCII CHARACTER IN AC TO TTY
/PRE : AC=ASCII CHARACTER
/POST: AC=0
/--------------------------------------------------------
CHROUT, .-.
        TLS             /SEND CHARACTER TO TTY
        TSF             /IS TTY READY FOR NEXT CHARACTER?
        JMP .-1         /NO TRY AGAIN
        CLA             /AC=0
        JMP I CHROUT    /RETURN

/--------------------------------------------------------
/WRITE NUL TERMINATED ASCII STRING TO TTY
/PRE : AC=ADDRESS OF STRING MINUS 1
/POST: AC=0
/--------------------------------------------------------
STROUT, .-.
        DCA AIX0        /STORE POINTER IN AUTO INDEX 0
STRLOP, TAD I AIX0      /GET NEXT CHARACTER FROM STRING
        SNA             /SKIP IF NOT EOT
        JMP I STROUT    /RETURN
        JMS CHROUT      /PRINT CHARACTER
        JMP STRLOP      /GO GET NEXT CHARACTER

/--------------------------------------------------------
/WRITE NUMBER IN AC TO TTY AS DECIMAL
/PRE : AC=UNSIGNED NUMBER BETWEEN 0000 AND 7777
/POST: AC=0
/--------------------------------------------------------
NUMOUT, .-.
        SWBA            /SET EAE IN MODE A
        MQL             /MQ=NUM; AC=0
        TAD BUFFER      /LOAD END OF BUFFER
        DCA BUFPTR      /IN BUFPTR
        SKP             /NUM IS ALREADY IN MQ
NUMLOP, MQL             /MQ=NUM; AC=0
        DVI             /MQ=NUM/10; AC=NUM-(NUM/10)*10
        K10             /DECIMAL 10
        TAD ("0         /ADD ASCII ZERO
        DCA I BUFPTR    /STORE CHAR BUFFER, BACK TO FRONT
        CMA             /AC=-1
        TAD BUFPTR      /DECREMENT
        DCA BUFPTR      /BUFFER POINTER
        MQA             /MQ -> AC
        SZA             /READY IF ZERO
        JMP NUMLOP      /GET NEXT DIGIT
        TAD BUFPTR      /LOAD START OF CONVERTED NUMBER
        JMS STROUT      /SEND IT TO TTY
        JMP I NUMOUT    /RETURN
BUFFER, .+4             /ADDRESS OF BUFFER
        *.+4            /RESERVE 4 LOCATIONS (MAX=4095)
        EOT             /END OF BUFFER
BUFPTR, 0               /POINTER IN BUFFER

/--------------------------------------------------------
/STRINGS
/--------------------------------------------------------
FIZSTR, .               /FIZZ STRING
        "F; "I; "Z; "Z; EOT
BUZSTR, .               /BUZZ STRING
        "B; "U; "Z; "Z; EOT
LINSTR, .               /NEWLINE STIRNG
        CR; LF; EOT
        $
```

Output:

```
.
.PAL FIZBUZ.PA
ERRORS DETECTED: 0
LINKS GENERATED: 0

.LOAD FIZBUZ.BN

.START
1
2
FIZZ
4
BUZZ
FIZZ
7
8
FIZZ
BUZZ
11
FIZZ
13
14
FIZZBUZZ
16
17
FIZZ
19
BUZZ
FIZZ
22
23
FIZZ
BUZZ
26
FIZZ
28
29
FIZZBUZZ
31
32
FIZZ
34
BUZZ
FIZZ
37
38
FIZZ
BUZZ
41
FIZZ
43
44
FIZZBUZZ
46
47
FIZZ
49
BUZZ
FIZZ
52
53
FIZZ
BUZZ
56
FIZZ
58
59
FIZZBUZZ
61
62
FIZZ
64
BUZZ
FIZZ
67
68
FIZZ
BUZZ
71
FIZZ
73
74
FIZZBUZZ
76
77
FIZZ
79
BUZZ
FIZZ
82
83
FIZZ
BUZZ
86
FIZZ
88
89
FIZZBUZZ
91
92
FIZZ
94
BUZZ
FIZZ
97
98
FIZZ
BUZZ

.
```


## Peloton

Variable-length padded English dialect

```mw
<# DEFINE USERDEFINEDROUTINE LITERAL>__FizzBuzz|<# SUPPRESSAUTOMATICWHITESPACE>
<# TEST ISITMODULUSZERO PARAMETER LITERAL>1|3</#>
<# TEST ISITMODULUSZERO PARAMETER LITERAL>1|5</#>
<# ONLYFIRSTOFLASTTWO><# SAY LITERAL>Fizz</#></#>
<# ONLYSECONDOFLASTTWO><# SAY LITERAL>Buzz</#></#>
<# BOTH><# SAY LITERAL>FizzBuzz</#></#>
<# NEITHER><# SAY PARAMETER>1</#></#>
</#></#>
<# ITERATE FORITERATION LITERAL LITERAL>100|<# ACT USERDEFINEDROUTINE POSITION FORITERATION>__FizzBuzz|...</#> </#>
```

Fixed-length English dialect

```mw
<@ DEFUDRLIT>__FizzBuzz|<@ SAW>
<@ TSTMD0PARLIT>1|3</@>
<@ TSTMD0PARLIT>1|5</@>
<@ O12><@ SAYLIT>Fizz</@></@>
<@ O22><@ SAYLIT>Buzz</@></@>
<@ BTH><@ SAYLIT>FizzBuzz</@></@>
<@ NTH><@ SAYPAR>1</@></@>
</@></@>
<@ ITEFORLITLIT>100|<@ ACTUDRPOSFOR>__FizzBuzz|...</@> </@>
```


## Perl

```mw
use strict;
use warnings;
use feature qw(say);

for my $i (1..100) {
    say $i % 15 == 0 ? "FizzBuzz"
      : $i %  3 == 0 ? "Fizz"
      : $i %  5 == 0 ? "Buzz"
      : $i;
}
```

More concisely:

```mw
print 'Fizz'x!($_ % 3) . 'Buzz'x!($_ % 5) || $_, "\n" for 1 .. 100;
```

For code-golfing:

```mw
print+(Fizz)[$_%3].(Buzz)[$_%5]||$_,$/for 1..1e2
```

For array of values:

```mw
map((Fizz)[$_%3].(Buzz)[$_%5]||$_,1..100);
```

Cheating:

```mw
use feature "say";

@a = ("FizzBuzz", 0, 0, "Fizz", 0, "Buzz", "Fizz", 0, 0, "Fizz", "Buzz", 0, "Fizz");

say $a[$_ % 15] || $_ for 1..100;
```

as a subroutine:

```mw
sub fizz_buzz {
    join("\n", map {
        sub mult {$_ % shift == 0};
        my @out;
        if (mult 3) { push @out, "Fizz"; }
        if (mult 5) { push @out, "Buzz"; }
        if (!@out) {push @out, $_; }
        join('', @out);
    } (1..100))."\n";
}
print fizz_buzz;
```

By transforming a list:

```mw
 
@FB1 = (1..100);
@FB2 = map{!($_%3 or $_%5)?'FizzBuzz': $_}@FB1;
@FB3 = map{(/\d/ and !($_%3))?'Fizz': $_}@FB2;
@FB4 = map{(/\d/ and !($_%5))?'Buzz': $_}@FB3;
@FB5 = map{$_."\n"}@FB4;
print @FB5;
```


## Phix

Library:

Phix/basics

Translation of

:

C

```
constant x = {"%d\n","Fizz\n","Buzz\n","FizzBuzz\n"}
for i=1 to 100 do
    printf(1,x[1+(remainder(i,3)=0)+2*(remainder(i,5)=0)],i)
end for
```

Two variants with tabulated output:

```
function f(integer i)
    integer idx = 1+(remainder(i,3)=0)+2*(remainder(i,5)=0)
    return sprintf({"%-8d","Fizz    ","Buzz    ","FizzBuzz"}[idx],i)
end function
printf(1,join_by(apply(tagset(100),f),10,10))
```

(output same as below)

```
sequence s = apply(true,sprintf,{{"%-8d"},tagset(100)})
for i=3 to 100 by 3 do s[i] = "Fizz    " end for
for i=5 to 100 by 5 do s[i] = "Buzz    " end for
for i=15 to 100 by 15 do s[i] = "FizzBuzz" end for
printf(1,join_by(s,10,10))
```

**Output:**

```
1          11         Fizz       31         41         Fizz       61         71         Fizz       91
2          Fizz       22         32         Fizz       52         62         Fizz       82         92
Fizz       13         23         Fizz       43         53         Fizz       73         83         Fizz
4          14         Fizz       34         44         Fizz       64         74         Fizz       94
Buzz       FizzBuzz   Buzz       Buzz       FizzBuzz   Buzz       Buzz       FizzBuzz   Buzz       Buzz
Fizz       16         26         Fizz       46         56         Fizz       76         86         Fizz
7          17         Fizz       37         47         Fizz       67         77         Fizz       97
8          Fizz       28         38         Fizz       58         68         Fizz       88         98
Fizz       19         29         Fizz       49         59         Fizz       79         89         Fizz
Buzz       Buzz       FizzBuzz   Buzz       Buzz       FizzBuzz   Buzz       Buzz       FizzBuzz   Buzz
```

Grotesquely inefficient (non-tabulated output), just for fun. Can you do worse, yet keep it semi-plausibile that someone might have actually earnestly written it?

```
constant threes = tagset(100,0,3),
         fives = tagset(100,0,5),
         fifteens = tagset(100,0,15)

for i=1 to 100 do
    if not find(i,threes) and not find(i,fives) and not find(i,fifteens) then
        printf(1,"%d",i)
    end if
    if find(i,threes) and not find(i,fives) and not find(i,fifteens) then
        printf(1,"Fizz")
    end if
    if not find(i,threes) and find(i,fives) and not find(i,fifteens) then
        printf(1,"Buzz",i)
    end if
    if find(i,threes) and find(i,fives) and find(i,fifteens) then
        printf(1,"FizzBuzz")
    end if
    printf(1,"\n")
end for
```


## Phixmonti

```mw
/# Rosetta Code problem: http://rosettacode.org/wiki/FizzBuzz
by Galileo, 10/2022 #/

100 for
    dup print " " print dup
    3 mod not if "Fizz" print endif
    5 mod not if "Buzz" print endif
    nl
endfor
```

**Output:**

```
1
2
3 Fizz
4
5 Buzz
6 Fizz
7
8
9 Fizz
10 Buzz
11
12 Fizz
13
14
15 FizzBuzz
16
17
18 Fizz
19
20 Buzz
21 Fizz
22
23
24 Fizz
25 Buzz
26
27 Fizz
28
29
30 FizzBuzz
31
32
33 Fizz
34
35 Buzz
36 Fizz
37
38
39 Fizz
40 Buzz
41
42 Fizz
43
44
45 FizzBuzz
46
47
48 Fizz
49
50 Buzz
51 Fizz
52
53
54 Fizz
55 Buzz
56
57 Fizz
58
59
60 FizzBuzz
61
62
63 Fizz
64
65 Buzz
66 Fizz
67
68
69 Fizz
70 Buzz
71
72 Fizz
73
74
75 FizzBuzz
76
77
78 Fizz
79
80 Buzz
81 Fizz
82
83
84 Fizz
85 Buzz
86
87 Fizz
88
89
90 FizzBuzz
91
92
93 Fizz
94
95 Buzz
96 Fizz
97
98
99 Fizz
100 Buzz

=== Press any key to exit ===
```


## PHL

Translation of

:

C

```mw
module fizzbuzz;

extern printf;

@Integer main [
	var i = 1;
	while (i <= 100) {
		if (i % 15 == 0)
		    printf("FizzBuzz");
		else if (i % 3 == 0)
		    printf("Fizz");
		else if (i % 5 == 0)
		    printf("Buzz");
		else
		    printf("%d", i);
	 
		printf("\n");
		i = i::inc;
	}
	
	return 0;
]
```


## PHP

### if/else ladder approach

```mw
<?php
for ($i = 1; $i <= 100; $i++)
{
    if (!($i % 15))
        echo "FizzBuzz\n";
    else if (!($i % 3))
        echo "Fizz\n";
    else if (!($i % 5))
        echo "Buzz\n";
    else
        echo "$i\n";
}
?>
```

### Concatenation approach

Uses PHP's concatenation operator (.=) to build the output string. The concatenation operator allows us to add data to the end of a string without overwriting the whole string. Since Buzz will always appear if our number is divisible by five, and Buzz is the second part of "FizzBuzz", we can simply append "Buzz" to our string.

In contrast to the if-else ladder, this method lets us skip the check to see if $i is divisible by both 3 and 5 (i.e. 15). However, we get the added complexity of needing to reset $str to an empty string (not necessary in some other languages), and we also need a separate if statement to check to see if our string is empty, so we know if $i was not divisible by 3 or 5.

```mw
<?php
for ( $i = 1; $i <= 100; ++$i )
{
     $str = "";

     if (!($i % 3 ) )
          $str .= "Fizz";

     if (!($i % 5 ) )
          $str .= "Buzz";

     if ( empty( $str ) )
          $str = $i;

     echo $str . "\n";
}
?>
```

### Concatenation approach without if-s

```mw
<?php
for (
    $i = 0;
    $i++ < 100;
    $o = ($i % 3 ? '' : 'Fizz') . ($i % 5 ? '' : 'Buzz')
)
    echo $o ? : $i, PHP_EOL;
?>
```

### One Liner Approach

```mw
<?php
for($i = 1; $i <= 100 and print(($i % 15 ? $i % 5 ? $i % 3 ? $i : 'Fizz' : 'Buzz' : 'FizzBuzz') . "\n"); ++$i);
?>
```

### Compact One Liner Approach

```mw
for($i=0;$i++<100;)echo($i%3?'':'Fizz').($i%5?'':'Buzz')?:$i,"\n";
```

### Array One Liner Approach

```mw
for($i = 0; $i++ < 100;) echo [$i, 'Fizz', 'Buzz', 'FizzBuzz'][!($i % 3) + 2 * !($i % 5)], "\n";
```


## Picat

Picat supports different programming styles/paradigms.

First some "standalone" predicates.

### Using a map

```mw
fizzbuzz_map =>
    println(fizzbuzz_map),
    FB = [I : I in 1..100],
    Map = [(3="Fizz"),(5="Buzz"),(15="FizzBuzz")],
    foreach(I in FB, K=V in Map) 
       if I mod K == 0 then
          FB[I] := V
       end
    end,
    println(FB).
```

### Using a template for the pattern

```mw
fizzbuzz_template1 =>
   println(fizzbuzz_template1),
   N = 100,
   F = [_,_,fizz,_,buzz,fizz,_,_,fizz,buzz,_,fizz,_,_,fizzbuzz],
   FF = [F : _I in 1..1+N div F.length].flatten(),
   foreach(I in 1..N)
      (var(FF[I]) -> print(I) ; print(FF[I])),
      print(" ")
   end,
   nl.
```

### Another version with templates

```mw
fizzbuzz_template2 =>
   println(fizzbuzz_template2),
   N = 100,
   F = new_list(N),
   FV = [3,5,15],
   FN = ["Fizz","Buzz","FizzBuzz"],
   foreach(I in 1..N, {Val,Name} in zip(FV,FN)) 
      if I mod Val == 0 then F[I] := Name end
   end,
   foreach(I in 1..N)
      printf("%w ", cond(var(F[I]),I, F[I]))
   end,
   nl.
```

Below are some versions for identifying the FizzBuzziness of a number. To be used with the following general wrapper:

```mw
fizzbuzz(Goal) => 
    println(Goal),
    foreach(I in 1..100)
       printf("%w ", apply(Goal,I))
    end,
    nl.
```

### Plain imperative approach: if/else

```mw
fb1(I) = V =>
   V = I.to_string(),
   if     I mod 15 == 0 then V := "FizzBuzz"
   elseif I mod  3 == 0 then V := "Fizz" 
   elseif I mod  5 == 0 then V := "Buzz" 
   end.
```

### Pattern matching + conditions in head

```mw
fb2(I) = "FizzBuzz", I mod 15 == 0 => true.
fb2(I) = "Fizz",     I mod  3 == 0 => true.
fb2(I) = "Buzz",     I mod  5 == 0 => true.
fb2(I) = I.to_string()             => true.
```

### Another pattern matching approach

```mw
fb3(I) = fb3b(I, I mod 3, I mod 5).
fb3b(_I,0,0) = "FizzBuzz".
fb3b(_I,_,0) = "Buzz".
fb3b(_I,0,_) = "Fizz".
fb3b(I,_,_)  = I.
```

### Using cond/3 and string concatenation

```mw
fb4(I) = cond(I mod 3 == 0, "Fizz", "") ++ 
         cond(I mod 5 == 0, "Buzz", "")  ++
         cond(not ((I mod 3 == 0; I mod 5==0)), I.to_string(), "").
```

### Recursive function (conditions in head)

```mw
fizzbuzz_rec =>
  print(fizzbuzz_rec),
  fb5(100,[],L),
  println(L).
  
fb5(N,L1,L), N = 0 ?=>
  L = L1.reverse().
fb5(N,L1,L),N mod 15 == 0 ?=>
  fb5(N-1,L1 ++ ["FizzBuzz"], L).
fb5(N,L1,L), N mod 5 == 0 ?=>
  fb5(N-1,L1 ++ ["Buzz"], L).
fb5(N,L1,L), N mod 3 == 0 ?=>
  fb5(N-1,L1 ++ ["Fizz"], L).
fb5(N,L1,L), N mod 3 > 0, N mod 5 > 0 =>
  fb5(N-1,L1 ++ [N.to_string()], L).
```

### Golfing style

```mw
fizzbuzz_golf =>
   println(fizzbuzz_golf),
   [cond(P=="",I,P):I in 1..100,(I mod 3==0->P="Fizz";P=""),(I mod 5==0->P:=P++"Buzz";true)].println().
```

### Planner version

Picat has support for "classic" planning problems. The `planner` module must be imported.

```mw
import planner.
fizzbuzz_planner =>
   println(fizzbuzz_planner),
   plan(100,Plan),
   println(Plan.reverse()),
   nl.

final(Goal) => Goal == 0.

action(H,To,Move,Cost) ?=> 
  H mod 15 == 0,
  Move = "FizzBuzz",
  To = H-1,
  Cost = 1.

action(H,To,Move,Cost) ?=> 
  H mod 5 == 0,
  Move = "Buzz",
  To = H-1,
  Cost = 1.

action(H,To,Move,Cost) ?=> 
  H mod 3 == 0,
  Move = "Fizz",
  To = H-1,
  Cost = 1.

action(H,To,Move,Cost) => 
  H mod 3 > 0,
  H mod 5 > 0,
  Move = H.to_string(),
  To = H-1,
  Cost = 1.
```

Here we test everything.

```mw
go =>
  fizzbuzz_map,
  fizzbuzz_template1,
  fizzbuzz_template2,
  fizzbuzz_planner,
  fizzbuzz_rec,
  fizzbuzz_golf,

  FBs = [fb1,fb2,fb3,fb4],
  foreach(FB in FBs)
    call(fizzbuzz,FB)
  end,
  nl.
```


## PicoLisp

We could simply use 'at' here:

```mw
(for N 100
   (prinl
      (or (pack (at (0 . 3) "Fizz") (at (0 . 5) "Buzz")) N) ) )

# Above, we simply count till 100 'prin'-ting number 'at' 3rd ('Fizz'), 5th ('Buzz') and 'pack'-ing 15th number ('FizzBuzz').
# Rest of the times 'N' is printed as it loops in 'for'.
```

Or do it the standard way:

```mw
(for N 100
   (prinl
      (cond
         ((=0 (% N 15)) "FizzBuzz")
         ((=0 (% N 3)) "Fizz")
         ((=0 (% N 5)) "Buzz")
         (T N) ) ) )
```


## Piet

See FizzBuzz/EsoLang#Piet


## Pike

```mw
int main(){
   for(int i = 1; i <= 100; i++) {
      if(i % 15 == 0) {
         write("FizzBuzz\n");
      } else if(i % 3 == 0) {
         write("Fizz\n");
      } else if(i % 5 == 0) {
         write("Buzz\n");
      } else {
         write(i + "\n");
      }
   }
}
```


## PILOT

```mw
C  :i = 0
*loop
C  :i = i + 1
J ( i > 100 )    : *finished
C  :modulo = i % 15
J ( modulo = 0 ) : *fizzbuzz
C  :modulo = i % 3
J ( modulo = 0 ) : *fizz
C  :modulo = i % 5
J ( modulo = 0 ) : *buzz
T  :#i
J  : *loop
*fizzbuzz
T  :FizzBuzz
J  : *loop
*fizz
T  :Fizz
J  : *loop
*buzz
T  :Buzz
J  : *loop
*finished
END:
```


## PIR

Works with

:

Parrot

version tested with 2.4.0

```mw
.sub main :main
  .local int f
  .local int mf
  .local int skipnum
  f = 1
LOOP: 
  if f > 100 goto DONE
  skipnum = 0
  mf = f % 3
  if mf == 0 goto FIZZ
FIZZRET:
  mf = f % 5
  if mf == 0 goto BUZZ
BUZZRET:
  if skipnum > 0 goto SKIPNUM
  print f
SKIPNUM:
  print "\n"
  inc f 
  goto LOOP
  end
FIZZ:
  print "Fizz"
  inc skipnum
  goto FIZZRET
  end
BUZZ:
  print "Buzz"
  inc skipnum
  goto BUZZRET
  end
DONE:
  end
.end
```


## PL/I

```mw
do i = 1 to 100;
   select;
      when (mod(i,15) = 0) put skip list ('FizzBuzz');
      when (mod(i,3)  = 0) put skip list ('Fizz');
      when (mod(i,5)  = 0) put skip list ('Buzz');
      otherwise put skip list (i);
   end;
end;
```


## PL/M

```mw
100H:

/* DECLARE OUTPUT IN TERMS OF CP/M - 
   PL/M DOES NOT COME WITH ANY STANDARD LIBRARY */
BDOS: PROCEDURE(FUNC, ARG);
    DECLARE FUNC BYTE, ARG ADDRESS;
    GO TO 5;
END BDOS;

PUT$STRING: PROCEDURE(STR);
    DECLARE STR ADDRESS;
    CALL BDOS(9, STR);
    CALL BDOS(9, .(13,10,'$'));
END PUT$STRING;

/* PRINT A NUMBER */
PUT$NUMBER: PROCEDURE(N);
    DECLARE S (5) BYTE INITIAL ('...$');
    DECLARE P ADDRESS;
    DECLARE (N, D, C BASED P) BYTE;
    P = .S(3);
DIGIT:
    P = P-1;
    C = (N MOD 10) + '0';
    N = N/10;
    IF N > 0 THEN GO TO DIGIT;
    CALL PUT$STRING(P);
END PUT$NUMBER;

/* FIZZBUZZ */
DECLARE N BYTE;
DO N = 1 TO 100;
    IF N MOD 15 = 0 THEN 
        CALL PUT$STRING(.'FIZZBUZZ$');
    ELSE IF N MOD 5 = 0 THEN 
        CALL PUT$STRING(.'BUZZ$');
    ELSE IF N MOD 3 = 0 THEN 
        CALL PUT$STRING(.'FIZZ$');
    ELSE
        CALL PUT$NUMBER(N);
END;

/* EXIT TO CP/M */
CALL BDOS(0,0);
EOF
```


## PL/SQL

```mw
begin
  for i in 1 .. 100
  loop
    case
    when mod(i, 15) = 0 then
      dbms_output.put_line('FizzBuzz');
    when mod(i, 5) = 0 then
      dbms_output.put_line('Buzz');
    when mod(i, 3) = 0 then
      dbms_output.put_line('Fizz');
    else
      dbms_output.put_line(i);
    end case;
  end loop;
end;
```


## Plain English

```mw
To play FizzBuzz up to a number:
Put "" into a string.
Loop.
If a counter is past the number, exit.
If the counter is evenly divisible by 3, append "Fizz" to the string.
If the counter is evenly divisible by 5, append "Buzz" to the string.
If the string is blank, append the counter then "" to the string.
Write the string to the console.
Clear the string.
Repeat.

To run:
Start up.
Play FizzBuzz up to 100.
Wait for the escape key.
Shut down.
```


## Pluto

```mw
for i = 1, 100 do
    if i % 15 == 0 then
        print("FizzBuzz")
    elseif i % 3 == 0 then
        print("Fizz")
    elseif i % 5 == 0 then
        print("Buzz")
    else
        print(i)
    end
end
```

**Output:**

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
...
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


## Pointless

```mw
output =
  range(1, 100)
  |> map(fizzBuzz)
  |> printLines

fizzBuzz(n) =
  if result == "" then n else result
  where result = fizzBuzzString(n)

fizzBuzzString(n) =
  (if n % 3 == 0 then "Fizz" else "")
  + (if n % 5 == 0 then "Buzz" else "")
```


## Pony

```mw
use "collections"
 
actor Main
  new create(env: Env) =>
    for i in Range[I32](1, 100) do
      env.out.print(fizzbuzz(i))
    end
 
  fun fizzbuzz(n: I32): String =>
    if (n % 15) == 0 then
      "FizzBuzz"
    elseif (n % 5) == 0 then
      "Buzz"
    elseif (n % 3) == 0 then
      "Fizz"
    else
      n.string()
    end
```


## Pop11

```mw
lvars str;
for i from 1 to 100 do
  if i rem 15 = 0 then
    'FizzBuzz' -> str;
  elseif i rem 3 = 0 then
    'Fizz' -> str;
  elseif i rem 5 = 0 then
    'Buzz' -> str;
  else
    '' >< i -> str;
  endif;
  printf(str, '%s\n');
endfor;
```


## PostScript

```mw
1 1 100 { 
	/c false def
	dup 3 mod 0 eq { (Fizz) print /c true def } if
	dup 5 mod 0 eq { (Buzz) print /c true def } if
    c {pop}{(   ) cvs print} ifelse
    (\n) print
} for
```

or...

```mw
/fizzdict 100 dict def
fizzdict begin
/notmod{ (   ) cvs } def
/mod15 { dup 15 mod 0 eq { (FizzBuzz)def }{pop}ifelse} def
/mod3  { dup 3 mod 0 eq {(Fizz)def}{pop}ifelse} def
/mod5  { dup 5 mod 0 eq {(Buzz)def}{pop}ifelse} def
1 1 100 { mod3 } for 
1 1 100 { mod5 } for 
1 1 100 { mod15} for
1 1 100 { dup currentdict exch known { currentdict exch get}{notmod} ifelse print (\n) print} for
end
```


## Potion

```mw
1 to 100 (a):
  if (a % 15 == 0):
    'FizzBuzz'.
  elsif (a % 3 == 0):
    'Fizz'.
  elsif (a % 5 == 0):
    'Buzz'.
  else: a. string print
  "\n" print.
```


## PowerShell

### Straightforward, looping

```mw
for ($i = 1; $i -le 100; $i++) {
    if ($i % 15 -eq 0) {
        "FizzBuzz"
    } elseif ($i % 5 -eq 0) {
        "Buzz"
    } elseif ($i % 3 -eq 0) {
        "Fizz"
    } else {
        $i
    }
}
```

### Pipeline, Switch

```mw
$txt=$null
1..100 | ForEach-Object {
    switch ($_) {
        { $_ % 3 -eq 0 }  { $txt+="Fizz" }
        { $_ % 5 -eq 0 }  { $txt+="Buzz" }
        $_                { if($txt) { $txt } else { $_ }; $txt=$null }
    }
}
```

### Concatenation

Translation of

:

C#

```mw
1..100 | ForEach-Object {
    $s = ''
    if ($_ % 3 -eq 0) { $s += "Fizz" }
    if ($_ % 5 -eq 0) { $s += "Buzz" }
    if (-not $s) { $s = $_ }
    $s
}
```

### Piping, Evaluation, Concatenation

```mw
1..100 | % {write-host("$(if(($_ % 3 -ne 0) -and ($_ % 5 -ne 0)){$_})$(if($_ % 3 -eq 0){"Fizz"})$(if($_ % 5 -eq 0){"Buzz"})")}
```

### Filter, Piping, Regex Matching, Array Auto-Selection

```mw
filter fizz-buzz{
    @(
        $_, 
        "Fizz", 
        "Buzz", 
        "FizzBuzz"
    )[
        2 * 
        ($_ -match '[05]$') + 
        ($_ -match '(^([369][0369]?|[258][147]|[147][258]))$')
    ]
}

1..100 | fizz-buzz
```

### String Manipulation with Regex

```mw
(1..100 -join "`n") + "`nFizzBuzz" -replace '(?ms)(^([369]([369]|(?=0|$))|[258][147]|[147]([28]|(?=5))))(?=[05]?$.*(Fizz))|(((?<=[369])|[^369])0+|((?<=[147\s])|[^147\s])5)(?=$.*(Buzz))|FizzBuzz', '$5$9'
```


## Processing

### Console & Visualization

Reserved variable "width" in Processing is 100 pixels by default, suitable for this FizzBuzz exercise. Accordingly, range is pixel index from 0 to 99.

```mw
for (int i = 0; i < width; i++) {
  if (i % 3 == 0 && i % 5 == 0) {
    stroke(255, 255, 0);
    println("FizzBuzz!");
  }
  else if (i % 5 == 0) {
    stroke(0, 255, 0);
    println("Buzz");
  }
  else if (i % 3 == 0) {
    stroke(255, 0, 0);
    println("Fizz");
  }
  else {
    stroke(0, 0, 255);
    println(i);
  } 
  line(i, 0, i, height);
}
```

### Console & Visualization, Ternary

```mw
for (int i = 0; i < width; i++) {
  stroke((i % 5 == 0 && i % 3 == 0) ? #FFFF00 : (i % 5 == 0) ? #00FF00 : (i % 3 == 0) ? #FF0000 : #0000FF);
  line(i, 0, i, height);
  println((i % 5 == 0 && i % 3 == 0) ? "FizzBuzz!" : (i % 5 == 0) ? "Buzz" : (i % 3 == 0) ? "Fizz" : i);
}
```

### Console

```mw
for (int i = 1; i <= 100; i++) {
  if (i % 3 == 0) {
    print("Fizz");
  }
  if (i % 5 == 0) {
    print("Buzz");
  }
  if (i % 3 != 0 && i % 5 != 0) {
    print(i);
  }
  print("\n");
}
```

### Console, "Futureproof"

```mw
for(int i = 1; i <= 100; i++){
  String output = "";
  	
  if(i % 3 == 0) output += "Fizz";
  if(i % 5 == 0) output += "Buzz";
  // copy & paste above line to add more tests
  
  if(output == "") output = str(i);
  println(output);
}
```

All examples produce the same console output:

**Output:**

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


## Prolog

Works with

:

SWI Prolog

version 4.8.0

Works with

:

Ciao Prolog

version 1.21.0

Maybe not the most conventional way to write this in Prolog. The fizzbuzz predicate uses a higher-order predicate and print_item uses the if-then-else construction.

```mw
fizzbuzz :-
   forall(between(1, 100, X), print_item(X)).

print_item(X) :-
   (  X mod 15 =:= 0
   -> write('FizzBuzz')
   ;  X mod 3 =:= 0
   -> write('Fizz')
   ;  X mod 5 =:= 0
   -> write('Buzz')
   ;  write(X)
   ),
   nl.
```

More conventional, doing the loop this time failure driven:

```mw
fizzbuzz(X) :- X mod 15 =:= 0, !, write('FizzBuzz').
fizzbuzz(X) :- X mod 3 =:= 0, !, write('Fizz').
fizzbuzz(X) :- X mod 5 =:= 0, !, write('Buzz').
fizzbuzz(X) :- write(X).

dofizzbuzz :-between(1, 100, X), fizzbuzz(X), nl, fail.
dofizzbuzz.
```

Clearer, doing the loop this time tail recursive, quite declarative:

```mw
%        N  /3?  /5?  V
fizzbuzz(_, yes, yes, 'FizzBuzz').
fizzbuzz(_, yes, no,  'Fizz').
fizzbuzz(_, no,  yes, 'Buzz').
fizzbuzz(N, no,  no,  N).

% Unifies V with 'yes' if D divides evenly into N, 'no' otherwise.
divisible_by(N, D, yes) :- N mod D =:= 0.
divisible_by(N, D, no) :- N mod D =\= 0.

% Print 'Fizz', 'Buzz', 'FizzBuzz' or N as appropriate.
fizz_buzz_or_n(N) :- N > 100.
fizz_buzz_or_n(N) :- N =< 100,
   divisible_by(N, 3, Fizz),
   divisible_by(N, 5, Buzz),
   fizzbuzz(N, Fizz, Buzz, FB),
   write(FB), nl,
   M is N+1, fizz_buzz_or_n(M).

main :-
   fizz_buzz_or_n(1).
```

Using modern Prolog techniques, resulting in idiomatic, highly declarative code:

Works with

:

SWI Prolog

version 8.2.1

Works with

:

Scryer Prolog

version 0.7.8

```mw
% This implementation uses modern Prolog techniques
% in order to be an idiomatic solution that uses logical purity, generality and determinism wherever possible:
% - CLP(Z): constraint logic programming on integers.
% - library(reif): efficient logical predicates based on 'Indexing dif/2'.
:- module(fizz_buzz, [main/0, integer_fizzbuzz_below_100/2, integer_fizzbuzz/2]).

:- use_module(library(reif)).

% for Scryer-Prolog:
:- use_module(library(clpz)).
:- use_module(library(between)).
:- use_module(library(iso_ext)).
:- use_module(library(si)).

% for SWI-Prolog:
% :- use_module(library(clpfd)).

% Prints all solutions to `integer_fizzbuzz_below_100` each on a separate line, in order.
% Logically-impure shell, as currently there is no logically-pure way to write to a filestream.
main :-
    forall(integer_fizzbuzz_below_100(_, FizzBuzz), write_line(FizzBuzz)).

write_line(Value) :-
    write(Value),
    nl.

% Constrains FizzBuzz results to the range 1 <= X <= 100,
% and (for the 'most general query' where neither X or FizzBuzz is concrete)
% ensures results are traversed in order low -> high X.
%
% ?- integer_fizzbuzz_below_100(X, FizzBuzz) % generate all the results in order
% ?- integer_fizzbuzz_below_100(27, Result) % Find out what output `27` will produce (it's 'Fizz'.)
% ?- integer_fizzbuzz_below_100(X, 'Fizz')   % generate all the numbers which would print 'Fizz' in order (3, 6, 9, etc).
% ?- integer_fizzbuzz_below_100(X, Res), integer_si(Res) % generate all the numbers which would print themselves in order (1, 2, 4, 6, 7, 8, 11, etc).
% ?- integer_fizzbuzz_below_100(X, Res), is_of_type(integer, Res) % SWI-Prolog version doing the same.
integer_fizzbuzz_below_100(X, FizzBuzz) :-
    between(1, 100, X),
    integer_fizzbuzz(X, FizzBuzz).

% States the relationship between a number
% and its FizzBuzz representation.
%
% Because constraints are propagated lazily,
% prompting this predicate without having constrained `Num`
% to a particular integer value will give you its definition back.
% Put differently: This predicate returns the whole solution space at once,
% and external labeling techniques are required to traverse and concretize this solution space
% in an order that we like.
integer_fizzbuzz(Num, FizzBuzz) :-
    if_(Num mod 15 #= 0, FizzBuzz = 'FizzBuzz',
        if_(Num mod 5 #= 0, FizzBuzz = 'Buzz',
            if_(Num mod 3 #= 0, FizzBuzz = 'Fizz',
                Num = FizzBuzz)
           )
       ).

% Reifiable `#=`.
#=(X, Y, T) :-
    X #= X1,
    Y #= Y1,
    zcompare(C, X1, Y1),
    eq_t(C, T).

eq_t(=, true).
eq_t(<, false).
eq_t(>, false).
```


## PureBasic

See FizzBuzz/Basic


## Pyret

````mw
fun fizzbuzz(n :: NumPositive) -> String:
  doc: ```For positive input which is multiples of three return 'Fizz', for the multiples of five return 'Buzz'. 
  For numbers which are multiples of both three and five return 'FizzBuzz'. Otherwise, return the number itself.```
  ask:
    | num-modulo(n, 15) == 0 then: "FizzBuzz"
    | num-modulo(n, 3) == 0 then: "Fizz"
    | num-modulo(n, 5) == 0 then: "Buzz"
    | otherwise: num-to-string(n)
  end
where:
  fizzbuzz(1) is "1"
  fizzbuzz(101) is "101"
  fizzbuzz(45) is "FizzBuzz"
  fizzbuzz(33) is "Fizz"
  fizzbuzz(25) is "Buzz"
end

range(1, 101).map(fizzbuzz).each(print)
````


## Python

### Python2: Simple

```mw
for i in range(1, 101):
    if i % 15 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i
```

### Python3: Simple

```mw
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Python: Simple - no duplication

```mw
for n in range(1,101):
    response = ''

    if not n%3:
        response += 'Fizz'
    if not n%5:
        response += 'Buzz'

    print(response or n)
```

One liner using string concatenation:

```mw
for i in range(1,101): print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)
```

One liner another code:

```mw
for i in range(100):print(i%3//2*'Fizz'+i%5//4*'Buzz'or i+1)
```

List Comprehensions:

```mw
for n in range(1, 100):
    fb = ''.join([ denom[1] if n % denom[0] == 0 else '' for denom in [(3,'fizz'),(5,'buzz')] ])
    print fb if fb else n
```

Another list comprehension:

```mw
print (', '.join([(x%3<1)*'Fizz'+(x%5<1)*'Buzz' or str(x) for x in range(1,101)]))
```

### Python: Call in dictionnary

```mw
actions = {
    0: lambda i: print(i),
    1: lambda i: print("fizz"),
    2: lambda i: print("buzz"),
    3: lambda i: print("fizzbuzz"),
}

for i in range(1, 101):
    action_index = 0

    if i % 3 == 0:
        action_index += 1

    if i % 5 == 0:
        action_index += 2

    actions[action_index](i)
```

### Python: List Comprehension (Python 3)

```mw
[print("FizzBuzz") if i % 15 == 0 else print("Fizz") if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i) for i in range(1,101)]
```

### Python: Lazily

You can also create a lazy, unbounded sequence by using generator expressions:

```mw
from itertools import cycle, izip, count, islice

fizzes = cycle([""] * 2 + ["Fizz"])
buzzes = cycle([""] * 4 + ["Buzz"])
both = (f + b for f, b in izip(fizzes, buzzes))

# if the string is "", yield the number
# otherwise yield the string
fizzbuzz = (word or n for word, n in izip(both, count(1)))

# print the first 100
for i in islice(fizzbuzz, 100):
    print i
```

Or equivalently, in terms of map, and Python 3 libraries:

Works with

:

Python

version 3.7

```mw
'''Fizz buzz'''

from itertools import count, cycle, islice

# fizzBuzz :: () -> Generator [String]
def fizzBuzz():
    '''A non-finite stream of fizzbuzz terms.
    '''
    return map(
        lambda f, b, n: (f + b) or str(n),
        cycle([''] * 2 + ['Fizz']),
        cycle([''] * 4 + ['Buzz']),
        count(1)
    )

# ------------------------- TEST -------------------------
def main():
    '''Display of first 100 terms of the fizzbuzz series.
    '''
    print(
        '\n'.join(
            list(islice(
                fizzBuzz(),
                100
            ))
        )
    )

if __name__ == '__main__':
    main()
```

### Python3.8: With walrus operator

```mw
print(*map(lambda n: 'Fizzbuzz '[(i):i+13] if (i := n**4%-15) > -14 else n, range(1,100)))
```

### Python: Math tricks

Numbers ending in 5 or 0 are divisible by 5. Numbers whose digits recursively summed to a single-digit number == 3,6 or 9 are divisible by 3.

```mw
def numsum(n):
	''' The recursive sum of all digits in a number 
        unit a single character is obtained'''
	res = sum([int(i) for i in str(n)])
	if res < 10: return res
	else : return numsum(res)
	
for n in range(1,101):
	response = 'Fizz'*(numsum(n) in [3,6,9]) + \
                   'Buzz'*(str(n)[-1] in ['5','0'])\
	            or n
	print(response)
```

### Python3: Super concise: 1 line

```mw
print(*((lambda x=x: ''.join(chr(c) for c in (102, 105)) + (2 * chr(122)) + ''.join(chr(c) for c in (98, 117)) + (2 * chr(122)) + '\n' if x % (30 >> 1) == 0 else ''.join(chr(c) for c in (102, 105)) + (2 * chr(122)) + '\n' if x % (6 >> 1) == 0 else ''.join(chr(c) for c in (98, 117)) + (2 * chr(122)) + '\n' if x % (10 >> 1) == 0 else str(x) + '\n')() for x in range(1, 101)))
```


## q

q is the query language for **kdb+**.

```mw
{(`$string x)^`fizzbuzz`buzz`fizz`(x mod\:15 5 3)?'0}
```

Usage:

```mw
q)/ Fizzbuzz
q)fb:{(`$string x)^`fizzbuzz`buzz`fizz`(x mod\:15 5 3)?'0}
q)fb 1+til 20
`1`2`fizz`4`buzz`fizz`7`8`fizz`buzz`11`fizz`13`14`fizzbuzz`16`17`fizz`19`buzz
```

https://https://q201.org/apply-fizzbuzz// https://code.kx.com/q/ref/mod/ https://code.kx.com/q/ref/fill

Explanation:

````mw
q)show x:1+til 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
q)x mod\:15 5 3
1  1 1
2  2 2
3  3 0
4  4 1
5  0 2
6  1 0
..
q)(x mod\:15 5 3)?'0
3 3 2 3 1 2 3 3 2 1 3 2 3 3 0 3 3 2 3 1
q)`fizzbuzz`buzz`fizz`(x mod\:15 5 3)?'0  / substitutions
```fizz``buzz`fizz```fizz`buzz``fizz```fizzbuzz```fizz``buzz
q)`$string x  / numbers => symbols
`1`2`3`4`5`6`7`8`9`10`11`12`13`14`15`16`17`18`19`20
q)(`$string x)^`fizzbuzz`buzz`fizz`(x mod\:15 5 3)?'0  / replace nulls with numbers
`1`2`fizz`4`buzz`fizz`7`8`fizz`buzz`11`fizz`13`14`fizzbuzz`16`17`fizz`19`buzz
````

### QBasic

See FizzBuzz/Basic


## QB64

```mw
For n = 1 To 100
    If n Mod 15 = 0 Then
        Print "FizzBuzz"
    ElseIf n Mod 5 = 0 Then
        Print "Buzz"
    ElseIf n Mod 3 = 0 Then
        Print "Fizz"
    Else
        Print n
    End If
Next
```


## Quackery

```mw
  100 times
    [ i^ 1+ true
      over 3 mod not 
        if [ say "fizz" drop false ]
      over 5 mod not 
        if [ say "buzz" drop false ]
      iff echo else drop 
      sp ]
```


## QuickBASIC

See FizzBuzz/Basic
