---
title: "Sieve of Eratosthenes (part 6/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/21
---

## EchoLisp

### Sieve

```mw
(require 'types) ;; bit-vector

;; converts sieve->list for integers in [nmin .. nmax[
(define (s-range sieve nmin nmax (base 0))
   (for/list ([ i (in-range nmin nmax)]) #:when (bit-vector-ref sieve i) (+ i base)))
   
;; next prime in sieve > p, or #f
(define (s-next-prime sieve p ) ;; 
      (bit-vector-scan-1 sieve (1+ p)))
      

;; returns a bit-vector - sieve- all numbers in [0..n[
(define (eratosthenes n)
  (define primes (make-bit-vector-1 n ))
  (bit-vector-set! primes 0 #f)
  (bit-vector-set! primes 1 #f)
  (for ([p (1+ (sqrt n))])
       #:when (bit-vector-ref primes  p)
         (for ([j (in-range (* p p) n p)])
    (bit-vector-set! primes j #f)))
   primes) 
  
(define s-primes (eratosthenes 10_000_000))

(s-range s-primes 0 100)
   → (2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
(s-range s-primes 1_000_000 1_000_100)
   → (1000003 1000033 1000037 1000039 1000081 1000099)
(s-next-prime s-primes 9_000_000)
   → 9000011
```

### Segmented sieve

Allow to extend the basis sieve (n) up to n^2. Memory requirement is O(√n)

```mw
;; ref :  http://research.cs.wisc.edu/techreports/1990/TR909.pdf
;; delta multiple of  sqrt(n)
;; segment is [left .. left+delta-1]

(define (segmented sieve left delta  (p 2) (first 0))
   (define segment (make-bit-vector-1 delta))
   (define right (+ left (1- delta)))
    (define pmax (sqrt right))
     (while p
     #:break (> p pmax)
    (set! first (+ left (modulo (- p (modulo left p)) p )))
         
   (for   [(q (in-range first (1+ right) p))]
   (bit-vector-set! segment (- q left) #f))  
        (set! p (bit-vector-scan-1 sieve (1+ p))))
   segment)

(define (seg-range nmin delta)
    (s-range (segmented s-primes nmin delta) 0 delta nmin))

(seg-range 10_000_000_000 1000) ;; 15 milli-sec

    → (10000000019 10000000033 10000000061 10000000069 10000000097 10000000103 10000000121 
       10000000141 10000000147 10000000207 10000000259 10000000277 10000000279 10000000319 
       10000000343 10000000391 10000000403 10000000469 10000000501 10000000537 10000000583 
       10000000589 10000000597 10000000601 10000000631 10000000643 10000000649 10000000667 
       10000000679 10000000711 10000000723 10000000741 10000000753 10000000793 10000000799 
       10000000807 10000000877 10000000883 10000000889 10000000949 10000000963 10000000991 
       10000000993 10000000999)

;; 8 msec using the native (prime?) function
(for/list ((p (in-range 1_000_000_000 1_000_001_000))) #:when (prime? p) p)
```

### Wheel

A 2x3 wheel gives a 50% performance gain.

```mw
;; 2x3 wheel
(define (weratosthenes n)
  (define primes (make-bit-vector n )) ;; everybody to #f (false)
  (bit-vector-set! primes 2 #t)
  (bit-vector-set! primes 3 #t)
  (bit-vector-set! primes 5 #t)
  
  (for ([i  (in-range 6 n 6) ]) ;; set candidate primes
      (bit-vector-set! primes (1+ i) #t)
      (bit-vector-set! primes (+ i 5) #t)
      )
      
  (for ([p  (in-range 5 (1+ (sqrt n)) 2 ) ])
       #:when (bit-vector-ref primes  p)
         (for ([j (in-range (* p p) n p)])
    (bit-vector-set! primes j #f)))
   primes)
```


## EDSAC order code

This sieve program is based on one by Eiiti Wada, which on 2020-07-05 could be found at https://www.dcs.warwick.ac.uk/~edsac/

The main external change is that the program is not designed to be viewed in the monitor; it just writes as many primes as possible within the limitations imposed by Rosetta Code. Apart from the addition of comments, internal changes include the elimination of one set of masks, and a revised method of switching from one mask to another.

On the EdsacPC simulator (see link above) the printout starts off very slowly, and gradually gets faster.

```mw
 [Sieve of Eratosthenes]
 [EDSAC program. Initial Orders 2]

[Memory usage:
   56..87   library subroutine P6, for printing
   88..222  main program
  224..293  mask table: 35 long masks; each has 34 1's and a single 0
  294..1023 array of bits for integers 2, 3, 4, ...,
            where bit is changed from 1 to 0 when integer is crossed out.
  The address of the mask table must be even, and clear of the main program.
  To change it, just change the value after "T47K" below.
  The address of the bit array will then be changed automatically.]
 
[Subroutine M3, prints header, terminated by blank row of tape.
 It's an "interlude", which runs and then gets overwritten.]
      PFGKIFAFRDLFUFOFE@A6FG@E8FEZPF
      @&*SIEVE!OF!ERATOSTHENES!#2020
      @&*BASED!ON!CODE!BY!EIITI!WADA!#2001
      ..PZ

[Subroutine P6, prints strictly positive integer.
 32 locations; working locations 1, 4, 5.]
        T  56 K
  GKA3FT25@H29@VFT4DA3@TFH30@S6@T1FV4DU4DAFG26@TFTF
  O5FA4DF4FS4FL4FT4DA1FS3@G9@EFSFO31@E20@J995FJF!F

  [Store address of mask table in (say) location 47
  (chosen because its code letter M is first letter of "Mask").
  Address must be even and clear of main program.]
        T  47 K
        P 224 F  [<-------- address of mask table]

[Main program]
        T  88 K  [Define load address for main program.
                 Must be even, because of long values at start.]
        G     K [set @ (theta) for relative addressing]

[Long constants]
        T#Z PF TZ [clears sandwich digit between 0 and 1]
    [0] PD PF     [long value 1; also low word = short 1]
        T2#Z PF T2Z [clears sandwich digit between 2 and 3]
    [2] PF K4096F [long value 1000...000 binary;
                   also high word = teleprinter null]

 [Short constants
  The address in the following C order is the (exclusive) end of the bit table.
  Must be even: max = 1024, min = M + 72 where M is address of mask table set up above.
  Usually 1024, but may be reduced, e.g. to make the program run faster.]
    [4] C1024 D [or e.g. C 326 D to make it much faster]
    [5] U     F ['U' = 'T' - 'C']
    [6] K     F ['K' = 'S' - 'C']
    [7] H    #M [H order for start of mask table]
    [8] H  70#M [used to test for end of mask table]
    [9] P   2 F [constant4, or 2 in address field]
   [10] P  70 F [constant 140, or 70 in address field]
   [11] @     F [carriage return]
   [12] &     F [line feed]

 [Short variables]
   [13] P   1 F [p = number under test
                Let p = 35*q + r, where 0 <= r < 35]
   [14] P     F [4*q]
   [15] P   4 F [4*r]

 [Initial values of orders; required only for optional code below.]
   [16] C  70#M [initial value of a variable C order]
   [17] T    #M [initial value of a variable T order]
   [18] T  70#M [initial value of a variable T order]

   [19]
   [Enter with acc = 0]

  [Optional code to do some initializing at run time.
   This code allows the program to run again without being loaded again.]
         A  7 @ [initial values of variable orders]
         T 65 @
         A 16 @
         T 66 @
         A 17 @
         T 44 @
         A 18 @
         T 52 @

  [Initialize variables]
         A    @ [load 1 (short)]
         L    D [shift left 1]
         U 13 @ [p := 2]
         L  1 F [shift left 2]
         T 15 @ [4*r :=  8]
         T 14 @ [4*q :=  0]
  [End of optional code]

 [Make table of 35 masks 111...110,  111...101, ...,  011...111
  Treat the mask 011...111 separately to avoid accumulator overflow.
  Assume acc = 0 here.]
        S    #@ [acc all 1's]
        S  2 #@ [acc := 0111...111]
   [35] T 68 #M [store at high end of mask table]
        S    #@ [acc := -1]        
        L     D [make mask 111...1110]
        G 43  @ [jump to store it
 [Loop shifting the mask right and storing the result in the mask table.
  Uses first entry of bit array as temporary store.]
   [39] T     F [clear acc]
        A 70 #M [load previous mask]
        L     D [shift left]
        A    #@ [add 1]
   [43] U 70 #M [update current mask]
   [44] T    #M [store it in table (order changed at run time)]
        A 44  @ [load preceding T order]
        A  9  @ [inc address by 2]
        U 44  @ [store back]
        S 35  @ [reached high entry yet?]
        G 39  @ [loop back if not]
 [Mask table is now complete]

 [Initialize bit array: no numbers crossed out, so all bits are 1]
   [50] T     F [clear acc]
        S     #@ [subtract long 1, make top 35 bits all 1's]
   [52] T 70 #M [store as long value, both words all 1's  (order changed at run time)]
        A  52 @ [load preceding order]
        A   9 @ [add 2 to address field]
        U  52 @ [and store back]
        S   5 @ [convert to C order with same address (*)]
        S   4 @ [test for end of bit array]
        G  50 @ [loop until stored all 1's in bit table]
 [(*) Done so that end of bit table can be stored at one place only
      in list of constants, i.e. 'C m D' only, not 'T m D' as well.]

 [Start of main loop.]
 [Testing whether number has been crossed out]
   [59] T     F [acc := 0]
        A  66 @ [deriving S order from C order]
        A   6 @
        T  64 @
        S    #@ [acc := -1]
   [64] S     F [acc := 1's complement of bit-table entry (order changed at run time)]
   [65] H    #M [mult reg := start of mask array (order changed at run time)]
   [66] C  70#M [acc := -1 iff p (current number) is crossed out (order changed at run time)]
 [The next order is to avoid accumulator overflow if acc = max positive number]
        E  70 @ [if acc >= 0, jump to process new prime]
       A     #@ [if acc < 0, add 1 to test for -1]
       E 106  @ [if acc now >= 0 number is crossed out, jump to test next]
 [Here if new prime found.
  Send it to the teleprinter]
   [70] O  11 @ [print CR]
        O  12 @ [print LF]
        T     F [clear acc]
        A  13 @ [load prime]
        T     F [store in C(0) for print routine]
        A  75 @ [for subroutine return]
        G 56  F [print prime]

 [Cross out its multiples by setting corresponding bits to 0]
        A  65 @ [load H order above]
        T 102 @ [plant in crossing-out loop]
        A  66 @ [load C order above]
        T1 03 @ [plant in crossing-out loop]

 [Start of crossing-out loop. Here acc must = 0]
   [81] A 102 @ [load H order below]
        A  15 @ [inc address field by 2*r, where p = 35q + r]
        U 102 @ [update H order]
        S   8 @ [compare with 'H 70 #M']
        G  93 @ [skip if not gone beyond end of mask table]
        T     F [wrap mask address and inc address in bit tsble]
        A 102 @ [load H order below]
        S  10 @ [reduce mask address by 70]
        T 102 @ [update H order]
        A 103 @ [load C order below]
        A   9 @ [add 2 to address]
        T 103 @ [update C order]
   [93] T     F [clear acc]
        A 103 @ [load C order below]
        A  14 @ [inc address field by 2*q, where p = 35q + r]
        U 103 @ [update C order]
        S   4 @ [test for end of bit array]
        E 106 @ [if finished crossing out, loop to test next number]
        A  4  @ [restore C order]
        A  5  @ [make T order with same address]
        T 104 @ [store below]

 [Execute the crossing-out orders created above]
  [102] X     F [mult reg := mask (order created at run time)]
  [103] X     F [acc := logical and with bit-table entry (order created at run time)]
  [104] X     F [update entry (order created at run time)]
        E  81 @ [loop back with acc = 0]

  [106] T     F [clear acc]
        A  13 @ [load p = number under test]
        A     @ [add 1 (single)]
        T  13 @ [update]
        A  15 @ [load 4*r, where p = 35q + r]
        A   9 @ [add 4]
        U  15 @ [store back (r inc'd by 1)]
        S  10 @ [is 4*r now >= 140?]
        G 119 @ [no, skip]
        T  15 @ [yes, reduce 4*r by 140]
        A  14 @ [load 4*q]
        A   9 @ [add 4]
        T  14 @ [store back (q inc'd by 1)]
  [119] T     F [clear acc]
        A  65 @ [load 'H ... D' order, which refers to a mask]
        A   9 @ [inc mask address by 2]
        U  65 @ [update order]
        S   8 @ [over end of mask table?]
        G  59 @ [no, skip wrapround code]
        A   7 @ [yes, add constant to wrap round]
        T  65 @ [update H order]
        A  66 @ 
        A   9 @ [inc address by 2]
        U  66 @ [and store back]
        S   4 @ [test for end, as defined by C order at start]
        G  59 @ [loop back if not at end]

[Finished whole thing]
  [132] O   3 @ [output null to flush teleprinter buffer]
        Z     F [stop]
        E  19 Z [address to start execution]
        P     F [acc = 0 at start]
```

**Output:**

```
SIEVE OF ERATOSTHENES 2020
BASED ON CODE BY EIITI WADA 2001
    2
    3
    5
    7
   11
   13
   17
[...]
12703
12713
12721
12739
12743
12757
12763
```


## Eiffel

Works with

:

EiffelStudio

version 6.6 beta (with provisional loop syntax)

```mw
class
    APPLICATION
 
create
    make
 
feature
       make
            -- Run application.
        do
            across primes_through (100) as ic loop print (ic.item.out + " ") end
        end
 
    primes_through (a_limit: INTEGER): LINKED_LIST [INTEGER]
            -- Prime numbers through `a_limit'
        require
            valid_upper_limit: a_limit >= 2
        local
            l_tab: ARRAY [BOOLEAN]
        do
            create Result.make
            create l_tab.make_filled (True, 2, a_limit)
            across
                l_tab as ic
            loop
                if ic.item then
                    Result.extend (ic.target_index)
                    across ((ic.target_index * ic.target_index) |..| l_tab.upper).new_cursor.with_step (ic.target_index) as id
                    loop
                        l_tab [id.item] := False
                    end
                end
            end
        end
end
```

Output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Elixir

```mw
defmodule Prime do
  def eratosthenes(limit \\ 1000) do
    sieve = [false, false | Enum.to_list(2..limit)] |> List.to_tuple
    check_list = [2 | Stream.iterate(3, &(&1+2)) |> Enum.take(round(:math.sqrt(limit)/2))]
    Enum.reduce(check_list, sieve, fn i,tuple ->
      if elem(tuple,i) do
        clear_num = Stream.iterate(i*i, &(&1+i)) |> Enum.take_while(fn x -> x <= limit end)
        clear(tuple, clear_num)
      else
        tuple
      end
    end)
  end
  
  defp clear(sieve, list) do
    Enum.reduce(list, sieve, fn i, acc -> put_elem(acc, i, false) end)
  end
end

limit = 199
sieve = Prime.eratosthenes(limit)
Enum.each(0..limit, fn n ->
  if x=elem(sieve, n), do: :io.format("~3w", [x]), else: :io.format("  .") 
  if rem(n+1, 20)==0, do: IO.puts ""
end)
```

**Output:**

```
  .  .  2  3  .  5  .  7  .  .  . 11  . 13  .  .  . 17  . 19
  .  .  . 23  .  .  .  .  . 29  . 31  .  .  .  .  . 37  .  .
  . 41  . 43  .  .  . 47  .  .  .  .  . 53  .  .  .  .  . 59
  . 61  .  .  .  .  . 67  .  .  . 71  . 73  .  .  .  .  . 79
  .  .  . 83  .  .  .  .  . 89  .  .  .  .  .  .  . 97  .  .
  .101  .103  .  .  .107  .109  .  .  .113  .  .  .  .  .  .
  .  .  .  .  .  .  .127  .  .  .131  .  .  .  .  .137  .139
  .  .  .  .  .  .  .  .  .149  .151  .  .  .  .  .157  .  .
  .  .  .163  .  .  .167  .  .  .  .  .173  .  .  .  .  .179
  .181  .  .  .  .  .  .  .  .  .191  .193  .  .  .197  .199
```

Shorter version (but slow):

```mw
defmodule Sieve do
  def primes_to(limit), do: sieve(Enum.to_list(2..limit))

  defp sieve([h|t]), do: [h|sieve(t -- for n <- 1..length(t), do: h*n)]
  defp sieve([]), do: []
end
```

**Alternate much faster odds-only version more suitable for immutable data structures using a (hash) Map**

The above code has a very limited useful range due to being very slow: for example, to sieve to a million, even changing the algorithm to odds-only, requires over 800 thousand "copy-on-update" operations of the entire saved immutable tuple ("array") of 500 thousand bytes in size, making it very much a "toy" application. The following code overcomes that problem by using a (immutable/hashed) Map to store the record of the current state of the composite number chains resulting from each of the secondary streams of base primes, which are only 167 in number up to this range; it is a functional "incremental" Sieve of Eratosthenes implementation:

```mw
defmodule PrimesSoEMap do
  @typep stt :: {integer, integer, integer, Enumerable.integer, %{integer => integer}}

  @spec advance(stt) :: stt
  defp advance {n, bp, q, bps?, map} do
    bps = if bps? === nil do Stream.drop(oddprms(), 1) else bps? end
    nn = n + 2
    if nn >= q do
      inc = bp + bp
      nbps = bps |> Stream.drop(1)
      [nbp] = nbps |> Enum.take(1)
      advance {nn, nbp, nbp * nbp, nbps, map |> Map.put(nn + inc, inc)}
    else if Map.has_key?(map, nn) do
      {inc, rmap} = Map.pop(map, nn)
      [next] =
        Stream.iterate(nn + inc, &(&1 + inc))
          |> Stream.drop_while(&(Map.has_key?(rmap, &1))) |> Enum.take(1)
      advance {nn, bp, q, bps, Map.put(rmap, next, inc)}
    else
      {nn, bp, q, bps, map}
    end end
  end

  @spec oddprms() :: Enumerable.integer
  defp oddprms do # put first base prime cull seq in Map so never empty
    # advance base odd primes to 5 when initialized
    init = {7, 5, 25, nil, %{9 => 6}}
    [3, 5] # to avoid race, preseed with the first 2 elements...
      |> Stream.concat(
            Stream.iterate(init, &(advance &1))
              |> Stream.map(fn {p,_,_,_,_} -> p end))
  end

  @spec primes() :: Enumerable.integer
  def primes do
    Stream.concat([2], oddprms())
  end

end

range = 1000000
IO.write "The first 25 primes are:\n( "
PrimesSoEMap.primes() |> Stream.take(25) |> Enum.each(&(IO.write "#{&1} "))
IO.puts ")"
testfunc =
  fn () ->
    ans =
      PrimesSoEMap.primes() |> Stream.take_while(&(&1 <= range)) |> Enum.count()
    ans end
:timer.tc(testfunc)
  |> (fn {t,ans} ->
    IO.puts "There are #{ans} primes up to #{range}."
    IO.puts "This test bench took #{t} microseconds." end).()
```

**Output:**

```
The first 25 primes are:
( 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 )
There are 78498 primes up to 1000000.
This test bench took 3811957 microseconds.
```

The output time of about 3.81 seconds to one million is on a 1.92 Gigahertz CPU meaning that it takes about 93 thousand CPU clock cycles per prime which is still quite slow compared to mutable data structure implementations but comparable to "functional" implementations in other languages and is slow due to the time to calculate the required hashes. One advantage that it has is that it is O(n log (log n)) asymptotic computational complexity meaning that it takes not much more than ten times as long to sieve a range ten times higher.

This algorithm could be easily changed to use a Priority Queue (preferably Min-Heap based for the least constant factor computational overhead) to save some of the computation time, but then it will have the same computational complexity as the following code and likely about the same execution time.

**Alternate faster odds-only version more suitable for immutable data structures using lazy Streams of Co-Inductive Streams**

In order to save the computation time of computing the hashes, the following version uses a deferred execution Co-Inductive Stream type (constructed using Tuple's) in an infinite tree folding structure (by the `pairs` function):

```mw
defmodule PrimesSoETreeFolding do
  @typep cis :: {integer, (() -> cis)}
  @typep ciss :: {cis, (() -> ciss)}

  @spec merge(cis, cis) :: cis
  defp merge(xs, ys) do
    {x, restxs} = xs; {y, restys} = ys
    cond do
      x < y -> {x, fn () -> merge(restxs.(), ys) end}
      y < x -> {y, fn () -> merge(xs, restys.()) end}
      true -> {x, fn () -> merge(restxs.(), restys.()) end}
    end
  end

  @spec smlt(integer, integer) :: cis
  defp smlt(c, inc) do
    {c, fn () -> smlt(c + inc, inc) end}
  end

  @spec smult(integer) :: cis
  defp smult(p) do
    smlt(p * p, p + p)
  end
P
  @spec allmults(cis) :: ciss
  defp allmults {p, restps} do
    {smult(p), fn () -> allmults(restps.()) end}
  end

  @spec pairs(ciss) :: ciss
  defp pairs {cs0, restcss0} do
    {cs1, restcss1} = restcss0.()
    {merge(cs0, cs1), fn () -> pairs(restcss1.()) end}
  end

  @spec cmpsts(ciss) :: cis
  defp cmpsts {cs, restcss} do
    {c, restcs} = cs
    {c, fn () -> merge(restcs.(), cmpsts(pairs(restcss.()))) end}
  end

  @spec minusat(integer, cis) :: cis
  defp minusat(n, cmps) do
    {c, restcs} = cmps
    if n < c do
      {n, fn () -> minusat(n + 2, cmps) end}
    else
      minusat(n + 2, restcs.())
    end
  end

  @spec oddprms() :: cis
  defp oddprms() do
    {3, fn () ->
      {5, fn () -> minusat(7, cmpsts(allmults(oddprms()))) end}
    end}
  end

  @spec primes() :: Enumerable.t
  def primes do
    [2] |> Stream.concat(
      Stream.iterate(oddprms(), fn {_, restps} -> restps.() end)
        |> Stream.map(fn {p, _} -> p end)
    )
  end

end

range = 1000000
IO.write "The first 25 primes are:\n( "
PrimesSoETreeFolding.primes() |> Stream.take(25) |> Enum.each(&(IO.write "#{&1} "))
IO.puts ")"
testfunc =
  fn () ->
    ans =
      PrimesSoETreeFolding.primes() |> Stream.take_while(&(&1 <= range)) |> Enum.count()
    ans end
:timer.tc(testfunc)
  |> (fn {t,ans} ->
    IO.puts "There are #{ans} primes up to #{range}."
    IO.puts "This test bench took #{t} microseconds." end).()
```

It's output is identical to the previous version other than the time required is less than half; however, it has a O(n (log n) (log (log n))) asymptotic computation complexity meaning that it gets slower with range faster than the above version. That said, it would take sieving to billions taking hours before the two would take about the same time.


## Elm

### Elm with immutable arrays

```mw
module PrimeArray exposing (main)

import Array exposing (Array, foldr, map, set)
import Html exposing (div, h1, p, text)
import Html.Attributes exposing (style)

{-
The Eratosthenes sieve task in Rosetta Code does not accept the use of modulo function  (allthough Elm functions modBy and remainderBy work always correctly as they require type Int excluding type Float). Thus the solution needs an indexed work array as Elm has no indexes for lists.

In this method we need no division remainder calculations, as we just set the markings of non-primes into the array. We need the indexes that we know, where the marking of the non-primes shall be set.

Because everything is immutable in Elm, every change of array values will create a new array save the original array unchanged. That makes the program running slower or consuming more space of memory than with non-functional imperative languages. All conventional loops (for, while, until) are excluded in Elm because immutability requirement.

   Live: https://ellie-app.com/pTHJyqXcHtpa1
-}

alist =
    List.range 2 150

-- Work array contains integers 2 ... 149

workArray =
    Array.fromList alist

n : Int
n =
    List.length alist

-- The max index of integers used in search for primes
-- limit * limit < n
-- equal: limit <= √n

limit : Int
limit =
    round (0.5 + sqrt (toFloat n))
 

-- Remove zero cells of the array

findZero : Int -> Bool
findZero =
    \el -> el > 0

zeroFree : Array Int
zeroFree =
    Array.filter findZero workResult

nrFoundPrimes =
    Array.length zeroFree

workResult : Array Int
workResult =
    loopI 2 limit workArray

{- As Elm has no loops (for, while, until)
we must use recursion instead!
The search of prime starts allways saving the 
first found value (not setting zero) and continues setting the multiples of prime to zero.
Zero is no integer and may thus be used as marking of non-prime numbers. At the end, only the primes remain in the array and the zeroes are removed from the resulted array to be shown in Html. 
-}

-- The recursion increasing variable i follows:

loopI : Int -> Int -> Array Int -> Array Int
loopI i imax arr =
    if i > imax then
        arr

    else
        let
            arr2 =
                phase i arr
        in
        loopI (i + 1) imax arr2

-- The helper function

phase : Int -> Array Int -> Array Int
phase i =
    arrayMarker i (2 * i - 2) n

lastPrime =
    Maybe.withDefault 0 <| Array.get (nrFoundPrimes - 1) zeroFree

outputArrayInt : Array Int -> String
outputArrayInt arr =
    decorateString <|
        foldr (++) "" <|
            Array.map (\x -> String.fromInt x ++ " ") arr

decorateString : String -> String
decorateString str =
    "[ " ++ str ++ "]"

-- Recursively marking the multiples of p with zero
-- This loop operates with constant p

arrayMarker : Int -> Int -> Int -> Array Int -> Array Int
arrayMarker p min max arr =
    let
        arr2 =
            set min 0 arr

        min2 =
            min + p
    in
    if min < max then
        arrayMarker p min2 max arr2

    else
        arr

main =
    div [ style "margin" "2%" ]
        [ h1 [] [ text "Sieve of Eratosthenes" ]
        , text ("List of integers [2, ... ," ++ String.fromInt n ++ "]")
        , p [] [ text ("Total integers " ++ String.fromInt n) ]
        , p [] [ text ("Max prime of search " ++ String.fromInt limit) ]
        , p [] [ text ("The largest found prime " ++ String.fromInt lastPrime) ]
        , p [ style "color" "blue", style "font-size" "1.5em" ]
            [ text (outputArrayInt zeroFree) ]
        , p [] [ text ("Found " ++ String.fromInt nrFoundPrimes ++ " primes") ]
        ]
```

**Output:**

```
List of integers [2, ... ,149]

Total integers 149

Max prime of search 13

The largest found prime 149

[ 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 ]

Found 35 primes 
```

### Concise Elm Immutable Array Version

Although functional, the above code is written in quite an imperative style, so the following code is written in a more concise functional style and includes timing information for counting the number of primes to a million:

```mw
module Main exposing (main)

import Browser exposing (element)
import Task exposing (Task, succeed, perform, andThen)
import Html exposing (Html, div, text)
import Time exposing (now, posixToMillis)

import Array exposing (repeat, get, set)

cLIMIT : Int
cLIMIT = 1000000

primesArray : Int -> List Int
primesArray n =
  if n < 2 then [] else
  let
    sz = n + 1
    loopbp bp arr =
      let s = bp * bp in
      if s >= sz then arr else
      let tst = get bp arr |> Maybe.withDefault True in
      if tst then loopbp (bp + 1) arr else
      let
        cullc c iarr =
          if c >= sz then iarr else
          cullc (c + bp) (set c True iarr)
      in loopbp (bp + 1) (cullc s arr)
    cmpsts = loopbp 2 (repeat sz False)
    cnvt (i, t) = if t then Nothing else Just i
  in cmpsts |> Array.toIndexedList
      |> List.drop 2 -- skip the values for zero and one
      |> List.filterMap cnvt -- primes are indexes of not composites

type alias Model = List String

type alias Msg = Model

test : (Int -> List Int) -> Int -> Cmd Msg
test primesf lmt =
  let
    to100 = primesf 100 |> List.map String.fromInt |> String.join ", "
    to100str = "The primes to 100 are:  " ++ to100
    timemillis() = now |> andThen (succeed << posixToMillis)
  in timemillis() |> andThen (\ strt ->
       let cnt = primesf lmt |> List.length
       in timemillis() |> andThen (\ stop ->
         let answrstr = "Found " ++ (String.fromInt cnt) ++ " primes to "
                          ++ (String.fromInt cLIMIT) ++ " in "
                          ++ (String.fromInt (stop - strt)) ++ " milliseconds."
         in succeed [to100str, answrstr] ) ) |> perform identity

main : Program () Model Msg
main =
  element { init = \ _ -> ( [], test primesArray cLIMIT )
          , update = \ msg _ -> (msg, Cmd.none)
          , subscriptions = \ _ -> Sub.none
          , view = div [] << List.map (div [] << List.singleton << text) }
```

**Output:**

```
The primes up to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
Found 78498 primes to 1000000 in 958 milliseconds.
```

The above output is the contents of the HTML web page as shown with Google Chrome version 1.23 running on an AMD 7840HS CPU at 5.1 GHz (single thread boosted).

### Concise Elm Immutable Array Odds-Only Version

The following code can replace the `primesArray` function in the above program and called from the testing and display code (two places):

```mw
primesArrayOdds : Int -> List Int
primesArrayOdds n =
  if n < 2 then [] else
  let
    sz = (n - 1) // 2
    loopi i arr =
      let s = (i + i) * (i + 3) + 3 in
      if s >= sz then arr else
      let tst = get i arr |> Maybe.withDefault True in
      if tst then loopi (i + 1) arr else
      let
        bp = i + i + 3
        cullc c iarr =
          if c >= sz then iarr else
          cullc (c + bp) (set c True iarr)
      in loopi (i + 1) (cullc s arr)
    cmpsts = loopi 0 (repeat sz False)
    cnvt (i, t) = if t then Nothing else Just <| i + i + 3
    oddprms = cmpsts |> Array.toIndexedList |> List.filterMap cnvt
  in 2 :: oddprms
```

**Output:**

```
The primes up to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
Found 78498 primes to 1000000 in 371 milliseconds.
```

The above output is the contents of the HTML web page as shown with Google Chrome version 1.23 running on an AMD 7840HS CPU at 5.1 GHz (single thread boosted).

### Richard Bird Tree Folding Elm Version

The Elm language doesn't efficiently handle the Sieve of Eratosthenes (SoE) algorithm because it doesn't have directly accessible linear arrays (the Array module used above is based on a persistent tree of sub arrays) and also does Copy On Write (COW) for every write to every location as well as a logarithmic process of updating as a "tree" to minimize the COW operations. Thus, there is better performance implementing the Richard Bird Tree Folding functional algorithm, as follows:

Translation of

:

Haskell

```mw
module Main exposing (main)

import Browser exposing (element)
import Task exposing (Task, succeed, perform, andThen)
import Html exposing (Html, div, text)
import Time exposing (now, posixToMillis)

cLIMIT : Int
cLIMIT = 1000000

type CIS a = CIS a (() -> CIS a)

uptoCIS2List : comparable -> CIS comparable -> List comparable
uptoCIS2List n cis =
  let loop (CIS hd tl) lst =
        if hd > n then List.reverse lst
        else loop (tl()) (hd :: lst)
  in loop cis []

countCISTo : comparable -> CIS comparable -> Int
countCISTo n cis =
  let loop (CIS hd tl) cnt =
        if hd > n then cnt else loop (tl()) (cnt + 1)
  in loop cis 0

primesTreeFolding : () -> CIS Int
primesTreeFolding() =
  let
    merge (CIS x xtl as xs) (CIS y ytl as ys) =
      case compare x y of
        LT -> CIS x <| \ () -> merge (xtl()) ys
        EQ -> CIS x <| \ () -> merge (xtl()) (ytl())
        GT -> CIS y <| \ () -> merge xs (ytl())
    pmult bp =
      let adv = bp + bp
          pmlt p = CIS p <| \ () -> pmlt (p + adv)
      in pmlt (bp * bp)
    allmlts (CIS bp bptl) =
      CIS (pmult bp) <| \ () -> allmlts (bptl())
    pairs (CIS frst tls) =
      let (CIS scnd tlss) = tls()
      in CIS (merge frst scnd) <| \ () -> pairs (tlss())
    cmpsts (CIS (CIS hd tl) tls) =
      CIS hd <| \ () -> merge (tl()) <| cmpsts <| pairs (tls())
    testprm n (CIS hd tl as cs) =
      if n < hd then CIS n <| \ () -> testprm (n + 2) cs
      else testprm (n + 2) (tl())
    oddprms() =
      CIS 3 <| \ () -> testprm 5 <| cmpsts <| allmlts <| oddprms()
  in CIS 2 <| \ () -> oddprms()

type alias Model = List String

type alias Msg = Model

test : (() -> CIS Int) -> Int -> Cmd Msg
test primesf lmt =
  let
    to100 = primesf() |> uptoCIS2List 100
              |> List.map String.fromInt |> String.join ", "
    to100str = "The primes to 100 are:  " ++ to100
    timemillis() = now |> andThen (succeed << posixToMillis)
  in timemillis() |> andThen (\ strt ->
       let cnt = primesf() |> countCISTo lmt
       in timemillis() |> andThen (\ stop ->
         let answrstr = "Found " ++ (String.fromInt cnt) ++ " primes to "
                          ++ (String.fromInt cLIMIT) ++ " in "
                          ++ (String.fromInt (stop - strt)) ++ " milliseconds."
         in succeed [to100str, answrstr] ) ) |> perform identity

main : Program () Model Msg
main =
  element { init = \ _ -> ( [], test primesTreeFolding cLIMIT )
          , update = \ msg _ -> (msg, Cmd.none)
          , subscriptions = \ _ -> Sub.none
          , view = div [] << List.map (div [] << List.singleton << text) }
```

**Output:**

```
The primes up to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
Found 78498 primes to 1000000 in 201 milliseconds.
```

The above output is the contents of the HTML web page as shown with Google Chrome version 1.23 running on an AMD 7840HS CPU at 5.1 GHz (single thread boosted).

### Elm Priority Queue Version

Using a Binary Minimum Heap Priority Queue is a constant factor faster than the above code as the data structure is balanced rather than "heavy to the right" and requires less memory allocations/deallocation in the following code, which implements enough of the Priority Queue for the purpose. Just substitute the following code for `primesTreeFolding` and pass `primesPQ` as an argument to `test` rather than `primesTreeFolding`:

```mw
type PriorityQ comparable v =
  Mt
  | Br comparable v (PriorityQ comparable v)
                    (PriorityQ comparable v)

emptyPQ : PriorityQ comparable v
emptyPQ = Mt

peekMinPQ : PriorityQ comparable v -> Maybe (comparable, v)
peekMinPQ  pq = case pq of
                  (Br k v _ _) -> Just (k, v)
                  Mt -> Nothing

pushPQ : comparable -> v -> PriorityQ comparable v
           -> PriorityQ comparable v
pushPQ wk wv pq =
  case pq of
    Mt -> Br wk wv Mt Mt
    (Br vk vv pl pr) -> 
      if wk <= vk then Br wk wv (pushPQ vk vv pr) pl
      else Br vk vv (pushPQ wk wv pr) pl

siftdown : comparable -> v -> PriorityQ comparable v
             -> PriorityQ comparable v -> PriorityQ comparable v
siftdown wk wv pql pqr =
  case pql of
    Mt -> Br wk wv Mt Mt
    (Br vkl vvl pll prl) ->
      case pqr of
        Mt -> if wk <= vkl then Br wk wv pql Mt
              else Br vkl vvl (Br wk wv Mt Mt) Mt
        (Br vkr vvr plr prr) ->
          if wk <= vkl && wk <= vkr then Br wk wv pql pqr
          else if vkl <= vkr then Br vkl vvl (siftdown wk wv pll prl) pqr
               else Br vkr vvr pql (siftdown wk wv plr prr)

replaceMinPQ : comparable -> v -> PriorityQ comparable v
                 -> PriorityQ comparable v
replaceMinPQ wk wv pq = case pq of
                          Mt -> Mt
                          (Br _ _ pl pr) -> siftdown wk wv pl pr

primesPQ : () -> CIS Int
primesPQ() =
  let    
    sieve n pq q (CIS bp bptl as bps) =
      if n >= q then
        let adv = bp + bp in let (CIS nbp _ as nbps) = bptl()
        in sieve (n + 2) (pushPQ (q + adv) adv pq) (nbp * nbp) nbps
      else let
             (nxtc, _) = peekMinPQ pq |> Maybe.withDefault (q, 0) -- default when empty
             adjust tpq =
               let (c, adv) = peekMinPQ tpq |> Maybe.withDefault (0, 0)
               in if c > n then tpq
                  else adjust (replaceMinPQ (c + adv) adv tpq)
           in if n >= nxtc then sieve (n + 2) (adjust pq) q bps
              else CIS n <| \ () -> sieve (n + 2) pq q bps
    oddprms() = CIS 3 <| \ () -> sieve 5 emptyPQ 9 <| oddprms()
  in CIS 2 <| \ () -> oddprms()
```

**Output:**

```
The primes up to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
Found 78498 primes to 1000000 in 124 milliseconds.
```

The above output is the contents of the HTML web page as shown with Google Chrome version 1.23 running on an AMD 7840HS CPU at 5.1 GHz (single thread boosted).


## Emacs Lisp

Library:

cl-lib

```mw
(defun sieve-set (limit)
  (let ((xs (make-vector (1+ limit) 0)))
    (cl-loop for i from 2 to limit
             when (zerop (aref xs i))
             collect i
             and do (cl-loop for m from (* i i) to limit by i
                             do (aset xs m 1)))))
```

Straightforward implementation of sieve of Eratosthenes, 2 times faster:

```mw
(defun sieve (limit)
  (let ((xs (vconcat [0 0] (number-sequence 2 limit))))
    (cl-loop for i from 2 to (sqrt limit)
             when (aref xs i)
             do (cl-loop for m from (* i i) to limit by i
                         do (aset xs m 0)))
    (remove 0 xs)))
```


## Erlang

### Erlang using Dicts

```mw
-module( sieve_of_eratosthenes ).

-export( [primes_upto/1] ).

primes_upto( N ) ->
   Ns = lists:seq( 2, N ),
   Dict = dict:from_list( [{X, potential_prime} || X <- Ns] ),
   {Upto_sqrt_ns, _T} = lists:split( erlang:round(math:sqrt(N)), Ns ),
   {N, Prime_dict} = lists:foldl( fun find_prime/2, {N, Dict}, Upto_sqrt_ns ),
   lists:sort( dict:fetch_keys(Prime_dict) ).

find_prime( N, {Max, Dict} ) -> find_prime( dict:find(N, Dict), N, {Max, Dict} ).

find_prime( error, _N, Acc ) -> Acc;
find_prime( {ok, _Value}, N, {Max, Dict} ) when Max > N*N ->
    {Max, lists:foldl( fun dict:erase/2, Dict, lists:seq(N*N, Max, N))};
find_prime( {ok, _Value}, _, R) -> R.
```

**Output:**

```
35> sieve_of_eratosthenes:primes_upto( 20 ).
[2,3,5,7,11,13,17,19]
```

### Erlang Lists of Tuples, Sloww

A much slower, perverse method, using only lists of tuples. Especially evil is the P = lists:filtermap operation which yields a list for every iteration of the X * M row. Has the virtue of working for any -> N :)

```mw
-module( sieve ).                                                                                                    
-export( [main/1,primes/2] ).                                                                                        
                                                                                                                     
main(N) -> io:format("Primes: ~w~n", [ primes(2,N) ]).                                                               
                                                                                                                     
primes(M,N) -> primes(M, N,lists:seq( M, N ),[]).                                                                    
                                                                                                                     
primes(M,N,_Acc,Tuples) when M > N/2-> out(Tuples);                                                                  

primes(M,N,Acc,Tuples) when length(Tuples) < 1 -> 
        primes(M,N,Acc,[{X, X} || X <- Acc]);                              

primes(M,N,Acc,Tuples) ->                                                                                            
        {SqrtN, _T} = lists:split( erlang:round(math:sqrt(N)), Acc ),                                                
        F = Tuples,                                                                                                  
        Ms = lists:filtermap(fun(X) -> if X > 0 -> {true, X * M}; true -> false end end, SqrtN),                     
        P = lists:filtermap(fun(T) -> 
            case lists:keymember(T,1,F) of true -> 
            {true, lists:keyreplace(T,1,F,{T,0})}; 
             _-> false end end,  Ms),                                                                                              
        AA = mergeT(P,lists:last(P),1 ),                                                                             
        primes(M+1,N,Acc,AA).                                                                                        
                                                                                                                     
mergeT(L,M,Acc) when Acc == length(L) -> M;                                                                          
mergeT(L,M,Acc) ->                                                                                                   
        A = lists:nth(Acc,L),                                                                                        
        B = M,                                                                                                       
        Mer = lists:zipwith(fun(X, Y) -> if X < Y -> X; true -> Y end end, A, B),                                    
        mergeT(L,Mer,Acc+1).                                                                                         
                                                                                                                     
out(Tuples) ->                                                                                                       
        Primes = lists:filter( fun({_,Y}) -> Y > 0 end,  Tuples),                                                    
        [ X || {X,_} <- Primes ].
```

**Output:**

```
109> sieve:main(20).
Primes: [2,3,5,7,11,13,17,19]
ok
110> timer:tc(sieve, main, [20]).        
Primes: [2,3,5,7,11,13,17,19]
{129,ok}
```

### Erlang with ordered sets

Since I had written a really odd and slow one, I thought I'd best do a better performer. Inspired by an example from https://github.com/jupp0r

```mw
-module(ossieve).
-export([main/1]).

sieve(Candidates,SearchList,Primes,_Maximum) when length(SearchList) == 0 ->
    ordsets:union(Primes,Candidates);
sieve(Candidates,SearchList,Primes,Maximum)  ->
     H = lists:nth(1,string:substr(Candidates,1,1)),
     Reduced1 = ordsets:del_element(H, Candidates),
     {Reduced2, ReducedSearch} = remove_multiples_of(H, Reduced1, SearchList),
     NewPrimes = ordsets:add_element(H,Primes),
     sieve(Reduced2, ReducedSearch, NewPrimes, Maximum).

remove_multiples_of(Number,Candidates,SearchList) ->                                 
    NewSearchList = ordsets:filter( fun(X) -> X >= Number * Number end, SearchList), 
    RemoveList = ordsets:filter( fun(X) -> X rem Number == 0 end, NewSearchList),
    {ordsets:subtract(Candidates, RemoveList), ordsets:subtract(NewSearchList, RemoveList)}.

main(N) ->      
    io:fwrite("Creating Candidates...~n"),
    CandidateList = lists:seq(3,N,2),
    Candidates = ordsets:from_list(CandidateList),
    io:fwrite("Sieving...~n"),
    ResultSet = ordsets:add_element(2,sieve(Candidates,Candidates,ordsets:new(),N)),
    io:fwrite("Sieved... ~w~n",[ResultSet]).
```

**Output:**

```
36> ossieve:main(100).
Creating Candidates...
Sieving...
Sieved... [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
ok
```

### Erlang Canonical

A pure list comprehension approach.

```mw
-module(sieveof).
-export([main/1,primes/1, primes/2]).                 
                                                      
main(X) -> io:format("Primes: ~w~n", [ primes(X) ]).  
                                 
primes(X) -> sieve(range(2, X)).                                         
primes(X, Y) -> remove(primes(X), primes(Y)).                            
                                                                         
range(X, X) -> [X];                                                      
range(X, Y) -> [X | range(X + 1, Y)].                                    
                                                                         
sieve([X]) -> [X];                                                       
sieve([H | T]) -> [H | sieve(remove([H * X || X <-[H | T]], T))].        
                                                                         
remove(_, []) -> [];                                                     
remove([H | X], [H | Y]) -> remove(X, Y);                                
remove(X, [H | Y]) -> [H | remove(X, Y)].
```

{out}

```
> timer:tc(sieve, main, [100]). 
Primes: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
{7350,ok}
61> timer:tc(sieveof, main, [100]). 
Primes: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
{363,ok}
```

Clearly not only more elegant, but faster :) Thanks to http://stackoverflow.com/users/113644/g-b, although it uses multiplications (and is thus more an "Euler's sieve"), whereas Eratosthenes' uses additions.

### Erlang ets + cpu distributed implementation

much faster previous erlang examples

```mw
#!/usr/bin/env escript
%% -*- erlang -*-
%%! -smp enable -sname p10_4
% vim:syn=erlang

-mode(compile).

main([N0]) ->
    N = list_to_integer(N0),
    ets:new(comp, [public, named_table, {write_concurrency, true} ]),
    ets:new(prim, [public, named_table, {write_concurrency, true}]),
    composite_mc(N),
    primes_mc(N),
    io:format("Answer: ~p ~n", [lists:sort([X||{X,_}<-ets:tab2list(prim)])]).

primes_mc(N) ->
    case erlang:system_info(schedulers) of
        1 -> primes(N);
        C -> launch_primes(lists:seq(1,C), C, N, N div C)
    end.
launch_primes([1|T], C, N, R) -> P = self(), spawn(fun()-> primes(2,R), P ! {ok, prm} end), launch_primes(T, C, N, R);
launch_primes([H|[]], C, N, R)-> P = self(), spawn(fun()-> primes(R*(H-1)+1,N), P ! {ok, prm} end), wait_primes(C);
launch_primes([H|T], C, N, R) -> P = self(), spawn(fun()-> primes(R*(H-1)+1,R*H), P ! {ok, prm} end), launch_primes(T, C, N, R).

wait_primes(0) -> ok;
wait_primes(C) ->
    receive
        {ok, prm} -> wait_primes(C-1)
    after 1000    -> wait_primes(C)
    end.

primes(N) -> primes(2, N).
primes(I,N) when I =< N ->
    case ets:lookup(comp, I) of
        [] -> ets:insert(prim, {I,1})
        ;_ -> ok
    end,
    primes(I+1, N);
primes(I,N) when I > N -> ok.

composite_mc(N) -> composite_mc(N,2,round(math:sqrt(N)),erlang:system_info(schedulers)).
composite_mc(N,I,M,C) when I =< M, C > 0 ->
    C1 = case ets:lookup(comp, I) of
        [] -> comp_i_mc(I*I, I, N), C-1
        ;_ -> C
    end,
    composite_mc(N,I+1,M,C1);
composite_mc(_,I,M,_) when I > M -> ok;
composite_mc(N,I,M,0) ->
    receive
        {ok, cim} -> composite_mc(N,I,M,1)
    after 1000    -> composite_mc(N,I,M,0)
    end.

comp_i_mc(J, I, N) -> 
    Parent = self(),
    spawn(fun() ->
        comp_i(J, I, N),
        Parent ! {ok, cim}
    end).

comp_i(J, I, N) when J =< N -> ets:insert(comp, {J, 1}), comp_i(J+I, I, N);
comp_i(J, _, N) when J > N -> ok.
```

**Output:**

```
mkh@mkh-xps:~/work/mblog/pr_euler/p10$ ./generator.erl 100
Answer: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,
         97]
```

another several erlang implementation: http://mijkenator.github.io/2015/11/29/project-euler-problem-10/

### Erlang using lists:seq\3 for the initial list and the lists of multiples to be removed

```mw
-module(primesieve).
-export([primes/1]).

mult(N, Limit) -> 
    case Limit > N * N of
        true -> lists:seq(N * N, Limit, N);
        false -> []
    end.

primes(Limit) -> 
    case Limit > 1 of
        true -> sieve(Limit, 3, [2] ++ lists:seq(3, Limit, 2), mult(3, Limit));
        false -> []
    end.

sieve(Limit, D, S, M) ->
    case Limit < D * D of
        true -> S;
        false -> sieve(Limit, D + 2, S -- M, mult(D + 2, Limit))
    end.
```

**Output:**

```
2> primesieve:primes(100).
[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
 79,83,89,97]

3> timer:tc(primesieve, primes, [100]).
{20,
 [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
  79,83,89,97]}
```
