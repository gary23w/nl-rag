---
title: "Ackermann function (part 3/6)"
source: https://rosettacode.org/wiki/Ackermann_function
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/6
---

## FutureBasic

```mw
include "NSLog.incl"

local fn Ackerman( m as NSInteger, n as NSInteger ) as NSInteger
  NSInteger result
  
  select
    case m == 0 : result = ( n + 1 )
    case n == 0 : result = fn Ackerman( ( m - 1 ), 1 )
    case else   : result = fn Ackerman( ( m - 1 ), fn Ackerman( m, ( n - 1 ) ) )
  end select
end fn = result

NSInteger          m, n
CFMutableStringRef mutStr

mutStr = fn StringWithCapacity( 0 )

for m = 0 to 3
  for n = 0 to 9
    StringAppendString( mutStr, fn StringWithFormat( @"fn Ackerman( %ld, %ld ) = %ld\n", m, n, fn Ackerman( m, n ) ) )
  next
next

NSLog( @"%@", mutStr )

HandleEvents
```

Output:

```
fn Ackerman( 0, 0 ) = 1
fn Ackerman( 0, 1 ) = 2
fn Ackerman( 0, 2 ) = 3
fn Ackerman( 0, 3 ) = 4
fn Ackerman( 0, 4 ) = 5
fn Ackerman( 0, 5 ) = 6
fn Ackerman( 0, 6 ) = 7
fn Ackerman( 0, 7 ) = 8
fn Ackerman( 0, 8 ) = 9
fn Ackerman( 0, 9 ) = 10
fn Ackerman( 1, 0 ) = 2
fn Ackerman( 1, 1 ) = 3
fn Ackerman( 1, 2 ) = 4
fn Ackerman( 1, 3 ) = 5
fn Ackerman( 1, 4 ) = 6
fn Ackerman( 1, 5 ) = 7
fn Ackerman( 1, 6 ) = 8
fn Ackerman( 1, 7 ) = 9
fn Ackerman( 1, 8 ) = 10
fn Ackerman( 1, 9 ) = 11
fn Ackerman( 2, 0 ) = 3
fn Ackerman( 2, 1 ) = 5
fn Ackerman( 2, 2 ) = 7
fn Ackerman( 2, 3 ) = 9
fn Ackerman( 2, 4 ) = 11
fn Ackerman( 2, 5 ) = 13
fn Ackerman( 2, 6 ) = 15
fn Ackerman( 2, 7 ) = 17
fn Ackerman( 2, 8 ) = 19
fn Ackerman( 2, 9 ) = 21
fn Ackerman( 3, 0 ) = 5
fn Ackerman( 3, 1 ) = 13
fn Ackerman( 3, 2 ) = 29
fn Ackerman( 3, 3 ) = 61
fn Ackerman( 3, 4 ) = 125
fn Ackerman( 3, 5 ) = 253
fn Ackerman( 3, 6 ) = 509
fn Ackerman( 3, 7 ) = 1021
fn Ackerman( 3, 8 ) = 2045
fn Ackerman( 3, 9 ) = 4093
```


## Fōrmulæ

Fōrmulæ programs are not textual, visualization/edition of programs is done showing/manipulating structures but not text. Moreover, there can be multiple visual representations of the same program. Even though it is possible to have textual representation —i.e. XML, JSON— they are intended for storage and transfer purposes more than visualization and edition.

Programs in Fōrmulæ are created/edited online in its website.

In **this page** you can see and run the program(s) related to this task and their results. You can also change either the programs or the parameters they are called with, for experimentation, but remember that these programs were created with the main purpose of showing a clear solution of the task, and they generally lack any kind of validation.

**Solution**

**Test case**


## Gambas

```mw
Public Function Ackermann(m As Float, n As Float) As Float
  If m = 0 Then
    Return n + 1
  End If
  If n = 0 Then
    Return Ackermann(m - 1, 1)
  End If
  Return Ackermann(m - 1, Ackermann(m, n - 1))
End

Public Sub Main()
  Dim m, n As Float
  For m = 0 To 3
    For n = 0 To 4
      Print "Ackermann("; m; ", "; n; ") = "; Ackermann(m, n)
    Next
  Next
End
```


## GAP

```mw
ack := function(m, n)
  if m = 0 then
    return n + 1;
  elif (m > 0) and (n = 0) then
    return ack(m - 1, 1);
  elif (m > 0) and (n > 0) then
    return ack(m - 1, ack(m, n - 1));
  else
    return fail;
  fi;
end;
```


## Genyris

```mw
def A (m n)
   cond
      (equal? m 0)
          + n 1
      (equal? n 0) 
          A (- m 1) 1
      else
          A (- m 1)
             A m (- n 1)
```


## GML

Define a script resource named ackermann and paste this code inside:

```mw
///ackermann(m,n)
var m, n;
m = argument0;
n = argument1;
if(m=0)
    {
    return (n+1)
    }
else if(n == 0)
    {
    return (ackermann(m-1,1,1))
    }
else
    {
    return (ackermann(m-1,ackermann(m,n-1,2),1))
    }
```


## gnuplot

```mw
A (m, n) = m == 0 ? n + 1 : n == 0 ? A (m - 1, 1) : A (m - 1, A (m, n - 1))
print A (0, 4)
print A (1, 4)
print A (2, 4)
print A (3, 4)
```

**Output:**

```
5
6
11
stack overflow
```


## Gleam

Translation of

:

Erlang

```mw
pub fn ackermann(m: Int, n: Int) -> Int {
  case m, n {
    0, n -> n + 1
    m, 0 -> ackermann(m - 1, 1)
    m, n -> ackermann(m - 1, ackermann(m, n - 1))
  }
}

pub fn main() {
  echo ackermann(0, 0)
  echo ackermann(0, 4)
  echo ackermann(1, 0)
  echo ackermann(1, 1)
  echo ackermann(2, 1)
  echo ackermann(2, 2)
  echo ackermann(3, 1)
  echo ackermann(3, 3)
  echo ackermann(4, 0)
  echo ackermann(4, 1)
}
```


## Go

### Classic version

```mw
func Ackermann(m, n uint) uint {
	switch 0 {
	case m:
		return n + 1
	case n:
		return Ackermann(m - 1, 1)
	}
	return Ackermann(m - 1, Ackermann(m, n - 1))
}
```

### Expanded version

```mw
func Ackermann2(m, n uint) uint {
  switch {
    case m == 0:
      return n + 1
    case m == 1:
      return n + 2
    case m == 2:
      return 2*n + 3
    case m == 3:
      return 8 << n - 3
    case n == 0:
      return Ackermann2(m - 1, 1)
  }
  return Ackermann2(m - 1, Ackermann2(m, n - 1))
}
```

### Expanded version with arbitrary precision

```mw
package main

import (
	"fmt"
	"math/big"
	"math/bits" // Added in Go 1.9
)

var one = big.NewInt(1)
var two = big.NewInt(2)
var three = big.NewInt(3)
var eight = big.NewInt(8)

func Ackermann2(m, n *big.Int) *big.Int {
	if m.Cmp(three) <= 0 {
		switch m.Int64() {
		case 0:
			return new(big.Int).Add(n, one)
		case 1:
			return new(big.Int).Add(n, two)
		case 2:
			r := new(big.Int).Lsh(n, 1)
			return r.Add(r, three)
		case 3:
			if nb := n.BitLen(); nb > bits.UintSize {
				// n is too large to represent as a
				// uint for use in the Lsh method.
				panic(TooBigError(nb))

				// If we tried to continue anyway, doing
				// 8*2^n-3 as bellow, we'd use hundreds
				// of megabytes and lots of CPU time
				// without the Exp call even returning.
				r := new(big.Int).Exp(two, n, nil)
				r.Mul(eight, r)
				return r.Sub(r, three)
			}
			r := new(big.Int).Lsh(eight, uint(n.Int64()))
			return r.Sub(r, three)
		}
	}
	if n.BitLen() == 0 {
		return Ackermann2(new(big.Int).Sub(m, one), one)
	}
	return Ackermann2(new(big.Int).Sub(m, one),
		Ackermann2(m, new(big.Int).Sub(n, one)))
}

type TooBigError int

func (e TooBigError) Error() string {
	return fmt.Sprintf("A(m,n) had n of %d bits; too large", int(e))
}

func main() {
	show(0, 0)
	show(1, 2)
	show(2, 4)
	show(3, 100)
	show(3, 1e6)
	show(4, 1)
	show(4, 2)
	show(4, 3)
}

func show(m, n int64) {
	defer func() {
		// Ackermann2 could/should have returned an error
		// instead of a panic. But here's how to recover
		// from the panic, and report "expected" errors.
		if e := recover(); e != nil {
			if err, ok := e.(TooBigError); ok {
				fmt.Println("Error:", err)
			} else {
				panic(e)
			}
		}
	}()

	fmt.Printf("A(%d, %d) = ", m, n)
	a := Ackermann2(big.NewInt(m), big.NewInt(n))
	if a.BitLen() <= 256 {
		fmt.Println(a)
	} else {
		s := a.String()
		fmt.Printf("%d digits starting/ending with: %s...%s\n",
			len(s), s[:20], s[len(s)-20:],
		)
	}
}
```

**Output:**

```
A(0, 0) = 1
A(1, 2) = 4
A(2, 4) = 11
A(3, 100) = 10141204801825835211973625643005
A(3, 1000000) = 301031 digits starting/ending with: 79205249834367186005...39107225301976875005
A(4, 1) = 65533
A(4, 2) = 19729 digits starting/ending with: 20035299304068464649...45587895905719156733
A(4, 3) = Error: A(m,n) had n of 65536 bits; too large
```


## Golfscript

```mw
{
  :_n; :_m;
  _m 0= {_n 1+}
        {_n 0= {_m 1- 1 ack}
               {_m 1- _m _n 1- ack ack}
               if}
        if
}:ack;
```


## Groovy

```mw
def ack ( m, n ) {
    assert m >= 0 && n >= 0 : 'both arguments must be non-negative'
    m == 0 ? n + 1 : n == 0 ? ack(m-1, 1) : ack(m-1, ack(m, n-1))
}
```

Test program:

```mw
def ackMatrix = (0..3).collect { m -> (0..8).collect { n -> ack(m, n) } }
ackMatrix.each { it.each { elt -> printf "%7d", elt }; println() }
```

**Output:**

```
      1      2      3      4      5      6      7      8      9
      2      3      4      5      6      7      8      9     10
      3      5      7      9     11     13     15     17     19
      5     13     29     61    125    253    509   1021   2045
```

Note: In the default groovyConsole configuration for WinXP, "ack(4,1)" caused a stack overflow error!


## Hare

```mw
use fmt;

fn ackermann(m: u64, n: u64) u64 = {
	if (m == 0) {
		return n + 1;
	};
	if (n == 0) {
		return ackermann(m - 1, 1);
	};
	return ackermann(m - 1, ackermann(m, n - 1));
};

export fn main() void = {
	for (let m = 0u64; m < 4; m += 1) {
		for (let n = 0u64; n < 10; n += 1) {
			fmt::printfln("A({}, {}) = {}", m, n, ackermann(m, n))!;
		};
		fmt::println()!;
	};
};
```


## Haskell

```mw
ack :: Int -> Int -> Int
ack 0 n = succ n
ack m 0 = ack (pred m) 1
ack m n = ack (pred m) (ack m (pred n))

main :: IO ()
main = mapM_ print $ uncurry ack <$> [(0, 0), (3, 4)]
```

**Output:**

```
1
125
```

Generating a list instead:

```mw
import Data.List (mapAccumL)

-- everything here are [Int] or [[Int]], which would overflow
-- * had it not overrun the stack first *
ackermann = iterate ack [1..] where
	ack a = s where
		s = snd $ mapAccumL f (tail a) (1 : zipWith (-) s (1:s))
	f a b = (aa, head aa) where aa = drop b a

main = mapM_ print $ map (\n -> take (6 - n) $ ackermann !! n) [0..5]
```


## Haxe

```mw
class RosettaDemo
{
    static public function main()
    {
        Sys.print(ackermann(3, 4));
    }

    static function ackermann(m : Int, n : Int)
    {
        if (m == 0)
        {
            return n + 1;
        }
        else if (n == 0)
        {
            return ackermann(m-1, 1);
        }
        return ackermann(m-1, ackermann(m, n-1));
    }
}
```


## Hobbes

```mw
ack :: (int * int) -> int
ack x = match x with
  | (0, n) -> n + 1
  | (m, 0) -> ack((m-1, 1))
  | (m, n) -> ack((m-1, ack((m, n-1))))
```

**Output:**

```
> [[ack((m, n)) | n <- [0..5]] | m <- [0..3]]
[[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 5, 7, 9, 11, 13], [5, 13, 29, 61, 125, 253]]
```


## Hoon

```mw
|=  [m=@ud n=@ud]
?:  =(m 0)
  +(n)
?:  =(n 0)
  $(n 1, m (dec m))
$(m (dec m), n $(n (dec n)))
```


## HPPPL

Works with

:

HP Prime calculator.

```mw
//subAck1();
EXPORT Ackermann_function(m,n)
BEGIN
PRINT;
 PRINT("Ackermann("+m+","+n+") = "+subAck1(m,n));
END;

subAck1(m,n)
BEGIN
CASE
 IF m<0 OR n<0 THEN "m y n deben ser >=0" END;
 IF m=0 THEN n+1 END;
 IF m>0 AND n=0 THEN subAck1((m-1),1); END;
 IF m>0 AND n>0 THEN subAck1((m-1),subAck1(m,(n-1))); END; 
 DEFAULT RETURN PRINT("ERROR");
END;
END;
```

**Input:**

```
m: 3
n: 8
```

**Output:**

```
Ackermann(3,8)=2045
```


## Icon and Unicon

Library:

Icon Programming Library

Taken from the public domain Icon Programming Library's acker in memrfncs, written by Ralph E. Griswold.

```mw
procedure acker(i, j)
   static memory

   initial {
      memory := table()
      every memory[0 to 100] := table()
      }

   if i = 0 then return j + 1

   if j = 0 then /memory[i][j] := acker(i - 1, 1)
   else /memory[i][j] := acker(i - 1, acker(i, j - 1))

   return memory[i][j]

end

procedure main()
   every m := 0 to 3 do {
      every n := 0 to 8 do {
         writes(acker(m, n) || " ")
         }
      write()
      }
end
```

**Output:**

```
1 2 3 4 5 6 7 8 9 
2 3 4 5 6 7 8 9 10 
3 5 7 9 11 13 15 17 19 
5 13 29 61 125 253 509 1021 2045
```


## Idris

```mw
A : Nat -> Nat -> Nat
A Z n = S n
A (S m) Z = A m (S Z)
A (S m) (S n) = A m (A (S m) n)
```


## Ioke

Translation of

:

Clojure

```mw
ackermann = method(m,n,
  cond(
    m zero?, n succ,
    n zero?, ackermann(m pred, 1),
    ackermann(m pred, ackermann(m, n pred)))
)
```


## J

```mw
ack=: >:@]`(<:@[ $: 1:)`(<:@[ $: ($: <:))@.(,&*i.0:)M.
```

The different cases can be split into different lines:

```mw
c1=: >:@]                     NB. if 0=x, 1+y
c2=: <:@[ ack 1:              NB. if 0=y, (x-1) ack 1
c3=: <:@[ ack [ ack <:@]      NB. else,   (x-1) ack x ack y-1
ack=: c1`c2`c3@.(,&* i. 0:)M.
```

**Example use:**

```mw
   0 ack 3
4
   1 ack 3
5
   2 ack 3
9
   3 ack 3
61
```

J's stack was too small for me to compute 4 ack 1.

### Alternative Primitive Recursive Version

This version works by first generating verbs (functions) and then applying them to compute the rows of the related Buck function; then the Ackermann function is obtained in terms of the Buck function. It uses extended precision to be able to compute 4 Ack 2.

The Ackermann function derived in this fashion is primitive recursive. This is possible because in J (as in some other languages) functions, or representations of them, are first-class values.

```mw
   Ack=. 3 -~ [ ({&(2 4$'>:  2x&+') ::(,&'&1'&'2x&*'@:(-&2))"0@:[ 128!:2 ]) 3 + ]
```

**Example use:**

```mw
   0 1 2 3 Ack 0 1 2 3 4 5 6 7
1  2  3  4   5   6   7    8
2  3  4  5   6   7   8    9
3  5  7  9  11  13  15   17
5 13 29 61 125 253 509 1021
   
   3 4 Ack 0 1 2
 5    13                                                                                                                                                                                                                                                        ...
13 65533 2003529930406846464979072351560255750447825475569751419265016973710894059556311453089506130880933348101038234342907263181822949382118812668869506364761547029165041871916351587966347219442930927982084309104855990570159318959639524863372367203002916...
   
   4 # @: ": @: Ack 2 NB. Number of digits of 4 Ack 2
19729
   
   5 Ack 0
65533
```

A structured derivation of Ack follows:

```mw
   o=. @: NB. Composition of verbs (functions) 
   x=. o[ NB. Composing the left noun (argument)
   
   (rows2up=. ,&'&1'&'2x&*') o i. 4 
2x&*      
2x&*&1    
2x&*&1&1  
2x&*&1&1&1
   NB. 2's multiplication, exponentiation, tetration, pentation, etc.
    
   0 1 2 (BuckTruncated=. (rows2up  x apply ]) f.) 0 1 2 3 4 5
0 2 4  6     8                                                                                                                                                                                                                                                  ...
1 2 4  8    16                                                                                                                                                                                                                                                  ...
1 2 4 16 65536 2003529930406846464979072351560255750447825475569751419265016973710894059556311453089506130880933348101038234342907263181822949382118812668869506364761547029165041871916351587966347219442930927982084309104855990570159318959639524863372367203...
   NB. Buck truncated function (missing the first two rows)
   
   BuckTruncated NB. Buck truncated function-level code
,&'&1'&'2x&*'@:[ 128!:2 ]
   
   (rows01=. {&('>:',:'2x&+')) 0 1 NB. The missing first two rows
>:  
2x&+
   
   Buck=. (rows01 :: (rows2up o (-&2)))"0 x apply ]
   
   (Ack=. (3 -~ [ Buck 3 + ])f.)  NB. Ackermann function-level code
3 -~ [ ({&(2 4$'>:  2x&+') ::(,&'&1'&'2x&*'@:(-&2))"0@:[ 128!:2 ]) 3 + ]
```


## Java

```mw
import java.math.BigInteger;

public static BigInteger ack(BigInteger m, BigInteger n) {
    return m.equals(BigInteger.ZERO)
            ? n.add(BigInteger.ONE)
            : ack(m.subtract(BigInteger.ONE),
                        n.equals(BigInteger.ZERO) ? BigInteger.ONE : ack(m, n.subtract(BigInteger.ONE)));
}
```

Works with

:

Java

version 8+

```mw
@FunctionalInterface
public interface FunctionalField<FIELD extends Enum<?>> {
  public Object untypedField(FIELD field);

  @SuppressWarnings("unchecked")
  public default <VALUE> VALUE field(FIELD field) {
    return (VALUE) untypedField(field);
  }
}
```

```mw
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;
import java.util.stream.Stream;

public interface TailRecursive {
  public static <INPUT, INTERMEDIARY, OUTPUT> Function<INPUT, OUTPUT> new_(Function<INPUT, INTERMEDIARY> toIntermediary, UnaryOperator<INTERMEDIARY> unaryOperator, Predicate<INTERMEDIARY> predicate, Function<INTERMEDIARY, OUTPUT> toOutput) {
    return input ->
      $.new_(
        Stream.iterate(
          toIntermediary.apply(input),
          unaryOperator
        ),
        predicate,
        toOutput
      )
    ;
  }

  public static <INPUT1, INPUT2, INTERMEDIARY, OUTPUT> BiFunction<INPUT1, INPUT2, OUTPUT> new_(BiFunction<INPUT1, INPUT2, INTERMEDIARY> toIntermediary, UnaryOperator<INTERMEDIARY> unaryOperator, Predicate<INTERMEDIARY> predicate, Function<INTERMEDIARY, OUTPUT> toOutput) {
    return (input1, input2) ->
      $.new_(
        Stream.iterate(
          toIntermediary.apply(input1, input2),
          unaryOperator
        ),
        predicate,
        toOutput
      )
    ;
  }

  public enum $ {
    $$;

    private static <INTERMEDIARY, OUTPUT> OUTPUT new_(Stream<INTERMEDIARY> stream, Predicate<INTERMEDIARY> predicate, Function<INTERMEDIARY, OUTPUT> function) {
      return stream
        .filter(predicate)
        .map(function)
        .findAny()
        .orElseThrow(RuntimeException::new)
      ;
    }
  }
}
```

```mw
import java.math.BigInteger;
import java.util.Stack;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public interface Ackermann {
  public static Ackermann new_(BigInteger number1, BigInteger number2, Stack<BigInteger> stack, boolean flag) {
    return $.new_(number1, number2, stack, flag);
  }
  public static void main(String... arguments) {
    $.main(arguments);
  }
  public BigInteger number1();
  public BigInteger number2();

  public Stack<BigInteger> stack();

  public boolean flag();

  public enum $ {
    $$;

    private static final BigInteger ZERO = BigInteger.ZERO;
    private static final BigInteger ONE = BigInteger.ONE;
    private static final BigInteger TWO = BigInteger.valueOf(2);
    private static final BigInteger THREE = BigInteger.valueOf(3);
    private static final BigInteger FOUR = BigInteger.valueOf(4);

    private static Ackermann new_(BigInteger number1, BigInteger number2, Stack<BigInteger> stack, boolean flag) {
      return (FunctionalAckermann) field -> {
        switch (field) {
          case number1: return number1;
          case number2: return number2;
          case stack: return stack;
          case flag: return flag;
          default: throw new UnsupportedOperationException(
            field instanceof Field
              ? "Field checker has not been updated properly."
              : "Field is not of the correct type."
          );
        }
      };
    }

    private static final BinaryOperator<BigInteger> ACKERMANN = 
      TailRecursive.new_(
        (BigInteger number1, BigInteger number2) ->
          new_(
            number1,
            number2,
            Stream.of(number1).collect(
              Collectors.toCollection(Stack::new)
            ),
            false
          )
        ,
        ackermann -> {
          BigInteger number1 = ackermann.number1();
          BigInteger number2 = ackermann.number2();
          Stack<BigInteger> stack = ackermann.stack();
          if (!stack.empty() && !ackermann.flag()) {
            number1 = stack.pop();
          }
          switch (number1.intValue()) {
            case 0:
              return new_(
                number1,
                number2.add(ONE),
                stack,
                false
              );
            case 1:
              return new_(
                number1,
                number2.add(TWO),
                stack,
                false
              );
            case 2:
              return new_(
                number1,
                number2.multiply(TWO).add(THREE),
                stack,
                false
              );
            default:
              if (ZERO.equals(number2)) {
                return new_(
                  number1.subtract(ONE),
                  ONE,
                  stack,
                  true
                );
              } else {
                stack.push(number1.subtract(ONE));
                return new_(
                  number1,
                  number2.subtract(ONE),
                  stack,
                  true
                );
              }
          }
        },
        ackermann -> ackermann.stack().empty(),
        Ackermann::number2
      )::apply
    ;

    private static void main(String... arguments) {
      System.out.println(ACKERMANN.apply(FOUR, TWO));
    }

    private enum Field {
      number1,
      number2,
      stack,
      flag
    }

    @FunctionalInterface
    private interface FunctionalAckermann extends FunctionalField<Field>, Ackermann {
      @Override
      public default BigInteger number1() {
        return field(Field.number1);
      }

      @Override
      public default BigInteger number2() {
        return field(Field.number2);
      }

      @Override
      public default Stack<BigInteger> stack() {
        return field(Field.stack);
      }

      @Override
      public default boolean flag() {
        return field(Field.flag);
      }
    }
  }
}
```

Template:Iterative version

```mw
/*
 * Source https://stackoverflow.com/a/51092690/5520417
 */

package matematicas;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Stack;

/**
 * @author rodri
 *
 */

public class IterativeAckermannMemoryOptimization extends Thread {

  /**
   * Max percentage of free memory that the program will use. Default is 10% since
   * the majority of the used devices are mobile and therefore it is more likely
   * that the user will have more opened applications at the same time than in a
   * desktop device
   */
  private static Double SYSTEM_MEMORY_LIMIT_PERCENTAGE = 0.1;

  /**
   * Attribute of the type IterativeAckermann
   */
  private IterativeAckermann iterativeAckermann;

  /**
   * @param iterativeAckermann
   */
  public IterativeAckermannMemoryOptimization(IterativeAckermann iterativeAckermann) {
    super();
    this.iterativeAckermann = iterativeAckermann;
  }

  /**
   * @return
   */
  public IterativeAckermann getIterativeAckermann() {
    return iterativeAckermann;
  }

  /**
   * @param iterativeAckermann
   */
  public void setIterativeAckermann(IterativeAckermann iterativeAckermann) {
    this.iterativeAckermann = iterativeAckermann;
  }

  public static Double getSystemMemoryLimitPercentage() {
    return SYSTEM_MEMORY_LIMIT_PERCENTAGE;
  }

  /**
   * Principal method of the thread. Checks that the memory used doesn't exceed or
   * equal the limit, and informs the user when that happens.
   */
  @Override
  public void run() {
    String operating_system = System.getProperty("os.name").toLowerCase();
    if ( operating_system.equals("windows") || operating_system.equals("linux") || operating_system.equals("macintosh") ) {
      SYSTEM_MEMORY_LIMIT_PERCENTAGE = 0.25;
    }

    while ( iterativeAckermann.getConsumed_heap() >= SYSTEM_MEMORY_LIMIT_PERCENTAGE * Runtime.getRuntime().freeMemory() ) {
      try {
        wait();
      }
      catch ( InterruptedException e ) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
    }
    if ( ! iterativeAckermann.isAlive() )
      iterativeAckermann.start();
    else
      notifyAll();

  }

}

public class IterativeAckermann extends Thread {

  /*
   * Adjust parameters conveniently
   */
  /**
   * 
   */
  private static final int HASH_SIZE_LIMIT = 636;

  /**
   * 
   */
  private BigInteger m;

  /**
   * 
   */
  private BigInteger n;

  /**
   * 
   */
  private Integer hash_size;

  /**
   * 
   */
  private Long consumed_heap;

  /**
   * @param m
   * @param n
   * @param invalid
   * @param invalid2
   */
  public IterativeAckermann(BigInteger m, BigInteger n, Integer invalid, Long invalid2) {
    super();
    this.m = m;
    this.n = n;
    this.hash_size = invalid;
    this.consumed_heap = invalid2;
  }

  /**
   * 
   */
  public IterativeAckermann() {
    // TODO Auto-generated constructor stub
    super();
    m = null;
    n = null;
    hash_size = 0;
    consumed_heap = 0l;
  }

  /**
   * @return
   */
  public static BigInteger getLimit() {
    return LIMIT;
  }

  /**
   * @author rodri
   *
   * @param <T1>
   * @param <T2>
   */
  /**
   * @author rodri
   *
   * @param <T1>
   * @param <T2>
   */
  static class Pair<T1, T2> {

    /**
     * 
     */
    /**
     * 
     */
    T1 x;

    /**
     * 
     */
    /**
     * 
     */
    T2 y;

    /**
     * @param x_
     * @param y_
     */
    /**
     * @param x_
     * @param y_
     */
    Pair(T1 x_, T2 y_) {
      x = x_;
      y = y_;
    }

    /**
     *
     */
    /**
     *
     */
    @Override
    public int hashCode() {
      return x.hashCode() ^ y.hashCode();
    }

    /**
     *
     */
    /**
     *
     */
    @Override
    public boolean equals(Object o_) {

      if ( o_ == null ) {
        return false;
      }
      if ( o_.getClass() != this.getClass() ) {
        return false;
      }
      Pair<?, ?> o = (Pair<?, ?>) o_;
      return x.equals(o.x) && y.equals(o.y);
    }
  }

  /**
   * 
   */
  private static final BigInteger LIMIT = new BigInteger("6");

  /**
   * @param m
   * @param n
   * @return
   */

  /**
   *
   */
  @Override
  public void run() {
    while ( hash_size >= HASH_SIZE_LIMIT ) {
      try {
        this.wait();
      }
      catch ( InterruptedException e ) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
    }
    for ( BigInteger i = BigInteger.ZERO; i.compareTo(LIMIT) == - 1; i = i.add(BigInteger.ONE) ) {
      for ( BigInteger j = BigInteger.ZERO; j.compareTo(LIMIT) == - 1; j = j.add(BigInteger.ONE) ) {
        IterativeAckermann iterativeAckermann = new IterativeAckermann(i, j, null, null);
        System.out.printf("Ackmermann(%d, %d) = %d\n", i, j, iterativeAckermann.iterative_ackermann(i, j));

      }
    }
  }

  /**
   * @return
   */
  public BigInteger getM() {
    return m;
  }

  /**
   * @param m
   */
  public void setM(BigInteger m) {
    this.m = m;
  }

  /**
   * @return
   */
  public BigInteger getN() {
    return n;
  }

  /**
   * @param n
   */
  public void setN(BigInteger n) {
    this.n = n;
  }

  /**
   * @return
   */
  public Integer getHash_size() {
    return hash_size;
  }

  /**
   * @param hash_size
   */
  public void setHash_size(Integer hash_size) {
    this.hash_size = hash_size;
  }

  /**
   * @return
   */
  public Long getConsumed_heap() {
    return consumed_heap;
  }

  /**
   * @param consumed_heap
   */
  public void setConsumed_heap(Long consumed_heap) {
    this.consumed_heap = consumed_heap;
  }

  /**
   * @param m
   * @param n
   * @return
   */
  public BigInteger iterative_ackermann(BigInteger m, BigInteger n) {
    if ( m.compareTo(BigInteger.ZERO) != - 1 && m.compareTo(BigInteger.ZERO) != - 1 )
      try {
        HashMap<Pair<BigInteger, BigInteger>, BigInteger> solved_set = new HashMap<Pair<BigInteger, BigInteger>, BigInteger>(900000);
        Stack<Pair<BigInteger, BigInteger>> to_solve = new Stack<Pair<BigInteger, BigInteger>>();
        to_solve.push(new Pair<BigInteger, BigInteger>(m, n));

        while ( ! to_solve.isEmpty() ) {
          Pair<BigInteger, BigInteger> head = to_solve.peek();
          if ( head.x.equals(BigInteger.ZERO) ) {
            solved_set.put(head, head.y.add(BigInteger.ONE));
            to_solve.pop();
          }
          else if ( head.y.equals(BigInteger.ZERO) ) {
            Pair<BigInteger, BigInteger> next = new Pair<BigInteger, BigInteger>(head.x.subtract(BigInteger.ONE), BigInteger.ONE);
            BigInteger result = solved_set.get(next);
            if ( result == null ) {
              to_solve.push(next);
            }
            else {
              solved_set.put(head, result);
              to_solve.pop();
            }
          }
          else {
            Pair<BigInteger, BigInteger> next0 = new Pair<BigInteger, BigInteger>(head.x, head.y.subtract(BigInteger.ONE));
            BigInteger result0 = solved_set.get(next0);
            if ( result0 == null ) {
              to_solve.push(next0);
            }
            else {
              Pair<BigInteger, BigInteger> next = new Pair<BigInteger, BigInteger>(head.x.subtract(BigInteger.ONE), result0);
              BigInteger result = solved_set.get(next);
              if ( result == null ) {
                to_solve.push(next);
              }
              else {
                solved_set.put(head, result);
                to_solve.pop();
              }
            }
          }
        }
        this.hash_size = solved_set.size();
        System.out.println("Hash Size: " + hash_size);
        consumed_heap = (Runtime.getRuntime().totalMemory() / (1024 * 1024));
        System.out.println("Consumed Heap: " + consumed_heap + "m");
        setHash_size(hash_size);
        setConsumed_heap(consumed_heap);
        return solved_set.get(new Pair<BigInteger, BigInteger>(m, n));

      }
      catch ( OutOfMemoryError e ) {
        // TODO: handle exception
        e.printStackTrace();
      }
    throw new IllegalArgumentException("The arguments must be non-negative integers.");
  }

  /**
   * @param args
   */
  /**
   * @param args
   */
  public static void main(String[] args) {
    IterativeAckermannMemoryOptimization iterative_ackermann_memory_optimization = new IterativeAckermannMemoryOptimization(
        new IterativeAckermann());
    iterative_ackermann_memory_optimization.start();
  }
}
```


## JavaScript

### ES5

```mw
function ack(m, n) {
 return m === 0 ? n + 1 : ack(m - 1, n === 0  ? 1 : ack(m, n - 1));
}
```

### Eliminating Tail Calls

```mw
function ack(M,N) {
  for (; M > 0; M--) {
    N = N === 0 ? 1 : ack(M,N-1);
  }
  return N+1;
}
```

### Iterative, With Explicit Stack

```mw
function stackermann(M, N) {
  const stack = [];
  for (;;) {
    if (M === 0) {
      N++;
      if (stack.length === 0) return N;
      const r = stack[stack.length-1];
      if (r[1] === 1) stack.length--;
      else r[1]--;
      M = r[0];
    } else if (N === 0) {
      M--;
      N = 1;
    } else {
      M--
      stack.push([M, N]);
      N = 1;
    }
  }
}
```

### Stackless Iterative

```mw
#!/usr/bin/env nodejs
function ack(M, N){
	const next = new Float64Array(M + 1);
	const goal = new Float64Array(M + 1).fill(1, 0, M);
	const n = N + 1;

	// This serves as a sentinel value;
	// next[M] never equals goal[M] == -1,
	// so we don't need an extra check for
	// loop termination below.
	goal[M] = -1;

	let v;
	do {
		v = next[0] + 1;
		let m = 0;
		while (next[m] === goal[m]) {
			goal[m] = v;
			next[m++]++;
		}
		next[m]++;
	} while (next[M] !== n);
	return v;
}
var args = process.argv;
console.log(ack(parseInt(args[2]), parseInt(args[3])));
```

**Output:**

```
> time ./ack.js 4 1            
65533
./ack.js 4 1  0,48s user 0,03s system 100% cpu 0,505 total ; AMD FX-8350 @ 4 GHz
```

### ES6

```mw
(() => {
    'use strict';

    // ackermann :: Int -> Int -> Int
    const ackermann = m => n => {
        const go = (m, n) =>
            0 === m ? (
                succ(n)
            ) : go(pred(m), 0 === n ? (
                1
            ) : go(m, pred(n)));
        return go(m, n);
    };

    // TEST -----------------------------------------------
    const main = () => console.log(JSON.stringify(
        [0, 1, 2, 3].map(
            flip(ackermann)(3)
        )
    ));

    // GENERAL FUNCTIONS ----------------------------------

    // flip :: (a -> b -> c) -> b -> a -> c
    const flip = f =>
        x => y => f(y)(x);

    // pred :: Enum a => a -> a
    const pred = x => x - 1;

    // succ :: Enum a => a -> a
    const succ = x => 1 + x;

    // MAIN ---
    return main();
})();
```

**Output:**

```
[4,5,9,61]
```


## Joy

```mw
DEFINE ack == [[[pop null] popd succ] 
[[null] pop pred 1 ack] 
[[dup pred swap] dip pred ack ack]] 
cond.
```

another using a combinator:

```mw
DEFINE ack == [[[pop null] [popd succ]] 
[[null] [pop pred 1] []] 
[[[dup pred swap] dip pred] [] []]] 
condnestrec.
```


## jq

Works with

:

jq

version 1.4

**Also works with gojq, the Go implementation of jq.**

Except for a minor tweak to the line using string interpolation, the following have also been tested using jaq, the Rust implementation of jq, as of April 13, 2023.

For infinite-precision integer arithmetic, use gojq or fq.

### Without Memoization

```mw
# input: [m,n]
def ack:
  .[0] as $m | .[1] as $n
  | if $m == 0 then $n + 1
    elif $n == 0 then [$m-1, 1] | ack
    else [$m-1, ([$m, $n-1 ] | ack)] | ack
    end ;
```

**Example:**

```mw
range(0;5) as $i
| range(0; if $i > 3 then 1 else 6 end) as $j
| "A(\($i),\($j)) = \( [$i,$j] | ack )"
```

**Output:**

```mw
# jq -n -r -f ackermann.jq
A(0,0) = 1
A(0,1) = 2
A(0,2) = 3
A(0,3) = 4
A(0,4) = 5
A(0,5) = 6
A(1,0) = 2
A(1,1) = 3
A(1,2) = 4
A(1,3) = 5
A(1,4) = 6
A(1,5) = 7
A(2,0) = 3
A(2,1) = 5
A(2,2) = 7
A(2,3) = 9
A(2,4) = 11
A(2,5) = 13
A(3,0) = 5
A(3,1) = 13
A(3,2) = 29
A(3,3) = 61
A(3,4) = 125
A(3,5) = 253
A(4,0) = 13
```

### With Memoization and Optimization

```mw
# input: [m,n, cache]
# output [value, updatedCache]
def ack:

  # input: [value,cache]; output: [value, updatedCache]
  def cache(key): .[1] += { (key): .[0] };
  
  def pow2: reduce range(0; .) as $i (1; .*2);
 
  .[0] as $m | .[1] as $n | .[2] as $cache
  | if   $m == 0 then [$n + 1, $cache]
    elif $m == 1 then [$n + 2, $cache]
    elif $m == 2 then [2 * $n + 3, $cache]
    elif $m == 3 then [8 * ($n|pow2) - 3, $cache]
    else
    (.[0:2]|tostring) as $key
    | $cache[$key] as $value
    | if $value then [$value, $cache]
      elif $n == 0 then
        ([$m-1, 1, $cache] | ack)
        | cache($key)
      else
        ([$m, $n-1, $cache ] | ack) 
        | [$m-1, .[0], .[1]] | ack
        | cache($key)
      end
    end;

def A(m;n): [m,n,{}] | ack | .[0];
```

**Examples:**

```mw
A(4;1)
```

**Output:**

```mw
65533
```

Using gojq:

```mw
A(4;2), A(3;1000000) | tostring | length
```

**Output:**

```mw
19729
301031
```


## Jsish

From javascript entry.

```mw
/* Ackermann function, in Jsish */

function ack(m, n) {
 return m === 0 ? n + 1 : ack(m - 1, n === 0  ? 1 : ack(m, n - 1));
}

if (Interp.conf('unitTest')) {
    Interp.conf({maxDepth:4096});
;    ack(1,3);
;    ack(2,3);
;    ack(3,3);
;    ack(1,5);
;    ack(2,5);
;    ack(3,5);
}

/*
=!EXPECTSTART!=
ack(1,3) ==> 5
ack(2,3) ==> 9
ack(3,3) ==> 61
ack(1,5) ==> 7
ack(2,5) ==> 13
ack(3,5) ==> 253
=!EXPECTEND!=
*/
```

**Output:**

```
prompt$ jsish --U Ackermann.jsi
ack(1,3) ==> 5
ack(2,3) ==> 9
ack(3,3) ==> 61
ack(1,5) ==> 7
ack(2,5) ==> 13
ack(3,5) ==> 253
```


## Julia

```mw
function ack(m,n)
    if m == 0
        return n + 1
    elseif n == 0
        return ack(m-1,1)
    else
        return ack(m-1,ack(m,n-1))
    end
end
```

**One-liner:**

```mw
ack2(m::Integer, n::Integer) = m == 0 ? n + 1 : n == 0 ? ack2(m - 1, 1) : ack2(m - 1, ack2(m, n - 1))
```

**Using memoization**, source:

```mw
using Memoize
@memoize ack3(m::Integer, n::Integer) = m == 0 ? n + 1 : n == 0 ? ack3(m - 1, 1) : ack3(m - 1, ack3(m, n - 1))
```

**Benchmarking**:

```
julia> @time ack2(4,1)
elapsed time: 71.98668457 seconds (96 bytes allocated)
65533

julia> @time ack3(4,1)
elapsed time: 0.49337724 seconds (30405308 bytes allocated)
65533
```


## K

Works with

:

Kona

```mw
   ack:{:[0=x;y+1;0=y;_f[x-1;1];_f[x-1;_f[x;y-1]]]}
   ack[2;2]
7
   ack[2;7]
17
```


## Kdf9 Usercode

```mw
V6; W0;
YS26000;
RESTART; J999; J999;
PROGRAM;                   (main program);
   V1 = B1212121212121212; (radix 10 for FRB);
   V2 = B2020202020202020; (high bits for decimal digits);
   V3 = B0741062107230637; ("A[3,"  in Flexowriter code);
   V4 = B0727062200250007; ("7] = " in Flexowriter code);
   V5 = B7777777777777777;

      ZERO; NOT; =M1;      (Q1 := 0/0/-1);
      SETAYS0; =M2; I2=2;  (Q2 := 0/2/AYS0: M2 is the stack pointer);
      SET 3; =RC7;         (Q7 := 3/1/0: C7 = m);
      SET 7; =RC8;         (Q8 := 7/1/0: C8 = n);
   JSP1;                   (call Ackermann function);
      V1; REV; FRB;        (convert result to base 10);
      V2; OR;              (convert decimal digits to characters);
      V5; REV;
      SHLD+24; =V5; ERASE; (eliminate leading zeros);
      SETAV5; =RM9;
      SETAV3; =I9;
      POAQ9;               (write result to Flexowriter);

999;  ZERO; OUT;           (terminate run);

P1; (To compute A[m, n]);

   99;
      J1C7NZ;           (to 1 if m ± 0);
         I8; =+C8;      (n := n + 1);
         C8;            (result to NEST);
      EXIT 1;           (return);
   *1;
      J2C8NZ;           (to 2 if n ± 0);
         I8; =C8;       (n := 1);
         DC7;           (m := m - 1);
      J99;              (tail recursion for A[m-1, 1]);
   *2;
         LINK; =M0M2;   (push return address);
         C7; =M0M2QN;   (push m);
         DC8;           (n := n - 1);
      JSP1;             (full recursion for A[m, n-1]);
         =C8;           (n := A[m, n-1]);
         M1M2; =C7;     (m := top of stack);
         DC7;           (m := m - 1);
         M-I2;          (pop stack);
         M0M2; =LINK;   (return address := top of stack);
      J99;              (tail recursion for A[m-1, A[m, n-1]]);

FINISH;
```


## Klingphix

```mw
:ack
    %n !n %m !m
 
    $m 0 ==
    ( [$n 1 +]
      [$n 0 ==
        ( [$m 1 - 1 ack]
          [$m 1 - $m $n 1 - ack ack]
        ) if
      ]
    ) if
;
 
3 6 ack print nl
msec print

" " input
```


## Klong

```mw
ack::{:[0=x;y+1:|0=y;.f(x-1;1);.f(x-1;.f(x;y-1))]}
ack(2;2)
```


## Kotlin

```mw
tailrec fun A(m: Long, n: Long): Long {
    require(m >= 0L) { "m must not be negative" }
    require(n >= 0L) { "n must not be negative" }
    if (m == 0L) {
        return n + 1L
    }
    if (n == 0L) {
        return A(m - 1L, 1L)
    }
    return A(m - 1L, A(m, n - 1L))
}

inline fun<T> tryOrNull(block: () -> T): T? = try { block() } catch (e: Throwable) { null }

const val N = 10L
const val M = 4L

fun main() {
    (0..M)
        .map { it to 0..N }
        .map { (m, Ns) -> (m to Ns) to Ns.map { n -> tryOrNull { A(m, n) } } }
        .map { (input, output) -> "A(${input.first}, ${input.second})" to output.map { it?.toString() ?: "?" } }
        .map { (input, output) -> "$input = $output" }
        .forEach(::println)
}
```

**Output:**

```
A(0, 0..10) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
A(1, 0..10) = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A(2, 0..10) = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
A(3, 0..10) = [5, 13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189]
A(4, 0..10) = [13, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?]
```


## Lambdatalk

```mw
{def ack
 {lambda {:m :n}
  {if {= :m 0}
   then {+ :n 1}
   else {if {= :n 0}
   then {ack {- :m 1} 1}
   else {ack {- :m 1} {ack :m {- :n 1}}}}}}}
-> ack

{S.map {ack 0} {S.serie 0 300000}}  // 2090ms
{S.map {ack 1} {S.serie 0 500}}     // 2038ms
{S.map {ack 2} {S.serie 0 70}}      // 2100ms
{S.map {ack 3} {S.serie 0 6}}       // 1800ms

{ack 2 700}     // 8900ms
-> 1403

{ack 3 7}       // 6000ms
-> 1021

{ack 4 1}       // too much
-> ???
```


## Lasso

```mw
#!/usr/bin/lasso9
 
define ackermann(m::integer, n::integer) => {
  if(#m == 0) => {
    return ++#n
  else(#n == 0)
    return ackermann(--#m, 1)
  else
    return ackermann(#m-1, ackermann(#m, --#n))
  }
}

with x in generateSeries(1,3),
     y in generateSeries(0,8,2)
do stdoutnl(#x+', '#y+': ' + ackermann(#x, #y))
```

**Output:**

```
1, 0: 2
1, 2: 4
1, 4: 6
1, 6: 8
1, 8: 10
2, 0: 3
2, 2: 7
2, 4: 11
2, 6: 15
2, 8: 19
3, 0: 5
3, 2: 29
3, 4: 125
3, 6: 509
3, 8: 2045
```


## LFE

```mw
(defun ackermann
  ((0 n) (+ n 1))
  ((m 0) (ackermann (- m 1) 1))
  ((m n) (ackermann (- m 1) (ackermann m (- n 1)))))
```


## Liberty BASIC

```mw
Print Ackermann(1, 2)

    Function Ackermann(m, n)
        Select Case
            Case (m < 0) Or (n < 0)
                Exit Function
            Case (m = 0)
                Ackermann = (n + 1)
            Case (m > 0) And (n = 0)
                Ackermann = Ackermann((m - 1), 1)
            Case (m > 0) And (n > 0)
                Ackermann = Ackermann((m - 1), Ackermann(m, (n - 1)))
        End Select
    End Function
```


## LiveCode

```mw
function ackermann m,n
    switch
        Case m = 0
            return n + 1
        Case (m > 0 And n = 0)
            return ackermann((m - 1), 1)
        Case (m > 0 And n > 0)
            return ackermann((m - 1), ackermann(m, (n - 1)))
    end switch
end ackermann
```


## Logo

```mw
to ack :i :j
  if :i = 0 [output :j+1]
  if :j = 0 [output ack :i-1 1]
  output ack :i-1 ack :i :j-1
end
```


## Logtalk

```mw
ack(0, N, V) :-
    !,
    V is N + 1.
ack(M, 0, V) :-
    !,
    M2 is M - 1,
    ack(M2, 1, V).
ack(M, N, V) :-
    M2 is M - 1,
    N2 is N - 1,
    ack(M, N2, V2),
    ack(M2, V2, V).
```


## LOLCODE

Translation of

:

C

```mw
HAI 1.3

HOW IZ I ackermann YR m AN YR n
    NOT m, O RLY?
        YA RLY, FOUND YR SUM OF n AN 1
    OIC

    NOT n, O RLY?
        YA RLY, FOUND YR I IZ ackermann YR DIFF OF m AN 1 AN YR 1 MKAY
    OIC

    FOUND YR I IZ ackermann YR DIFF OF m AN 1 AN YR...
     I IZ ackermann YR m AN YR DIFF OF n AN 1 MKAY MKAY
IF U SAY SO

IM IN YR outer UPPIN YR m TIL BOTH SAEM m AN 5
    IM IN YR inner UPPIN YR n TIL BOTH SAEM n AN DIFF OF 6 AN m
        VISIBLE "A(" m ", " n ") = " I IZ ackermann YR m AN YR n MKAY
    IM OUTTA YR inner
IM OUTTA YR outer

KTHXBYE
```


## Lua

```mw
function ack(M,N)
    if M == 0 then return N + 1 end
    if N == 0 then return ack(M-1,1) end
    return ack(M-1,ack(M, N-1))
end
```

### Stackless iterative solution with multiple precision, fast

```mw
 
#!/usr/bin/env luajit
local gmp = require 'gmp' ('libgmp')
local mpz, 		z_mul, 		z_add, 		z_add_ui, 		z_set_d = 
	gmp.types.z, gmp.z_mul,	gmp.z_add,	gmp.z_add_ui, 	gmp.z_set_d
local z_cmp, 	z_cmp_ui, 		z_init_d, 			z_set=
	gmp.z_cmp,	gmp.z_cmp_ui, 	gmp.z_init_set_d, 	gmp.z_set
local printf = gmp.printf

local function ack(i,n)
	local nxt=setmetatable({},  {__index=function(t,k) local z=mpz() z_init_d(z, 0) t[k]=z return z end})
	local goal=setmetatable({}, {__index=function(t,k) local o=mpz() z_init_d(o, 1) t[k]=o return o end})
	goal[i]=mpz() z_init_d(goal[i], -1)
	local v=mpz() z_init_d(v, 0) 
	local ic
	local END=n+1
	local ntmp,gtmp
	repeat
		ic=0
		ntmp,gtmp=nxt[ic], goal[ic]
		z_add_ui(v, ntmp, 1)
		while z_cmp(ntmp, gtmp) == 0 do
			z_set(gtmp,v)
			z_add_ui(ntmp, ntmp, 1)
			nxt[ic], goal[ic]=ntmp, gtmp
			ic=ic+1
			ntmp,gtmp=nxt[ic], goal[ic]
		end
		z_add_ui(ntmp, ntmp, 1)
		nxt[ic]=ntmp
	until z_cmp_ui(nxt[i], END) == 0
	return v
end

if #arg<1 then
	print("Ackermann: "..arg[0].." <num1> [num2]")
else
	printf("%Zd\n", ack(tonumber(arg[1]), arg[2] and tonumber(arg[2]) or 0))
end
```

**Output:**

```
> time ./ackermann_iter.lua 4 1
65533
./ackermann_iter.lua 4 1  0,01s user 0,01s system 95% cpu 0,015 total // AMD FX-8350@4 GHz
> time ./ackermann.lua 3 10                                              ⏎
8189
./ackermann.lua 3 10  0,22s user 0,00s system 98% cpu 0,222 total // recursive solution
> time ./ackermann_iter.lua 3 10
8189
./ackermann_iter.lua 3 10  0,00s user 0,00s system 92% cpu 0,009 total
```


## Lucid

```mw
ack(m,n)
 where
  ack(m,n) = if m eq 0 then n+1
                       else if n eq 0 then ack(m-1,1)
                                      else ack(m-1, ack(m, n-1)) fi
                       fi;
 end
```


## Luck

```mw
function ackermann(m: int, n: int): int = (
   if m==0 then n+1
   else if n==0 then ackermann(m-1,1)
   else ackermann(m-1,ackermann(m,n-1))
)
```


## M2000 Interpreter

```mw
Module Checkit {
      Def ackermann(m,n) =If(m=0-> n+1, If(n=0-> ackermann(m-1,1), ackermann(m-1,ackermann(m,n-1))))
      For m = 0 to 3 {For n = 0 to 4 {Print m;" ";n;" ";ackermann(m,n)}}
}
Checkit

Module Checkit {
      Module Inner (ack) {
            For m = 0 to 3 {For n = 0 to 4 {Print m;" ";n;" ";ack(m,n)}} 
      }
      Inner lambda (m,n) ->If(m=0-> n+1, If(n=0-> lambda(m-1,1),lambda(m-1,lambda(m,n-1))))
}
Checkit
```


## M4

```mw
define(`ack',`ifelse($1,0,`incr($2)',`ifelse($2,0,`ack(decr($1),1)',`ack(decr($1),ack($1,decr($2)))')')')dnl
ack(3,3)
```

**Output:**

```
61 
```


## MACRO-11

```mw
        .TITLE  ACKRMN
        .MCALL  .TTYOUT,.EXIT
ACKRMN::JMP     MKTBL

        ; R0 = ACK(R0,R1)
ACK:    MOV     SP,R2           ; KEEP OLD STACK PTR
        MOV     #ASTK,SP        ; USE PRIVATE STACK
        JSR     PC,1$
        MOV     R2,SP           ; RESTORE STACK PTR
        RTS     PC
1$:     TST     R0
        BNE     2$
        INC     R1
        MOV     R1,R0 
        RTS     PC
2$:     TST     R1
        BNE     3$
        DEC     R0
        INC     R1
        BR      1$
3$:     MOV     R0,-(SP)
        DEC     R1
        JSR     PC,1$
        MOV     R0,R1
        MOV     (SP)+,R0
        DEC     R0
        BR      1$
        .BLKB   4000           ; BIG STACK
ASTK    =       .

        ; PRINT TABLE
MMAX    =       4
NMAX    =       7
MKTBL:  CLR     R3
1$:     CLR     R4
2$:     MOV     R3,R0
        MOV     R4,R1 
        JSR     PC,ACK
        JSR     PC,PR0 
        INC     R4
        CMP     R4,#NMAX
        BLT     2$
        MOV     #15,R0
        .TTYOUT
        MOV     #12,R0
        .TTYOUT
        INC     R3
        CMP     R3,#MMAX
        BLT     1$
        .EXIT
        
        ; PRINT NUMBER IN R0 AS DECIMAL
PR0:    MOV     #4$,R1
1$:     MOV     #-1,R2
2$:     INC     R2
        SUB     #12,R0
        BCC     2$
        ADD     #72,R0
        MOVB    R0,-(R1)
        MOV     R2,R0
        BNE     1$
3$:     MOVB    (R1)+,R0
        .TTYOUT
        BNE     3$
        RTS     PC
        .ASCII  /...../
4$:     .BYTE   11,0
        .END    ACKRMN
```

**Output:**

```
1       2       3       4       5       6       7
2       3       4       5       6       7       8
3       5       7       9       11      13      15
5       13      29      61      125     253     509
```
