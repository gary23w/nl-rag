---
title: "Towers of Hanoi (part 3/5)"
source: https://rosettacode.org/wiki/Towers_of_Hanoi
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/5
---

## Groovy

Unlike most solutions here this solution manipulates more-or-less actual stacks of more-or-less actual rings.

```mw
def tail = { list, n ->  def m = list.size(); list.subList([m - n, 0].max(),m) }

final STACK = [A:[],B:[],C:[]].asImmutable()

def report = { it -> }
def check = { it -> }

def moveRing = { from, to ->  to << from.pop(); report(); check(to) }

def moveStack
moveStack = { from, to, using = STACK.values().find { !(it.is(from) || it.is(to)) } ->
    if (!from) return
    def n = from.size()
    moveStack(tail(from, n-1), using, to)
    moveRing(from, to)
    moveStack(tail(using, n-1), to, from)
}
```

Test program:

```mw
enum Ring {
    S('°'), M('o'), L('O'), XL('( )');
    private sym
    private Ring(sym) { this.sym=sym }
    String toString() { sym }
}

report = { STACK.each { k, v ->  println "${k}: ${v}" }; println() }
check = { to -> assert to == ([] + to).sort().reverse() }

Ring.values().reverseEach { STACK.A << it }
report()
check(STACK.A)
moveStack(STACK.A, STACK.C)
```

**Output:**

```
A: [( ), O, o, °]
B: []
C: []

A: [( ), O, o]
B: [°]
C: []

A: [( ), O]
B: [°]
C: [o]

A: [( ), O]
B: []
C: [o, °]

A: [( )]
B: [O]
C: [o, °]

A: [( ), °]
B: [O]
C: [o]

A: [( ), °]
B: [O, o]
C: []

A: [( )]
B: [O, o, °]
C: []

A: []
B: [O, o, °]
C: [( )]

A: []
B: [O, o]
C: [( ), °]

A: [o]
B: [O]
C: [( ), °]

A: [o, °]
B: [O]
C: [( )]

A: [o, °]
B: []
C: [( ), O]

A: [o]
B: [°]
C: [( ), O]

A: []
B: [°]
C: [( ), O, o]

A: []
B: []
C: [( ), O, o, °]
```


## Haskell

Most of the programs on this page use an imperative approach (i.e., print out movements as side effects during program execution). Haskell favors a purely functional approach, where you would for example return a (lazy) list of movements from a to b via c:

```mw
hanoi :: Integer -> a -> a -> a -> [(a, a)]
hanoi 0 _ _ _ = []
hanoi n a b c = hanoi (n-1) a c b ++ [(a,b)] ++ hanoi (n-1) c b a
```

You can also do the above with one tail-recursion call:

```mw
hanoi :: Integer -> a -> a -> a -> [(a, a)]

hanoi n a b c = hanoiToList n a b c []
  where
    hanoiToList 0 _ _ _ l = l
    hanoiToList n a b c l = hanoiToList (n-1) a c b ((a, b) : hanoiToList (n-1) c b a l)
```

One can use this function to produce output, just like the other programs:

```mw
hanoiIO n = mapM_ f $ hanoi n 1 2 3 where
  f (x,y) = putStrLn $ "Move " ++ show x ++ " to " ++ show y
```

or, instead, one can of course also program imperatively, using the IO monad directly:

```mw
hanoiM :: Integer -> IO ()
hanoiM n = hanoiM' n 1 2 3 where
  hanoiM' 0 _ _ _ = return ()
  hanoiM' n a b c = do
    hanoiM' (n-1) a c b
    putStrLn $ "Move " ++ show a ++ " to " ++ show b
    hanoiM' (n-1) c b a
```

or, defining it as a monoid, and adding some output:

```mw
-------------------------- HANOI -------------------------

hanoi ::
  Int ->
  String ->
  String ->
  String ->
  [(String, String)]
hanoi 0 _ _ _ = mempty
hanoi n l r m =
  hanoi (n - 1) l m r
    <> [(l, r)]
    <> hanoi (n - 1) m r l

--------------------------- TEST -------------------------
main :: IO ()
main = putStrLn $ showHanoi 5

------------------------- DISPLAY ------------------------
showHanoi :: Int -> String
showHanoi n =
  unlines $
    fmap
      ( \(from, to) ->
          concat [justifyRight 5 ' ' from, " -> ", to]
      )
      (hanoi n "left" "right" "mid")

justifyRight :: Int -> Char -> String -> String
justifyRight n c = (drop . length) <*> (replicate n c <>)
```

**Output:**

```
 left -> right
 left -> mid
right -> mid
 left -> right
  mid -> left
  mid -> right
 left -> right
 left -> mid
right -> mid
right -> left
  mid -> left
right -> mid
 left -> right
 left -> mid
right -> mid
 left -> right
  mid -> left
  mid -> right
 left -> right
  mid -> left
right -> mid
right -> left
  mid -> left
  mid -> right
 left -> right
 left -> mid
right -> mid
 left -> right
  mid -> left
  mid -> right
 left -> right
```


## Hobbes

```mw
hanoi :: (int, [char], [char], [char]) -> ()
hanoi n from to via =
  if (n == 0) then
    ()
  else
    do {
      hanoi(n - 1, from, via, to);
      putStrLn("Move disk " ++ show(n) ++ " from " ++ from ++ " to " ++ to);
      hanoi(n - 1, via, to, from);
    }
```

**Output:**

```
> hanoi(3, "A", "C", "B")
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```


## HolyC

Translation of

:

C

```mw
U0 Move(U8 n, U8 from, U8 to, U8 via) {
  if (n > 0) {
    Move(n - 1, from, via, to);
    Print("Move disk from pole %d to pole %d\n", from, to);
    Move(n - 1, via, to, from);
  }
}

Move(4, 1, 2, 3);
```


## Icon and Unicon

The following is based on a solution in the Unicon book.

```mw
procedure main(arglist)
hanoi(arglist[1]) | stop("Usage: hanoi n\n\rWhere n is the number of disks to move.")
end

#procedure hanoi(n:integer, needle1:1, needle2:2)   # unicon shorthand for icon code 1,2,3 below

procedure hanoi(n, needle1, needle2)   #: solve towers of hanoi by moving  n disks from needle 1 to needle2 via other
local other

n := integer(0 < n) | runerr(n,101)       # 1 ensure integer (this also ensures it's positive too)
/needle1 := 1                             # 2 default
/needle2 := 2                             # 3 default

if n = 1 then
   write("Move disk from ", needle1, " to ", needle2)
else {
   other := 6 - needle1 - needle2         # clever but somewhat un-iconish way to find other
   hanoi(n-1, needle1, other)             
   write("Move disk from ", needle1, " to ", needle2)
   hanoi(n-1, other, needle2)            
}
return
end
```


## Imp77

```mw
%begin
  %routine do hanoi(%integer n, f, t, u)
    do hanoi(n - 1, f, u, t) %if n >= 2
    print string("Move disk from ".itos(f,0)." to ".itos(t,0).to string(nl))
    do hanoi(n - 1, u, t, f) %if n >= 2
  %end
  do hanoi(4, 1, 2, 3)
  print string("Towers of Hanoi puzzle completed!".to string(nl))
%end %of %program
```

**Output:**

```
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 2 to 1
Move disk from 2 to 3
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 3 to 1
Move disk from 2 to 1
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Towers of Hanoi puzzle completed!
```


## Inform 7

```mw
Hanoi is a room.

A post is a kind of supporter. A post is always fixed in place.

The left post, the middle post, and the right post are posts in Hanoi.

A disk is a kind of supporter.
The red disk is a disk on the left post.
The orange disk is a disk on the red disk.
The yellow disk is a disk on the orange disk.
The green disk is a disk on the yellow disk.

Definition: a disk is topmost if nothing is on it.

When play begins:
	move 4 disks from the left post to the right post via the middle post.

To move (N - number) disk/disks from (FP - post) to (TP - post) via (VP - post):
	if N > 0:
		move N - 1 disks from FP to VP via TP;
		say "Moving a disk from [FP] to [TP]...";
		let D be a random topmost disk enclosed by FP;
		if a topmost disk (called TD) is enclosed by TP, now D is on TD;
		otherwise now D is on TP;
		move N - 1 disks from VP to TP via FP.
```


## Io

```mw
hanoi := method(n, from, to, via,
  if (n == 1) then (
    writeln("Move from ", from, " to ", to)
  ) else (
    hanoi(n - 1, from, via, to  )
    hanoi(1    , from, to , via )
    hanoi(n - 1, via , to , from)
  )
)
```


## Ioke

```mw
 = method(n, f, u, t,
  if(n < 2,
    "#{f} --> #{t}" println,

    H(n - 1, f, t, u)
    "#{f} --> #{t}" println
    H(n - 1, u, f, t)
  )
)

hanoi = method(n,
  H(n, 1, 2, 3)
)
```


## J

**Solutions**

```mw
H =: i.@,&2 ` (({&0 2 1,0 2,{&1 0 2)@$:@<:) @. *    NB. tacit using anonymous recursion
```

**Example use:**

```mw
   H 3
0 2
0 1
2 1
0 2
1 2
1 0
2 0
```

The result is a 2-column table; a row i,j is interpreted as: move a disk (the top disk) from peg i to peg j . Or, using explicit rather than implicit code:

```mw
H1=: monad define                                   NB. explicit equivalent of H
  if. y do.
    ({&0 2 1 , 0 2 , {&1 0 2) H1 y-1
  else.
    i.0 2
  end.
)
```

The usage here is the same:

```
   H1 2
0 1
0 2
1 2
```

**Alternative solution**

If a textual display is desired, similar to some of the other solutions here (counting from 1 instead of 0, tracking which disk is on the top of the stack, and of course formatting the result for a human reader instead of providing a numeric result):

```mw
hanoi=: monad define
  moves=. H y
  disks=.  $~` ((],[,]) $:@<:) @.* y
  ('move disk ';' from peg ';' to peg ');@,."1 ":&.>disks,.1+moves
)
```

**Demonstration:**

```mw
   hanoi 3
move disk 1 from peg 1 to peg 3
move disk 2 from peg 1 to peg 2
move disk 1 from peg 3 to peg 2
move disk 3 from peg 1 to peg 3
move disk 1 from peg 2 to peg 1
move disk 2 from peg 2 to peg 3
move disk 1 from peg 1 to peg 3
```


## Java

```mw
public void move(int n, int from, int to, int via) {
  if (n == 1) {
    System.out.println("Move disk from pole " + from + " to pole " + to);
  } else {
    move(n - 1, from, via, to);
    move(1, from, to, via);
    move(n - 1, via, to, from);
  }
}
```

Where n is the number of disks to move and from, to, and via are the poles.

**Example use:**

```mw
move(3, 1, 2, 3);
```

**Output:**

```mw
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
```


## JavaScript

### ES5

```mw
function move(n, a, b, c) {
  if (n > 0) {
    move(n-1, a, c, b);
    console.log("Move disk from " + a + " to " + c);
    move(n-1, b, a, c);
  }
}
move(4, "A", "B", "C");
```

Or, as a functional expression, rather than a statement with side effects:

```mw
(function () {

    // hanoi :: Int -> String -> String -> String -> [[String, String]]
    function hanoi(n, a, b, c) {
        return n ? hanoi(n - 1, a, c, b)
            .concat([
                [a, b]
            ])
            .concat(hanoi(n - 1, c, b, a)) : [];
    }

    return hanoi(3, 'left', 'right', 'mid')
        .map(function (d) {
            return d[0] + ' -> ' + d[1];
        });
})();
```

**Output:**

```mw
["left -> right", "left -> mid",
 "right -> mid", "left -> right", 
 "mid -> left", "mid -> right", 
 "left -> right"]
```

### ES6

```mw
(() => {
    "use strict";

    // ----------------- TOWERS OF HANOI -----------------

    // hanoi :: Int -> String -> String ->
    // String -> [[String, String]]
    const hanoi = n =>
        (a, b, c) => {
            const go = hanoi(n - 1);

            return n
                ? [
                    ...go(a, c, b),
                    [a, b],
                    ...go(c, b, a)
                ]
                : [];
        };

    // ---------------------- TEST -----------------------
    return hanoi(3)("left", "right", "mid")
    .map(d => `${d[0]} -> ${d[1]}`)
    .join("\n");
})();
```

**Output:**

```
left -> right
left -> mid
right -> mid
left -> right
mid -> left
mid -> right
left -> right
```


## Joy

```mw
DEFINE hanoi == [[rolldown] infra] dip 
[[[null] [pop pop] ] 
 [[dup2 [[rotate] infra] dip pred] 
 [[dup rest put] dip 
  [[swap] infra] dip pred] 
 []]] 
condnestrec.
```

Using it (5 is the number of disks.)

```mw
[source destination temp] 5 hanoi.
```


## jq

Works with

:

jq

version 1.4

The algorithm used here is used elsewhere on this page but it is worthwhile pointing out that it can also be read as a proof that:

(a) move(n;"A";"B";"C") will logically succeed for n>=0; and

(b) move(n;"A";"B";"C") will generate the sequence of moves, assuming sufficient computing resources.

The proof of (a) is by induction:

- As explained in the comments, the algorithm establishes that move(n;x;y;z) is possible for all n>=0 and distinct x,y,z if move(n-1;x;y;z)) is possible;
- Since move(0;x;y;z) evidently succeeds, (a) is established by induction.

The truth of (b) follows from the fact that the algorithm emits an instruction of what to do when moving a single disk.

```mw
# n is the number of disks to move from From to To
def move(n; From; To; Via):
  if n > 0 then
     # move all but the largest at From to Via (according to the rules):
     move(n-1; From; Via; To),
     # ... so the largest disk at From is now free to move to its final destination:
     "Move disk from \(From) to \(To)",
     # Move the remaining disks at Via to To:
     move(n-1; Via; To; From)
  else empty
  end;
```

**Example**:

```
move(5; "A"; "B"; "C")
```


## Jsish

From Javascript ES5 entry.

```mw
/* Towers of Hanoi, in Jsish */

function move(n, a, b, c) {
  if (n > 0) {
    move(n-1, a, c, b);
    puts("Move disk from " + a + " to " + c);
    move(n-1, b, a, c);
  }
}

if (Interp.conf('unitTest')) move(4, "A", "B", "C");

/*
=!EXPECTSTART!=
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from A to B
Move disk from C to A
Move disk from C to B
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from B to A
Move disk from C to A
Move disk from B to C
Move disk from A to B
Move disk from A to C
Move disk from B to C
=!EXPECTEND!=
*/
```

**Output:**

```
prompt$ jsish -u towersOfHanoi.jsi
[PASS] towersOfHanoi.jsi
```


## Julia

Translation of

:

R

```mw
function solve(n::Integer, from::Integer, to::Integer, via::Integer)
  if n == 1
    println("Move disk from $from to $to")
  else
    solve(n - 1, from, via, to)
    solve(1, from, to, via)
    solve(n - 1, via, to, from)
  end
end

solve(4, 1, 2, 3)
```

**Output:**

```
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 2 to 1
Move disk from 2 to 3
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 3 to 1
Move disk from 2 to 1
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
```


## K

```mw
   h:{[n;a;b;c]if[n>0;_f[n-1;a;c;b];`0:,//$($n,":",$a,"->",$b,"\n");_f[n-1;c;b;a]]}
   h[4;1;2;3]
1:1->3
2:1->2
1:3->2
3:1->3
1:2->1
2:2->3
1:1->3
4:1->2
1:3->2
2:3->1
1:2->1
3:3->2
1:1->3
2:1->2
1:3->2
```

The disk to move in the i'th step is the same as the position of the leftmost 1 in the binary representation of 1..2^n.

```mw
   s:();{[n;a;b;c]if[n>0;_f[n-1;a;c;b];s,:n;_f[n-1;c;b;a]]}[4;1;2;3];s
1 2 1 3 1 2 1 4 1 2 1 3 1 2 1

   1_{*1+&|x}'a:(2_vs!_2^4)
1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
```


## Klingphix

Translation of

:

MiniScript

```mw
include ..\Utilitys.tlhy

:moveDisc %B !B %C !C %A !A %n !n { n A C B }
    $n [
        $n 1 - $A $B $C moveDisc
        ( "Move disc " $n " from pole " $A " to pole " $C ) lprint nl
        $n 1 - $B $C $A moveDisc
    ] if
;
 
{ Move disc 3 from pole 1 to pole 3, with pole 2 as spare }
3 1 3 2 moveDisc

" " input
```

**Output:**

```
Move disc 1 from pole 1 to pole 3
Move disc 2 from pole 1 to pole 2
Move disc 1 from pole 3 to pole 2
Move disc 3 from pole 1 to pole 3
Move disc 1 from pole 2 to pole 1
Move disc 2 from pole 2 to pole 3
Move disc 1 from pole 1 to pole 3
```


## Kotlin

```mw
// version 1.1.0

class Hanoi(disks: Int) {
    private var moves = 0

    init {
        println("Towers of Hanoi with $disks disks:\n")
        move(disks, 'L', 'C', 'R')
        println("\nCompleted in $moves moves\n")
    }

    private fun move(n: Int, from: Char, to: Char, via: Char) {
        if (n > 0) {
            move(n - 1, from, via, to)
            moves++
            println("Move disk $n from $from to $to")
            move(n - 1, via, to, from)
        }
    }
}

fun main(args: Array<String>) {
    Hanoi(3)
    Hanoi(4)
}
```

**Output:**

```
Towers of Hanoi with 3 disks:

Move disk 1 from L to C
Move disk 2 from L to R
Move disk 1 from C to R
Move disk 3 from L to C
Move disk 1 from R to L
Move disk 2 from R to C
Move disk 1 from L to C

Completed in 7 moves

Towers of Hanoi with 4 disks:

Move disk 1 from L to R
Move disk 2 from L to C
Move disk 1 from R to C
Move disk 3 from L to R
Move disk 1 from C to L
Move disk 2 from C to R
Move disk 1 from L to R
Move disk 4 from L to C
Move disk 1 from R to C
Move disk 2 from R to L
Move disk 1 from C to L
Move disk 3 from R to C
Move disk 1 from L to R
Move disk 2 from L to C
Move disk 1 from R to C

Completed in 15 moves
```


## Lambdatalk

```mw
PSEUDO-CODE:

hanoi disks from A to B via C
  if no disks
  then stop
  else hanoi upper disks from A to C via B
       move  lower disk  from A to B 
       hanoi upper disks from C to B via A

CODE:

{def hanoi          
 {lambda {:disks :a :b :c}
  {if {A.empty? :disks} 
   then
   else {hanoi {A.rest :disks} :a :c :b}
        {div > move {A.first :disks} from :a to :b}
        {hanoi {A.rest :disks} :c :b :a} }}} 
-> hanoi

{hanoi {A.new ==== === == =} A B C}  
->  
> move = from A to C  
> move == from A to B  
> move = from C to B  
> move === from A to C  
> move = from B to A  
> move == from B to C  
> move = from A to C  
> move ==== from A to B  
> move = from C to B  
> move == from C to A  
> move = from B to A  
> move === from C to B  
> move = from A to C  
> move == from A to B  
> move = from C to B
```


## Lasso

```mw
#!/usr/bin/lasso9

define towermove(
	disks::integer,
	a,b,c
) => {
	if(#disks > 0) => {
		towermove(#disks - 1, #a, #c, #b )
		stdoutnl("Move disk from " + #a + " to " + #c)
		towermove(#disks - 1, #b, #a, #c )
	}
}

towermove((integer($argv -> second || 3)), "A", "B", "C")
```

Called from command line:

```mw
./towers
```

**Output:**

```
Move disk from A to C
Move disk from A to B
Move disk from C to B
Move disk from A to C
Move disk from B to A
Move disk from B to C
Move disk from A to C
```

Called from command line:

```mw
./towers 4
```

**Output:**

```
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from A to B
Move disk from C to A
Move disk from C to B
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from B to A
Move disk from C to A
Move disk from B to C
Move disk from A to B
Move disk from A to C
Move disk from B to C
```


## Liberty BASIC

This looks much better with a GUI interface.

```mw
   source$ ="A"
    via$    ="B"
    target$ ="C"

    call hanoi 4, source$, target$, via$        '   ie call procedure to move legally 4 disks from peg A to peg C via peg B

    wait

    sub hanoi numDisks, source$, target$, via$
        if numDisks =0 then
            exit sub
        else
            call hanoi numDisks -1, source$, via$, target$
            print " Move disk "; numDisks; " from peg "; source$; " to peg "; target$
            call hanoi numDisks -1, via$, target$, source$
        end if
    end sub

    end
```


## Lingo

```mw
on hanoi (n, a, b, c)
  if n > 0 then
    hanoi(n-1, a, c, b)
    put "Move disk from" && a && "to" && c
    hanoi(n-1, b, a, c)
  end if
end
```

```mw
hanoi(3, "A", "B", "C")
-- "Move disk from A to C"
-- "Move disk from A to B"
-- "Move disk from C to B"
-- "Move disk from A to C"
-- "Move disk from B to A"
-- "Move disk from B to C"
-- "Move disk from A to C"
```


## Logo

```mw
to move :n :from :to :via
  if :n = 0 [stop]
  move :n-1 :from :via :to
  (print [Move disk from] :from [to] :to)
  move :n-1 :via :to :from
end
move 4 "left "middle "right
```


## Logtalk

```mw
:- object(hanoi).

    :- public(run/1).
    :- mode(run(+integer), one).
    :- info(run/1, [
        comment is 'Solves the towers of Hanoi problem for the specified number of disks.',
        argnames is ['Disks']]).

    run(Disks) :-
        move(Disks, left, middle, right).

    move(1, Left, _, Right):-
        !,
        report(Left, Right).
    move(Disks, Left, Aux, Right):-
        Disks2 is Disks - 1,
        move(Disks2, Left, Right, Aux),
        report(Left, Right),
        move(Disks2, Aux, Left, Right).

    report(Pole1, Pole2):-
        write('Move a disk from '),
        writeq(Pole1),
        write(' to '),
        writeq(Pole2),
        write('.'),
        nl.

:- end_object.
```


## LOLCODE

```mw
HAI 1.2
 
HOW IZ I HANOI YR N AN YR SRC AN YR DST AN YR VIA
    BTW VISIBLE SMOOSH "HANOI N=" N " SRC=" SRC " DST=" DST " VIA=" VIA MKAY
    BOTH SAEM N AN 0, O RLY?
        YA RLY
            BTW VISIBLE "Done."
            GTFO
        NO WAI
            I HAS A LOWER ITZ DIFF OF N AN 1
            I IZ HANOI YR LOWER AN YR SRC AN YR VIA AN YR DST MKAY
            VISIBLE SMOOSH "Move disc " N " from " SRC " to " DST MKAY
            I IZ HANOI YR LOWER AN YR VIA AN YR DST AN YR SRC MKAY
    OIC
IF U SAY SO
 
I IZ HANOI YR 4 AN YR 1 AN YR 2 AN YR 3  MKAY
 
KTHXBYE
```


## Lua

```mw
function move(n, src, dst, via)
    if n > 0 then
        move(n - 1, src, via, dst)
        print(src, 'to', dst)
        move(n - 1, via, dst, src)
    end
end

move(4, 1, 2, 3)
```

More informative version

```mw
function move(n, src, via, dst)
    if n > 0 then
        move(n - 1, src, dst, via)
        print('Disk ',n,' from ' ,src, 'to', dst)
        move(n - 1, via, src, dst)
        
    end
end
 
move(4, 1, 2, 3)
```

### Hanoi Iterative

```mw
#!/usr/bin/env luajit
local function printf(fmt, ...) io.write(string.format(fmt, ...)) end
local runs=0
local function move(tower, from, to)
	if #tower[from]==0 
		or (#tower[to]>0 
		and tower[from][#tower[from]]>tower[to][#tower[to]]) then
			to,from=from,to
	end
	if #tower[from]>0 then
		tower[to][#tower[to]+1]=tower[from][#tower[from]]
		tower[from][#tower[from]]=nil

		io.write(tower[to][#tower[to]],":",from, "→", to, " ")
	end
end

local function hanoi(n)
	local src,dst,via={},{},{}
	local tower={src,dst,via}
	for i=1,n do src[i]=n-i+1 end
	local one,nxt,lst
	if n%2==1 then -- odd
		one,nxt,lst=1,2,3
	else
		one,nxt,lst=1,3,2
	end
	--repeat
	::loop::
		move(tower, one, nxt)
		if #dst==n then return end
		move(tower, one, lst)
		one,nxt,lst=nxt,lst,one
	goto loop
	--until false
end

local num=arg[1] and tonumber(arg[1]) or 4

hanoi(num)
```

**Output:**

```
> ./hanoi_iter.lua 5
1:1→2 2:1→3 1:2→3 3:1→2 1:3→1 2:3→2 1:1→2 4:1→3 1:2→3 2:2→1 1:3→1 3:2→3 1:1→2 2:1→3 1:2→3 5:1→2 1:3→1 2:3→2 1:1→2 3:3→1 1:2→3 2:2→1 1:3→1 4:3→2 1:1→2 2:1→3 1:2→3 3:1→2 1:3→1 2:3→2 1:1→2
```

### Hanoi Bitwise Fast

```mw
#!/usr/bin/env luajit
-- binary solution
local bit=require"bit"
local band,bor=bit.band,bit.bor
local function hanoi(n)
	local even=(n-1)%2
	for m=1,2^n-1 do
		io.write(m,":",band(m,m-1)%3+1, "→", (bor(m,m-1)+1)%3+1, " ")
	end
end

local num=arg[1] and tonumber(arg[1]) or 4

hanoi(num)
```

**Output:**

```
> ./hanoi_bit.lua 4
1:1→3 2:1→2 3:3→2 4:1→3 5:2→1 6:2→3 7:1→3 8:1→2 9:3→2 10:3→1 11:2→1 12:3→2 13:1→3 14:1→2 15:3→2 
> time ./hanoi_bit.lua 30 >/dev/null  ; on AMD FX-8350 @ 4 GHz
./hanoi_bit.lua 30 > /dev/null  297,40s user 1,39s system 99% cpu 4:59,01 total
```


## M2000 Interpreter

Translation of

:

FreeBasic

```mw
Module Hanoi {
      Rem HANOI TOWERS
      Print "Three disks" : Print
      move(3, 1, 2, 3)
      Print 
      Print "Four disks" : Print
      move(4, 1, 2, 3)
      
      
      Sub move(n, from, to, via)
            If n <=0 Then Exit Sub
            move(n - 1, from, via, to)
            Print "Move disk"; n; " from pole"; from; " to pole"; to
            move(n - 1, via, to, from)
      End Sub
}
Hanoi
```

**Output:**

same as in FreeBasic


## MACRO-11

```mw
        .TITLE  HANOI
        .MCALL  .PRINT,.EXIT
HANOI:: MOV     #4,R2
        MOV     #61,R3
        MOV     #62,R4
        MOV     #63,R5
        JSR     PC,MOVE
        .EXIT
MOVE:   DEC     R2
        BLT     1$
        MOV     R2,-(SP)
        MOV     R3,-(SP)
        MOV     R4,-(SP)
        MOV     R5,-(SP)
        MOV     R5,R0
        MOV     R4,R5
        MOV     R0,R4
        JSR     PC,MOVE
        MOV     (SP)+,R5
        MOV     (SP)+,R4
        MOV     (SP)+,R3
        MOV     (SP)+,R2
        MOVB    R3,3$
        MOVB    R4,4$
        .PRINT  #2$
        MOV     R3,R0
        MOV     R4,R3
        MOV     R5,R4
        MOV     R0,R5
        BR      MOVE
1$:     RTS     PC
2$:     .ASCII  /MOVE DISK FROM PEG /
3$:     .ASCII  /* TO PEG /
4$:     .ASCIZ  /*/
        .EVEN
        .END    HANOI
```

**Output:**

```
MOVE DISK FROM PEG 1 TO PEG 3
MOVE DISK FROM PEG 1 TO PEG 2
MOVE DISK FROM PEG 2 TO PEG 3
MOVE DISK FROM PEG 1 TO PEG 3
MOVE DISK FROM PEG 3 TO PEG 1
MOVE DISK FROM PEG 3 TO PEG 2
MOVE DISK FROM PEG 2 TO PEG 1
MOVE DISK FROM PEG 1 TO PEG 2
MOVE DISK FROM PEG 2 TO PEG 3
MOVE DISK FROM PEG 2 TO PEG 1
MOVE DISK FROM PEG 1 TO PEG 3
MOVE DISK FROM PEG 2 TO PEG 3
MOVE DISK FROM PEG 3 TO PEG 2
MOVE DISK FROM PEG 3 TO PEG 1
MOVE DISK FROM PEG 1 TO PEG 2
```


## MAD

```mw
            NORMAL MODE IS INTEGER
            DIMENSION LIST(100)
            SET LIST TO LIST
            
            VECTOR VALUES MOVFMT = 
          0  $20HMOVE DISK FROM POLE ,I1,S1,8HTO POLE ,I1*$
           
            INTERNAL FUNCTION(DUMMY)
            ENTRY TO MOVE.
LOOP        NUM = NUM - 1
            WHENEVER NUM.E.0
                PRINT FORMAT MOVFMT,FROM,DEST
            OTHERWISE
                SAVE RETURN
                SAVE DATA NUM,FROM,VIA,DEST
                TEMP=DEST
                DEST=VIA
                VIA=TEMP
                MOVE.(0)
                RESTORE DATA NUM,FROM,VIA,DEST
                RESTORE RETURN
                PRINT FORMAT MOVFMT,FROM,DEST
                TEMP=FROM
                FROM=VIA
                VIA=TEMP
                TRANSFER TO LOOP
            END OF CONDITIONAL
            FUNCTION RETURN
            END OF FUNCTION
            
            NUM  = 4
            FROM = 1
            VIA  = 2
            DEST = 3
            MOVE.(0)
            
            END OF PROGRAM
```

**Output:**

```
MOVE DISK FROM POLE 1 TO POLE 2
MOVE DISK FROM POLE 1 TO POLE 3
MOVE DISK FROM POLE 2 TO POLE 3
MOVE DISK FROM POLE 1 TO POLE 2
MOVE DISK FROM POLE 3 TO POLE 1
MOVE DISK FROM POLE 3 TO POLE 2
MOVE DISK FROM POLE 1 TO POLE 2
MOVE DISK FROM POLE 1 TO POLE 3
MOVE DISK FROM POLE 2 TO POLE 3
MOVE DISK FROM POLE 2 TO POLE 1
MOVE DISK FROM POLE 3 TO POLE 1
MOVE DISK FROM POLE 2 TO POLE 3
MOVE DISK FROM POLE 1 TO POLE 2
MOVE DISK FROM POLE 1 TO POLE 3
MOVE DISK FROM POLE 2 TO POLE 3
```


## Maple

```mw
Hanoi := proc(n::posint,a,b,c)
   if n = 1 then
       printf("Move disk from tower %a to tower %a.\n",a,c);
   else
       Hanoi(n-1,a,c,b);
       Hanoi(1,a,b,c);
       Hanoi(n-1,b,a,c);
    fi;
end:

printf("Moving 2 disks from tower A to tower C using tower B.\n");
Hanoi(2,A,B,C);
```

**Output:**

Moving 2 disks from tower A to tower C using tower B.

Move disk from tower A to tower B.

Move disk from tower A to tower C.

Move disk from tower B to tower C.


## Mathematica /Wolfram Language

```mw
Hanoi[0, from_, to_, via_] := Null  
Hanoi[n_Integer, from_, to_, via_] := (Hanoi[n-1, from, via, to];Print["Move disk from pole ", from, " to ", to, "."];Hanoi[n-1, via, to, from])
```


## MATLAB

This is a direct translation from the Python example given in the Wikipedia entry for the Tower of Hanoi puzzle.

```mw
function towerOfHanoi(n,A,C,B)
    if (n~=0)
        towerOfHanoi(n-1,A,B,C);
        disp(sprintf('Move plate %d from tower %d to tower %d',[n A C]));
        towerOfHanoi(n-1,B,C,A);
    end
end
```

**Sample output:**

```
towerOfHanoi(3,1,3,2)
Move plate 1 from tower 1 to tower 3
Move plate 2 from tower 1 to tower 2
Move plate 1 from tower 3 to tower 2
Move plate 3 from tower 1 to tower 3
Move plate 1 from tower 2 to tower 1
Move plate 2 from tower 2 to tower 3
Move plate 1 from tower 1 to tower 3
```


## Maxima

```mw
hanoi(n, a, b, c) := block(
if(n=1) then print(sconcat("peg ", a, " to peg ", b))
else block(
    hanoi(n-1, a, c, b),
    hanoi(1, a, b, c),
    hanoi(n-1, c, b, a)))$

hanoi(4,1,2,3)$
```

**Output:**

```
peg 1 to peg 3
peg 1 to peg 2
peg 3 to peg 2
peg 1 to peg 3
peg 2 to peg 1
peg 2 to peg 3
peg 1 to peg 3
peg 1 to peg 2
peg 3 to peg 2
peg 3 to peg 1
peg 2 to peg 1
peg 3 to peg 2
peg 1 to peg 3
peg 1 to peg 2
peg 3 to peg 2
```


## MiniScript

```mw
moveDisc = function(n, A, C, B)
    if n == 0 then return
    moveDisc n-1, A, B, C
    print "Move disc " + n + " from pole " + A + " to pole " + C
    moveDisc n-1, B, C, A
end function

// Move disc 3 from pole 1 to pole 3, with pole 2 as spare
moveDisc 3, 1, 3, 2
```

**Output:**

```
Move disc 1 from pole 1 to pole 3
Move disc 2 from pole 1 to pole 2
Move disc 1 from pole 3 to pole 2
Move disc 3 from pole 1 to pole 3
Move disc 1 from pole 2 to pole 1
Move disc 2 from pole 2 to pole 3
Move disc 1 from pole 1 to pole 3
```


## Miranda

```mw
main :: [sys_message]
main = [Stdout (lay (map showmove (move 4 1 2 3)))]

showmove :: (num,num)->[char]
showmove (src,dest)
    = "Move disk from pole " ++ show src ++ " to pole " ++ show dest

move :: num->*->*->*->[(*,*)]
move n src via dest
    = [], if n=0
    = left ++ [(src,dest)] ++ right, otherwise
      where left  = move (n-1) src dest via
            right = move (n-1) via src dest
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## MIPS Assembly

```mw
# Towers of Hanoi
# MIPS assembly implementation (tested with MARS)
# Source: https://stackoverflow.com/questions/50382420/hanoi-towers-recursive-solution-using-mips/50383530#50383530

.data
prompt: .asciiz "Enter a number: "
part1: .asciiz "\nMove disk "
part2: .asciiz " from rod "
part3: .asciiz " to rod "

.text
.globl main
main:
    li $v0,  4          # print string
    la $a0,  prompt
    syscall
    li $v0,  5          # read integer
    syscall

    # parameters for the routine
    add $a0, $v0, $zero # move to $a0
    li $a1, 'A'
    li $a2, 'B'
    li $a3, 'C'

    jal hanoi           # call hanoi routine

    li $v0, 10          # exit
    syscall

hanoi:

    #save in stack
    addi $sp, $sp, -20 
    sw   $ra, 0($sp)
    sw   $s0, 4($sp)
    sw   $s1, 8($sp)
    sw   $s2, 12($sp)
    sw   $s3, 16($sp)

    add $s0, $a0, $zero
    add $s1, $a1, $zero
    add $s2, $a2, $zero
    add $s3, $a3, $zero

    addi $t1, $zero, 1
    beq $s0, $t1, output

    recur1:

        addi $a0, $s0, -1
        add $a1, $s1, $zero
        add $a2, $s3, $zero
        add $a3, $s2, $zero
        jal hanoi

        j output

    recur2:

        addi $a0, $s0, -1
        add $a1, $s3, $zero
        add $a2, $s2, $zero
        add $a3, $s1, $zero
        jal hanoi

    exithanoi:

        lw   $ra, 0($sp)        # restore registers from stack
        lw   $s0, 4($sp)
        lw   $s1, 8($sp)
        lw   $s2, 12($sp)
        lw   $s3, 16($sp)

        addi $sp, $sp, 20       # restore stack pointer

        jr $ra

    output:

        li $v0,  4              # print string
        la $a0,  part1
        syscall
        li $v0,  1              # print integer
        add $a0, $s0, $zero
        syscall
        li $v0,  4              # print string
        la $a0,  part2
        syscall
        li $v0,  11             # print character
        add $a0, $s1, $zero
        syscall
        li $v0,  4              # print string
        la $a0,  part3
        syscall
        li $v0,  11             # print character
        add $a0, $s2, $zero
        syscall

        beq $s0, $t1, exithanoi
        j recur2
```


## МК-61/52

```mw
^	2	x^y	П0	<->	2	/	{x}	x#0	16
3	П3	2	П2	БП	20	3	П2	2	П3
1	П1	ПП	25	КППB	ПП	28	КППA	ПП	31
КППB	ПП	34	КППA	ИП1	ИП3	КППC	ИП1	ИП2	КППC
ИП3	ИП2	КППC	ИП1	ИП3	КППC	ИП2	ИП1	КППC	ИП2
ИП3	КППC	ИП1	ИП3	КППC	В/О	ИП1	ИП2	БП	62
ИП2	ИП1	КППC	ИП1	ИП2	ИП3	П1	->	П3	->
П2	В/О	1	0	/	+	С/П	КИП0	ИП0	x=0
89	3	3	1	ИНВ	^	ВП	2	С/П	В/О
```

Instruction: РA = 56; РB = 60; РC = 72; N В/О С/П, where 2 <= N <= 7.


## Modula-2

```mw
MODULE Towers;
FROM FormatString IMPORT FormatString;
FROM Terminal IMPORT WriteString,ReadChar;

PROCEDURE Move(n,from,to,via : INTEGER);
VAR buf : ARRAY[0..63] OF CHAR;
BEGIN
    IF n>0 THEN
        Move(n-1, from, via, to);
        FormatString("Move disk %i from pole %i to pole %i\n", buf, n, from, to);
        WriteString(buf);
        Move(n-1, via, to, from)
    END
END Move;

BEGIN
    Move(3, 1, 3, 2);

    ReadChar
END Towers.
```


## Modula-3

```mw
MODULE Hanoi EXPORTS Main;

FROM IO IMPORT Put;
FROM Fmt IMPORT Int;

PROCEDURE doHanoi(n, from, to, using: INTEGER) =
  BEGIN
    IF n > 0 THEN
      doHanoi(n - 1, from, using, to);
      Put("move " & Int(from) & " --> " & Int(to) & "\n");
      doHanoi(n - 1, using, to, from);
    END;
  END doHanoi;

BEGIN
  doHanoi(4, 1, 2, 3);
END Hanoi.
```


## Monte

```mw
def move(n, fromPeg, toPeg, viaPeg):
    if (n > 0):
        move(n.previous(), fromPeg, viaPeg, toPeg)
        traceln(`Move disk $n from $fromPeg to $toPeg`)
        move(n.previous(), viaPeg, toPeg, fromPeg)

move(3, "left", "right", "middle")
```


## MoonScript

```mw
hanoi = (n, src, dest, via) ->
  if n > 1
    hanoi n-1, src, via, dest
  print "#{src} -> #{dest}"
  if n > 1
    hanoi n-1, via, dest, src

hanoi 4,1,3,2
```

**Output:**

```
1 -> 2
1 -> 3
2 -> 3
1 -> 2
3 -> 1
3 -> 2
1 -> 2
1 -> 3
2 -> 3
2 -> 1
3 -> 1
2 -> 3
1 -> 2
1 -> 3
2 -> 3
```


## Nemerle

```mw
using System; 
using System.Console;

module Towers
{
    Hanoi(n : int, from = 1, to = 3, via = 2) : void
    {
        when (n > 0)
        {
            Hanoi(n - 1, from, via, to);
            WriteLine("Move disk from peg {0} to peg {1}", from, to);
            Hanoi(n - 1, via, to, from);
        }
    }
    
    Main() : void
    {
        Hanoi(4)
    } 
}
```


## NetRexx

```mw
/* NetRexx */
options replace format comments java crossref symbols binary

runSample(arg)
return

-- 09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)~~
method runSample(arg) private static
  parse arg discs .
  if discs = '', discs < 1 then discs = 4
  say 'Minimum moves to solution:' 2 ** discs - 1
  moves = move(discs)
  say 'Solved in' moves 'moves.'
  return

-- 09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)09:02, 27 August 2022 (UTC)~~
method move(discs = int 4, towerFrom = int 1, towerTo = int 2, towerVia = int 3, moves = int 0) public static
  if discs == 1 then do
    moves = moves + 1
    say 'Move disc from peg' towerFrom 'to peg' towerTo '- Move No:' Rexx(moves).right(5)
    end
  else do
    moves = move(discs - 1, towerFrom, towerVia, towerTo, moves)
    moves = move(1, towerFrom, towerTo, towerVia, moves)
    moves = move(discs - 1, towerVia, towerTo, towerFrom, moves)
    end
  return moves
```

**Output:**

```
Minimum moves to solution: 15
Move disc from peg 1 to peg 3 - Move No:     1
Move disc from peg 1 to peg 2 - Move No:     2
Move disc from peg 3 to peg 2 - Move No:     3
Move disc from peg 1 to peg 3 - Move No:     4
Move disc from peg 2 to peg 1 - Move No:     5
Move disc from peg 2 to peg 3 - Move No:     6
Move disc from peg 1 to peg 3 - Move No:     7
Move disc from peg 1 to peg 2 - Move No:     8
Move disc from peg 3 to peg 2 - Move No:     9
Move disc from peg 3 to peg 1 - Move No:    10
Move disc from peg 2 to peg 1 - Move No:    11
Move disc from peg 3 to peg 2 - Move No:    12
Move disc from peg 1 to peg 3 - Move No:    13
Move disc from peg 1 to peg 2 - Move No:    14
Move disc from peg 3 to peg 2 - Move No:    15
Solved in 15 moves.
```


## NewLISP

```mw
(define (move n from to via)
			(if (> n 0) 
				(move (- n 1) from via to
				(print "move disk from pole " from " to pole " to "\n")
				(move (- n 1) via to from))))

(move 4 1 2 3)
```


## Nim

```mw
proc hanoi(disks: int; fromTower, toTower, viaTower: string) =
  if disks != 0:
    hanoi(disks - 1, fromTower, viaTower, toTower)
    echo("Move disk ", disks, " from ", fromTower, " to ", toTower)
    hanoi(disks - 1, viaTower, toTower, fromTower)
    
hanoi(4, "1", "2", "3")
```

**Output:**

```
Move disk 1 from 1 to 3
Move disk 2 from 1 to 2
Move disk 1 from 3 to 2
Move disk 3 from 1 to 3
Move disk 1 from 2 to 1
Move disk 2 from 2 to 3
Move disk 1 from 1 to 3
Move disk 4 from 1 to 2
Move disk 1 from 3 to 2
Move disk 2 from 3 to 1
Move disk 1 from 2 to 1
Move disk 3 from 3 to 2
Move disk 1 from 1 to 3
Move disk 2 from 1 to 2
Move disk 1 from 3 to 2
```


## Oberon-2

Translation of

:

C

```mw
MODULE Hanoi;

  IMPORT Out;

  PROCEDURE Move(n,from,via,to:INTEGER);
  BEGIN
    IF n > 1 THEN
      Move(n-1,from,to,via);
      Out.String("Move disk from pole ");
      Out.Int(from,0);
      Out.String(" to pole ");
      Out.Int(to,0);
      Out.Ln;
      Move(n-1,via,from,to);
    ELSE
      Out.String("Move disk from pole ");
      Out.Int(from,0);
      Out.String(" to pole ");
      Out.Int(to,0);
      Out.Ln;
    END;
  END Move;
  
BEGIN
  Move(4,1,2,3);
END Hanoi.
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## Objeck

```mw
class Hanoi {
  function : Main(args : String[]) ~ Nil {
    Move(4, 1, 2, 3);
  }

  function: Move(n:Int, f:Int, t:Int, v:Int) ~ Nil {
    if(n = 1) {
      "Move disk from pole {$f} to pole {$t}"->PrintLine();
    }
    else {
      Move(n - 1, f, v, t);
      Move(1, f, t, v);
      Move(n - 1, v, t, f);
    };
  }
}
```


## Objective-C

From here

Works with

:

GNUstep

It should be compatible with XCode/Cocoa on MacOS too.

The Interface - TowersOfHanoi.h:

```mw
#import <Foundation/NSObject.h>

@interface TowersOfHanoi: NSObject {
	int pegFrom;
	int pegTo;
	int pegVia;
	int numDisks;
}

-(void) setPegFrom: (int) from andSetPegTo: (int) to andSetPegVia: (int) via andSetNumDisks: (int) disks;
-(void) movePegFrom: (int) from andMovePegTo: (int) to andMovePegVia: (int) via andWithNumDisks: (int) disks;
@end
```

The Implementation - TowersOfHanoi.m:

```mw
#import "TowersOfHanoi.h"
@implementation TowersOfHanoi

-(void) setPegFrom: (int) from andSetPegTo: (int) to andSetPegVia: (int) via andSetNumDisks: (int) disks {
	pegFrom = from;
	pegTo = to;
	pegVia = via;
	numDisks = disks;
}

-(void) movePegFrom: (int) from andMovePegTo: (int) to andMovePegVia: (int) via andWithNumDisks: (int) disks {
	if (disks == 1) {
            printf("Move disk from pole %i to pole %i\n", from, to);
        } else {
 			[self movePegFrom: from andMovePegTo: via andMovePegVia: to andWithNumDisks: disks-1];
			[self movePegFrom: from andMovePegTo: to andMovePegVia: via andWithNumDisks: 1];
			[self movePegFrom: via andMovePegTo: to andMovePegVia: from andWithNumDisks: disks-1];
        }
}

@end
```

Test code: TowersTest.m:

```mw
#import <stdio.h>
#import "TowersOfHanoi.h"

int main( int argc, const char *argv[] ) {
	@autoreleasepool {

		TowersOfHanoi *tower = [[TowersOfHanoi alloc] init];

		int from = 1;
		int to = 3;
		int via = 2;
		int disks = 3;

		[tower setPegFrom: from andSetPegTo: to andSetPegVia: via andSetNumDisks: disks];

		[tower movePegFrom: from andMovePegTo: to andMovePegVia: via andWithNumDisks: disks];

	}
	return 0;
}
```


## OCaml

```mw
let rec hanoi n a b c =
  if n <> 0 then begin
    hanoi (pred n) a c b;
    Printf.printf "Move disk from pole %d to pole %d\n" a b;
    hanoi (pred n) c b a
  end

let () =
  hanoi 4 1 2 3
```


## Octave

```mw
function hanoimove(ndisks, from, to, via)
  if ( ndisks == 1 )
    printf("Move disk from pole %d to pole %d\n", from, to);
  else
    hanoimove(ndisks-1, from, via, to);
    hanoimove(1, from, to, via);
    hanoimove(ndisks-1, via, to, from);
  endif
endfunction

hanoimove(4, 1, 2, 3);
```


## Oforth

```mw
: move(n, from, to, via)
   n 0 > ifTrue: [
      move(n 1-, from, via, to)
      System.Out "Move disk from " << from << " to " << to << cr
      move(n 1-, via, to, from)
      ] ;

5 $left $middle $right) move
```


## Oz

```mw
declare
  proc {TowersOfHanoi N From To Via}
     if N > 0 then
        {TowersOfHanoi N-1 From Via To}
        {System.showInfo "Move from "#From#" to "#To}
        {TowersOfHanoi N-1 Via To From}
     end
  end
in
  {TowersOfHanoi 4 left middle right}
```


## PARI/GP

Translation of

:

Python

```mw
\\ Towers of Hanoi
\\ 8/19/2016 aev
\\ Where: n - number of disks, sp - start pole, ep - end pole.
HanoiTowers(n,sp,ep)={
  if(n!=0, 
    HanoiTowers(n-1,sp,6-sp-ep);
    print("Move disk ", n, " from pole ", sp," to pole ", ep);
    HanoiTowers(n-1,6-sp-ep,ep); 
    );
}
\\ Testing n=3:
HanoiTowers(3,1,3);
```

**Output:**

```
> HanoiTower(3,1,3);
Move disk 1 from pole 1 to pole 3
Move disk 2 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 2
Move disk 3 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 1
Move disk 2 from pole 2 to pole 3
Move disk 1 from pole 1 to pole 3
```


## Pascal

Works with

:

Free Pascal

version 2.0.4

I think it is standard pascal, except for the constant array "strPole". I am not sure if constant arrays are part of the standard. However, as far as I know, they are a "de facto" standard in every compiler.

```mw
program Hanoi;
type
  TPole = (tpLeft, tpCenter, tpRight);
const
  strPole:array[TPole] of string[6]=('left','center','right');

 procedure MoveStack (const Ndisks : integer; const Origin,Destination,Auxiliary:TPole);
 begin
  if Ndisks >0 then begin
     MoveStack(Ndisks - 1, Origin,Auxiliary, Destination );
     Writeln('Move disk ',Ndisks ,' from ',strPole[Origin],' to ',strPole[Destination]);
     MoveStack(Ndisks - 1, Auxiliary, Destination, origin);
  end;
 end;

begin
 MoveStack(4,tpLeft,tpCenter,tpRight);
end.
```

A little longer, but clearer for my taste

```mw
program Hanoi;
type
  TPole = (tpLeft, tpCenter, tpRight);
const
  strPole:array[TPole] of string[6]=('left','center','right');

 procedure MoveOneDisk(const DiskNum:integer; const Origin,Destination:TPole);
 begin
  Writeln('Move disk ',DiskNum,' from ',strPole[Origin],' to ',strPole[Destination]);
 end;

 procedure MoveStack (const Ndisks : integer; const Origin,Destination,Auxiliary:TPole);
 begin
  if Ndisks =1 then
       MoveOneDisk(1,origin,Destination)
  else begin
       MoveStack(Ndisks - 1, Origin,Auxiliary, Destination );
       MoveOneDisk(Ndisks,origin,Destination);
       MoveStack(Ndisks - 1, Auxiliary, Destination, origin);
  end;
 end;

begin
 MoveStack(4,tpLeft,tpCenter,tpRight);
end.
```


## PascalABC.NET

```mw

## procedure Hanoi(n,rfrom,rto,rwork: integer);
begin
  if n = 0 then
    exit;
  Hanoi(n-1,rfrom,rwork,rto);
  Print($'{rfrom}→{rto} ');
  Hanoi(n-1,rwork,rto,rfrom);
end;
Hanoi(5,1,3,2);
```

**Output:**

```
1→3  1→2  3→2  1→3  2→1  2→3  1→3  1→2  3→2  3→1  2→1  3→2  1→3  1→2  3→2  1→3  2→1  2→3  1→3  2→1  3→2  3→1  2→1  2→3  1→3  1→2  3→2  1→3  2→1  2→3  1→3  
```


## Perl

```mw
sub hanoi {
    my ($n, $from, $to, $via) = (@_, 1, 2, 3);

    if ($n == 1) {
        print "Move disk from pole $from to pole $to.\n";
    } else {
        hanoi($n - 1, $from, $via, $to);
        hanoi(1, $from, $to, $via);
        hanoi($n - 1, $via, $to, $from);
    };
};
```


## Phix

```
constant poles = {"left","middle","right"}
enum               left,  middle,  right
 
sequence disks
integer moves

procedure showpegs(integer src, integer dest)
    string desc = sprintf("%s to %s:",{poles[src],poles[dest]})
    disks[dest] &= disks[src][$]
    disks[src] = disks[src][1..$-1]
    for i=1 to length(disks) do
        printf(1,"%-16s | %s\n",{desc,join(sq_add(disks[i],'0'),' ')})
        desc = ""
    end for
    printf(1,"\n")
    moves += 1
end procedure
 
procedure hanoir(integer n, src=left, dest=right, via=middle)
    if n>0 then
        hanoir(n-1, src, via, dest)
        showpegs(src,dest)
        hanoir(n-1, via, dest, src)
    end if
end procedure
 
procedure hanoi(integer n)
    disks = {reverse(tagset(n)),{},{}}
    moves = 0
    hanoir(n)
    printf(1,"completed in %d moves\n",{moves})
end procedure
 
hanoi(3) -- (output of 4,5,6 also shown)
```

**Output:**

```
left to right:   | 3 2
                 |
                 | 1

left to middle:  | 3
                 | 2
                 | 1

right to middle: | 3
                 | 2 1
                 |

left to right:   |
                 | 2 1
                 | 3

middle to left:  | 1
                 | 2
                 | 3

middle to right: | 1
                 |
                 | 3 2

left to right:   |
                 |
                 | 3 2 1

completed in 7 moves
```

```
left to middle:  | 4 3 2
                 | 1
                 |

left to right:   | 4 3
                 | 1
                 | 2

middle to right: | 4 3
                 |
                 | 2 1

   ...

left to middle:  | 2
                 | 1
                 | 4 3

left to right:   |
                 | 1
                 | 4 3 2

middle to right: |
                 |
                 | 4 3 2 1

completed in 15 moves
```

```
left to right:   | 5 4 3 2
                 |
                 | 1

left to middle:  | 5 4 3
                 | 2
                 | 1

right to middle: | 5 4 3
                 | 2 1
                 |

    ...

middle to left:  | 1
                 | 2
                 | 5 4 3

middle to right: | 1
                 |
                 | 5 4 3 2

left to right:   |
                 |
                 | 5 4 3 2 1

completed in 31 moves
```

```
left to middle:  | 6 5 4 3 2
                 | 1
                 |

left to right:   | 6 5 4 3
                 | 1
                 | 2

middle to right: | 6 5 4 3
                 |
                 | 2 1

    ...

left to middle:  | 2
                 | 1
                 | 6 5 4 3

left to right:   |
                 | 1
                 | 6 5 4 3 2

middle to right: |
                 |
                 | 6 5 4 3 2 1

completed in 63 moves
```


## PHL

Translation of

:

C

```mw
module hanoi;

extern printf;

@Void move(@Integer n, @Integer from, @Integer to, @Integer via) [
	if (n > 0) {
		move(n - 1, from, via, to);
		printf("Move disk from pole %d to pole %d\n", from, to);
		move(n - 1, via, to, from);
	}
]

@Integer main [
	move(4, 1,2,3);
	return 0;
]
```


## PHP

Translation of

:

Java

```mw
function move($n,$from,$to,$via) {
    if ($n === 1) {
        print("Move disk from pole $from to pole $to");
    } else {
        move($n-1,$from,$via,$to);
        move(1,$from,$to,$via);
        move($n-1,$via,$to,$from);
    }
}
```
