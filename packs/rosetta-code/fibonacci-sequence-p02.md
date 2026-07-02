---
title: "Fibonacci sequence (part 2/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/10
---

## AWK

As in many examples, this one-liner contains the function as well as testing with input from stdin, output to stdout.

```mw
$ awk 'func fib(n){return(n<2?n:fib(n-1)+fib(n-2))}{print "fib("$1")="fib($1)}'
10
fib(10)=55
```


## Axe

A recursive solution is not practical in Axe because there is no concept of variable scope in Axe.

Iterative solution:

```mw
Lbl FIB
r₁→N
0→I
1→J
For(K,1,N)
 I+J→T
 J→I
 T→J
End
J
Return
```


## Babel

In Babel, we can define fib using a stack-based approach that is not recursive:

```mw
fib { <- 0 1 { dup <- + -> swap } -> times zap } <
```

foo x < puts x in foo. In this case, x is the code list between the curly-braces. This is how you define callable code in Babel. The definition works by initializing the stack with 0, 1. On each iteration of the times loop, the function duplicates the top element. In the first iteration, this gives 0, 1, 1. Then it moves down the stack with the <- operator, giving 0, 1 again. It adds, giving 1. then it moves back up the stack, giving 1, 1. Then it swaps. On the next iteration this gives:

```
1, 1, 1 (dup)  
1, 1, (<-)  
2 (+)  
2, 1 (->)  
1, 2 (swap)  
```

And so on. To test fib:

```mw
{19 iter - fib !} 20 times collect ! lsnum !
```

**Output:**

```
( 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 )
```


## Ballerina

Translation of

:

11l

```mw
// https://rosettacode.org/wiki/Fibonacci_sequence
import ballerina/io;
function fib_iter(int n) returns int {
    if (n < 2) {
        return n;
    }
    int fib_prev = 1;
    int fib = 1;
    int temp = 0;
    foreach int _ in int:range(2, n, 1) {
        temp = fib;
        fib  = fib_prev + fib;
        fib_prev = temp;
    }
    return fib;
}

public function main() {
    foreach int i in int:range(1, 21, 1) {
        io:println(fib_iter(i));
    }
}
```

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
610
987
1597
2584
4181
6765
```


## bash

### Iterative

```mw
$ fib=1;j=1;while((fib<100));do echo $fib;((k=fib+j,fib=j,j=k));done
```

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
```

### Recursive

```mw
fib()
{
  if [ $1 -le 0 ]
  then
    echo 0
    return 0
  fi
  if [ $1 -le 2 ]
  then
    echo 1
  else
    a=$(fib $[$1-1])
    b=$(fib $[$1-2])
    echo $(($a+$b))
  fi
}
```


## BASIC

### ANSI BASIC

Translation of

:

MoonRock

Works with

:

Decimal BASIC

```mw
100 REM Fibonacci sequence
110 DECLARE EXTERNAL FUNCTION Fib
120 INPUT PROMPT "Enter n for fib(n): ": N 
130 PRINT Fib(N)
140 END
150 REM ***
160 EXTERNAL FUNCTION Fib(N)
170 IF N = 0 THEN
180    LET Fib = 0
190 ELSEIF N = 1 THEN
200    LET Fib = 1
210 ELSE
220    LET Prev = 0
230    LET Curr = 1
240    FOR I = 2 TO N
250       LET T = Curr
260       LET Curr = Prev + Curr
270       LET Prev = T
280    NEXT I
290    LET Fib = Curr
300 END IF
310 END FUNCTION
```

**Output:**

2 runs.

```
Enter n for fib(n): 9
 34
```

```
Enter n for fib(n): 13
 233
```

### Applesoft BASIC

#### Iterative

Same code as Commodore BASIC. Entering a value of -184 < N > 183, produces an error message:

```
?OVERFLOW ERROR IN 220
```

#### Binet's Formula

```mw
 0  DEF  FN F(N) =  INT ((((1 +  SQR (5)) / 2) ^ N - ((1 -  SQR (5)) / 2) ^ N) /  SQR (5) + 0.5)
 1 S =  - 38: FOR I = S TO  - S: PRINT  MID$ (" ",(I = S) + 1) FN F(I);: NEXT
```

```
-39088169 24157817 -14930352 9227465 -5702887 3524578 -2178309 1346269 -832040 514229 -317811 196418 -121393 75025 -46368 28657 -17711 10946 -6765 4181 -2584 1597 -987 610 -377 233 -144 89 -55 34 -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157818 39088170
```

Entering a value of -38 < N > 38, produces an incorrect result due to inadequate precision in the calculation. The correct result for N = 39 should be 63245986. Entering a value of -44 < N > 44, produces a result in scientific notation. Entering a value of -182 < N > 182, produces an error message.

```mw
? FN F(39)" " FN F(45)" " FN F(183)
```

```
63245988 1.1349032E+09 
?OVERFLOW ERROR
```

### BASIC256

```mw
# Basic-256 ver 1.1.4
# iterative Fibonacci sequence
# Matches sequence A000045 in the OEIS, https://oeis.org/A000045/list

# Return the Nth Fibonacci number

input "N = ",f
limit = 500                        # set upper limit - can be changed, removed
f = int(f)
if f > limit then f = limit        
a = 0 : b = 1 : c = 0 : n = 0      # initial values

while n < f
    print n + chr(9) + c   # chr(9) = tab
    a = b
    b = c
    c = a + b  
    n += 1
        
end while

print " "
print n + chr(9) + c
```

### BazzBasic

```mw
' ============================================
' https://rosettacode.org/wiki/Fibonacci_sequence
' BazzBasic: https://github.com/EkBass/BazzBasic
' ============================================

DEF FN FibRecursive$(n$)
    IF n$ <= 1 THEN RETURN n$
    RETURN FN FibRecursive$(n$ - 1) + FN FibRecursive$(n$ - 2)
END DEF

DEF FN FibIterative$(n$)
    IF n$ <= 1 THEN RETURN n$
    LET a$ = 0
    LET b$ = 1
    FOR i$ = 2 TO n$
        LET temp$ = a$ + b$
        a$ = b$
        b$ = temp$
    NEXT
    RETURN b$
END DEF

DEF FN FibBinet$(n$)
    LET sqrt5$ = SQR(5)
    RETURN CINT((POW((1 + sqrt5$) / 2, n$) - POW((1 - sqrt5$) / 2, n$)) / sqrt5$)
END DEF

[main]
    INPUT "Enter n: ", n$

    IF n$ < 0 THEN
        PRINT "Negative numbers not supported."
        END
    END IF

    PRINT "Fibonacci("; n$; ")"
    PRINT " Recursive: "; FN FibRecursive$(n$)
    PRINT " Iterative: "; FN FibIterative$(n$)
    PRINT " Binet:     "; FN FibBinet$(n$)
END

' Output:
' Enter n: 6
' Fibonacci(6)
 ' Recursive: 8
 ' Iterative: 8
 ' Binet:     8
```

### BBC BASIC

```mw
      PRINT FNfibonacci_r(1),  FNfibonacci_i(1)
      PRINT FNfibonacci_r(13), FNfibonacci_i(13)
      PRINT FNfibonacci_r(26), FNfibonacci_i(26)
      END
      
      DEF FNfibonacci_r(N)
      IF N < 2 THEN = N
      = FNfibonacci_r(N-1) + FNfibonacci_r(N-2)
      
      DEF FNfibonacci_i(N)
      LOCAL F, I, P, T
      IF N < 2 THEN = N
      P = 1
      FOR I = 1 TO N
        T = F
        F += P
        P = T
      NEXT
      = F
```

**Output:**

```
         1         1
       233       233
    121393    121393
```

### bootBASIC

Variables in bootBASIC are 2 byte unsigned integers that roll over if there is an overflow. Entering a number greater than 24 will result in an incorrect outcome.

```mw
10 print "Enter a ";
20 print "number ";
30 print "greater ";
40 print "than 1";
50 print " and less";
60 print " than 25";
70 input z
80 b=1
90 a=0
100 n=2
110 f=a+b
120 a=b
130 b=f
140 n=n+1
150 if n-z-1 goto 110
160 print "The ";
170 print z ;
180 print "th ";
190 print "Fibonacci ";
200 print "Number is ";
210 print f
```

### CBASIC

Works with

:

CBASIC 2

Works with

:

CB80

Since CBASIC does not support recursion, only an iterative solution is possible

```mw
def fn.fib%(n%)
  p1% = 0
  p2% = 1
  if n% = 0 then \
    f% = 0 \
  else \
    for i% = 1 to n%
      f% = p1% + p2%
      p2% = p1%
      p1% = f%
    next i%
  fn.fib% = f% 
  return
fend    

print "First 20 Fibonacci numbers:"
for k% = 1 to 20
   print fn.fib%(k%);
next k%

end
```

**Output:**

```
First 20 Fibonacci numbers
 1 1 2 3 5 8 13 21 34 55 89 144 233 370 610 987 1597 2584 4181 6765
```

### Chipmunk Basic

Works with

:

Chipmunk Basic

version 3.6.4

```mw
100 cls
110 for i = 0 to 20 : print fibor(i); : next i
120 print
130 for i = 0 to 20 : print fiboi(i); : next i
140 print
150 for i = 0 to 20 : print fiboa(i); : next i
160 end
170 sub fibor(n) : 'Recursive
180   if n < 2 then
190     fibor = n
200   else
210     fibor = fibor(n-1)+fibor(n-2)
220   endif
230 end sub
240 sub fiboi(n) : 'Iterative
250   n1 = 0
260   n2 = 1
270   for k = 1 to abs(n)
280     sum = n1+n2
290     n1 = n2
300     n2 = sum
310   next k
320   if n < 0 then
330     fiboi = n1*((-1)^((-n)+1))
340   else
350     fiboi = n1
360   endif
370 end sub
380 sub fiboa(n) : 'Analytic
390   fiboa = int(0.5+(((sqr 5+1)/2)^n)/sqr 5)
400 end sub
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```

### Commodore BASIC

```mw
100 PRINT CHR$(147); CHR$(18); "****      FIBONACCI GENERATOR       ****"
110 INPUT "MIN, MAX"; N1, N2
120 IF N1 > N2 THEN T = N1: N1 = N2: N2 = T
130 A = 0: B = 1: S = SGN(N1)
140 FOR I = S TO N1 STEP S
150 : IF S > 0 THEN T = A + B: A = B: B = T
160 : IF S < 0 THEN T = B - A: B = A: A = T
170 NEXT I
180 PRINT
190 PRINT STR$(A); : REM STR$() PREVENTS TRAILING SPACE
200 IF N2 = N1 THEN 250
210 FOR I = N1 + 1 TO N2
220 : T = A + B: A = B: B = T
230 : PRINT ","; STR$(A);
240 NEXT I
250 PRINT
```

**Output:**

```
****      FIBONACCI GENERATOR       ****

MIN, MAX? -6,6

-8, 5,-3, 2,-1, 1, 0, 1, 1, 2, 3, 5, 8

READY.
```

### Craft Basic

```mw
let a = 1
let b = 1

print "Fibonacci Sequence"

for i = 0 to 20

   let s = a + b
   let a = b
   let b = s

   print s

next i
```

**Output:**

```
Fibonacci Sequence
2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 
```

### FreeBASIC

Extended sequence coded big integer.

```mw
'Fibonacci extended
'Freebasic version 24  Windows
Dim Shared ADDQmod(0 To 19) As Ubyte
Dim Shared ADDbool(0 To 19) As Ubyte

For z As Integer=0 To 19
    ADDQmod(z)=(z Mod 10+48)
    ADDbool(z)=(-(10<=z))
Next z 

Function plusINT(NUM1 As String,NUM2 As String) As String
    Dim As Byte flag
    #macro finish()
    three=Ltrim(three,"0")
    If three="" Then Return "0"
    If flag=1 Then Swap NUM2,NUM1
    Return three
    Exit Function
    #endmacro
    var lenf=Len(NUM1)
    var lens=Len(NUM2)
    If lens>lenf Then 
        Swap NUM2,NUM1
        Swap lens,lenf
        flag=1
    End If
    
    var diff=lenf-lens-Sgn(lenf-lens)
    var three="0"+NUM1
    var two=String(lenf-lens,"0")+NUM2
    Dim As Integer n2
    Dim As Ubyte addup,addcarry
    
    addcarry=0
    
    For n2=lenf-1 To diff Step -1 
        addup=two[n2]+NUM1[n2]-96
        three[n2+1]=addQmod(addup+addcarry)
        addcarry=addbool(addup+addcarry)
    Next n2 
    If addcarry=0 Then 
        finish()
    End If
    If n2=-1 Then 
        three[0]=addcarry+48
        finish()
    End If
    
    For n2=n2 To 0 Step -1 
        addup=two[n2]+NUM1[n2]-96
        three[n2+1]=addQmod(addup+addcarry)
        addcarry=addbool(addup+addcarry)
    Next n2
    three[0]=addcarry+48
    finish()
End Function

Function  fibonacci(n As Integer) As String
    Dim As String sl,l,term
    sl="0": l="1"
    If n=1 Then Return "0"
    If n=2 Then Return "1"
    n=n-2
    For x As Integer= 1 To n
        term=plusINT(l,sl)
        sl=l
        l=term
    Next x
    Function =term
End Function

'==============  EXAMPLE ===============
print "THE SEQUENCE TO 10:"
print
For n As Integer=1 To 10
    Print "term";n;": "; fibonacci(n)
Next n
print
print "Selected Fibonacci number"
print "Fibonacci 500"
print
print fibonacci(500)
Sleep
```

**Output:**

```
THE SEQUENCE TO 10:

term 1: 0
term 2: 1
term 3: 1
term 4: 2
term 5: 3
term 6: 5
term 7: 8
term 8: 13
term 9: 21
term 10: 34

Selected Fibonacci number
Fibonacci 500

86168291600238450732788312165664788095941068326060883324529903470149056115823592
713458328176574447204501
```

### FTCBASIC

```mw
define a = 1, b = 1, s = 0, i = 0

cls

print "Fibonacci Sequence"

do

   let s = a + b
   let a = b
   let b = s
   +1 i

   print s

loop i < 20

pause
end
```

### GFA Basic

```mw
'
' Compute nth Fibonacci number
'
' open a window for display
OPENW 1
CLEARW 1
' Display some fibonacci numbers
' Fib(46) is the largest number GFA Basic can reach
' (long integers are 4 bytes)
FOR i%=0 TO 46
  PRINT "fib(";i%;")=";@fib(i%)
NEXT i%
' wait for a key press and tidy up
~INP(2)
CLOSEW 1
'
' Function to compute nth fibonacci number
' n must be in range 0 to 46, inclusive
'
FUNCTION fib(n%)
  LOCAL n0%,n1%,nn%,i%
  n0%=0
  n1%=1
  SELECT n%
  CASE 0
    RETURN n0%
  CASE 1
    RETURN n1%
  DEFAULT
    FOR i%=2 TO n%
      nn%=n0%+n1%
      n0%=n1%
      n1%=nn%
    NEXT i%
    RETURN nn%
  ENDSELECT
ENDFUNC
```

### GW-BASIC

Works with

:

BASICA

#### Iterative

```mw
10 ' SAVE"FIBONA", A
20 ' Secuencia de Fibonacci
30 ' Var
40 DEFDBL D
50 IMAXFIBO% = 76
60 DNUM1 = 1: DNUM2 = DNUM1
70 CLS
80 PRINT "Este programa calcula la serie de Fibonacci."
90 PRINT DNUM1; DNUM2;
100 FOR I% = 1 TO IMAXFIBO%
110   DNUM3 = DNUM1 + DNUM2
120   PRINT DNUM3;
130   DNUM1 = DNUM2: DNUM2 = DNUM3
140 NEXT I%
150 PRINT
160 PRINT "Fin de la ejecución del programa."
170 END
```

**Output:**

```
Este programa calcula la serie de Fibonacci.
 1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584
 4181  6765  10946  17711  28657  46368  75025  121393  196418  317811  514229
 832040  1346269  2178309  3524578  5702887  9227465  14930352  24157817
 39088169  63245986  102334155  165580141  267914296  433494437  701408733
 1134903170  1836311903  2971215073  4807526976  7778742049  12586269025
 20365011074  32951280099  53316291173  86267571272  139583862445  225851433717
 365435296162  591286729879  956722026041  1548008755920  2504730781961
 4052739537881  6557470319842  10610209857723  17167680177565  27777890035288
 44945570212853  72723460248141  117669030460994  190392490709135
 308061521170129  498454011879264  806515533049393  1304969544928657
 2111485077978050  3416454622906707  5527939700884757  8944394323791464
Fin de la ejecución del programa.
Ok
```

#### Binet formula

```mw
10 ' SAVE"FIBINF", A
20 ' Secuencia de Fibonacci mediante la fórmula de Binet
30 ' Var
40 DEFDBL D
50 IMAXFIBO% = 77
60 DSQR5 = SQR(5)
70 DPIV1 = (1 + DSQR5) / 2
80 DPIV2 = (1 - DSQR5) / 2
90 DNUM1 = DPIV1: DNUM2 = DPIV2
100 CLS
110 PRINT "Este programa calcula la serie de Fibonacci."
120 FOR I% = 1 TO IMAXFIBO%
130   DNUM1 = DNUM1 * DPIV1
140   DNUM2 = DNUM2 * DPIV2
150   PRINT FIX(((DNUM1 - DNUM2) / DSQR5)+.5);
160 NEXT I%
170 PRINT
180 PRINT "Fin de la ejecución del programa."
190 END
```

**Output:**

```
Este programa calcula la serie de Fibonacci.
 1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584  4181
 6765  10946  17711  28657  46368  75025  121393  196418  317811  514229
 832040  1346269  2178310  3524579  5702889  9227468  14930357  24157826
 39088183  63246010  102334195  165580207  267914406  433494620  701409036
 1134903671  1836312733  2971216446  4807529247  7778745802  12586275225
 20365021312  32951296999  53316319058  86267617266  139583938281  225851558714
 365435502118  591287069122  956722584654  1548009675479  2504732295250
 4052742027550  6557474414738  10610216591046  17167691246479  27777908226979
 44945600103607  72723509350188  117669111103547  190392623123089
 308061738545741  498454368657289  806516118510594  1304970505463907
 2111486653578091  3416457206941612  5527943938022908  8944401270367342
Fin de la ejecución del programa.
Ok 
```

### Integer BASIC

Only works with quite small values of ${\displaystyle n}$ .

```mw
 10 INPUT N
 20 A=0
 30 B=1
 40 FOR I=2 TO N
 50 C=B
 60 B=A+B
 70 A=C
 80 NEXT I
 90 PRINT B
100 END
```

### IS-BASIC

```mw
100 PROGRAM "Fibonac.bas"
110 FOR I=0 TO 20
120   PRINT "F";I,FIB(I)
130 NEXT
140 DEF FIB(N)
150   NUMERIC I
160   LET A=0:LET B=1
170   FOR I=1 TO N
180     LET T=A+B:LET A=B:LET B=T
190   NEXT
200   LET FIB=A
210 END DEF
```

### Liberty BASIC

#### Iterative/Recursive

Works with

:

Just BASIC

```mw
for i = 0 to 15
    print fiboR(i),fiboI(i)
next i
 
function fiboR(n)
    if n <= 1 then
        fiboR = n
    else
        fiboR = fiboR(n-1) + fiboR(n-2)
    end if
end function
 
function fiboI(n)
    a = 0
    b = 1
    for i = 1 to n
        temp = a + b
        a = b
        b = temp
    next i
    fiboI = a
end function
```

**Output:**

```
0             0
1             1
1             1
2             2
3             3
5             5
8             8
13            13
21            21
34            34
55            55
89            89
144           144
233           233
377           377
610           610
```

#### Iterative/Negative

Works with

:

Just BASIC

```mw
print "Rosetta Code - Fibonacci sequence": print
print "  n             Fn"
for x=-12 to 12 '68 max
    print using("### ", x); using("##############", FibonacciTerm(x))
next x
print
[start]
input "Enter a term#: "; n$
n$=lower$(trim$(n$))
if n$="" then print "Program complete.": end
print FibonacciTerm(val(n$))
goto [start]

function FibonacciTerm(n)
    n=int(n)
    FTa=0: FTb=1: FTc=-1
    select case
        case n=0  : FibonacciTerm=0  : exit function
        case n=1  : FibonacciTerm=1  : exit function
        case n=-1 : FibonacciTerm=-1 : exit function
        case n>1
            for x=2 to n
                FibonacciTerm=FTa+FTb
                FTa=FTb: FTb=FibonacciTerm
            next x
            exit function
        case n<-1
            for x=-2 to n step -1
                FibonacciTerm=FTa+FTc
                FTa=FTc: FTc=FibonacciTerm
            next x
            exit function
    end select
end function
```

**Output:**

```
Rosetta Code - Fibonacci sequence

  n             Fn
-12           -144
-11            -89
-10            -55
 -9            -34
 -8            -21
 -7            -13
 -6             -8
 -5             -5
 -4             -3
 -3             -2
 -2             -1
 -1             -1
  0              0
  1              1
  2              1
  3              2
  4              3
  5              5
  6              8
  7             13
  8             21
  9             34
 10             55
 11             89
 12            144

Enter a term#: 12
144
Enter a term#:
Program complete.
```

### Microsoft Small Basic

#### Iterative

```mw
' Fibonacci sequence - 31/07/2018
  n = 139
  f1 = 0
  f2 = 1
  TextWindow.WriteLine("fibo(0)="+f1)
  TextWindow.WriteLine("fibo(1)="+f2)
  For i = 2 To n
    f3 = f1 + f2
    TextWindow.WriteLine("fibo("+i+")="+f3)
    f1 = f2
    f2 = f3
  EndFor
```

**Output:**

```
fibo(139)=50095301248058391139327916261
```

#### Binet's Formula

```mw
' Fibonacci sequence - Binet's Formula - 31/07/2018
  n = 69
  sq5=Math.SquareRoot(5)
  phi1=(1+sq5)/2
  phi2=(1-sq5)/2
  phi1n=phi1
  phi2n=phi2
  For i = 2 To n
    phi1n=phi1n*phi1
    phi2n=phi2n*phi2
    TextWindow.Write(Math.Floor((phi1n-phi2n)/sq5)+" ")
  EndFor
```

**Output:**

```
1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 12586269025 20365011074 32951280099 53316291173 86267571272 139583862445 225851433717 365435296162 591286729879 956722026041 1548008755920 2504730781961 4052739537881 6557470319842 10610209857723 17167680177565 27777890035288 44945570212853 72723460248141 117669030460994 
```

### Minimal BASIC

Works with

:

QBasic

Works with

:

BASICA

Works with

:

Chipmunk Basic

Works with

:

GW-BASIC

Works with

:

IS-BASIC

Works with

:

MSX Basic

```mw
110 REM THE ARRAY F HOLDS THE FIBONACCI NUMBERS
120 DIM F(22)
130 LET F(0) = 0
140 LET F(1) = 1
150 LET N = 1
160 REM COMPUTE THE NEXT FIBBONACCI NUMBER
170 LET F(N+1) = F(N)+F(N-1)
180 LET N = N+1
190 PRINT F(N-2);
200 REM STOP AFTER PRINTING  20 NUMBERS
210 IF N < 22 THEN 170
220 END
```

### MoonRock

Works with

:

MoonRock

version 0.50

MoonRock 0.50 does not support functions. So, a subroutine is written.

```mw
' Fibonacci sequence

BEGIN DEF
pointer dword FibPtr~ ' Why "pointer dword" must be in lower case?
SUB CalcFib(N%, FibPtr~)

BEGIN CODE
PRINT "Enter n for fib(n): "
INPUT SN$ 
N% = VAL(SN$) 
PRINT "\n"
CALL CalcFib(N%, VARPTR(Fib&))
PRINT Fib& + "\n"
END

SUB CalcFib(N%, FibPtr~)
IF N% = 0 THEN
  Fib& = 0
ELSE
  IF N% = 1 THEN
    Fib& = 1
  ELSE
    Prev& = 0
    Fib& = 1
    FOR I% = 2 TO N%
      T& = Fib&
      Fib& = Prev& + Fib&
      Prev& = T&
    NEXT
  ENDIF
ENDIF
[FibPtr~] = Fib&
END SUB
```

**Output:**

2 runs.

```
Enter n for fib(n): 9
34
```

```
Enter n for fib(n): 13
233
```

### MSX Basic

Works with

:

QBasic

Works with

:

Chipmunk Basic

Works with

:

GW-BASIC

```mw
100 CLS
110 FOR N = 0 TO 15: GOSUB 130: PRINT FIBOI; : NEXT N
120 END
130 REM Iterative Fibonacci sequence
140 N1 = 0
150 N2 = 1
160 FOR K = 1 TO ABS(N)
170   SUM = N1 + N2
180   N1 = N2
190   N2 = SUM
200 NEXT K
210 IF N < 0 THEN FIBOI = N1 * ((-1) ^ ((-N) + 1)) ELSE FIBOI = N1
220 RETURN
```

### Palo Alto Tiny BASIC

```mw
10 REM FIBONACCI SEQUENCE
20 INPUT "ENTER N FOR FIB(N)"N
30 LET A=0,B=1
40 FOR I=2 TO N
50 LET T=B,B=A+B,A=T
60 NEXT I
70 PRINT B
80 STOP
```

**Output:**

2 runs.

```
ENTER N FOR FIB(N):9
     34
```

```
ENTER N FOR FIB(N):13
    233
```

### PowerBASIC

Translation of

:

BASIC

There seems to be a limitation (dare I say, bug?) in PowerBASIC regarding how large numbers are stored. 10E17 and larger get rounded to the nearest 10. For F(n), where ABS(n) > 87, is affected like this:

```
      actual:             displayed:
F(88) 1100087778366101931 1100087778366101930
F(89) 1779979416004714189 1779979416004714190
F(90) 2880067194370816120 2880067194370816120
F(91) 4660046610375530309 4660046610375530310
F(92) 7540113804746346429 7540113804746346430
```

```mw
FUNCTION fibonacci (n AS LONG) AS QUAD
    DIM u AS LONG, a AS LONG, L0 AS LONG, outP AS QUAD
    STATIC fibNum() AS QUAD

    u = UBOUND(fibNum)
    a = ABS(n)

    IF u < 1 THEN
        REDIM fibNum(1)
        fibNum(1) = 1
        u = 1
    END IF

    SELECT CASE a
        CASE 0 TO 92
            IF a > u THEN
                REDIM PRESERVE fibNum(a)
                FOR L0 = u + 1 TO a
                    fibNum(L0) = fibNum(L0 - 1) + fibNum(L0 - 2)
                    IF 88 = L0 THEN fibNum(88) = fibNum(88) + 1
                NEXT
            END IF
            IF n < 0 THEN
                fibonacci = fibNum(a) * ((-1)^(a+1))
            ELSE
                fibonacci = fibNum(a)
            END IF
        CASE ELSE
            'Even without the above-mentioned bug, we're still limited to
            'F(+/-92), due to data type limits. (F(93) = &hA94F AD42 221F 2702)
            ERROR 6
    END SELECT
END FUNCTION

FUNCTION PBMAIN () AS LONG
    DIM n AS LONG
    #IF NOT %DEF(%PB_CC32)
        OPEN "out.txt" FOR OUTPUT AS 1
    #ENDIF
    FOR n = -92 TO 92
        #IF %DEF(%PB_CC32)
            PRINT STR$(n); ": "; FORMAT$(fibonacci(n), "#")
        #ELSE
            PRINT #1, STR$(n) & ": " & FORMAT$(fibonacci(n), "#")
        #ENDIF
    NEXT
    CLOSE
END FUNCTION
```

### PureBasic

#### Macro based calculation

```mw
Macro Fibonacci (n)
   Int((Pow(((1+Sqr(5))/2),n)-Pow(((1-Sqr(5))/2),n))/Sqr(5))
EndMacro
```

#### Recursive

```mw
Procedure FibonacciReq(n)
  If n<2
    ProcedureReturn n
  Else
    ProcedureReturn FibonacciReq(n-1)+FibonacciReq(n-2)
  EndIf
EndProcedure
```

#### Recursive & optimized with a static hash table

This will be much faster on larger n's, this as it uses a table to store known parts instead of recalculating them. On my machine the speedup compares to above code is

```
Fib(n) Speedup
20           2
25          23
30         217
40       25847
46     1156741
```

```mw
Procedure Fibonacci(n)
  Static NewMap Fib.i()
  Protected FirstRecursion
  
  If MapSize(Fib())= 0        ; Init the hash table the first run
    Fib("0")=0: Fib("1")=1
    FirstRecursion = #True
  EndIf
 
  If n >= 2
    Protected.s s=Str(n)
    If Not FindMapElement(Fib(),s)  ; Calculate only needed parts
      Fib(s)= Fibonacci(n-1)+Fibonacci(n-2)
    EndIf
    n = Fib(s)  
  EndIf
  If FirstRecursion ; Free the memory when finalizing the first call
    ClearMap(Fib())
  EndIf
  ProcedureReturn n
EndProcedure
```

**Example**

```
Fibonacci(0)= 0
Fibonacci(1)= 1
Fibonacci(2)= 1
Fibonacci(3)= 2
Fibonacci(4)= 3
Fibonacci(5)= 5

FibonacciReq(0)= 0
FibonacciReq(1)= 1
FibonacciReq(2)= 1
FibonacciReq(3)= 2
FibonacciReq(4)= 3
FibonacciReq(5)= 5
```

### QB64

*CBTJD*: 2020/03/13

```mw
_DEFINE F AS _UNSIGNED _INTEGER64
CLS
PRINT
PRINT "Enter 40 to more easily see the difference in calculation speeds."
PRINT
INPUT "Enter n for Fibonacci(n): ", n
PRINT
PRINT " Analytic Method (Fastest): F("; LTRIM$(STR$(n)); ") ="; fA(n)
PRINT "Iterative Method    (Fast): F("; LTRIM$(STR$(n)); ") ="; fI(n)
PRINT "Recursive Method    (Slow): F("; LTRIM$(STR$(n)); ") ="; fR(n)
END

' === Analytic Fibonacci Function (Fastest)
FUNCTION fA (n)
  fA = INT(0.5 + (((SQR(5) + 1) / 2) ^ n) / SQR(5))
END FUNCTION

' === Iterative Fibonacci Function (Fast)
FUNCTION fI (n)
  FOR i = 1 TO n
    IF i < 3 THEN a = 1: b = 1
    t = fI + b: fI = b: b = t
  NEXT
END FUNCTION

' === Recursive Fibonacci function (Slow)
FUNCTION fR (n)
  IF n <= 1 THEN
    fR = n
  ELSE
    fR = fR(n - 1) + fR(n - 2)
  END IF
END FUNCTION
```

Fibonacci from Russia

```mw
DIM F(80) AS DOUBLE 'FibRus.bas DANILIN
F(1) = 0: F(2) = 1
'OPEN "FibRus.txt" FOR OUTPUT AS #1
FOR i = 3 TO 80
    F(i) = F(i-1)+F(i-2)
NEXT i

FOR i = 1 TO 80
    f$ = STR$(F(i)): LF = 22 - LEN(f$)
    n$ = ""
    FOR j = 1 TO LF: n$ = " " + n$: NEXT
    f$ = n$ + f$
    PRINT i, f$: ' PRINT #1, i, f$
NEXT i
```

**Output:**

```
1                                 0
2                                 1
3                                 1
4                                 2
5                                 3
6                                 5
7                                 8
8                                13
9                                21
...
24                            28657
25                            46368
26                            75025
...
36                          9227465
37                         14930352
38                         24157817
...
48                       2971215073
49                       4807526976
50                       7778742049
...
60                     956722026041
61                    1548008755920
62                    2504730781961
...
76                 2111485077978050
77                 3416454622906707
78                 5527939700884757
79                 8944394323791464
80            1.447233402467622D+16
```

### QBasic

Works with

:

QBasic

Works with

:

FreeBASIC

#### Iterative

```mw
FUNCTION itFib (n)
    n1 = 0
    n2 = 1
    FOR k = 1 TO ABS(n)
        sum = n1 + n2
        n1 = n2
        n2 = sum
    NEXT k
    IF n < 0 THEN
        itFib = n1 * ((-1) ^ ((-n) + 1))
    ELSE
        itFib = n1
    END IF
END FUNCTION
```

Next version calculates each value once, as needed, and stores the results in an array for later retreival (due to the use of `REDIM PRESERVE`, it requires QuickBASIC 4.5 or newer):

```mw
DECLARE FUNCTION fibonacci& (n AS INTEGER)

REDIM SHARED fibNum(1) AS LONG

fibNum(1) = 1

'*****sample inputs*****
PRINT fibonacci(0)      'no calculation needed
PRINT fibonacci(13)     'figure F(2)..F(13)
PRINT fibonacci(-42)    'figure F(14)..F(42)
PRINT fibonacci(47)     'error: too big
'*****sample inputs*****

FUNCTION fibonacci& (n AS INTEGER)
    DIM a AS INTEGER
    a = ABS(n)
    SELECT CASE a
        CASE 0 TO 46
            SHARED fibNum() AS LONG
            DIM u AS INTEGER, L0 AS INTEGER
            u = UBOUND(fibNum)
            IF a > u THEN
                REDIM PRESERVE fibNum(a) AS LONG
                FOR L0 = u + 1 TO a
                    fibNum(L0) = fibNum(L0 - 1) + fibNum(L0 - 2)
                NEXT
            END IF
            IF n < 0 THEN
                fibonacci = fibNum(a) * ((-1) ^ (a + 1))
            ELSE
                fibonacci = fibNum(n)
            END IF
        CASE ELSE
            'limited to signed 32-bit int (LONG)
            'F(47)=&hB11924E1
            ERROR 6 'overflow
    END SELECT
END FUNCTION
```

**Output:**

(unhandled error in final input prevents output)

```
 0
 233
-267914296
```

#### Recursive

This example can't handle n < 0.

```mw
FUNCTION recFib (n)
    IF (n < 2) THEN
   recFib = n
    ELSE
   recFib = recFib(n - 1) + recFib(n - 2)
    END IF
END FUNCTION
```

#### Array (Table) Lookup

This uses a pre-generated list, requiring much less run-time processor usage. (Since the sequence never changes, this is probably the best way to do this in "the real world". The same applies to other sequences like prime numbers, and numbers like pi and e.)

```mw
DATA -1836311903,1134903170,-701408733,433494437,-267914296,165580141,-102334155
DATA 63245986,-39088169,24157817,-14930352,9227465,-5702887,3524578,-2178309
DATA 1346269,-832040,514229,-317811,196418,-121393,75025,-46368,28657,-17711
DATA 10946,-6765,4181,-2584,1597,-987,610,-377,233,-144,89,-55,34,-21,13,-8,5,-3
DATA 2,-1,1,0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765
DATA 10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269
DATA 2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986
DATA 102334155,165580141,267914296,433494437,701408733,1134903170,1836311903

DIM fibNum(-46 TO 46) AS LONG

FOR n = -46 TO 46
    READ fibNum(n)
NEXT

'*****sample inputs*****
FOR n = -46 TO 46
    PRINT fibNum(n),
NEXT
PRINT
'*****sample inputs*****
```

### Quite BASIC

```mw
100 CLS
110 rem The array F holds the Fibonacci numbers
120 ARRAY f : rem DIM f(22) para Quite BASIC and MSX-BASIC
130 LET f(0) = 0
140 LET f(1) = 1
150 LET n = 1
160 rem Compute the NEXT Fibbonacci number
170 LET f(n+1) = f(n)+f(n-1)
180 LET n = n+1
190 PRINT f(n-2);" ";
200 rem STOP after printing  20 numbers
210 IF n < 22 THEN GOTO 170
```

### Run BASIC

```mw
for i = 0 to 10
 print i;" ";fibR(i);" ";fibI(i)
next i
end
 
 function fibR(n)
 if n < 2 then fibR = n else fibR = fibR(n-1) + fibR(n-2)
 end function
 
 function fibI(n)
   b = 1
   for i = 1 to n
       t = a + b
       a = b
       b = t
   next i
fibI = a
end function
```

### S-BASIC

Note that the 23rd Fibonacci number (=28657) is the largest that can be generated without overflowing S-BASIC's integer data type.

```mw
rem - iterative function to calculate nth fibonacci number
function fibonacci(n = integer) = integer
var f, i, p1, p2 = integer
p1 = 0    
p2 = 1
if n = 0 then
   f = 0
else
   for i = 1 to n
      f = p1 + p2
      p2 = p1
      p1 = f
   next i
end = f

rem - exercise the function
var i = integer
for i = 0 to 10
   print fibonacci(i);
next i

end
```

**Output:**

```
 0 1 1 2 3 5 8 13 21 34 55
```

### Sinclair ZX81 BASIC

#### Analytic

```mw
 10 INPUT N
 20 PRINT INT (0.5+(((SQR 5+1)/2)**N)/SQR 5)
```

#### Iterative

```mw
 10 INPUT N
 20 LET A=0
 30 LET B=1
 40 FOR I=2 TO N
 50 LET C=B
 60 LET B=A+B
 70 LET A=C
 80 NEXT I
 90 PRINT B
```

#### Tail recursive

```mw
 10 INPUT N
 20 LET A=0
 30 LET B=1
 40 GOSUB 70
 50 PRINT B
 60 STOP
 70 IF N=1 THEN RETURN
 80 LET C=B
 90 LET B=A+B
100 LET A=C
110 LET N=N-1
120 GOSUB 70
130 RETURN
```

### smart BASIC

The Iterative method is slow (relatively) and the Recursive method doubly so since it references the recursion function twice.

The N-th Term (fibN) function is much faster as it utilizes Binet's Formula.

- fibR: Fibonacci Recursive
- fibI: Fibonacci Iterative
- fibN: Fibonacci N-th Term

```mw
FOR i = 0 TO 15
    PRINT fibR(i),fibI(i),fibN(i)
NEXT i

/* Recursive Method */
DEF fibR(n)
    IF n <= 1 THEN
        fibR = n
    ELSE
        fibR = fibR(n-1) + fibR(n-2)
    ENDIF
END DEF

/* Iterative Method */
DEF fibI(n)
    a = 0
    b = 1
    FOR i = 1 TO n
        temp = a + b
        a = b
        b = temp
    NEXT i
    fibI = a
END DEF

/* N-th Term Method */
DEF fibN(n)
    uphi = .5 + SQR(5)/2
    lphi = .5 - SQR(5)/2
    fibN = (uphi^n-lphi^n)/SQR(5)
END DEF
```

### Softbridge BASIC

#### Iterative

```mw
Function Fibonacci(n)
   x = 0
   y = 1
   i = 0
   n = ABS(n)
   If n < 2 Then
   Fibonacci = n
   Else
   Do Until (i = n)
      sum = x+y
      x=y
      y=sum
      i=i+1
   Loop
   Fibonacci = x
   End If

End Function
```

### TI-83 BASIC

#### Sequence table

```mw
[Y=]
nMin=0
u(n)=u(n-1)+u(n-2)
u(nMin)={1,0}
[TABLE]
n  u(n)
-------  -------
0  0
1  1
2  1
3  2
4  3
5  5
6  8
7  13
8  21
9  34
10 55
11 89
12 144
```

#### Iterative

```mw
{0,1
While 1
Disp Ans(1
{Ans(2),sum(Ans
End
```

#### Binet's formula

```mw
Prompt N
.5(1+√(5    //golden ratio
(Ans^N–(-Ans)^-N)/√(5
```

### TI-89 BASIC

#### Recursive

Optimized implementation (too slow to be usable for *n* higher than about 12).

```mw
fib(n)
when(n<2, n, fib(n-1) + fib(n-2))
```

#### Iterative

Unoptimized implementation (I think the for loop can be eliminated, but I'm not sure).

```mw
fib(n)
Func
Local a,b,c,i
0→a
1→b
For i,1,n
  a→c
  b→a
  c+b→b
EndFor
a
EndFunc
```

### Tiny BASIC

Works with

:

TinyBasic

```mw
10 LET A = 0
20 LET B = 1
30 PRINT "Which F_n do you want?"
40 INPUT N
50 IF N = 0 THEN GOTO 140
60 IF N = 1 THEN GOTO 120
70 LET C = B + A
80 LET A = B
90 LET B = C
100 LET N = N - 1
110 GOTO 60
120 PRINT B
130 END
140 PRINT 0
150 END
```

### True BASIC

```mw
FUNCTION fibonacci (n)
    LET n1 = 0
    LET n2 = 1
    FOR k = 1 TO ABS(n)
        LET sum = n1 + n2
        LET n1 = n2
        LET n2 = sum
    NEXT k
    IF n < 0 THEN
       LET fibonacci = n1 * ((-1) ^ ((-n) + 1))
    ELSE
       LET fibonacci = n1
    END IF
END FUNCTION

PRINT fibonacci(0)      ! 0
PRINT fibonacci(13)     ! 233
PRINT fibonacci(-42)    !-267914296
PRINT fibonacci(47)     ! 2971215073
END
```

### VBA

Like Visual Basic .NET, but with keyword "Public" and type Variant (subtype Currency) instead of Decimal:

```mw
Public Function Fib(ByVal n As Integer) As Variant
    Dim fib0 As Variant, fib1 As Variant, sum As Variant
    Dim i As Integer
    fib0 = 0
    fib1 = 1
    For i = 1 To n
        sum = fib0 + fib1
        fib0 = fib1
        fib1 = sum
    Next i
    Fib = fib0
End Function
```

With Currency type, maximum value is fibo(73).

The (slow) recursive version:

```mw
Public Function RFib(Term As Integer) As Long
  If Term < 2 Then RFib = Term Else RFib = RFib(Term - 1) + RFib(Term - 2)
End Function
```

With Long type, maximum value is fibo(46).

### VBScript

#### Non-recursive, object oriented, generator

Defines a generator class, with a default Get property. Uses Currency for larger-than-Long values. Tests for overflow and switches to Double. Overflow information also available from class.

##### Class Definition:

```mw
class generator
   dim t1
   dim t2
   dim tn
   dim cur_overflow
   
   Private Sub Class_Initialize
      cur_overflow = false
      t1 = ccur(0)
      t2 = ccur(1)
      tn = ccur(t1 + t2)
   end sub
   
   public default property get generated
      on error resume next

      generated = ccur(tn)
      if err.number <> 0 then 
         generated = cdbl(tn)
         cur_overflow = true
      end if
      t1 = ccur(t2)
      if err.number <> 0 then 
         t1 = cdbl(t2)
         cur_overflow = true
      end if
      t2 = ccur(tn)
      if err.number <> 0 then 
         t2 = cdbl(tn)
         cur_overflow = true
      end if
      tn = ccur(t1+ t2)
      if err.number <> 0 then 
         tn = cdbl(t1) + cdbl(t2)
         cur_overflow = true
      end if
      on error goto 0
   end property
   
   public property get overflow
      overflow = cur_overflow
   end property
      
end class
```

##### Invocation:

```mw
dim fib
set fib = new generator
dim i
for i = 1 to 100
   wscript.stdout.write " " & fib 
   if fib.overflow then
      wscript.echo
      exit for
   end if
next
```

**Output:**

```
 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 12586269025 20365011074 32951280099 53316291173 86267571272 139583862445 225851433717 365435296162 591286729879 956722026041 1548008755920 2504730781961 4052739537881 6557470319842 10610209857723 17167680177565 27777890035288 44945570212853 72723460248141 117669030460994 190392490709135 308061521170129 498454011879264 806515533049393
```

### Visual Basic

Works with

:

Visual Basic

version VB6 Standard

Maximum integer value (7*10^28) can be obtained by using decimal type, but decimal type is only a sub type of the variant type.

```mw
Sub fibonacci()
    Const n = 139 
    Dim i As Integer
    Dim f1 As Variant, f2 As Variant, f3 As Variant 'for Decimal
    f1 = CDec(0): f2 = CDec(1) 'for Decimal setting
    Debug.Print "fibo("; 0; ")="; f1
    Debug.Print "fibo("; 1; ")="; f2
    For i = 2 To n
        f3 = f1 + f2
        Debug.Print "fibo("; i; ")="; f3
        f1 = f2
        f2 = f3
    Next i
End Sub 'fibonacci
```

**Output:**

```
fibo( 0 )= 0 
fibo( 1 )= 1 
fibo( 2 )= 1 
...
fibo( 137 )= 19134702400093278081449423917 
fibo( 138 )= 30960598847965113057878492344 
fibo( 139 )= 50095301248058391139327916261 
```

### Visual Basic .NET

**Platform:** .NET

#### Iterative

Works with

:

Visual Basic .NET

version 9.0+

With Decimal type, maximum value is fibo(139).

```mw
Function Fib(ByVal n As Integer) As Decimal
    Dim fib0, fib1, sum As Decimal
    Dim i As Integer
    fib0 = 0
    fib1 = 1
    For i = 1 To n
        sum = fib0 + fib1
        fib0 = fib1
        fib1 = sum
    Next
    Fib = fib0
End Function
```

#### Recursive

Works with

:

Visual Basic .NET

version 9.0+

```mw
Function Seq(ByVal Term As Integer)
        If Term < 2 Then Return Term
        Return Seq(Term - 1) + Seq(Term - 2)
End Function
```

#### BigInteger

There is no real maximum value of BigInterger class, except the memory to store the number. Within a minute, fibo(2000000) is a number with 417975 digits.

```mw
    Function FiboBig(ByVal n As Integer) As BigInteger
        ' Fibonacci sequence with BigInteger
        Dim fibn2, fibn1, fibn As BigInteger
        Dim i As Integer
        fibn = 0
        fibn2 = 0
        fibn1 = 1
        If n = 0 Then
            Return fibn2
        ElseIf n = 1 Then
            Return fibn1
        ElseIf n >= 2 Then
            For i = 2 To n
                fibn = fibn2 + fibn1
                fibn2 = fibn1
                fibn1 = fibn
            Next i
            Return fibn
        End If
        Return 0
    End Function 'FiboBig

    Sub fibotest()
        Dim i As Integer, s As String
        i = 2000000  ' 2 millions
        s = FiboBig(i).ToString
        Console.WriteLine("fibo(" & i & ")=" & s & " - length=" & Len(s))
    End Sub 'fibotest
```

#### BigInteger, speedier method

Library:

System.Numerics

This method doesn't need to iterate the entire list, and is much faster. The 2000000 (two millionth) Fibonacci number can be found in a fraction of a second. Algorithm from here, see section 3, *Finding Fibonacci Numbers Fully*.

```mw
Imports System
Imports System.Collections.Generic
Imports BI = System.Numerics.BigInteger

Module Module1

    ' A sparse array of values calculated along the way
    Dim sl As SortedList(Of Integer, BI) = New SortedList(Of Integer, BI)()

    ' Square a BigInteger
    Function sqr(ByVal n As BI) As BI
        Return n * n
    End Function

    ' Helper routine for Fsl(). It adds an entry to the sorted list when necessary
    Sub IfNec(n As Integer)
        If Not sl.ContainsKey(n) Then sl.Add(n, Fsl(n))
    End Sub

    ' This routine is semi-recursive, but doesn't need to evaluate every number up to n.
    ' Algorithm from here: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section3
    Function Fsl(ByVal n As Integer) As BI
        If n < 2 Then Return n
        Dim n2 As Integer = n >> 1, pm As Integer = n2 + ((n And 1) << 1) - 1 : IfNec(n2) : IfNec(pm)
        Return If(n2 > pm, (2 * sl(pm) + sl(n2)) * sl(n2), sqr(sl(n2)) + sqr(sl(pm)))
    End Function

    ' Conventional iteration method (not used here)
    Function Fm(ByVal n As BI) As BI
        If n < 2 Then Return n
        Dim cur As BI = 0, pre As BI = 1
        For i As Integer = 0 To n - 1
            Dim sum As BI = cur + pre : pre = cur : cur = sum : Next : Return cur
    End Function

    Sub Main()
        Dim vlen As Integer, num As Integer = 2_000_000, digs As Integer = 35
        Dim sw As System.Diagnostics.Stopwatch = System.Diagnostics.Stopwatch.StartNew()
        Dim v As BI = Fsl(num) : sw.[Stop]()
        Console.Write("{0:n3} ms to calculate the {1:n0}th Fibonacci number, ", sw.Elapsed.TotalMilliseconds, num)
        vlen = CInt(Math.Ceiling(BI.Log10(v))) : Console.WriteLine("number of digits is {0}", vlen)
        If vlen < 10000 Then
            sw.Restart() : Console.WriteLine(v) : sw.[Stop]()
            Console.WriteLine("{0:n3} ms to write it to the console.", sw.Elapsed.TotalMilliseconds)
        Else
            Console.Write("partial: {0}...{1}", v / BI.Pow(10, vlen - digs), v Mod BI.Pow(10, digs))
        End If
    End Sub
End Module
```

**Output:**

```
120.374 ms to calculate the 2,000,000th Fibonacci number, number of digits is 417975
partial: 85312949175076415430516606545038251...91799493108960825129188777803453125
```

### Xojo

Pass n to this function where n is the desired number of iterations. This example uses the UInt64 datatype which is as unsigned 64 bit integer. As such, it overflows after the 93rd iteration.

```mw
Function fibo(n As Integer) As UInt64

  Dim noOne As UInt64 = 1
  Dim noTwo As UInt64 = 1  
  Dim sum As UInt64

  For i As Integer = 3 To n
      sum = noOne + noTwo
      noTwo = noOne
      noOne = sum
  Next

  Return noOne
End Function
```

### Yabasic

#### Iterative

```mw
sub fibonacciI (n)
    local n1, n2, k, sum

    n1 = 0
    n2 = 1
    for k = 1 to abs(n)
        sum = n1 + n2
        n1 = n2
        n2 = sum
    next k
    if n < 1 then
       return n1 * ((-1) ^ ((-n) + 1))
    else
       return n1
    end if
end sub
```

#### Recursive

Only positive numbers

```mw
sub fibonacciR(n)
    if n <= 1 then
        return n
    else
        return fibonacciR(n-1) + fibonacciR(n-2)
    end if
end sub
```

#### Analytic

Only positive numbers

```mw
sub fibonacciA (n)
    return int(0.5 + (((sqrt(5) + 1) / 2) ^ n) / sqrt(5))
end sub
```

#### Binet's formula

Fibonacci sequence using the Binet formula

```mw
sub fibonacciB(n)
    local sq5, phi1, phi2, dn1, dn2, k

    sq5 = sqrt(5)
    phi1 = (1 + sq5) / 2
    phi2 = (1 - sq5) / 2
    dn1 = phi1: dn2 = phi2
    for k = 0 to n
        dn1 = dn1 * phi1
        dn2 = dn2 * phi2
        print int(((dn1 - dn2) / sq5) + .5);
    next k
end sub
```

### ZX Spectrum Basic

#### Iterative

```mw
10 REM Only positive numbers
20 LET n=10
30 LET n1=0: LET n2=1
40 FOR k=1 TO n
50 LET sum=n1+n2
60 LET n1=n2
70 LET n2=sum
80 NEXT k
90 PRINT n1
```

#### Analytic

```mw
10 DEF FN f(x)=INT (0.5+(((SQR 5+1)/2)^x)/SQR 5)
```


## Batch File

Recursive version

```mw
::fibo.cmd
@echo off
if "%1" equ "" goto :eof
call :fib %1
echo %errorlevel%
goto :eof

:fib
setlocal enabledelayedexpansion
if %1 geq 2 goto :ge2 
exit /b %1

:ge2
set /a r1 = %1 - 1
set /a r2 = %1 - 2
call :fib !r1!
set r1=%errorlevel%
call :fib !r2!
set r2=%errorlevel%
set /a r0 = r1 + r2
exit /b !r0!
```

**Output:**

```
>for /L %i in (1,5,20) do fibo.cmd %i

>fibo.cmd 1
1

>fibo.cmd 6
8

>fibo.cmd 11
89

>fibo.cmd 16
987
```


## Battlestar

```mw
// Fibonacci sequence, recursive version
fun fibb
    loop
        a = funparam[0]
        break (a < 2)

        a--

        // Save "a" while calling fibb
        a -> stack

        // Set the parameter and call fibb
        funparam[0] = a
        call fibb

        // Handle the return value and restore "a"
        b = funparam[0]
        stack -> a

        // Save "b" while calling fibb again
        b -> stack

        a--

        // Set the parameter and call fibb
        funparam[0] = a
        call fibb

        // Handle the return value and restore "b"
        c = funparam[0]
        stack -> b

        // Sum the results
        b += c
        a = b

        funparam[0] = a

        break
    end
end

// vim: set syntax=c ts=4 sw=4 et:
```


## bc

### iterative

```mw
#! /usr/bin/bc -q

define fib(x) {
    if (x <= 0) return 0;
    if (x == 1) return 1;

    a = 0;
    b = 1;
    for (i = 1; i < x; i++) {
        c = a+b; a = b; b = c;
    }
    return c;
}
fib(1000)
quit
```


## BCPL

```mw
get "libhdr"

let fib(n) = n<=1 -> n, valof
$(  let a=0 and b=1
    for i=2 to n
    $(  let c=a
        a := b
        b := a+c
    $)
    resultis b
$)

let start() be
    for i=0 to 10 do
        writef("F_%N*T= %N*N", i, fib(i))
```

**Output:**

```
F_0     = 0
F_1     = 1
F_2     = 1
F_3     = 2
F_4     = 3
F_5     = 5
F_6     = 8
F_7     = 13
F_8     = 21
F_9     = 34
F_10    = 55
```


## beeswax

```mw
                        #>'#{;
_`Enter n: `TN`Fib(`{`)=`X~P~K#{;
                         #>~P~L#MM@>+@'q@{;
                                    b~@M<
```

Example output:

Notice the UInt64 wrap-around at `Fib(94)`!

```mw
julia> beeswax("n-th Fibonacci number.bswx")
Enter n: i0

Fib(0)=0
Program finished!

julia> beeswax("n-th Fibonacci number.bswx")
Enter n: i10
         
Fib(10)=55
Program finished!

julia> beeswax("n-th Fibonacci number.bswx")
Enter n: i92

Fib(92)=7540113804746346429
Program finished!

julia> beeswax("n-th Fibonacci number.bswx")
Enter n: i93
                                                                             
Fib(93)=12200160415121876738                                                 
Program finished!                                                            

julia> beeswax("n-th Fibonacci number.bswx")
Enter n: i94                                                                 
                                                                             
Fib(94)=1293530146158671551                                                  
Program finished!
```


## Befunge

```mw
00:.1:.>:"@"8**++\1+:67+`#@_v
       ^ .:\/*8"@"\%*8"@":\ <
```


## Binary Lambda Calculus

Fibonacci on Church numerals in the lambda calculus is `λn. n (λc λa λb.c b (λx.a (b x))) (λx λy.x) (λx.x)` (see https://github.com/tromp/AIT/blob/master/numerals/fib.lam) which in BLC is the 52 bits

```
0001010110000000010111101000011110011101000001100010
```


## BlitzMax

```mw
local a:int = 0, b:int = 1, c:int = 1, n:int

n = int(input( "Enter n: "))
if n = 0 then
    print 0
    end
else if n = 1
    print 1
    end
end if

while n>2
    a = b
    b = c
    c = a + b
    n = n - 1
wend
print c
```


## Blue

```mw
: fib ( nth:ecx -- result:edi ) 1 0 
: compute ( times:ecx accum:eax scratch:edi -- result:edi ) xadd latest loop ;

: example ( -- ) 11 fib drop ;
```


## BQN

All given functions return the nth element in the sequence.

### Recursive

A primitive recursive can be done with predicates:

```mw
Fib ← {𝕩>1 ? (𝕊 𝕩-1) + 𝕊 𝕩-2; 𝕩}
```

Or, it can be done with the Choose(`◶`) modifier:

```mw
Fib2 ← {(𝕩-1) (𝕩>1)◶⟨𝕩, +○𝕊⟩ 𝕩-2}
```

### Iterative

An iterative solution can be made with the Repeat(`⍟`) modifier:

```mw
{⊑(+`⌽)⍟𝕩 0‿1}
```


## Bracmat

### Recursive

```mw
fib=.!arg:<2|fib$(!arg+-2)+fib$(!arg+-1)
```

```
 fib$30
 832040
```

### Iterative

```mw
(fib=
  last i this new
.   !arg:<2
  |   0:?last:?i
    & 1:?this
    &   whl
      ' ( !i+1:<!arg:?i
        & !last+!this:?new
        & !this:?last
        & !new:?this
        )
    & !this
)
```

```
 fib$777
 1081213530912648191985419587942084110095342850438593857649766278346130479286685742885693301250359913460718567974798268702550329302771992851392180275594318434818082
```
