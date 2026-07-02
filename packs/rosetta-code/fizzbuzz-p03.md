---
title: "FizzBuzz (part 3/7)"
source: https://rosettacode.org/wiki/FizzBuzz
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/7
---

## Eero

```mw
#import <Foundation/Foundation.h>

int main()
  autoreleasepool

    for int i in 1 .. 100
      s := ''
      if i % 3 == 0
        s << 'Fizz'
      if i % 5 == 0
        s << 'Buzz'
      Log( '(%d) %@', i, s )

  return 0
```


## Egel

```mw
import "prelude.eg"
import "io.ego"

using System
using IO

def fizzbuzz =
    [ 100 -> print "100\n"
    | N -> 
        if and ((N%3) == 0) ((N%5) == 0) then 
            let _ = print "fizz buzz, " in fizzbuzz (N+1)
        else if (N%3) == 0 then
            let _ = print "fizz, " in fizzbuzz (N+1)
        else if (N%5) == 0 then
            let _ = print "buzz, " in fizzbuzz (N+1)
        else
            let _ = print N ", " in fizzbuzz (N+1) ]

def main = fizzbuzz 1
```


## Eiffel

```mw
class
	APPLICATION

create
	make

feature

	make
		do
			fizzbuzz
		end

	fizzbuzz
	        --Numbers up to 100, prints "Fizz" instead of multiples of 3, and "Buzz" for multiples of 5.
	        --For multiples of both 3 and 5 prints "FizzBuzz".
		do
			across
				1 |..| 100 as c
			loop
				if c.item \\ 15 = 0 then
					io.put_string ("FIZZBUZZ%N")
				elseif c.item \\ 3 = 0 then
					io.put_string ("FIZZ%N")
				elseif c.item \\ 5 = 0 then
					io.put_string ("BUZZ%N")
				else
					io.put_string (c.item.out + "%N")
				end
			end
		end

end
```


## Ela

```mw
open list

prt x | x % 15 == 0 = "FizzBuzz"
      | x % 3 == 0  = "Fizz"
      | x % 5 == 0  = "Buzz"
      | else        = x

[1..100] |> map prt
```


## Elixir

### Standard approaches

used case

```mw
Enum.each 1..100, fn x ->
  IO.puts(case { rem(x,3) == 0, rem(x,5) == 0 } do
    { true, true }   -> "FizzBuzz"
    { true, false }  -> "Fizz"
    { false, true }  -> "Buzz"
    { false, false } -> x
  end)
end
```

Alternate approach using pipes and cond:

```mw
#!/usr/bin/env elixir
1..100 |> Enum.map(fn i ->
  cond do
    rem(i,3*5) == 0 -> "FizzBuzz"
    rem(i,3) == 0   -> "Fizz"
    rem(i,5) == 0   -> "Buzz"
    true            -> i
  end
end) |> Enum.each(fn i -> IO.puts i end)
```

used Stream.cycle version:

```mw
defmodule RC do
  def fizzbuzz(limit \\ 100) do
    fizz = Stream.cycle(["", "", "Fizz"])
    buzz = Stream.cycle(["", "", "", "", "Buzz"])
    Stream.zip(fizz, buzz)
    |> Enum.take(limit)
    |> Enum.with_index
    |> Enum.each(fn {{f,b},i} ->
         IO.puts if f<>b=="", do: i+1, else: f<>b
       end)
  end
end

RC.fizzbuzz
```

Yet another approach:

```mw
defmodule FizzBuzz do
  def fizzbuzz(n) when rem(n, 15) == 0, do: "FizzBuzz"
  def fizzbuzz(n) when rem(n,  5) == 0, do: "Buzz"
  def fizzbuzz(n) when rem(n,  3) == 0, do: "Fizz"
  def fizzbuzz(n),                      do: n  
end

Enum.each(1..100, &IO.puts FizzBuzz.fizzbuzz &1)
```

used anonymous function

```mw
f = fn(n) when rem(n,15)==0 -> "FizzBuzz"
      (n) when rem(n,5)==0  -> "Fizz"
      (n) when rem(n,3)==0  -> "Buzz"
      (n)                   -> n
end

for n <- 1..100, do: IO.puts f.(n)
```

Enum.at version: Returns nil if index is out of bounds.

```mw
Enum.each(1..100, fn i ->
  str = "#{Enum.at([:Fizz], rem(i,3))}#{Enum.at([:Buzz], rem(i,5))}"
  IO.puts if str=="", do: i, else: str
end)
```

### A macro too far

The Stream.cycle version above, but as an overpowered FizzBuzz DSL.

```mw
defmodule BadFizz do
  # Hand-rolls a bunch of AST before injecting the resulting FizzBuzz code.
  defmacrop automate_fizz(fizzers, n) do
    # To begin, we need to process fizzers to produce the various components
    # we're using in the final assembly. As told by Mickens telling as Antonio
    # Banderas, first you must specify a mapping function:
    build_parts = (fn {fz, n} ->
      ast_ref = {fz |> String.downcase |> String.to_atom, [], __MODULE__}
      clist   = List.duplicate("", n - 1) ++ [fz]
      cycle   = quote do: unquote(ast_ref) = unquote(clist) |> Stream.cycle

      {ast_ref, cycle}
    end)

    # ...and then a reducing function:
    collate = (fn 
      ({ast_ref, cycle}, {ast_refs, cycles}) ->
        {[ast_ref | ast_refs], [cycle | cycles]}
    end)

    # ...and then, my love, when you are done your computation is ready to run
    # across thousands of fizzbuzz:
    {ast_refs, cycles} = fizzers
    |> Code.eval_quoted([], __ENV__) |> elem(0) # Gotta unwrap this mystery code~
    |> Enum.sort(fn ({_, ap}, {_, bp}) -> ap < bp end) # Sort so that Fizz, 3 < Buzz, 5
    |> Enum.map(build_parts) 
    |> Enum.reduce({[], []}, collate)

    # Setup the anonymous functions used by Enum.reduce to build our AST components.
    # This was previously handled by List.foldl, but ejected because reduce/2's
    # default behavior reduces repetition.
    #
    # ...I was tempted to move these into a macro themselves, and thought better of it.
    build_zip    = fn (varname, ast) -> 
      quote do: Stream.zip(unquote(varname), unquote(ast))
    end
    build_tuple  = fn (varname, ast) -> 
      {:{}, [], [varname, ast]} 
    end
    build_concat = fn (varname, ast) ->
        {:<>,
        [context: __MODULE__, import: Kernel], # Hygiene values may change; accurate to Elixir 1.1.1
        [varname, ast]}
    end

    # Toss cycles into a block by hand, then smash ast_refs into
    # a few different computations on the cycle block results.
    cycles = {:__block__, [], cycles}
    tuple  = ast_refs |> Enum.reduce(build_tuple)
    zip    = ast_refs |> Enum.reduce(build_zip)
    concat = ast_refs |> Enum.reduce(build_concat)

    # Finally-- Now that all our components are assembled, we can put
    # together the fizzbuzz stream pipeline. After quote ends, this
    # block is injected into the caller's context.
    quote do
      unquote(cycles)

      unquote(zip)
      |> Stream.with_index
      |> Enum.take(unquote(n))
      |> Enum.each(fn 
      {unquote(tuple), i} ->
        ccats = unquote(concat)
        IO.puts if ccats == "", do: i + 1, else: ccats
      end)
    end
  end

  @doc ~S"""
    A fizzing, and possibly buzzing function. Somehow, you feel like you've
    seen this before. An old friend, suddenly appearing in Kafkaesque nightmare...

    ...or worse, during a whiteboard interview.
  """
  def fizz(n \\ 100) when is_number(n) do
    # In reward for all that effort above, we now have the latest in
    # programmer productivity: 
    #
    # A DSL for building arbitrary fizzing, buzzing, bazzing, and more!
    [{"Fizz", 3}, 
     {"Buzz", 5}#,
     #{"Bar", 7},
     #{"Foo", 243}, # -> Always printed last (largest number)
     #{"Qux", 34}
    ] 
    |> automate_fizz(n)
  end
end

BadFizz.fizz(100) # => Prints to stdout
```


## Elm

A bit too simple:

```mw
import Html exposing (text)
import List exposing (map)

main =
  [1..100] |> map getWordForNum |> text

getWordForNum num =
  if num % 15 == 0 then
    "FizzBuzz"
  else if num % 3 == 0 then
    "Fizz"
  else if num % 5 == 0 then
    "Buzz"
  else
    String.fromInt num
```

A bit too clever:

```mw
import Html exposing (text)
import List exposing (map)
import String exposing (join, fromInt)

main : Html.Html
main =
  [1..100] |> map fizzbuzz |> join " " |> text

fizzbuzz : Int -> String
fizzbuzz num =
  let
    fizz = if num % 3 == 0 then "Fizz" else ""
    buzz = if num % 5 == 0 then "Buzz" else ""
  in
    if fizz == buzz then
      fromInt num
    else
      fizz ++ buzz
```


## Emacs Lisp

```mw
(defun fizzbuzz (n) 
  (cond ((and (zerop (% n 5)) (zerop (% n 3))) "FizzBuzz") 
	((zerop (% n 3)) "Fizz") 
	((zerop (% n 5)) "Buzz") 
	(t n)))

;; loop & print from 0 to 100
(dotimes (i 101)
  (message "%s" (fizzbuzz i)))
```


## EMal

```mw
logic isFizz, isBuzz
for int count ← 1; count ≤ 100; ++count
  isFizz ← count % 3 æ 0
  isBuzz ← count % 5 æ 0
  if isFizz and isBuzz do writeLine("Fizz Buzz")
  else if isFizz do writeLine("Fizz")
  else if isBuzz do writeLine("Buzz")
  else do writeLine(count)
  end
end
```


## Emojicode

### Simple 1

```mw
🏁🍇
  🔂 i 🆕⏩ 1 101 1 ❗ 🍇
    ↪️ i 🚮 15 🙌 0 🍇
      😀 🔤FizzBuzz🔤 ❗
    🍉
    🙅↪️ i 🚮 3 🙌 0 🍇
      😀 🔤Fizz🔤 ❗
    🍉
    🙅↪️ i 🚮 5 🙌 0 🍇
      😀 🔤Buzz🔤 ❗
    🍉🙅🍇
      😀 🔤🧲i🧲🔤 ❗
    🍉
  🍉
🍉
```

### Simple 2

```mw
🏁🍇
  🔂 i 🆕⏩ 1 101 1 ❗ 🍇
    🔤🔤 ➡️ 🖍🆕 msg
    ↪️ i 🚮 3 🙌 0 🍇
      🔤Fizz🔤 ➡️ 🖍 msg
    🍉
    ↪️ i 🚮 5 🙌 0 🍇
      🔤🧲msg🧲Buzz🔤 ➡️ 🖍 msg
    🍉
    ↪️ msg 🙌 🔤🔤 🍇
      😀 🔤🧲i🧲🔤 ❗
    🍉🙅🍇
      😀 🔤🧲msg🧲🔤 ❗
    🍉
  🍉
🍉
```


## Enguage

```mw
FizzBuzz
```

This source code is supposed to look like plain old English but is, in fact, executable. When used in an Android app, it gives the user direct access to computational abilities of your phone.

It is taken from the dictionary entry for fizzbuzz

This shows the interpretation of two utterances, the latter of which are called recursively. Enguage is not very efficient, but that's not its goal!

NB. Any line beginning with a '#' is a comment, like Unix shells, but any comment following the ']' character are unit tests exercising this code.

```
On "what is the fizzbuzz of N":
	is N divisible by 5 and 3;
	if so, reply "fizzbuzz";
	
	is N divisible by 5;
	if so, reply "buzz";
	
	is N divisible by 3;
	if so, reply "fizz";
	
	reply "N".
	
On "do fizzbuzz between N and LIMIT":
	what is the fizzbuzz of N;
	remember this;
	set next to the	evaluation of N + 1;
	NEXT is equal to LIMIT;
	if so, what is the fizzbuzz of LIMIT;
	if not, do fizzbuzz between NEXT and LIMIT.
	
#] what is the fizzbuzz of  1: 1.
#] what is the fizzbuzz of 12: fizz.
#] what is the fizzbuzz of 25: buzz.
#] what is the fizzbuzz of 75: fizzbuzz.

#] set limit to 5.
#] do fizzbuzz between 1 and LIMIT.
```

On downloading this repo, if git and make are installed, this unit test can be run with:

```
    $ git clone https://github.com/martinwheatman/enguage.git
    $ cd enguage
    $ make jar
    $ export PATH=$PATH:./sbin
    $ java -jar lib/enguage.jar -T fizzbuzz
```

Output:

```
TEST: fizzbuzz
==============

user> what is the fizzbuzz of  1.
enguage> 1.

user> what is the fizzbuzz of 12.
enguage> fizz.

user> what is the fizzbuzz of 25.
enguage> buzz.

user> what is the fizzbuzz of 75.
enguage> fizzbuzz.

user> set limit to 5.
enguage> ok , limit is set to 5.

user> do fizzbuzz between 1 and LIMIT.
enguage> 1 . 2 . fizz . 4 . buzz.
1 test group(s) found
+++ PASSED 6 tests in 442ms +++
```


## Erlang

### Nice

```mw
-spec fizzbuzz() -> Result :: string().
fizzbuzz() ->
    F = fun(N) when N rem 15 == 0 -> "FizzBuzz";
           (N) when N rem 3 == 0  -> "Fizz";
           (N) when N rem 5 == 0  -> "Buzz";
           (N) -> integer_to_list(N)
        end,
    lists:flatten([[F(N)] ++ ["\n"] || N <- lists:seq(1,100)]).
```

### Unnecessarily Concurrent

```mw
-module(fizzbuzz).
-export([start/1, count/2, display/0]).

fizzbuzz(N) when N rem 15 == 0 -> fizzbuzz;
fizzbuzz(N) when N rem 5  == 0 -> buzz;
fizzbuzz(N) when N rem 3  == 0 -> fizz;
fizzbuzz(N) -> N.

count(N, Limit) when N==Limit ->
    display ! fizzbuzz(N),
    display ! finished;
count(N, Limit) when N<Limit ->
    display ! fizzbuzz(N),
    count(N+1, Limit).

display() ->
    receive
        finished -> io:format("end!\n");
        fizzbuzz -> io:format("FizzBuzz!\n"), display();
        buzz     -> io:format("Buzz!\n"), display();
        fizz     -> io:format("Fizz!\n"), display();
        N        -> io:format("~p\n", [N]), display()
    end.

start(Max) ->
    register(display, spawn(fizzbuzz, display, [])),
    count(1, Max).
```


## ERRE

```mw
PROGRAM FIZZ_BUZZ
!
! for rosettacode.org
!
BEGIN
 FOR A=1 TO 100 DO
   IF A MOD 15=0 THEN
      PRINT("FizzBuzz")
   ELSIF A MOD 3=0 THEN
      PRINT("Fizz")
   ELSIF A MOD 5=0 THEN
      PRINT("Buzz")
   ELSE
      PRINT(A)
   END IF
 END FOR
END PROGRAM
```


## Euler

The original Euler implementations did not allow "long" strings, hence the use of a list here to print FizzBuzz.

```
begin  new i; label iLoop;
       i <- 0;
iLoop: if [ i <- i + 1 ] <= 100 then begin
          out if      i mod 15 = 0 then ( "Fizz", "Buzz" )
              else if i mod  5 = 0 then "Buzz"
              else if i mod  3 = 0 then "Fizz"
              else i;
          goto iLoop
       end else 0
end $
```


## Euphoria

Works with

:

Euphoria

version 4.0.0

This is based on the VBScript example.

```mw
include std/utils.e

function fb( atom n )
	sequence fb
	if remainder( n, 15 ) = 0 then
		fb = "FizzBuzz"
	elsif remainder( n, 5 ) = 0 then
		fb = "Fizz"
	elsif remainder( n, 3 ) = 0 then
		fb = "Buzz"
	else
		fb = sprintf( "%d", n )
	end if
	return fb
end function
 
function fb2( atom n )
	return iif( remainder(n, 15) = 0, "FizzBuzz", 
		iif( remainder( n, 5 ) = 0, "Fizz", 
		iif( remainder( n, 3) = 0, "Buzz", sprintf( "%d", n ) ) ) ) 
end function

for i = 1 to 30 do
	printf( 1, "%s ", { fb( i ) } )
end for

puts( 1, "\n" )

for i = 1 to 30 do
	printf( 1, "%s ", { fb2( i ) } )
end for

puts( 1, "\n" )
```


## Excel

```mw
=LET(
  i, SEQUENCE(100),
  isDivBy3, MOD(i, 3) = 0,
  isDivBy5, MOD(i, 5) = 0,
  IFS(
    isDivBy3 * isDivBy5, "FizzBuzz",
    isDivBy3, "Fizz",
    isDivBy5, "Buzz",
    TRUE, i
  )
 )
```


## F

```mw
let fizzbuzz n =
    match n%3 = 0, n%5 = 0 with
    | true, false -> "fizz"
    | false, true -> "buzz"
    | true, true  -> "fizzbuzz"
    | _ -> string n

let printFizzbuzz() =
    [1..100] |> List.iter (fizzbuzz >> printfn "%s")
```

```mw
[1..100] 
|> List.map (fun x ->
            match x with 
            | _ when x % 15 = 0 ->"fizzbuzz"
            | _ when x % 5 = 0 -> "buzz"
            | _ when x % 3 = 0 -> "fizz"
            | _ ->  x.ToString())
|> List.iter (fun x -> printfn "%s" x)
```

Another example using (unnecessary) partial active pattern :D

```mw
let (|MultipleOf|_|) divisors number =
    if Seq.exists ((%) number >> (<>) 0) divisors
    then None
    else Some ()

let fizzbuzz = function
| MultipleOf [3; 5] -> "fizzbuzz"
| MultipleOf [3]    -> "fizz"
| MultipleOf [5]    -> "buzz"
| n                 -> string n

{ 1 .. 100 }
|> Seq.iter (fizzbuzz >> printfn "%s")
```


## Factor

We get a terse, elegant solution by exploiting that `true x and` returns `x` and that the boolean `f` is also an empty sequence; this allows us to `and` together the boolean result of `mod 0 =` with each of "Fizz" or "Buzz", then concatenate those results to get either "Fizz", "Buzz", or "FizzBuzz".

```mw
USE: math.parser
100 [1..b] [ { "Fizz" "Buzz" } { 3 5 } [ overd mod 0 = swap and ] 2map concat swap >dec or print ] each
```

I wrote this solution to demonstrate that defining helper words is not necessary. Factor's shuffle words, combinators, and object system alone give readable, terse solutions that generalize & refactor easily. I write most of my real-world production code like this. Alternative solutions follow.

```mw
USING: math kernel io math.functions math.parser math.ranges ;
IN: fizzbuzz
: fizz ( n -- str ) 3 divisor? "Fizz" "" ? ;
: buzz ( n -- str ) 5 divisor? "Buzz" "" ? ;
: fizzbuzz ( n -- str ) dup [ fizz ] [ buzz ] bi append [ number>string ] [ nip ] if-empty ;
: main ( -- ) 100 [1,b] [ fizzbuzz print ] each ;
MAIN: main
```

More flexible variant without divisibility tests.

```mw
USING: kernel sequences arrays generalizations fry math math.parser prettyprint ;
IN: fizzbuzz

: zz ( m seq -- v ) dup length 1 <array> V{ } clone 4 -nrot 1 4 -nrot 3 nrot
 '[ dup _ <= ]
  3 -nrot
 '[
    "" _ [ _ [ swap execute( str n -- str n ) ] change-nth ] each-index
    dup empty? [ drop dup number>string ] [ ] if swapd suffix! swap 1 +
  ]
  while drop ;

: fizz ( str n -- str n ) dup 3 < [ 1 + ] [ drop "Fizz" append 1 ] if ;
: buzz ( str n -- str n ) dup 5 < [ 1 + ] [ drop "Buzz" append 1 ] if ;
: quxx ( str n -- str n ) dup 7 < [ 1 + ] [ drop "Quxx" append 1 ] if ;
: FizzBuzzQuxx ( m -- v ) { fizz buzz quxx } zz ;
: FizzBuzzQuxx-100 ( -- ) 100 FizzBuzzQuxx . ;

MAIN: FizzBuzzQuxx-100
```

Another approach is leverage Factor's predicate and intersection classes.

```mw
USING: io kernel math math.functions math.parser ranges
sequences ;
IN: rosetta-code.fizz-buzz

PREDICATE: fizz < integer 3 divisor? ;
PREDICATE: buzz < integer 5 divisor? ;

INTERSECTION: fizzbuzz fizz buzz ;

GENERIC: fizzbuzz>string ( n -- str )

M: fizz fizzbuzz>string 
    drop "Fizz" ;

M: buzz fizzbuzz>string
    drop "Buzz" ;

M: fizzbuzz fizzbuzz>string 
    drop "FizzBuzz" ;

M: integer fizzbuzz>string
    number>string ;

MAIN: [ 1 100 [a..b] [ fizzbuzz>string print ] each ]
```


## Falcon

```mw
for i in [1:101]
    switch i % 15
    case 0        : > "FizzBuzz"
    case 5,10     : > "Buzz"
    case 3,6,9,12 : > "Fizz"
    default       : > i
    end
end
```


## FALSE

See FizzBuzz/EsoLang


## Fantom

```mw
class FizzBuzz
{
  public static Void main ()
  {
    for (Int i:=1; i <= 100; ++i)
    {
      if (i % 15 == 0)
        echo ("FizzBuzz")
      else if (i % 3 == 0)
        echo ("Fizz")
      else if (i % 5 == 0) 
        echo ("Buzz") 
      else
        echo (i)
    }
  }
}
```


## FBSL

**No 'MOD 15' needed.**

```mw
#APPTYPE CONSOLE

DIM numbers AS STRING
DIM imod5 AS INTEGER
DIM imod3 AS INTEGER

FOR DIM i = 1 TO 100
    numbers = ""
    imod3 = i MOD 3
    imod5 = i MOD 5
    IF NOT imod3 THEN numbers = "Fizz"
    IF NOT imod5 THEN numbers = numbers & "Buzz"
    IF imod3 AND imod5 THEN numbers = i
    PRINT numbers, " ";
NEXT

PAUSE
```

**Output:**

```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fiz
z 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz
 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 Fi
zzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz
 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97
98 Fizz Buzz
Press any key to continue...
```


## Fe

There is no built-in *mod* function, but you can add it via the C API.

```mw
static fe_Object *mod(fe_Context *ctx, fe_Object *args) {
  fe_Number n = fe_tonumber(ctx, fe_nextarg(ctx, &args));
  return fe_number(ctx, fmod(n, fe_tonumber(ctx, fe_nextarg(ctx, &args))));
}
```

Then, you can solve 'FizzBuzz' the traditional way:

```mw
(= i 0)
(while (< i 100)
  (= i (+ i 1))
  (print
    (if (is (mod i 15) 0) "FizzBuzz"
        (is (mod i  3) 0) "Fizz"
        (is (mod i  5) 0) "Buzz"
        i)))
```

Of course, you can solve this without *mod*:

```mw
(= i 0)
(= fizz 0)
(= buzz 0)
(= fizzbuzz 0)

(while (< i 100)
  (= i (+ i 1))
  (= fizz (+ fizz 1))
  (= buzz (+ buzz 1))
  (= fizzbuzz (+ fizzbuzz 1))
  ; check and reset counters
  (print
    (if (is fizzbuzz 15) (do (= fizzbuzz 0) (= fizz 0) (= buzz 0) "fizzbuzz")
        (is fizz 3) (do (= fizz 0) "fizz")
        (is buzz 5) (do (= buzz 0) "buzz")
        i)))
```


## Fennel

```mw
(for [i 1 100]
  (print (if (= (% i 15) 0) :FizzBuzz
             (= (% i 3) 0) :Fizz
             (= (% i 5) 0) :Buzz
             i)))
```

Use pattern matching and recursive function:

```mw
(fn fizz-buzz [from to]
  (print (match [(% from 3) (% from 5)]
           [0 0] :FizzBuzz
           [0 _] :Fizz
           [_ 0] :Buzz
           _     from))
  (when (< from to)
    (fizz-buzz (+ from 1) to)))

(fizz-buzz 1 100)
```

Alternative matching pattern:

Translation of

:

D

```mw
(for [i 1 100]
  (print (match (% i 15)
           0                     :FizzBuzz
           (where (or 3 6 9 12)) :Fizz
           (where (or 5 10)      :Buzz
           _                      i)))
```


## FOCAL

FITR is a built-in function that truncates a floating-point number to an integer. Note that FOCAL uses an arithmetic (three-way) IF statement, rather like early Fortran.

```mw
01.10 FOR I=1,100; DO 2.0
01.20 QUIT

02.10 SET ZB=I/15 - FITR(I/15)
02.20 IF (ZB) 2.4, 2.3, 2.4
02.30 TYPE "FizzBuzz" !
02.35 RETURN
02.40 SET Z=I/3 - FITR(I/3)
02.50 IF (Z) 2.7, 2.6, 2.7
02.60 TYPE "Fizz" !
02.65 RETURN
02.70 SET B=I/5 - FITR(I/5)
02.80 IF (B) 2.99, 2.9, 2.99
02.90 TYPE "Buzz" !
02.95 RETURN
02.99 TYPE %3, I, !
```


## Fermat

```mw
for i = 1 to 100 do if i|15=0 then !'FizzBuzz ' else if i|5=0 then !'Buzz ' else if i|3=0 then !'Fizz ' else !i;!' ' fi fi fi od
```

**Output:**

```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```


## Fish

See FizzBuzz/EsoLang#Fish


## Forth

### table-driven

```mw
: fizz ( n -- ) drop ." Fizz" ;
: buzz ( n -- ) drop ." Buzz" ;
: fb   ( n -- ) drop ." FizzBuzz" ;
: vector create does> ( n -- )
  over 15 mod cells + @ execute ;
vector .fizzbuzz
  ' fb   , ' . ,    ' . ,
  ' fizz , ' . ,    ' buzz ,
  ' fizz , ' . ,    ' . ,
  ' fizz , ' buzz , ' . ,
  ' fizz , ' . ,    ' . ,
```

### or the classic approach

```mw
: .fizzbuzz ( n -- )
  0 pad c!
  dup 3 mod 0= if s" Fizz" pad  place then
  dup 5 mod 0= if s" Buzz" pad +place then
  pad c@ if drop pad count type else . then ;

: zz ( n -- )
  1+ 1 do i .fizzbuzz cr loop ;
100 zz
```

### the well factored approach

SYNONYM is a Forth200x word.

```mw
SYNONYM NOT INVERT \ Bitwise boolean not

: Fizz?  ( n -- ? )  3 MOD 0=  DUP IF ." Fizz" THEN ;
: Buzz?  ( n -- ? )  5 MOD 0=  DUP IF ." Buzz" THEN ;
: ?print  ( n ? -- )  IF . THEN ;
: FizzBuzz  ( -- )
   101 1 DO CR  I  DUP Fizz? OVER Buzz? OR  NOT ?print  LOOP ;

FizzBuzz
```

### the unrolled approach

```mw
: n     ( n -- n+1 )    dup .         1+ ;
: f     ( n -- n+1 )    ." Fizz "     1+ ;
: b     ( n -- n+1 )    ." Buzz "     1+ ;
: fb    ( n -- n+1 )    ." FizzBuzz " 1+ ;
: fb10  ( n -- n+10 )   n n f n b f n n f b ;
: fb15  ( n -- n+15 )   fb10 n f n n fb ;
: fb100 ( n -- n+100 )  fb15 fb15 fb15 fb15 fb15 fb15 fb10 ;
: .fizzbuzz ( -- )      1 fb100 drop ;
```

### manipulating return stack

```mw
: | >r >r dup r> mod 0= if r> count type drop then r> drop ;
: fizzbuzz1 15 c" FizzBuzz " | 3 c" Fizz " | 5 c" Buzz " | . ;
: fizzbuzz 101 1 do i fizzbuzz1 loop ;
fizzbuzz
```


## Fortran

In ANSI FORTRAN 77 or later use structured IF-THEN-ELSE (example uses some ISO Fortran 90 features):

```mw
program fizzbuzz_if
   integer :: i
   
   do i = 1, 100
      if     (mod(i,15) == 0) then; print *, 'FizzBuzz'
      else if (mod(i,3) == 0) then; print *, 'Fizz'
      else if (mod(i,5) == 0) then; print *, 'Buzz'
      else;                         print *, i
      end if
   end do
end program fizzbuzz_if
```

This example uses If statements to print "Fizz" and "Buzz" next to each other if the number is divisible by 3 and 5 by waiting to use a line break until after the If statements.

```mw
program FizzBuzz
implicit none
integer :: i = 1

do i = 1, 100
    if (Mod(i,3) == 0)write(*,"(A)",advance='no')  "Fizz"
    if (Mod(i,5) == 0)write(*,"(A)",advance='no') "Buzz"
    if (Mod(i,3) /= 0 .and. Mod(i,5) /=0 )write(*,"(I3)",advance='no') i
    print *, ""
end do
end program FizzBuzz
```

In ISO Fortran 90 or later use SELECT-CASE statement:

```mw
program fizzbuzz_select
    integer :: i
    
    do i = 1, 100
       select case (mod(i,15))
          case 0;        print *, 'FizzBuzz'
          case 3,6,9,12; print *, 'Fizz'
          case 5,10;     print *, 'Buzz'
          case default;  print *, i
       end select
    end do
 end program fizzbuzz_select
```


## FreeBASIC

See FizzBuzz/Basic


## Frege

```mw
gen n word = cycle (take (n - 1) (repeat "") ++ [word])
pattern = zipWith (++) (gen 3 "fizz") (gen 5 "buzz")
fizzbuzz = zipWith combine pattern [1..] where
    combine word number = if null word
                             then show number
                             else word
show $ take 100 fizzbuzz
```


## Frink

```mw
for i = 1 to 100
{
   flag = false
   if i mod 3 == 0
   {
      flag = true
      print["Fizz"]
   }
   
   if i mod 5 == 0
   {
      flag = true
      print["Buzz"]
   }

   if flag == false
      print[i]

   println[]
}
```


## FutureBasic

```mw
include "NSLog.incl"

long fizz, buzz, i

for i = 1 to 100
  fizz = (i mod 3 )
  buzz = (i mod 5 )
  if fizz + buzz == 0 then NSLog(@"FizzBuzz") : continue
  if fizz == 0 then NSLog(@"Fizz") : continue
  if buzz == 0 then NSLog(@"Buzz") : continue
  NSLog(@"%ld",i)
next i

HandleEvents
```

Output:

```
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
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
```


## Fōrmulæ

Fōrmulæ programs are not textual, visualization/edition of programs is done showing/manipulating structures but not text. Moreover, there can be multiple visual representations of the same program. Even though it is possible to have textual representation —i.e. XML, JSON— they are intended for storage and transfer purposes more than visualization and edition.

Programs in Fōrmulæ are created/edited online in its website.

In **this page** you can see and run the program(s) related to this task and their results. You can also change either the programs or the parameters they are called with, for experimentation, but remember that these programs were created with the main purpose of showing a clear solution of the task, and they generally lack any kind of validation.

**Solution**


## Gambas

**Click this link to run this code**

```mw
Public Sub Main()
Dim siCount As Short
Dim sText As String

For siCount = 1 To 100
  sText = ""
  If siCount Mod 3 = 0 Then sText = "Fizz"
  If siCount Mod 5 = 0 Then sText = "Buzz"
  If siCount Mod 15 = 0 Then sText = "FizzBuzz"
  If sText Then Print sText Else Print siCount
Next

End
```

Output:

```
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
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
```


## GAP

```mw
FizzBuzz := function()
	local i;
	for i in [1 .. 100] do
		if RemInt(i, 15) = 0 then
			Print("FizzBuzz\n");
		elif RemInt(i, 3) = 0 then
			Print("Fizz\n");
		elif RemInt(i, 5) = 0 then
			Print("Buzz\n");
		else
			Print(i, "\n");
		fi;
	od;
end;
```


## GDScript

```mw
extends Node

func _ready():
	for i in range(1, 101):
		if i % 15 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

	get_tree().quit()
```


## Genyris

```mw
@prefix u "http://www.genyris.org/lang/utilities#"

def fizzbuzz (n)
    map-left ^((3 = 'fizz') (5 = 'buzz'))
        lambda (d)
            cond
                (equal? 0 (% n d!left))
                    d!right
                else
                    ''
                        

for n in (range 1 100)
    define fb (''(.join (fizzbuzz n)))
    u:format "%a\n"
        cond 
            (equal? fb '') 
                n
            else
                fb
```


## GFA Basic

```mw
' Fizz Buzz
'
FOR i%=1 TO 100
  IF i% MOD 15=0
    PRINT "FizzBuzz"
  ELSE IF i% MOD 3=0
    PRINT "Fizz"
  ELSE IF i% MOD 5=0
    PRINT "Buzz"
  ELSE
    PRINT i%
  ENDIF
NEXT i%
```


## Gleam

```mw
import gleam/int
import gleam/io
import gleam/list

pub fn main() {
  int.range(100, 0, [], list.prepend)
  |> list.map(fizz_buzz)
  |> list.each(io.println)
}

pub fn fizz_buzz(i) {
  case i % 3, i % 5 {
    0, 0 -> "FizzBuzz"
    0, _ -> "Fizz"
    _, 0 -> "Buzz"
    _, _ -> int.to_string(i)
  }
}
```


## Go

### switch/case approach

```mw
package main

import "fmt"

func main() {
    for i := 1; i <= 100; i++ {
        switch {
        case i%15==0:
            fmt.Println("FizzBuzz")
        case i%3==0:
            fmt.Println("Fizz")
        case i%5==0:
            fmt.Println("Buzz")
        default: 
            fmt.Println(i)
        }
    }
}
```

### map approach

```mw
package main

import "fmt"

func main() {
    for i := 1; i <= 100; i++ {
        fmt.Println(map[bool]map[bool]interface{}{
            false: {false: i, true: "Fizz"}, true: {false: "Buzz", true: "FizzBuzz"},
        }[i%5 == 0][i%3 == 0])
    }
}
```


## Golfscript

```mw
100,{)6,{.(&},{1$1$%{;}{4*35+6875*25base{90\-}%}if}%\or}%n*
```


## Golo

```mw
module FizzBuzz

augment java.lang.Integer {
	function getFizzAndOrBuzz = |this| -> match {
		when this % 15 == 0 then "FizzBuzz"
		when this % 3 == 0 then "Fizz"
		when this % 5 == 0 then "Buzz"
		otherwise this
	}
}

function main = |args| {
  foreach i in [1..101] {
	println(i: getFizzAndOrBuzz())
  }
}
```


## Gosu

```mw
for (i in 1..100) {
    
    if (i % 3 == 0 && i % 5 == 0) {
        print("FizzBuzz")
        continue
    }
    
    if (i % 3 == 0) {
        print("Fizz")
        continue
    }
    
    if (i % 5 == 0) {
        print("Buzz")
        continue
    }
    
    // default
    print(i)
    
}
```

One liner version (I added new lines to better readability but when you omit them it's one liner):

```mw
// note that compiler reports error (I don't know why) but still it's working
for (i in 1..100) { 
    print(i % 5 == 0 ? i % 3 == 0 ? "FizzBuzz" : "Buzz" : i % 3 == 0 ? "Fizz" : i)
}
```


## Groovy

```mw
1.upto(100) { i -> println "${i % 3 ? '' : 'Fizz'}${i % 5 ? '' : 'Buzz'}" ?: i }
```


## GW-BASIC

See FizzBuzz/Basic


## Hare

```mw
use fmt;

export fn main() void = {
	for (let i = 1z; i <= 100; i += 1) {
		fmt::println(
			if (i % 15 == 0) "FizzBuzz"
			else if (i % 3 == 0) "Fizz"
			else if (i % 5 == 0) "Buzz"
			else i
		)!;
	};
};
```


## Haskell

Variant directly implementing the specification:

```mw
fizzbuzz :: Int -> String
fizzbuzz x
  | f 15 = "FizzBuzz"
  | f 3 = "Fizz"
  | f 5 = "Buzz"
  | otherwise = show x
  where
    f = (0 ==) . rem x

main :: IO ()
main = mapM_ (putStrLn . fizzbuzz) [1 .. 100]
```

```mw
fizzbuzz :: Int -> String
fizzbuzz n =
  '\n' :
  if null (fizz ++ buzz)
    then show n
    else fizz ++ buzz
  where
    fizz =
      if mod n 3 == 0
        then "Fizz"
        else ""
    buzz =
      if mod n 5 == 0
        then "Buzz"
        else ""

main :: IO ()
main = putStr $ concatMap fizzbuzz [1 .. 100]
```

Does not perform the mod 15 step, extesible to arbitrary addtional tests, ex: [bar| n `mod` 7 == 0].

```mw
main = mapM_ (putStrLn . fizzbuzz) [1..100]

fizzbuzz n = 
    show n <|> [fizz| n `mod` 3 == 0] ++ 
               [buzz| n `mod` 5 == 0]

-- A simple default choice operator. 
-- Defaults if both fizz and buzz fail, concats if any succeed.
infixr 0 <|>
d <|> [] = d
_ <|> x = concat x

fizz = "Fizz"
buzz = "Buzz"
```

Alternate implementation using lazy infinite lists and avoiding use of "mod":

```mw
main = mapM_ putStrLn $ take 100 $ zipWith show_number_or_fizzbuzz [1..] fizz_buzz_list           

show_number_or_fizzbuzz x y = if null y then show x else y

fizz_buzz_list = zipWith (++) (cycle ["","","Fizz"]) (cycle ["","","","","Buzz"])
```

Or in terms (still without **mod** or **rem**) of an applicative **ZipList**:

```mw
import Control.Applicative ( ZipList(ZipList, getZipList) )

fizzBuzz :: [String]
fizzBuzz =
  getZipList $ go <$> 
    ZipList (cycle $ replicate 2 [] <> ["fizz"]) <*>
    ZipList (cycle $ replicate 4 [] <> ["buzz"]) <*>
    ZipList (show <$> [1 ..])

go :: String -> String -> String -> String
go f b n
  | null f && null b = n
  | otherwise = f <> b

main :: IO ()
main = mapM_ putStrLn $ take 100 fizzBuzz
```

or using an applicative test:

```mw
import Data.Bool (bool)

fizzBuzz :: [String]
fizzBuzz =
  let fb n k = cycle $ replicate (pred n) [] <> [k]
   in zipWith
        (flip . bool <*> null)
        (zipWith (<>) (fb 3 "fizz") (fb 5 "buzz"))
        (show <$> [1 ..])

main :: IO ()
main = mapM_ putStrLn $ take 100 fizzBuzz
```

Using heavy artillery (needs the mtl package):

```mw
import Control.Monad.State
import Control.Monad.Trans
import Control.Monad.Writer

main = putStr $ execWriter $ mapM_ (flip execStateT True . fizzbuzz) [1..100]

fizzbuzz :: Int -> StateT Bool (Writer String) ()
fizzbuzz x = do
 when (x `mod` 3 == 0) $ tell "Fizz" >> put False
 when (x `mod` 5 == 0) $ tell "Buzz" >> put False
 get >>= (flip when $ tell $ show x)
 tell "\n"
```

Using guards plus where.

```mw
fizzBuzz :: (Integral a) => a -> String
fizzBuzz i
  | fizz && buzz = "FizzBuzz"
  | fizz         = "Fizz"
  | buzz         = "Buzz"
  | otherwise    = show i
  where fizz = i `mod` 3 == 0
        buzz = i `mod` 5 == 0

main = mapM_ (putStrLn . fizzBuzz) [1..100]
```

An elegant solution exploiting monoidal and applicative properties of functions:

```mw
import Data.Monoid

fizzbuzz = max
       <$> show
       <*> "fizz" `when` divisibleBy 3
       <>  "buzz" `when` divisibleBy 5
       <>  "quxx" `when` divisibleBy 7
  where
    when m p x = if p x then m else mempty
    divisibleBy n x = x `mod` n == 0

main = mapM_ (putStrLn . fizzbuzz) [1..100]
```

And pattern matching approach:

```mw
fizzbuzz n = case (rem n 3, rem n 5) of
               (0, 0) -> "FizzBuzz"
               (0, _) -> "Fizz"
               (_, 0) -> "Buzz"
               (_, _) -> show n

main = mapM_ (putStrLn . fizzbuzz) [1..100]
```

Generalised solution:

```mw
wordthing :: [(Int, String)] -> Int -> String
wordthing lst n =
  if matches == [] then
    show n
  else
    concat $ map snd matches
  where matches = filter (\x -> n `mod` (fst x) == 0) lst

fizzbuzz :: Int -> String
fizzbuzz = wordthing [(3, "Fizz"), (5, "Buzz")]

main = do
  mapM_ (putStrLn . fizzbuzz) [1..100]
```


## hexiscript

```mw
for let i 1; i <= 100; i++
  if   i % 3 = 0 && i % 5 = 0; println "FizzBuzz"
  elif i % 3 = 0; println "Fizz"
  elif i % 5 = 0; println "Buzz"
  else println i; endif
endfor
```


## HicEst

```mw
DO i = 1, 100
  IF(     MOD(i, 15) == 0 ) THEN
    WRITE() "FizzBuzz"
  ELSEIF( MOD(i, 5) == 0 ) THEN
    WRITE() "Buzz"
  ELSEIF( MOD(i, 3) == 0 ) THEN
    WRITE() "Fizz"
  ELSE
    WRITE() i
  ENDIF
ENDDO
```

Alternatively:

```mw
CHARACTER string*8

DO i = 1, 100
  string = " "
  IF( MOD(i, 3) == 0 ) string = "Fizz"
  IF( MOD(i, 5) == 0 ) string = TRIM(string) // "Buzz"
  IF( string == " ") WRITE(Text=string) i
  WRITE() string
ENDDO
```


## Hobbes

Using a list comprehension with conditional expressions:

```mw
[putStrLn(if (n%15==0) then "FizzBuzz"
          else if (n%3==0) then "Fizz"
          else if (n%5==0) then "Buzz"
          else show(n))
 | n <- [1..100]]
```

Alternatively, using pattern matching on a tuple (in a `.hob` file):

```mw
fizzbuzz :: int -> [char]
fizzbuzz n =
  match (n % 3, n % 5) with
  | (0, 0) -> "FizzBuzz"
  | (0, _) -> "Fizz"
  | (_, 0) -> "Buzz"
  | _      -> show(n)

// Usage: [putStrLn(fizzbuzz(n)) | n <- [1..100]]
```


## HolyC

```mw
U8 i;
for (i = 1; i <= 100; i++) {
  if (!(i % 15))
    Print("FizzBuzz");
  else if (!(i % 3))
    Print("Fizz");
  else if (!(i % 5))
    Print("Buzz");
  else
    Print("%d", i);
  Print("\n");
}
```


## Hoon

```mw
:-  %say
|=  [^ ~ ~]
  :-  %noun
  %+  turn   (gulf [1 101])
  |=  a=@
    =+  q=[=(0 (mod a 3)) =(0 (mod a 5))]
    ?+  q  <a>
      [& &]  "FizzBuzz"
      [& |]  "Fizz"
      [| &]  "Buzz"
    ==
```


## Huginn

```mw
import Algorithms as algo;

main( argv_ ) {
	if ( size( argv_ ) < 2 ) {
		throw Exception( "usage: fizzbuzz {NUM}" );
	}
	top = integer( argv_[1] );
	for ( i : algo.range( 1, top + 1 ) ) {
		by3 = ( i % 3 ) == 0;
		by5 = ( i % 5 ) == 0;
		if ( by3 ) {
			print( "fizz" );
		}
		if ( by5 ) {
			print( "buzz" );
		}
		if ( ! ( by3 || by5 ) ) {
			print( i );
		}
		print( "\n" );
	}
	return ( 0 );
}
```


## Hy

```mw
(for [i (range 1 101)] (print (cond
  [(not (% i 15)) "FizzBuzz"]
  [(not (% i  5)) "Buzz"]
  [(not (% i  3)) "Fizz"]
  [True           i])))
```


## i

```mw
software {
	for each 1 to 100		
		if i % 15 = 0
			print("FizzBuzz")
		else if i % 3 = 0
			print("Fizz")
		else if i % 5 = 0
			print("Buzz")
		else
			print(i)
		end
	end
}
```


## IBM 1620 SPS

```mw
     START RCTY
     LOOP  SM  FC,1
           SM  BC,1
           CM  FC,0
           BNE DOBUZ
           WATYFIZZ
           AM  OUT,1
           AM  FC,3
     DOBUZ CM  BC,0
           BNE END
           WATYBUZZ
           AM  OUT,1
           AM  BC,5
     END   CM  OUT,0
           BNE ENDL
           WNTYIT-2
     ENDL  AM  IT,1
           SM  COUNT,1
           TFM OUT,0
           RCTY
           CM  COUNT,0
           BNE LOOP
           H    
     FIZZ  DAC 5,FIZZ@
     BUZZ  DAC 5,BUZZ@
     FC    DC  5,3
     BC    DC  5,5
     OUT   DC  5,0
     IT    DC  5,1
           DC  1,@
     COUNT DC  5,100
           DENDSTART
```


## Icon and Unicon

```mw
# straight-forward modulo tester
procedure main()
    every i := 1 to 100 do
        if i % 15 = 0 then
            write("FizzBuzz")
        else if i % 5 = 0 then
            write("Buzz")
        else if i % 3 = 0 then
            write("Fizz")
        else
            write(i)
end
```

```mw
# idiomatic modulo tester, 1st alternative
procedure main()
    every i := 1 to 100 do
        write((i % 15 = 0 & "FizzBuzz") | (i % 5 = 0 & "Buzz") | (i % 3 = 0 & "Fizz") | i)
end
```

```mw
# idiomatic modulo tester, 2nd alternative
procedure main()
    every i := 1 to 100 do
        write(case 0 of {
                 i % 15 : "FizzBuzz"
                 i % 5  : "Buzz"
                 i % 3  : "Fizz"
                 default: i
        })
end
```

```mw
# straight-forward buffer builder
procedure main()
    every i := 1 to 100 do {
        s := ""
        if i % 3 = 0 then
            s ||:= "Fizz"
        if i % 5 = 0 then
            s ||:= "Buzz"
        if s == "" then
            s := i
        write(s)
    }
end
```

```mw
# idiomatic buffer builder, 1st alternative
procedure main()
    every i := 1 to 100 do
        write("" ~== (if i % 3 = 0 then "Fizz" else "") || (if i % 5 == 0 then "Buzz" else "") | i)
end
```

```mw
# idiomatic buffer builder, 2nd alternative
procedure main()
    every i := 1 to 100 do {
        s   := if i%3 = 0 then "Fizz" else ""
        s ||:= if i%5 = 0 then "Buzz"
        write(("" ~= s) | i)
    }
end
```


## Idris

```mw
partial
fizzBuzz : Nat -> String
fizzBuzz n = if (n `modNat` 15) == 0 then "FizzBuzz"
             else if (n `modNat` 3) == 0 then "Fizz"
             else if (n `modNat` 5)  == 0 then "Buzz"
             else show n

main : IO ()
main = sequence_ $ map (putStrLn . fizzBuzz) [1..100]
```


## Inform 6

```mw
[ Main i;
    for (i = 1: i <= 100: i++) {
        if (i % 3 == 0)
            print "Fizz";
        if (i % 5 == 0)
            print "Buzz";
        if (i % 3 ~= 0 && i % 5 ~= 0)
            print i;

        print "^";
    }
];
```


## Inform 7

(Does not work in the current version of Inform 7)

```mw
Home is a room.

When play begins:
	repeat with N running from 1 to 100:
		let printed be false;
		if the remainder after dividing N by 3 is 0:
			say "Fizz";
			now printed is true;
		if the remainder after dividing N by 5 is 0:
			say "Buzz";
			now printed is true;
		if printed is false, say N;
		say ".";
	end the story.
```

(Version which is less "programmy", and more in the natural English style of interactive fiction.)

```mw
The space is a room.  An item is a kind of thing.  In the space are 100 items.

To say the name:
	let the count be the number of items carried by the player;
	say "[if the count is the count to the nearest 15]fizzbuzz.[otherwise if the count is the count to the nearest 3]fizz.[otherwise if the count is the count to the nearest 5]buzz.[otherwise][the count in words].".

To count:
	if an item is in the space
	begin;
		let the next one be a random item in the space; silently try taking the next one;
		say "[the name]" in sentence case;
		count;
		end the story;
	end if.
		
When play begins: count.  Use no scoring.
```


## Insitux

```mw
(function fizzbuzz n
  (match (map (rem n) [3 5])
    [0 0] "FizzBuzz"
    [0 _] "Fizz"
    [_ 0] "Buzz"
    n))

(loop 100 i
  (-> i inc fizzbuzz print))
```


## Io

Here's one way to do it:

```mw
for(a,1,100,
   if(a % 15 == 0) then(
      "FizzBuzz" println
   ) elseif(a % 3 == 0) then(
      "Fizz" println
   ) elseif(a % 5 == 0) then(
      "Buzz" println
   ) else (
      a println
   )
)
```

And here's a port of the Ruby version, which I personally prefer:

```mw
a := 0; b := 0
for(n, 1, 100,
    if(a = (n % 3) == 0, "Fizz" print);
    if(b = (n % 5) == 0, "Buzz" print);
    if(a not and b not, n print);
    "\n" print
)
```

And here is another more idiomatic version:

```mw
for (n, 1, 100,
    fb := list (
        if (n % 3 == 0, "Fizz"),
        if (n % 5 == 0, "Buzz")) select (isTrue)
    
    if (fb isEmpty, n, fb join) println
)
```


## Ioke

```mw
(1..100) each(x,
  cond(
    (x % 15) zero?, "FizzBuzz" println,
    (x % 3) zero?, "Fizz" println,
    (x % 5) zero?, "Buzz" println
  )
)
```


## Iptscrae

```mw
; FizzBuzz in Iptscrae
1 a =
{
   "" b =
   { "fizz" b &= } a 3 % 0 == IF
   { "buzz" b &= } a 5 % 0 == IF
   { a ITOA LOGMSG } { b LOGMSG } b STRLEN 0 == IFELSE
   a ++
}
{ a 100 <= } WHILE
```


## IS-BASIC

See FizzBuzz/Basic


## J

### "One number at a time" solutions

Perhaps the most concise approach would be

```mw
(":[^:(0=#@])Fizz`Buzz;@#~0=3 5&|)"0>:i.100
```

This uses Copy (`#`) to apply a 2-integer replication vector to the boxed array `'Fizz';'Buzz'`, and then razes (`;`) the result, producing either 'Fizz', 'Buzz', or 'FizzBuzz'. The expression Fizz`Buzz exploits an implementation detail of Tie (`) to create two boxed strings. `": [^:(0=#@]) ...` conditionally replaces the result of Copy with the formatted input number if the former is empty.

A more elegant version, in that it treats all cases symmetrically:

```mw
((+:/,])@(0=3 5&|);@#Fizz`Buzz;~":)"0>:i.100
```

This version prepends the formatted input number to the boxed array consisting of `'Fizz';'Buzz'`, and computes a 3-integer replication vector to select from it. `(+:/,])@(0=3 5&|)` says to append 1 (to select the formatted number), if the input is neither divisible by 3 nor 5, or otherwise to append 0 (`+:` is NOR). So the replication vector ends up being `0 1 0` (selecting 'Fizz'), `0 0 1` ('Buzz'), `0 1 1` ('FizzBuzz'), or `1 0 0` (the formatted number).

Using antibase and indexing:

```mw
>((2#.0=5 3|]){Fizz`Buzz`FizzBuzz;~":)&>1+i.100
```

This solution uses antibase (`#.`) to decode e.g. `1 1` (a possible result of `5 3|]`) from base-2 into base-10, yielding e.g. `3`, which is used to select appropriate output from the vector of strings.

A more complex approach:

```mw
>((2#.3 q:15&+.){(|.(;~;);:'Fizz Buzz');~":)&>1+i.100
```

You can run this here: >((2#.3 q:15&+.){(|.(;~,&;);:'Fizz Buzz');~":)&>1+i.100

(The above is a live link to a browser based implementation of fizzbuzz in J. To see how this expression works, remove the leading > leaving items in boxes rather than on lines by themselves. And, then, replace the { with ; which means that instead of using the left argument to select (index) from a list of boxes, the left argument is appended in a box to the left of those boxes. Perhaps also replace the 100 with 20 to shrink the result size. If you remove the 1+i.20 (or 1+i.100) entirely, that would display as the verb (function) which is applied to each number.)

Other approaches are possible: Solution _1: Using agent (`@.`) as a switch:

```mw
":`('Fizz'"_)`('Buzz'"_)`('FizzBuzz'"_)@.(2#.0=5 3&|)"0>:i.100
```

Solution 0

```mw
> }. (<'FizzBuzz') (I.0=15|n)} (<'Buzz') (I.0=5|n)} (<'Fizz') (I.0=3|n)} ":&.> n=: i.101
```

Solution 1

```mw
Fizz=: 'Fizz' #~ 0 = 3&|
Buzz=: 'Buzz' #~ 0 = 5&|
FizzBuzz=: ": [^:('' -: ]) Fizz,Buzz

FizzBuzz"0 >: i.100
```

Solution 2 (has taste of table-driven template programming)

```mw
CRT0=: 2 : ' (, 0 = +./)@(0 = m | ]) ;@# n , <@": '
NB. Rather (, 0 = +./) than (, +:/) because designed for
NB. 3 5 7 CRT0 (;:'Chinese Remainder Period') "0 >: i. */3 5 7
FizzBuzz=: 3 5 CRT0 (;:'Fizz Buzz')

FizzBuzz"0 >: i.100
```

Solution 3 (depends on an obsolete feature of @ in f`g`h@p)

```mw
'`f   b   fb'  =: ('Fizz'"_) ` ('Buzz'"_) ` (f , b)
'`cm3 cm5 cm15'=: (3&|)      ` (5&|)      ` (15&|)  (0&=@)
FizzBuzz=: ": ` f @. cm3 ` b @. cm5 ` fb @. cm15  NB. also:
FizzBuzz=: ": ` f @. cm3 ` b @. cm5 ` (f,b) @. (cm3 *. cm5)

FizzBuzz"0 >: i.100
```

### "Whole array at once" solutions

Solution 4 (relatively concise):

```mw
{{>(#.|:0=3 5|&><L)}(":&.>L=.1+i.y),|:(y,3)$;:'Fizz Buzz FizzBuzz'}}100
```

This solution makes use of Composite Item (`m}y`) to select from a boxed table.

Solution 5 (relatively concise):

```mw
   ;:inv}.(":&.> [^:(0 = #@])&.> [: ,&.>/ ;:@'Fizz Buzz' #&.>~ 0=3 5|/])i.101
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fiz...
```

Here's some intermediate results for subexpressions of this last version (but with a shorter list of numbers):

```mw
   i.10
0 1 2 3 4 5 6 7 8 9
   (3 5 |/ ])i.10
0 1 2 0 1 2 0 1 2 0
0 1 2 3 4 0 1 2 3 4
   (0=3 5 |/ ])i.10
1 0 0 1 0 0 1 0 0 1
1 0 0 0 0 1 0 0 0 0
   (;:'Fizz Buzz')
┌────┬────┐
│Fizz│Buzz│
└────┴────┘
   ((;:'Fizz Buzz') #&.>~0=3 5 |/ ])i.10
┌────┬┬┬────┬┬────┬────┬┬┬────┐
│Fizz│││Fizz││    │Fizz│││Fizz│
├────┼┼┼────┼┼────┼────┼┼┼────┤
│Buzz│││    ││Buzz│    │││    │
└────┴┴┴────┴┴────┴────┴┴┴────┘
   ([: ,&.>/ (;:'Fizz Buzz') #&.>~0=3 5 |/ ])i.10
┌────────┬┬┬────┬┬────┬────┬┬┬────┐
│FizzBuzz│││Fizz││Buzz│Fizz│││Fizz│
└────────┴┴┴────┴┴────┴────┴┴┴────┘
   (":&.>)i.10
┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
│0│1│2│3│4│5│6│7│8│9│
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
   (":&.> [^:(0 = #@])&.> [: ,&.>/ (;:'Fizz Buzz') #&.>~0=3 5 |/ ])i.10
┌────────┬─┬─┬────┬─┬────┬────┬─┬─┬────┐
│FizzBuzz│1│2│Fizz│4│Buzz│Fizz│7│8│Fizz│
└────────┴─┴─┴────┴─┴────┴────┴─┴─┴────┘
   }.(":&.> [^:(0 = #@])&.> [: ,&.>/ (;:'Fizz Buzz') #&.>~0=3 5 |/ ])i.10
┌─┬─┬────┬─┬────┬────┬─┬─┬────┐
│1│2│Fizz│4│Buzz│Fizz│7│8│Fizz│
└─┴─┴────┴─┴────┴────┴─┴─┴────┘
   ;:inv}.(":&.> [^:(0 = #@])&.> [: ,&.>/ (;:'Fizz Buzz') #&.>~0=3 5 |/ ])i.10
1 2 Fizz 4 Buzz Fizz 7 8 Fizz
```


## Jactl

```mw
100.map{ it + 1 }
   .map{ [it, (it % 5 == 0 ? 'Fizz' : '') + (it % 3 == 0 ? 'Buzz' : '')] }
   .each{ println it[1] ? it[1] : it[0] }
```


## Janet

```mw
(loop [i :range [1 101]
       :let [fizz (zero? (% i 3))
             buzz (zero? (% i 5))]]
  (print (cond
           (and fizz buzz) "fizzbuzz"
           fizz "fizz"
           buzz "buzz"
           i)))
```
