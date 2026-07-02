---
title: "Sieve of Eratosthenes (part 8/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 8/21
---

## Forth

```
: prime? ( n -- ? ) here + c@ 0= ;
: composite! ( n -- ) here + 1 swap c! ;

: sieve ( n -- )
  here over erase
  2
  begin
    2dup dup * >
  while
    dup prime? if
      2dup dup * do
        i composite!
      dup +loop
    then
    1+
  repeat
  drop
  ." Primes: " 2 do i prime? if i . then loop ;

100 sieve
```

**Output:**

```
Primes: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
```

### Alternate Odds-Only, Better Style

The above code is not really very good Forth style as the main initialization, sieving, and output, are all in one `sieve` routine which makes it difficult to understand and refactor; Forth code is normally written in a series of very small routines which makes it easier to understand what is happening on the data stack, since Forth does not have named local re-entrant variable names as most other languages do for local variables (which other languages also normally store local variables on the stack). Also, it uses the `HERE` pointer to user space which points to the next available memory after all compilation is done as a unsized buffer pointer, but as it does not reserve that space for the sieving buffer, it can be changed by other concatenated routines in unexpected ways; better is to allocate the sieving buffer as required from the available space at the time the routines are run and pass that address between concatenated functions until a finalization function frees the memory and clears the stack; this is equivalent to allocating from the "heap" in other languages. The below code demonstrates these ideas:

```mw
: prime? ( addr -- ? ) C@ 0= ; \ test composites array for prime

\ given square index and prime index, u0, sieve the multiples of said prime...
: cullpi! ( u addr u u0 -- u addr u0 )
   DUP DUP + 3 + ROT 4 PICK SWAP \ -- numv addr i prm numv sqri
   DO 2 PICK I + TRUE SWAP C! DUP +LOOP DROP ;

\ process for required prime limit; allocate and initialize returned buffer...
: initsieve ( u -- u a-addr)
   3 - DUP 0< IF 0 ELSE
      1 RSHIFT 1+ DUP ALLOCATE 0<> IF ABORT" Memory allocation error!!!"
      ELSE 2DUP SWAP ERASE THEN
   THEN ;

\ pass through sieving to given index in given buffer address as side effect...
: sieve ( u a-addr -- u a-addr )
   0 \ initialize test index i -- numv bufa i
   BEGIN \ test prime square index < limit
      DUP DUP DUP + SWAP 3 + * 3 + TUCK 4 PICK SWAP > \ sqri = 2*i * (I+3) + 3
   WHILE \ -- numv bufa sqri i
      2 PICK OVER + prime? IF cullpi! \ -- numv bufa i
      ELSE SWAP DROP THEN 1+ \ -- numv bufa ni
   REPEAT 2DROP ; \ -- numv bufa; drop sqri i

\ print primes to given limit...
: .primes ( u a-addr -- )
   OVER 0< IF DROP 2 - 0< IF ( ." No primes!" ) ELSE ( ." Prime:  2" ) THEN
   ELSE ." Primes:  2 " SWAP 0
      DO DUP I + prime? IF I I + 3 + . THEN LOOP FREE DROP THEN ;

\ count number of primes found for number odd numbers within
\ given presumed sieved buffer starting at address...
: countprimes@ ( u a-addr -- )
  SWAP DUP 0< IF 1+ 0< IF DROP 0 ELSE 1 THEN
   ELSE 1 SWAP \ -- bufa cnt numv
      0 DO OVER I + prime? IF 1+ THEN LOOP SWAP FREE DROP
   THEN ;

\ shows counted number of primes to the given limit...
: .countprimesto ( u -- )
   DUP initsieve sieve countprimes@
   CR ." Found " . ." primes Up to the " . ." limit." ;

\ testing the code...
100 initsieve sieve .primes
1000000 .countprimesto
```

**Output:**

```
Primes:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Found 78498 primes Up to the 1000000 limit.
```

As well as solving the stated problems making it much easier to understand and refactor, an odds-only sieve takes half the space and less than half the time.

### Bit-Packing the Sieve Buffer (Odds-Only)

Although the above version resolves many problems of the first version, it is wasteful of memory as each composite number in the sieve buffer is a byte of eight bits representing a boolean value. The memory required can be reduced eight-fold by bit packing the sieve buffer; this will take more "bit-twiddling" to read and write the bits, but reducing the memory used will give better cache assiciativity to larger ranges such that there will be a net gain in performance. This will make the code more complex and the stack manipulations will be harder to write, debug, and maintain, so ANS Forth 1994 provides a local variable naming facility to make this much easier. The following code implements bit-packing of the sieve buffer using local named variables when required:

```mw
\ produces number of one bits in given word...
: numbts ( u -- u ) \ pop count number of bits...
   0 SWAP BEGIN DUP 0<> WHILE SWAP 1+ SWAP DUP 1- AND REPEAT DROP ;

\ constants for variable 32/64 etc. CELL size...
1 CELLS 3 LSHIFT 1- CONSTANT CellMsk
CellMsk numbts CONSTANT CellShft

CREATE bits 8 ALLOT \ bit position Look Up Table...
: mkbts 8 0 DO 1 I LSHIFT I bits + c! LOOP ; mkbts

\ test bit index composites array for prime...
: prime? ( u addr -- ? )
    OVER 3 RSHIFT + C@ SWAP 7 AND bits + C@ AND 0= ;

\ given square index and prime index, u0, sieve the multiples of said prime...
: cullpi! ( u addr u u0 -- u addr u0 )
   DUP DUP + 3 + ROT 4 PICK SWAP \ -- numv addr i prm numv sqri
   DO I 3 RSHIFT 3 PICK + DUP C@ I 7 AND bits + C@ OR SWAP C! DUP +LOOP
   DROP ;

\ initializes sieve storage and parameters
\ given sieve limit, returns bit limit and buffer address ..
: initsieve ( u -- u a-addr )
   3 - \ test limit...
   DUP 0< IF 0 ELSE \ return if number of bits is <= 0!
      1 RSHIFT 1+ \ finish conbersion to number of bits
      DUP 1- CellShft RSHIFT 1+ \ round up to even number of cells
      CELLS DUP ALLOCATE 0= IF DUP ROT ERASE \ set cells0. to zero
      ELSE ABORT" Memory allocation error!!!"
      THEN
   THEN ;

\ pass through sieving to given index in given buffer address as side effect...
: sieve ( u a-addr -- u a-addr )
   0 \ initialize test index i -- numv bufa i
   BEGIN \ test prime square index < limit
      DUP DUP DUP + SWAP 3 + * 3 + TUCK 4 PICK SWAP > \ sqri = 2*i * (I+3) + 3
   WHILE \ -- numv bufa sqri i
      DUP 3 PICK prime? IF cullpi! \ -- numv bufa i
      ELSE SWAP DROP THEN 1+ \ -- numv bufa ni
   REPEAT 2DROP ; \ -- numv bufa; drop sqri i

\ prints already found primes from sieved array...
: .primes ( u a-addr -- )
   SWAP CR ." Primes to " DUP DUP + 2 + 2 MAX . ." are:  "
   DUP 0< IF 1+ 0< IF ." none." ELSE 2 . THEN DROP \ case no primes or just 2
   ELSE 2 . 0 DO I OVER prime? IF I I + 3 + . THEN LOOP FREE DROP
   THEN ;

\ pop count style Look Up Table by 16 bits entry;
\ is a 65536 byte array containing number of zero bits for each index...
CREATE cntLUT16 65536 ALLOT
: mkpop ( u -- u )   numbts 16 SWAP - ;
: initLUT ( -- )   cntLUT16 65536 0 DO I mkpop OVER I + C! LOOP DROP ; initLUT
: popcount@ ( u -- u )
   0 1 CELlS 1 RSHIFT 0
   DO OVER 65535 AND cntLUT16 + C@ + SWAP 16 RSHIFT SWAP LOOP SWAP DROP ;

\ count number of zero bits up to given bits index-1 in array address;
\ params are number of bits used - bits, negative indicates <2/2 out: 0/1,
\ given address is of the allocated bit buffer - bufa;
\ values used: bmsk is bit mask to limit bit in last cell,
\ lci is cell index of last cell used, cnt is the return value...
\ NOTE. this is for little-endian; big-endian needs a byte swap
\ before the last mask and popcount operation!!!
: primecount@ ( u a-addr -- u )
   LOCALS| bufa numb |
   numb 0< IF numb 1+ 0< IF 0 ELSE 1 THEN \ < 3 -> <2/2 -> 0/1!
   ELSE
      numb 1- TO numb \ numb -= 1
      1 \ initial count
      numb CellShft RSHIFT CELLS TUCK \ lci = byte index of CELL including numv
      0 ?DO bufa I + @ popcount@ + 1 CELLS +LOOP \ -- lci cnt
      SWAP bufa + @ \ -- cnt lstCELL
      -2 numb CellMsk AND LSHIFT OR \ bmsk for last CELL -- cnt mskdCELL
      popcount@ + \ add popcount of last masked CELL -- cnt
      bufa FREE DROP \ free bufa -- bmsk cnt lastcell@
   THEN ;

: .countprimesto ( u -- u )
   dup initsieve sieve primecount@
   CR ." There are " . ." primes Up to the " . ." limit." ;

100 initsieve sieve .primes
1000000000 .countprimesto
```

The output of the above code is the same as the previous version, but it takes about two thirds the time while using eight times less memory; it takes about 6.5 seconds on my Intel Skylake i5-6500 at 3.6 GHz (turbo) using swiftForth (32-bit) and about 3.5 seconds on VFX Forth (64-bit), both of which compile to machine code but with the latter much more optimized; gforth-fast is about twice as slow as swiftForth and five times slower then VFX Forth as it just compiles to threaded execution tokens (more like an interpreter).

### Page-Segmented Bit-Packed Odds-Only Version

While the above version does greatly reduce the amount of memory used for a given sieving range and thereby also somewhat reduces execution time; any sieve intended for sieving to limits of a hundred million or more should use a page-segmented implementation; page-segmentation means that only storage for a representation of the base primes up to the square root of the limit plus a sieve buffer that should also be at least proportional to the same square root is required; this will again make the execution faster as ranges go up due to better cache associativity with most memory accesses being within the CPU cache sizes. The following Forth code implements a basic version that does this:

```mw
\ CPU L1 and L2 cache sizes in bits; power of 2...
1 17 LSHIFT CONSTANT L1CacheBits
L1CacheBits 8 * CONSTANT L2CacheBits

\ produces number of one bits in given word...
: numbts ( u -- u ) \ pop count number of bits...
   0 SWAP BEGIN DUP 0<> WHILE SWAP 1+ SWAP DUP 1- AND REPEAT DROP ;

\ constants for variable 32/64 etc. CELL size...
1 CELLS 3 LSHIFT 1- CONSTANT CellMsk
CellMsk numbts CONSTANT CellShft

CREATE bits 8 ALLOT \ bit position Look Up Table...
: mkbts 8 0 DO 1 I LSHIFT I bits + c! LOOP ; mkbts

\ initializes sieve buffer storage and parameters
\ given sieve buffer bit size (even number of CELLS), returns buffer address ..
: initSieveBuffer ( u -- a-addr )
   CellShft RSHIFT \ even number of cells
   CELLS ALLOCATE 0<> IF ABORT" Memory allocation error!!!" THEN ;

\ test bit index composites array for prime...
: prime? ( u addr -- ? )
    OVER 3 RSHIFT + C@ SWAP 7 AND bits + C@ AND 0= ;

\ given square index and prime index, u0, as sell as bitsz,
\ sieve the multiples of said prime leaving prime index on the stack...
: cullpi! ( u u0 u u addr -- u0 )
   LOCALS| sba bitsz lwi | DUP DUP + 3 + ROT \ -- i prm sqri
   \ culling start incdx address calculation...
   lwi 2DUP > IF - ELSE SWAP - OVER MOD DUP 0<> IF OVER SWAP - THEN
   THEN bitsz SWAP \ -- i prm bitsz strti
   DO I 3 RSHIFT sba + DUP C@ I 7 AND bits + C@ OR SWAP C! DUP +LOOP
   DROP ;

\ cull sieve buffer given base wheel index, bit size, 
\ address base prime sieved buffer and
\ the address of the sieve buffer to be culled of composite bits...
: cullSieveBuffer ( u u a-addr a-addr -- )
   >R >R 2DUP + R> R>  \ -- lwi bitsz rngi bpba sba
   LOCALS| sba bpba rngi bitsz lwi |
   bitsz 1- CellShft RSHIFT 1+ CELLS sba SWAP ERASE \ clear sieve buffer
   0 \ initialize base prime index i -- i
   BEGIN \ test prime square index < limit
      DUP DUP DUP + SWAP 3 + * 3 + TUCK rngi < \ sqri = 2*i * (I+3) + 3
   WHILE \ -- sqri i
      DUP bpba prime? IF lwi bitsz sba cullpi! ELSE SWAP DROP THEN \ -- i     
   1+ REPEAT 2DROP ; \ --

\ pop count style Look Up Table by 16 bits entry;
\ is a 65536 byte array containing number of zero bits for each index...
CREATE cntLUT16 65536 ALLOT
: mkpop ( u -- u )   numbts 16 SWAP - ;
: initLUT ( -- )   cntLUT16 65536 0 DO I mkpop OVER I + C! LOOP DROP ; initLUT
: popcount@ ( u -- u )
   0 1 CELlS 1 RSHIFT 0
   DO OVER 65535 AND cntLUT16 + C@ + SWAP 16 RSHIFT SWAP LOOP SWAP DROP ;

\ count number of zero bits up to given bits index in array address...
: countSieveBuffer@ ( u a-addr -- u )
   LOCALS| bufa lmti |
   0 \ initial count -- cnt
   lmti CellShft RSHIFT CELLS TUCK \ lci = byte index of CELL including numv
   0 ?DO bufa I + @ popcount@ + 1 CELLS +LOOP \ -- lci cnt
   SWAP bufa + @ \ -- cnt lstCELL
   -2 lmti CellMsk AND LSHIFT OR \ bmsk for last CELL -- cnt mskdCELL
   popcount@ + ; \ add popcount of last masked CELL -- cnt

\ prints found primes from series of culled sieve buffers...
: .primes ( u -- )
   DUP CR ." Primes to " . ." are:  "
   DUP 3 - 0< IF DUP 2 - 0< IF ." none." ELSE 2 . THEN \ <2/2 -> 0/1
   ELSE 2 .
      3 - 1 RSHIFT 1+ \ -- rngi
      DUP 1- L2CacheBits / L2CacheBits * 3 RSHIFT \ -- rng rngi pglmtbytes
      L1CacheBits initSieveBuffer \ address of base prime sieve buffer
      L2CacheBits initSieveBuffer \ address of main sieve buffer
      LOCALS| sba bpsba pglmt | \ local variables -- rngi
      0 OVER L1CacheBits MIN bpsba bpsba cullSieveBuffer
      pglmt 0 ?DO
         I L2CacheBits bpsba sba cullSieveBuffer
         I L2CacheBits 0 DO I sba prime? IF DUP I + DUP + 3 + . THEN LOOP DROP
      L2CacheBits +LOOP \ rngi
      L2CacheBits mod DUP 0> IF \ one more page!
         pglmt DUP L2CacheBits bpsba sba cullSieveBuffer
         SWAP 0 DO I sba prime? IF DUP I + DUP + 3 + . THEN LOOP DROP
      THEN bpsba FREE DROP sba FREE DROP
   THEN ; \ --

\ prints count of found primes from series of culled sieve buffers...
: .countPrimesTo ( u -- )
   DUP 3 - 0< IF 2 - 0< IF 0 ELSE 1 THEN \ < 3 -> <2/2 -> 0/1!
   ELSE
      DUP 3 - 1 RSHIFT 1+
      DUP 1- L2CacheBits / L2CacheBits * \ -- rng rngi pglmtbytes
      L1CacheBits initSieveBuffer \ address of base prime sieve buffer
      L2CacheBits initSieveBuffer \ address of main sieve buffer
      LOCALS| sba bpsba pglmt | \ local variables -- rng rngi
      0 OVER L1CacheBits MIN bpsba bpsba cullSieveBuffer
      1 pglmt 0 ?DO
         I L2CacheBits bpsba sba cullSieveBuffer
         L2CacheBits 1- sba countSieveBuffer@ +
      L2CacheBits +LOOP \ rng rngi cnt
      SWAP L2CacheBits mod DUP 0> IF \ one more page!
         pglmt OVER bpsba sba cullSieveBuffer
         1- sba countSieveBuffer@ + \ partial count!
      THEN
      bpsba FREE DROP sba FREE DROP \ -- range cnt
   THEN CR ." There are " . ." primes Up to the " . ." limit." ;

100 .primes
1000000000 .countPrimesTo
```

**Output:**

```
Primes to 100 are:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
There are 50847534 primes Up to the 1000000000 limit.
```

For simplicity, the base primes array is left as a sieved bit packed array (which takes minimum space) at the cost of having to scan the bit array for base primes on every page-segment culling pass. The page-segment sieve buffer is set as a fixed multiple of this (intended to fit within the CPU L2 cache size) in order to reduce the base prime start index address calculation overhead by this factor at the cost of slightly increased memory access times, which access times are still only about the same as the fastest inner culling time or less anyway. When the cache sizes are set to the 32 Kilobyte/256 Kilobyte size for L1/L2, respectively, by changing `1 18 LSHIFT CONSTANT L1CacheBits`) as for my Intel Skylake i5-6500 at 3.6 GHz (single-threaded turbo), it runs in about 1.25 seconds on 64-bit VFX Forth, 3.75 seconds on 32-bit swiftForth, and 12.4 seconds on 64-bit gforth-fast, obviously with the tuned in-lined machine language compiling of VFX Forth much faster than the threaded execution token interpreting of gforth and with swiftForth lacking the machine code inlining of VFX Forth.

VFX Forth is only about 25 % slower than the algorithm as written in the fastest of languages, just as they advertise.

As written, the algorithm works efficiently up to over ten billion (1e10) with 64-bit systems, but could easily be refactored to use floating point or double precision for inputs and outputs as I have done in a StackOverflow answer in JavaScript without costing much in execution time so 32-bit systems would have the much higher limit.

The implementation is efficient up to this range, but with a change so that the base primes array can grow with increasing limit, can sieve to much higher ranges with a loss of efficiency in unused base prime start address calculations that can't be used as the culling spans exceed the fixed sieve buffer size. Again, this can be solved by also making the page-segmentation sieve buffer grow as the square root of the limit.

Further improvements by a factor of almost four in overall execution speed would be gained by implementing maximum wheel-factorization as per my other StackOverflow JavaScript answer, which also effectively increases sieve buffer sizes by a factor of 48 in sieving by modulo residual bit planes.

Finally, multi-processing could be applied to increase the execution speed by about the number of effective cores (non SMT - Hyper Threads) as in four on my Skylake machine; however, neither the 1994 ANS Forth standard nor the 2012 standard has a standard Forth way of implementing this so each of the implementations use their own custom WORDS; since the resulting code would not be cross-implementation, I am not going to do this.

I likely won't even add the Maximum Wheel-Factorized version as in the above linked JavaScript code, since this code is enough to demonstrate what I was going to show: that Forth can be an efficient language, albeit a little hard to code, read, and maintain due to the reliance on anonymous data stack operations; it is a language whose best use is likely in cross-compiling to embedded systems where it can easily be customized and extended as required, and because it doesn't actually require a base operating system, can use its core facilities, functions, and extensions in place of such an OS to result in a minimum memory footprint.


## Fortran

Works with

:

Fortran

version 77

```mw
      PROGRAM MAIN
      INTEGER LI
      WRITE (6,100)
      READ  (5,110) LI
      call SOE(LI)
 100  FORMAT( 'Limit:' )
 110  FORMAT( I4 )
      STOP
      END
      
C --- SIEVE OF ERATOSTHENES ----------
      SUBROUTINE SOE( LI )
      INTEGER LI
      LOGICAL A(LI)
      INTEGER SL,P,I
      
      DO 10 I=1,LI
         A(I) = .TRUE.
 10   CONTINUE
      
      SL = INT(SQRT(REAL(LI)))
      A(1) = .FALSE.
      DO 30 P=2,SL
         IF ( .NOT. A(P) ) GOTO 30
         DO 20 I=P*P,LI,P
            A(I)=.FALSE.
 20      CONTINUE
 30   CONTINUE

      DO 40 I=2,LI
         IF ( A(I) ) WRITE(6,100) I
 40   CONTINUE

 100  FORMAT(I3)
      RETURN
      END
```

Works with

:

Fortran

version 90 and later

```mw
program sieve

  implicit none
  integer, parameter :: i_max = 100
  integer :: i
  logical, dimension (i_max) :: is_prime

  is_prime = .true.
  is_prime (1) = .false.
  do i = 2, int (sqrt (real (i_max)))
    if (is_prime (i)) is_prime (i * i : i_max : i) = .false.
  end do
  do i = 1, i_max
    if (is_prime (i)) write (*, '(i0, 1x)', advance = 'no') i
  end do
  write (*, *)

end program sieve
```

Output:

```mw
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

Because it uses four byte logical's (default size) as elements of the sieve buffer, the above code uses 400 bytes of memory for this trivial task of sieving to 100; it also has 49 + 31 + 16 + 8 = 104 (for the culling by the primes of two, three, five, and seven) culling operations.

**Optimised using a pre-computed wheel based on 2:**

```mw
program sieve_wheel_2

  implicit none
  integer, parameter :: i_max = 100
  integer :: i
  logical, dimension (i_max) :: is_prime

  is_prime = .true.
  is_prime (1) = .false.
  is_prime (4 : i_max : 2) = .false.
  do i = 3, int (sqrt (real (i_max))), 2
    if (is_prime (i)) is_prime (i * i : i_max : 2 * i) = .false.
  end do
  do i = 1, i_max
    if (is_prime (i)) write (*, '(i0, 1x)', advance = 'no') i
  end do
  write (*, *)

end program sieve_wheel_2
```

Output:

```mw
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

This so-called "optimized" version still uses 400 bytes of memory but slightly reduces to 74 operations from 104 operations including the initialization of marking all of the even representations as composite due to skipping the re-culling of the even representation, so isn't really much of an optimization at all!

**Optimized using a proper implementation of a wheel 2:**

The above implementations, especially the second odds-only code, are some of the most inefficient versions of the Sieve of Eratosthenes in any language here as to time and space efficiency, only worse by some naive JavaScript implementations that use eight-byte Number's as logical values; the second claims to be wheel factorized but still uses all the same memory as the first and still culls by the even numbers in the initialization of the sieve buffer. As well, using four bytes (default logical size) to store a boolean value is terribly wasteful if these implementations were to be extended to non-toy ranges. The following code implements proper wheel factorization by two, reducing the space used by a factor of about eight to 49 bytes by using `byte` as the sieve buffer array elements and not requiring the evens initialization, thus reducing the number of operations to 16 + 8 + 4 = 28 (for the culling primes of three, five, and seven) culling operations:

```mw
program sieve_wheel_2
 
  implicit none
  integer, parameter :: i_max = 100
  integer, parameter :: i_limit = (i_max - 3) / 2
  integer :: i
  byte, dimension (0:i_limit) :: composites
 
  composites = 0
  do i = 0, (int (sqrt (real (i_max))) - 3) / 2
    if (composites(i) == 0) composites ((i + i) * (i + 3) + 3 : i_limit : i + i + 3) = 1.
  end do
  write (*, '(i0, 1x)', advance = 'no') 2
  do i = 0, i_limit
    if (composites (i) == 0) write (*, '(i0, 1x)', advance = 'no') (i + i + 3)
  end do
  write (*, *)
 
end program sieve_wheel_2
```

The output is the same as the earlier version.

**Optimized using bit packing to reduce the memory use by a further factor of eight:**

The above implementation is still space inefficient in effectively only using one bit out of eight; the following version implements bit packing to reduce memory use by a factor of eight by using bits to represent composite numbers rather than bytes:

```mw
program sieve_wheel_2
 
  implicit none
  integer, parameter :: i_max = 10000000
  integer, parameter :: i_range = (i_max - 3) / 2
  integer :: i, j, k, cnt
  byte, dimension (0:i_range / 8) :: composites
 
  composites = 0 ! pre-initialized?
  do i = 0, (int (sqrt (real (i_max))) - 3) / 2
    if (iand(composites(shiftr(i, 3)), shiftl(1, iand(i, 7))) == 0) then
      do j = (i + i) * (i + 3) + 3, i_range, i + i + 3
        k = shiftr(j, 3)
        composites(k) = ior(composites(k), shiftl(1, iand(j, 7)))
      end do
    end if
  end do
!  write (*, '(i0, 1x)', advance = 'no') 2
  cnt = 1
  do i = 0, i_range
    if (iand(composites(shiftr(i, 3)), shiftl(1, iand(i, 7))) == 0) then
!      write (*, '(i0, 1x)', advance = 'no') (i + i + 3)
      cnt = cnt + 1
    end if
  end do
!  write (*, *)
  print '(a, i0, a, i0, a, f0.0, a)', &
        'There are ', cnt, ' primes up to ', i_max, '.'
end program sieve_wheel_2
```

**Output:**

```
There are 664579 primes up to 10000000.
```

When the lines to print the results are enabled, the output to a maximum value of 100 is still exactly the same as the other versions, and it has exactly the same number of culling operations as the immediately above optimized version for the same range; the only difference is that less memory is used. Although the culling operations are somewhat more complex, for larger ranges the time saved in better cache associativity due to more effective use of the cache more than makes up for it so average culling time is actually reduced, so that this version can count the number of primes to several million (it takes a lot of time to list hundreds of thousands of primes, but counting is faster) in a few tens of milliseconds. For ranges above a few tens of millions, a page-segmented sieve is much more efficient due to further improved use of the CPU caches.

### Multi-Threaded Page-Segmented Bit-Packed Odds-Only Version

As well as adding page-segmentation, the following code adds multi-processing which is onc of the capabilities for which modern Fortran is known:

```mw
subroutine cullSieveBuffer(lwi, size, bpa, sba)

    implicit none
    integer, intent(in) :: lwi, size
    byte, intent(in) :: bpa(0:size - 1)
    byte, intent(out) :: sba(0:size - 1)
    integer :: i_limit, i_bitlmt, i_bplmt, i, sqri, bp, si, olmt, msk, j
    byte, dimension (0:7) :: bits
    common /twiddling/ bits
    
    i_bitlmt = size * 8 - 1
    i_limit = lwi + i_bitlmt
    i_bplmt = size / 4
    sba = 0
    i = 0
    sqri = (i + i) * (i + 3) + 3
    do while (sqri <= i_limit)
      if (iand(int(bpa(shiftr(i, 3))), shiftl(1, iand(i, 7))) == 0) then
        ! start index address calculation...
        bp = i + i + 3
        if (lwi <= sqri) then
          si = sqri - lwi
        else
          si = mod((lwi - sqri), bp)
          if (si /= 0) si = bp - si
        end if
        if (bp <= i_bplmt) then
          olmt = min(i_bitlmt, si + bp * 8 - 1)
          do while (si <= olmt)
            msk = bits(iand(si, 7))
            do j = shiftr(si, 3), size - 1, bp
              sba(j) = ior(int(sba(j)), msk)
            end do
            si = si + bp
          end do
        else
          do while (si <= i_bitlmt)
            j = shiftr(si, 3)
            sba(j) = ior(sba(j), bits(iand(si, 7)))
            si = si + bp
          end do
        end if
      end if
      i = i + 1
      sqri = (i + i) * (i + 3) + 3
    end do
  
  end subroutine cullSieveBuffer
  
  integer function countSieveBuffer(lmti, almti, sba)
  
    implicit none
    integer, intent(in) :: lmti, almti
    byte, intent(in) :: sba(0:almti)
    integer :: bmsk, lsti, i, cnt
    byte, dimension (0:65535) :: clut
    common /counting/ clut
  
    cnt = 0
    bmsk = iand(shiftl(-2, iand(lmti, 15)), 65535)
    lsti = iand(shiftr(lmti, 3), -2)
    do i = 0, lsti - 1, 2
      cnt = cnt + clut(shiftl(iand(int(sba(i)), 255), 8) + iand(int(sba(i + 1)), 255))
    end do
    countSieveBuffer = cnt + clut(ior(shiftl(iand(int(sba(lsti)), 255), 8) + iand(int(sba(lsti + 1)), 255), bmsk))
    
  end function countSieveBuffer
  
  program sieve_paged
  
    use OMP_LIB
    implicit none
    integer, parameter :: i_max = 1000000000, i_range = (i_max - 3) / 2
    integer, parameter :: i_l1cache_size = 16384, i_l1cache_bitsz = i_l1cache_size * 8
    integer, parameter :: i_l2cache_size = i_l1cache_size * 8, i_l2cache_bitsz = i_l2cache_size * 8
    integer :: cr, c0, c1, i, j, k, cnt
    integer, save :: scnt
    integer :: countSieveBuffer
    integer :: numthrds
    byte, dimension (0:i_l1cache_size - 1) :: bpa
    byte, save, allocatable, dimension (:) :: sba
    byte, dimension (0:7) :: bits = (/ 1, 2, 4, 8, 16, 32, 64, -128 /)
    byte, dimension (0:65535) :: clut
    common /twiddling/ bits
    common /counting/ clut
  
    type heaparr
      byte, allocatable, dimension(:) :: thrdsba
    end type heaparr
    type(heaparr), allocatable, dimension (:) :: sbaa
  
    !$OMP THREADPRIVATE(scnt, sba)
  
    numthrds = 1
    !$ numthrds = OMP_get_max_threads()
    allocate(sbaa(0:numthrds - 1))
    do i = 0, numthrds - 1
      allocate(sbaa(i)%thrdsba(0:i_l2cache_size - 1))
    end do
  
    CALL SYSTEM_CLOCK(count_rate=cr)
    CALL SYSTEM_CLOCK(c0)
    do k = 0, 65535 ! initialize counting Look Up Table
      j = k
      i = 16
      do while (j > 0)
        i = i - 1
        j = iand(j, j - 1)
      end do
      clut(k) = i
    end do
    bpa = 0 ! pre-initialization not guaranteed!
    call cullSieveBuffer(0, i_l1cache_size, bpa, bpa)
  
    cnt = 1
    !$OMP PARALLEL DO ORDERED
      do i = i_l2cache_bitsz, i_range, i_l2cache_bitsz * 8
        scnt = 0
        sba = sbaa(mod(i, numthrds))%thrdsba
        do j = i, min(i_range, i + 8 * i_l2cache_bitsz - 1), i_l2cache_bitsz
          call cullSieveBuffer(j - i_l2cache_bitsz, i_l2cache_size, bpa, sba)
          scnt = scnt + countSieveBuffer(i_l2cache_bitsz - 1, i_l2cache_size, sba)
        end do
        !$OMP ATOMIC
          cnt = cnt + scnt
      end do
    !$OMP END PARALLEL DO
  
    j = i_range / i_l2cache_bitsz * i_l2cache_bitsz
    k = i_range - j
    if (k /= i_l2cache_bitsz - 1) then
      call cullSieveBuffer(j, i_l2cache_size, bpa, sbaa(0)%thrdsba)
      cnt = cnt + countSieveBuffer(k, i_l2cache_size, sbaa(0)%thrdsba)
    end if
  !  write (*, '(i0, 1x)', advance = 'no') 2
  !  do i = 0, i_range
  !    if (iand(sba(shiftr(i, 3)), bits(iand(i, 7))) == 0) write (*, '(i0, 1x)', advance='no') (i + i + 3)
  !  end do
  !  write (*, *)
    CALL SYSTEM_CLOCK(c1)
    print '(a, i0, a, i0, a, f0.0, a)', 'Found ', cnt, ' primes up to ', i_max, &
          ' in ', ((c1 - c0) / real(cr) * 1000), ' milliseconds.'
  
    do i = 0, numthrds - 1
      deallocate(sbaa(i)%thrdsba)
    end do
    deallocate(sbaa)
  
  end program sieve_paged
```

**Output:**

```
Found 50847534 primes up to 1000000000 in 219. milliseconds.
```

The above output was as compiled with gfortran -O3 -fopenmp using version 11.1.1-1 on my Intel Skylake i5-6500 CPU at 3.2 GHz multithreaded with four cores. There are a few more optimizations that could be made in applying Maximum Wheel-Factorization as per my StackOverflow answer in JavaScript, which will make this almost four times faster yet again. If that optimization were done, sieving to a billion as here is really too trivial to measure and one should sieve at least up to ten billion to start to get a long enough time to be measured accurately. As explained in that answer, the Maximum Wheel-Factorized code will work efficiently up to about a trillion (1e12), when it needs yet another "bucket sieve" optimization to allow it to continue to scale efficiently for increasing range. The final optimization which can speed up the code by almost a factor of two is a very low level loop unrolling technique that I'm not sure will work with the compiler, but as it works in C/C++ and other similar languages including those that compile through LLVM, it ought to.


## Free Pascal

### Basic version

function Sieve returns a list of primes less than or equal to the given aLimit

```mw
program prime_sieve;
{$mode objfpc}{$coperators on}
uses
  SysUtils, GVector;
type
  TPrimeList = specialize TVector<DWord>;
function Sieve(aLimit: DWord): TPrimeList;
var
  IsPrime: array of Boolean;
  I, SqrtBound: DWord;
  J: QWord;
begin
  Result := TPrimeList.Create;
  Inc(aLimit, Ord(aLimit < High(DWord))); //not a problem because High(DWord) is composite
  SetLength(IsPrime, aLimit);
  FillChar(Pointer(IsPrime)^, aLimit, Byte(True));
  SqrtBound := Trunc(Sqrt(aLimit));
  for I := 2 to aLimit do
    if IsPrime[I] then
      begin
        Result.PushBack(I);
        if I <= SqrtBound then
          begin
            J := I * I;
            repeat
              IsPrime[J] := False;
              J += I;
            until J > aLimit;
          end;
      end;
end;

 //usage

var
  Limit: DWord = 0;
function ReadLimit: Boolean;
var
  Lim: Int64;
begin
  if (ParamCount = 1) and Lim.TryParse(ParamStr(1), Lim) then
    if (Lim >= 0) and (Lim <= High(DWord)) then
      begin
        Limit := DWord(Lim);
        exit(True);
      end;
  Result := False;
end;
procedure PrintUsage;
begin
  WriteLn('Usage: prime_sieve Limit');
  WriteLn('  where Limit in the range [0, ', High(DWord), ']');
  Halt;
end;
procedure PrintPrimes(aList: TPrimeList);
var
  I: DWord;
begin
  if aList.Size <> 0 then begin
    if aList.Size > 1 then
      for I := 0 to aList.Size - 2 do
        Write(aList[I], ', ');
    WriteLn(aList[aList.Size - 1]);
  end;
  aList.Free;
end;
begin
  if not ReadLimit then
    PrintUsage;
  try
    PrintPrimes(Sieve(Limit));
  except
    on e: Exception do
      WriteLn('An exception ', e.ClassName, ' occurred with message: ', e.Message);
  end;
end.
```

### Alternative segmented(odds only) version

function OddSegmentSieve returns a list of primes less than or equal to the given aLimit

```mw
program prime_sieve;
{$mode objfpc}{$coperators on}
uses
  SysUtils, Math;
type
  TPrimeList = array of DWord;
function OddSegmentSieve(aLimit: DWord): TPrimeList;
  function EstimatePrimeCount(aLimit: DWord): DWord;
  begin
    case aLimit of
      0..1:   Result := 0;
      2..200: Result := Trunc(1.6 * aLimit/Ln(aLimit)) + 1;
    else
      Result := Trunc(aLimit/(Ln(aLimit) - 2)) + 1;
    end;
  end;
  function Sieve(aLimit: DWord; aNeed2: Boolean): TPrimeList;
  var
    IsPrime: array of Boolean;
    I: DWord = 3;
    J, SqrtBound: DWord;
    Count: Integer = 0;
  begin
    if aLimit < 2 then
      exit(nil);
    SetLength(IsPrime, (aLimit - 1) div 2);
    FillChar(Pointer(IsPrime)^, Length(IsPrime), Byte(True));
    SetLength(Result, EstimatePrimeCount(aLimit));
    SqrtBound := Trunc(Sqrt(aLimit));
    if aNeed2 then
      begin
        Result[0] := 2;
        Inc(Count);
      end;
    for I := 0 to High(IsPrime) do
      if IsPrime[I] then
        begin
          Result[Count] := I * 2 + 3;
          if Result[Count] <= SqrtBound then
            begin
              J := Result[Count] * Result[Count];
              repeat
                IsPrime[(J - 3) div 2] := False;
                J += Result[Count] * 2;
              until J > aLimit;
            end;
          Inc(Count);
        end;
    SetLength(Result, Count);
  end;
const
  PAGE_SIZE = $8000;
var
  IsPrime: array[0..Pred(PAGE_SIZE)] of Boolean; //current page
  SmallPrimes: TPrimeList = nil;
  I: QWord;
  J, PageHigh, Prime: DWord;
  Count: Integer;
begin
  if aLimit < PAGE_SIZE div 4 then
    exit(Sieve(aLimit, True));
  I := Trunc(Sqrt(aLimit));
  SmallPrimes := Sieve(I + 1, False);
  Count := Length(SmallPrimes) + 1;
  I += Ord(not Odd(I));
  SetLength(Result, EstimatePrimeCount(aLimit));
  while I <= aLimit do
    begin
      PageHigh := Min(Pred(PAGE_SIZE * 2), aLimit - I);
      FillChar(IsPrime, PageHigh div 2 + 1, Byte(True));
      for Prime in SmallPrimes do
        begin
          J := DWord(I) mod Prime;
          if J <> 0 then
            J := Prime shl (1 - J and 1) - J;
          while J <= PageHigh do
            begin
              IsPrime[J div 2] := False;
              J += Prime * 2;
            end;
        end;
      for J := 0 to PageHigh div 2 do
        if IsPrime[J] then
          begin
            Result[Count] := J * 2 + I;
            Inc(Count);
          end;
      I += PAGE_SIZE * 2;
    end;
  SetLength(Result, Count);
  Result[0] := 2;
  Move(SmallPrimes[0], Result[1], Length(SmallPrimes) * SizeOf(DWord));
end;

  //usage

var
  Limit: DWord = 0;
function ReadLimit: Boolean;
var
  Lim: Int64;
begin
  if (ParamCount = 1) and Lim.TryParse(ParamStr(1), Lim) then
    if (Lim >= 0) and (Lim <= High(DWord)) then
      begin
        Limit := DWord(Lim);
        exit(True);
      end;
  Result := False;
end;
procedure PrintUsage;
begin
  WriteLn('Usage: prime_sieve Limit');
  WriteLn('  where Limit in the range [0, ', High(DWord), ']');
  Halt;
end;
procedure PrintPrimes(const aList: TPrimeList);
var
  I: DWord;
begin
  for I := 0 to Length(aList) - 2 do
    Write(aList[I], ', ');
  if aList <> nil then
    WriteLn(aList[High(aList)]);
end;
begin
  if not ReadLimit then
    PrintUsage;
  PrintPrimes(OddSegmentSieve(Limit));
end.
```


## FreeBASIC

```mw
' FB 1.05.0

Sub sieve(n As Integer)
  If n < 2 Then Return
  Dim a(2 To n) As Integer
  For i As Integer = 2 To n : a(i) = i : Next
  Dim As Integer p = 2, q
  ' mark non-prime numbers by setting the corresponding array element to 0
  Do
    For j As Integer = p * p To n Step p
      a(j) = 0
    Next j
    ' look for next non-zero element in array after 'p'
    q = 0
    For j As Integer = p + 1 To Sqr(n)
      If a(j) <> 0 Then
        q = j
        Exit For
      End If
    Next j    
    If q = 0 Then Exit Do
    p = q
  Loop

  ' print the non-zero numbers remaining i.e. the primes
  For i As Integer = 2 To n
    If a(i) <> 0 Then
      Print Using "####"; a(i);      
    End If
  Next
  Print
End Sub

Print "The primes up to 1000 are :"
Print
sieve(1000)
Print
Print "Press any key to quit"
Sleep
```

**Output:**

```
The primes up to 1000 are :

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


## Frink

```mw
n = eval[input["Enter highest number: "]]
results = array[sieve[n]]
println[results]
println[length[results] + " prime numbers less than or equal to " + n]

sieve[n] :=
{
   // Initialize array
   array = array[0 to n]
   array@1 = 0

   for i = 2 to ceil[sqrt[n]]
      if array@i != 0
         for j = i^2 to n step i
            array@j = 0

   return select[array, { |x| x != 0 }]
}
```


## Furor

*Note: With benchmark function*

```mw
tick sto startingtick
#g 100000 sto MAX
@MAX mem !maximize sto primeNumbers
one count
@primeNumbers 0 2 [^]
2 @MAX külső: {||
@count {|
{}§külső {} []@primeNumbers !/ else{<}§külső
|} // @count vége
@primeNumbers @count++ {} [^]
|} // @MAX vége
@primeNumbers free
."Time : " tick @startingtick - print ." tick\n"
."Prímek száma = " @count printnl
end
{ „MAX” } { „startingtick” } { „primeNumbers” } { „count” }
```


## Peri

*Note: With benchmark function*

```mw
###sysinclude standard.uh
tick sto startingtick
#g 100000 sto MAX
@MAX mem !maximize sto primeNumbers
one count
2 0 sto#s primeNumbers
2 @MAX külső: {{ ,
@count {{
{{}}§külső primeNumbers[{{}}] !/ else {{<}}§külső
}} // @count vége
//{{}} gprintnl  // A talált prímszám kiiratásához kommentezzük ki e sort
{{}} @count++ sto#s primeNumbers
}} // @MAX vége
@primeNumbers inv mem
//."Time : " tick @startingtick - print ." tick\n"
."Prímek száma = " @count printnl
end
{ „MAX” } { „startingtick” } { „primeNumbers” } { „count” }
```


## FutureBasic

### Basic sieve of array of booleans

```mw
window 1, @"Sieve of Eratosthenes", (0,0,720,300)

begin globals
dynamic gPrimes(1) as Boolean
end globals

local fn SieveOfEratosthenes( n as long )
  long i, j
  
  for i = 2 to  n
    for j = i * i to n step i
      gPrimes(j) = _true
    next
    if gPrimes(i) = 0 then print i,
  next i
  kill gPrimes
end fn

fn SieveOfEratosthenes( 100 )

HandleEvents
```

Output:

```
 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Fōrmulæ

Fōrmulæ programs are not textual, visualization/edition of programs is done showing/manipulating structures but not text. Moreover, there can be multiple visual representations of the same program. Even though it is possible to have textual representation —i.e. XML, JSON— they are intended for storage and transfer purposes more than visualization and edition.

Programs in Fōrmulæ are created/edited online in its website.

In **this page** you can see and run the program(s) related to this task and their results. You can also change either the programs or the parameters they are called with, for experimentation, but remember that these programs were created with the main purpose of showing a clear solution of the task, and they generally lack any kind of validation.

**Solution**

**Test case**


## GAP

```mw
Eratosthenes := function(n)
    local a, i, j;
    a := ListWithIdenticalEntries(n, true);
    if n < 2 then
        return [];
    else
        for i in [2 .. n] do
            if a[i] then
                j := i*i;
                if j > n then
                    return Filtered([2 .. n], i -> a[i]);
                else
                    while j <= n do
                        a[j] := false;
                        j := j + i;
                    od;
                fi;
            fi;
        od;
    fi;
end;

Eratosthenes(100);

[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
```


## GLBasic

```mw
// Sieve of Eratosthenes (find primes)
// GLBasic implementation

GLOBAL n%, k%, limit%, flags%[]
 
limit = 100       // search primes up to this number

DIM flags[limit+1]      // GLBasic arrays start at 0
 
FOR n = 2 TO SQR(limit)
    IF flags[n] = 0
        FOR k = n*n TO limit STEP n
            flags[k] = 1
        NEXT
    ENDIF
NEXT
 
// Display the primes
FOR n = 2 TO limit
    IF flags[n] = 0 THEN STDOUT n + ", "
NEXT

KEYWAIT
```
