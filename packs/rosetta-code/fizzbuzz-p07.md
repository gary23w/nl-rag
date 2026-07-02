---
title: "FizzBuzz (part 7/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 7/7
---

## Tailspin

```mw
templates fizz
  $ mod 3 -> #
  when <=0> do 'Fizz' !
end fizz

templates buzz
  $ mod 5 -> #
  when <=0> do 'Buzz' !
end buzz

[ 1..100 -> '$->fizz;$->buzz;' ] -> \[i](when <=''> do $i ! otherwise $ !\)... -> '$;
' -> !OUT::write
```

v0.5

```mw
fizz templates
  $ mod 3 -> # !
  when <|=0> do 'Fizz' !
end fizz

buzz templates
  $ mod 5 -> # !
  when <|=0> do 'Buzz' !
end buzz

[ 1..100 -> '$->fizz;$->buzz;' ] -> $(.. as i; -> templates
  when <|=''> do $i !
  otherwise $ !
end)... -> '$;
' !
```


## tbas

See FizzBuzz/Basic


## Tcl

```mw
proc fizzbuzz {n {m1 3} {m2 5}} {
    for {set i 1} {$i <= $n} {incr i} {
        set ans ""
        if {$i % $m1 == 0} {append ans Fizz}
        if {$i % $m2 == 0} {append ans Buzz}
        puts [expr {$ans eq "" ? $i : $ans}]
    }
}
fizzbuzz 100
```

The following example shows Tcl's substitution mechanism that allows to concatenate the results of two successive commands into a string:

```mw
while {[incr i] < 101} {
    set fb [if {$i % 3 == 0} {list Fizz}][if {$i % 5 == 0} {list Buzz}]
    if {$fb ne ""} {puts $fb} {puts $i}
}
```

This version uses list rotation, so avoiding an explicit mod operation:

```mw
set f [lrepeat 5 "Fizz" {$i} {$i}]
foreach i {5 10} {lset f $i "Buzz"};lset f 0 "FizzBuzz"
for {set i 1} {$i <= 100} {incr i} {
    puts [subst [lindex [set f [list {*}[lassign $f ff] $ff]] 0]]
}
```


## TI SR-56

| Display | Key | Display | Key | Display | Key | Display | Key |
|---|---|---|---|---|---|---|---|
| 00 22 | GTO | 25 64 | x | 50 03 | 3 | 75 |   |
| 01 03 | 3 | 26 52 | ( | 51 34 | RCL | 76 |   |
| 02 07 | 7 | 27 52 | ( | 52 01 | 1 | 77 |   |
| 03 53 | ) | 28 34 | RCL | 53 59 | *pause | 78 |   |
| 04 12 | INV | 29 01 | 1 | 54 22 | GTO | 79 |   |
| 05 29 | *Int | 30 54 | / | 55 03 | 3 | 80 |   |
| 06 56 | *CP | 31 05 | 5 | 56 08 | 8 | 81 |   |
| 07 12 | INV | 32 57 | subr | 57 |   | 82 |   |
| 08 37 | *x=t | 33 00 | 0 | 58 |   | 83 |   |
| 09 01 | 1 | 34 03 | 3 | 59 |   | 84 |   |
| 10 03 | 3 | 35 94 | = | 60 |   | 85 |   |
| 11 01 | 1 | 36 58 | rtn | 61 |   | 86 |   |
| 12 84 | + | 37 38 | *CMs | 62 |   | 87 |   |
| 13 00 | 0 | 38 01 | 1 | 63 |   | 88 |   |
| 14 53 | ) | 39 35 | SUM | 64 |   | 89 |   |
| 15 58 | rtn | 40 02 | 2 | 65 |   | 90 |   |
| 16 33 | STO | 41 34 | RCL | 66 |   | 91 |   |
| 17 01 | 1 | 42 02 | 2 | 67 |   | 92 |   |
| 18 54 | / | 43 57 | subr | 68 |   | 93 |   |
| 19 03 | 3 | 44 01 | 1 | 69 |   | 94 |   |
| 20 57 | subr | 45 06 | 6 | 70 |   | 95 |   |
| 21 00 | 0 | 46 93 | +/- | 71 |   | 96 |   |
| 22 03 | 3 | 47 12 | INV | 72 |   | 97 |   |
| 23 84 | + | 48 47 | *x>=t | 73 |   | 98 |   |
| 24 02 | 2 | 49 05 | 5 | 74 |   | 99 |   |

Asterisk denotes 2nd function key.

| 0: Unused | 1: Argument | 2: Number | 3: Unused | 4: Unused |
|---|---|---|---|---|
| 5: Unused | 6: Unused | 7: Unused | 8: Unused | 9: Unused |

Annotated listing:

```mw
// Address 00: Entry point

GTO 3 7   // Jump to the main program

// Address 03: Subroutine
// Takes a pending division such as ((12/5 and evaluates whether it
// is evenly divisible.
// Result 1: evenly divisible, 0: not divisible

)              // Complete the pending division
INV *Int       // Take the fractional part
*CP            // RegT := 0
INV *x=t 1 3   // If fractional part is zero, don't increment
1 +            // Start a pending increment of the return value
0 ) rtn        // Return the return value

// Address 16: Subroutine
// Takes a number and evaluates whether it is divisible by 3 and 5.
// Result:  0=indivisible, 1=fizz, 2=buzz, 3=fizzbuzz

STO 1                    // Save subroutine argument
/ 3   subr 0 3           // 1 if fizz else 0
+ 2 x                    // Buzz is worth 2x as much as Fizz
( ( RCL 1 / 5 subr 0 3   // 1 if buzz else 0
=                        // Finish the pending + and x
rtn                      // Return result

// Address 37: Main program

*CMs            // Zero out registers
1 SUM 2         // Number += 1
RCL 2           // Retrieve Number
subr 1 6        // Evaluate whether it is divisible by 3 and 5
+/-             // Negate (0=indiv., -1=fizz, -2=buzz, -3=fizzbuzz)
INV *x>=t 5 3   // If negative, skip the next line.
RCL 1           // Retrieve number instead of zero.
*pause          // Flash the number on the display
GTO 3 8         // Loop
```

**Usage:**

Press RST R/S to start the program. Increasing numbers will flash on the screen. Positive numbers represent themselves; -1 means fizz, -2 buzz and -3 fizzbuzz. About 25 numbers are calculated per minute.


## TI-83 BASIC

See FizzBuzz/Basic


## TI-83 Hex Assembly

See FizzBuzz/Assembly


## TI-99/4a TI BASIC / Extended BASIC

See FizzBuzz/Basic


## Tiny BASIC

See FizzBuzz/Basic


## TransFORTH

```mw
: FIZZBUZZ
101 1 DO
I 15 MOD 0 = IF
PRINT " FIZZBUZZ "
ELSE I 3 MOD 0 = IF
PRINT " FIZZ "
ELSE I 5 MOD 0 = IF
PRINT " BUZZ "
ELSE I . THEN THEN THEN
CR LOOP ;
```


## True BASIC

See FizzBuzz/Basic


## Turing

```mw
for i : 1 .. 100
    if i mod 15 = 0 then
        put "Fizzbuzz"
    elsif i mod 5 = 0 then
        put "Buzz"
    elsif i mod 3 = 0 then
        put "Fizz"
    else
        put i
    end if
end for
```


## TUSCRIPT

```mw
$$ MODE TUSCRIPT
LOOP n=1,100
mod=MOD (n,15)
SELECT mod
CASE 0
PRINT n," FizzBuzz"
CASE 3,6,9,12
PRINT n," Fizz"
CASE 5,10
PRINT n," Buzz"
DEFAULT
PRINT n
ENDSELECT
ENDLOOP
```


## TXR

```mw
$ txr -p "(mapcar (op if @1 @1 @2) (repeat '(nil nil fizz nil buzz fizz nil nil fizz buzz nil fizz nil nil fizzbuzz)) (range 1 100))"
```


## UNIX Shell

This solution should work with any Bourne-compatible shell:

```mw
i=1
while expr $i '<=' 100 >/dev/null; do
	w=false
	expr $i % 3 = 0 >/dev/null && { printf Fizz; w=true; }
	expr $i % 5 = 0 >/dev/null && { printf Buzz; w=true; }
	if $w; then echo; else echo $i; fi
	i=`expr $i + 1`
done
```

### Versions for specific shells

The other solutions work with fewer shells.

The next solution requires `$(( ))` arithmetic expansion, and it should work with every POSIX shell.

```mw
n=1
while [ 100 -ge n ]; do
  if [ $((n % 15)) -eq 0 ]; then
    echo FizzBuzz
  elif [ $((n % 3)) -eq 0 ]; then
    echo Fizz
  elif [ $((n % 5)) -eq 0 ]; then
    echo Buzz
  else
    echo $n
  fi
  n=$((n + 1))
done
```

The next solution requires the `(( ))` command from the Korn Shell.

Works with

:

pdksh

version 5.2.14

```mw
NUM=1
until ((NUM == 101)) ; do
   if ((NUM % 15 == 0)) ; then
       echo FizzBuzz
   elif ((NUM % 3 == 0)) ; then
       echo Fizz
   elif ((NUM % 5 == 0)) ; then
       echo Buzz
   else 
       echo "$NUM"
   fi
   ((NUM = NUM + 1))
done
```

A version using concatenation:

Works with

:

bash

version 3

```mw
for ((n=1; n<=100; n++))
do
  fb=''
  [ $(( n % 3 )) -eq 0 ] && fb="${fb}Fizz"
  [ $(( n % 5 )) -eq 0 ] && fb="${fb}Buzz"
  [ -n "${fb}" ] && echo "${fb}" || echo "$n"
done
```

A version using some of the insane overkill of Bash 4:

Works with

:

bash

version 4

```mw
command_not_found_handle () { 
  local Fizz=3 Buzz=5
  [ $(( $2 % $1 )) -eq 0 ] && echo -n $1 && [ ${!1} -eq 3 ]
} 

for i in {1..100}
do
  Fizz $i && ! Buzz $i || echo -n $i
  echo
done
```

Bash one-liner:

```mw
for i in {1..100};do ((($i%15==0))&& echo FizzBuzz)||((($i%5==0))&& echo Buzz;)||((($i%3==0))&& echo Fizz;)||echo $i;done
```

### C Shell

```mw
@ n = 1
while ( $n <= 100 )
  if ($n % 15 == 0) then
    echo FizzBuzz
  else if ($n % 5 == 0) then
    echo Buzz
  else if ($n % 3 == 0) then
    echo Fizz
  else
    echo $n
  endif
  @ n += 1
end
```


## Uiua

Works with

:

Uiua

version 0.18.0-dev.3

```mw
⨬(&p|&p"Fizz"|&p"Buzz"|&p"Fizzbuzz")°⋯⍉=0⊸⊞◿3_5+1⇡100
```

**Output:**

As expected. See here for proof.


## Ursa

```mw
#
# fizzbuzz
#
decl int i
for (set i 1) (< i 101) (inc i)
        if (= (mod i 3) 0)
                out "fizz" console
        end if
        if (= (mod i 5) 0)
                out "buzz" console
        end if
        if (not (or (= (mod i 3) 0) (= (mod i 5) 0)))
                out i console
        end if
        out endl console
end for
```


## Ursala

```mw
#import std
#import nat

fizzbuzz = ^T(&&'Fizz'! not remainder\3,&&'Buzz'! not remainder\5)|| ~&h+ %nP

#show+

main = fizzbuzz*t iota 101
```


## Ursalang

```mw
let write = process.stdout.write

for i in range(100) {
    let n = i + 1
    if (n % 3 == 0) {write("Fizz")}
    if (n % 5 == 0) {write("Buzz")}
    if (n % 3 != 0 and n % 5 != 0) {write(n.toString())}
    write("\n")
}
```


## Uxntal

```mw
%<newline> ( -- ) { [ LIT2 -NewLine -Console/write ] DEO }
|18 @Console/write $1
|0a @NewLine

|100 @fizzbuzz ( -> )
	#6501
	&>loop ( length i -- )
		DUP fizz OVR buzz ORA ?{ DUP <dec> }
		<newline>
		INC GTHk ?&>loop
	POP2 BRK
	
%MOD ( a b -- a%b ) { DIVk MUL SUB }
@fizz ( n -- ) #03 MOD ?{ #01 ;Dict/fizz !<str> } #00 JMP2r
@buzz ( n -- ) #05 MOD ?{ #01 ;Dict/buzz !<str> } #00 JMP2r

%<EMIT> ( c -- ) { .Console/write DEO }
@<dec> ( n -- ) DUP #0a DIV /d #0a MOD &d #30 ADD <EMIT> JMP2r
@<str> ( s* -- ) LDAk <EMIT> INC2 LDAk ?<str> POP2 JMP2r

@Dict &fizz "Fizz $1 &buzz "Buzz $1
```

**Output:**

```
01
02
Fizz
04
Buzz
Fizz
07
08
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


## V

```mw
[fizzbuzz
    1 [>=] [
     [[15 % zero?] ['fizzbuzz' puts]
      [5 % zero?]  ['buzz' puts]
      [3 % zero?]  ['fizz' puts]
      [true] [dup puts]
    ] when succ
  ] while].
 |100 fizzbuzz
```

### Second try

(a compiler for fizzbuzz)

define a command that will generate a sequence

```mw
[seq [] swap dup [zero? not] [rolldown [dup] dip cons rollup pred] while pop pop].
```

create a quote that will return a quote that returns a quote if its argument is an integer (A HOF)

```mw
[check [N X F : [[integer?] [[X % zero?] [N F cons] if] if]] view].
```

Create a quote that will make sure that the above quote is applied correctly if given (Number Function) as arguments.

```mw
[func [[N F] : [dup N F check i] ] view map].
```

And apply it

```mw
100 seq [
        [15 [pop 'fizzbuzz' puts]]
        [5  [pop 'buzz' puts]]
        [3  [pop 'fizz' puts]] 
        [1  [puts]]] [func dup] step
        [i true] map pop
```

the first one is much better :)


## Vala

```mw
int main() {
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0) stdout.printf("Fizz\n");
        if (i % 5 == 0) stdout.printf("Buzz\n");
        if (i % 15 == 0) stdout.printf("FizzBuzz\n");
        if (i % 3 != 0 && i % 5 != 0) stdout.printf("%d\n", i);    
          
    }
return 0;;
}
```


## Vale

Works with

:

Vale

version 0.2.0

```mw
import stdlib.*;

exported func main(){
	fizzBuzz(1, 100);
}

func fizzBuzz(i int, stop int) {
	result = if i.mod(3) == 0 {
		"Fizz" } else { ""
	} + if i.mod(5) == 0 {
		"Buzz" } else { ""
	};

	println(if result == "" { i.str() } else { result });

	if i < stop {
		return fizzBuzz(i + 1, stop);
	}
}
```


## VAX Assembly

```mw
                           00000008  0000     1 len	=8
                           00000008  0000     2 msg:	.blkb	len			;output buffer
                           0000000C  0008     3 desc:	.blkl	1			;descriptor lenght field
                           00000000' 000C     4 	.address msg			;pointer to buffer
                           00000012  0010     5 outlen:	.blkw	1
         4C 55 21 0000001A'010E0000' 0012     6 ctr:	.ascid	"!UL"
                                     001D     7 
                               0000  001D     8 .entry	start,0
                            52   7C  001F     9 	clrq	r2			;r2+r3 64bit
                            52   D6  0021    10 	incl	r2			;start index 1
                                     0023    11 loop:
                         E2 AF   B4  0023    12 	clrw	desc			;assume not fizz and or buzz
                    55   D7 AF   9E  0026    13 	movab	msg, r5			;pointer to message buffer
             54   50   52   03   7B  002A    14 	ediv	#3,r2,r0,r4		;divr.rl,divd.rq,quo.wl,rem.wl
                            54   D5  002F    15 	tstl	r4			;remainder
                            0B   12  0031    16 	bneq	not_fizz		;not equal zero
                                     0033    17 
              85   7A7A6966 8F   D0  0033    18 	movl	#^a"fizz", (r5)+	;add to message
                    CA AF   04   A0  003A    19 	addw2	#4, desc		;and update length
                                     003E    20 not_fizz:
             54   50   52   05   7B  003E    21 	ediv	#5,r2,r0,r4
                            54   D5  0043    22 	tstl	r4
                            0B   12  0045    23 	bneq	not_buzz
                                     0047    24 
              85   7A7A7562 8F   D0  0047    25 	movl	#^a"buzz", (r5)+
                    B6 AF   04   A0  004E    26 	addw2	#4, desc
                                     0052    27 not_buzz:
                         B3 AF   B5  0052    28 	tstw	desc			;fizz and or buzz?
                            1B   12  0055    29 	bneq	show_buffer		;neq - yes
                                     0057    30 
                    AD AF   08   B0  0057    31 	movw	#len, desc		;fao length limit
                                     005B    32 	$fao_s -			;eql -no
                                     005B    33 		 ctrstr = ctr, -	;show number
                                     005B    34 		 outlen = outlen, -
                                     005B    35 		 outbuf = desc, -
                                     005B    36 		 p1     = r2
                 96 AF   A0 AF   B0  006D    37 	movw	outlen, desc		;characters filled by fao
                                     0072    38 show_buffer:
                         93 AF   7F  0072    39 	pushaq	desc
              00000000'GF   01   FB  0075    40 	calls	#1, g^lib$put_output
           9F 52   00000064 8F   F3  007C    41 	AOBLEQ	#100,r2,loop		;limit.rl, index.ml
                                 04  0084    42 	ret
                                     0085    43 .end	start
```


## VBA

```mw
Option Explicit

Sub FizzBuzz()
Dim Tb(1 To 100) As Variant
Dim i As Integer
    For i = 1 To 100
        'Tb(i) = i ' move to Else
        If i Mod 15 = 0 Then
            Tb(i) = "FizzBuzz"
        ElseIf i Mod 5 = 0 Then
            Tb(i) = "Buzz"
        ElseIf i Mod 3 = 0 Then
            Tb(i) = "Fizz"
        Else
            Tb(i) = i
        End If
    Next
    Debug.Print Join(Tb, vbCrLf)
End Sub
```

As an alternative, testing each number only once:

```mw
Sub FizzBuzz()
    Dim i As Integer
    Dim T(1 To 99) As Variant
    For i = 1 To 99 Step 3
        T(i + 0) = IIf((i + 0) Mod 5 = 0, "Buzz", i)
        T(i + 1) = IIf((i + 1) Mod 5 = 0, "Buzz", i + 1)
        T(i + 2) = IIf((i + 2) Mod 5 = 0, "FizzBuzz", "Fizz")
    Next i
    Debug.Print Join(T, ", ") & ", Buzz"
End Sub
```


## VBScript

Works with

:

Windows Script Host

version *

```mw
For i = 1 To 100
	If i Mod 15 = 0 Then
		WScript.Echo "FizzBuzz"
	ElseIf i Mod 5 = 0 Then
		WScript.Echo "Buzz"
	ElseIf i Mod 3 = 0 Then
		WScript.Echo "Fizz"
	Else
		WScript.Echo i
	End If
Next
```

##### An Alternative

Works with

:

Windows Script Host

version *

```mw
With WScript.StdOut
	For i = 1 To 100
		If i Mod 3 = 0 Then .Write "Fizz"
		If i Mod 5 = 0 Then .Write "Buzz"
		If .Column = 1 Then .WriteLine i Else .WriteLine ""
	Next
End With
```


## Verbexx

```mw
@LOOP init:{@VAR t3 t5; @VAR i = 1} while:(i <= 100) next:{i++}
{
  t3 = (i % 3 == 0); 
  t5 = (i % 5 == 0);

  @SAY ( @CASE when:(t3 && t5) { 'FizzBuzz }
               when: t3        { 'Fizz     }
               when: t5        { 'Buzz     }
               else:           { i         }           
       );
};
```


## Verilog

```mw
module main;
  integer  number;
  
  initial begin

  for(number = 1; number < 100; number = number + 1) begin
    if (number % 15 == 0) $display("FizzBuzz");
    else begin
      if(number % 3 == 0) $display("Fizz");
      else begin
        if(number % 5 == 0) $display("Buzz");
        else $display(number);
      end
    end
  end
  $finish;
  end
endmodule
```


## VHDL

```mw
entity fizzbuzz is
end entity fizzbuzz;

architecture beh of fizzbuzz is

	procedure fizzbuzz(num : natural) is
	begin
		if num mod 15 = 0 then
			report "FIZZBUZZ";
		elsif num mod 3 = 0 then
			report "FIZZ";
		elsif num mod 5 = 0 then
		    report "BUZZ";
		else
			report to_string(num);
		end if;
	end procedure fizzbuzz;

begin

	p_fizz : process is
	begin
		for i in 1 to 100 loop
		fizzbuzz(i);
		end loop;
		wait for 200 us;
	end process p_fizz;

end architecture beh;
```


## Vim Script

```mw
for i in range(1, 100)
    if i % 15 == 0
        echo "FizzBuzz"
    elseif i % 5 == 0
        echo "Buzz"
    elseif i % 3 == 0
        echo "Fizz"
    else
        echo i
    endif
endfor
```


## Visual Basic .NET

See FizzBuzz/Basic


## Visual Prolog

```mw
implement main
   open core, console

class predicates
   fizzbuzz : (integer) -> string procedure (i).

clauses
    fizzbuzz(X) = S :- X mod 15 = 0, S = "FizzBuzz", !.
    fizzbuzz(X) = S :- X mod 5 = 0, S = "Buzz", !.
    fizzbuzz(X) = S :- X mod 3 = 0, S = "Fizz", !.
    fizzbuzz(X) = S :- S = toString(X).

    run() :-
        foreach X = std::fromTo(1,100) do
            write(fizzbuzz(X)), write("\n")
        end foreach,
        succeed.

end implement main

goal
    console::runUtf8(main::run).
```


## V (Vlang)

Updated for V (Vlang) version 0.2.2

```mw
const (
    fizz = Tuple{true, false}
    buzz = Tuple{false, true}
    fizzbuzz = Tuple{true, true}
)

struct Tuple{
    val1 bool
    val2 bool
}

fn fizz_or_buzz( val int ) Tuple {
    return Tuple{ val % 3 == 0, val % 5 == 0 }
}

fn fizzbuzz( n int ) {
    for i in 1..(n + 1) {
        match fizz_or_buzz(i) {
            fizz { println('Fizz') }
            buzz { println('Buzz') }
            fizzbuzz { println('FizzBuzz') }
            else { println(i) }
        }
    }
}

fn main(){
    fizzbuzz(15)
}
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
11
Fizz
13
14
FizzBuzz
```

Basic example with a for loop and match:

```mw
fn main() {
	mut i := 1
	for i <= 100 {
		match true {
			i % 15 == 0 { println('FizzBuzz') }
			i % 3 == 0  { println('Fizz') }
			i % 5 == 0  { println('Buzz') }
			else { println(i) }
		}
		i++
	}
}
```

Another basic example using the ubiquitous if/else (if) statement:

```mw
fn main() {
	for i in 1..100 {
		if i % 15 == 0 {
			println('FizzBuzz')
		} else if i % 3 == 0  {
			println('Fizz')
		} else if i % 5 == 0 {
			println('Buzz')
		} else {
			println(i)
		}
	}
}
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


## VTL-2

```mw
10 N=1
20 #=30
30 #=N/3*0+%=0*110
40 #=N/5*0+%=0*130
50 #=!+30
60 ?=N
70 ?=""
80 N=N+1
90 #=100>N*20
100 #=999
110 ?="Fizz";
120 #=!
130 ?="Buzz";
140 #=!
180 #=70
```


## Vyxal

```mw
₁⟑₍₃₅kF½*∑∴,
```


## Wart

```mw
for i 1 (i <= 100) ++i
  prn (if (divides i 15)
            "FizzBuzz"
          (divides i 3)
            "Fizz"
          (divides i 5)
            "Buzz"
          :else
            i)
```


## WDTE

```mw
let io => import 'io';
let s => import 'stream';

let multiple of n => == (% n of) 0;

let fizzbuzz n => switch n {
	multiple (* 3 5) => 'FizzBuzz';
	multiple 3 => 'Fizz';
	multiple 5 => 'Buzz';
	default => n;
} -- io.writeln io.stdout;

s.range 1 101 -> s.map fizzbuzz -> s.drain;
```


## Whitespace

See FizzBuzz/EsoLang


## Wortel

```mw
@each &x!console.log x !*&x?{%%x 15 "FizzBuzz" %%x 5 "Buzz" %%x 3 "Fizz" x} @to 100
```


## Wren

```mw
for (i in 1..100) {
    if (i % 15 == 0) {
        System.print("FizzBuzz")
    } else if (i % 3 == 0) {
        System.print("Fizz")
    } else if (i % 5 == 0) {
        System.print("Buzz")
    } else {
        System.print(i)
    }
}
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


## X86 Assembly

```mw
; x86_64 linux nasm

section .bss
number resb 4

section .data
fizz: db "Fizz"
buzz: db "Buzz"
newLine: db 10

section .text
global _start

_start:

  mov rax, 1      ; initialize counter

  loop:
    push rax
    call fizzBuzz
    pop rax
    inc rax
    cmp rax, 100
    jle loop

  mov rax, 60
  mov rdi, 0
  syscall

fizzBuzz:
  mov r10, rax
  mov r15, 0       ; boolean fizz or buzz
  checkFizz:
    xor rdx, rdx   ; clear rdx for division
    mov rbx, 3
    div rbx
    cmp rdx, 0     ; modulo result here
    jne checkBuzz
    mov r15, 1
    mov rsi, fizz
    mov rdx, 4
    mov rax, 1
    mov rdi, 1
    syscall
  checkBuzz:
    mov rax, r10
    xor rdx, rdx
    mov rbx, 5
    div rbx
    cmp rdx, 0
    jne finishLine
    mov r15, 1
    mov rsi, buzz
    mov rdx, 4
    mov rax, 1
    mov rdi, 1
    syscall
  finishLine:      ; print number if no fizz or buzz
    cmp r15, 1
    je nextLine
    mov rax, r10
    call printNum
    ret
    nextLine:
      mov rsi, newLine
      mov rdx, 1
      mov rax, 1
      mov rdi, 1
      syscall
      ret

printNum:          ; write proper digits into number buffer
  cmp rax, 100
  jl lessThanHundred
  mov byte [number], 49
  mov byte [number + 1], 48
  mov byte [number + 2], 48
  mov rdx, 3
  jmp print

  lessThanHundred: ; get digits to write through division 
    xor rdx, rdx
    mov rbx, 10
    div rbx
    add rdx, 48
    cmp rax, 0
    je lessThanTen
    add rax, 48
    mov byte [number], al
    mov byte [number + 1], dl
    mov rdx, 2
    jmp print

  lessThanTen:
    mov byte [number], dl
    mov rdx, 1
  print:
    mov byte [number + rdx], 10   ; add newline
    inc rdx
    mov rax, 1
    mov rdi, 1
    mov rsi, number
    syscall
  ret
```


## XBasic

See FizzBuzz/Basic


## XLISP

```mw
(defun fizzbuzz ()
    (defun fizzb (x y)
        (display (cond
            ((= (mod x 3) (mod x 5) 0) "FizzBuzz")
            ((= (mod x 3) 0) "Fizz")
            ((= (mod x 5) 0) "Buzz")
            (t x)))
        (newline)
        (if (< x y)
            (fizzb (+ x 1) y)))
    (fizzb 1 100))

(fizzbuzz)
```


## XMIDAS

```mw
startmacro
  loop 100 count
    calc/quiet three ^count 3 modulo
    calc/quiet five ^count 5 modulo
    if ^three eq 0 and ^five eq 0
      say "fizzbuzz"
    elseif ^three eq 0
      say "fizz"
    elseif ^five eq 0
      say "buzz"
    else
      say ^count
    endif
  endloop
endmacro
```


## Xojo

```mw
  For i As Integer = 1 To 100
    If i Mod 3 = 0 And i Mod 5 = 0 Then
      Print("FizzBuzz")
    ElseIf i Mod 3 = 0 Then
      Print("Fizz")
    ElseIf i Mod 5 = 0 Then
      Print("Buzz")
    Else
      Print(Str(i))
    End If
  Next
```

An alternative syntax:

```mw
  For i As Integer = 1 To 100
    Select Case True
      Case i Mod 3 = 0 And i Mod 5 = 0
      Print("FizzBuzz")
    Case i Mod 3 = 0
      Print("Fizz")
    Case i Mod 5 = 0
      Print("Buzz")
    Else
      Print(Str(i))
    End Select
  Next
```


## XPath 2.0

```mw
for $n in 1 to 100 return  
  concat('fizz'[not($n mod 3)], 'buzz'[not($n mod 5)], $n[$n mod 15 = (1,2,4,7,8,11,13,14)])
```

...or alternatively...

```mw
for $n in 1 to 100 return 
  ($n, 'Fizz', 'Buzz', 'FizzBuzz')[number(($n mod 3) = 0) + number(($n mod 5) = 0)*2 + 1]
```


## XPL0

```mw
code CrLf=9, IntOut=11, Text=12;
int     N;
[for N:= 1 to 100 do
       [if rem(N/3)=0 then Text(0,"Fizz");
        if rem(N/5)=0 then Text(0,"Buzz")
        else if rem(N/3)#0 then IntOut(0,N);
        CrLf(0);
       ];
]
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
...
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


## XSLT

### XSLT 1.0

Works with

:

xsltproc

version libxslt 10126

```mw
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="text" encoding="utf-8"/>

	<!-- Outputs a line for a single FizzBuzz iteration. -->
	<xsl:template name="fizzbuzz-single">
		<xsl:param name="n"/>
		
		<!-- $s will be "", "Fizz", "Buzz", or "FizzBuzz". -->
		<xsl:variable name="s">
			<xsl:if test="$n mod 3 = 0">Fizz</xsl:if>
			<xsl:if test="$n mod 5 = 0">Buzz</xsl:if>
		</xsl:variable>
		
		<!-- Output $s. If $s is blank, also output $n. -->
		<xsl:value-of select="$s"/>
		<xsl:if test="$s = ''">
			<xsl:value-of select="$n"/>
		</xsl:if>
		
		<!-- End line. -->
		<xsl:value-of select="'&#10;'"/>
	</xsl:template>
	
	<!-- Calls fizzbuzz-single over each value in a range. -->
	<xsl:template name="fizzbuzz-range">
		<!-- Default parameters: From 1 through 100 -->
		<xsl:param name="startAt" select="1"/>
		<xsl:param name="endAt" select="$startAt + 99"/>
		
		<!-- Simulate a loop with tail recursion. -->
		
		<!-- Loop condition -->
		<xsl:if test="$startAt &lt;= $endAt">
			<!-- Loop body -->
			<xsl:call-template name="fizzbuzz-single">
				<xsl:with-param name="n" select="$startAt"/>
			</xsl:call-template>

			<!-- Increment counter, repeat -->
			<xsl:call-template name="fizzbuzz-range">
				<xsl:with-param name="startAt" select="$startAt + 1"/>
				<xsl:with-param name="endAt" select="$endAt"/>
			</xsl:call-template>
		</xsl:if>
	</xsl:template>
	
	<!-- Main procedure -->
	<xsl:template match="/">
		<!-- Default parameters are used -->
		<xsl:call-template name="fizzbuzz-range"/>
	</xsl:template>
</xsl:stylesheet>
```

### XSLT 1.0 With EXSLT

```mw
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:exsl="http://exslt.org/common"
  exclude-result-prefixes="xsl exsl">
<xsl:output method="text"/>

<xsl:template name="FizzBuzz" match="/">
  <xsl:param name="n" select="1" />
  <xsl:variable name="_">
    <_><xsl:value-of select="$n" /></_>
  </xsl:variable>  
  <xsl:apply-templates select="exsl:node-set($_)/_" />
  <xsl:if test="$n < 100">
    <xsl:call-template name="FizzBuzz">
      <xsl:with-param name="n" select="$n + 1" />
    </xsl:call-template>  
  </xsl:if>  
</xsl:template>
      
<xsl:template match="_[. mod 3 = 0]">Fizz
</xsl:template>
      
<xsl:template match="_[. mod 5 = 0]">Buzz
</xsl:template>
      
<xsl:template match="_[. mod 15 = 0]" priority="1">FizzBuzz
</xsl:template>
      
<xsl:template match="_">
  <xsl:value-of select="concat(.,'&#x0A;')" />
</xsl:template>
      
</xsl:stylesheet>
```

### XSLT 2.0

```mw
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text"/>

<xsl:template match="/">
  <xsl:value-of separator="&#x0A;" select="  
    for $n in 1 to 100 return  
      concat('fizz'[not($n mod 3)], 'buzz'[not($n mod 5)], $n[$n mod 15 = (1,2,4,7,8,11,13,14)])"/>
</xsl:template>

</xsl:stylesheet>
```


## Yabasic

See FizzBuzz/Basic


## YAMLScript

```mw
!ys-0

defn main(n=100):
  each x (1 .. n): !:say
    or? _ x:
      str ((x % 3).! &&& 'Fizz'):
          ((x % 5).! &&& 'Buzz')
```

**Output:**

```
$ ys fizzbuzz.ys
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
...
```


## Yorick

### Iterative solution

```mw
for(i = 1; i <= 100; i++) {
    if(i % 3 == 0)
        write, format="%s", "Fizz";
    if(i % 5 == 0)
        write, format="%s", "Buzz";
    if(i % 3 && i % 5)
        write, format="%d", i;
    write, "";
}
```

### Vectorized solution

```mw
output = swrite(format="%d", indgen(100));
output(3::3) = "Fizz";
output(5::5) = "Buzz";
output(15::15) = "FizzBuzz";
write, format="%s\n", output;
```


## Z80 Assembly

See FizzBuzz/Assembly


## Zen C

Zen C offers multiple ways to solve FizzBuzz. Here are two approaches: one using standard `if/else` statements and another using the `match` control flow feature.

### Using if/else

This approach demonstrates Zen C's inclusive range loops (`..=`), basic modulo arithmetic, and implicit string interpolation.

```mw
fn main() {
    for i in 1..=100 {
        if i % 15 == 0 {
            println "FizzBuzz";
        } else if i % 3 == 0 {
            println "Fizz";
        } else if i % 5 == 0 {
            println "Buzz";
        } else {
            println "{i}";
        }
    }
}
```

### Using match

This implementation utilizes the `match` statement, which serves as a powerful alternative to `switch`. It supports multiple value matching on a single branch using commas, and includes a catch-all wildcard (`_`).

```mw
fn main() {
    for i in 1..=100 {
        match i % 15 {
            0           => { println "FizzBuzz" },
            3, 6, 9, 12 => { println "Fizz" },
            5, 10       => { println "Buzz" },
            _           => { println "{i}" },
        }
    }
}
```


## Zig

```mw
const print = @import("std").debug.print;
pub fn main() void {
    
    for(1..101) |i| {
        if (i % 3 == 0 and i % 5 == 0) {
            print("FizzBuzz\n", .{});
        } else if (i % 3 == 0) {
            print("Fizz\n", .{});
        } else if (i % 5 == 0) {
            print("Buzz\n", .{});
        } else {
            print("{}\n", .{i});
        }
    }
}
```


## zkl

```mw
foreach n in ([1..100]) {
   if(n % 3 == 0) print("Fizz");
   if(not (n%5)) "Buzz".print();
   if(n%3 and n%5) print(n);
   println();
}
```

Or, using infinite lazy sequences:

```mw
fcn f(a,b,c){ a+b and a+b or c }
Walker.cycle("","","Fizz").zipWith(f,Walker.cycle("","","","","Buzz"),[1..])
   .walk(100).concat("\n").println();
```

More of the same:

```mw
Walker.cycle(0,0,"Fizz",0,"Buzz","Fizz",0,0,"Fizz","Buzz",0,"Fizz",0,0,"FizzBuzz")
   .zipWith(fcn(a,b){ a or b },[1..]).walk(100).concat("\n").println();
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
11
Fizz
13
14
FizzBuzz
...
```


## ZX Spectrum Basic

Translation of

:

Applesoft BASIC

```mw
10 DEF FN m(a,b)=a-INT (a/b)*b
20 FOR a=1 TO 100
30 LET o$=""
40 IF FN m(a,3)=0 THEN LET o$="Fizz"
50 IF FN m(a,5)=0 THEN LET o$=o$+"Buzz"
60 IF o$="" THEN LET o$=STR$ a
70 PRINT o$
80 NEXT a
```

Retrieved from "

https://rosettacode.org/wiki/FizzBuzz?oldid=405106

"
