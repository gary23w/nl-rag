---
title: "Sieve of Eratosthenes (part 18/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 18/21
---

## Raku

(formerly Perl 6)

```mw
sub sieve( Int $limit ) {
    my @is-prime = False, False, slip True xx $limit - 1;

    gather for @is-prime.kv -> $number, $is-prime {
        if $is-prime {
            take $number;
            loop (my $s = $number**2; $s <= $limit; $s += $number) {
                @is-prime[$s] = False;
            }
        }
    }
}

(sieve 100).join(",").say;
```

### Set-based approaches

More or less the same as the first Python example:

```mw
sub sieve($n) {
    # Requires n(1 - 1/(log(n-1))) storage
    my $multiples = set();
    gather for 2..$n -> $i {
        unless $i (&) $multiples { # is subset
            take $i;
            $multiples (+)= set($i**2, *+$i ... (* > $n)); # union
        }
    }
}
```

Another set approach is to take the set symmetric difference of all sequences of multiples:

```mw
sub sieve($n) {
    sort keys [⊖] map { $_, 2×$_ ... $n }, 2 .. $n
}
```

Either approach gives:

```mw
say flat sieve(100);
#  (2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
```

### Using a chain of filters

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** This version uses modulo (division) testing and so is a trial division algorithm, not a sieve of Eratosthenes. |
|---|

*Note: while this is "incorrect" by a strict interpretation of the rules, it is being left as an interesting example*

```mw
sub primes ( UInt $n ) {
    gather {
        # create an iterator from 2 to $n (inclusive)
        my $iterator := (2..$n).iterator;

        loop {
            # If it passed all of the filters it must be prime
            my $prime := $iterator.pull-one;
            # unless it is actually the end of the sequence
            last if $prime =:= IterationEnd;

            take $prime; # add the prime to the `gather` sequence

            # filter out the factors of the current prime
            $iterator := Seq.new($iterator).grep(* % $prime).iterator;
            # (2..*).grep(* % 2).grep(* % 3).grep(* % 5).grep(* % 7)…
        }
    }
}

put primes( 100 );
```

Which prints

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## RATFOR

```mw
program prime
#
define(true,1)
define(false,0)
#
integer loop,loop2,limit,k,primes,count
integer isprime(1000)

limit = 1000
count = 0

for (loop=1; loop<=limit; loop=loop+1)
    {
       isprime(loop) = true
    }

isprime(1) = false

for (loop=2; loop<=limit; loop=loop+1)

    {
       if (isprime(loop) == true) 
          {
              count = count + 1
              for (loop2=loop*loop; loop2 <= limit; loop2=loop2+loop)
                 {
                     isprime(loop2) = false
                 }
          }
    }
write(*,*)
write(*,101) count

101 format('There are ',I12,' primes.')

count = 0
for (loop=1; loop<=limit; loop=loop+1)
        if (isprime(loop) == true)
           {
               Count = count + 1
               write(*,'(I6,$)')loop
               if (mod(count,10) == 0) write(*,*)
           }
write(*,*)

end
```


## Rebol

Translation of

:

Red

```mw
Rebol [
    title: "Rosetta code: Sieve of Eratosthenes"
    file:  %Sieve_of_Eratosthenes.r3
    url:   https://rosettacode.org/wiki/Sieve_of_Pritchard
    note:  "Translated from Red"
]

eratosthenes: function [
    "Eratosthenes sieve: finds all primes up to `limit` using a bitset-based sieve."
    limit [integer!]
][
    primes: copy []
    ;; Use a bitset as a boolean composite-marker array.
    ;; Index i is true if i has been marked as composite.
    prim: make bitset! limit
    prim/1: true ;; 1 is not prime, mark it as composite

    rtlim: to integer! square-root limit  ;; Only need primes up to sqrt(limit)

    ;; For each r starting at 2, mark all multiples of r as composite.
    ;; Only need to check up to sqrt(limit), since any composite above it
    ;; must have a prime factor at or below it.
    r: 2
    while [r <= rtlim][
        ;; Mark r*2, r*3, ..., r*floor(limit/r) as composite
        repeat q limit / r - 1 [
            prim/(q + 1 * r): true
        ]
        ;; Advance r to the next unmarked (prime) candidate
        until [not prim/(r: r + 1)]
    ]
    ;; Any index still unset in the bitset is prime.
    repeat i limit [
        unless prim/:i [append primes i]
    ]
    primes
]

probe eratosthenes 100
print rejoin ["Number of primes up to 1'000'000: " length? eratosthenes 1'000'000]
```

**Output:**

```
[2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]
Number of primes up to 1'000'000: 78498
```


## Red

```mw
primes: function [n [integer!]][
   poke prim: make bitset! n 1 true
   r: 2 while [r * r <= n][
      repeat q n / r - 1 [poke prim q + 1 * r true] 
      until [not pick prim r: r + 1]
   ]
   collect [repeat i n [if not prim/:i [keep i]]]
]

primes 100
== [2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]
```


## Retro

```mw
{ [ @start &start v:inc  @end @start gt? ] while } creates an array from 2 to 100
:make filter filters
dup-pair is used or else the number is compared with the flag from if. Curry pushes the argument (the number from 1 to the square root of n) into the quote.
array is used to create an array from 2 to square root of 100.
You go over this array and use filter on the other array from 2 to 100.
~~~
   
    :make-filter (n-q) [ dup-pair eq? not [ mod #0 eq? not ] if ] curry ;
   
   'start var
    #2 !start
   'end var
    #100 !end
   'limit var
    @end n:sqrt #1 + !limit
    
    :array (-a) { [ @start &start v:inc @limit @start gteq? ] while }  ; 
    array
    #2 !start
    { [ @start &start v:inc  @end @start gt? ] while } 
    #2 !start
    array [ make-filter a:filter ] a:for-each [ n:put '_  s:put ] a:for-each 
   
   
~~~
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Refal

```mw
$ENTRY Go {
    = <Print <Primes 100>>;
};

Primes {
    s.N = <Sieve <Iota 2 s.N>>;
};

Iota {
    s.End s.End = s.End;
    s.Start s.End = s.Start <Iota <+ 1 s.Start> s.End>;
};

Cross {
    s.Step e.List = <Cross (s.Step 1) s.Step e.List>;
    (s.Step s.Skip) = ;
    (s.Step 1) s.Item e.List = X <Cross (s.Step s.Step) e.List>;
    (s.Step s.N) s.Item e.List = s.Item <Cross (s.Step <- s.N 1>) e.List>;
};

Sieve {
    = ;
    X e.List = <Sieve e.List>;
    s.N e.List = s.N <Sieve <Cross s.N e.List>>;
};
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## REXX

### Wheel Version restructured

```mw
/*REXX program generates primes via sieve of Eratosthenes algorithm.
* 21.07.2012 Walter Pachl derived from above Rexx version
*                       avoid symbols @ and # (not supported by ooRexx)
*                       avoid negations (think positive)
**********************************************************************/
  highest=200                       /*define highest number to use.  */
  is_prime.=1                       /*assume all numbers are prime.  */
  w=length(highest)                 /*width of the biggest number,   */
                                    /*  it's used for aligned output.*/
  Do j=3 To highest By 2,           /*strike multiples of odd ints.  */
               While j*j<=highest   /* up to sqrt(highest)           */
      If is_prime.j Then Do
        Do jm=j*3 To highest By j+j /*start with next odd mult. of J */
          is_prime.jm=0             /*mark odd mult. of J not prime. */
          End
        End
    End
  np=0                              /*number of primes shown         */
  Call tell 2
  Do n=3 To highest By 2            /*list all the primes found.     */
    If is_prime.n Then Do
      Call tell n
      End
    End
  Exit
tell: Parse Arg prime
      np=np+1
      Say '           prime number' right(np,w) " --> " right(prime,w)
      Return
```

```
           prime number   1  -->    2
           prime number   2  -->    3
           prime number   3  -->    5
           prime number   4  -->    7
           prime number   5  -->   11
           prime number   6  -->   13
           prime number   7  -->   17
           prime number   8  -->   19
           prime number   9  -->   23
           prime number  10  -->   29
           prime number  11  -->   31
           prime number  12  -->   37
           prime number  13  -->   41
           prime number  14  -->   43
           prime number  15  -->   47
           prime number  16  -->   53
           prime number  17  -->   59
           prime number  18  -->   61
           prime number  19  -->   67
           prime number  20  -->   71
           prime number  21  -->   73
           prime number  22  -->   79
           prime number  23  -->   83
           prime number  24  -->   89
           prime number  25  -->   97
           prime number  26  -->  101
           prime number  27  -->  103
           prime number  28  -->  107
           prime number  29  -->  109
           prime number  30  -->  113
           prime number  31  -->  127
           prime number  32  -->  131
           prime number  33  -->  137
           prime number  34  -->  139
           prime number  35  -->  149
           prime number  36  -->  151
           prime number  37  -->  157
           prime number  38  -->  163
           prime number  39  -->  167
           prime number  40  -->  173
           prime number  41  -->  179
           prime number  42  -->  181
           prime number  43  -->  191
           prime number  44  -->  193
           prime number  45  -->  197
           prime number  46  -->  199
```

### Using modules

**Modules:** How to use **Modules:** Source code Procedure Basic in below program is a simple unoptimized sieve. Procedure Primes in Sequences has a few improvements: only odd integers and better loop control. I tried all the tricks: clever memory management, isqrt function, sophisticated wheels... none of them did better.

```mw
-- 23 Aug 2025
include Setting

call Time('r')
say 'SIEVE OF ERATOSTHENES'
say version
say
call GetBasic 200
call ShowPrimes 200
call GetPrimes 200
call ShowPrimes 200
say Format(Time('e'),,3) 'seconds'; say
exit

GetBasic:
procedure expose prim.
arg xx
say 'Basic sieve up to' xx'...'
call Basic xx
say prim.0 'found'
say
return

Basic:
procedure expose prim. work.
arg xx
work. = 1
do i = 2 while i*i <= xx
   if work.i then do
      do j = i*i by i to xx
         work.j = 0
      end
   end
end
zz = 0
do i = 2 to xx
   if work.i then do
      zz = zz+1; prim.zz = i
   end
end
prim.0 = zz
return zz

GetPrimes:
procedure expose prim. flag.
arg xx
say 'Wheeled sieve up to' xx'...'
call Primes xx
say prim.0 'found'
say
return

ShowPrimes:
procedure expose prim.
arg xx
say 'Primes up to' xx
do i = 1 to prim.0
   call Charout ,right(prim.i,4)
   if i//10 = 0 then
      say
end
say
say
return

include Math
```

**Output:**

```
SIEVE OF ERATOSTHENES
REXX-Regina_3.9.7(MT) 5.00 18 Mar 2025

Basic sieve up to 200...
46 found

Primes up to 200
   2   3   5   7  11  13  17  19  23  29
  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97 101 103 107 109 113
 127 131 137 139 149 151 157 163 167 173
 179 181 191 193 197 199

Wheeled sieve up to 200...
46 found

Primes up to 200
   2   3   5   7  11  13  17  19  23  29
  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97 101 103 107 109 113
 127 131 137 139 149 151 157 163 167 173
 179 181 191 193 197 199

0.001 seconds
```


## Ring

```mw
limit = 100
sieve = list(limit)
for i = 2 to limit
    for k = i*i to limit step i 
        sieve[k] = 1
    next
    if sieve[i] = 0 see "" + i + " " ok
next
```

Output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## RISC-V Assembly

for Raspberry pi pico 2 see instructions to page risc v

```mw
# riscv assembly raspberry pico2 rp2350
# program cribleera.s
# connexion putty com3
/*********************************************/
/*           CONSTANTES                      */
/********************************************/
/* for this file see risc-v task include a file */
.include "../../../constantesRiscv.inc"
.equ MAXI,          101
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
szMessNum:           .asciz "Prime : "

.align 2
/*******************************************/ 
/*  UNINITIALED DATA                    */
/*******************************************/ 
.bss
sConvArea:           .skip 24
.align 2
tablePrime:          .skip   4 * MAXI
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
	
	li s0,2                    # start indice
	la s2,tablePrime
	li s3,MAXI
	li s4,1
1:                             # loop for multiple of 2
    sh2add t0,s0,s2            # compute adresse of s0 index
	sw s4,(t0)                 # mark  multiple of 2 
	addi s0,s0,2               # increment indice
	blt s0,s3,1b               # and loop if not maxi
	
    li s0,3                    # new start
	#li s4,1
2:
    sh2add t0,s0,s2            # compute adresse of s0 index
    lw 	t1,(t0)                # load mark
	bnez t1,4f                 # if not zero -> continue
	

    la a0,szMessNum            # else display prime 
	call writeString
	mv a0,s0
    la a1,sConvArea
	call conversion10
	la a0,sConvArea
	call writeString
    la a0,szCariageReturn
	call writeString
	mv s1,s0                   # new prime
3:	                           # and loop to mark multiples of this prime
    sh2add t0,s1,s2            # compute adresse of s0 index
    sw 	s4,(t0)                # mark multiple
	add s1,s0,s1               # add the prime
	ble s1,s3,3b               # and loop if not maxi 
4:	
    addi s0,s0,2               # increment indice
	ble s0,s3,2b               # and loop if not maxi 

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
Prime : 3
Prime : 5
Prime : 7
Prime : 11
Prime : 13
Prime : 17
Prime : 19
Prime : 23
Prime : 29
Prime : 31
Prime : 37
Prime : 41
Prime : 43
Prime : 47
Prime : 53
Prime : 59
Prime : 61
Prime : 67
Prime : 71
Prime : 73
Prime : 79
Prime : 83
Prime : 89
Prime : 97
Prime : 101
Program riscv end OK.
```


## RPL

This is a direct translation from Wikipedia. The variable `i` has been renamed `ii` to avoid confusion with the language constant `i`=√ -1

Works with

:

Halcyon Calc

version 4.2.8

| RPL code | Comment |
|---|---|
| ≪ → n ≪ { } n + 1 CON 'A' STO 2 n √ **FOR** ii **IF** A ii GET **THEN** ii SQ n **FOR** j 'A' j 0 PUT ii **STEP** **END** **NEXT** { } 2 n **FOR** ii **IF** A ii GET **THEN** ii + **END NEXT** 'A' PURGE ≫ ≫ 'SIEVE' STO | SIEVE *( n -- { prime_numbers } )* let A be an array of Boolean values, indexed by 2 to n, initially all set to true. for i = 2, 3, 4, ..., not exceeding √n do if A[i] is true for j = i^2, i^2+i,... not exceeding n do set A[j] := false return all i such that A[i] is true. |

```
100 SIEVE
```

**Output:**

```
1: { 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 }
```

Latest RPL versions allow to remove some slow `FOR..NEXT` loops and use local variables only.

Works with

:

HP

version 49

```
« 'X' DUP 1 4 PICK 1 SEQ DUP → n a seq123
  « 2 n √ FOR ii 
       IF a ii GET THEN
          ii SQ n FOR j
             'a' j 0 PUT ii STEP
       END
    NEXT 
    a seq123 IFT TAIL
» » 'SIEVE' STO
```

Works with

:

HP

version 49


## Ruby

*eratosthenes* starts with `nums = [nil, nil, 2, 3, 4, 5, ..., n]`, then marks (　the nil setting　) multiples of `2, 3, 5, 7, ...` there, then returns all non-nil numbers which are the primes.

```mw
def eratosthenes(n)
  nums = [nil, nil, *2..n]
  (2..Math.sqrt(n)).each do |i|
    (i**2..n).step(i){|m| nums[m] = nil}  if nums[i]
  end
  nums.compact
end
 
p eratosthenes(100)
```

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

### With a wheel

*eratosthenes2* adds more optimizations, but the code is longer.

- The array `nums` only tracks odd numbers (skips multiples of 2).
- The array `nums` holds booleans instead of integers, and every multiple of 3 begins `false`.
- The outer loop skips multiples of 2 and 3.
- Both inner loops skip multiples of 2 and 3.

```mw
def eratosthenes2(n)
  # For odd i, if i is prime, nums[i >> 1] is true.
  # Set false for all multiples of 3.
  nums = [true, false, true] * ((n + 5) / 6)
  nums[0] = false  # 1 is not prime.
  nums[1] = true   # 3 is prime.

  # Outer loop and both inner loops are skipping multiples of 2 and 3.
  # Outer loop checks i * i > n, same as i > Math.sqrt(n).
  i = 5
  until (m = i * i) > n
    if nums[i >> 1]
      i_times_2 = i << 1
      i_times_4 = i << 2
      while m <= n
        nums[m >> 1] = false
        m += i_times_2
        nums[m >> 1] = false
        m += i_times_4  # When i = 5, skip 45, 75, 105, ...
      end
    end
    i += 2
    if nums[i >> 1]
      m = i * i
      i_times_2 = i << 1
      i_times_4 = i << 2
      while m <= n
        nums[m >> 1] = false
        m += i_times_4  # When i = 7, skip 63, 105, 147, ...
        nums[m >> 1] = false
        m += i_times_2
      end
    end
    i += 4
  end

  primes = [2]
  nums.each_index {|i| primes << (i * 2 + 1) if nums[i]}
  primes.pop while primes.last > n
  primes
end

p eratosthenes2(100)
```

This simple benchmark compares *eratosthenes* with *eratosthenes2*.

```mw
require 'benchmark'
Benchmark.bmbm {|x|
  x.report("eratosthenes") { eratosthenes(1_000_000) }
  x.report("eratosthenes2") { eratosthenes2(1_000_000) }
}
```

*eratosthenes2* runs about 4 times faster than *eratosthenes*.

### With the standard library

MRI 1.9.x implements the sieve of Eratosthenes at file prime.rb, `class EratosthensesSeive` (around line 421). This implementation optimizes for space, by packing the booleans into 16-bit integers. It also hardcodes all primes less than 256.

```mw
require 'prime'
p Prime::EratosthenesGenerator.new.take_while {|i| i <= 100}
```


## Run BASIC

```mw
input "Gimme the limit:"; limit
dim flags(limit)
for i = 2 to  limit
 for k = i*i to limit step i 
  flags(k) = 1
 next k
if flags(i) = 0 then print i;", ";
next i
```

```
Gimme the limit:?100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
```


## Rust

### Unboxed Iterator

A slightly more idiomatic, optimized and modern iterator output example.

```mw
fn primes(n: usize) -> impl Iterator<Item = usize> {
    const START: usize = 2;
    if n < START {
        Vec::new()
    } else {
        let mut is_prime = vec![true; n + 1 - START];
        let limit = (n as f64).sqrt() as usize;
        for i in START..limit + 1 {
            let mut it = is_prime[i - START..].iter_mut().step_by(i);
            if let Some(true) = it.next() {
                it.for_each(|x| *x = false);
            }
        }
        is_prime
    }
    .into_iter()
    .enumerate()
    .filter_map(|(e, b)| if b { Some(e + START) } else { None })
}
```

Notes:

1. Starting at an offset of 2 means that an `n < 2` input requires zero allocations, because `Vec::new()` doesn't allocate memory until elements are pushed into it.
2. Using `Vec` as an output to the `if .. {} else {}` condition means the output is statically deterministic, avoiding the need for a boxed trait object.
3. Iterating `is_prime` with `.iter_mut()` and then using `.step_by(i)` makes all the optimizations required, and removes a lot of tediousness.
4. Returning `impl Iterator` allows for static dispatching instead of dynamic dispatching, which is possible because the type is now statically known at compile time, making the zero input/output condition an order of magnitude faster.

### Sieve of Eratosthenes - No optimization

```mw
fn simple_sieve(limit: usize) -> Vec<usize> {

    let mut is_prime = vec![true; limit+1];
    is_prime[0] = false;
    if limit >= 1 { is_prime[1] = false }

    for num in 2..limit+1 {
        if is_prime[num] {
            let mut multiple = num*num;
            while multiple <= limit {
                is_prime[multiple] = false;
                multiple += num;
            }
        }
    }

    is_prime.iter().enumerate()
        .filter_map(|(pr, &is_pr)| if is_pr {Some(pr)} else {None} )
        .collect()
}

fn main() {
    println!("{:?}", simple_sieve(100));
}
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

### Basic Version slightly optimized, Iterator output

The above code doesn't even do the basic optimizing of only culling composites by primes up to the square root of the range as allowed in the task; it also outputs a vector of resulting primes, which consumes memory. The following code fixes both of those, outputting the results as an Iterator:

```mw
use std::iter::{empty, once};
use std::time::Instant;

fn basic_sieve(limit: usize) -> Box<Iterator<Item = usize>> {
    if limit < 2 { return Box::new(empty()) }

    let mut is_prime = vec![true; limit+1];
    is_prime[0] = false;
    if limit >= 1 { is_prime[1] = false }
    let sqrtlmt = (limit as f64).sqrt() as usize + 1; 

    for num in 2..sqrtlmt {
        if is_prime[num] {
            let mut multiple = num * num;
            while multiple <= limit {
                is_prime[multiple] = false;
                multiple += num;
            }
        }
    }

    Box::new(is_prime.into_iter().enumerate()
                .filter_map(|(p, is_prm)| if is_prm { Some(p) } else { None }))

}
 
fn main() {
    let n = 1000000;
    let vrslt = basic_sieve(100).collect::<Vec<_>>();
    println!("{:?}", vrslt);
    let strt = Instant::now();

    // do it 1000 times to get a reasonable execution time span...
    let rslt = (1..1000).map(|_| basic_sieve(n)).last().unwrap();

    let elpsd = strt.elapsed();

    let count = rslt.count();
    println!("{}", count);

    let secs = elpsd.as_secs();
    let millis = (elpsd.subsec_nanos() / 1000000) as u64;
    let dur = secs * 1000 + millis;
    println!("Culling composites took {} milliseconds.", dur);
}
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
78498
Culling composites took 4595 milliseconds.
```

The sieving operation is run for 1000 loops in order to get a reasonable execution time for comparison.

### Odds-only bit-packed array, Iterator output

The following code improves the above code by sieving only odd composite numbers as 2 is the only even prime for a reduction in number of operations by a factor of about two and a half with reduction of memory use by a factor of two, and bit-packs the composite sieving array for a further reduction of memory use by a factor of eight and with some saving in time due to better CPU cache use for a given sieving range; it also demonstrates how to eliminate the redundant array bounds check:

```mw
fn optimized_sieve(limit: usize) -> Box<Iterator<Item = usize>> {
    if limit < 3 {
        return if limit < 2 { Box::new(empty()) } else { Box::new(once(2)) }
    }

    let ndxlmt = (limit - 3) / 2 + 1;
    let bfsz = ((limit - 3) / 2) / 32 + 1;
    let mut cmpsts = vec![0u32; bfsz];
    let sqrtndxlmt = ((limit as f64).sqrt() as usize - 3) / 2 + 1;

    for ndx in 0..sqrtndxlmt {
        if (cmpsts[ndx >> 5] & (1u32 << (ndx & 31))) == 0 {
            let p = ndx + ndx + 3;
            let mut cullpos = (p * p - 3) / 2;
            while cullpos < ndxlmt {
                unsafe { // avoids array bounds check, which is already done above
               let cptr = cmpsts.get_unchecked_mut(cullpos >> 5);
               *cptr |= 1u32 << (cullpos & 31);
                }
//                cmpsts[cullpos >> 5] |= 1u32 << (cullpos & 31); // with bounds check
                cullpos += p;
            }
        }
    }

    Box::new((-1 .. ndxlmt as isize).into_iter().filter_map(move |i| {
                if i < 0 { Some(2) } else {
                    if cmpsts[i as usize >> 5] & (1u32 << (i & 31)) == 0 {
                        Some((i + i + 3) as usize) } else { None } }
    }))
}
```

The above function can be used just by substituting "optimized_sieve" for "basic_sieve" in the previous "main" function, and the outputs are the same except that the time is only 1584 milliseconds, or about three times as fast.

### Unbounded Page-Segmented bit-packed odds-only version with Iterator

**Caution!** This implementation is used in the Extensible prime generator task, so be sure not to break that implementation when changing this code.

While that above code is quite fast, as the range increases above the 10's of millions it begins to lose efficiency due to loss of CPU cache associativity as the size of the one-large-array used for culling composites grows beyond the limits of the various CPU caches. Accordingly the following page-segmented code where each culling page can be limited to not larger than the L1 CPU cache is about four times faster than the above for the range of one billion:

```mw
use std::iter::{empty, once};
use std::rc::Rc;
use std::cell::RefCell;
use std::time::Instant;

const RANGE: u64 = 1000000000;
const SZ_PAGE_BTS: u64 = (1 << 14) * 8; // this should be the size of the CPU L1 cache
const SZ_BASE_BTS: u64 = (1 << 7) * 8;
static CLUT: [u8; 256] = [
   8, 7, 7, 6, 7, 6, 6, 5, 7, 6, 6, 5, 6, 5, 5, 4, 7, 6, 6, 5, 6, 5, 5, 4, 6, 5, 5, 4, 5, 4, 4, 3, 
   7, 6, 6, 5, 6, 5, 5, 4, 6, 5, 5, 4, 5, 4, 4, 3, 6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 
   7, 6, 6, 5, 6, 5, 5, 4, 6, 5, 5, 4, 5, 4, 4, 3, 6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 
   6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 5, 4, 4, 3, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 2, 1, 
   7, 6, 6, 5, 6, 5, 5, 4, 6, 5, 5, 4, 5, 4, 4, 3, 6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 
   6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 5, 4, 4, 3, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 2, 1, 
   6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 5, 4, 4, 3, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 2, 1, 
   5, 4, 4, 3, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 2, 1, 4, 3, 3, 2, 3, 2, 2, 1, 3, 2, 2, 1, 2, 1, 1, 0 ];

fn count_page(lmti: usize, pg: &[u32]) -> i64 {
   let pgsz = pg.len(); let pgbts = pgsz * 32;
   let (lmt, icnt) = if lmti >= pgbts { (pgsz, 0) } else {
      let lstw = lmti / 32;
      let msk = 0xFFFFFFFEu32 << (lmti & 31);
      let v = (msk | pg[lstw]) as usize;
      (lstw, (CLUT[v & 0xFF] + CLUT[(v >> 8) & 0xFF]
         + CLUT[(v >> 16) & 0xFF] + CLUT[v >> 24]) as u32)
   };
   let mut count = 0u32;
   for i in 0 .. lmt {
      let v = pg[i] as usize;
      count += (CLUT[v & 0xFF] + CLUT[(v >> 8) & 0xFF]
               + CLUT[(v >> 16) & 0xFF] + CLUT[v >> 24]) as u32;
   }
   (icnt + count) as i64
}

fn primes_pages() -> Box<Iterator<Item = (u64, Vec<u32>)>> {
   // a memoized iterable enclosing a Vec that grows as needed from an Iterator...
   type Bpasi = Box<Iterator<Item = (u64, Vec<u32>)>>; // (lwi, base cmpsts page)
   type Bpas = Rc<(RefCell<Bpasi>, RefCell<Vec<Vec<u32>>>)>; // interior mutables
   struct Bps(Bpas); // iterable wrapper for base primes array state
   struct Bpsi<'a>(usize, &'a Bpas); // iterator with current pos, state ref's
   impl<'a> Iterator for Bpsi<'a> {
      type Item = &'a Vec<u32>;
      fn next(&mut self) -> Option<Self::Item> {
         let n = self.0; let bpas = self.1;
         while n >= bpas.1.borrow().len() { // not thread safe
            let nbpg = match bpas.0.borrow_mut().next() {
                        Some(v) => v, _ => (0, vec!()) };
            if nbpg.1.is_empty() { return None } // end if no source iter
            bpas.1.borrow_mut().push(cnvrt2bppg(nbpg));
         }
         self.0 += 1; // unsafe pointer extends interior -> exterior lifetime
         // multi-threading might drop following Vec while reading - protect
         let ptr = &bpas.1.borrow()[n] as *const Vec<u32>;
         unsafe { Some(&(*ptr)) }
      }
   }
   impl<'a> IntoIterator for &'a Bps {
      type Item = &'a Vec<u32>;
      type IntoIter = Bpsi<'a>;
      fn into_iter(self) -> Self::IntoIter {
         Bpsi(0, &self.0)
      }
   }
   fn make_page(lwi: u64, szbts: u64, bppgs: &Bpas)
         -> (u64, Vec<u32>) {
      let nxti = lwi + szbts;
      let pbts = szbts as usize;
      let mut cmpsts = vec!(0u32; pbts / 32);
      'outer: for bpg in Bps(bppgs.clone()).into_iter() { // in the inner tight loop...
         let pgsz = bpg.len();
         for i in 0 .. pgsz {
            let p = bpg[i] as u64; let pc = p as usize;
            let s = (p * p - 3) / 2;
            if s >= nxti { break 'outer; } else { // page start address:
               let mut cp = if s >= lwi { (s - lwi) as usize } else {
                  let r = ((lwi - s) % p) as usize;
                  if r == 0 { 0 } else { pc - r }
               };
               while cp < pbts {
                  unsafe { // avoids array bounds check, which is already done above
                     let cptr = cmpsts.get_unchecked_mut(cp >> 5);
                     *cptr |= 1u32 << (cp & 31); // about as fast as it gets...
                  }
//                cmpsts[cp >> 5] |= 1u32 << (cp & 31);
                  cp += pc;
               }
            }
         }
      }
      (lwi, cmpsts)
   }
   fn pages_from(lwi: u64, szbts: u64, bpas: Bpas)
         -> Box<Iterator<Item = (u64, Vec<u32>)>> {
      struct Gen(u64,  u64);
      impl Iterator for Gen {
         type Item = (u64, u64);
         #[inline]
         fn next(&mut self) -> Option<(u64, u64)> {
            let v = self.0; let inc = self.1; // calculate variable size here
            self.0 = v + inc;
            Some((v, inc))
         }
      }
      Box::new(Gen(lwi, szbts)
               .map(move |(lwi, szbts)| make_page(lwi, szbts, &bpas)))
   }
   fn cnvrt2bppg(cmpsts: (u64, Vec<u32>)) -> Vec<u32> {
      let (lwi, pg) = cmpsts;
      let pgbts = pg.len() * 32;
      let cnt = count_page(pgbts, &pg) as usize;
      let mut bpv = vec!(0u32; cnt);
      let mut j = 0; let bsp = (lwi + lwi + 3) as usize;
      for i in 0 .. pgbts {
         if (pg[i >> 5] & (1u32 << (i & 0x1F))) == 0u32 {
            bpv[j] = (bsp + i + i) as u32; j += 1;
         }
      }
      bpv
   }
   // recursive Rc/RefCell variable bpas - used only for init, then fixed ...
   // start with just enough base primes to init the first base primes page...
   let base_base_prms = vec!(3u32,5u32,7u32);
   let rcvv = RefCell::new(vec!(base_base_prms));
   let bpas: Bpas = Rc::new((RefCell::new(Box::new(empty())), rcvv));
   let initpg = make_page(0, 32, &bpas); // small base primes page for SZ_BASE_BTS = 2^7 * 8
   *bpas.1.borrow_mut() = vec!(cnvrt2bppg(initpg)); // use for first page
   let frstpg = make_page(0, SZ_BASE_BTS, &bpas); // init bpas for first base prime page
   *bpas.0.borrow_mut() = pages_from(SZ_BASE_BTS, SZ_BASE_BTS, bpas.clone()); // recurse bpas
   *bpas.1.borrow_mut() = vec!(cnvrt2bppg(frstpg)); // fixed for subsequent pages
   pages_from(0, SZ_PAGE_BTS, bpas) // and bpas also used here for main pages
}
 
fn primes_paged() -> Box<Iterator<Item = u64>> {
   fn list_paged_primes(cmpstpgs: Box<Iterator<Item = (u64, Vec<u32>)>>)
         -> Box<Iterator<Item = u64>> {
      Box::new(cmpstpgs.flat_map(move |(lwi, cmpsts)| {
         let pgbts = (cmpsts.len() * 32) as usize;
         (0..pgbts).filter_map(move |i| {
            if cmpsts[i >> 5] & (1u32 << (i & 31)) == 0 {
               Some((lwi + i as u64) * 2 + 3) } else { None } }) }))
   }
   Box::new(once(2u64).chain(list_paged_primes(primes_pages())))
}

fn count_primes_paged(top: u64) -> i64 {
   if top < 3 { if top < 2 { return 0i64 } else { return 1i64 } }
   let topi = (top - 3u64) / 2;
   primes_pages().take_while(|&(lwi, _)| lwi <= topi)
      .map(|(lwi, pg)| { count_page((topi - lwi) as usize, &pg) })
      .sum::<i64>() + 1
}

fn main() {
   let n = 262146;
   let vrslt = primes_paged()
         .take_while(|&p| p <= 100)
         .collect::<Vec<_>>();
   println!("{:?}", vrslt);

   let strt = Instant::now();

// let count = primes_paged().take_while(|&p| p <= RANGE).count(); // slow way to count
   let count = count_primes_paged(RANGE); // fast way to count

   let elpsd = strt.elapsed();

   println!("{}", count);

   let secs = elpsd.as_secs();
   let millis = (elpsd.subsec_nanos() / 1000000) as u64;
   let dur = secs * 1000 + millis;
   println!("Culling composites took {} milliseconds.", dur);
}
```

The output is about the same as the previous codes except much faster; as well as cache size improvements mentioned above, it has a population count primes counting function that is able to determine the number of found primes about twice as fast as using the Iterator count() method (commented out and labelled as "the slow way" in the main function).

As listed above, the code maintains its efficiency up to about sixteen billion, and can easily be extended to be useful above that point by having the buffer size dynamically calculated to be proportional to the square root of the current range as commented in the code.

It would also be quite easy to extend the code to use multi-threading per page so that the time would be reduced proportionally to the number of true CPU cores used (not Hyper-Threaded ones) as in four true cores for many common high end desktop CPU's.

Before being extended to truly huge ranges such a 1e14, the code should have maximum wheel factorization added (2;3;5;7 wheels and the culling buffers further pre-culled by the primes (11;13;17; and maybe 19), which would speed it up by another factor of four or so for the range of one billion. It would also be possible to use extreme loop unrolling techniques such as used by "primesieve" written in C/C++ to increase the speed for this range by another factor of two or so.

The above code demonstrates some techniques to work within the limitations of Rust's ownership/borrowing/lifetime memory model as it: 1) uses a recursive secondary base primes Iterator made persistent by using a Vec that uses its own value as a source of its own page stream, 2) this is done by using a recursive variable that accessed as a Rc reference counted heap value with internal mutability by a pair of RefCell's, 3) note that the above secondary stream is not thread safe and needs to have the Rc changed to an Arc, the RefCell's changed to Mutex'es or (probably preferably RwLock's that enclose/lock all reading and writing operations in the secondary stream "Bpsi"'s next() method, and 4) the use of Iterators where their performance doesn't matter (at the page level) while using tight loops at more inner levels.


## S-BASIC

```mw
comment
   Find primes up to the specified limit (here 1,000) using
   classic Sieve of Eratosthenes
end

$constant limit = 1000
$constant false = 0
$constant true = FFFFH

var i, k, count, col = integer
dim integer flags(limit)

print "Finding primes from 2 to";limit

rem - initialize table
for i = 1 to limit
  flags(i) = true
next i

rem - sieve for primes
for i = 2 to int(sqr(limit))
  if flags(i) = true then
     for k = (i*i) to limit step i
        flags(k) = false
     next k
next i

rem - write out primes 10 per line
count = 0
col = 1
for i = 2 to limit
   if flags(i) = true then
      begin
         print using "#####";i;
         count = count + 1
         col = col + 1
         if col > 10 then
            begin
               print
               col = 1
            end
      end
next i
print
print count; " primes were found."

end
```

**Output:**

```
Finding primes from 2 to 1000
    2    3    5    7   11   13   17   19   23   29
   31   37   41   43   47   53   59   61   67   71
                      . . .
  877  881  883  887  907  911  919  929  937  941
  947  953  967  971  977  983  991  997
168 primes were found.
```


## SAS

The following defines an IML routine to compute the sieve, and as an example stores the primes below 1000 in a dataset.

```mw
proc iml;
start sieve(n);
    a = J(n,1);
    a[1] = 0;
    do i = 1 to n;
        if a[i] then do;
            if i*i>n then return(a);
            a[i*(i:int(n/i))] = 0;
        end;
    end;
finish;

a = loc(sieve(1000))`;
create primes from a;
append from a;
close primes;
quit;
```


## SASL

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** These use REM (division) testing and so are Trial Division algorithms, not Sieve of Eratosthenes. |
|---|

Copied from SASL manual, top of page 36. This provides an infinite list.

```mw
show primes
WHERE
primes = sieve (2...)
sieve (p : x ) = p : sieve {a <- x; a REM p > 0}
?
```

The limited list for the first 1000 numbers

```mw
show primes
WHERE
primes = sieve (2..1000)
sieve (p : x ) = p : sieve {a <- x; a REM p > 0}
?
```
