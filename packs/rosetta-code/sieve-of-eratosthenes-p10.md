---
title: "Sieve of Eratosthenes (part 10/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 10/21
---

## Haskell

### Mutable unboxed arrays

Mutable array of unboxed `Bool`s indexed by `Int`s:

```mw
{-# LANGUAGE FlexibleContexts #-} -- too lazy to write contexts...
{-# OPTIONS_GHC -O2 #-}

import Control.Monad.ST ( runST, ST )
import Data.Array.Base ( MArray(newArray, unsafeRead, unsafeWrite),
                         IArray(unsafeAt),
                         STUArray, unsafeFreezeSTUArray, assocs )
import Data.Time.Clock.POSIX ( getPOSIXTime ) -- for timing...

primesTo :: Int -> [Int] -- generate a list of primes to given limit...
primesTo limit = runST $ do
  let lmt = limit - 2-- raw index of limit!
  cmpsts <- newArray (2, limit) False -- when indexed is true is composite
  cmpstsf <- unsafeFreezeSTUArray cmpsts -- frozen in place!
  let getbpndx bp = (bp, bp * bp - 2) -- bp -> bp, raw index of start cull
      cullcmpst i = unsafeWrite cmpsts i True -- cull composite by raw ndx
      cull4bpndx (bp, si0) = mapM_ cullcmpst [ si0, si0 + bp .. lmt ]
  mapM_ cull4bpndx
        $ takeWhile ((>=) lmt . snd) -- for bp's <= square root limit
                    [ getbpndx bp | (bp, False) <- assocs cmpstsf ]
  return [ p | (p, False) <- assocs cmpstsf ] -- non-raw ndx is prime

-- testing...
main :: IO ()
main = do
  putStrLn $ "The primes up to 100 are " ++ show (primesTo 100)
  putStrLn $ "The number of primes up to a million is " ++
               show (length $ primesTo 1000000)
  let top = 1000000000
  start <- getPOSIXTime
  let answr = length $ primesTo top
  stop <- answr `seq` getPOSIXTime -- force result for timing!
  let elpsd =  round $ 1e3 * (stop - start) :: Int

  putStrLn $ "Found " ++ show answr ++ " to " ++ show top ++
               " in " ++ show elpsd ++ " milliseconds."
```

The above code chooses conciseness and elegance over speed, but it isn't too slow:

**Output:**

```
The primes up to 100 are [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
The number of primes up to a million is 78498
Found 50847534 to 1000000000 in 12435 milliseconds.
```

Run on an Intel Sky Lake i5-2500 at 3.6 GHZ (single threaded boost). As per the comments in the below, this is greatly sped up by a constant factor by using the raw `unsafeWrite`; use of the "unsafe" versions that avoid run time array bounds checks on every operation is entirely safe here as the indexing is inherently limited to be within the bounds by their use in the loops. There is an additional benefit of about 20 per cent in speed if run with the LLVM back end compiler option (add the "-fllvm" flag) if the right version of LLVM is available to the GHC Haskell compiler. We see the relatively small benefit of using LLVM in that this program spends a relatively small percentage of time in the tight inner culling loop where LLVM can help the most and a high part of the time is spent just enumerating the result list.

### Mutable unboxed arrays, odds only

Mutable array of unboxed `Bool`s indexed by `Int`s, representing odds only:

```mw
import Control.Monad (forM_, when)
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed

sieveUO :: Int -> UArray Int Bool
sieveUO top = runSTUArray $ do
    let m = (top-1) `div` 2
        r = floor . sqrt $ fromIntegral top + 1
    sieve <- newArray (1,m) True          -- :: ST s (STUArray s Int Bool)
    forM_ [1..r `div` 2] $ \i -> do       -- prime(i) = 2i+1
      isPrime <- readArray sieve i        -- ((2i+1)^2-1)`div`2 = 2i(i+1)
      when isPrime $ do                   
        forM_ [2*i*(i+1), 2*i*(i+2)+1..m] $ \j -> do
          writeArray sieve j False
    return sieve

primesToUO :: Int -> [Int]
primesToUO top | top > 1   = 2 : [2*i + 1 | (i,True) <- assocs $ sieveUO top]
               | otherwise = []
```

This represents *odds only* in the array. Empirical orders of growth is ~ *n1.2* in *n* primes produced, and improving for bigger *n*‍ ‍s. Memory consumption is low (array seems to be packed) and growing about linearly with *n*. Can further be significantly sped up by re-writing the `forM_` loops with direct recursion, and using `unsafeRead` and `unsafeWrite` operations.

In light of the performance of the previous and following submissions results, the IDEOne results seem somewhat slow at about 10 seconds over a range of about a third of a billion, likely due to some lazily deferred operations in the processing. See the next submission for expected speeds for odds only.

The measured empirical orders of growth as per the table in the IDEOne link are easily understood if one considers that these slowish run times are primarily limited by the time to lazily enumerate the results and that the number of found primes to enumerate varies as (top / log top) by the Euler relationship. Since the prime density decreases by this relationship, the enumeration has the inverse relationship as it takes longer per prime to find the primes in the sieved buffer. Log of a million is 1.2 times larger than log of a hundred thousand and of course this ratio gets smaller with range: the ratio of the log of a billion as compared to log of a hundred million is 1.125, etc.

### Alternate Version of Mutable unboxed arrays, odds only

The reason for this alternate version is to have an accessible version of "odds only" that uses the same optimizations and is written in the same coding style as the basic version. This can be used by just substituting the following code for the function of the same name in the first base example above. Mutable array of unboxed `Bool`s indexed by `Int`s, representing odds only:

```mw
primesTo :: Int -> [Int] -- generate a list of primes to given limit...
primesTo limit
  | limit < 2 = []
  | otherwise = runST $ do
      let lmt = (limit - 3) `div` 2 - 1 -- limit index!
      oddcmpsts <- newArray (0, lmt) False -- when indexed is true is composite
      oddcmpstsf <- unsafeFreezeSTUArray oddcmpsts -- frozen in place!
      let getbpndx i = (i + i + 3, (i + i) * (i + 3) + 3) -- index -> bp, si0
          cullcmpst i = unsafeWrite oddcmpsts i True -- cull composite by index
          cull4bpndx (bp, si0) = mapM_ cullcmpst [ si0, si0 + bp .. lmt ]
      mapM_ cull4bpndx
            $ takeWhile ((>=) lmt . snd) -- for bp's <= square root limit
                        [ getbpndx i | (i, False) <- assocs oddcmpstsf ]
      return $ 2 : [ i + i + 3 | (i, False) <- assocs oddcmpstsf ]
```

**Output:**

```
The primes up to 100 are [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
The number of primes up to a million is 78498
Found 50847534 to 1000000000 in 6085 milliseconds.
```

A "monolithic buffer" odds only sieve uses half the memory as compared to the basic version.

This is not the expected about 2.5 times faster as the basic version because there are other factors to execution time cost than just the number of culling operations, as follows:

1) Since the amount of memory used to sieve to a billion has been dropped from 125 million bytes to 62.5 million bytes, the cache associativity is slightly better, which should make it faster; however

2) We have eliminated the culling by the very small span of the base prime of two, which means a lesser percentage of the culling span operations will be within a given CPU cache size, which will make it slower, but

3) The primary reason we observe only about a factor of two difference in run times is that we have increased the prime density in the sieving buffer by a factor of two, which means that we have half the work to enumerate the primes. Since enumeration of the found primes is a major contribution of the execution time, the execution time will tend to change more by its cost than any other.

As to "empirical orders of growth", the comments made in the above are valid, but there is a further observation. For smaller ranges of primes up to a few million where the sieving buffer fits within the CPU L2 cache size (generally 256 Kilobytes/2 million bits, representing a range of about four million for this version), the cull times are their fastest and enumeration is a bigger percentage of the time; as ranges increase above that, more and more time is spent waiting on memory at the access times of the next level memory (CPU L3 cache, if present, followed by main memory) so that the controlling factor is a little less that of the enumeration time as range gets larger.

**Because of the greatly increasing memory demands and the high execution cost of memory access as ranges exceed the span of the CPU caches, it is not recommended that these simple "monolithic buffer" sieves be used for sieving of ranges above about a hundred million.** Rather, one should use a "Paged-Segmented" sieve as per the examples near the end of this Haskell section.

### Immutable arrays

Monolithic sieving array. *Even* numbers above 2 are pre-marked as composite, and sieving is done only by *odd* multiples of *odd* primes:

```mw
import Data.Array.Unboxed
 
primesToA m = sieve 3 (array (3,m) [(i,odd i) | i<-[3..m]] :: UArray Int Bool)
  where
    sieve p a 
      | p*p > m   = 2 : [i | (i,True) <- assocs a]
      | a!p       = sieve (p+2) $ a//[(i,False) | i <- [p*p, p*p+2*p..m]]
      | otherwise = sieve (p+2) a
```

Its performance sharply depends on compiler optimizations. Compiled with -O2 flag in the presence of the explicit type signature, it is very fast in producing first few million primes. `(//)` is an array update operator.

### Immutable arrays, by segments

Works by segments between consecutive primes' squares. Should be the fastest of non-monadic code. *Evens* are entirely ignored:

```mw
import Data.Array.Unboxed

primesSA = 2 : prs ()
  where 
    prs () = 3 : sieve 3 [] (prs ())
    sieve x fs (p:ps) = [i*2 + x | (i,True) <- assocs a] 
                        ++ sieve (p*p) fs2 ps
     where
      q     = (p*p-x)`div`2                  
      fs2   = (p,0) : [(s, rem (y-q) s) | (s,y) <- fs]
      a     :: UArray Int Bool
      a     = accumArray (\ b c -> False) True (1,q-1)
                         [(i,()) | (s,y) <- fs, i <- [y+s, y+s+s..q]]
```

#### As list comprehension

```mw
import Data.Array.Unboxed
import Data.List (tails, inits)

primes = 2 : [ n |
   (r:q:_, px) <- zip (tails (2 : [p*p | p <- primes]))
                      (inits primes),
   (n, True)   <- assocs ( accumArray (\_ _ -> False) True
                     (r+1,q-1)
                     [ (m,()) | p <- px
                              , s <- [ div (r+p) p * p]
                              , m <- [s,s+p..q-1] ] :: UArray Int Bool
                  ) ]
```

### Basic list-based sieve

Straightforward implementation of the sieve of Eratosthenes in its original bounded form. This finds primes in gaps between the composites, and composites as an enumeration of each prime's multiples.

```mw
primesTo m = eratos [2..m] where
   eratos (p : xs) 
      | p*p > m   = p : xs
      | otherwise = p : eratos (xs `minus` [p*p, p*p+p..m])
                                    -- map (p*) [p..]  
                                    -- map (p*) (p:xs)   -- (Euler's sieve)
   
minus a@(x:xs) b@(y:ys) = case compare x y of
         LT -> x : minus  xs b
         EQ ->     minus  xs ys
         GT ->     minus  a  ys
minus a        b        = a
```

Its time complexity is similar to that of optimal trial division because of limitations of Haskell linked lists, where `(minus a b)` takes time proportional to `length(union a b)` and not `(length b)`, as achieved in imperative setting with direct-access memory. Uses ordered list representation of sets.

This is reasonably useful up to ranges of fifteen million or about the first million primes.

### Unbounded list based sieve

Unbounded, "naive", too eager to subtract (see above for the definition of `minus`):

```mw
primesE  = sieve [2..] 
           where
           sieve (p:xs) = p : sieve (minus xs [p, p+p..])
-- unfoldr (\(p:xs)-> Just (p, minus xs [p, p+p..])) [2..]
```

This is slow, with complexity increasing as a square law or worse so that it is only moderately useful for the first few thousand primes or so.

The number of active streams can be limited to what's strictly necessary by postponement until the square of a prime is seen, getting a massive complexity improvement to better than *~ n1.5* so it can get first million primes or so in a tolerable time:

```mw
primesPE = 2 : sieve [3..] 4 primesPE
               where
               sieve (x:xs) q (p:t)
                 | x < q     = x : sieve xs q (p:t)
                 | otherwise =     sieve (minus xs [q, q+p..]) (head t^2) t
-- fix $ (2:) . concat 
--     . unfoldr (\(p:ps,xs)-> Just . second ((ps,) . (`minus` [p*p, p*p+p..])) 
--                                  . span (< p*p) $ xs) . (,[3..])
```

Transposing the workflow, going by segments between the consecutive squares of primes:

```mw
import Data.List (inits)

primesSE = 2 : sieve 3 4 (tail primesSE) (inits primesSE) 
               where
               sieve x q ps (fs:ft) =  
                  foldl minus [x..q-1] [[n, n+f..q-1] | f <- fs, let n=div x f * f]
                          -- [i|(i,True) <- assocs ( accumArray (\ b c -> False) 
                          --     True (x,q-1) [(i,()) | f <- fs, let n=div(x+f-1)f*f,
                          --         i <- [n, n+f..q-1]] :: UArray Int Bool )]
                  ++ sieve q (head ps^2) (tail ps) ft
```

The basic gradually-deepening left-leaning `(((a-b)-c)- ... )` workflow of `foldl minus a bs` above can be rearranged into the right-leaning `(a-(b+(c+ ... )))` workflow of `minus a (foldr union [] bs)`. This is the idea behind Richard Bird's unbounded code presented in M. O'Neill's article, equivalent to:

```mw
primesB = _Y ( (2:) . minus [3..] . foldr (\p-> (p*p :) . union [p*p+p, p*p+2*p..]) [] )

--      = _Y ( (2:) . minus [3..] . _LU . map(\p-> [p*p, p*p+p..]) )
-- _LU ((x:xs):t) = x : (union xs . _LU) t             -- linear folding big union

_Y g = g (_Y g)  -- = g (g (g ( ... )))      non-sharing multistage fixpoint combinator
--                  = g . g . g . ...            ... = g^inf
--   = let x = g x in g x -- = g (fix g)     two-stage fixpoint combinator 
--   = let x = g x in x   -- = fix g         sharing fixpoint combinator

union a@(x:xs) b@(y:ys) = case compare x y of
         LT -> x : union  xs b
         EQ -> x : union  xs ys
         GT -> y : union  a  ys
```

Using `_Y` is meant to guarantee the separate supply of primes to be independently calculated, recursively, instead of the same one being reused, corecursively; thus the memory footprint is drastically reduced. This idea was introduced by M. ONeill as a double-staged production, with a separate primes feed.

The above code is also useful to a range of the first million primes or so. The code can be further optimized by fusing `minus [3..]` into one function, preventing a space leak with the newer GHC versions, getting the function `gaps` defined below.

### Tree-merging incremental sieve

Linear merging structure can further be replaced with an wiki.haskell.org/Prime_numbers#Tree_merging indefinitely deepening to the right tree-like structure, `(a-(b+((c+d)+( ((e+f)+(g+h)) + ... ))))`.

This merges primes' multiples streams in a *tree*-like fashion, as a sequence of balanced trees of `union` nodes, likely achieving theoretical time complexity only a *log n* factor above the optimal *n log n log (log n)*, for *n* primes produced. Indeed, empirically it runs at about *~ n1.2* (for producing first few million primes), similarly to priority-queue–based version of M. O'Neill's, and with very low space complexity too (not counting the produced sequence of course):

```mw
primes :: () -> [Int]   
primes() = 2 : _Y ((3:) . gaps 5 . _U . map(\p-> [p*p, p*p+2*p..])) where
  _Y g = g (_Y g)  -- = g (g (g ( ... )))   non-sharing multistage fixpoint combinator
  gaps k s@(c:cs) | k < c     = k : gaps (k+2) s  -- ~= ([k,k+2..] \\ s)
                  | otherwise =     gaps (k+2) cs --   when null(s\\[k,k+2..]) 
  _U ((x:xs):t) = x : (merge xs . _U . pairs) t   -- tree-shaped folding big union
  pairs (xs:ys:t) = merge xs ys : pairs t
  merge xs@(x:xt) ys@(y:yt) | x < y     = x : merge xt ys
                            | y < x     = y : merge xs yt
                            | otherwise = x : merge xt yt
```

Works with odds only, the simplest kind of wheel. Here's the test entry on Ideone.com, and a comparison with more versions.

#### With Wheel

Using `_U` defined above,

```mw
primesW :: [Int]   
primesW = [2,3,5,7] ++ _Y ( (11:) . gapsW 13 (tail wheel) . _U .
                            map (\p->  
                              map (p*) . dropWhile (< p) $
                                scanl (+) (p - rem (p-11) 210) wheel) )

gapsW k (d:w) s@(c:cs) | k < c     = k : gapsW (k+d) w s    -- set difference
                       | otherwise =     gapsW (k+d) w cs   --   k==c

wheel = 2:4:2:4:6:2:6:4:2:4:6:6:2:6:4:2:6:4:6:8:4:2:4:2:    -- gaps = (`gapsW` cycle [2])
        4:8:6:4:6:2:4:6:2:6:6:4:2:4:6:2:6:4:2:4:2:10:2:10:wheel
  -- cycle $ zipWith (-) =<< tail $ [i | i <- [11..221], gcd i 210 == 1]
```

Used here and here.

#### Improved efficiency Wheels

1. The generation of large wheels such as the 2/3/5/7/11/13/17 wheel, which has 92160 cyclic elements, needs to be done based on sieve culling which is much better as to performance and can be used without inserting the generated table.

2. Improving the means to re-generate the position on the wheel for the recursive base primes without the use of `dropWhile`, etc. The below improved code uses a copy of the place in the wheel for each found base prime for ease of use in generating the composite number to-be-culled chains.

```mw
-- autogenerates wheel primes, first sieve prime, and gaps
wheelGen :: Int -> ([Int],Int,[Int])
wheelGen n = loop 1 3 [2] [2] where
  loop i frst wps gps =
    if i >= n then (wps, frst, gps) else
    let nfrst = frst + head gps
        nhts = (length gps) * (frst - 1)
        cmpsts = scanl (\ c g -> c + frst * g)  (frst * frst) (cycle gps)
        cull n (g:gs') cs@(c:cs') og
            | nn >= c = cull nn gs' cs' (og + g) -- n == c; never greater!
            | otherwise = (og + g) : cull nn gs' cs 0 where nn = n + g
    in nfrst `seq` nhts `seq` loop (i + 1) nfrst (wps ++ [frst]) $ take nhts
                                $ cull nfrst (tail $ cycle gps) cmpsts 0

(wheelPrimes, firstSievePrime, gaps) = wheelGen 7

primesTreeFoldingWheeled :: () -> [Int]   
primesTreeFoldingWheeled() =    
    wheelPrimes ++ map fst (
      _Y ( ((firstSievePrime, wheel) :) .
               gapsW (firstSievePrime + head wheel, tail wheel) . _U .
                 map (\ (p,w) ->
                          scanl (\ c m -> c + m * p) (p * p) w ) ) ) where

  _Y g = g (_Y g) -- non-sharing multi-stage fixpoint Y-combinator

  wheel = cycle gaps

  gapsW k@(n,d:w) s@(c:cs) | n < c     = k : gapsW (n + d, w) s  -- set diff
                           | otherwise =     gapsW (n + d, w) cs --   n == c
 
  _U ((x:xs):t) = -- exactly the same as for odds-only!
      x : (union xs . _U . pairs) t where   -- tree-shaped folding big union
    pairs (xs:ys:t) = union xs ys : pairs t --  ~= nub . sort . concat
    union xs@(x:xs') ys@(y:ys')
      | x < y = x : union xs' ys
      | y < x = y : union xs ys'
      | otherwise = x : union xs' ys' -- x and y must be equal!
```

When compiled with -O2 optimization and -fllvm (the LLVM back end), the above code is over twice as fast as the Odds-Only version as it should be as that is about the ratio of reduced operations minus some slightly increased operation complexity, sieving the primes to a hundred million in about seven seconds on a modern middle range desktop computer. It is almost twice as fast as the "primesW" version due to the increased algorithmic efficiency!

Note that the "wheelGen" code could be used to not need to do further culling at all by continuously generating wheels until the square of the "firstSievePrime" is greater than the range as there are no composites left up to that limit, but this is always slower than a SoE due to the high overhead in generating the wheels - this would take a wheel generation of 1229 (number of primes to the square root of a hundred thousand is ten thousand) to create the required wheel sieved to a hundred million; however, the theoretical (if the time to advance through the lists per element were zero, which of course it is not) asymptotic performance would be O(n) instead of O(n log (log n)) where n is the range sieved. Just another case where theory supports (slightly) reduced number of operations, but practicality means that the overheads to do this are so big as to make it useless for any reasonable range ;-) !

### Priority Queue based incremental sieve

The above work is derived from the Epilogue of the Melissa E. O'Neill paper which is much referenced with respect to incremental functional sieves; however, that paper is now dated and her comments comparing list based sieves to her original work leading up to a Priority Queue based implementation is no longer current given more recent work such as the above Tree Merging version. Accordingly, a modern "odd's-only" Priority Queue version is developed here for more current comparisons between the above list based incremental sieves and a continuation of O'Neill's work.

In order to implement a Priority Queue version with Haskell, an efficient Priority Queue, which is not part of the standard Haskell libraries, is required. A Min Heap implementation is likely best suited for this task in providing the most efficient frequently used peeks of the next item in the queue and replacement of the first item in the queue (not using a "pop" followed by a "push) with "pop" operations then not used at all, and "push" operations used relatively infrequently. Judging by O'Neill's use of an efficient "deleteMinAndInsert" operation which she states "(We provide deleteMinAndInsert becausea heap-based implementation can support this operation with considerably less rearrangement than a deleteMin followed by an insert.)", which statement is true for a Min Heap Priority Queue and not others, and her reference to a priority queue by (Paulson, 1996), the queue she used is likely the one as provided as a simple true functional Min Heap implementation on RosettaCode, from which the essential functions are reproduced here:

```mw
data PriorityQ k v = Mt
                     | Br !k v !(PriorityQ k v) !(PriorityQ k v)
  deriving (Eq, Ord, Read, Show)

emptyPQ :: PriorityQ k v
emptyPQ = Mt
 
peekMinPQ :: PriorityQ k v -> Maybe (k, v)
peekMinPQ Mt           = Nothing
peekMinPQ (Br k v _ _) = Just (k, v)

pushPQ :: Ord k => k -> v -> PriorityQ k v -> PriorityQ k v
pushPQ wk wv Mt           = Br wk wv Mt Mt
pushPQ wk wv (Br vk vv pl pr)
             | wk <= vk   = Br wk wv (pushPQ vk vv pr) pl
             | otherwise  = Br vk vv (pushPQ wk wv pr) pl
 
siftdown :: Ord k => k -> v -> PriorityQ k v -> PriorityQ k v -> PriorityQ k v
siftdown wk wv Mt _          = Br wk wv Mt Mt
siftdown wk wv (pl @ (Br vk vv _ _)) Mt
    | wk <= vk               = Br wk wv pl Mt
    | otherwise              = Br vk vv (Br wk wv Mt Mt) Mt
siftdown wk wv (pl @ (Br vkl vvl pll plr)) (pr @ (Br vkr vvr prl prr))
    | wk <= vkl && wk <= vkr = Br wk wv pl pr
    | vkl <= vkr             = Br vkl vvl (siftdown wk wv pll plr) pr
    | otherwise              = Br vkr vvr pl (siftdown wk wv prl prr)
 
replaceMinPQ :: Ord k => k -> v -> PriorityQ k v -> PriorityQ k v
replaceMinPQ wk wv Mt             = Mt
replaceMinPQ wk wv (Br _ _ pl pr) = siftdown wk wv pl pr
```

The "peekMin" function retrieves both the key and value in a tuple so processing is required to access whichever is required for further processing. As well, the output of the peekMin function is a Maybe with the case of an empty queue providing a Nothing output.

The following code is O'Neill's original odds-only code (without wheel factorization) from her paper slightly adjusted as per the requirements of this Min Heap implementation as laid out above; note the `seq` adjustments to the "adjust" function to make the evaluation of the entry tuple more strict for better efficiency:

```mw
-- (c) 2006-2007 Melissa O'Neill.  Code may be used freely so long as
-- this copyright message is retained and changed versions of the file
-- are clearly marked.
--   the only changes are the names of the called PQ functions and the
--   included processing for the result of the peek function being a maybe tuple.

primesPQ() = 2 : sieve [3,5..]
  where
    sieve [] = []
    sieve (x:xs) = x : sieve' xs (insertprime x xs emptyPQ)
      where
        insertprime p xs table = pushPQ (p*p) (map (* p) xs) table
        sieve' [] table = []
        sieve' (x:xs) table
            | nextComposite <= x = sieve' xs (adjust table)
            | otherwise = x : sieve' xs (insertprime x xs table)
          where
            nextComposite = case peekMinPQ table of
                              Just (c, _) -> c
            adjust table
                | n <= x = adjust (replaceMinPQ n' ns table)
                | otherwise = table
              where (n, n':ns) = case peekMinPQ table of
                                   Just tpl -> tpl
```

The above code is almost four times slower than the version of the Tree Merging sieve above for the first million primes although it is about the same speed as the original Richard Bird sieve with the "odds-only" adaptation as above. It is slow and uses a huge amount of memory for primarily one reason: over eagerness in adding prime composite streams to the queue, which are added as the primes are listed rather than when they are required as the output primes stream reaches the square of a given base prime; this over eagerness also means that the processed numbers must have a large range in order to not overflow when squared (as in the default Integer = infinite precision integers as used here and by O'Neill, but Int64's or Word64's would give a practical range) which processing of wide range numbers adds processing and memory requirement overhead. Although O'Neill's code is elegant, it also loses some efficiency due to the extensive use of lazy list processing, not all of which is required even for a wheel factorization implementation.

The following code is adjusted to reduce the amount of lazy list processing and to add a secondary base primes stream (or a succession of streams when the combinator is used) so as to overcome the above problems and reduce memory consumption to only that required for the primes below the square root of the currently sieved number; using this means that 32-bit Int's are sufficient for a reasonable range and memory requirements become relatively negligible:

```mw
primesPQx :: () -> [Int]
primesPQx() = 2 : _Y ((3 :) . sieve 5 emptyPQ 9) -- initBasePrms
  where
    _Y g = g (_Y g)        -- non-sharing multi-stage fixpoint combinator OR

    sieve n table q bps@(bp:bps')
        | n >= q = let nbp = head bps' in let ntbl = insertprime bp table in
                   ntbl `seq` sieve (n + 2) ntbl (nbp * nbp) bps'
        | n >= nextComposite = let ntbl = adjust table in
                               ntbl `seq` sieve (n + 2) ntbl q bps
        | otherwise = n : sieve (n + 2) table q bps
      where
        insertprime p table = let adv = 2 * p in let nv = p * p + adv
                              in nv `seq` pushPQ nv adv table
        nextComposite = case peekMinPQ table of
                          Nothing -> q -- at beginning when queue empty!
                          Just (c, _) -> c
        adjust table
            | c <= n = let ntbl = replaceMinPQ (c + adv) adv table
                       in ntbl `seq` adjust ntbl
            | otherwise = table
          where (c, adv) = case peekMinPQ table of Just ct -> ct `seq` ct
```

The above code is over five times faster than the previous (O'Neill) Priority Queue code half again faster than the Tree-Merging Odds-Only code for a range of a hundred million primes; it is likely faster as the Min Heap is slightly more efficient than Tree Merging due to better tree balancing.

Since the Tree-Folding version above includes the minor changes to work with a factorization wheel, this should have the same minor modifications for comparison purposes, with the code as follows:

```mw
-- Note:  this code segment uses the same wheelGen as the Tree-Folding version...

primesPQWheeled :: () -> [Int]
primesPQWheeled() =
    wheelPrimes ++ map fst (
      _Y (((firstSievePrime, wheel) :) .
            sieve (firstSievePrime + head wheel, tail wheel)
                  emptyPQ (firstSievePrime * firstSievePrime)) )
  where
    _Y g = g (_Y g)        -- non-sharing multi-stage fixpoint combinator OR

    wheel = cycle gaps

    sieve npr@(n,(g:gs')) table q bpprs@(bppr:bpprs')
        | n >= q =
            let (nbp,_) = head bpprs' in let ntbl = insertprime bppr table in
            nbp `seq` ntbl `seq` sieve (n + g, gs') ntbl (nbp * nbp) bpprs'
        | n >= nextComposite = let ntbl = adjust table in
                               ntbl `seq` sieve (n + g, gs') ntbl q bpprs
        | otherwise = npr : sieve (n + g, gs') table q bpprs
      where
        insertprime (p,(pg:pgs')) table =
          let nv = p * (p + pg) in nv `seq` pushPQ nv (map (* p) pgs') table
        nextComposite = case peekMinPQ table of
                          Nothing -> q -- at beginning when queue empty!
                          Just (c, _) -> c
        adjust table
            | c <= n = let ntbl = replaceMinPQ (c + a) as' table
                       in ntbl `seq` adjust ntbl
            | otherwise = table
          where (c, (a:as')) = case peekMinPQ table of Just ct -> ct `seq` ct
```

Compiled with -O2 optimization and -fllvm (the LLVM back end), this code gains about the expected ratio in performance in sieving to a range of a hundred million, sieving to this range in about five seconds on a modern medium range desktop computer. This is likely the fastest purely functional incremental type SoE useful for moderate ranges up to about a hundred million to a billion.

### Page Segmented Sieve using a mutable unboxed array

All of the above unbounded sieves are quite limited in practical sieving range due to the large constant factor overheads in computation, making them mostly just interesting intellectual exercises other than for small ranges of up to about the first million to ten million primes; the following **"odds-only"** page-segmented version using (bit-packed internally) mutable unboxed arrays is about 50 times faster than the fastest of the above algorithms for ranges of about that and higher, making it practical for the first several hundred million primes:

```mw
{-# OPTIONS_GHC -O2 -fllvm #-} -- use LLVM for about double speed!

import Data.Int ( Int64 )
import Data.Word ( Word64 )
import Data.Bits ( Bits(shiftR) )
import Data.Array.Base ( IArray(unsafeAt), UArray(UArray),     
                         MArray(unsafeWrite), unsafeFreezeSTUArray ) 
import Control.Monad ( forM_ )
import Data.Array.ST ( MArray(newArray), runSTUArray )

type Prime = Word64

cSieveBufferRange :: Int
cSieveBufferRange = 2^17 * 8 -- CPU L2 cache in bits

primes :: () -> [Prime]
primes() = 2 : _Y (listPagePrms . pagesFrom 0) where
  _Y g = g (_Y g) -- non-sharing multi-stage fixpoint combinator
  szblmt = cSieveBufferRange - 1
  listPagePrms pgs@(hdpg@(UArray lwi _ rng _) : tlpgs) =
    let loop i | i >= fromIntegral rng = listPagePrms tlpgs
               | unsafeAt hdpg i = loop (i + 1)
               | otherwise = let ii = lwi + fromIntegral i in
                             case fromIntegral $ 3 + ii + ii of
                               p -> p `seq` p : loop (i + 1) in loop 0
  makePg lwi bps = runSTUArray $ do
    let limi = lwi + fromIntegral szblmt
        bplmt = floor $ sqrt $ fromIntegral $ limi + limi + 3
        strta bp = let si = fromIntegral $ (bp * bp - 3) `shiftR` 1
                   in if si >= lwi then fromIntegral $ si - lwi else
                   let r = fromIntegral (lwi - si) `mod` bp
                   in if r == 0 then 0 else fromIntegral $ bp - r
    cmpsts <- newArray (lwi, limi) False
    fcmpsts <- unsafeFreezeSTUArray cmpsts
    let cbps = if lwi == 0 then listPagePrms [fcmpsts] else bps
    forM_ (takeWhile (<= bplmt) cbps) $ \ bp ->
      forM_ (let sp = fromIntegral $ strta bp
             in [ sp, sp + fromIntegral bp .. szblmt ]) $ \c ->
        unsafeWrite cmpsts c True
    return cmpsts
  pagesFrom lwi bps = map (`makePg` bps)
                          [ lwi, lwi + fromIntegral szblmt + 1 .. ]
```

The above code as written has a maximum practical range of about 10^12 or so in about an hour.

The above code takes only a few tens of milliseconds to compute the first million primes and a few seconds to calculate the first 50 million primes up to a billion, with over half of those times expended in just enumerating the result lazy list. A further improvement to reduce the computational cost of repeated list processing across the base pages for every page segment would be to store the required base primes (or base prime gaps) in a lazy list of base prime arrays; in that way the scans across base primes per page segment would just mostly be array accesses which are much faster than list enumeration.

Unlike many other other unbounded examples, this algorithm has the true Sieve of Eratosthenes computational time complexity of O(n log log n) where n is the sieving range with no extra "log n" factor while having a very low computational time cost per composite number cull of less than ten CPU clock cycles per cull (well under as in under 4 clock cycles for the Intel i7 using a page buffer size of the CPU L1 cache size).

There are other ways to make the algorithm faster including high degrees of wheel factorization, which can reduce the number of composite culling operations by a factor of about four for practical ranges, and multi-processing which can reduce the computation time proportionally to the number of available independent CPU cores, but there is little point to these optimizations as long as the lazy list enumeration is the bottleneck as it is starting to be in the above code. To take advantage of those optimizations, functions need to be provided that can compute the desired results without using list processing.

For ranges above about 10^14 where culling spans begin to exceed even an expanded size page array, other techniques need to be adapted such as such as automatically extending the sieving buffer size to the square root of the maximum range currently sieved and sieving by CPU L1/L2 cache sized segments/sections.

However, even with the above code and its limitations for large sieving ranges, the speeds will never come close to as slow as the other "incremental" sieve algorithms, as the time will never exceed about 20 CPU clock cycles per composite number cull, where the fastest of those other algorithms takes many hundreds of CPU clock cycles per cull.

**A faster method of counting primes with a similar algorithm**

To show the limitations of the individual prime enumeration, the following code has been refactored from the above to provide an alternate very fast method of counting the unset bits in the culled array (the primes = none composite) using a CPU native pop count instruction:

```mw
{-# LANGUAGE  FlexibleContexts #-}
{-# OPTIONS_GHC -O2 -fllvm #-} -- use LLVM for about double speed!

import Data.Time.Clock.POSIX ( getPOSIXTime ) -- for timing

import Data.Int ( Int64 )
import Data.Word ( Word64 )
import Data.Bits ( Bits((.&.), (.|.), shiftL, shiftR, popCount) )
import Control.Monad.ST ( ST, runST )
import Data.Array.Base ( IArray(unsafeAt), UArray(UArray), STUArray,
                         MArray(unsafeRead, unsafeWrite), castSTUArray,
                         unsafeThawSTUArray, unsafeFreezeSTUArray ) 
import Control.Monad ( forM_ )
import Data.Array.ST ( MArray(newArray), runSTUArray )

type Prime = Word64

cSieveBufferRange :: Int
cSieveBufferRange = 2^17 * 8 -- CPU L2 cache in bits

type PrimeNdx = Int64
type SieveBuffer = UArray PrimeNdx Bool
cWHLPRMS :: [Prime]
cWHLPRMS = [ 2 ]
cFRSTSVPRM :: Prime
cFRSTSVPRM = 3
primesPages :: () -> [SieveBuffer]
primesPages() = _Y (pagesFrom 0 . listPagePrms) where
  _Y g = g (_Y g) -- non-sharing multi-stage fixpoint Y-combinator
  szblmt = fromIntegral (cSieveBufferRange `shiftR` 1) - 1
  makePg lwi bps = runSTUArray $ do
    let limi = lwi + fromIntegral szblmt
        mxprm = cFRSTSVPRM + fromIntegral (limi + limi)
        bplmt = floor $ sqrt $ fromIntegral mxprm
        strta bp = let si = fromIntegral $ (bp * bp - cFRSTSVPRM) `shiftR` 1
                   in if si >= lwi then fromIntegral $ si - lwi else
                   let r = fromIntegral (lwi - si) `mod` bp
                   in if r == 0 then 0 else fromIntegral $ bp - r
    cmpsts <- newArray (lwi, limi) False
    fcmpsts <- unsafeFreezeSTUArray cmpsts
    let cbps = if lwi == 0 then listPagePrms [fcmpsts] else bps
    forM_ (takeWhile (<= bplmt) cbps) $ \ bp ->
      forM_ (let sp = fromIntegral $ strta bp
             in [ sp, sp + fromIntegral bp .. szblmt ]) $ \c ->
        unsafeWrite cmpsts c True
    return cmpsts
  pagesFrom lwi bps = map (`makePg` bps)
                          [ lwi, lwi + fromIntegral szblmt + 1 .. ]

-- convert a list of sieve buffers to a list of primes...
listPagePrms :: [SieveBuffer] -> [Prime]
listPagePrms pgs@(pg@(UArray lwi _ rng _) : pgstl) = bsprm `seq` loop 0 where
  bsprm = cFRSTSVPRM + fromIntegral (lwi + lwi)
  loop i | i >= rng = listPagePrms pgstl
         | unsafeAt pg i = loop (i + 1)
         | otherwise = case bsprm + fromIntegral (i + i) of
                         p -> p `seq` p : loop (i + 1)
 
primes :: () -> [Prime]
primes() = cWHLPRMS ++ listPagePrms (primesPages())

-- very fast using popCount by words technique...
countSieveBuffer :: Int -> UArray PrimeNdx Bool -> Int64
countSieveBuffer lstndx sb = fromIntegral $ runST $ do
  cmpsts <- unsafeThawSTUArray sb :: ST s (STUArray s PrimeNdx Bool)
  wrdcmpsts <-
    (castSTUArray :: STUArray s PrimeNdx Bool ->
                      ST s (STUArray s PrimeNdx Word64)) cmpsts
  let lstwrd = lstndx `shiftR` 6
      lstmsk = 0xFFFFFFFFFFFFFFFE `shiftL` (lstndx .&. 63) :: Word64
      loop wi cnt
        | wi < lstwrd = do
          v <- unsafeRead wrdcmpsts wi
          case cnt - popCount v of ncnt -> ncnt `seq` loop (wi + 1) ncnt
        | otherwise = do
            v <- unsafeRead wrdcmpsts lstwrd
            return $ fromIntegral (cnt - popCount (v .|. lstmsk))
  loop 0 (lstwrd * 64 + 64)

-- count the remaining un-marked composite bits using very fast popcount...
countPrimesTo :: Prime -> Int64
countPrimesTo limit =
  let lmtndx = fromIntegral $ (limit - 3) `shiftR` 1
      loop (pg@(UArray lwi lmti rng _) : pgstl) cnt
        | lmti >= lmtndx =
          (cnt + countSieveBuffer (fromIntegral $ lmtndx - lwi) pg)
        | otherwise = loop pgstl (cnt + countSieveBuffer (rng - 1) pg)
  in if limit < 3 then if limit < 2 then 0 else 1
     else loop (primesPages()) 1

-- test it...
main :: IO ()
main = do
  let limit = 10^9 :: Prime

  strt <- getPOSIXTime
--  let answr = length $ takeWhile (<= limit) $ primes()-- slow way
  let answr = countPrimesTo limit -- fast way
  stop <- answr `seq` getPOSIXTime -- force evaluation of answr b4 stop time!
  let elpsd = round $ 1e3 * (stop - strt) :: Int64
 
  putStr $ "Found " ++ show answr
  putStr $ " primes up to " ++ show limit
  putStrLn $ " in " ++ show elpsd ++ " milliseconds."
```

When compiled with the "fast way" commented out and the "slow way enabled, the time to find the number of primes up to one billion is about 3.65 seconds on an Intel Sandy Bridge i3-2100 at 3.1 Ghz; with the "fast way" enabled instead, the time is only about 1.45 seconds for the same range, both compiled with the LLVM back end. This shows that more than half of the time for the "slow way" is spent just producing and enumerating the list of primes!

On a Intel Sky Lake i5-2500 CPU @ 3.6 GHz (turbo boost for single threaded as here) compiled with LLVM and 256 Kilobyte buffer size (CPU L2 sized), using the fast counting method:

- takes 1.085 seconds to sieve to 10^9: about 3.81 CPU clocks per cull
- takes 126 seconds to sieve to 10^11: about 4.0 CPU clocks per cull

This shows a slight loss of efficiency in clocks per cull due to the average culling span size coming closer to the cull buffer span size, meaning that the loop overhead in address calculation and CPU L1 cache overflows increases just a bit for these relative ranges.

This an extra about 20% faster than using the Sandy Bridge i5-2100 above by more than the ratio of CPU clock speeds likely due to the better Instructions Per Clock of the newer Sky Lake architecture due to improved branch prediction and elision of a correctly predicted branch down to close to zero time.

This is about 25 to 30 per cent faster than not using LLVM for this Sky Lake processor due to the poor register allocation and optimizations by the Native Code Gnerator compared to LLVM.

### APL-style

Rolling set subtraction over the rolling element-wise addition on integers. Basic, slow, worse than quadratic in the number of primes produced, empirically:

```mw
zipWith (flip (!!)) [0..]    -- or: take n . last . take n ...
     . scanl1 minus 
     . scanl1 (zipWith (+)) $ repeat [2..]
```

Or, a wee bit faster:

```mw
unfoldr (\(a:b:t) -> Just . (head &&& (:t) . (`minus` b)
                                           . tail) $ a)
     . scanl1 (zipWith (+)) $ repeat [2..]
```

A bit optimized, much faster, with better complexity,

```mw
tail . concat 
     . unfoldr (\(a:b:t) -> Just . second ((:t) . (`minus` b))
                                 . span (< head b) $ a)
     . scanl1 (zipWith (+) . tail) $ tails [1..]
  -- $ [ [n*n, n*n+n..] | n <- [1..] ]
```

getting nearer to the functional equivalent of the `primesPE` above, i.e.

```mw
fix ( (2:) . concat 
      . unfoldr (\(a:b:t) -> Just . second ((:t) . (`minus` b))
                                  . span (< head b) $ a)
      . ([3..] :) . map (\p-> [p*p, p*p+p..]) )
```

An illustration:

```mw
> mapM_ (print . take 15) $ take 10 $ scanl1 (zipWith(+)) $ repeat [2..]
[  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16]
[  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
[  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
[  8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64]
[ 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
[ 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
[ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98,105,112]
[ 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96,104,112,120,128]
[ 18, 27, 36, 45, 54, 63, 72, 81, 90, 99,108,117,126,135,144]
[ 20, 30, 40, 50, 60, 70, 80, 90,100,110,120,130,140,150,160]

> mapM_ (print . take 15) $ take 10 $ scanl1 (zipWith(+) . tail) $ tails [1..]
[  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]
[  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
[  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
[ 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72]
[ 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[ 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96,102,108,114,120]
[ 49, 56, 63, 70, 77, 84, 91, 98,105,112,119,126,133,140,147]
[ 64, 72, 80, 88, 96,104,112,120,128,136,144,152,160,168,176]
[ 81, 90, 99,108,117,126,135,144,153,162,171,180,189,198,207]
[100,110,120,130,140,150,160,170,180,190,200,210,220,230,240]
```


## HicEst

```mw
REAL :: N=100,  sieve(N)

sieve = $ > 1     ! = 0 1 1 1 1 ...
DO i = 1, N^0.5
  IF( sieve(i) ) THEN
     DO j = i^2, N, i
       sieve(j) = 0
     ENDDO
  ENDIF
ENDDO

DO i = 1, N
  IF( sieve(i) ) WRITE() i
ENDDO
```


## Hobbes

| This example is **incorrect**. Please fix the code and remove this message.***Details:*** Not a true Sieve of Eratosthenes but rather a Trial Division Sieve due to modulo/% testing |
|---|

```mw
hasDivisor :: (int * int) -> bool
hasDivisor x = match x with
  | (n, d) -> if (d * d > n) then false else if (n % d == 0) then true else hasDivisor((n, d + 1))

isPrime :: int -> bool
isPrime n = if (n < 2) then false else not(hasDivisor((n, 2)))

sieve :: int -> [int]
sieve n = [k | k <- [2..n], isPrime(k)]

sieve(100)
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## Hoon

```mw
::  Find primes by the sieve of Eratosthenes
!:
|=  end=@ud
=/  index  2
=/  primes  `(list @ud)`(gulf 1 end)
|-  ^-  (list @ud)
?:  (gte index (lent primes))  primes
$(index +(index), primes +:(skid primes |=([a=@ud] &((gth a index) =(0 (mod a index))))))
```


## Icon and Unicon

```mw
 procedure main()
    sieve(100)
 end

 procedure sieve(n)
    local p,i,j
    p:=list(n, 1)
    every i:=2 to sqrt(n) & j:= i+i to n by i & p[i] == 1
      do p[j] := 0
    every write(i:=2 to n & p[i] == 1 & i)
 end
```

Alternatively using sets

```mw
 procedure main()
     sieve(100)
 end

 procedure sieve(n)
     primes := set()
     every insert(primes,1 to n)
     every member(primes,i := 2 to n) do
         every delete(primes,i + i to n by i)
     delete(primes,1)
     every write(!sort(primes))
end
```


## J

Generally, this task should be accomplished in J using

i.&.(p:inv)

. Here we take an approach that's more comparable with the other examples on this page.

Implementation:

```mw
sieve=: {{
  r=. 0#t=. y# j=.1
  while. y>j=.j+1 do.
    if. j{t do.
      t=. t > y$j{.1
      r=. r, j
    end.
  end.
}}
```

Example:

```mw
   sieve 100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

To see into how this works, we can change the definition:

```mw
sieve=: {{
  r=. 0#t=. y# j=.1
  while. y>j=.j+1 do.
    if. j{t do.
      echo j;(y$j{.1);t=. t > y$j{.1
      r=. r, j
    end.
  end.
}}
```

And go:

```mw
   sieve 10
┌─┬───────────────────┬───────────────────┐
│2│1 0 1 0 1 0 1 0 1 0│0 1 0 1 0 1 0 1 0 1│
└─┴───────────────────┴───────────────────┘
┌─┬───────────────────┬───────────────────┐
│3│1 0 0 1 0 0 1 0 0 1│0 1 0 0 0 1 0 1 0 0│
└─┴───────────────────┴───────────────────┘
┌─┬───────────────────┬───────────────────┐
│5│1 0 0 0 0 1 0 0 0 0│0 1 0 0 0 0 0 1 0 0│
└─┴───────────────────┴───────────────────┘
┌─┬───────────────────┬───────────────────┐
│7│1 0 0 0 0 0 0 1 0 0│0 1 0 0 0 0 0 0 0 0│
└─┴───────────────────┴───────────────────┘
2 3 5 7
```

Thus, here, `t` would select numbers which have not yet been determined to be a multiple of a prime number.
