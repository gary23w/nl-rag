---
title: "Fibonacci sequence (part 5/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/10
---

## Haskell

### Analytic

Works with

:

exact-real

version 0.12.5.1

Using Binet's formula and exact real arithmetic library we can calculate arbitrary Fibonacci number **exactly**.

```mw
import Data.CReal

phi = (1 + sqrt 5) / 2

fib :: (Integral b) => b -> CReal 0
fib n = (phi^^n - (-phi)^^(-n))/sqrt 5
```

Let's try it for large numbers:

```mw
λ> fib 10 :: CReal 0
55
(0.01 secs, 137,576 bytes)
λ> fib 100 :: CReal 0
354224848179261915075
(0.01 secs, 253,152 bytes)
λ> fib 10000 :: CReal 0
33644764876431783266621612005107543310302148460680063906564769974680081442166662368155595513633734025582065332680836159373734790483865268263040892463056431887354544369559827491606602099884183933864652731300088830269235673613135117579297437854413752130520504347701602264758318906527890855154366159582987279682987510631200575428783453215515103870818298969791613127856265033195487140214287532698187962046936097879900350962302291026368131493195275630227837628441540360584402572114334961180023091208287046088923962328835461505776583271252546093591128203925285393434620904245248929403901706233888991085841065183173360437470737908552631764325733993712871937587746897479926305837065742830161637408969178426378624212835258112820516370298089332099905707920064367426202389783111470054074998459250360633560933883831923386783056136435351892133279732908133732642652633989763922723407882928177953580570993691049175470808931841056146322338217465637321248226383092103297701648054726243842374862411453093812206564914032751086643394517512161526545361333111314042436854805106765843493523836959653428071768775328348234345557366719731392746273629108210679280784718035329131176778924659089938635459327894523777674406192240337638674004021330343297496902028328145933418826817683893072003634795623117103101291953169794607632737589253530772552375943788434504067715555779056450443016640119462580972216729758615026968443146952034614932291105970676243268515992834709891284706740862008587135016260312071903172086094081298321581077282076353186624611278245537208532365305775956430072517744315051539600905168603220349163222640885248852433158051534849622434848299380905070483482449327453732624567755879089187190803662058009594743150052402532709746995318770724376825907419939632265984147498193609285223945039707165443156421328157688908058783183404917434556270520223564846495196112460268313970975069382648706613264507665074611512677522748621598642530711298441182622661057163515069260029861704945425047491378115154139941550671256271197133252763631939606902895650288268608362241082050562430701794976171121233066073310059947366875
(0.02 secs, 4,847,128 bytes)
λ> fib (-10) :: CReal 0
-55
(0.01 secs, 138,408 bytes)
```

### Recursive

Simple definition, very inefficient.

```mw
fib x =
  if x < 1
    then 0
    else if x < 2
           then 1
           else fib (x - 1) + fib (x - 2)
```

### Recursive with Memoization

Very fast.

```mw
fib x =
  if x < 1
    then 0
    else if x == 1
           then 1
           else fibs !! (x - 1) + fibs !! (x - 2)
  where
    fibs = map fib [0 ..]
```

### Recursive with Memoization using memoized library

Even faster and simpler is to use a defined memoizer (e.g. from MemoTrie package):

```mw
import Data.MemoTrie
fib :: Integer -> Integer
fib = memo f where
   f 0 = 0
   f 1 = 1
   f n = fib (n-1) + fib (n-2)
```

You can rewrite this without introducing f explicitly

```mw
import Data.MemoTrie
fib :: Integer -> Integer
fib = memo $ \x -> case x of
   0 -> 0
   1 -> 1
   n -> fib (n-1) + fib (n-2)
```

Or using LambdaCase extension you can write it even shorter:

```mw
{-# Language LambdaCase #-}
import Data.MemoTrie
fib :: Integer -> Integer
fib = memo $ \case 
   0 -> 0
   1 -> 1
   n -> fib (n-1) + fib (n-2)
```

The version that supports negative numbers:

```mw
{-# Language LambdaCase #-}
import Data.MemoTrie
fib :: Integer -> Integer
fib = memo $ \case 
   0 -> 0
   1 -> 1
   n | n>0 -> fib (n-1) + fib (n-2)
     | otherwise -> fib (n+2) - fib (n+1)
```

### Iterative

```mw
fib n = go n 0 1
  where
    go n a b
      | n == 0 = a
      | otherwise = go (n - 1) b (a + b)
```

#### With lazy lists

This is a standard example how to use lazy lists. Here's the (infinite) list of all Fibonacci numbers:

```mw
fib = 0 : 1 : zipWith (+) fib (tail fib)
```

Or alternatively:

```mw
fib = 0 : 1 : (zipWith (+) <*> tail) fib
```

The *n*th Fibonacci number is then just `fib !! n`. The above is equivalent to

```mw
fib = 0 : 1 : next fib where next (a: t@(b:_)) = (a+b) : next t
```

Also

```mw
fib = 0 : scanl (+) 1 fib
```

#### As a fold

Accumulator holds last two members of the series:

```mw
import Data.List (foldl') --'

fib :: Integer -> Integer
fib n =
  fst $
  foldl' --'
    (\(a, b) _ -> (b, a + b))
    (0, 1)
    [1 .. n]
```

#### As an unfold

Create an infinite list of integers using an unfold. The nth fibonacci number is the nth number in the list.

```mw
import Data.List (unfoldr)

fibs :: [Integer]
fibs = unfoldr (\(x, y) -> Just (x, (y, x + y))) (0, 1)

fib n :: Integer -> Integer
fib n = fibs !! n
```

### With matrix exponentiation

Adapting the (rather slow) code from Matrix exponentiation operator, we can simply write:

```mw
import Data.List (transpose)

fib
  :: (Integral b, Num a)
  => b -> a
fib 0 = 0 -- this line is necessary because "something ^ 0" returns "fromInteger 1", which unfortunately
-- in our case is not our multiplicative identity (the identity matrix) but just a 1x1 matrix of 1
fib n = (last . head . unMat) (Mat [[1, 1], [1, 0]] ^ n)

-- Code adapted from Matrix exponentiation operator task ---------------------
(<+>)
  :: Num c
  => [c] -> [c] -> [c]
(<+>) = zipWith (+)

(<*>)
  :: Num a
  => [a] -> [a] -> a
(<*>) = (sum .) . zipWith (*)

newtype Mat a = Mat
  { unMat :: [[a]]
  } deriving (Eq)

instance Show a =>
         Show (Mat a) where
  show xm = "Mat " ++ show (unMat xm)

instance Num a =>
         Num (Mat a) where
  negate xm = Mat $ map (map negate) $ unMat xm
  xm + ym = Mat $ zipWith (<+>) (unMat xm) (unMat ym)
  xm * ym =
    Mat
      [ [ xs Main.<*> ys -- to distinguish from standard applicative operator
        | ys <- transpose $ unMat ym ]
      | xs <- unMat xm ]
  fromInteger n = Mat [[fromInteger n]]
  abs = undefined
  signum = undefined

-- TEST ----------------------------------------------------------------------
main :: IO ()
main = (print . take 10 . show . fib) (10 ^ 5)
```

So, for example, the hundred-thousandth Fibonacci number starts with the digits:

**Output:**

```
"2597406934"
```

### Generating Functions

Start by defining a Num instance for infinite power series:

```mw
import Data.Ratio (numerator)

infixl 7 *.
(*.) :: Num a => a -> [a] -> [a]
x *. (p:ps) = x*p : x*.ps

instance Num a => Num [a] where
    negate = map negate
    (+) = zipWith (+)
    (*) (p:ps) (q:qs) = p*q : ((p*.qs) + ps*(q:qs))
    fromInteger n = fromInteger n:repeat 0

instance (Eq a, Fractional a) => Fractional [a] where
    (/) (0:ps) (0:qs) = ps/qs
    (/) (p:ps) (q:qs) = let r=p/q in r : (ps - r*.qs)/(q:qs)

    fromRational q = fromRational q:repeat 0
```

The generating function for the Fibonacci numbers is

${\displaystyle \sum _{n}F_{n}x^{n}={\frac {1}{1-x-x^{2}}}}$

We can express this in Haskell with just the Prelude:

```mw
fibs :: [Integer]
fibs = map numerator
    (1/(1 : (-1) : (-1) : repeat 0))
```

```mw
ghci> take 15 fibs
[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
```

### Escardó-Oliva Functional

We can use the history-dependent version of the Escardó-Oliva functional for course-of-value recursion, viz.

```mw
import Data.Functor.Identity (Identity (..))

fibs :: [Integer]
fibs = runIdentity (hsequence (repeat f))
    where f []  = Identity 1
          f [_] = Identity 1
          f xs  = Identity ((xs !! (i-1)) + (xs !! i))
              where i = length xs-1
```

where `hsequence` is defined as in the paper,

```mw
hsequence :: Monad m => [[x] -> m x] -> m [x]
hsequence []     = pure []
hsequence (r:rs) = do
    x <- r []
    xs <- hsequence [ \ys -> g (x:ys) | g <- rs ]
    pure (x:xs)
```

Notice that `fibs` is not recursive; the recursion is handled by the higher-order functional `hsequence`

```mw
ghci> take 17 fibs
[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
```

### With recurrence relations

Using `Fib[m=3n+r]` recurrence identities:

```mw
import Control.Arrow ((&&&))

fibstep :: (Integer, Integer) -> (Integer, Integer)
fibstep (a, b) = (b, a + b)

fibnums :: [Integer]
fibnums = map fst $ iterate fibstep (0, 1)

fibN2 :: Integer -> (Integer, Integer)
fibN2 m
  | m < 10 = iterate fibstep (0, 1) !! fromIntegral m
fibN2 m = fibN2_next (n, r) (fibN2 n)
  where
    (n, r) = quotRem m 3

fibN2_next (n, r) (f, g)
  | r == 0 = (a, b) -- 3n  ,3n+1
  | r == 1 = (b, c) -- 3n+1,3n+2
  | r == 2 = (c, d) -- 3n+2,3n+3   (*)
  where
    a =
      5 * f ^ 3 +
      if even n
        then 3 * f
        else (-3 * f) -- 3n
    b = g ^ 3 + 3 * g * f ^ 2 - f ^ 3 -- 3n+1
    c = g ^ 3 + 3 * g ^ 2 * f + f ^ 3 -- 3n+2
    d =
      5 * g ^ 3 +
      if even n
        then (-3 * g)
        else 3 * g -- 3(n+1)   (*)

main :: IO ()
main = print $ (length &&& take 20) . show . fst $ fibN2 (10 ^ 2)
```

**Output:**

```
(21,"35422484817926191507")
```

`(fibN2 n)` directly calculates a pair `(f,g)` of two consecutive Fibonacci numbers, `(Fib[n], Fib[n+1])`, from recursively calculated such pair at about `n/3`:

```mw
 *Main> (length &&& take 20) . show . fst $ fibN2 (10^6)
(208988,"19532821287077577316")
```

The above should take less than 0.1s to calculate on a modern box.

Other identities that could also be used are here. In particular, for *(n-1,n) ---> (2n-1,2n)* transition which is equivalent to the matrix exponentiation scheme, we have

```mw
f (n,(a,b)) = (2*n,(a*a+b*b,2*a*b+b*b))     -- iterate f (1,(0,1)) ; b is nth
```

and for *(n,n+1) ---> (2n,2n+1)* (derived from d'Ocagne's identity, for example),

```mw
g (n,(a,b)) = (2*n,(2*a*b-a*a,a*a+b*b))     -- iterate g (1,(1,1)) ; a is nth
```


## Haxe

### Iterative

```mw
static function fib(steps:Int, handler:Int->Void)
{
   var current = 0;
   var next = 1;
      
   for (i in 1...steps)
   {
      handler(current);

      var temp = current + next;
      current = next;
      next = temp;
   }
   handler(current);
}
```

### As Iterator

```mw
class FibIter
{
   private var current = 0;
   private var nextItem = 1;
   private var limit:Int;
   
   public function new(limit) this.limit = limit;

   public function hasNext() return limit > 0;
   
   public function next() {
      limit--;
      var ret = current;
      var temp = current + nextItem;
      current = nextItem;
      nextItem = temp;
      return ret;
   }
}
```

Used like:

```mw
for (i in new FibIter(10))
   Sys.println(i);
```


## HicEst

```mw
REAL :: Fibonacci(10)

Fibonacci = ($==2) + Fibonacci($-1) + Fibonacci($-2)
WRITE(ClipBoard) Fibonacci ! 0 1 1 2 3 5 8 13 21 34
```


## Hobbes

Recursive definition in a `.hob` script file:

```mw
fib :: int -> int
fib n =
  match n with
  | 0 -> 0
  | 1 -> 1
  | _ -> fib(n - 1) + fib(n - 2)
```

**Output:**

```
> [fib(n) | n <- [1..20]]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
```


## Hoon

```mw
|=  n=@ud
=/  a=@ud  0
=/  b=@ud  1
|-
?:  =(n 0)  a
$(a b, b (add a b), n (dec n))
```


## Hope

### Recursive

```mw
dec f : num -> num;
--- f 0 <= 0;
--- f 1 <= 1;
--- f(n+2) <= f n + f(n+1);
```

### Tail-recursive

```mw
dec fib : num -> num;
--- fib n <= l (1, 0, n)
    whererec l == \(a,b,succ c) => if c<1 then a else l((a+b),a,c)
                  |(a,b,0) => 0;
```

### With lazy lists

This language, being one of Haskell's ancestors, also has lazy lists. Here's the (infinite) list of all Fibonacci numbers:

```mw
dec fibs : list num;
--- fibs <= fs whererec fs == 0::1::map (+) (tail fs||fs);
```

The *n*th Fibonacci number is then just `fibs @ n`.


## Hy

Recursive implementation.

```mw
(defn fib [n]
    (if (< n 2)
        n
        (+ (fib (- n 2)) (fib (- n 1)))))
```


## IBM 1620 SPS

```mw
     START RCTY                ,,, RETURN CARRIAGE
     LOOP  BT  FIBO,FIBN       ,,, PASS FIBN VALUE TO FUNCTION FIBO
           AM  FIBN,1          ,,, ADD 1 TO FIBN
           CM  FIBN,20         ,,, LOOP OVER THE FIRST 20 FIBONACCI NUMBERS
           BNE LOOP            ,,, JUMP BACK TO LOOP IF 20 NOT YET REACHED
           H                   ,,, HALT WHEN DONE
     N     DC  5,0             ,,, INPUT VALUE N GOES HERE
     FIBO  CM  FIBO-1,3        ,,, START OF FIBONACCI FUNCTION
           BL  PRINT           ,,, JUMP TO PRINT AND OUTPUT 1 IF N LESS THAN 3
           TFM L2,2            ,,, OTHERWISE SET UP VARIABLES FOR SUMMATION LOOP
           TFM A,1
           TFM B,1
     LOOP2 TFM C,0             ,,, ITERATIVE LOOP FOR SUMMING VALUE
           A   C,A
           A   C,B
           TF  A,B
           TF  B,C
           AM  L2,1
           C   L2,FIBO-1
           BL  LOOP2
           WNTYB-3             ,,, OUTPUT B (SHOWING LAST 4 DIGITS)
           RCTY
           BB                  ,,, BRANCH BACK TO MAIN LOOP
     PRINT WNTYONE-3           ,,, OUTPUT 1
           RCTY
           BB                  ,,, BRANCH BACK TO MAIN LOOP
     FIBN  DC  5,1             ,,, WHICH FIBONACCI NUMBER TO PRINT
     ONE   DC  5,1
           DC  1,@             ,,, ADD A RECORD MARK SO ONE CAN BE PRINTED
     L2    DC  5,0             ,,, LOOP 2 INDEX
     A     DC  5,0
     B     DC  5,0
           DC  1,@             ,,, ADD A RECORD MARK SO B CAN BE PRINTED
     C     DC  5,0
           DENDSTART
```

**Output:**

```
0001
0001
0002
0003
0005
0008
0013
0021
0034
0055
0089
0144
0233
0377
0610
0987
1597
2584
4181
```


## Icon and Unicon

Icon has built-in support for big numbers. First, a simple recursive solution augmented by caching for non-negative input. This examples computes fib(1000) if there is no integer argument.

```mw
procedure main(args)
    write(fib(integer(!args) | 1000)
end

procedure fib(n)
    static fCache
    initial {
        fCache := table()
        fCache[0] := 0
        fCache[1] := 1
        }
    /fCache[n] := fib(n-1) + fib(n-2)
    return fCache[n]
end
```

Library:

Icon Programming Library

The above solution is similar to the one provided fib in memrfncs

Now, an O(logN) solution. For large N, it takes far longer to convert the result to a string for output than to do the actual computation. This example computes fib(1000000) if there is no integer argument.

```mw
procedure main(args)
    write(fib(integer(!args) | 1000000))
end

procedure fib(n)
    return fibMat(n)[1]
end

procedure fibMat(n)
    if n <= 0 then return [0,0]
    if n  = 1 then return [1,0]
    fp := fibMat(n/2)
    c := fp[1]*fp[1] + fp[2]*fp[2]
    d := fp[1]*(fp[1]+2*fp[2])
    if n%2 = 1 then return [c+d, d]
    else return [d, c]
end
```


## IDL

### Recursive

```mw
function fib,n
   if n lt 3 then return,1L else return, fib(n-1)+fib(n-2)
end
```

Execution time O(2^n) until memory is exhausted and your machine starts swapping. Around fib(35) on a 2GB Core2Duo.

### Iterative

```mw
function fib,n
  psum = (csum = 1uL)
  if n lt 3 then return,csum
  for i = 3,n do begin
    nsum = psum + csum
    psum = csum
    csum = nsum
  endfor
  return,nsum
end
```

Execution time O(n). Limited by size of uLong to fib(49)

### Analytic

```mw
function fib,n
  q=1/( p=(1+sqrt(5))/2 ) 
  return,round((p^n+q^n)/sqrt(5))
end
```

Execution time O(1), only limited by the range of LongInts to fib(48).


## Idris

### Analytic

```mw
fibAnalytic : Nat -> Double
fibAnalytic n = 
    floor $ ((pow goldenRatio n) - (pow (-1.0/goldenRatio) n))  / sqrt(5)
  where goldenRatio : Double 
        goldenRatio = (1.0 + sqrt(5)) / 2.0
```

### Recursive

```mw
fibRecursive : Nat -> Nat
fibRecursive Z = Z
fibRecursive (S Z) = (S Z)
fibRecursive (S (S n)) = fibRecursive (S n) + fibRecursive n
```

### Iterative

```mw
fibIterative : Nat -> Nat
fibIterative n = fibIterative' n Z (S Z)
  where fibIterative' : Nat -> Nat -> Nat -> Nat
        fibIterative' Z a _ = a
        fibIterative' (S n) a b = fibIterative' n b (a + b)
```

### Lazy

```mw
fibLazy : Lazy (List Nat)
fibLazy = 0 :: 1 :: zipWith (+) fibLazy (
              case fibLazy of
                (x::xs) => xs
                [] => [])
```


## J

The Fibonacci Sequence essay on the J Wiki presents a number of different ways of obtaining the nth Fibonacci number.

### Recursive

This implementation is doubly recursive except that results are cached across function calls:

```mw
fibN=: (-&2 +&$: <:)^:(1&<) M."0
```

An amusing variant using an array operand to `^:`:

```mw
fibN=: ([: +&$:/ <:^:1 2)^:(1&<) M."0
```

### Iterative

```mw
fibN=: [: {."1 +/\@|.@]^:[&0 1
```

**Examples:**

```mw
   fibN 12
144
   fibN  i.31
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
```


## Jactl

```mw
long fib(int n) { n <= 2 ? 1 : fib(n-1) + fib(n-2) }
```


## Java

### Iterative

```mw
public static long itFibN(int n)
{
 if (n < 2)
  return n;
 long ans = 0;
 long n1 = 0;
 long n2 = 1;
 for(n--; n > 0; n--)
 {
  ans = n1 + n2;
  n1 = n2;
  n2 = ans;
 }
 return ans;
}
```

```mw
/**
 * O(log(n))
 */
public static long fib(long n) {
    if (n <= 0)
   return 0;

    long i = (int) (n - 1);
    long a = 1, b = 0, c = 0, d = 1, tmp1,tmp2;

    while (i > 0) {
   if (i % 2 != 0) {
            tmp1 = d * b + c * a;
       tmp2 = d * (b + a) + c * b;
       a = tmp1;
       b = tmp2;
   }

        tmp1 = (long) (Math.pow(c, 2) + Math.pow(d, 2));
        tmp2 = d * (2 * c + d);
         
        c = tmp1;
        d = tmp2;

        i = i / 2;
    }
    return a + b;
}
```

### Recursive

```mw
public static long recFibN(final int n)
{
 return (n < 2) ? n : recFibN(n - 1) + recFibN(n - 2);
}
```

### Caching-recursive

A variant on recursive, that caches previous results, reducing complexity from O(n2) to simply O(n). Leveraging Java’s Map.computeIfAbsent makes this thread-safe, and the implementation pretty trivial.

```mw
public class Fibonacci {

    static final Map<Integer, Long> cache = new HashMap<>();
    static {
        cache.put(1, 1L);
        cache.put(2, 1L);
    }

    public static long get(int n)
    {
        return (n < 2) ? n : impl(n);
    }
    
    private static long impl(int n)
    {
        return cache.computeIfAbsent(n, k -> impl(k-1) + impl(k-2));
    }
}
```

### Analytic

This method works up to the 92nd Fibonacci number. After that, it goes out of range.

```mw
public static long anFibN(final long n)
{
 double p = (1 + Math.sqrt(5)) / 2;
 double q = 1 / p;
 return (long) ((Math.pow(p, n) + Math.pow(q, n)) / Math.sqrt(5));
}
```

### Tail-recursive

```mw
public static long fibTailRec(final int n)
{
 return fibInner(0, 1, n);
}

private static long fibInner(final long a, final long b, final int n)
{
 return n < 1 ? a : n == 1 ?  b : fibInner(b, a + b, n - 1);
}
```

### Streams

```mw
import java.util.function.LongUnaryOperator;
import java.util.stream.LongStream;

public class FibUtil {
 public static LongStream fibStream() {
  return LongStream.iterate( 1l, new LongUnaryOperator() {
   private long lastFib = 0;
   @Override public long applyAsLong( long operand ) {
    long ret = operand + lastFib;
    lastFib = operand;
    return ret;
   }
  });
 }
 public static long fib(long n) {
  return fibStream().limit( n ).reduce((prev, last) -> last).getAsLong();
 }
}
```


## JavaScript

### ES5

#### Recursive

Basic recursive function:

```mw
function fib(n) {
  return n<2?n:fib(n-1)+fib(n-2);
}
```

Can be rewritten as:

```mw
function fib(n) {
 if (n<2) { return n; } else { return fib(n-1)+fib(n-2); }
}
```

One possibility familiar to Scheme programmers is to define an internal function for iteration through anonymous tail recursion:

```mw
function fib(n) {
  return function(n,a,b) {
    return n>0 ? arguments.callee(n-1,b,a+b) : a;
  }(n,0,1);
}
```

### Iterative

```mw
function fib(n) {
  var a = 0, b = 1, t;
  while (n-- > 0) {
    t = a;
    a = b;
    b += t;
    console.log(a);
  }
  return a;
}
```

#### Memoization

With the keys of a dictionary,

```mw
var fib = (function(cache){
    return cache = cache || {}, function(n){
        if (cache[n]) return cache[n];
        else return cache[n] = n == 0 ? 0 : n < 0 ? -fib(-n)
            : n <= 2 ? 1 : fib(n-2) + fib(n-1);
    };
})();
```

with the indices of an array,

```mw
(function () {
    'use strict';

    function fib(n) {
        return Array.apply(null, Array(n + 1))
            .map(function (_, i, lst) {
                return lst[i] = (
                    i ? i < 2 ? 1 :
                    lst[i - 2] + lst[i - 1] :
                    0
                );
            })[n];
    }

    return fib(32);

})();
```

**Output:**

```
2178309
```

#### Y-Combinator

```mw
function Y(dn) {
    return (function(fn) {
        return fn(fn);
    }(function(fn) {
        return dn(function() {
            return fn(fn).apply(null, arguments);
        });
    }));
}
var fib = Y(function(fn) {
    return function(n) {
        if (n === 0 || n === 1) {
            return n;
        }
        return fn(n - 1) + fn(n - 2);
    };
});
```

#### Generators

```mw
function* fibonacciGenerator() {
    var prev = 0;
    var curr = 1;
    while (true) {
        yield curr;
        curr = curr + prev;
        prev = curr - prev;
    }
}
var fib = fibonacciGenerator();
```

### ES6

#### Memoized

If we want access to the whole preceding series, as well as a memoized route to a particular member, we can use an accumulating fold.

```mw
(() => {
    'use strict';

    // Nth member of fibonacci series

    // fib :: Int -> Int
    function fib(n) {
        return mapAccumL(([a, b]) => [
            [b, a + b], b
        ], [0, 1], range(1, n))[0][0];
    };

    // GENERIC FUNCTIONS

    // mapAccumL :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
    let mapAccumL = (f, acc, xs) => {
        return xs.reduce((a, x) => {
            let pair = f(a[0], x);

            return [pair[0], a[1].concat(pair[1])];
        }, [acc, []]);
    }

    // range :: Int -> Int -> Maybe Int -> [Int]
    let range = (m, n) =>
        Array.from({
            length: Math.floor(n - m) + 1
        }, (_, i) => m + i);

    // TEST
    return fib(32);

    // --> 2178309
})();
```

Otherwise, a simple fold will suffice.

Translation of

:

Haskell

(Memoized fold example)

```mw
(() => {
    'use strict';

    // fib :: Int -> Int
    let fib = n => range(1, n)
        .reduce(([a, b]) => [b, a + b], [0, 1])[0];

    // GENERIC [m..n]

    // range :: Int -> Int -> [Int]
    let range = (m, n) =>
        Array.from({
            length: Math.floor(n - m) + 1
        }, (_, i) => m + i);

    // TEST
    return fib(32);

    // --> 2178309
})();
```

**Output:**

```
2178309
```


## Joy

### Recursive

```mw
DEFINE fib == [small] [] [pred dup pred] [+] binrec.
```

### Iterative

```mw
DEFINE fib == [1 0] dip [swap [+] unary] times popd.
```


## jq

Works with

:

jq

**Works with gojq, the Go implementation of jq**

The C implementation of jq does not (yet) have infinite-precision integer arithmetic, and so using it, the following algorithms only give exact answers up to fib(78). By contrast, using the Go implementation of jq and the definition of nth_fib given below:

```mw
nth_fib(pow(2;20)) | tostring | [length, .[:10], .[-10:]]
```

yields

```
[219140,"1186800606","0691163707"]
```

in about 20 seconds on a 3GHz machine.

Using either the C or Go implementations, at a certain point, integers are converted to floats, but floating point precision for fib(n) fails after n = 1476: in jq, fib(1476) evaluates to 1.3069892237633987e+308

### Recursive

```mw
def nth_fib_naive(n):
  if (n < 2) then n
  else nth_fib_naive(n - 1) + nth_fib_naive(n - 2)
  end;
```

### Tail Recursive

Recent versions of jq (after July 1, 2014) include basic optimizations for tail recursion, and nth_fib is defined here to take advantage of TCO. For example, nth_fib(10000000) completes with only 380KB (that's K) of memory. However nth_fib can also be used with earlier versions of jq.

```mw
def nth_fib(n):
  # input: [f(i-2), f(i-1), countdown]
  def fib: (.[0] + .[1]) as $sum
    | .[2] as $n
    | if ($n <= 0) then $sum
      else [ .[1], $sum, $n - 1 ]
    | fib end;
  [-1, 1, n] | fib;
```

Example:

```mw
(range(0;5), 50) | [., nth_fib(.)]
```

yields:

```mw
[0,0]
[1,1]
[2,1]
[3,2]
[4,3]
[50,12586269025]
```

### Binet's Formula

```mw
def fib_binet(n):
  (5|sqrt) as $rt
  | ((1 + $rt)/2) as $phi
  | (($phi | log) * n | exp) as $phin
  | (if 0 == (n % 2) then 1 else -1 end) as $sign
  | ( ($phin - ($sign / $phin) ) / $rt ) + .5
  | floor;
```

### Generator

The following is a jq generator which produces the first n terms of the Fibonacci sequence efficiently, one by one. Notice that it is simply a variant of the above tail-recursive function. The function is in effect turned into a generator by changing "( _ | fib )" to "$sum, (_ | fib)".

```mw
# Generator
def fibonacci(n):
  # input: [f(i-2), f(i-1), countdown]
  def fib: (.[0] + .[1]) as $sum
           | if .[2] == 0 then $sum
             else $sum, ([ .[1], $sum, .[2] - 1 ] | fib)
             end;
  [-1, 1, n] | fib;
```


## Julia

### Recursive

```mw
fib(n) = n < 2 ? n : fib(n-1) + fib(n-2)
```

### Iterative

```mw
function fib(n)
  x,y = (0,1)
  for i = 1:n x,y = (y, x+y) end
  x
end
```

### Matrix form

```mw
fib(n) = ([1 1 ; 1 0]^n)[1,2]
```


## K

Works with

:

Kona

### Recursive

```mw
{:[x<3;1;+/_f'x-1 2]}
```

### Recursive with memoization

Using a (global) dictionary c.

```mw
{c::.();{v:c[a:`$$x];:[x<3;1;_n~v;c[a]:+/_f'x-1 2;v]}x}
```

### Analytic

```mw
phi:(1+_sqrt(5))%2
{_((phi^x)-((1-phi)^x))%_sqrt[5]}
```

### Iterative

Works with

:

ngn/k

```mw
+/[;0;1]
```

### Sequence to n

Works with

:

Kona

Works with

:

ngn/k

```mw
{(x(|+\)\1 1)[;1]}
```

```mw
{x{x,+/-2#x}/!2}
```

Works with

:

ngn/k

```mw
+\[;0;1]
```


## Kabap

### Sequence to n

```mw
// Calculate the $n'th Fibonacci number

// Set this to how many in the sequence to generate
$n = 10;

// These are what hold the current calculation
$a = 0;
$b = 1;

// This holds the complete sequence that is generated
$sequence = "";

// Prepare a loop
$i = 0;
:calcnextnumber;
   $i = $i++;

   // Do the calculation for this loop iteration
   $b = $a + $b;
   $a = $b - $a;

   // Add the result to the sequence
   $sequence = $sequence << $a;

   // Make the loop run a fixed number of times
   if $i < $n; {
      $sequence = $sequence << ", ";
      goto calcnextnumber;
   }

// Use the loop counter as the placeholder
$i--;

// Return the sequence
return = "Fibonacci number " << $i << " is " << $a << " (" << $sequence << ")";
```


## KatLang

```mw
Fib = {b~, a + b}.repeat(n, 0, 1):0
Fib(20)
```

**Output:**

```
6765
```


## Klingphix

```mw
:Fibonacci
    dup 0 less
    ( ["Invalid argument"]
      [1 1 rot 2 sub [drop over over add] for]
    ) if
;

30 Fibonacci pstack print nl

msec print nl
"bertlham " input
```


## Kotlin

```mw
enum class Fibonacci {
    ITERATIVE {
        override fun get(n: Int): Long = if (n < 2) {
            n.toLong()
        } else {
            var n1 = 0L
            var n2 = 1L
            repeat(n) {
                val sum = n1 + n2
                n1 = n2
                n2 = sum
            }
            n1
        }
    },
    RECURSIVE {
        override fun get(n: Int): Long = if (n < 2) n.toLong() else this[n - 1] + this[n - 2]
    },
    CACHING {
        val cache: MutableMap<Int, Long> = mutableMapOf(0 to 0L, 1 to 1L)
        override fun get(n: Int): Long = if (n < 2) n.toLong() else impl(n)
        private fun impl(n: Int): Long = cache.computeIfAbsent(n) { impl(it-1) + impl(it-2) }
    },
    ;
 
    abstract operator fun get(n: Int): Long
}
 
fun main() {
    val r = 0..30
    for (fib in Fibonacci.values()) {
        print("${fib.name.padEnd(10)}:")
        for (i in r) { print(" " + fib[i]) }
        println()
    }
}
```

**Output:**

```
ITERATIVE:  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
RECURSIVE:  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
CACHING   : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040
```


## L++

```mw
(defn int fib (int n) (return (? (< n 2) n (+ (fib (- n 1)) (fib (- n 2))))))
(main (prn (fib 30)))
```


## LabVIEW

This image is a VI Snippet, an executable image of LabVIEW code. The LabVIEW version is shown on the top-right hand corner. You can download it, then drag-and-drop it onto the LabVIEW block diagram from a file browser, and it will appear as runnable, editable code.


## Lambdatalk

```mw
1) basic version 
{def fib1 
 {lambda {:n}
  {if {< :n 3}
   then 1
   else {+ {fib1 {- :n 1}} {fib1 {- :n 2}}} }}}

{fib1 16} -> 987   (CPU ~ 16ms)
{fib1 30} = 832040 (CPU > 12000ms)

2) tail-recursive version
{def fib2
 {def fib2.r 
  {lambda {:a :b :i}
   {if {< :i 1} 
    then :a 
    else {fib2.r :b {+ :a :b} {- :i 1}} }}}
 {lambda {:n} {fib2.r 0 1 :n}}}

{fib2 16} -> 987    (CPU ~ 1ms)
{fib2 30} -> 832040 (CPU ~2ms)
{fib2 1000} -> 4.346655768693743e+208 (CPU ~ 22ms)  

3) Dijkstra Algorithm
{def fib3
 {def fib3.r
  {lambda {:a :b :p :q :count}
   {if {= :count 0}
    then :b
    else {if {= {% :count 2} 0}
    then {fib3.r :a :b
                {+ {* :p :p} {* :q :q}}
                {+ {* :q :q} {* 2 :p :q}}
                {/ :count 2}}
    else {fib3.r {+ {* :b :q} {* :a :q} {* :a :p}}
                {+ {* :b :p} {* :a :q}}
                :p :q
                {- :count 1}} }}}}
 {lambda {:n}
  {fib3.r 1 0 0 1 :n} }}

{fib3 16} -> 987    (CPU ~ 2ms)
{fib3 30} -> 832040 (CPU ~ 2ms)
{fib3 1000} -> 4.346655768693743e+208 (CPU ~ 3ms)  

4) memoization
{def fib4
 {def fib4.m {array.new}}    // init an empty array
 {def fib4.r {lambda {:n}
  {if {< :n 2}
   then {array.get {array.set! {fib4.m} :n 1} :n}      // init with 1,1
   else {if {equal? {array.get {fib4.m} :n} undefined} // if not exists
   then {array.get {array.set! {fib4.m} :n
                        {+ {fib4.r {- :n 1}}
                           {fib4.r {- :n 2}}}} :n}   // compute it
   else {array.get {fib4.m} :n} }}}}                   // else get it
 {lambda {:n}
  {fib4.r :n} 
  {fib4.m} }} // display the number AND all its predecessors
-> fib4
{fib4 90}  
-> 4660046610375530000 
[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,
317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,
165580141,267914296,433494437,701408733,1134903170,1836311903,2971215073,4807526976,7778742049,12586269025,
20365011074,32951280099,53316291173,86267571272,139583862445,225851433717,365435296162,591286729879,956722026041,
1548008755920,2504730781961,4052739537881,6557470319842,10610209857723,17167680177565,27777890035288,44945570212853,
72723460248141,117669030460994,190392490709135,308061521170129,498454011879264,806515533049393,1304969544928657,
2111485077978050,3416454622906707,5527939700884757,8944394323791464,14472334024676220,23416728348467684,
37889062373143900,61305790721611580,99194853094755490,160500643816367070,259695496911122560,420196140727489660,
679891637638612200,1100087778366101900,1779979416004714000,2880067194370816000,4660046610375530000]

5) Binet's formula (non recursive)
{def fib5 
 {lambda {:n}
  {let { {:n :n} {:sqrt5 {sqrt 5}} }
   {round {/ {- {pow {/ {+ 1 :sqrt5} 2} :n} 
                {pow {/ {- 1 :sqrt5} 2} :n}} :sqrt5}}} }}

{fib5 16} -> 987    (CPU ~ 1ms) 
{fib5 30} -> 832040 (CPU ~ 1ms)
{fib5 1000} -> 4.346655768693743e+208 (CPU ~ 1ms)
```


## Lang

### Iterative

```mw
fp.fib = ($n) -> {
   if($n < 2) {
      return $n
   }
   
   $prev = 1
   $cur = 1
   $i = 2
   while($i < $n) {
      $tmp = $cur
      $cur += $prev
      $prev = $tmp
      
      $i += 1
   }
   
   return $cur
}
```

### Recursive

```mw
fp.fib = ($n) -> {
   if($n < 2) {
      return $n
   }
   
   return parser.op(fp.fib($n - 1) + fp.fib($n - 2))
}
```


## Lang5

```mw
[] '__A set : dip swap __A swap 2 compress collapse '__A set execute
    __A -1 extract nip ;  : nip swap drop ;  : tuck swap over ;
: -rot rot rot ; : 0= 0 == ; : 1+ 1 + ; : 1- 1 - ; : sum '+ reduce ;
: bi 'keep dip execute ;  : keep over 'execute dip ;

: fib dup 1 > if dup 1- fib swap 2 - fib + then ;
: fib  dup 1 > if "1- fib" "2 - fib" bi + then ;
```


## langur

```mw
val fibonacci = fn(x number) { if(x < 2: x ; fn((x - 1)) + fn((x - 2))) }

writeln map(0..20, by=fibonacci)
```

```mw
val fibonacci = fn(x number) {
    for[f=[0, 1]] of x-1 {
        f &= [f[-1]+f[-2]]
    }
}

writeln fibonacci(20)
```

**Output:**

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
```


## Lasso

```mw
define fibonacci(n::integer) => {

   #n < 1 ? return false

   local(
      swap  = 0,
      n1    = 0,
      n2    = 1
   )

   loop(#n) => {
        #swap = #n1 + #n2;
        #n2 = #n1;
        #n1 = #swap;
   }
   return #n1

}

fibonacci(0) //->output false
fibonacci(1) //->output 1
fibonacci(2) //->output 1
fibonacci(3) //->output 2
```


## Latitude

### Recursive

```mw
fibo := {
  takes '[n].
  if { n <= 1. } then {
    n.
  } else {
    fibo (n - 1) + fibo (n - 2).
  }.
}.
```

### Memoization

```mw
fibo := {
  takes '[n].
  cache := here cache.
  { cache slot? (n ordinal). } ifFalse {
    cache slot (n ordinal) =
      if { n <= 1. } then {
        n.
      } else {
        fibo (n - 1) + fibo (n - 2).
      }.
  }.
  cache slot (n ordinal).
} tap {
  ;; Attach the cache to the method object itself.
  #'self cache := Object clone.
}.
```


## Lean

It runs on Lean 3.4.2:

```mw
-- Our first implementation is the usual recursive definition:
def fib1 : ℕ → ℕ 
| 0       := 0
| 1       := 1
| (n + 2) := fib1 n + fib1 (n + 1)

-- We can give a second more efficient implementation using an auxiliary function:
def fib_aux : ℕ → ℕ → ℕ → ℕ 
| 0 a b       := b
| (n + 1) a b := fib_aux n (a + b) a

def fib2 : ℕ → ℕ 
| n := fib_aux n 1 0

-- Use #eval to check computations:
#eval fib1 20
#eval fib2 20
```

It runs on Lean 4:

```mw
-- Naive version
def fib1 (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | 1 => 1
  | (k + 2) => fib1 k + fib1 (k + 1)

-- More efficient version
def fib_aux (n : Nat) (a : Nat) (b : Nat) : Nat :=
  match n with
  | 0 => b
  | (k + 1) => fib_aux k (a + b) a
 
def fib2 (n : Nat) : Nat :=
  fib_aux n 1 0

-- Examples
#eval fib1 20
#eval fib2 20
```


## LFE

### Recursive

```mw
(defun fib
  ((0) 0)
  ((1) 1)
  ((n)
    (+ (fib (- n 1))
       (fib (- n 2)))))
```

### Iterative

```mw
(defun fib
  ((n) (when (>= n 0))
    (fib n 0 1)))

(defun fib
  ((0 result _)
    result)
  ((n result next)
    (fib (- n 1) next (+ result next))))
```


## Lingo

### Recursive

```mw
on fib (n)
  if n<2 then return n
  return fib(n-1)+fib(n-2)
end
```

### Iterative

```mw
on fib (n)
  if n<2 then return n    
  fibPrev = 0
  fib = 1
  repeat with i = 2 to n
    tmp = fib
    fib = fib + fibPrev
    fibPrev = tmp
  end repeat
  return fib
end
```

### Analytic

```mw
on fib (n)
  sqrt5 = sqrt(5.0)
  p = (1+sqrt5)/2
  q = 1 - p
  return integer((power(p,n)-power(q,n))/sqrt5)
end
```


## Lisaac

```mw
- fib(n : UINTEGER_32) : UINTEGER_64 <- (
  + result : UINTEGER_64;
  (n < 2).if {
    result := n;
  } else {
    result := fib(n - 1) + fib(n - 2);
  };
  result
);
```


## LiveCode

```mw
-- Iterative, translation of the basic version.
function fibi n
    put 0 into aa
    put 1 into b
    repeat with i = 1 to n
        put aa + b into temp
        put b into aa
        put temp into b
    end repeat
    return aa
end fibi

-- Recursive
function fibr n
     if n <= 1 then
        return n
    else
        return fibr(n-1) + fibr(n-2)
    end if
end fibr
```


## LLVM

```mw
; This is not strictly LLVM, as it uses the C library function "printf".
; LLVM does not provide a way to print values, so the alternative would be
; to just load the string into memory, and that would be boring.

; Additional comments have been inserted, as well as changes made from the output produced by clang such as putting more meaningful labels for the jumps

$"PRINT_LONG" = comdat any
@"PRINT_LONG" = linkonce_odr unnamed_addr constant [5 x i8] c"%ld\0A\00", comdat, align 1

;--- The declaration for the external C printf function.
declare i32 @printf(i8*, ...)

;--------------------------------------------------------------------
;-- Function for calculating the nth fibonacci numbers
;--------------------------------------------------------------------
define i32 @fibonacci(i32) {
    %2 = alloca i32, align 4            ;-- allocate local copy of n
    %3 = alloca i32, align 4            ;-- allocate a
    %4 = alloca i32, align 4            ;-- allocate b
    store i32 %0, i32* %2, align 4      ;-- store copy of n
    store i32 0, i32* %3, align 4       ;-- a := 0
    store i32 1, i32* %4, align 4       ;-- b := 1
    br label %loop

loop:
    %5 = load i32, i32* %2, align 4     ;-- load n
    %6 = icmp sgt i32 %5, 0             ;-- n > 0
    br i1 %6, label %loop_body, label %exit

loop_body:
    %7 = load i32, i32* %3, align 4     ;-- load a
    %8 = load i32, i32* %4, align 4     ;-- load b
    %9 = add nsw i32 %7, %8             ;-- t = a + b
    store i32 %8, i32* %3, align 4      ;-- store a = b
    store i32 %9, i32* %4, align 4      ;-- store b = t
    %10 = load i32, i32* %2, align 4    ;-- load n
    %11 = add nsw i32 %10, -1           ;-- decrement n
    store i32 %11, i32* %2, align 4     ;-- store n
    br label %loop

exit:
    %12 = load i32, i32* %3, align 4    ;-- load a
    ret i32 %12                         ;-- return a
}

;--------------------------------------------------------------------
;-- Main function for printing successive fibonacci numbers
;--------------------------------------------------------------------
define i32 @main() {
    %1 = alloca i32, align 4            ;-- allocate index
    store i32 0, i32* %1, align 4       ;-- index := 0
    br label %loop

loop:
    %2 = load i32, i32* %1, align 4     ;-- load index
    %3 = icmp sle i32 %2, 12            ;-- index <= 12
    br i1 %3, label %loop_body, label %exit

loop_body:
    %4 = load i32, i32* %1, align 4     ;-- load index
    %5 = call i32 @fibonacci(i32 %4)
    %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @"PRINT_LONG", i32 0, i32 0), i32 %5)
    %7 = load i32, i32* %1, align 4     ;-- load index
    %8 = add nsw i32 %7, 1              ;-- increment index
    store i32 %8, i32* %1, align 4      ;-- store index
    br label %loop

exit:
    ret i32 0                           ;-- return EXIT_SUCCESS
}
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
```


## Logo

```mw
to fib "loop
make   "fib1 0
make   "fib2 1

type [You requested\ ]
type :loop
print [\ Fibonacci Numbers]
   type :fib1
   type [\  ]
   type :fib2  
   type [\  ]
   
make "loop :loop - 2
repeat :loop [ make "fibnew :fib1 + :fib2 type :fibnew type [\  ] make "fib1 :fib2 make "fib2 :fibnew ]
   print [\  ]
     
end
```


## LOLCODE

```mw
HAI 1.2
HOW DUZ I fibonacci YR N
  EITHER OF BOTH SAEM N AN 1 AN BOTH SAEM N AN 0
  O RLY?
    YA RLY, FOUND YR 1
    NO WAI
      I HAS A N1
      I HAS A N2
      N1 R DIFF OF N AN 1
      N2 R DIFF OF N AN 2
      N1 R fibonacci N1
      N2 R fibonacci N2
      FOUND YR SUM OF N1 AN N2
  OIC
IF U SAY SO
KTHXBYE
```


## LSL

Rez a box on the ground, and add the following as a New Script.

```mw
integer Fibonacci(integer n) {
   if(n<2) {
      return n;
   } else {
      return Fibonacci(n-1)+Fibonacci(n-2);
   }
}
default {
   state_entry() {
      integer x = 0;
      for(x=0 ; x<35 ; x++) {
         llOwnerSay("Fibonacci("+(string)x+")="+(string)Fibonacci(x));
      }
   }
}
```

Output:

```
Fibonacci(0)=0
Fibonacci(1)=1
Fibonacci(2)=1
Fibonacci(3)=2
Fibonacci(4)=3
Fibonacci(5)=5
Fibonacci(6)=8
Fibonacci(7)=13
Fibonacci(8)=21
Fibonacci(9)=34
Fibonacci(10)=55
Fibonacci(11)=89
Fibonacci(12)=144
Fibonacci(13)=233
Fibonacci(14)=377
Fibonacci(15)=610
Fibonacci(16)=987
Fibonacci(17)=1597
Fibonacci(18)=2584
Fibonacci(19)=4181
Fibonacci(20)=6765
Fibonacci(21)=10946
Fibonacci(22)=17711
Fibonacci(23)=28657
Fibonacci(24)=46368
Fibonacci(25)=75025
Fibonacci(26)=121393
Fibonacci(27)=196418
Fibonacci(28)=317811
Fibonacci(29)=514229
Fibonacci(30)=832040
Fibonacci(31)=1346269
Fibonacci(32)=2178309
Fibonacci(33)=3524578
Fibonacci(34)=5702887
```


## Lua

### Recursive

```mw
--calculates the nth fibonacci number. Breaks for negative or non-integer n.
function fibs(n) 
  return n < 2 and n or fibs(n - 1) + fibs(n - 2) 
end
```

### Pedantic Recursive

```mw
--more pedantic version, returns 0 for non-integer n
function pfibs(n)
  if n ~= math.floor(n) then return 0
  elseif n < 0 then return pfibs(n + 2) - pfibs(n + 1)
  elseif n < 2 then return n
  else return pfibs(n - 1) + pfibs(n - 2)
  end
end
```

### Tail Recursive

```mw
function a(n,u,s) if n<2 then return u+s end return a(n-1,u+s,u) end
function trfib(i) return a(i-1,1,0) end
```

### Table Recursive

```mw
fib_n = setmetatable({1, 1}, {__index = function(z,n) return n<=0 and 0 or z[n-1] + z[n-2] end})
```

### Table Recursive 2

```mw
-- table recursive done properly (values are actually saved into table;
-- also the first element of Fibonacci sequence is 0, so the initial table should be {0, 1}).
fib_n = setmetatable({0, 1}, {
  __index = function(t,n)
    if n <= 0 then return 0 end
    t[n] = t[n-1] + t[n-2]
    return t[n]
  end
})
```

### Iterative

```mw
function ifibs(n)
  local p0,p1=0,1
  for _=1,n do p0,p1 = p1,p0+p1 end
  return p0
end
```


## Luck

```mw
function fib(x: int): int = (
   let cache = {} in
   let fibc x = if x<=1 then x else (
      if x not in cache then
      cache[x] = fibc(x-1) + fibc(x-2);
      cache[x]
   ) in fibc(x)
);;
for x in range(10) do print(fib(x))
```


## Lush

```mw
(de fib-rec (n)
  (if (< n 2)
      n
     (+ (fib-rec (- n 2)) (fib-rec (- n 1)))))
```


## M2000 Interpreter

Return decimal type and use an Inventory (as closure) to store known return values. All closures are in scope in every recursive call (we use here lambda(), but we can use fib(), If we make Fib1=fib then we have to use lambda() for recursion.

```mw
Inventory K=0:=0,1:=1
fib=Lambda K (x as decimal)-> {
      If Exist(K, x) Then =Eval(K) :Exit
      Def Ret as Decimal
      Ret=If(x>1->Lambda(x-1)+Lambda(x-2), x)
      Append K, x:=Ret
      =Ret
}
\\ maximum 139
For i=1 to 139 {
      Print Fib(i)
}
```

Here an example where we use a BigNum class to make a Group which hold a stack of values, and take 14 digits per item in stack. We can use inventory to hold groups, so we use the fast fib() function from code above, where we remove the type definition of Ret variable, and set two first items in inventory as groups.

```mw
Class BigNum {
      a=stack
      Function Digits {
            =len(.a)*14-(14-len(str$(stackitem(.a,len(.a)) ,"")))
      }
      Operator "+" (n) {
            \\ we get a copy, but .a is pointer
             \\ we make a copy, and get a new pointer
            .a<=stack(.a)
            acc=0
            carry=0
            const d=100000000000000@
                  k=min.data(Len(.a), len(n.a))
                  i=each(.a, 1,k )
                  j=each(n.a, 1,k)
                  while  i, j {
                        acc=stackitem(i)+stackitem(j)+carry
                        carry= acc div d
                        return .a, i^+1:=acc mod d
                  } 
                  if len(.a)<len(n.a) Then  {
                        i=each(n.a, k+1, -1)
                        while i {
                              acc=stackitem(i)+carry
                              carry= acc div d
                              stack .a  {data acc mod d}
                        }
                  } ELse.if len(.a)>len(n.a) Then  {
                        i=each(.a, k+1, -1)
                        while i {
                              acc=stackitem(i)+carry
                              carry= acc div d
                              Return .a, i^+1:=acc mod d
                              if carry else exit
                        }     
                  }
                  if carry then stack .a { data carry}
      }
      Function tostring$ {
            if len(.a)=0 then ="0" : Exit
            if len(.a)=1 then =str$(Stackitem(.a),"") : Exit
            document buf$=str$(Stackitem(.a, len(.a)),"")
            for i=len(.a)-1 to  1 {
                  Stack .a {
                        buf$=str$(StackItem(i), "00000000000000")
                  }
            }
            =buf$
      }
      class:
      Module BigNum (s$) {
            s$=filter$(s$,"+-.,")
            if s$<>""  Then {
                  repeat {
                        If len(s$)<14 then Stack .a { Data  val(s$) }: Exit
                        Stack .a { Data  val(Right$(s$, 14)) }
                        S$=Left$(S$, len(S$)-14)
                  } Until S$=""
            }
      }
} 

Inventory K=0:=BigNum("0"),1:=BigNum("1")
fib=Lambda K (x as decimal)-> {
      If Exist(K, x) Then =Eval(K) :Exit
      Ret=If(x>1->Lambda(x-1)+Lambda(x-2), bignum(str$(x,"")))
      Append K, x:=Ret
      =Ret
}
\\ Using this to handle form  refresh by code
Set Fast!
For i=1 to 4000 {
      N=Fib(i)
      Print i
      Print N.tostring$()
      Refresh
}
```


## M4

```mw
define(`fibo',`ifelse(0,$1,0,`ifelse(1,$1,1,
`eval(fibo(decr($1)) + fibo(decr(decr($1))))')')')dnl
define(`loop',`ifelse($1,$2,,`$3($1) loop(incr($1),$2,`$3')')')dnl
loop(0,15,`fibo')
```


## MAD

```mw
            NORMAL MODE IS INTEGER
            
            INTERNAL FUNCTION(N)
            ENTRY TO FIB.
            A = 0
            B = 1
            THROUGH LOOP, FOR N=N, -1, N.E.0
            C = A + B
            A = B
LOOP        B = C
            FUNCTION RETURN A
            END OF FUNCTION
            
            THROUGH SHOW, FOR I=0, 1, I.GE.20
SHOW        PRINT FORMAT FNUM, I, FIB.(I)
            VECTOR VALUES FNUM = $4HFIB(,I2,4H) = ,I4*$
            END OF PROGRAM
```

**Output:**

```
FIB( 0) =    0
FIB( 1) =    1
FIB( 2) =    1
FIB( 3) =    2
FIB( 4) =    3
FIB( 5) =    5
FIB( 6) =    8
FIB( 7) =   13
FIB( 8) =   21
FIB( 9) =   34
FIB(10) =   55
FIB(11) =   89
FIB(12) =  144
FIB(13) =  233
FIB(14) =  377
FIB(15) =  610
FIB(16) =  987
FIB(17) = 1597
FIB(18) = 2584
FIB(19) = 4181
```


## Maple

```mw
> f := n -> ifelse(n<3,1,f(n-1)+f(n-2));
> f(2);
  1
> f(3);
  2
```
