---
title: "FizzBuzz (part 4/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/7
---

## Java

```mw
public class FizzBuzz {
    public static void main(String[] args) {
        for (int number = 1; number <= 100; number++) {
            if (number % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (number % 3 == 0) {
                System.out.println("Fizz");
            } else if (number % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(number);
            }
        }
    }
}
```

**Or:**

```mw
public class FizzBuzz {
    public static void main(String[] args) {
        int number = 1;
        while (number <= 100) {
            if (number % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (number % 3 == 0) {
                System.out.println("Fizz");
            } else if (number % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(number);
            }
            number++;
        }
    }
}
```

**Or:**

```mw
public class FizzBuzz {
    public static void main(String[] args) {
        int number = 1;
        while (number <= 100) {
            System.out.println(number % 15 == 0 ? "FizzBuzz" : number % 3 == 0 ? "Fizz" : number % 5 == 0 ? "Buzz" : number);
            number++;
        }
    }
}
```

**Or:**

```mw
import java.util.stream.IntStream;
class FizzBuzzJdk12 {
    public static void main(String[] args) {
        IntStream.range(1,101)
        .mapToObj(i->switch (i%15) {
            case 0 -> "FizzBuzz";
            case 3, 6, 9, 12 -> "Fizz";
            case 5, 10 -> "Buzz";
            default -> Integer.toString(i);
        })
        .forEach(System.out::println)
        ;
    }
}
```

**Or:**

```mw
import java.util.stream.IntStream;

class FizzBuzzJdk12 {
    static final int FIZZ_FLAG = 0x8000_0000;
    static final int BUZZ_FLAG = 0x4000_0000;
    static final int FIZZ_BUZZ_FLAG = FIZZ_FLAG|BUZZ_FLAG;
    static final int[] FLAGS = new int[] {
        FIZZ_BUZZ_FLAG|0, 1, 2, FIZZ_FLAG|3, 4, 
        BUZZ_FLAG|5, FIZZ_FLAG|6, 7, 8, FIZZ_FLAG|9,
        BUZZ_FLAG|10, 11, FIZZ_FLAG|12, 13, 14
    };
    public static void main(String[] args) {
    IntStream.iterate(0,i->++i)
       .flatMap(i -> IntStream.range(0,15).map(j->FLAGS[j]+15*i))
       .mapToObj(
        // JDK12 switch expression ...
        n-> switch(n & FIZZ_BUZZ_FLAG) {
            case FIZZ_BUZZ_FLAG -> "fizzbuzz";
            case FIZZ_FLAG -> "fizz";
            case BUZZ_FLAG -> "buzz";
            default -> Integer.toString(~FIZZ_BUZZ_FLAG & n);
            }
       )
       .skip(1)
       .limit(100)
       .forEach(System.out::println)
       ;
    }
}
```


## JavaScript

### ES5

```mw
var fizzBuzz = function () {
  var i, output;
  for (i = 1; i < 101; i += 1) {
    output = '';
    if (!(i % 3)) { output += 'Fizz'; }
    if (!(i % 5)) { output += 'Buzz'; }
    console.log(output || i);//empty string is false, so we short-circuit
  }
};
```

Alternate version with ghetto pattern matching

```mw
for (var i = 1; i <= 100; i++) {
  console.log({
    truefalse: 'Fizz', 
    falsetrue: 'Buzz', 
    truetrue: 'FizzBuzz'
  }[(i%3==0) + '' + (i%5==0)] || i)
}
```

Or very tersely:

```mw
for(i=1;i<101;i++)console.log((x=(i%3?'':'Fizz')+(i%5?'':'Buzz'))?x:i);
```

Or with even less characters:

```mw
for(i=1;i<101;i++)console.log((i%3?'':'Fizz')+(i%5?'':'Buzz')||i)
```

Or, in a more functional style, without mutations

```mw
(function rng(i) {
    return i ? rng(i - 1).concat(i) : []
})(100).map(
    function (n) {
        return n % 3 ? (
            n % 5 ? n : "Buzz"
        ) : (
            n % 5 ? "Fizz" : "FizzBuzz"
        )
    }
).join(' ')
```

### ES6

```mw
(() => {

    // FIZZBUZZ --------------------------------------------------------------

    // fizzBuzz :: Int -> String
    const fizzBuzz = n =>
        caseOf(n, [
            [x => x % 15 === 0, "FizzBuzz"],
            [x => x % 3 === 0, "Fizz"],
            [x => x % 5 === 0, "Buzz"]
        ], n.toString());

    // GENERIC FUNCTIONS -----------------------------------------------------

    // caseOf :: a -> [(a -> Bool, b)] -> b -> b
    const caseOf = (e, pvs, otherwise) =>
        pvs.reduce((a, [p, v]) =>
            a !== otherwise ? a : (p(e) ? v : a), otherwise);

    // enumFromTo :: Int -> Int -> [Int]
    const enumFromTo = (m, n) =>
        Array.from({
            length: Math.floor(n - m) + 1
        }, (_, i) => m + i);

    // map :: (a -> b) -> [a] -> [b]
    const map = (f, xs) => xs.map(f);

    // unlines :: [String] -> String
    const unlines = xs => xs.join('\n');

    // TEST ------------------------------------------------------------------
    return unlines(
        map(fizzBuzz, enumFromTo(1, 100))
    );
})();
```

A functional implementation:

```mw
const factors = [[3, 'Fizz'], [5, 'Buzz']]
const fizzBuzz = num => factors.map(([factor,text]) => (num % factor)?'':text).join('') || num
const range1 = x => [...Array(x+1).keys()].slice(1)
const outputs = range1(100).map(fizzBuzz)

console.log(outputs.join('\n'))
```

Or composing generic functions, and without use of modulo (or other) numeric tests:

Translation of

:

Python

Translation of

:

Haskell

```mw
(() => {
    'use strict';

    // main :: IO ()
    const main = () => {

        // FIZZBUZZ ---------------------------------------

        // fizzBuzz :: Generator [String]
        const fizzBuzz = () => {
            const fb = n => k => cycle(
                replicate(n - 1)('').concat(k)
            );
            return zipWith(
                liftA2(flip)(bool)(isNull)
            )(
                zipWith(append)(fb(3)('fizz'))(fb(5)('buzz'))
            )(fmap(str)(enumFrom(1)));
        };

        // TEST -------------------------------------------
        console.log(
            unlines(
                take(100)(
                    fizzBuzz()
                )
            )
        );
    };

    // GENERIC FUNCTIONS ----------------------------------

    // Just :: a -> Maybe a
    const Just = x => ({
        type: 'Maybe',
        Nothing: false,
        Just: x
    });

    // Nothing :: Maybe a
    const Nothing = () => ({
        type: 'Maybe',
        Nothing: true,
    });

    // Tuple (,) :: a -> b -> (a, b)
    const Tuple = a => b => ({
        type: 'Tuple',
        '0': a,
        '1': b,
        length: 2
    });

    // append (++) :: [a] -> [a] -> [a]
    // append (++) :: String -> String -> String
    const append = xs => ys => xs.concat(ys);

    // bool :: a -> a -> Bool -> a
    const bool = f => t => p =>
        p ? t : f;

    // cycle :: [a] -> Generator [a]
    function* cycle(xs) {
        const lng = xs.length;
        let i = 0;
        while (true) {
            yield(xs[i])
            i = (1 + i) % lng;
        }
    }

    // enumFrom :: Int => Int -> [Int]
    function* enumFrom(x) {
        let v = x;
        while (true) {
            yield v;
            v = 1 + v;
        }
    }

    // flip :: (a -> b -> c) -> b -> a -> c
    const flip = f =>
        x => y => f(y)(x);

    // fmap <$> :: (a -> b) -> Gen [a] -> Gen [b]
    const fmap = f =>
        function*(gen) {
            let v = take(1)(gen);
            while (0 < v.length) {
                yield(f(v[0]))
                v = take(1)(gen)
            }
        };

    // fst :: (a, b) -> a
    const fst = tpl => tpl[0];

    // isNull :: [a] -> Bool
    // isNull :: String -> Bool
    const isNull = xs =>
        1 > xs.length;

    // Returns Infinity over objects without finite length.
    // This enables zip and zipWith to choose the shorter
    // argument when one is non-finite, like cycle, repeat etc

    // length :: [a] -> Int
    const length = xs =>
        (Array.isArray(xs) || 'string' === typeof xs) ? (
            xs.length
        ) : Infinity;

    // liftA2 :: (a0 -> b -> c) -> (a -> a0) -> (a -> b) -> a -> c
    const liftA2 = op => f => g =>
        // Lift a binary function to a composition
        // over two other functions.
        // liftA2 (*) (+ 2) (+ 3) 7 == 90
        x => op(f(x))(g(x));

    // replicate :: Int -> a -> [a]
    const replicate = n => x =>
        Array.from({
            length: n
        }, () => x);

    // snd :: (a, b) -> b
    const snd = tpl => tpl[1];

    // str :: a -> String
    const str = x => x.toString();

    // take :: Int -> [a] -> [a]
    // take :: Int -> String -> String
    const take = n => xs =>
        'GeneratorFunction' !== xs.constructor.constructor.name ? (
            xs.slice(0, n)
        ) : [].concat.apply([], Array.from({
            length: n
        }, () => {
            const x = xs.next();
            return x.done ? [] : [x.value];
        }));

    // The first argument is a sample of the type
    // allowing the function to make the right mapping

    // uncons :: [a] -> Maybe (a, [a])
    const uncons = xs => {
        const lng = length(xs);
        return (0 < lng) ? (
            lng < Infinity ? (
                Just(Tuple(xs[0])(xs.slice(1))) // Finite list
            ) : (() => {
                const nxt = take(1)(xs);
                return 0 < nxt.length ? (
                    Just(Tuple(nxt[0])(xs))
                ) : Nothing();
            })() // Lazy generator
        ) : Nothing();
    };

    // unlines :: [String] -> String
    const unlines = xs => xs.join('\n');

    // zipWith :: (a -> b -> c) Gen [a] -> Gen [b] -> Gen [c]
    const zipWith = f => ga => gb => {
        function* go(ma, mb) {
            let
                a = ma,
                b = mb;
            while (!a.Nothing && !b.Nothing) {
                let
                    ta = a.Just,
                    tb = b.Just
                yield(f(fst(ta))(fst(tb)));
                a = uncons(snd(ta));
                b = uncons(snd(tb));
            }
        }
        return go(uncons(ga), uncons(gb));
    };

    // MAIN ---
    return main();
})();
```


## Joy

The following program first defines a function "out", that handles the Fizz / Buzz logic, and then loops from 1 to 100 mapping the function onto each number, and printing ("put") the output.

```mw
DEFINE out == [[[15 rem null] "FizzBuzz"]
[[ 3 rem null] "Fizz"]
[[ 5 rem null] "Buzz"]
[]] cond
[putchars pop] [put] ifstring '\n putch.

100 [] [out] primrec.
```


## jq

```mw
range(1;101)
  | if   . % 15 == 0 then "FizzBuzz"
    elif . % 5  == 0 then "Buzz"
    elif . % 3  == 0 then "Fizz"
    else .
    end
```

Another solution:

```mw
range(100) + 1 | [(
	(select(. % 3 == 0) | "Fizz"),
	(select(. % 5 == 0) | "Buzz")
) // tostring] | join("")
```


## Julia

Works with

:

Julia

version 1.8.5

One basic solution:

```mw
for i in 1:100
    if i % 15 == 0
        println("FizzBuzz")
    elseif i % 3 == 0
        println("Fizz")
    elseif i % 5 == 0
        println("Buzz")
    else
        println(i)
    end
end
```

Another possible solution:

```mw
collect(i % 15 == 0 ? "FizzBuzz" : i % 5 == 0 ? "Buzz" : i % 3 == 0 ? "Fizz" : i for i in 1:100) |> println
```

A 3rd possible solution:

```mw
fb(i::Integer) = "Fizz" ^ (i % 3 == 0) * "Buzz" ^ (i % 5 == 0) * string(i) ^ (i % 3 != 0 && i % 5 != 0)
for i in 1:100 println(fb(i)) end
```

A 4th one:

```mw
println.(map(fb, 1:100))
```

A fifth (DRY, Don't Repeat Yourself) possible solution:

```mw
for i in 1:100
    msg = "Fizz" ^ (i % 3 == 0) * "Buzz" ^ (i % 5 == 0)
    println(isempty(msg) ? i : msg)
end
```


## K

### Solution 0

For kona:

```mw
{,/$(s;x)@~#s:`Fizz`Buzz@&~x!'3 5}'1+!30
```

For k6 and oK, change `x!'3 5` to `3 5!'x`. This method first chooses the symbols `Fizz and/or `Buzz (or neither, giving the empty symbol vector 0#`) based on the input's divisibility by 3 and 5, naming the result `s`. The `(s;x)@~#s` means "index into the pair `s;x` based on whether `s` is empty"), effectively functioning as an if-else. This result is then cast to a (potentially nested) string vector (`$`) and raveled (flattened into a single vector) (`,/`).

### Solution 1

```mw
  {:[0=x!15;`0:,"FizzBuzz";0=x!3;`0:,"Fizz";0=x!5;`0:,"Buzz";`0:,$x]}'1+!100
```

### Solution 2

```mw
`0:\:{:[0=#a:{,/$(:[0=x!3;"Fizz"];:[0=x!5;"Buzz"])}@x;$x;a]}'1_!101
```

### Solution 3

```mw
fizzbuzz:{
  v:1+!x
  i:(&0=)'v!/:3 5 15
  r:@[v;i 0;{"Fizz"}]
  r:@[r;i 1;{"Buzz"}]
  @[r;i 2;{"FizzBuzz"}]}

`0:$fizzbuzz 100
```


## Kamailio Script

To run it, send a SIP message to the server and FizzBuzz will appear in the logs.

This will only work up to 100 because Kamailio terminates all while loops after 100 iterations.

```mw
# FizzBuzz
log_stderror=yes
loadmodule "pv"
loadmodule "xlog"
 
route {
    $var(i) = 1;
    while ($var(i) <= 1000) {
        if ($var(i) mod 15 == 0) {
            xlog("FizzBuzz\n");
        } else if ($var(i) mod 5 == 0) {
            xlog("Buzz\n");
        } else if ($var(i) mod 3 == 0) {
            xlog("Fizz\n");
        } else {
            xlog("$var(i)\n");
        }
        $var(i) = $var(i) + 1;
    }
}
```


## KatLang

```mw
FizzBuzz(1, 1, i) = 'FizzBuzz'
FizzBuzz(1, 0, i) = 'Fizz'
FizzBuzz(0, 1, i) = 'Buzz'
FizzBuzz(0, 0, i) = i

range(1, 100).map{FizzBuzz(i mod 3 == 0, i mod 5 == 0, i)}
```


## Kaya

```mw
// fizzbuzz in Kaya
program fizzbuzz;

Void fizzbuzz(Int size) {
    for i in [1..size] {
        if (i % 15 == 0) {
            putStrLn("FizzBuzz");
        } else if (i % 5 == 0) {
            putStrLn("Buzz");
        } else if (i % 3 == 0) {
            putStrLn("Fizz");
        } else {
            putStrLn( string(i) );
        }
    }
}

Void main() {
    fizzbuzz(100);
}
```


## KL1

```mw
:- module main.

main :-
    nats(100, Nats),
    fizzbuzz(Nats, Output),
    display(Output).

nats(Max, Out) :-
    nats(Max, 1, Out).
nats(Max, Count, Out) :- Count =< Max |
    Out = [Count|NewOut],
    NewCount := Count + 1,
    nats(Max, NewCount, NewOut).
nats(Max, Count, Out) :- Count > Max |
    Out = [].

fizzbuzz([N|Rest], Out) :- N mod 3 =:= 0, N mod 5 =:= 0 |
    Out = ['FizzBuzz' | NewOut],
    fizzbuzz(Rest, NewOut).
fizzbuzz([], Out) :-
    Out = [].
alternatively.
fizzbuzz([N|Rest], Out) :- N mod 3 =:= 0 |
    Out = ['Fizz' | NewOut],
    fizzbuzz(Rest, NewOut).
fizzbuzz([N|Rest], Out) :- N mod 5 =:= 0 |
    Out = ['Buzz' | NewOut],
    fizzbuzz(Rest, NewOut).
alternatively.
fizzbuzz([N|Rest], Out) :-
    Out = [N | NewOut],
    fizzbuzz(Rest, NewOut).

display([Message|Rest]) :-
    io:outstream([print(Message), nl]),
    display(Rest).
display([]).
```


## Klong

```mw
{:[0=x!15;:FizzBuzz:|0=x!5;:Buzz:|0=x!3;:Fizz;x]}'1+!100
```


## Komodo

```mw
let fizzBuzz(n) :=
    let fb(0, 0) := "fizzbuzz"
    let fb(0, _) := "fizz"
    let fb(_, 0) := "buzz"
    let fb(_, _) := n
    fb(n % 3, n % 5)

for i in 1..101 do println(fizzBuzz(i))
```


## Kotlin

### Imperative solution

```mw
fun fizzBuzz() {
    for (number in 1..100) {
        println(
            when {
                number % 15 == 0 -> "FizzBuzz"
                number % 3 == 0 -> "Fizz"
                number % 5 == 0 -> "Buzz"
                else -> number
            }
        )
    }
}
```

### Functional solution 1

```mw
fun fizzBuzz1() {
    fun fizzBuzz(x: Int) = if (x % 15 == 0) "FizzBuzz" else x.toString()
    fun fizz(x: Any) = if (x is Int && x % 3 == 0) "Buzz" else x
    fun buzz(x: Any) = if (x is Int && x.toInt() % 5 == 0) "Fizz" else x

    (1..100).map { fizzBuzz(it) }.map { fizz(it) }.map { buzz(it) }.forEach { println(it) }
}
```

### Functional solution 2

```mw
fun fizzBuzz2() {
    fun fizz(x: Pair<Int, StringBuilder>) = if(x.first % 3 == 0) x.apply { second.append("Fizz") } else x
    fun buzz(x: Pair<Int, StringBuilder>) = if(x.first % 5 == 0) x.apply { second.append("Buzz") } else x
    fun none(x: Pair<Int, StringBuilder>) = if(x.second.isBlank()) x.second.apply { append(x.first) } else x.second

    (1..100).map { Pair(it, StringBuilder()) }
            .map { fizz(it) }
            .map { buzz(it) }
            .map { none(it) }
            .forEach { println(it) }
}
```

### Short version with mapOf

```mw
fun fizzBuzz() {
    (1..100).forEach { println(mapOf(0 to it, it % 3 to "Fizz", it % 5 to "Buzz", it % 15 to "FizzBuzz")[0]) }
}
```


## KQL

```mw
range i from 1 to 100 step 1
| project Result =
    case(
        i % 15 == 0, "FizzBuzz",
        i % 3 == 0, "Fizz",
        i % 5 == 0, "Buzz",
        tostring(i)
    )
```


## KSI

```mw
`plain
[1 100] `for pos : n ~
	out = []
	n `mod 3 == 0 ? out.# = 'Fizz' ;
	n `mod 5 == 0 ? out.# = 'Buzz' ;
	(out `or n) #write_ln #
;
```


## LabVIEW

This image is a VI Snippet, an executable image of LabVIEW code. The LabVIEW version is shown on the top-right hand corner. You can download it, then drag-and-drop it onto the LabVIEW block diagram from a file browser, and it will appear as runnable, editable code.


## Lambdatalk

```mw
1. direct:

{S.map 
 {lambda {:i}
  {if {= {% :i 15} 0} 
   then fizzbuzz 
   else {if {= {% :i 3} 0}
   then fizz 
   else {if {= {% :i 5} 0}
   then buzz 
   else :i}}}} 
 {S.serie 1 100}}
-> 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 31 32 fizz 34 buzz fizz 37 38 fizz buzz 41 fizz 43 44 fizzbuzz 46 47 fizz 49 buzz fizz 52 53 fizz buzz 56 fizz 58 59 fizzbuzz 61 62 fizz 64 buzz fizz 67 68 fizz buzz 71 fizz 73 74 fizzbuzz 76 77 fizz 79 buzz fizz 82 83 fizz buzz 86 fizz 88 89 fizzbuzz 91 92 fizz 94 buzz fizz 97 98 fizz buzz

2. via a function

{def fizzbuzz
 {lambda {:i :n}
  {if {> :i :n}
   then .
   else {if {= {% :i 15} 0} 
   then fizzbuzz 
   else {if {= {% :i 3} 0}
   then fizz 
   else {if {= {% :i 5} 0}
   then buzz 
   else :i}}} {fizzbuzz {+ :i 1} :n}
}}}
-> fizzbuzz

{fizzbuzz 1 100}
-> same as above.
```


## Lang

```mw
$i = 1
while($i <= 100) {
	if($i % 15 == 0) {
		fn.println(FizzBuzz)
	}elif($i % 5 == 0) {
		fn.println(Buzz)
	}elif($i % 3 == 0) {
		fn.println(Fizz)
	}else {
		fn.println($i)
	}
	
	$i += 1
}
```


## langur

```mw
for i of 100 {
    writeln switch(0; i rem 15: "FizzBuzz"; i rem 5: "Buzz"; i rem 3: "Fizz"; i)
}
```


## Lasso

```mw
with i in generateSeries(1, 100)
select ((#i % 3 == 0 ? 'Fizz' | '') + (#i % 5 == 0 ? 'Buzz' | '') || #i)
```


## LaTeX

Library:

ifthen

Library:

intcalc

This version uses the ifthen and intcalc packages. There sure are more native solutions including solutions in plain TeX, but for me this is a readable and comprehensible one.

```mw
\documentclass{minimal}
\usepackage{ifthen}
\usepackage{intcalc}
\newcounter{mycount}
\newboolean{fizzOrBuzz}
\newcommand\fizzBuzz[1]{%
\setcounter{mycount}{1}\whiledo{\value{mycount}<#1}
    {
    \setboolean{fizzOrBuzz}{false}
    \ifthenelse{\equal{\intcalcMod{\themycount}{3}}{0}}{\setboolean{fizzOrBuzz}{true}Fizz}{}
    \ifthenelse{\equal{\intcalcMod{\themycount}{5}}{0}}{\setboolean{fizzOrBuzz}{true}Buzz}{}
    \ifthenelse{\boolean{fizzOrBuzz}}{}{\themycount}
    \stepcounter{mycount}
    \\
    }
}
\begin{document}
\fizzBuzz{101}
\end{document}
```


## LDPL

```mw
data:
i is number
n is number

procedure:
for i from 1 to 101 step 1 do
    modulo i by 15 in n
    if n is equal to 0 then
        display "FizzBuzz" lf
        continue
    end if
    modulo i by 5 in n
    if n is equal to 0 then
        display "Buzz" lf
        continue
    end if
    modulo i by 3 in n
    if n is equal to 0 then
        display "Fizz" lf
        continue
    end if
    display i lf
repeat
```


## Lean

Lean 4:

```mw
def fizz : String :=
  "Fizz"

def buzz : String :=
  "Buzz"

def newLine : String :=
  "\n"

def isDivisibleBy (n : Nat) (m : Nat) : Bool :=
  match m with
  | 0 => false
  | (k + 1) => (n % (k + 1)) = 0

def getTerm (n : Nat) : String :=
  if (isDivisibleBy n 15) then (fizz ++ buzz)
  else if (isDivisibleBy n 3) then fizz
  else if (isDivisibleBy n 5) then buzz
  else toString (n)

def range (a : Nat) (b : Nat) : List (Nat) :=
  match b with
  | 0 => []
  | m + 1 => a :: (range (a + 1) m)

def getTerms (n : Nat) : List (String) :=
  (range 1 n).map (getTerm) 

def addNewLine (accum : String) (elem : String) : String :=
  accum ++ elem ++ newLine

def fizzBuzz : String :=
  (getTerms 100).foldl (addNewLine) ("")

def main : IO Unit :=
  IO.println (fizzBuzz)

#eval main
```


## Liberty BASIC

See FizzBuzz/Basic


## LIL

```mw
# fizzbuzz in LIL
for {set i 1} {$i <= 100} {inc i} {
    set show ""
    if {[expr $i % 3 == 0]} {set show "Fizz"}
    if {[expr $i % 5 == 0]} {set show $show"Buzz"}
    if {[expr [length $show] == 0]} {set show $i}
    print $show
}
```

**Output:**

```
prompt$ lil fizzbuzz.lil | sed -n '1,16p'
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```


## LiveCode

```mw
repeat with i = 1 to 100
    switch
        case i mod 15 = 0
            put "FizzBuzz" & cr after fizzbuzz
            break
        case i mod 5 = 0
            put "Buzz" & cr after fizzbuzz
            break
        case i mod 3 = 0
            put "Fizz" & cr after fizzbuzz
            break
        default
            put i & cr after fizzbuzz
    end switch 
end repeat
put fizzbuzz
```


## LiveScript

See: http://livescript.net/blog/fizzbuzzbazz.html

```mw
[1 to 100] map -> [k + \zz for k, v of {Fi: 3, Bu: 5} | it % v < 1] * '' || it
```


## LLVM

```mw
; ModuleID = 'fizzbuzz.c'
; source_filename = "fizzbuzz.c"
; target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"
; target triple = "x86_64-pc-windows-msvc19.21.27702"
 
; This is not strictly LLVM, as it uses the C library function "printf".
; LLVM does not provide a way to print values, so the alternative would be
; to just load the string into memory, and that would be boring.

; Additional comments have been inserted, as well as changes made from the output produced by clang such as putting more meaningful labels for the jumps

$"\01??_C@_09NODAFEIA@FizzBuzz?6?$AA@" = comdat any
$"\01??_C@_05KEBFOHOF@Fizz?6?$AA@" = comdat any
$"\01??_C@_05JKJENPHA@Buzz?6?$AA@" = comdat any
$"\01??_C@_03PMGGPEJJ@?$CFd?6?$AA@" = comdat any

;--- String constant defintions
@"\01??_C@_09NODAFEIA@FizzBuzz?6?$AA@" = linkonce_odr unnamed_addr constant [10 x i8] c"FizzBuzz\0A\00", comdat, align 1
@"\01??_C@_05KEBFOHOF@Fizz?6?$AA@" = linkonce_odr unnamed_addr constant [6 x i8] c"Fizz\0A\00", comdat, align 1
@"\01??_C@_05JKJENPHA@Buzz?6?$AA@" = linkonce_odr unnamed_addr constant [6 x i8] c"Buzz\0A\00", comdat, align 1
@"\01??_C@_03PMGGPEJJ@?$CFd?6?$AA@" = linkonce_odr unnamed_addr constant [4 x i8] c"%d\0A\00", comdat, align 1

;--- The declaration for the external C printf function.
declare i32 @printf(i8*, ...)

; Function Attrs: noinline nounwind optnone uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 1, i32* %1, align 4
;--- It does not seem like this branch can be removed
  br label %loop

;--- while (i <= 100)
loop:
  %2 = load i32, i32* %1, align 4
  %3 = icmp sle i32 %2, 100
  br i1 %3, label %divisible_15, label %finished

;--- if (i % 15 == 0)
divisible_15:
  %4 = load i32, i32* %1, align 4
  %5 = srem i32 %4, 15
  %6 = icmp eq i32 %5, 0
  br i1 %6, label %print_fizzbuzz, label %divisible_3

;--- Print 'FizzBuzz'
print_fizzbuzz:
  %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @"\01??_C@_09NODAFEIA@FizzBuzz?6?$AA@", i32 0, i32 0))
  br label %next

;--- if (i % 3 == 0)
divisible_3:
  %8 = load i32, i32* %1, align 4
  %9 = srem i32 %8, 3
  %10 = icmp eq i32 %9, 0
  br i1 %10, label %print_fizz, label %divisible_5

;--- Print 'Fizz'
print_fizz:
  %11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @"\01??_C@_05KEBFOHOF@Fizz?6?$AA@", i32 0, i32 0))
  br label %next

;--- if (i % 5 == 0)
divisible_5:
  %12 = load i32, i32* %1, align 4
  %13 = srem i32 %12, 5
  %14 = icmp eq i32 %13, 0
  br i1 %14, label %print_buzz, label %print_number

;--- Print 'Buzz'
print_buzz:
  %15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @"\01??_C@_05JKJENPHA@Buzz?6?$AA@", i32 0, i32 0))
  br label %next

;--- Print the number
print_number:
  %16 = load i32, i32* %1, align 4
  %17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @"\01??_C@_03PMGGPEJJ@?$CFd?6?$AA@", i32 0, i32 0), i32 %16)
;--- It does not seem like this branch can be removed
  br label %next

;--- i = i + 1
next:
  %18 = load i32, i32* %1, align 4
  %19 = add nsw i32 %18, 1
  store i32 %19, i32* %1, align 4
  br label %loop

;--- exit main
finished:
  ret i32 0
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0, !1}
!llvm.ident = !{!2}

!0 = !{i32 1, !"wchar_size", i32 2}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{!"clang version 6.0.1 (tags/RELEASE_601/final)"}
```


## Lobster

```mw
include "std.lobster"

forbias(100, 1) i:
    fb := (i % 3 == 0 and "fizz" or "") +
          (i % 5 == 0 and "buzz" or "")
    print fb.length and fb or "" + i
```


## Logo

```mw
to fizzbuzz :n
  output cond [ [[equal? 0 modulo :n 15] "FizzBuzz]
                [[equal? 0 modulo :n  5] "Buzz]
                [[equal? 0 modulo :n  3] "Fizz]
                [else :n] ]
end

repeat 100 [print fizzbuzz #]
```

"cond" was undefined in Joshua Bell's online interpreter. So here is a version that works there. It also works in UCB logo by using # instead of "repcount". This version also factors away modulo 15:

```mw
to fizzbuzz :n
 make "c "
  if equal? 0 modulo :n 5 [make "c "Buzz]
  if equal? 0 modulo :n 3 [make "c word "Fizz :c]
 output ifelse equal? :c " [:n] [:c]
end

repeat 100 [print fizzbuzz repcount]
```

Lhogho can use the above code, except that 'modulo' must be replaced with 'remainder'.


## LOLCODE

See FizzBuzz/EsoLang


## LSE

```mw
1* FIZZBUZZ en L.S.E. 
10 CHAINE FB
20 FAIRE 45 POUR I_1 JUSQUA 100 
30 FB_SI &MOD(I,3)=0 ALORS SI &MOD(I,5)=0 ALORS 'FIZZBUZZ' SINON 'FIZZ' SINON SI &MOD(I,5)=0 ALORS 'BUZZ' SINON ''
40 AFFICHER[U,/] SI FB='' ALORS I SINON FB
45*FIN BOUCLE
50 TERMINER
100 PROCEDURE &MOD(A,B) LOCAL A,B
110 RESULTAT A-B*ENT(A/B)
```


## Lua

### If/else Ladder

```mw
for i = 1, 100 do
	if i % 15 == 0 then
		print("FizzBuzz")
	elseif i % 3 == 0 then
		print("Fizz")
	elseif i % 5 == 0 then
		print("Buzz")
	else
		print(i)
	end
end
```

### Concatenation

```mw
for i = 1, 100 do
	output = ""
	if i % 3 == 0 then
		output = output.."Fizz"
	end
	if i % 5 == 0 then
		output = output.."Buzz"
	end
	if(output == "") then
		output = i
	end
	print(output)
end
```

### Quasi bit field

```mw
word = {"Fizz", "Buzz", "FizzBuzz"}

for i = 1, 100 do
        print(word[(i % 3 == 0 and 1 or 0) + (i % 5 == 0 and 2 or 0)] or i)
end
```

### Lookup table

```mw
local t = {
        [0]  = "FizzBuzz",
        [3]  = "Fizz",
        [5]  = "Buzz",
        [6]  = "Fizz",
        [9]  = "Fizz",
        [10] = "Buzz",
        [12] = "Fizz"
}

for i = 1, 100 do
        print(t[i%15] or i)
end
```

### Metatable insertion

Sets any numeric key to its fizzbuzz value so that fizzbuzz[30] is "fizzbuzz"

```mw
local mt = {
	__newindex = (function (t, k, v)
		if type(k) ~= "number" then	rawset(t, k, v)
		elseif 0 == (k % 15) then	rawset(t, k, "fizzbuzz") 
		elseif 0 == (k % 5) then	rawset(t, k, "fizz") 
		elseif 0 == (k % 3) then	rawset(t, k, "buzz") 
		else 						rawset(t, k, k) end
		return t[k]
end)
}

local fizzbuzz = {}
setmetatable(fizzbuzz, mt)

for i=1,100 do fizzbuzz[i] = i end
for i=1,100 do print(fizzbuzz[i]) end
```

### Fast Version without Modulo

```mw
#!/usr/bin/env luajit
local to=arg[1] or tonumber(arg[1]) or 100
local CF,CB=3,5
local cf,cb=CF,CB
for i=1,to do
	cf,cb=cf-1,cb-1
	if cf~=0 and cb~=0 then
		io.write(i)
	else
		if cf==0 then
			cf=CF
			io.write("Fizz")
		end
		if cb==0 then
			cb=CB
			io.write("Buzz")
		end
	end
	io.write(", ")
end
```

**Output:**

```
> ./fizzbuzz.lua  
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz, %
```


## Luck

```mw
for i in range(1,101) do (
   if i%15 == 0 then print("FizzBuzz")
   else if i%3 == 0 then print("Fizz")
   else if i%5 == 0 then print("Buzz")
   else print(i)
)
```


## M2000 Interpreter

```mw
\\ one line, hard to read
For i=1 to 100 {If i mod 3=0 Then {if i mod 5=0 Then Print "FizzBuzz",  Else Print "Fizz",} Else {if i mod 5=0 Then Print "Buzz", else print i, } } : Print

\\ Better code
For i=1 to 100 {
      Push str$(i,0)+". "+if$(i mod 3=0->"Fizz","")+if$(i mod 5=0->"Buzz","")
      If stackitem$()="" then Drop : Continue
      Print Letter$
}

\\ Far Better Code
For i=1 to 100 {
      Printme(if$(i mod 3=0->"Fizz","")+if$(i mod 5=0->"Buzz",""))
}
Print
Sub Printme(a$)
      If a$<>"" Then Print a$, else Print i,
End Sub
```


## M4

```mw
define(`for',
   `ifelse($#,0,``$0'',
   `ifelse(eval($2<=$3),1,
   `pushdef(`$1',$2)$5`'popdef(`$1')$0(`$1',eval($2+$4),$3,$4,`$5')')')')

for(`x',1,100,1,
   `ifelse(eval(x%15==0),1,FizzBuzz,
   `ifelse(eval(x%3==0),1,Fizz,
   `ifelse(eval(x%5==0),1,Buzz,x)')')
')
```


## MACRO-11

```mw
        .TITLE  FIZBUZ
        .MCALL  .TTYOUT,.EXIT
FIZBUZ::MOV     #1,R2           ; COUNTER
        MOV     #3,R3           ; FIZZ COUNTER
        MOV     #5,R4           ; BUZZ COUNTER
NUMBER: CLR     R5
CHKFIZ: DEC     R3
        BNE     CHKBUZ
        MOV     #FIZZ,R1
        JSR     PC,PRSTR
        MOV     #3,R3
        INC     R5
CHKBUZ: DEC     R4
        BNE     CHKNUM
        MOV     #BUZZ,R1
        JSR     PC,PRSTR
        MOV     #5,R4
        INC     R5
CHKNUM: TST     R5
        BNE     NEXNUM
        MOV     R2,R0
        JSR     PC,PR0
NEXNUM: MOV     #NL,R1
        JSR     PC,PRSTR
        INC     R2
        CMP     R2,#^D100
        BLE     NUMBER
        .EXIT
        ; STRING DATA
FIZZ:   .ASCIZ  /FIZZ/
BUZZ:   .ASCIZ  /BUZZ/
NL:     .BYTE   15,12,0
        .EVEN
        ; PRINT NUMBER IN R0 AS DECIMAL
PR0:    MOV     R2,-(SP)
        MOV     #4$,R1
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
        MOV     (SP)+,R2
        RTS     PC
        .ASCII  /...../
4$:     .BYTE   0
        ; PRINT STRING IN R1
PRSTR:  MOVB    (R1)+,R0
        .TTYOUT
        BNE     PRSTR
        RTS     PC
        .END FIZBUZ
```


## MAD

```mw
            NORMAL MODE IS INTEGER
            VECTOR VALUES FIZZ = $4HFIZZ*$
            VECTOR VALUES BUZZ = $4HBUZZ*$
            VECTOR VALUES FIBU = $8HFIZZBUZZ*$
            VECTOR VALUES NUM  = $I2*$

            INTERNAL FUNCTION REM.(A,B) = A-(A/B)*B

            THROUGH LOOP, FOR I = 1, 1, I .G. 100
            WHENEVER REM.(I,15).E.0
                PRINT FORMAT FIBU
            OR WHENEVER REM.(I,5).E.0
                PRINT FORMAT BUZZ
            OR WHENEVER REM.(I,3).E.0
                PRINT FORMAT FIZZ
            OTHERWISE
                PRINT FORMAT NUM,I
LOOP        END OF CONDITIONAL

            END OF PROGRAM
```


## make

Works with

:

BSD make

Library:

jot

```mw
MOD3 = 0
MOD5 = 0
ALL != jot 100

all: say-100

.for NUMBER in $(ALL)

MOD3 != expr \( $(MOD3) + 1 \) % 3; true
MOD5 != expr \( $(MOD5) + 1 \) % 5; true

. if "$(NUMBER)" > 1
PRED != expr $(NUMBER) - 1
say-$(NUMBER): say-$(PRED)
. else
say-$(NUMBER):
. endif
. if "$(MOD3)$(MOD5)" == "00"
	@echo FizzBuzz
. elif "$(MOD3)" == "0"
	@echo Fizz
. elif "$(MOD5)" == "0"
	@echo Buzz
. else
	@echo $(NUMBER)
. endif

.endfor
```


## Maple

One line:

```mw
seq(print(`if`(modp(n,3)=0,`if`(modp(n,15)=0,"FizzBuzz","Fizz"),`if`(modp(n,5)=0,"Buzz",n))),n=1..100):
```

With a fizzbuzz function defined:

```mw
fizzbuzz1 := n->`if`(modp(n,3)=0,`if`(modp(n,15)=0,"FizzBuzz","Fizz"),`if`(modp(n,5)=0,"Buzz",n)):
for i to 100 do fizzbuzz1(i); od;
```

Using piecewise:

```mw
fizzbuzz2 := n->piecewise(modp(n,15)=0,"FizzBuzz",modp(n,3)=0,"Fizz",modp(n,5)=0,"Buzz",n):
for i to 100 do fizzbuzz2(i); od;
```

Using conventional if/then branches:

```mw
fizzbuzz3 := proc(n) local r;
  r:=map2(modp,n,[3,5]);
  if r=[0,0] then "FizzBuzz"
  elif r[1]=0 then "Fizz"
  elif r[2]=0 then "Buzz"
  else n fi;
end proc:
for i to 100 do fizzbuzz3(i); od;
```


## Mathematica / Wolfram Language

```mw
Do[Print[Which[Mod[i, 15] == 0, "FizzBuzz", Mod[i, 5] == 0, "Buzz", Mod[i, 3] == 0, "Fizz", True, i]], {i, 100}]
```

Using rules,

```mw
fizz[i_] := Mod[i, 3] == 0
buzz[i_] := Mod[i, 5] == 0
Range[100] /. {i_ /; fizz[i]&&buzz[i] :> "FizzBuzz", \
               i_?fizz :> "Fizz", i_?buzz :> "Buzz"}
```

Using rules, but different approach:

```mw
SetAttributes[f,Listable]
f[n_ /; Mod[n, 15] == 0] := "FizzBuzz";
f[n_ /; Mod[n, 3] == 0] := "Fizz";
f[n_ /; Mod[n, 5] == 0] := "Buzz";
f[n_] := n;

f[Range[100]]
```

An extendible version using Table

```mw
Table[If[# === "", i, #]&@StringJoin[
   Table[If[Divisible[i, First@nw], Last@nw, ""], 
         {nw, {{3, "Fizz"}, {5, "Buzz"}}}]], 
      {i, 1, 100}]
```

Another one-liner using Map (the /@ operator shorthand of it) and a pure function with a very readable Which

```mw
 Which[ Mod[#,15] == 0, "FizzBuzz", Mod[#, 3] == 0, "Fizz", Mod[#,5]==0, "Buzz",  True, #]& /@ Range[1,100]
```

Additional examples using DownValue pattern matching, the first without Mod'ing 15:

```mw
f[n_] := f[n, Mod[n, {3, 5}]]
f[_, {0, 0}] := "FizzBuzz"
f[_, {0, _}] := "Fizz"
f[_, {_, 0}] := "Buzz"
f[n_, {_, _}] := n

f /@ Range[100]
```

```mw
f[n_] := f[n, Mod[n, 15]]
f[_, 0] := "FizzBuzz"

f[n_, _] := f[n, Mod[n, {3, 5}]]
f[_, {0, _}] := "Fizz"
f[_, {_, 0}] := "Buzz"
f[n_, {_, _}] := n

f /@ Range[100]
```


## MATLAB

There are more sophisticated solutions to this task, but in the spirit of "lowest level of comprehension required to illustrate adequacy" this is what one might expect from a novice programmer (with a little variation in how the strings are stored and displayed).

```mw
function fizzBuzz() 
    for i = (1:100)
        if mod(i,15) == 0
           fprintf('FizzBuzz ')
        elseif mod(i,3) == 0
           fprintf('Fizz ')
        elseif mod(i,5) == 0
           fprintf('Buzz ')
        else
           fprintf('%i ',i)) 
        end
    end
    fprintf('\n');    
end
```

Here's a more extendible version that uses disp() to print the output:

```mw
function out = fizzbuzzS()
	nums = [3, 5];
	words = {'fizz', 'buzz'};
	for (n=1:100)
		tempstr = '';
		for (i = 1:2)
			if mod(n,nums(i))==0
				tempstr = [tempstr,  words{i}];
			end
		end
		if length(tempstr) == 0 
			disp(n);
		else 
			disp(tempstr);
		end
	end
end
```

**straightforward**

```mw
x            = string(1:100);
x(3:3:$)     = 'Fizz';
x(5:5:$)     = 'Buzz';
x(3*5:3*5:$) = 'FizzBuzz'
```


## Maxima

```mw
for n:1 thru 100 do
   if mod(n, 15) = 0 then (sprint("FizzBuzz"), newline())
   elseif mod(n, 3) = 0 then (sprint("Fizz"), newline())
   elseif mod(n,5) = 0 then (sprint("Buzz"), newline())
   else (sprint(n), newline());
```


## MAXScript

```mw
for i in 1 to 100 do
(
    case of
    (
        (mod i 15 == 0): (print "FizzBuzz")
        (mod i 5 == 0):  (print "Buzz")
        (mod i 3 == 0):  (print "Fizz")
        default:         (print i)
    )
)
```


## MEL

```mw
for($i=1; $i<=100; $i++)
{    
    if($i % 15 == 0)
        print "FizzBuzz\n";
    else if ($i % 3 == 0)
        print "Fizz\n";
    else if ($i % 5 == 0) 
        print "Buzz\n";
    else
        print ($i + "\n");
}
```


## Mercury

```mw
:- module fizzbuzz.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
:- implementation.
:- import_module int, string, bool.

:- func fizz(int) = bool.
fizz(N) = ( if N mod 3 = 0 then yes else no ).

:- func buzz(int) = bool.
buzz(N) = ( if N mod 5 = 0 then yes else no ).

%                N    3?    5?
:- func fizzbuzz(int, bool, bool) = string.
fizzbuzz(_, yes, yes) = "FizzBuzz".
fizzbuzz(_, yes, no)  = "Fizz".
fizzbuzz(_, no,  yes) = "Buzz".
fizzbuzz(N, no,  no)  = from_int(N).

main(!IO) :- main(1, 100, !IO).

:- pred main(int::in, int::in, io::di, io::uo) is det.
main(N, To, !IO) :-
    io.write_string(fizzbuzz(N, fizz(N), buzz(N)), !IO),
    io.nl(!IO),
    ( if N < To then
        main(N + 1, To, !IO)
    else
        true
    ).
```


## Metafont

```mw
for i := 1 upto 100:
message if i mod 15 = 0: "FizzBuzz" &
elseif i mod 3 = 0: "Fizz" &
elseif i mod 5 = 0: "Buzz" &
else: decimal i & fi "";
endfor
end
```


## Microsoft Small Basic

Translation of

:

GW-BASIC

```mw
For n = 1 To 100
  op = ""
  If Math.Remainder(n, 3) = 0 Then
    op = "Fizz"
  EndIf  
  IF Math.Remainder(n, 5) = 0 Then
    op = text.Append(op, "Buzz")
  EndIf
  If op = "" Then 
    TextWindow.WriteLine(n)
  Else 
    TextWindow.WriteLine(op)
  EndIf  
EndFor
```


## min

Works with

:

min

version 0.19.3

```mw
0 (
  succ false :hit
  (3 mod 0 ==) ("Fizz" print! true @hit) when
  (5 mod 0 ==) ("Buzz" print! true @hit) when
  (hit) (print) unless newline
) 100 times
```


## Minimal BASIC

See FizzBuzz/Basic


## MiniScript

```mw
for i in range(1,100)
    if i % 15 == 0 then
        print "FizzBuzz"
    else if i % 3 == 0 then
        print "Fizz"
    else if i % 5 == 0 then
        print "Buzz"
    else
        print i
    end if
end for
```


## MIPS Assembly

```mw
#################################
# Fizz Buzz                     #
# MIPS Assembly targetings MARS #
# By Keith Stellyes             #
# August 24, 2016               #
#################################

# $a0 left alone for printing
# $a1 stores our counter
# $a2 is 1 if not evenly divisible

.data
	fizz: .asciiz "Fizz\n"
	buzz: .asciiz "Buzz\n"
	fizzbuzz: .asciiz "FizzBuzz\n"
	newline: .asciiz "\n"

.text
loop:
	beq $a1,100,exit
	add $a1,$a1,1
	
	#test for counter mod 15 ("FIZZBUZZ")
	div $a2,$a1,15
	mfhi $a2
	bnez $a2,loop_not_fb #jump past the fizzbuzz print logic if NOT MOD 15
	
#### PRINT FIZZBUZZ: ####
	li $v0,4 #set syscall arg to PRINT_STRING
	la $a0,fizzbuzz #set the PRINT_STRING arg to fizzbuzz
	syscall #call PRINT_STRING
	j loop #return to start
#### END PRINT FIZZBUZZ ####
	
loop_not_fb:	
	div $a2,$a1,3 #divide $a1 (our counter) by 3 and store remainder in HI
	mfhi $a2 #retrieve remainder (result of MOD)
	bnez $a2, loop_not_f #jump past the fizz print logic if NOT MOD 3
	
#### PRINT FIZZ ####
	li $v0,4 
	la $a0,fizz
	syscall
	j loop
#### END PRINT FIZZ ####

loop_not_f:
	div $a2,$a1,5
	mfhi $a2
	bnez $a2,loop_not_b

#### PRINT BUZZ ####
	li $v0,4 
	la $a0,buzz
	syscall
	j loop
#### END PRINT BUZZ ####

loop_not_b:
	#### PRINT THE INTEGER ####
	li $v0,1 #set syscall arg to PRINT_INTEGER
	move $a0,$a1 #set PRINT_INTEGER arg to contents of $a1
	syscall #call PRINT_INTEGER
	
	### PRINT THE NEWLINE CHAR ###
	li $v0,4 #set syscall arg to PRINT_STRING
	la $a0,newline
	syscall
	
	j loop #return to beginning

exit:
	li $v0,10
	syscall
```


## Mirah

```mw
1.upto(100) do |n|
    print "Fizz" if a = ((n % 3) == 0)
    print "Buzz" if b = ((n % 5) == 0) 
    print n unless (a || b)
    print "\n"
end
```

A little more straight forward:

```mw
1.upto(100) do |n|
    if (n % 15) == 0
        puts "FizzBuzz"
    elsif (n % 5) == 0
        puts "Buzz"
    elsif (n % 3) == 0
        puts "Fizz"
    else
        puts n
    end
end
```


## Miranda

```mw
main :: [sys_message]
main = [Stdout (lay (map fizzbuzz [1..100]))]

fizzbuzz :: num->[char]
fizzbuzz n = "FizzBuzz", if n mod 15 = 0
           = "Fizz",     if n mod 3  = 0
           = "Buzz",     if n mod 5  = 0
           = show n,     otherwise
```


## ML

### Standard ML

First using two helper functions, one for deciding what to output and another for performing recursion with an auxiliary argument j.

```mw
local
  fun fbstr i =
      case (i mod 3 = 0, i mod 5 = 0) of
          (true , true ) => "FizzBuzz"
        | (true , false) => "Fizz"
        | (false, true ) => "Buzz"
        | (false, false) => Int.toString i

  fun fizzbuzz' (n, j) =
      if n = j then () else (print (fbstr j ^ "\n"); fizzbuzz' (n, j+1))
in
  fun fizzbuzz n = fizzbuzz' (n, 1)
  val _ = fizzbuzz 100
end
```

Second using the standard-library combinator List.tabulate and a helper function, fb, that calculates and prints the output.

```mw
local
  fun fb i = let val fizz = i mod 3 = 0 andalso (print "Fizz"; true)
                 val buzz = i mod 5 = 0 andalso (print "Buzz"; true)
             in fizz orelse buzz orelse (print (Int.toString i); true) end
in
  fun fizzbuzz n = (List.tabulate (n, fn i => (fb (i+1); print "\n")); ())
  val _ = fizzbuzz 100
end
```

### mLite

```mw
local
	fun fizzbuzz' 
			(x mod 15 = 0) = "FizzBuzz"
		|	(x mod  5 = 0) = "Buzz"
		|	(x mod  3 = 0) = "Fizz"
		|	x = ntos x
in		
	fun fizzbuzz
			([], s) = rev s
		|	(x :: xs, s) = fizzbuzz (xs, fizzbuzz' x :: s)
		|	(x :: xs)    = fizzbuzz (x :: xs, [])
end
;

println ` fizzbuzz ` iota 100;
```


## MMIX

```mw
t   IS $255
Ja  IS $127

       LOC Data_Segment
data   GREG   @

fizz   IS @-Data_Segment
       BYTE "Fizz",0,0,0,0

buzz   IS @-Data_Segment
       BYTE "Buzz",0,0,0,0

nl     IS @-Data_Segment
       BYTE #a,0,0,0,0,0,0,0

buffer IS @-Data_Segment

       LOC #1000
       GREG @

% "usual" print integer subroutine
printnum LOC @
       OR   $1,$0,0
       SETL $2,buffer+64
       ADDU $2,$2,data
       XOR  $3,$3,$3
       STBU $3,$2,1
loop   DIV  $1,$1,10
       GET  $3,rR
       ADDU $3,$3,'0'
       STBU $3,$2,0
       SUBU $2,$2,1
       PBNZ $1,loop
       ADDU t,$2,1
       TRAP 0,Fputs,StdOut
       GO   Ja,Ja,0

Main   SETL $0,1           % i = 1
1H     SETL $2,0           % fizz not taken
       CMP  $1,$0,100      % i <= 100
       BP   $1,4F          % if no, go to end
       DIV  $1,$0,3
       GET  $1,rR          % $1 = mod(i,3)
       CSZ  $2,$1,1        % $2 = Fizz taken?
       BNZ  $1,2F          % $1 != 0? yes, then skip
       ADDU t,data,fizz
       TRAP 0,Fputs,StdOut % print "Fizz"
2H     DIV  $1,$0,5
       GET  $1,rR          % $1 = mod(i,5)
       BNZ  $1,3F          % $1 != 0? yes, then skip
       ADDU t,data,buzz
       TRAP 0,Fputs,StdOut % print "Buzz"
       JMP  5F             % skip print i
3H     BP   $2,5F          % skip if Fizz was taken
       GO   Ja,printnum    % print i
5H     ADDU t,data,nl
       TRAP 0,Fputs,StdOut % print newline
       ADDU $0,$0,1
       JMP  1B             % repeat for next i
4H     XOR  t,t,t
       TRAP 0,Halt,0       % exit(0)
```


## Modula-2

```mw
MODULE Fizzbuzz;
FROM FormatString IMPORT FormatString;
FROM Terminal IMPORT WriteString,WriteLn,ReadChar;

TYPE CB = PROCEDURE(INTEGER);

PROCEDURE Fizz(n : INTEGER);
BEGIN
    IF n MOD 3 = 0 THEN
        WriteString("Fizz");
        Buzz(n,Newline)
    ELSE
        Buzz(n,WriteInt)
    END
END Fizz;

PROCEDURE Buzz(n : INTEGER; f : CB);
BEGIN
    IF n MOD 5 = 0 THEN
        WriteString("Buzz");
        WriteLn
    ELSE
        f(n)
    END
END Buzz;

PROCEDURE WriteInt(n : INTEGER);
VAR buf : ARRAY[0..9] OF CHAR;
BEGIN
    FormatString("%i\n", buf, n);
    WriteString(buf)
END WriteInt;

PROCEDURE Newline(n : INTEGER);
BEGIN
    WriteLn
END Newline;

VAR i : INTEGER;
BEGIN
    FOR i:=1 TO 30 DO
        Fizz(i)
    END;

    ReadChar
END Fizzbuzz.
```


## Modula-3

```mw
MODULE Fizzbuzz EXPORTS Main;

IMPORT IO;

BEGIN
   FOR i := 1 TO 100 DO 
      IF i MOD 15 = 0 THEN 
         IO.Put("FizzBuzz\n");
      ELSIF i MOD 5 = 0 THEN
         IO.Put("Buzz\n");
      ELSIF i MOD 3 = 0 THEN 
         IO.Put("Fizz\n");
      ELSE 
         IO.PutInt(i);
         IO.Put("\n");
      END;
   END;
END Fizzbuzz.
```


## Monte

```mw
def fizzBuzz(top):
    var t := 1
    while (t < top):
        if ((t % 3 == 0) || (t % 5 == 0)):
            if (t % 15 == 0):
                traceln(`$t  FizzBuzz`)
            else if (t % 3 == 0):
                traceln(`$t  Fizz`)
            else:
                traceln(`$t  Buzz`)
        t += 1

fizzBuzz(100)
```


## MontiLang

```mw
&DEFINE LOOP 100&
1 VAR i .

FOR LOOP
    || VAR ln .
    i 5 % 0 == 
    IF : .
        ln |Buzz| + VAR ln .
    ENDIF
    i 3 % 0 ==
    IF : .
        ln |Fizz| + VAR ln .
    ENDIF
    ln || ==
    IF : .
        i PRINT .
    ENDIF
    ln || !=
    IF : .
        ln PRINT .
    ENDIF
i 1 + VAR i .
ENDFOR
```


## Moonli

```mw
loop :for i :from 1 :to 100 :do 
  if (rem(i, 3) == 0) and (rem(i, 5) == 0): write-line("FizzBuzz")
  elif rem(i, 3) == 0: write-line("Fizz")
  elif rem(i, 5) == 0: write-line("Buzz")
  else: format(t, "~D~%", i)
  end if
end loop
# Keyword after end is optional
```


## MoonScript

```mw
for i = 1,100
    print ((a) -> a == "" and i or a) table.concat {
        i % 3 == 0 and "Fizz" or ""
        i % 5 == 0 and "Buzz" or ""}
```


## MUMPS

```mw
FIZZBUZZ
 NEW I
 FOR I=1:1:100 WRITE !,$SELECT(('(I#3)&'(I#5)):"FizzBuzz",'(I#5):"Buzz",'(I#3):"Fizz",1:I)
 KILL I
 QUIT
```

```mw
fizzbuzz
 for i=1:1:100 do  write !
 . write:(i#3)&(i#5) i write:'(i#3) "Fizz" write:'(i#5) "Buzz"
```


## Nanoquery

```mw
for i in range(1, 100)
	if ((i % 3) = 0) and ((i % 5) = 0)
		println "FizzBuzz"
	else if i % 3 = 0
		println "Fizz"
	else if i % 5 = 0
		println "Buzz"
	else
		println i
	end
end
```


## NATURAL

```mw
DEFINE DATA                               
LOCAL                                     
1 #I       (I4)                           
1 #MODULO  (I4)                           
1 #DIVISOR (I4)                           
1 #OUT     (A10)                          
END-DEFINE                                
*                                         
FOR #I := 1 TO 100                        
  #DIVISOR := 15                          
  #OUT := 'FizzBuzz'                      
  PERFORM MODULO                          
*                                         
  #DIVISOR := 5                           
  #OUT := 'Buzz'                          
  PERFORM MODULO                          
*                                         
  #DIVISOR := 3                           
  #OUT := 'Fizz'                          
  PERFORM MODULO                          
*                                         
  WRITE #I                                
END-FOR                                   
*                                         
DEFINE SUBROUTINE MODULO                  
#MODULO := #I - (#I / #DIVISOR) * #DIVISOR
IF #MODULO = 0                            
  WRITE NOTITLE #OUT                      
  ESCAPE TOP                              
END-IF                                    
END-SUBROUTINE                            
*                                         
END
```


## Neko

```mw
var i = 1

while(i < 100) {
	if(i % 15 == 0) {
		$print("FizzBuzz\n");
	} else if(i % 3 == 0) {
		$print("Fizz\n");
	} else if(i % 5 == 0) {
		$print("Buzz\n");
	} else {
		$print(i + "\n");
	}

	i ++= 1
}
```


## Nemerle

The naive approach:

```mw
using System;
using System.Console;

module FizzBuzz
{
    FizzBuzz(x : int) : string
    {
        |x when x % 15 == 0 => "FizzBuzz"
        |x when x %  5 == 0 => "Buzz"
        |x when x %  3 == 0 => "Fizz"
        |_                  => $"$x"
    }
    
    Main() : void
    {
        foreach (i in [1 .. 100])
            WriteLine($"$(FizzBuzz(i))")
    }
}
```

A much slicker approach is posted here
