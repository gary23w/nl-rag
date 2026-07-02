---
title: "99 bottles of beer (part 4/5)"
source: https://rosettacode.org/wiki/99_Bottles_of_Beer
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/5
---

## Fortran

### F90 version

```mw
program bottlestest

  implicit none

  integer :: i
  
  character(len=*), parameter   :: bwall = " on the wall", &
                                   bottles = "bottles of beer", &
                                   bottle  = "bottle of beer", &
                                   take = "Take one down, pass it around", &
                                   form = "(I0, ' ', A)"

  do i = 99,0,-1
     if ( i /= 1 ) then
        write (*,form)  i, bottles // bwall
        if ( i > 0 ) write (*,form)  i, bottles
     else
        write (*,form)  i, bottle // bwall
        write (*,form)  i, bottle
     end if
     if ( i > 0 ) write (*,*) take
  end do

end program bottlestest
```

### MPI version

```mw
program bottlesMPI

  implicit none

  integer :: ierr,rank,nproc
  
  character(len=*), parameter   :: bwall = " on the wall", &
                                   bottles = "bottles of beer", &
                                   bottle  = "bottle of beer", &
                                   take = "Take one down, pass it around", &
                                   form = "(I0, ' ', A)"

  call mpi_init(ierr)
  call mpi_comm_size(MPI_COMM_WORLD,nproc, ierr)
  call mpi_comm_rank(MPI_COMM_WORLD,rank,ierr)

  if ( rank /= 1 ) then
     write (*,form)  rank, bottles // bwall
     if ( rank > 0 ) write (*,form)  rank, bottles
  else
     write (*,form)  rank, bottle // bwall
     write (*,form)  rank, bottle
  end if
  if ( rank > 0 ) write (*,*) take

  call mpi_finalize(ierr)

end program bottlesMPI
```

Usage:

```
mpif90 filename.f90
mpiexec -np 99 a.out
```

### Fortran 2003/2008 OOP version

Works with GNU gfortran 5.0.0 and Intel ifort 15.0.2

```mw
module song_typedefs
   implicit none

   private ! all
   public :: TBottles

   type, abstract :: TContainer
      integer :: quantity
   contains
      ! deferred method i.e. abstract method =  must be overridden in extended type
      procedure(take_one), deferred, pass :: take_one
      procedure(show_quantity), deferred, pass :: show_quantity
   end type TContainer

   abstract interface
      subroutine  take_one(this)
         import TContainer
         implicit none
         class(TContainer) :: this
      end subroutine take_one
      subroutine  show_quantity(this)
         import TContainer
         implicit none
         class(TContainer) :: this
      end subroutine show_quantity
   end interface

   ! extended derived type
   type, extends(TContainer) :: TBottles
   contains
      procedure, pass :: take_one => take_one_bottle
      procedure, pass :: show_quantity => show_bottles
      final :: finalize_bottles
   end type TBottles

 contains

   subroutine  show_bottles(this)
      implicit none
      class(TBottles) :: this
      ! integer :: show_bottles
      character(len=*), parameter :: bw0 = "No more bottles of beer on the wall,"
      character(len=*), parameter :: bwx = "bottles of beer on the wall,"
      character(len=*), parameter :: bw1 = "bottle of beer on the wall,"
      character(len=*), parameter :: bb0 = "no more bottles of beer."
      character(len=*), parameter :: bbx = "bottles of beer."
      character(len=*), parameter :: bb1 = "bottle of beer."
      character(len=*), parameter :: fmtxdd = "(I2,1X,A28,1X,I2,1X,A16)"
      character(len=*), parameter :: fmtxd = "(I1,1X,A28,1X,I1,1X,A16)"
      character(len=*), parameter :: fmt1 = "(I1,1X,A27,1X,I1,1X,A15)"
      character(len=*), parameter :: fmt0 = "(A36,1X,A24)"

      select case (this % quantity)
       case (10:)
         write(*,fmtxdd) this % quantity, bwx, this % quantity, bbx
       case (2:9)
         write(*,fmtxd) this % quantity, bwx, this % quantity, bbx
       case (1)
         write(*,fmt1) this % quantity, bw1, this % quantity, bb1
       case (0)
         write(*,*)
         write(*,fmt0) bw0, bb0
       case default
         write(*,*)"Warning!  Number of bottles exception, error 42. STOP"
         stop
      end select
      !    show_bottles = this % quantity
   end subroutine show_bottles

   subroutine  take_one_bottle(this) ! bind(c, name='take_one_bottle')
      implicit none
      class(TBottles) :: this
      ! integer :: take_one_bottle
      character(len=*), parameter :: t1 = "Take one down and pass it around,"
      character(len=*), parameter :: remx = "bottles of beer on the wall."
      character(len=*), parameter :: rem1 = "bottle of beer on the wall."
      character(len=*), parameter :: rem0 = "no more bottles of beer on the wall."
      character(len=*), parameter :: fmtx = "(A33,1X,I2,1X,A28)"
      character(len=*), parameter :: fmt1 = "(A33,1X,I2,1X,A27)"
      character(len=*), parameter :: fmt0 = "(A33,1X,A36)"

      this % quantity = this % quantity -1

      select case (this%quantity)
       case (2:)
         write(*,fmtx) t1, this%quantity, remx
       case (1)
         write(*,fmt1) t1, this%quantity, rem1
       case (0)
         write(*,fmt0) t1, rem0
       case (-1)
         write(*,'(A66)') "Go to the store and buy some more, 99 bottles of beer on the wall."
       case default
         write(*,*)"Warning!  Number of bottles exception, error 42. STOP"
         stop
      end select

   end subroutine take_one_bottle

   subroutine  finalize_bottles(bottles)
      implicit none
      type(TBottles) :: bottles
   ! here can be more code
   end subroutine finalize_bottles

end module song_typedefs

!-----------------------------------------------------------------------
!Main program
!-----------------------------------------------------------------------
program    bottles_song
   use song_typedefs
   implicit none
   integer, parameter :: MAGIC_NUMBER = 99
   type(TBottles), target :: BTLS

   BTLS = TBottles(MAGIC_NUMBER)

   call make_song(BTLS)

 contains

   subroutine make_song(bottles)
      type(TBottles) :: bottles
      do while(bottles%quantity >= 0)
         call bottles%show_quantity()
         call bottles%take_one()
      enddo
   end subroutine make_song

end program bottles_song
```


## Frege

Translation of

:

Haskell

(*identical* to the Haskell, apart from adding the module declaration)

Works with

:

Frege

version 3.21.586-g026e8d7

```mw
module Beer where

main = mapM_ (putStrLn . beer) [99, 98 .. 0]
beer 1 = "1 bottle of beer on the wall\n1 bottle of beer\nTake one down, pass it around"
beer 0 = "better go to the store and buy some more."
beer v = show v ++ " bottles of beer on the wall\n"
                ++ show v
                ++ " bottles of beer\nTake one down, pass it around\n"
                ++ head (lines $ beer $ v-1) ++ "\n"
```


## friendly interactive shell

See 99 Bottles of Beer/Shell


## Frink

Frink tracks units of measure through all calculations. It has a large library of built-in units of measure, including volume. The following program prints out the remaining volume of beer (assuming we start with 99 bottles of beer, each containing 12 fluid ounces) in different random units of volume, never repeating a unit.

```mw
units = array[units[volume]]
showApproximations[false]

for n = 99 to 0 step -1
{
   unit = units.removeRandom[]
   str = getBottleString[n, unit]
   
   println["$str of beer on the wall, $str."]

   if (n == 0)
      println["Go to the store and buy some more, 99 bottles of beer on the wall."]
   else
      println["Take one down and pass it around, " + getBottleString[n-1, unit] + " on the wall.\n"]
}

getBottleString[n, unit] := format[n*12 floz, unit, 6] + "s"
```

Sample randomized output:

```
0.019386 facecords of beer on the wall, 0.019386 facecords.
Take one down and pass it around, 0.019190 facecords on the wall.

36.750000 quarts of beer on the wall, 36.750000 quarts.
Take one down and pass it around, 36.375000 quarts on the wall.

581539.650545 brminims of beer on the wall, 581539.650545 brminims.
Take one down and pass it around, 575544.396416 brminims on the wall.

10.377148 scotsoatlippys of beer on the wall, 10.377148 scotsoatlippys.
Take one down and pass it around, 10.269053 scotsoatlippys on the wall.

7.416004 cangallons of beer on the wall, 7.416004 cangallons.
Take one down and pass it around, 7.337941 cangallons on the wall.

3335.894135 dessertspoons of beer on the wall, 3335.894135 dessertspoons.
Take one down and pass it around, 3300.405899 dessertspoons on the wall.

0.233105 barrelbulks of beer on the wall, 0.233105 barrelbulks.
Take one down and pass it around, 0.230599 barrelbulks on the wall.

21.766118 magnums of beer on the wall, 21.766118 magnums.
Take one down and pass it around, 21.529530 magnums on the wall.

1092.000000 fluidounces of beer on the wall, 1092.000000 fluidounces.
Take one down and pass it around, 1080.000000 fluidounces on the wall.
...
12.000000 ponys of beer on the wall, 12.000000 ponys.
Take one down and pass it around, 0.000000 ponys on the wall.

0.000000 brfluidounces of beer on the wall, 0.000000 brfluidounces.
Go to the store and buy some more, 99 bottles of beer on the wall.
```


## FunL

```mw
val
  numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
    8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve'}
  alt = {3:'thir', 5:'fif'}

def
  suffix( a, b ) = (if a.endsWith( 't' ) then a.substring( 0, a.length()-1 ) else a) + b

  number( n@(13 | 15) ) = suffix( alt(n%10), 'teen' )
  number( 20 ) = 'twenty'
  number( n@(30 | 50) ) = suffix( alt(n\10), 'ty' )
  number( n )
    | n <= 12 = numbers(n)
    | n <= 19 = suffix( numbers(n%10), 'teen' )
    | 10|n = suffix( numbers(n\10), 'ty' )
    | otherwise = number( n\10*10 ) + '-' + number( n%10 )

  cap( s ) = s.substring( 0, 1 ).toUpperCase() + s.substring( 1, s.length() )

  bottles( 0 ) = 'no more bottles'
  bottles( 1 ) = 'one bottle'
  bottles( n ) = number( n ) + ' bottles'

  verse( 0 )   = ('No more bottles of beer on the wall, no more bottles of beer.\n'
                  + 'Go to the store and buy some more, ninety-nine bottles of beer on the wall.')
  verse( n )   = (cap( bottles(n) ) + ' of beer on the wall, ' + bottles( n ) + ' of beer.\n'
                  + 'Take one down and pass it around, ' + bottles( n-1 )
                  + ' of beer on the wall.\n')

for i <- 99..0 by -1 do println( verse(i) )
```


## FutureBasic

```mw
include "NSLog.incl"

NSUInteger  i
CFStringRef a, b, c

a = @" bottles of beer on the wall,\n"
b = @" bottles of beer.\n"
c = @"Take one down, pass it around,\n"

for i = 99 to 1 step -1
  NSLog( @"%ld%@%ld%@%@%ld%@\n", i, a, i, b, c, i -1, a )
next

HandleEvents
```


## Gambas

Implementation of the code '99 bottles of beer' written in Visual Basic. Code tested in Gambas 3.15.2

```mw
' Gambas module file

Public Const bottlesofbeer As String = " bottles of beer."
Public Const onthewall As String = " on the wall."
Public Const takeonedown As String = "Take one down, pass it around."
Public Const onebeer As String = "1 bottle of beer"

Public Sub Main()
  
  Dim bottles As Byte
  
  For bottles = 99 To 3 Step -1
    Print CStr(bottles) & bottlesofbeer & onthewall
    Print CStr(bottles) & bottlesofbeer
    Print takeonedown
    Print CStr(bottles - 1) & bottlesofbeer & onthewall
    Print
  Next
  
  Print "2" & bottlesofbeer & onthewall
  Print "2" & bottlesofbeer
  Print takeonedown
  Print onebeer & onthewall
  Print
  
  Print onebeer & onthewall
  Print onebeer
  Print takeonedown
  Print "No more" & bottlesofbeer & onthewall
  Print
  
  Print "No" & bottlesofbeer & onthewall
  Print "No" & bottlesofbeer
  Print "Go to the store, buy some more."
  Print "99" & bottlesofbeer & onthewall
  
End
```


## GAP

```mw
Bottles := function(n)
	local line, i, j, u;
	line := function(n)
		s := String(n);
		if n < 2 then
			return Concatenation(String(n), " bottle of beer");
		else
			return Concatenation(String(n), " bottles of beer");
		fi;
	end;
	for i in [1 .. n] do
		j := n - i + 1;
		u := line(j);
		Display(Concatenation(u, " on the wall"));
		Display(u);
		Display("Take one down, pass it around");
		Display(Concatenation(line(j - 1), " on the wall"));
		if i <> n then
			Display("");
		fi;
	od;
end;
```


## GDScript

Works with

:

Godot

version 4.0

```mw
extends MainLoop

# Represents a count of bottles
class Bottles:
	var count := 99

	func take(n: int = 1) -> void:
		count -= n

	func _to_string() -> String:
		match count:
			0: return "No more bottles"
			1: return "1 bottle"
			_: return "%s bottles" % count

func _process(_delta: float) -> bool:
	var bottles := Bottles.new()
	while bottles.count > 0:
		print("%s of beer on the wall" % bottles)
		print("%s of beer" % bottles)
		print("Take one down, pass it around")
		bottles.take()
		print("%s of beer on the wall" % bottles)
		# Seperate paragraphs
		if bottles.count > 0:
			print()

	return true # Makes the program exit
```

### Silly node-tree version

This uses the node's children as the display method (which can be viewed in-editor with the remote tab).

```mw
extends Node

@export var alcoholism: int = 99

func _ready():
	# Add the lyrics as child nodes
	var padding := "" # Avoid name clashes by adding spaces
	for bottleCount in range(alcoholism, 0, -1):
		# Seperate paragraphs with blank nodes
		if bottleCount < alcoholism:
			add_lyric(padding)
		add_lyric("%s of beer on the wall" % [_formatBottles(bottleCount)])
		add_lyric("%s of beer" % [_formatBottles(bottleCount)])
		add_lyric("Take one down, pass it around" + padding)
		add_lyric("%s of beer on the wall " % [_formatBottles(bottleCount - 1)]) # Extra space for name clash avoidance
		padding += " " # Add spaces so the names don't clash

func _formatBottles(bottleCount: int) -> String:
	return "%d bottle%s" % [bottleCount, "" if bottleCount == 1 else "s"]

func add_lyric(lyric: String) -> void:
	var new_child := Node.new()
	new_child.name = lyric
	add_child(new_child)
```


## Genie

```mw
[indent=4]
def plural(n:uint):string
    return (n == 1) ? "" : "s"
def no(n:uint):string
    return (n == 0) ? "No" : n.to_string()
init
    bottles:uint = 99;
    do
        print "%u bottle%s of beer on the wall", bottles, plural(bottles)
        print "%u bottle%s of beer", bottles, plural(bottles)
        print "Take one down, pass it around"
        --bottles
        print "%s bottle%s of beer on the wall\n", no(bottles), plural(bottles)
    while bottles != 0
```

**Output:**

```
prompt$ valac 99bottles.gs
prompt$ ./99bottles | tail -10
2 bottles of beer on the wall
2 bottles of beer
Take one down, pass it around
1 bottle of beer on the wall

1 bottle of beer on the wall
1 bottle of beer
Take one down, pass it around
No bottles of beer on the wall
```


## Gleam

```
import gleam/int
import gleam/io
import gleam/list

pub fn main() -> Nil {
  use verse <- list.each(list.range(99, 1))
  sing(drunkenly: verse |> BottlesOfBeer(OnTheWall))
  sing(drunkenly: verse |> BottlesOfBeer(NotOnTheWall))
  sing(drunkenly: TakeOneDown)
  sing(drunkenly: verse - 1 |> BottlesOfBeer(OnTheWall))
  io.println("")
}

fn bottles(amount: Int) -> String {
  case amount {
    1 -> "One bottle"
    0 -> "No bottles"
    x -> int.to_string(x) <> " bottles"
  }
}

pub type Line {
  BottlesOfBeer(Int, Where)
  TakeOneDown
}

pub type Where {
  OnTheWall
  NotOnTheWall
}

pub fn sing(drunkenly line: Line) -> Nil {
  let rng = int.random(100)
  case line {
    BottlesOfBeer(amount, OnTheWall) ->
      { amount |> bottles <> " of beer on the wall" } |> io.println
    BottlesOfBeer(amount, NotOnTheWall) ->
      { amount |> bottles <> " of beer on the wall" } |> io.println
    TakeOneDown if rng < 50 -> "Take one down, pass it around" |> io.println
    TakeOneDown -> "If one of those bottles should happen to fall" |> io.println
  }
}
```


## gnuplot

```mw
if (!exists("bottles")) bottles = 99
print sprintf("%i bottles of beer on the wall", bottles)
print sprintf("%i bottles of beer", bottles)
print "Take one down, pass it around"
bottles = bottles - 1
print sprintf("%i bottles of beer on the wall", bottles)
print ""
if (bottles > 0) reread
```


## Go

### No sense of humor

```mw
package main

import "fmt"

func main() {
	bottles := func(i int) string {
		switch i {
		case 0:
			return "No more bottles"
		case 1:
			return "1 bottle"
		default:
			return fmt.Sprintf("%d bottles", i)
		}
	}

	for i := 99; i > 0; i-- {
		fmt.Printf("%s of beer on the wall\n", bottles(i))
		fmt.Printf("%s of beer\n", bottles(i))
		fmt.Printf("Take one down, pass it around\n")
		fmt.Printf("%s of beer on the wall\n", bottles(i-1))
	}
}
```

### Typoglycemic

With code from RC tasks Number names, Knuth shuffle.

```mw
package main

import (
    "fmt"
    "math/rand"
    "strings"
    "time"
)

func main() {
    rand.Seed(time.Now().UnixNano())
    for i := 99; i > 0; i-- {
        fmt.Printf("%s %s %s\n",
            slur(numberName(i), i),
            pluralizeFirst(slur("bottle of", i), i),
            slur("beer on the wall", i))
        fmt.Printf("%s %s %s\n",
            slur(numberName(i), i),
            pluralizeFirst(slur("bottle of", i), i),
            slur("beer", i))
        fmt.Printf("%s %s %s\n",
            slur("take one", i),
            slur("down", i),
            slur("pass it around", i))
        fmt.Printf("%s %s %s\n",
            slur(numberName(i-1), i),
            pluralizeFirst(slur("bottle of", i), i-1),
            slur("beer on the wall", i))
    }
}

// adapted from Number names task
func numberName(n int) string {
    switch {
    case n < 0:
    case n < 20:
        return small[n]
    case n < 100:
        t := tens[n/10]
        s := n % 10
        if s > 0 {
            t += " " + small[s]
        }
        return t
    }
    return ""
}

var small = []string{"no", "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
    "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
var tens = []string{"ones", "ten", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"}

// pluralize first word of s by adding an s, but only if n is not 1.
func pluralizeFirst(s string, n int) string {
    if n == 1 {
        return s
    }
    w := strings.Fields(s)
    w[0] += "s"
    return strings.Join(w, " ")
}

// p is string to slur, d is drunkenness, from 0 to 99
func slur(p string, d int) string {
    // shuffle only interior letters
    a := []byte(p[1 : len(p)-1])
    // adapted from Knuth shuffle task.
    // shuffle letters with probability d/100.
    for i := len(a) - 1; i >= 1; i-- {
        if rand.Intn(100) >= d {
            j := rand.Intn(i + 1)
            a[i], a[j] = a[j], a[i]
        }
    }
    // condense spaces
    w := strings.Fields(p[:1] + string(a) + p[len(p)-1:])
    return strings.Join(w, " ")
}
```

**Output:**

Things start out pretty well...

```
ninety nine bottles of beer on the wall
ninety nine bottles of beer
take one down pass it around
ninety eight bottles of beer on the wall
ninety eight bottles of beer on the wall
ninety eight bottles of beer
take one down pass it around
ninety seven bottles of beer on the wall
ninety seven boetlts of beer on the wall
ninety seven bottles of beer
take one down pass it around
ninety six botelts of beer on the wall
```

Soon,

```
eighty four bottles of bere wn the oall
ehigty four bottles of beer
tkae one down pnssti arouad
eihhty tgree bttoles of beer en tho wall
eighty three blottes of beet on rhe wall
eighty three bottles of beer
taen oke down pass it around
eiwyth tgo bttoles of beew on lhr eatl
```

It ends very well, if you're drinking along.

```
two btloots ef bre enehta wo ll
two bs tleootf beer
tnoeka e dwon pts ou nsaaird
one bolote tf betwr le ao enhl
one beoo ttlf blwtenr ehoa el
one bltooe tf beer
tne okae down pasaostiu rnd
no bletts oof beloethw r ea nl
```


## Go!

Copied from The 99 Bottles of Beer web site with a minor bug fix.

```mw
-- 
-- 99 Bottles of Beer in Go!
-- John Knottenbelt
-- 
-- Go! is a multi-paradigm programming language that is oriented
-- to the needs of programming secure, production quality, agent
-- based applications.
-- 
--    http://www.doc.ic.ac.uk/~klc/dalt03.html 
-- 

main .. {
  include "sys:go/io.gof".
  include "sys:go/stdlib.gof".

  main() ->
      drink(99);
      stdout.outLine("Time to buy some more beer...").

  drink(0) -> {}.
  drink(i) -> stdout.outLine(
       bottles(i) <> " on the wall,\n" <>
       bottles(i) <> ".\n" <>
       "take one down, pass it around,\n" <>
       bottles(i-1) <> " on the wall.\n");
      drink(i-1).

  bottles(0) => "no bottles of beer".
  bottles(1) => "1 bottle of beer".
  bottles(i) => i^0 <> " bottles of beer".
}
```


## Goboscript

```mw
%include inflator/string

costumes "assets/blank.svg";

func add_bottle(n) {
    local s = "s";
    local s2 = "s";        
    local n_minus_1 = $n - 1;
    local end = "\n";

    if $n == 1 {
        n_minus_1 = "No more";
        s = "";
        end = "";
    } elif $n == 2 {
        s2 = "";
    }

    return $n&" bottle"&s&" of beer on the wall\n" &
        $n&" bottle"&s&" of beer\n" &
        "Take one down, pass it around\n" &
        n_minus_1&" bottle"&s2&" of beer on the wall" & end;
}

proc do_99_bottles_of_beer {
    local ret = "";
    local i = 99;
    repeat 99 {
        ret &= add_bottle(i);
        i--;
    }

    split ret, "\n";
    i = 1;
    repeat length split {
        log split[i];
        i++;
    }
}

onflag{main;}
proc main {
    do_99_bottles_of_beer;
}
```


## Golfscript

```mw
[296,{3/)}%-1%["No more"]+[" bottles":b]294*[b-1<]2*+[b]+[" of beer on the wall\n".8<"\nTake one down, pass it around\n"+1$n+]99*]zip
```


## Golo

```mw
module Bottles

augment java.lang.Integer {
	function bottles = |self| -> match {
		when self == 0 then "No bottles"
		when self == 1 then "One bottle"
		otherwise self + " bottles"
	}
}

function main = |args| {
	99: downTo(1, |i| {
		println(i: bottles() + " of beer on the wall,")
		println(i: bottles() + " of beer!")
		println("Take one down, pass it around,")
		println((i - 1): bottles() + " of beer on the wall!")
		println("--------------------------------------")
	})
}
```


## Gosu

```mw
for (i in 99..0) {

    print("${i} bottles of beer on the wall")

    if (i > 0) {
        print("${i} bottles of beer")
        print("Take one down, pass it around")
    }
    print("");

}
```


## Groovy

### Basic Solution

With a closure to handle special cardinalities of bottles.

```mw
def bottles = { "${it==0 ? 'No more' : it} bottle${it==1 ? '' : 's' }" }

99.downto(1) { i ->
    print """
${bottles(i)} of beer on the wall
${bottles(i)} of beer
Take one down, pass it around
${bottles(i-1)} of beer on the wall
"""
}
```

### Single Print Version

Uses a single print algorithm for all four lines. Handles cardinality on bottles, uses 'No more' instead of 0.

```mw
298.downto(2) {
    def (m,d) = [it%3,(int)it/3]
    print "${m==1?'\n':''}${d?:'No more'} bottle${d!=1?'s':''} of beer" +
          "${m?' on the wall':'\nTake one down, pass it around'}\n"
}
```

### Bottomless Beer Solution

Using more closures to create a richer lyrical experience.

```mw
def bottles = { "${it==0 ? 'No more' : it} bottle${it==1 ? '' : 's' }" }

def initialState = {
  """${result(it)}
${resultShort(it)}"""
}

def act = {
  it > 0 ?
      "Take ${it==1 ? 'it' : 'one'} down, pass it around" :
      "Go to the store, buy some more"
}

def delta = { it > 0 ? -1 : 99 }

def resultShort = { "${bottles(it)} of beer" }

def result = { "${resultShort(it)} on the wall" }

// //// uncomment commented lines to create endless drunken binge //// //
// while (true) {
99.downto(0) { i ->
  print """
${initialState(i)}
${act(i)}
${result(i+delta(i))}
"""
}
// Thread.sleep(1000)
// }
```


## GUISS

We will just use the calculator and keep taking one off. We do not get the full text here, but the number of the calculator shows how many bottles we still have left to drink:

```mw
Start,Programs,Accessories,Calculator,Button:9,Button:9,
Button:[hyphen],Button:1,Button:[equals],Button:[hyphen],Button:1,Button:[equals],
Button:[hyphen],Button:1,Button:[equals],Button:[hyphen],Button:1,Button:[equals],
Button:[hyphen],Button:1,Button:[equals],Button:[hyphen],Button:1,Button:[equals],
Button:[hyphen],Button:1,Button:[equals],Button:[hyphen],Button:1,Button:[equals]
```

We haven't drank all of the bottles at this point, but we can keep going, if we want.


## Halon

```mw
$plural = "s";
$x = 99;
while ($x > 0) {
    echo "$x bottle$plural of beer on the wall";
    echo "$x bottle$plural of beer";
    echo "Take one down, pass it around";
    $x -= 1;
    if ($x == 1)
        $plural = "";
    if ($x > 0)
        echo "$x bottle$plural of beer on the wall\n";
    else
        echo "No more bottles of beer on the wall!";
}
```


## Haskell

#### Brevity

A relatively concise solution:

```mw
main = mapM_ (putStrLn . beer) [99, 98 .. 0]
beer 1 = "1 bottle of beer on the wall\n1 bottle of beer\nTake one down, pass it around"
beer 0 = "better go to the store and buy some more."
beer v = show v ++ " bottles of beer on the wall\n" 
                ++ show v 
                ++" bottles of beer\nTake one down, pass it around\n" 
                ++ head (lines $ beer $ v-1) ++ "\n"
```

#### List comprehension

As a list comprehension:

```mw
import qualified Char

main = putStr $ concat
   [up (bob n) ++ wall ++ ", " ++ bob n ++ ".\n" ++
    pass n ++ bob (n - 1) ++ wall ++ ".\n\n" |
    n <- [99, 98 .. 0]]
   where bob n = (num n) ++ " bottle" ++ (s n) ++ " of beer"
         wall = " on the wall"
         pass 0 = "Go to the store and buy some more, "
         pass _ = "Take one down and pass it around, "
         up (x : xs) = Char.toUpper x : xs
         num (-1) = "99"
         num 0    = "no more"
         num n    = show n
         s 1 = ""
         s _ = "s"
```

#### Writer monad and Template Haskell

Another version, which uses a Writer monad to collect each part of the song. It also uses Template Haskell to generate the song at compile time.

```mw
{-# LANGUAGE TemplateHaskell #-}
-- build with "ghc --make beer.hs"
module Main where
import Language.Haskell.TH
import Control.Monad.Writer

-- This is calculated at compile time, and is equivalent to
-- songString = "99 bottles of beer on the wall\n99 bottles..."
songString = 
    $(let
         sing = tell -- we can't sing very well...

         someBottles 1 = "1 bottle of beer "
         someBottles n = show n ++ " bottles of beer "

         bottlesOfBeer n = (someBottles n ++) 

         verse n = do
           sing $ n `bottlesOfBeer` "on the wall\n"
           sing $ n `bottlesOfBeer` "\n"
           sing $ "Take one down, pass it around\n"
           sing $ (n - 1) `bottlesOfBeer` "on the wall\n\n"

         song = execWriter $ mapM_ verse [99,98..1]

      in return $ LitE $ StringL $ song)

main = putStr songString
```

#### Avoiding append by spelling bottle backwards

Is there something just a little prickly and displeasing about (++) ? Monoid (<>) is less spiky, but neither is needed when 'bottle' is written backwards.

```mw
location, distribution, solution :: String
[location, distribution, solution] =
  [ "on the wall",
    "Take one down, pass it around",
    "Better go to the store to buy some more"
  ]

incantation :: Int -> String
incantation n
  | 0 == n = solution
  | otherwise =
    unlines
      [ inventory n,
        asset n,
        distribution,
        inventory $ pred n
      ]

inventory :: Int -> String
inventory = unwords . (: [location]) . asset

asset :: Int -> String
asset n =
  let suffix n
        | 1 == n = []
        | otherwise = ['s']
   in unwords
        [show n, (reverse . concat) $ suffix n : ["elttob"]]

main :: IO ()
main = putStrLn $ unlines (incantation <$> [99, 98 .. 0])
```


## Haxe

### Simple solution

```mw
class RosettaDemo
{
    static public function main()
    {
        singBottlesOfBeer(100);
    }

    static function singBottlesOfBeer(bottles : Int)
    {
        var plural : String = 's';

        while (bottles >= 1)
        {
            Sys.println(bottles + " bottle" + plural + " of beer on the wall,");
            Sys.println(bottles + " bottle" + plural + " of beer!");
            Sys.println("Take one down, pass it around,");
            if (bottles - 1 == 1)
            {
                plural = '';
            }

            if (bottles > 1)
            {
                Sys.println(bottles-1 + " bottle" + plural + " of beer on the wall!\n");
            }
            else
            {
                Sys.println("No more bottles of beer on the wall!");
            }
            bottles--;
        }
    }
}
```

### Macro solution

All those counters, loops and conditinal blocks are pretty expensive in runtime compared to single print of fully inlined text of the song. Let's generate that print with macro.

```mw
class Bottles {

    static public function main () : Void {
        singBottlesOfBeer(100);
    }

    macro static public function singBottlesOfBeer (bottles:Int) {
        var lines = [];
        var s : String = 's';

        var song : String = '';
        while( bottles >= 1 ){
            song += '$bottles bottle$s of beer on the wall,\n';
            song += '$bottles bottle$s of beer!\n';
            song += 'Take one down, pass it around,\n';

            bottles --;

            if( bottles > 1 ){
                song += '$bottles bottles of beer on the wall!\n\n';
            }else if( bottles == 1 ){
                s = '';
                song += '$bottles bottle of beer on the wall!\n\n';
            }else{
                song += 'No more bottles of beer on the wall!\n';
            }
        }

        return macro Sys.print($v{song});
    }

}
```


## hexiscript

```mw
fun bottles amount beverage location
  let bottle " bottles of "
  if   amount = 0; let amount "No more"
  elif amount = 1; let bottle " bottle of "; endif
  return amount + bottle + beverage + " " + location
endfun

fun take amount location
  return "Take " + amount + " " + location
endfun

fun pass entity destination
  return ", pass " + entity + " " + destination
endfun

let amount 99
while amount > 0
  println bottles amount "beer" "on the wall"
  println bottles amount "beer" ""
  println take "one" "down" + pass "it" "around"
  println bottles (--amount) "beer" "on the wall\n"
endwhile
```


## HicEst

```mw
DO x = 99, 1, -1
  WRITE()   x       , "bottles of beer on the wall"
  BEEP("T16 be be be   bH bH   bH be   be be  2be ")

  WRITE()   x       , "bottles of beer"
  BEEP("2p  f f f      c  c    c  2f  ")

  WRITE()  "take one down,  pass it around"
  BEEP("2p  2d   d   d   2p d    d  d 2d  ")

  WRITE()   x     , "bottles of beer on the wall"
  BEEP("2p  #A #A #A c  c    d  #d   #d #d  2#d 2p")
ENDDO
```


## Hobbes

```mw
bottles :: int -> [char]
bottles n =
  match n with
  | 0 -> "no more bottles"
  | 1 -> "1 bottle"
  | _ -> show(n) ++ " bottles"

verse :: int -> [char]
verse n =
  if (n == 0) then
    "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
  else
    bottles(n) ++ " of beer on the wall, " ++ bottles(n) ++ " of beer.\nTake one down and pass it around, " ++ bottles(n - 1) ++ " of beer on the wall.\n"

// Usage: [putStrLn(verse(n)) | n <- reverse([0..99])]
```

**Output:**

```
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
...
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
```


## HolyC

The default is 99 bottles, but it can be modified by the parameter.

```mw
U0 BottlesOfBeer (I64 initial=99) {
	// This is made I64 rather than U64
	// Because, a U64 would overflow
	// At the end of the loop, thus it would loop forever (i-- would be 0-1 so it overflows and is always  greater than or equal to 0)
	I64 i = initial;

	for (; i >= 0; i--) {
		if (i == 1) {
			// Just a string on it's own will pass it to an inbuilt HolyC function that puts it to terminal
			"1 Bottle of Beer on the wall, 1 bottle of beer.\n";
			"Take one down and pass it around, no more bottles of beer on the wall.\n";
		} else if (i == 0) {
			"No more bottles of beer on the wall, no more bottles of beer.\n";
			"Go to the store and buy some more, 99 bottles of beer on the wall.\n";
		} else {
			"%d bottles of beer on the wall, %d bottles of beer.\n",i,i;
			"Take one down and pass it around, %d bottle",(i-1);
			// Only add the s if it's not 1
			if ((i-1) != 1) {
				"s";
			}

			" of beer on the wall.\n";
		}
	}
}

// Calls the function, which goes to the default parameters
BottlesOfBeer;
```


## Hoon

```mw
:-  %say
|=  [* * [bottles=_99 ~]]
:-  %noun
^-  wall
=/  output  `(list tape)`~
|-
?:  =(1 bottles)
  %-  flop
  :-  "1 bottle of beer on the wall"
  :-  "Take one down, pass it around"
  :-  "1 bottle of beer"
  :-  "1 bottle of beer on the wall"
      output
%=  $
  bottles  (dec bottles)
  output
  :-  "{<bottles>} bottles of beer on the wall"
  :-  "Take one down, pass it around"
  :-  "{<bottles>} bottles of beer"
  :-  "{<bottles>} bottles of beer on the wall"
      output
==
```


## Hope

El código es de Wolfgang Lohmann (wlohmann@informatik.uni-rostock.de)

```mw
dec app  :( list ( char ) X list ( char )) -> list ( char ) ;
dec i2c  : num -> char;
dec i2s  : num -> list(char);
dec beer : num -> list(char);

--- app ( nil , w )
       <= w  ;
--- app (( a  ::  v ), w )
       <=( a  ::  app ( v , w )) ;

--- i2c(0) <= '0';
--- i2c(1) <= '1';
--- i2c(2) <= '2';
--- i2c(3) <= '3';
--- i2c(4) <= '4';
--- i2c(5) <= '5';
--- i2c(6) <= '6';
--- i2c(7) <= '7';
--- i2c(8) <= '8';
--- i2c(9) <= '9';

--- i2s(x) <= if x < 10 then [i2c(x)] else
				app(i2s(x div 10), i2s( x mod 10)); 

--- beer(x) <= if x = 1 then app( i2s(x), 
				" bottle of beer. No more beer on the wall.")
                	else app( app( app( app( app( 
				i2s(x), 
				" bottles of beer on the wall, "),
				i2s(x)), 
				" bottles of beer. "),
				"Take one down, pass it around. "), 
				beer(y))
                        where y== x-1;
```


## HQ9+

See 99 Bottles of Beer/EsoLang


## Huginn

```mw
#! /bin/sh
exec huginn --no-argv -E "${0}" "${@}"
#! huginn

import Algorithms as algo;

main() {
	x = "{} bottle{} of beer on the wall,\n"
		"{} bottle{} of beer.\n"
		"Take one down, pass it around,\n"
		"{} bottle{} of beer on the wall.\n\n";
	for ( n : algo.range( 99, 0, -1 ) ) {
		bot = n > 0 ? n : "No";
		plu = n != 1 ? "s" : "";
		print( x.format( bot, plu, bot, plu, n > 1 ? n - 1 : "No", n != 2 ? "s" : "" ) );
	}
	print(
		"No bottles of beer on the wall,\n"
		"No bottles of beer.\n"
		"Go to the store, buy some more,\n"
		"99 bottles of beer on the wall.\n"
	);
	return ( 0 );
}
```


## HyperTalk

El código es de Eric Carlson eric@bungdabba.com

```mw
on BeerSong99
  BottlesOfBeer 99
end BeerSong99

on OutputBeerLyric beerString
  if ( beerString is "<reset>" ) then
    put empty into cd fld "beer song"
  else
    put beerString & return after cd fld "beer song"
  end if
end OutputBeerLyric

on BottlesOfBeer bottleCount
  put bottleCount into initialCount
  OutputBeerLyric "<reset>"
  
  repeat until ( bottleCount < 1 )
    set cursor to busy     -- let 'em know this might take a while
    put BottleString(bottleCount) into currentString
    OutputBeerLyric currentString && "of beer on the wall,"
    OutputBeerLyric currentString && "of beer."
    OutputBeerLyric "Take one down, and pass it around,"
    
    subtract one from bottleCount
    OutputBeerLyric BottleString(bottleCount) && "of beer on the wall." & return
  end repeat
  
  OutputBeerLyric "Go to the store and buy some more..."
  OutputBeerLyric initialCount & " bottles of beer on the wall."
end BottlesOfBeer

function BottleString bottleCount
  if ( bottleCount is 1 ) then
    return "1 bottle"
  else if ( bottleCount is 0 ) then
    return "no more bottles"
  else
    return bottleCount && "bottles"
  end if
end BottleString
```


## Icon and Unicon

The default is 99 bottles, but you can change this on the command line for really long trips...

```mw
procedure main(args)
   numBeers := integer(args[1]) | 99
   drinkUp(numBeers)
end

procedure drinkUp(beerMax)
    static beerMap
    initial {
        beerMap := table(" bottles")
        beerMap[1] := " bottle"
        }

    every beerCount := beerMax to 1 by -1 do {
       writes( beerCount,beerMap[beerCount]," of beer on the wall, ")
       write(  beerCount,beerMap[beerCount]," of beer.")

       writes("Take one down and pass it around, ")
       write(case x := beerCount-1 of {
             0       : "no more bottles"
             default : x||beerMap[x]
             }," of beer on the wall.\n")
       }

    write("No more bottles of beer on the wall, no more bottles of beer.")
    write("Go to the store and buy some more, ",
          beerMax," bottles of beer on the wall.")
end
```


## IDL

```mw
Pro bottles

for i=1,99 do begin
 print, 100-i, " bottles of beer on the wall.", 100-i, $
 " bottles of beer.", " Take one down, pass it around," , $
 99-i, " bottles of beer on the wall."
endfor
End
```

Since in IDL "FOR"-loops are the embodiment of pure evil (see http://www.idlcoyote.com/tips/forloops.html and http://www.idlcoyote.com/tips/forloops2.html) there is also a loop free IDL way:

```mw
Pro bottles_noloop
    b=(reverse(shift(sindgen(100),-1)))[1:99]
    b2=reverse(sindgen(99))
    wallT=replicate(' bottles of beer on the wall.', 100)
    wallT2=replicate(' bottles of beer.', 100)
    takeT=replicate('Take one down, pass it around,', 100)
    print, b+wallT+string(10B)+b+wallT2+string(10B)+takeT+string(10B)+b2+wallT+string(10B)
End
```

I found the above example very helpful but overdone. This is a more simple version:

```mw
Pro bottles_noloop2
    n_bottles=99
    b1 = reverse(SINDGEN(n_bottles,START=1))
    b2= reverse(SINDGEN(n_bottles))
    wallT=replicate(' bottles of beer on the wall.', n_bottles)
    wallT2=replicate(' bottles of beer.', n_bottles)
    takeT=replicate('Take one down, pass it around,', n_bottles)
    print, b1+wallT+string(10B)+b1+wallT2+string(10B)+takeT+string(10B)+b2+wallT+string(10B)
End
```


## Idris

```mw
beerSong : Fin 100 -> String
beerSong x = verses x where

    bottlesOfBeer : Fin n -> String
    bottlesOfBeer fZ      = "No more bottles of beer"
    bottlesOfBeer (fS fZ) = "1 bottle of beer"
    bottlesOfBeer k       = (show (finToInteger k)) ++ " bottles of beer"

    verse : Fin n -> String 
    verse fZ     = ""
    verse (fS n) = 
        (bottlesOfBeer (fS n)) ++ " on the wall,\n" ++
        (bottlesOfBeer (fS n)) ++ "\n" ++
        "Take one down, pass it around\n" ++
        (bottlesOfBeer n) ++ " on the wall\n"

    verses : Fin n -> String
    verses fZ     = ""
    verses (fS n) = (verse (fS n)) ++ (verses n)
```


## Inform 6

```mw
[ Bottles i;
  if(i == 1) return "bottle";

  return "bottles";
];

[ Beer i;
  print i, " ", (string) Bottles(i), " of beer on the wall^";
  print i, " ", (string) Bottles(i), " of beer^";
  print "Take one down, pass it around^";
  i--;
  print i, " ", (string) Bottles(i), " of beer on the wall^^";

  if(i ~= 0) Beer(i);
];

[ Main;
  Beer(99);
];
```


## Inform 7

### Programmatic solution

```mw
Beer Hall is a room.

When play begins:
	repeat with iteration running from 1 to 99:
		let N be 100 - iteration;
		say "[N] bottle[s] of beer on the wall[line break]";
		say "[N] bottle[s] of beer[line break]";
		say "Take one down, pass it around[line break]";
		say "[N - 1] bottle[s] of beer on the wall[paragraph break]";
	end the story.
```

### World model solution

This solution uses in-game objects to represent the wall and the bottles.

```mw
Beer Hall is a room.

The plural of bottle of beer is bottles of beer. A bottle of beer is a kind of thing.

The wall is a scenery supporter in Beer Hall. 99 bottles of beer are on the wall.

When play begins:
	while something is on the wall:
		say "[what's on the wall] on the wall[line break]";
		say "[what's on the wall][line break]";
		say "Take one down, pass it around[line break]";
		remove a random thing on the wall from play;
		say "[what's on the wall] on the wall[paragraph break]";
	end the story.

To say what's on the wall:
	if more than one thing is on the wall, say list of things on the wall;
	otherwise say "[number of things on the wall in words] bottle[s] of beer".
```


## Io

```mw
bottles := method(i,
    if(i==0, return "no more bottles of beer")
    if(i==1, return "1 bottle of beer")
    "" .. i .. " bottles of beer"
)
for(i, 99, 1, -1,
    write(
        bottles(i), " on the wall, ", 
        bottles(i), ",\n",
        "take one down, pass it around,\n",
        bottles(i - 1), " on the wall.\n\n"
    )
)
```
