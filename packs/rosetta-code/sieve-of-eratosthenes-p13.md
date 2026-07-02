---
title: "Sieve of Eratosthenes (part 13/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 13/21
---

## Lambdatalk

```mw
• 1) create an array of natural numbers, [0,1,2,3, ... ,n-1]
• 2) the 3rd number is 2, we set to dots all its composites by steps of 2,
• 3) the 4th number is 3, we set to dots all its composites by steps of 3,
• 4) the 6th number is 5, we set to dots all its composites by steps of 5,
• 5) the remaining numbers are primes and we clean all dots.

For instance:

1: 0 0 0 0 0 0 0 0 0 9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
2: 0 1 2 3 . 5 . 7 . 9 . 1 . 3 . 5 . 7 . 9 . 1 . 3 . 5 . 7 . 9 .
3: 0 1 2 3 . 5 . 7 . . . 1 . 3 . . . 7 . 9 . . . 3 . 5 . . . 9 .
4: 0 1 2 3 . 5 . 7 . . . 1 . 3 . . . 7 . 9 . . . 3 . . . . . 9 .
       | |   |   |       |   |       |   |       |           |
5:     0 0   0   0       1   1       1   1       2           2
       2 3   5   7       1   3       7   9       3           9

1) recursive version {rsieve n}

{def rsieve

  {def rsieve.mark
   {lambda {:n :a :i :j}
    {if {< :j :n}
     then {rsieve.mark :n 
                       {A.set! :j . :a}
                       :i
                       {+ :i :j}}
     else :a}}}

  {def rsieve.loop
   {lambda {:n :a :i}
    {if {< {* :i :i} :n}
     then {rsieve.loop :n
                       {if {W.equal? {A.get :i :a} .}
                        then :a 
                        else {rsieve.mark :n :a :i {* :i :i}}}
                       {+ :i 1}}
     else :a}}}

 {lambda {:n}
  {S.replace \s by space in 
   {S.replace (\[|\]|\.|,) by space in
    {A.disp
     {A.slice 2 -1 
      {rsieve.loop :n
       {A.new {S.serie 0 :n}} 2}}}}}}}
-> rsieve

{rsieve 1000}
-> 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997

Note: this version doesn't avoid stackoverflow.

2) iterative version {isieve n}

{def isieve

 {def isieve.mark 
  {lambda {:n :a :i}
   {S.map {{lambda {:a :j} {A.set! :j . :a}
           } :a}
          {S.serie {* :i :i} :n :i} }}}

 {lambda {:n}
  {S.replace \s by space in 
   {S.replace (\[|\]|\.|,) by space in
    {A.disp
     {A.slice 2 -1 
      {S.last 
       {S.map {{lambda {:n :a :i} {if {W.equal? {A.get :i :a} .}
                                   then
                                   else {isieve.mark :n :a :i}}
               } :n {A.new {S.serie 0 :n}}}
              {S.serie 2 {sqrt :n} 1}}}}}}}}}
-> isieve

{isieve 1000}
-> 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997

Notes: 
- this version avoids stackoverflow. 
- From 1 to 1000000 there are 78500 primes (computed in ~15000ms) and the last is 999983.
```


## langur

Translation of

:

D

```mw
val sieve = fn(limit) {
    if limit < 2: return []

    var composite = limit * [false]
    composite[1] = true

    for n in 2 .. trunc(limit ^/ 2) + 1 {
        if not composite[n] {
            for k = n^2 ; k < limit ; k += n {
                composite[k] = true
            }
        }
    }

    filter series(limit-1), by=fn(n) { not composite[n] }
}

writeln sieve(100)
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## LFE

```mw
(defmodule eratosthenes
   (export (sieve 1)))

(defun sieve (limit)
   (sieve limit (lists:seq 2 limit)))

(defun sieve
   ((limit (= l (cons p _))) (when (> (* p p) limit))
      l)
   ((limit (cons p ns))
      (cons p (sieve limit (remove-multiples p (* p p) ns)))))

(defun remove-multiples (p q l)
   (lists:reverse (remove-multiples p q l '())))

(defun remove-multiples
   ((_ _ '() s) s)
   ((p q (cons q ns) s)
      (remove-multiples p q ns s))
   ((p q (= r (cons a _)) s) (when (> a q))
      (remove-multiples p (+ q p) r s))
   ((p q (cons n ns) s)
      (remove-multiples p q ns (cons n s))))
```

**Output:**

```
lfe> (slurp "sieve.lfe")
#(ok eratosthenes)
lfe> (sieve 100)
(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
```


## Liberty BASIC

```mw
    'Notice that arrays are globally visible to functions.
    'The sieve() function uses the flags() array.
    'This is a Sieve benchmark adapted from BYTE 1985
    ' May, page 286

    size = 7000
    dim flags(7001)
    start = time$("ms")
    print sieve(size); " primes found."
    print "End of iteration.  Elapsed time in milliseconds: "; time$("ms")-start
    end

    function sieve(size)
        for i = 0 to size
            if flags(i) = 0 then
                prime = i + i + 3
                k = i + prime
                while k <= size
                    flags(k) = 1
                    k = k + prime
                wend
                sieve = sieve + 1
            end if
        next i
    end function
```


## Limbo

```mw
implement Sieve;

include "sys.m";
   sys: Sys;
   print: import sys;
include "draw.m";
   draw: Draw;

Sieve : module
{
   init : fn(ctxt : ref Draw->Context, args : list of string);
};

init (ctxt: ref Draw->Context, args: list of string)
{
   sys = load Sys Sys->PATH;

   limit := 201;
   sieve : array of int;
   sieve = array [201] of {* => 1};
   (sieve[0], sieve[1]) = (0, 0);

   for (n := 2; n < limit; n++) {
      if (sieve[n]) {
         for (i := n*n; i < limit; i += n) {
            sieve[i] = 0;
         }
      }
   }

   for (n = 1; n < limit; n++) {
      if (sieve[n]) {
         print ("%4d", n);
      } else {
         print("   .");
      };
      if ((n%20) == 0) 
         print("\n\n");
   }  
}
```


## Lingo

```mw
-- parent script "sieve"
property _sieve

----------------------------------------
-- @constructor
----------------------------------------
on new (me)
    me._sieve = []
    return me
end

----------------------------------------
-- Returns list of primes <= n
----------------------------------------
on getPrimes (me, limit)
    if me._sieve.count<limit then me._primeSieve(limit)
    primes = []
    repeat with i = 2 to limit
        if me._sieve[i] then primes.add(i)
    end repeat
    return primes
end

----------------------------------------
-- Sieve of Eratosthenes
----------------------------------------
on _primeSieve (me, limit)
    me._sieve = [0]
    repeat with i = 2 to limit
        me._sieve[i] = 1
    end repeat
    c = sqrt(limit)
    repeat with i = 2 to c
        if (me._sieve[i]=0) then next repeat
        j = i*i -- start with square
        repeat while (j<=limit)
            me._sieve[j] = 0
            j = j + i
        end repeat
    end repeat
end
```

```mw
sieve = script("sieve").new()
put sieve.getPrimes(100)
```

**Output:**

```
-- [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## LiveCode

```mw
function sieveE int
    set itemdel to comma
    local sieve
    repeat with i = 2 to int
        put i into sieve[i]
    end repeat
    put 2 into n
    repeat while n < int
        repeat with p = n to int step n
            if p = n then 
                next repeat
            else
                put empty into sieve[p]
            end if
        end repeat
        add 1 to n
    end repeat
    combine sieve with comma
    filter items of sieve without empty
    sort items of sieve ascending numeric
    return sieve
end sieveE
```

Example

```mw
put sieveE(121)
--  2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113
```

```mw
# Sieve of Eratosthenes
# calculates prime numbers up to a given number
 
on mouseUp
   put field "maximum" into limit  
   put the ticks into startTicks      # start a timer
   repeat with i = 2 to limit step 1  # load array with zeros
      put 0 into prime_array[i]
   end repeat
   
   repeat with i = 2 to trunc(sqrt(limit)) # truncate square root
      if prime_array[i] = 0 then  
         repeat with k = (i * i) to limit step i
            delete variable prime_array[k] # remove non-primes
         end repeat
      end if
   end repeat
   put the ticks - startTicks into elapsedTicks  # stop timer
   put elapsedTicks / 60 into field "elapsed"    # calculate time
   
   put the keys of prime_array into prime_numbers # array to variable
   put the number of lines of keys of prime_array into field "count"
   sort lines of prime_numbers ascending numeric  
   put prime_numbers into field "primeList"      # show prime numbers
end mouseUp
```

LiveCode output example

LiveCode uses a mouse graphical drag and drop. No text code was used to create a button and fields; The user enters a number into the 'maximum' field and then clicks a button to run the code. It runs identically whether in the LiveCode IDE or when compiled to a executable on Mac, Windows, and Linux.

The example was run on an Intel i5 CPU @ 3.29 GHz; all primes found up to 1,000,000 in 3 seconds.


## Logo

```
to sieve :limit
  make "a (array :limit 2)     ; initialized to empty lists
  make "p []
  for [i 2 :limit] [
    if empty? item :i :a [
      queue "p :i
      for [j [:i * :i] :limit :i] [setitem :j :a :i]
    ]
  ]
  output :p
end
print sieve 100   ; 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Logtalk

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** Not a true Sieve of Eratosthenes but rather a Trial Division Sieve |
|---|

```
due to the use of mod (modulo = division) in the filter function.
```

A coinduction based solution just for fun:

```mw
:- object(sieve).

   :- public(primes/2).

   :- coinductive([
      sieve/2, filter/3
   ]).

   % computes a coinductive list with all the primes in the 2..N interval
   primes(N, Primes) :-
      generate_infinite_list(N, List),
      sieve(List, Primes).

   % generate a coinductive list with a 2..N repeating patern
   generate_infinite_list(N, List) :-
      sequence(2, N, List, List).

   sequence(Sup, Sup, [Sup| List], List) :-
      !.
   sequence(Inf, Sup, [Inf| List], Tail) :-
      Next is Inf + 1,
      sequence(Next, Sup, List, Tail).

   sieve([H| T], [H| R]) :-
      filter(H, T, F),
      sieve(F, R).

   filter(H, [K| T], L) :-
      (  K > H, K mod H =:= 0 ->
         % throw away the multiple we found
         L = T1
      ;  % we must not throw away the integer used for filtering
         % as we must return a filtered coinductive list
         L = [K| T1]
      ),
      filter(H, T, T1).

:- end_object.
```

Example query:

```mw
?- sieve::primes(20, P).
P = [2, 3|_S1], % where
    _S1 = [5, 7, 11, 13, 17, 19, 2, 3|_S1] .
```


## LOLCODE

```mw
HAI 1.2
CAN HAS STDIO?

HOW IZ I Eratosumthin YR Max
  I HAS A Siv ITZ A BUKKIT
  Siv HAS A SRS 1 ITZ 0
  I HAS A Index ITZ 2
  IM IN YR Inishul UPPIN YR Dummy WILE DIFFRINT Index AN SUM OF Max AN 1
    Siv HAS A SRS Index ITZ 1
    Index R SUM OF Index AN 1
  IM OUTTA YR Inishul

  I HAS A Prime ITZ 2
  IM IN YR MainLoop UPPIN YR Dummy WILE BOTH SAEM Max AN BIGGR OF Max AN PRODUKT OF Prime AN Prime
    BOTH SAEM Siv'Z SRS Prime AN 1
    O RLY?
      YA RLY
        Index R SUM OF Prime AN Prime
        IM IN YR MarkMultipulz UPPIN YR Dummy WILE BOTH SAEM Max AN BIGGR OF Max AN Index
          Siv'Z SRS Index R 0
          Index R SUM OF Index AN Prime
        IM OUTTA YR MarkMultipulz
    OIC
    Prime R SUM OF Prime AN 1
  IM OUTTA YR MainLoop

  Index R 1
  I HAS A First ITZ WIN
  IM IN YR PrintPrimes UPPIN YR Dummy WILE BOTH SAEM Max AN BIGGR OF Max AN Index
    BOTH SAEM Siv'Z SRS Index AN 1
    O RLY?
      YA RLY
        First
        O RLY?
          YA RLY
            First R FAIL
          NO WAI
            VISIBLE ", "!
        OIC
        VISIBLE Index!
    OIC
    Index R SUM OF Index AN 1
  IM OUTTA YR PrintPrimes
  VISIBLE ""
IF U SAY SO

I IZ Eratosumthin YR 100 MKAY

KTHXBYE
```

**Output:**

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
```


## Lua

```mw
function erato(n)
  if n < 2 then return {} end
  local t = {0} -- clears '1'
  local sqrtlmt = math.sqrt(n)
  for i = 2, n 
    do t[i] = 1 
  end
  for i = 2, sqrtlmt do 
        if t[i] ~= 0 then 
               for j = i*i, n, i do  
                  t[j] = 0 
               end 
        end 
  end
  local primes = {}
  for i = 2, n do 
         if t[i] ~= 0 then 
              table.insert(primes, i) 
         end 
  end
  return primes
end
```

The following changes the code to **odds-only** using the same large array-based algorithm:

```mw
function erato2(n)
  if n < 2 then return {} end
  if n < 3 then return {2} end
  local t = {}
  local lmt = (n - 3) / 2
  local sqrtlmt = (math.sqrt(n) - 3) / 2
  for i = 0, lmt do t[i] = 1 end
  for i = 0, sqrtlmt do if t[i] ~= 0 then
    local p = i + i + 3
    for j = (p*p - 3) / 2, lmt, p do t[j] = 0 end end end
  local primes = {2}
  for i = 0, lmt do if t[i] ~= 0 then table.insert(primes, i + i + 3) end end
  return primes
end
```

The following code implements **an odds-only "infinite" generator style using a table as a hash table**, including postponing adding base primes to the table:

```mw
function newEratoInf()
  local _cand = 0; local _lstbp = 3; local _lstsqr = 9
  local _composites = {}; local _bps = nil
  local _self = {}
  function _self.next()
    if _cand < 9 then if _cand < 1 then _cand = 1; return 2
                     elseif _cand >= 7 then
                       --advance aux source base primes to 3...
                       _bps = newEratoInf()
                       _bps.next(); _bps.next() end end
    _cand = _cand + 2
    if _composites[_cand] == nil then -- may be prime
      if _cand >= _lstsqr then -- if not the next base prime
        local adv = _lstbp + _lstbp -- if next base prime
        _composites[_lstbp * _lstbp + adv] = adv -- add cull seq
        _lstbp = _bps.next(); _lstsqr = _lstbp * _lstbp -- adv next base prime
        return _self.next()
      else return _cand end -- is prime
    else
      local v = _composites[_cand]
      _composites[_cand] = nil
      local nv = _cand + v
      while _composites[nv] ~= nil do nv = nv + v end
      _composites[nv] = v
      return _self.next() end
  end
  return _self
end

gen = newEratoInf()
count = 0
while gen.next() <= 10000000 do count = count + 1 end -- sieves to 10 million
print(count)
```

which outputs "664579" in about three seconds. As this code uses much less memory for a given range than the previous ones and retains efficiency better with range, it is likely more appropriate for larger sieve ranges.


## Lucid

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** Not a true Sieve of Eratosthenes but rather a Trial Division Sieve |
|---|

```
prime
 where
    prime = 2 fby (n whenever isprime(n));
    n = 3 fby n+2;
    isprime(n) = not(divs) asa divs or prime*prime > N
                    where
                      N is current n;
                      divs = N mod prime eq 0;
                    end;
 end
```

### recursive

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** Not a true Sieve of Eratosthenes but rather a Trial Division Sieve |
|---|

```
sieve( N )
   where
    N = 2 fby N + 1;
    sieve( i ) =
      i fby sieve ( i whenever i mod first i ne 0 ) ;
   end
```


## M2000 Interpreter

```mw
Module EratosthenesSieve (x) {
      \\ Κόσκινο του Ερατοσθένη
      Profiler
      If x>2000000 Then Exit
      Dim i(x+1): k=2: k2=sqrt(x)
      While k<=k2{if i(k) else for m=k*k to x step k{i(m)=1}
      k++}
      Print str$(timecount/1000,"####0.##")+" s"
      Input "Press enter skip print or a non zero to get results:", a%
      if a% then For i=2to x{If i(i)=0 Then Print i, 
      }
      Print:Print "Done"
}
EratosthenesSieve 1000
```


## M4

```mw
define(`lim',100)dnl
define(`for',
   `ifelse($#,0,
      ``$0'',
      `ifelse(eval($2<=$3),1,
         `pushdef(`$1',$2)$5`'popdef(`$1')$0(`$1',eval($2+$4),$3,$4,`$5')')')')dnl
for(`j',2,lim,1,
   `ifdef(a[j],
      `',
      `j for(`k',eval(j*j),lim,j,
         `define(a[k],1)')')')
```

Output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## MAD

```mw
            NORMAL MODE IS INTEGER
          
          R TO GENERATE MORE PRIMES, CHANGE BOTH THESE NUMBERS          
            BOOLEAN PRIME
            DIMENSION PRIME(10000)
            MAXVAL = 10000
            PRINT FORMAT BEGIN,MAXVAL
            
          R ASSUME ALL ARE PRIMES AT BEGINNING
            THROUGH SET, FOR I=2, 1, I.G.MAXVAL
SET         PRIME(I) = 1B

          R REMOVE ALL PROVEN COMPOSITES
            SQMAX = SQRT.(MAXVAL)
            THROUGH NEXT, FOR P=2, 1, P.G.SQMAX
            WHENEVER PRIME(P)
                THROUGH MARK, FOR I=P*P, P, I.G.MAXVAL
MARK            PRIME(I) = 0B
NEXT        END OF CONDITIONAL

          R PRINT PRIMES
            THROUGH SHOW, FOR P=2, 1, P.G.MAXVAL
SHOW        WHENEVER PRIME(P), PRINT FORMAT NUMFMT, P
            
            VECTOR VALUES BEGIN = $13HPRIMES UP TO ,I9*$
            VECTOR VALUES NUMFMT = $I9*$
            END OF PROGRAM
```

**Output:**

```
PRIMES UP TO     10000
        2
        3
        5
        7
       11
       13
       17
...
     9979
     9983
     9985
     9989
     9991
     9995
     9997
```


## Maple

```mw
Eratosthenes := proc(n::posint) 
  local numbers_to_check, i, k; 
  numbers_to_check := [seq(2 .. n)]; 
  for i from 2 to floor(sqrt(n)) do 
      for k from i by i while k <= n do 
          if evalb(k <> i) then
            numbers_to_check[k - 1] := 0; 
          end if; 
      end do; 
  end do; 
  numbers_to_check := remove(x -> evalb(x = 0), numbers_to_check); 
  return numbers_to_check; 
  end proc:
```

**Output:**

```
Eratosthenes(100);
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## Mathematica /Wolfram Language

```mw
Eratosthenes[n_] := Module[{numbers = Range[n]},
  Do[If[numbers[[i]] != 0, Do[numbers[[i j]] = 0, {j, 2, n/i}]], {i, 
    2, Sqrt[n]}];
  Select[numbers, # > 1 &]]

Eratosthenes[100]
```

### Slightly Optimized Version

The below has been improved to not require so many operations per composite number cull for about two thirds the execution time:

```mw
Eratosthenes[n_] := Module[{numbers = Range[n]},
  Do[If[numbers[[i]] != 0, Do[numbers[[j]] = 0, {j,i i,n,i}]],{i,2,Sqrt[n]}];
  Select[numbers, # > 1 &]]

Eratosthenes[100]
```

### Sieving Odds-Only Version

The below has been further improved to only sieve odd numbers for a further reduction in execution time by a factor of over two:

```mw
Eratosthenes2[n_] := Module[{numbers = Range[3, n, 2], limit = (n - 1)/2}, 
  Do[c = numbers[[i]]; If[c != 0,
    Do[numbers[[j]] = 0, {j,(c c - 1)/2,limit,c}]], {i,1,(Sqrt[n] - 1)/2}];
  Prepend[Select[numbers, # > 1 &], 2]]

Eratosthenes2[100]
```


## MATLAB / Octave

### Somewhat optimized true Sieve of Eratosthenes

```mw
function P = erato(x)        % Sieve of Eratosthenes: returns all primes between 2 and x
        
    P = [0 2:x];             % Create vector with all ints between 2 and x where
                             %   position 1 is hard-coded as 0 since 1 is not a prime.

    for n = 2:sqrt(x)        % All primes factors lie between 2 and sqrt(x).
       if P(n)               % If the current value is not 0 (i.e. a prime),
          P(n*n:n:x) = 0;    % then replace all further multiples of it with 0.
       end
    end                      % At this point P is a vector with only primes and zeroes.

    P = P(P ~= 0);           % Remove all zeroes from P, leaving only the primes.
end
```

The optimization lies in fewer steps in the for loop, use of MATLAB's built-in array operations and no modulo calculation.

**Limitation:** your machine has to be able to allocate enough memory for an array of length x.

### A more efficient Sieve

A more efficient Sieve avoids creating a large double precision vector P, instead using a logical array (which consumes 1/8 the memory of a double array of the same size) and only converting to double those values corresponding to primes.

```mw
function P = sieveOfEratosthenes(x)
    ISP = [false true(1, x-1)]; % 1 is not prime, but we start off assuming all numbers between 2 and x are
    for n = 2:sqrt(x)
        if ISP(n)
            ISP(n*n:n:x) = false; % Multiples of n that are greater than n*n are not primes
        end
    end
    % The ISP vector that we have calculated is essentially the output of the ISPRIME function called on 1:x
    P = find(ISP); % Convert the ISPRIME output to the values of the primes by finding the locations 
                   % of the TRUE values in S.
end
```

You can compare the output of this function against the PRIMES function included in MATLAB, which performs a somewhat more memory-efficient Sieve (by not storing even numbers, at the expense of a more complicated indexing expression inside the IF statement.)


## Maxima

```mw
sieve(n):=block(
   [a:makelist(true,n),i:1,j],
   a[1]:false,
   do (
      i:i+1,
      unless a[i] do i:i+1,
      if i*i>n then return(sublist_indices(a,identity)),
      for j from i*i step i while j<=n do a[j]:false
   )
)$
```


## MAXScript

```
fn eratosthenes n =
(
    multiples = #()
    print 2
    for i in 3 to n do
    (
        if (findItem multiples i) == 0 then
        (
            print i
            for j in (i * i) to n by i do
            (
                append multiples j
            )
        )
    )
)

eratosthenes 100
```


## Mercury

```mw
:- module sieve.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
:- implementation.
:- import_module bool, array, int.

main(!IO) :-
    sieve(50, Sieve),
    dump_primes(2, size(Sieve), Sieve, !IO).

:- pred dump_primes(int, int, array(bool), io, io).
:- mode dump_primes(in, in, array_di, di, uo) is det.
dump_primes(N, Limit, !.A, !IO) :-
    ( if N < Limit then
        unsafe_lookup(!.A, N, Prime),
        (
            Prime = yes,
            io.write_line(N, !IO)
        ;
            Prime = no
        ),
        dump_primes(N + 1, Limit, !.A, !IO)
    else
        true
    ).

:- pred sieve(int, array(bool)).
:- mode sieve(in, array_uo) is det.
sieve(N, !:A) :-
    array.init(N, yes, !:A),
    sieve(2, N, !A).

:- pred sieve(int, int, array(bool), array(bool)).
:- mode sieve(in, in, array_di, array_uo) is det.
sieve(N, Limit, !A) :-
    ( if N < Limit then
        unsafe_lookup(!.A, N, Prime),
        (
            Prime = yes,
            sift(N + N, N, Limit, !A),
            sieve(N + 1, Limit, !A)
        ;
            Prime = no,
            sieve(N + 1, Limit, !A)
        )
    else
        true
    ).

:- pred sift(int, int, int, array(bool), array(bool)).
:- mode sift(in, in, in, array_di, array_uo) is det.
sift(I, N, Limit, !A) :-
    ( if I < Limit then
        unsafe_set(I, no, !A),
        sift(I + N, N, Limit, !A)
    else
        true
    ).
```


## Microsoft Small Basic

Translation of

:

GW-BASIC

```mw
TextWindow.Write("Enter number to search to: ")
limit = TextWindow.ReadNumber()
For n = 2 To limit 
  flags[n] = 0
EndFor
For n = 2 To math.SquareRoot(limit)
  If flags[n] = 0 Then
    For K = n * n To limit Step n
      flags[K] = 1
    EndFor
  EndIf
EndFor
' Display the primes
If limit >= 2 Then
  TextWindow.Write(2)
  For n = 3 To limit
    If flags[n] = 0 Then 
      TextWindow.Write(", " + n)
    EndIf  
  EndFor
  TextWindow.WriteLine("")
EndIf
```


## Modula-2

```mw
MODULE Erato;
FROM InOut IMPORT WriteCard, WriteLn;
FROM MathLib IMPORT sqrt;

CONST Max = 100; 

VAR prime: ARRAY [2..Max] OF BOOLEAN;
    i: CARDINAL;

PROCEDURE Sieve;
    VAR i, j, sqmax: CARDINAL;
BEGIN
    sqmax := TRUNC(sqrt(FLOAT(Max)));

    FOR i := 2 TO Max DO prime[i] := TRUE; END;
    FOR i := 2 TO sqmax DO
        IF prime[i] THEN
            j := i * 2;
            (* alas, the BY clause in a FOR loop must be a constant *)
            WHILE j <= Max DO 
                prime[j] := FALSE;
                j := j + i;
            END;
        END;
    END;
END Sieve;

BEGIN
    Sieve;
    FOR i := 2 TO Max DO
        IF prime[i] THEN
            WriteCard(i,5);
            WriteLn;
        END;
    END;
END Erato.
```

**Output:**

```
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


## Modula-3

### Regular version

This version runs slow because of the way I/O is implemented in the CM3 compiler. Setting `ListPrimes = FALSE` achieves speed comparable to C on sufficiently high values of `LastNum` (e.g., 10^6).

```mw
MODULE Eratosthenes EXPORTS Main;

IMPORT IO;

FROM Math IMPORT sqrt;

CONST
  LastNum    = 1000;
  ListPrimes = TRUE;

VAR
  a: ARRAY[2..LastNum] OF BOOLEAN;

VAR
  n := LastNum - 2 + 1;

BEGIN

  (* set up *)
  FOR i := FIRST(a) TO LAST(a) DO
    a[i] := TRUE;
  END;

  (* declare a variable local to a block *)
  VAR b := FLOOR(sqrt(FLOAT(LastNum, LONGREAL)));

  (* the block must follow immediately *)
  BEGIN

    (* print primes and mark out composites up to sqrt(LastNum) *)
    FOR i := FIRST(a) TO b DO
      IF a[i] THEN
        IF ListPrimes THEN IO.PutInt(i); IO.Put(" "); END;
        FOR j := i*i TO LAST(a) BY i DO
          IF a[j] THEN
            a[j] := FALSE;
            DEC(n);
          END;
        END;
      END;
    END;

    (* print remaining primes *)
    IF ListPrimes THEN
      FOR i := b + 1 TO LAST(a) DO
        IF a[i] THEN
          IO.PutInt(i); IO.Put(" ");
        END;
      END;
    END;

  END;

  (* report *)
  IO.Put("There are ");         IO.PutInt(n);
  IO.Put(" primes from 2 to "); IO.PutInt(LastNum);
  IO.PutChar('\n');

END Eratosthenes.
```

### Advanced version

This version uses more "advanced" types.

```mw
(* From the CM3 examples folder (comments removed). *)

MODULE Sieve EXPORTS Main;

IMPORT IO;

TYPE
  Number = [2..1000];
  Set = SET OF Number;

VAR
  prime: Set := Set {FIRST(Number) .. LAST(Number)};

BEGIN
  FOR i := FIRST(Number) TO LAST(Number) DO
    IF i IN prime THEN
      IO.PutInt(i);
      IO.Put(" ");

      FOR j := i TO LAST(Number) BY i DO
        prime := prime - Set{j};
      END;
    END;
  END;
  IO.Put("\n");
END Sieve.
```
