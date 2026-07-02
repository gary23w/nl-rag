---
title: "FizzBuzz (part 1/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/7
---

# FizzBuzz

**Task**

Write a program that prints the integers from   **1**   to   **100**   (inclusive).

But:

- for multiples of three,   print   **Fizz**     instead of the number;
- for multiples of five,   print   **Buzz**     instead of the number;
- for multiples of both three and five,   print   **FizzBuzz**     instead of the number.

The   *FizzBuzz*   problem was presented as the lowest level of comprehension required to illustrate adequacy.

**Also see**

- (a blog)   dont-overthink-fizzbuzz
- (a blog)   fizzbuzz-the-programmers-stairway-to-heaven


## 11l

Translation of

:

Python3: Simple

```mw
L(i) 1..100
   I i % 15 == 0
      print(‘FizzBuzz’)
   E I i % 3 == 0
      print(‘Fizz’)
   E I i % 5 == 0
      print(‘Buzz’)
   E
      print(i)
```


## 360 Assembly

See FizzBuzz/Assembly


## 6502 Assembly

See FizzBuzz/Assembly


## 68000 Assembly

See FizzBuzz/Assembly


## 8080 Assembly

See FizzBuzz/Assembly


## 8086 Assembly

See FizzBuzz/Assembly


## 8th

```mw
with: n

: num?  \ n f --   ) 
	if drop else . then ;

\ is m mod n 0? leave the result twice on the stack
: div? \ m n -- f f
	mod 0 = dup ;

: fizz? \ n -- n f
	dup 3 
	div? if "Fizz" .  then ;

: buzz? \ n f -- n f
	over 5 
	div? if "Buzz" .  then or ;

\ print a message as appropriate for the given number:
: fizzbuzz  \ n --
	fizz? buzz? num? 
	space ;

\ iterate from 1 to 100:
' fizzbuzz 1 100 loop 
cr bye
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program FizzBuzz64.s   */

/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"

/*******************************************/
/* Initialized data                        */
/*******************************************/
.data
szMessFizz:        .asciz "Fizz\n"
szMessBuzz:        .asciz "Buzz\n"
szMessFizzBuzz:    .asciz "FizzBuzz\n"
szMessNumber:      .asciz "Number : @ "
szCarriageReturn:  .asciz "\n"
 
/*******************************************/
/* UnInitialized data                      */
/*******************************************/
.bss 
sZoneConv:         .skip 24
/*******************************************/
/*  code section                           */
/*******************************************/
.text
.global main 
main:                           // entry of program 
    mov x10,3                   // divisor 3
    mov x11,5                   // divisor 5
    mov x12,15                  // divisor 15
    mov x13,1                   // indice
1:                              // loop begin
    udiv x14,x13,x12            // multiple 15
    msub x15,x14,x12,x13        // remainder
    cbnz x15,2f                 // zero ?
    mov x0,x13
    ldr x1,qAdrszMessFizzBuzz
    bl displayResult
    b 4f
2:                              // multiple 3
    udiv x14,x13,x10
    msub x15,x14,x10,x13        // remainder
    cbnz x15,3f                 // zero ?
    mov x0,x13
    ldr x1,qAdrszMessFizz
    bl displayResult
    b 4f
3:                               // multiple 5
    udiv x14,x13,x11
    msub x15,x14,x11,x13         // remainder 
    cbnz x15,4f                  // zero ?
    mov x0,x13
    ldr x1,qAdrszMessBuzz
    bl displayResult
4:
    add x13,x13,1                // increment indice 
    cmp x13,100                  // maxi ?
    ble 1b

100:                            // standard end of the program 
    mov x8,EXIT                 // request to exit program
    svc 0                       // perform the system call
qAdrszMessFizzBuzz:        .quad szMessFizzBuzz
qAdrszMessFizz:            .quad szMessFizz
qAdrszMessBuzz:            .quad szMessBuzz
/******************************************************************/
/*     Display résult                                            */ 
/******************************************************************/
/* x0 contains the number*/
/* x1 contains display string address    */
displayResult:
    stp x2,lr,[sp,-16]!            // save  registers
    mov x2,x1
    ldr x1,qAdrsZoneConv           // conversion number
    bl conversion10S               // decimal conversion
    ldr x0,qAdrszMessNumber
    ldr x1,qAdrsZoneConv
    bl strInsertAtCharInc          // insert result at @ character
    bl affichageMess               // display message final
    mov x0,x2
    bl affichageMess 

    ldp x2,lr,[sp],16              // restaur  2 registers
    ret                            // return to address lr x30
qAdrsZoneConv:        .quad sZoneConv
qAdrszMessNumber:     .quad szMessNumber
/********************************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```


## ABAP

### Impure Functional 1

Works with

:

ABAP

version 7.4 SP05 or Above only

```mw
DATA: tab TYPE TABLE OF string.

tab = VALUE #(
  FOR i = 1 WHILE i <= 100 (
    COND string( LET r3 = i MOD 3
                     r5 = i MOD 5 IN
                 WHEN r3 = 0 AND r5 = 0 THEN |FIZZBUZZ|
                 WHEN r3 = 0            THEN |FIZZ|
                 WHEN r5 = 0            THEN |BUZZ|
                 ELSE i ) ) ).

cl_demo_output=>write( tab ).
cl_demo_output=>display( ).
```

### Impure Functional 2

Works with

:

ABAP

version 7.4 SP05 or Above only

```mw
cl_demo_output=>display( value stringtab( for i = 1 until i > 100
                                          let fizz = cond #( when i mod 3 = 0 then |fizz| else space )
                                              buzz = cond #( when i mod 5 = 0 then |buzz| else space )
                                              fb   = |{ fizz }{ buzz }| in
                                         ( switch #( fb when space then i else fb ) ) ) ).
```


## ABC

```mw
HOW TO RETURN fizzbuzz num:
    PUT "" IN result
    PUT {[3]: "Fizz"; [5]: "Buzz"} IN divwords
    FOR div IN keys divwords:
        IF num mod div=0:
            PUT result^divwords[div] IN result
    IF result="":
        PUT num>>0 IN result
    RETURN result

FOR i IN {1..100}:
    WRITE fizzbuzz i/
```


## ACL2

```mw
(defun fizzbuzz-r (i)
   (declare (xargs :measure (nfix (- 100 i))))
   (prog2$
    (cond ((= (mod i 15) 0) (cw "FizzBuzz~%"))
          ((= (mod i 5) 0) (cw "Buzz~%"))
          ((= (mod i 3) 0) (cw "Fizz~%"))
          (t (cw "~x0~%" i)))
    (if (zp (- 100 i))
        nil
        (fizzbuzz-r (1+ i)))))

(defun fizzbuzz () (fizzbuzz-r 1))
```


## Action!

```mw
PROC Main()
  BYTE i,d3,d5

  d3=1 d5=1
  FOR i=1 TO 100
  DO
    IF d3=0 AND d5=0 THEN
      Print("FizzBuzz")
    ELSEIF d3=0 THEN
      Print("Fizz")
    ELSEIF d5=0 THEN
      Print("Buzz")
    ELSE
      PrintB(i)
    FI
    Put(32)
    
    d3==+1 d5==+1
    IF d3=3 THEN d3=0 FI
    IF d5=5 THEN d5=0 FI
  OD
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23
Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44
FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64
Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz
86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```


## ActionScript

The ActionScript solution works just like the JavaScript solution (they share the ECMAScript specification). The difference is that ActionScript has the *trace* command to write out to a console.

```mw
for (var i:int = 1; i <= 100; i++) {
  if (i % 15 == 0)
    trace('FizzBuzz');
  else if (i % 5 == 0)
    trace('Buzz');
  else if (i % 3 == 0)
    trace('Fizz');
  else
    trace(i);
}
```


## Ada

```mw
with Ada.Text_IO; use Ada.Text_IO;
 
procedure Fizzbuzz is
begin
   for I in 1..100 loop
      if I mod 15 = 0 then
         Put_Line("FizzBuzz");
      elsif I mod 5 = 0 then
         Put_Line("Buzz");
      elsif I mod 3 = 0 then
         Put_Line("Fizz");
      else
         Put_Line(Integer'Image(I));
      end if;
   end loop;
end Fizzbuzz;
```


## Agda

```mw
module FizzBuzz where

open import Agda.Builtin.IO using (IO)

open import Agda.Builtin.Unit renaming (⊤ to Unit)

open import Data.Bool using (Bool ; false ; true ; if_then_else_)

open import Data.Nat using (ℕ ; zero ; suc ; _≡ᵇ_ ; _%_)

open import Data.Nat.Show using (show)

open import Data.List using (List ; [] ; _∷_ ; map)

open import Data.String using (String ; _++_ ; unlines)

postulate putStrLn : String -> IO Unit
{-# FOREIGN GHC import qualified Data.Text as T #-}
{-# COMPILE GHC putStrLn = putStrLn . T.unpack #-}

fizz : String
fizz = "Fizz"

buzz : String
buzz = "Buzz"

_isDivisibleBy_ : (n : ℕ) -> (m : ℕ) -> Bool
n isDivisibleBy zero = false
n isDivisibleBy (suc k) = ((n % (suc k)) ≡ᵇ 0)

getTerm : (n : ℕ) -> String
getTerm n =
  if (n isDivisibleBy 15) then (fizz ++ buzz)
  else if (n isDivisibleBy 3) then fizz
  else if (n isDivisibleBy 5) then buzz
  else (show n)

range : (a : ℕ) -> (b : ℕ) -> List (ℕ)
range k zero = []
range k (suc m) = k ∷ (range (suc k) m)

getTerms : (n : ℕ) -> List (String)
getTerms n = map getTerm (range 1 n)

fizzBuzz : String
fizzBuzz = unlines (getTerms 100)

main : IO Unit
main = putStrLn fizzBuzz
```


## ALGOL 68

```mw
main:(
  FOR i TO 100 DO
    printf(($gl$,
      IF i %* 15 = 0 THEN
        "FizzBuzz"
      ELIF i %* 3 = 0 THEN
        "Fizz"
      ELIF i %* 5 = 0 THEN
        "Buzz"
      ELSE
        i
      FI
    ))
  OD
)
```

or simply:

```mw
FOR i TO 100 DO print(((i%*15=0|"FizzBuzz"|:i%*3=0|"Fizz"|:i%*5=0|"Buzz"|i),new line)) OD
```

or only testing for divisibility by 3 and 5 (AND does not shortcut in Algol 68), as suggested in the #NewLISP second sample:

```mw
FOR i TO 100 DO
    IF  IF i MOD 3 = 0 THEN print( "Fizz" ); FALSE ELSE TRUE FI
    AND IF i MOD 5 = 0 THEN print( "Buzz" ); FALSE ELSE TRUE FI
    THEN
        print( ( whole( i, 0 ) ) )
    FI;
    print( ( newline ) )
OD
```


## ALGOL-M

```mw
BEGIN

INTEGER FUNCTION DIVBY(N, D);
INTEGER N;
INTEGER D;
BEGIN
  DIVBY := 1 - (N - D * (N / D));
END;

INTEGER I;
FOR I := 1 STEP 1 UNTIL 100 DO
BEGIN
  IF DIVBY(I, 15) = 1 THEN
    WRITE("FizzBuzz")
  ELSE IF DIVBY(I, 5) = 1 THEN
    WRITE("Buzz")
  ELSE IF DIVBY(I, 3) = 1 THEN
    WRITE("Fizz")
  ELSE
    WRITE(I);
END;

END
```


## ALGOL W

```mw
begin
    i_w := 1; % set integers to print in minimum space %
    for i := 1 until 100 do begin
        if      i rem 15 = 0 then write( "FizzBuzz" )
        else if i rem  5 = 0 then write( "Buzz" )
        else if i rem  3 = 0 then write( "Fizz" )
        else                      write( i )
    end for_i
end.
```


## ANSI BASIC

See FizzBuzz/Basic


## AntLang

```mw
n:{1+ x}map range[100]
s:{a:0eq x mod 3;b:0eq x mod 5;concat apply{1elem x}map{0elem x}hfilter seq[1- max[a;b];a;b]merge seq[str[x];"Fizz";"Buzz"]}map n
echo map s
```


## APEX

```mw
for(integer i=1; i <= 100; i++){
    String output = '';
    if(math.mod(i, 3) == 0) output += 'Fizz';
    if(math.mod(i, 5) == 0) output += 'Buzz';
    if(output != ''){
        System.debug(output);
    } else {
        System.debug(i);
    }
}
```


## APL

### "One number at a time" solutions

Works with

:

Dyalog APL

Works with

:

GNU APL

```mw
⎕io←1
{⎕←∊'Fizz' 'Buzz'⍵/⍨d,⍱/d←0=3 5|⍵}¨⍳100
```

Explanation:

```
⎕io←1                                   Set the index origin to 1; if it were set to 0, the next
                                        step would count from 0 to 99 instead of 1 to 100.

{                                }¨⍳100 Do the thing in braces for each integer from 1 through 100.

                            3 5|⍵       Make a list of the remainders when the current number is
                                        divided by 3 and 5.

                        d←0=            Make it a Boolean vector: true for remainder=0, false
                                        otherwise. Name it d.

                    d,⍱/                Prepend d to the result of reducing itself with NOR, 
                                        yielding a three-element Boolean vector. The first element
                                        is true if the number is divisible by 3; the second if it's
                                        divisible by 5; and the third only if it's divisible by
                                        neither.

    'Fizz' 'Buzz'⍵/⍨                    Use the Boolean vector as a mask to select elements from
                                        a new triple consisting of 'Fizz', 'Buzz', and the current
                                        number. Each of the three elements will be included in the 
                                        selection only if the corresponding Boolean is true.

   ∊                                    Combine the selected elements into one vector/string

 ⎕←                                     And print it out.
```

You may want to prepend `⍬⊣` to the whole thing in GNU to keep it from returning the list as the value of the expression, causing the interpreter to print it out a second time.

```mw
{⍵ 'Fizz' 'Buzz' 'FizzBuzz'[2⊥0=5 3|⍵]}¨1+⍳100
```

A slightly different version that works both in Dyalog and GNU APL -- credit to Aniket Bhattacharyea, posted on codeburst.io (https://codeburst.io/fizzbuzz-in-apl-a193d1954b4b):

```mw
{('FizzBuzz' 'Fizz' 'Buzz',⍵)[(0=15 3 5|⍵)⍳1]}¨⍳100
```

### "Whole array at once" solutions

Slightly different approach that makes use of the Decode function (⊥):

```mw
⎕IO←0
A[I]←1+I←(0⍷A)/⍳⍴A←('FIZZBUZZ' 'FIZZ' 'BUZZ' 0)[2⊥¨×(⊂3 5)|¨1+⍳100]
```

The idea here is to first calculate the residues for all numbers 1..100 after division with both 3 and 5. This generates 100 pairs of numbers a b, where a is either 0,1,2 and b is either 0,1,2,3,4.

These pairs are then put through the sign function which returns 0 for a 0, and a 1 for anything greater than 0. Now we have binary pairs. The binary pairs are encoded with a left argument of 2 resulting in 0,1,2,3. These are treated as indices for the "FizzBuzz vector" where 0 is in position 3.

Variable A holds this new vector of words and zeros. Variable I is assigned the zeros' positions. Finally A[I] is replaced with corresponding indices.

If you have an aversion against mixed vectors, consider inserting ⍕¨ before the final (i.e. left-most) assignment.

A longer one-liner:

```mw
⎕IO←0
(L,'Fizz' 'Buzz' 'FizzBuzz')[¯1+(L×W=0)+W←(100×0≠W)+W←⊃+/1 2×0=3 5|⊂L←1+⍳100]
```

Or equivalently, using At (@) (available in the Dyalog and April dialects) for replacement:

```mw
⎕IO←0
(L,'Fizz' 'Buzz' 'FizzBuzz')[¯1+(100+W[I])@(I←⍸0≠W←⊃+/1 2×0=3 5|⊂L)⊢L←1+⍳100]
```

This version processes the entire array in a single pass rather than using "each". It calculates the residues; then effectively decodes them by base-2 to give numbers in the range [0,3]; then it offsets each non-zero number by 99; then it splices this array with the original numbers 1 through 100. Here are some indices of the final index vector V next to their values :

```
1 2   3 4   5   6 7 8   9  10 11  12 13 14  15 16 ... ⍝ L (1+⍳100)
0 0   2 0   1   2 0 0   2   1  0   2  0  0   3  0 ... ⍝ W (decoded residues)
0 1 101 3 100 101 6 7 101 100 10 101 12 13 102 15 ... ⍝ final index vector
```

Finally this vector is used to index into a 103-length vector consisting of the 100 numbers followed by the FizzBuzz strings. Each number indexes to itself (well, almost; off by one), except that those that are divisible by 3 and/or 5 are offset by 100, into the FizzBuzz strings.

Yet another solution, excessively commented:

Works with

:

GNU_APL

(and Dyalog, with ⎕ML ← 2)

```mw
    ∇ sv ← fizzbuzz n; t;d
[1]   ⍝⍝ Solve the popular 'fizzbuzz' problem in APL.
[2]   ⍝⍝ \param n - highest number to compute (≥0)
[3]   ⍝⍝ \returns sv - a vector of strings representing the fizzbuzz solution for ⍳n
[4]   ⍝⍝     (note we return a string vector to avoid a mixed-type result; remove the
[5]   ⍝⍝     ⍕ function from the (⍕t[⍵]) term to see the difference).
[6]   ⍝⍝⍝⍝
[7]   t←⍳n   ⍝ the sequence 1..n itself which we'll pick from
[8]   ⍝  ... or the words 'fizz', 'buzz', 'fizzbuzz' depending on
[9]   ⍝  ... divisibility by 3 and/or 5
[10]  ⍝⎕←t   ⍝ (Uncomment to see during call)
[11] 
[12]  d←1+(+⌿ ⊃ {((0=3|⍵)) (2×(0=5|⍵))} ⍳n)
[13]  ⍝ || || | |                     | ↓↓
[14]  ⍝ || || | |                     | ⍳n: generate range (1..n)
[15]  ⍝ || || | ↓.....................↓                 ↓↓
[16]  ⍝ || || | A dfn (lambda) taking its right arg (⍵, ⍳n here) to compute two boolean
[17]  ⍝ || || |   vectors(v12): divisibility by 3 and 5, respectively, for each of ⍳n
[18]  ⍝ || || ↓
[19]  ⍝ || || ⊃: Disclose ('lift-up' and pad w/zeros) the 'ragged' matrix of vectors (v12)
[20]  ⍝ || ||    holding divisibility by 3 and 5 of each ⍳n
[21]  ⍝ || ↓↓
[22]  ⍝ || +⌿: Sum (v12) row-wise to count divisibility (0=neither 3 nor 5, 1=3, 2=3 and 5)
[23]  ⍝ ↓↓
[24]  ⍝ 1+: Add one to (v12) to make them 1-based for indexing below:
[25]  ⍝⎕←d
[26] 
[27]  sv ← { ((⍕t[⍵]) 'Fizz' 'Buzz' 'FizzBuzz') [d[⍵]]}¨ ⍳n
[28]  ⍝    | |                                | |    | |
[29]  ⍝    | |                                | ↓....↓ |
[30]  ⍝    | |................................↓  idx   |
[31]  ⍝    | (      lookup output vector      )        |
[32]  ⍝    ↓...........................................↓
[33]  ⍝    A dfn (lambda) taking as its right arg (⍵) ⍳n and using the 'each' (¨)
[34]  ⍝      operator to apply the lambda to each (idx) of ⍳n.
[35] 
[36]  ⍝⍝ USAGE
[37]  ⍝⍝ ⎕ ← ,fizzbuzz 15
[38]  ⍝ 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
    ∇
```


## AppleScript

### Procedural

```mw
property outputText: ""
repeat with i from 1 to 100
  if i mod 15 = 0 then
    set outputText to outputText & "FizzBuzz"
  else if i mod 3 = 0 then
    set outputText to outputText & "Fizz"
  else if i mod 5 = 0 then
    set outputText to outputText & "Buzz"
  else
    set outputText to outputText & i
  end if
  set outputText to outputText & linefeed
end repeat
outputText
```

If this were a useful task requiring a degree of efficiency, it would be better to replace the cumulative text concatenations with additions to a fast-to-access list and coerce this list to text in one go at the end. Less critically, the (i mod … = 0) tests could be nested to reduce the number of these performed from 261 to 200:

```mw
on fizzBuzz(n)
    script o
        property output : {}
    end script
    
    repeat with i from 1 to n
        if (i mod 3 = 0) then
            if (i mod 15 = 0) then
                set end of o's output to "FizzBuzz"
            else
                set end of o's output to "Fizz"
            end if
        else if (i mod 5 = 0) then
            set end of o's output to "Buzz"
        else
            set end of o's output to i
        end if
    end repeat
    
    set astid to AppleScript's text item delimiters
    set AppleScript's text item delimiters to linefeed
    set output to o's output as text
    set AppleScript's text item delimiters to astid
    
    return output
end fizzBuzz

fizzBuzz(100)
```

Another alternative would be simply to fill the list with numbers and then go through it again three times overwriting the relevant slots with the appropriate words:

```mw
on fizzBuzz(n)
    script o
        property output : {}
    end script
    
    repeat with i from 1 to n
        set end of o's output to i
    end repeat
    repeat with x in {{3, "Fizz"}, {5, "Buzz"}, {15, "FizzBuzz"}}
        set {m, t} to x
        repeat with i from m to n by m
            set item i of o's output to t
        end repeat
    end repeat
    
    set astid to AppleScript's text item delimiters
    set AppleScript's text item delimiters to linefeed
    set output to o's output as text
    set AppleScript's text item delimiters to astid
    
    return output
end fizzBuzz

fizzBuzz(100)
```

With the number of numbers raised from 100 to 10,000, the two scripts inserted here take around 0.051 seconds to execute on my current machine, the original AppleScript above around 0.25 seconds, and the one below (originally described as "functional composition") 3.52 seconds.

### Functional

For simplicity, and more efficient use of the scripter's time:

```mw
------------------------- FIZZBUZZ -------------------------

-- fizz :: Int -> Bool
on fizz(n)
    n mod 3 = 0
end fizz

-- buzz :: Int -> Bool
on buzz(n)
    n mod 5 = 0
end buzz

-- fizzAndBuzz :: Int -> Bool
on fizzAndBuzz(n)
    n mod 15 = 0
end fizzAndBuzz

-- fizzBuzz :: Int -> String
on fizzBuzz(x)
    caseOf(x, [[my fizzAndBuzz, "FizzBuzz"], ¬
        [my fizz, "Fizz"], ¬
        [my buzz, "Buzz"]], x as string)
end fizzBuzz

--------------------------- TEST ---------------------------
on run
    
    intercalate(linefeed, ¬
        map(fizzBuzz, enumFromTo(1, 100)))
    
end run

-------------------- GENERIC FUNCTIONS ---------------------

-- caseOf :: a -> [(predicate, b)] -> Maybe b -> Maybe b
on caseOf(e, lstPV, default)
    repeat with lstCase in lstPV
        set {p, v} to contents of lstCase
        if mReturn(p)'s |λ|(e) then return v
    end repeat
    return default
end caseOf

-- enumFromTo :: Int -> Int -> [Int]
on enumFromTo(m, n)
    if m > n then
        set d to -1
    else
        set d to 1
    end if
    set lst to {}
    repeat with i from m to n by d
        set end of lst to i
    end repeat
    return lst
end enumFromTo

-- intercalate :: Text -> [Text] -> Text
on intercalate(strText, lstText)
    set {dlm, my text item delimiters} to {my text item delimiters, strText}
    set strJoined to lstText as text
    set my text item delimiters to dlm
    return strJoined
end intercalate

-- map :: (a -> b) -> [a] -> [b]
on map(f, xs)
    tell mReturn(f)
        set lng to length of xs
        set lst to {}
        repeat with i from 1 to lng
            set end of lst to |λ|(item i of xs, i, xs)
        end repeat
        return lst
    end tell
end map

-- Lift 2nd class handler function into 1st class script wrapper 
-- mReturn :: Handler -> Script
on mReturn(f)
    if class of f is script then
        f
    else
        script
            property |λ| : f
        end script
    end if
end mReturn
```


## Applesoft BASIC

See FizzBuzz/Basic


## Arbre

```mw
fizzbuzz():
  for x in [1..100]
    if x%5==0 and x%3==0
      return "FizzBuzz"
    else
      if x%3==0
        return "Fizz"
      else
        if x%5==0
          return "Buzz"
        else
           return x

main():
  fizzbuzz() -> io
```


## Arc

### Arc 3.1 Base

```mw
(for n 1 100
  (prn:if
    (multiple n 15) 'FizzBuzz
    (multiple n 5) 'Buzz
    (multiple n 3) 'Fizz
    n))
```

```mw
(for n 1 100 
     (prn:check (string (when (multiple n 3) 'Fizz) 
                        (when (multiple n 5) 'Buzz)) 
                ~empty n)) ; check created string not empty, else return n
```

### Waterhouse Arc

```mw
(for n 1 100
  (prn:case (gcd n 15)
    1 n
    3 'Fizz
    5 'Buzz
      'FizzBuzz))
```


## ArkScript

Works with

:

ArkScript

version 4.0.0

```mw
(import std.Range)

(let r (range:range 0 100))
(range:forEach r
  (fun (e)
    (if (= 0 (mod e 15))
      (print "FizzBuzz")
      (if (= 0 (mod e 3))
        (print "Fizz")
        (if (= 0 (mod e 5))
          (print "Buzz")
          (print e))))))
```


## ARM Assembly

```mw
/ * linux GAS */

.global _start

.data

Fizz: .ascii "Fizz\n"
Buzz: .ascii "Buzz\n"
FizzAndBuzz: .ascii "FizzBuzz\n"

numstr_buffer: .skip 3
newLine: .ascii "\n"

.text

_start:

  bl FizzBuzz

  mov r7, #1
  mov r0, #0
  svc #0

FizzBuzz:

  push {lr}
  mov r9, #100

  fizzbuzz_loop:

    mov r0, r9
    mov r1, #15
    bl divide
    cmp r1, #0
    ldreq r1, =FizzAndBuzz
    moveq r2, #9
    beq fizzbuzz_print

    mov r0, r9
    mov r1, #3
    bl divide
    cmp r1, #0
    ldreq r1, =Fizz
    moveq r2, #5
    beq fizzbuzz_print

    mov r0, r9
    mov r1, #5
    bl divide
    cmp r1, #0
    ldreq r1, =Buzz
    moveq r2, #5
    beq fizzbuzz_print

    mov r0, r9
    bl make_num
    mov r2, r1
    mov r1, r0

    fizzbuzz_print:

      mov r0, #1
      mov r7, #4
      svc #0

      sub r9, #1
      cmp r9, #0

    bgt fizzbuzz_loop

  pop {lr}
  mov pc, lr

make_num:

  push {lr}
  ldr r4, =numstr_buffer
  mov r5, #4
  mov r6, #1

  mov r1, #100
  bl divide

  cmp r0, #0
  subeq r5, #1
  movne r6, #0

  add r0, #48
  strb r0, [r4, #0]

  mov r0, r1
  mov r1, #10
  bl divide

  cmp r0, #0
  movne r6, #0
  cmp r6, #1
  subeq r5, #1

  add r0, #48
  strb r0, [r4, #1]

  add r1, #48
  strb r1, [r4, #2]

  mov r2, #4
  sub r0, r2, r5
  add r0, r4, r0
  mov r1, r5

  pop {lr}
  mov pc, lr

divide:
  udiv r2, r0, r1
  mul r3, r1, r2
  sub r1, r0, r3
  mov r0, r2
  mov pc, lr
```


## Arturo

```mw
loop 1..100 [x][
	when [
		zero? x % 15 	-> print "FizzBuzz"
		zero? x % 3		-> print "Fizz"
		zero? x % 5  	-> print "Buzz"
		true   			-> print x
	]
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


## AsciiDots

See FizzBuzz/EsoLang#AsciiDots


## ASIC

See FizzBuzz/Basic


## Asymptote

```mw
for(int number = 1; number <= 100; ++number) {
    if (number % 15 == 0) {
        write("FizzBuzz");
    } else {
      if (number % 3 == 0) {
        write("Fizz");
    } else {
        if (number % 5 == 0) {
        write("Buzz");
    } else {
        write(number);
           }
        }
    }
}
```


## ATS

```mw
#include "share/atspre_staload.hats"

implement main0() = loop(1, 100) where {
  fun loop(from: int, to: int): void =
    if from > to then () else
    let
      val by3 = (from % 3 = 0)
      val by5 = (from % 5 = 0)
    in
      case+ (by3, by5) of
      | (true, true) => print_string("FizzBuzz")
      | (true, false) => print_string("Fizz")
      | (false, true) => print_string("Buzz")
      | (false, false) => print_int(from);
      print_newline();
      loop(from+1, to)
    end
}
```


## AutoHotkey

*Search autohotkey.com*: [1]

```mw
Loop, 100
{
  If (Mod(A_Index, 15) = 0)
    output .= "FizzBuzz`n"
  Else If (Mod(A_Index, 3) = 0)
    output .= "Fizz`n"
  Else If (Mod(A_Index, 5) = 0)
    output .= "Buzz`n"
  Else
    output .= A_Index "`n"
}
FileDelete, output.txt
FileAppend, %output%, output.txt
Run, cmd /k type output.txt
```

A short example with cascading ternary operators and graphical output. Press Esc to close the window.

```mw
Gui, Add, Edit, r20
Gui,Show
Loop, 100
  Send, % (!Mod(A_Index, 15) ? "FizzBuzz" : !Mod(A_Index, 3) ? "Fizz" : !Mod(A_Index, 5) ? "Buzz" : A_Index) "`n"
Return
Esc::
ExitApp
```


## AutoIt

### Example1

Output via MsgBox():

```mw
For $i = 1 To 100
	If Mod($i, 15) = 0 Then
		MsgBox(0, "FizzBuzz", "FizzBuzz")
	ElseIf Mod($i, 5) = 0 Then
		MsgBox(0, "FizzBuzz", "Buzz")
	ElseIf Mod($i, 3) = 0 Then
		MsgBox(0, "FizzBuzz", "Fizz")
	Else
		MsgBox(0, "FizzBuzz", $i)
	EndIf
Next
```

### Example2

Output via console, logfile and/or messagebox:

```mw
#include <Constants.au3>

; uncomment how you want to do the output
Func Out($Msg)
	ConsoleWrite($Msg & @CRLF)

;~	FileWriteLine("FizzBuzz.Log", $Msg)

;~ 	$Btn = MsgBox($MB_OKCANCEL + $MB_ICONINFORMATION, "FizzBuzz", $Msg)
;~ 	If $Btn > 1 Then Exit	; Pressing 'Cancel'-button aborts the program
EndFunc   ;==>Out

Out("# FizzBuzz:")
For $i = 1 To 100
	If Mod($i, 15) = 0 Then
		Out("FizzBuzz")
	ElseIf Mod($i, 5) = 0 Then
		Out("Buzz")
	ElseIf Mod($i, 3) = 0 Then
		Out("Fizz")
	Else
		Out($i)
	EndIf
Next
Out("# Done.")
```


## Avail

```mw
For each i from 1 to 100 do [
    Print:
        if i mod 15 = 0 then ["FizzBuzz"]
        else if i mod 3 = 0 then ["Fizz"]
        else if i mod 5 = 0 then ["Buzz"]
        else [“i”]
        ++ "\n";
];
```


## AWK

See FizzBuzz/AWK


## Axe

```mw
For(I,1,100)
!If I^3??I^5
 Disp "FIZZBUZZ",i
Else!If I^3
 Disp "FIZZ",i
Else!If I^5
 Disp "BUZZ",i
Else
 Disp I▶Dec,i
End
.Pause to allow the user to actually read the output
Pause 1000
End
```


## Babel

```mw
main: 
     { { iter 1 + dup
        
        15 %
            { "FizzBuzz" << 
                zap }
            { dup
            3 % 
                { "Fizz" << 
                    zap }
                { dup
                5 % 
                    { "Buzz" << 
                        zap}
                    { %d << }
                if }
            if }
        if

        "\n" << }

    100 times }
```


## BabyCobol

```mw
      * NB: ANY does not exist in BabyCobol so the elegant
      * EVALUATE-based COBOL-style solution is impossible here.
      * Note the subtly unbalanced IF/ENDs yet valid END at the end.
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FIZZBUZZ.
       DATA DIVISION.
       01 INT PICTURE IS 9(3).
       01 REM LIKE INT.
       01 TMP LIKE INT.
       PROCEDURE DIVISION.
           LOOP VARYING INT TO 100
               DIVIDE 3 INTO INT GIVING TMP REMAINDER REM
               IF REM = 0
               THEN DISPLAY "Fizz" WITH NO ADVANCING
               DIVIDE 5 INTO INT GIVING TMP REMAINDER REM
               IF REM = 0
               THEN DISPLAY "Buzz" WITH NO ADVANCING
               DIVIDE 15 INTO INT GIVING TMP REMAINDER REM
               IF REM = 0
               THEN DISPLAY ""
               ELSE DISPLAY INT
           END.
```


## BaCon

See FizzBuzz/Basic#BaCon


## bash

Any bash hacker would do this as a one liner at the shell, so...

```mw
for n in {1..100}; do ((( n % 15 == 0 )) && echo 'FizzBuzz') || ((( n % 5 == 0 )) && echo 'Buzz') || ((( n % 3 == 0 )) && echo 'Fizz') || echo $n; done
```

For the sake of readability...

```mw
for n in {1..100}; do
  ((( n % 15 == 0 )) && echo 'FizzBuzz') ||
  ((( n % 5 == 0 )) && echo 'Buzz') ||
  ((( n % 3 == 0 )) && echo 'Fizz') ||
  echo $n;
done
```

Here's a very concise approach, with only 75 characters total. Unfortunately it relies on aspects of Bash which are rarely used.

```mw
for i in {1..100};do((i%3))&&x=||x=Fizz;((i%5))||x+=Buzz;echo ${x:-$i};done
```

Here's the concise approach again, this time separated into multiple lines.

```mw
# FizzBuzz in Bash.  A concise version, but with verbose comments.
for i in {1..100} # Use i to loop from "1" to "100", inclusive.
do  ((i % 3)) &&  # If i is not divisible by 3...
        x= ||     # ...blank out x (yes, "x= " does that).  Otherwise,...
        x=Fizz    # ...set (not append) x to the string "Fizz".
    ((i % 5)) ||  # If i is not divisible by 5, skip (there's no "&&")...
        x+=Buzz   # ...Otherwise, append (not set) the string "Buzz" to x.
   echo ${x:-$i}  # Print x unless it is blanked out.  Otherwise, print i.
done
```

It's a bit silly to optimize such a small & fast program, but for the sake of algorithm analysis it's worth noting that the concise approach is reasonably efficient in several ways. Each divisibility test appears in the code exactly once, only two variables are created, and the approach avoids setting variables unnecessarily. As far as I can tell, the divisibility tests only fire the minimum number of times required for the general case (e.g. where the 100/3/5 constants can be changed), unless you introduce more variables and test types. Corrections invited. I avoided analyzing the non-general case where 100/3/5 never change, because one "optimal" solution is to simply print the pre-computed answer,


## BASIC

See FizzBuzz/Basic


## Basic09

See FizzBuzz/Basic


## BASIC256

See FizzBuzz/Basic


## Ballerina

```mw
// https://rosettacode.org/wiki/FizzBuzz
import ballerina/io;

public function main() {
    foreach int i in int:range(1,101,1) {
        if i % 15 == 0 {
            io:println("FizzBuzz");
        } else if i % 5 == 0 {
            io:println("Buzz");
        } else if i % 3 == 0 {
            io:println("Fizz");
        } else {
            io:println(i);
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


## Batch File

FOR /L version:

```mw
@echo off
for /L %%i in (1,1,100) do call :tester %%i
goto :eof

:tester
  set /a test = %1 %% 15
  if %test% NEQ 0 goto :NotFizzBuzz
  echo FizzBuzz
  goto :eof

:NotFizzBuzz
  set /a test = %1 %% 5
  if %test% NEQ 0 goto :NotBuzz
  echo Buzz
  goto :eof

:NotBuzz
  set /a test = %1 %% 3
  if %test% NEQ 0 goto :NotFizz
  echo Fizz
  goto :eof

:NotFizz
  echo %1
```

Loop version:

```mw
@echo off
set n=1

:loop
  call :tester %n%
  set /a n += 1
  if %n% LSS 101 goto loop
  goto :eof

:tester
  set /a test = %1 %% 15
  if %test% NEQ 0 goto :NotFizzBuzz
  echo FizzBuzz
  goto :eof

:NotFizzBuzz
  set /a test = %1 %% 5
  if %test% NEQ 0 goto :NotBuzz
  echo Buzz
  goto :eof

:NotBuzz
  set /a test = %1 %% 3
  if %test% NEQ 0 goto :NotFizz
  echo Fizz
  goto :eof

:NotFizz
  echo %1
```

FOR /L with a block instead of very-high-overhead subroutine call:

```mw
@echo off & setlocal enabledelayedexpansion
for /l %%i in (1,1,100) do (
  set /a m5=%%i %% 5
  set /a m3=%%i %% 3
  set s=
  if !m5! equ 0 set s=!s!Fizz
  if !m3! equ 0 set s=!s!Buzz
  if "!s!"=="" set s=%%i
  echo !s!
)
```

Another For /L solution:

```mw
@echo off
setlocal enableextensions enabledelayedexpansion
for /L %%i in (1,1,100) do (
  set /a "fizz=%%i%%3, buzz=%%i%%5, fizzbuzz=fizz+buzz" %= or fizzbuzz=%%i%%15 =%
  if "!fizzbuzz!"=="0" (echo FizzBuzz
  ) else (if "!fizz!"=="0" (echo Fizz
  ) else (if "!buzz!"=="0" (echo Buzz) else (echo %%i)))
)
```


## BazzBasic

```mw
' ============================================
' FizzBuzz - BazzBasic Edition
' https://rosettacode.org/wiki/FizzBuzz
' BazzBasic: https://github.com/EkBass/BazzBasic
' ============================================
' Print numbers 1 to 100.
' Multiples of 3  -> "Fizz"
' Multiples of 5  -> "Buzz"
' Multiples of both -> "FizzBuzz"
' ============================================

[main]
    FOR n$ = 1 TO 100
        IF MOD(n$, 15) = 0 THEN
            PRINT "FizzBuzz"
        ELSEIF MOD(n$, 3) = 0 THEN
            PRINT "Fizz"
        ELSEIF MOD(n$, 5) = 0 THEN
            PRINT "Buzz"
        ELSE
            PRINT n$
        END IF
    NEXT
END

' Output (first 20 lines):
' 1
' 2
' Fizz
' 4
' Buzz
' Fizz
' 7
' 8
' Fizz
' Buzz
' 11
' Fizz
' 13
' 14
' FizzBuzz
' 16
' 17
' Fizz
' 19
' Buzz
```


## BBC BASIC

See FizzBuzz/Basic


## bc

This solution never uses else, because bc has no else keyword (but some implementations add else as an extension).

```mw
for (i = 1; i <= 100; i++) {
	w = 0
	if (i % 3 == 0) { "Fizz"; w = 1; }
	if (i % 5 == 0) { "Buzz"; w = 1; }
	if (w == 0) i
	if (w == 1) "
"
}
quit
```


## BCPL

```mw
GET "libhdr"

LET start() BE $(

    FOR i=1 TO 100 DO $(

        TEST (i REM 15) = 0 THEN
            writes("FizzBuzz")
        ELSE TEST (i REM 3) = 0 THEN
            writes("Fizz")
        ELSE TEST (i REM 5) = 0 THEN
            writes("Buzz")
        ELSE
            writen(i, 0)

        newline()
    $)
$)
```


## beeswax

Also see on FizzBuzz/EsoLang

“Ordinary” FizzBuzz solution:

```mw
               >     q
        >@F5~%"d@F{  >  @F     q
_1>F3~%'d`Fizz`@F5~%'d >`Buzz`@FNp
  ;bL@~.~4~.5~5@                P<
```

Example without double mod 5 check, using a flag instead, to check if Fizz already got printed (in this case the number n must not be printed if mod 5 is > 0):

```mw
                            >@?q
         >      q       >Ag'd@{?p
_>"1F3~%'d`Fizz`f>@F5~%'d`Buzz`@p
  b            P~;"-~@~.+0~P9@N?<
```


## Befunge

See FizzBuzz/EsoLang


## blz

```mw
for i = 0; i <= 100; i++
    out = ""
    if i % 3 == 0
        out = "Fizz"
    end
    if i % 5 == 0
        out = out + "Buzz"
    end
    if out == ""
        out = i
    end
    print(out)
end
```


## Boo

```mw
def fizzbuzz(size):
    for i in range(1, size):
        if i%15 == 0:
            print 'FizzBuzz'
        elif i%5 == 0:
            print 'Buzz'
        elif i%3 == 0:
            print 'Fizz'
        else:
            print i

fizzbuzz(101)
```


## BQN

```mw
(∾´∾⟜"Fizz"‿"Buzz"/˜·(¬∨´)⊸∾0=3‿5|⊢)¨1+↕100
```

Using the Catch modifier for flow control

```mw
((∾´"fizz"‿"buzz"/˜0=3‿5|⊢)⎊⊢)¨1+↕100
```

Using the Choose combinator with a rank-2 array

```mw
(3‿5 (0=|)◶[⊢‿"fizz","buzz"‿"fizzbuzz"] ⊢)¨ 1+↕100
```


## Bracmat

```mw
0:?i&whl'(1+!i:<101:?i&out$(mod$(!i.3):0&(mod$(!i.5):0&FizzBuzz|Fizz)|mod$(!i.5):0&Buzz|!i))
```

Same code, pretty printed:

```mw
  0:?i
&   whl
  ' ( 1+!i:<101:?i
    &   out
      $ (   mod$(!i.3):0
          & ( mod$(!i.5):0&FizzBuzz
            | Fizz
            )
        | mod$(!i.5):0&Buzz
        | !i
        )
    )
```


## Brainf***

See FizzBuzz/EsoLang


## Brat

```mw
1.to 100 { n |
  true? n % 15 == 0
    { p "FizzBuzz" }
    { true? n % 3 == 0
      { p "Fizz" }
      { true? n % 5 == 0
        { p "Buzz" }
        { p n }
      }
    }
  }
```


## BrightScript (for Roku)

```mw
FOR i = 1 TO 100
	fz = i MOD 3 = 0
	bz = i MOD 5 = 0
	IF fz OR bz
		IF fz AND NOT bz: str = "Fizz"
		ELSEIF bz AND NOT fz: str = "Buzz"
		ELSE str = "FizzBuzz"
		END IF
	ELSE
		str = i.ToStr()
	END IF
	? str
END FOR
```


## Bruijn

```mw
:import std/Combinator .
:import std/String .
:import std/Number .

main [y [[0 =? (+101) case-end case-rec]] (+1)]
	case-rec str ++ "\n" ++ (1 ++0)
		str fizzbuzz "FizzBuzz" (fizz "Fizz" (buzz "Buzz" (number→string 0)))
			fizz =?(0 % (+3))
			buzz =?(0 % (+5))
			fizzbuzz fizz buzz fizz
	case-end empty
```


## C

For 2 prime numbers and based on a similar minimal JavaScript solution with low signal-to-noise, the C code is:

```mw
  int i = 0 ;  char B[88] ;
  while ( i++ < 100 )
    !sprintf( B, "%s%s", i%3 ? "":"Fizz", i%5 ? "":"Buzz" )
    ? sprintf( B, "%d", i ):0, printf( ", %s", B );
```

With 4 prime numbers:

```mw
  int i = 0 ;  char B[88] ;
  while ( i++ < 100 )
    !sprintf( B, "%s%s%s%s", 
       i%3 ? "":"Fiz", i%5 ? "":"Buz", i%7 ? "":"Goz", i%11 ? "":"Kaz" )
    ? sprintf( B, "%d", i ):0, printf( ", %s", B );
```

```mw
Output: ..., 89, FizBuz, Goz, 92, Fiz, 94, Buz, Fiz, 97, Goz, FizKaz, Buz
```

One line version, with pretty printing

```mw
#include <stdio.h>

int main() {
  for (int i=1; i<=105; i++) if (i%3 && i%5) printf("%3d ", i); else printf("%s%s%s", i%3?"":"Fizz", i%5?"":"Buzz", i%15?" ":"\n");
}
```

This actually works (the array init part, saves 6 bytes of static data, whee):

```mw
#include<stdio.h>
 
int main ()
{
  int i;
  const char *s[] = { "%d\n", "Fizz\n", s[3] + 4, "FizzBuzz\n" };
  for (i = 1; i <= 100; i++)
    printf(s[!(i % 3) + 2 * !(i % 5)], i);
  return 0;
}
```

```mw
#include<stdio.h>

int main (void)
{
    int i;
    for (i = 1; i <= 100; i++)
    {
        if (!(i % 15))
            printf ("FizzBuzz");
        else if (!(i % 3))
            printf ("Fizz");
        else if (!(i % 5))
            printf ("Buzz");
        else
            printf ("%d", i);

        printf("\n");
    }
    return 0;
}
```

Implicit int main and return 0 (C99+):

```mw
#include <stdio.h>
 
main() {
  int i = 1;
  while(i <= 100) {
    if(i % 15 == 0)
      puts("FizzBuzz");
    else if(i % 3 == 0)
      puts("Fizz");
    else if(i % 5 == 0)
      puts("Buzz");
    else
      printf("%d\n", i);
    i++;
  }
}
```

obfuscated:

```mw
#include <stdio.h>
#define F(x,y) printf("%s",i%x?"":#y"zz")
int main(int i){for(--i;i++^100;puts(""))F(3,Fi)|F(5,Bu)||printf("%i",i);return 0;}
```

With numbers theory:

```mw
#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 100; ++i) {
        if (i % 3 == 0) printf("fizz");
        if (i % 5 == 0) printf("buzz");
        if (i * i * i * i % 15 == 1) printf("%d", i);
        puts("");
    }
}
```

Without conditionals, anything in the loop body gcc compiles with branching, duplicate tests or duplicate strings. Depends on ASCII and two's complement arithmetic:

```mw
#include <stdio.h>
int main()
{
    for (int i=0;++i<101;puts(""))
    {
        char f[] = "FizzBuzz%d";
        f[8-i%5&12]=0;
        printf (f+(-i%3&4+f[8]/8), i);
    }
}
```


## C3

Translation of

:

C

```mw
module rosettacode;

import std::io;

fn int main(String[] args)
{
	for (int i = 1; i <= 100; i++)
	{
		if (i % 15 == 0)
		{
			io::printn("FizzBuzz");
		}
		else if (i % 5 == 0)
		{
			io::printn("Buzz");
		}
		else if (i % 3 == 0)
		{
			io::printn("Fizz");
		}
		else
		{
			io::printn(i);
		}
	}
	return 0;
}
```
