---
title: "Fibonacci sequence (part 10/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 10/10
---

## TUSCRIPT

```mw
$$ MODE TUSCRIPT
ASK "What fibionacci number do you want?": searchfib=""
IF (searchfib!='digits') STOP
Loop n=0,{searchfib}
 IF (n==0) THEN
   fib=fiba=n
 ELSEIF (n==1) THEN
   fib=fibb=n
 ELSE
   fib=fiba+fibb, fiba=fibb, fibb=fib
 ENDIF
 IF (n!=searchfib) CYCLE
 PRINT "fibionacci number ",n,"=",fib
ENDLOOP
```

Output:

```
What fibionacci number do you want? >12
fibionacci number 12=144
```

Output:

```
What fibionacci number do you want? >31
fibionacci number 31=1346269 
```

Output:

```
What fibionacci number do you want? >46
fibionacci 46=1836311903
```


## Uiua

### Recursive

Works with

:

Uiua

version 0.10.0-dev.1

Simple recursive example with memoisation.

```mw
F ← |1 memo⟨+⊃(F-1)(F-2)|∘⟩<2.
F ⇡20
```

### Iterative

Works with

:

Uiua

version 0.17.0-dev.2

Simple iterative example:

```mw
15                # length of final array
[1 1]             # starting two values in the sequence
⊙◌⍢(⊂/+⊸↙2|>⧻) # do iteration while less than desired length
```


## UNIX Shell

Works with

:

bash

version 3

```mw
#!/bin/bash

a=0
b=1
max=$1

for (( n=1; "$n" <= "$max"; $((n++)) ))
do
  a=$(($a + $b))
  echo "F($n): $a"
  b=$(($a - $b))
done
```

Recursive:

Works with

:

bash

version 3

```mw
fib() {
  local n=$1
  [ $n -lt 2 ] && echo -n $n || echo -n $(( $( fib $(( n - 1 )) ) + $( fib $(( n - 2 )) ) ))
}
```


## UnixPipes

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** There is a race between parallel commands. `tee last` might open and truncate the file before `cat last` opens it. Then `cat last` pipes the empty file to *xargs*, and *expr* reports a syntax error, and the script hangs forever. |
|---|

```mw
echo 1 |tee last fib ; tail -f fib | while read x
do
   cat last | tee -a fib | xargs -n 1 expr $x + |tee last
done
```


## Ursa

Translation of

:

Python

### Iterative

```mw
def fibIter (int n)
   if (< n 2)
      return n
   end if
   decl int fib fibPrev num
   set fib (set fibPrev 1)
   for (set num 2) (< num n) (inc num)
      set fib (+ fib fibPrev)
      set fibPrev (- fib fibPrev)
   end for
   return fib
end
```


## Ursala

All three methods are shown here, and all have unlimited precision.

```mw
#import std
#import nat

iterative_fib = ~&/(0,1); ~&r->ll ^|\predecessor ^/~&r sum

recursive_fib = {0,1}^?<a/~&a sum^|W/~& predecessor^~/~& predecessor

analytical_fib =

%np+ -+
   mp..round; ..mp2str; sep`+; ^CNC/~&hh take^\~&htt %np@t,
   (mp..div^|\~& mp..sub+ ~~ @rlX mp..pow_ui)^lrlPGrrPX/~& -+
      ^\~& ^(~&,mp..sub/1.E0)+ mp..div\2.E0+ mp..add/1.E0,
      mp..sqrt+ ..grow/5.E0+-+-
```

The analytical method uses arbitrary precision floating point arithmetic from the mpfr library and then converts the result to a natural number. Sufficient precision for an exact result is always chosen based on the argument. This test program computes the first twenty Fibonacci numbers by all three methods.

```mw
#cast %nLL

examples = <.iterative_fib,recursive_fib,analytical_fib>* iota20
```

output:

```
<
   <0,0,0>,
   <1,1,1>,
   <1,1,1>,
   <2,2,2>,
   <3,3,3>,
   <5,5,5>,
   <8,8,8>,
   <13,13,13>,
   <21,21,21>,
   <34,34,34>,
   <55,55,55>,
   <89,89,89>,
   <144,144,144>,
   <233,233,233>,
   <377,377,377>,
   <610,610,610>,
   <987,987,987>,
   <1597,1597,1597>,
   <2584,2584,2584>,
   <4181,4181,4181>>
```


## Uxntal

```mw
%newline { [ LIT2 0a -Console/write ] DEO }

|18 @Console/write

|100 

#1400 
&loop
   DUP #00 SWP fibonacci print/dec newline
   INC GTHk ?&loop
POP2

BRK

@fibonacci ( n* -- n!* )
    ORAk ?{ JMP2r }
    ORAk #01 NEQ ?{ JMP2r } 
    DUP2 #0001 SUB2 fibonacci STH2
    #0002 SUB2 fibonacci
    STH2r ADD2
   JMP2r

@print/dec ( short* -- )
   #000a SWP2 [ LITr ff ]
   &get ( -- )
      SWP2k DIV2k MUL2 SUB2 STH
      POP OVR2 DIV2 ORAk ?&get
   POP2 POP2
   &put ( -- )
      STHr INCk ?{ POP JMP2r }
      [ LIT "0 ] ADD .Console/write DEO !&put
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


## V

Generate n'th fib by using binary recursion

```mw
[fib
   [small?] []
     [pred dup pred]
     [+]
   binrec].
```


## Vala

### Recursive

Using int, but could easily replace with double, long, ulong, etc.

```mw
int fibRec(int n){
   if (n < 2)
      return n;
   else
      return fibRec(n - 1) + fibRec(n - 2);
}
```

### Iterative

Using int, but could easily replace with double, long, ulong, etc.

```mw
int fibIter(int n){
   if (n < 2)
      return n;
   
   int last = 0;
   int cur = 1;
   int next;
   
   for (int i = 1; i < n; ++i){
      next = last + cur;
      last = cur;
      cur = next;
   }
   
   return cur;
}
```


## VAX Assembly

```mw
                               0000  0000     1 .entry  main,0
                            7E 7CFD  0002     2    clro  -(sp)       ;result buffer
                            5E   DD  0005     3    pushl sp       ;pointer to buffer
                            10   DD  0007     4    pushl #16         ;descriptor: len of buffer
                       5B   5E   D0  0009     5    movl  sp, r11        ;-> descriptor
                                     000C     6 
                       7E   01   7D  000C     7    movq  #1, -(sp)      ;init 0,1
                                     000F     8 loop:
               7E   6E   04 AE   C1  000F     9    addl3 4(sp), (sp), -(sp)   ;next element on stack
                            17   1D  0014    10    bvs   ret         ;vs - overflow set, exit
                                     0016    11 
                            5B   DD  0016    12    pushl r11         ;-> descriptor by ref
                         04 AE   DF  0018    13    pushal   4(sp)       ;-> fib on stack by ref
              00000000'GF   02   FB  001B    14    calls #2, g^ots$cvt_l_ti   ;convert integer to string
                            5B   DD  0022    15    pushl r11         ;
              00000000'GF   01   FB  0024    16    calls #1, g^lib$put_output ;show result
                            E2   11  002B    17    brb   loop
                                     002D    18 ret:
                                 04  002D    19    ret
                                     002E    20 .end  main
$ run fib
...
        14930352
        24157817
        39088169
        63245986
       102334155
       165580141
       267914296
       433494437
       701408733
      1134903170
      1836311903
$
```


## Vedit macro language

### Iterative

Calculate fibonacci(#1). Negative values return 0.

```mw
:FIBONACCI:
#11 = 0
#12 = 1
Repeat(#1) {
    #10 = #11 + #12
    #11 = #12
    #12 = #10
}
Return(#11)
```

### Unlimited precision

```mw
// Fibonacci, unlimited precision.
//  input: #1 = n
//  return: fibonacci(n) in text register 10
//
:fibo_unlimited:
if (#1 < 2) {
    Num_Str(#1, 10)
    return
} else {
    Buf_Switch(Buf_Free)
    IC('0') IN
    IC('1') IN
    #10 = #1
    While (#10 > 1) {
        #12 = 0         // carry out
   #15 = 1        // column (ones, tens, hundreds...)
   Repeat (ALL) {    // Sum all columns
       Line(-1)         // n-1
       Goto_col(#15)
       if (At_EOL) {    // all digits added
      break
       }
       #11 = Cur_Char - '0' + #12   // digit of (n-1) + carry
       Line(-1)         // n-2
       Goto_Col(#15)
       if (!At_EOL) {      // may contain fewer digits than n-1
      #11 += Cur_Char - '0'
       }
       Goto_Line(3)     // sum
       EOL
       #12 = #11 / 10      // carry out
       Ins_Char((#11 % 10) + '0')
       #15++         // next column
   }
   if (#12) {        
       Goto_Line(3)
       EOL
       Ins_Char(#12 + '0')    // any extra digit from carry
        }
   BOF
   Del_Line(1)       // Next n
   Line(1) EOL
   Ins_Newline
   #10--
    }
    Goto_Line(2)     // Results on line 2
}
// Copy the results to text register 10 in reverse order
Reg_Empty(10)
While(!At_EOL) {
    Reg_Copy_Block(10, CP, CP+1, INSERT)
    Char()
}
Buf_Quit(OK)
return
```

Test:

```mw
#1 = Get_Num("n: ", STATLINE)
Ins_Text("fibonacci(") Num_Ins(#1, LEFT+NOCR) Ins_Text(") = ")
Call("fibo_unlimited")
Reg_Ins(10) IN
return
```

**Output:**

```
fibonacci(1000) = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
```


## V (Vlang)

Update V (Vlang) to version 0.2.2

### Iterative

```mw
fn fib_iter(n int) int {
    if n < 2 {
      return n
    }

    mut prev, mut fib := 0, 1
    for _ in 0..(n - 1){
        prev, fib = fib, prev + fib
    }
    return fib
}

fn main() {
    for val in 0..11 {
        println('fibonacci(${val:2d}) = ${fib_iter(val):3d}')
    }
}
```

### Recursive

```mw
fn fib_rec(n int) int {
    if n < 2 {
      return n
    }
    return fib_rec(n - 2) + fib_rec(n - 1)
}

fn main() {
    for val in 0..11 {
        println('fibonacci(${val:2d}) = ${fib_rec(val):3d}')
    }
}
```

**Output:**

```
fibonacci( 0) =   0
fibonacci( 1) =   1
fibonacci( 2) =   1
fibonacci( 3) =   2
fibonacci( 4) =   3
fibonacci( 5) =   5
fibonacci( 6) =   8
fibonacci( 7) =  13
fibonacci( 8) =  21
fibonacci( 9) =  34
fibonacci(10) =  55
```


## Wart

### Recursive, all at once

```mw
def (fib n)
  if (n < 2)
    n
    (+ (fib n-1) (fib n-2))
```

### Recursive, using cases

```mw
def (fib n)
  (+ (fib n-1) (fib n-2))

def (fib n) :case (n < 2)
  n
```

### Recursive, using memoization

```mw
def (fib n saved)
  # all args in Wart are optional, and we expect callers to not provide `saved`
  default saved :to (table 0 0 1 1)  # pre-populate base cases
  default saved.n :to
    (+ (fib n-1 saved) (fib n-2 saved))
  saved.n
```


## WDTE

### Memoized Recursive

```mw
let memo fib n => n { > 1 => + (fib (- n 1)) (fib (- n 2)) };
```

### Iterative

```mw
let s => import 'stream';
let a => import 'arrays';

let fib n => (
   let reducer p n => [a.at p 1; + (a.at p 0) (a.at p 1)];
   s.range 1 n
   -> s.reduce [0; 1] reducer
   -> a.at 1
   ;
);
```


## WebAssembly

```mw
(func $fibonacci_nth (param $n i32) (result i32)

    ;;Declare some local registers
    (local $i i32)
    (local $a i32)
    (local $b i32)
 
    ;;Handle first 2 numbers as special cases
    (if (i32.eq (get_local $n) (i32.const 0))
        (return (i32.const 0))
    )
    (if (i32.eq (get_local $n) (i32.const 1))
        (return (i32.const 1))
    )
 
    ;;Initialize first two values
    (set_local $i (i32.const 1))
    (set_local $a (i32.const 0))
    (set_local $b (i32.const 1))
 
    (block 
        (loop 
            ;;Add two previous numbers and store the result
            local.get $a
            local.get $b
            i32.add 
            (set_local $a (get_local $b))
            set_local $b
 
            ;;Increment counter i by one
            (set_local $i                 
                (i32.add 
                    (get_local $i)
                    (i32.const 1)
                )
            )
 
            ;;Check if loop is done
            (br_if 1 (i32.ge_u (get_local $i) (get_local $n)))
            (br 0)
        )
    )
 
    ;;The result is stored in b, so push that to the stack
    get_local $b
)
```


## Whitespace

### Iterative

This program generates Fibonacci numbers until it is forced to terminate.

It was generated from the following pseudo-Assembly.

```mw
push 0
push 1

0:
    swap
    dup
    onum
    push 10
    ochr
    copy 1
    add
    jump 0
```

**Output:**

```
$ wspace fib.ws | head -n 6
0
1
1
2
3
5
```

### Recursive

This program takes a number *n* on standard input and outputs the *n*th member of the Fibonacci sequence.

```mw
; Read n.
push 0
dup
inum
load

; Call fib(n), ouput the result and a newline, then exit.
call 0
onum
push 10
ochr
exit

0:
    dup
    push 2
    sub
    jn 1   ; Return if n < 2.
    dup
    push 1
    sub
    call 0 ; Call fib(n - 1).
    swap   ; Get n back into place.
    push 2
    sub
    call 0 ; Call fib(n - 2).
    add    ; Leave the sum on the stack.
1:
    ret
```

**Output:**

```
$ echo 10 | wspace fibrec.ws
55
```


## Wrapl

### Generator

```mw
DEF fib() (
    VAR seq <- [0, 1]; EVERY SUSP seq:values;
    REP SUSP seq:put(seq:pop + seq[1])[-1];
);
```

To get the 17th number:

```mw
16 SKIP fib();
```

To get the list of all 17 numbers:

```mw
ALL 17 OF fib();
```

### Iterator

Using type match signature to ensure integer argument:

```mw
TO fib(n @ Integer.T) (
    VAR seq <- [0, 1];
    EVERY 3:to(n) DO seq:put(seq:pop + seq[1]);
    RET seq[-1];
);
```


## Wren

```mw
// iterative (quick)
var fibItr = Fn.new { |n|
    if (n < 2) return n
    var a = 0
    var b = 1
    for (i in 2..n) {
        var c = a + b
        a = b
        b = c
    }
    return b
}

// recursive (slow)
var fibRec
fibRec = Fn.new { |n|
    if (n < 2) return n
    return fibRec.call(n-1) + fibRec.call(n-2)
}

System.print("Iterative: %(fibItr.call(36))")
System.print("Recursive: %(fibRec.call(36))")
```

**Output:**

```
Iterative: 14930352
Recursive: 14930352
```


## x86 Assembly

Works with

:

MASM

```mw
TITLE i hate visual studio 4       (Fibs.asm)
;       __         __/--------\
;      >__ \      /  |        |\
;         \  \___/ @  \      /   \__________________
;           \____       \  /                         \\\
;                \____         Coded with love by:    |||
;                      \      Alexander Alvonellos    |||
;                       |          9/29/2011         / ||
;                       |                           |  MM
;                       |      |--------------|     |
;                       |<     |              |<    |
;                       |      |              |     |
;                       |mmmmmm|              |mmmmm|
;; Epic Win. 

INCLUDE Irvine32.inc
                                                                              
.data
   BEERCOUNT = 48;
   Fibs dd 0, 1, BEERCOUNT DUP(0);

.code
main PROC
; I am not responsible for this code.
; They made me write it, against my will.
   ;Here be dragons
   mov esi, offset Fibs; offset array;  ;;were to start (start)
   mov ecx, BEERCOUNT;     ;;count of items (how many)
   mov ebx, 4;       ;;size (in number of bytes)
   call DumpMem;
   
   mov ecx, BEERCOUNT;  ;//http://www.wolframalpha.com/input/?i=F ib%5B47%5D+%3E+4294967295
   mov esi, offset Fibs
   NextPlease:;
      mov eax, [esi];   ;//Get me the data from location at ESI
      add eax, [esi+4]; ;//add into the eax the data at esi + another double (next mem loc)
      mov [esi+8], eax; ;//Move that data into the memory location after the second number
      add esi, 4;       ;//Update the pointer
   loop NextPlease;  ;//Thank you sir, may I have another?
   
   
   ;Here be dragons
   mov esi, offset Fibs; offset array;  ;;were to start (start)
   mov ecx, BEERCOUNT;     ;;count of items (how many)
   mov ebx, 4;       ;;size (in number of bytes)
   call DumpMem;

   exit     ; exit to operating system
main ENDP

END main
```


## xEec

This will display the first 93 numbers of the sequence.

```mw
h#1 h#1 h#1 o# 
h#10 o$ p 
>f 
  o# h#10 o$ p 
  ma h? jnext p
  t
jnf
```


## XLISP

### Analytic

Uses Binet's method, based on the golden ratio, which almost feels like cheating—but the task specification doesn't require any particular algorithm, and this one is straightforward and fast.

```mw
(DEFUN FIBONACCI (N)
    (FLOOR (+ (/ (EXPT (/ (+ (SQRT 5) 1) 2) N) (SQRT 5)) 0.5)))
```

To test it, we'll define a RANGE function and ask for the first 50 numbers in the sequence:

```mw
(DEFUN RANGE (X Y)
    (IF (<= X Y)
        (CONS X (RANGE (+ X 1) Y))))

(PRINT (MAPCAR FIBONACCI (RANGE 1 50)))
```

**Output:**

```
(1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 12586269025)
```

### Tail recursive

Alternatively, this approach is reasonably efficient:

```mw
(defun fibonacci (x)
    (defun fib (a b n)
        (if (= n 2)
            b
            (fib b (+ a b) (- n 1)) ) )
    (if (< x 2)
        x
        (fib 1 1 x) ) )
```


## XPL0

```mw
func Fib1(N);   \Return Nth Fibonacci number using iteration
int N;
int Fn, F0, F1;
[F0:= 0;  F1:= 1;  Fn:= N;
while N > 1 do
        [Fn:= F0 + F1;
        F0:= F1;
        F1:= Fn;
        N:= N-1;
        ];
return Fn;
];

func Fib2(N);   \Return Nth Fibonacci number using recursion
int N;
return if N < 2 then N else Fib2(N-1) + Fib2(N-2);

int N;
[for N:= 0 to 20 do [IntOut(0, Fib1(N));  ChOut(0, ^ )];
 CrLf(0);
 for N:= 0 to 20 do [IntOut(0, Fib2(N));  ChOut(0, ^ )];
 CrLf(0);
]
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 
```


## XQuery

```mw
declare function local:fib($n as xs:integer) as xs:integer {
  if($n < 2)
  then $n
  else local:fib($n - 1) + local:fib($n - 2)
};
```


## YAMLScript

```mw
!ys-0

defn main(n=10):
  loop a 0, b 1, i 1:
    say: a
    when i < n:
      recur: b, (a + b), i.++
```

**Output:**

```
$ ys fibonacci-sequence.ys
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
```


## Z80 Assembly

```mw
; 8 bit version
; IN : a = n  (n <= 13, otherwise overflows)
; OUT: a = FIB(n)

fib8: cp 2
   ret c ; if n < 2 then done

   ld b,a
   dec b ; b = n - 1
   ld c,0   ; F0
   ld a,1   ; F1

f8_l: ld d,a
   add a,c
   ld c,d
   djnz f8_l

   ret
```

8 bits only? That's so 80's!

Let's go 32 bits...

```mw
; 32 bit version
; IN : a = n  (n <= 47, otherwise overflows)
; OUT: hlh'l' = FIB(n)

fib32:   ld l,a   ; lower bytes in the alt set
   ld h,0
   exx   ; now in regular set
   ld hl,0
   cp 2
   ret c ; if n < 2 then done

   dec a ; loopcount = n - 1
   ld bc,0
   exx   ; now in alt set
   ld bc,0
   ld hl,1

f32_l:   ld d,h
   ld e,l
   add hl,bc
   ld b,d
   ld c,e
   exx   ; now in reg set
   ld d,h
   ld e,l
   adc hl,bc
   ld b,d
   ld c,e
   exx   ; now in alt set
   dec a
   jr nz,f32_l

   exx   ; now in reg set
   ret
```


## Zen C

Zen C supports both recursive and iterative approaches natively. The following complete program demonstrates both methods, utilizing pattern matching for the recursive base cases and exclusive range loops for the iterative calculation.

```mw
// Recursive approach using pattern matching
fn fib_rec(n: int) -> int {
    match n {
        0 => { return 0; },
        1 => { return 1; },
        _ => { return fib_rec(n - 1) + fib_rec(n - 2); }
    }
}

// Iterative approach using exclusive range loops
fn fib_iter(n: int) -> int {
    let a = 0;
    let b = 1;
    
    // The loop variable is ignored using the '_' wildcard
    for _ in 0..<n {
        let next = a + b;
        a = b;
        b = next;
    }
    
    return a;
}

fn main() {
    println "Fibonacci Sequence (0 to 20):";
    
    println "\nRecursive:";
    for i in 0..=20 {
        let res = fib_rec(i);
        println "fib({i}) = {res}";
    }

    println "\nIterative:";
    for i in 0..=20 {
        let res = fib_iter(i);
        println "fib({i}) = {res}";
    }
}
```

**Output:**

```
Fibonacci Sequence (0 to 20):

Recursive:
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
fib(8) = 21
fib(9) = 34
fib(10) = 55
fib(11) = 89
fib(12) = 144
fib(13) = 233
fib(14) = 377
fib(15) = 610
fib(16) = 987
fib(17) = 1597
fib(18) = 2584
fib(19) = 4181
fib(20) = 6765

Iterative:
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
fib(8) = 21
fib(9) = 34
fib(10) = 55
fib(11) = 89
fib(12) = 144
fib(13) = 233
fib(14) = 377
fib(15) = 610
fib(16) = 987
fib(17) = 1597
fib(18) = 2584
fib(19) = 4181
fib(20) = 6765
```


## Zig

Translation of

:

C++

```mw
const std = @import("std");

pub fn main() !void {
    var a: u32 = 1;
    var b: u32 = 1;
    const target: u32 = 48;

    for (3..target + 1) |n| {
        const fib = a + b;
        std.debug.print("F({}) = {}\n", .{n, fib});
        a = b;
        b = fib;
    }
}
```

**Output:**

```
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144
F(13) = 233
F(14) = 377
F(15) = 610
F(16) = 987
F(17) = 1597
F(18) = 2584
F(19) = 4181
F(20) = 6765
F(21) = 10946
F(22) = 17711
F(23) = 28657
F(24) = 46368
F(25) = 75025
F(26) = 121393
F(27) = 196418
F(28) = 317811
F(29) = 514229
F(30) = 832040
F(31) = 1346269
F(32) = 2178309
F(33) = 3524578
F(34) = 5702887
F(35) = 9227465
F(36) = 14930352
F(37) = 24157817
F(38) = 39088169
F(39) = 63245986
F(40) = 102334155
F(41) = 165580141
F(42) = 267914296
F(43) = 433494437
F(44) = 701408733
F(45) = 1134903170
F(46) = 1836311903
F(47) = 2971215073
```


## zkl

A slight tweak to the task; creates a function that continuously generates fib numbers

```mw
var fibShift=fcn(ab){ab.append(ab.sum()).pop(0)}.fp(L(0,1));
```

```
zkl: do(15){ fibShift().print(",") }
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,

zkl: do(5){ fibShift().print(",") }
610,987,1597,2584,4181,
```

1. R. L. Graham and N. J. A. Sloane, Anti-Hadamard matrices, Linear Algebra Appl. 62 (1984), 113–137.

Retrieved from "

https://rosettacode.org/wiki/Fibonacci_sequence?oldid=404151

"
