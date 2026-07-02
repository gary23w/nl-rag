---
title: "Sieve of Eratosthenes (part 5/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/21
---

## COBOL

```mw
*> Please ignore the asterisks in the first column of the next comments,
*> which are kludges to get syntax highlighting to work.
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Sieve-Of-Eratosthenes.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  Max-Number       USAGE UNSIGNED-INT.
       01  Max-Prime        USAGE UNSIGNED-INT.

       01  Num-Group.
           03  Num-Table PIC X VALUE "P"
                   OCCURS 1 TO 10000000 TIMES DEPENDING ON Max-Number
                   INDEXED BY Num-Index.
               88  Is-Prime VALUE "P" FALSE "N".
               
       01  Current-Prime    USAGE UNSIGNED-INT.

       01  I                USAGE UNSIGNED-INT.

       PROCEDURE DIVISION.
           DISPLAY "Enter the limit: " WITH NO ADVANCING
           ACCEPT Max-Number
           DIVIDE Max-Number BY 2 GIVING Max-Prime

*          *> Set Is-Prime of all non-prime numbers to false.
           SET Is-Prime (1) TO FALSE
           PERFORM UNTIL Max-Prime < Current-Prime
*              *> Set current-prime to next prime.
               ADD 1 TO Current-Prime
               PERFORM VARYING Num-Index FROM Current-Prime BY 1
                   UNTIL Is-Prime (Num-Index)
               END-PERFORM
               MOVE Num-Index TO Current-Prime

*              *> Set Is-Prime of all multiples of current-prime to
*              *> false, starting from current-prime sqaured.
               COMPUTE Num-Index = Current-Prime ** 2
               PERFORM UNTIL Max-Number < Num-Index
                   SET Is-Prime (Num-Index) TO FALSE
                   SET Num-Index UP BY Current-Prime
               END-PERFORM
           END-PERFORM

*          *> Display the prime numbers.
           PERFORM VARYING Num-Index FROM 1 BY 1
                   UNTIL Max-Number < Num-Index
               IF Is-Prime (Num-Index)
                   DISPLAY Num-Index
               END-IF
           END-PERFORM

           GOBACK
           .
```


## Comal

Translation of

:

BASIC

```mw
// Sieve of Eratosthenes
input "Limit? ": limit
dim sieve(1:limit)
sqrlimit:=sqr(limit)
sieve(1):=1
p:=2
while p<=sqrlimit do
 while sieve(p) and p<sqrlimit do
  p:=p+1
 endwhile
 if p>sqrlimit then goto done
 for i:=p*p to limit step p do
  sieve(i):=1
 endfor i
 p:=p+1
endwhile
done:
print 2,
for i:=3 to limit do
 if sieve(i)=0 then
  print ", ",i,
 endif
endfor i
print
```

**Output:**

```
Limit? 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
79, 83, 89, 97

end
```


## Common Lisp

```mw
(defun sieve-of-eratosthenes (maximum)
  (loop
     with sieve = (make-array (1+ maximum)
                              :element-type 'bit
                              :initial-element 0)
     for candidate from 2 to maximum
     when (zerop (bit sieve candidate))
     collect candidate
     and do (loop for composite from (expt candidate 2) 
               to maximum by candidate
               do (setf (bit sieve composite) 1))))
```

Working with odds only (above twice speedup), and marking composites only for primes up to the square root of the maximum:

```mw
(defun sieve-odds (maximum)
  "Prime numbers sieve for odd numbers. 
   Returns a list with all the primes that are 
                      not greater than maximum."
  (loop :with maxi = (ash (1- maximum) -1)
        :with stop = (ash (isqrt maximum) -1)
        :with sieve = (make-array (1+ maxi) :element-type 'bit 
                                            :initial-element 0)
        :for i :from 1 :to maxi
        :for odd-number = (1+ (ash i 1))
        :when (zerop (sbit sieve i))
          :collect odd-number :into values
        :when (<= i stop)
          :do (loop :for j 
                      :from (* i (1+ i) 2) :to maxi :by odd-number
                    :do (setf (sbit sieve j) 1))
        :finally (return (cons 2 values))))
```

The indexation scheme used here interprets each index `i` as standing for the value `n = 2i+1` such that `i = (n-1)/2`. Bit `0` is unused, a small price to pay for the simpler index calculations compared with the `2i+3` indexation scheme. The multiples of a given odd prime `p` are enumerated in increments of `2p`, which corresponds to the index increment of `p` on the sieve array. The starting point `p*p = (2i+1)(2i+1) = 4i(i+1)+1` corresponds to the index `2i(i+1)`.

While formally a *wheel*, odds are uniformly spaced and do not require any special processing except for value translation. Wheels proper aren't uniformly spaced and are thus trickier.


## Cowgol

```mw
include "cowgol.coh";

# To change the maximum prime, change the size of this array
# Everything else is automatically filled in at compile time
var sieve: uint8[5000];

# Make sure all elements of the sieve are set to zero
MemZero(&sieve as [uint8], @bytesof sieve);

# Generate the sieve
var prime: @indexof sieve := 2;
while prime < @sizeof sieve loop
    if sieve[prime] == 0 then
        var comp: @indexof sieve := prime * prime;
        while comp < @sizeof sieve loop
            sieve[comp] := 1;
            comp := comp + prime;
        end loop;
    end if;
    prime := prime + 1;
end loop;

# Print all primes
var cand: @indexof sieve := 2;
while cand < @sizeof sieve loop
    if sieve[cand] == 0 then
        print_i16(cand as uint16);
        print_nl();
    end if;
    cand := cand + 1;
end loop;
```

**Output:**

```
2
3
5
7
11
...
4967
4969
4973
4987
4999
```


## Craft Basic

```mw
define limit = 120

dim flags[limit]

for n = 2 to limit

   let flags[n] = 1

next n

print "prime numbers less than or equal to ", limit ," are:"

for n = 2 to sqrt(limit)

   if flags[n] = 1 then

      for i = n * n to limit step n

         let flags[i] = 0

      next i

   endif

next n

for n = 1 to limit

   if flags[n] then

      print n

   endif

next n
```

**Output:**

```
prime numbers less than or equal to 120 are:

2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 
```


## Crystal

### Basic Version

This implementation uses a `BitArray` so it is automatically bit-packed to use just one bit per number representation:

```mw
# compile with `--release --no-debug` for speed...

require "bit_array"

alias Prime = UInt64

class SoE
  include Iterator(Prime)
  @bits : BitArray; @bitndx : Int32 = 2

  def initialize(range : Prime)
    if range < 2
      @bits = BitArray.new 0
    else
      @bits = BitArray.new((range + 1).to_i32)
    end
    ba = @bits; ndx = 2
    while true
      wi = ndx * ndx
      break if wi >= ba.size
      if ba[ndx]
        ndx += 1; next
      end
      while wi < ba.size
        ba[wi] = true; wi += ndx
      end
      ndx += 1
    end
  end

  def next
    while @bitndx < @bits.size
      if @bits[@bitndx]
        @bitndx += 1; next
      end
      rslt = @bitndx.to_u64; @bitndx += 1; return rslt
    end
    stop
  end
end

print "Primes up to a hundred:  "
SoE.new(100).each { |p| print " ", p }; puts
print "Number of primes to a million:  "
puts SoE.new(1_000_000).each.size
print "Number of primes to a billion:  "
start_time = Time.monotonic
print SoE.new(1_000_000_000).each.size
elpsd = (Time.monotonic - start_time).total_milliseconds
puts " in #{elpsd} milliseconds."
```

**Output:**

```
Primes up to a hundred:   2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
Number of primes to a million:  78498
Number of primes to a billion:  50847534 in 10219.222539 milliseconds.
```

This is as run on an Intel SkyLake i5-6500 at 3.6 GHz (automatic boost for single threaded as here).

### Odds-Only Version

the non-odds-only version as per the above should never be used because in not using odds-only, it uses twice the memory and over two and a half times the CPU operations as the following odds-only code, which is very little more complex:

```mw
# compile with `--release --no-debug` for speed...

require "bit_array"

alias Prime = UInt64

class SoE_Odds
  include Iterator(Prime)
  @bits : BitArray; @bitndx : Int32 = -1

  def initialize(range : Prime)
    if range < 3
      @bits = BitArray.new 0
    else
      @bits = BitArray.new(((range - 1) >> 1).to_i32)
    end
    ba = @bits; ndx = 0
    while true
      wi = (ndx + ndx) * (ndx + 3) + 3 # start cull index calculation
      break if wi >= ba.size
      if ba[ndx]
        ndx += 1; next
      end
      bp = ndx + ndx + 3
      while wi < ba.size
        ba[wi] = true; wi += bp
      end
      ndx += 1
    end
  end

  def next
    while @bitndx < @bits.size
      if @bitndx < 0
        @bitndx += 1; return 2_u64
      elsif @bits[@bitndx]
        @bitndx += 1; next
      end
      rslt = (@bitndx + @bitndx + 3).to_u64; @bitndx += 1; return rslt
    end
    stop
  end
end

print "Primes up to a hundred:  "
SoE_Odds.new(100).each { |p| print " ", p }; puts
print "Number of primes to a million:  "
puts SoE_Odds.new(1_000_000).each.size
print "Number of primes to a billion:  "
start_time = Time.monotonic
print SoE_Odds.new(1_000_000_000).each.size
elpsd = (Time.monotonic - start_time).total_milliseconds
puts " in #{elpsd} milliseconds."
```

**Output:**

```
Primes up to a hundred:   2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
Number of primes to a million:  78498
Number of primes to a billion:  50847534 in 4877.829642 milliseconds.
```

As can be seen, this is over two times faster than the non-odds-only version when run on the same CPU due to reduced pressure on the CPU data cache; however it is only reasonably performant for ranges of a few millions, and above that a page-segmented version of odds-only (or further wheel factorization) should be used plus other techniques for a further reduction of number of CPU clock cycles per culling/marking operation.

### Page-Segmented Odds-Only Version

For sieving of ranges larger than a few million efficiently, a page-segmented sieve should always be used to preserve CPU cache associativity by making the page size to be about that of the CPU L1 data cache. The following code implements a page-segmented version that is an extensible sieve (no upper limit needs be specified) using a secondary memoized feed of base prime value arrays which use a smaller page-segment size for efficiency. When the count of the number of primes is desired, the sieve is polymorphic in output and counts the unmarked composite bits by using fast `popcount` instructions taken 64-bits at a time. The code is as follows:

```mw
# compile with `--release --no-debug` for speed...

alias Prime = UInt64
alias PrimeNdx = Int64
alias PrimeArr = Array(Prime)
alias SieveBuffer = Pointer(UInt8)
alias BasePrime = UInt32
alias BasePrimeArr = Array(BasePrime)

CPUL1CACHE = 131072 # 16 Kilobytes in nimber of bits

BITMASK = Pointer(UInt8).malloc(8) { |i| 1_u8 << i }

# Count number of non-composite (zero) bits within index range...
# sieve buffer is always evenly divisible by 64-bit words...
private def count_page_to(ndx : Int32, sb : SieveBuffer)
  lstwrdndx = ndx >> 6; mask = (~1_u64) << (ndx & 63)
  cnt = lstwrdndx * 64 + 64; sbw = sb.as(Pointer(UInt64))
  lstwrdndx.times { |i| cnt -= sbw[i].popcount }
  cnt - (sbw[lstwrdndx] | mask).popcount
end

# Cull composite bits from sieve buffer using base prime arrays;
# starting at overall given prime index for given buffer bit size...
private def cull_page(pndx : PrimeNdx, bitsz : Int32,
              bps : Iterator(BasePrimeArr), sb : SieveBuffer)
  bps.each { |bpa|
    bpa.each { |bpu32|
      bp = bpu32.to_i64; bpndx = (bp - 3) >> 1
      swi = (bpndx + bpndx) * (bpndx + 3) + 3 # calculate start prime index
      return if swi >= pndx + bitsz.to_i64
      bpi = bp.to_i32 # calculate buffer start culling index...
      bi = (swi >= pndx) ? (swi - pndx).to_i32 : begin
        r = (pndx - swi) % bp; r == 0 ? 0 : bpi - r.to_i32
      end
      # when base prime is small enough, cull using strided loops to
      # simplify the inner loops at the cost of more loop overhead...
      # allmost all of the work is done by the following loop...
      if bpi < (bitsz >> 4)
        bilmt = bi + (bpi << 3); cplmt = sb + (bitsz >> 3)
        bilmt = CPUL1CACHE if bilmt > CPUL1CACHE
        while bi < bilmt
          cp = sb + (bi >> 3); msk = BITMASK[bi & 7]
          while cp < cplmt # use pointer to save loop overhead
            cp[0] |= msk; cp += bpi
          end
          bi += bpi
        end
      else
        while bi < bitsz # bitsz
          sb[bi >> 3] |= BITMASK[bi & 7]; bi += bpi
        end
      end } }
end

# Iterator over processed prime pages, polymorphic by the converter function...
private class PagedResults(T)
  @bpas : BasePrimeArrays
  @cmpsts : SieveBuffer

  def initialize(@prmndx : PrimeNdx,
                 @cmpstsbitsz : Int32,
                 @cnvrtrfnc : (Int64, Int32, SieveBuffer) -> T)
    @bpas = BasePrimeArrays.new
    @cmpsts = SieveBuffer.malloc(((@cmpstsbitsz + 63) >> 3) & (-8))
  end

  private def dopage
    (@prmndx..).step(@cmpstsbitsz.to_i64).map { |pn|
        @cmpsts.clear(@cmpstsbitsz >> 3)
        cull_page(pn, @cmpstsbitsz, @bpas.each, @cmpsts)
        @cnvrtrfnc.call(pn, @cmpstsbitsz, @cmpsts) }
  end

  def each
    dopage
  end

  def each(& : T -> _) : Nil
    itr = dopage
    while true
      value = itr.next
      break if value.is_a?(Iterator::Stop)
      yield value
    end
  end
end

# Secondary memoized chain of BasePrime arrays (by small page size),
# which is actually a iterable lazy list (memoized) of BasePrimeArr;
# Crystal has closures, so it is easy to implement a LazyList class
# which memoizes the results of the thunk so it is only executed once...
private class BasePrimeArrays
  @baseprmarr : BasePrimeArr # head of lezy list
  @tail : BasePrimeArrays? = nil # tail starts as non-existing

  def initialize # special case for first page of base primes
    # converter of sieve buffer to base primes array...
    sb2bparrprc = -> (pn : PrimeNdx, bl : Int32, sb : SieveBuffer) {
      cnt = count_page_to(bl - 1, sb)
      bparr = BasePrimeArr.new(cnt, 0); j = 0
      bsprm = (pn + pn + 3).to_u32
      bl.times.each { |i|
        next if (sb[i >> 3] & BITMASK[i & 7]) != 0 
        bparr[j] = bsprm + (i + i).to_u32; j += 1 }
      bparr }

    cmpsts = SieveBuffer.malloc 128 # fake bparr for first iter...
    frstbparr = sb2bparrprc.call(0_i64, 1024, cmpsts)
    cull_page(0_i64, 1024, Iterator.of(frstbparr).each, cmpsts)
    @baseprmarr = sb2bparrprc.call(0_i64, 1024, cmpsts)

    # initialization of pages after the first is deferred to avoid data race...
    initbpas = -> { PagedResults.new(1024_i64, 1024, sb2bparrprc).each }
    # recursive LazyList generator function...
    nxtbpa = uninitialized Proc(Iterator(BasePrimeArr), BasePrimeArrays)
    nxtbpa = -> (bppgs : Iterator(BasePrimeArr)) {
      nbparr = bppgs.next
      abort "Unexpectedbase primes end!!!" if nbparr.is_a?(Iterator::Stop)
      BasePrimeArrays.new(nbparr, ->{ nxtbpa.call(bppgs) }) }
    @thunk = ->{ nxtbpa.call(initbpas.call) }
  end
  def initialize(@baseprmarr : BasePrimeArr, @thunk : Proc(BasePrimeArrays))
  end
  def initialize(@baseprmarr : BasePrimeArr, @thunk : Proc(Nil))
  end
  def initialize(@baseprmarr : BasePrimeArr, @thunk : Nil)
  end

  def tail # not thread safe without a lock/mutex...
    if thnk = @thunk
      @tail = thnk.call; @thunk = nil
    end
    @tail
  end

  private class BasePrimeArrIter # iterator over BasePrime arrays...
    include Iterator(BasePrimeArr)
    @dbparrs : Proc(BasePrimeArrays?)

    def initialize(fromll : BasePrimeArrays)
      @dbparrs = ->{ fromll.as(BasePrimeArrays?) }
    end

    def next
      if bpas = @dbparrs.call
        rslt = bpas.@baseprmarr; @dbparrs = -> { bpas.tail }; rslt
      else
        abort "Unexpected end of base primes array iteration!!!"
      end
    end
  end
  
  def each
    BasePrimeArrIter.new(self)
  end
end

# An "infinite" extensible iteration of primes,...
def primes
  sb2prms = ->(pn : PrimeNdx, bitsz : Int32, sb : SieveBuffer) {
    cnt = count_page_to(bitsz - 1, sb)
    prmarr = PrimeArr.new(cnt, 0); j = 0
    bsprm = (pn + pn + 3).to_u64
    bitsz.times.each { |i|
      next if (sb[i >> 3] & BITMASK[i & 7]) != 0
      prmarr[j] = bsprm + (i + i).to_u64; j += 1 }
    prmarr
  }
  (2_u64..2_u64).each
    .chain PagedResults.new(0, CPUL1CACHE, sb2prms).each.flat_map { |prmspg| prmspg.each }
end

# Counts number of primes to given limit...
def primes_count_to(lmt : Prime)
  if lmt < 3
    lmt < 2 ? return 0 : return 1
  end
  lmtndx = ((lmt - 3) >> 1).to_i64
  sb2cnt = ->(pn : PrimeNdx, bitsz : Int32, sb : SieveBuffer) {
    pglmt = pn + bitsz.to_i64 - 1
    if (pn + CPUL1CACHE.to_i64) > lmtndx
      Tuple.new(count_page_to((lmtndx - pn).to_i32, sb).to_i64, pglmt)
    else
      Tuple.new(count_page_to(bitsz - 1, sb).to_i64, pglmt)
    end
  }
  count = 1
  PagedResults.new(0, CPUL1CACHE, sb2cnt).each { |(cnt, lmt)|
    count += cnt; break if lmt >= lmtndx }
  count
end

print "The primes up to 100 are: "
primes.each.take_while { |p| p <= 100_u64 }.each { |p| print " ", p }
print ".\r\nThe Number of primes up to a million is "
print primes.each.take_while { |p| p <= 1_000_000_u64 }.size
print ".\r\nThe number of primes up to a billion is "
start_time = Time.monotonic
# answr = primes.each.take_while { |p| p <= 1_000_000_000_u64 }.size # slow way
answr = primes_count_to(1_000_000_000) # fast way
elpsd = (Time.monotonic - start_time).total_milliseconds
print "#{answr} in #{elpsd} milliseconds.\r\n"
```

**Output:**

```
The primes up to 100 are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97.
The Number of primes up to a million is 78498.
The number of primes up to a billion is 50847534 in 658.466028 milliseconds.
```

When run on the same machine as the previous version, the code is about seven and a half times as fast as even the above Odds-Only version at about 2.4 CPU clock cycles per culling operation rather than over 17, partly due to better cache associativity (about half the gain) but also due to tuning the inner culling loop for small base prime values to operate by byte pointer strides with a constant mask value to simplify the code generated for these inner loops; as there is some overhead in the eight outer loops that set this up, this technique is only applicable for smaller base primes.

Further gains are possible by using maximum wheel factorization rather than just factorization for odd base primes which can reduce the number of operations by a factor of about four and the number of CPU clock cycles per culling operation can be reduced by an average of a further about 25 percent for sieving to a billion by using extreme loop unrolling techniques for both the dense and sparse culling cases. As well, multi-threading by pages can reduce the wall clock time by a factor of the number of effective cores (non Hyper-Threaded cores).


## D

### Simpler Version

Prints all numbers less than the limit.

```mw
import std.stdio, std.algorithm, std.range, std.functional;

uint[] sieve(in uint limit) nothrow @safe {
    if (limit < 2)
        return [];
    auto composite = new bool[limit];

    foreach (immutable uint n; 2 .. cast(uint)(limit ^^ 0.5) + 1)
        if (!composite[n])
            for (uint k = n * n; k < limit; k += n)
                composite[k] = true;

    //return iota(2, limit).filter!(not!composite).array;
    return iota(2, limit).filter!(i => !composite[i]).array;
}

void main() {
    50.sieve.writeln;
}
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Faster Version

This version uses an array of bits (instead of booleans, that are represented with one byte), and skips even numbers. The output is the same.

```mw
import std.stdio, std.math, std.array;

size_t[] sieve(in size_t m) pure nothrow @safe {
    if (m < 3)
        return null;
    immutable size_t n = m - 1;
    enum size_t bpc = size_t.sizeof * 8;
    auto F = new size_t[((n + 2) / 2) / bpc + 1];
    F[] = size_t.max;

    size_t isSet(in size_t i) nothrow @safe @nogc {
        immutable size_t offset = i / bpc;
        immutable size_t mask = 1 << (i % bpc);
        return F[offset] & mask;
    }

    void resetBit(in size_t i) nothrow @safe @nogc {
        immutable size_t offset = i / bpc;
        immutable size_t mask = 1 << (i % bpc);
        if ((F[offset] & mask) != 0)
            F[offset] = F[offset] ^ mask;
    }

    for (size_t i = 3; i <= sqrt(real(n)); i += 2)
        if (isSet((i - 3) / 2))
            for (size_t j = i * i; j <= n; j += 2 * i)
                resetBit((j - 3) / 2);

    Appender!(size_t[]) result;
    result ~= 2;
    for (size_t i = 3; i <= n; i += 2)
        if (isSet((i - 3) / 2))
            result ~= i;
    return result.data;
}

void main() {
    50.sieve.writeln;
}
```

### Extensible Version

(This version is used in the task Extensible prime generator.)

```mw
/// Extensible Sieve of Eratosthenes.
struct Prime {
    uint[] a = [2];

    private void grow() pure nothrow @safe {
        immutable p0 = a[$ - 1] + 1;
        auto b = new bool[p0];

        foreach (immutable di; a) {
            immutable uint i0 = p0 / di * di;
            uint i = (i0 < p0) ? i0 + di - p0 : i0 - p0;
            for (; i < b.length; i += di)
                b[i] = true;
        }

        foreach (immutable i, immutable bi; b)
            if (!b[cast(uint)i])
                a ~= p0 + cast(uint)i;
    }

    uint opCall(in uint n) pure nothrow @safe {
        while (n >= a.length)
            grow;
        return a[n];
    }
}

version (sieve_of_eratosthenes3_main) {
    void main() {
        import std.stdio, std.range, std.algorithm;

        Prime prime;
        uint.max.iota.map!prime.until!q{a > 50}.writeln;
    }
}
```

Compile with -d-version=sieve_of_eratosthenes3_main or, if you're using GDC, -fversion=sieve_of_eratosthenes3_main.

The output is the same as the first version.


## Dart

```mw
// helper function to pretty print an Iterable
String iterableToString(Iterable seq) {
  String str = "[";

  Iterator i = seq.iterator;

  if (i.moveNext()) str += i.current.toString();

  while(i.moveNext()) {
    str += ", " + i.current.toString();
  }

  return str + "]";
}

main() {
  int limit = 1000;

  int start = new DateTime.now().millisecondsSinceEpoch;

  Set<int> sieve = new Set<int>();
  
  for(int i = 2; i <= limit; i++) {
    sieve.add(i);
  }

  for(int i = 2; i * i <= limit; i++) {
   if(sieve.contains(i)) {
     for(int j = i * i; j <= limit; j += i) {
       sieve.remove(j);
     }
   }
  }

  var sortedValues = new List<int>.from(sieve);

  int elapsed = new DateTime.now().millisecondsSinceEpoch - start;

  print("Found ${sieve.length} primes up to ${limit} in ${elapsed} milliseconds.");
  print(iterableToString(sortedValues)); // expect sieve.length to be 168 up to 1000...
  //  Expect.equals(168, sieve.length);
}
```

**Output:**

```
Found 168 primes up to 1000 in 9 milliseconds.
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
```

Although it has the characteristics of a true Sieve of Eratosthenes, the above code isn't very efficient due to the remove/modify operations on the Set. Due to these, the computational complexity isn't close to linear with increasing range and it is quite slow for larger sieve ranges compared to compiled languages, taking an average of about 22 thousand CPU clock cycles for each of the 664579 primes (about 4 seconds on a 3.6 Gigahertz CPU) just to sieve to ten million.

### faster bit-packed array odds-only solution

```mw
import 'dart:typed_data';
import 'dart:math';

Iterable<int> soeOdds(int limit) {
  if (limit < 3) return limit < 2 ? Iterable.empty() : [2];
  int lmti = (limit - 3) >> 1;
  int bfsz = (lmti >> 3) + 1;
  int sqrtlmt = (sqrt(limit) - 3).floor() >> 1;
  Uint32List cmpsts = Uint32List(bfsz);
  for (int i = 0; i <= sqrtlmt; ++i)
    if ((cmpsts[i >> 5] & (1 << (i & 31))) == 0) {
      int p = i + i + 3;
      for (int j = (p * p - 3) >> 1; j <= lmti; j += p)
        cmpsts[j >> 5] |= 1 << (j & 31);
    }
  return
    [2].followedBy(
      Iterable.generate(lmti + 1)
      .where((i) => cmpsts[i >> 5] & (1 << (i & 31)) == 0)
      .map((i) => i + i + 3) );
}

void main() {
  final int range = 100000000;
  String s = "( ";
  primesPaged().take(25).forEach((p)=>s += "$p "); print(s + ")");
  print("There are ${countPrimesTo(1000000)} primes to 1000000.");
  final start = DateTime.now().millisecondsSinceEpoch;
  final answer = soeOdds(range).length;
  final elapsed = DateTime.now().millisecondsSinceEpoch - start;
  print("There were $answer primes found up to $range.");
  print("This test bench took $elapsed milliseconds.");
}
```

**Output:**

```
( 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 )
There are 78498 primes to 1000000.
There were 5761455 primes found up to 100000000.
This test bench took 4604 milliseconds.
```

The above code is somewhat faster at about 1.5 thousand CPU cycles per prime here run on a 1.92 Gigahertz low end Intel x5-Z8350 CPU or about 2.5 seconds on a 3.6 Gigahertz CPU using the Dart VM to sieve to 100 million.

### Unbounded infinite iterators/generators of primes

**Infinite generator using a (hash) Map (sieves odds-only)**

The following code will have about O(n log (log n)) performance due to a hash table having O(1) average performance and is only somewhat slow due to the constant overhead of processing hashes:

```mw
Iterable<int> primesMap() {
    Iterable<int> oddprms() sync* {
      yield(3); yield(5); // need at least 2 for initialization
      final Map<int, int> bpmap = {9: 6};
      final Iterator<int> bps = oddprms().iterator;
      bps.moveNext(); bps.moveNext(); // skip past 3 to 5
      int bp = bps.current;
      int n = bp;
      int q = bp * bp;
      while (true) {
        n += 2;
        while (n >= q || bpmap.containsKey(n)) {
          if (n >= q) {
            final int inc = bp << 1;
            bpmap[bp * bp + inc] = inc;
            bps.moveNext(); bp = bps.current; q = bp * bp;
          } else {
            final int inc = bpmap.remove(n);
            int next = n + inc;
            while (bpmap.containsKey(next)) {
              next += inc;
            }
            bpmap[next] = inc;
          }
          n += 2;
        }
        yield(n);
      }
    }
    return [2].followedBy(oddprms());
}

void main() {
  final int range = 100000000;
  String s = "( ";
  primesMap().take(25).forEach((p)=>s += "$p "); print(s + ")");
  print("There are ${primesMap().takeWhile((p)=>p<=1000000).length} preimes to 1000000.");
  final start = DateTime.now().millisecondsSinceEpoch;
  final answer = primesMap().takeWhile((p)=>p<=range).length;
  final elapsed = DateTime.now().millisecondsSinceEpoch - start;
  print("There were $answer primes found up to $range.");
  print("This test bench took $elapsed milliseconds.");
}
```

**Output:**

```
( 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 )
There are 78498 preimes to 1000000.
There were 5761455 primes found up to 100000000.
This test bench took 16086 milliseconds.
```

This takes about 5300 CPU clock cycles per prime or about 8.4 seconds if run on a 3.6 Gigahertz CPU, which is slower than the above fixed bit-packed array version but has the advantage that it runs indefinitely, (at least on 64-bit machines; on 32 bit machines it can only be run up to the 32-bit number range, or just about a factor of 20 above as above).

Due to the constant execution overhead this is only reasonably useful for ranges up to tens of millions anyway.

**Fast page segmented array infinite generator (sieves odds-only)**

The following code also theoretically has a O(n log (log n)) execution speed performance and the same limited use on 32-bit execution platformas, but won't realize the theoretical execution complexity for larger primes due to the cache size increasing in size beyond its limits; but as the CPU L2 cache size that it automatically grows to use isn't any slower than the basic culling loop speed, it won't slow down much above that limit up to ranges of about 2.56e14, which will take in the order of weeks:

Translation of

:

Kotlin

```mw
import 'dart:typed_data';
import 'dart:math';
import 'dart:collection';

// a lazy list
typedef _LazyList _Thunk();
class _LazyList<T> {
  final T head;
  _Thunk thunk;
  _LazyList<T> _rest;
  _LazyList(T this.head, _Thunk this.thunk);
  _LazyList<T> get rest {
    if (this.thunk != null) {
      this._rest = this.thunk();
      this.thunk = null;
    }
    return this._rest;
  }
}

class _LazyListIterable<T> extends IterableBase<T> {
  _LazyList<T> _first;
  _LazyListIterable(_LazyList<T> this._first);
  @override Iterator<T> get iterator {
    Iterable<T> inner() sync* {
      _LazyList<T> current = this._first;
      while (true) {
        yield(current.head);
        current = current.rest;
      }
    }
    return inner().iterator;
  }
}

// zero bit population count Look Up Table for 16-bit range...
final Uint8List CLUT =
  Uint8List.fromList(
    Iterable.generate(65536)
    .map((i) {
      final int v0 = ~i & 0xFFFF;
      final int v1 = v0 - ((v0 & 0xAAAA) >> 1);
      final int v2 = (v1 & 0x3333) + ((v1 & 0xCCCC) >> 2);
      return (((((v2 & 0x0F0F) + ((v2 & 0xF0F0) >> 4)) * 0x0101)) >> 8) & 31;
    })
    .toList());

int _countComposites(Uint8List cmpsts) {
  Uint16List buf = Uint16List.view(cmpsts.buffer);
  int lmt = buf.length;
  int count = 0;
  for (var i = 0; i < lmt; ++i) {
    count += CLUT[buf[i]];
  }
  return count;
} 

// converts an entire sieved array of bytes into an array of UInt32 primes,
// to be used as a source of base primes...
Uint32List _composites2BasePrimeArray(int low, Uint8List cmpsts) {
  final int lmti = cmpsts.length << 3;
  final int len = _countComposites(cmpsts);
  final Uint32List rslt = Uint32List(len);
  int j = 0;
  for (int i = 0; i < lmti; ++i) {
    if (cmpsts[i >> 3] & 1 << (i & 7) == 0) {
        rslt[j++] = low + i + i;
    }
  }
  return rslt;
}

// do sieving work based on low starting value for the given buffer and
// the given lazy list of base prime arrays...
void _sieveComposites(int low, Uint8List buffer, Iterable<Uint32List> bpas) {
  final int lowi = (low - 3) >> 1;
  final int len = buffer.length;
  final int lmti = len << 3;
  final int nxti = lowi + lmti;
  for (var bpa in bpas) {
    for (var bp in bpa) {
      final int bpi = (bp - 3) >> 1;
      int strti = ((bpi * (bpi + 3)) << 1) + 3;
      if (strti >= nxti) return;
      if (strti >= lowi) strti = strti - lowi;
      else {
        strti = (lowi - strti) % bp;
        if (strti != 0) strti = bp - strti;
      }
      if (bp <= len >> 3 && strti <= lmti - bp << 6) {
        final int slmti = min(lmti, strti + bp << 3);
        for (var s = strti; s < slmti; s += bp) {
          final int msk = 1 << (s & 7);
          for (var c = s >> 3; c < len; c += bp) {
              buffer[c] |= msk;
          }
        }
      }
      else {
        for (var c = strti; c < lmti; c += bp) {
            buffer[c >> 3] |= 1 << (c & 7);
        }
      }
    }
  } 
}

// starts the secondary base primes feed with minimum size in bits set to 4K...
// thus, for the first buffer primes up to 8293,
// the seeded primes easily cover it as 97 squared is 9409...
Iterable<Uint32List> _makeBasePrimeArrays() {
  var cmpsts = Uint8List(512);
  _LazyList<Uint32List> _nextelem(int low, Iterable<Uint32List> bpas) {
    // calculate size so that the bit span is at least as big as the
    // maximum culling prime required, rounded up to minsizebits blocks...
    final int rqdsz = 2 + sqrt((1 + low).toDouble()).toInt();
    final sz = (((rqdsz >> 12) + 1) << 9); // size in bytes
    if (sz > cmpsts.length) cmpsts = Uint8List(sz);
    cmpsts.fillRange(0, cmpsts.length, 0);
    _sieveComposites(low, cmpsts, bpas);
    final arr = _composites2BasePrimeArray(low, cmpsts);
    final nxt = low + (cmpsts.length << 4);
    return _LazyList(arr, () => _nextelem(nxt, bpas));
  }
  // pre-seeding breaks recursive race,
  // as only known base primes used for first page...
  final preseedarr = Uint32List.fromList( [ // pre-seed to 100, can sieve to 10,000...
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
    , 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ] );
  return _LazyListIterable(
           _LazyList(preseedarr,
           () => _nextelem(101, _makeBasePrimeArrays()))
         );
}

// an iterable sequence over successive sieved buffer composite arrays,
// returning a tuple of the value represented by the lowest possible prime
// in the sieved composites array and the array itself;
// the array has a 16 Kilobytes minimum size (CPU L1 cache), but
// will grow so that the bit span is larger than the
// maximum culling base prime required, possibly making it larger than
// the L1 cache for large ranges, but still reasonably efficient using
// the L2 cache: very efficient up to about 16e9 range;
// reasonably efficient to about 2.56e14 for two Megabyte L2 cache = > 1 day...
Iterable<List> _makeSievePages() sync*  {
  final bpas = _makeBasePrimeArrays(); // secondary source of base prime arrays
  int low = 3;
  Uint8List cmpsts = Uint8List(16384);
  _sieveComposites(3, cmpsts, bpas);
  while (true) {
    yield([low, cmpsts]);
    final rqdsz = 2 + sqrt((1 + low).toDouble()).toInt(); // problem with sqrt not exact past about 10^12!!!!!!!!!
    final sz = ((rqdsz >> 17) + 1) << 14; // size iin bytes
    if (sz > cmpsts.length) cmpsts = Uint8List(sz);
    cmpsts.fillRange(0, cmpsts.length, 0);
    low += cmpsts.length << 4;
    _sieveComposites(low, cmpsts, bpas);
  }
}

int countPrimesTo(int range) {
  if (range < 3) { if (range < 2) return 0; else return 1; }
  var count = 1;
  for (var sp in _makeSievePages()) {
    int low = sp[0]; Uint8List cmpsts = sp[1];
    if ((low + (cmpsts.length << 4)) > range) {
      int lsti = (range - low) >> 1;
      var lstw = (lsti >> 4); var lstb = lstw << 1;
      var msk = (-2 << (lsti & 15)) & 0xFFFF;
      var buf = Uint16List.view(cmpsts.buffer, 0, lstw);
      for (var i = 0; i < lstw; ++i)
        count += CLUT[buf[i]];
      count += CLUT[(cmpsts[lstb + 1] << 8) | cmpsts[lstb] | msk];
      break;
    } else {
      count += _countComposites(cmpsts);
    }
  }
  return count;
}

// sequence over primes from above page iterator;
// unless doing something special with individual primes, usually unnecessary;
// better to do manipulations based on the composites bit arrays...
// takes at least as long to enumerate the primes as sieve them...
Iterable<int> primesPaged() sync* {
  yield(2);
  for (var sp in _makeSievePages()) {
    int low = sp[0]; Uint8List cmpsts = sp[1];
    var szbts = cmpsts.length << 3;
    for (var i = 0; i < szbts; ++i) {
        if (cmpsts[i >> 3].toInt() & (1 << (i & 7)) != 0) continue;
        yield(low + i + i);
    }
  }
}

void main() {
  final int range = 1000000000;
  String s = "( ";
  primesPaged().take(25).forEach((p)=>s += "$p "); print(s + ")");
  print("There are ${countPrimesTo(1000000)} primes to 1000000.");
  final start = DateTime.now().millisecondsSinceEpoch;
  final answer = countPrimesTo(range); // fast way
//  final answer = primesPaged().takeWhile((p)=>p<=range).length; // slow way using enumeration
  final elapsed = DateTime.now().millisecondsSinceEpoch - start;
  print("There were $answer primes found up to $range.");
  print("This test bench took $elapsed milliseconds.");
}
```

**Output:**

```
( 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 )
There are 78498 primes to 1000000.
There were 50847534 primes found up to 1000000000.
This test bench took 9385 milliseconds.
```

This version counts the primes up to one billion in about five seconds at 3.6 Gigahertz (a low end 1.92 Gigahertz CPU used here) or about 350 CPU clock cycles per prime under the Dart Virtual Machine (VM).

Note that it takes about four times as long to do this using the provided primes generator/enumerator as noted in the code, which is normal for all languages that it takes longer to actually enumerate the primes than it does to sieve in culling the composite numbers, but Dart is somewhat slower than most for this.

The algorithm can be sped up by a factor of four by extreme wheel factorization and (likely) about a factor of the effective number of CPU cores by using multi-processing isolates, but there isn't much point if one is to use the prime generator for output. For most purposes, it is better to use custom functions that directly manipulate the culled bit-packed page segments as `countPrimesTo` does here.


## dc

```mw
[dn[,]n dsx [d 1 r :a lx + d ln!<.] ds.x lx] ds@
[sn 2 [d;a 0=@ 1 + d ln!<#] ds#x] se

100 lex
```

**Output:**

```
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,\
97,
```


## Delphi

```mw
program erathostenes;

{$APPTYPE CONSOLE}

type
  TSieve = class
  private
    fPrimes: TArray<boolean>;
    procedure InitArray;
    procedure Sieve;
    function getNextPrime(aStart: integer): integer;
    function getPrimeArray: TArray<integer>;
  public
    function getPrimes(aMax: integer): TArray<integer>;
  end;

  { TSieve }

function TSieve.getNextPrime(aStart: integer): integer;
begin
  result := aStart;
  while not fPrimes[result] do
    inc(result);
end;

function TSieve.getPrimeArray: TArray<integer>;
var
  i, n: integer;
begin
  n := 0;
  setlength(result, length(fPrimes)); // init array with maximum elements
  for i := 2 to high(fPrimes) do
  begin
    if fPrimes[i] then
    begin
      result[n] := i;
      inc(n);
    end;
  end;
  setlength(result, n); // reduce array to actual elements
end;

function TSieve.getPrimes(aMax: integer): TArray<integer>;
begin
  setlength(fPrimes, aMax);
  InitArray;
  Sieve;
  result := getPrimeArray;
end;

procedure TSieve.InitArray;
begin
  for i := 2 to high(fPrimes) do
    fPrimes[i] := true;
end;

procedure TSieve.Sieve;
var
  i, n, max: integer;
begin
  max := length(fPrimes);
  i := 2;
  while i < sqrt(max) do
  begin
    n := sqr(i);
    while n < max do
    begin
      fPrimes[n] := false;
      inc(n, i);
    end;
    i := getNextPrime(i + 1);
  end;
end;

var
  i: integer;
  Sieve: TSieve;

begin
  Sieve := TSieve.Create;
  for i in Sieve.getPrimes(100) do
    write(i, ' ');
  Sieve.Free;
  readln;
end.
```

Output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
```


## Draco

```mw
/* Sieve of Eratosthenes - fill a given boolean array */
proc nonrec sieve([*] bool prime) void:
    word p, c, max;
    max := dim(prime,1)-1;
    prime[0] := false;
    prime[1] := false;
    for p from 2 upto max do prime[p] := true od;
    for p from 2 upto max>>1 do
        if prime[p] then
            for c from p*2 by p upto max do
                prime[c] := false
            od
        fi
    od
corp

/* Print primes up to 1000 using the sieve */
proc nonrec main() void:
    word MAX = 1000;
    unsigned MAX i;
    byte c;
    [MAX+1] bool prime;
    sieve(prime);     

    c := 0;
    for i from 0 upto MAX do
        if prime[i] then
            write(i:4);
            c := c + 1;
            if c=10 then c:=0; writeln() fi
        fi
    od
corp
```

**Output:**

```
   2   3   5   7  11  13  17  19  23  29
  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97 101 103 107 109 113
 127 131 137 139 149 151 157 163 167 173
 179 181 191 193 197 199 211 223 227 229
 233 239 241 251 257 263 269 271 277 281
 283 293 307 311 313 317 331 337 347 349
 353 359 367 373 379 383 389 397 401 409
 419 421 431 433 439 443 449 457 461 463
 467 479 487 491 499 503 509 521 523 541
 547 557 563 569 571 577 587 593 599 601
 607 613 617 619 631 641 643 647 653 659
 661 673 677 683 691 701 709 719 727 733
 739 743 751 757 761 769 773 787 797 809
 811 821 823 827 829 839 853 857 859 863
 877 881 883 887 907 911 919 929 937 941
 947 953 967 971 977 983 991 997
```


## DuckDB

Works with

:

DuckDB

version V1.1

Works with

:

DuckDB

version V1.0

If Eratosthenes had been constrained to work with SQL, he might have come up with something like the following. The algorithm is a memory hog as it requires copying a portion of the "sieve" at each iteration.

If the order of the results is important, add an ORDER BY clause.

```mw
# Produce a table of primes less than or equal to mx
create or replace function sieve(mx) as table (
  with recursive
  sieve(prime, n) AS (
    -- Base case: a table wherein the column labeled n ranges from 2 through mx.
    -- The condition `prime = n` will serve as a flag that n is prime.
    select 2, unnest(range(2, 1+mx)) as n
    union all
    -- remove multiples of the current prime
    select prime + (case when prime = 2 then 1 else 2 end), n
    from sieve
    where n % prime != 0
      and prime <= mx   -- constrain the recursion
  )
  select prime
  from   sieve
  where  n = prime
);

from sieve(19);
```

**Output:**

```
 
┌───────┐
│ prime │
│ int32 │
├───────┤
│     2 │
│     3 │
│     5 │
│     7 │
│    11 │
│    13 │
│    17 │
│    19 │
└───────┘
```


## DWScript

```mw
function Primes(limit : Integer) : array of Integer;
var
   n, k : Integer;
   sieve := new Boolean[limit+1];
begin
   for n := 2 to Round(Sqrt(limit)) do begin
      if not sieve[n] then begin
         for k := n*n to limit step n do
            sieve[k] := True;
      end;
   end;
   
   for k:=2 to limit do
      if not sieve[k] then
         Result.Add(k);
end;

var r := Primes(50);
var i : Integer;
for i:=0 to r.High do
   PrintLn(r[i]);
```


## Dylan

With outer to sqrt and inner to p^2 optimizations:

```mw
define method primes(n)
  let limit = floor(n ^ 0.5) + 1;
  let sieve = make(limited(<simple-vector>, of: <boolean>), size: n + 1, fill: #t);
  let last-prime = 2;

  while (last-prime < limit)
    for (x from last-prime ^ 2 to n by last-prime)
      sieve[x] := #f;
    end for;
    block (found-prime)
      for (n from last-prime + 1 below limit)
        if (sieve[n] = #f)
          last-prime := n;
          found-prime()
        end;
      end;
      last-prime := limit;
    end block;
  end while;

  for (x from 2 to n)
    if (sieve[x]) format-out("Prime: %d\n", x); end;
  end;
end;
```


## E

E's standard library doesn't have a step-by-N numeric range, so we'll define one, implementing the standard iteration protocol.

```
def rangeFromBelowBy(start, limit, step) {
  return def stepper {
    to iterate(f) {
      var i := start
      while (i < limit) {
        f(null, i)
        i += step
      }
    }
  }
}
```

The sieve itself:

```
def eratosthenes(limit :(int > 2), output) {
  def composite := [].asSet().diverge()
  for i ? (!composite.contains(i)) in 2..!limit {
    output(i)
    composite.addAll(rangeFromBelowBy(i ** 2, limit, i))
  }
}
```

Example usage:

```
? eratosthenes(12, println)
# stdout: 2
#         3
#         5
#         7
#         11
```


## EasyLang

```mw
len sieve[] 100
max = sqrt len sieve[]
for i = 2 to max
   if sieve[i] = 0
      for j = i * i step i to len sieve[]
         sieve[j] = 1
      .
   .
.
for i = 2 to len sieve[]
   if sieve[i] = 0 : write i & " "
.
print ""
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
```


## eC

```mw
class BitArray : private Array<byte>
{
   uint64 bitSize;

   property uint64 size
   {
      set
      {
         bitSize = value;
         Array::size = (uint)((value + 7) >> 3);
      }
      get { return bitSize; }
   }

   bool check(uint64 n)
   {
      uint b = (uint)(n >> 3), s = (uint)(n & 7);
      return (bool)this[b] & (1 << s);
   }

   void explore(uint64 n)
   {
      uint b = (uint)(n >> 3), s = (uint)n & 7;
      this[b] |= (1 << s);
   }
}

class EratosthenesSieve
{
   BitArray isComposite { };

   uint64 limit;

   void sieve(uint64 limit)
   {
      this.limit = limit;

      if(limit >= 2)
      {
         uint64 i, j, m = (uint64)(sqrt((double)limit) + 0.1);

         isComposite.size = limit + 1;
         isComposite.explore(0);
         isComposite.explore(1);

         for(i = 2; i <= m; i++)
            if(!isComposite.check(i))
               for(j = i * i; j <= limit; j += i)
                  isComposite.explore(j);
      }
      else
         isComposite.Free();
   }

   void printPrimes()
   {
      if(!isComposite.count)
         PrintLn("No primes found within limit (", limit, ").");
      else
      {
         uint64 i, count = 0;

         for(i = 2; i <= limit; i++)
            if(!isComposite.check(i))
            {
               Print(i, " ");
               count++;
            }
         PrintLn("");
         PrintLn(count, " primes found up to ", limit);
      }
   }
}

class SieveOfEratosthenesApp : Application
{
   EratosthenesSieve sieve { };

   void Main()
   {
      sieve.sieve(argc > 1 ? (uint64)strtoull(argv[1], null, 10) : 100);
      sieve.printPrimes();
   }
}
```
