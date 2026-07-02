---
title: "Fibonacci sequence (part 9/10)"
source: https://rosettacode.org/wiki/Fibonacci_sequence
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 9/10
---

## Rhovas

Solutions support arbitrarily large numbers as Rhovas's `Integer` type is arbitrary-precision (Java `BigInteger`). Additional notes:

- `require num >= 0;` asserts input range preconditions, throwing on negative numbers

### Iterative

Standard iterative solution using a `for` loop:

- `range(1, num, :incl)` creates an inclusive range (`1 <= i <= num`) for iteration.
  - The loop uses `_` as the variable name since the value is unused.

```mw
func fibonacci(num: Integer): Integer {
    require num >= 0;
    var previous = 1;
    var current = 0;
    for (val _ in range(1, num, :incl)) {
        val next = current + previous;
        previous = current;
        current = next;
    }
    return current;
}
```

### Recursive

Standard recursive solution using a pattern matching approach:

- `match` without arguments is a *conditional match*, which works like `if/else` chains.
- Rhovas doesn't perform tail-call optimization yet, hence why this solution isn't tail recursive.

```mw
func fibonacci(num: Integer): Integer {
    require num >= 0;
    match {
        num == 0: return 0;
        num == 1: return 1;
        else: return fibonacci(num - 1) + fibonacci(num - 2);
    }
}
```

### Negatives

Standard solution using a pattern matching approach, delegating to an existing `positiveFibonacci` solution (as shown above). For negative fibonacci numbers, odd inputs return positive results while evens return negatives.

```mw
func fibonacci(num: Integer): Integer {
    match {
        num >= 0: return positiveFibonacci(num);
        num.mod(2) != 0: return positiveFibonacci(-num);
        else: return -positiveFibonacci(-num);
    }
}
```


## Ring

```mw
give n
x = fib(n)
see n + " Fibonacci is : " + x

func fib nr if nr = 0 return 0 ok
            if nr = 1 return 1 ok 
            if nr > 1 return fib(nr-1) + fib(nr-2) ok
```


## Rockstar

### Iterative (minimized)

```mw
Fibonacci takes Number
  FNow is 0
  FNext is 1
  While FNow is less than Number
    Say FNow
    Put FNow into Temp
    Put FNow into FNext
    Put FNext plus Temp into FNext

Say Fibonacci taking 1000 (prints out highest number in Fibonacci sequence less than 1000)
```

### Iterative (idiomatic)

```mw
Love takes Time
My love was addictions
Put my love into your heart
Build it up
Until my love is as strong as Time
Whisper my love
Put my love into a river
Put your heart into my love
Put it with a river into your heart

Shout; Love taking 1000 (years, years)
```

The semicolon and the comment `(years, years)` in this version are there only for poetic effect

### Recursive

```mw
The Italian takes a lover, a kiss, a promise
love is population
hate is information
If a lover is love
Give back a kiss

If a lover is hate
Give back a promise

Knock a lover down
Put a promise with a kiss into my heart
Give back The Italian taking a lover, a promise, my heart

Listen to your heart
your mind is everything
your soul is opportunity
Whisper The Italian taking your heart, your mind, your soul
```


## Rocq

```mw
Fixpoint rec_fib (m : nat) (a : nat) (b : nat) : nat :=
  match m with
    | 0 => a
    | S k => rec_fib k b (a + b)
  end.

Definition fib (n : nat) : nat :=
  rec_fib n 0 1 .
```


## RPL

Works with

:

Halcyon Calc

version 4.2.7

### Iterative, with n<0 support

```
≪ IF DUP 0 < THEN NEG -1 OVER ^ ELSE 1 END
   SWAP 0 1
   0 4 ROLL START OVER + SWAP NEXT 
   SWAP DROP *
≫ '→FIB' STO

≪ { } 0 20 FOR j j →FIB + NEXT ≫ EVAL
```

### Recursive

```
≪ IF DUP 2 > THEN 
     DUP 1 - →FIB 
     SWAP 2 - →FIB + 
   ELSE SIGN END 
≫ '→FIB' STO
```

**Output:**

```
1: { 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 }
```

### Fast recursive

A much better recursive approach, based on the formulas: `F(2k) = [2*F(k-1) + F(k)]*F(k)` and `F(2k+1) = F(k)² + F(k+1)²`

```
≪ IF DUP 2 ≤ THEN SIGN ELSE
     IF DUP 2 MOD
     THEN 1 - 2 / DUP →FIB SQ SWAP 1 + →FIB SQ +
     ELSE 2 / DUP →FIB DUP ROT 1 - →FIB 2 * + *
   END END
≫ '→FIB' STO
```


## Ruby

### Iterative

```mw
def fib(n)
  if n < 2
    n
  else
    prev, fib = 0, 1
    (n-1).times do
      prev, fib = fib, fib + prev
    end
    fib
  end
end

p (0..10).map { |i| fib(i) }
```

Output:

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Recursive

```mw
def fib(n, sequence=[1])
  return sequence.last if n == 0

  current_number, last_number = sequence.last(2)
  sequence << current_number + (last_number or 0)

  fib(n-1, sequence)
end
```

### Recursive with Memoization

```mw
# Use the Hash#default_proc feature to
# lazily calculate the Fibonacci numbers.

fib = Hash.new do |f, n|
  f[n] = if n <= -2
           (-1)**(n + 1) * f[n.abs]
         elsif n <= 1
           n.abs
         else
           f[n - 1] + f[n - 2]
         end
end
# examples: fib[10] => 55, fib[-10] => (-55/1)
```

### Matrix

```mw
require 'matrix'

# To understand why this matrix is useful for Fibonacci numbers, remember
# that the definition of Matrix.**2 for any Matrix[[a, b], [c, d]] is
# is [[a*a + b*c, a*b + b*d], [c*a + d*b, c*b + d*d]].  In other words, the
# lower right element is computing F(k - 2) + F(k - 1) every time M is multiplied
# by itself (it is perhaps easier to understand this by computing M**2, 3, etc, and
# watching the result march up the sequence of Fibonacci numbers).

M = Matrix[[0, 1], [1,1]]

# Matrix exponentiation algorithm to compute Fibonacci numbers.
# Let M be Matrix [[0, 1], [1, 1]].  Then, the lower right element of M**k is
# F(k + 1).  In other words, the lower right element of M is F(2) which is 1, and the
# lower right element of M**2 is F(3) which is 2, and the lower right element
# of M**3 is F(4) which is 3, etc.
#
# This is a good way to compute F(n) because the Ruby implementation of Matrix.**(n)
# uses O(log n) rather than O(n) matrix multiplications.  It works by squaring squares
# ((m**2)**2)... as far as possible
# and then multiplying that by by M**(the remaining number of times).  E.g., to compute
# M**19, compute partial = ((M**2)**2) = M**16, and then compute partial*(M**3) = M**19.
# That's only 5 matrix multiplications of M to compute M*19. 
def self.fib_matrix(n)
  return 0 if n <= 0 # F(0)
  return 1 if n == 1 # F(1)
  # To get F(n >= 2), compute M**(n - 1) and extract the lower right element.
  return CS::lower_right(M**(n - 1))
end

# Matrix utility to return
# the lower, right-hand element of a given matrix.
def self.lower_right matrix
  return nil if matrix.row_size == 0
  return matrix[matrix.row_size - 1, matrix.column_size - 1]
end
```

### Generative

```mw
fib = Enumerator.new do |y|
  f0, f1 = 0, 1
  loop do
    y <<  f0
    f0, f1 = f1, f0 + f1
  end
end
```

Usage:

```
p fib.lazy.drop(8).next # => 21
```

Works with

:

Ruby

version 1.9

"Fibers are primitives for implementing light weight cooperative concurrency in Ruby. Basically they are a means of creating code blocks that can be paused and resumed, much like threads. The main difference is that they are never preempted and that the scheduling must be done by the programmer and not the VM." [2]

```mw
fib = Fiber.new do
  a,b = 0,1
  loop do
    Fiber.yield a
    a,b = b,a+b
  end
end
9.times {puts fib.resume}
```

using a lambda

```mw
def fib_gen
    a, b = 1, 1
    lambda {ret, a, b = a, b, a+b; ret}
end
```

```
irb(main):034:0> fg = fib_gen
=> #<Proc:0xb7cdf750@(irb):22>
irb(main):035:0> 9.times { puts fg.call}
1
1
2
3
5
8
13
21
34
=> 9
```

### Binet's Formula

```mw
def fib
    phi = (1 + Math.sqrt(5)) / 2
    ((phi**self - (-1 / phi)**self) / Math.sqrt(5)).to_i
end
```

```
1.9.3p125 :001 > def fib
1.9.3p125 :002?>   phi = (1 + Math.sqrt(5)) / 2
1.9.3p125 :003?>   ((phi**self - (-1 / phi)**self) / Math.sqrt(5)).to_i
1.9.3p125 :004?>   end
 => nil 
1.9.3p125 :005 > (0..10).map(&:fib)
 => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```


## Rust

### Iterative

```mw
fn main() {
    let mut prev = 0;
    // Rust needs this type hint for the checked_add method
    let mut curr = 1usize;

    while let Some(n) = curr.checked_add(prev) {
        prev = curr;
        curr = n;
        println!("{}", n);
    }
}
```

### Recursive

```mw
use std::mem;
fn main() {
    fibonacci(0,1);
}

fn fibonacci(mut prev: usize, mut curr: usize) {
    mem::swap(&mut prev, &mut curr);
    if let Some(n) = curr.checked_add(prev) {
        println!("{}", n);
        fibonacci(prev, n);
    }
}
```

### Recursive (with pattern matching)

```mw
fn fib(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        n => fib(n - 1) + fib(n - 2),
    }
}
```

### Tail recursive (with pattern matching)

```mw
fn fib_tail_recursive(nth: usize) -> usize {
  fn fib_tail_iter(n: usize, prev_fib: usize, fib: usize) -> usize {
    match n {
      0 => prev_fib,
      n => fib_tail_iter(n - 1, fib, prev_fib + fib),
    }
  }
  fib_tail_iter(nth, 0, 1)
}
```

### Analytic

```mw
fn main() {
    for num in fibonacci_sequence() {
        println!("{}", num);
    }
}

fn fibonacci_sequence() -> impl Iterator<Item = u64> {
    let sqrt_5 = 5.0f64.sqrt();
    let p = (1.0 + sqrt_5) / 2.0;
    let q = 1.0 / p;
    // The range is sufficient up to 70th Fibonacci number
    (0..1).chain((1..70).map(move |n| ((p.powi(n) + q.powi(n)) / sqrt_5 + 0.5) as u64))
}
```

### Using an Iterator

Iterators are very idiomatic in rust, though they may be overkill for such a simple problem.

```mw
use std::mem;

struct Fib {
    prev: usize,
    curr: usize,
} 

impl Fib {
    fn new() -> Self {
        Fib {prev: 0, curr: 1}
    }
}

impl Iterator for Fib {
    type Item = usize;
    fn next(&mut self) -> Option<Self::Item>{
        mem::swap(&mut self.curr, &mut self.prev);
        self.curr.checked_add(self.prev).map(|n| { 
            self.curr = n;
            n
        })
    }
}

fn main() {
    for num in Fib::new() {
        println!("{}", num);
    }
}
```

#### Iterator "Successors"

```mw
fn main() {
    std::iter::successors(Some((1u128, 0)), |&(a, b)| a.checked_add(b).map(|s| (b, s)))
        .for_each(|(_, u)| println!("{}", u));
}
```


## SAS

### Iterative

This code builds a table `fib` holding the first few values of the Fibonacci sequence.

```mw
data fib;
    a=0;
    b=1;
    do n=0 to 20;
       f=a;
       output;
       a=b;
       b=f+a;
    end;
    keep n f;
run;
```

### Naive recursive

This code provides a simple example of defining a function and using it recursively. One of the members of the sequence is written to the log.

```mw
options cmplib=work.f;

proc fcmp outlib=work.f.p;
    function fib(n);
    if n = 0 or n = 1
        then return(1);
        else return(fib(n - 2) + fib(n - 1));
    endsub;
run;

data _null_;
    x = fib(5);
    put 'fib(5) = ' x;
run;
```


## Sather

The implementations use the arbitrary precision class INTI.

```mw
class MAIN is

  -- RECURSIVE --
  fibo(n :INTI):INTI
    pre n >= 0
  is
    if n < 2.inti then return n; end;
    return fibo(n - 2.inti) + fibo(n - 1.inti);
  end;

  -- ITERATIVE --
  fibo_iter(n :INTI):INTI
    pre n >= 0
  is
    n3w :INTI;

    if n < 2.inti then return n; end;
    last ::= 0.inti; this ::= 1.inti;
    loop (n - 1.inti).times!;
      n3w := last + this;
      last := this;
      this := n3w;
    end;   
    return this;
  end;

  main is
    loop i ::= 0.upto!(16);
      #OUT + fibo(i.inti) + " ";
      #OUT + fibo_iter(i.inti) + "\n";
    end;
  end;

end;
```


## Scala

### Recursive

```mw
def fib(i: Int): Int = i match {
  case 0 => 0
  case 1 => 1
  case _ => fib(i - 1) + fib(i - 2)
}
```

### Lazy sequence

```mw
lazy val fib: LazyList[Int] = 0 #:: 1 #:: fib.zip(fib.tail).map { case (a, b) => a + b }
```

### Tail recursive

```mw
import scala.annotation.tailrec
@tailrec
final def fib(x: Int, prev: BigInt = 0, next: BigInt = 1): BigInt = x match {
  case 0 => prev
  case _ => fib(x - 1, next, next + prev)
}
```

### foldLeft

```mw
// Fibonacci using BigInt with LazyList.foldLeft optimized for GC (Scala v2.13 and above)
// Does not run out of memory for very large Fibonacci numbers
def fib(n: Int): BigInt = {

  def series(i: BigInt, j: BigInt): LazyList[BigInt] = i #:: series(j, i + j)

  series(1, 0).take(n).foldLeft(BigInt("0"))(_ + _)
}

// Small test
(0 to 13) foreach {n => print(fib(n).toString + " ")}

// result: 0 1 1 2 3 5 8 13 21 34 55 89 144 233
```

### Iterator

```mw
val it: Iterator[Int] = Iterator.iterate((0, 1)) { case (a, b) => (b, a + b) }.map(_._1)

def fib(n: Int): Int = it.drop(n).next()

// example:
println(it.take(13).mkString(",")) // prints: 0,1,1,2,3,5,8,13,21,34,55,89,144
```


## Scheme

### Iterative

```mw
(define (fib-iter n)
  (do ((num 2 (+ num 1))
       (fib-prev 1 fib)
       (fib 1 (+ fib fib-prev)))
      ((>= num n) fib)))
```

### Recursive

```mw
(define (fib-rec n)
  (if (< n 2)
      n
      (+ (fib-rec (- n 1))
         (fib-rec (- n 2)))))
```

This version is tail recursive:

```mw
(define (fib n)
  (let loop ((a 0) (b 1) (n n))
    (if (= n 0) a
        (loop b (+ a b) (- n 1)))))
```

### Recursive Sequence Generator

Although the tail recursive version above is quite efficient, it only generates the final nth Fibonacci number and not the sequence up to that number without wasteful repeated calls to the procedure/function.

The following procedure generates the sequence of Fibonacci numbers using a simplified version of a lazy list/stream - since no memoization is requried, it just implements future values by using a zero parameter lambda "thunk" with a closure containing the last and the pre-calculated next value of the sequence; in this way it uses almost no memory during the sequence generation other than as required for the last and the next values of the sequence (note that the test procedure does not generate a linked list to contain the elements of the sequence to show, but rather displays each one by one in sequence):

```mw
(define (fib)
  (define (nxt lv nv) (cons nv (lambda () (nxt nv (+ lv nv)))))
  (cons 0 (lambda () (nxt 0 1))))

;;; test...
(define (show-stream-take n strm)
  (define (shw-nxt n strm) (begin (display (car strm))
                                  (if (> n 1) (begin (display " ") (shw-nxt (- n 1) ((cdr strm)))) (display ")"))))
  (begin (display "(") (shw-nxt n strm)))
(show-stream-take 30 (fib))
```

**Output:**

```
(0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229)
```

### Dijkstra Algorithm

```mw
;;; Fibonacci numbers using Edsger Dijkstra's algorithm
;;; http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF

(define (fib n)
  (define (fib-aux a b p q count)
    (cond ((= count 0) b)
          ((even? count)
           (fib-aux a
                    b
                    (+ (* p p) (* q q))
                    (+ (* q q) (* 2 p q))
                    (/ count 2)))
          (else
           (fib-aux (+ (* b q) (* a q) (* a p))
                    (+ (* b p) (* a q))
                    p
                    q
                    (- count 1)))))
  (fib-aux 1 0 0 1 n))
```

### Schönhage Algorithm

```mw
(define (fast-fib-pair n)
  ;; By Arnold Schönhage, personal communication, 2004
  ;; returns f_n f_{n+1}
  (case n
    ((1) (values 1 1))
    ((2) (values 1 2))
    (else
     (let ((m (quotient n 2)))
       (call-with-values
           (lambda () (fast-fib-pair m))
         (lambda (f_m f_m+1)
           (let ((f_m^2   (square f_m))
                 (f_m+1^2 (square f_m+1)))
             (if (even? n)
                 (values (- (* 2 f_m+1^2)
                            (* 3 f_m^2)
                            (if (odd? m) -2 2))
                         (+ f_m^2 f_m+1^2))
                 (values (+ f_m^2 f_m+1^2)
                         (- (* 3 f_m+1^2)
                            (* 2 f_m^2)
                            (if (odd? m) -2 2)))))))))))

(call-with-values
    (lambda ()
      (fast-fib-pair 100000000))
  (lambda (f_n f_n+1)
    (display (list (modulo f_n 100000) (modulo f_n+1 100000)))
    (newline)))
```

**Output:**

```
(46875 37501)
```


## Scilab

```mw
    clear
    n=46
    f1=0; f2=1
    printf("fibo(%d)=%d\n",0,f1)
    printf("fibo(%d)=%d\n",1,f2)
    for i=2:n
        f3=f1+f2
        printf("fibo(%d)=%d\n",i,f3)
        f1=f2
        f2=f3
    end
```

**Output:**

```
...
fibo(43)=433494437
fibo(44)=701408733
fibo(45)=1134903170
fibo(46)=1836311903
```


## sed

```mw
#!/bin/sed -f

# First we need to convert each number into the right number of ticks 
# Start by marking digits
s/[0-9]/<&/g

# We have to do the digits manually.
s/0//g; s/1/|/g; s/2/||/g; s/3/|||/g; s/4/||||/g; s/5/|||||/g
s/6/||||||/g; s/7/|||||||/g; s/8/||||||||/g; s/9/|||||||||/g

# Multiply by ten for each digit from the front.
:tens
s/|</<||||||||||/g
t tens

# Done with digit markers
s/<//g

# Now the actual work.
:split
# Convert each stretch of n >= 2 ticks into two of n-1, with a mark between
s/|\(|\+\)/\1-\1/g
# Convert the previous mark and the first tick after it to a different mark
# giving us n-1+n-2 marks.
s/-|/+/g
# Jump back unless we're done.
t split
# Get rid of the pluses, we're done with them.
s/+//g

# Convert back to digits
:back
s/||||||||||/</g
s/<\([0-9]*\)$/<0\1/g
s/|||||||||/9/g;
s/|||||||||/9/g; s/||||||||/8/g; s/|||||||/7/g; s/||||||/6/g;
s/|||||/5/g; s/||||/4/g; s/|||/3/g; s/||/2/g; s/|/1/g;
s/</|/g
t back
s/^$/0/
```


## Seed7

### Recursive

```mw
const func integer: fib (in integer: number) is func
  result
    var integer: result is 1;
  begin
    if number > 2 then
      result := fib(pred(number)) + fib(number - 2);
    elsif number = 0 then
      result := 0;
    end if;
  end func;
```

Original source: [3]

### Iterative

This funtion uses a bigInteger result:

```mw
const func bigInteger: fib (in integer: number) is func
  result
    var bigInteger: result is 1_;
  local
    var integer: i is 0;
    var bigInteger: a is 0_;
    var bigInteger: c is 0_;
  begin
    for i range 1 to pred(number) do
      c := a;
      a := result;
      result +:= c;
    end for;
  end func;
```

Original source: [4]


## SequenceL

### Recursive

```mw
fibonacci(n) := 
      n when n < 2
   else
      fibonacci(n - 1) + fibonacci(n - 2);
```

Based on: [5]

### Tail Recursive

```mw
fibonacci(n) := fibonacciHelper(0, 1, n);
      
fibonacciHelper(prev, next, n) :=
      prev when n < 1
   else
      next when n = 1
   else
      fibonacciHelper(next, next + prev, n - 1);
```

### Matrix

```mw
fibonacci(n) := fibonacciHelper([[1,0],[0,1]], n);

fibonacciHelper(M(2), n) := 
   let
      N := [[1,1],[1,0]];
   in
      M[1,1] when n <= 1
   else
      fibonacciHelper(matmul(M, N), n - 1);

matmul(A(2), B(2)) [i,j] := sum( A[i,all] * B[all,j] );
```

Based on the C# version: [6]

Using the SequenceL Matrix Multiply solution: [7]


## SETL

```mw
$ Print out the first ten Fibonacci numbers
$ This uses Set Builder Notation, it roughly means
$ 'collect fib(n) forall n in {0,1,2,3,4,5,6,7,8,9,10}'
print({fib(n) : n in {0..10}});

$ Iterative Fibonacci function
proc fib(n);
    A := 0; B := 1; C := n;
    for i in {0..n} loop
        C := A + B;
        A := B;
        B := C;
    end loop;
    return C;
end proc;
```


## Shen

```mw
(define fib
  0 -> 0
  1 -> 1
  N -> (+ (fib (+ N 1)) (fib (+ N 2))) 
       where (< N 0)
  N -> (+ (fib (- N 1)) (fib (- N 2))))
```


## Sidef

### Iterative

```mw
func fib_iter(n) {
    var (a, b) = (0, 1)
    { (a, b) = (b, a+b) } * n
    return a
}
```

### Recursive

```mw
func fib_rec(n) {
    n < 2 ? n : (__FUNC__(n-1) + __FUNC__(n-2))
}
```

### Recursive with memoization

```mw
func fib_mem (n) is cached {
    n < 2 ? n : (__FUNC__(n-1) + __FUNC__(n-2))
}
```

### Closed-form

```mw
func fib_closed(n) {
    define S = (1.25.sqrt + 0.5)
    define T = (-S + 1)
    (S**n - T**n) / (-T + S) -> round
}
```

### Built-in

```mw
say fib(12)    #=> 144
```


## Simula

Straightforward iterative implementation.

```mw
INTEGER PROCEDURE fibonacci(n);
INTEGER n;
BEGIN
    INTEGER lo, hi, temp, i;
    lo := 0;
    hi := 1;
    FOR i := 1 STEP 1 UNTIL n - 1 DO
    BEGIN
        temp := hi;
        hi := hi + lo;
        lo := temp
    END;
    fibonacci := hi
END;
```


## SkookumScript

### Built-in

SkookumScript's `Integer` class has a fast built-in `fibonnaci()` method.

```mw
42.fibonacci
```

SkookumScript is designed to work in tandem with C++ and its strength is at the high-level stage-direction of things. So when confronted with benchmarking scripting systems it is genrally better to make a built-in call. Though in most practical cases this isn't necessary.

### Recursive

Simple recursive method in same `42.fibonacci` form as built-in form above.

```mw
// Assuming code is in Integer.fibonacci() method
() Integer
  [
  if this < 2 [this] else [[this - 1].fibonacci + [this - 2].fibonacci]
  ]
```

Recursive procedure in `fibonacci(42)` form.

```mw
// Assuming in fibonacci(n) procedure
(Integer n) Integer
  [
  if n < 2 [n] else [fibonacci(n - 1) + fibonacci(n - 2)]
  ]
```

### Iterative

Iterative method in `42.fibonacci` form.

```mw
// Assuming code is in Integer.fibonacci() method
() Integer
  [
  if this < 2
    [this]
  else
    [
    !prev: 1
    !next: 1
    2.to_pre this
      [
      !sum :  prev + next
      prev := next
      next := sum
      ]
      
    next
    ]    
  ]
```

Optimized iterative method in `42.fibonacci` form. Though the best optimiation is to write it in C++ as with the built-in form that comes with SkookumScript.

```mw
// Bind : is faster than assignment :=
// loop is faster than to_pre (which uses a closure)
() Integer
  [
  if this < 2
    [this]
  else
    [
    !prev: 1
    !next: 1
    !sum
    !count: this - 2
    loop
      [
      if count = 0 [exit]
      count--
      sum  : prev + next
      prev : next
      next : sum
      ]
      
    next
    ]    
  ]
```


## Slate

```mw
n@(Integer traits) fib
[
  n <= 0 ifTrue: [^ 0].
  n = 1 ifTrue: [^ 1].
  (n - 1) fib + (n - 2) fib
].

slate[15]> 10 fib = 55.
True
```


## Smalltalk

Smalltalk already has a builtin fib in the Integer class (so I call them fibI and fibR in the code below, to not overwrite it). The integer algorithms below are all naive; there are faster ways to do it (see benchmark at the end). I gave the recursive version roughly 100Mb of stack. The analytical computation generates inexact results and fails for arguments somewhere above 1470 due to floating point overflow (with extended precision, the overflow appears a bit later).

iterative (slow):

```mw
Integer >> fibI
    |aNMinus1 an t|

    aNMinus1 := 1.
    an := 0.
    self timesRepeat:[
        t := an.
        an := an + aNMinus1 .
        aNMinus1 := t.
    ].
    ^ an
```

The recursive version although nice to read is the worst; it suffers from a huge stack requirement and a super poor performance (an anti-example for recursion):

```mw
Integer >> fibR
    (self > 1) ifTrue:[
        ^ (self - 1) fibR + (self - 2) fibR
    ].
    ^ self
```

analytic (fast, but inexact, and limited to small n below 1475 if we use double precision IEEE floats):

```mw
Integer >> fibBinet
    |phi rPhi|

    phi := Float phi.
    rPhi := 1 / phi.

    ^ (1 / 5 sqrt) * ((phi raisedTo:self) - (rPhi raisedTo:self))
```

using more bits in the exponent, we can compute larger fibs (up to 23599 with x86 extended precision floats), but still inexact:

```mw
Integer >> fibBinetFloatE
    |phi rPhi|

    phi := FloatE phi.
    rPhi := 1 / phi.

    ^ (1 / 5 sqrt) * ((phi raisedTo:self) - (rPhi raisedTo:self))
```

```mw
(10 to:1e6 byFactor:10) do:[:n |
  Transcript printCR:'----',n,'----'.
  Transcript printCR: n fibI.
  Transcript printCR: ([[n fibR] on:RecursionError do:['recursion']] valueWithTimeout:30 seconds) ? 'timeout'.
  Transcript printCR: n fibBinet.
  Transcript printCR: n fibBinetFloatE.
].

Transcript cr; showCR:'Timing:'; showCR:'------'.
[ 1000 fibI ] benchmark:'1000 fibI'.
[ 1000 fibR ] benchmark:'1000 fibR' timeLimit:30 seconds.
[ 1000 fibBinet ] benchmark:'1000 fibBinet'.
[ 1000 fibBinetFloatE] benchmark:'1000 fibBinetFloatE'.
[ 1000 fib ] benchmark:'1000 fib (builtin)'.

[ 10000 fibI ] benchmark:'10000 fibI'.
[ 10000 fib ] benchmark:'10000 fib (builtin)'.

[ 100000 fibI ] benchmark:'100000 fibI'.
[ 100000 fib ] benchmark:'100000 fib (builtin)'.

[ 1000000 fibI ] benchmark:'100000 fibI'.
[ 1000000 fib ] benchmark:'1000000 fib (builtin)'.
[ 2000000 fib ] benchmark:'2000000 fib (builtin)'.
[ 10000000 fib ] benchmark:'10000000 fib (builtin)'
```

**Output:**

```
----10----
55
55
55.0
54.99999999999
----100----
354224848179261915075
timeout
3.54224848179262E+020
3.54224848179263E+020
----1000----
43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
timeout
4.34665576869373E+208
4.34665576869373E+208
----10000----
336447648764317832666216120051075433103021...050562430701794976171121233066073310059947366875 (2089 digits)
timeout
INF
3.364476487643176087E+2089
----100000----
259740693472217241661550340212759154148804853...653428746875 (20898 digits)
recursion
INF
INF
----1000000----
19532821287077577316320149475962563324435429965918733...2043347225419033684684301719893411568996526838242546875 (208987 digits)
recursion
INF
INF

Timing:
-------
1000 fibI: 94 µs (394736 cycles)
timeout after 30000ms
1000 fibBinet: 5500 ns (21746 cycles)
1000 fibBinetFloatE: 12 µs (43444 cycles)
1000 fib (builtin): 37 µs (130842 cycles)
10000 fibI: 2.44 ms (8775334 cycles)
10000 fib (builtin): 49 µs (175466 cycles)
100000 fibI: 156ms (563848550 cycles)
100000 fib (builtin): 1.66 ms (5970368 cycles)
1000000 fibI: 14.3s (51676292910 cycles)
1000000 fib (builtin): 71.95 ms (259023588 cycles)
2000000 fib (builtin): 229ms (827461038 cycles)
10000000 fib (builtin): 2.769s (9970686190 cycles)
```


## SNOBOL4

### Recursive

```mw
  define("fib(a)")  :(fib_end)
fib   fib = lt(a,2) a   :s(return)
   fib = fib(a - 1) + fib(a - 2) :(return)
fib_end

while a = trim(input)   :f(end)
   output = a " " fib(a)   :(while)
end
```

### Tail-recursive

```mw
        define('trfib(n,a,b)') :(trfib_end)
trfib   trfib = eq(n,0) a :s(return)
        trfib = trfib(n - 1, a + b, a) :(return)
trfib_end
```

### Iterative

```mw
        define('ifib(n)f1,f2') :(ifib_end)
ifib    ifib = le(n,2) 1 :s(return)
        f1 = 1; f2 = 1
if1     ifib = gt(n,2) f1 + f2 :f(return)
        f1 = f2; f2 = ifib; n = n - 1 :(if1)
ifib_end
```

### Analytic

Works with

:

Macro Spitbol

Works with

:

CSnobol

Note: Snobol4+ lacks built-in sqrt( ) function.

```mw
        define('afib(n)s5') :(afib_end)
afib    s5 = sqrt(5)
        afib = (((1 + s5) / 2) ^ n - ((1 - s5) / 2) ^ n) / s5
        afib = convert(afib,'integer') :(return)
afib_end
```

Test and display all, Fib 1 .. 10

```mw
loop    i = lt(i,10) i + 1 :f(show)
        s1 = s1 fib(i) ' ' ; s2 = s2 trfib(i,0,1) ' '
        s3 = s3 ifib(i) ' '; s4 = s4 afib(i) ' ' :(loop)
show    output = s1; output = s2; output = s3; output = s4
end
```

Output:

```
1 1 2 3 5 8 13 21 34 55
1 1 2 3 5 8 13 21 34 55
1 1 2 3 5 8 13 21 34 55
1 1 2 3 5 8 13 21 34 55
```


## SNUSP

This is modular SNUSP (which introduces @ and # for threading).

### Iterative

```mw
 @!\+++++++++#  /<<+>+>-\       
fib\==>>+<<?!/>!\      ?/\      
  #<</?\!>/@>\?-<<</@>/@>/>+<-\ 
     \-/  \       !\ !\ !\   ?/#
```

### Recursive

```mw
             /========\    />>+<<-\  />+<-\
fib==!/?!\-?!\->+>+<<?/>>-@\=====?/<@\===?/<#
      |  #+==/     fib(n-2)|+fib(n-1)|
      \=====recursion======/!========/
```


## Spin

### Iterative

Works with

:

BST/BSTC

Works with

:

FastSpin/FlexSpin

Works with

:

HomeSpun

Works with

:

OpenSpin

```mw
con
  _clkmode = xtal1 + pll16x
  _clkfreq = 80_000_000
 
obj
  ser : "FullDuplexSerial.spin"
 
pub main | i
  ser.start(31, 30, 0, 115200)

  repeat i from 0 to 10
    ser.dec(fib(i))
    ser.tx(32)

  waitcnt(_clkfreq + cnt)
  ser.stop
  cogstop(0)

pub fib(i) : b | a 
  b := a := 1 
  repeat i 
    a := b + (b := a)
```

**Output:**

```
1 1 2 3 5 8 13 21 34 55 89
```


## SPL

### Analytic

```mw
fibo(n)=
  s5 = #.sqrt(5)
  <= (((1+s5)/2)^n-((1-s5)/2)^n)/s5
.
```

### Iterative

```mw
fibo(n)=
  ? n<2, <= n
  f2 = 0
  f1 = 1
  > i, 2..n
    f = f1+f2
    f2 = f1
    f1 = f
  <
  <= f
.
```

### Recursive

```mw
fibo(n)=
  ? n<2, <= n
  <= fibo(n-1)+fibo(n-2)
.
```


## SQL

### Analytic

As a running sum:

```mw
select round ( exp ( sum (ln ( ( 1 + sqrt( 5 ) ) / 2)
        ) over ( order by level ) ) / sqrt( 5 ) ) fibo
from dual
connect by level <= 10;
```

```
       FIB
----------
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

10 rows selected.
```

As a power:

```mw
select round ( power( ( 1 + sqrt( 5 ) ) / 2, level ) / sqrt( 5 ) ) fib
from dual
connect by level <= 10;
```

```
       FIB
----------
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

10 rows selected.
```

### Recursive

Works with

:

Oracle

Oracle 12c required

```mw
SQL> with fib(e,f) as (select 1, 1 from dual union all select e+f,e from fib where e <= 55) select f from fib;

         F
----------
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

10 rows selected.
```

Works with

:

PostgreSQL

```mw
CREATE FUNCTION fib(n int) RETURNS numeric AS $$
    -- This recursive with generates endless list of Fibonacci numbers.
    WITH RECURSIVE fibonacci(current, previous) AS (
        -- Initialize the current with 0, so the first value will be 0.
        -- The previous value is set to 1, because its only goal is not
        -- special casing the zero case, and providing 1 as the second
        -- number in the sequence.
        --
        -- The numbers end with dots to make them numeric type in
        -- Postgres. Numeric type has almost arbitrary precision
        -- (technically just 131,072 digits, but that's good enough for
        -- most purposes, including calculating huge Fibonacci numbers)
        SELECT 0., 1.
    UNION ALL
        -- To generate Fibonacci number, we need to add together two
        -- previous Fibonacci numbers. Current number is saved in order
        -- to be accessed in the next iteration of recursive function.
        SELECT previous + current, current FROM fibonacci
    )
    -- The user is only interested in current number, not previous.
    SELECT current FROM fibonacci
    -- We only need one number, so limit to 1
    LIMIT 1
    -- Offset the query by the requested argument to get the correct
    -- position in the list.
    OFFSET n
$$ LANGUAGE SQL RETURNS NULL ON NULL INPUT IMMUTABLE;
```

Works with

:

MariaDB

```mw
SET @row_count := 10;
WITH RECURSIVE fibonacci_row (seq, current_value, next_value) AS
(
    (
        SELECT
            CAST(1 AS UNSIGNED INTEGER) AS seq,
            CAST(0 AS UNSIGNED INTEGER) AS current_value,
            CAST(1 AS UNSIGNED INTEGER) AS next_value
    ) UNION ALL (
        SELECT
            seq + 1 AS seq,
            next_value AS current_value,
            current_value + next_value AS next_value
        FROM fibonacci_row
        WHERE seq + 1 <= @row_count
    )
)
SELECT seq, current_value
    FROM fibonacci_row
;
```


## SSEM

Calculates the tenth Fibonacci number. To calculate the *n*th, change the initial value of the counter to *n*-1 (subject to the restriction that the answer must be small enough to fit in a signed 32-bit integer, the SSEM's only data type). The algorithm is basically straightforward, but the absence of an Add instruction makes the implementation a little more complicated than it would otherwise be.

```mw
10101000000000100000000000000000    0. -21 to c    acc = -n
01101000000001100000000000000000    1. c   to 22   temp = acc
00101000000001010000000000000000    2. Sub. 20     acc -= m
10101000000001100000000000000000    3. c   to 21   n = acc
10101000000000100000000000000000    4. -21 to c    acc = -n
10101000000001100000000000000000    5. c   to 21   n = acc
01101000000000100000000000000000    6. -22 to c    acc = -temp
00101000000001100000000000000000    7. c   to 20   m = acc
11101000000000100000000000000000    8. -23 to c    acc = -count
00011000000001010000000000000000    9. Sub. 24     acc -= -1
00000000000000110000000000000000   10. Test        skip next if acc<0
10011000000000000000000000000000   11. 25  to CI   goto (15 + 1)
11101000000001100000000000000000   12. c   to 23   count = acc
11101000000000100000000000000000   13. -23 to c    acc = -count
11101000000001100000000000000000   14. c   to 23   count = acc
00011000000000000000000000000000   15. 24  to CI   goto (-1 + 1)
10101000000000100000000000000000   16. -21 to c    acc = -n
10101000000001100000000000000000   17. c   to 21   n = acc
10101000000000100000000000000000   18. -21 to c    acc = -n
00000000000001110000000000000000   19. Stop
00000000000000000000000000000000   20. 0           var m = 0
10000000000000000000000000000000   21. 1           var n = 1
00000000000000000000000000000000   22. 0           var temp = 0
10010000000000000000000000000000   23. 9           var count = 9
11111111111111111111111111111111   24. -1          const -1
11110000000000000000000000000000   25. 15          const 15
```


## Stata

```mw
program fib
args n
clear
qui set obs `n'
qui gen a=1
qui replace a=a[_n-1]+a[_n-2] in 3/l
end
```

An implementation using **dyngen**.

```mw
program fib
args n
clear
qui set obs `n'
qui gen a=.
dyngen {
   update a=a[_n-1]+a[_n-2], missval(1)
}
end

fib 10
list
```

**Output**

```
     +----+
     |  a |
     |----|
  1. |  1 |
  2. |  1 |
  3. |  2 |
  4. |  3 |
  5. |  5 |
     |----|
  6. |  8 |
  7. | 13 |
  8. | 21 |
  9. | 34 |
 10. | 55 |
     +----+
```

### Mata

```mw
. mata
: function fib(n) {
        return((((1+sqrt(5))/2):^n-((1-sqrt(5))/2):^n)/sqrt(5))
}

: fib(0..10)
        1    2    3    4    5    6    7    8    9   10   11
    +--------------------------------------------------------+
  1 |   0    1    1    2    3    5    8   13   21   34   55  |
    +--------------------------------------------------------+

: end
```


## Stax

```
{v|5}
```

Non-builtin:

```
{01a{n+s}*d}Y
AFy!P
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
```


## StreamIt

```mw
void->int feedbackloop Fib {
    join roundrobin(0,1);
    body in->int filter {
        work pop 1 push 1 peek 2 { push(peek(0) + peek(1)); pop(); }
    };
    loop Identity<int>;
    split duplicate;
    enqueue(0);
    enqueue(1);
}
```


## SuperCollider

### Recursive

nth fibonacci term for positive n

```mw
f = { |n| if(n < 2) { n } { f.(n-1) + f.(n-2) } };
(0..20).collect(f)
```

nth fibonacci term for positive and negative n.

```mw
f = { |n| var u = neg(sign(n)); if(abs(n) < 2) { n } { f.(2 * u + n) + f.(u + n) } };
(-20..20).collect(f)
```

### Analytic

```mw
(
   f = { |n|
      var sqrt5 = sqrt(5);
      var p = (1 + sqrt5) / 2;
      var q = reciprocal(p);
      ((p ** n) + (q ** n) / sqrt5 + 0.5).trunc
   };
   (0..20).collect(f)
)
```

### Iterative

```mw
f = { |n| var a = [1, 1]; n.do { a = a.addFirst(a[0] + a[1]) }; a.reverse };
f.(18)
```


## Swift

### Analytic

```mw
import Cocoa

func fibonacci(n: Int) -> Int {
    let square_root_of_5 = sqrt(5.0)
    let p = (1 + square_root_of_5) / 2
    let q = 1 / p
    return Int((pow(p,CDouble(n)) + pow(q,CDouble(n))) / square_root_of_5 + 0.5)
}

for i in 1...30 {
    println(fibonacci(i))
}
```

### Iterative

```mw
func fibonacci(n: Int) -> Int {
    if n < 2 {
        return n
    }
    var fibPrev = 1
    var fib = 1
    for num in 2...n {
        (fibPrev, fib) = (fib, fib + fibPrev)
    }
    return fib
}
```

Sequence:

```mw
func fibonacci() -> SequenceOf<UInt> {
  return SequenceOf {() -> GeneratorOf<UInt> in
    var window: (UInt, UInt, UInt) = (0, 0, 1)
    return GeneratorOf {
      window = (window.1, window.2, window.1 + window.2)
      return window.0
    }
  }
}
```

### Recursive

```mw
func fibonacci(n: Int) -> Int {
    if n < 2 {
        return n
    } else {
        return fibonacci(n-1) + fibonacci(n-2)
    }
}

println(fibonacci(30))
```


## Tailspin

### Recursive simple

The simplest exponential-time recursive algorithm only handling positive N. Note that the "#" is the tailspin internal recursion which sends the value to the matchers. In this case where there is no initial block and no templates state, we could equivalently write the templates name "nthFibonacci" in place of the "#" to do a normal recursion.

```mw
templates nthFibonacci
  when <=0|=1> do $ !
  otherwise ($ - 1 -> #) + ($ - 2 -> #) !
end nthFibonacci
```

v0.5

```mw
nthFibonacci templates
  when <|=0|=1> do $ !
  otherwise ($ - 1 -> #) + ($ - 2 -> #) !
end nthFibonacci
```

### Iterative, mutable state

We could use the templates internal mutable state, still only positive N.

```mw
templates nthFibonacci
  @: {n0: 0"1", n1: 1"1"};
  1..$ -> @: {n0: $@.n1, n1: $@.n0 + $@.n1};
  $@.n0!
end nthFibonacci
```

v0.5 no longer has dot access

```mw
nthFibonacci templates
  @ set {n0: 0"1", n1: 1"1"};
  1..$ -> @ set {n0: $@(n1:), n1: $@(n0:) + $@(n1:)};
  $@(n0:)!
end nthFibonacci
```

To handle negatives, we can keep track of the sign and send it to the matchers.

```mw
templates nthFibonacci
  @: {n0: 0"1", n1: 1"1"};
  def sign: $ -> \(<0..> 1! <> -1!\);
  1..$*$sign -> $sign -> #
  $@.n0!
  <=1>
    @: {n0: $@.n1, n1: $@.n0 + $@.n1};
  <=-1>
    @: {n0: $@.n1 - $@.n0, n1: $@.n0};
end nthFibonacci
```

v0.5

```mw
nthFibonacci templates
  @ set {n0: 0"1", n1: 1"1"};
  sign is $ -> templates
    when <|0..> do 1!
    otherwise -1!
  end;
  1..$*$sign -> $sign -> !#
  $@(n0:)!
  when <|=1> do
    @ set {n0: $@(n1:), n1: $@(n0:) + $@(n1:)};
  when <|=-1> do
    @ set {n0: $@(n1:) - $@(n0:), n1: $@(n0:)};
end nthFibonacci
```

### State machine

Instead of mutating state, we could just recurse internally on a state structure.

```mw
templates nthFibonacci
  { N: ($)"1", n0: 0"1", n1: 1"1" } -> #
  when <{ N: <=0"1"> }> do
    $.n0 !
  when <{ N: <1"1"..>}> do
    { N: $.N - 1"1", n0: $.n1, n1: $.n0 + $.n1} -> #
  otherwise
    { N: $.N + 1"1", n1: $.n0, n0: $.n1 - $.n0} -> #
end nthFibonacci
 
8 -> nthFibonacci -> '$;
' -> !OUT::write
-5 -> nthFibonacci -> '$;
' -> !OUT::write
-6 -> nthFibonacci -> '$;
' -> !OUT::write
```

v0.5

```mw
nthFibonacci templates
  { N: ($)"1", n0: 0"1", n1: 1"1" } -> # !
  when <|{ N: <|=0"1"> }> do
    $(n0:) !
  when <|{ N: <|1"1"..>}> do
    { N: $(N:) - 1"1", n0: $(n1:), n1: $(n0:) + $(n1:)} -> # !
  otherwise
    { N: $(N:) + 1"1", n1: $(n0:), n0: $(n1:) - $(n0:)} -> # !
end nthFibonacci
```

**Output:**

```
21"1"
5"1"
-8"1"
```


## TAV

```mw
\ Fibonacci numbers (iterative, with tuples)  
main (parms):+
  lim =: string parms[1] as integer else 100
  fp =: 0, 1
  ?# i =: from 1 upto lim
    print i, fp.1
    fp =: fp.2, fp.1 + fp.2
  print i, fp.2
```

**Output:**

```
1 0
2 1
3 1
4 2
5 3
6 5
7 8
8 13
9 21
10 34
...
94 12200160415121876738
95 19740274219868223167
96 31940434634990099905
97 51680708854858323072
98 83621143489848422977
99 135301852344706746049
100 218922995834555169026
101 573147844013817084101
```

### recursive

```mw
\ Fibonacci numbers (recursive)
\+ stdlib 
fibo (n):
  ? n < 2
    :> n
  :> (fibo n - 1) + fibo n - 2  \ not: fibo(n-1) + fibo(n-2) == fibo (n - 1 + fibo (n-2)
   
main (parms):+
    lim =: string parms[1] as integer else 30
    ?# i =: from 1 upto lim
      print i, fibo i
```


## Tcl

### Simple Version

These simple versions do not handle negative numbers -- they will return N for N < 2

#### Iterative

Translation of

:

Perl

```mw
proc fibiter n {
    if {$n < 2} {return $n}
    set prev 1
    set fib 1
    for {set i 2} {$i < $n} {incr i} {
        lassign [list $fib [incr fib $prev]] prev fib
    }
    return $fib
}
```

#### Recursive

```mw
proc fib {n} {
    if {$n < 2} then {expr {$n}} else {expr {[fib [expr {$n-1}]]+[fib [expr {$n-2}]]} }
}
```

The following

Works with

:

Tcl

version 8.5

: defining a procedure in the `::tcl::mathfunc` namespace allows that proc to be used as a function in `expr` expressions.

```mw
proc tcl::mathfunc::fib {n} {
    if { $n < 2 } {
        return $n
    } else {
        return [expr {fib($n-1) + fib($n-2)}]
    }
}

# or, more tersely

proc tcl::mathfunc::fib {n} {expr {$n<2 ? $n : fib($n-1) + fib($n-2)}}
```

E.g.:

```mw
expr {fib(7)} ;# ==> 13

namespace path tcl::mathfunc #; or, interp alias {} fib {} tcl::mathfunc::fib
fib 7 ;# ==> 13
```

#### Tail-Recursive

In Tcl 8.6 a *tailcall* function is available to permit writing tail-recursive functions in Tcl. This makes deeply recursive functions practical. The availability of large integers also means no truncation of larger numbers.

```mw
proc fib-tailrec {n} {
    proc fib:inner {a b n} {
        if {$n < 1} {
            return $a
        } elseif {$n == 1} {
            return $b
        } else {
            tailcall fib:inner $b [expr {$a + $b}] [expr {$n - 1}]
        }
    }
    return [fib:inner 0 1 $n]
}
```

```
% fib-tailrec 100
354224848179261915075
```

### Handling Negative Numbers

#### Iterative

```mw
proc fibiter n {
    if {$n < 0} {
        set n [expr {abs($n)}]
        set sign [expr {-1**($n+1)}]
    } else {
        set sign 1
    }
    if {$n < 2} {return $n}
    set prev 1
    set fib 1
    for {set i 2} {$i < $n} {incr i} {
        lassign [list $fib [incr fib $prev]] prev fib
    }
    return [expr {$sign * $fib}]
}
fibiter -5 ;# ==> 5
fibiter -6 ;# ==> -8
```

#### Recursive

```mw
proc tcl::mathfunc::fib {n} {expr {$n<-1 ? -1**($n+1) * fib(abs($n)) : $n<2 ? $n : fib($n-1) + fib($n-2)}}
expr {fib(-5)} ;# ==> 5
expr {fib(-6)} ;# ==> -8
```

### For the Mathematically Inclined

This works up to ${\displaystyle fib(70)}$ , after which the limited precision of IEEE double precision floating point arithmetic starts to show.

Works with

:

Tcl

version 8.5

```mw
proc fib n {expr {round((.5 + .5*sqrt(5)) ** $n / sqrt(5))}}
```


## Tern

### Recursive

```mw
func fib(n) {
   if (n < 2) {
      return 1;
   }
   return fib(n - 1) + fib(n - 2);
}
```

### Coroutine

```mw
func fib(n) {
   let a = 1;
   let b = 2;
   
   until(n-- <= 0) {
      yield a;
      (a, b) = (b, a + b);
   }
}
```


## TI SR-56

| Display | Key | Display | Key | Display | Key | Display | Key |
|---|---|---|---|---|---|---|---|
| 00 33 | STO | 25 |   | 50 |   | 75 |   |
| 01 00 | 0 | 26 |   | 51 |   | 76 |   |
| 02 01 | 1 | 27 |   | 52 |   | 77 |   |
| 03 33 | STO | 28 |   | 53 |   | 78 |   |
| 04 01 | 1 | 29 |   | 54 |   | 79 |   |
| 05 00 | 0 | 30 |   | 55 |   | 80 |   |
| 06 84 | + | 31 |   | 56 |   | 81 |   |
| 07 39 | *EXC | 32 |   | 57 |   | 82 |   |
| 08 01 | 1 | 33 |   | 58 |   | 83 |   |
| 09 94 | = | 34 |   | 59 |   | 84 |   |
| 10 27 | *dsz | 35 |   | 60 |   | 85 |   |
| 11 00 | 0 | 36 |   | 61 |   | 86 |   |
| 12 06 | 6 | 37 |   | 62 |   | 87 |   |
| 13 41 | R/S | 38 |   | 63 |   | 88 |   |
| 14 22 | GTO | 39 |   | 64 |   | 89 |   |
| 15 00 | 0 | 40 |   | 65 |   | 90 |   |
| 16 06 | 6 | 41 |   | 66 |   | 91 |   |
| 17 |   | 42 |   | 67 |   | 92 |   |
| 18 |   | 43 |   | 68 |   | 93 |   |
| 19 |   | 44 |   | 69 |   | 94 |   |
| 20 |   | 45 |   | 70 |   | 95 |   |
| 21 |   | 46 |   | 71 |   | 96 |   |
| 22 |   | 47 |   | 72 |   | 97 |   |
| 23 |   | 48 |   | 73 |   | 98 |   |
| 24 |   | 49 |   | 74 |   | 99 |   |

Asterisk denotes 2nd function key.

| 0: Nth term requested | 1: Last term | 2: Unused | 3: Unused | 4: Unused |
|---|---|---|---|---|
| 5: Unused | 6: Unused | 7: Unused | 8: Unused | 9: Unused |

Annotated listing:

```mw
STO 0        // Nth term requested := User input
1 STO 1      // Last term := 1
0            // Initial value: 0
+ *EXC 1 =   // Calculate next term.
*dsz 0 6     // Loop while R0 positive
R/S          // Done, show answer
GTO 0 6      // If user hits R/S calculate next term
```

**Usage:**

At the keypad enter a number N, then press RST R/S to calculate and display the Nth Fibonacci number. R/S for the following numbers.

**Input:**

```
1 RST R/S
```

**Output:**

```
1
```

**Input:**

```
2 RST R/S
```

**Output:**

```
1
```

**Input:**

```
3 RST R/S
```

**Output:**

```
2
```

**Input:**

```
10 RST R/S
```

**Output:**

```
55
```

```
R/S -> 89
```

```
R/S -> 144
```


## TI-57

```
00	 STO 0	      R0 = n
01	 C.t	      R7 = 0
02	 1            Display = 1
03	 INV SUM 0    R0 -= 1
04	 Lbl 1	      loop start
05	 +	
06	 x⮂t	      
07	 =            Display += R7
08	 Dsz	      if --R0 ≠ 0
09	 GTO 1	      then go loop
10	 R/S	      stop
11	 RST	      Go back to step 0
```

```
10  RST R/S
```

**Output:**

```
55.
```


## TI-58/59

This version is longer than the TI-57 one, but it handles the cases n = 0 and 1 correctly, and it can use other starting values (you just need to modify steps 4 and 7). It can also be called as a monadic function in the flow of a calculation, without affecting operator precedence.

```
000    Lbl A        Function keystroke
002    STO 09       R09 = n
004    0            
005    STO 00       initialize R00 with F(0) = 0
007    1
008    STO 01       initialize R01 with F(1) = 1
010    x⇄t          t = 1 
011    RCL 09       x = n
013    x⇄t          swap t and x
014    INV x≥t      if x < t
016    Nop          then go to Nop label
017    RCL Ind 09   else return R0n = F(n)
019    RTN
020    Lbl Nop      loop start to compute F(n) for n>1
022    RCL 01       
024    x⇄t          t = F(n)
025    RCL 00       x = F(n-1)
027    Pause        display x
028    SUM 01       F(n) += x
030    x⇄t 
031    STO 00       F(n-1) = t
033    Dsz 9        if --R09 ≠ 0
035    Nop          then loop
036    RCL 00       else return F(n-1)
038    RTN
```

```
1 + 10 A = 
```

**Output:**

```
56
```


## TSE SAL

```mw
// library: math: get: series: fibonacci <description></description> <version control></version control> <version>1.0.0.0.3</version> <version control></version control> (filenamemacro=getmasfi.s) [<Program>] [<Research>] [kn, ri, su, 20-01-2013 22:04:02]
INTEGER PROC FNMathGetSeriesFibonacciI( INTEGER  nI )
 //
 // Method:
 //
 // 1. Take the sum of the last 2 terms
 //
 // 2. Let the sum be the last term
 //    and goto step 1
 //
 INTEGER I = 0
 INTEGER minI = 1
 INTEGER maxI = nI
 INTEGER term1I = 0
 INTEGER term2I = 1
 INTEGER term3I = 0
 //
 FOR I = minI TO maxI
  //
  // make value 3 equal to sum of two previous values 1 and 2
  //
  term3I = term1I + term2I
  //
  // make value 1 equal to next value 2
  //
  term1I = term2I
  //
  // make value 2 equal to next value 3
  //
  term2I = term3I
  //
  ENDFOR
  //
 RETURN( term3I )
 //
END

PROC Main()
 STRING s1[255] = "3"
 REPEAT
  IF ( NOT ( Ask( " = ", s1, _EDIT_HISTORY_ ) ) AND ( Length( s1 ) > 0 ) ) RETURN() ENDIF
  Warn( FNMathGetSeriesFibonacciI( Val( s1 ) ) ) // gives e.g. 3
 UNTIL FALSE
END
```


## Turing

```mw
% Recursive
function fibb (n: int) : int
    if n < 2 then
        result n
    else
        result fibb (n-1) + fibb (n-2)
    end if
end fibb

% Iterative
function ifibb (n: int) : int
    var a := 0  
    var b := 1
    for : 1 .. n
        a := a + b
        b := a - b
    end for
    result a
end ifibb

for i : 0 .. 10
    put fibb (i) : 4, ifibb (i) : 4
end for
```

Output:

```
   0   0
   1   1
   1   1
   2   2
   3   3
   5   5
   8   8
  13  13
  21  21
  34  34
  55  55
```
