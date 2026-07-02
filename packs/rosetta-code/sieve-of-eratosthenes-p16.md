---
title: "Sieve of Eratosthenes (part 16/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 16/21
---

## Perl

For highest performance and ease, typically a module would be used, such as Math::Prime::Util, Math::Prime::FastSieve, or Math::Prime::XS.

### Classic Sieve

```mw
sub sieve {
  my $n = shift;
  my @composite;
  for my $i (2 .. int(sqrt($n))) {
    if (!$composite[$i]) {
      for (my $j = $i*$i; $j <= $n; $j += $i) {
        $composite[$j] = 1;
      }
    }
  }
  my @primes;
  for my $i (2 .. $n) {
    $composite[$i] || push @primes, $i;
  }
  @primes;
}
```

### Odds only (faster)

```mw
sub sieve2 {
  my($n) = @_;
  return @{([],[],[2],[2,3],[2,3])[$n]} if $n <= 4;

  my @composite;
  for (my $t = 3;  $t*$t <= $n;  $t += 2) {
     if (!$composite[$t]) {
        for (my $s = $t*$t;  $s <= $n;  $s += $t*2)
           { $composite[$s]++ }
     }
  }
  my @primes = (2);
  for (my $t = 3;  $t <= $n;  $t += 2) { 
     $composite[$t] || push @primes, $t;
  }
  @primes;
}
```

### Odds only, using vectors for lower memory use

```mw
sub dj_vector {
  my($end) = @_;
  return @{([],[],[2],[2,3],[2,3])[$end]} if $end <= 4;
  $end-- if ($end & 1) == 0; # Ensure end is odd

  my ($sieve, $n, $limit, $s_end) = ( '', 3, int(sqrt($end)), $end >> 1 );
  while ( $n <= $limit ) {
    for (my $s = ($n*$n) >> 1; $s <= $s_end; $s += $n) {
      vec($sieve, $s, 1) = 1;
    }
    do { $n += 2 } while vec($sieve, $n >> 1, 1) != 0;
  }
  my @primes = (2);
  do { push @primes, 2*$_+1 if !vec($sieve,$_,1) } for (1..int(($end-1)/2));
  @primes;
}
```

### Odds only, using strings for best performance

Compared to array versions, about 2x faster (with 5.16.0 or later) and lower memory. Much faster than the experimental versions below. It's possible a mod-6 or mod-30 wheel could give more improvement, though possibly with obfuscation. The best next step for performance and functionality would be segmenting.

```mw
sub string_sieve {
  my ($n, $i, $s, $d, @primes) = (shift, 7);

  local $_ = '110010101110101110101110111110' .
             '101111101110101110101110111110' x ($n/30);

  until (($s = $i*$i) > $n) {
    $d = $i<<1;
    do { substr($_, $s, 1, '1') } until ($s += $d) > $n;
    1 while substr($_, $i += 2, 1);
  }
  $_ = substr($_, 1, $n); 
  # For just the count:  return ($_ =~ tr/0//);
  push @primes, pos while m/0/g;
  @primes;
}
```

This older version uses half the memory, but at the expense of a bit of speed and code complexity:

```mw
sub dj_string {
  my($end) = @_;
  return @{([],[],[2],[2,3],[2,3])[$end]} if $end <= 4;
  $end-- if ($end & 1) == 0;
  my $s_end = $end >> 1;

  my $whole = int( ($end>>1) / 15);    # prefill with 3 and 5 marked
  my $sieve = '100010010010110' . '011010010010110' x $whole;
  substr($sieve, ($end>>1)+1) = '';
  my ($n, $limit, $s) = ( 7, int(sqrt($end)), 0 );
  while ( $n <= $limit ) {
    for ($s = ($n*$n) >> 1; $s <= $s_end; $s += $n) {
      substr($sieve, $s, 1) = '1';
    }
    do { $n += 2 } while substr($sieve, $n>>1, 1);
  }
  # If you just want the count, it's very fast:
  #       my $count = 1 + $sieve =~ tr/0//;
  my @primes = (2);
  push @primes, 2*pos($sieve)-1 while $sieve =~ m/0/g;
  @primes;
}
```

### Experimental

These are examples of golfing or unusual styles.

Golfing a bit, at the expense of speed:

```mw
sub sieve{ my (@s, $i);
   grep { not $s[ $i  = $_ ] and do
       { $s[ $i += $_ ]++ while $i <= $_[0]; 1 }
   } 2..$_[0]
}

print join ", " => sieve 100;
```

Or with bit strings (much slower than the vector version above):

```mw
sub sieve{ my ($s, $i);
   grep { not vec $s, $i  = $_, 1 and do 
      { (vec $s, $i += $_, 1) = 1 while $i <= $_[0]; 1 }
   } 2..$_[0]
}

print join ", " => sieve 100;
```

A short recursive version:

```mw
sub erat {
    my $p = shift;
    return $p, $p**2 > $_[$#_] ? @_ : erat(grep $_%$p, @_)
}

print join ', ' => erat 2..100000;
```

Regexp (purely an example -- the regex engine limits it to only 32769):

```mw
sub sieve {
   my ($s, $p) = "." . ("x" x shift);

   1 while ++$p
      and $s =~ /^(.{$p,}?)x/g
      and $p = length($1)
      and $s =~ s/(.{$p})./${1}./g
      and substr($s, $p, 1) = "x";
   $s
}

print sieve(1000);
```

### Extensible sieves

Here are two incremental versions, which allows one to create a tied array of primes:

```mw
use strict;
use warnings;
package Tie::SieveOfEratosthenes;

sub TIEARRAY {
   my $class = shift;
   bless \$class, $class;
}

# If set to true, produces copious output.  Observing this output
# is an excellent way to gain insight into how the algorithm works.
use constant DEBUG => 0;

# If set to true, causes the code to skip over even numbers,
# improving runtime.  It does not alter the output content, only the speed.
use constant WHEEL2 => 0;

BEGIN {

   # This is loosely based on the Python implementation of this task,
   # specifically the "Infinite generator with a faster algorithm"

   my @primes = (2, 3);
   my $ps = WHEEL2 ? 1 : 0;
   my $p = $primes[$ps];
   my $q = $p*$p;
   my $incr = WHEEL2 ? 2 : 1;
   my $candidate = $primes[-1] + $incr;
   my %sieve;
   
   print "Initial: p = $p, q = $q, candidate = $candidate\n" if DEBUG;

   sub FETCH {
      my $n = pop;
      return if $n < 0;
      return $primes[$n] if $n <= $#primes;
      OUTER: while( 1 ) {

         # each key in %sieve is a composite number between
         # p and p-squared.  Each value in %sieve is $incr x the prime
         # which acted as a 'seed' for that key.  We use the value
         # to step through multiples of the seed-prime, until we find
         # an empty slot in %sieve.
         while( my $s = delete $sieve{$candidate} ) {
            print "$candidate a multiple of ".($s/$incr).";\t\t" if DEBUG;
            my $composite = $candidate + $s;
            $composite += $s while exists $sieve{$composite};
            print "The next stored multiple of ".($s/$incr)." is $composite\n" if DEBUG;
            $sieve{$composite} = $s;
            $candidate += $incr;
         }

         print "Candidate $candidate is not in sieve\n" if DEBUG;

         while( $candidate < $q ) {
            print "$candidate is prime\n" if DEBUG;
            push @primes, $candidate;
            $candidate += $incr;
            next OUTER if exists $sieve{$candidate};
         } 

         die "Candidate = $candidate, p = $p, q = $q" if $candidate > $q;
         print "Candidate $candidate is equal to $p squared;\t" if DEBUG;

         # Thus, it is now time to add p to the sieve,
         my $step = $incr * $p;
         my $composite = $q + $step;
         $composite += $step while exists $sieve{$composite};
         print "The next multiple of $p is $composite\n" if DEBUG;
         $sieve{$composite} = $step;
      
         # and fetch out a new value for p from our primes array.
         $p = $primes[++$ps];
         $q = $p * $p;  
         
         # And since $candidate was equal to some prime squared,
         # it's obviously composite, and we need to increment it.
         $candidate += $incr;
         print "p is $p, q is $q, candidate is $candidate\n" if DEBUG;
      } continue {
         return $primes[$n] if $n <= $#primes;
      }
   }

}

if( !caller ) {
   tie my (@prime_list), 'Tie::SieveOfEratosthenes';
   my $limit = $ARGV[0] || 100;
   my $line = "";
   for( my $count = 0; $prime_list[$count] < $limit; ++$count ) {
      $line .= $prime_list[$count]. ", ";
      next if length($line) <= 70;
      if( $line =~ tr/,// > 1 ) {
         $line =~ s/^(.*,) (.*, )/$2/;
         print $1, "\n";
      } else {
         print $line, "\n";
         $line = "";
      }
   }
   $line =~ s/, \z//;
   print $line, "\n" if $line;
}

1;
```

This one is based on the vector sieve shown earlier, but adds to a list as needed, just sieving in the segment. Slightly faster and half the memory vs. the previous incremental sieve. It uses the same API -- arguably we should be offset by one so $primes[$n] returns the $n'th prime.

```mw
use strict;
use warnings;
package Tie::SieveOfEratosthenes;

sub TIEARRAY {
  my $class = shift;
  my @primes = (2,3,5,7);
  return bless \@primes, $class;
}

sub prextend { # Extend the given list of primes using a segment sieve
  my($primes, $to) = @_;
  $to-- unless $to & 1; # Ensure end is odd
  return if $to < $primes->[-1];
  my $sqrtn = int(sqrt($to)+0.001);
  prextend($primes, $sqrtn) if $primes->[-1] < $sqrtn;
  my($segment, $startp) = ('', $primes->[-1]+1);
  my($s_beg, $s_len) = ($startp >> 1, ($to>>1) - ($startp>>1));
  for my $p (@$primes) {
    last if $p > $sqrtn;
    if ($p >= 3) {
      my $p2 = $p*$p;
      if ($p2 < $startp) {   # Bump up to next odd multiple of p >= startp
        my $f = 1+int(($startp-1)/$p);
        $p2 = $p * ($f | 1);
      }
      for (my $s = ($p2>>1)-$s_beg; $s <= $s_len; $s += $p) {
        vec($segment, $s, 1) = 1;   # Mark composites in segment
      }
    }
  }
  # Now add all the primes found in the segment to the list
  do { push @$primes, 1+2*($_+$s_beg) if !vec($segment,$_,1) } for 0 .. $s_len;
}

sub FETCHSIZE { 0x7FFF_FFFF }  # Allows foreach to work
sub FETCH {
  my($primes, $n) = @_;
  return if $n < 0;
  # Keep expanding the list as necessary, 5% larger each time.
  prextend($primes, 1000+int(1.05*$primes->[-1])) while $n > $#$primes;
  return $primes->[$n];
}

if( !caller ) {
  tie my @prime_list, 'Tie::SieveOfEratosthenes';
  my $limit = $ARGV[0] || 100;
  print $prime_list[0];
  my $i = 1;
  while ($prime_list[$i] < $limit) { print " ", $prime_list[$i++]; }
  print "\n";
}

1;
```


## Phix

Translation of

:

Euphoria

```
constant limit = 1000
sequence primes = {}
sequence flags = repeat(1, limit)
for i=2 to floor(sqrt(limit)) do
    if flags[i] then
        for k=i*i to limit by i do
            flags[k] = 0
        end for
    end if
end for
for i=2 to limit do
    if flags[i] then
        primes &= i
    end if
end for
pp(primes,{pp_Maxlen,77})
```

**Output:**

```
{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
 101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,
 193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,
 293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,
 409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,
 521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,
 641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,
 757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,
 881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997}
```

See also Sexy_primes#Phix where the sieve is more useful than a list of primes. Most applications should use the builtins, eg `get_primes(-get_maxprime(1000*1000))` or `get_primes_le(1000)` both give exactly the same output as above.


## Phixmonti

```mw
include ..\Utilitys.pmt

def sequence /# ( ini end [step] ) #/
    ( ) swap for 0 put endfor
enddef

1000 var limit

( 1 limit ) sequence

( 2 limit ) for >ps
    ( tps dup * limit tps ) for
        dup limit < if 0 swap set else drop endif
    endfor
    cps
endfor
( 1 limit 0 ) remove
pstack
```

Another solution

```mw
include ..\Utilitys.pmt
   
1000

( "Primes in " over ": " ) lprint

2 swap 2 tolist for >ps
    2
    dup tps < while
        tps over mod 0 == if false else 1 + true endif
        over tps < and
    endwhile
    tps < ps> swap if drop endif
endfor

pstack
```

**Output:**

```
Primes in 1000:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

=== Press any key to exit ===
```


## PHP

```mw
function iprimes_upto($limit)
{
    for ($i = 2; $i < $limit; $i++)
    {
       $primes[$i] = true;
    }
    
    for ($n = 2; $n < $limit; $n++)
    {
       if ($primes[$n])
       {
           for ($i = $n*$n; $i < $limit; $i += $n)
           {
                $primes[$i] = false;
           }
       }
    }
    
    return $primes;
}

echo wordwrap(
    'Primes less or equal than 1000 are : ' . PHP_EOL .
    implode(' ', array_keys(iprimes_upto(1000), true, true)),
    100
);
```

**Output:**

```
Primes less or equal than 1000 are : 
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131
137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269
271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421
431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587
593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743
751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919
929 937 941 947 953 967 971 977 983 991 997
```


## Picat

The SoE is provided in the standard library, defined as follows:

```mw
primes(N) = L =>
    A = new_array(N),
    foreach(I in 2..floor(sqrt(N)))
        if (var(A[I])) then
            foreach(J in I**2..I..N)
                A[J]=0
            end
         end
     end,
     L=[I : I in 2..N, var(A[I])].
```

**Output:**

```
Picat> L = math.primes(100).
L = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
yes
```


## PicoLisp

```mw
(de sieve (N)
   (let Sieve (range 1 N)
      (set Sieve)
      (for I (cdr Sieve)
         (when I
            (for (S (nth Sieve (* I I)) S (nth (cdr S) I))
               (set S) ) ) )
      (filter bool Sieve) ) )
```

Output:

```
: (sieve 100)
-> (2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
```

### Alternate Version Using a 2x3x5x7 Wheel

This works by destructively modifying the CDR of the previous cell when it finds a composite number. For sieving large sets (e.g. 1,000,000) it's much faster than the above.

```mw
(setq WHEEL-2357
    (2  4  2  4  6  2  6  4
     2  4  6  6  2  6  4  2
     6  4  6  8  4  2  4  2
     4  8  6  4  6  2  4  6
     2  6  6  4  2  4  6  2
     6  4  2  4  2 10  2 10 .))

(de roll2357wheel (Limit)
    (let W WHEEL-2357
        (make
            (for (N 11  (<= N Limit)  (+ N (pop 'W)))
                (link N)))))

(de sqr (X) (* X X))

(de remove-multiples (L)
    (let (N (car L)  M (* N N)  P L  Q (cdr L))
        (while Q
            (let A (car Q)
                (until (>= M A)
                    (setq M (+ M N)))
                (when (= A M)
                    (con P (cdr Q))))
            (setq  P Q  Q (cdr Q)))))

(de sieve (Limit)
    (let Sieve (roll2357wheel Limit)
        (for (P Sieve  (<= (sqr (car P)) Limit)  (cdr P))
            (remove-multiples P))
        (append (2 3 5 7) Sieve)))
```

**Output:**

```
: (sieve 100)
-> (2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
: (filter '((N) (> N 900)) (sieve 1000))
-> (907 911 919 929 937 941 947 953 967 971 977 983 991 997)
: (last (sieve 1000000))
-> 999983
```


## PL/I

```mw
eratos: proc options (main) reorder;

dcl i  fixed bin (31);
dcl j  fixed bin (31);
dcl n  fixed bin (31);
dcl sn fixed bin (31);

dcl hbound builtin;
dcl sqrt   builtin;

dcl sysin    file;
dcl sysprint file;

get list (n);
sn = sqrt(n);

begin;
  dcl primes(n) bit (1) aligned init ((*)((1)'1'b));

  i = 2;

  do while(i <= sn);
    do j = i ** 2 by i to hbound(primes, 1);
      /* Adding a test would just slow down processing! */
      primes(j) = '0'b; 
     end;

    do i = i + 1 to sn until(primes(i));
    end;
  end;

  do i = 2 to hbound(primes, 1);
    if primes(i) then
      put data(i);
  end;
end;
end eratos;
```


## PL/M

```mw
100H:

DECLARE PRIME$MAX LITERALLY '5000';

/* CREATE SIEVE OF GIVEN SIZE */
MAKE$SIEVE: PROCEDURE(START, SIZE);
    DECLARE (START, SIZE, M, N) ADDRESS;
    DECLARE PRIME BASED START BYTE;
    
    PRIME(0)=0; /* 0 AND 1 ARE NOT PRIMES */
    PRIME(1)=0; 
    DO N=2 TO SIZE;
        PRIME(N)=1; /* ASSUME ALL OTHERS ARE PRIME AT BEGINNING */
    END;
    
    DO N=2 TO SIZE;
        IF PRIME(N) THEN DO; /* IF A NUMBER IS PRIME... */
            DO M=N*N TO SIZE BY N;
                PRIME(M) = 0; /* THEN ITS MULTIPLES ARE NOT */
            END;
        END;
    END;
END MAKE$SIEVE;

/* CP/M CALLS */
BDOS: PROCEDURE(FUNC, ARG);
    DECLARE FUNC BYTE, ARG ADDRESS;
    GO TO 5;
END BDOS;

DECLARE BDOS$EXIT  LITERALLY '0',
        BDOS$PRINT LITERALLY '9';

/* PRINT A 16-BIT NUMBER */
PRINT$NUMBER: PROCEDURE(N);
    DECLARE (N, P) ADDRESS;
    DECLARE S (8) BYTE INITIAL ('.....',10,13,'$');
    DECLARE C BASED P BYTE;
    P = .S(5);
DIGIT:
    P = P - 1;
    C = (N MOD 10) + '0';
    N = N / 10;
    IF N > 0 THEN GO TO DIGIT;
    CALL BDOS(BDOS$PRINT, P);
END PRINT$NUMBER;

/* PRINT ALL PRIMES UP TO N */
PRINT$PRIMES: PROCEDURE(N, SIEVE);
    DECLARE (I, N, SIEVE) ADDRESS;
    DECLARE PRIME BASED SIEVE BYTE;
    CALL MAKE$SIEVE(SIEVE, N);
    DO I = 2 TO N;
        IF PRIME(I) THEN CALL PRINT$NUMBER(I);
    END;
END PRINT$PRIMES;

CALL PRINT$PRIMES(PRIME$MAX, .MEMORY);

CALL BDOS(BDOS$EXIT, 0);
EOF
```

**Output:**

```
2
3
5
7
11
....
4967
4969
4973
4987
4999
```


## PL/SQL

```mw
create or replace package sieve_of_eratosthenes as
  type array_of_booleans is varray(100000000) of boolean;
  type table_of_integers is table of integer;
  function find_primes (n number) return table_of_integers pipelined;
end sieve_of_eratosthenes;
/

create or replace package body sieve_of_eratosthenes as
  function find_primes (n number) return table_of_integers pipelined is
      flag array_of_booleans;
      ptr  integer;
      i    integer;
  begin
      flag := array_of_booleans(false, true);
      flag.extend(n - 2, 2);
      ptr  := 1;
      << outer_loop >>
      while ptr * ptr <= n loop
          while not flag(ptr) loop
              ptr := ptr + 1;
          end loop;
          i := ptr * ptr;
          while i <= n loop
              flag(i) := false;
              i := i + ptr;
          end loop;
          ptr := ptr + 1;
      end loop outer_loop;
      for i in 1 .. n loop
          if flag(i) then
              pipe row (i);
          end if;
      end loop;
      return;
  end find_primes;
end sieve_of_eratosthenes;
/
```

Usage:

```mw
select column_value as prime_number
from   table(sieve_of_eratosthenes.find_primes(30));

PRIME_NUMBER
------------
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

10 rows selected.

Elapsed: 00:00:00.01

select count(*) as number_of_primes, sum(column_value) as sum_of_primes
from   table(sieve_of_eratosthenes.find_primes(1e7));

NUMBER_OF_PRIMES   SUM_OF_PRIMES
---------------- ---------------
          664579   3203324994356

Elapsed: 00:00:02.60
```


## Pluto

```mw
function sieve(n)
  if n < 2 then return {} end
  t = {0}
  for i = 2,n do
    t[i] = 1
  end
  for i = 2,math.sqrt(n) do
    if t[i]==1 then
      for j = i*i,n,i do
        t[j] = 0
      end
    end
  end
  return t
end

for k, v in sieve(20) do
  if v == 1 then
    print(k)
  end
end
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
```


## Pony

```mw
use "time" // for testing
use "collections"

class Primes is Iterator[U32] // returns an Iterator of found primes...
  let _bitmask: Array[U8] = [ 1; 2; 4; 8; 16; 32; 64; 128 ]
  var _lmt: USize
  let _cmpsts: Array[U8]
  var _ndx: USize = 2
  var _curr: U32 = 2
  
  new create(limit: U32) ? =>
    _lmt = USize.from[U32](limit)
    let sqrtlmt = USize.from[F64](F64.from[U32](limit).sqrt())
    _cmpsts = Array[U8].init(0, (_lmt + 8) / 8) // already zeroed; bit array
    _cmpsts(0)? = 3 // mark 0 and 1 as not prime!
    if sqrtlmt < 2 then return end
    for p in Range[USize](2, sqrtlmt + 1) do
      if (_cmpsts(p >> 3)? and _bitmask(p and 7)?) == 0 then
        var s = p * p // cull start address for p * p!
        let slmt = (s + (p << 3)).min(_lmt + 1)
        while s < slmt do
          let msk = _bitmask(s and 7)?
          var c = s >> 3
          while c < _cmpsts.size() do
            _cmpsts(c)? = _cmpsts(c)? or msk
            c = c + p
          end
          s = s + p
        end
      end
    end

  fun ref has_next(): Bool val => _ndx < (_lmt + 1)
  
  fun ref next(): U32 ? =>
    _curr = U32.from[USize](_ndx); _ndx = _ndx + 1
    while (_ndx <= _lmt) and ((_cmpsts(_ndx >> 3)? and _bitmask(_ndx and 7)?) != 0) do
      _ndx = _ndx + 1
    end
    _curr

actor Main
  new create(env: Env) =>
    let limit: U32 = 1_000_000_000
    try
      env.out.write("Primes to 100:  ")
      for p in Primes(100)? do env.out.write(p.string() + " ") end
      var count: I32 = 0
      for p in Primes(1_000_000)? do count = count + 1 end
      env.out.print("\nThere are " + count.string() + " primes to a million.")
      let t = Time
      let start = t.millis()
      let prms = Primes(limit)?
      let elpsd = t.millis() - start
      count = 0
      for _ in prms do count = count + 1 end
      env.out.print("Found " + count.string() + " primes to " + limit.string() + ".")
      env.out.print("This took " + elpsd.string() + " milliseconds.")
    end
```

**Output:**

```
Primes to 100:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
There are 78498 primes to a million.
Found 50847534 primes to 1000000000.
This took 28123 milliseconds.
```

Note to users: a naive monolithic sieve (one huge array) isn't really the way to implement this for other than trivial usage in sieving ranges to a few millions as cache locality becomes a very large problem as the size of the array (even bit packed with one bit per number representation as here) limits the maximum range that can be sieved and the "cache thrashing" limits the speed.

For extended ranges, a Page Segmented version should be used. As well, for any extended ranges in the billions, it is a waste of available computer resources to not use the multi-threading available in a modern CPU, at which Pony would do very well with its built-in Actor concurrency model.

These versions use "loop unpeeling" (not full loop unrolling), which recognizes the repeating modulo pattern of masking the bytes by the base primes less than the square root of the limit so that an "unpeeling" by eight loops can cull by a constant bit mask over the whole range. For smaller ranges where the speed is not limited by "cache thrashing", this can provide about a factor-of-two speed-up.

### Alternate Odds-Only version of the above

It is a waste not to do the trivial changes to the above code to sieve odds-only, which is about two and a half times faster due to the decreased number of culling operations; it doesn't really do much about the huge array problem though, other than to reduce it by a factor of two.

```mw
use "time" // for testing
use "collections"

class Primes is Iterator[U32] // returns an Iterator of found primes...
  let _bitmask: Array[U8] = [ 1; 2; 4; 8; 16; 32; 64; 128 ]
  var _lmti: USize
  let _cmpsts: Array[U8]
  var _ndx: USize = 0
  var _curr: U32 = 0
  
  new create(limit: U32) ? =>
    if limit < 3 then _lmti = 0; _cmpsts = Array[U8](); return end
    _lmti = USize.from[U32]((limit - 3) / 2)
    let sqrtlmti = (USize.from[F64](F64.from[U32](limit).sqrt()) - 3) / 2
    _cmpsts = Array[U8].init(0, (_lmti + 8) / 8) // already zeroed; bit array
    for i in Range[USize](0, sqrtlmti + 1) do
      if (_cmpsts(i >> 3)? and _bitmask(i and 7)?) == 0 then
        let p = i + i + 3
        var s = ((i << 1) * (i + 3)) + 3 // cull start address for p * p!
        let slmt = (s + (p << 3)).min(_lmti + 1)
        while s < slmt do
          let msk = _bitmask(s and 7)?
          var c = s >> 3
          while c < _cmpsts.size() do
            _cmpsts(c)? = _cmpsts(c)? or msk
            c = c + p
          end
          s = s + p
        end
      end
    end

  fun ref has_next(): Bool val => _ndx < (_lmti + 1)
  
  fun ref next(): U32 ? =>
    if _curr < 1 then _curr = 3; if _lmti == 0 then _ndx = 1 end; return 2 end
    _curr = U32.from[USize](_ndx + _ndx + 3); _ndx = _ndx + 1
    while (_ndx <= _lmti) and ((_cmpsts(_ndx >> 3)? and _bitmask(_ndx and 7)?) != 0) do
      _ndx = _ndx + 1
    end
    _curr

actor Main
  new create(env: Env) =>
    let limit: U32 = 1_000_000_000
    try
      env.out.write("Primes to 100:  ")
      for p in Primes(100)? do env.out.write(p.string() + " ") end
      var count: I32 = 0
      for p in Primes(1_000_000)? do count = count + 1 end
      env.out.print("\nThere are " + count.string() + " primes to a million.")
      let t = Time
      let start = t.millis()
      let prms = Primes(limit)?
      let elpsd = t.millis() - start
      count = 0
      for _ in prms do count = count + 1 end
      env.out.print("Found " + count.string() + " primes to " + limit.string() + ".")
      env.out.print("This took " + elpsd.string() + " milliseconds.")
    end
```

The output is the same as the above except that it is about two and a half times faster due to that many less culling operations.


## Pop11

```
define eratostenes(n);
lvars bits = inits(n), i, j;
for i from 2 to n do
   if bits(i) = 0 then
      printf('' >< i, '%s\n');
      for j from 2*i by i to n do
         1 -> bits(j);
      endfor;
   endif;
endfor;
enddefine;
```


## PostScript

Works with

:

Ghostscript

version 10.06.0

An implementation representing the natural numbers as an array. The following source is a bare-bones version that will dump the result to the console. It probably makes no sense to send this document to a real Postscript printer.

```mw
%!PS
% Calculate primes using the Sieve of Eratosthenes
% and dump the result to the console.

/sieve
{
  % Usage: maxnumber sieve
  %                        primes... 5 3 2
  /limit exch def
  % Generate an array of all the numbers, representing the prime candidates
  % (Start at 0 for ease of indexing.)
  [ 0 1 limit { } for ]
  % Replace all composite numbers by 0
  dup 1 0 put
  2 1 limit sqrt floor
  {
    1 index exch get dup 0 ne
    {
      dup dup mul exch limit { 1 index exch 0 put } for
    } { pop } ifelse
  } for
  % The stack now contains an array of primes and zeroes.
  % Push the primes onto the stack with the smallest at the top:
  limit -1 1
  {
    exch dup 3 -1 roll get dup
    0 eq { pop } { exch } ifelse
  } for
  pop
  % The stack now contains the list of primes (smallest = 2 on top)
} bind def

300 sieve pstack % <-- replace "300" with the desired maximum number to check.
% 300000 sieve pstack 
%%EOF
```

**Output:**

```
2
3
5
7
...
```

The following version is identical with respect to the sieve implementation but will properly print the output.

```mw
%!PS
% Calculate primes using the Sieve of Eratosthenes and
% print them out.

/sieve
{
  % Usage: maxnumber sieve
  %                        primes... 5 3 2
  /limit exch def
  % Generate an array of all the numbers, representing the prime candidates
  % (Start at 0 for ease of indexing.)
  [ 0 1 limit { } for ]
  % Replace all composite numbers by 0
  dup 1 0 put
  2 1 limit sqrt floor
  {
    1 index exch get dup 0 ne
    {
      dup dup mul exch limit { 1 index exch 0 put } for
    } { pop } ifelse
  } for
  % The stack now contains an array of primes and zeroes.
  % Push the primes onto the stack with the smallest at the top:
  limit -1 1
  {
    exch dup 3 -1 roll get dup
    0 eq { pop } { exch } ifelse
  } for
  pop
  % The stack now contains the list of primes (smallest = 2 on top)
} bind def

/showstack
{
  % Usage: primes... 5 3 2 showstack
  %                                  -
  % (This is just for output. No business logic here.)

  /fontsize   12     def
  /lineheight fontsize 3 add def
  /Helvetica  findfont
  fontsize    scalefont setfont
  /margin     30     def
  /left       margin def
  /bottom     margin def
  currentpagedevice /PageSize get aload pop
  margin sub fontsize sub /top exch def
  margin sub /right exch def

  /buffer 42 string def
  left top moveto
  1 1 count 2 sub
  { pop dup 0 ne
    {
      buffer cvs
      dup stringwidth pop currentpoint pop add
      right gt {
        left currentpoint exch pop lineheight sub
        dup bottom lt {
          showpage
          pop top
        } if
        moveto
      } if
      show
      ( ) show
    } { pop } ifelse
  } for
  showpage
} bind def

300 sieve showstack % <-- replace "300" with the desired maximum number to check.
% 300000 sieve showstack % will yield about 40 A4 pages
%%EOF
```

The following is a very inefficient "pure-stack" implementation not using arrays. It will be usable only for small maximum numbers (a couple of 100s at best).

```mw
%!PS
% Calculate primes using the Sieve of Eratosthenes
% and dump the result to the console.
% (Stack-centric implementation without direct memory access)

/sieve
{
  % Usage: maxnumber sieve
  %                        primes... 5 3 2
  % Put all the candidates on the stack (1 = lowest number on top)
  % but always keep our max number on top of stack (i.e., index 0)
  dup -1 2 { exch } for
  0 exch                                % 1 is no prime

  % Phase 1: find next prime (up to sqrt(limit)),
  % mark all multiples by setting to 0.
  dup 2 1 3 -1 roll sqrt floor
  {
    dup 2 add -1 roll
    dup 3 -1 roll 2 add 1 roll
    dup
    0 ne
    { % Found a prime. Delete all multiples, starting with square of this prime.
      dup dup mul exch 2 index
      {
        dup 2 add -1 roll
        pop
        0 exch 1 add 1 roll
      } for
    } { pop }  % known composite: no action needed.
    ifelse
  } for

  % Phase 2: find all primes (i.e., non-zero numbers), push them
  % densely on the stack, starting from highest.
  % Always keep the current stack size on top
  dup 1 add exch
  {
    dup -1 roll dup
    0 ne { exch } { pop 1 sub } ifelse
  } repeat
  pop          % remove stack size
  % The stack now contains the list of primes (smallest = 2 on top)
} bind def

300 sieve pstack
%%EOF
```


## PowerShell

### Basic procedure

It outputs immediately so that the number can be used by the pipeline.

```mw
function Sieve ( [int] $num )
{
    $isprime = @{}
    2..$num | Where-Object {
        $isprime[$_] -eq $null } | ForEach-Object {
        $_
        $isprime[$_] = $true
        $i=$_*$_
        for ( ; $i -le $num; $i += $_ )
        { $isprime[$i] = $false }
    }
}
```

### Another implementation

```mw
function eratosthenes ($n) {
    if($n -ge 1){
        $prime = @(1..($n+1) | foreach{$true})
        $prime[1] = $false
        $m = [Math]::Floor([Math]::Sqrt($n))
        for($i = 2; $i -le $m; $i++) {
            if($prime[$i]) {
                for($j = $i*$i; $j -le $n; $j += $i) {
                    $prime[$j] = $false
                }
            }
        }
        1..$n | where{$prime[$_]}
    } else {
        Write-Warning "$n is less than 1"
    }
}
"$(eratosthenes 100)"
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```


## Processing

Calculate the primes up to 1000000 with Processing, including a visualisation of the process.

```mw
int i=2;
int maxx;
int maxy;
int max;
boolean[] sieve;

void setup() {
  size(1000, 1000);
  // frameRate(2);
  maxx=width;
  maxy=height;
  max=width*height;
  sieve=new boolean[max+1];

  sieve[1]=false;
  plot(0, false);
  plot(1, false);
  for (int i=2; i<=max; i++) {
    sieve[i]=true;
    plot(i, true);
  }
}

void draw() {
  if (!sieve[i]) {
    while (i*i<max && !sieve[i]) {
      i++;
    }
  }
  if (sieve[i]) {
    print(i+" ");
    for (int j=i*i; j<=max; j+=i) {
      if (sieve[j]) {
        sieve[j]=false;
        plot(j, false);
      }
    }
  }
  if (i*i<max) {
    i++;
  } else {
    noLoop();
    println("finished");
  }
}

void plot(int pos, boolean active) {
  set(pos%maxx, pos/maxx, active?#000000:#ffffff);
}
```

As an additional visual effect, the layout of the pixel could be changed from the line-by-line layout to a spiral-like layout starting in the middle of the screen.

### Processing Python mode

```mw
from __future__ import print_function

i = 2

def setup():
    size(1000, 1000)
    # frameRate(2)
    global maxx, maxy, max_num, sieve
    maxx = width
    maxy = height
    max_num = width * height
    sieve = [False] * (max_num + 1)

    sieve[1] = False
    plot(0, False)
    plot(1, False)
    for i in range(2, max_num + 1):
        sieve[i] = True
        plot(i, True)

def draw():
    global i
    if not sieve[i]:
        while (i * i < max_num and not sieve[i]):
            i += 1

    if sieve[i]:
        print("{} ".format(i), end = '')
        for j in range(i * i, max_num + 1, i):
            if sieve[j]:
                sieve[j] = False
                plot(j, False)

    if i * i < max_num:
        i += 1
    else:
        noLoop()
        println("finished")

def plot(pos, active):
    set(pos % maxx, pos / maxx, color(0) if active else color(255))
```


## Prolog

### Using lists

#### Basic bounded sieve

```mw
primes(N, L) :- numlist(2, N, Xs),
           sieve(Xs, L).

sieve([H|T], [H|X]) :- H2 is H + H, 
                       filter(H, H2, T, R),
                       sieve(R, X).
sieve([], []).

filter(_, _, [], []).
filter(H, H2, [H1|T], R) :- 
    (   H1 < H2 -> R = [H1|R1], filter(H, H2, T, R1)
    ;   H3 is H2 + H,
        (   H1 =:= H2  ->       filter(H, H3, T, R)
        ;                       filter(H, H3, [H1|T], R) ) ).
```

**Output:**

```
 ?- time(( primes(7920,X), length(X,N) )).
% 1,131,127 inferences, 0.109 CPU in 0.125 seconds (88% CPU, 10358239 Lips)
X = [2, 3, 5, 7, 11, 13, 17, 19, 23|...],
N = 1000 .
```

#### Basic bounded Euler's sieve

Translation of

:

Erlang Canonical

This is actually the Euler's variant of the sieve of Eratosthenes, generating (and thus removing) each multiple only once, though a sub-optimal implementation.

```mw
primes(X, PS) :- X > 1, range(2, X, R), sieve(R, PS).

range(X, X, [X]) :- !.
range(X, Y, [X | R]) :- X < Y, X1 is X + 1, range(X1, Y, R).

mult(A, B, C) :- C is A*B.

sieve([X], [X]) :- !.
sieve([H | T], [H | S]) :- maplist( mult(H), [H | T], MS), 
                           remove(MS, T, R), sieve(R, S).
 
remove( _,       [],      []     ) :- !.
remove( [H | X], [H | Y], R      ) :- !, remove(X, Y, R).
remove( X,       [H | Y], [H | R]) :- remove(X, Y, R).
```

Running in SWI Prolog,

**Output:**

```
 ?- time(( primes(7920,X), length(X,N) )).
% 2,087,373 inferences, 0.203 CPU in 0.203 seconds (100% CPU, 10297621 Lips)
X = [2, 3, 5, 7, 11, 13, 17, 19, 23|...],
N = 1000.
```

#### Optimized Euler's sieve

We can stop early, with massive improvement in complexity (below ~ *n1.5* inferences, empirically, vs. the ~ *n2* of the above, in *n* primes produced; showing only the modified predicates):

```mw
primes(X, PS) :- X > 1, range(2, X, R), sieve(X, R, PS).

sieve(X, [H | T], [H | T]) :- H*H > X, !.
sieve(X, [H | T], [H | S]) :- maplist( mult(H), [H | T], MS), 
                              remove(MS, T, R), sieve(X, R, S).
```

**Output:**

```
 ?- time(( primes(7920,X), length(X,N) )).
% 174,437 inferences, 0.016 CPU in 0.016 seconds (100% CPU, 11181787 Lips)
X = [2, 3, 5, 7, 11, 13, 17, 19, 23|...],
N = 1000.
```

#### Bounded sieve

Optimized by stopping early, traditional sieve of Eratosthenes generating multiples by iterated addition.

```mw
primes(X, PS) :- X > 1, range(2, X, R), sieve(X, R, PS).

range(X, X, [X]) :- !.
range(X, Y, [X | R]) :- X < Y, X1 is X + 1, range(X1, Y, R).

sieve(X, [H | T], [H | T]) :- H*H > X, !.
sieve(X, [H | T], [H | S]) :- mults( H, X, MS), remove(MS, T, R), sieve(X, R, S).

mults( H, Lim, MS):- M is H*H, mults( H, M, Lim, MS).
mults( _, M, Lim, []):- M > Lim, !.
mults( H, M, Lim, [M|MS]):- M2 is M+H, mults( H, M2, Lim, MS).

remove( _,       [],      []     ) :- !.
remove( [H | X], [H | Y], R      ) :- !, remove(X, Y, R).
remove( [H | X], [G | Y], R      ) :- H < G, !, remove(X, [G | Y], R).
remove( X,       [H | Y], [H | R]) :- remove(X, Y, R).
```

**Output:**

```
?- time(( primes(7920,X), length(X,N) )).
% 140,654 inferences, 0.016 CPU in 0.011 seconds (142% CPU, 9016224 Lips)
X = [2, 3, 5, 7, 11, 13, 17, 19, 23|...],
N = 1000.
```

#### Sift the Two's and Sift the Three's

Another version, based on Cloksin&Mellish p.175, modified to stop early as well as to work with odds only and use addition in the removing predicate, instead of the `mod` testing as the original was doing:

```mw
primes(N,[]):- N < 2, !.
primes(N,[2|R]):- ints(3,N,L), sift(N,L,R).
ints(A,B,[A|C]):- A=<B -> D is A+2, ints(D,B,C).
ints(_,_,[]).
sift(_,[],[]).
sift(N,[A|B],[A|C]):- A*A =< N ->  rmv(A,B,D), sift(N,D,C)
                      ; C=B.
rmv(A,B,D):- M is A*A, rmv(A,M,B,D).
rmv(_,_,[],[]).
rmv(P,M,[A|B],C):- (   M>A ->  C=[A|D], rmv(P,M,B,D)
                   ;   M==A ->  M2 is M+2*P, rmv(P,M2,B,C) 
                   ;   M<A ->  M2 is M+2*P, rmv(P,M2,[A|B],C)
                   ).
```

Runs at about n^1.4 time empirically, producing 20,000 primes in 1.4 secs on the SWISH platform as of 2021-11-26.

### Using lazy lists

In SWI Prolog and others, where `freeze/2` is available.

#### Basic variant

```mw
primes(PS):- count(2, 1, NS), sieve(NS, PS).

count(N, D, [N|T]):- freeze(T, (N2 is N+D, count(N2, D, T))).

sieve([N|NS],[N|PS]):- N2 is N*N, count(N2,N,A), remove(A,NS,B), freeze(PS, sieve(B,PS)).

take(N, X, A):- length(A, N), append(A, _, X).

remove([A|T],[B|S],R):- A < B -> remove(T,[B|S],R) ;
                        A=:=B -> remove(T,S,R) ; 
                        R = [B|R2], freeze(R2, remove([A|T], S, R2)).
```

**Output:**

```
 ?- time(( primes(PS), take(1000,PS,R1), length(R,10), append(_,R,R1), writeln(R), false )).
[7841,7853,7867,7873,7877,7879,7883,7901,7907,7919]
% 8,464,518 inferences, 0.702 CPU in 0.697 seconds (101% CPU, 12057641 Lips)
false.
```

#### Optimized by postponed removal

Showing only changed predicates.

```mw
primes([2|PS]):- 
    freeze(PS, (primes(BPS), count(3, 1, NS), sieve(NS, BPS, 4, PS))). 

sieve([N|NS], BPS, Q, PS):- 
    N < Q -> PS = [N|PS2], freeze(PS2, sieve(NS, BPS, Q, PS2))
    ;  BPS = [BP,BP2|BPS2], Q2 is BP2*BP2, count(Q, BP, MS),
       remove(MS, NS, R), sieve(R, [BP2|BPS2], Q2, PS).
```

**Output:**

```
 ?- time(( primes(PS), take(1000,PS,R1), length(R,10), append(_,R,R1), writeln(R), false )).
[7841,7853,7867,7873,7877,7879,7883,7901,7907,7919]
% 697,727 inferences, 0.078 CPU in 0.078 seconds (100% CPU, 8945161 Lips)
false.       %% odds only: 487,441 inferences
```

### Using facts to record composite numbers

The first two solutions use Prolog "facts" to record the composite (i.e. already-visited) numbers.

#### Elementary approach: multiplication-free, division-free, mod-free, and cut-free

The basic Eratosthenes sieve depends on nothing more complex than counting. In celebration of this simplicity, the first approach to the problem taken here is free of multiplication and division, as well as Prolog's non-logical "cut".

It defines the predicate between/4 to avoid division, and composite/1 to record integers that are found to be composite.

```mw
% %sieve( +N, -Primes ) is true if Primes is the list of consecutive primes
% that are less than or equal to N
sieve( N, [2|Rest]) :-
  retractall( composite(_) ),
  sieve( N, 2, Rest ) -> true.  % only one solution

% sieve P, find the next non-prime, and then recurse:
sieve( N, P, [I|Rest] ) :-
  sieve_once(P, N),
  (P = 2 -> P2 is P+1; P2 is P+2),
  between(P2, N, I), 
  (composite(I) -> fail; sieve( N, I, Rest )).

% It is OK if there are no more primes less than or equal to N:
sieve( N, P, [] ).

sieve_once(P, N) :-
  forall( between(P, N, P, IP),
          (composite(IP) -> true ; assertz( composite(IP) )) ).

% To avoid division, we use the iterator
% between(+Min, +Max, +By, -I) 
% where we assume that By > 0
% This is like "for(I=Min; I <= Max; I+=By)" in C.
between(Min, Max, By, I) :- 
  Min =< Max, 
  A is Min + By, 
  (I = Min; between(A, Max, By, I) ).

% Some Prolog implementations require the dynamic predicates be
%  declared:

:- dynamic( composite/1 ).
```

The above has been tested with SWI-Prolog and gprolog.

```mw
% SWI-Prolog:

?- time( (sieve(100000,P), length(P,N), writeln(N), last(P, LP), writeln(LP) )).
% 1,323,159 inferences, 0.862 CPU in 0.921 seconds (94% CPU, 1534724 Lips)
P = [2, 3, 5, 7, 11, 13, 17, 19, 23|...],
N = 9592,
LP = 99991.
```

#### Optimized approach

Works with SWI-Prolog.

```mw
sieve(N, [2|PS]) :-       % PS is list of odd primes up to N
    retractall(mult(_)),
    sieve_O(3,N,PS).

sieve_O(I,N,PS) :-        % sieve odds from I up to N to get PS
    I =< N, !, I1 is I+2,
    (   mult(I) -> sieve_O(I1,N,PS)
    ;   (   I =< N / I -> 
            ISq is I*I, DI  is 2*I, add_mults(DI,ISq,N)
        ;   true 
        ),
        PS = [I|T],
        sieve_O(I1,N,T)
    ).
sieve_O(I,N,[]) :- I > N.

add_mults(DI,I,N) :-
    I =< N, !,
    ( mult(I) -> true ; assert(mult(I)) ),
    I1 is I+DI,
    add_mults(DI,I1,N).
add_mults(_,I,N) :- I > N.

main(N) :- current_prolog_flag(verbose,F),
  set_prolog_flag(verbose,normal), 
  time( sieve( N,P)), length(P,Len), last(P, LP), writeln([Len,LP]),
  set_prolog_flag(verbose,F).
 
:- dynamic( mult/1 ).
:- main(100000), main(1000000).
```

Running it produces

```mw
%% stdout copy
[9592, 99991]
[78498, 999983]

%% stderr copy
% 293,176 inferences, 0.14 CPU in 0.14 seconds (101% CPU, 2094114 Lips)
% 3,122,303 inferences, 1.63 CPU in 1.67 seconds (97% CPU, 1915523 Lips)
```

which indicates *~ N1.1* empirical orders of growth, which is consistent with the *O(N log log N)* theoretical runtime complexity.

### Using a priority queue

Uses a ariority queue, from the paper "The Genuine Sieve of Eratosthenes" by Melissa O'Neill. Works with YAP (Yet Another Prolog)

```mw
?- use_module(library(heaps)).

prime(2).
prime(N) :- prime_heap(N, _).

prime_heap(3, H) :- list_to_heap([9-6], H).
prime_heap(N, H) :-
    prime_heap(M, H0), N0 is M + 2,
    next_prime(N0, H0, N, H).

next_prime(N0, H0, N, H) :-
    \+ min_of_heap(H0, N0, _),
    N = N0, Composite is N*N, Skip is N+N,
    add_to_heap(H0, Composite, Skip, H).
next_prime(N0, H0, N, H) :-
    min_of_heap(H0, N0, _),
    adjust_heap(H0, N0, H1), N1 is N0 + 2,
    next_prime(N1, H1, N, H).

adjust_heap(H0, N, H) :-
    min_of_heap(H0, N, _),
    get_from_heap(H0, N, Skip, H1),
    Composite is N + Skip, add_to_heap(H1, Composite, Skip, H2),
    adjust_heap(H2, N, H).
adjust_heap(H, N, H) :-
    \+ min_of_heap(H, N, _).
```


## PureBasic

### Basic procedure

```mw
For n=2 To Sqr(lim)
  If Nums(n)=0
    m=n*n
    While m<=lim
      Nums(m)=1
      m+n
    Wend
  EndIf
Next n
```

### Working example

```mw
Dim Nums.i(0)
Define l, n, m, lim

If OpenConsole()

  ; Ask for the limit to search, get that input and allocate a Array
  Print("Enter limit for this search: ")
  lim=Val(Input())
  ReDim Nums(lim)
  
  ; Use a basic Sieve of Eratosthenes
  For n=2 To Sqr(lim)
    If Nums(n)=#False
      m=n*n
      While m<=lim
        Nums(m)=#True
        m+n
      Wend
    EndIf
  Next n
  
  ;Present the result to our user
  PrintN(#CRLF$+"The Prims up to "+Str(lim)+" are;")
  m=0: l=Log10(lim)+1
  For n=2 To lim
    If Nums(n)=#False
      Print(RSet(Str(n),l)+" ")
      m+1
      If m>72/(l+1)
        m=0: PrintN("")
      EndIf
    EndIf
  Next
  
  Print(#CRLF$+#CRLF$+"Press ENTER to exit"): Input()
  CloseConsole()
EndIf
```

Output may look like;

```
Enter limit for this search: 750

The Prims up to 750 are;
   2    3    5    7   11   13   17   19   23   29   31   37   41   43   47
  53   59   61   67   71   73   79   83   89   97  101  103  107  109  113
 127  131  137  139  149  151  157  163  167  173  179  181  191  193  197
 199  211  223  227  229  233  239  241  251  257  263  269  271  277  281
 283  293  307  311  313  317  331  337  347  349  353  359  367  373  379
 383  389  397  401  409  419  421  431  433  439  443  449  457  461  463
 467  479  487  491  499  503  509  521  523  541  547  557  563  569  571
 577  587  593  599  601  607  613  617  619  631  641  643  647  653  659
 661  673  677  683  691  701  709  719  727  733  739  743

Press ENTER to exit
```
