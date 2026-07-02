---
title: "Sieve of Eratosthenes (part 2/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/21
---

## AutoHotkey

*Search autohotkey.com*: of Eratosthenes Source: AutoHotkey forum by Laszlo

```mw
MsgBox % "12345678901234567890`n" Sieve(20) 

Sieve(n) { ; Sieve of Eratosthenes => string of 0|1 chars, 1 at position k: k is prime 
   Static zero := 48, one := 49 ; Asc("0"), Asc("1") 
   VarSetCapacity(S,n,one) 
   NumPut(zero,S,0,"char") 
   i := 2 
   Loop % sqrt(n)-1 { 
      If (NumGet(S,i-1,"char") = one) 
         Loop % n//i 
            If (A_Index > 1) 
               NumPut(zero,S,A_Index*i-1,"char") 
      i += 1+(i>2) 
   } 
   Return S 
}
```

### Alternative Version

```mw
Sieve_of_Eratosthenes(n){
   arr := []
   loop % n-1
      if A_Index>1
         arr[A_Index] := true

   for i, v in arr   {
      if (i>Sqrt(n))
         break
      else if arr[i]
         while ((j := i*2 + (A_Index-1)*i) < n)
            arr.delete(j)
   }
   return Arr
}
```

Examples:

```mw
n := 101
Arr := Sieve_of_Eratosthenes(n)
loop, % n-1
   output .= (Arr[A_Index] ? A_Index : ".") . (!Mod(A_Index, 10) ? "`n" : "`t")
MsgBox % output
return
```

**Output:**

```
.   2  3  .  5  .  7  .  .  .
11 .  13 .  .  .  17 .  19 .
.  .  23 .  .  .  .  .  29 .
31 .  .  .  .  .  37 .  .  .
41 .  43 .  .  .  47 .  .  .
.  .  53 .  .  .  .  .  59 .
61 .  .  .  .  .  67 .  .  .
71 .  73 .  .  .  .  .  79 .
.  .  83 .  .  .  .  .  89 .
.  .  .  .  .  .  97 .  .  .
```


## AutoIt

```mw
#include <Array.au3>
$M = InputBox("Integer", "Enter biggest Integer")
Global $a[$M], $r[$M], $c = 1
For $i = 2 To $M -1
   If Not $a[$i] Then
      $r[$c] = $i
      $c += 1
      For $k = $i To $M -1 Step $i
         $a[$k] = True
      Next
   EndIf
Next
$r[0] = $c - 1
ReDim $r[$c]
_ArrayDisplay($r)
```


## AWK

An initial array holds all numbers 2..max (which is entered on stdin); then all products of integers are deleted from it; the remaining are displayed in the unsorted appearance of a hash table. Here, the script is entered directly on the commandline, and input entered on stdin:

```
$ awk '{for(i=2;i<=$1;i++) a[i]=1;
>       for(i=2;i<=sqrt($1);i++) for(j=2;j<=$1;j++) delete a[i*j];
>       for(i in a) printf i" "}'
100
71 53 17 5 73 37 19 83 47 29 7 67 59 11 97 79 89 31 13 41 23 2 61 43 3
```

The following variant does not unset non-primes, but sets them to 0, to preserve order in output:

```
$ awk '{for(i=2;i<=$1;i++) a[i]=1;
>       for(i=2;i<=sqrt($1);i++) for(j=2;j<=$1;j++) a[i*j]=0;
>       for(i=2;i<=$1;i++) if(a[i])printf i" "}'
100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

Now with the script from a file, input from commandline as well as stdin, and input is checked for valid numbers:

```mw
# usage:  gawk  -v n=101  -f sieve.awk

function sieve(n) { # print n,":"
   for(i=2; i<=n;      i++) a[i]=1;
   for(i=2; i<=sqrt(n);i++) for(j=2;j<=n;j++) a[i*j]=0;
   for(i=2; i<=n;      i++) if(a[i]) printf i" "
   print ""
}

BEGIN { print "Sieve of Eratosthenes:"
     if(n>1) sieve(n)
   }

   { n=$1+0 }
n<2   { exit }
   { sieve(n) }

END   { print "Bye!" }
```

Here is an alternate version that uses an associative array to record composites with a prime dividing it. It can be considered a slow version, as it does not cross out composites until needed. This version assumes enough memory to hold all primes up to ULIMIT. It prints out noncomposites greater than 1.

```mw
BEGIN {  ULIMIT=100

for ( n=1 ; (n++) < ULIMIT ; ) 
    if (n in S) {
        p = S[n]
        delete S[n]
        for ( m = n ; (m += p) in S ; )  { }
        S[m] = p 
        }
    else  print ( S[(n+n)] = n )
}
```


## Ballerina

```mw
import ballerina/io;

function primes_upto(int lim) returns boolean[] {
    boolean[] is_prime = [];
    foreach int i in 0...lim {
        is_prime.push(i >= 2);
    }
    int upper = <int>((<float> lim).sqrt().ceiling()) + 1;
    foreach int n in int:range(2, upper, 1) {
        if is_prime[n] {
            foreach int i in int:range(n*n, lim+1, n) {
                is_prime[i] = false;
            }
        }
    }
    return is_prime;
}

public function main() {
    foreach any[] [num, cond] in primes_upto(100).enumerate() {
        if cond {
            io:print(num," ");
        }
    }
    io:println();
}
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Bash

*See solutions at UNIX Shell.*


## BASIC

Works with

:

FreeBASIC

Works with

:

RapidQ

```mw
DIM n AS Integer, k AS Integer, limit AS Integer

INPUT "Enter number to search to: "; limit
DIM flags(limit) AS Integer

FOR n = 2 TO SQR(limit)
    IF flags(n) = 0 THEN
        FOR k = n*n TO limit STEP n
            flags(k) = 1
        NEXT k
    END IF
NEXT n

' Display the primes
FOR n = 2 TO limit
    IF flags(n) = 0 THEN PRINT n; ", ";
NEXT n
```

### Applesoft BASIC

```mw
10  INPUT "ENTER NUMBER TO SEARCH TO: ";LIMIT
20  DIM FLAGS(LIMIT)
30  FOR N = 2 TO SQR (LIMIT)
40  IF FLAGS(N) < > 0 GOTO 80
50  FOR K = N * N TO LIMIT STEP N
60  FLAGS(K) = 1
70  NEXT K
80  NEXT N
90  REM  DISPLAY THE PRIMES
100  FOR N = 2 TO LIMIT
110  IF FLAGS(N) = 0 THEN PRINT N;", ";
120  NEXT N
```

### Atari BASIC

Translation of

:

Commodore BASIC

Auto-initialization of arrays is not reliable, so we have to do our own. Also, PRINTing with commas doesn't quite format as nicely as one might hope, so we do a little extra work to keep the columns lined up.

```mw
100 REM SIEVE OF ERATOSTHENES
110 PRINT "LIMIT";:INPUT LI
120 DIM N(LI):FOR I=0 TO LI:N(I)=1:NEXT I
130 SL = SQR(LI)
140 N(0)=0:N(1)=0
150 FOR P=2 TO SL
160  IF N(P)=0 THEN 200
170  FOR I=P*P TO LI STEP P
180    N(I)=0
190  NEXT I
200 NEXT P
210 C=0
220 FOR I=2 TO LI
230   IF N(I)=0 THEN 260
240   PRINT I,:C=C+1
250   IF C=3 THEN PRINT:C=0
260 NEXT I
270 IF C THEN PRINT
```

**Output:**

```
  Ready
  RUN
  LIMIT?100
  2         3         5
  7         11        13
  17        19        23
  29        31        37
  41        43        47
  53        59        61
  67        71        73
  79        83        89
  97
```

### CBASIC

Works with

:

CBASIC 2

Works with

:

CB80

```mw
limit% = 1000
true% = -1
false% = 0
dim flags%(limit%)

print "Finding primes from 2 to"; limit%

rem - all numbers above 1 are potentially prime
for i% = 2 to limit%
  flags%(i%) = true%
next i%

rem - strike out multiples of each prime found
outer.loop.limit% = int%(sqr(limit%))
for i% = 2 to outer.loop.limit%
  if flags%(i%) = true% then \
     for k% = i% * i% to limit% step i%
       if k% <= limit% then flags%(k%) = false%
     next k%
next i%

rem - write out the primes 12 per line
count% = 0
col% = 1
for i% = 2 to limit%
  if flags%(i%) = true% then \
    print using "### "; i%; : \ 
    count% = count% + 1 : \
    col% = col% + 1 
  if col% > 12 then print : col% = 1
next i%
print
print count%; "were found"

end
```

**Output:**

```
Finding primes from 2 to 1000
  2   3   5   7  11  13  17  19  23  29  31  37
 41  43  47  53  59  61  67  71  73  79  83  84
                      <snip>
829 839 853 857 859 863 877 881 883 887 907 911
919 929 937 941 947 953 967 971 997 983 991 997

 168 were found
```

### Commodore BASIC

Since C= BASIC initializes arrays to all zeroes automatically, we avoid needing our own initialization loop by simply letting 0 mean prime and using 1 for composite.

```mw
100 REM SIEVE OF ERATOSTHENES
110 INPUT "LIMIT";LI
120 DIM N(LI)
130 SL = SQR(LI)
140 N(0)=1:N(1)=1
150 FOR P=2 TO SL
160 : IF N(P) THEN 200
170 : FOR I=P*P TO LI STEP P
180 :   N(I)=1
190 : NEXT I
200 NEXT P
210 FOR I=2 TO LI
220 : IF N(I)=0 THEN PRINT I,
230 NEXT I
240 PRINT
```

**Output:**

```
READY.
RUN
LIMIT? 100
 2         3         5         7
 11        13        17        19
 23        29        31        37
 41        43        47        53
 59        61        67        71
 73        79        83        89
 97

READY.
```

### IS-BASIC

```mw
100 PROGRAM "Sieve.bas"
110 LET LIMIT=100
120 NUMERIC T(1 TO LIMIT)
130 FOR I=1 TO LIMIT
140   LET T(I)=0
150 NEXT
160 FOR I=2 TO SQR(LIMIT)
170   IF T(I)<>1 THEN
180     FOR K=I*I TO LIMIT STEP I
190       LET T(K)=1
200     NEXT
210   END IF
220 NEXT
230 FOR I=2 TO LIMIT ! Display the primes
240   IF T(I)=0 THEN PRINT I;
250 NEXT
```

### Locomotive Basic

```mw
10 DEFINT a-z
20 INPUT "Limit";limit
30 DIM f(limit)
40 FOR n=2 TO SQR(limit)
50 IF f(n)=1 THEN 90
60 FOR k=n*n TO limit STEP n
70 f(k)=1
80 NEXT k
90 NEXT n
100 FOR n=2 TO limit
110 IF f(n)=0 THEN PRINT n;",";
120 NEXT
```

### MSX Basic

```mw
5 REM Tested with MSXPen web emulator
6 REM Translated from Rosetta's ZX Spectrum implementation 
10 INPUT "Enter number to search to: ";l
20 DIM p(l)
30 FOR n=2 TO SQR(l)
40 IF p(n)<>0 THEN NEXT n
50 FOR k=n*n TO l STEP n
60 LET p(k)=1
70 NEXT k
80 NEXT n
90 REM Display the primes
100 FOR n=2 TO l
110 IF p(n)=0 THEN PRINT n;", ";
120 NEXT n
```

### Sinclair ZX81 BASIC

If you only have 1k of RAM, this program will work—but you will only be able to sieve numbers up to 101. The program is therefore more useful if you have more memory available.

A note on `FAST` and `SLOW`: under normal circumstances the CPU spends about 3/4 of its time driving the display and only 1/4 doing everything else. Entering `FAST` mode blanks the screen (which we do not want to update anyway), resulting in substantially improved performance; we then return to `SLOW` mode when we have something to print out.

```mw
 10 INPUT L
 20 FAST
 30 DIM N(L)
 40 FOR I=2 TO SQR L
 50 IF N(I) THEN GOTO 90
 60 FOR J=I+I TO L STEP I
 70 LET N(J)=1
 80 NEXT J
 90 NEXT I
100 SLOW
110 FOR I=2 TO L
120 IF NOT N(I) THEN PRINT I;" ";
130 NEXT I
```

### ZX Spectrum Basic

```mw
10 INPUT "Enter number to search to: ";l
20 DIM p(l)
30 FOR n=2 TO SQR l
40 IF p(n)<>0 THEN NEXT n
50 FOR k=n*n TO l STEP n
60 LET p(k)=1
70 NEXT k
80 NEXT n
90 REM Display the primes
100 FOR n=2 TO l
110 IF p(n)=0 THEN PRINT n;", ";
120 NEXT n
```

### QBasic

Works with

:

QBasic

version 1.1

Works with

:

QuickBasic

version 4.5

```mw
limit = 120

DIM flags(limit)
FOR n = 2 TO limit
    flags(n) = 1
NEXT n

PRINT "Prime numbers less than or equal to "; limit; " are: "
FOR n = 2 TO SQR(limit)
    IF flags(n) = 1 THEN
        FOR i = n * n TO limit STEP n
            flags(i) = 0
    NEXT i
    END IF
NEXT n

FOR n = 1 TO limit
    IF flags(n) THEN PRINT USING "####"; n;
NEXT n
```

**Output:**

```
Prime numbers less than or equal to 120 are: 
   2   3   5   7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97 101 103 107 109 113
```

### BASIC256

```mw
arraybase 1
limit = 120

dim  flags(limit)
for n = 2 to limit
    flags[n] = True
next n

print "Prime numbers less than or equal to "; limit; " are: "
for n = 2 to sqr(limit)
    if flags[n] then
        for i = n * n to limit step n
            flags[i] = False
        next i
    end if
next n

for n = 1 to limit
    if flags[n] then print rjust(n,4);
next n
```

**Output:**

```
Prime numbers less than or equal to 120 are: 
   2   3   5   7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97 101 103 107 109 113
```

### True BASIC

Translation of

:

QBasic

```mw
LET limit = 120
DIM flags(0)
MAT redim flags(limit)
FOR n = 2 to limit
    LET flags(n) = 1
NEXT n
PRINT "Prime numbers less than or equal to "; limit; " are: "
FOR n = 2 to sqr(limit)
    IF flags(n) = 1 then
       FOR i = n*n to limit step n
           LET flags(i) = 0
       NEXT i
    END IF
NEXT n
FOR n = 1 to limit
    IF flags(n)<>0 then PRINT  using "####": n;
NEXT n
END
```

**Output:**

```
Same as QBasic entry.
```

### QL SuperBASIC

#### using 'easy way' to 'add' 2n wheels

Translation of

:

ZX Spectrum Basic

Sets h$ to 1 for higher multiples of 2 via `FILL$`, later on sets `STEP` to 2n; replaces Floating Pt array p(z) with string variable h$(z) to sieve out all primes < z=441 (`l`=21) in under 1K, so that h$ is fillable to its maximum (32766), even on a 48K ZX Spectrum if translated back.

```mw
10 INPUT "Enter Stopping Pt for squared factors: ";z
15 LET l=SQR(z)
20 LET h$="10" : h$=h$ & FILL$("01",z)
40      FOR n=3 TO l 
50 IF h$(n): NEXT n
60 FOR k=n*n TO z STEP n+n: h$(k)=1 
80      END FOR n   
90 REM Display the primes     
100 FOR n=2 TO z: IF h$(n)=0: PRINT n;", ";
```

#### 2i wheel emulation of Sinclair ZX81 BASIC

Backward-compatible also on Spectrums, as well as 1K ZX81s for all primes < Z=441. N.B. the `STEP` of 2 in line 40 mitigates line 50's inefficiency when going to 90.

```mw
 10 INPUT Z
 15 LET L=SQR(Z)
 30 LET H$="10"
 32 FOR J=3 TO Z STEP 2
 34 LET H$=H$ & "01"
 36 NEXT J
 40 FOR I=3 TO L STEP 2
 50 IF H$(I)="1" THEN GOTO 90
 60 FOR J=I*I TO Z STEP I+I
 70 LET H$(J)="1"
 80 NEXT J
 90 NEXT I
110 FOR I=2 TO Z
120 IF H$(I)="0" THEN PRINT I!
130 NEXT I
```

#### 2i wheel emulation of Sinclair ZX80 BASIC

. . . with 2:1 compression (of 16-bit integer variables on ZX80s) such that it obviates having to account for any multiple of 2; one has to input odd upper limits on factors to be squared, `L` (=21 at most on 1K ZX80s for all primes till 439).

Backward-compatible on ZX80s after substituting ** for ^ in line 120.

```mw
 10 INPUT L
 15 LET Z=(L+1)*(L- 1)/2
 30 DIM H(Z)
 40 FOR I=3 TO L STEP 2
 50 IF H((I-1)/ 2) THEN GOTO 90
 60 FOR J=I*I TO L*L STEP I+I
 70 LET H((J-1)/ 2)=1
 80 NEXT J
 90 NEXT I
110 FOR I=0 TO Z
120 IF NOT H(I) THEN PRINT 0^I+1+I*2!
130 NEXT I
```

#### Sieve of Sundaram

Objections that the latter emulation has strayed far from the given task are obviously justified. Yet not as obvious is that we are now just a slight transformation away from the Sieve of Sundaram, as transformed as follows: `O` is the highest value for an Index of succesive diagonal elements in Sundaram's matrix, for which H(J) also includes the off-diagonal elements in-between, such that duplicate entries are omitted. Thus, a slightly transformed Sieve of Sundaram is what Eratosthenes' Sieve becomes upon applying all optimisations incorporated into the prior entries for QL SuperBASIC, except for any equivalent to line 50 in them.

Backward-compatible on 1K ZX80s for all primes < 441 (O=10) after substituting ** for ^ in line 120.

```mw
 10 INPUT O
 15 LET Z=2*O*O+O*2
 30 DIM H(Z)
 40 FOR I=1 TO O
 45 LET A=2*I*I+I*2
 50 REM IF H(A) THEN GOTO 90
 60 FOR J=A TO Z STEP 1+I*2
 65 REM IF H(J) THEN GOTO 80
 70 LET H(J)=1
 80 NEXT J
 90 NEXT I 
110 FOR I=0 TO Z
120 IF NOT H(I) THEN PRINT 0^I+1+I*2!
130 NEXT I
```

#### Eulerian optimisation

While slower than the optimised Sieve of Eratosthenes before it, the Sieve of Sundaram above has a compatible compression scheme that's more convenient than the conventional one used beforehand. It is therefore applied below along with Euler's alternative optimisation in a reversed implementation that lacks backward-compatibility to ZX80 BASIC. This program is designed around features & limitations of the QL, yet can be rewritten more efficiently for 1K ZX80s, as they allow integer variables to be parameters of `FOR` statements (& as their 1K of static RAM is equivalent to L1 cache, even in `FAST` mode). That's left as an exercise for ZX80 enthusiasts, who for o%=14 should be able to generate all primes < 841, i.e. 3 orders of (base 2) magnitude above the limit for the program listed under Sinclair ZX81 BASIC. In QL SuperBASIC, o% may at most be 127--generating all primes < 65,025 (almost 2x the upper limit for indices & integer variables used to calculate them ~2x faster than for floating point as used in line 30, after which the integer code mimics an assembly algorithm for the QL's 68008.)

```mw
 
10 INPUT "Enter highest value of diagonal index q%: ";o%
15 LET z%=o%*(2+o%*2) : h$=FILL$(" ",z%+o%) : q%=1 : q=q% : m=z% DIV (2*q%+1)
30 FOR p=m TO q STEP -1: h$((2*q+1)*p+q)="1" 
42 GOTO 87
61 IF h$(p%)="1": GOTO 63
62 IF p%<q%: GOTO 87 : ELSE h$((2*q%+1)*p%+q%)="1"
63 LET p%=p%-1 : GOTO 61
87 LET q%=q%+1 : IF h$(q%)="1": GOTO 87
90 LET p%=z% DIV (2*q%+1) : IF q%<=o%: GOTO 61
100 LET z%=z%-1 : IF z%=0: PRINT N%(z%) : STOP
101 IF h$(z%)=" ": PRINT N%(z%)! 
110 GOTO 100
127 DEF FN N%(i)=0^i+1+i*2
```


## Batch File

```mw
:: Sieve of Eratosthenes for Rosetta Code - PG
@echo off
setlocal ENABLEDELAYEDEXPANSION
setlocal ENABLEEXTENSIONS
rem echo on
set /p n=limit: 
rem set n=100
for /L %%i in (1,1,%n%) do set crible.%%i=1
for /L %%i in (2,1,%n%) do (
  if !crible.%%i! EQU 1 (
    set /A w = %%i * 2
    for /L %%j in (!w!,%%i,%n%) do (
     set crible.%%j=0
   )
  )
)
for /L %%i in (2,1,%n%) do (
  if !crible.%%i! EQU 1 echo %%i 
)
pause
```

**Output:**

```
limit: 100
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

### Optimized solution

https://gist.github.com/tnhung2011/0b4528836098f16fce4da5d7bb40f9da

Optimizations applied:

- Skipping multiples of both 2 and 3 by only checking for 6k-1 and 6k+1 (k >= 1). This is implemented by having two iterations starting at 5 and 7 each and increment by steps of 6.
- Since the above technique cannot be easily applied to printing primes, SET is used to list out all the primes, which would be parsed through to ensure numerical order.
- Stop the sieve at the (approximate) integer square root instead of multiplying towards the end.

Since Batch is limited to 32-bit integers, this script can only calculate to 46340, and complete this in just 7 seconds as opposed to >1 minute for the one above.

```mw
@if defined eratosSort goto sort
@echo off
setlocal enabledelayedexpansion enableextensions
%= Input is either first argument or stdin =%
if "%~1"=="" (
  set /p n=|| goto :eof
  set /a n=n
) else (set /a n=%~1)
(
if %n% lss 2 goto help
if %n% gtr 46340 goto help
%= Guess isqrt using Newton method =%
%= Modified to remove adjustments for negative integers =%
%= www.dostips.com/forum/viewtopic.php?f=3&t=5819&start=15#p43998 =%
set /a "x=(%n%)/(11*1024)+40, x=((%n%)/x+x)>>1, x=((%n%)/x+x)>>1, x=((%n%)/x+x)>>1, x=((%n%)/x+x)>>1, x=((%n%)/x+x)>>1"
for /f "delims==" %%a in ('set . 2^>nul') do set "%%a="
set .2=1
if %n% gtr 2 set .3=1
for %%a in (5 7) do for /l %%i in (%%a,6,%n%) do set .%%i=1
for %%a in (5 7) do for /l %%i in (%%a,6,!x!) do (
  if defined .%%i (
  set /a t=%%i*%%i
  for /l %%j in (!t!,%%i,%n%) do set .%%j=
))
set eratosSort=1
for /f %%i in ('cmd /q /v:on /e:on /d /c "%~f0" ^| sort') do echo/%%i
goto :eof
)
:sort
(
%= Sort numbers =%
%= stackoverflow.com/a/32306526 =%
(for /f "delims=.=" %%i in ('set .') do (
  set "Z=    %%i"
  echo !Z:~-5!
))
goto :eof
)
:help
>&2 echo Numbers should be in range 2-46340. 46341^^2 and greater exceeds 32 bits of precision.
```


## BBC BASIC

```mw
      limit% = 100000
      DIM sieve% limit%
      
      prime% = 2
      WHILE prime%^2 < limit%
        FOR I% = prime%*2 TO limit% STEP prime%
          sieve%?I% = 1
        NEXT
        REPEAT prime% += 1 : UNTIL sieve%?prime%=0
      ENDWHILE
      
      REM Display the primes:
      FOR I% = 1 TO limit%
        IF sieve%?I% = 0 PRINT I%;
      NEXT
```


## bc

```mw
define ero(x){
   
   for(i = 1; i < x; i++) 
      {
      sieve[i]=i+1
       }
   
   for(j = 2; j <= sqrt(x); j++)
   {
      
      if (sieve[j-1]%j==0 && sieve[j-1]!=0)
      {
         for (k=j;k<x;k++)
         {
            if (sieve[k]%j==0) 
            {
               sieve[k]=0
            }
         }
         
       }
   
   }

}

limit=100

sum=0
sth=ero(limit)
sieve[0]=0
for(i = 0; i < limit; i++) 
      {
      if (sieve[i]!=0)
      {
         
         print(sieve[i])
         print " "
      }
       }

print "\n"
quit
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 \
97
```


## BCPL

```mw
get "libhdr"

manifest $( LIMIT = 1000 $)

let sieve(prime,max) be
$(  let i = 2
    0!prime := false
    1!prime := false
    for i = 2 to max do i!prime := true
    while i*i <= max do
    $(  if i!prime do
        $(  let j = i*i
            while j <= max do
            $(  j!prime := false
                j := j + i
            $)
        $)
        i := i + 1
    $)
$)

let start() be
$(  let prime = vec LIMIT
    let col = 0
    sieve(prime, LIMIT)
    for i = 2 to LIMIT do
        if i!prime do
        $(  writef("%I4",i)   
            col := col + 1
            if col rem 20 = 0 then wrch('*N')
        $)
    wrch('*N')
$)
```

**Output:**

```
   2   3   5   7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173
 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281
 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409
 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541
 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659
 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809
 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941
 947 953 967 971 977 983 991 997
```

### Odds-only bit packed array version (64 bit)

This sieve also uses an iterator structure to enumerate the primes in the sieve. It's inspired by the golang bit packed sieve that returns a closure as an iterator. However, BCPL does not support closures, so the code uses an iterator object.

```mw
GET "libhdr"

LET lowbit(n) =
    0 -> -1,
    VALOF {
        // The table is byte packed to conserve space; therefore we must
        // unpack the structure.
        //
        LET deBruijn64 = TABLE
            #x0001300239311C03, #x3D3A322A261D1104,
            #x3E373B2435332B16, #x2D27211E18120C05,
            #x3F2F381B3C292510, #x362334152C20170B,
            #x2E1A280F22141F0A, #x190E13090D080706

        LET x6 = (n & -n) * #x3F79D71B4CB0A89 >> 58
        RESULTIS deBruijn64[x6 >> 3] >> (7 - (x6 & 7) << 3) & #xFF
    }

LET primes_upto(limit) =
    limit < 3 -> 0,
    VALOF {
        LET bit_sz = (limit + 1) / 2 - 1
        LET bit, p = ?, ?
        LET q, r = bit_sz >> 6, bit_sz & #x3F
        LET sz = q - (r > 0)
        LET sieve = getvec(sz)

        // Initialize the array
        FOR i = 0 TO q - 1 DO
            sieve!i := -1
        IF r > 0 THEN sieve!q := ~(-1 << r)
        sieve!sz := -1 // Sentinel value to mark the end -
              // (after sieving, we'll never have 64 consecutive odd primes.)

        // run the sieve
        bit := 0
        {
            WHILE (sieve[bit >> 6] & 1 << (bit & #x3F)) = 0 DO
                bit +:= 1
            p := 2*bit + 3
            q := p*p
            IF q > limit THEN RESULTIS sieve
            r := (q - 3) >> 1
            UNTIL r >= bit_sz DO {
                sieve[r >> 6] &:= ~(1 << (r & #x3F))
                r +:= p
            }
            bit +:= 1
        } REPEAT
    }

MANIFEST { // fields in an iterable
    sieve_start; sieve_bits; sieve_ptr
}

LET prime_iter(sieve) = VALOF {
    LET iter = getvec(2)
    iter!sieve_start := 0
    iter!sieve_bits := sieve!0
    iter!sieve_ptr := sieve
    RESULTIS iter
}

LET nextprime(iter) =
    !iter!sieve_ptr = -1 -> 0,  // guard entry if at the end already
    VALOF {
        LET p, x = ?, ?

        // iter!sieve_start is also a flag to yield 2.
        IF iter!sieve_start = 0 {
            iter!sieve_start := 3
            RESULTIS 2
        }
        x := iter!sieve_bits
        {
            TEST x ~= 0
            THEN {
                p := (lowbit(x) << 1) + iter!sieve_start
                x &:= x - 1
                iter!sieve_bits := x
                RESULTIS p
            }
            ELSE {
                iter!sieve_start +:= 128
                iter!sieve_ptr +:= 1
                x := !iter!sieve_ptr
                IF x = -1 RESULTIS 0
            }
        } REPEAT
    }

LET show(sieve) BE {
    LET iter = prime_iter(sieve)
    LET c, p = 0, ?
    {
        p := nextprime(iter)
        IF p = 0 THEN {
            wrch('*n')
            freevec(iter)
            RETURN
        }
        IF c MOD 10 = 0 THEN wrch('*n')
        c +:= 1
        writef("%8d", p)
    } REPEAT
}

LET start() = VALOF {
    LET n = ?
    LET argv = VEC 20
    LET sz = ?
    LET primes = ?

    sz := rdargs("upto/a/n/p", argv, 20)
    IF sz = 0 RESULTIS 1
    n := !argv!0
    primes := primes_upto(n)
    IF primes = 0 RESULTIS 1 // no array allocated because limit too small
    show(primes)
    freevec(primes)
    RESULTIS 0
}
```

**Output:**

```
$ ./sieve 1000

BCPL 64-bit Cintcode System (13 Jan 2020)
0.000> 
       2       3       5       7      11      13      17      19      23      29
      31      37      41      43      47      53      59      61      67      71
      73      79      83      89      97     101     103     107     109     113
     127     131     137     139     149     151     157     163     167     173
     179     181     191     193     197     199     211     223     227     229
     233     239     241     251     257     263     269     271     277     281
     283     293     307     311     313     317     331     337     347     349
     353     359     367     373     379     383     389     397     401     409
     419     421     431     433     439     443     449     457     461     463
     467     479     487     491     499     503     509     521     523     541
     547     557     563     569     571     577     587     593     599     601
     607     613     617     619     631     641     643     647     653     659
     661     673     677     683     691     701     709     719     727     733
     739     743     751     757     761     769     773     787     797     809
     811     821     823     827     829     839     853     857     859     863
     877     881     883     887     907     911     919     929     937     941
     947     953     967     971     977     983     991     997
0.005> 
```


## Befunge

```
2>:3g" "-!v\  g30          <
 |!`"O":+1_:.:03p>03g+:"O"`|
 @               ^  p3\" ":<
2 234567890123456789012345678901234567890123456789012345678901234567890123456789
```


## Binary Lambda Calculus

The BLC sieve of Eratosthenes as documented at https://github.com/tromp/AIT/blob/master/characteristic_sequences/primes.lam is the 167 bit program

```
00010001100110010100011010000000010110000010010001010111110111101001000110100001110011010000000000101101110011100111111101111000000001111100110111000000101100000110110
```

The infinitely long output is

```
001101010001010001010001000001010000010001010001000001000001010000010001010000010001000001000000010001010001010001000000000000010001000001010000000001010000010000010001000001000001010000000001010001010000000000010000000000010001010001000001010000000001000001000001000001010000010001010000000001000000000000010001010001000000000000010000010000000001010001000001000...
```


## BQN

A more efficient sieve (primes below one billion in around a second) is provided as `PrimesTo` in bqn-libs primes.bqn.

```mw
Primes ← {
  𝕩≤2 ? ↕0 ;             # No primes below 2
  p ← 𝕊⌈√n←𝕩             # Initial primes by recursion
  b ← 2≤↕n               # Initial sieve: no 0 or 1
  E ← {↕∘⌈⌾((𝕩×𝕩+⊢)⁼)n}  # Multiples of 𝕩 under n, starting at 𝕩×𝕩
  / b E⊸{0¨⌾(𝕨⊸⊏)𝕩}´ p   # Cross them out
}
```

**Output:**

```mw
   Primes 100
⟨ 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 ⟩
   ≠∘Primes¨ 10⋆↕7  # Number of primes below 1e0, 1e1, ... 1e6
⟨ 0 4 25 168 1229 9592 78498 ⟩
```


## Bracmat

This solution does not use an array. Instead, numbers themselves are used as variables. The numbers that are not prime are set (to the silly value "nonprime"). Finally all numbers up to the limit are tested for being initialised. The uninitialised (unset) ones must be the primes.

```mw
( ( eratosthenes
  =   n j i
    .   !arg:?n
      & 1:?i
      &   whl
        ' ( (1+!i:?i)^2:~>!n:?j
          & ( !!i
            |   whl
              ' ( !j:~>!n
                & nonprime:?!j
                & !j+!i:?j
                )
            )
          )
      & 1:?i
      &   whl
        ' ( 1+!i:~>!n:?i
          & (!!i|put$(!i " "))
          )
  )
& eratosthenes$100
)
```

**Output:**

2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


## C

Plain sieve, without any optimizations:

```mw
#include <stdlib.h>
#include <math.h>

char*
eratosthenes(int n, int *c)
{
   char* sieve;
   int i, j, m;

   if(n < 2)
      return NULL;

   *c = n-1;     /* primes count */
   m = (int) sqrt((double) n);

   /* calloc initializes to zero */
   sieve = calloc(n+1,sizeof(char));
   sieve[0] = 1;
   sieve[1] = 1;
   for(i = 2; i <= m; i++)
      if(!sieve[i])
         for (j = i*i; j <= n; j += i)
            if(!sieve[j]){
               sieve[j] = 1; 
               --(*c);
            }
   return sieve;
}
```

Possible optimizations include sieving only odd numbers (or more complex wheels), packing the sieve into bits to improve locality (and allow larger sieves), etc.

**Another example:**

We first fill ones into an array and assume all numbers are prime. Then, in a loop, fill zeroes into those places where i * j is less than or equal to n (number of primes requested), which means they have multiples! To understand this better, look at the output of the following example.

To print this back, we look for ones in the array and only print those spots.

```mw
#include <stdio.h>
#include <malloc.h>
void sieve(int *, int);

int main(int argc, char *argv)
{
    int *array, n=10;
    array =(int *)malloc((n + 1) * sizeof(int));
    sieve(array,n);
    return 0;
}

void sieve(int *a, int n)
{
    int i=0, j=0;

    for(i=2; i<=n; i++) {
        a[i] = 1;
    }

    for(i=2; i<=n; i++) {
        printf("\ni:%d", i);
        if(a[i] == 1) {
            for(j=i; (i*j)<=n; j++) {
                printf ("\nj:%d", j);
                printf("\nBefore a[%d*%d]: %d", i, j, a[i*j]);
                a[(i*j)] = 0;
                printf("\nAfter a[%d*%d]: %d", i, j, a[i*j]);
            }
        }
    }

    printf("\nPrimes numbers from 1 to %d are : ", n);
    for(i=2; i<=n; i++) {
        if(a[i] == 1)
            printf("%d, ", i);
    }
    printf("\n\n");
}
```

**Output:**

```mw
i:2
j:2
Before a[2*2]: 1
After a[2*2]: 0
j:3
Before a[2*3]: 1
After a[2*3]: 0
j:4
Before a[2*4]: 1
After a[2*4]: 0
j:5
Before a[2*5]: 1
After a[2*5]: 0
i:3
j:3
Before a[3*3]: 1
After a[3*3]: 0
i:4
i:5
i:6
i:7
i:8
i:9
i:10
Primes numbers from 1 to 10 are : 2, 3, 5, 7,
```


## C

Works with

:

C#

version 2.0+

```mw
using System;
using System.Collections;
using System.Collections.Generic;

namespace SieveOfEratosthenes
{
    class Program
    {
        static void Main(string[] args)
        {
            int maxprime = int.Parse(args[0]);
            var primelist = GetAllPrimesLessThan(maxprime);
            foreach (int prime in primelist)
            {
                Console.WriteLine(prime);
            }
            Console.WriteLine("Count = " + primelist.Count);
            Console.ReadLine();
        }

        private static List<int> GetAllPrimesLessThan(int maxPrime)
        {
            var primes = new List<int>();
            var maxSquareRoot = (int)Math.Sqrt(maxPrime);
            var eliminated = new BitArray(maxPrime + 1);

            for (int i = 2; i <= maxPrime; ++i)
            {
                if (!eliminated[i])
                {
                    primes.Add(i);
                    if (i <= maxSquareRoot)
                    {
                        for (int j = i * i; j <= maxPrime; j += i)
                        {
                            eliminated[j] = true;
                        }
                    }
                }
            }
            return primes;
        }
    }
}
```

### Richard Bird Sieve

Translation of

:

F#

To show that C# code can be written in somewhat functional paradigms, the following in an implementation of the Richard Bird sieve from the Epilogue of [Melissa E. O'Neill's definitive article](http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf) in Haskell:

```mw
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using PrimeT = System.UInt32;
  class PrimesBird : IEnumerable<PrimeT> {
    private struct CIS<T> {
      public T v; public Func<CIS<T>> cont;
      public CIS(T v, Func<CIS<T>> cont) {
        this.v = v; this.cont = cont;
      }
    }
    private CIS<PrimeT> pmlts(PrimeT p) {
      Func<PrimeT, CIS<PrimeT>> fn = null;
      fn = (c) => new CIS<PrimeT>(c, () => fn(c + p));
      return fn(p * p);
    }
    private CIS<CIS<PrimeT>> allmlts(CIS<PrimeT> ps) {
      return new CIS<CIS<PrimeT>>(pmlts(ps.v), () => allmlts(ps.cont())); }
    private CIS<PrimeT> merge(CIS<PrimeT> xs, CIS<PrimeT> ys) {
      var x = xs.v; var y = ys.v;
      if (x < y) return new CIS<PrimeT>(x, () => merge(xs.cont(), ys));
      else if (y < x) return new CIS<PrimeT>(y, () => merge(xs, ys.cont()));
      else return new CIS<PrimeT>(x, () => merge(xs.cont(), ys.cont()));
    }
    private CIS<PrimeT> cmpsts(CIS<CIS<PrimeT>> css) {
      return new CIS<PrimeT>(css.v.v, () => merge(css.v.cont(), cmpsts(css.cont()))); }
    private CIS<PrimeT> minusat(PrimeT n, CIS<PrimeT> cs) {
      var nn = n; var ncs = cs;
      for (; ; ++nn) {
        if (nn >= ncs.v) ncs = ncs.cont();
        else return new CIS<PrimeT>(nn, () => minusat(++nn, ncs));
      }
    }
    private CIS<PrimeT> prms() {
      return new CIS<PrimeT>(2, () => minusat(3, cmpsts(allmlts(prms())))); }
    public IEnumerator<PrimeT> GetEnumerator() {
      for (var ps = prms(); ; ps = ps.cont()) yield return ps.v;
    }
    IEnumerator IEnumerable.GetEnumerator() { return (IEnumerator)GetEnumerator(); }
  }
```

### Tree Folding Sieve

Translation of

:

F#

The above code can easily be converted to "**odds-only**" and a infinite tree-like folding scheme with the following minor changes:

```mw
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using PrimeT = System.UInt32;
  class PrimesTreeFold : IEnumerable<PrimeT> {
    private struct CIS<T> {
      public T v; public Func<CIS<T>> cont;
      public CIS(T v, Func<CIS<T>> cont) {
        this.v = v; this.cont = cont;
      }
    }
    private CIS<PrimeT> pmlts(PrimeT p) {
      var adv = p + p;
      Func<PrimeT, CIS<PrimeT>> fn = null;
      fn = (c) => new CIS<PrimeT>(c, () => fn(c + adv));
      return fn(p * p);
    }
    private CIS<CIS<PrimeT>> allmlts(CIS<PrimeT> ps) {
      return new CIS<CIS<PrimeT>>(pmlts(ps.v), () => allmlts(ps.cont()));
    }
    private CIS<PrimeT> merge(CIS<PrimeT> xs, CIS<PrimeT> ys) {
      var x = xs.v; var y = ys.v;
      if (x < y) return new CIS<PrimeT>(x, () => merge(xs.cont(), ys));
      else if (y < x) return new CIS<PrimeT>(y, () => merge(xs, ys.cont()));
      else return new CIS<PrimeT>(x, () => merge(xs.cont(), ys.cont()));
    }
    private CIS<CIS<PrimeT>> pairs(CIS<CIS<PrimeT>> css) {
      var nxtcss = css.cont();
      return new CIS<CIS<PrimeT>>(merge(css.v, nxtcss.v), () => pairs(nxtcss.cont())); }
    private CIS<PrimeT> cmpsts(CIS<CIS<PrimeT>> css) {
      return new CIS<PrimeT>(css.v.v, () => merge(css.v.cont(), cmpsts(pairs(css.cont()))));
    }
    private CIS<PrimeT> minusat(PrimeT n, CIS<PrimeT> cs) {
      var nn = n; var ncs = cs;
      for (; ; nn += 2) {
        if (nn >= ncs.v) ncs = ncs.cont();
        else return new CIS<PrimeT>(nn, () => minusat(nn + 2, ncs));
      }
    }
    private CIS<PrimeT> oddprms() {
      return new CIS<PrimeT>(3, () => minusat(5, cmpsts(allmlts(oddprms()))));
    }
    public IEnumerator<PrimeT> GetEnumerator() {
      yield return 2;
      for (var ps = oddprms(); ; ps = ps.cont()) yield return ps.v;
    }
    IEnumerator IEnumerable.GetEnumerator() { return (IEnumerator)GetEnumerator(); }
  }
```

The above code runs over ten times faster than the original Richard Bird algorithm.

### Priority Queue Sieve

Translation of

:

F#

First, an implementation of a Min Heap Priority Queue is provided as extracted from the entry at RosettaCode, with only the necessary methods duplicated here:

```mw
namespace PriorityQ {
  using KeyT = System.UInt32;
  using System;
  using System.Collections.Generic;
  using System.Linq;
  class Tuple<K, V> { // for DotNet 3.5 without Tuple's
    public K Item1; public V Item2;
    public Tuple(K k, V v) { Item1 = k; Item2 = v; }
    public override string ToString() {
      return "(" + Item1.ToString() + ", " + Item2.ToString() + ")";
    }
  }
  class MinHeapPQ<V> {
    private struct HeapEntry {
      public KeyT k; public V v;
      public HeapEntry(KeyT k, V v) { this.k = k; this.v = v; }
    }
    private List<HeapEntry> pq;
    private MinHeapPQ() { this.pq = new List<HeapEntry>(); }
    private bool mt { get { return pq.Count == 0; } }
    private Tuple<KeyT, V> pkmn {
      get {
        if (pq.Count == 0) return null;
        else {
          var mn = pq[0];
          return new Tuple<KeyT, V>(mn.k, mn.v);
        }
      }
    }
    private void psh(KeyT k, V v) { // add extra very high item if none
      if (pq.Count == 0) pq.Add(new HeapEntry(UInt32.MaxValue, v));
      var i = pq.Count; pq.Add(pq[i - 1]); // copy bottom item...
      for (var ni = i >> 1; ni > 0; i >>= 1, ni >>= 1) {
        var t = pq[ni - 1];
        if (t.k > k) pq[i - 1] = t; else break;
      }
      pq[i - 1] = new HeapEntry(k, v);
    }
    private void siftdown(KeyT k, V v, int ndx) {
      var cnt = pq.Count - 1; var i = ndx;
      for (var ni = i + i + 1; ni < cnt; ni = ni + ni + 1) {
        var oi = i; var lk = pq[ni].k; var rk = pq[ni + 1].k;
        var nk = k;
        if (k > lk) { i = ni; nk = lk; }
        if (nk > rk) { ni += 1; i = ni; }
        if (i != oi) pq[oi] = pq[i]; else break;
      }
      pq[i] = new HeapEntry(k, v);
    }
    private void rplcmin(KeyT k, V v) {
      if (pq.Count > 1) siftdown(k, v, 0); }
    public static MinHeapPQ<V> empty { get { return new MinHeapPQ<V>(); } }
    public static Tuple<KeyT, V> peekMin(MinHeapPQ<V> pq) { return pq.pkmn; }
    public static MinHeapPQ<V> push(KeyT k, V v, MinHeapPQ<V> pq) {
      pq.psh(k, v); return pq; }
    public static MinHeapPQ<V> replaceMin(KeyT k, V v, MinHeapPQ<V> pq) {
      pq.rplcmin(k, v); return pq; }
}
```

### Restricted Base Primes Queue

The following code implements an improved version of the **odds-only** O'Neil algorithm, which provides the improvements of only adding base prime composite number streams to the queue when the sieved number reaches the square of the base prime (saving a huge amount of memory and considerable execution time, including not needing as wide a range of a type for the internal prime numbers) as well as minimizing stream processing using fusion:

```mw
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using PrimeT = System.UInt32;
  class PrimesPQ : IEnumerable<PrimeT> {
    private IEnumerator<PrimeT> nmrtr() {
      MinHeapPQ<PrimeT> pq = MinHeapPQ<PrimeT>.empty;
      PrimeT bp = 3; PrimeT q = 9;
      IEnumerator<PrimeT> bps = null;
      yield return 2; yield return 3;
      for (var n = (PrimeT)5; ; n += 2) {
        if (n >= q) { // always equal or less...
          if (q <= 9) {
            bps = nmrtr();
            bps.MoveNext(); bps.MoveNext(); } // move to 3...
          bps.MoveNext(); var nbp = bps.Current; q = nbp * nbp;
          var adv = bp + bp; bp = nbp;
          pq = MinHeapPQ<PrimeT>.push(n + adv, adv, pq);
        }
        else {
          var pk = MinHeapPQ<PrimeT>.peekMin(pq);
          var ck = (pk == null) ? q : pk.Item1;
          if (n >= ck) {
            do { var adv = pk.Item2;
                  pq = MinHeapPQ<PrimeT>.replaceMin(ck + adv, adv, pq);
                  pk = MinHeapPQ<PrimeT>.peekMin(pq); ck = pk.Item1;
            } while (n >= ck);
          }
          else yield return n;
        }
      }
    }
    public IEnumerator<PrimeT> GetEnumerator() { return nmrtr(); }
    IEnumerator IEnumerable.GetEnumerator() { return (IEnumerator)GetEnumerator(); }
  }
```

The above code is at least about 2.5 times faster than the Tree Folding version.

### Dictionary (Hash table) Sieve

The above code adds quite a bit of overhead in having to provide a version of a Priority Queue for little advantage over a Dictionary (hash table based) version as per the code below:

```mw
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using PrimeT = System.UInt32;
  class PrimesDict : IEnumerable<PrimeT> {
    private IEnumerator<PrimeT> nmrtr() {
      Dictionary<PrimeT, PrimeT> dct = new Dictionary<PrimeT, PrimeT>();
      PrimeT bp = 3; PrimeT q = 9;
      IEnumerator<PrimeT> bps = null;
      yield return 2; yield return 3;
      for (var n = (PrimeT)5; ; n += 2) {
        if (n >= q) { // always equal or less...
          if (q <= 9) {
            bps = nmrtr();
            bps.MoveNext(); bps.MoveNext();
          } // move to 3...
          bps.MoveNext(); var nbp = bps.Current; q = nbp * nbp;
          var adv = bp + bp; bp = nbp;
          dct.Add(n + adv, adv);
        }
        else {
          if (dct.ContainsKey(n)) {
            PrimeT nadv; dct.TryGetValue(n, out nadv); dct.Remove(n); var nc = n + nadv;
            while (dct.ContainsKey(nc)) nc += nadv;
            dct.Add(nc, nadv);
          }
          else yield return n;
        }
      }
    }
    public IEnumerator<PrimeT> GetEnumerator() { return nmrtr(); }
    IEnumerator IEnumerable.GetEnumerator() { return (IEnumerator)GetEnumerator(); }
  }
```

The above code runs in about three quarters of the time as the above Priority Queue based version for a range of a million primes which will fall even further behind for increasing ranges due to the Dictionary providing O(1) access times as compared to the O(log n) access times for the Priority Queue; the only slight advantage of the PQ based version is at very small ranges where the constant factor overhead of computing the table hashes becomes greater than the "log n" factor for small "n".

### Best performance: CPU-Cache-Optimized Segmented Sieve

All of the above unbounded versions are really just an intellectual exercise as with very little extra lines of code above the fastest Dictionary based version, one can have an bit-packed page-segmented array based version as follows:

```mw
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using PrimeT = System.UInt32;
  class PrimesPgd : IEnumerable<PrimeT> {
    private const int PGSZ = 1 << 14; // L1 CPU cache size in bytes
    private const int BFBTS = PGSZ * 8; // in bits
    private const int BFRNG = BFBTS * 2;
    public IEnumerator<PrimeT> nmrtr() {
      IEnumerator<PrimeT> bps = null;
      List<uint> bpa = new List<uint>();
      uint[] cbuf = new uint[PGSZ / 4]; // 4 byte words
      yield return 2;
      for (var lowi = (PrimeT)0; ; lowi += BFBTS) {
        for (var bi = 0; ; ++bi) {
          if (bi < 1) {
            if (bi < 0) { bi = 0; yield return 2; }
            PrimeT nxt = 3 + lowi + lowi + BFRNG;
            if (lowi <= 0) { // cull very first page
              for (int i = 0, p = 3, sqr = 9; sqr < nxt; i++, p += 2, sqr = p * p)
                if ((cbuf[i >> 5] & (1 << (i & 31))) == 0)
                  for (int j = (sqr - 3) >> 1; j < BFBTS; j += p)
                    cbuf[j >> 5] |= 1u << j;
            }
            else { // cull for the rest of the pages
              Array.Clear(cbuf, 0, cbuf.Length);
              if (bpa.Count == 0) { // inite secondar base primes stream
                bps = nmrtr(); bps.MoveNext(); bps.MoveNext();
                bpa.Add((uint)bps.Current); bps.MoveNext();
              } // add 3 to base primes array
              // make sure bpa contains enough base primes...
              for (PrimeT p = bpa[bpa.Count - 1], sqr = p * p; sqr < nxt; ) {
                p = bps.Current; bps.MoveNext(); sqr = p * p; bpa.Add((uint)p);
              }
              for (int i = 0, lmt = bpa.Count - 1; i < lmt; i++) {
                var p = (PrimeT)bpa[i]; var s = (p * p - 3) >> 1;
                // adjust start index based on page lower limit...
                if (s >= lowi) s -= lowi;
                else {
                  var r = (lowi - s) % p;
                  s = (r != 0) ? p - r : 0;
                }
                for (var j = (uint)s; j < BFBTS; j += p)
                  cbuf[j >> 5] |= 1u << ((int)j);
              }
            }
          }
          while (bi < BFBTS && (cbuf[bi >> 5] & (1 << (bi & 31))) != 0) ++bi;
          if (bi < BFBTS) yield return 3 + (((PrimeT)bi + lowi) << 1);
          else break; // outer loop for next page segment...
        }
      }
    }
    public IEnumerator<PrimeT> GetEnumerator() { return nmrtr(); }
    IEnumerator IEnumerable.GetEnumerator() { return (IEnumerator)GetEnumerator(); }
  }
```

The above code is about 25 times faster than the Dictionary version at computing the first about 50 million primes (up to a range of one billion), with the actual enumeration of the result sequence now taking longer than the time it takes to cull the composite number representation bits from the arrays, meaning that it is over 50 times faster at actually sieving the primes. The code owes its speed as compared to a naive "one huge memory array" algorithm to using an array size that is the size of the CPU L1 or L2 caches and using bit-packing to fit more number representations into this limited capacity; in this way RAM memory access times are reduced by a factor of from about four to about 10 (depending on CPU and RAM speed) as compared to those naive implementations, and the minor computational cost of the bit manipulations is compensated by a large factor in total execution time.

The time to enumerate the result primes sequence can be reduced somewhat (about a second) by removing the automatic iterator "yield return" statements and converting them into a "roll-your-own" IEnumerable<PrimeT> implementation, but for page segmentation of **odds-only**, this iteration of the results will still take longer than the time to actually cull the composite numbers from the page arrays.

In order to make further gains in speed, custom methods must be used to avoid using iterator sequences. If this is done, then further gains can be made by extreme wheel factorization (up to about another about four times gain in speed) and multi-processing (with another gain in speed proportional to the actual independent CPU cores used).

Note that all of these gains in speed are not due to C# other than it compiles to reasonably efficient machine code, but rather to proper use of the Sieve of Eratosthenes algorithm.

All of the above unbounded code can be tested by the following "main" method (replace the name "PrimesXXX" with the name of the class to be tested):

```mw
    static void Main(string[] args) {
      Console.WriteLine(new PrimesXXX().ElementAt(1000000 - 1)); // zero based indexing...
    }
```

To produce the following output for all tested versions (although some are considerably faster than others):

**Output:**

```
15485863
```
